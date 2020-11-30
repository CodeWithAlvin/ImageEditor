from tkinter import *
from tkinter.filedialog import askopenfile
import os 
from PIL import ImageTk,Image



class GUI(Tk):
	def __init__(self):
		super().__init__()
		self.config(bg="black")
		self.geometry("1038x1910")		
		self.title("Alvin's PhotoShop")
		self.sc_height=self.winfo_screenheight()
		self.sc_width=self.winfo_screenwidth()
	 	
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
		self.canvas=Canvas(self,width=1040,height=1700,bg="grey")	
		self.canvas.pack(fill='x',padx=20,pady=20)
		
	def EditingBar(self):
		#=========creating Editing menu=========#
		self.EditingMenu=Menu(self)
		
		#========creating sub menus==========#
		self.E1=Menu(self.EditingMenu)

		self.EditingMenu.add_command(label="Crop")
		self.EditingMenu.add_cascade(label="Contrast",menu=self.E1)
		self.EditingMenu.add_cascade(label="Brightness",menu=self.E1)
		self.EditingMenu.add_cascade(label="Sharpness",menu=self.E1)
		self.EditingMenu.add_cascade(label="Blur",menu=self.E1)
			

		#====adding command in menu m1=====#
		self.E1.add_command(label="Open",)
		self.E1.add_command(label="Settings")
		self.E1.add_command(label="Clear")
		
		#=========configing Menu===========#
		self.config(menu=self.EditingMenu)	
	
	#Functions 
	def HackImage(self):	
		self.image=askopenfile(mode='r', filetypes=[('Select an Image', '.jpg  .png .jpeg')])
		self.pic=Image.open(self.image.name)
		self.pic=self.pic.resize((self.sc_width-200 ,self.sc_height-400),Image.ANTIALIAS)
		self.img = ImageTk.PhotoImage(self.pic)
		self.canvas.create_image((self.sc_width-80)/2,(self.sc_height-380)/2,image=self.img)
		

if __name__=="__main__":
	app=GUI()
	
	#runnings methods
	app.Menu()
	app.CanvasWindow()
	app.EditingBar()
	#running mainloop
	app.mainloop()
	
