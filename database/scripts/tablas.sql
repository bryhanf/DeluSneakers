-- CREACIÓN DE LAS TABLAS DE LA BASE DE DATOS 

-- Creación de los tipos de dato específicos
CREATE TYPE estado_pedido AS ENUM ('pendiente', 'enviado', 'entregado', 'cancelado');
CREATE TYPE estado_dev AS ENUM ('pendiente', 'aprobada', 'rechazada');
CREATE TYPE estado_pago AS ENUM ('pendiente', 'completado', 'fallido');
CREATE TYPE tipo_movimiento AS ENUM ('entrada', 'salida', 'ajuste');
CREATE TYPE metodo_pago AS ENUM ('efectivo', 'tarjeta_credito', 'tarjeta_debito', 'paypal');
-- Nuevo tipo de dato para el genero del prodcuto
CREATE TYPE genero AS ENUM ('femenino', 'masculino', 'unisex');

-- CREACIÓN DE LAS TABLAS 

CREATE TABLE categorias (
id_categoria SERIAL PRIMARY KEY,
nombre_categoria VARCHAR(30) NOT NULL,
descripcion_cat TEXT
);

CREATE TABLE clientes (
id_cliente SERIAL PRIMARY KEY,
nombre VARCHAR(50) NOT NULL,
email VARCHAR(50) NOT NULL,
celular VARCHAR(20),
direccion VARCHAR(150)
);

CREATE TABLE proveedores (
id_proveedor SERIAL PRIMARY KEY,
empresa VARCHAR(100) NOT NULL,
nombre_contacto VARCHAR(50),
celular_prov VARCHAR(20),
email_prov VARCHAR(50)
);

CREATE TABLE productos (
id_producto SERIAL PRIMARY KEY,
id_categoria INTEGER NOT NULL,
id_proveedor INTEGER NOT NULL,
nombre_producto VARCHAR(100) NOT NULL,
genero_producto genero NOT NULL,
descripcion_producto TEXT,
precio NUMERIC(12,2) NOT NULL,
stock_minimo INTEGER,
CONSTRAINT fk_categoria
    FOREIGN KEY (id_categoria)
    REFERENCES categorias (id_categoria),
CONSTRAINT fk_proveedor
    FOREIGN KEY (id_proveedor)
    REFERENCES proveedores(id_proveedor)
);

CREATE TABLE movimientos (
id_movimiento SERIAL PRIMARY KEY,
id_producto INTEGER NOT NULL,
tipo_movimiento tipo_movimiento NOT NULL,
cantidad_movimiento INTEGER NOT NULL,
fecha_movimiento TIMESTAMP NOT NULL,
CONSTRAINT fk_producto_mov 
    FOREIGN KEY (id_producto) 
    REFERENCES productos(id_producto)
);


CREATE TABLE pedidos (
id_pedido SERIAL PRIMARY KEY,
id_cliente INTEGER NOT NULL,
fecha_pedido TIMESTAMP NOT NULL,
total_pedido NUMERIC(12, 2) NOT NULL,
costo_envio NUMERIC(12, 2),
estado_pedido estado_pedido NOT NULL,
num_seguimiento VARCHAR(50),
CONSTRAINT fk_cliente_ped 
    FOREIGN KEY (id_cliente) 
    REFERENCES clientes(id_cliente)
);

CREATE TABLE devoluciones (
id_devolucion SERIAL PRIMARY KEY,
id_pedido INTEGER NOT NULL,
id_producto INTEGER NOT NULL,
cantidad_dev INTEGER NOT NULL,
motivo TEXT,
estado_dev estado_dev NOT NULL,
CONSTRAINT fk_pedido
	FOREIGN KEY (id_pedido) 
	REFERENCES pedidos(id_pedido),
CONSTRAINT fk_producto
	FOREIGN KEY (id_producto)
	REFERENCES productos(id_producto)
);


CREATE TABLE detalle_pedidos (
id_detalle SERIAL PRIMARY KEY,
id_pedido INTEGER NOT NULL,
id_producto INTEGER NOT NULL,
cantidad_comprada INTEGER NOT NULL,
precio_unitario NUMERIC(12, 2) NOT NULL,
CONSTRAINT fk_pedido_det 
    FOREIGN KEY (id_pedido) 
    REFERENCES pedidos(id_pedido),
CONSTRAINT fk_producto_det 
    FOREIGN KEY (id_producto) 
    REFERENCES productos(id_producto)
);

CREATE TABLE pagos (
id_pago SERIAL PRIMARY KEY,
id_pedido INTEGER NOT NULL,
metodo_pago metodo_pago NOT NULL,
monto NUMERIC(12, 2) NOT NULL,
fecha_pago TIMESTAMP NOT NULL,
estado_pago estado_pago NOT NULL,
CONSTRAINT fk_pedido_pag 
    FOREIGN KEY (id_pedido) 
    REFERENCES pedidos(id_pedido)
);

-- Nueva tabla para las tallas
CREATE TABLE tallas_productos (
    id_talla SERIAL PRIMARY KEY,
    id_producto INTEGER NOT NULL,
    talla VARCHAR(10) NOT NULL,
    stock_talla INTEGER NOT NULL,
    CONSTRAINT fk_producto_talla 
        FOREIGN KEY (id_producto) 
        REFERENCES productos(id_producto)
);