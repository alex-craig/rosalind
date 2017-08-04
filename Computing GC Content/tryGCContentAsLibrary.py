# tryGCContentAsLibrary.py
# Alexander Craig
#
# Attempt to import functions from other py files

import sys
import gcContent

if __name__ == "__main__":
    listTuples = gcContent.getDataAndSeparate()
    # Unpack into variables
    fastaNames, fastaData = listTuples
    print (gcContent.getGCContent(fastaNames, fastaData))

