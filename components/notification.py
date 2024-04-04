import customtkinter as ctk
import threading
import time
from typing import Any

class Notification(ctk.CTkFrame):
  def __init__(self, master, button_type, title: str='', message: str='',):
    super().__init__(master=master, width=240, height=200, border_width=1)

    self._master = master
    self._complete = False
    
    self._label_title = ctk.CTkLabel(master=self, text=title, font=('Calibri', 16), width=240)
    self._label_title.pack(side='top', fill='x', pady=(20,0), padx=10)
    
    self._label_content = ctk.CTkLabel(master=self, text=message, width=240, wraplength=240)
    self._label_content.pack(side='top', fill='x', pady=(30, 20), padx=10)
    
    self._button_close = None
    self._button_proceed = None
    if button_type == 0:
      self._button_close = ctk.CTkButton(master=self, text='Close', font=('Calibri', 16), width=80, height=40, command=lambda: self.on_click('no'))
      self._button_close.pack(side='top', fill='x', pady=(10, 40), padx=10)
    elif button_type == 1:
      self._button_proceed = ctk.CTkButton(master=self, text='Proceed', font=('Calibri', 16), width=80, height=40, command=lambda: self.on_click('yes'))
      self._button_proceed.pack(side='right', pady=(10, 30), padx=(0, 40))
      self._button_close = ctk.CTkButton(master=self, text='Close', font=('Calibri', 16), width=80, height=40, command=lambda: self.on_click('no'))
      self._button_close.pack(side='left', pady=(10, 30), padx=(40, 0))
    
    # self.grid_columnconfigure(0, width=1)
    # self.grid_columnconfigure(1, width=1)
    # self.grid_rowconfigure(1, weight=1)
    
  def show_notificication(self):
    ctk.CTkToplevel
    
    thread = threading.Thread(target=lambda: self.start_thread())
  
  def start_thread(self):
    while self._complete == False:
      time.sleep(50)
    
  def add_method_to_on_click(self, method):
    self._method = method
    
  def center_self_from_parent(self, master):
    window_width = master.winfo_width()
    window_height = master.winfo_height()
    
    frame_width = 240
    frame_height = self.winfo_reqheight()
    
    x = (window_width - frame_width) // 2
    y = (window_height - frame_height) // 2
    
    self.place(x=x - 10, y=y)
    self.lift()
    
  def on_click(self, button_clicked):
    self._method(button_clicked)
    self.destroy()

    