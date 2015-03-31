import sys

name = sys.argv[1]
ref = sys.argv[2]
file_out = sys.argv[3]
csv_read = open(name, "r")

rind = name.index('.')
base = name[0:rind]

lines = csv_read.readlines()
csv_read.close()

data = dict()

for line in lines[1:]:
    info = line.split(",")
    data[info[1]] = [info[2],info[3],info[4]]

csv_ref = open(ref, "r")

query_lines = csv_ref.readlines()
csv_ref.close()

csv_write = open(base+"_rpm_blasted_"+file_out+"mm.csv", "w") 
csv_write.write("query,sequence,hit,count,normalized read count (RPM)\n")

for query in query_lines[1:]:
    info = query.split(",")
    curr_query = info[1][1:]
    curr_id = info[2][5:]
    if (curr_query in data):
        csv_write.write(curr_query+","+data[curr_query][0]+","+curr_id+","+data[curr_query][1]+","+data[curr_query][2])
    else:
        print "Not here \n"
csv_write.close()
