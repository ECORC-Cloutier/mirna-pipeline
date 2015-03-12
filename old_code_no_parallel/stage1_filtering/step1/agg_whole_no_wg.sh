#!/bin/bash

if [ ! -d save_fasta ]; then 
	mkdir save_fasta
fi

for src in *.fasta
do
	base=${src%%.*}
	mkdir ${base}
	cp $src ${base}/master.fasta
	cp aggregate_whole_no_wg.py ${base}
	cd ${base}
	python aggregate_whole_no_wg.py &
	cd ..
	mv $src save_fasta
done
wait

