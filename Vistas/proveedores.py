
import tkinter as tk
from tkinter import ttk


def mostrar_proveedores(contenido):

    # Limpiar el contenido anterior
    for widget in contenido.winfo_children():
        widget.destroy()

    # Título
    tk.Label(
        contenido,
        text="Gestión de proveedores",
        bg="#F4F6F8",
        fg="#202A35",
        font=("Arial", 18, "bold")
    ).pack(anchor="w", padx=30, pady=(30, 20))

    # Panel del formulario
    formulario = tk.Frame(contenido, bg="white")
    formulario.pack(fill="x", padx=30, pady=10)

    tk.Label(
        formulario,
        text="Registrar proveedor",
        bg="white",
        fg="#202A35",
        font=("Arial", 14, "bold")
    ).pack(anchor="w", padx=20, pady=15)

    # Campos del formulario
    campos = tk.Frame(formulario, bg="white")
    campos.pack(fill="x", padx=20, pady=10)

    tk.Label(campos, text="Nombre o razón social", bg="white").grid(row=0, column=0, sticky="w", padx=5)
    tk.Entry(campos, width=30).grid(row=1, column=0, padx=5, pady=8)

    tk.Label(campos, text="RUC", bg="white").grid(row=0, column=1, sticky="w", padx=5)
    tk.Entry(campos, width=20).grid(row=1, column=1, padx=5, pady=8)

    tk.Label(campos, text="Teléfono", bg="white").grid(row=0, column=2, sticky="w", padx=5)
    tk.Entry(campos, width=20).grid(row=1, column=2, padx=5, pady=8)

    tk.Label(campos, text="Correo electrónico", bg="white").grid(row=2, column=0, sticky="w", padx=5)
    tk.Entry(campos, width=30).grid(row=3, column=0, padx=5, pady=8)

    tk.Label(campos, text="Dirección", bg="white").grid(row=2, column=1, sticky="w", padx=5)
    tk.Entry(campos, width=50).grid(row=3, column=1, columnspan=2, padx=5, pady=8, sticky="w")

    # Botones
    botones = tk.Frame(formulario, bg="white")
    botones.pack(fill="x", padx=20, pady=15)

    tk.Button(
        botones,
        text="Registrar",
        bg="#202A35",
        fg="white",
        relief="flat",
        padx=20,
        pady=8
    ).pack(side="left", padx=5)

    tk.Button(
        botones,
        text="Editar",
        bg="#E5E9ED",
        fg="#202A35",
        relief="flat",
        padx=20,
        pady=8
    ).pack(side="left", padx=5)

    tk.Button(
        botones,
        text="Eliminar",
        bg="#E5E9ED",
        fg="#202A35",
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

    # Panel de la tabla
    tabla_frame = tk.Frame(contenido, bg="white")
    tabla_frame.pack(fill="both", expand=True, padx=30, pady=20)

    tk.Label(
        tabla_frame,
        text="Lista de proveedores",
        bg="white",
        fg="#202A35",
        font=("Arial", 14, "bold")
    ).pack(anchor="w", padx=20, pady=15)

    tabla = ttk.Treeview(
        tabla_frame,
        columns=("codigo", "nombre", "ruc", "telefono", "correo", "direccion"),
        show="headings"
    )

    tabla.heading("codigo", text="Código")
    tabla.heading("nombre", text="Proveedor")
    tabla.heading("ruc", text="RUC")
    tabla.heading("telefono", text="Teléfono")
    tabla.heading("correo", text="Correo")
    tabla.heading("direccion", text="Dirección")

    tabla.column("codigo", width=70)
    tabla.column("nombre", width=180)
    tabla.column("ruc", width=110)
    tabla.column("telefono", width=110)
    tabla.column("correo", width=180)
    tabla.column("direccion", width=200)

    tabla.pack(fill="both", expand=True, padx=20, pady=(0, 20))


