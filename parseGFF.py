#!/usr/bin/env python3

# read in data from fasta file
import argparse
from Bio import SeqIO

def get_args():

    parser = argparse.ArgumentParser(description="This script filters out sequences from FASTA files")

    parser.add_argument("fasta", help="name of FASTA file - must be first")

    parser.add_argument("gff", help="name of GFF file - must be second")

return parser.parse_args()


def rev_comp(dna):
    dna = genone.seq
    compA=(dna.replace("A", "t"))
    compT=(compA.replace("T", "a"))
    compC=(compT.replace("C", "g"))
    compG=(compC.replace("G", "c"))

    dna_comp = compG.upper()
#print(dna_comp)
    dna_comp = dna_comp[::-1]
    print(dna_comp)
return(dna_comp)

def main():
    for genome in SeqIO.parse(args.fasta, "fasta"):
        dna = genome.seq

        with open(args.gff) as lines:
            for line in lines.readlines():
                (seqname, source, feature, start, end, score, strand, frame, attribute) = line.split("\t")
                gene = line.split()[10]
                rev = line.split()[6]
                if rev == "+"
                    print(">{}_{}".format(seqname, gene) + '\n' + (genome.seq[int(start):int(end)+1]))
                else
                    print(">{}_{}".format(seqname, gene) + '\n' + (genome.seq.rev_comp()[int(start):int(end)+1]))

args = get_args()
# split line into list, use begin and end coords to extract info from the genome
# print with header that tells gene and organism
# close GFF file
