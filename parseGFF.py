#!/usr/bin/env python3

# read in data from fasta file
import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser(description="This script filters out sequences from FASTA files")

parser.add_argument("fasta", help="name of FASTA file - must be first")

parser.add_argument("gff", help="name of GFF file - must be second")

args = parser.parse_args()

for genome in SeqIO.parse(args.fasta, "fasta"):
    #print(genome.seq)

# get info from gff that tell which parts to print
#open gff file and read in line by line with loop
    with open(args.gff) as lines:
        for line in lines.readlines():
            #(seqname, source, feature, start, end, score, strand, frame, attribute) = line.split("\t")
             #find the headers for gff files
            start = line.split()[4]
            end = line.split()[5]
            gene = line.split()[10]
            h1 = line.split()[0]
            h2 = line.split()[1]
            print(">{}_{}".format(h1, gene) + '\n' + (genome.seq[int(start):int(end)+1]))
# split lin into list, use begin and end coords to extract info from the genome
# print with header that tells gene and organism
# close GFF file
#seqname, attribute
