#!/usr/bin/env python

Cufflinks_output =  "/Users/cmdb/data/day1/Tophat_output/accepted_hits_no_head.sam"

f = open(Cufflinks_output)

for l in f:
    column = l.split("\t")
    print column[2]
    
    
         
        
            


        
