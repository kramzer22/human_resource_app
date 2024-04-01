import customtkinter as ctk

from components.textinput import TextInput
from components.linkedlabel import LinkedLabel

class RegistrationForm(ctk.CTkFrame):
  def __init__(self, master, controller, pady=0, padx=0):
    super().__init__(master=master)
    
    self._NAME = 'REGISTRATION_FORM'
    
    self._controller = controller

    self._header = ctk.CTkLabel(master=self, text="User registration", font=('Calibri', 24), anchor='w')
    self._header.grid(row=0, column=0, pady=10, padx=padx, sticky='we')
    
    self._entry_user = TextInput(master=self, name='USER', label='User name', require=True)
    self._entry_user.grid(row=1, column=0, pady=10, padx=padx, sticky='we')
    self._entry_user.on_text_changed(self._controller.set_user)
    
    self._entry_email = TextInput(master=self, name='EMAIL', label='Email', require=True)
    self._entry_email.grid(row=2, column=0, pady=10, padx=padx, sticky='we')
    self._entry_email.on_text_changed(self._controller.set_email)
    
    self._entry_mobile = TextInput(master=self, name='MOBILE', label='Mobile number', require=False)
    self._entry_mobile.grid(row=3, column=0, pady=10, padx=padx, sticky='we')
    self._entry_mobile.on_text_changed(self._controller.set_mobile)
    
    self._entry_password = TextInput(master=self, name='PASSWORD', label='Password', require=True)
    self._entry_password.grid(row=4, column=0, pady=10, padx=padx, sticky='we')
    self._entry_password.add_hide_event()
    
    self._entry_repassword = TextInput(master=self, label='Re password', require=True)
    self._entry_repassword.grid(row=5, column=0, pady=10, padx=padx, sticky='we')
    self._entry_repassword.add_hide_event()
    
    self._entry_password.on_text_changed(self._controller.set_password, self._entry_repassword)
    self._entry_repassword.on_text_changed(self._controller.set_repassword, self._entry_password)
    
    self._link_login = LinkedLabel(master=self, text="Already a member? Click here to login", anchor='e')
    self._link_login.grid(row=6, column=0, pady=10, padx=padx, sticky='e')
    
    self._save = ctk.CTkButton(master=self, text='Register', font=('Calibri', 16), width=80, height=40, command=lambda: self._controller.print_user())
    self._save.grid(row=7, column=0, pady=10, padx=0)
    
    self.grid_columnconfigure(0, weight=1)
    
  def enable_link_clickevent(self, frame) -> None:
    self._link_login.click(self._controller.switch_frame, frame)
    
  @property
  def name(self):
    return self._NAME
  
  @property
  def user(self):
    return self._entry_user.text
  
  @property
  def email(self):
    return self._entry_email.text
  
  @property
  def mobile(self):
    return self._entry_mobile.text
  
  @property
  def password(self):
    return self._entry_password.text
  
  @property
  def user(self):
    return self._entry_repassword.text
