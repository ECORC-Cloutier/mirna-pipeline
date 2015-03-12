#!/bin/bash

for next in *L001_R1_001* 
do
    cp crush_gene.py ${next}
    cd ${next}
    python crush_gene.py ${next}_summary.csv ${next}_uniq.fasta.gene &
    cd ..
done
wait
