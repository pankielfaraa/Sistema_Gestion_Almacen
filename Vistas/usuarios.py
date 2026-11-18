
import tkinter as tk
from tkinter import ttk


def mostrar_usuarios(contenido):

    # Limpiar el contenido anterior
    for widget in contenido.winfo_children():
        widget.destroy()

    # Título
    tk.Label(
        contenido,
        text="Gestión de usuarios",
        bg="#F4F6F8",
        fg="#202A35",
        font=("Arial", 18, "bold")
    ).pack(anchor="w", padx=30, pady=(30, 20))

    # Panel del formulario
    formulario = tk.Frame(contenido, bg="white")
    formulario.pack(fill="x", padx=30, pady=10)

    tk.Label(
        formulario,
        text="Registrar usuario",
        bg="white",
        fg="#202A35",
        font=("Arial", 14, "bold")
    ).pack(anchor="w", padx=20, pady=15)

    # Campos del formulario
    campos = tk.Frame(formulario, bg="white")
    campos.pack(fill="x", padx=20, pady=10)

    tk.Label(campos, text="Nombre completo", bg="white").grid(row=0, column=0, sticky="w", padx=5)
    tk.Entry(campos, width=30).grid(row=1, column=0, padx=5, pady=8)

    tk.Label(campos, text="Nombre de usuario", bg="white").grid(row=0, column=1, sticky="w", padx=5)
    tk.Entry(campos, width=25).grid(row=1, column=1, padx=5, pady=8)

    tk.Label(campos, text="Contraseña", bg="white").grid(row=0, column=2, sticky="w", padx=5)
    tk.Entry(campos, width=25, show="*").grid(row=1, column=2, padx=5, pady=8)

    tk.Label(campos, text="Rol", bg="white").grid(row=2, column=0, sticky="w", padx=5)
    ttk.Combobox(
        campos,
        values=("Administrador", "Vendedor"),
        width=27,
        state="readonly"
    ).grid(row=3, column=0, padx=5, pady=8)

    tk.Label(campos, text="Estado", bg="white").grid(row=2, column=1, sticky="w", padx=5)
    ttk.Combobox(
        campos,
        values=("Activo", "Inactivo"),
        width=22,
        state="readonly"
    ).grid(row=3, column=1, padx=5, pady=8)

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
        text="Lista de usuarios",
        bg="white",
        fg="#202A35",
        font=("Arial", 14, "bold")
    ).pack(anchor="w", padx=20, pady=15)

    tabla = ttk.Treeview(
        tabla_frame,
        columns=("codigo", "nombre", "usuario", "rol", "estado"),
        show="headings"
    )

    tabla.heading("codigo", text="Código")
    tabla.heading("nombre", text="Nombre completo")
    tabla.heading("usuario", text="Usuario")
    tabla.heading("rol", text="Rol")
    tabla.heading("estado", text="Estado")

    tabla.column("codigo", width=80)
    tabla.column("nombre", width=250)
    tabla.column("usuario", width=180)
    tabla.column("rol", width=150)
    tabla.column("estado", width=120)

    tabla.pack(fill="both", expand=True, padx=20, pady=(0, 20))
