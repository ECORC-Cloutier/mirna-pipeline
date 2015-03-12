# assumes all CSV files are in same directory 
#!/bin/tcsh
#PBS -N crush 
#PBS -l walltime=6:00:00
#PBS -l mem=4g

module load python/2.7.2
cd $PBS_O_WORKDIR
python csv_split.py 500000 ${filename}

