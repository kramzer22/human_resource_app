import customtkinter as ctk

class ComboBox(ctk.CTkFrame):
  def __init__(self, master:any, font: tuple | ctk.CTkFont | None = None, combo_height:int=40, label:str='', values:list=[], **kwargs):
    super().__init__(master=master, **kwargs)
    
    self._change_handler: callable = None
    
    self._label = ctk.CTkLabel(master=self, text=label, font=font, anchor='sw')
    self._label.grid(row=0, column=0, pady=(0,10), padx=0, sticky='we')
    
    self._combobox = ctk.CTkComboBox(master=self, values=values, font=font, height=combo_height, state='readonly', command=self.on_change)
    self._combobox.grid(row=1, column=0, pady=0, padx=0, sticky='we')
    
    self.grid_columnconfigure(0, weight=1)
    
  def on_change(self, choice)-> None: 
    if self._change_handler:
      self._change_handler(choice)
    
  def attach_handler_to_change_event(self, handler:callable) -> None:
    self._change_handler = handler
    
  def destroy(self):
    # Class clean up here
    self._change_handler = None
    
    self._label.destroy()
    self._combobox.destroy()
    # self._note.destroy()   
    # self._entry.destroy()
    
    super().destroy()
    
  @property
  def text(self):
    return self._combobox.get()
  
  @text.setter
  def text(self, value):
    self._combobox.set(value)