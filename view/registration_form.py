import customtkinter as ctk

from components.textinput import TextInput
from components.linkedlabel import LinkedLabel

from controller.registration_controller import RegistrationController

class RegistrationForm(ctk.CTkFrame):
  def __init__(self, master, pady=0, padx=0):
    self._master =  master
    self._reg_controller = RegistrationController(self)
    
    super().__init__(master=master)
    
    self._NAME = 'REGISTRATION_FORM'

    self._header = ctk.CTkLabel(master=self, text="User registration", font=('Calibri', 24), anchor='w')
    self._header.grid(row=0, column=0, pady=10, padx=padx, sticky='we')
    
    self._entry_user = TextInput(master=self, label='User name', require=True)
    self._entry_user.grid(row=1, column=0, pady=10, padx=padx, sticky='we')
    self._entry_user.attach_handler_to_keypress_event(handler=self._reg_controller.set_user)
    
    self._entry_email = TextInput(master=self, label='Email', require=True)
    self._entry_email.grid(row=2, column=0, pady=10, padx=padx, sticky='we')
    self._entry_email.attach_handler_to_keypress_event(handler=self._reg_controller.set_email)
    
    self._entry_mobile = TextInput(master=self, label='Mobile number', require=False)
    self._entry_mobile.grid(row=3, column=0, pady=10, padx=padx, sticky='we')
    self._entry_mobile.attach_handler_to_keypress_event(handler=self._reg_controller.set_mobile)
    
    self._entry_password = TextInput(master=self, label='Password', require=True)
    self._entry_password.grid(row=4, column=0, pady=10, padx=padx, sticky='we')
    self._entry_password.attach_handler_to_keypress_event(handler=self._reg_controller.set_password)
    self._entry_password.enable_entry_mask()
    
    self._entry_repassword = TextInput(master=self, label='Re password', require=True)
    self._entry_repassword.grid(row=5, column=0, pady=10, padx=padx, sticky='we')
    self._entry_repassword.attach_handler_to_keypress_event(handler=self._reg_controller.set_repassword)
    self._entry_repassword.enable_entry_mask()
    
    self._link_login = LinkedLabel(master=self, text="Already a member? Click here to login", anchor='e')
    self._link_login.grid(row=6, column=0, pady=10, padx=padx, sticky='e')
    self._link_login.attach_handler_to_click_event(handler=self.switch_to_login_form)
    
    self._save = ctk.CTkButton(master=self, text='Register', font=('Calibri', 16), width=80, height=40, command=self._reg_controller.register_user)
    self._save.grid(row=7, column=0, pady=10, padx=0)
    
    self.grid_columnconfigure(0, weight=1)
    
  def clear_form(self):
    self.user = ''
    self.email = ''
    self.mobile = ''
    self.password = ''
    self.repassword = ''
    
    self.set_user_note('')
    self.set_email_note('')
    self.set_mobile_note('')
    self.set_password_note('')
    
    self.user_focus()
    
  def disable(self):
    self._link_login.disable()
    self._save.configure(state='disabled')
    
  def enable(self):
    self._link_login.enable()
    self._save.configure(state='normal')
    
  def switch_to_login_form(self):
    self._master.switch_to_login_form()
    
  def messagebox(self, title, message, option1, option2=None):
    return self._master.messagebox(title, message, option1, option2)
    
  def set_userdata_to_default(self):
    self._reg_controller.set_userdata_to_default()
    
  def user_focus(self):
    self._entry_user.focus()
    
  def email_focus(self):
    self._entry_email.focus()
    
  def mobile_focus(self):
    self._entry_mobile.focus()
    
  def password_focus(self):
    self._entry_password.focus()
  
  def repassword_focus(self):
    self._entry_repassword.focus()
    
  @property
  def name(self):
    return self._NAME
  
  @property
  def user(self):
    return self._entry_user.text
  
  @user.setter
  def user(self, value):
    self._entry_user.text = value
  
  def set_user_note(self, note):
    self._entry_user.set_note(note)
  
  @property
  def email(self):
    return self._entry_email.text
  
  @email.setter
  def email(self, value):
    self._entry_email.text = value
  
  def set_email_note(self, note):
    self._entry_email.set_note(note)
  
  @property
  def mobile(self):
    return self._entry_mobile.text
  
  @mobile.setter
  def mobile(self, value):
    self._entry_mobile.text = value
  
  def set_mobile_note(self, note):
    self._entry_mobile.set_note(note)
  
  @property
  def password(self):
    return self._entry_password.text
  
  @password.setter
  def password(self, value):
    self._entry_password.text = value
  
  def set_password_note(self, note):
    self._entry_password.set_note(note)
  
  @property
  def repassword(self):
    return self._entry_repassword.text
  
  @repassword.setter
  def repassword(self, value):
    self._entry_repassword.text = value
