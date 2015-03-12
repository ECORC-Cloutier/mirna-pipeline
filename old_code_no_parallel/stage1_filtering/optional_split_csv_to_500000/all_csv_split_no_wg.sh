#assumes all csv files are in the same directory.
#!/bin/bash

for next in *.cons 
do
    filename=${next}
    python csv_split.py 500000 ${filename} &
done
wait
