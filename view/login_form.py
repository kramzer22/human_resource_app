import customtkinter as ctk

from components.textinput import TextInput
from components.linkedlabel import LinkedLabel

from controller.login_controller import LoginController

class LoginForm(ctk.CTkFrame):
  
  def __init__(self, master, parent, pady=0, padx=0):
    super().__init__(master=master)
    self._NAME = 'LOGIN_FORM'
    
    self._parent = parent
    self._login_controller = LoginController(self)
    
    self._label_header = ctk.CTkLabel(master=self, text="Login", font=('Calibri', 24), anchor='w')
    self._label_header.grid(row=0, column=0, pady=10, padx=padx, sticky='we')
    
    self._entry_user = TextInput(master=self, label='User account')
    self._entry_user.grid(row=1, column=0, pady=10, padx=padx, sticky='we')
    self._entry_user.set_text_changed(self._login_controller.set_user)
    
    self._entry_password = TextInput(master=self, label='Password')
    self._entry_password.grid(row=2, column=0, pady=10, padx=padx, sticky='we')
    self._entry_password.set_text_changed(self._login_controller.set_password)
    self._entry_password.add_hide_event()
    
    self._link_register = LinkedLabel(master=self, text="Not yet a member? Click here to register", anchor='e')
    self._link_register.grid(row=3, column=0, pady=10, padx=padx, sticky='e')
    self._link_register.set_click_event(method=parent.switch_to_registration_form)
    
    self._button_save = ctk.CTkButton(master=self, text='Proceed', font=('Calibri', 16), width=80, height=40, command=self._login_controller.login_user)
    self._button_save.grid(row=4, column=0, pady=10, padx=0)
    
    self.grid_columnconfigure(0, weight=1)
    
  def clear_form(self):
    self.user = ''
    self.password = ''
    
    self.set_user_note('')
    self.set_password_note('')
    
  def messagebox(self, title, message, option1, option2=None):
    return self._parent.messagebox(title, message, option1, option2)
  
  def on_login(self):
    self._parent.on_login()
    
  @property
  def user(self):
    return self._entry_user.text
  
  @user.setter
  def user(self, value):
    self._entry_user.text = value
    
  def set_user_note(self, note):
    self._entry_user.set_note(note)
    
  @property
  def password(self):
    return self._entry_password.text
  
  @password.setter
  def password(self, value):
    self._entry_password.text = value
  
  def set_password_note(self, note):
    self._entry_password.set_note(note)
    
    
    
  