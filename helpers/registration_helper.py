import re

from module.util_module import CheckerFunctions as cf

class RegistrationChecker:
      
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
      
    def check_email_entry(email):
      if len(email) <= 0:
        return False, ''
      elif not cf.is_email_format(email):
        return False, 'Invalid email format'
      else:
        return True, ''
      
    def check_mobile_entry(number):
      if len(number) <= 0:
        return True, ''
      elif not cf.is_mobile_format(number):
        return False, 'Invalid mobile number'
      else:
        return True, ''
      
    def check_password_entry(password, repassword):
      if len(password) <= 0:
        return False, ''
      elif len(password) in range(1, 6):
        return False, 'Password is too short'
      elif len(repassword) > 0 and password != repassword:
        return False, 'Password mismatch'
      else:
        return True, ''
      
    def check_repassword_entry(password, repassword):
      if len(password) <= 0:
        return False, ''
      elif len(repassword) > 0 and password != repassword:
        return False, 'Password mismatch'
      else:
        return True, ''
      
       