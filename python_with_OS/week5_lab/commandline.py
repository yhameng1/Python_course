# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 17:29:57 2021

@author: yhame
"""

import os
import sys

filename = sys.argv[1]
if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New file created\n")
else:
    print("Error, the file {} already exists!".format(filename))
    sys.exit(1)