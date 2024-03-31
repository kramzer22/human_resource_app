import customtkinter as ctk

from components.textinput import TextInput
from components.linkedlabel import LinkedLabel

class LoginForm(ctk.CTkFrame):
  
  def __init__(self, master):
    super().__init__(master=master)
    
    self.__header = ctk.CTkLabel(master=self, text="Login", font=('Calibri', 24), anchor='w')
    self.__header.grid(row=0, column=0, pady=10, padx=10, sticky='we')
    
    self.__entry_user = TextInput(master=self, label='User account')
    self.__entry_user.grid(row=1, column=0, pady=10, padx=10, sticky='we')
    
    self.__entry_password = TextInput(master=self, label='Password')
    self.__entry_password.grid(row=2, column=0, pady=10, padx=10, sticky='we')
    self.__entry_password.hide_text()
    
    self.__register = LinkedLabel(master=self, text="Click here to register", anchor='e')
    self.__register.grid(row=3, column=0, pady=10, padx=10, sticky='e')
    
    self.__save = ctk.CTkButton(master=self, text='Proceed', font=('Calibri', 16), width=80, height=40)
    self.__save.grid(row=4, column=0, pady=10, padx=0)
    
    self.grid_columnconfigure(0, weight=1)
    
  def set_switch_display_event(self, command) -> None:
    self.__register.click(command, 'registration')
    
  