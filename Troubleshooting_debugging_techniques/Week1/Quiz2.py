# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 21:42:48 2021

@author: yhame
"""

import re
def compare_strings(string1, string2):
  #Convert both strings to lowercase
  #and remove leading and trailing blanks
  string1 = string1.lower().strip()
  string2 = string2.lower().strip()

  #Ignore punctuation
  punctuation = r"[.?!,;:']"
  string1 = re.sub(punctuation, "", string1)
  string2 = re.sub(punctuation, "", string2)

  #DEBUG CODE GOES HERE
  #print(___)

  return string1 == string2
def main():
    output = compare_strings("Have a Great Day!", "Have a great day?")  # True
    #print(compare_strings("It's raining again.", "its raining, again"))  # True
    #print(compare_strings("Learn to count: 1, 2, 3.", "Learn to count: one, two, three."))  # False
    #print(compare_strings("They found some body.", "They found somebody."))  # False
    return print(output)
    import matplotlib.pyplot as plt
#    import matplotlib as mpl
    import numpy as np

    x = np.linspace(0, 20, 100)
    plt.plot(x, np.sin(x))
    plt.grid()
    plt.show()
if __name__=="__main__":
    main()