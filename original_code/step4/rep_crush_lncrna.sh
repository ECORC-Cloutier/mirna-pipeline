#!/bin/bash

module load python/2.7.2
for next in *DAT* 
do
    cp ~mdomarat/wheat/safe/crush_qs_lncrna.sh ~mdomarat/wheat/safe/crush_lncrna.py ${next}
    cd ${next}
    qsub -v filename=${next} crush_qs_lncrna.sh 
    cd ..
done
