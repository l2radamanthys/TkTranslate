import sys
import os
from cx_Freeze import setup, Executable

path = '\\'.join(os.path.realpath(__file__).split('\\')[:-1])
print(path)
os.environ['TCL_LIBRARY'] = path + r'\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = path + r'\\tcl\\tk8.6'

base = None #d default x64
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [Executable('main.py', base=base)] 

setup(
    name='Tk Translate',
    options = { 
        "build_exe": {
            "packages":["tkinter"], 
            # "include_files": ["appicon.ico"]
        }
    },
    version = "0.0.3",
    description = "Herramienta de traduccion",
    executables = executables
)


