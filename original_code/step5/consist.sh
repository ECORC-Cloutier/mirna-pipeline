#!/bin/tcsh
#PBS -N consistent_naming 
#PBS -l walltime=6:00:00

module load python/2.7.2
cd $PBS_O_WORKDIR
cp ../../*.pickle* .
python consist_new.py $csv $fasta
cp *.pickle ../../
