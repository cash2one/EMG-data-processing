#!/bin/bash

source ../conf/conf.sh

python train.py \
	${train_data_file_name} \
	${model_file_name} \
	${feature_size} ${label_size} ${hidden_layers} \
	${train_test_ratio} \
	> ../log/train.log 2>&1

python skywalker.py \
	${model_file_name} \
	${test_data_file_name} \
	${feature_size} ${label_size} ${hidden_layers} \
	> ../results/${contrast_result_file_name} \
	2> ../log/skywalker.log
