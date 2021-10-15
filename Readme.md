# Project Name  
fhx_processing.py  

# Description  
fhx_processing.py is a program written in Python (ver 3.5) designed to processes a DeltaV FHX file and compile data to CSV files. Developed based on a FHX file exported from DeltaV version 14.3.  

# Installation  
Execution requires Python 3.x installation.  
Copy fhx_processing.py to a local directory.  
Create a folder named 'output' in the same directory as fhx_processing.py.  

# Usage  
Place a copy of a DeltaV FHX file in the same directory as fhx_processing.py and rename it 'DeltaV_In.fhx'.
To execute, used the command line to navigate to the folder containing fhx_processing.py and type fhx_processing.py at the prompt.  

When run, the program will generate six files (placed in the 'output' folder):
- _classless_modles.csv  
- _classless_modle_attrib.csv  
- _module_class.csv  
- _module_class_attrib.csv  
- _module_class_inst.csv  
- _module_class_inst_attrib.csv  

These output files will be overwrite each time the program is run.

# Contributing  
# Credits  
# License
GPLv3  
reference LICENCE file
