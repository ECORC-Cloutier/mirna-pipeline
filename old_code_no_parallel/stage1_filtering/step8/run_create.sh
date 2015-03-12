#!bin/bash

for file in *cons
do
    base=${file%%.*}
    mkdir $base
    cp create_id_rpmlist.py $base
    file1=${base}.smaller.cons
    file2=${base}_cons_master.fasta_mature.csv
    file3=${base}_cons_master.fasta_1_4mm.fa_mature.csv
    mv $file $file1 $file2 $file3 $base
    cd $base
    python create_id_rpmlist.py $file1 $file2 0 &
    cd ..
done
wait

for file in *L001_R1*
do
    cd $file
    file1=${file}.smaller.cons
    file2=${file}_cons_master.fasta_1_4mm.fa_mature.csv
    python create_id_rpmlist.py $file1 $file2 1_4 &
    cd ..
done
wait    
