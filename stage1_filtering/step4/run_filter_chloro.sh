#!/bin/bash

filename=$1
for file in *fasta.ncgl.???			
do
    num=${file##*.}
    python newFilter.py $filename.ncgl.$num CHLORO $filename.xml.$num $filename.ncglch.$num $filename.chloro.$num
done
