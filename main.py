
import tkinter as tk
from tkinter import ttk

from Vistas.inicio import mostrar_inicio


# CREACIÓN DE LA VENTANA

ventana = tk.Tk()
ventana.title("Almacen Velasquez")
ventana.geometry("1200x700")
ventana.minsize(1000, 600)
ventana.configure(bg="#F4F6F8")


# MENÚ IZQUIERDO

menu = tk.Frame(ventana, bg="#202A35", width=220)
menu.pack(side="left", fill="y")
menu.pack_propagate(False)


# TÍTULOS PRINCIPALES

titulo = tk.Label(
    menu,
    text="VELASQUEZ",
    bg="#202A35",
    fg="white",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=(30, 5))


subtitulo = tk.Label(
    menu,
    text="GESTIÓN DE ALMACÉN",
    bg="#202A35",
    fg="#AAB4BE",
    font=("Arial", 9)
)
subtitulo.pack(pady=(0, 20))


# PANEL DERECHO

panel_derecho = tk.Frame(ventana, bg="#F4F6F8")
panel_derecho.pack(side="right", fill="both", expand=True)


# ENCABEZADO

encabezado = tk.Frame(panel_derecho, bg="white", height=75)
encabezado.pack(fill="x")
encabezado.pack_propagate(False)

tk.Label(
    encabezado,
    text="SISTEMA DE GESTIÓN Y CONTROL DE ACTIVIDADES",
    bg="white",
    fg="#202A35",
    font=("Arial", 17, "bold")
).pack(side="left", padx=30, pady=20)


# CONTENIDO DE LAS PANTALLAS

contenido = tk.Frame(panel_derecho, bg="#F4F6F8")
contenido.pack(fill="both", expand=True)


# FUNCIÓN PARA CAMBIAR DE PANTALLA

def mostrar_pantalla(opcion):

    for widget in contenido.winfo_children():
        widget.destroy()

    if opcion == "Inicio":
        mostrar_inicio(contenido)



# OPCIONES DEL MENÚ

opciones = [
    "Inicio",
    "Productos",
    "Categorías",
    "Compras",
    "Ventas",
    "Proveedores",
    "Clientes",
    "Inventario",
    "Reportes",
    "Configuración"
]


# BOTONES DEL MENÚ

for i in opciones:

    boton = tk.Button(
        menu,
        text=i,
        bg="#202A35",
        fg="white",
        font=("Arial", 11),
        relief="flat",
        anchor="w",
        padx=25,
        pady=10,
        activebackground="#34495E",
        activeforeground="white",
        command=lambda opcion=i: mostrar_pantalla(opcion)
    )

    boton.pack(fill="x", padx=10, pady=2)


# COPYRIGHT

copyright = tk.Label(
    menu,
    text="Desarrollado por \nFernando Velásquez.",
    bg="#202A35",
    fg="#AAB4BE",
    font=("Arial", 9),
    justify="center"
)
copyright.pack(pady=15, padx=15)


# MOSTRAR INICIO AL ABRIR EL PROGRAMA

mostrar_inicio(contenido)


# EJECUTAR VENTANA

ventana.mainloop()
