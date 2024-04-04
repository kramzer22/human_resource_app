import re

from typing import List

from module.util_module import CheckerFunctions as cf

class LoginHelper:
  
  @staticmethod
  def check_username_entry(text):
    if len(text) <= 0:
      return False, ''
    elif not cf.checklen(text, 5):
      return False, 'Username must be at least 5 char long.'
    elif not cf.is_user_format(text):
      return False, 'Invalid format, must be alphanumerical.'
    else:
      if len(text) > 30:
        return False, 'Username must not exceed 30 char long'
      else:
        return True, ''
  
  @staticmethod 
  def check_password_entry(password):
    if len(password) <= 0:
      return False, ''
    else:
      return True, ''
    
  @staticmethod
  def check_login_flags(flags: List[bool]) -> bool:
    result = True
      
    for flag in flags:
      if flag == False:
        result = False
        break
          
    return result