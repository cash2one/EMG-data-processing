from matplotlib import pyplot as plt
import numpy as np
import sys

# Get data from stdin
contrasts = []
for line in sys.stdin:
    data = line.strip().split('#')
    test_output = map(float, data[0].split('\t'))
    real_output = map(float, data[1].split('\t'))
    contrasts.append(zip(test_output, real_output))

# Re-organize the contrasts data
reorg_contrasts = []
num_contrasts = len(contrasts[0])
for i in range(num_contrasts):
    test = []
    real = []
    for c in contrasts:
        test.append(c[i][0])
        real.append(c[i][1])
    reorg_contrasts.append([test, real])

# Plot the contrasts
x = range(len(contrasts))
i = 0
for con in reorg_contrasts:
    plt.figure(figsize=(50,8))
    with plt.style.context('fivethirtyeight'):
        plt.plot(x, con[0])
        plt.plot(x, con[1])
    plt.savefig('../results/plot/contrast' + str(i))
    i += 1
