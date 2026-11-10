import customtkinter as ctk
ctk.set_appearance_mode("light") 

#COLORCITOS 
FONDO = "#F6F2EE"
TEXTO_SECUNDARIO = "#77726E"
TARJETAS = "#CACBCD"
BORDES = "#B3B9C1"
BLOQUES_CLAROS = "#F2F2F2"
ACENTO = "#7CB9F2"
PRINCIPAL = "#323841"
AZUL = "#2F80C8"

app = ctk.CTk()  #variable donde se guardará la ventana
app.geometry("1250x720")
app.title("DeluSneakers.com") # configuracion inicial de la ventana
app.configure(fg_color=FONDO)

########### FUNCIONES ################
def login():
    print("login funciona")

def menu ():
    global menu_visible

    if menu_visible:
        menu_lateral.place_forget()
        menu_visible = False
    else:
        menu_lateral.place(x=0, y=0, relheight=1)
        menu_lateral.lift()
        menu_visible = True

def crear_tarjeta(parent, producto, fila, columna):
    tarjeta = ctk.CTkFrame(parent, corner_radius=10, height=300, fg_color=BLOQUES_CLAROS, border_width=1, border_color=BORDES)
    tarjeta.grid(row=fila, column=columna, padx=10, pady=10, sticky="nsew")

    tarjeta.grid_propagate(False)
    tarjeta.grid_columnconfigure(0, weight=1)

    imagen = ctk.CTkLabel(tarjeta, text=producto["imagen"], 
                          font=("Arial",60,"bold"))
    imagen.grid(row=0, column=0, padx=10, pady=(10,5))

    nombre = ctk.CTkLabel(tarjeta, text=producto["nombre"], 
                          font=("Arial",12,"bold"))
    nombre.grid(row=1, column=0, padx=10, pady=(10,5))

    marca = ctk.CTkLabel(tarjeta, text="Marca: "+ producto["marca"], 
                          font=("Arial",12,"bold"))
    marca.grid(row=2, column=0, padx=10, pady=5)

    talla = ctk.CTkLabel(tarjeta, text="Talla: "+ str(producto["talla"]), 
                          font=("Arial",12,"bold"))
    talla.grid(row=3, column=0, padx=10, pady=5)

    precio = ctk.CTkLabel(tarjeta, text=f"${producto['precio']:,}", 
                          font=("Arial",12,"bold"))
    precio.grid(row=4, column=0, padx=10, pady=5)

    disponibilidad = ctk.CTkLabel(tarjeta, text="Disponible", text_color="green",
                          font=("Arial",12,"bold"))
    disponibilidad.grid(row=5, column=0, padx=10, pady=5)

