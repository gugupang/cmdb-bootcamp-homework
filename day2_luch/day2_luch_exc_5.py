#!/usr/bin/env python

Cufflinks_output =  "/Users/cmdb/data/day1/Tophat_output/accepted_hits_no_head.sam"

f = open (Cufflinks_output)

num_al_2L = 0
num_al_2R = 0
num_al_3L = 0
num_al_3R = 0
num_al_4X = 0

for line in f:
    column = line.split("\t")
    if column[2] == "2L":
        num_al_2L =+ 1

for line in f:
    column = line.split("\t")
    if column[2] == "2R":
        num_al_2R =+ 1
                    
for line in f:
    column = line.split("\t")
    if column[2] == "3L":
        num_al_3L =+ 1
            
            
for line in f:
    column = line.split("\t")
    if column[2] == "3R":
        num_al_3R =+ 1  
            
for line in f:
    column = line.split("\t")
    if column[2] == "4X":
        num_al_4X =+ 1  
            
            
print num_al_2L
print num_al_2R 
print num_al_3L
print num_al_3R
print num_al_4X                                     