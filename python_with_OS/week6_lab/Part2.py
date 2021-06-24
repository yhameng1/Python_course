# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 16:42:10 2021

@author: yhame
"""

#!/usr/bin/env python3
import sys
import subprocess


f = open(sys.argv[1], "r")
for line in f.readlines():
 old_name = line.strip()
 new_name = old_name.replace("jane", "jdoe")
 subprocess.run(["mv", old_name, new_name])
f.close()