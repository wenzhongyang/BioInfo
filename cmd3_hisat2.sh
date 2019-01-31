hisat2 -x ../ref/yeast_ref -U ../data//SRR1916152.fastq |samtools view -bS -|samtools sort - -o EV_3.srt.bam
hisat2 -x ../ref/yeast_ref -U ../data//SRR1916153.fastq |samtools view -bS -|samtools sort - -o EV_4.srt.bam
hisat2 -x ../ref/yeast_ref -U ../data//SRR1916154.fastq |samtools view -bS -|samtools sort - -o 3b_2.srt.bam
hisat2 -x ../ref/yeast_ref -U ../data//SRR1916155.fastq |samtools view -bS -|samtools sort - -o 3b_3.srt.bam
hisat2 -x ../ref/yeast_ref -U ../data//SRR1916156.fastq |samtools view -bS -|samtools sort - -o 3b_4.srt.bam
