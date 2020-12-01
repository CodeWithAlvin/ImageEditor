from GUI import *
from Backend import *
import tkinter



if __name__=="__main__":
	app=GUI()
		
	#runnings methods
	app.EditingBar()
	app.CanvasWindow()
	
	#running mainloop
	app.mainloop()