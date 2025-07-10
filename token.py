#!/usr/bin/env python3

import sys

#create a new file with the arguments from the commandline
with open(sys.argv[1], 'w') as file:
    #write the next command line  argument to a file
    file.write(sys.argv[2])