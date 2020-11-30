from PIL import Image,ImageEnhance
import time

class ManualEdits:
	def __init__(self,image):
		self.image=image
		
	def Brightness(self,value):
		initial=Image.open(self.image)
		Middle=ImageEnhance.Brightness(initail)
		final=Middle.enhance(value)
		return final

	def Sharpness(self,value):
		initial=Image.open(self.image)
		Middle=ImageEnhance.Sharpness(initail)
		final=Middle.enhance(value)
		return final		
	
	def Color(self,value):
		initial=Image.open(self.image)
		Middle=ImageEnhance.Color(initail)
		final=Middle.enhance(value)
		return final

	def Contrast(self,value):
		initial=Image.open(self.image)
		Middle=ImageEnhance.Contrast(initail)
		final=Middle.enhance(value)
		return final


class Save:
	def __init__(self,image,path):
		image.save(str(time.time).replace(".","")+".jpg")



