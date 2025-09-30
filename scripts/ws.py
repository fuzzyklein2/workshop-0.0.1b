#!/usr/bin/env python3

"""
@file ws.py
@version 0.0.1b
@brief Establishes the Workshop file system.

This module:

    * Creates the directory `~/.workshop` if it doesn't exist.
    * Defines constant names for:

        - The data directory `~/.workshop`.

    For more information, see:
    https://github.com/fuzzyklein2/workshop-0.0.1b
"""

# import os
# from pathlib import Path

# from arguments import *
# from lumberjack import *

from constants import *

# WORKSHOP = Path(os.environ['WORKSHOP_DIRECTORY'])
if RUNNING_CLI:
    WORKSHOP = Path(__file__).resolve().parent.parent
elif RUNNING_IN_JUPYTER:
    try:
        import ipynbname
        nb_path = ipynbname.path()
        print(f"Notebook name: {nb_path.name}")
        print(f"Full path: {nb_path}")
    except FileNotFoundError:
        stop("Can't find the notebook name. Are you running this in a notebook?")
        exit(2)
    finally: # WORKSHOP = os.environ["WORKSHOP_DIRECTORY"]
        stop("Application directory can't be found! 😲")
        exit(3)

# debug(f'Application directory: {str(WORKSHOP)}')
# print(f'Workshop directory: {WORKSHOP}')
WORKSHOP_DATA_DIR = Path.home() / '.workshop'
print(f'Data directory: {WORKSHOP_DATA_DIR}')
if not WORKSHOP_DATA_DIR.exists():
    print("Data directory does not exist. Creating it now.")
    WORKSHOP_DATA_DIR.mkdir()

# WORKSHOP = Path('.').resolve()

BACKUP = WORKSHOP_DATA_DIR / 'backup'
if not BACKUP.exists():
    BACKUP.mkdir()

PROJECTS = WORKSHOP_DATA_DIR / 'projects.txt'
if not PROJECTS.exists():
    PROJECTS.touch()

DEFAULT_PKGS_FILE = WORKSHOP_DATA_DIR / 'etc/packages.txt'
if not DEFAULT_PKGS_FILE.exists():
    DEFAULT_PKGS_FILE.parent.mkdir(parents=True, exist_ok=True)
    DEFAULT_PKGS_FILE.touch(exist_ok=True)

CMD_LINE_ARGS_FILE = WORKSHOP_DATA_DIR / 'data/std_opts.csv'