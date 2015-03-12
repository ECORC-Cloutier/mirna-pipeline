#!/bin/bash

for src in *L001_R1_001* 
do
    cp CHLORO.* newFilter.py run_filter_chloro.sh ${src}	
    filename=${src}_uniq.fasta
    cd ${src}
    bash run_filter_chloro.sh $filename &
    cd ..
done
wait
