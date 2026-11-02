# ESTE ARCHIVO ES MERAMENTE REFERENCIA Y POR NINGUN MOTIVO DEBEMOS COPIARLO POR COMPLETO
# NOSOTROS NO ESTAMOS A FAVOR DEL VIBECODING AQUI PURO TRABAJO LIMPIO
# A NO SER QUE SE NOS ACABE EL TIEMPO PUES AHÍ SI
# UNA TIENDA? PARECE MÁS UNA ÑIENDA
#Y odio a Adriela. ATTE: Emmanuel

import customtkinter as ctk
from tkinter import messagebox

# ---------------------------------------------------------------
# 1. CONFIGURACION GENERAL
# ---------------------------------------------------------------
ctk.set_appearance_mode("dark")          # "dark", "light" o "system"
ctk.set_default_color_theme("blue")      # tema de colores de los widgets

# ---------------------------------------------------------------
# 2. DATOS (por ahora una lista; luego vendran de PostgreSQL)
# ---------------------------------------------------------------
# Cada producto es un diccionario. Con psycopg2 harias algo asi:
#
#   import psycopg2
#   conexion = psycopg2.connect(dbname="tienda", user="postgres",
#                               password="tu_clave", host="localhost")
#   cursor = conexion.cursor()
#   cursor.execute("SELECT id, nombre, categoria, precio, color FROM tenis")
#   filas = cursor.fetchall()
#   productos = [{"id": f[0], "nombre": f[1], "categoria": f[2],
#                 "precio": f[3], "color": f[4]} for f in filas]
#
productos = [
    {"id": 1, "nombre": "Air Max 90",       "categoria": "Running",    "precio": 2499, "color": "#e63946"},
    {"id": 2, "nombre": "Air Force 1",      "categoria": "Lifestyle",  "precio": 2199, "color": "#457b9d"},
    {"id": 3, "nombre": "Pegasus 41",       "categoria": "Running",    "precio": 2999, "color": "#2a9d8f"},
    {"id": 4, "nombre": "Dunk Low",         "categoria": "Lifestyle",  "precio": 2399, "color": "#f4a261"},
    {"id": 5, "nombre": "LeBron 21",        "categoria": "Basketball", "precio": 3899, "color": "#9b5de5"},
    {"id": 6, "nombre": "Kyrie Infinity",   "categoria": "Basketball", "precio": 3299, "color": "#e76f51"},
    {"id": 7, "nombre": "Metcon 9",         "categoria": "Training",   "precio": 2799, "color": "#06d6a0"},
    {"id": 8, "nombre": "Air Jordan 1",     "categoria": "Lifestyle",  "precio": 3599, "color": "#d00000"},
    {"id": 9, "nombre": "Vaporfly 3",       "categoria": "Running",    "precio": 3999, "color": "#00b4d8"},
]

carrito = []   # lista de productos agregados

# ---------------------------------------------------------------
# 3. VENTANA PRINCIPAL
# ---------------------------------------------------------------
app = ctk.CTk()
app.title("✔ Naik.Com")
app.geometry("1250x720")

# La ventana se divide en una cuadricula (grid):
# fila 0 = encabezado | fila 1 = contenido
# columna 0 = filtros | columna 1 = catalogo | columna 2 = carrito
app.grid_rowconfigure(1, weight=1)       # la fila 1 se estira
app.grid_columnconfigure(1, weight=1)    # la columna 1 se estira

# Variables de control (guardan el valor de los widgets)
talla_var = ctk.StringVar(value="9")
categoria_var = ctk.StringVar(value="Todas")


