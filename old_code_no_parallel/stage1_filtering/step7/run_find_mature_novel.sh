#!/bin/bash

for file in *cons_master 
do
    cp find_mature_1_4mm.py $file
    cd $file
    name=${file}.fasta_1_4mm.fa
    python find_mature_1_4mm.py $name MPC $name MPC.fa &
    cd ..
done
wait  
