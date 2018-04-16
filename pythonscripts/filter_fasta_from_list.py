#!/usr/bin/env python3

import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser(description="This script filters out sequences from FASTA files that are identified from a user-specified list")

parser.add_argument("fasta", help="name of FASTA file - must be first")

parser.add_argument("txt", help="name of text file - must be second", type=str)

args = parser.parse_args()

delete_these_seq = []

with open(args.txt, 'r') as list:
    for line in list.readlines():
        delete_these_seq.append(line.strip())
        #print(delete_these_seq)




for files in SeqIO.parse(args.fasta, "fasta"):
    if files.id not in delete_these_seq:
        print(files.format("fasta"))

    #    if files.id not in list:
    #        print(files.id, '\n', files.seq)




       #names = [l.strip() for l in list]

    #with open(args.fasta, 'r') as f:
    #    for query in names:
        #    for line in f:
        #       if not query in line:
        #           print(line, next(f))

    #with open(args.fasta, 'r') as f:
    #    lines = [l.strip() for l in f]

    #with open(args.txt, 'r') as list:
    #    for line in list:
    #        for query in lines:
        #        if query in line:

    #with open(args.fasta, 'r') as f:
    #    with open(args.txt, 'r') as list:
    #        for line in f.readlines():
    #            name = line.split()[0]
                #        print(line)
    #if gene_fa != gene_list:
