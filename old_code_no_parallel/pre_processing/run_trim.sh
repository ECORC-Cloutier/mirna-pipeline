#!/bin/bash

for file in *001.txt #change wildcard to something specific as ".txt" may conflict with report.txt files
do
    base=${file%%.*}
    perl adapter_trim.pl -a TGGAATTCTCGGGTGCCAAGGC -r ${base}_report.txt < $file > ${base}_trimmed.txt &  #adapter sequence at -a
done
wait
