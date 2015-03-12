#!/bin/bash

source main.sh

export -f replicate_cat replicate_gene replicate_lncrna replicate_chloro

parallel replicate_cat {} ::: *L001_R1_001*  #change wildcard if necessary

parallel replicate_gene {} ::: *L001_R1_001*  #change wildcard if necessary

parallel replicate_lncrna {} ::: *L001_R1_001*  #change wildcard if necessary

parallel replicate_chloro {} ::: *L001_R1_001*  #change wildcard if necessary
