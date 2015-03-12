#!/bin/bash

source main.sh

export -f fastq_qseq

parallel fastq_qseq {} ::: *.fastq  

