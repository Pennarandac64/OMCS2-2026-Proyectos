import tkinter as tk

def convertir_temperatura():
    # .get() extrae lo que el usuario escribió en el cuadro de texto como un string
    texto_ingresado = cuadro_texto.get()
    
    try:
        # Tratamiento de datos de Computer Science: validar y convertir tipos
        celsius = float(texto_ingresado)
        fahrenheit = (celsius * 9/5) + 32
        
        # Modificamos la etiqueta para mostrar el resultado
        resultado_label.config(text=f"{celsius}°C equivalen a {fahrenheit:.2f}°F", fg="#deff9a")
    except ValueError:
        # Si el usuario escribió letras en vez de números, evitamos que el programa explote
        resultado_label.config(text="Error: Introduce un número válido.", fg="#ff8a8a")

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Conversor de Temperatura")
ventana.geometry("450x250")
ventana.config(bg="#8C0B0B") # Fondo oscuro para descansar la vista

# Componentes visuales
instruccion = tk.Label(ventana, text="Introduce la temperatura en Celsius:", bg="#121212", fg="#fff", font=("Arial", 12))
instruccion.pack(pady=10)

# El sustituto de input(): Cuadro de entrada de texto
cuadro_texto = tk.Entry(ventana, font=("Arial", 12), justify="center")
cuadro_texto.pack(pady=10)

# Botón que dispara la acción
boton_calcular = tk.Button(ventana, text="Convertir a Fahrenheit", command=convertir_temperatura, bg="#deff9a", fg="#000", font=("Arial", 11, "bold"))
boton_calcular.pack(pady=15)

# Etiqueta para mostrar respuestas o errores
resultado_label = tk.Label(ventana, text="", bg="#121212", font=("Arial", 12, "bold"))
resultado_label.pack(pady=10)

ventana.mainloop()