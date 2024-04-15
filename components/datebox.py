import customtkinter as ctk
import datetime as dt

class DateSelector(ctk.CTkFrame):
  def __init__(self, master, font: tuple | ctk.CTkFont | None = None, label='', date_value: dt.date='', entry_height=40, **kwargs):
    super().__init__(master=master, **kwargs)
    
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
    
    self.__label = ctk.CTkLabel(master=self, text=label, font=font, anchor='sw')
    self.__label.grid(row=0, column=0, columnspan=3, pady=(0,10), padx=0, sticky='we')
    
    self.__combo_month = ctk.CTkComboBox(master=self,  values=months, font=font, height=entry_height)
    self.__combo_month.grid(row=1, column=0, pady=0, padx=(0,10), sticky='we')
    
    self.__combo_day = ctk.CTkComboBox(master=self, values=days, font=font, height=entry_height)
    self.__combo_day.grid(row=1, column=1, pady=0, padx=(0,10), sticky='we')
    
    self.__combo_year = ctk.CTkComboBox(master=self, values=years, font=font, height=entry_height)
    self.__combo_year.grid(row=1, column=2, pady=0, padx=0, sticky='we')
    
    self.grid_columnconfigure(0, weight=1)
    self.grid_columnconfigure(1, weight=1)
    self.grid_columnconfigure(2, weight=1)
    
  # def load_default(self):
  #   self.__combomonth
  
  @property 
  def date(self):
    year = int(self.__combo_year.get())
    month =  dt.datetime.strptime(self.__combo_month.get(), '%b').month
    day = int(self.__combo_day.get())

    return dt.date(year, month, day)
  
  @date.setter
  def date(self, value):
    self.__combo_year.set(value.year)
    self.__combo_month.set(value.month)
    self.__combo_day.set(value.day)
    
  