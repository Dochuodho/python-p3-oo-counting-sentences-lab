#!/usr/bin/env python3

class MyString:
  def __init__(self, value=0):
    self._value = value

  def get_value(self):
    return self._value
  
  def set_value(self, value):
    if type(value)==str:
      print(f"{value}")
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return True if self._value.endswith(".") else False
  
  def is_question(self):
    return True if self._value.endswith("?") else False
  
  def is_exclamation(self):
    return True if self._value.endswith("!") else False
  
  
  

    

  value = property(get_value, set_value)

  pass
