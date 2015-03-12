from Bio import SeqIO
import re
l = [ 'tae', 'ttu', 'ata', 'bdi', 'hvu', 'egu', 'far', 'osa', 'sbi', 'sof', 'ssp', 'zma', 'cca', 'han', 'har', 'hci', 'hex', 'hpa', 'hpe', 'htu', 'aly', 'ath', 'bna', 'bol', 'bra', 'cpa', 'cme', 'hbr', 'mes', 'rco', 'aau', 'ahy', 'amg', 'gma', 'gso', 'lja', 'mtr', 'pvu', 'vun', 'ama', 'dpr', 'rgl', 'ssl', 'lus', 'gar', 'ghb', 'ghr', 'gra', 'tcc', 'aqc', 'bcy', 'bgy', 'mdm', 'ppe', 'ccl', 'crt', 'csi', 'ctr', 'peu', 'ptc', 'nta', 'sly', 'stu', 'vvi', 'pgi', 'ppt', 'smo', 'cln', 'pab', 'pde', 'pta', 'cre' ];
#l = ['>'+x for x in l]

name = 'mature.fa'
record_index = SeqIO.index(name, "fasta")

plants_records = (record_index[id] for x in l for id in record_index if x in id)
#mirna_dict = dict()
#
#for id in plants_records:
#  seq = record_index[id].seq
#  if not (seq in mirna_dict):
#    mirna_dict[seq] = [id]
#  else:
#    mirna_dict[seq].append(id)
#
#for x in mirna_dict.keys():
#  if len(mirna_dict[x]) > 1:
#    print mirna_dict[x][0], x, mirna_dict[x], 

SeqIO.write(plants_records, 'MPC.fa', "fasta")

