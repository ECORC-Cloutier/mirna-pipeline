#!/bin/bash

for next in *L001_R1_001*  #change wildcard if necessary
do
    cp splitFasta.py ${next}
    cd ${next}
    python splitFasta.py 300 ${next}_uniq.fasta &
    cd ..
done
wait