def mostrar_productos(lista_productos):

    # Limpiar catálogo
    for widget in catalogo.winfo_children():
        widget.destroy()

    for columna in range(4):
        catalogo.grid_columnconfigure(columna, weight=1)

    # BANNER SUPERIOR
    banner = ctk.CTkFrame(catalogo,height=170,corner_radius=12,fg_color="#323841")
    banner.grid(row=0,column=0,columnspan=4,padx=15,pady=15,sticky="ew")
    banner.grid_propagate(False)

    texto_banner = ctk.CTkLabel(banner,text="DEJA HUELLA",font=("Arial", 28, "bold"),text_color="white",justify="left")
    texto_banner.grid(row=0, column=0, padx=30, pady=(20, 0), sticky="w")

    texto_banner_2 = ctk.CTkLabel(banner,text="CON CADA PISADA.",font=("Arial", 28, "bold"),text_color=ACENTO,justify="left")
    texto_banner_2.grid(row=1, column=0, padx=30, pady=0, sticky="w")

    descripcion_banner = ctk.CTkLabel(banner,text="Y encuentra tu par (te hacemos descuento)",text_color="white")
    descripcion_banner.grid(row=2, column=0, padx=30, pady=(5, 15), sticky="w")

    # TITULO DEBAJO DEL BANNER
    titulo_catalogo = ctk.CTkLabel(catalogo, text="Nuestros productos",
                                   font=("Arial", 24, "bold"))
    titulo_catalogo.grid(row=1, column=0, columnspan=4, sticky="w", padx=20, pady=(5, 10))

    # PRODUCTOS
    if len(lista_productos) == 0:
        mensaje = ctk.CTkLabel(
            catalogo,
            text="No encontramos tenis :(",
            font=("Arial", 18, "bold")
        )
        mensaje.grid(row=2, column=0, columnspan=4, pady=30)

    for i, producto in enumerate(lista_productos):
        fila = (i // 4) + 2
        columna = i % 4
        crear_tarjeta(catalogo, producto, fila, columna)

    # BANNER INFERIOR PEQUEÑO
    fila_banner = ((len(lista_productos) + 3) // 4) + 2

    banner_inferior = ctk.CTkFrame(catalogo,height=75,corner_radius=10,fg_color="#7CB9F2")
    banner_inferior.grid(row=fila_banner,
        column=0,
        columnspan=4,
        padx=15,
        pady=20,
        sticky="ew"
    )
    banner_inferior.grid_propagate(False)

    texto_inferior = ctk.CTkLabel(
        banner_inferior,
        text="✨ DELUSNEAKERS | ¡Encuentra tu próximo par!",
        font=("Arial", 16, "bold"),
        text_color="#323841"
    )
    texto_inferior.place(relx=0.5, rely=0.5, anchor="center")


def buscar_productos():
    texto = buscar.get().lower()
    resultados = []

    for producto in productos:
        if texto in producto["nombre"].lower() or texto in producto["marca"].lower():
            resultados.append(producto)

    mostrar_productos(resultados)
    ############################

app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(0, weight=1) 

######################################################################
#Encabezado:
encabezado = ctk.CTkFrame(app, height=60, corner_radius=0)
encabezado.grid(row=0, column=0, sticky="ew", padx=10, pady=10) #va en la fila 0
encabezado.grid_columnconfigure(0, weight=0) 
encabezado.grid_columnconfigure(1, weight=0) 
encabezado.grid_columnconfigure(2, weight=1)
encabezado.grid_columnconfigure(3, weight=0)
encabezado.configure(fg_color=BLOQUES_CLAROS)

cuadro_busqueda = ctk.CTkFrame(encabezado, fg_color="transparent")
cuadro_busqueda.grid(row=0, column=1, padx=20, pady=10, sticky="ew")
cuadro_busqueda.grid_columnconfigure(0, weight=1)

######################################################################

btn_menu = ctk.CTkButton(encabezado, text="Menu", width=45, command=menu)
btn_menu.grid(row=0, column=0, padx=10, pady=10)

buscar = ctk.CTkEntry(cuadro_busqueda, placeholder_text="Buscale :p", height=35)
buscar.grid(row=0, column=1, padx=10, pady=10)

buscar.bind("<Return>", lambda event: buscar_productos())

titulo = ctk.CTkLabel(encabezado, text="DeluSneakers", 
                      font=("Arial", 24, "bold"))
titulo.grid(row=0, column=2, padx=10, pady=10)

btn_login = ctk.CTkButton(encabezado, text="Iniciar sesion", width=60, command=login)
btn_login.configure(fg_color=PRINCIPAL, hover_color=AZUL, text_color="white")
btn_login.grid(row=0, column=4, padx=10, pady=10)

########################################################
#Cuerpo:
cuerpo = ctk.CTkFrame(app, corner_radius=0, fg_color="transparent")
cuerpo.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0,10)) #va en la fila 1
cuerpo.grid_columnconfigure(0, weight=1)
cuerpo.grid_rowconfigure(0, weight=1)

##########################################################

################# CONTENIDO A LA DERECHA ######
contenido = ctk.CTkFrame(cuerpo, corner_radius=10)
contenido.configure(fg_color=BLOQUES_CLAROS)
contenido.grid(row=0, column=0, sticky="nsew")
contenido.grid_columnconfigure(0, weight=1)
contenido.grid_rowconfigure(0, weight=1)

pantalla_tienda = ctk.CTkFrame(contenido, fg_color="transparent")
pantalla_tienda.grid(row=0, column=0, sticky="nsew")

pantalla_login = ctk.CTkFrame(contenido)

##########################################################
#productos:
catalogo = ctk.CTkScrollableFrame(pantalla_tienda)
catalogo.grid(row=0, column=0, sticky="nsew")

