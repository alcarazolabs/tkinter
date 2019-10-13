from tkinter import * 
from tkinter import font
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog as fd

#funcion para sumar los dos números
def suma():
	suma = int(entrada1.get())+int(entrada2.get())
	return var.set(suma)

def cerrar():
	ventana.destroy()

ventana = Tk()
ventana.title("Sumador")
ventana.geometry('380x300')
ventana.configure(background='dark turquoise')

#variables
var = StringVar()

#etiqueta
e1 = Label(ventana, text="Numero 1:", bg='pink', fg='white')
e1.pack(padx=5, pady=4, ipadx=5, ipady=5)
#lugar donde poner el numero 1
entrada1= Entry(ventana)
entrada1.pack(padx=5, pady=5, ipadx=5, ipady=5)


e2 = Label(ventana, text="Numero 2:", bg='pink', fg='white')
e2.pack(padx=5, pady=4, ipadx=5, ipady=5)
#lugar donde poner el numero 1
entrada2= Entry(ventana)
entrada2.pack(padx=5, pady=5, ipadx=5, ipady=5)

botonsuma = Button(ventana, text="Sumar", fg='blue', command=suma)
botonsuma.pack(side=TOP)

res = Label(ventana, bg='plum', textvariable=var, padx=5, pady=5, width=50)
res.pack()

botoncerrar = Button(ventana, text="Cerrar", fg='blue', command=cerrar)
botoncerrar.pack(side=TOP)


ventana.mainloop()