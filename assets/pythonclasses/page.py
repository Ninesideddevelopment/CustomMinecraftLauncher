import customtkinter as ctk

class Page(ctk.CTkFrame):
	def __init__(self, master, **kwargs):
		super().__init__(master, **kwargs)

	def hide(self):
		self.grid_remove()

	def show(self):
		self.homepage.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")