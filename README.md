# DeluSneakers 👟

Aplicación de escritorio que simula la interfaz gráfica de una tienda en línea de tenis. El proyecto busca desarrollar un catálogo visual de productos y, progresivamente, incorporar funcionalidades de búsqueda, filtrado y administración de inventario.

Actualmente, el desarrollo se encuentra en la etapa de construcción de la interfaz gráfica (GUI).

## 1. Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python | Lenguaje principal del proyecto. |
| CustomTkinter | Desarrollo de la interfaz gráfica. |
| Tkinter | Sistema de ventanas y gestión de elementos gráficos integrado con Python. |
| Pillow (PIL) | Carga y manipulación de imágenes de productos. |
| Git y GitHub | Control de versiones y colaboración del equipo. |

**Nota:** PostgreSQL, MySQL u otras tecnologías de bases de datos podrán incorporarse en etapas posteriores, cuando se desarrolle la persistencia de la información.

## 2. Requisitos previos

Antes de ejecutar el proyecto, es necesario contar con:

- Python 3 instalado.
- pip (administrador de paquetes de Python).
- Git.
- Un editor de código, preferentemente Visual Studio Code.

Se recomienda utilizar una versión de Python compatible con las librerías del proyecto.

## 3. Instalación y configuración

### Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

Entrar en la carpeta del proyecto:

```bash
cd DeluSneakers
```

### Crear un entorno virtual (recomendado)

```bash
python -m venv venv
```

Activarlo en Windows:

```bash
venv\Scripts\activate
```

### Instalar las dependencias

```bash
python -m pip install --upgrade pip
pip install customtkinter pillow
```

### Ejecutar la aplicación

```bash
python main.py
```

**Importante:** Ejecutar los comandos desde la carpeta raíz del proyecto, donde se encuentra `main.py`.

## 4. Estructura inicial del proyecto

La estructura propuesta para organizar los archivos es la siguiente:

```text
DeluSneakers/
│
├── main.py
├── README.md
│
├── assets/
│   └── images/
│       ├── airforce1.png
│       ├── samba.png
│       ├── newbalance550.png
│       └── dunklow.png
│
└── venv/
```

- `main.py`: contiene la ventana principal, los componentes gráficos y la lógica actual de la interfaz.
- `README.md`: documentación general del proyecto.
- `assets/images/`: almacena las imágenes utilizadas en las tarjetas de productos.
- `venv/`: entorno virtual local. No debe subirse al repositorio.

La estructura podrá modificarse conforme el proyecto crezca.

## 5. Descripción de la interfaz gráfica

La interfaz está construida con CustomTkinter y actualmente se divide en tres secciones principales:

### Encabezado
- Nombre de la tienda: DeluSneakers.
- Botón para mostrar u ocultar el menú lateral.
- Botón de inicio de sesión (actualmente demostrativo).

### Menú lateral
Contiene opciones para organizar o consultar los productos:
- Marcas.
- Tallas.
- Tipo.
- Rebajas.

### Catálogo de productos
- Área desplazable para visualizar los productos.
- Distribución de tarjetas en cuatro columnas.
- Cada tarjeta muestra información como nombre, marca, talla, precio y disponibilidad.
- Se contempla incorporar imágenes individuales para cada producto.

## 6. Información de los productos

Actualmente, los productos se manejan mediante una lista de diccionarios en Python.

Cada producto contiene los siguientes atributos:

| Atributo | Descripción |
|---|---|
| nombre | Nombre o modelo del tenis. |
| marca | Marca del producto. |
| talla | Talla disponible. |
| precio | Precio del producto. |
| imagen | Ruta de la imagen correspondiente (en proceso de integración). |

Los registros actuales son ficticios y se utilizan para las pruebas de la interfaz.

## 7. Pendientes del proyecto

### Interfaz gráfica
- [ ] Integrar imágenes en las tarjetas de productos.
- [ ] Ajustar tamaños, espaciados y distribución de los componentes.
- [ ] Definir la paleta de colores y el diseño visual definitivo.
- [ ] Mejorar la presentación de las tarjetas.

### Funcionalidades
- [ ] Implementar filtros por marca.
- [ ] Implementar filtros por talla.
- [ ] Implementar filtros por tipo de calzado.
- [ ] Implementar filtro de productos en rebaja.
- [ ] Incorporar una barra de búsqueda.
- [ ] Definir el funcionamiento del inicio de sesión.
- [ ] Implementar un carrito de compras.

### Datos y almacenamiento
- [ ] Definir el modelo de datos definitivo.
- [ ] Diseñar la base de datos.
- [ ] Conectar la aplicación con la base de datos.
- [ ] Implementar operaciones para consultar, registrar, actualizar y eliminar productos.

### Organización y documentación
- [ ] Separar la interfaz, los datos y la lógica en módulos cuando sea conveniente.
- [ ] Documentar las funciones principales.
- [ ] Registrar las dependencias del proyecto en `requirements.txt`.
- [ ] Documentar los cambios y avances de cada versión.

## 8. Colaboración mediante GitHub

Para mantener actualizado el proyecto, se recomienda trabajar con ramas y realizar commits descriptivos.

Ejemplo:

```bash
git pull
git add .
git commit -m "Agrega estructura inicial del catalogo"
git push
```

Se recomienda evitar subir:
- La carpeta `venv/`.
- Archivos temporales.
- Configuraciones locales del editor.
- Información sensible o credenciales.

## 9. Estado actual

**Etapa:** Desarrollo de la interfaz gráfica.

El proyecto cuenta con una ventana principal, encabezado, menú lateral, catálogo desplazable y tarjetas de productos generadas dinámicamente a partir de una lista de diccionarios.

Las funcionalidades de búsqueda, filtrado, autenticación, carrito y conexión a bases de datos todavía se encuentran pendientes de implementación.

---

*Este documento corresponde a una versión inicial de la documentación. Se actualizará conforme avance el desarrollo y se definan la arquitectura, las funcionalidades y las tecnologías definitivas del proyecto.*
