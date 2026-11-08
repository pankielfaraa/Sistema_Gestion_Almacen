
import tkinter as tk
from tkinter import ttk


def mostrar_inicio(contenido):

    # Limpiar el contenido anterior
    for widget in contenido.winfo_children():
        widget.destroy()

    # Bienvenida
    tk.Label(
        contenido,
        text="Bienvenido al Sistema de almacenamiento VELASQUEZ!",
        bg="#F4F6F8",
        fg="#202A35",
        font=("Arial", 18, "bold")
    ).pack(anchor="w", padx=30, pady=(30, 20))

    # Estadísticas principales
    tarjetas = tk.Frame(contenido, bg="#F4F6F8")
    tarjetas.pack(fill="x", padx=30)

    datos = [
        ("Productos registrados", "0", "#5E6C75"),
        ("Ventas del día", "S/ 0", "#5E6C75"),
        ("Compras realizadas", "S/ 0", "#5E6C75"),
        ("Stock bajo", "0", "#FC2205")
    ]

    for i, (nombre, valor, color) in enumerate(datos):

        tarjeta = tk.Frame(
            tarjetas,
            bg="white",
            height=125
        )

        tarjeta.grid(
            row=0,
            column=i,
            padx=7,
            sticky="nsew"
        )

        tarjeta.grid_propagate(False)

        tk.Label(
            tarjeta,
            text=nombre,
            bg="white",
            fg="#707B84",
            font=("Arial", 10)
        ).pack(anchor="center", padx=15, pady=(20, 8))

        tk.Label(
            tarjeta,
            text=valor,
            bg="white",
            fg=color,
            font=("Arial", 19, "bold")
        ).pack(anchor="center", padx=15)

        tarjetas.grid_columnconfigure(i, weight=1)

    # Actividad reciente
    seccion = tk.Frame(contenido, bg="white")
    seccion.pack(fill="both", expand=True, padx=37, pady=30)

    tk.Label(
        seccion,
        text="Actividad reciente",
        bg="white",
        fg="#202A35",
        font=("Arial", 14, "bold")
    ).pack(anchor="w", padx=20, pady=20)

    tabla = ttk.Treeview(
        seccion,
        columns=("operacion", "detalle", "fecha"),
        show="headings"
    )

    tabla.heading("operacion", text="Operación")
    tabla.heading("detalle", text="Descripción")
    tabla.heading("fecha", text="Fecha")

    tabla.column("operacion", width=150)
    tabla.column("detalle", width=300)
    tabla.column("fecha", width=150)

    tabla.pack(fill="both", expand=True, padx=20, pady=(0, 20))
