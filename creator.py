import cx_Freeze
import sys
import os
import tkinter as tk
import datetime

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [cx_Freeze.Executable("main.py", base=base, icon='icon.ico')]

cx_Freeze.setup (
    name = "DeskClock",
    options = {"build.exe": {"packages":["tkinter"], "include_files":["icon.ico", "schedule.png"]}},
    version = "1.0.0",
    description = "School desktop clock",
    executables = executables
)