from CTkMessagebox import CTkMessagebox

from model.userlogin import UserLogin

from helpers.login_helper import LoginHelper as logincheck
from helpers.login_services import LoginServices as loginservices

class LoginController:
  def __init__(self, view):
    self._login_view = view
    self._user_login = UserLogin()
    
  def set_userlogin_to_default(self):
    self._user_login.clear()
    
  def set_user(self, event):
    self._user_login.username = self._login_view.user
    
    is_valid, note = logincheck.check_username_entry(self._user_login.username)
    self._user_login.is_valid_user = is_valid
    self._login_view.set_user_note(note)
    
  def set_password(self, event):
    self._user_login.password = self._login_view.password
    
    is_valid, note = logincheck.check_password_entry(self._user_login.password)
    self._user_login._is_valid_password = is_valid
    self._login_view.set_password_note(note)
    
  def login_user(self):
    print(self._user_login.flags())
    
    if logincheck.check_login_flags(self._user_login.flags()):
      is_completed, err = loginservices.login_user(self._user_login)
      
      if is_completed == False:
        if (err['field'] == 'username'):
          self._login_view.set_user_note(err['message'])
      else:
        self._login_view.clear_form()
        self._user_login.clear()
        
        print('Welcome user')
        result = self._login_view.messagebox('Login successful', 'welcome!', 'Proceed')
  