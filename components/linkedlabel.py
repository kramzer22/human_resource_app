import customtkinter as ctk


class LinkedLabel(ctk.CTkLabel):
  
  def __init__(self, master:any, text:str, anchor:str='', font_family:str='Calibri', font_size:int=14):
    super().__init__(master=master, text=text, font=(font_family, font_size), anchor=anchor)
    self._default_text_color = self._text_color
    
    self._state: str ='normal'
    self._click_attached_handler: callable = None 
    
    self.bind("<Enter>", lambda event: self.on_enter(event))
    self.bind("<Leave>", lambda event: self.on_leave(event))
    self.bind('<Button-1>',lambda event: self.on_click(event))
    
  def disable(self) -> None:
    self._state = 'disabled'
    
  def enable(self) -> None:
    self._state = 'normal'
    
  def attach_handler_to_click_event(self, handler: callable) -> None:
    self._click_attached_handler = handler
    
  def on_enter(self, event:any) -> None:
    if self._state == 'normal':
      self.configure(text_color='blue', font=('Calibri', 14, 'underline'))

  def on_leave(self, event:any) -> None:
    if self._state == 'normal':
      self.configure(text_color=self._default_text_color, font=('Calibri', 14, 'normal'))
    
  def on_click(self, event:any) -> None:
    if self._state == 'normal':
      if self._click_attached_handler:
        self._click_attached_handler()
    