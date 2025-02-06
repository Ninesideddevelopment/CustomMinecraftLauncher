import customtkinter as ctk
from customtkinter import *
import tkinter as tk
from PIL import Image

from mojang_news import fetch_mojang_news
from assets.pythonclasses.changelogwidget import ChangeLogWidget
from launcher_audio import AudioPlayerClass
from launcher import launch
import styles_loader

#Functions
def button_up(self, button:str, button_location:str, style_assets:dict, style_name:str):
	exec(f'{button_location}.{button}.configure(image=ctk.CTkImage(light_image=Image.open("assets/styles/{style_name}/{style_assets[button]["image"]}"), dark_image=Image.open("assets/styles/{style_name}/{style_assets[button]["image"]}"), size=(170, 50)))')

def button_down(self, button:str, button_location:str, style_assets:dict, style_name:str):
	exec(f'{button_location}.{button}.configure(image=ctk.CTkImage(light_image=Image.open("assets/styles/{style_name}/{style_assets[button]["image_down"]}"), dark_image=Image.open("assets/styles/{style_name}/{style_assets[button]["image_down"]}"), size=(170, 50)))')

#Classes

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

        self.homebutton = ctk.CTkButton(master=self, text="", corner_radius=0, hover_color="#1E1E1E", width=170, height=50, image=ctk.CTkImage(light_image=Image.open(f"assets/styles/{self.master.style_name}/assets/sidebar/HomeButton.png"), 
											 																										dark_image=Image.open(f"assets/styles/{self.master.style_name}/assets/sidebar/HomeButton.png"),
											 																										size=(170, 50)), fg_color="#1E1E1E")
        self.homebutton.bind('<ButtonRelease-1>', lambda event: self.master.homepage_button_function())
        self.homebutton.grid(row=0, column=0, padx=10, pady=(10, 0))

        self.friendsbutton = ctk.CTkButton(master=self, text="", corner_radius=0, hover_color="#1E1E1E", width=170, height=50, image=ctk.CTkImage(light_image=Image.open(f"assets/styles/{self.master.style_name}/assets/sidebar/HomeButton.png"), 
											 																										  dark_image=Image.open(f"assets/styles/{self.master.style_name}/assets/sidebar/FriendsButton.png"),
											 																										  size=(170, 50)), fg_color="#1E1E1E")
        self.friendsbutton.bind('<ButtonRelease-1>', lambda event: self.master.friends_button_function())
        self.friendsbutton.grid(row=1, column=0, padx=10)

        self.installationsbutton = ctk.CTkButton(master=self, text="", corner_radius=0, hover_color="#1E1E1E", width=170, height=50, image=ctk.CTkImage(light_image=Image.open(f"assets/styles/{self.master.style_name}/assets/sidebar/InstallationsButton.png"), 
											 																										  dark_image=Image.open(f"assets/styles/{self.master.style_name}/assets/sidebar/InstallationsButton.png"),
											 																										  size=(170, 50)), fg_color="#1E1E1E")
        self.installationsbutton.bind('<ButtonRelease-1>', lambda event: self.master.installations_button_function())
        self.installationsbutton.grid(row=2, column=0, padx=10)

        self.settingsbutton = ctk.CTkButton(master=self, text="Settings", corner_radius=0)
        self.settingsbutton.bind('<ButtonRelease-1>', lambda event: self.master.settings_button_function())
        self.settingsbutton.grid(row=3, column=0, sticky=ctk.S, pady=90, padx=10)

        self.customisebutton = ctk.CTkButton(master=self, text="Customisation", corner_radius=0)
        self.customisebutton.bind('<ButtonRelease-1>', lambda event: self.master.customise_button_function())
        self.customisebutton.grid(row=3, column=0, sticky=ctk.S, pady=50, padx=10)

        #self.accountswidget = SBarAccountWidget(master=self)
        #self.accountswidget.grid(row=4, column=0, sticky=ctk.S)

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

		self.bannerimage = ctk.CTkImage(light_image=Image.open(f"assets/styles/{self.master.style_name}/assets/homepage/banner.png"), 
											 dark_image=Image.open(f"assets/styles/{self.master.style_name}/assets/homepage/banner.png"),
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

		self.style_name = "default"

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

		self.sidebar = Sidebar(master=self, fg_color="#1E1E1E")

		self.music_player = AudioPlayerClass(f"assets/styles/{self.style_name}/music/music.wav")

		style, self.style_assets = styles_loader.load_style(json_path="assets/styles/default/style.json")
		for arg in style:
			print(arg)
			exec(arg)
			self.sidebar.update()
			self.homepage.update()

		self.homepage.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")
		self.sidebar.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

		self.homepage_button_function()

	def music_loop(self):
		self.music_player.play_audio()
		self.after(self.music_player.length+2000, self.music_loop)

	def homepage_button_function(self):
		self.homepage.show()
		button_down(self=self, button="homebutton", button_location="self.sidebar", style_name=self.style_name, style_assets=self.style_assets)
		button_up(self=self, button="friendsbutton", button_location="self.sidebar", style_name=self.style_name, style_assets=self.style_assets)
		button_up(self=self, button="installationsbutton", button_location="self.sidebar", style_name=self.style_name, style_assets=self.style_assets)

	def friends_button_function(self):
		self.homepage.hide()
		button_down(self=self, button="friendsbutton", button_location="self.sidebar", style_name=self.style_name, style_assets=self.style_assets)
		button_up(self=self, button="homebutton", button_location="self.sidebar", style_name=self.style_name, style_assets=self.style_assets)
		button_up(self=self, button="installationsbutton", button_location="self.sidebar", style_name=self.style_name, style_assets=self.style_assets)

	def installations_button_function(self):
		self.homepage.hide()
		button_down(self=self, button="installationsbutton", button_location="self.sidebar", style_name=self.style_name, style_assets=self.style_assets)
		button_up(self=self, button="homebutton", button_location="self.sidebar", style_name=self.style_name, style_assets=self.style_assets)
		button_up(self=self, button="friendsbutton", button_location="self.sidebar", style_name=self.style_name, style_assets=self.style_assets)

	def settings_button_function(self):
		self.homepage.hide()
		self.sidebar.homebutton.configure(image=ctk.CTkImage(light_image=Image.open(f"assets/styles/{self.style_name}/assets/sidebar/HomeButton.png"), 
			dark_image=Image.open(f"assets/styles/{self.style_name}/assets/sidebar/HomeButton.png"),
			size=(170, 50)))
		self.sidebar.homebutton.configure(image=ctk.CTkImage(light_image=Image.open(f"assets/styles/{self.style_name}/assets/sidebar/HomeButton.png"), 
			dark_image=Image.open(f"assets/styles/{self.style_name}/assets/sidebar/HomeButton.png"),
			size=(170, 50)))
		self.sidebar.homebutton.configure(image=ctk.CTkImage(light_image=Image.open(f"assets/styles/{self.style_name}/assets/sidebar/HomeButton.png"), 
			dark_image=Image.open(f"assets/styles/{self.style_name}/assets/sidebar/HomeButton.png"),
			size=(170, 50)))

	def customise_button_function(self):
		self.homepage.hide()
		self.sidebar.homebutton.configure(image=ctk.CTkImage(light_image=Image.open(f"assets/styles/{self.style_name}/assets/sidebar/HomeButton.png"), 
			dark_image=Image.open(f"assets/styles/{self.style_name}/assets/sidebar/HomeButton.png"),
			size=(170, 50)))
		self.sidebar.homebutton.configure(image=ctk.CTkImage(light_image=Image.open(f"assets/styles/{self.style_name}/assets/sidebar/HomeButton.png"), 
			dark_image=Image.open(f"assets/styles/{self.style_name}/assets/sidebar/HomeButton.png"),
			size=(170, 50)))
		self.sidebar.homebutton.configure(image=ctk.CTkImage(light_image=Image.open(f"assets/styles/{self.style_name}/assets/sidebar/HomeButton.png"), 
			dark_image=Image.open(f"assets/styles/{self.style_name}/assets/sidebar/HomeButton.png"),
			size=(170, 50)))

	def play_button_function(self):
		launch()