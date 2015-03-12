
from Bio import SeqIO
import sys
import math


if ( len(sys.argv) < 3):
  print 'usage: python splitFasta.py <numParts> <fileName>'
  sys.exit()

num_parts = int(sys.argv[1])
num_digits = int(math.floor(math.log10(num_parts))) + 1
file_name = sys.argv[2]
record_index = SeqIO.index(file_name,'fasta')
ids =  [ rec.id for rec in SeqIO.parse(file_name,'fasta')]
num_ids = len(ids)
chunk_length = num_ids/num_parts
for i in range ( 1, num_parts  ):
    len_i = int(math.floor(math.log10(i)))+1
    full_string = '0'*(num_digits-len_i) + str(i)
    records = (record_index[id] for id in ids[(i-1)*chunk_length:i*chunk_length])
    SeqIO.write(records, file_name+'.'+full_string, 'fasta')
records = (record_index[id] for id in ids[(num_parts-1)*chunk_length:])
SeqIO.write(records, file_name+'.'+str(num_parts), 'fasta')
