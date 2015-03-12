#!/bin/bash

for next in *L001_R1_001* #change wildcard if necessary	 
do
    echo $next
    cd ${next}
    csv=${next}_summary.smaller.csv 
    fasta=${next}_uniq.fasta
    cp ../../day0.pickle . #if not starting on day0, change day0.pickle to the correct day
    cp ../consist_day0.py .
    python consist_day0.py $csv $fasta
    cp *.pickle ../../ 
    cd ..
done
