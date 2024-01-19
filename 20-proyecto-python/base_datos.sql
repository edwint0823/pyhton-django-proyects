CREATE DATABASE IF NOT EXISTS master_python;
use master_python;

CREATE TABLE usuarios
(
    id        INTEGER AUTO_INCREMENT NOT NULL,
    nombre    VARCHAR(100),
    apellidos VARCHAR(255),
    email     VARCHAR(255)           not null,
    password  VARCHAR(255)           not null,
    fecha     DATE                   NOT NULL,
    CONSTRAINT pk_usuarios PRIMARY KEY (id),
    CONSTRAINT uq_email UNIQUE (email)
) ENGINE = InnoDb;


CREATE TABLE notas
(
    id          INTEGER AUTO_INCREMENT NOT NULL,
    usuario_id  INTEGER                NOT NULL,
    titulo      VARCHAR(255)           NOT NULL,
    descripcion MEDIUMTEXT,
    fecha       DATE                   NOT NULL,
    CONSTRAINT pk_notas PRIMARY KEY (id),
    CONSTRAINT fk_nota_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
) ENGINE = InnoDb;