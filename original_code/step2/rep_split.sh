#!/bin/bash

module load python/2.7.2
lastrun='' 
for next in *DAT* 
do
    cp ~mdomarat/wheat/safe/preprocess_qs.sh ~mdomarat/wheat/safe/splitFasta.py ${next}
    cd ${next}
    qsub -v filename=${next}_uniq.fasta preprocess_qs.sh 
    cd ..
done
