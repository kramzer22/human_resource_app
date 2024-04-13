import customtkinter as ctk

from CTkMessagebox import CTkMessagebox

from helpers.services import Services
from module.util_module import DisplayFunctions

from view.login_form import LoginForm
from view.registration_form import RegistrationForm

from components.notification import Notification

from controller.auth_controller import AuthController
class Auth(ctk.CTkToplevel):
  def __init__(self, master):
    self._master = master
    self._auth_cotroller = AuthController(self)
    
    super().__init__(master)   
    self._services = Services()
    # self._display = DisplayFunctions()
    
    # self.__x_pos, self.__y_pos = self.__display.centerposition(self.__app_width, self.__app_height, self.__root)
    
    self.title('(SA)Simple Applicant - Login')
    self.resizable(width=False, height=False)
    
    self.grid_columnconfigure(0, weight=1)
    self.grid_rowconfigure(0, weight=1)
    
    self._login_form = LoginForm(master=self, padx=30) 
    # self.__loginform.grid(row=0, column=0, padx=0, pady=0, sticky='nswe')
    
    self._registration_form = RegistrationForm(master=self, padx=30)
    
    self.switch_to_login_form()
    
    # initialized handlers goes here

    
  def disable_frames(self):
    self._registration_form.disable()
    
  def enable_frames(self):
    self._registration_form.enable()
    
  def messagebox(self, title, message, option1, option2=None, icon=None):
    msg = None
    if not option2:
      msg = CTkMessagebox(master=self, title=title, message=message, icon=icon, option_1=option1, button_height=40, button_width=80)
    else:
      msg = CTkMessagebox(master=self, title=title, icon=icon, message=message, option_1=option1, option_2=option2, button_height=40, button_width=80)    
    return msg.get()
    
  def switch_to_registration_form(self):
    self.clear_registration_form()
    self.remove_frames()
    self.display_registration_frame()
    self.resize_app(self._auth_cotroller.get_registration_formsize())
    
  def switch_to_login_form(self):
    self.remove_frames()
    self.display_login_frame()
    self.resize_app(self._auth_cotroller.get_login_formsize())
    
  def display_registration_frame(self):
    self.title('(SA)Simple Applicant - Registration')
    self._registration_form.grid(row=0, column=0, padx=0, pady=0, sticky='nswe')
    
  def clear_registration_form(self):
    self._registration_form.set_userdata_to_default()
    self._registration_form.clear_form()
    
  def display_login_frame(self):
    self.title('(SA)Simple Applicant - Login')
    self._login_form.grid(row=0, column=0, padx=0, pady=0, sticky='nswe')
  
  # Remove frame in use on auth window
  def remove_frames(self) -> None:
      if self._registration_form.grid_info() != {}:
        self._registration_form.grid_forget()
      if self._login_form.grid_info() != {}:
        self._login_form.grid_forget()  
    
  def resize_app(self, size) -> None:
    self.geometry(f'{size['width']}x{size['height']}')
    
  def center_on_screen(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - self.winfo_reqwidth()) // 2
        y = (screen_height - self.winfo_reqheight()) // 2

        # Set the position of the window
        self.geometry(f"+{x}+{y}")
    
  def login(self):
    self._master.login()
    
  def on_closing(self, destroy_app) -> None:
    self.close(destroy_app)
    
  def destroy(self, destroy_app:bool=True) -> None:
    if destroy_app:
      super().destroy()
      self._master.destroy()
    else:
      super().destroy()
    
  def hide_window(self):
    self.withdraw()
    
  def show_window(self):
    self.deiconify()
    
    
  
    
    