#!/bin/bash

for file in *.cons 
do
    python make_master.py $file &
done
wait 

