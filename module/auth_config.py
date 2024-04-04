class AuthConfig:
  
  _LOGIN_SIZE = {'width':440, 'height': 380}
  _REGISTRATION_SIZE = {'width':440, 'height': 680}
  
  @staticmethod      
  def login_size():
    return AuthConfig._LOGIN_SIZE
  
  @staticmethod
  def registration_size():
    return AuthConfig._REGISTRATION_SIZE