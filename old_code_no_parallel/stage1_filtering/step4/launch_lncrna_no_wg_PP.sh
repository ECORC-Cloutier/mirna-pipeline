#!/bin/bash

for src in *L001_R1_001* 
do
    cp LNCRNA.* newFilter.py run_filter_lncrna.sh ${src}	
    filename=${src}_uniq.fasta
    cd ${src}
    bash run_filter_lncrna.sh $filename &
    cd ..
done
wait
