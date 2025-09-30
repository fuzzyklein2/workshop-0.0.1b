#!/usr/bin/env python3

"""
@file tools.py
@version 0.0.1b
@brief Defines helper functions for scripts in the Workshop project..

This module:

    * Determines whether the script is running in Jupyter or CLI. [Deprecated.].
    * Defines a file system for new projects.
    * Imports config files.
    * Defines constants for doxygen tags in docstrings.
    * Looks for ~/.workshop/ and creates it if necessary.

    For more information, see:
    https://github.com/fuzzyklein2/workshop-0.0.1b
"""

# from argparse import ArgumentParser as AP
# from io import StringIO
# import os
# from pathlib import Path
# from subprocess import run
# import sys

# # from matplotlib import colors
# import pandas as pd
# from rich.color import Color
# from rich.console import Console

from constants import *

def pwd():
    print(f'Current working directory: {Path(os.curdir).resolve()}')

def color_str(color, s:str) -> str:
    if is_rich_color(color):
        buffer = StringIO()
        console = Console(file=buffer, color_system='truecolor', force_terminal=True)
        console.print(f"[{color}]{s}")
        return buffer.getvalue().strip()
    else:
        return f'[red]ERROR![end] Invalid color!'

def is_rich_color(name: str) -> bool:
    try:
        Color.parse(name)
        return True
    except Exception:
        return False

def yes_or_no(question:str, message=None)->bool:
    if input(f'{(message + NEWLINE) if message else ''}'
             + f'{ASK_PICT + question} (y/n): ').lower() \
            in AFFIRMATIVES:
        return True
    return False
        
run_cmd = partial(run, encoding='utf-8', capture_output=True, check=True)

@singledispatch
def chk_cmd(arg):
    error(f"Bad `run` argument: {arg}")
    return None

@chk_cmd.register
def _(L:list) -> int|None:
    p = run_cmd(L)
    if p.stderr:
        error(p.stderr)
    if p.stdout:
        info(p.stdout)
    if p.returncode:
        warn(f'{color_str('yellow', "WARNING")}! {L[1]} returned error code {p.returncode}')

@chk_cmd.register
def _(s:str) -> None:
    chk_cmd(s.split())