#!/bin/bash

for next in *L001_R1_001* 
do
    cp crush_lncrna.py ${next}
    cd ${next}
    python crush_lncrna.py ${next}_summary.csv ${next}_uniq.fasta.lncrna &
    cd ..
done
wait
