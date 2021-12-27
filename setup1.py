import sys
import os
from cx_Freeze import setup, Executable

# Include the name of all folder or files in your project folder that is necessary for the project excluding your main flask file.

# If there are multiple files, you can add them into a folder and then specify the folder name.

# In place of main.py file add your main flask file name

includefiles = ['LPAs','template', 'static', 'test.py','contents.xlsx']

includes = [ 'jinja2' , 'jinja2.ext']


setup(

name='Sample Flask App',

version = '0.1',

description = 'Sample Flask App',

options = {'build_exe': {'include_files':includefiles, 'includes':includes}},

executables = [Executable('main.py')]

)