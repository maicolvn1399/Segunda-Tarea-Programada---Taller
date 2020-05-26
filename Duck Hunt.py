from tkinter import *
from tkinter import messagebox
import random
import time
import pygame
import time
import sys
import os
from threading import Thread

salmon = "#FA8072"
orangered = "#FF4500"
springgreen = "#00FF7F"
dodgerblue = "#1E90FF"
darkmagenta = "#8B008B"
mediumorchid = "#BA55D3"
hotpink = "#FF69B4"
chocolate = "#D2691E"
lime = "#00FF00"
green = "#008000"
yellow = "#FFFF00"
red = "#FF0000"
darkred = "#8B0000"
gold = "#FFD700"
orange = "#FFA500"
white = "#FFFFFF"
black = "#000000"

colores = [salmon,orangered,springgreen,dodgerblue,darkmagenta,mediumorchid,
                hotpink,chocolate,lime,green,yellow,red,darkred,gold,
                orange,white]

def cargarImagen(nombre):
     """Función que permite cargar una imagen"""
     ruta = os.path.join('Multimedia',nombre)
     imagen = PhotoImage(file=ruta)
     return imagen

def PlayMusic():
     pygame.mixer.init()#inicializa la función para reproducir archivos de audio
     pygame.mixer.music.load(os.path.join('Multimedia',"backgroundMusic.wav")) #Carga el archivo de audio para ser reproducido 
     pygame.mixer.music.play(loops=-1) #Reproduce el archivo
     



def DatosIngresados(nombre,cantidadBolas):
     if isinstance(nombre,str) and isinstance(cantidadBolas,str):
          if cantidadBolas.isdigit() and int(cantidadBolas) != 0:
               return VentanaJuego(nombre,int(cantidadBolas))
          else:
               return messagebox.showerror("Error","Debe ingresar un número válido")
     else:
          return messagebox.showerror("Error","Los datos ingresados son incorrectos")



def DatosJugador():
     #Aparece la primera pantalla del juego
     ventanaDatos = Tk()
     ventanaDatos.title("Datos del jugador")
     ventanaDatos.minsize(600,400)
     ventanaDatos.resizable(width=NO,height=NO)
     imagenFondo = cargarImagen("datosBackground.gif")
     labelFondo = Label(ventanaDatos, image=imagenFondo)
     labelFondo.place(x=0,y=0)
     labelDatoNombre = Label(ventanaDatos,text="Ingrese su nombre",font = "Fixedsys 16",bg="#b3a9c7")
     labelDatoNombre.place(x=100,y=200)
     labelCantidad = Label(ventanaDatos,text="Ingrese la cantidad de bolas",font = "Fixedsys 16",bg="#b3a9c7")
     labelCantidad.place(x=100,y=260)
     entryNombre = Entry(ventanaDatos,width=25)
     entryNombre.place(x=300,y=200)
     entryCantidad = Entry(ventanaDatos,width=16)
     entryCantidad.place(x=350,y=260)
     buttonAceptar = Button(ventanaDatos,text="Aceptar",fg="black",bg="#b3a9c7",font = "Fixedsys 13",command=lambda:DatosIngresados(str(entryNombre.get()),str(entryCantidad.get())))
     bienvenidaLabel = Label(ventanaDatos,text="BIENVENIDO/A",font = "Fixedsys 35",bg="#34a1eb")#Label de bienvenida
     bienvenidaLabel.place(x=100,y=50)
     buttonAceptar.place(x=200,y=300) 
     ventanaDatos.mainloop()

def AnimacionRecursiva(canvas,bola,velocidadx,velocidady,a):
        canvas.move(bola,velocidadx,velocidady)
        posicion=canvas.coords(bola) #toma la posición actual de la bola
        if posicion[3]>=400 or posicion[1]<=0:
            velocidady=-velocidady
        if posicion[2]>=800 or posicion[0]<=0:
            velocidadx=-velocidadx
        a.update()
        time.sleep(0.025)#comando que retarda el programa
        
        def Delete():
             canvas.delete(bola)


        def clickedBall(*args):
               print("Ball clicked")
               playShot()
               Delete()

        canvas.tag_bind(bola,"<Button-1>",clickedBall)#reconoce el click de la


        return AnimacionRecursiva(canvas,bola,velocidadx,velocidady,a)


def VentanaJuego(nombre,cantidadBolas):
     
    ventanaJuego=Toplevel()#crea una ventana
    MusicaFondo = Thread(target= PlayMusic)
    MusicaFondo.daemon = True
    MusicaFondo.start()
    ventanaJuego.minsize(800,400)# tamaño de ventana
    ventanaJuego.resizable(width=NO,height=NO)
    ventanaJuego.title("Juego")
    imagenFondo = cargarImagen("gameBackground1.gif")
    LabelFondo = Label(ventanaJuego, image=imagenFondo)
    LabelFondo.place(x=0,y=0,relwidth=1,height=1)
    LabelFondo.image = imagenFondo
    
    canvasJuego = Canvas(ventanaJuego, width=800, height=400,bg="#326fa8")#contenedor de la bola
    
    canvasJuego.grid()# divide la pantalla

    
    for i in range(cantidadBolas):
         velocidadx=random.randrange(2,8)# esta es la velocidad en el eje x
         velocidady=random.randrange(2,8) #Velocidad en eje y 
         x = random.randrange(0,800) #posicion en el eje x
         y = random.randrange(0,400) #posicion en el eje y 
         randomColor = random.choice(colores) #elige un color de la lista aleatorio
         
         bola=canvasJuego.create_oval(x,y,x+50,y+50,fill=randomColor) #crea la bola
         bola_thread = Thread(target= AnimacionRecursiva,args = (canvasJuego,bola,velocidadx,velocidady,ventanaJuego))
         bola_thread.daemon = True
         bola_thread.start()

         
    canvasJuego.pack()
     
    ventanaJuego.mainloop()

def playShot(*args):
     pygame.mixer.init()#inicializa la función para reproducir archivos de audio
     pygame.mixer.music.load(os.path.join('Multimedia',"shot.wav")) #Carga el archivo de audio para ser reproducido 
     pygame.mixer.music.play() #Reproduce el archivo




def ventanaGameOver():
     ventanaGameOver = Toplevel()
     ventanaGameOver.minsize(600,400)
     ventanaGameOver.resizable(width=NO,height=NO)
     ventanaGameOver.title("Perdió")
     imagenFondo = cargarImagen("gameOverBackground.gif")
     LabelFondo = Label(ventanaGameOver, image=imagenFondo)
     LabelFondo.place(x=0,y=0)
     gameOverLabel = Label(ventanaGameOver,text="Perdiste :(",font = "Fixedsys 35",bg="#34a1eb")#Label de bienvenida
     gameOverLabel.place(x=100,y=50)
     retryButton = Button(ventanaGameOver,text="Intentar otra vez",fg="black",bg="#b3a9c7",font = "Fixedsys 19",command=lambda: Datos())
     retryButton.place(x=200,y=200)

     ventanaGameOver.mainloop()
     
     
#ventanaGameOver() 
      
DatosJugador()
