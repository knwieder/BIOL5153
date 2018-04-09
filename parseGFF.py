#!/usr/bin/env python3

# read in data from fasta file
from Bio import SeqIO

for genome in SeqIO.parse("watermelon.fsa", "fasta"):
    #print(genome.seq)

# get info from gff that tell which parts to print
#open gff file and read in line by line with loop
    with open('watermelon.gff') as lines:
        for line in lines.readlines():
            start = line.split()[4]
            end = line.split()[5]
            gene = line.split()[10]
            print(">Citrullus_lanatus_{}".format(gene) + '\n' + (genome.seq[int(start):int(end)+1]))
# split lin into list, use begin and end coords to extract info from the genome
# print with header that tells gene and organism
# close GFF file
