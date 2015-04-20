#Author: Douglas Huang
#Modified: April 20, 2015
#Function: Prepares a .fasta file from DGE analysis output for submission to psRNATarget
#Instructions: Use the sequence log as the first command-line argument and the filtered file as the second. Change the write name if desired. By default, it will be the directory name.

import sys
import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord  

workdir = sys.argv[1] #filepath of replicate directory
ref_file = sys.argv[2] #get log of sequences
filtered_matrix_file = sys.argv[3] #get matrix file

os.chdir(workdir)
write_name = os.path.basename(os.getcwd()) #uses directory name as basename for output files; change if desired

read_ref = open(ref_file, "r")
read_matrix = open(filtered_matrix_file, "r")
write_fasta = open(write_name + ".fasta", "w")

matrix_species = []
fasta_seq = []

matrix_info = read_matrix.read().splitlines()
read_matrix.close()

for line in matrix_info[1:]:
	info = line.split(",")
	matrix_species.append(info[0])

sequence_list = read_ref.read().splitlines()
read_ref.close()

for line in sequence_list:
	info = line.split(",")
	species = info[0]
	#If the species exists in the filtered matrix, create a new SeqRecord object
	if str(species) in matrix_species:
		sequence = info[1]
		write_seq = SeqRecord(Seq(sequence))
		write_seq.id = species 
		write_seq.description = ""
		fasta_seq.append(write_seq)

SeqIO.write(fasta_seq, write_fasta, "fasta")

write_fasta.close()
