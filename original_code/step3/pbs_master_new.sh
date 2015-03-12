#!/bin/tcsh
#PBS -t 1-300
#PBS -N filter_CAT1 
#PBS -l walltime=24:00:00

module load python/2.7.2
module load blast/ncbi-2.2.26+
cd $PBS_O_WORKDIR
python newFilter.py $filename.`printf %03d ${PBS_ARRAYID}` CAT1 $filename.xml.`printf %03d ${PBS_ARRAYID}` $filename.nc.`printf %03d ${PBS_ARRAYID}` $filename.c.`printf %03d ${PBS_ARRAYID}`
