from helpers.services import Services
from module.helper_module import DisplayFunctions

from view.login_form import LoginForm
from view.registration_form import RegistrationForm

from controller.auth_controller import AuthController
class Auth:
  
  def __init__(self, ctk):
    self.__app_width = 400
    self.__app_height = 360
    self.__services = Services()
    self.__display = DisplayFunctions()
    
    self.__root = ctk.CTk()
    
    self.__x_pos, self.__y_pos = self.__display.centerposition(self.__app_width, self.__app_height, self.__root)
    
    self.__root.geometry(f'{self.__app_width}x{self.__app_height}')
    self.__root.title('(SA)Simple Applicant - Login')
    self.__root.resizable(width=False, height=False) 
    
    self.__loginform = LoginForm(master=self.__root)
    # self.__loginform.grid(row=0, column=0, padx=0, pady=0, sticky='nswe')
    
    
    self.__registrationform = RegistrationForm(master=self.__root)
    
    self.__root.grid_columnconfigure(0, weight=1)
    self.__root.grid_rowconfigure(0, weight=1)
    
    self.__auth_cotroller = AuthController(auth_view=self,frames=[self.__loginform, self.__registrationform])
    self.__loginform.set_switch_display_event(self.__auth_cotroller.switch_frame)
    self.__registrationform.set_switch_display_event(self.__auth_cotroller.switch_frame)
    
    self.display_frame(self.__loginform)
    
  def run(self):
    self.__root.geometry(f'+{self.__x_pos}+{self.__y_pos}')
    self.__root.mainloop()
    
  def display_frame(self, frame) -> None:
    frame.grid(row=0, column=0, padx=0, pady=0, sticky='nswe')
    
  def remove_frame(self, frame) -> None:
    frame.grid_forget()
    
  
    
    