#!/bin/bash

names=()

for file in *cons*
do
    names+=($file)
done

for (( i=0; i<${#names[@]}; i++ ))
do
    if [ $i != $(( ${#names[@]} -1 )) ] 
    then
        echo \'${names[$i]}\', >> namelist.txt
    else
        echo \'${names[$i]}\' >> namelist.txt
    fi
done

