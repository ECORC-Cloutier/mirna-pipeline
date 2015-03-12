#!/bin/bash

for next in *L001_R1_001* 
do
	cp crush_generic.py ${next}
	cd ${next}
	python crush_generic.py ${next}_summary.csv ${next}_uniq.fasta.ncgl 
    cd ..
done
