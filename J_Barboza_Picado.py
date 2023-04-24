from tkinter import *
import time
import random
import pygame

global pts_nivel, puntos
puntos = 0
pts_nivel = {
	"nivel1": 10,
	"nivel2": 20,
	"nivel3": 30
}


class PantallaPresentacion():
	def __init__(self, master):
		self.canvas = Canvas( master, width=1000, height=500, highlightthickness=0, relief="ridge", bg="#1a1a1a")
		self.canvas.place(x=0, y=0)

		#https://stackoverflow.com/questions/42393916/how-can-i-play-multiple-sounds-at-the-same-time-in-pygame
		pygame.mixer.Channel(0).play(pygame.mixer.Sound("./audio/StartMenu.mp3"), loops=-1)

		self.bg = PhotoImage(file="./img/bg2.png")
		self.canvas.create_image( 0, 0, image = self.bg, anchor = "nw")

		self.label_Presentacion = Label( self.canvas, text="Space Game", font=("Helventica", 26), fg="#f2f2f2", bg="#1d0a35")
		#https://stackoverflow.com/questions/18736465/how-to-center-a-tkinter-widget
		self.label_Presentacion.place(relx=0.5, y=50, anchor=CENTER)

		self.label_nombre = Label(self.canvas, text="Ingrese un nombre:", font=("Helventica", 16), fg="#f2f2f2", bg="#1d0a35")
		self.label_nombre.place(x=400, y=150, anchor=CENTER)
		self.entrada_nombre = Entry(self.canvas, font=("Helventica", 11))
		self.entrada_nombre.place( x=600, y=150, width=150, height=30, anchor=CENTER )
		self.entrada_nombre.focus()

		self.nivel_var = StringVar()
		# https://stackoverflow.com/questions/42845090/give-a-radio-button-a-default-value-in-tkinter-python
		self.nivel_var.set("nivel1")

		self.label_nivel = Label(self.canvas, text="Seleccione nivel de dificultad:", font=("Helventica", 16), fg="#f2f2f2", bg="#1d0a35")
		self.label_nivel.place(x=350, y=200, anchor=CENTER)

		self.radio_button1 = Radiobutton( self.canvas, text="1", variable=self.nivel_var, value="nivel1" , font=("Helventica", 11), fg="#f2f2f2", bg="#1d0030" )
		# https://www.tutorialspoint.com/python/tk_anchors.htm
		self.radio_button1.place( x=525, y=200, width=50, height=50, anchor=W)

		self.radio_button2 = Radiobutton( self.canvas, text="2", variable=self.nivel_var, value="nivel2", font=("Helventica", 11), fg="#f2f2f2", bg="#1d0030" )
		# https://www.tutorialspoint.com/python/tk_anchors.htm
		self.radio_button2.place( x=575, y=200, width=50, height=50, anchor=W)

		self.radio_button3 = Radiobutton( self.canvas, text="3", variable=self.nivel_var, value="nivel3", font=("Helventica", 11), fg="#f2f2f2", bg="#1d0030" )
		# https://www.tutorialspoint.com/python/tk_anchors.htm
		self.radio_button3.place( x=625, y=200, width=50, height=50, anchor=W)

		self.button_jugar = Button( self.canvas, text="Jugar",  font=("Helventica", 16), fg="#f2f2f2", bg="#1d0a35", command=self.iniciar_juego )
		self.button_jugar.place(relx=0.5, rely=0.5, anchor=CENTER)

		self.button_info = Button( self.canvas, text="Info",  font=("Helventica", 16), fg="#f2f2f2", bg="#1d0a35", command=self.pantalla_info )
		self.button_info.place(x=900, y=10)

	def iniciar_juego(self):
		nombre = self.entrada_nombre.get()
		nivel = self.nivel_var.get()
		global aliens
		global puntos
		global balas
		aliens = []
		puntos = 0

		print(nivel)
		# https://stackoverflow.com/questions/63251775/how-to-delete-and-recreate-a-canvas-tkinter-canvas
		self.canvas.destroy()
		PantallaJuego(nombre, nivel)

	def pantalla_info(self):
		nombre = self.entrada_nombre.get()
		self.canvas.destroy()
		PantallaInfo(nombre)

