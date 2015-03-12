#!/bin/bash

source main.sh

export -f master_fasta

parallel master_fasta {} ::: *cons  #change wildcard if necessary
