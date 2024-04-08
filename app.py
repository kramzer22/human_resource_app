import customtkinter as ctk

from auth import Auth 

from module.fonts import *

from helpers.services import Services

from components.sidebar import SideBar

from view.applicant_form import ApplicationForm
from model.applicant import Applicant

from controller.applicant_controller import ApplicantController
from controller.app_controller import AppController

# from module.helper_module import DateFunctions 

class App(ctk.CTk):
  def __init__(self):
    # Initialized classes goes here
    self.__services = Services()  
    
    super().__init__()
    
    self._auth = None
    self._applicant_controller = ApplicantController(self)
    self._app_controller = AppController(self)
    
    # CTk initialization goes here 
    self.title('(SA)Simple Applicant App v0.1')
    self.resizable(width=False, height=False)
    
    self.grid_columnconfigure(0, minsize=100)
    self.grid_columnconfigure(1, weight=1)
    self.grid_rowconfigure(0, weight=1)
    
    self._sidebar = SideBar(master=self, font_family=NAVIGATION_BAR_FONT_FAMILY, font_size=NAVIGATION_BAR_FONT_SIZE, list_height=60)
    self._sidebar.grid(row=0, column=0, padx=(0,2), pady=0, sticky='nswe')

    self._applicant = Applicant()
    self._application_form = ApplicationForm(self)
    self._application_form.grid(row=0, column=1, padx=0, pady=0, sticky='nswe')
    
    self.resize_app()
    
    # initialized handlers goes here
    self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
  def open_app(self): 
    self._app_controller.initialize_app()
    
  def run(self):
    self.set_form_commands()
    self.mainloop()
    
  def hide(self):
    self.withdraw()
    
  def show_auth_window(self):
    if self._auth is None or not self._auth.winfo_exists():
      self._auth = Auth(self)
      
  def destroy_auth_window(self):
    if self._auth or self._auth.winfo_exists():
      self._auth.close(False)
  
  def show(self):
    self.deiconify()
    
  def login(self):
    self._app_controller.login()
  
  def set_form_commands(self):
    pass
    # self._application_form.set_save_command(self.save_applicant)
    
  def testbackend(self):
    self.__services.test_connection()
    
  def save_applicant(self):
    applicant_form = self._application_form.get_applicant()
    self._applicant_controller.save_applicant(self.__applicant, applicant_form)
     
  def resize_app(self) -> None:
    size = self._app_controller.get_app_formsize()
    self.geometry(f'{size['width']}x{size['height']}')
    
  def on_closing(self) -> None:
    print('closing app...')
    self.destroy()