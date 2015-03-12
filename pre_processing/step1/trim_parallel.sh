#!/bin/bash

source main.sh

export -f trim

parallel trim {} ::: *001.txt ::: TGGAATTCTCGGGTGCCAAGGC #change wildcard to something specific as ".txt" may conflict with future .txt files and also change the adaptor sequence if necessary
