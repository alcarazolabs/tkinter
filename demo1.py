from tkinter import * 
from tkinter import font
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog as fd

#Inicializar la ventana principal:
root = Tk()
root.configure(background='black')
root.title("Clasificación Automática de Citrus Aurantifolia Usando Visión Artificial")

#Contenedor del formulario
frameform1 = Frame(bg="#28E469", width="215", height="500")
#Contenedor del formulario 2
frameform2 = Frame(bg="#28E469", width="215", height="500")

global nombres
global apellidos
global dni

def procesar():
	noms = nombres.get()


nombre_label= Label(frameform2, text="Cual es tu nombre:", bg="#28E469")
nombre_label.grid(row=1, column=0)
nombre_label.config(padx=10, pady=10)
cuadro_nombre = Entry(frameform2, textvariable=nombres)
cuadro_nombre.grid(row=1, column=1)

apellido_label= Label(frameform2, text="Cual es tu apellido:", bg="#28E469")
apellido_label.grid(row=2, column=0)
apellido_label.config(padx=10, pady=10)
cuadro_apellido=Entry(frameform2)
cuadro_apellido.grid(row=2, column=1)


dni_label= Label(frameform1, text="Cual es tu dni:", bg="#28E469")
dni_label.grid(row=1, column=0)
dni_label.config(padx=10, pady=10)
cuadro_dni=Entry(frameform1)
cuadro_dni.grid(row=1, column=1)

Button(frameform2, text = "Procesar",width = 10, height = 1, command = procesar).pack()

#Agregar frame al root
frameform1.pack(side="right", anchor="n", padx=10, pady=12)
frameform2.pack(side="right", anchor="n", padx=10, pady=12)

root.resizable(0,0)
root.mainloop()