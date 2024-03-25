import customtkinter as ctk


class SideBar(ctk.CTkFrame):
  def __init__(self, master, font_family='Calibri', font_size=14, list_height=40):
    super().__init__(master=master)
    
    self.nav_buttons = [] 
    self.button_text = ['list', 'form', 'report']
    
    for i, value in enumerate(self.button_text):
      button = ctk.CTkButton(master=self, text=value, font=(font_family, font_size), height=list_height, command=lambda v=i: self.button_clicked(v))
      button.grid(row=i, column=0, padx=20, pady=(20, 0), sticky="we")
      self.nav_buttons.append(button)
      
    self.grid_columnconfigure(0, weight=1)
      
  def button_clicked(self, value):
        print(f"Button clicked: {value}")
  
  
    
    