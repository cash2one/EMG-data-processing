import numpy as np
import tensorflow as tf
import dbn
import sys
import os

file_name        = sys.argv[1]
NUM_OF_FEATURE   = int(sys.argv[2])
NUM_OF_LABEL     = int(sys.argv[3])
TRAIN_TEST_RATIO = float(sys.argv[4])

print 'The number of feature and label: %s, %s' % (NUM_OF_FEATURE, NUM_OF_LABEL)

# Get the myo data and the label data from local file.
data_path  = './'
model_path = './model/'
res_path   = './results/'
features = []
labels   = []
with open(data_path + file_name) as data_file:
    for line in data_file:
        # take the first NUM_OF_FEATURE values as the feature vector
        feature_vector = map(float, line.strip().split("\t")[0:NUM_OF_FEATURE])
        label_vector   = map(float, line.strip().split("\t")[NUM_OF_FEATURE:NUM_OF_FEATURE+NUM_OF_LABEL])
        features.append(feature_vector)
        labels.append(label_vector)
        
print 'The number of training data:\t%d' % len(features)
print 'A example the feature data:\t%s' % features[0]
print 'A example the label data:\t%s' % labels[0]

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
_, input_size  = training_features.shape
_, output_size = training_labels.shape
network = dbn.DBN(layers=[input_size, 20, 20, output_size], iters=20, batch_size=100, mu=.0005)
with tf.Session() as sess:
    tr, test = network.train(sess, training_features, training_labels, testing_features, testing_labels)
    np.savetxt(res_path + 'training_result.txt', tr)
    np.savetxt(res_path + 'testing_result.txt', test)

    tf_saver = tf.train.Saver()
    tf_saver.save(sess, model_path + 'model_para.ckpt')
