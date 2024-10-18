from creaVentana import Ventana

def main():
    # Crear un objeto de la clase Ventana
    mi_ventana = Ventana()

    # Establecer dimensiones de la ventana
    mi_ventana.set_dimensiones(1920, 1080)  # Por ejemplo, 1024x768 píxeles

    # Permitir que la ventana sea redimensionable
    mi_ventana.set_redimensionable(True)

    # Crear la ventana
    mi_ventana.crear_ventana()

if __name__ == "__main__":
    main()
