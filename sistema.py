from tkinter import *

root = Tk()
root.geometry('500x500')
root.title("Sistema de Clasificación de Morosidad CIP-TESIS")

#variables que tiene el valor de los combobox/option menu
estadocivil = ""
tiposeguro = ""
especialidad = ""
categoria = ""
estadopago = ""

def procesar():
	global estadocivil
	global tiposeguro
	global especialidad
	global categoria
	global estadopago

	genero = vargenero.get()
	print("genero: " +str(genero))
	print("estado civil: "+str(estadocivil))
	print("edad: "+str(entry_edad.get()))
	print("Nro de Hijos: "+str(entry_hijos.get()))
	print("Tipo de Seguro: "+str(tiposeguro))
	print("Tipo de Especialidad: "+str(especialidad))
	print("Categoria: "+str(categoria))
	print("Estado de Pago: "+str(estadopago))

def callback_ecivil(selection):
	global estadocivil
	estadocivil = selection

def callback_tiposeguro(selection):
	global tiposeguro
	tiposeguro = selection

def callback_especialidad(selection):
	global especialidad
	especialidad = selection

def callback_categoria(selection):
	global categoria
	categoria = selection

def callback_estadopago(selection):
	global estadopago
	estadopago = selection



label_0 = Label(root, text="Verificar Moroso",width=20,font=("bold", 20))
label_0.place(x=10,y=10)

#-------- Sección Género 
label_genero = Label(root, text="Género:",width=20,font=("bold", 10))
label_genero.place(x=40,y=50)

vargenero = IntVar()
Radiobutton(root, text="Masculino",padx = 5, variable=vargenero, value=1).place(x=150,y=50)
Radiobutton(root, text="Femenino",padx = 20, variable=vargenero, value=2).place(x=240,y=50)

#-------- Sección Estado Civil
label_estadocivil = Label(root, text="Estado Civil:",width=20,font=("bold", 10))
label_estadocivil.place(x=25,y=80)

list1 = ['Soltero','Casado','Divorsiado'];
c = StringVar()
droplist = OptionMenu(root,c, *list1, command=callback_ecivil)
droplist.config(width=15)
c.set('Estado Civil:') 
droplist.place(x=155,y=75)

#-------- Sección Edad
label_edad = Label(root, text="Edad:",width=20,font=("bold", 10))
label_edad.place(x=45,y=110)

entry_edad = Entry(root)
entry_edad.place(x=155,y=110)

#-------- Sección Número de Hijos
label_hijos = Label(root, text="Número de Hijos:",width=20,font=("bold", 10))
label_hijos.place(x=12,y=140)

entry_hijos = Entry(root)
entry_hijos.place(x=155,y=140)

#-------- Sección Tipo de Seguro
label_estadocivil = Label(root, text="Tipo de Seguro:",width=20,font=("bold", 10))
label_estadocivil.place(x=17,y=173)

list2 = ['EPS',
		'ESSALUD',
		'MAPFRE EPS',
		'ONCOSALUD',
		'PACIFICO EPS',
		'PACIFICO SEGUROS',
		'POSITIVA SEGUROS',
		'RIMAC EPS',
		'RIMAC SEGUROS',
		'SANIDADES',
		'SANITAS EPS',
		'SANITAS PERU EPS',
		'SIN REGISTROS',
		'SIS'];

c = StringVar()
droplist=OptionMenu(root,c, *list2, command=callback_tiposeguro)
droplist.config(width=15)
c.set('Tipo de Seguro:') 
droplist.place(x=155,y=170)

#-------- Sección Especialidad
label_estadocivil = Label(root, text="Especialidad:",width=20,font=("bold", 10))
label_estadocivil.place(x=25,y=213)

list3 = ['AGRICOLA',
	'AGROINDUSTRIAL Y COMERCIO EXTERIOR',
	'AGRONOMA',
	'AGRONOMICA',
	'AGRONOMO',
	'AMBIENTAL',
	'CIVIL',
	'CIVIL AMBIENTAL',
	'COMPUTACION E INFORMATICA',
	'DE COMPUTACION Y SISTEMAS',
	'DE SISTEMAS',
	'DE SISTEMAS Y COMPUTACION',
	'ELECTRICISTA',
	'ELECTRONICO',
	'EN COMPUTACION E INFORMATICA',
	'EN INDUSTRIAS ALIMENTARIAS',
	'FORESTAL',
	'INDUSTRIAL',
	'INDUSTRIAL Y DE SISTEMAS',
	'INFORMATICA Y DE SISTEMAS',
	'INFORMATICO Y DE SISTEMAS',
	'INGENIERIA ALIMENTARIA',
	'INGENIERIA CIVIL AMBIENTAL',
	'INGENIERIA DE SISTEMAS',
	'MECANICO',
	'MECANICO ELECTRICISTA',
	'MECANICO ELECTRICO',
	'MECANICO Y ELECTRICISTA',
	'OTROS',
	'PESQUERA',
	'QUIMICA',
	'QUIMICO',
	'SISTEMAS Y COMPUTACION',
	'ZOOTECNIA',
	'ZOOTECNISTA'];
c = StringVar()
droplist=OptionMenu(root, c, *list3, command=callback_especialidad)
droplist.config(width=15)
c.set('Especialidad:') 
droplist.place(x=155,y=210)

#-------- Sección Categoria
label_categoria = Label(root, text="Categoría:",width=20,font=("bold", 10))
label_categoria.place(x=34, y=250)

list4 = ['Ordinario','Vitalicio'];
c = StringVar()
droplist=OptionMenu(root, c, *list4, command=callback_categoria)
droplist.config(width=15)
c.set('Ordinario/Vitalicio') 
droplist.place(x=155,y=245)

#-------- Sección Pago Tiempo
label_pago = Label(root, text="Estado de Pago:",width=20,font=("bold", 10))
label_pago.place(x=15, y=283)

list5 = ['NO PAGO','PAGO DESTIEMPO', 'PAGO TIEMPO'];
c=StringVar()
droplist=OptionMenu(root,c, *list5, command=callback_estadopago)
droplist.config(width=15)
c.set('Seleccionar Estado:') 
droplist.place(x=155,y=280)

#------- Sección Botón
Button(root, text='Procesar', width=20, bg='brown', fg='white', command=procesar).place(x=150,y=320)


root.mainloop()