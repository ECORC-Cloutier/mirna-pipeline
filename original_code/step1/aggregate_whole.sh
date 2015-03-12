#!/bin/tcsh
#PBS -N aggregate 
#PBS -l walltime=6:00:00

module load python/2.7.2
cd $PBS_O_WORKDIR
python aggregate_whole.py 
