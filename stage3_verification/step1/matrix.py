#Author: Douglas Huang
#Modified: April 15, 2015
#Function: Finds unique and common species betweeen replicates and merges their RPMs into one table.
#Instructions: Enter the filepath to the stress directory and the number of files to process as command-line arguments. Change wildcard on line 18 if necessary.

import sys
import glob
import os 	

workdir = sys.argv[1] #filepath of stress directory
num_reps = int(sys.argv[2]) #number of files must be entered as a command-line argument
counter = 0
namelist = []
species = {}
stress_list = []
control_list = []

os.chdir(workdir)
write_name = os.path.basename(os.getcwd()) #uses directory name as basename for output files

seqeuence_log = open(write_name + "_sequence_log.txt", "w") #create log file (comma-delimited) to store sequences for later processing

#iterate through directory and sort files into stress or control categories
for rpm_file in glob.glob("*rpm_blasted*.csv"):	#replicate .csv wildcard
	if "Heat" in rpm_file or "UV" in rpm_file or "Light" in rpm_file: #change search terms if necessary
		stress_list.append(rpm_file)
	else:
		control_list.append(rpm_file)

file_list = control_list + stress_list

for rpm_file in file_list:	#replicate .csv wildcard
	read_file = open(rpm_file, "r")
	length = len(read_file.name)
	lines = read_file.read().splitlines()

	ind_1 = read_file.name.index(".") 
	base = read_file.name[:ind_1] 

	read_file.close()

	namelist.append(base) #collecting replicate names to create the table headings

	for line in lines[1:]:
		info = line.split(",")
		curr_species = info[2].split(" ")[0]
		curr_rpm = info[4]
		#print(curr_species+"\t"+str(curr_rpm)) #for debugging
		if (float(curr_rpm) < 10): #filter out entries with less than 10 RPM
			continue 
		if curr_species not in species:
			species[curr_species] = [0]*num_reps
			seqeuence_log.write(curr_species + "," + info[1] + "\n") 
		if curr_species in species:
			species[curr_species][counter] += float(curr_rpm) #adding RPM for identical entries
		
	counter += 1

seqeuence_log.close()

write_file = open(write_name + "_matrix.csv", "w")
write_file.write("species,")

#since it is .csv format, the last element is written separately from regular iteration to accomodate the newline

for i in range(0,(num_reps-1)):
	write_file.write(namelist[i]+",")

write_file.write(namelist[num_reps-1]+"\n")

for key in species:
	write_file.write(key+",")
	for i in range(0,(num_reps-1)):
		write_file.write(str(species[key][i])+",")
	write_file.write(str(species[key][num_reps-1])+"\n")

write_file.close()