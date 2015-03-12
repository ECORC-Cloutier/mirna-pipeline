
import sys

name = sys.argv[1]
f = open (name,'r')
o = open (name + '.fa', 'w')

ids = set()
count = 0
for line in f:
  sp = line.split(',')
  if (sp[1] not in ids):
    o.write(sp[1] +'\n')
    o.write(sp[2] +'\n')
    ids.add(sp[1])
