CREATE DATABASE disafra;
USE disafra;
CREATE TABLE persona(
	id_persona INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    telefono VARCHAR(20),
    direccion VARCHAR(75),
    email VARCHAR(50),
    fecha_nacimiento DATE,
    edad INT,
    PRIMARY KEY(id_persona)
) ENGINE=InnoDB;

CREATE TABLE sucursal(
	id_sucursal INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    direccion VARCHAR(75) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    email VARCHAR(50),
    PRIMARY KEY(id_sucursal)
) ENGINE=InnoDB;

CREATE TABLE auth_venta(
	id_auth INT NOT NULL AUTO_INCREMENT,
    rango_valor_inicial INT NOT NULL,
    rango_valor_final INT NOT NULL,
    serie VARCHAR(3) NOT NULL,
    PRIMARY KEY(id_auth)
) ENGINE=InnoDB;

CREATE TABLE categoria(
	id_categoria INT NOT NULL AUTO_INCREMENT,
	nombre VARCHAR(25) NOT NULL,
    PRIMARY KEY(id_categoria)
) ENGINE=InnoDB;

CREATE TABLE marca(
	id_marca INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(25) NOT NULL,
    PRIMARY KEY(id_marca)
) ENGINE=InnoDB;

CREATE TABLE descuento(
	cod_descuento VARCHAR(25) NOT NULL,
    descripcion VARCHAR(40) NOT NULL,
    porcentaje INT NOT NULL,
    PRIMARY KEY(cod_descuento)
)ENGINE=InnoDB;

CREATE TABLE proveedor(
	id_proveedor INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50)NOT NULL,
    direccion VARCHAR(75) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    email VARCHAR(50),
    PRIMARY KEY(id_proveedor)
)ENGINE=InnoDB;

CREATE TABLE cliente(
	nit_cliente VARCHAR(13) NOT NULL,
    persona_id INT NOT NULL,
	PRIMARY KEY(nit_cliente),
    FOREIGN KEY(persona_id) REFERENCES persona(id_persona)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE=InnoDB;

CREATE TABLE empleado(
	cod_empleado INT NOT NULL,
    dpi VARCHAR(15) NOT NULL,
    puesto VARCHAR(20) NOT NULL,
    sueldo DOUBLE(7,2) NOT NULL,
    persona_id INT NOT NULL,
	PRIMARY KEY(cod_empleado),
    FOREIGN KEY(persona_id) REFERENCES persona(id_persona)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE=InnoDB;

CREATE TABLE contacto_proveedor(
	id_contacto_proveedor INT NOT NULL AUTO_INCREMENT,
    persona_id INT NOT NULL,
    proveedor_id INT NOT NULL,
	PRIMARY KEY(id_contacto_proveedor),
    FOREIGN KEY(persona_id) REFERENCES persona(id_persona)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY(proveedor_id) REFERENCES proveedor(id_proveedor)
	ON DELETE CASCADE
	ON UPDATE CASCADE
)ENGINE=InnoDB;

CREATE TABLE venta(
	num_venta INT NOT NULL AUTO_INCREMENT,
    fecha_venta DATE NOT NULL,
    total DOUBLE(7,2) NOT NULL,
    cliente_nit VARCHAR(13) NOT NULL,
    empleado_cod INT NOT NULL,
    sucursal_id INT NOT NULL,
    auth_id INT NOT NULL,
    PRIMARY KEY(num_venta),
    FOREIGN KEY(cliente_nit) REFERENCES cliente(nit_cliente)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY(empleado_cod) REFERENCES empleado(cod_empleado)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY(sucursal_id) REFERENCES sucursal(id_sucursal)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY(auth_id) REFERENCES auth_venta(id_auth)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE=InnoDB;

CREATE TABLE producto(
	cod_producto VARCHAR(25) NOT NULL,
    nombre VARCHAR(75) NOT NULL,
    descripcion VARCHAR(100),
    fecha_expiracion DATE NOT NULL,
    existencia INT NOT NULL,
    marca_id INT NOT NULL,
    categoria_id INT NOT NULL,
    precio_venta DOUBLE(7,2) NOT NULL,
    precio_costo DOUBLE(7,2) NOT NULL,
    PRIMARY KEY(cod_producto),
    FOREIGN KEY(marca_id) REFERENCES marca(id_marca)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY(categoria_id) REFERENCES categoria(id_categoria)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE=InnoDB;

CREATE TABLE detalle_producto(
	id_detalle_producto INT NOT NULL AUTO_INCREMENT,
    producto_cod VARCHAR(25) NOT NULL,
    proveedor_id INT NOT NULL,
	PRIMARY KEY(id_detalle_producto),
    FOREIGN KEY(producto_cod) REFERENCES producto(cod_producto)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY(proveedor_id) REFERENCES proveedor(id_proveedor)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE=InnoDB;

CREATE TABLE detalle_venta(
	id_detalle_venta INT NOT NULL AUTO_INCREMENT,
    cantidad INT NOT NULL,
    sub_total DOUBLE(7,2),
    producto_cod VARCHAR(25),
    venta_num INT NOT NULL,
    descuento_cod VARCHAR(25),
    PRIMARY KEY(id_detalle_venta),
    FOREIGN KEY(producto_cod) REFERENCES producto(cod_producto)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY(venta_num) REFERENCES venta(num_venta)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY(descuento_cod) REFERENCES descuento(cod_descuento)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE=InnoDB;

CREATE TABLE compra(
	num_compra INT NOT NULL AUTO_INCREMENT,
    descripcion VARCHAR(40),
    total DOUBLE(7,2) NOT NULL,
    total_pagado DOUBLE(7,2),
    pagado TINYINT(1),
    empleado_cod INT NOT NULL,
	pago_compra_id INT NOT NULL,
    fecha_entrega DATE,
    contacto_proveedor_id INT NOT NULL,
	PRIMARY KEY(num_compra),
    FOREIGN KEY(empleado_cod) REFERENCES empleado(cod_empleado)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY(contacto_proveedor_id) REFERENCES contacto_proveedor(id_contacto_proveedor)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE=InnoDB;

CREATE TABLE pago_compra(
	id_pago_compra INT NOT NULL AUTO_INCREMENT,
    descripcion VARCHAR(25)NOT NULL,
    fecha_pago DATE NOT NULL,
    compra_num INT NOT NULL,
    sub_total DOUBLE(7,2) NOT NULL,
    PRIMARY KEY(id_pago_compra),
    FOREIGN KEY(compra_num) REFERENCES compra(num_compra)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE=InnoDB;

CREATE TABLE detalle_compra(
	id_detalle_compra INT NOT NULL AUTO_INCREMENT,
    compra_num INT NOT NULL,
    detalle_producto_id INT NOT NULL,
    cantidad INT NOT NULL,
    subtotal DOUBLE(7,2) NOT NULL,
	PRIMARY KEY(id_detalle_compra),
    FOREIGN KEY(compra_num) REFERENCES compra(num_compra)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY(detalle_producto_id) REFERENCES detalle_producto(id_detalle_producto)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE=InnoDB;