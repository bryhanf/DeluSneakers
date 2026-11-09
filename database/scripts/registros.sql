-- INSERCIÓN DE REGISTROS EN LAS TABLAS DE LA BASE DE DATOS (TEMPORAL/FUNCIONAL)

-- Categorías
INSERT INTO categorias (nombre_categoria, descripcion_cat) VALUES
    ('Casual', 'Calzado clásico y de estilo urbano para uso diario'),
    ('Running', 'Tenis diseñados para alto rendimiento y comodidad al correr'),
    ('Basketball', 'Calzado deportivo con soporte de tobillo especializado para la duela'),
    ('Skateboarding', 'Tenis de suela plana y alta durabilidad para patinar y uso casual');

-- Proveedores (Marcas Principales)
INSERT INTO proveedores (empresa, nombre_contacto, celular_prov, email_prov) VALUES
    ('Nike de México S.A.', 'Roberto Sánchez', '5511223344', 'ventas@nike.com.mx'),
    ('Adidas Group México', 'Claudia Morales', '5522334455', 'contacto@adidas.mx'),
    ('Converse Inc.', 'Alejandro Garza', '5533445566', 'pedidos@converse.com'),
    ('Vans Distribution', 'Fernando Ruiz', '5544556677', 'mx.ventas@vans.com'),
    ('Puma Sports México', 'Mariana Torres', '5555667788', 'contacto@puma.com'),
    ('New Balance Athletics', 'Daniel Pérez', '5566778899', 'ventas@newbalance.mx'),
    ('Reebok International', 'Sofía Gómez', '5577889900', 'pedidos@reebok.mx');

-- Productos (Modelos Más Populares)
INSERT INTO productos (id_categoria, id_proveedor, nombre_producto, genero_producto, descripcion_producto, precio, stock_minimo) VALUES
    -- Nike Air Force 1
        (1, 1, 'Nike Air Force 1 07 (Triple White)', 'unisex', 'Clásico calzado urbano de piel en color blanco total con amortiguación Air', 2399.00, 5),
    -- Adidas Samba OG
        (1, 2, 'Adidas Samba OG (Cloud White / Core Black)', 'unisex', 'Tenis icónicos de perfil bajo con exterior de piel prémium y franjas negras', 2199.00, 5),
    -- Converse Chuck Taylor All Star
        (1, 3, 'Converse Chuck Taylor All Star Bota (Classic Black)', 'unisex', 'El clásico e inconfundible tenis de lona de bota alta en color negro', 1599.00, 5),
        (1, 3, 'Converse Chuck Taylor All Star Choclo (Classic Black)', 'unisex', 'Versión clásica de corte bajo en lona color negro', 1499.00, 5),
    -- Vans Old Skool
        (4, 4, 'Vans Old Skool (Black / White)', 'unisex', 'Tenis clásicos de skate con la emblemática franja lateral Sidestripe', 1499.00, 5),
    -- Nike Dunk Low
        (1, 1, 'Nike Dunk Low Retro (White / Black - Panda)', 'unisex', 'Diseño retro de básquetbol adaptado al estilo urbano en combinación blanco y negro', 2499.00, 5),
        (1, 1, 'Nike Dunk Low (University Blue)', 'femenino', 'Combinación popular en tonos blancos y azul universitario', 2699.00, 5),
        (1, 1, 'Nike Dunk Low (Grey Fog)', 'masculino', 'Diseño minimalista en tonos gris claro y blanco', 2599.00, 5),
        (1, 1, 'Nike Dunk Low (Rose Whisper)', 'femenino', 'Modelo clásico en tonos blanco y rosa pastel suave', 2499.00, 5),
    -- Puma Suede
        (1, 5, 'Puma Suede Classic (Black / White)', 'masculino', 'Legendario calzado de gamuza suave con suela de goma adherente', 1899.00, 5),
        (1, 5, 'Puma Suede Classic (Peacoat / White)', 'femenino', 'Versión en color azul marino oscuro con detalles blancos', 1899.00, 5),
    -- Nike Jordan 4
        (3, 1, 'Nike Air Jordan 4 Retro (Bred Reimagined)', 'masculino', 'Silueta emblemática de alta gama con detalles icónicos en piel negra y roja', 4799.00, 3),
    -- Adidas Spezial
        (1, 2, 'Adidas Handball Spezial (Core Black / Clear Pink)', 'femenino', 'Calzado retro de perfil estilizado con gamuza negra y acentos rosados', 2399.00, 5),
    -- Converse Chuck Taylor 70
        (1, 3, 'Converse Chuck Taylor 70 Vintage (Canvas White)', 'unisex', 'Edición de lujo inspirada en el diseño original de los años 70 con lona más gruesa', 1999.00, 5),
    -- New Balance 530
        (2, 6, 'New Balance 530 (White / Silver / Navy)', 'unisex', 'Tenis de running retro con malla transpirable y estética de los 2000', 2799.00, 5),
    -- Reebok Club C
        (1, 7, 'Reebok Club C 85 Vintage (Chalk / Classic White)', 'unisex', 'Tenis minimalistas de piel suave con suela de caucho retro', 2199.00, 5);

