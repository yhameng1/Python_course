# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 16:41:19 2021

@author: yhame
"""

#!/bin/bash
>oldFiles.txt
files=$(grep "jane" ../data/list.txt | cut -d ' ' -f 3)
for f in $files; do
 if [ -e $HOME$f ];then
    echo $HOME$f >> oldFiles.txt; 
 fi
 done