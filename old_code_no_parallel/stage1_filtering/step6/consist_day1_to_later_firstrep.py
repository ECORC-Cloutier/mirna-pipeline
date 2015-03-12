import cPickle
import sys

csv = sys.argv[1]
fasta = sys.argv[2]
num = sys.argv[3]
fasta_write = open ( fasta , 'w')
csv_read = open  ( csv, 'r')
rind = csv.rindex('.')
base = csv[0:rind]
csv_write = open ( base+'.cons','w')
seq_num = 0
csv_write.write('seq#,distinct read,seq,read count,normalized read count (RPM)\n')
old = dict()
lines = csv_read.readlines()
for line in lines[1:]:
  info = line.split(',')
  seq = info[2]
  ind = info[1].index('_')
  rest = info[1][ind:]
  if seq in old:
    seq_num = old[seq]
  else:
    seq_num = len(old)+1
    old[seq] = seq_num
    fasta_write.write('>species'+str(seq_num)+rest+'\n'+seq+'\n')

  to_write = '>species'+str(seq_num)+rest
  csv_write.write( info[0] + ',' + to_write + ',' + info[2] + ',' + info[3] + ',' + info[4])

#csv_write.write ( lines[-1] )

pick = open ('day'+ num +'.pickle','w') #replace NUMBER with day number
cPickle.dump ( old, pick)
pick.close()

csv_write.close()
csv_read.close()
fasta_write.close()
