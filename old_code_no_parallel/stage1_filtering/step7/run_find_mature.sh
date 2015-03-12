#!/bin/bash

for file in *.fasta 
do
    base=${file%%.*}
    mkdir ${base}
    cp find_mature_0mm.py MPC* $file $base
    cd $base
    python find_mature_0mm.py $file MPC $file MPC.fa &
    cd ..
done
wait  
