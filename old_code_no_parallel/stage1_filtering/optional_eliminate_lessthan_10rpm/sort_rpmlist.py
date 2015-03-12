import natsort
file = open("test2.out", "r")
species = file.read().splitlines()
file.close()
sortedlist = natsort.natsorted(species)
output = open("test2_sorted.out", "w")
for line in sortedlist:
    output.write(line)
    output.write('\n')
output.close()
