import sys
import socket
import arrow

UDP_IP = sys.argv[1]
SENDER_UDP_PORT = sys.argv[2]
content = sys.argv[3]

print "udp ip addr:\t %s" % UDP_IP
print "udp port:\t %s" % SENDER_UDP_PORT
print "udp content:\t %s" % content

def main():
    # Setup udp sockets.
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.sendto(bytearray(content), (UDP_IP, int(SENDER_UDP_PORT)))

if __name__ == "__main__":
    main()
