from matplotlib import pyplot as plt
import numpy as np
import sys

plot_file_name   = sys.argv[1]
NUM_OF_FEATURE   = int(sys.argv[2])
NUM_OF_LABEL     = int(sys.argv[3])

# Get data from stdin
raw_data = []
features = []
labels   = []
for line in sys.stdin:
    data = line.strip().split('\t')
    feature = data[0:NUM_OF_FEATURE]
    label   = data[NUM_OF_FEATURE:NUM_OF_FEATURE+NUM_OF_LABEL]
    features.append(feature)
    labels.append(label)

features = np.array(features).T
labels   = np.array(labels).T

# Plot the features
if NUM_OF_FEATURE > 0:
    i = 0
    axs = []
    f, axs = plt.subplots(NUM_OF_FEATURE, 1, figsize=(80, 80), sharex='col', sharey='row')
    for ax in axs:
        ax.plot(features[i])
        i += 1
    plt.savefig('../results/plot/' + plot_file_name + '_features')

# Plot the labels
if NUM_OF_LABEL > 0:
    i = 0
    axs = []
    f, axs = plt.subplots(NUM_OF_LABEL, 1, figsize=(80, 50), sharex='col', sharey='row')
    for ax in axs:
        ax.plot(labels[i])
        i += 1
    plt.savefig('../results/plot/' + plot_file_name + '_labels')
