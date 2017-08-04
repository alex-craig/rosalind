# mendelianInheritance.py
# Alexander Craig
#
# Given: Three positive integers k, m, and n, representing a population 
# containing k+m+n organisms: k individuals are homozygous dominant for 
# a factor, m are heterozygous, and n are homozygous recessive.
#
# Return: The probability that two randomly selected mating organisms will 
# produce an individual possessing a dominant allele (and thus displaying the 
# dominant phenotype). Assume that any two organisms can mate.
#
# Sample Dataset: 2 2 2
# Sample Output: 0.78333

import sys

def calcProbDom():
    # creates list of import k m n data
    mendDataTuple = sys.stdin.read().strip().split(' ')
    # converts list members to int
    for i in range(0, len(mendDataTuple)):
        mendDataTuple[i] = float(mendDataTuple[i]) 
    # tuple convert
    mendDataTuple = tuple(mendDataTuple)
    # unpacks data into vars
    k, m, n = mendDataTuple
    total = k + m + n
    kFreq = k / total
    mFreq = m / total
    nFreq = n / total

    # all mates with K will be dom
    probK = kFreq 
 
    probM = mFreq * ( (k/(total-1)) + 
    (((m-1)/(total-1)) * 0.75) + 
    ((n/(total-1)) * 0.5) )

    probN = nFreq * ( (k/(total-1)) + 
    ((m/(total-1))*0.5))

    prob = probK + probM + probN

    return prob

if __name__ == "__main__":
    print calcProbDom()
