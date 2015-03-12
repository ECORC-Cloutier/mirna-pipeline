#!/bin/bash

source main.sh

export -f csv_split

parallel csv_split {} ::: *.cons
