from tkinter import *
import time


class PantallaPresentacion():
	def __init__(self, master):
		self.canvas = Canvas( master, width=500, height=300, highlightthickness=0, relief="ridge" )
		self.canvas.place(x=0, y=0)

		self.label_Presentacion = Label( self.canvas, text="Space Game")
		self.label_Presentacion.place(x=100, y=50)

		self.button_jugar = Button( self.canvas, text="Jugar", command=self.iniciar_juego )
		self.button_jugar.place(x=100, y=100)

	def iniciar_juego(self):
		PantallaJuego()

class PantallaJuego():
	def __init__(self):
		
		self.canvas = Canvas( window, width=500, height=300, highlightthickness=0, relief="ridge" )
		self.canvas.place(x=0, y=0)

		self.nave_cuerpo = Canvas( window, width=30, height=10, bg="#2a2a2a", highlightthickness=0, relief="ridge")
		self.nave_cuerpo.place( x=20, y=20)
		self.nave_techo = Canvas( window, width=20, height=10, bg="#a2a2a2", highlightthickness=0, relief="ridge")
		self.nave_techo.place( x=25, y=15)


		self.button_jugar = Button( self.canvas, text="Jugar", command=self.disparar )
		self.button_jugar.place(x=100, y=100)

	def disparar(self):
		x=50
		self.cuadro = Canvas( window, width=15, height=10, bg="#a2a2a2", highlightthickness=0, relief="ridge" )
		self.cuadro.place( x=x, y=20)

		self.punta = Canvas( window, width=2, height=10, bg="#2a2a2a", highlightthickness=0, relief="ridge" )
		self.punta.place(x=x+11, y=20)
		
		self.animar(x)


	def animar(self, x):
		
		self.cuadro.place(x=x, y=20)
		self.punta.place(x=x+11, y=20)
		window.update()
		time.sleep(0.1)
		x += 5
		if x < 200:
			self.animar(x)
		else:
			self.punta.place_forget()
			self.cuadro.place_forget()
			## https://stackoverflow.com/questions/44727258/unplace-all-widgets-from-canvas




window = Tk()
pantalla_presentacion = PantallaPresentacion( window )
window.title( "Space" )
window.minsize( 500, 300 )
window.mainloop( )
