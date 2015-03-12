#!/bin/tcsh
#PBS -t 1-300
#PBS -N filter_LNCRNA
#PBS -l walltime=24:00:00

module load python/2.7.2
module load blast/ncbi-2.2.26+
cd $PBS_O_WORKDIR
python newFilter.py $filename.ncg.`printf %03d ${PBS_ARRAYID}` LNCRNA $filename.xml.`printf %03d ${PBS_ARRAYID}` $filename.ncgl.`printf %03d ${PBS_ARRAYID}` $filename.lncrna.`printf %03d ${PBS_ARRAYID}`
