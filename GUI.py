from tkinter import *
from tkinter.filedialog import askopenfile
import os 
from PIL import ImageTk,Image



class App:
	def __init__(self):
		self.root=Tk()
				
		#Setting Variables
		
		#Display Screen
		self.Settings()
		self.Menu()
		self.CanvasWindow()
		
		
		self.root.mainloop()
	
	def Settings(self):
		self.root.config(bg="black")
		self.root.geometry("1040x1900")
		self.root.title("Alvin's PhotoShop")
	 
	def Menu(self):
		#=========creating main menu=========#
		mainMenu=Menu(self.root)
		
		#========creating sub menus==========#
		m1=Menu(mainMenu)

		mainMenu.add_cascade(label="Files",menu=m1)
		mainMenu.add_command(label="Export")

		#====adding command in menu m1=====#
		m1.add_command(label="Open",command=self.HackImage)
		m1.add_command(label="Settings")
		m1.add_command(label="Clear",command=lambda: canvas.delete("all"))
		
		#=========configing Menu===========#
		self.root.config(menu=mainMenu)
	
	def CanvasWindow(self):
		self.canvas=Canvas(width=1040,height=1700,bg="white")
		self.canvas.pack()
		pic=Image.open("/storage/emulated/0/DCIM/Screenshots/IMG_20201126_084733.jpg")
		img = ImageTk.PhotoImage(pic)
		self.canvas.create_image(500,500,image=img)
		  	

	#Functions 
	def HackImage(self):	
		image=askopenfile(mode='r', filetypes=[('Select an Image', '.jpg  .png .jpeg')])
		pic=Image.open("/storage/emulated/0/DCIM/Screenshots/IMG_20201126_084733.jpg")
		img = ImageTk.PhotoImage(pic)
		self.canvas.create_image(500,500,anchor="nw",image=img)
		

App()
