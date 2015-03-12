#!/bin/bash

source main.sh

if [ ! -d save_fasta ]; then 
	mkdir save_fasta
fi

export -f aggregate_fasta

parallel aggregate_fasta {} ::: *.fasta

