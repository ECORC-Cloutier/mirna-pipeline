from subprocess import call
from Bio import SeqIO
from Bio.Align.Applications import MafftCommandline
from extract_precursor import extract_precursor
import sys

input_file = sys.argv[1]
wheat_file = sys.argv[2]

contig_index = SeqIO.index(wheat_file, "fasta")

# code for selecting a group

start = False
data = ''
mirbase_id_line = ''
mature_miRNA_id = ''
mature_miRNA_seq = ''
precursor = ''
fp = open(input_file)
for line_0mmfa in fp:
    if line_0mmfa.startswith('>>'):
        if data:
            """data contains all the species that matched with a mature mRNA
            creating a species file which will be used as a input to bowtie2"""            
            species = mature_miRNA_id + '_species.fa'
            f_species=open (species,'w')
            #writing species to a file            
            f_species.write(data)
            f_species.close()
            #output sam file creation
            output_file = species + '.sam'
            #performing bowtie2 with wheat genome and grouped species
            call(["bowtie2", "--score-min", "C,0",  "-a", "-f", "-x", "trit", "-U", species, "-S", output_file])
            #deleting species file as we don't need the file
            call(["rm", species])
            #taking only the matched contigs informations
            match_output_file = output_file + '.matches'
            
            f_matches = open (match_output_file,'w')
                      
            with open(output_file,'r') as sam_file:
                call(["mkdir", mature_miRNA_id])
                for line in sam_file:
                    if line.startswith('species'):
                        move_to_folder_name = 'msa_' + mature_miRNA_id + '_*'
                        try:            
                            no_of_match = int(line.split()[5].split('M')[0])
                            f_matches.write(line)
                            spec = line.split()[0] +  '_' + str(no_of_match)                          
                            contig = line.split()[2]
                            input_mafft_file = 'in_mafft_' + mature_miRNA_id + '_' + contig + '.fa'
                            output_mafft_file = 'msa_' + mature_miRNA_id + '_' + contig + '.fa'
                            
                            fin_mafft = open (input_mafft_file, 'w')
                            fout_mafft = open (output_mafft_file, 'w')
                            flag = int(line.split()[1]) & 16
                            if flag == 16:
                                contig_seq = contig_index[contig].seq.reverse_complement()
                            elif flag == 0:
                                contig_seq = contig_index[contig].seq
                            else:
                                pass
                            contig = '>' + line.split()[2]                            
                            to_write = str(data + contig + '\n' + contig_seq + '\n' + precursor + '\n>' + mirbase_id_line + '\n' + mature_miRNA_seq)                           
                            fin_mafft.write(to_write)
                            fin_mafft.close()
                            """Code for mafft 
                            Ref: 
                            http://biopython.org/DIST/docs/api/Bio.Align.Applications._Mafft.MafftCommandline-class.html
                            http://lists.open-bio.org/pipermail/biopython/2010-November/006900.html"""
                            mafft_cline = MafftCommandline(input=input_mafft_file)
                            stdout, stderr = mafft_cline()
                            fout_mafft.write(stdout)
                            fout_mafft.close()
                            call(["mv", input_mafft_file, mature_miRNA_id])
                            call(["mv", output_mafft_file, mature_miRNA_id])
                        except ValueError:
                            pass
                call(["mv", match_output_file, mature_miRNA_id])        
                f_matches.close()
                call(["rm", output_file])
        start = False
        data = ""
        # fetching mature mRNA id and sequence for each group        
        mirbase_id_line = line_0mmfa[2:].rstrip('\n')
        mature_miRNA_id = mirbase_id_line.split()[0]
        mature_miRNA_seq = next(fp).rstrip('\n')
        #fetching precursor using a functiion --> passing mature mRNA as a input to the function        
        precursor = extract_precursor(mature_miRNA_id, 'hairpin.fa')
    elif line_0mmfa.startswith('>species'):
        start = True
        data += line_0mmfa
    elif start:
        data += line_0mmfa

fp.close()
"""doing previous operation to the very last group"""            
species = mature_miRNA_id + '_species.fa'
f_species=open (species,'w')
#writing species to a file            
f_species.write(data)
f_species.close()
#output sam file creation
output_file = species + '.sam'
#performing bowtie2 with wheat genome and grouped species
call(["bowtie2", "--score-min", "C,0",  "-a", "-f", "-x", "trit", "-U", species, "-S", output_file])
#deleting species file as we don't need the file
call(["rm", species])
#taking only the matched contigs informations
match_output_file = output_file + '.matches'

f_matches = open (match_output_file,'w')
          
with open(output_file,'r') as sam_file:
    call(["mkdir", mature_miRNA_id])
    move_to_folder_name = 'msa_' + mature_miRNA_id + '_*'
    for line in sam_file:
        if line.startswith('species'):
            try:            
                no_of_match = int(line.split()[5].split('M')[0])
                f_matches.write(line)
                spec = line.split()[0] +  '_' + str(no_of_match)                          
                contig = line.split()[2]
                input_mafft_file = 'in_mafft_' + mature_miRNA_id + '_' + contig + '.fa'
                output_mafft_file = 'msa_' + mature_miRNA_id + '_' + contig + '.fa'
                
                fin_mafft = open (input_mafft_file, 'w')
                fout_mafft = open (output_mafft_file, 'w')
                flag = int(line.split()[1]) & 16
                if flag == 16:
                    contig_seq = contig_index[contig].seq.reverse_complement()
                elif flag == 0:
                    contig_seq = contig_index[contig].seq
                else:
                    pass
                contig = '>' + line.split()[2]                            
                to_write = str(data + contig + '\n' + contig_seq + '\n' + precursor + '\n>' + mirbase_id_line + '\n' + mature_miRNA_seq)                           
                fin_mafft.write(to_write)
                fin_mafft.close()
                """Code for mafft 
                Ref: 
                http://biopython.org/DIST/docs/api/Bio.Align.Applications._Mafft.MafftCommandline-class.html
                http://lists.open-bio.org/pipermail/biopython/2010-November/006900.html"""
                mafft_cline = MafftCommandline(input=input_mafft_file)
                stdout, stderr = mafft_cline()
                fout_mafft.write(stdout)
                fout_mafft.close()
                call(["mv", input_mafft_file, mature_miRNA_id])
                call(["mv", output_mafft_file, mature_miRNA_id])
            except ValueError:
                pass
    call(["mv", match_output_file, mature_miRNA_id])
    f_matches.close()
    call(["rm", output_file])
