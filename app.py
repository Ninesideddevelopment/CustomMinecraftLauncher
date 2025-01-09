import customtkinter as ctk
import tkinter as tk
from PIL import Image

from mojang_news import fetch_mojang_news
from assets.pythonclasses.changelogwidget import ChangeLogWidget
from launcher_audio import AudioPlayerClass
from launcher import launch

class SBarAccountWidget(ctk.CTkFrame):
	def __init__(self, master, **kwargs):
		super().__init__(master, **kwargs)

		self.name = ctk.CTkLabel(master=self, text="Username")
		self.name.place(relx=0, relwidth=1, rely=0)

		self.accountbutton = ctk.CTkButton(master=self, text="Account", corner_radius=0)
		self.accountbutton.place(relwidth=0.49, rely=1, relx=0, anchor=ctk.SW)

		self.profilebutton = ctk.CTkButton(master=self, text="Profile", corner_radius=0)
		self.profilebutton.place(relwidth=0.49, rely=1, relx=0.51, anchor=ctk.SW)

class Sidebar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.homebutton = ctk.CTkButton(master=self, text="Home", command=self.master.homepage_button_function, corner_radius=0)
        self.homebutton.grid(row=0, column=0, pady=5)

        self.friendsbutton = ctk.CTkButton(master=self, text="Friends", command=self.master.friends_button_function, corner_radius=0)
        self.friendsbutton.grid(row=1, column=0, pady=5)

        self.installationsbutton = ctk.CTkButton(master=self, text="Installations", command=self.master.installations_button_function, corner_radius=0)
        self.installationsbutton.grid(row=2, column=0, pady=5)

        self.settingsbutton = ctk.CTkButton(master=self, text="Settings", command=self.master.settings_button_function, corner_radius=0)
        self.settingsbutton.grid(row=3, column=0, sticky=ctk.S, pady=90)

        self.customisebutton = ctk.CTkButton(master=self, text="Customisation", command=self.master.customise_button_function, corner_radius=0)
        self.customisebutton.grid(row=3, column=0, sticky=ctk.S, pady=50)

        self.accountswidget = SBarAccountWidget(master=self)
        self.accountswidget.grid(row=4, column=0, sticky=ctk.S)

class Changelog(ctk.CTkFrame):
	def __init__(self, master, **kwargs):
		super().__init__(master, **kwargs)
		#self.widgets = []
		#for i, entry in enumerate(self.master.master.mojang_news):
		#	self.widgets.append(ChangeLogWidget(master=self, title=self.master.master.mojang_news[i]["title"], description=self.master.master.mojang_news[i]["text"], corner_radius=0))
		#for i, entry in enumerate(self.widgets):
		#	entry.place(relx=0.5, y=(i+1)*250, relwidth=0.9, anchor=ctk.CENTER)

class HomePage(ctk.CTkFrame):
	def __init__(self, master, **kwargs):
		super().__init__(master, **kwargs)

		self.bannerimage = ctk.CTkImage(light_image=Image.open(f"assets/styles/{self.master.style}/images/homepage/banner.png"), 
											 dark_image=Image.open(f"assets/styles/{self.master.style}/images/homepage/banner.png"),
											 size=(1920, 1080))
		self.bannerlabel = ctk.CTkLabel(master=self, image=self.bannerimage, text="")
		self.bannerlabel.place(relx=0.5, rely=0.25, anchor=ctk.CENTER)

		self.below = ctk.CTkFrame(master=self, corner_radius=0, fg_color="black")
		self.below.place(relx=0, rely=0.5, relwidth=2, relheight=0.5, anchor=ctk.N)

		self.Changelog = Changelog(master=self, fg_color="grey", corner_radius=0)
		self.Changelog.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

		self.playbutton = ctk.CTkButton(master=self, text="Play", command=self.master.play_button_function, corner_radius=0)
		self.playbutton.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

	def hide(self):
		self.grid_remove()

	def show(self):
		self.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")

class App(ctk.CTk):
	def __init__(self, title="Custom Minecraft Launcher"):
		super().__init__()

		self.style = "default"

		self.mojang_news = fetch_mojang_news("data/minecraft_news.json")

		ctk.set_appearance_mode("System")
		ctk.set_default_color_theme("green")

		self.minsize(1300, 700)
		self.geometry("1300x700")
		self.title(title)

		self.grid_rowconfigure(0, weight=1)
		self.grid_columnconfigure(0, weight=0)
		self.grid_columnconfigure(1, weight=1)

		self.homepage = HomePage(master=self, corner_radius=0, fg_color="black")
		self.homepage.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")

		self.sidebar = Sidebar(master=self, corner_radius=0)
		self.sidebar.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

		self.music_player = AudioPlayerClass(f"assets/styles/{self.style}/music/music.wav")

	def music_loop(self):
		self.music_player.play_audio()
		self.after(self.music_player.length+2000, self.music_loop)

	def homepage_button_function(self):
		self.homepage.show()

	def friends_button_function(self):
		self.homepage.hide()

	def installations_button_function(self):
		self.homepage.hide()

	def settings_button_function(self):
		self.homepage.hide()

	def customise_button_function(self):
		self.homepage.hide()

	def play_button_function(self):
		launch()