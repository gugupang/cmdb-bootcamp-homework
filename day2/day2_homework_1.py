#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
# male data set
cufflinks_output = "/Users/cmdb/data/results/SRR072893_clout/genes.fpkm_tracking"
df = pd.read_table( cufflinks_output )
#female data set
cufflinks_output2 = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"
df2 =  pd.read_table(cufflinks_output2)

male_female = pd.DataFrame({"male":df["FPKM"], "female": df2["FPKM"]})

#print df,info()

first_one_third = df.sort("FPKM", ascending = False).iloc[0: 5199]
second_one_third = df.sort("FPKM", ascending = False).iloc[5200: 10399]
last_one_third = df.sort("FPKM", ascending = False).iloc[10400: ]


list_boxplot = [ first_one_third["FPKM"], second_one_third["FPKM"], last_one_third["FPKM"] ]

#print list_boxplot
plt.figure()
#plt.boxplot( [first_one_third["FPKM"]])
plt.boxplot(list_boxplot)
plt.ylim(-50, 300)
plt.savefig("boxplot_one_third.png")

