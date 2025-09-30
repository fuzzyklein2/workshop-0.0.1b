#!/usr/bin/env python3

"""
@file ignition.py
@version 1.2.3
@brief Startup module for simple Python scripts.

This module:

    * Parses arguments.
    * Sets up logging.
    * Imports config files.

    For more information, see:
    https://github.com/fuzzyklein2/workshop-0.0.1b
"""

# from enum import auto, Enum
# from glob import glob
# import logging
# import os
# from pathlib import Path
# from pprint import pformat
# from subprocess import run
# import sys

from tools import *

# ap = AP(prog=PROGRAM, description=DESCRIPTION, epilog=EPILOG)
# for option in STD_OPTS:
#     ap.add_argument(*option[0], **option[1])

# ARGS = ap.parse_args(sys.argv[1:])
                     
# if __debug__:
#     print(f'{ARGS.debug=}')
#     print(f'{ARGS.verbose=}')

DEBUG = bool({'-d', '--debug'}.intersection(sys.argv))
# VERBOSE = ARGS.verbose
# WARNINGS = ARGS.warnings
# TESTING = ARGS.testing

VERBOSE = bool({'-v', '--verbose'}.intersection(sys.argv))
WARNINGS = bool({'-w', '--warnings'}.intersection(sys.argv))
TESTING = bool({'-t', '--test'}.intersection(sys.argv))

if VERBOSE:
    print(f"{WARNING_PICT}{color_str('yellow', "WARNING!")} {color_str('green', PROGRAM)} is under construction!{CONSTRUCTION_PICT}")


# LOGFILE = None
# if not LOGFILE:
#     LOGFILE = f'logs/{PROGRAM}.log'
# LOGFILE = Path(LOGFILE)

# LOG_PICTS = { logging.DEBUG: DEBUG_PICT,
#               logging.INFO: INFO_PICT,
#               logging.WARNING: WARNING_PICT,
#               logging.ERROR: ERROR_PICT,
#               logging.CRITICAL: CRITICAL_PICT
#             }

# # if not LOGFILE.exists():
# #     LOGFILE.parent.mkdir(parents=True, exist_ok=True)
# #     LOGFILE.touch()


# if DEBUG:
#     level = logging.DEBUG
# elif VERBOSE:
#     level = logging.INFO
# elif WARNINGS or TESTING:
#     level = logging.WARNING
# else:
#     level = logging.ERROR

# if LOGFILE.exists():
#     LOGFILE.write_text('')
# LOGFILE.parent.mkdir(parents=True, exist_ok=True)

# # # Determine logging level
# # level = logging.DEBUG  # or INFO/WARNING depending on your flags

# # Create logger
# logger = logging.getLogger()
# logger.setLevel(level)

# # Formatter
# formatter = logging.Formatter('%(message)s')
# # formatter = logging.Formatter(f'{LOG_PICTS

# # Console handler
# console_handler = logging.StreamHandler(sys.stderr)
# console_handler.setFormatter(formatter)
# logger.addHandler(console_handler)

# # File handler
# file_handler = logging.FileHandler(LOGFILE)
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)

# if VERBOSE:
#     print(f"{GEAR_PICT}Logging configuration complete.")
#     print(f'{LOG_PICT}Log file: {LOGFILE.resolve()}')

# def log(level, message):
#     if NEWLINE in message:
#         logging.log(level, '')
#     logging.log(level, f"{LOG_PICTS[level]}{message}")
#     # if NEWLINE in message:
#     #     logging.log(level, '')

# def debug(message):
#     log(logging.DEBUG, message)

# def info(message):
#     log(logging.INFO, message)

# def warn(message):
#     log(logging.WARNING, message)

# def error(message):
#     log(logging.ERROR, message)

# def stop(message):
#     log(logging.CRITICAL, message)
#     if RUNNING_CLI:
#         exit(1)

# info(f'Workshop data directory: {WORKSHOP_DATA_DIR}')
# info(f'Backup directory: {BACKUP}')