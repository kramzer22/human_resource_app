from typing import List

class User:
  def __init__(self) -> None:
    self._username = ''
    self._email = ''
    self._mobile = ''
    self._password = ''
    self._repassword = ''
    
    self._is_valid_username = False
    self._is_valid_email = False
    self._is_valid_mobile = False
    self._is_valid_password = False
    
  def __str__(self):
    return f'User: {self._username}\nEmail: {self._email}\nMobile: {self._mobile}\nPassword: {self._password}'
  
  def clear(self):
    self._username = ''
    self._email = ''
    self._mobile = ''
    self._password = ''
    
    self._is_valid_username = False
    self._is_valid_email = False
    self._is_valid_mobile = False
    self._is_valid_password = False
    
  def flags(self) -> List[bool]:
    flags = [
      self._is_valid_username,
      self._is_valid_email,
      self._is_valid_mobile,
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
  def email(self):
    return self._email
  
  @email.setter
  def email(self, value):
    self._email = value
    
  @property
  def is_valid_email(self):
    return self._is_valid_email
  
  @is_valid_email.setter
  def is_valid_email(self, value):
    self._is_valid_email = value    
    
  @property
  def mobile(self):
    return self._mobile
  
  @mobile.setter
  def mobile(self, value):
    self._mobile = value
    
  @property
  def is_valid_mobile(self):
    return self._is_valid_mobile
  
  @is_valid_mobile.setter
  def is_valid_mobile(self, value):
    self._is_valid_mobile = value 
  
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
    
  @property
  def repassword(self):
    return self._repassword
  
  @repassword.setter
  def repassword(self, value):
    self._repassword = value
                                   
    