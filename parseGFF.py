#!/usr/bin/env python3

# read in data from fasta file
import argparse
import sys
import os
import re
from Bio import SeqIO
from collections import defaultdict

def get_args():

    parser = argparse.ArgumentParser(description="This script filters out sequences from FASTA files")

    parser.add_argument("fasta", help="name of FASTA file - must be first")

    parser.add_argument("gff", help="name of GFF file - must be second")

    return parser.parse_args()

def parse_fasta(fasta):
        # open and read the fasta files
        genome = SeqIO.read(fasta, "fasta")
        # for genome in SeqIO.parse(args.fasta, "fasta"):
        return genome.seq

def rev_comp(dna):
    #return dna.reverse_complement()
    dna1 = str(dna.upper())
    compA=(dna1.replace("A", "t"))
    compT=(compA.replace("T", "a"))
    compC=(compT.replace("C", "g"))
    compG=(compC.replace("G", "c"))

    dna_comp = compG.upper()

    dna_comp = dna_comp[::-1]
    #print(dna_comp)
    return(dna_comp)

def parse_gff(dna, gff):
    # open and parse the GFF file
    exon_list = []
    seq = defaultdict(list)

    gff_file = open(gff, 'r')
    for line in gff_file:
        # split each line on tab
        (seqname, source, feature, start, end, score, strand, frame, attribute) = line.split("\t")
        if(feature == "CDS" or feature == "tRNA" or feature == "rRNA"):
            # split attributes field
            atts = attribute.split(';')
            # grab the gene name and, if present the exon number
            gene = re.search("^Gene\s+(\S+)", atts[0])
            #exon = re.search("exon\s+(\d+)", atts[0])
            #if(gene and exon):
                #print(">" + seqname.replace(" ", "_") + "_" + gene.group(1) + "_" + exon.group(1))
            #else:
            #    print(">" + seqname.replace(" ", "_") + "_" + gene.group(1))

#for line in gff_file:
    #     (seqname, source, feature, start, end, score, strand, frame, attribute) = line.split("\t")
        # gene = re.search("^Gene\s+(\S+)", atts[0])
        # for gene
        #    exon_list.append(exon.strip())
            gene_name = gene.group(1)
    # extract corresponding sequence
            fragment = dna[int(start)-1:int(end)]
            if strand == "+":
                exon_list.append((gene_name, fragment))
            else:
                exon_list.append((gene_name, rev_comp(fragment)))

    for gene, sequence in exon_list:
        seq[gene].append(sequence)

    return seq, seqname

    gff_file.close()

def seqprint(seq, seqname):
    for gene, sequence in seq.items():
        print(">" + seqname.replace(" ", "_") + "_" + gene)
        print(str(sequence).replace("', '", ""))

def main():
    genome = parse_fasta(args.fasta)
    dictionary, seqname=parse_gff(genome, args.gff)
    seqprint(dictionary, seqname)


# get the command-line arguments
args = get_args()

main()
