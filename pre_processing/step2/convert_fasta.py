from Bio import SeqIO
import sys

name = sys.argv[1]
SeqIO.convert(name+".fastq", "fastq", name+".fasta", "fasta")

