#!/bin/bash

source main.sh

export -f convert_fasta

parallel convert_fasta {} ::: *.fastq
