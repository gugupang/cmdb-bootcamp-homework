#!/usr/bin/env python

Cufflinks_output =  "/Users/cmdb/data/day1/Tophat_output/accepted_hits_no_head.sam"

f = open (Cufflinks_output)

nl = 0 

while True:
    line = f.readline()
    if not line:
        break
    else:
        nl = nl + 1
    
print "# of alignments is ", nl