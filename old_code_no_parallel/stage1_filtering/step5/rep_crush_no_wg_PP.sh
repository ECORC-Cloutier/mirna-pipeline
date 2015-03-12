#!/bin/bash

for next in *L001_R1_001* #change wildcard if necessary
do
	cp crush.py ${next}
	cd ${next}
	python crush.py ${next}_summary.csv ${next}_uniq.fasta.ncglch &
    cd ..
done
wait
