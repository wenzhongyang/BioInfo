#hista2 -x ../../data/ref/yeast_ref -U ../../data/SRR1916152.fastq |samtools view -bS -|samtools sort - -o EV_strain_3.srt.bam


import sys
acc_file = sys.argv[1]
ref = sys.argv[2]
fq_dir = sys.argv[3]

with open (acc_file) as acc_file_handle:
    for line in acc_file_handle:
        # SRR1916152    EV_3
        line = line.rstrip()
        ele = line.split("\t")
       # print (line)
       # line1 = line.split
       # print (line1[0])
        cmd_str="hisat2 -x {ref} -U {fq_dir}/{SRR_acc}.fastq |samtools view -bS -|samtools sort - -o {sample_real_name}.srt.bam\nsamtools index {sample_real_name}.srt.bam".format(ref = ref, fq_dir = fq_dir, SRR_acc = ele[0], sample_real_name = ele[1])
        print (cmd_str)
