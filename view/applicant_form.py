import tkinter as tk
import customtkinter as ctk

from controller.applicant_controller import ApplicantController

from components.textinput import TextInput
from components.combobox import ComboBox
from components.datebox import DateSelector
from components.fileselector import FileSelector
from components.taskbar import TaskBar
from components.educationlist import EducationList

from module.fonts import *

class ApplicationForm(ctk.CTkFrame):
  def __init__(self, master, **kwargs):
    self._master: any = master 
    self._applicant_controller = ApplicantController(view=self)
    
    super().__init__(master=self._master, **kwargs)
    
    self.grid_columnconfigure(0, weight=1)
    self.grid_columnconfigure(1, minsize=340)
    self.grid_rowconfigure(0, weight=1)
    
    self._form_frame = ctk.CTkFrame(master=self)
    self._form_frame.grid(row=0, column=0, pady=0, padx=(0, 2), sticky='nswe')
    
    self._form_frame.grid_columnconfigure(0, weight=1, uniform='layout_1')
    self._form_frame.grid_columnconfigure(1, weight=1, uniform='layout_1')
    self._form_frame.grid_columnconfigure(2, weight=1, uniform='layout_1')
    self._form_frame.grid_rowconfigure(1, weight=1)
    
    self.__task_frame = TaskBar(master=self, title='Applicant progress')
    self.__task_frame.grid(row=0, column=1, pady=0, padx=0, sticky='nswe')
    
    self._header = ctk.CTkLabel(master=self._form_frame, text="Applicant registration form", font=('Calibri', 24), anchor='w')
    self._header.grid(row=0, column=0, columnspan=3, pady=10, padx=10, sticky='we')
    
    self._form_info_scrollframe = ctk.CTkScrollableFrame = ctk.CTkScrollableFrame(master=self._form_frame, orientation='vertical')
    self._form_info_scrollframe.grid(row=1, column=0, columnspan=3, pady=10, padx=10, sticky='nswe')
    
    self._form_info_scrollframe.grid_columnconfigure(0, weight=1)
    
    self._personalinfo_form_frame = ctk.CTkFrame(master=self._form_info_scrollframe)
    self._personalinfo_form_frame.grid(row=0, column=0, pady=(10, 0), padx=10, sticky='nwe')
    
    self._personalinfo_form_frame.grid_columnconfigure(0, weight=1, uniform='personalinfo_layout')
    self._personalinfo_form_frame.grid_columnconfigure(1, weight=1, uniform='personalinfo_layout')
    self._personalinfo_form_frame.grid_columnconfigure(2, weight=1, uniform='personalinfo_layout')
    
    self._personal_info_label = ctk.CTkLabel(master=self._personalinfo_form_frame, text="Personal information", font=('Calibri', 18, 'bold'), anchor='w')
    self._personal_info_label.grid(row=0, column=0, columnspan=3, pady=(10, 20), padx=10, sticky='we')
    
    self._entry_firstname = TextInput(master=self._personalinfo_form_frame, label_text='First name', input_require=True, font=(FORM_FONT_FAMILY, FORM_FONT_SIZE), fg_color='transparent')
    self._entry_firstname.grid(row=1, column=0, pady=(0, 10), padx=(10, 0), sticky='we')
    
    self._entry_middlename = TextInput(master=self._personalinfo_form_frame, label_text='Middle name', font=(FORM_FONT_FAMILY, FORM_FONT_SIZE), fg_color='transparent')
    self._entry_middlename.grid(row=1, column=1, pady=(0, 10), padx=(5, 5), sticky='we')
    
    self._entry_lastname = TextInput(master=self._personalinfo_form_frame, label_text='Last name', input_require=True, font=(FORM_FONT_FAMILY, FORM_FONT_SIZE), fg_color='transparent')
    self._entry_lastname.grid(row=1, column=2, pady=(0, 10), padx=(0, 10), sticky='we')
    
    self._datebox_bday = DateSelector(master=self._personalinfo_form_frame, label='Birthdate', font=(FORM_FONT_FAMILY, FORM_FONT_SIZE), fg_color='transparent')
    self._datebox_bday.grid(row=2, column=0, pady=(0, 20), padx=(10, 0), sticky='we')
    
    self._combo_gender = ComboBox(master=self._personalinfo_form_frame, values=self._applicant_controller.get_genders(), label='Gender', font=(FORM_FONT_FAMILY, FORM_FONT_SIZE), fg_color='transparent')
    self._combo_gender.grid(row=2, column=1, pady=(0, 20), padx=(5, 5), sticky='we')
    
    self._entry_marital = TextInput(master=self._personalinfo_form_frame, label_text='Marital Status', font=(FORM_FONT_FAMILY, FORM_FONT_SIZE), fg_color='transparent')
    self._entry_marital.grid(row=2, column=2, pady=(0, 20), padx=(0, 10), sticky='we')
    
    self._address_contant_form_frame = ctk.CTkFrame(master=self._form_info_scrollframe)
    self._address_contant_form_frame.grid(row=1, column=0, pady=(20, 0), padx=10, sticky='nwe')
    
    self._address_contant_form_frame.grid_columnconfigure(0, weight=1, uniform='addresscontant_layout')
    self._address_contant_form_frame.grid_columnconfigure(1, weight=1, uniform='addresscontant_layout')
    self._address_contant_form_frame.grid_columnconfigure(2, weight=1, uniform='addresscontant_layout')
    
    self._address_contant_label = ctk.CTkLabel(master=self._address_contant_form_frame, text="Address and contant information", font=('Calibri', 18, 'bold'), anchor='w')
    self._address_contant_label.grid(row=0, column=0, columnspan=3, pady=(10, 20), padx=10, sticky='we')
    
    self._country = TextInput(master=self._address_contant_form_frame, label_text='Country', font=(FORM_FONT_FAMILY, FORM_FONT_SIZE), fg_color='transparent')
    self._country.grid(row=1, column=0, pady=(0, 10), padx=(10, 0), sticky='we')
  
    self._province = TextInput(master=self._address_contant_form_frame, label_text='Province/State', font=(FORM_FONT_FAMILY, FORM_FONT_SIZE), fg_color='transparent')
    self._province.grid(row=1, column=1, pady=(0, 10), padx=(5, 5), sticky='we')
    
    self._city = TextInput(master=self._address_contant_form_frame, label_text='City', font=(FORM_FONT_FAMILY, FORM_FONT_SIZE), fg_color='transparent')
    self._city.grid(row=1, column=2, pady=(0, 10), padx=(0, 10), sticky='we')
    
    self._address = TextInput(master=self._address_contant_form_frame, label_text='Address', font=(FORM_FONT_FAMILY, FORM_FONT_SIZE), fg_color='transparent')
    self._address.grid(row=2, column=0, columnspan=3, pady=(0, 10), padx=10, sticky='we')
    
    self._contact_entry = TextInput(master=self._address_contant_form_frame, label_text='Contact number', font=(FORM_FONT_FAMILY, FORM_FONT_SIZE), fg_color='transparent')
    self._contact_entry.grid(row=3, column=0, columnspan=2, pady=(0, 20), padx=(10, 5), sticky='we')
    
    self._email_entry = TextInput(master=self._address_contant_form_frame, label_text='Email', font=(FORM_FONT_FAMILY, FORM_FONT_SIZE), fg_color='transparent')
    self._email_entry.grid(row=3, column=2, pady=(0, 20), padx=(0, 10), sticky='we')
    
    self._education_form_frame = EducationList(master=self._form_info_scrollframe)
    self._education_form_frame.grid(row=2, column=0, pady=(20, 0), padx=20, sticky='nwe')
    
    self._work_experience_form_frame = ctk.CTkFrame(master=self._form_info_scrollframe)
    self._work_experience_form_frame.grid(row=4, column=0, pady=(20, 0), padx=0, sticky='nwe')
    
    self.__save = ctk.CTkButton(master=self._form_frame, text='Save', font=('Calibri', 22), width=140, height=60, command=self.click)
    self.__save.grid(row=2, column=0, columnspan=3, pady=0, padx=0)
    
    self.__command = None
    
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
    
  
  def disable_form(self) -> None:
    pass
    # for item in self.__form_frame.winfo_children():
    #   if isinstance(item, ctk.CTkFrame):
    #     for component in item.winfo_children():
    #       component.configure(state='disable')
    #   else:
    #     item.configure(state='disable')
        
  def enable_form(self) -> None:
    pass
    # for item in self.__form_frame.winfo_children():
    #   if isinstance(item, ctk.CTkFrame):
    #     for component in item.winfo_children():
    #       component.configure(state='normal')
    #   else:
    #     item.configure(state='normal')
        
  def set_save_command(self, command):
    self.__command = command
   