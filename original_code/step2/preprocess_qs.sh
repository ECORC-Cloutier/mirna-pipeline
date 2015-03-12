#!/bin/tcsh
#PBS -N preprocess 
#PBS -l walltime=6:00:00
#PBS -l mem=4g

module load python/2.7.2
cd $PBS_O_WORKDIR
python splitFasta.py 1000 $filename 
