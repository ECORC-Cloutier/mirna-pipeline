import sys

csv = sys.argv[1]
rind = csv.index('.')
base = csv[0:rind]

csv_read = open(csv, "r")
lines = csv_read.readlines()
csv_read.close()

fasta_write = open(base+"_cons_master.fasta", "w")

for line in lines[1:]:
    info = line.split(",")
    seq_id = info[1]
    seq = info[2]
    fasta_write.write(seq_id+"\n"+seq+"\n") 

fasta_write.close()

