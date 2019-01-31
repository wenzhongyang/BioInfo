#wget ftp://ftp-trace.ncbi.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR191/SRR1916155/SRR1916155.sra

import sys
srr_acc = sys.argv[1]
#ref = sys.argv[2]
with open ( srr_acc) as acc_file_handle:
    for line in acc_file_handle:
        line = line.rstrip()
       # print (line)
       # line1 = line.split
       # print (line1[0])
        cmd_str="wget ftp://ftp-trace.ncbi.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/{SRR_Six}/{SRR_acc}/{sra_file}".format(SRR_Six = line[0:6], SRR_acc=line,sra_file = line + '.sra')
        print (cmd_str)
