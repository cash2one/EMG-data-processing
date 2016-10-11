# Plot the raw data
# cat ../data/last_5000_without_thumb_middle.txt | python ../code/plot/plot_raw_data.py raw_data 16 3

# Kalman filter test
cat ../data/without_thumb_middle.txt | python ../code/utils/kalman_filter.py 16 > ../results/filtered_raw_data.txt
# cat ../results/filtered_raw_data.txt | python ../code/plot/plot_raw_data.py filtered_data 16 0