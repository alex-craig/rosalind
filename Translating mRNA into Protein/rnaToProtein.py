# rnaToProtein.py
# Alexander Craig
#
# Takes a single RNA string via terminal and outputs the protein string

import sys

def rnaToCodon():
    rnaStr = sys.stdin.read()
    rnaStr = [x.strip() for x in rnaStr]
    
    # string read to list to prevent conversion to list beforehand
    tempBaseStore = []
    codonList = []
    
    for base in rnaStr:
        if len(tempBaseStore) == 3:
            codonList.append(''.join(tempBaseStore))
            del tempBaseStore[:]
        tempBaseStore.append(base)
    #codonList.append(''.join(tempBaseStore))

    return codonList

def codonToProtein(codonList):
    codonTable = {
        'UUU': 'F',
        'UUC': 'F',
        'UUA': 'L',
        'UUG': 'L',
        'UCU': 'S',
        'UCC': 'S',
        'UCA': 'S',
        'UCG': 'S',
        'UAU': 'Y',
        'UAC': 'Y',
        'UAA': 'Stop',
        'UAG': 'Stop',
        'UGU': 'C',
        'UGC': 'C',
        'UGA': 'Stop',
        'UGG': 'W',
        'CUU': 'L',
        'CUC': 'L',
        'CUA': 'L',
        'CUG': 'L',
        'CCU': 'P',
        'CCC': 'P',
        'CCA': 'P',
        'CCG': 'P',
        'CAU': 'H',
        'CAC': 'H',
        'CAA': 'Q',
        'CAG': 'Q',
        'CGU': 'R',
        'CGC': 'R',
        'CGA': 'R',
        'CGG': 'R',
        'AUU': 'I',
        'AUC': 'I',
        'AUA': 'I',
        'AUG': 'M',
        'ACU': 'T',
        'ACC': 'T',
        'ACA': 'T',
        'ACG': 'T',
        'AAU': 'N',
        'AAC': 'N',
        'AAA': 'K',
        'AAG': 'K',
        'AGU': 'S',
        'AGC': 'S',
        'AGA': 'R',
        'AGG': 'R',
        'GUU': 'V',
        'GUC': 'V',
        'GUA': 'V',
        'GUG': 'V',
        'GCU': 'A',
        'GCC': 'A',
        'GCA': 'A',
        'GCG': 'A',
        'GAU': 'D',
        'GAC': 'D',
        'GAA': 'E',
        'GAG': 'E',
        'GGU': 'G',
        'GGC': 'G',
        'GGA': 'G',
        'GGG': 'G'
    }

    aaList = []
    for codon in codonList:
        if codonTable[codon] == 'Stop':
            break
        aaList.append(codonTable[codon])

    protein = ''.join(aaList)
    return protein

if __name__ == "__main__":
    codonList = rnaToCodon()
    print codonToProtein(codonList)