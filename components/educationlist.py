from typing import Any, Tuple
import customtkinter as ctk

from .textinput import TextInput

class EducationList(ctk.CTkFrame):
  def __init__(self, master: Any, font: tuple | ctk.CTkFont | None = None, **kwargs):
    super().__init__(master, **kwargs)
    
    self._font = font
    
    self.grid_columnconfigure(0, weight=1, uniform='education_col')
    self.grid_columnconfigure(1, weight=1, uniform='education_col')
    self.grid_columnconfigure(2, weight=1, uniform='education_col')
    
    self._title_label = ctk.CTkLabel(master=self, text="Education background information", font=('Calibri', 18, 'bold'), anchor='w')
    self._title_label.grid(row=0, column=0, columnspan=2, pady=0, padx=0, sticky='we')
    
    self._add_education_button = ctk.CTkButton(master=self, text='+', font=('Calibri', 14, 'bold'), width=20, height=20, command=self.create_education)
    self._add_education_button.grid(row=0, column=2, pady=0, padx=0, sticky='e')
    
    self._education_list = []
    
  def create_education(self) -> None:
    def on_cancel(education):
      education['education'].destroy()
      education['university'].destroy()
      education['year'].destroy()
      education['save'].destroy()
      education['cancel'].destroy()
      education['button_frame'].destroy()
      education['frame'].destroy()
      education = None
    
    education = {
      'frame':ctk.CTkFrame,
      'education': TextInput,
      'university': TextInput,
      'year': TextInput,
      'button_frame':ctk.CTkFrame,
      'save': ctk.CTkButton,
      'cancel': ctk.CTkButton,
    }
    
    columns, rows = self.grid_size()
    
    print(rows)
    
    education['frame'] = ctk.CTkFrame(master=self)
    education['frame'].grid(row=rows, column=0, columnspan=3, sticky='nwe')
    
    education['frame'].grid_columnconfigure(0, weight=1, uniform='nice')
    education['frame'].grid_columnconfigure(1, weight=1, uniform='nice')
    education['frame'].grid_columnconfigure(2, weight=1, uniform='nice')
    
    education['button_frame'] = ctk.CTkFrame(master=education['frame'], fg_color='transparent')
    education['button_frame'].grid(row=0, column=2, pady=0, padx=0, sticky='nwe')
    
    education['button_frame'].grid_columnconfigure(0, weight=1)
    
    education['save'] = ctk.CTkButton(master=education['button_frame'], text='save', font=('Calibri', 14, 'bold'), width=60, height=30)
    education['save'].grid(row=0, column=1, pady=(10, 0), padx=(0, 10), sticky='w')
    
    education['cancel'] = ctk.CTkButton(master=education['button_frame'], text='cancel', font=('Calibri', 14, 'bold'), width=60, height=30, command= lambda: on_cancel(education))
    education['cancel'].grid(row=0, column=0, pady=(10, 0), padx=(0, 10), sticky='e')
    
    education['education'] = TextInput(master=education['frame'], label_text='Education', font=self._font, fg_color='transparent')
    education['education'].grid(row=1, column=0, columnspan=3, pady=(0, 10), padx=(10, 5), sticky='we')
     
    education['university'] = TextInput(master=education['frame'], label_text='School/University', font=self._font, fg_color='transparent')
    education['university'].grid(row=2, column=0, columnspan=2, pady=(0, 10), padx=(10, 5), sticky='we')
    
    education['year'] = TextInput(master=education['frame'], label_text='Year Graduate', font=self._font, fg_color='transparent')
    education['year'].grid(row=2, column=2, pady=(0, 10), padx=(10, 5), sticky='we')