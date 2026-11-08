import customtkinter as ctk
ctk.set_appearance_mode("light") 
app = ctk.CTk()  #variable donde se guardará la ventana

app.geometry("1250x720")
app.title("DeluSneakers.com") # configuracion inicial de la ventana

app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(0, weight=1) 

######################################################################
#Encabezado:
encabezado = ctk.CTkFrame(app, height=60, corner_radius=0)
encabezado.grid(row= 0, column = 0, sticky="ew", padx=10, pady=10) #va en la fila 0
encabezado.grid_columnconfigure(0, weight=0) 
encabezado.grid_columnconfigure(1, weight=1) 
encabezado.grid_columnconfigure(2, weight=0)
######################################################################
menu_visible = False
def menu ():
    global menu_visible

    if menu_visible:
        menu_lateral.grid_remove()
        menu_visible = False
    else:
        menu_lateral.grid()
        menu_visible = True

def login():
    print("login funciona")

btn_menu = ctk.CTkButton (encabezado, text="Menu", width=45, command=menu)
btn_menu.grid(row=0, column=0, padx=10, pady=10)

titulo = ctk.CTkLabel(encabezado, text="DeluSneakers", 
                      font=("Arial", 24, "bold") )
titulo.grid(row = 0, column = 1, padx=10, pady=10)

btn_login = ctk.CTkButton(encabezado, text="Iniciar sesion", width= 60, command=login)
btn_login.grid(row=0, column =2, padx=10, pady=10)

########################################################
#Cuerpo:
cuerpo = ctk.CTkFrame(app, corner_radius=0, fg_color= "transparent")
cuerpo.grid(row=1, column=0, sticky= "nsew", padx=10, pady=(0,10) )#va en la fila 1
cuerpo.grid_columnconfigure(1, weight=1)
cuerpo.grid_rowconfigure(0, weight=1)
##########################################################

#### MENU A LA IZQUIERDA   #############################
menu_lateral = ctk.CTkFrame(cuerpo, width=190, corner_radius=10)
menu_lateral.grid(row=0, column=0, sticky="ns", padx=(0,10))
menu_lateral.grid_remove()
menu_lateral.grid_propagate(False)


opciones = ["Marcas","Tallas","Tipo","Rebajas"]

for i, opcion in enumerate(opciones):

    boton = ctk.CTkButton(menu_lateral,text=opcion,anchor="w")
    boton.grid(row=i,column=0,padx=10,pady=8,sticky="ew")
##########################################################

################# CONTENIDO A LA DERECHA ######
contenido = ctk.CTkFrame(cuerpo, corner_radius=10)
contenido.grid (row = 0, column = 1, sticky = "nsew")
contenido.grid_columnconfigure(0,weight=1)
contenido.grid_rowconfigure(1,weight=1)

##########################################################
#productos:
titulo_catalogo = ctk.CTkLabel(contenido, text="Nuestros productos", 
                      font=("Arial", 24, "bold") )
titulo_catalogo.grid(row= 0, column = 0, sticky="w", padx=20, pady=20)

catalogo = ctk.CTkScrollableFrame(contenido)
catalogo.grid(row= 1, column=0, sticky = "nsew")

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
    {"nombre": "MB-03", "marca": "Puma", "talla": 27, "precio": 2499,"imagen": "👟"} ]

for columna in range (4):
    catalogo.grid_columnconfigure(columna, weight=1)

def crear_tarjeta(parent, producto, fila, columna):
    tarjeta = ctk.CTkFrame( parent, corner_radius=10, height=300)
    tarjeta.grid(row=fila, column=columna, padx=10, pady=10, sticky="nsew")

    tarjeta.grid_propagate(False)
    tarjeta.grid_columnconfigure(0,weight=1)

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


for i, producto in enumerate(productos):
    fila = i // 4
    columna = i % 4

    crear_tarjeta(catalogo,producto, fila, columna)
app.mainloop()
