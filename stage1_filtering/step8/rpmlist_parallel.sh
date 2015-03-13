#!/bin/bash

source main.sh

export -f create_rpm_0mm create_rpm_1_4mm

parallel create_rpm_0mm {} ::: *cons  #change wildcard if necessary

parallel create_rpm_1_4mm {} ::: *L001_R1_001*  #change wildcard if necessary
