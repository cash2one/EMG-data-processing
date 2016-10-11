import sys
import numpy as np
from pykalman import KalmanFilter
from pykalman import UnscentedKalmanFilter



def kalman_filter(seq):
    def f(state, noise):
        return state + np.sin(noise)
    def g(state, noise):
        return state + np.cos(noise)
    # kf = KalmanFilter(initial_state_mean=0, n_dim_obs=2)
    ukf = UnscentedKalmanFilter(f, g, 0.001)
    return ukf.smooth(seq)[0].T[0]
    

if __name__ == '__main__':

    NUM_OF_FEATURE   = int(sys.argv[1])
    # Get features data from stdin
    features = []
    for line in sys.stdin:
        data = map(int, line.strip().split('\t')[0:NUM_OF_FEATURE])
        features.append(data)
    features = np.array(features).T
    # Apply the kalman filter on each feature
    filtered_features = []
    for feature in features:
        filtered_feature = kalman_filter(feature)
        filtered_features.append(filtered_feature)
    filtered_features = np.array(filtered_features).T
    # Output
    # kalman_filter()
    for row in filtered_features:
        print '\t'.join(map(str, row))
    