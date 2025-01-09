import customtkinter as ctk
import tkinter as tk

class ChangeLogWidget(ctk.CTkFrame):
	def __init__(self, master, title="Placeholder Text", description="Placeholder Text", **kwargs):
		super().__init__(master, **kwargs)

		self.title = ctk.CTkLabel(master=self, text=title, font=("Arial", 20))
		self.title.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

		self.decription = ctk.CTkLabel(master=self, text=description)
		self.decription.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)