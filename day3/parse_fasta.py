#!/usr/bin/env python

"""
Parse a single FASTA record from stdin and print it
"""
import sys
from fasta import FASTAReader
            
reader = FASTAReader( sys.stdin)

sequence_list = []
for sid, sequence in reader:
    sequence_list.append(sequence)

sorted_sequence_list = sorted(sequence_list, key=len, reverse=True)

longest_100 = sorted_sequence_list[0:100]

for i in longest_100:
    if i.str.find("ATG")
    
    
    