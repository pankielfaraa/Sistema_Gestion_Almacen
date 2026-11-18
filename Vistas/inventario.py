
import tkinter as tk
from tkinter import ttk


def mostrar_inventario(contenido):

    # Limpiar el contenido anterior
    for widget in contenido.winfo_children():
        widget.destroy()

    # Título
    tk.Label(
        contenido,
        text="Control de inventario",
        bg="#F4F6F8",
        fg="#202A35",
        font=("Arial", 18, "bold")
    ).pack(anchor="w", padx=30, pady=(30, 20))

    # Panel de indicadores
    indicadores = tk.Frame(contenido, bg="#F4F6F8")
    indicadores.pack(fill="x", padx=30, pady=10)

    # Tarjeta 1
    tarjeta1 = tk.Frame(indicadores, bg="white")
    tarjeta1.pack(side="left", fill="both", expand=True, padx=5)

    tk.Label(
        tarjeta1,
        text="Total de productos",
        bg="white",
        fg="#6B7280",
        font=("Arial", 11)
    ).pack(anchor="w", padx=20, pady=(15, 5))

    tk.Label(
        tarjeta1,
        text="120",
        bg="white",
        fg="#202A35",
        font=("Arial", 22, "bold")
    ).pack(anchor="w", padx=20, pady=(0, 15))

    # Tarjeta 2
    tarjeta2 = tk.Frame(indicadores, bg="white")
    tarjeta2.pack(side="left", fill="both", expand=True, padx=5)

    tk.Label(
        tarjeta2,
        text="Productos disponibles",
        bg="white",
        fg="#6B7280",
        font=("Arial", 11)
    ).pack(anchor="w", padx=20, pady=(15, 5))

    tk.Label(
        tarjeta2,
        text="105",
        bg="white",
        fg="#16A34A",
        font=("Arial", 22, "bold")
    ).pack(anchor="w", padx=20, pady=(0, 15))

    # Tarjeta 3
    tarjeta3 = tk.Frame(indicadores, bg="white")
    tarjeta3.pack(side="left", fill="both", expand=True, padx=5)

    tk.Label(
        tarjeta3,
        text="Stock bajo",
        bg="white",
        fg="#6B7280",
        font=("Arial", 11)
    ).pack(anchor="w", padx=20, pady=(15, 5))

    tk.Label(
        tarjeta3,
        text="15",
        bg="white",
        fg="#DC2626",
        font=("Arial", 22, "bold")
    ).pack(anchor="w", padx=20, pady=(0, 15))

    # Panel de la tabla
    tabla_frame = tk.Frame(contenido, bg="white")
    tabla_frame.pack(fill="both", expand=True, padx=30, pady=20)

    tk.Label(
        tabla_frame,
        text="Existencias de productos",
        bg="white",
        fg="#202A35",
        font=("Arial", 14, "bold")
    ).pack(anchor="w", padx=20, pady=15)

    # Tabla
    tabla = ttk.Treeview(
        tabla_frame,
        columns=("codigo", "nombre", "categoria", "stock", "minimo", "estado"),
        show="headings"
    )

    tabla.heading("codigo", text="Código")
    tabla.heading("nombre", text="Producto")
    tabla.heading("categoria", text="Categoría")
    tabla.heading("stock", text="Stock actual")
    tabla.heading("minimo", text="Stock mínimo")
    tabla.heading("estado", text="Estado")

    tabla.column("codigo", width=80)
    tabla.column("nombre", width=200)
    tabla.column("categoria", width=160)
    tabla.column("stock", width=120)
    tabla.column("minimo", width=120)
    tabla.column("estado", width=120)

    tabla.pack(fill="both", expand=True, padx=20, pady=(0, 20))

    # Colores según el estado
    tabla.tag_configure("disponible", foreground="#16A34A")
    tabla.tag_configure("bajo", foreground="#DC2626")

