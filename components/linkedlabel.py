import customtkinter as ctk


class LinkedLabel(ctk.CTkLabel):
  
  def __init__(self, master, text, anchor='', font_family='Calibri', font_size=14):
    super().__init__(master=master, text=text, font=(font_family, font_size), anchor=anchor)
    self.__default_text_color = self._text_color
    
    self.bind("<Enter>", self.on_enter)
    self.bind("<Leave>", self.on_leave)
    
  def on_enter(self, e):
    self.configure(text_color='blue', font=('Calibri', 14, 'underline'))

  def on_leave(self, e):
    self.configure(text_color=self.__default_text_color, font=('Calibri', 14, 'normal'))
    
  def click(self, command, name):
    self.bind('<Button-1>', lambda event: command(name))