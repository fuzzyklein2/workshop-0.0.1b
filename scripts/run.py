#!/usr/bin/env python3

"""
@file run.py
@version 1.2.3
@brief Scan `projects/` for `bin/{PROJECT_NAME}' and run it.

This script scans the `projects` directory for a folder name matching the...

    For more information, see:
    https://github.com/fuzzyklein2/workshop-0.0.1b
"""

from ws import *

PROJECT_ARGS_START = 0
for i, a in enumerate(sys.argv[1:]):
    if a in {'-d', '--debug'}: DEBUG = True
    elif a in {'-v', '--verbose'}: VERBOSE = True
    else:
        PROJECT_NAME = a
        PROJECT_ARGS_START = i + 1
        if i > len(sys.argv):
            i = 0
        break

# PROJECT_NAME = ARGS.args[0]
debug(f"Project name: {PROJECT_NAME}")
PROJECT_DIR = Path(f'./projects/{PROJECT_NAME}')
debug(f"Project directory: {PROJECT_DIR}")
debug(f"System arguments:{pformat(sys.argv)}")
PROJECT_CONFIG_DIR = PROJECT_DIR / 'etc'
PROJECT_JSON = PROJECT_CONFIG_DIR / "project.json"
PROJECT_BUILD_DIR = PROJECT_DIR / 'bin'
CMD_LINE = [f"{PROJECT_BUILD_DIR}/{PROJECT_NAME.split('-')[0]}"]
if PROJECT_ARGS_START and not PROJECT_JSON.exists():
    CMD_LINE.extend(sys.argv[PROJECT_ARGS_START:])
result = run(CMD_LINE, encoding='utf-8', capture_output=True)
if result.stderr:
    print(result.stderr.strip())
print(str(result.stdout).strip())