#!/bin/bash
num=1   #set day number
for next in *L001_R1_001* #change wildcard if necessary 	 
do
    echo $next
    cd ${next}
    csv=${next}_summary.smaller.csv 
    fasta=${next}_uniq.fasta
    cp ../../*.pickle* .
    cp ../consist_day1_to_later.py .
    python consist_day1_to_later.py $csv $fasta $num
    cp *.pickle ../../ 
    cd ..
done

