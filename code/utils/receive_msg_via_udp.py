import socket
import select

port_ch1 = 30326
port_ch2 = 30325
ip = "0.0.0.0"

# socket channel 1 for upper Myoband (black) & glove
sock_ch1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_ch1.bind((ip, port_ch1))
# socket channel 2 for lower Myoband (white)
sock_ch2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_ch2.bind((ip, port_ch2))

sockets = [sock_ch1, sock_ch2]

empty = []
upper_myo_glove_data = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
lower_myo_data = ['0', '0', '0', '0', '0', '0', '0', '0']
while True:
    readable, writable, exceptional = select.select(sockets, empty, empty)
    for s in readable:
        (raw_data, client_address) = s.recvfrom(1024)
        if s == sock_ch1:
            upper_myo_glove_data = raw_data.strip().split(" ")
        elif s == sock_ch2:
            lower_myo_data = raw_data.strip().split(" ")
    output_data = lower_myo_data + upper_myo_glove_data        
    print "\t".join(output_data)

for s in sockets:
    s.close()
