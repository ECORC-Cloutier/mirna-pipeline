
#!/bin/bash

for src in *DAT* 
    do
    #base=${src%%.*}
    cp ~mdomarat/wheat/safe/GENE.* ~mdomarat/wheat/safe/pbs_master_gene.sh  ${src}
    cd ${src}
    qsub -v filename=${src}_uniq.fasta pbs_master_gene.sh 
    cd ..
    done