# ---------------------------------------------------------------
# 4. FUNCIONES (lo que hacen los botones)
# ---------------------------------------------------------------
def mostrar_productos(*args):
    """Dibuja las tarjetas de productos segun los filtros."""
    # Primero borramos las tarjetas anteriores
    for widget in frame_catalogo.winfo_children():
        widget.destroy()

    texto_busqueda = entry_busqueda.get().lower()
    categoria = categoria_var.get()
    precio_max = slider_precio.get()

    fila = 0
    columna = 0

    for p in productos:
        # Aplicar filtros
        if texto_busqueda not in p["nombre"].lower():
            continue
        if categoria != "Todas" and p["categoria"] != categoria:
            continue
        if p["precio"] > precio_max:
            continue

        # --- TARJETA (un frame por producto) ---
        tarjeta = ctk.CTkFrame(frame_catalogo, corner_radius=15)
        tarjeta.grid(row=fila, column=columna, padx=10, pady=10, sticky="n")

        # "Imagen" (un frame de color con un emoji; luego puedes usar CTkImage)
        imagen = ctk.CTkFrame(tarjeta, width=200, height=140,
                              corner_radius=12, fg_color=p["color"])
        imagen.pack(padx=10, pady=10)
        imagen.pack_propagate(False)   # evita que el frame se encoja
        ctk.CTkLabel(imagen, text="👟", font=("Arial", 60)).pack(expand=True)

        # Textos (labels)
        ctk.CTkLabel(tarjeta, text=p["nombre"],
                     font=("Arial", 16, "bold")).pack()
        ctk.CTkLabel(tarjeta, text=p["categoria"],
                     text_color="gray").pack()
        ctk.CTkLabel(tarjeta, text=f"${p['precio']:,} MXN",
                     font=("Arial", 14)).pack(pady=5)

        # Boton: command= recibe la funcion que se ejecuta al hacer clic.
        # Usamos lambda para poder pasarle el producto (p=p es importante).
        ctk.CTkButton(tarjeta, text="Agregar al carrito",
                      fg_color="black", hover_color="#333333",
                      command=lambda p=p: agregar_al_carrito(p)
                      ).pack(padx=10, pady=(5, 12))

        # Pasar a la siguiente posicion (3 tarjetas por fila)
        columna += 1
        if columna == 3:
            columna = 0
            fila += 1


def agregar_al_carrito(producto):
    """Agrega un producto (con la talla elegida) al carrito."""
    item = {"nombre": producto["nombre"],
            "precio": producto["precio"],
            "talla": talla_var.get()}
    carrito.append(item)
    actualizar_carrito()


def quitar_del_carrito(indice):
    carrito.pop(indice)
    actualizar_carrito()


def actualizar_carrito():
    """Redibuja la lista del carrito y el total."""
    for widget in frame_lista_carrito.winfo_children():
        widget.destroy()

    total = 0
    for i, item in enumerate(carrito):
        fila = ctk.CTkFrame(frame_lista_carrito)
        fila.pack(fill="x", pady=3, padx=3)

        ctk.CTkLabel(fila, text=f"{item['nombre']}\nTalla {item['talla']} - ${item['precio']:,}",
                     justify="left").pack(side="left", padx=8, pady=4)
        ctk.CTkButton(fila, text="✕", width=30, fg_color="#c0392b",
                      hover_color="#922b21",
                      command=lambda i=i: quitar_del_carrito(i)
                      ).pack(side="right", padx=8)
        total += item["precio"]

    label_total.configure(text=f"Total: ${total:,} MXN")
    boton_carrito.configure(text=f"🛒 Carrito ({len(carrito)})")


def vaciar_carrito():
    carrito.clear()
    actualizar_carrito()


def comprar():
    if not carrito:
        messagebox.showwarning("Carrito vacio", "Agrega al menos un producto.")
        return
    nombre = entry_nombre.get().strip()
    if nombre == "":
        messagebox.showwarning("Falta el nombre", "Escribe tu nombre para continuar.")
        return

    total = sum(item["precio"] for item in carrito)
    # AQUI iria el INSERT con psycopg2 para guardar la venta
    messagebox.showinfo("Compra realizada",
                        f"Gracias {nombre}!\nTotal pagado: ${total:,} MXN")
    entry_nombre.delete(0, "end")
    vaciar_carrito()


def cambiar_tema():
    if switch_tema.get() == 1:
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")


def actualizar_label_precio(valor):
    label_precio.configure(text=f"Precio max: ${int(valor):,}")
    mostrar_productos()


# ---------------------------------------------------------------
# 5. ENCABEZADO (fila 0)
# ---------------------------------------------------------------
frame_header = ctk.CTkFrame(app, height=60, corner_radius=0)
frame_header.grid(row=0, column=0, columnspan=3, sticky="ew")

ctk.CTkLabel(frame_header, text="✔ Naik.Com",
             font=("Arial", 24, "bold")).pack(side="left", padx=20, pady=10)

ctk.CTkLabel(frame_header, text="Pagina oficial de naik, tu mete tu tarjeta...",
             font=("Arial", 24, "bold")).pack(side="left", padx=20, pady=10)

