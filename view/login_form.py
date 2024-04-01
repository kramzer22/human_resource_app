import customtkinter as ctk

from components.textinput import TextInput
from components.linkedlabel import LinkedLabel

class LoginForm(ctk.CTkFrame):
  
  def __init__(self, master, controller, pady=0, padx=0):
    super().__init__(master=master)
    self._NAME = 'LOGIN_FORM'
    
    self._controller = controller
    
    self._label_header = ctk.CTkLabel(master=self, text="Login", font=('Calibri', 24), anchor='w')
    self._label_header.grid(row=0, column=0, pady=10, padx=padx, sticky='we')
    
    self._entry_user = TextInput(master=self, label='User account')
    self._entry_user.grid(row=1, column=0, pady=10, padx=padx, sticky='we')
    
    self._entry_password = TextInput(master=self, label='Password')
    self._entry_password.grid(row=2, column=0, pady=10, padx=padx, sticky='we')
    self._entry_password.hide_text()
    
    self._link_register = LinkedLabel(master=self, text="Not yet a member? Click here to register", anchor='e')
    self._link_register.grid(row=3, column=0, pady=10, padx=padx, sticky='e')
    
    self._button_save = ctk.CTkButton(master=self, text='Proceed', font=('Calibri', 16), width=80, height=40)
    self._button_save.grid(row=4, column=0, pady=10, padx=0)
    
    self.grid_columnconfigure(0, weight=1)
    
  def enable_link_clickevent(self, frame) -> None:
    self._link_register.click(self._controller.switch_frame, frame)
    
  @property
  def name(self):
    return self._NAME
    
  