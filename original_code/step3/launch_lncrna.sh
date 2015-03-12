
#!/bin/bash

for src in *DAT* 
    do
    #base=${src%%.*}
    cp ~mdomarat/wheat/safe/LNCRNA.* ~mdomarat/wheat/safe/pbs_master_lncrna.sh  ${src}
    cd ${src}
    qsub -v filename=${src}_uniq.fasta pbs_master_lncrna.sh 
    cd ..
    done
