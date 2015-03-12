#!/bin/bash

for src in *L001_R1_001* 
do
    cp CAT1.* newFilter.py run_filter_cat.sh ${src}	
    filename=${src}_uniq.fasta
    cd ${src}
    bash run_filter_cat.sh $filename &
    cd ..
done
wait
