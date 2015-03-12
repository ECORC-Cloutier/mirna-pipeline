from Bio import SeqIO
import sys

input_file_name = sys.argv[1] 
 

input_seq_iterator = SeqIO.parse(open(input_file_name, "rU"), "fasta")
gene_types = set(record.id.split('_')[2] for record in input_seq_iterator if len(record.id.split('_'))>3 and record.id.split('_')[1]=='Gene-' )
input_seq_iterator = SeqIO.parse(open(input_file_name, "rU"), "fasta")
types = set("-".join(record.id.split('_')[1:2]) for record in input_seq_iterator) 
print types
print gene_types

