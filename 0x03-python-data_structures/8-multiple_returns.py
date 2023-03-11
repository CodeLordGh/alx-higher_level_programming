#!/usr/bin/python3
def multiple_returns(sentence):
  if sentence != '':
    first_character = sentence[0]
    string_length = len(sentence)
    return (string_length, first_character)
  else:
    return (0, None)
