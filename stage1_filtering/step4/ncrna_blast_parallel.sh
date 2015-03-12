#!bin/bash

source main.sh
export -f launch_cat launch_gene launch_lncrna launch_chloro

echo Start time: `date`
echo Starting CAT1 BLAST...
parallel launch_cat {} ::: *L001_R1_001*  #change wildcard if necessary
echo Finished CAT1 at `date`. Starting GENE BLAST...

parallel launch_gene {} ::: *L001_R1_001*  #change wildcard if necessary
echo Finished GENE at `date`. Starting LNCRNA BLAST...

parallel launch_lncrna {} ::: *L001_R1_001*  #change wildcard if necessary
echo Finished LNCRNA at `date`. Starting CHLORO BLAST...

parallel launch_chloro {} ::: *L001_R1_001*  #change wildcard if necessary
echo All BLASTs completed a `date`.



