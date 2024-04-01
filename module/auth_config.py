class AuthConfig:
  
  _LOGIN_SIZE = {'width':400, 'height': 360}
  _REGISTRATION_SIZE = {'width':400, 'height': 620}
  
  @staticmethod      
  def login_size():
    return AuthConfig._LOGIN_SIZE
  
  @staticmethod
  def registration_size():
    return AuthConfig._REGISTRATION_SIZE