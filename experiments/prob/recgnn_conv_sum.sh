cd src
python main.py prob --exp_id recgnn_convsum --data_dir ../data/benchmarks/merged/ --num_rounds 10 --dataset benchmarks --gpus 0 --gate_types INPUT,AND,NOT --dim_node_feature 3 --no_node_cop --aggr_function conv_sum --wx_update
