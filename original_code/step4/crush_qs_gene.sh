#!/bin/tcsh
#PBS -N crush_GENE
#PBS -l walltime=6:00:00
#PBS -l mem=4g

module load python/2.7.2
cd $PBS_O_WORKDIR
python crush_gene.py ${filename}_summary.csv ${filename}_uniq.fasta.gene
