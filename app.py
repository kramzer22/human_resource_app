import customtkinter as ctk

from components.sidebar import SideBar
from view.applicant_form import ApplicationForm

# from module.helper_module import DateFunctions 

class App():
  def __init__(self):
    main_font = 'Roboto'
    
    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('green')
  
    self.__root = ctk.CTk()
    self.__root.geometry('1366x768')
    
    self.__sidebar = SideBar(master=self.__root, font_family='Roboto', font_size=16, list_height=70)
    self.__sidebar.grid(row=0, column=0, padx=(0,2), pady=0, sticky='nswe')
  
    self.__application_form = ApplicationForm(master=self.__root)
    self.__application_form.grid(row=0, column=1, padx=0, pady=0, sticky='nswe')
  
    self.__root.grid_columnconfigure(0, minsize=100)
    self.__root.grid_columnconfigure(1, weight=1)
    self.__root.grid_rowconfigure(0, weight=1)
    
    
    
  def run(self):
    self.__root.mainloop()