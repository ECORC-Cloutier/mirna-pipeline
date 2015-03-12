import cPickle
import sys

days = [0,1,2,3,7,10]
day = 2
csv = sys.argv[1]
fasta = sys.argv[2]

csv_read = open  (csv, 'r')
rind = csv.rindex('.')
base = csv[0:rind]
csv_write = open ( base+'.cons','w')
fasta_write = open ( fasta , 'w')
csv_write.write('seq#,distinct read,seq,read count,normalized read count (RPM)\n')

count = 0
new_found = []
if day > 0:
  lines = csv_read.readlines()
  pick = open ('day0.pickle','r')
  old = cPickle.load( pick)
  count += len(old)
  pick.close()
  for line in lines[1:]:
    info = line.split(',')
    seq = info[2]
    ind = info[1].index('_')
    rest = info[1][ind:]
    if seq in old:
      seq_num = old[seq]
      to_write = '>species'+str(seq_num)+rest
      csv_write.write( info[0] + ',' + to_write + ',' + info[2] + ',' + info[3] + ',' + info[4])
    else:
      new_found.append(info)
  day_index = 1
  while (days[day_index] <= day):
    pick = open ('day'+str(days[day_index])+'.pickle','r')
    old = cPickle.load(pick)
    pick.close()
    count += len(old)
    for info in new_found[:]: 
      seq = info[2]
      ind = info[1].index('_')
      rest = info[1][ind:]
      if seq in old:
        seq_num = old[seq]
        new_found.remove(info)
        to_write = '>species'+str(seq_num)+rest
        csv_write.write( info[0] + ',' + to_write + ',' + info[2] + ',' + info[3] + ',' + info[4])
    day_index+=1
  
  pick = open ('day'+str(day)+'.pickle','r')
  current = cPickle.load(pick)
  pick.close()
  seq_num = count + 1
  for info in new_found[:]:
    seq = info[2]
  	ind = info[1].index('_')
  	rest = info[1][ind:]
  	current[seq] = seq_num
  	fasta_write.write('>species'+str(seq_num)+rest+'\n'+seq+'\n')
  	to_write = '>species'+str(seq_num)+rest
  	csv_write.write( info[0] + ',' + to_write + ',' + info[2] + ',' + info[3] + ',' + info[4])
  	seq_num += 1
	new_found.remove(info)
  	
pick = open ('day'+str(day)+'.pickle','w')
cPickle.dump (current, pick)
pick.close()

csv_write.close()
csv_read.close()
fasta_write.close()

