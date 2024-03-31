import customtkinter as ctk

from components.linkedlabel import LinkedLabel

class RegistrationForm(ctk.CTkFrame):
  def __init__(self, master):
    super().__init__(master=master)

    self.__header = ctk.CTkLabel(master=self, text="User registration", font=('Calibri', 24), anchor='w')
    self.__header.grid(row=0, column=0, pady=10, padx=10, sticky='we')
    
    self.__register = LinkedLabel(master=self, text="Already a member? Click here to login", anchor='e')
    self.__register.grid(row=3, column=0, pady=10, padx=10, sticky='e')
    
    self.grid_columnconfigure(0, weight=1)
    
  def set_switch_display_event(self, command) -> None:
    self.__register.click(command, 'login')
