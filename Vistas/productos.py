import tkinter as tk
from tkinter import ttk

#db
from Controladores.productos_controlador import obtener_productos, registrar_producto


def mostrar_productos(contenido):

    # Limpiar el contenido anterior
    for widget in contenido.winfo_children():
        widget.destroy()

    # Título
    tk.Label(
        contenido,
        text="Gestión de productos",
        bg="#F4F6F8",
        fg="#202A35",
        font=("Arial", 18, "bold")
    ).pack(anchor="w", padx=30, pady=(30, 20))

    # Panel de registro
    formulario = tk.Frame(contenido, bg="white")
    formulario.pack(fill="x", padx=30, pady=10)

    tk.Label(
        formulario,
        text="Registrar producto",
        bg="white",
        fg="#202A35",
        font=("Arial", 14, "bold")
    ).pack(anchor="w", padx=20, pady=15)



    # Campos del formulario
    campos = tk.Frame(formulario, bg="white")
    campos.pack(fill="x", padx=20, pady=10)
    

    nombre_texto = tk.Label(campos, text="Nombre de Producto",bg="#FFFFFF")
    nombre_texto.grid(row=0, column=0,sticky="w",padx=5)
    nombre = tk.StringVar()
    tk.Entry(campos, textvariable=nombre, width=30).grid(row=1, column=0, padx=5, pady=8)


    categoria_texto = tk.Label(campos, text="Categoria",bg="#FFFFFF")
    categoria_texto.grid(row=0,column=1,sticky="w",padx=5)
    categoria = tk.StringVar()
    ttk.Combobox(campos, textvariable=categoria, width=25, state="readonly").grid(row=1, column=1, padx=5, pady=8)


    precio_texto = tk.Label(campos, text="Precio Unitario",bg="#FFFFFF")
    precio_texto.grid(row=0,column=2,sticky="w",padx=5)
    precio = tk.StringVar()
    tk.Entry(campos, textvariable=precio, width=20).grid(row=1, column=2, padx=5, pady=8)


    categoria_texto = tk.Label(campos, text="Stock",bg="#FFFFFF")
    categoria_texto.grid(row=0,column=3,sticky="w",padx=5)
    stock = tk.StringVar()
    tk.Entry(campos, textvariable=stock, width=20).grid(row=1, column=3, padx=5, pady=8)



    def registrar():
        nombre_producto = nombre.get()
        categoria_producto = categoria.get()
        precio_producto = precio.get()
        stock_producto = stock.get()

        registrar_producto(
            nombre_producto,
            categoria_producto,
            precio_producto,
            stock_producto
        )

        cargar_productos()

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
        pady=8,
        command=registrar
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

    # Tabla de productos
    tabla_frame = tk.Frame(contenido, bg="white")
    tabla_frame.pack(fill="both", expand=True, padx=30, pady=20)

    tk.Label(
        tabla_frame,
        text="Lista de productos",
        bg="white",
        fg="#202A35",
        font=("Arial", 14, "bold")
    ).pack(anchor="w", padx=20, pady=15)

    tabla = ttk.Treeview(
        tabla_frame,
        columns=("codigo", "nombre", "categoria", "precio", "stock"),
        show="headings"
    )

    tabla.heading("codigo", text="Código")
    tabla.heading("nombre", text="Producto")
    tabla.heading("categoria", text="Categoría")
    tabla.heading("precio", text="Precio")
    tabla.heading("stock", text="Stock")

    tabla.column("codigo", width=80)
    tabla.column("nombre", width=250)
    tabla.column("categoria", width=180)
    tabla.column("precio", width=120)
    tabla.column("stock", width=100)

    tabla.pack(fill="both", expand=True, padx=20, pady=(0, 20))


    def cargar_productos():
        tabla.delete(*tabla.get_children())

        productos = obtener_productos()

        for i in productos:
            tabla.insert("", "end", values=i)

    cargar_productos()