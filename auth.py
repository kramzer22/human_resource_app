from CTkMessagebox import CTkMessagebox

from helpers.services import Services
from module.util_module import DisplayFunctions

from view.login_form import LoginForm
from view.registration_form import RegistrationForm

from components.notification import Notification

from controller.auth_controller import AuthController
class Auth:
  
  def __init__(self, ctk, master):   
    self._master = master
    self._services = Services()
    
    self._auth_cotroller = AuthController(self)
    # self._display = DisplayFunctions()
    
    self._root = ctk.CTk()
    
    # self.__x_pos, self.__y_pos = self.__display.centerposition(self.__app_width, self.__app_height, self.__root)
    
    self._root.title('(SA)Simple Applicant - Login')
    self._root.resizable(width=False, height=False)
    
    self._login_form = LoginForm(master=self._root, parent=self, padx=30) 
    # self.__loginform.grid(row=0, column=0, padx=0, pady=0, sticky='nswe')
    
    self._registration_form = RegistrationForm(master=self._root, parent=self, padx=30)
    
    self._root.grid_columnconfigure(0, weight=1)
    self._root.grid_rowconfigure(0, weight=1)
    
    self.switch_to_login_form()
    
  def run(self):
    # self.__root.geometry(f'+{self.__x_pos}+{self.__y_pos}')
    self._root.mainloop()
    
  def disable_frames(self):
    self._registration_form.disable()
    
  def enable_frames(self):
    self._registration_form.enable()
    
  def messagebox(self, title, message, option1, option2=None, icon=None):
    msg = None
    if not option2:
      msg = CTkMessagebox(master=self._root, title=title, message=message, icon=icon, option_1=option1, button_height=40, button_width=80, topmost=False)
    else:
      msg = CTkMessagebox(master=self._root, title=title, icon=icon, message=message, option_1=option1, option_2=option2, button_height=40, button_width=80, topmost=False)    
    return msg.get()
    
  def switch_to_registration_form(self):
    self.clear_registration_form()
    self.remove_frames()
    self.display_registration_frame()
    self.resize_frame(self._auth_cotroller.get_registration_formsize())
    
  def switch_to_login_form(self):
    self.remove_frames()
    self.display_login_frame()
    self.resize_frame(self._auth_cotroller.get_login_formsize())
    
  def display_registration_frame(self):
    self._root.title('(SA)Simple Applicant - Registration')
    self._registration_form.grid(row=0, column=0, padx=0, pady=0, sticky='nswe')
    
  def clear_registration_form(self):
    self._registration_form.set_userdata_to_default()
    self._registration_form.clear_form()
    
  def display_login_frame(self):
    self._root.title('(SA)Simple Applicant - Login')
    self._login_form.grid(row=0, column=0, padx=0, pady=0, sticky='nswe')
  
  # Remove frame in use on auth window
  def remove_frames(self) -> None:
      if self._registration_form.grid_info() != {}:
        self._registration_form.grid_forget()
      if self._login_form.grid_info() != {}:
        self._login_form.grid_forget()  
    
  def resize_frame(self, size) -> None:
    self._root.geometry(f'{size['width']}x{size['height']}')
    
  def on_login(self):
    self._master.open_app()
    
  def close(self):
    try:
        if self._root.winfo_exists():
            self._root.destroy()
    except Exception as e:
        print(f"Error closing window: {e}")
    
  def hide_window(self):
    self._root.withdraw()
    
    
  
    
    