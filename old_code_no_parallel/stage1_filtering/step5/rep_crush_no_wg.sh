#!/bin/bash

for next in *L001_R1_001* 
do
	cp crush.py ${next}
	cd ${next}
	python crush.py ${next}_summary.csv ${next}_uniq.fasta.ncglch 
    cd ..
done
