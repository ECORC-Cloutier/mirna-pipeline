#!/bin/bash

for src in *L001_R1_001* 
do
    cp GENE.* newFilter.py run_filter_gene.sh ${src}	
    filename=${src}_uniq.fasta
    cd ${src}
    bash run_filter_gene.sh $filename &
    cd ..
done
wait