class PantallaJuego():
	def __init__(self, nombre, nivel):
		
		self.canvas = Canvas( window, width=1000, height=500, highlightthickness=0, relief="ridge" )
		self.canvas.pack()
		#https://stackoverflow.com/questions/20446782/how-to-hide-or-disable-the-mouse-pointer-in-tkinter
		self.canvas.config(cursor="fleur")
		#https://stackoverflow.com/questions/42393916/how-can-i-play-multiple-sounds-at-the-same-time-in-pygame
		pygame.mixer.Channel(0).play(pygame.mixer.Sound("./audio/MusicaJuego.mp3"), loops=-1)
		
		#https://www.geeksforgeeks.org/how-to-use-images-as-backgrounds-in-tkinter/
		self.bg = PhotoImage(file="./img/bg3.png")
		self.canvas.create_image( 0, 0, image = self.bg, anchor = "nw")

		self.button_inicio = Button( self.canvas, text="Volver", command=self.volver_inicio,  font=("Helventica", 16), fg="#f2f2f2", bg="#1d0a35", cursor="hand1" )
		self.button_inicio.place(x=50, y=10)

		self.label_puntos = Label(self.canvas, text=f"{puntos}", font=("Helventica", 30), bg="#1b022a", fg="#f2f2f2" )
		self.label_puntos.place(x=900,y=10)


		self.label_dificult = Label(self.canvas, text=f"Dificultad: {pts_nivel[nivel]//10}", height=200, width=500, font=("Helventica", 30), bg="#1b022a", fg="#f2f2f2" )
		self.label_dificult.place(relx=0.5, rely=0.5, anchor=CENTER)
		window.update()
		time.sleep(1)
		self.label_dificult.place_forget()
		
		self.label_restantes = Label(self.canvas, text=f"", font=("Helventica", 10), bg="#1b022a", fg="#f2f2f2" )
		self.label_restantes.place(x=750,y=10)

		self.label_nombre = Label(self.canvas, text=f"{nombre}", font=("Helventica", 30), bg="#1b022a", fg="#f2f2f2" )
		self.label_nombre.place(relx=0.5,y=30, anchor=CENTER)

		self.img = PhotoImage(file="./img/nave2.png")
		self.img_nave = self.img
		self.alien = self.canvas.create_image(50, 250, image=self.img_nave)

		self.img1 = PhotoImage(file="./img/alien.png")
		self.img_alien = self.img1

		self.generate(None, pts_nivel[nivel]//3, 0, nivel)

		self.canvas.bind("<Motion>", self.mouse)
		self.canvas.bind("<Button-1>", self.disparar)

	def volver_inicio(self):
		# https://stackoverflow.com/questions/63251775/how-to-delete-and-recreate-a-canvas-tkinter-canvas
		self.canvas.destroy()
		PantallaPresentacion(window)


	def generate(self, event, num, i, nivel):
		global aliens
		self.aliens = aliens
		if i == num:
			return print(aliens)
		else:
			random_x = random.randint(200, 970)
			random_y = random.randint(120,480)

			#https://www.delftstack.com/howto/python/python-string-to-variable-name/
			self.aliens += [[f"alien{i}" ,random_x, random_y, pts_nivel[nivel]]]
			self.aliens[i][0] = self.canvas.create_image( random_x, random_y, image=self.img_alien)
			self.label_restantes['text'] = f"Enemigos restantes:{len(self.aliens)}"
			return self.generate(None, num, i+1, nivel)

	def mouse(self, event):
		x1 = self.canvas.coords(self.alien)[0]
		y1 = self.canvas.coords(self.alien)[1]
		
		x2 = event.x - x1
		y2 = event.y - y1
		self.canvas.move(self.alien, x2,y2)

	def disparar(self, event):
		pygame.mixer.Channel(1).play(pygame.mixer.Sound("./audio/shot.mp3"))
		x = self.canvas.coords(self.alien)[0]
		y = self.canvas.coords(self.alien)[1]
		self.bala = Canvas( window, width=15, height=4, bg="#ffe305", highlightthickness=0, relief="ridge" )

		self.animar(x, y)
	
	def colision(self,x,y,i):
		global colide
		if i == len(self.aliens):
			return False
		elif self.aliens[i][2] - 30 < y < self.aliens[i][2] + 35 and self.aliens[i][1] - 50 < x < self.aliens[i][1] -40:
			colide = i
			return True
		else:
			return self.colision(x,y,i+1)


	def animar(self, x, y):
		# x=x+"ancho de nave", y=y+"parte del alto de nave"
		self.bala.place(x = x + 20, y= y - 2)
		global puntos
		self.puntos = puntos
		global colide
		window.update()
		time.sleep(0.01)
		x += 7
		if self.colision(x,y,0):
			self.canvas.delete(self.aliens[colide][0])
			self.bala.place_forget()
			puntos += self.aliens[0][3]

			self.label_puntos['text'] = f"{puntos}"
			# https://www.edureka.co/blog/python-list-remove/
			del self.aliens[colide]
			print(self.aliens)
			
			self.label_restantes['text'] = f"Enemigos restantes:{len(self.aliens)}"

		elif x < 1000:
			return self.animar(x,y)
		else:
			# https://stackoverflow.com/questions/44727258/unplace-all-widgets-from-canvas
			self.bala.place_forget()


img3 = None

class PantallaInfo():
	def __init__(self, nombre):
		self.canvas = Canvas( window, width=1000, height=500, highlightthickness=0, relief="ridge", bg="#2c2c2c" )
		self.canvas.pack()
		
		#https://stackoverflow.com/questions/42393916/how-can-i-play-multiple-sounds-at-the-same-time-in-pygame
		pygame.mixer.Channel(0).play(pygame.mixer.Sound("./audio/StartMenu.mp3"), loops=-1)

		# https://stackoverflow.com/questions/26479728/tkinter-canvas-image-not-displaying
		global img3
		img3 = PhotoImage(file="./img/foto.png")
		self.img_foto = img3
		self.foto = self.canvas.create_image(520, 60, image=self.img_foto, anchor=NW)
		window.update()
		
		self.label_itcr = Label(self.canvas, text="Instituto Tecnologico de Costa Rica", bg="#2c2c2c", fg="#f2f2f2", font=("Helventica", 12) )
		self.label_itcr.place(relx=0.5, y=30, anchor=E)
		
		self.label_carrera = Label(self.canvas, text="Ingenieria en computadores", bg="#2c2c2c", fg="#f2f2f2", font=("Helventica", 12) )
		self.label_carrera.place(relx=0.5, y=60, anchor=E)
		
		self.label_asignatura = Label(self.canvas, text="Taller de Programacion", bg="#2c2c2c", fg="#f2f2f2", font=("Helventica", 12) )
		self.label_asignatura.place(relx=0.5, y=90, anchor=E)
		
		self.label_profesor = Label(self.canvas, text="Luis Barboza", bg="#2c2c2c", fg="#f2f2f2", font=("Helventica", 12) )
		self.label_profesor.place(relx=0.4, y=120, anchor=W)
		self.label_profNom = Label(self.canvas, text="Profesor: ", bg="#2c2c2c", fg="#f2f2f2", font=("Helventica", 12) )
		self.label_profNom.place(relx=0.4, y=120, anchor=E)
		
		self.label_estudiante = Label(self.canvas, text="Joel Barboza", bg="#2c2c2c", fg="#f2f2f2", font=("Helventica", 12) )
		self.label_estudiante.place(relx=0.4, y=150, anchor=W)
		self.label_estNom = Label(self.canvas, text="Estudiante: ", bg="#2c2c2c", fg="#f2f2f2", font=("Helventica", 12) )
		self.label_estNom.place(relx=0.4, y=150, anchor=E)

		self.label_carne = Label(self.canvas, text="2023218734", bg="#2c2c2c", fg="#f2f2f2", font=("Helventica", 12) )
		self.label_carne.place(relx=0.4, y=180, anchor=W)
		self.label_carneNum = Label(self.canvas, text="Carné: ", bg="#2c2c2c", fg="#f2f2f2", font=("Helventica", 12) )
		self.label_carneNum.place(relx=0.4, y=180, anchor=E)
		
		self.label_year = Label(self.canvas, text="2023", bg="#2c2c2c", fg="#f2f2f2", font=("Helventica", 12) )
		self.label_year.place(relx=0.4, y=210, anchor=W)
		self.label_yearNom = Label(self.canvas, text="Año: ", bg="#2c2c2c", fg="#f2f2f2", font=("Helventica", 12) )
		self.label_yearNom.place(relx=0.4, y=210, anchor=E)
		
		self.label_pais = Label(self.canvas, text="Costa Rica", bg="#2c2c2c", fg="#f2f2f2", font=("Helventica", 12) )
		self.label_pais.place(relx=0.4, y=240, anchor=W)
		self.label_paisNom = Label(self.canvas, text="País: ", bg="#2c2c2c", fg="#f2f2f2", font=("Helventica", 12) )
		self.label_paisNom.place(relx=0.4, y=240, anchor=E)
		
		self.label_version = Label(self.canvas, text="v.1.0", bg="#2c2c2c", fg="#f2f2f2", font=("Helventica", 12) )
		self.label_version.place(relx=0.4, y=270, anchor=W)
		self.label_ver = Label(self.canvas, text="Versión: ", bg="#2c2c2c", fg="#f2f2f2", font=("Helventica", 12) )
		self.label_ver.place(relx=0.4, y=270, anchor=E)

		self.button_inicio = Button( self.canvas, text="Volver", command=self.volver_inicio,  font=("Helventica", 16), fg="#f2f2f2", bg="#1d0a35", cursor="hand1" )
		self.button_inicio.place(x=50, y=10)

	def volver_inicio(self):
		# https://stackoverflow.com/questions/63251775/how-to-delete-and-recreate-a-canvas-tkinter-canvas
		self.canvas.destroy()
		PantallaPresentacion(window)

#https://youtu.be/djDcVWbEYoE
pygame.mixer.init()


window = Tk()
pantalla_presentacion = PantallaPresentacion( window )
window.title( "Space" )
window.minsize( 1000, 500 )
window.mainloop( )
