from typing import Any, Tuple
import customtkinter as ctk

from .textinput import TextInput
from .combobox import ComboBox

class EducationList(ctk.CTkFrame):
  def __init__(self, master: Any, font: tuple | ctk.CTkFont | None = None, **kwargs):
    super().__init__(master, **kwargs)
    
    self._font = font
    self._enable_create = True
    
    self.grid_columnconfigure(0, weight=1, uniform='education_col')
    self.grid_columnconfigure(1, weight=1, uniform='education_col')
    self.grid_columnconfigure(2, weight=1, uniform='education_col')
    
    self._title_label = ctk.CTkLabel(master=self, text="Education background information", font=('Calibri', 18, 'bold'), anchor='w')
    self._title_label.grid(row=0, column=0, columnspan=2, pady=0, padx=0, sticky='we')
    
    self._add_education_button = ctk.CTkButton(master=self, text='+', font=('Calibri', 14, 'bold'), width=20, height=20, command=self.create_education)
    self._add_education_button.grid(row=0, column=2, pady=0, padx=0, sticky='e')
    
    self._education_list = []
    
  def enable_create(self) -> None:
    self._enable_create = True
    self._add_education_button.configure(state='normal')
    
  def disable_create(self) -> None:
    self._enable_create = False
    self._add_education_button.configure(state='disabled')
    
  def create_education(self) -> None:
    new_education = None
    
    def on_cancel(education):
      destroy(education)
      
    def on_save(education):
      add_education_to_list(education)
      display_education_list()
      
    def on_degree_change(value) -> None:
      if value == '':
        new_education['course'].disable()
        new_education['university'].disable()
        new_education['year'].disable()
      elif value == 'High school':
        new_education['course'].disable()
        new_education['university'].enable()
        new_education['year'].enable()
        new_education['university'].focus()
      else:
        new_education['course'].enable()
        new_education['university'].enable()
        new_education['year'].enable()
        new_education['course'].focus()
      
      
    def destroy(education):
      self._education_list.remove(education)
      
      education['degree'].destroy()
      education['course'].destroy()
      education['university'].destroy()
      education['year'].destroy()
      education['save'].destroy()
      education['cancel'].destroy()
      education['button_frame'].destroy()
      education['frame'].destroy()
      education = None
          
      self.enable_create()
      
    def adjust_education_list():
      for index, education in enumerate(self._education_list, start=2):
        education['frame'].grid(row=index, column=0, columnspan=3, sticky='nwe')
      
    def add_education_to_list(education):
      self._education_list.append(education)
      
    def display_education_list():
      for education in self._education_list:
        education['frame'].grid_forget()
      
      for education in self._education_list:
        set_education_item(education)
      
    def set_education_item(education) -> dict:
      columns, rows = self.grid_size()
      
      education['frame'].configure(fg_color='transparent')
      education['frame'].grid(row=rows, column=0, columnspan=3, sticky='nwe')
      education['save'].configure(command=None, text='update')
      education['cancel'].configure(text='remove')
      
      education['degree'].grid_remove()
      education['degree_text'].text = education['degree'].text
      education['degree_text'].grid()
      
      if education['degree_text'].text == 'High school':
        education['course'].grid_remove()
        education['university'].grid(row=1, column=1, columnspan=1, pady=(0, 10), padx=(5, 5), sticky='we')
        education['year'].grid(row=1, column=2, pady=(0, 10), padx=(5, 10), sticky='we')
      else:
        education['course'].grid(row=1, column=1, columnspan=2, pady=(0, 10), padx=(5, 10), sticky='we')
        education['university'].grid(row=2, column=0, columnspan=2, pady=(0, 10), padx=(10, 5), sticky='we')
        education['year'].grid(row=2, column=2, pady=(0, 10), padx=(5, 10), sticky='we')
     
        
    def create_education_form() -> dict:
      adjust_education_list()
      
      education = {
        'frame':ctk.CTkFrame,
        'degree': ComboBox,
        'degree_text': TextInput,
        'course': TextInput,
        'university': TextInput,
        'year': TextInput,
        'button_frame':ctk.CTkFrame,
        'save': ctk.CTkButton,
        'cancel': ctk.CTkButton,
      }
      
      degrees = ['High school', 'Certificate', 'Vocational', 'Associate', 'Bachelors', 'Masteral', 'Doctoral']
      columns, rows = self.grid_size()
      
      education['frame'] = ctk.CTkFrame(master=self)
      education['frame'].grid(row=1, column=0, columnspan=3, sticky='nwe')
      
      education['frame'].grid_columnconfigure(0, weight=3, uniform='nice')
      education['frame'].grid_columnconfigure(1, weight=5, uniform='nice')
      education['frame'].grid_columnconfigure(2, weight=2, uniform='nice')
      
      education['button_frame'] = ctk.CTkFrame(master=education['frame'], fg_color='transparent')
      education['button_frame'].grid(row=0, column=2, pady=0, padx=0, sticky='nwe')
      
      education['button_frame'].grid_columnconfigure(0, weight=1)
      
      education['save'] = ctk.CTkButton(master=education['button_frame'], text='save', font=('Calibri', 14, 'bold'), width=60, height=30, command=lambda: on_save(education))
      education['save'].grid(row=0, column=1, pady=(10, 0), padx=(0, 10), sticky='w')
      
      education['cancel'] = ctk.CTkButton(master=education['button_frame'], text='cancel', font=('Calibri', 14, 'bold'), width=60, height=30, command=lambda: on_cancel(education))
      education['cancel'].grid(row=0, column=0, pady=(10, 0), padx=(0, 10), sticky='e')
      
      education['degree'] = ComboBox(master=education['frame'], values=degrees, label='Education degree', font=('Calibri', 14, 'bold'), fg_color='transparent')
      education['degree'].grid(row=1, column=0, pady=(0, 10), padx=(10, 5), sticky='we')
      education['degree'].attach_handler_to_change_event(on_degree_change)
      
      education['degree_text'] = TextInput(master=education['frame'], label_text='Education degree', font=self._font, fg_color='transparent')
      education['degree_text'].grid(row=1, column=0, pady=(0, 10), padx=(10, 5), sticky='we')
      education['degree_text'].grid_remove()
      
      education['course'] = TextInput(master=education['frame'], label_text='Course', font=self._font, fg_color='transparent')
      education['course'].grid(row=1, column=1, columnspan=2, pady=(0, 10), padx=(5, 10), sticky='we')
      education['course'].disable()
      
      education['university'] = TextInput(master=education['frame'], label_text='School/University', font=self._font, fg_color='transparent')
      education['university'].grid(row=2, column=0, columnspan=2, pady=(0, 10), padx=(10, 5), sticky='we')
      education['university'].disable()
      
      education['year'] = TextInput(master=education['frame'], label_text='Year Graduate', font=self._font, fg_color='transparent')
      education['year'].grid(row=2, column=2, pady=(0, 10), padx=(5, 10), sticky='we')
      education['year'].disable()
      
      return education
    
    new_education = create_education_form()