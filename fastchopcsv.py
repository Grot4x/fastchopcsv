#!/usr/bin/env python3
"""
Quite fast spliting of csv files in python3

Usage:

python3 fastchopcsv.py FILE LINES_PER_FILE

FILE = the file you want to spliting
LINES_PER_FILE = the amount of lines you want to have in the new files

"""
import sys
import os
import time

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

start = time.time()

with open(sys.argv[1], 'r') as SOURCE_FILE:
    userlen = int(sys.argv[2])
    basename = SOURCE_FILE.name
    filelen = file_len(basename)
    header = SOURCE_FILE.readline()
    c=0
    maxlen = filelen / userlen
    print("Here some stats:\n Your file %s has %s lines it will be splitted into %s files.\n Each file has %s lines." % (basename,filelen,int(maxlen)+1,userlen))
    while c <= maxlen:
        with open("%s-%s.csv" % (os.path.splitext(basename)[0],c+1) ,'a') as target:
            print("Percentage: %s" % ( float((c*userlen)/filelen*100)))
            if os.stat(target.name).st_size == 0:
                target.write("%s" % (header))
            i=0
            while i <= userlen:
                target.write(SOURCE_FILE.readline())
                i+=1
        c+=1
end = time.time()
print("Time elapsed: %ss" % (end-start))
