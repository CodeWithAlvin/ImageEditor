from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter import messagebox
from PIL import ImageTk,Image
from Backend import * 


class GUI(Tk):
	def __init__(self):
		#setting some variables
		self.VALUES={'CONTRAST':5,'COLOR':5,'BRIGHTNESS':5,'SHARPNESS':5}
		
		super().__init__()
		self.export_path="/storage/emulated/0/AlvinPhotoShop/"
		try:
			os.mkdir("/storage/emulated/0/AlvinPhotoShop")
		except:
			None
		self.config(bg="black")		
		self.title("Alvin's PhotoShop")
		self.sc_height=self.winfo_screenheight()
		self.sc_width=self.winfo_screenwidth()
                self.geometry(f"{self.sc_width}x{self.sc_height}")
	 			
	def CanvasWindow(self):
		self.canvas=Canvas(self,width=1030,height=1600,bg="grey")	
		self.canvas.pack(fill='x',padx=20,pady=20)
		
	def EditingBar(self):
		#=========creating Editing menu=========#
		self.EditingMenu=Menu(self)
		self.EditingMenu.add_command(label="Open",command=self.OpenPanel)
		self.EditingMenu.add_command(label="Color",command=lambda:self.OpenScale("Color"))
		self.EditingMenu.add_command(label="Contrast",command=lambda:self.OpenScale("Contrast"))
		self.EditingMenu.add_command(label="Brightness",command=lambda:self.OpenScale("Brightness"))
		self.EditingMenu.add_command(label="Sharpness",command=lambda:self.OpenScale("Sharpness"))
		self.EditingMenu.add_command(label="Clear",command=lambda:self.ShowImage(self.imgpath))
		self.EditingMenu.add_command(label="Filters")
		self.EditingMenu.add_command(label="Save",command=lambda : self.Save(image=self.pic,path=self.export_path,originalSize=[self.width,self.height]))		
		#=========configing Menu===========#
		self.config(menu=self.EditingMenu)	
	
	#Handling Scale Here
	def OpenScale(self,name):
		try:
			self.scale.destroy()
			self.btn.destroy()
		except:
			None
		self.scale=Scale(self,from_=0,to=10,orient=HORIZONTAL)
		self.btn=Button(text="Update",command=lambda : self.CallBackend(name))
		self.scale.pack(anchor="n",ipadx=840,side="top")
		self.scale.set(self.VALUES.get(name.upper()))
		self.btn.pack()
	
	#Calling the Backend to Process Image
	def CallBackend(self,name):
		 #getting value from dict
		 self.VALUES[name.upper()]=self.scale.get()
		 #Running Editors for image
		 img=Image.open(self.imgpath)
		 first=ManualEdits(img).Contrast(self.VALUES.get('CONTRAST')/5)
		 second=ManualEdits(first).Color(self.VALUES.get('COLOR')/5)
		 third=ManualEdits(second).Sharpness(self.VALUES.get('SHARPNESS')/5)
		 fourth=ManualEdits(third).Brightness(self.VALUES.get('BRIGHTNESS')/5)
		 self.ShowImage(fourth)
		 
	#Halding Image Showing
	def ShowImage(self,img):
		if type(img) == str:
			self.pic=Image.open(img)
			#Doing all the value as defualt
			for i in self.VALUES.keys():
				self.VALUES[i]=5
		else:
			self.pic=img
		self.img = ImageTk.PhotoImage(self.Resize(self.pic))
		self.canvas.create_image((self.sc_width-80)/2,(self.sc_height-430)/2,image=self.img)
		
	
	#Opens Panel for Upload Image
	def OpenPanel(self):
		self.imgpath=askopenfile(mode='r',title="Choose an Image" ,filetypes=[('Select an Image', '.jpg  .png .jpeg')],initialdir="/storage/emulated/0/").name
		self.ShowImage(str(self.imgpath))
		
	
	#Resizing Image to fit frame
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
				x=1600/self.height
				new_width=self.width*x
		new_image=image.resize((int(new_width),int(new_height)),Image.ANTIALIAS)
		return new_image

	# save the image

	def Save(self,image,path,originalSize):
		try:
			new_image=image.resize((int(originalSize[0]),int(originalSize[1])),Image.ANTIALIAS)
			new_image.save(path+str(time.time()).replace(".","")+".jpg")
			#Pops up message
			messagebox.showinfo("Success","Your Image have been Saved")
		except:
			messagebox.showinfo("Failed","An error Occured Please try again")
			

