"""
- The  dir  function returns a list of the names of the attributes and methods of an object. 
- The list comprehension  [attr for attr in dir(obj)]  generates a list of all the available attributes and methods of the given object. 
- The  sorted  function sorts the list alphabetically. 
- The function returns the sorted list. 
"""

def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return sorted([attr for attr in dir(obj)])