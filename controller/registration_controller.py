from model.user import User

from helpers.registration_helper import RegistrationChecker as regcheck
from helpers.registration_services import RegistrationServices as regservices

class RegistrationController:
  def __init__(self, view):
    self._registration_view = view
    
    self._user = User()
    
  def set_userdata_to_default(self):
    self._user.clear()
    
  def set_user(self, event):
    self._user.username = self._registration_view.user
    
    is_valid, note = regcheck.check_username_entry(self._user.username)
    self._user.is_valid_user = is_valid
    self._registration_view.set_user_note(note)
    
  def set_email(self, event):
    self._user.email = self._registration_view.email
    
    is_valid, note = regcheck.check_email_entry(self._user.email)
    self._user.is_valid_email = is_valid
    self._registration_view.set_email_note(note)
    
  def set_mobile(self, event):
    self._user.mobile = self._registration_view.mobile
    
    is_valid, note = regcheck.check_mobile_entry(self._user.mobile)
    self._user._is_valid_mobile = is_valid
    self._registration_view.set_mobile_note(note)
    
  def set_password(self, event):
    self._user.password = self._registration_view.password
    repassword = self._registration_view.repassword
    
    is_valid, note = regcheck.check_password_entry(self._user.password, repassword)
    self._user._is_valid_password = is_valid
    self._registration_view.set_password_note(note)
    
  def set_repassword(self, event):
    repassword = self._registration_view.repassword
    password = self._registration_view.password
    
    is_valid, note = regcheck.check_password_entry(password, repassword)
    self._user._is_valid_password = is_valid
    self._registration_view.set_password_note(note)
    
  def register_user(self):
    if regcheck.check_registration_flags(self._user.flags()):
      self._registration_view.disable()
         
      is_completed, err = regservices.save_user(self._user)
      
      if is_completed == False:
        if err['field'] == 'username':
          # print(f'{err['message']}: field={err['field']} - value={err['value']}')
          self._registration_view.set_user_note('Username is already taken.')
          self._registration_view.user_focus()
        elif err['field'] == 'email':
          self._registration_view.set_email_note('Email is already registered.')
          self._registration_view.email_focus()
        elif err['field'] == 'mobile':
          self._registration_view.set_mobile_note('Mobile is already registered.')
          self._registration_view.password_focus()
        else:
          self._registration_view.set_user_note('Internal error problem.')
          
        self._registration_view.enable()
      else:
        self._registration_view.clear_form()
        self._user.clear()
        self._registration_view.notification("Registration comlete", "Registered  account can now proceed to login. Proceed to login?", 1, self.notification_registration_choice) 
    else:
      print('bad')
      
  def notification_registration_choice(self, choice):
    if choice == 'yes':
      self._registration_view.switch_to_login_form()
      
    self._registration_view.enable()
    