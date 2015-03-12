#assumes all csv files are in the same directory.
#!/bin/bash

module load python/2.7.2
cp ~mdomarat/wheat/safe/csv_split.sh ~mdomarat/wheat/safe/csv_split.py .
for next in *.cons 
do
    qsub -v filename=${next} csv_split.sh 
done
