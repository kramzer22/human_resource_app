import customtkinter as ctk

class TextInput(ctk.CTkFrame):
  def __init__(self, master:any, name:str='', label:str='', text:str='', placeholder_text:str='', font_family:str='Calibri', font_size:int=14, entry_height:int=40, require=False):
    super().__init__(master=master, fg_color='transparent')
    
    self._name: str = name
    self._key_release_handler: callable = None
    # self.text = text
    
    self.grid_columnconfigure(2, weight=1)
    
    self._show_button: ctk.CTkButton = None 
    
    self._label: ctk.CTkLabel = ctk.CTkLabel(master=self, text=label, font=(font_family, font_size), anchor='sw')
    self._label.grid(row=0, column=0, pady=(0,10), padx=0, sticky='we')
    
    self._require: ctk.CTkLabel = ctk.CTkLabel(master=self, text='*' if require else '', text_color='red', font=(font_family, font_size), anchor='sw')
    self._require.grid(row=0, column=1, pady=(0,10), padx=0, sticky='we')
  
    self._note: ctk.CTkLabel = ctk.CTkLabel(master=self, text='', font=(font_family, font_size), text_color='red', anchor='se')
    self._note.grid(row=0, column=2, pady=(0,10), padx=0, sticky='we')
    
    self._entry: ctk.CTkEntry = ctk.CTkEntry(master=self, font=(font_family, font_size), height=entry_height, placeholder_text=placeholder_text) 
    self._entry.grid(row=1, column=0, columnspan=3, pady=0, padx=0, sticky='we')
    self._entry.bind("<KeyRelease>", lambda event: self.on_entry_key_release(event))
  
  def on_entry_key_release(self, event:any)-> None: 
    if self._key_release_handler:
      self._key_release_handler(event)
  
  def attach_handler_to_keypress_event(self, handler:callable) -> None:
    self._key_release_handler = handler
    
  def enable_entry_mask(self) -> None:
    if not self._show_button:
      self._show_button = ctk.CTkButton(master=self, text='view', width=28, height=28, font=('Calibri', 12), fg_color='transparent', border_width=1)
      self._show_button.grid(row=1, column=0, columnspan=3, pady=2, padx=(0, 4), sticky='e')
      self._show_button.lift()
      
      self._show_button.bind("<ButtonPress-1>",lambda event: self.on_button_show_mouse_down(event))
      self._show_button.bind("<ButtonRelease-1>",lambda event: self.on_button_show_mouse_release(event))
      
      self._entry.configure(show='*')
    else:
      print('Entry masking is already enabled')
      
  def on_button_show_mouse_down(self, event:any) -> None:
    self._entry.configure(show='')
      
  def on_button_show_mouse_release(self, event:any) -> None:
    self._entry.configure(show='*')
    
  def set_note(self, text: str) -> None:
    self._note.configure(text=text)
    
  def focus(self) -> None:
    self._entry.focus()
    
  def enable(self) -> None:
    self._entry.configure(state='normal')
    if self._show_button:
      self._show_button.configure(state='normal')
    
  def disable(self) -> None:
    self._entry.configure(state='disabled')
    if self._show_button:
      self._show_button.configure(state='disabled')
  
  @property   
  def text(self) -> str:
    return self._entry.get()
  
  @text.setter
  def text(self, text: str) -> None:
    self._entry.delete(0, 'end') 
    self._entry.insert('end', text)