pantalla_tienda.grid_columnconfigure(0, weight=1)
pantalla_tienda.grid_rowconfigure(0, weight=1)

productos = [
    {"nombre": "Air Force 1", "marca": "Nike", "talla": 27, "precio": 2399,"imagen": "👟"},
    {"nombre": "Samba OG", "marca": "Adidas", "talla": 26, "precio": 2199,"imagen": "👟"},
    {"nombre": "550", "marca": "New Balance", "talla": 27, "precio": 2499,"imagen": "👟"},
    {"nombre": "Dunk Low", "marca": "Nike", "talla": 26, "precio": 2299,"imagen": "👟"},
    {"nombre": "Jordan 1", "marca": "Nike", "talla": 28, "precio": 3199,"imagen": "👟"},
    {"nombre": "Campus 00s", "marca": "Adidas", "talla": 27, "precio": 1999,"imagen": "👟"},
    {"nombre": "2002R", "marca": "New Balance", "talla": 26, "precio": 2799,"imagen": "👟"},
    {"nombre": "Old Skool", "marca": "Vans", "talla": 25, "precio": 1499,"imagen": "👟"},
    {"nombre": "Gel-1130", "marca": "Asics", "talla": 27, "precio": 1899,"imagen": "👟"},
    {"nombre": "Blazer mid '77", "marca": "Nike", "talla": 27, "precio": 2099,"imagen": "👟"},
    {"nombre": "Chuck Taylor All Star", "marca": "Converse", "talla": 28, "precio": 129,"imagen": "👟"},
    {"nombre": "MB-03", "marca": "Puma", "talla": 27, "precio": 2499,"imagen": "👟"}
]

#### MENU A LA IZQUIERDA   #############################
menu_lateral = ctk.CTkFrame(cuerpo, width=250, corner_radius=10)
menu_lateral.configure(fg_color=TARJETAS, border_color=BORDES)
menu_lateral.grid_propagate(False)
menu_lateral.grid_columnconfigure(0, weight=1)

encabezado_menu = ctk.CTkFrame(menu_lateral, fg_color="transparent")
encabezado_menu.grid(row=0, column=0, padx=10, pady=(10,0), sticky="ew")
encabezado_menu.grid_columnconfigure(0, weight=1)

titulo_menu = ctk.CTkLabel(encabezado_menu, text="MENÚ", text_color=PRINCIPAL,
                           font=("Arial", 14, "bold"))
titulo_menu.grid(row=0, column=0, padx=5, sticky="w")

btn_cerrar = ctk.CTkButton(encabezado_menu, text="✕", width=28, height=28, corner_radius=14,
                           fg_color=PRINCIPAL, hover_color=AZUL, text_color="white", command=menu)
btn_cerrar.grid(row=0, column=1)

secciones = [
    ("GÉNERO", ["Hombre","Mujer","Niños"]),
    ("EXPLORAR", ["Marcas","Tallas","Tipo (running, casual, skate)"])
]

fila_menu = 1

for nombre_seccion, opciones in secciones:

    etiqueta = ctk.CTkLabel(menu_lateral, text=nombre_seccion, text_color=TEXTO_SECUNDARIO,
                            font=("Arial", 10, "bold"))
    etiqueta.grid(row=fila_menu, column=0, padx=15, pady=(15,0), sticky="w")
    fila_menu += 1

    for opcion in opciones:

        boton = ctk.CTkButton(menu_lateral, text=opcion + "   ›", anchor="w",
                              fg_color="transparent", hover_color=BLOQUES_CLAROS,
                              text_color=PRINCIPAL)
        boton.grid(row=fila_menu, column=0, padx=10, pady=4, sticky="ew")
        fila_menu += 1

boton_rebajas = ctk.CTkButton(menu_lateral, text="Rebajas   %", anchor="w",
                              fg_color=ACENTO, hover_color=AZUL, text_color=PRINCIPAL,
                              font=("Arial", 12, "bold"))
boton_rebajas.grid(row=fila_menu, column=0, padx=10, pady=(20,8), sticky="ew")

##########################################################

menu_visible = False
mostrar_productos(productos)

app.mainloop()
