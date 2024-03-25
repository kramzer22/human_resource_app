import customtkinter as ctk

class TaskBar(ctk.CTkFrame):
  def __init__(self, master, title='', title_fontfamily='Calibri', title_fontsize=24):
    super().__init__(master=master)

    self.__title = ctk.CTkLabel(master=self, text=title, font=(title_fontfamily, title_fontsize), anchor='w')
    self.__title.grid(row=0, column=0, pady=(10,0), padx=(10,0), sticky='we')
    self.__addtask = ctk.CTkButton(master=self, text="+", width=40, font=(title_fontfamily, title_fontsize, 'bold'))
    self.__addtask.grid(row=0, column=1, pady=(10,0), padx=(0,10))
    self.__tasklist = ctk.CTkScrollableFrame(master=self)
    self.__tasklist.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')
    
    self.grid_columnconfigure(0, weight=1)
    self.grid_rowconfigure(1, weight=1)