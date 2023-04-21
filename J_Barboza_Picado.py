from tkinter import *
import time
import random
import pygame
import os

global puntos
puntos = 0

def cargar_imagen(nombre):
	ruta = os.path.join('img', nombre)
	imagen = PhotoImage(file = ruta)
	return imagen


class PantallaPresentacion():
	def __init__(self, master):
		self.canvas = Canvas( master, width=1000, height=500, highlightthickness=0, relief="ridge" )
		self.canvas.place(x=0, y=0)

		self.label_Presentacion = Label( self.canvas, text="Space Game")
		self.label_Presentacion.place(x=100, y=50)

		self.button_jugar = Button( self.canvas, text="Jugar", command=self.iniciar_juego )
		self.button_jugar.place(x=100, y=100)



	def iniciar_juego(self):
		#https://stackoverflow.com/questions/42393916/how-can-i-play-multiple-sounds-at-the-same-time-in-pygame
		#pygame.mixer.Channel(0).play(pygame.mixer.Sound("./audio/soundtrack.mp3"))
		PantallaJuego()

class PantallaJuego():
	def __init__(self):
		
		self.canvas = Canvas( window, width=1000, height=500, highlightthickness=0, relief="ridge" )
		self.canvas.pack()
		#https://stackoverflow.com/questions/20446782/how-to-hide-or-disable-the-mouse-pointer-in-tkinter
		self.canvas.config(cursor="none")
		#https://www.geeksforgeeks.org/how-to-use-images-as-backgrounds-in-tkinter/
		self.bg = PhotoImage(file="./img/bg.png").zoom(2,2)
		self.canvas.create_image( 0, 0, image = self.bg, anchor = "nw")

		self.label_puntos = Label(self.canvas, text=f"{puntos}", font=("Helventica", 30) )
		self.label_puntos.place(x=900,y=10)

		self.img = PhotoImage(file="./img/nave2.png")
		self.alien_Img = self.img
		self.alien = self.canvas.create_image(50, 250, image=self.alien_Img)
		self.alien2_x = random.randint(30, 970)
		self.alien2_y = random.randint(70,480)

		self.alien3_x = random.randint(30, 970)
		self.alien3_y = random.randint(70,480)

		self.alien4_x = random.randint(30, 970)
		self.alien4_y = random.randint(70,480)

		self.alien5_x = random.randint(30, 970)
		self.alien5_y = random.randint(70,480)



		self.alien3 = self.canvas.create_image( self.alien3_x, self.alien3_y, image=self.alien_Img)
		self.alien4 = self.canvas.create_image( self.alien4_x, self.alien4_y, image=self.alien_Img)
		self.alien5 = self.canvas.create_image( self.alien5_x, self.alien5_y, image=self.alien_Img)


		#https://pythonguides.com/python-tkinter-image/#Python_Tkinter_Image_Size
		#self.img1 = cargar_imagen("nave.png").subsample(10,10)
		#self.label_img = Label(self.canvas, image=self.img1)
		#self.label_img.place(x=0, y=10, width=70, height=70)
		#self.canvas.create_image(0,0, image=self.img1, anchor=NW)
		
		#self.nave_jugador = nave(10,10, self.canvas)
		#print(self.nave_jugador.x)

		#self.button_jugar = Button( self.canvas, text="Jugar", command=self.disparar )
		#self.button_jugar.place(x=100, y=100)


		window.bind("<a>", self.leftKey)
		#window.bind("<KeyRelease-a>", self.keyRelease)
		window.bind("<d>", self.rightKey)
		window.bind("<w>", self.upKey)
		window.bind("<s>", self.downKey)
		window.bind("<k>", self.generate)
		window.bind("<space>", self.disparar)
		window.bind("<Motion>", self.mouse)
		#window.bind("<Button-1>", self.disparar)

	def generate(self, event):
		self.alien3_x = random.randint(30, 970)
		self.alien3_y = random.randint(70,480)

		self.alien4_x = random.randint(30, 970)
		self.alien4_y = random.randint(70,480)

		self.alien5_x = random.randint(30, 970)
		self.alien5_y = random.randint(70,480)
		self.alien3 = self.canvas.create_image( self.alien3_x, self.alien3_y, image=self.alien_Img)
		self.alien4 = self.canvas.create_image( self.alien4_x, self.alien4_y, image=self.alien_Img)
		self.alien5 = self.canvas.create_image( self.alien5_x, self.alien5_y, image=self.alien_Img)


	def mouse(self, event):
		#self.alien.set_focus()
		x1 = self.canvas.coords(self.alien)[0]
		y1 = self.canvas.coords(self.alien)[1]


		
		x2 = event.x - x1
		y2 = event.y - y1
		self.canvas.move(self.alien, x2,y2)


	def leftKey(self, event):
		#https://www.tutorialspoint.com/how-to-get-the-coordinates-of-an-object-in-a-tkinter-canvas
		x = self.canvas.coords(self.alien)[0]
		if x > 30:
			self.canvas.move(self.alien, -10,0)

	def rightKey(self, event):
		#https://www.tutorialspoint.com/how-to-get-the-coordinates-of-an-object-in-a-tkinter-canvas
		x = self.canvas.coords(self.alien)[0]
		if x < 970:
		 	self.canvas.move(self.alien, 10,0)


	def upKey(self, event):
		#https://www.tutorialspoint.com/how-to-get-the-coordinates-of-an-object-in-a-tkinter-canvas
		y = self.canvas.coords(self.alien)[1]
		if y > 70:
			self.canvas.move(self.alien, 0,-10)


	def downKey(self, event):
		#https://www.tutorialspoint.com/how-to-get-the-coordinates-of-an-object-in-a-tkinter-canvas
		y = self.canvas.coords(self.alien)[1]
		if y < 280:
			self.canvas.move(self.alien, 0,10)

	def disparar(self, event):
		#pygame.mixer.Channel(1).play(pygame.mixer.Sound("./audio/shot.mp3"))
		x = self.canvas.coords(self.alien)[0]
		y = self.canvas.coords(self.alien)[1]
		self.cuadro = Canvas( window, width=15, height=4, bg="#ffe305", highlightthickness=0, relief="ridge" )
		#self.cuadro.place( x=x+20, y=y+10)
		self.animar(x,y)


	def animar(self, x, y):
		# x=x+"ancho de nave", y=y+"parte del alto de nave"
		self.cuadro.place(x = x + 20, y= y - 2)
		window.update()
		time.sleep(0.01)
		global puntos
		x += 7
		if self.alien2_y - 20 < y < self.alien2_y + 20 and self.alien2_x - 50 < x < self.alien2_x -40:
			self.alien2_y = 0
			self.alien2_x = 0
			self.canvas.delete(self.alien2)
			self.cuadro.place_forget()
			puntos += 10
			self.label_puntos['text'] = f"{puntos}"

		elif self.alien3_y - 20 < y < self.alien3_y + 20 and self.alien3_x - 50 < x < self.alien3_x -40:
			self.alien3_y = 0
			self.alien3_x = 0
			self.canvas.delete(self.alien3)
			self.cuadro.place_forget()
			puntos += 10
			self.label_puntos['text'] = f"{puntos}"

		elif self.alien4_y - 20 < y < self.alien4_y + 20 and self.alien4_x - 50 < x < self.alien4_x -40:
			self.alien4_y = 0
			self.alie4_x = 0
			self.canvas.delete(self.alien4)
			self.cuadro.place_forget()
			puntos += 10
			self.label_puntos['text'] = f"{puntos}"

		elif self.alien5_y - 20 < y < self.alien5_y + 20 and self.alien5_x - 50 < x < self.alien5_x -40:
			self.alien5_y = 0
			self.alien5_x = 0
			self.canvas.delete(self.alien5)
			self.cuadro.place_forget()
			puntos += 10
			self.label_puntos['text'] = f"{puntos}"

		elif x < 1000:
			return self.animar(x,y)
		else:
			# https://stackoverflow.com/questions/44727258/unplace-all-widgets-from-canvas
			self.cuadro.place_forget()

class nave():
	def __init__(self, x, y, canvas):

		img1 = PhotoImage(file="nave.png")
		self.canvas = canvas
		self.x = x
		self.y = y
		print(self.x, y)


#https://stackoverflow.com/questions/19895877/tkinter-cant-bind-arrow-key-events




#https://youtu.be/djDcVWbEYoE
pygame.mixer.init()




window = Tk()
pantalla_presentacion = PantallaPresentacion( window )
#pantalla_presentacion = PantallaJuego( window )
window.title( "Space" )
window.minsize( 1000, 500 )
window.mainloop( )
