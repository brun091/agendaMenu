#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
from json import loads
from json import dump


mainForm = tk.Tk()
mainForm.geometry("400x200")
mainForm.title("Ejemplo Menú")


def cargaDatos():
	person = {}
	
	person["Nombre"]= sd.askstring("Información", "Ingrese su nombre")
	person["Apellido"]= sd.askstring("Información", "Ingrese su apellido")
	person["Telefono"]= sd.askstring("Información", "Ingrese su N° de Telefono")
	
	with open("persona.json", "w") as fileOut:
		dump(person, fileOut)
		
def showData():
	vertical = 80
	
	person = loads(open("persona.json").read())

	for key, value in person.items():
		dataLanbel = tk.Label(mainForm, text = key + ": " + value)
		dataLanbel.place(x = 10, y = vertical)
		vertical +=20


mainMenu = tk.Menu(mainForm)
fileMenu = tk.Menu(mainMenu, tearoff = 0)
fileMenu.add_command(label = "Salir", command = quit) 

personMenu = tk.Menu(mainForm)
contactMenu = tk.Menu(mainMenu, tearoff = 1)
contactMenu.add_cascade(label = "Archivo", menu = fileMenu)
contactMenu.add_cascade(label = "Cargar personas", command = cargaDatos)
contactMenu.add_cascade(label = "Contactos", command = showData,)


mainForm.config(menu = mainMenu)

mainForm.mainloop()
