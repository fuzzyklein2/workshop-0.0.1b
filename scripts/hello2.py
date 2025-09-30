#!/usr/bin/env python3

#!/usr/bin/env python3

"""
@file hello2.py
@version 0.0.1c
@brief Example GTK4 app with logging.

https://github.com/fuzzyklein2/workshop-0.0.1b.git
"""

import sys
import logging
import argparse
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GLib

from ignition import *

# ------------------------
# 3. Define GTK Application
# ------------------------
class MyApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.example.MyApp")

    def do_activate(self):
        info("Application activated")
        win = Gtk.ApplicationWindow(application=self)
        win.set_title("GTK4 App Template")
        win.set_default_size(400, 200)
        win.present()

# ------------------------
# 4. Run the application
# ------------------------
if __name__ == "__main__":
    app = MyApplication()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)
