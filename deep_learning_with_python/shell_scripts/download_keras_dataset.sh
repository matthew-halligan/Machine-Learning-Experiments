#! /bin/bash

dataset=$1
dataset_url="https://storage.googleapis.com/tensorflow/tf-keras-datasets/"${dataset}".npz"
path_to_datasets="/home/tpcp/.keras/datasets"

echo $dataset_url

wget --no-check-certificate ${dataset_url} -P ${path_to_datasets}
