
import tkinter as tk
from tkinter import ttk, messagebox


def mostrar_categorias(contenido):

    # Limpiar el contenido anterior
    for widget in contenido.winfo_children():
        widget.destroy()

    # Título
    tk.Label(
        contenido,
        text="Gestión de categorías",
        bg="#F4F6F8",
        fg="#202A35",
        font=("Arial", 18, "bold")
    ).pack(anchor="w", padx=30, pady=(30, 20))

    # Panel del formulario
    formulario = tk.Frame(contenido, bg="white")
    formulario.pack(fill="x", padx=30, pady=10)

    tk.Label(
        formulario,
        text="Registrar categoría",
        bg="white",
        fg="#202A35",
        font=("Arial", 14, "bold")
    ).pack(anchor="w", padx=20, pady=15)

    # Campos
    campos = tk.Frame(formulario, bg="white")
    campos.pack(fill="x", padx=20, pady=10)

    tk.Label(
        campos,
        text="Nombre de la categoría",
        bg="white"
    ).grid(row=0, column=0, sticky="w", padx=5)

    entrada_nombre = tk.Entry(campos, width=35)
    entrada_nombre.grid(row=1, column=0, padx=5, pady=8)

    tk.Label(
        campos,
        text="Descripción",
        bg="white"
    ).grid(row=0, column=1, sticky="w", padx=5)

    entrada_descripcion = tk.Entry(campos, width=60)
    entrada_descripcion.grid(row=1, column=1, padx=5, pady=8)

    # Botones
    botones = tk.Frame(formulario, bg="white")
    botones.pack(fill="x", padx=20, pady=15)

    tk.Button(
        botones,
        text="Registrar",
        bg="#E5E9ED",
        fg="#202A35",
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
        text="Lista de categorías",
        bg="white",
        fg="#202A35",
        font=("Arial", 14, "bold")
    ).pack(anchor="w", padx=20, pady=15)

    tabla = ttk.Treeview(
        tabla_frame,
        columns=("codigo", "nombre", "descripcion"),
        show="headings"
    )

    tabla.heading("codigo", text="Código")
    tabla.heading("nombre", text="Categoría")
    tabla.heading("descripcion", text="Descripción")

    tabla.column("codigo", width=100)
    tabla.column("nombre", width=250)
    tabla.column("descripcion", width=500)

    tabla.pack(fill="both", expand=True, padx=20, pady=(0, 20))


