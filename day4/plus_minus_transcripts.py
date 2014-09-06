#!/usr/bin/env python
import pandas as pd

cufflinks_output = "/Users/cmdb/data/day1/Cufflinks_output/transcripts.gtf"
df = pd.read_table(cufflinks_output, header=None)

transcripts = df[2].str.contains("transcript")
#print transcripts
#print df[transcripts].head()
#print type(transcripts[7])

#plus = df[transcripts][6] == "+" #.str.contains("\+")
#minus = df[transcripts][6].str.contains("-")

#print transcripts
#print plus
plus = df[ df[2].str.contains("transcript") ][df[6] == "+"]
minus = df[ df[2].str.contains("transcript")][df[6]== "-"]

#print plus

plus.to_csv( "plus.gtf", sep = "\t" ,header=False,index=False)
minus.to_csv( "minus.gtf", sep = "\t",header=False,index=False)


