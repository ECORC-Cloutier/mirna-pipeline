#!/bin/bash

source main.sh

export -f replicate_crush

parallel replicate_crush {} ::: *L001_R1_001*  #change wildcard if necessary
