from module.main_config import MainConfig as main_config

class AuthController:
  def __init__(self, view):

    self._auth_view = view 
    
  def get_registration_formsize(self):
    return main_config.get_registration_size()
    
  def get_login_formsize(self):
    return main_config.get_login_size()
    