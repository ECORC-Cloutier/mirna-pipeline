#!/bin/bash

source main.sh

export -f replicate_split

parallel replicate_split {} ::: *L001_R1_001*  #change wildcard if necessary
