import sys

if ( len(sys.argv) < 3):
  print 'usage: python csv_split.py <size>> <fileName>'
  sys.exit()

length = int(sys.argv[1])
csv = sys.argv[2]
csv_read = open  ( csv, 'r')
lines = csv_read.readlines()
csv_read.close()
header = lines[0]
count = 0
start = True
file_num = 1
for line in lines[1:]:
    if (start):
      start = False
      csv_write = open ( csv + '.part' + str(file_num) , 'w')
      csv_write.write(header)
      csv_write.write(line)
      count+=1
    else:
      count+=1
      csv_write.write(line)
      if (count==length):
        csv_write.close()
        count = 0
        start = True
        file_num += 1
csv_write.close()
