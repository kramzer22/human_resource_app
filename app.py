from helpers.services import Services

from components.sidebar import SideBar

from view.applicant_form import ApplicationForm
from model.applicant import Applicant
from controller.applicant_controller import ApplicantController

# from module.helper_module import DateFunctions 

class App():
  def __init__(self, ctk):
    self.__services = Services()
    
    main_font = 'Roboto'
  
    self.__root = ctk.CTk()
    self.__root.geometry('1366x768')
    
    self.__sidebar = SideBar(master=self.__root, font_family='Roboto', font_size=16, list_height=70)
    self.__sidebar.grid(row=0, column=0, padx=(0,2), pady=0, sticky='nswe')

    self.__applicant = Applicant()
    self.__applicant_controller = ApplicantController()
    self.__application_form = ApplicationForm(master=self.__root)
    self.__application_form.grid(row=0, column=1, padx=0, pady=0, sticky='nswe')
  
    self.__root.grid_columnconfigure(0, minsize=100)
    self.__root.grid_columnconfigure(1, weight=1)
    self.__root.grid_rowconfigure(0, weight=1)
        
  def run(self): 
    self.testbackend() 
    self.set_form_commands()
    self.__root.mainloop()
    
  def set_form_commands(self):
    self.__application_form.set_save_command(self.save_applicant)
    
  def testbackend(self):
    self.__services.test_connection()
    
  def save_applicant(self):
    applicant_form = self.__application_form.get_applicant()
    self.__applicant_controller.save_applicant(self.__applicant, applicant_form)