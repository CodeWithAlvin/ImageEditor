from PIL import Image,ImageEnhance
import time

class ManualEdits:
	def __init__(self,image):
		self.image=image
		
	def Brightness(self,value):
		try:
			initail=ImageEnhance.Brightness(self.image)
			final=initail.enhance(value)
			return final
		except:
			return self.image

	def Sharpness(self,value):
		try:
			initail=ImageEnhance.Sharpness(self.image)
			final=initail.enhance(value)
			return final	
		except:
			return self.image	
	
	def Color(self,value):
		try:
			initail=ImageEnhance.Color(self.image)
			final=initail.enhance(value)
			return final
		except:
			return self.image

	def Contrast(self,value):
		try:
			initail=ImageEnhance.Contrast(self.image)
			final=initail.enhance(value)
			return final
		except:
			return self.image




