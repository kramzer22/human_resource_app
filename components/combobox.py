import customtkinter as ctk

class ComboBox(ctk.CTkFrame):
  def __init__(self, master:any, label:str='', values:list=[], font_family='Calibri', font_size=14):
    super().__init__(master=master, fg_color='transparent')
    
    self.__label = ctk.CTkLabel(master=self, text=label, font=(font_family, font_size), anchor='sw')
    self.__label.grid(row=0, column=0, pady=(0,10), padx=0, sticky='we')
    
    self.__combobox = ctk.CTkComboBox(master=self, values=values, font=(font_family, font_size))
    self.__combobox.grid(row=1, column=0, pady=0, padx=0, sticky='we')
    
    self.grid_columnconfigure(0, weight=1)
    
  @property
  def text(self):
    return self.__combobox.get()
  
  @text.setter
  def text(self, value):
    self.__combobox.set(value)