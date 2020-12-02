from tkinter import *
from tkinter.filedialog import askopenfile
from PIL import ImageTk,Image
from Backend import * 


class GUI(Tk):
	def __init__(self):
		super().__init__()
		self.export_path="/storage/emulated/0/AlvinPhotoShop/"
		try:
			os.mkdir("/storage/emulated/0/AlvinPhotoShop")
		except:
			None
		self.config(bg="black")
		self.geometry("1038x1910")		
		self.title("Alvin's PhotoShop")
		self.sc_height=self.winfo_screenheight()
		self.sc_width=self.winfo_screenwidth()
	 			
	def CanvasWindow(self):
		self.canvas=Canvas(self,width=1030,height=1600,bg="grey")	
		self.canvas.pack(fill='x',padx=20,pady=20)
		
	def EditingBar(self):
		#=========creating Editing menu=========#
		self.EditingMenu=Menu(self)
		self.EditingMenu.add_command(label="Open",command=self.OpenPanel)
		self.EditingMenu.add_command(label="Crop",command=lambda:self.OpenScale("Crop"))
		self.EditingMenu.add_command(label="Contrast",command=lambda:self.OpenScale("Contrast"))
		self.EditingMenu.add_command(label="Brightness",command=lambda:self.OpenScale("Brightness"))
		self.EditingMenu.add_command(label="Sharpness",command=lambda:self.OpenScale("Sharpness"))
		self.EditingMenu.add_command(label="Clear")
		self.EditingMenu.add_command(label="Save",command=lambda : Save(image=self.pic,path=self.export_path,originalSize=[self.width,self.height]))		
		#=========configing Menu===========#
		self.config(menu=self.EditingMenu)	
		
	def OpenScale(self,name):
		try:
			self.scale.destroy()
			self.btn.destroy()
		except:
			None
		self.scale=Scale(self,from_=-10,to=10,orient=HORIZONTAL)
		self.btn=Button(text="Update",command=lambda : self.CallBackend(name))
		self.scale.pack(anchor="n",ipadx=840,side="top")
		self.btn.pack()
	
		
	def CallBackend(self,name):
		 if name=="Contrast":
		 	im=ManualEdits(self.pic).Contrast(self.scale.get())
		 elif name=="Color":
		 	im=ManualEdits(self.pic).Color(self.scale.get())
		 elif name=="Sharpness":
		 	im=ManualEdits(self.pic).Sharpness(self.scale.get())
		 elif name=="Brightness":
		 	im=ManualEdits(self.pic).Brightness(self.scale.get())
		 print(im)
		 self.ShowImage(im)
		 
		 
	def ShowImage(self,img):
		if type(img) == str:
			self.pic=Image.open(self.image)
		else:
			self.pic=img
		self.img = ImageTk.PhotoImage(self.Resize(self.pic))
		self.canvas.create_image((self.sc_width-80)/2,(self.sc_height-380)/2,image=self.img)

	def OpenPanel(self):
		self.image=askopenfile(mode='r', filetypes=[('Select an Image', '.jpg  .png .jpeg')]).name
		self.ShowImage(str(self.image))
		
	def Resize(self,image):
		#resizing without losing aspect ratio of image to fit frame
		self.width,self.height=image.size
		new_width=self.width
		new_height=self.height
		if self.width>1030 or self.height>1600:
			if self.width > self.height :
				new_width=1030
				x=1030/self.width
				new_height=self.height*x
			else:
				new_height=1600
				x=1700/self.height
				new_width=self.width*x
		new_image=image.resize((int(new_width),int(new_height)),Image.ANTIALIAS)
		return new_image


if __name__=="__main__":
	app=GUI()
		
	#runnings methods
	app.EditingBar()
	app.CanvasWindow()
	
	#running mainloop
	app.mainloop()