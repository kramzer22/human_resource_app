class MainConfig:
  
  _LOGIN_SIZE = {'width':480, 'height': 380}
  _REGISTRATION_SIZE = {'width':480, 'height': 680}
  
  _APP_SIZE = {'width': 1500, 'height': 740}
  
  @staticmethod      
  def get_login_size():
    return MainConfig._LOGIN_SIZE
  
  @staticmethod
  def get_registration_size():
    return MainConfig._REGISTRATION_SIZE
  
  @staticmethod
  def get_app_size(): 
    return MainConfig._APP_SIZE