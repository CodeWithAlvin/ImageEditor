from tkinter import *
from tkinter.filedialog import askopenfile
import os 
from PIL import ImageTk,Image



class GUI(Tk):
	def __init__(self):
		super().__init__()
		self.config(bg="black")
		self.geometry("1040x1900")
		self.title("Alvin's PhotoShop")
	 
	def Menu(self):
		#=========creating main menu=========#
		self.mainMenu=Menu(self)
		
		#========creating sub menus==========#
		self.m1=Menu(self.mainMenu)

		self.mainMenu.add_cascade(label="Files",menu=self.m1)
		self.mainMenu.add_command(label="Export")

		#====adding command in menu m1=====#
		self.m1.add_command(label="Open",command=self.HackImage)
		self.m1.add_command(label="Settings")
		self.m1.add_command(label="Clear",command=lambda: canvas.delete("all"))
		
		#=========configing Menu===========#
		self.config(menu=self.mainMenu)
	
	def CanvasWindow(self):
		self.canvas=Canvas(self,width=1040,height=1700,bg="white")	
		self.canvas.pack()
		

	#Functions 
	def HackImage(self):	
		self.image=askopenfile(mode='r', filetypes=[('Select an Image', '.jpg  .png .jpeg')])
		self.pic=Image.open(self.image.name)
		self.img = ImageTk.PhotoImage(self.pic)
		self.canvas.create_image(0,0,anchor="nw",image=self.img)
		

if __name__=="__main__":
	app=GUI()
	
	#runnings methods
	app.Menu()
	app.CanvasWindow()
	
	#running mainloop
	app.mainloop()
	
