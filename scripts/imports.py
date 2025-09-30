#!/usr/bin/env python3

"""
@file imports.py
@version 0.0.1b
@brief Import modules from the system and any required packages.

For more information, see:

    [GitHub](https://github.com/fuzzyklein2/workshop-0.0.1b)
"""
import ast
from collections import namedtuple, OrderedDict
from enum import auto, Enum
from functools import partial, singledispatch
from glob import glob
from io import StringIO
import json
import logging
import os
from pathlib import Path
from pprint import pformat
import shutil
from subprocess import run
import sys

import pandas as pd
from rich.color import Color
from rich.console import Console