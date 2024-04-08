from typing import Any, Callable, Tuple
import customtkinter as ctk

import threading
import time

class LoadingButton(ctk.CTkButton):
  def __init__(self, master: Any, **kwargs):
    super().__init__(master, **kwargs)
    
    self._button_1_handler = None
    self._button_text = kwargs.get('text')
    self._is_loading = False
    
    self.bind('<Button-1>', lambda event: self.on_click(event))
    
  def on_click(self, event) -> None:
    if self._button_1_handler:
      self._button_1_handler()
    else:
      print('no handler triggered')
  
  def attach_handler_to_click_event(self, handler:callable) -> None:
    self._button_1_handler = handler
    
  def start_loading_display(self) -> None:
    self._is_loading = True
    
    threading.Thread(target=self.load_display, daemon=True).start()
    
  def stop_loading_display(self) -> None:
    self._is_loading = False
    self.configure(text=self._button_text)
    
  def load_display(self) -> None:
    self.configure(text='.')
    while self._is_loading:
      if self.cget('text') == '.':
        self.configure(text='. .')
      elif self.cget('text') == '. .':
        self.configure(text='. . .')
      elif self.cget('text') == '. . .':
        self.configure(text='. . . .')
      else:
         self.configure(text='.')
      time.sleep(0.5)       
    
      
  