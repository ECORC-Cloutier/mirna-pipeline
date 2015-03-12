from Bio.Blast import NCBIXML
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Blast.Applications import NcbiblastnCommandline
import sys
#import timeit


def extract_mir_id( full_title):
    return full_title.split()[-1].split('_')[0]

e_val = 10
name = sys.argv[1] #input_file
db_name = sys.argv[2]
haveXML = False 
out_file_name =  sys.argv[3] 
xml_file_name = out_file_name + ".xml"
novel_file_name = out_file_name + "_novel" 
mature_file_name = out_file_name + "_mature" 
db_fasta = sys.argv[4] #mirBASE (mature.fa)

#time_file_name = out_file_name + "_execution_time.txt"
#time_handle = open(time_file_name, "w")
#start = timeit.default_timer()

if not haveXML:
    blastn_cline = NcbiblastnCommandline(penalty=-5, reward=4, max_target_seqs=100, word_size=11, query=name, db=db_name, evalue=e_val,outfmt=5, out=xml_file_name)
    stdout, stderr = blastn_cline()
try:
    handle = open (xml_file_name)
    success = True
except IOError:
    pass

if success:
    novel = []
    mature = [] 
    records  = NCBIXML.parse(handle)
    record_index = SeqIO.index(name, "fasta")
    mirbase_index = SeqIO.index(db_fasta, "fasta")
    mir_dict = dict()
    mature_summary = open (mature_file_name+".csv",'w')
    mature_fasta = open (mature_file_name+".fa",'w')
    mature_summary.write('Seq#,Query,Hit,Query start,Query end,Subject start,Subject end,Strand,Score,E-Value,Query length,Match length,Mismatches in HSPS\n')
    count = 1
    flag = 0
    mismatches_in_hsp = 0
    mature_title = ''
    group_mature_dict = dict()
    group_mature_fasta_dict = dict()
    
    #create dict for mature.fa
    lookup_mature = dict()
    for seq_record in SeqIO.parse(db_fasta,"fasta"):
        lookup_mature[seq_record.id] = seq_record.seq
    for rec in records:
        if (len(rec.alignments)==0):
            novel.append(">" + rec.query + "\n" + str(record_index[rec.query].seq))
        else:
            found = False
            counter = 0    
            for a in rec.alignments:
                alignment = str(a)
                hit = '>' + str(alignment.split()[1]) + ' ' + str(alignment.split()[2]) + ' ' + alignment.split()[3] + ' ' + alignment.split()[4] + ' ' + alignment.split()[5]
                               
                for x in a.hsps:
                    hsps = str(x).split()    
                    query = str(record_index[rec.query].seq)
                    mismatches_in_hsp = x.match.count(' ')
                    mismatches_flag = 0
                    gap_flag = 0

                    if mismatches_in_hsp in range(1,5):
                        mismatches_flag = 1

                    if x.query.find('-') == -1:
                        if x.sbjct.find('-') == -1:
                            pass
                        else:
                            gap_flag = 1
                    else:
                        gap_flag = 1
                    
                    score = int(hsps[1])
                    mature_title = a.title.split()[1]
                    match_length = len(x.match)
                    query_length = len(query)
                    subject_length = len(str(lookup_mature[mature_title]))
                    strand = str(x.frame)
                    query_seq = Seq(str(record_index[rec.query].seq))
                    strand_csv = strand.split(',')[0] + ';' + strand.split(',')[1].split(' ')[1]
                    out_score = str(score) + ' (' + hsps[2].split('(')[1] + ' bits)'
                    query = str(record_index[rec.query].seq)  
                    subject = x.sbjct
                    mir_dict[rec.query] =  extract_mir_id(mature_title)	  
                    mismatches_out = abs(len(query) - len(x.match))
                    total = mismatches_in_hsp + mismatches_out
                    
                    if (match_length >= 18 and ((query_length == match_length) or (subject_length == match_length)) and counter == 0 and mismatches_flag == 1 and gap_flag == 0):
                        print "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                        print "hsps: "
                        print str(x)
                        print "\nquery length: " + str(query_length) + "\nsubjt length: " + str(subject_length) + "\nmatch length: " + str(match_length)
                        print "\nmismatches_in_hsp: " + str(mismatches_in_hsp)
                        print "\nQuery:   " + query.upper()
                        print "Subject: " + str(lookup_mature[mature_title])
                        print rec.query
                        
                        count = count + 1
                        found = True                        
                        counter = 1
                        
                        if (int(strand.split(',')[1].split(' ')[1].split(')')[0]) == -1):
                            mature_fasta.write('>>' + str(rec.query) + '-rc' + '\n')
                            mature_fasta.write((str(query_seq.reverse_complement()) + '\n'))
                        else:
                            mature_fasta.write('>>' + str(rec.query) + '\n')
                            mature_fasta.write(str(record_index[rec.query].seq) + '\n')
                        mature_fasta.write(str(hit) + '\n')
                        mature_fasta.write(str(lookup_mature[mature_title]) + '\n')
                        
                        mature_summary.write(str(count) + ',>>' + str(rec.query) + ',' + hit + ',' + str(hsps[10]) + ',' 
                        + str(hsps[12]) + ',' + str(hsps[-3]) + ',' + str(hsps[-1]) + ',' + strand_csv + ',' + out_score + ',' 
                        + str(hsps[5]).split(',')[0] + ',' + str(len(query)) + ',' + str(len(x.match)) + ',' 
                        + str(mismatches_in_hsp) + '\n')
                        
                        
                        mature_mirna = str(lookup_mature[mature_title])
                        group_mature_fasta_header_line = '>>' + str(alignment.split()[1]) + ' ' + str(alignment.split()[2]) + ' ' + alignment.split()[3] + ' ' + alignment.split()[4] + ' ' + alignment.split()[5]
                        group_mature_fasta_header_line = group_mature_fasta_header_line + '\n' + mature_mirna
                        
                        if (group_mature_fasta_header_line[9] == '-'):
                            group_mature_fasta_header_line = group_mature_fasta_header_line[0:9] + group_mature_fasta_header_line[10:]        
                                
                        if (mature_title[7] == '-'):
                            mature_title = mature_title[0:7] + mature_title[8:]
                        
                        mature.append(rec.query)
                        mirna =  mature_title
                        
                        ### code for group mature csv file                   
                        try:
                            current_mature_dict = group_mature_dict[mirna]
                        except KeyError:
                            group_mature_dict[mirna] = ''
                        current_mature_dict = group_mature_dict[mirna]
                        current_mature_dict = current_mature_dict + rec.query + ',' + str(mismatches_in_hsp) + ","
                        group_mature_dict[mirna] = current_mature_dict
                        
                        ### code for group mature fasta file
                        try:
                            current_fasta_dict = group_mature_fasta_dict[group_mature_fasta_header_line]
                        except KeyError:
                            group_mature_fasta_dict[group_mature_fasta_header_line] = ''
                        current_fasta_dict = group_mature_fasta_dict[group_mature_fasta_header_line]
                        if (int(strand.split(',')[1].split(' ')[1].split(')')[0]) == -1):
                            current_fasta_dict = group_mature_fasta_dict[group_mature_fasta_header_line] + '\n>' + str(rec.query) + '-rc\n' + str(query_seq.reverse_complement())
                        else:
                            current_fasta_dict = group_mature_fasta_dict[group_mature_fasta_header_line] + '\n>' + str(rec.query) + '\n' + str(record_index[rec.query].seq)
                        group_mature_fasta_dict[group_mature_fasta_header_line] = current_fasta_dict
                        group_mature_dict[mirna] = current_mature_dict
                
            if not found:
                novel.append(">" + rec.query + "\n" + str(record_index[rec.query].seq))
    mature_summary.close()
    mature_fasta.close()
    count = 1
    novel_file = open (novel_file_name+".fa",'w')
    for id in novel:
        char = '>'
        m_id = char + str(id)
        novel_file.write(id + '\n')
        count += 1
    novel_file.close()
  
f=open ("group_mature_" + sys.argv[3] + ".csv",'w')
f.write('miRBase miRNA,best matching sample reads,related_miRNAs' + '\n')
for mirna in sorted(group_mature_dict, key=lambda x: x[7:]):
    if group_mature_dict[mirna] != '':
        #print ('miRNA %s at %s' % (mirna, sample))      
        f.write(str(mirna) + ',' + group_mature_dict[mirna] + '\n')
f.close()

f=open ("group_mature_" + sys.argv[3] + ".fa",'w')
for group_mature_fasta_header_line in sorted(group_mature_fasta_dict, key=lambda x: x[9:]):
    if group_mature_fasta_dict[group_mature_fasta_header_line] != '':
        #print ('miRNA %s at %s' % (mirna, sample))      
        f.write(str(group_mature_fasta_header_line) + group_mature_fasta_dict[group_mature_fasta_header_line] + '\n')
f.close()
#stop = timeit.default_timer()
#time_handle.write("Total time: %.5f" % ((stop-start)/60) + " minutes")
#time_handle.close()