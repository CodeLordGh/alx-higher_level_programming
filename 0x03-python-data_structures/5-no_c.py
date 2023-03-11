#!/usr/bin/python3
def no_c(my_string):
  newstr = ''
  for char in my_string:
    if char != 'c' and char != 'C':
      newstr += char
  return newstr
# print(no_c("My name is Carol"))
# print(no_c("I am learning Python"))
 # Output
#My name isarl
#I am leaning Python
#CodeLordGh
