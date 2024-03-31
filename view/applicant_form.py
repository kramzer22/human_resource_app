import customtkinter as ctk

from components.textinput import TextInput
from components.combobox import ComboBox
from components.datebox import DateSelector
from components.fileselector import FileSelector

from components.taskbar import TaskBar

class ApplicationForm(ctk.CTkFrame):
  def __init__(self, master):
    super().__init__(master=master, fg_color='transparent')
    
    gender = ['male', 'female', 'others']
    
    self.__form_frame = ctk.CTkFrame(master=self)
    self.__form_frame.grid(row=0, column=0, pady=0, padx=(0, 2), sticky='nswe')
    
    self.__task_frame = TaskBar(master=self, title='Applicant progress')
    self.__task_frame.grid(row=0, column=1, pady=0, padx=0, sticky='nswe')
    
    self.grid_columnconfigure(0, weight=1)
    self.grid_columnconfigure(1, minsize=340)
    self.grid_rowconfigure(0, weight=1)
    
    self.__header = ctk.CTkLabel(master=self.__form_frame, text="Applicant registration form", font=('Calibri', 24), anchor='w')
    self.__header.grid(row=0, column=0, columnspan=3, pady=10, padx=10, sticky='we')
    
    self.__entry_firstname = TextInput(master=self.__form_frame, label='First name')
    self.__entry_firstname.grid(row=1, column=0, pady=10, padx=10, sticky='we')
    
    self.__entry_middlename = TextInput(master=self.__form_frame, label='Middle name')
    self.__entry_middlename.grid(row=1, column=1, pady=10, padx=10, sticky='we')
    
    self.__entry_lastname = TextInput(master=self.__form_frame, label='Last name')
    self.__entry_lastname.grid(row=1, column=2, pady=10, padx=10, sticky='we')
    
    self.__datebox_bday = DateSelector(master=self.__form_frame, label='Birthdate')
    self.__datebox_bday.grid(row=2, column=0, pady=10, padx=10, sticky='we')
    
    self.__combo_gender = ComboBox(master=self.__form_frame, values=gender, label='Gender')
    self.__combo_gender.grid(row=2, column=1, pady=10, padx=10, sticky='we')
    
    self.__entry_contact = TextInput(master=self.__form_frame, label='Contact number')
    self.__entry_contact.grid(row=2, column=2, pady=10, padx=10, sticky='we')
    
    self.__country = TextInput(master=self.__form_frame, label='Country')
    self.__country.grid(row=3, column=0, pady=10, padx=10, sticky='we')
    
    self.__province = TextInput(master=self.__form_frame, label='Province')
    self.__province.grid(row=3, column=1, pady=10, padx=10, sticky='we')
    
    self.__city = TextInput(master=self.__form_frame, label='City')
    self.__city.grid(row=3, column=2, pady=10, padx=10, sticky='we')
    
    self.__address = TextInput(master=self.__form_frame, label='Address')
    self.__address.grid(row=4, column=0, columnspan=3, pady=10, padx=10, sticky='we')
    
    self.__position = TextInput(master=self.__form_frame, label='Position')
    self.__position.grid(row=5, column=0, columnspan=2, pady=10, padx=10, sticky='we')
    
    self.__source = TextInput(master=self.__form_frame, label='Source')
    self.__source.grid(row=5, column=2, pady=10, padx=10, sticky='we')
    
    self.__resume = FileSelector(master=self.__form_frame, label='Resume')
    self.__resume.grid(row=6, column=0, columnspan=3, pady=10, padx=10, sticky='we')
    
    self.__save = ctk.CTkButton(master=self.__form_frame, text='Save', font=('Calibri', 22), width=140, height=60, command=self.click)
    self.__save.grid(row=7, column=0, columnspan=3, pady=0, padx=0)
    
    self.__command = None
      
    self.__form_frame.grid_columnconfigure(0, weight=1, uniform='layout_1')
    self.__form_frame.grid_columnconfigure(1, weight=1, uniform='layout_1')
    self.__form_frame.grid_columnconfigure(2, weight=1, uniform='layout_1')
    self.__form_frame.grid_rowconfigure(7, weight=1)
    
    self.enable_form()
    
  def click(self):
    if self.__command:
      self.__command()
      
    
  def get_applicant(self):
    applicant = {}
    applicant['name'] = {}
    applicant['name']['firstname'] = self.__entry_firstname.text
    applicant['name']['middlename'] = self.__entry_middlename.text
    applicant['name']['lastname'] = self.__entry_lastname.text
    applicant['birthdate'] = self.__datebox_bday.date
    applicant['gender'] = self.__combo_gender.text
    
    return applicant
    
  
  def disable_form(self):
    for item in self.__form_frame.winfo_children():
      if isinstance(item, ctk.CTkFrame):
        for component in item.winfo_children():
          component.configure(state='disable')
      else:
        item.configure(state='disable')
        
  def enable_form(self):
    for item in self.__form_frame.winfo_children():
      if isinstance(item, ctk.CTkFrame):
        for component in item.winfo_children():
          component.configure(state='normal')
      else:
        item.configure(state='normal')
        
  def set_save_command(self, command):
    self.__command = command
   