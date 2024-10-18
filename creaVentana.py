import tkinter as tk

class Ventana:
    def __init__(self):
        # Atributos privados
        self.__ancho = 800  # Valor por defecto
        self.__alto = 600   # Valor por defecto
        self.__redimensionable = True
        self.__titulo = 'Ventana del futuro Inge'

    # Método para establecer las dimensiones de la ventana
    def set_dimensiones(self, ancho, alto):
        self.__ancho = ancho
        self.__alto = alto

    # Método para permitir redimensionar la ventana
    def set_redimensionable(self, redimensionable):
        self.__redimensionable = redimensionable

    # Método para establecer el título de la etiqueta dentro de la ventana
    def set_titulo(self, titulo):
        self.__titulo = titulo

    # Método para crear la ventana
    def crear_ventana(self):
        ventana = tk.Tk()
        ventana.title("Ventana del futuro Inge")
        # Establecer el tamaño de la ventana
        ventana.geometry(f"{self.__ancho}x{self.__alto}")
        # Definir si es redimensionable
        ventana.resizable(self.__redimensionable, self.__redimensionable)
        #Crear una etiqueta dentro de la ventana con el titulo
        etiqueta = tk.LabelFrame(ventana, text=self.__titulo, font=("arial", 15))
        etiqueta.pack(pady=20)
        # Iniciar el bucle principal de la ventana
        ventana.mainloop()
