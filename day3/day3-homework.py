#!/usr/bin/env python

import sys

line = sys.stdin.readline()
assert line.startswith(">")
id = line[1:].rstrip("\r\n")

sequences = []
while True:
    line = sys.stdin.readline()
    if line.startswith(">"):
        break
    else:
        sequences.append (line.strip())
        
sequence = "".join( sequences)

print id, sequence
