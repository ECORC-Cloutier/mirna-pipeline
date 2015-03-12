#!/bin/bash

for src in *L001_R1_001* #change wildcard if necessary
do
    cp CAT1.* newFilter.py run_filter_cat.sh ${src}	
    filename=${src}_uniq.fasta
    cd ${src}
    bash run_filter_cat.sh $filename &
    cd ..
done
wait

for src in *L001_R1_001* #change wildcard if necessary
do
    cp GENE.* newFilter.py run_filter_gene.sh ${src}	
    filename=${src}_uniq.fasta
    cd ${src}
    bash run_filter_gene.sh $filename &
    cd ..
done
wait

for src in *L001_R1_001* #change wildcard if necessary
do
    cp LNCRNA.* newFilter.py run_filter_lncrna.sh ${src}	
    filename=${src}_uniq.fasta
    cd ${src}
    bash run_filter_lncrna.sh $filename &
    cd ..
done
wait

for src in *L001_R1_001* #change wildcard if necessary
do
    cp CHLORO.* newFilter.py run_filter_chloro.sh ${src}	
    filename=${src}_uniq.fasta
    cd ${src}
    bash run_filter_chloro.sh $filename &
    cd ..
done
wait
