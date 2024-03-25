import customtkinter as ctk

class TextInput(ctk.CTkFrame):
  def __init__(self, master, label='', value='', placeholder_text='', font_family='Calibri', font_size=14):
    super().__init__(master=master, fg_color='transparent')
    
    self.__label = ctk.CTkLabel(master=self, text=label, font=(font_family, font_size), anchor='sw')
    self.__label.grid(row=0, column=0, pady=(0,10), padx=0, sticky='we')
    
    self.__entry = ctk.CTkEntry(master=self, font=(font_family, font_size), placeholder_text=placeholder_text) 
    self.__entry.grid(row=1, column=0, pady=0, padx=0, sticky='we')
    self.value(value=value)
    
    self.grid_columnconfigure(0, weight=1)
    
  def value(self, value):
    self.__entry.insert(0, value)