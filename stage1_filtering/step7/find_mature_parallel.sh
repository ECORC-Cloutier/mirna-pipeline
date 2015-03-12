#!/bin/bash

source main.sh

export -f find_mature

parallel find_mature {} ::: *.fasta  #change wildcard if necessary
