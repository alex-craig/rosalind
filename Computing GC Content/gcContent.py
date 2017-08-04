# gcContent.py
# Alexander Craig
#
# Takes a data file of named FASTA seqs, manipulates and sorts the data and 
# prints the code responding to the one with the largest gc content

import sys

# use on piped text data returns a tuple of two lists (Names,Values)
def getDataAndSeparate():
    # takes the piped txt file and creates a list for each line
    rawDataset = sys.stdin.readlines()
    # removes the newline char for each line with a list comprehension 
    rawDataset = [x.strip() for x in rawDataset]
    # empty lists to store the data names and values accessable by keys
    fastaNames = []
    fastaData = []

    # iterates the items of the rawDataset appends names to name list and 
    # temporarily stores values in a temp list before recombining them 
    # into a permenent list
    keyCounter = -1
    tempSeqStore = []
    for line in rawDataset:
        if '>' in line:
            fastaNames.append(line)
            if keyCounter > -1:
                fastaData.append("".join(tempSeqStore))
                del tempSeqStore[:]
            keyCounter += 1
        else:
            tempSeqStore.append(line)
    fastaData.append("".join(tempSeqStore))

    return fastaNames, fastaData

# takes a list of Names and FASTA strings and returns the name of the one
# with the highest GC content
def getGCContent(fastaNames, fastaData):
    percentageList = []
    for fastaSeq in fastaData:
        A = 0
        T = 0
        C = 0
        G = 0
        
        for base in fastaSeq:
            if base == 'A':
                A += 1
            elif base == 'T':
                T += 1
            elif base == 'C':
                C += 1
            elif base == 'G':
                G += 1
        
        GCPercent = (float(G+C) / float(A+T+G+C))
        percentageList.append(GCPercent)
    
    return ((fastaNames[percentageList.index(max(percentageList))])[1:] + ' ' + str(max(percentageList)*100) + '%')

if __name__ == "__main__":
    listTuples = getDataAndSeparate()
    # Unpack into variables
    fastaNames, fastaData = listTuples
    print (getGCContent(fastaNames, fastaData))

