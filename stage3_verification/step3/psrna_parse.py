#Author: Douglas Huang
#Modified: April 16, 2015
#Function: Splits psRNATarget output into wheat and non-wheat files and extracts key target description information
#Instructions: Enter the filepath to the stress directory and the name of the psRNA output file as command-line arguments

import sys
import re
import os

workdir = sys.argv[1] #filepath of stress directory
file_name = sys.argv[2]	#name of psRNA output file

os.chdir(workdir)
write_name = os.path.basename(os.getcwd()) #uses directory name as basename for output files; change if desired

#get basename to name output files
# ind = file_name.index(".")
# base = file_name[:ind]

file_read = open(file_name, "r") 
file_write_wheat = open(write_name+"_wheat_processed.csv", "w") #wheat file
file_write_nonwheat = open(write_name+"_non_wheat_processed.csv", "w") #non-wheat file

lines = file_read.read().splitlines()

file_write_wheat.write("miRNA_Acc.\tTarget_Acc.\tUni_ID\tRep\tTarget_Desc.\n")
file_write_nonwheat.write("miRNA_Acc.\tTarget_Acc.\tUni_ID\tRep\tTarget_Desc.\n")

for line in lines[2:]:
	info = line.split("\t")
	target_info = info[11]

	#split data into wheat and non-wheat
	if "Triticum aestivum" in target_info:
		if "UniRef" in target_info: #check for desired target description information (i.e. UniRef and/or Rep, no UniRef)
			if "Rep:" in target_info:
				matches = re.search('_(\w\w\w\w\w\w).*(Rep:.*)', target_info)
				file_write_wheat.write(info[0]+"\t"+info[1]+"\t"+matches.group(1)+"\t"+matches.group(2)+"\t"+target_info+"\n")
			else:
				match = re.search('_(\w\w\w\w\w\w)', target_info)
				file_write_wheat.write(info[0]+"\t"+info[1]+"\t"+match.group(1)+"\tUnknown\t"+target_info+"\n")
		else:
			file_write_wheat.write(info[0]+"\t"+info[1]+"\tUnknown\tUnknown\t"+target_info+"\n")
	else: 
		if "UniRef" in target_info: #check for desired target description information
			if "Rep:" in target_info:
				matches = re.search('_(\w\w\w\w\w\w).*(Rep:.*)', target_info)
				file_write_nonwheat.write(info[0]+"\t"+info[1]+"\t"+matches.group(1)+"\t"+matches.group(2)+"\t"+target_info+"\n")
			else:
				match = re.search('_(\w\w\w\w\w\w)', target_info)
				file_write_nonwheat.write(info[0]+"\t"+info[1]+"\t"+match.group(1)+"\tUnknown\t"+target_info+"\n")
		else:
			file_write_nonwheat.write(info[0]+"\t"+info[1]+"\tUnknown\tUnknown\t"+target_info+"\n")

file_read.close()
file_write_wheat.close()
file_write_nonwheat.close()