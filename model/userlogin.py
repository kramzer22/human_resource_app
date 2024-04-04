from typing import List

class UserLogin:
  def __init__(self) -> None:
    self._username = ''
    self._repassword = ''
    
    self._is_valid_username = False
    self._is_valid_password = False
    
  def clear(self):
    self._username = ''
    self._password = ''
    
    self._is_valid_username = False
    self._is_valid_password = False
    
  def flags(self) -> List[bool]:
    flags = [
      self._is_valid_username,
      self.is_valid_password
      ]
    
    return flags
    
  @property
  def username(self):
    return self._username
  
  @username.setter
  def username(self, value):
    self._username = value
    
  @property
  def is_valid_user(self):
    return self._is_valid_username
  
  @is_valid_user.setter
  def is_valid_user(self, value):
    self._is_valid_username = value 
    
  @property
  def password(self):
    return self._password
  
  @password.setter
  def password(self, value):
    self._password = value
    
  @property
  def is_valid_password(self):
    return self._is_valid_password
  
  @is_valid_password.setter
  def is_valid_password(self, value):
    self._is_valid_username = value 