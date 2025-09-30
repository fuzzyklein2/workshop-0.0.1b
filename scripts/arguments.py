
from argparse import ArgumentParser as AP

from tools import *

def get_args(p:Path|str)->list[list[list|dict]]|None:
    """ Look for arguments in a CSV.
    """
    if type(p) is str:
        p = Path(p)
    df = pd.read_csv(p).fillna('')
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


def parse_arguments(arg_file:Path|str,
                    program_name:str,
                    program_version:str,
                    description:str,
                    epilog:str):
    STD_OPTS = get_args(arg_file)
    STD_OPTS.append([["-V", "--version"],
                     {"action": "version",
                      "version": f"{program_name} {program_version}",
                      "help": "Display the program name and version, then exit."}])
    

    ap = AP(prog=program_name, description=description, epilog=epilog)
    for option in STD_OPTS:
        ap.add_argument(*option[0], **option[1])

    return ap.parse_args(sys.argv[1:])
                     
