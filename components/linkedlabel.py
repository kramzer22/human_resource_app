import customtkinter as ctk


class LinkedLabel(ctk.CTkLabel):
  
  def __init__(self, master, text, anchor='', font_family='Calibri', font_size=14):
    super().__init__(master=master, text=text, font=(font_family, font_size), anchor=anchor)
    self._default_text_color = self._text_color
    
    self._state ='normal'
    
    self.bind("<Enter>", self.on_enter)
    self.bind("<Leave>", self.on_leave)
    
  def on_enter(self, e):
    if self._state == 'normal':
      self.configure(text_color='blue', font=('Calibri', 14, 'underline'))

  def on_leave(self, e):
    if self._state == 'normal':
      self.configure(text_color=self._default_text_color, font=('Calibri', 14, 'normal'))
    
  def on_click(self, method):
    if self._state == 'normal':
      method()
    
  def set_click_event(self, method):
    self.bind('<Button-1>', lambda event: self.on_click(method))
    
  def disable(self):
    self._state = 'disabled'
    
  def enable(self):
    self._state = 'normal'
    