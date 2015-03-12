#!/bin/bash


module load python/2.7.2
mkdir save_fasta
for src in *.fasta
    do
    base=${src%%.*}
    mkdir ${base}
    cp $src ${base}/master.fasta
    cp ~mdomarat/wheat/safe/aggregate_whole.py ~mdomarat/wheat/safe/aggregate_whole.sh ${base}
    cd ${base}
    qsub aggregate_whole.sh 
    cd ..
    mv $src save_fasta
    done
