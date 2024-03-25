import customtkinter as ctk
import datetime as dt
import json

class DateSelector(ctk.CTkFrame):
  def __init__(self, master, label='', date_value='', font_family='Calibri', font_size=14):
    super().__init__(master=master, fg_color='transparent')
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov', 'Dec']
    
    days = []
    for i in range (1, 31):
      days.append(str(i))
      
    # print(days)
    
    current_year = dt.datetime.now().year
    years = []
    for i in range(current_year, current_year - 100, -1):
      years.append(str(i))
    
    # print(years)
    
    self.__label = ctk.CTkLabel(master=self, text=label, font=(font_family, font_size), anchor='sw')
    self.__label.grid(row=0, column=0, columnspan=3, pady=(0,10), padx=0, sticky='we')
    
    self.__combomonth = ctk.CTkComboBox(master=self,  values=months, font=(font_family, font_size))
    self.__combomonth.grid(row=1, column=0, pady=0, padx=(0,10), sticky='we')
    
    self.__comboday = ctk.CTkComboBox(master=self, values=days, font=(font_family, font_size))
    self.__comboday.grid(row=1, column=1, pady=0, padx=(0,10), sticky='we')
    
    self.__comboyear = ctk.CTkComboBox(master=self, values=years, font=(font_family, font_size))
    self.__comboyear.grid(row=1, column=2, pady=0, padx=0, sticky='we')
    
    self.grid_columnconfigure(0, weight=1)
    self.grid_columnconfigure(1, weight=1)
    self.grid_columnconfigure(2, weight=1)
    
  # def load_default(self):
  #   self.__combomonth
  