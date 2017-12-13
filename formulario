#!/usr/bin/env python3

import tkinter as tk

def otroFormulario():
	anotherForm = tk.Toplevel(mainForm)
	anotherForm.geometry("300x100")
	anotherForm.title("Este es otro formulario")

	miLabel = tk.Label(anotherForm, text = "Este es otro formulario")
	miLabel.place(x = 10, y = 10)

mainForm = tk.Tk()
mainForm.geometry("300x100")
mainForm.title("Este es otro formulario")

button = tk.Button(mainForm, text = "Abrir otro formulario", command = otroFormulario)
button.place(x = 10, y = 10)

mainForm.mainloop()
