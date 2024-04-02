from helpers.registration_helper import RegistrationChecker as regcheck
from module.auth_config import AuthConfig as auth_config

from model.user import User

class AuthController:
  def __init__(self, auth_view, registration_controller):
    self._user = User()
    self._auth_view = auth_view   
    self._registration_controller = registration_controller
    
  def go_to_registration_form(self):
    self._registration_controller.set_userdata_to_default()
    
    self._auth_view.clear_registration_form()
    self._auth_view.remove_frames()
    self._auth_view.display_registration_frame()
    self._auth_view.resize_frame(auth_config.registration_size())
    
  def got_to_login_form(self):
    self._auth_view.remove_frames()
    self._auth_view.display_Login_frame()
    self._auth_view.resize_frame(auth_config.login_size())
    