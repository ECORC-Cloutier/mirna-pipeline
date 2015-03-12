#!/bin/bash

source main.sh

export -f align_groups

parallel align_groups {} ::: group*  #change wildcard if necessary
