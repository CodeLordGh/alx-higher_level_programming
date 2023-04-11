#Importing the class from the module:
MyList = __import__("1-my_list").MyList

#Checking for module  docstring:
m = __import__("1-my_list").__doc__
len(m) > 1