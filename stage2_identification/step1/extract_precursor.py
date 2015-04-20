
#import sys


def extract_precursor(mature_mRNA, hairpin):
    precursor = ''
     
    
    premiRNA_file = hairpin
    mirbase_seq_line=''
    
    pre_mRNA = ''
    pre_mRNA_r = 'false' #for those sequences that have R159 in mature.fa but r-159 in hairpin.fa 
    pre_mRNA_r2 = 'false' #for those sequences that have miR-159 in mature.fa but MIR-159 in hairpin.fa    
    pre_mRNA_r3 = 'false' #for those sequences that have miR-159 in mature.fa but mir-159 in hairpin.fa
    if mature_mRNA[3:7] == ('-let' or '-lin'):
        if mature_mRNA[3:7] == '-let':
            mature_mRNA = mature_mRNA.replace('-let','-let-')
        else:
            mature_mRNA = mature_mRNA.replace('-lin','-lin-')
        if mature_mRNA[-3] == '-' :
            last_char = mature_mRNA[-3:]
            mature_mRNA = mature_mRNA.replace(last_char,'')
        pre_mRNA_r = mature_mRNA
    
    elif mature_mRNA[-1] == 'p':
        if mature_mRNA[-2] == '5' or mature_mRNA[-2] == '3':                
            pre_mRNA = mature_mRNA.replace('-5p','')
            pre_mRNA = pre_mRNA.replace('-3p','')
            if pre_mRNA[-2] == '.' :
                last_char = pre_mRNA[-1]
                pre_mRNA = pre_mRNA.replace('.' + last_char,'')
            pre_mRNA_r = pre_mRNA.replace('R','r-')
            pre_mRNA_r2 = pre_mRNA.replace('miR','MIR')
            pre_mRNA_r3 = pre_mRNA.replace('R','r')
        else:
            pre_mRNA = mature_mRNA
            pre_mRNA_r = pre_mRNA.replace('R','r-')
            pre_mRNA_r2 = pre_mRNA.replace('miR','MIR')
            pre_mRNA_r3 = pre_mRNA.replace('R','r')
    elif mature_mRNA[-2] == '.':
        pre_mRNA = mature_mRNA
        if mature_mRNA[-4] == '5' or mature_mRNA[-4] == '3':
            pre_mRNA = mature_mRNA.replace('-5p','')
            pre_mRNA = pre_mRNA.replace('-3p','')
        if pre_mRNA[-2] == '.' :
            last_char = pre_mRNA[-1]
            pre_mRNA = pre_mRNA.replace('.' + last_char,'')
        pre_mRNA_r = pre_mRNA.replace('R','r-')
        pre_mRNA_r2 = pre_mRNA.replace('miR','MIR')
        pre_mRNA_r3 = pre_mRNA.replace('R','r')
    
    else:
            pre_mRNA = mature_mRNA
            pre_mRNA_r = pre_mRNA.replace('R','r-')
            pre_mRNA_r2 = pre_mRNA.replace('miR','MIR')
            pre_mRNA_r3 = pre_mRNA.replace('R','r')
                  
    with open(premiRNA_file) as pre_mRNA_fp:
        ipre_mRNA_fp = iter(pre_mRNA_fp)
        found_flag = False
        precursor = ''
        
        for line in pre_mRNA_fp:

            if found_flag == True:
                break
            if pre_mRNA_r in line or (pre_mRNA_r2 in line) or (pre_mRNA_r3 in line):
                found_flag = True
                precursor = line
                pre_mRNA_seq_line = next(ipre_mRNA_fp).rstrip('\n')
                next_line = next(ipre_mRNA_fp)
                while not next_line.startswith('>') or (pre_mRNA_r in next_line or pre_mRNA_r2 in next_line or pre_mRNA_r3 in next_line):
                    if  pre_mRNA_r in next_line or pre_mRNA_r2 in next_line or pre_mRNA_r3 in next_line:
                        next_line = next(ipre_mRNA_fp)
                        pre_mRNA_seq_line += '\n' + next_line
                    pre_mRNA_seq_line += next_line.rstrip('\n')
                    try:
                        next_line = next(ipre_mRNA_fp)
                    except StopIteration:
                        break
                mirbase_seq_line += pre_mRNA_seq_line
                precursor += mirbase_seq_line                
            
            else:
                pass    

    return precursor
