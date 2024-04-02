from model.user import User

from helpers.registration_helper import RegistrationChecker as regcheck
from helpers.registration_services import RegistrationServices as regservices

class RegistrationController:
  def __init__(self, view):
    self._view = view
    
    self._user = User()
    
  def set_userdata_to_default(self):
    self._user.clear()
    
  def set_user(self, event):
    self._user.username = self._view._registrationform.user
    
    is_valid, note = regcheck.check_username_entry(self._user.username)
    self._user.is_valid_user = is_valid
    self._view._registrationform.set_user_note(note)
    
  def set_email(self, event):
    self._user.email = self._view._registrationform.email
    
    is_valid, note = regcheck.check_email_entry(self._user.email)
    self._user.is_valid_email = is_valid
    self._view._registrationform.set_email_note(note)
    
  def set_mobile(self, event):
    self._user.mobile = self._view._registrationform.mobile
    
    is_valid, note = regcheck.check_mobile_entry(self._user.mobile)
    self._user._is_valid_mobile = is_valid
    self._view._registrationform.set_mobile_note(note)
    
  def set_password(self, event):
    self._user.password = self._view._registrationform.password
    repassword = self._view._registrationform.repassword
    
    is_valid, note = regcheck.check_password_entry(self._user.password, repassword)
    self._user._is_valid_password = is_valid
    self._view._registrationform.set_password_note(note)
    
  def set_repassword(self, event):
    repassword = self._view._registrationform.repassword
    password = self._view._registrationform.password
    
    is_valid, note = regcheck.check_password_entry(password, repassword)
    self._user._is_valid_password = is_valid
    self._view._registrationform.set_password_note(note)
    
  def register_user(self):
    print(self._user)
    print(self._user.flags())
    
    if regcheck.check_registration_flags(self._user.flags()):
      is_completed, err = regservices.save_user(self._user)
      
      if is_completed == False:
        if err['field'] == 'username':
          # print(f'{err['message']}: field={err['field']} - value={err['value']}')
          self._view._registrationform.set_user_note('Username is already taken.')
        elif err['field'] == 'email':
          self._view._registrationform.set_email_note('Email is already registered.')
      else:
        print('ok')
    else:
      print('bad')
    