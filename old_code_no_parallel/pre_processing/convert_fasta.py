from Bio import SeqIO
import os
import os.path
import glob
import shutil

path_name = os.getcwd() + "/FASTA"		#if using Windows, change to "\FASTA"
if not os.path.exists(path_name):		#creates sub-directory within the directory containing FASTQ files to store FASTA files
	os.mkdir(path_name, 0755)

for file in glob.glob("*.fastq"):		#finds all files with .fastq extension
	base = os.path.splitext(file)[0]	#gets file root	
	new_name = base + ".fasta"
	SeqIO.convert(file, "fastq", new_name, "fasta")
	shutil.move(new_name, path_name)	#moves new file to destination
