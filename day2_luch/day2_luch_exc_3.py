#!/usr/bin/env python

Cufflinks_output =  "/Users/cmdb/data/day1/Tophat_output/accepted_hits.sam"

f = open (Cufflinks_output)

npm = 0
 
if "NM:i:1" in f:
    npm = npm + 1
print npm
    
    
         
        
            


        
