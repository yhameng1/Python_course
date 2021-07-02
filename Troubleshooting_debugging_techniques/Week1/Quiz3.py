# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 08:21:33 2021

@author: yhame
"""
def find_item(list, item):
  """ The find_item function uses binary search to recursively locate an item in the list, returning True if found, False otherwise. Something is missing from this function. Can you spot what it is and fix it? Add debug lines where appropriate, to help narrow down the problem."""
  #Returns True if the item is in the list, False if not.
  if len(list) == 0:
    return False
  list.sort()
  #Is the item in the center of the list?
  middle = len(list)//2
  if list[middle] == item:
    return True

  #Is the item in the first half of the list? 
  if item < list[middle]:
    #Call the function with the first half of the list
    return find_item(list[:middle], item)
  else:
    #Call the function with the second half of the list
    return find_item(list[middle+1:], item)

  return False

def binary_search(list, key):
  """The binary_search function returns the position of key in the list if found, or -1 if not found. We want to make sure that it's working correctly, so we need to place debugging lines to let us know each time that the list is cut in half, whether we're on the left or the right. Nothing needs to be printed when the key has been located.   

For example, binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) first determines that the key, 3, is in the left half of the list, and prints "Checking the left side", then determines that it's in the right half of the new list and prints "Checking the right side", before returning the value of 2, which is the position of the key in the list.  

Add commands to the code, to print out "Checking the left side" or "Checking the right side", in the appropriate places."""

#Returns the position of key in the list if found, -1 otherwise.

#List must be sorted:
  list.sort()
  left = 0
  right = len(list) - 1

  while left <= right:
     middle = (left + right) // 2

     if list[middle] == key:
            return middle
     if list[middle] > key:
            print("Checking the left side")
            right = middle - 1
     if list[middle] < key:
            print("Checking the right side")
            left = middle + 1
  return -1 








def main():
    list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]

    print(find_item(list_of_names, "Alex")) # True
    print(find_item(list_of_names, "Andrew")) # False
    print(find_item(list_of_names, "Drew")) # True
    print(find_item(list_of_names, "Jared")) # False
    
    print(binary_search([10, 2, 9, 6, 7, 1, 5, 3, 4, 8], 1))
    """Should print 2 debug lines and the return value:
    Checking the left side
    Checking the left side
0
"""

    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
    """Should print no debug lines, as it's located immediately:
4
"""

    print(binary_search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 7))
    """Should print 3 debug lines and the return value:
Checking the right side
Checking the left side
Checking the right side
6
"""

    print(binary_search([1, 3, 5, 7, 9, 10, 2, 4, 6, 8], 10))
    """Should print 3 debug lines and the return value:
Checking the right side
Checking the right side
Checking the right side
9
"""
    
if __name__=="__main__":
    main()