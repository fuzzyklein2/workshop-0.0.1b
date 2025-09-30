STD_OPTS = [[[],
  {"dest": "args",
   "metavar": "ARGUMENT",
   "nargs": "*",
   "help": "Files to be processed."
  }
 ],

      [["-d", "--debug"], {"action": "store_true", "dest": "debug", "help": "Set to run the program in DEBUG mode."}],
      [["-v", "--verbose"], {"action": "store_true", "dest": "verbose", "help": "Display extra information."}],
      [["-r", "--recursive"], {"action": "store_true", "dest": "recursive", "help": "Process files recursively."}],
      [["-t", "--testing"], {"action": "store_true", "dest": "testing", "help": "Run the `doctest`s in `main.py`"}],
      [["-s", "--follow"], {"action": "store_true", "dest": "follow", "help": "Follow symbolic links."}],
      [["-a", "--all"], {"action": "store_true", "dest": "all", "help": "Process hidden files."}],
      [["-c", "--config"], {"dest": "config", "help": "Specify a configuration file."}],
      [["-i", "--input"], {"dest": "input", "help": "Specify a file to be used as input."}],
      [["-o", "--output"], {"dest": "output", "help": "Specify a file to be used as output."}],
      [["-q", "--quiet"], {"action": "store_true", "dest": "quiet", "help": "Suppress screen output."}],
      [["-l", "--log"], {"dest": "log", "help": "Specify a log file."}],
      [["-w", "--warnings"], {"action": "store_true", "dest": "warnings", "help": "Display warning messages."}]
    ]

