#!/usr/bin/env python3

"""
@file create.py
@version 0.0.1c
@brief Create a new Workshop project.

https://github.com/fuzzyklein2/workshop-0.0.1b.git
"""

import json
from pathlib import Path
import shutil

from arguments import *
from lumberjack import *
from ws import *

if __name__ == '__main__':
    
    ARGS = parse_arguments(CMD_LINE_ARGS_FILE,
                           PROGRAM, VERSION,
                           DESCRIPTION, EPILOG)

    logfile = ARGS.logfile if ARGS.log else WORKSHOP_DATA_DIR / 'logs' / f'{PROGRAM}.log'

    
    if DEBUG:
        level = logging.DEBUG
    elif VERBOSE:
        level = logging.INFO
    elif WARNINGS or TESTING:
        level = logging.WARNING
    else:
        level = logging.ERROR
    
    setuplog(logfile, level)
    
    info(f'Running {PROGRAM} {VERSION}')
    debug(f"""Command line arguments:
    {pformat(ARGS.args)}
    """)
    
    PROJECT_NAME = ARGS.args[0]
    info(f'Creating project {PROJECT_NAME}')

    PROJECTS_JSON = json.loads((WORKSHOP_DATA_DIR / 'data/projects.json').read_text())
    debug(f"""Projects:
{pformat(PROJECTS_JSON)}
""")
    
    PROJECT_DIR = Path(PROJECT_NAME)

    if PROJECT_NAME in PROJECTS_JSON.keys():
        if not yes_or_no(f'{ASK_PICT}Do you want to replace it?',
                     message=f'{STOP_PICT}Project ' + str(PROJECT_NAME) + ' already exists.'):
            stop('Execution cancelled.')
            exit(1)
        else:
            BACKUP_DEST = BACKUP / PROJECT_NAME
            info(f'Backing up project {PROJECT_NAME} to {str(BACKUP_DEST)}...')
            if BACKUP_DEST.exists():
                info(f'Removing previous backup: {str(BACKUP_DEST)}')
                shutil.rmtree(str(BACKUP_DEST))

            
            BACKUP_DEST.mkdir(parents=True, exist_ok=True)
            debug(f'Moving {PROJECT_DIR} to {BACKUP_DEST}')                
            # shutil.move(str(PROJECT_DIR), str(BACKUP_DEST))


    
    
    if PROJECT_DIR.exists():
        if not yes_or_no(f'{ASK_PICT}Do you wish to proceed?',
                     message=f'{STOP_PICT}Directory ' + str(PROJECT_DIR) + ' already exists.'):
            stop('Execution cancelled.')
            exit(1)
        else:
            BACKUP_DEST = BACKUP / PROJECT_NAME
            info(f'Backing up project {PROJECT_NAME} to {str(BACKUP_DEST)}...')
            if BACKUP_DEST.exists():
                info('Removing previous backup...')
                shutil.rmtree(str(BACKUP_DEST))
            shutil.move(str(PROJECT_DIR), str(BACKUP_DEST))
    
    info(f'Creating project directory: {str(PROJECT_DIR)}...')
    PROJECT_DIR.mkdir()
    for s in CPP_SUBDIRS:
        p = PROJECT_DIR / s
        info(f'Creating subdirectory: {str(p)}')
        p.mkdir()

    debug(f'Default `packages.txt`: {str(DEFAULT_PKGS_FILE)}')
    shutil.copy2(DEFAULT_PKGS_FILE, PROJECT_DIR / 'etc/packages.txt')