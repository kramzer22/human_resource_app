from helpers.services import Services
from module.util_module import DisplayFunctions

from view.login_form import LoginForm
from view.registration_form import RegistrationForm

from controller.auth_controller import AuthController
class Auth:
  
  def __init__(self, ctk):
    
    self._services = Services()
    # self._display = DisplayFunctions()
    
    self._root = ctk.CTk()
    
    # self.__x_pos, self.__y_pos = self.__display.centerposition(self.__app_width, self.__app_height, self.__root)
    
    self._root.title('(SA)Simple Applicant - Login')
    self._root.resizable(width=False, height=False) 
    
    self._auth_cotroller = AuthController(auth_view=self)
    
    self._loginform = LoginForm(master=self._root, controller=self._auth_cotroller, padx=30) 
    # self.__loginform.grid(row=0, column=0, padx=0, pady=0, sticky='nswe')
    
    self._registrationform = RegistrationForm(master=self._root, controller=self._auth_cotroller, padx=30)
    
    self._root.grid_columnconfigure(0, weight=1)
    self._root.grid_rowconfigure(0, weight=1)
    
    # Add click event to form links
    self._loginform.enable_link_clickevent(self._registrationform)
    self._registrationform.enable_link_clickevent(self._loginform)
    
    self._auth_cotroller.switch_frame(self._loginform)
    
  def run(self):
    # self.__root.geometry(f'+{self.__x_pos}+{self.__y_pos}')
    self._root.mainloop()
    
  def display_frame(self, frame) -> None:
    frame.grid(row=0, column=0, padx=0, pady=0, sticky='nswe')
  
  # Remove frame in use on auth window
  def remove_frames(self) -> None:
      if self._registrationform.grid_info() != {}:
        self._registrationform.grid_forget()
      if self._loginform.grid_info() != {}:
        self._loginform.grid_forget()  
    
  def resize_frame(self, size) -> None:
    print(size)
    self._root.geometry(f'{size['width']}x{size['height']}')
    
    
    
  
    
    