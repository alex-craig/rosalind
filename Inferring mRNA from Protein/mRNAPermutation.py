# mRNAPermutation.py
# Alexander Craig
#
# Takes a protein sequence and returns the number of possible mRNA sequences
# it could have came from.

import sys

def tabulateAAFrequency():
    # takes terminal input and turns it into a iterable string list
    proteinStr = sys.stdin.read()
    proteinList = []
    for char in proteinStr[:len(proteinStr)-1]:
        proteinList.append(char)
    
    # a dictionary of the number of redundancies in the codon table
    aaDict = {
        'F':2,
        'L':2,
        'S':4,
        'Y':2,
        'C':2,
        'W':1,
        'L':4,
        'P':4,
        'H':2,
        'Q':2,
        'R':4,
        'I':3,
        'M':1,
        'T':4,
        'N':2,
        'K':2,
        'S':2,
        'R':2,
        'V':4,
        'A':4,
        'D':2,
        'E':2,
        'G':4
    }

    product = 3
    for x in range(len(proteinList)):
        product = product * aaDict[proteinList[x]] 

    print product % 1000000

    '''# an updatable dictionary to tally the number of aa in a protein
    frequencyDict = {
        'F':0,
        'L':0,
        'S':0,
        'Y':0,
        'C':0,
        'W':0,
        'L':0,
        'P':0,
        'H':0,
        'Q':0,
        'R':0,
        'I':0,
        'M':0,
        'T':0,
        'N':0,
        'K':0,
        'S':0,
        'R':0,
        'V':0,
        'A':0,
        'D':0,
        'E':0,
        'G':0
    }

    # updates the frequencyDict
    for aa in proteinList:
        frequencyDict[aa] += 1
    
    # permutations starts at 3 because of the 3 stop codons
    permutations = 3

    # for any nonzero key-value in the frequency dict multiply it by the redundancy
    # and then the existing permutations
    for aa in frequencyDict:
        if frequencyDict[aa] != 0:
            permutations *= (frequencyDict[aa] * aaDict[aa])
    
    print permutations % 1000000
    print frequencyDict'''
    
if __name__ == "__main__":
    print tabulateAAFrequency()