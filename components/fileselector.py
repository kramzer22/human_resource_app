import customtkinter as ctk

class FileSelector(ctk.CTkFrame):
  def __init__(self, master, label='', value='', placeholder_text='', font_family='Calibri', font_size=14):
    super().__init__(master=master, fg_color='transparent')
    
    self.__label = ctk.CTkLabel(master=self, text=label, font=(font_family, font_size), anchor='sw')
    self.__label.grid(row=0, column=0, columnspan=2, pady=(0,10), padx=0, sticky='we')
    
    self.__entry = ctk.CTkEntry(master=self, font=(font_family, font_size), placeholder_text=placeholder_text, state='readonly') 
    self.__entry.grid(row=1, column=0, pady=0, padx=0, sticky='we')
    # self.value(value=value)
    
    self.__open = ctk.CTkButton(master=self, text='Select', width=40, font=(font_family, font_size))
    self.__open.grid(row=1, column=1, pady=0, padx=(10, 0))
    
    self.grid_columnconfigure(0, weight=1)
    self.grid_rowconfigure(1, weight=1)