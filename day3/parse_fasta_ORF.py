#!/usr/bin/env python

import sys
from fasta import FASTAReader
            
reader = FASTAReader( sys.stdin)

sequence_list = []
for sid, sequence in reader:
    sequence_list.append(sequence)

sorted_sequence_list = sorted(sequence_list, key=len, reverse=True)

longest_100 = sorted_sequence_list[0:100]

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
index = 0

starts_list = []

for long_seq in longest_100 :
    for i in range( 0, len(long_seq) - k):
        read_trimer = long_seq[i:i+k]
        if read_trimer == "ATG":
            starts_list.append(long_seq[i:])
print starts_list
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
    
    