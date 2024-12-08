import tkinter as tk


from Animales import Animal, animalAnfibios, animalReptiles


def siguienteAnimal():
    # Cambiar al siguiente animal
    if Animal.cont < len(listaAnimales) - 1:
        Animal.cont += 1
    else:
        Animal.cont = 0

    # Etiquetas generales
    lblEspecieData.config(text=listaAnimales[Animal.cont].especie)
    lblEdadMediaData.config(text=listaAnimales[Animal.cont].edadMedia)
    lblEnfComunesData.config(text=listaAnimales[Animal.cont].enfComunes)
    lblPesoMedioData.config(text=listaAnimales[Animal.cont].pesoMedio)
    lblDietaMediaData.config(text=listaAnimales[Animal.cont].dietaMedia)
    lblHabitatData.config(text=listaAnimales[Animal.cont].habitat)

    # Etiquetas específicas para anfibios y reptiles
    if isinstance(listaAnimales[Animal.cont], animalAnfibios):
        lblNumeroHuevosData.config(text=listaAnimales[Animal.cont].numeroHuevos)
        lblNumeroHuevos.grid(column=1, row=7)
        lblNumeroHuevosData.grid(column=2, row=7)
        lblNumeroEscamas.grid_forget()
        lblNumeroEscamasData.grid_forget()
    elif isinstance(listaAnimales[Animal.cont], animalReptiles):
        lblNumeroEscamasData.config(text=listaAnimales[Animal.cont].escamas)
        lblNumeroEscamas.grid(column=1, row=7)
        lblNumeroEscamasData.grid(column=2, row=7)
        lblNumeroHuevos.grid_forget()
        lblNumeroHuevosData.grid_forget()
    else:
        lblNumeroHuevos.grid_forget()
        lblNumeroHuevosData.grid_forget()
        lblNumeroEscamas.grid_forget()
        lblNumeroEscamasData.grid_forget()

    limpiarDatos()


def calcularKcal():

    try:
        peso = float(entPeso.get())
        dieta_media = listaAnimales[Animal.cont].dietaMedia
        kcal_necesarias = (peso ** 0.75)+dieta_media #Función para calcular las kcal
        lblResultado.config(text=f"La dieta media ha sido de: {kcal_necesarias:.2f} Kcal")
    except ValueError:
        lblResultado.config(text="Introduce un peso válido")


def limpiarDatos():
    entPeso.delete(0, tk.END)
    lblResultado.config(text="")



#Como objetos, introducimos los siguientes ejemplos de animales
animal1= Animal("Perro Bernes", 10, "Displasia de cadera", 40, 2000, "Montañas frías")
animal2= Animal("Caballo Appaloosa", 25, "Cólicos", 500, 25000, "Praderas")
animal3=animalAnfibios("Rana Dardo", 8, "Infecciones cutáneas", 0.2, 500, "Selva", 13)
animal4=animalAnfibios("Tritón Ibérico", 10, "Hongos", 0.3, 400, "Charcas", 3)
animal5=animalReptiles("Iguana Verde", 15, "Parásitos intestinales", 5, 1500, "Bosques", 100)
animal6=animalReptiles("Caimán del Orinoco", 50, "Heridas en combate", 250, 4000, "Ríos", 200)


Animal.cont = 0
listaAnimales=[animal1, animal2, animal3, animal4, animal5, animal6]

#Configuración de la ventana
window = tk.Tk()
window.title("Mi Centro Veterinario")
window.geometry("400x300")


#Título
lblTitulo = tk.Label(window, text="Centro Veterinario Sabiñánigo ")
lblTitulo.pack()


frmInfoAnimales = tk.Frame(window)
frmInfoAnimales.pack()

#Etiquetas
lblEspecie = tk.Label(frmInfoAnimales, text="Especie: ")
lblEspecie.grid(column=1, row=1)
lblEspecieData = tk.Label(frmInfoAnimales, text=listaAnimales[0].especie)
lblEspecieData.grid(column=2, row=1)

lblEdadMedia = tk.Label(frmInfoAnimales, text="Edad Media (años): ")
lblEdadMedia.grid(column=1, row=2)
lblEdadMediaData = tk.Label(frmInfoAnimales, text=listaAnimales[0].edadMedia)
lblEdadMediaData.grid(column=2, row=2)

lblEnfComunes = tk.Label(frmInfoAnimales, text="Enfermedades Comunes: ")
lblEnfComunes.grid(column=1, row=3)
lblEnfComunesData = tk.Label(frmInfoAnimales, text=listaAnimales[0].enfComunes)
lblEnfComunesData.grid(column=2, row=3)

lblPesoMedio = tk.Label(frmInfoAnimales, text="Peso Medio (Kg): ")
lblPesoMedio.grid(column=1, row=4)
lblPesoMedioData = tk.Label(frmInfoAnimales, text=listaAnimales[0].pesoMedio)
lblPesoMedioData.grid(column=2, row=4)

lblDietaMedia = tk.Label(frmInfoAnimales, text="Dieta Media (Kcal): ")
lblDietaMedia.grid(column=1, row=5)
lblDietaMediaData = tk.Label(frmInfoAnimales, text=listaAnimales[0].dietaMedia)
lblDietaMediaData.grid(column=2, row=5)

lblHabitat = tk.Label(frmInfoAnimales, text="Hábitat: ")
lblHabitat.grid(column=1, row=6)
lblHabitatData = tk.Label(frmInfoAnimales, text=listaAnimales[0].habitat)
lblHabitatData.grid(column=2, row=6)

#Etiquetas específicas inicialmente ocultas
lblNumeroHuevos = tk.Label(frmInfoAnimales, text="Número de Huevos: ")
lblNumeroHuevosData = tk.Label(frmInfoAnimales, text="")

lblNumeroEscamas = tk.Label(frmInfoAnimales, text="Número de Escamas: ")
lblNumeroEscamasData = tk.Label(frmInfoAnimales, text="")


# Sección de peso personalizado
frmPeso = tk.Frame(window)
frmPeso.pack(pady=10)
lblPeso = tk.Label(frmPeso, text="Introduce el peso de tu animal (Kg): ")
lblPeso.grid(column=1, row=1)
entPeso = tk.Entry(frmPeso, width=10)
entPeso.grid(column=2, row=1)

# Botón calcular
btnCalcular = tk.Button(frmPeso, text="Calcular", command=calcularKcal)
btnCalcular.grid(column=1, row=2)

# Botón limpiar
btnLimpiar = tk.Button(frmPeso, text="Limpiar", command=limpiarDatos)
btnLimpiar.grid(column=2, row=2)

# Resultado
lblResultado = tk.Label(window, text="")
lblResultado.pack()

# Botón siguiente animal
btnSiguienteAnimal = tk.Button(window, text="Siguiente", command=siguienteAnimal)
btnSiguienteAnimal.pack()



frmBotones=tk.Frame(window, padx=20, pady=20)
frmBotones.pack()




window.mainloop()