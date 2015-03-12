#!/bin/bash

source main.sh

export -f find_mature_novel

parallel find_mature_novel {} ::: *.cons_master  #change wildcard if necessary
