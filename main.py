import customtkinter as ctk

from auth import Auth
from app import App

ctk.set_appearance_mode('dark')

class Main:
  def __init__(self) -> None:
    self._auth = None
    self._app = None

  def open_auth(self) -> None:
    self._auth = Auth(ctk, self)
    self._auth.run()
    
  def open_app(self) -> None:
    self._auth.hide_window()
    self._app = App(self)
    self._app.run()
    
  def close(self):
    self._auth.close()
    
  
if __name__ == '__main__':
  main = Main()
  main.open_auth()