-- Tallas y Stock
INSERT INTO tallas_productos (id_producto, talla, stock_talla) VALUES
    -- Producto 1 (Air Force 1 - Unisex)
        (1, '22', 6), (1, '23', 8), (1, '24', 7), (1, '25', 10), (1, '26', 9), (1, '27', 8), (1, '28', 6), (1, '29', 5), (1, '30', 5),
    -- Producto 2 (Adidas Samba OG - Unisex)
        (2, '22.5', 5), (2, '23', 8), (2, '24', 9), (2, '25', 7), (2, '26', 10), (2, '27', 8), (2, '28', 6), (2, '29', 5),
    -- Productos 3 y 4 (Converse Bota y Choclo - Unisex)
        (3, '23', 8), (3, '24', 10), (3, '25', 9), (3, '26', 7), (3, '27', 8), (3, '28', 6),
        (4, '23', 7), (4, '24', 9), (4, '25', 10), (4, '26', 8), (4, '27', 6), (4, '28', 5),
    -- Producto 5 (Vans Old Skool - Unisex)
        (5, '23', 6), (5, '24', 8), (5, '25', 9), (5, '26', 10), (5, '27', 7), (5, '28', 6), (5, '29', 5),
    -- Productos 6, 7, 8, 9 (Nike Dunk Low - Variantes)
        (6, '23', 7), (6, '24', 9), (6, '25', 10), (6, '26', 8), (6, '27', 6), (6, '28', 5), (6, '29', 5),
        (7, '22', 6), (7, '23', 8), (7, '24', 10), (7, '25', 7), (7, '26', 6), (7, '27', 5),
        (8, '25', 8), (8, '26', 10), (8, '27', 9), (8, '28', 7), (8, '29', 6), (8, '30', 5),
        (9, '22', 5), (9, '23', 7), (9, '24', 9), (9, '25', 8), (9, '26', 6), (9, '27', 5),
    -- Productos 10 y 11 (Puma Suede)
        (10, '25', 7), (10, '26', 9), (10, '27', 8), (10, '28', 6), (10, '29', 5), (10, '30', 5),
        (11, '22', 6), (11, '23', 8), (11, '24', 7), (11, '25', 9), (11, '26', 6), (11, '27', 5),
    -- Producto 12 (Jordan 4 - Masculino)
        (12, '25', 5), (12, '26', 6), (12, '27', 7), (12, '28', 5), (12, '29', 5), (12, '30', 5),
    -- Producto 13 (Adidas Spezial - Femenino)
        (13, '22', 6), (13, '23', 8), (13, '24', 9), (13, '25', 7), (13, '26', 6), (13, '27', 5),
    -- Producto 14 (Converse 70 - Unisex)
        (14, '23', 7), (14, '25', 8), (14, '26', 10), (14, '27', 6), (14, '28', 5),
    -- Producto 15 (New Balance 530 - Unisex)
        (15, '23', 6), (15, '24', 8), (15, '25', 10), (15, '26', 9), (15, '27', 7), (15, '28', 6), (15, '29', 5),
    -- Producto 16 (Reebok Club C - Unisex)
        (16, '23', 7), (16, '24', 9), (16, '25', 8), (16, '26', 10), (16, '27', 6), (16, '28', 5);