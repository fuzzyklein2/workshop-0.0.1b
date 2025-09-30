#!/usr/bin/env python3

"""
@file constants.py
@version 0.0.1b
@brief Defines constant values.

This module:

    * Determines whether the script is running in Jupyter or CLI. [Deprecated.].
    * Defines a file system for new projects.
    * Imports config files.
    * Defines constants for doxygen tags in docstrings.
    * Looks for ~/.workshop/ and creates it if necessary.

    For more information, see:
    https://github.com/fuzzyklein2/workshop-0.0.1b
"""

from picts import *
from responses import *
from stdopts import STD_OPTS
from utils import *

NEWLINE = '\n'
HYPHEN = '-'

RUNNING_IN_JUPYTER = Path(sys.argv[0]).stem.startswith('ipykernel')
RUNNING_CLI = not RUNNING_IN_JUPYTER
NOTEBOOK = 'notebook'

FILE_TAG = '@file'
BRIEF_TAG = '@brief'
VERSION_TAG = '@version'

CPP_SUBDIRS = [
    'bin',
    'data',
    'etc',
    'img',
    'inc',
    'src'
]

PY_SUBDIRS = [
    
]


COLORS = {
    "black": "black",
    "white": "white",
    "red": "#CC0000",
    "blue": "#0000FF",
    "green": "#006600",
    "yellow": "#FFFF00",
    "orange": "#FF3300",
    "purple": "#CC0066",
    "peach": "#FF9933",
    "lavender": "#FF66CC",
    "sky_blue": "#66CCFF",
    "cyan": "#0099CC",
    "magenta": "#FF0066",
    "yellow_green": "#00FF00",
    "midnight_blue": "#003366",
    "brown": "#663300",
    "sienna": "#CC3300",
    "grey": "#757575",
}

if RUNNING_CLI: 
    MAIN_FILE = Path(sys.modules["__main__"].__file__)
    COMPONENTS = MAIN_FILE.stem.split('-')
elif RUNNING_IN_JUPYTER:
    MAIN_FILE = 'notebook'
    COMPONENTS = ['notebook']

# # WORKSHOP = Path(os.environ['WORKSHOP_DIRECTORY'])
# if RUNNING_CLI:
#     WORKSHOP = Path(__file__).resolve().parent.parent
# elif RUNNING_IN_JUPYTER:
#     try:
#         import ipynbname
#         nb_path = ipynbname.path()
#         print(f"Notebook name: {nb_path.name}")
#         print(f"Full path: {nb_path}")
#     except FileNotFoundError:
#         stop("Can't find the notebook name. Are you running this in a notebook?")
#         exit(2)
#     finally: WORKSHOP = os.environ["WORKSHOP_DIRECTORY"]
    



PROGRAM = COMPONENTS[0]
VERSION = None

DOCSTR = get_docstring_from_file(MAIN_FILE)
DOCSTR_MISSING = not bool(DOCSTR)
    

if DOCSTR_MISSING:
    VERSION = '1.0.0'
    DESCRIPTION = f'Python script: {MAIN_FILE}'
    EPILOG = 'https://github.com/fuzzyklein2/workshop-0.0.1b'
else:
    VERSION = remove_tag(grep(VERSION_TAG, DOCSTR)[0])
    DESCRIPTION = remove_tag(grep(BRIEF_TAG, DOCSTR)[0])
    EPILOG = DOCSTR[-1]

CWD = Path.cwd()