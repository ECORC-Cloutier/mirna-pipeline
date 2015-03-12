from Bio import SeqIO
import cPickle
import sys
import math



csv = sys.argv[1]
fasta = sys.argv[2]

csv_read = open  ( csv, 'r')
map = dict()
lines = csv_read.readlines()
for line in lines:
  ind = line.split(',')[1][1:]
  map[ind] = line
csv_read.close()

rind = csv.rindex('.')
base = csv[0:rind]
csv_write = open ( base+'.chloro.csv','w') #change to appropriate database name
csv_write.write('seq#,distinct read,seq,read count,normalized read count (RPM)\n')

all = [] # Setup an empty list
for i in range(1,301):
  len_i = int(math.floor(math.log10(i)))+1
  full_string = '0'*(3-len_i) + str(i)
  handle = open ( fasta +'.' + full_string, 'rU')
  for record in SeqIO.parse(handle, "fasta"):
     all.append(record)
     if record.id in map:
       csv_write.write(str(map[record.id]))

fasta_write = open ( fasta + '.all' , 'w')
SeqIO.write(all, fasta_write, "fasta")
csv_write.close()
fasta_write.close()
