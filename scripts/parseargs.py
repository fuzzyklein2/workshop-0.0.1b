#!/usr/bin/env python3

# from argparse import ArgumentParser as AP
# from enum import auto, Enum
# from glob import glob
# import logging
# import os
# from pathlib import Path
# from pprint import pformat
# from subprocess import run
# import sys

from argparse import ArgumentParser as AP

from ws import *

def get_args():
    """ Look for arguments in a CSV.
    """
    df = pd.read_csv(WORKSHOP_DATA_DIR / 'data/std_opts.csv').fillna('')
    retval = list()
    # for each row
    for i in range(len(df)):
        L = list()
        L2 = list()
        
        SHORT = df.at[i, 'short']
        if SHORT:
            L2.append(SHORT)
        LONG = df.at[i, 'long']
        if LONG:
            L2.append(LONG)
        L.append(L2)
        D = dict()
    
        for c in df:
            if not c in {'short', 'long'}:
                value = df.at[i, c]
                if value:
                    D[c] = value
        L.append(D)
        retval.append(L)
    return retval

STD_OPTS = get_args()
STD_OPTS.append([["-V", "--version"],
                 {"action": "version",
                  "version": f"{PROGRAM} {VERSION}",
                  "help": "Display the program name and version, then exit."}])

def parse_arguments():
    STD_OPTS = get_args()
    STD_OPTS.append([["-V", "--version"],
                     {"action": "version",
                      "version": f"{PROGRAM} {VERSION}",
                      "help": "Display the program name and version, then exit."}])
    

    ap = AP(prog=PROGRAM, description=DESCRIPTION, epilog=EPILOG)
    for option in STD_OPTS:
        ap.add_argument(*option[0], **option[1])

    return ap.parse_args(sys.argv[1:])
                     
