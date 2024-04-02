from helpers.services import Services
from module.util_module import DisplayFunctions

from view.login_form import LoginForm
from view.registration_form import RegistrationForm

from controller.auth_controller import AuthController
from controller.registration_controller import RegistrationController
class Auth:
  
  def __init__(self, ctk):
    
    self._services = Services()
    self._user_reg_control = RegistrationController(self)
    self._auth_cotroller = AuthController(self, self._user_reg_control)
    # self._display = DisplayFunctions()
    
    self._root = ctk.CTk()
    
    # self.__x_pos, self.__y_pos = self.__display.centerposition(self.__app_width, self.__app_height, self.__root)
    
    self._root.title('(SA)Simple Applicant - Login')
    self._root.resizable(width=False, height=False)
    
    self._loginform = LoginForm(master=self._root, auth_controller=self._auth_cotroller, padx=30) 
    # self.__loginform.grid(row=0, column=0, padx=0, pady=0, sticky='nswe')
    
    self._registrationform = RegistrationForm(master=self._root, reg_controller=self._user_reg_control, auth_controller=self._auth_cotroller, padx=30)
    
    self._root.grid_columnconfigure(0, weight=1)
    self._root.grid_rowconfigure(0, weight=1)
    
    self._auth_cotroller.got_to_login_form()
    
  def run(self):
    # self.__root.geometry(f'+{self.__x_pos}+{self.__y_pos}')
    self._root.mainloop()
    
  def display_registration_frame(self):
    self._root.title('(SA)Simple Applicant - Registration')
    self._registrationform.grid(row=0, column=0, padx=0, pady=0, sticky='nswe')
    
  def clear_registration_form(self):
    self._registrationform.clear_form()
    
  def display_Login_frame(self):
    self._root.title('(SA)Simple Applicant - Login')
    self._loginform.grid(row=0, column=0, padx=0, pady=0, sticky='nswe')
  
  # Remove frame in use on auth window
  def remove_frames(self) -> None:
      if self._registrationform.grid_info() != {}:
        self._registrationform.grid_forget()
      if self._loginform.grid_info() != {}:
        self._loginform.grid_forget()  
    
  def resize_frame(self, size) -> None:
    self._root.geometry(f'{size['width']}x{size['height']}')
    
    
    
  
    
    