import numpy as np
import tensorflow as tf
import model.dbn as dbn
import sys
import os

data_file_name   = sys.argv[1]
model_file_name  = sys.argv[2]
NUM_OF_FEATURE   = int(sys.argv[3])
NUM_OF_LABEL     = int(sys.argv[4])
HIDDEN_LAYERS    = map(int, sys.argv[5].strip().split(','))
TRAIN_TEST_RATIO = float(sys.argv[6])

layers = [NUM_OF_FEATURE] + HIDDEN_LAYERS + [NUM_OF_LABEL]

print 'The number of feature and label:\t%s, %s' % (NUM_OF_FEATURE, NUM_OF_LABEL)
print 'The layers of the network:\t%s' % (layers)

# Get the myo data and the label data from local file.
data_path  = '../data/'
model_path = '../model_file/'
res_path   = '../results/'
features = []
labels   = []
with open(data_path + data_file_name) as data_file:
    for line in data_file:
        # take the first NUM_OF_FEATURE values as the feature vector
        feature_vector = map(float, line.strip().split("\t")[0:NUM_OF_FEATURE])
        label_vector   = map(float, line.strip().split("\t")[NUM_OF_FEATURE:NUM_OF_FEATURE+NUM_OF_LABEL])
        features.append(feature_vector)
        labels.append(label_vector)
        
print 'The number of training data:\t%d' % len(features)
print 'A example of the feature data:\t%s' % features[0]
print 'A example of the label data:\t%s' % labels[0]

# Divide the raw data into the training part and testing part
start_test = end_train = int(float(len(features)) / float(TRAIN_TEST_RATIO + 1) * TRAIN_TEST_RATIO)
training_features = np.array(features[0:end_train])
training_labels   = np.array(labels[0:end_train])
testing_features  = np.array(features[start_test:len(features)])
testing_labels    = np.array(labels[start_test:len(labels)])

# Check path
if not os.path.exists(model_path):
    os.makedirs(model_path)
if not os.path.exists(res_path):
    os.makedirs(res_path)

# Training
# _, input_size  = training_features.shape
# _, output_size = training_labels.shape
network = dbn.DBN(layers=layers, iters=50, batch_size=500, mu=.0005)
with tf.Session() as sess:
    tr, test = network.train(sess, training_features, training_labels, testing_features, testing_labels)
    np.savetxt(res_path + 'training_result.txt', tr)
    np.savetxt(res_path + 'testing_result.txt', test)

    tf_saver = tf.train.Saver()
    tf_saver.save(sess, model_path + model_file_name)
