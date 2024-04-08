from tkinter.constants import NORMAL
from typing import Any, Tuple
import customtkinter as ctk

class Sample(ctk.CTkEntry):
  def __init__(self, master: Any, width: int = 140, height: int = 28, corner_radius: int | None = None, border_width: int | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, text_color: str | Tuple[str, str] | None = None, placeholder_text_color: str | Tuple[str, str] | None = None, textvariable: ctk.Variable | None = None, placeholder_text: str | None = None, font: tuple | ctk.CTkFont | None = None, state: str = tkinter.NORMAL, **kwargs):
    super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, text_color, placeholder_text_color, textvariable, placeholder_text, font, state, **kwargs)