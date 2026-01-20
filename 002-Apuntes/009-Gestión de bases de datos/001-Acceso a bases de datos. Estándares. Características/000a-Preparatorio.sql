sudo mysql -u root -p

CREATE DATABASE empresa2026;
Use empresa2026;

CREATE TABLE clientes(
	nombre VARCHAR(255),
	apellidos VARCHAR(255),
	email VARCHAR(255)
);

INSERT INTO clientes VALUES(
	"Daniel",
	"Oliveira Vidal",
	"info@elorange.com"
);

SELECT * FROM clientes;

+--------+----------------+-------------------+
| nombre | apellidos      | email             |
+--------+----------------+-------------------+
| Daniel | Oliveira Vidal | info@elorange.com |
+--------+----------------+-------------------+

