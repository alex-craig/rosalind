# hammingDistance.py
# Alexander Craig
#
# Takes a single text file of DNA sequences of same length and outputs the 
# hamming distance or the differing frequency

import sys

def findHammingDistance():
    # takes terminal text file FASTA DNA seqs and splits on newline 
    rawData = sys.stdin.read().strip().split('\n')
    
    hammingDistance = 0
    for base in range(0, len(rawData[0])):
        if (rawData[0][base] != rawData[1][base]):
            hammingDistance += 1
    return hammingDistance

if __name__ == "__main__":
    print findHammingDistance()