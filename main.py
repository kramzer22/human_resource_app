import customtkinter as ctk

from auth import Auth

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')
  
def open_auth(auth) -> None:
  auth.run()
  
if __name__ == '__main__':
  auth = Auth(ctk)
  open_auth(auth)