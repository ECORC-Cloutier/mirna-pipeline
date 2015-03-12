from Bio.Blast import NCBIXML
from Bio import SeqIO
from Bio.Blast.Applications import NcbiblastnCommandline
import os
import sys

# version: jun 27.
# notes: short circuit through alignments / hsps via method. 
# wordsize is present ... number of alignments is not. 
# w 
def find_in_alignments (alignments):
  for a in alignments:
     for x in a.hsps:
       query_name = rec.query ## query name - from wheat
       match = x.match
       query = str(record_index[rec.query].seq)  
       has_match = match.find('|'*17)
       if (has_match >= 0):
  	    return True	
  return False
  

success= False
e_val = 10
name = sys.argv[1] 
db_name = sys.argv[2]
haveXML = False 
out_file_name =  sys.argv[3]
not_contam = sys.argv[4]
contam = sys.argv[5]
if not haveXML:
  #blastn_cline = NcbiblastnCommandline(query=name, db=db_name, evalue=e_val,outfmt=5, out=out_file_name) 
  blastn_cline = NcbiblastnCommandline(word_size=17, query=name, db=db_name, evalue=e_val,outfmt=5, out=out_file_name) 
  stdout, stderr = blastn_cline()
try:
  handle = open (out_file_name)  
  success = True
except IOError:
  pass

if success:
  not_contams = [] 
  contams = [] 
  records  = NCBIXML.parse (  handle )
  record_index = SeqIO.index(name, "fasta")
  for rec in records:
    if (len(rec.alignments)==0):
       not_contams.append(rec.query)
    else:
      found = find_in_alignments( rec.alignments)
      if not found:
        not_contams.append(rec.query)
      else:
        contams.append(rec.query)
  records = (record_index[id] for id in not_contams) 
  SeqIO.write(records, not_contam, "fasta") 
  records = (record_index[id] for id in contams) 
  SeqIO.write(records, contam, "fasta") 
