#!/usr/bin/env python

import sys
from fasta import FASTAReader
            
reader = FASTAReader( sys.stdin)

sequence_list = []
for sid, sequence in reader:
    sequence_list.append(sequence)

sorted_sequence_list = sorted(sequence_list, key=len, reverse=True)

longest_100 = sorted_sequence_list[0:100]

def complement(s): 
    basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 
    letters = list(s) 
    letters = [basecomplement[base] for base in letters] 
    return ''.join(letters)

longest_100_revcom = []
for strand in longest_100:
   revcom = complement(strand[::-1])
   longest_100_revcom.append(revcom)

#print longest_100_revcom  

longest_both_strands = [longest_100, longest_100_revcom]

#import re

#start = "ATG"

#for i in longest_100:
    
#    print type (i)
#    start = re.compile("ATG")
#    h.match(i)
#    start = re.match(i, "ATG")
#print start    
#start = re.match("ATG", longest_100)

#print start

k = 3

starts_list = []

for long_seq in longest_100 :
    for i in range( 0, len(long_seq) - k):
        read_trimer = long_seq[i:i+k]
        if read_trimer == "ATG":
            starts_list.append(long_seq[i:])
#print starts_list
#            starts[start] = set( [index] )
#        else:
#            starts[start].add(index)
#    index += 1
#print  starts
#matched_sequences = set()
#for i in range(0, len( query) - k ):
#    kmer = query[i:i+k]
#    matched_sequences.update( kmers[kmer])
#    if kmer in kmers:
#        matched_sequences.update( kmers[kmer])
#print "Query matched", sorted(matched_sequences)
    
stop_list = []

for seq in starts_list :
    n = len(seq)//3-1
    for j in range( 0, n):
        multiple_3 = 3*j 
        read_trimer2 = seq[multiple_3:multiple_3+3]
        if read_trimer2 == "TAG" or "TAA" or "TGA":
            stop_list.append(seq[,])
            

#print stop_list












    
    