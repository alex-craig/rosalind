# motifFind.py
# Alexander Craig  
# 
# Given: Two DNA strings s and t (each of length at most 1 kbp).
# Return: All locations of t as a substring of s.
#
# Note!! gives string and list index plus 1

import sys

def reportMotifLocations():
    s, t = sys.stdin.read().strip().split('\n')
    print s
    print t

    results = ""
    for pos in range(0, len(s)):
        if s[pos : pos + len(t)] == t:
            results = results + str(pos + 1) + ' '
    print results

if __name__ == "__main__":
    reportMotifLocations()