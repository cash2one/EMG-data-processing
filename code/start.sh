python train.py \
	without_thumb_middle.txt \
	model_para.ckpt \
	16 3 20,20 \
	9 \
	> ../log/train.log 2>&1

python skywalker.py \
	model_para.ckpt \
	last_5000_without_thumb_middle.txt \
	16 3 20,20 \
	> ../results/contrast_result.txt \
	2> ../log/skywalker.log
