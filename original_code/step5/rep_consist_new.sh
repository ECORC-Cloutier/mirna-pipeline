#!/bin/bash

module load python/2.7.2
lastrun='' 
for next in *DAT* 
do
  echo $next
  cp ~/new/consist.sh ~/new/consist_new.py ${next}
  cd ${next}
  if [ -z "$lastrun" ] 
  then 
    lastrun=`qsub -v csv=${next}_summary.smaller.csv,fasta=${next}_uniq.fasta consist.sh`
  else
    lastrun=`qsub -W depend=afterok:$lastrun -v csv=${next}_summary.smaller.csv,fasta=${next}_uniq.fasta consist.sh`
  fi 
  echo $lastrun
  cd ..
done
