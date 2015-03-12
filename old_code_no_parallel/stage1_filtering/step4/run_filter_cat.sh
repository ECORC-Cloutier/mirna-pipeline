#!/bin/bash

filename=$1
for file in *fasta.???			
do
    num=${file##*.}
    python newFilter.py $filename.$num CAT1 $filename.xml.$num $filename.nc.$num $filename.c.$num
done
