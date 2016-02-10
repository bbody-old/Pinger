from distutils.core import setup
import py2exe

# For py2exe, setting up an executable

setup(options = {
        "py2exe": {
            "dll_excludes": ["MSVCP90.dll"]
        }
    }, windows=['Pinger.py'])
