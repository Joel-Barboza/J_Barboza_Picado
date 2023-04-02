from tkinter import *


class PantallaPresentacion():
	def __init__(self, master):
		self.canvas = Canvas( master, width=500, height=300, highlightthickness=0, relief="ridge" )
		self.canvas.place(x=0, y=0)



window = Tk()
pantalla_presentacion = PantallaPresentacion( window )
window.title( "Space" )
window.minsize( 500, 300 )
window.mainloop( )
