import sys
import numpy as np
import model.dbn as dbn
import tensorflow as tf
from matplotlib import pyplot as plt

model_file_name  = sys.argv[1]
data_file_name   = sys.argv[2]
NUM_OF_FEATURE   = int(sys.argv[3])
NUM_OF_LABEL     = int(sys.argv[4])
HIDDEN_LAYERS    = map(int, sys.argv[5].strip().split(','))

layers = [NUM_OF_FEATURE] + HIDDEN_LAYERS + [NUM_OF_LABEL]

# print 'The layers of the network:\t%s' % (layers)

data_path       = '../data/'
model_file_path = '../model_file/'

def get_test_data(data_file_name):
    features = []
    labels   = []
    # Open the data file and get test data
    with open(data_path + data_file_name) as data_file:
        for line in data_file:
            feature_vector = map(float, line.strip().split("\t")[0:NUM_OF_FEATURE])
            label_vector   = map(float, line.strip().split("\t")[NUM_OF_FEATURE:NUM_OF_FEATURE+NUM_OF_LABEL])
            features.append(feature_vector)
            labels.append(label_vector)
    
    testing_features = np.array(features)
    testing_labels   = np.array(labels)
    
    return testing_features, testing_labels

def test_main(testing_features):
    # Restore the well-trained model
    network = dbn.DBN(layers=layers, batch_size=1)

    with tf.Session() as sess:
        tf_saver = tf.train.Saver()
        tf_saver.restore(sess, model_file_path + model_file_name)
    
        # Get the ouput from test data
        # for i in testing_features:
        #     outputs = network.get_output(sess, [i])[0]
        #     print outputs
        outputs = network.get_output(sess, testing_features)
    return outputs

def output_contrasts(testing_outputs, real_outputs):
    for t,r in zip(testing_outputs, real_outputs):
        print '%s#%s' % ('\t'.join(map(str, t)), '\t'.join(map(str, r)))

if __name__ == '__main__':
    testing_inputs, real_outputs = get_test_data(data_file_name)
    testing_outputs = test_main(testing_inputs)
    output_contrasts(testing_outputs, real_outputs)
