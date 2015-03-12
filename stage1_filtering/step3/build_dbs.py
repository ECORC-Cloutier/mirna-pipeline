
from Bio import SeqIO
import sys

input_file_name = sys.argv[1] 
lnc_file_name = input_file_name + '.lncrna'
nlnc_file_name = input_file_name + '.no_lncrna'
 
## lncRNA

input_seq_iterator = SeqIO.parse(open(input_file_name, "rU"), "fasta")
lnc_filter_iterator = (record for record in input_seq_iterator if str(record.id).find('lncRNA') >= 0 )
input_seq_iterator = SeqIO.parse(open(input_file_name, "rU"), "fasta")
not_filter_iterator = (record for record in input_seq_iterator if (not str(record.id).find('lncRNA') >= 0) )
 
output_handle = open(lnc_file_name, "w")
SeqIO.write(lnc_filter_iterator, output_handle, "fasta")
output_handle.close()
 
another_output_handle = open(nlnc_file_name, "w")
SeqIO.write(not_filter_iterator, another_output_handle, "fasta")
another_output_handle.close()

