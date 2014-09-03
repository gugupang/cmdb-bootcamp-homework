#!/bin/bash

#
# Day 1 - Homework: Part 2 - debug this bash script
#

echo "There are around 6 mistakes"

FASTQ_DIR=/Users/cmdb/data/fastq
OUTPUT_DIR=/Users/cmdb/data/day1
SAMPLE_PREFIX=SRR072

GENOME_DIR=/Users/cmdb/data/genomes
GENOME_INDEX_BASE=dmel-all-chromosome-r5.57
ANNOTATION=dmel-all-r5.57.gff

CORES=4

for i in $(seq 893 916)
do
  echo fastqc -o $OUTPUT_DIR $FASTQ_DIR/$SAMPLE_PREFIX$i.fastq.gz 
  echo tophat -p4 -G $GENOME_DIR/$ANNOTATION -o $SAMPLE_PREFIX$i --no-novel-junc --segment-length 20 $GENOME_DIR/$GENOME_INDEX_BASE $FASTQ_DIR/$SAMPLE_PREFIX$i.fastq
  echo cufflinks -p4 -G $GENOME_DIR/$ANNOTATION -o $SAMPLE_PREFIX$i $OUTPUT_DIR/$SAMPLE_PREFIX$i/accepted_hits.bam
done