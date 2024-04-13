from module.main_config import MainConfig as main_config

class AppController:
  def __init__(self, view:any) -> None:
    self._app_view = view 
    
  def get_app_formsize(self) -> dict:
    return main_config.get_app_size()
  
  def initialize_app(self) -> None:
    self._app_view.hide()
    self._app_view.open_auth_window()
    self._app_view.run()
    
  def open_auth_window(self) -> None:
    self._app_view.open_auth_window()
    
  def login(self):
    self._app_view.show()
    
    