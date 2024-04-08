from typing import Any, Callable, Tuple
import customtkinter as ctk

import threading
import time

class LoadingButton(ctk.CTkButton):
  def __init__(self, master: Any, width: int = 140, height: int = 28, corner_radius: int | None = None, border_width: int | None = None, border_spacing: int = 2, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, hover_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, text_color: str | Tuple[str, str] | None = None, text_color_disabled: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, round_width_to_even_numbers: bool = True, round_height_to_even_numbers: bool = True, text: str = "CTkButton", font: tuple | ctk.CTkFont | None = None, textvariable: ctk.Variable | None = None, image: ctk.CTkImage | Any | None = None, state: str = "normal", hover: bool = True, command: Callable[[], Any] | None = None, compound: str = "left", anchor: str = "center", **kwargs):
    super().__init__(master, width, height, corner_radius, border_width, border_spacing, bg_color, fg_color, hover_color, border_color, text_color, text_color_disabled, background_corner_colors, round_width_to_even_numbers, round_height_to_even_numbers, text, font, textvariable, image, state, hover, command, compound, anchor, **kwargs)
    
    self._button_1_handler = None
    self._button_text = text
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
    
      
  