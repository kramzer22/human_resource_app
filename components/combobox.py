import customtkinter as ctk

class ComboBox(ctk.CTkFrame):
  def __init__(self, master:any, font: tuple | ctk.CTkFont | None = None, combo_height:int=40, label:str='', values:list=[], **kwargs):
    super().__init__(master=master, **kwargs)
    
    self.__label = ctk.CTkLabel(master=self, text=label, font=font, anchor='sw')
    self.__label.grid(row=0, column=0, pady=(0,10), padx=0, sticky='we')
    
    self.__combobox = ctk.CTkComboBox(master=self, values=values, font=font, height=combo_height)
    self.__combobox.grid(row=1, column=0, pady=0, padx=0, sticky='we')
    
    self.grid_columnconfigure(0, weight=1)
    
  @property
  def text(self):
    return self.__combobox.get()
  
  @text.setter
  def text(self, value):
    self.__combobox.set(value)