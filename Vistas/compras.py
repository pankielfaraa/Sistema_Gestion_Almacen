
import tkinter as tk
from tkinter import ttk


def mostrar_compras(contenido):

    # Limpiar el contenido anterior
    for widget in contenido.winfo_children():
        widget.destroy()

    # Título
    tk.Label(
        contenido,
        text="Gestión de compras",
        bg="#F4F6F8",
        fg="#202A35",
        font=("Arial", 18, "bold")
    ).pack(anchor="w", padx=30, pady=(30, 20))

    # Panel del formulario
    formulario = tk.Frame(contenido, bg="white")
    formulario.pack(fill="x", padx=30, pady=10)

    tk.Label(
        formulario,
        text="Registrar compra",
        bg="white",
        fg="#202A35",
        font=("Arial", 14, "bold")
    ).pack(anchor="w", padx=20, pady=15)

    # Campos del formulario
    campos = tk.Frame(formulario, bg="white")
    campos.pack(fill="x", padx=20, pady=10)

    tk.Label(campos, text="Número de compra", bg="white").grid(row=0, column=0, sticky="w", padx=5)
    tk.Entry(campos, width=30).grid(row=1, column=0, padx=5, pady=8)

    tk.Label(campos, text="Proveedor", bg="white").grid(row=0, column=1, sticky="w", padx=5)
    ttk.Combobox(
        campos,
        values=("Distribuidora Lima", "Tech Solutions", "Comercial del Perú"),
        width=27,
        state="readonly"
    ).grid(row=1, column=1, padx=5, pady=8)

    tk.Label(campos, text="Fecha", bg="white").grid(row=0, column=2, sticky="w", padx=5)
    tk.Entry(campos, width=20).grid(row=1, column=2, padx=5, pady=8)

    tk.Label(campos, text="Producto", bg="white").grid(row=2, column=0, sticky="w", padx=5)
    ttk.Combobox(
        campos,
        values=("Teclado", "Mouse", "Monitor", "Laptop"),
        width=27,
        state="readonly"
    ).grid(row=3, column=0, padx=5, pady=8)

    tk.Label(campos, text="Cantidad", bg="white").grid(row=2, column=1, sticky="w", padx=5)
    tk.Entry(campos, width=30).grid(row=3, column=1, padx=5, pady=8)

    tk.Label(campos, text="Precio unitario (S/)", bg="white").grid(row=2, column=2, sticky="w", padx=5)
    tk.Entry(campos, width=20).grid(row=3, column=2, padx=5, pady=8)

    tk.Label(
        campos,
        text="Total de compra: S/ 0.00",
        bg="white",
        fg="#202A35",
        font=("Arial", 12, "bold")
    ).grid(row=4, column=2, sticky="e", padx=5, pady=10)

    # Botones
    botones = tk.Frame(formulario, bg="white")
    botones.pack(fill="x", padx=20, pady=15)

    tk.Button(
        botones,
        text="Registrar compra",
        bg="#202A35",
        fg="white",
        relief="flat",
        padx=20,
        pady=8
    ).pack(side="left", padx=5)

    tk.Button(
        botones,
        text="Limpiar",
        bg="#E5E9ED",
        fg="#202A35",
        relief="flat",
        padx=20,
        pady=8
    ).pack(side="left", padx=5)

    # Panel del historial
    tabla_frame = tk.Frame(contenido, bg="white")
    tabla_frame.pack(fill="both", expand=True, padx=30, pady=20)

    tk.Label(
        tabla_frame,
        text="Historial de compras",
        bg="white",
        fg="#202A35",
        font=("Arial", 14, "bold")
    ).pack(anchor="w", padx=20, pady=15)

    tabla = ttk.Treeview(
        tabla_frame,
        columns=("codigo", "proveedor", "fecha", "producto", "cantidad", "total"),
        show="headings"
    )

    tabla.heading("codigo", text="N.º Compra")
    tabla.heading("proveedor", text="Proveedor")
    tabla.heading("fecha", text="Fecha")
    tabla.heading("producto", text="Producto")
    tabla.heading("cantidad", text="Cantidad")
    tabla.heading("total", text="Total")

    tabla.column("codigo", width=100)
    tabla.column("proveedor", width=180)
    tabla.column("fecha", width=120)
    tabla.column("producto", width=180)
    tabla.column("cantidad", width=100)
    tabla.column("total", width=120)

    tabla.pack(fill="both", expand=True, padx=20, pady=(0, 20))

