#!/bin/bash

filename=$1
for file in *fasta.ncg.???			
do
    num=${file##*.}
    python newFilter.py $filename.ncg.$num LNCRNA $filename.xml.$num $filename.ncgl.$num $filename.lncrna.$num
done
