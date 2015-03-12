#!/bin/bash

source main.sh

export -f qseq_fastq

parallel qseq_fastq {} ::: *_trimmed.txt

