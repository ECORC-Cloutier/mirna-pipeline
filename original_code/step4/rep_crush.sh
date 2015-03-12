#!/bin/bash

module load python/2.7.2
for next in *DAT* 
do
    cp ~mdomarat/wheat/safe/crush_qs.sh ~mdomarat/wheat/safe/crush.py ${next}
    cd ${next}
    qsub -v filename=${next} crush_qs.sh 
    cd ..
done
