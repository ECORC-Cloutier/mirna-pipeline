#!/bin/bash

filename=$1
for file in *fasta.nc.???			
do
    num=${file##*.}
    python newFilter.py $filename.nc.$num GENE $filename.xml.$num $filename.ncg.$num $filename.gene.$num
done
