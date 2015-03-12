#!/bin/bash

for file in *_trimmed.txt
do
    base=${file%%.*}
    perl qseq2fastq.pl < $file > ${base}.fastq &
done
wait
