import sys
from cx_Freeze import setup, Executable


# Dependencies are automatically detected, but it might need fine tuning.

build_exe_options = {"packages": ["re","tkinter"], "excludes": []}



setup(  name = "字典生成器",

        version = "0.2",

        description = "Auto dictionary Generator",

        options = {"build_exe": build_exe_options},

        executables = [Executable("vocabulary_manager.py")])
