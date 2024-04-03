from module.auth_config import AuthConfig as auth_config

class AuthController:
  def __init__(self, view):

    self._auth_view = view 
    
  def get_registration_formsize(self):
    return auth_config.registration_size()
    
  def get_login_formsize(self):
    return auth_config.login_size()
    