from tkinter import * 
#Importar libreria matplotlib para mostrar gráficos de la contabilizacion de predicción
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from pandas import DataFrame

root = Tk()
#root.configure(background='black')
root.geometry('700x400')
root.title("Formulario con Gráfico de Barras - Tkinter (Surflaweb")

framecontenedor = Frame(width="600", height="130", bg="#28E469")
framecontenedor.pack(side="top", anchor='n', padx=1, pady=1)

A = 0
B = 0
C = 0

def procesar():
	global A
	global B
	global C

	x1 = entry_clasea.get()
	x2 = entry_claseb.get()
	x3 = entry_clasec.get()

	A = int(int(x1) + A)
	B = int(int(x2) + B)
	C = int(int(x3) + C)
	
	actualizarGraficoBarras();
	actualizarGraficoCircular();

def actualizarGraficoBarras():
	global A
	global B
	global C
	
	global barras
	barras.clear()
	#crear dataframe
	Data1 = {'Clases': ['A','B','C'], 'Encuesta': [A, B, C]}
	df1 = DataFrame(Data1, columns= ['Clases', 'Encuesta'])
	df1 = df1[['Clases', 'Encuesta']].groupby('Clases').sum()
	#Agregar data al grafico de barras	
	df1.plot(kind='bar', legend=True, ax=barras)
	barras.set_title('Encuesta de Clases')
	bar1.draw()

def actualizarGraficoCircular():
	global A
	global B
	global C
	labels = 'A', 'B', 'C'
	sizes = [A, B, C]
	explode = (0, 0.1, 0)
	#Variable que tiene grafico circular
	global circulo
	circulo.clear()
	circulo.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
	circulo.set_title("Gráfico Circular - Clases Socioeconómicas")
	#refrescar gráfico circular:
	pie1.draw()

#-------- Sección Número 1
label_clasea = Label(framecontenedor, text="Clase A:",width=20,font=("bold", 10), bg="#28E469")
label_clasea.place(x=20,y=8)

entry_clasea = Entry(framecontenedor)
entry_clasea.place(x=140,y=10)

#-------- Sección Número 2
label_claseb = Label(framecontenedor, text="Clase B:",width=20,font=("bold", 10), bg="#28E469")
label_claseb.place(x=20,y=40)

entry_claseb = Entry(framecontenedor)
entry_claseb.place(x=140,y=40)

#-------- Sección Número 3
label_clasec = Label(framecontenedor, text="Clase C:",width=20,font=("bold", 10), bg="#28E469")
label_clasec.place(x=20,y=66)

entry_clasec = Entry(framecontenedor)
entry_clasec.place(x=140,y=70)

#------- Sección Botón
Button(framecontenedor, text='Procesar', width=20, bg='brown', fg='white', command=procesar).place(x=120,y=105)

#------- Sección Gráficos
framegraficos = Frame(bg="#949292", width="215", height="620")
framegraficos.pack (side="bottom", anchor='n',padx=1,pady=1)

#Gráfico 
#valores iniciales para el gráfico de barras:
Data1 = {'Clases': ['A','B','C'], 'Encuesta': [0,0,0]}
df1 = DataFrame(Data1, columns= ['Clases', 'Encuesta'])
df1 = df1[['Clases', 'Encuesta']].groupby('Clases').sum()

#Crear Gráfico de barras:
grafico1 = plt.Figure(figsize=(6,5), dpi=50)
barras = grafico1.add_subplot(111)
bar1 = FigureCanvasTkAgg(grafico1, framegraficos)
bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
df1.plot(kind='bar', legend=True, ax=barras)
barras.set_title('Encuesta de Clases')

#Grafico #2
#Valores iniciales para grafico "pie/pastel" circular
labels = 'A', 'B', 'C'
sizes = [0, 0, 0]
explode = (0, 0.1, 0)
#crear grafico circular/pastel
grafico2 = plt.Figure(figsize=(6,5), dpi=50)
circulo = grafico2.add_subplot(111)
circulo.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
pie1 = FigureCanvasTkAgg(grafico2, framegraficos) 
pie1.get_tk_widget().pack()
circulo.set_title("Gráfico Circular - Clases Socioeconómicas")

#root.resizable(0,0)
root.mainloop()