ctk.CTkLabel(frame_header, text="Envio GRATIS!!!",
             font=("Arial", 24, "bold")).pack(side="left", padx=20, pady=10)

boton_carrito = ctk.CTkButton(frame_header, text="🛒 Carrito (0)", width=130)
boton_carrito.pack(side="right", padx=20)

# Entry = cuadro de texto de una linea
entry_busqueda = ctk.CTkEntry(frame_header, placeholder_text="Buscar tenis...",
                              width=300)
entry_busqueda.pack(side="right", padx=10)
entry_busqueda.bind("<KeyRelease>", mostrar_productos)  # filtra al escribir

# ---------------------------------------------------------------
# 6. PANEL DE FILTROS (fila 1, columna 0)
# ---------------------------------------------------------------
frame_filtros = ctk.CTkFrame(app, width=220)
frame_filtros.grid(row=1, column=0, sticky="ns", padx=(10, 5), pady=10)

ctk.CTkLabel(frame_filtros, text="Filtros",
             font=("Arial", 18, "bold")).pack(pady=(15, 10), padx=20)

# OptionMenu = lista desplegable
ctk.CTkLabel(frame_filtros, text="Categoria").pack(anchor="w", padx=20)
ctk.CTkOptionMenu(frame_filtros, variable=categoria_var,
                  values=["Todas", "Running", "Lifestyle", "Basketball", "Training"],
                  command=mostrar_productos).pack(padx=20, pady=(0, 15))

# Slider = barra deslizante
label_precio = ctk.CTkLabel(frame_filtros, text="Precio max: $4,000")
label_precio.pack(anchor="w", padx=20)
slider_precio = ctk.CTkSlider(frame_filtros, from_=2000, to=4000,
                              number_of_steps=20,
                              command=actualizar_label_precio)
slider_precio.set(4000)
slider_precio.pack(padx=20, pady=(0, 15))

# SegmentedButton = botones de seleccion unica (tallas)
ctk.CTkLabel(frame_filtros, text="Talla (MX)").pack(anchor="w", padx=20)
ctk.CTkSegmentedButton(frame_filtros, variable=talla_var,
                       values=["7", "8", "9", "10", "11"]
                       ).pack(padx=10, pady=(0, 15))

# Switch = interruptor on/off
switch_tema = ctk.CTkSwitch(frame_filtros, text="Modo oscuro",
                            command=cambiar_tema)
switch_tema.select()    # lo dejamos encendido
switch_tema.pack(padx=20, pady=20)

# ---------------------------------------------------------------
# 7. CATALOGO (fila 1, columna 1)
# ---------------------------------------------------------------
# ScrollableFrame = frame con barra de desplazamiento
frame_catalogo = ctk.CTkScrollableFrame(app, label_text="Catalogo")
frame_catalogo.grid(row=1, column=1, sticky="nsew", padx=5, pady=10)

# ---------------------------------------------------------------
# 8. CARRITO (fila 1, columna 2)
# ---------------------------------------------------------------
frame_carrito = ctk.CTkFrame(app, width=290)
frame_carrito.grid(row=1, column=2, sticky="ns", padx=(5, 10), pady=10)

ctk.CTkLabel(frame_carrito, text="Tu carrito",
             font=("Arial", 18, "bold")).pack(pady=(15, 5))

frame_lista_carrito = ctk.CTkScrollableFrame(frame_carrito, width=250, height=350)
frame_lista_carrito.pack(padx=10, pady=5)

label_total = ctk.CTkLabel(frame_carrito, text="Total: $0 MXN",
                           font=("Arial", 16, "bold"))
label_total.pack(pady=10)

entry_nombre = ctk.CTkEntry(frame_carrito, placeholder_text="Tu nombre", width=250)
entry_nombre.pack(pady=5)

ctk.CTkButton(frame_carrito, text="Comprar", width=250,
              fg_color="#27ae60", hover_color="#1e8449",
              command=comprar).pack(pady=5)
ctk.CTkButton(frame_carrito, text="Vaciar carrito", width=250,
              fg_color="gray30", hover_color="gray20",
              command=vaciar_carrito).pack(pady=5)

# ---------------------------------------------------------------
# 9. ARRANQUE
# ---------------------------------------------------------------
mostrar_productos()    # dibuja el catalogo la primera vez
app.mainloop()         # mantiene la ventana abierta (siempre al final)