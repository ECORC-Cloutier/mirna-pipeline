
from Bio import SeqIO
import sys

input_file_name = sys.argv[1] 
cat1_file_name = input_file_name + '.cat1'
ncat1_file_name = input_file_name + '.no_cat1'
 
## lncRNA

#cat1 = set('Gene-_snRNA','Gene-_antisense-', 'Gene-_snRNA-', 'Gene-_sRNA-', 'Gene-_rRNA-', 'Gene-_ribozyme-')
input_seq_iterator = SeqIO.parse(open(input_file_name, "rU"), "fasta")
cat1_filter_iterator = (record for record in input_seq_iterator if record.id.split('_')[1]=='Gene-' and len(record.id.split('_'))>3 )
input_seq_iterator = SeqIO.parse(open(input_file_name, "rU"), "fasta")
not_cat1_filter_iterator = (record for record in input_seq_iterator if not(record.id.split('_')[1]=='Gene-' and len(record.id.split('_'))>3 ))
 
output_handle = open(cat1_file_name, "w")
SeqIO.write(cat1_filter_iterator, output_handle, "fasta")
output_handle.close()
 
another_output_handle = open(ncat1_file_name, "w")
SeqIO.write(not_cat1_filter_iterator, another_output_handle, "fasta")
another_output_handle.close()
