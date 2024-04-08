import asyncio

from CTkMessagebox import CTkMessagebox

from model.userlogin import UserLogin

from helpers.login_helper import LoginHelper as logincheck
from helpers.login_services import LoginServices as loginservices

class LoginController:
  def __init__(self, view):
    self._login_view = view
    self._user_login = UserLogin()
    
    self._login_services = loginservices()
    
    self._initialize_result: str
    
  def set_userlogin_to_default(self):
    self._user_login.clear()
    
  def set_user_handler(self, event):
    self._user_login.username = self._login_view.user
    
    is_valid, note = logincheck.check_username_entry(self._user_login.username)
    self._user_login.is_valid_user = is_valid
    self._login_view.set_user_note(note)
    
  def set_password_handler(self, event):
    if event.keysym == 'Return':
      self.initialize_user_login()
    else:
      self._user_login.password = self._login_view.password
      
      is_valid, note = logincheck.check_password_entry(self._user_login.password)
      self._user_login._is_valid_password = is_valid
      self._login_view.set_password_note(note)
    
  def initialize_user_login(self) -> None:
    print(self._user_login.flags())
    self._login_view.disable()
    if logincheck.check_login_flags(self._user_login.flags()):    
      self._login_services.initialize_user_login(self._user_login, self.user_login) 
    else:
      self._login_view.enable()
      
  def user_login(self, result:bool, error_data:tuple|None) -> None:
    if result == False:
      if (error_data['field'] == 'username'):
        self._login_view.set_user_note(error_data['message'])
          
      self._login_view.enable()
    else:
      self._user_login.clear() 
      self._login_view.clear_form()
          
      msg_result = self._login_view.messagebox('Login successful', 'welcome!', 'Proceed')
        
      self._login_view.enable()       
      if msg_result == 'Proceed':
        self._login_view.login()
    