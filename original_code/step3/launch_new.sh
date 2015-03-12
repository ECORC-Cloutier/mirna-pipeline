
#!/bin/bash

for src in *DAT* 
    do
    #base=${src%%.*}
    cp ~mdomarat/wheat/safe/CAT1.* ~mdomarat/wheat/safe/pbs_master_new.sh ~mdomarat/wheat/safe/newFilter.py ${src}
    cd ${src}
    qsub -v filename=${src}_uniq.fasta pbs_master_new.sh 
    cd ..
    done
