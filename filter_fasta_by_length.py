#!/usr/bin/env python3

# load the required modules
import argparse
from Bio import SeqIO


# create an ArgumentParser object ('parser') that will hold all the information necessary to parse the command line
parser = argparse.ArgumentParser(description="This script filters out sequences from FASTA files that are shorter than a user-specific length cutoff")

# must have required and optional arguments
# there are positional arguments that are *required* input and their position/order matters

# use the add_argument() method to add a positional argument
# argparse treats all options as strings unless told to do otherwise
parser.add_argument("fasta", help="name of FASTA file")

# add an optional argument, the length of cutoff for our filter
# set the optional arguments with two dashes
parser.add_argument("-m", "--min_seq_len", help="filter sequences that are <= min_seq_len in length (default = 300 nt)", type=int, default=300)

args = parser.parse_args()

parser.add_argument('filename')

for file in SeqIO.parse(args.fasta, "fasta"):
    with open(args.fasta) as lines:
        for line in lines.readlines():
            length = len(line)
            if length >= args.min_seq_len:
                print(line)
