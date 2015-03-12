#!/bin/bash

for file in *.fastq
do
    base=${file%%.*}
    perl fastq2qseq.pl < $file > ${base}.txt &
done
wait
