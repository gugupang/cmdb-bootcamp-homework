#!/usr/bin/env python


f = open ("/Users/cmdb/data/day1/Tophat_output/accepted_hits.sam")

npm = 0
 
for line in f:
    
    if "NM:i:0" in line:
        npm = npm + 1
print npm




    
    
         
        
            


        