import customtkinter as ctk

class TextInput(ctk.CTkFrame):
  def __init__(self, master, name='', label='', text='', placeholder_text='', font_family='Calibri', font_size=14, entry_height=40, require=False):
    super().__init__(master=master, fg_color='transparent')
    
    self._name = name
    self._button = None 
    
    self._label = ctk.CTkLabel(master=self, text=label, font=(font_family, font_size), anchor='sw')
    self._label.grid(row=0, column=0, pady=(0,10), padx=0, sticky='we')
    
    self._require = ctk.CTkLabel(master=self, text='*' if require else '', text_color='red', font=(font_family, font_size), anchor='sw')
    self._require.grid(row=0, column=1, pady=(0,10), padx=0, sticky='we')
  
    self._note = ctk.CTkLabel(master=self, text='', font=(font_family, font_size), text_color='red', anchor='se')
    self._note.grid(row=0, column=2, pady=(0,10), padx=0, sticky='we')
    
    self._entry = ctk.CTkEntry(master=self, font=(font_family, font_size), height=entry_height, placeholder_text=placeholder_text) 
    self._entry.grid(row=1, column=0, columnspan=3, pady=0, padx=0, sticky='we')
    self.text = text
    
    self.grid_columnconfigure(2, weight=1)
    
  def set_text_changed(self, command):
    self._entry.bind("<KeyRelease>", lambda event: command(event))
    
  def add_hide_event(self):
    if not self._button:
      self._button = ctk.CTkButton(master=self, text='view', width=28, height=28, font=('Calibri', 12), fg_color='transparent', border_width=1)
      self._button.grid(row=1, column=0, columnspan=3, pady=2, padx=(0, 4), sticky='e')
      self._button.lift()
      
      self._button.bind("<Button-1>", self.show_text)
      self._button.bind("<ButtonRelease-1>",lambda event: self.hide_text(event))
      
      self._entry.configure(show='*')
      
  def show_text(self, event):
    self._entry.configure(show='')
      
  def hide_text(self, event):
    self._entry.configure(show='*')
    
  def set_note(self, text):
    self._note.configure(text=text)
    
  def focus(self):
    self._entry.focus()
  
  @property   
  def text(self):
    return self._entry.get()
  
  @text.setter
  def text(self, text):
    self._entry.delete(0, 'end') 
    self._entry.insert(0, text)