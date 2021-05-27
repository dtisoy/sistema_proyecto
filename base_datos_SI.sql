-- DROP DATABASE IF EXISTS proyecto_SistemaYRedes;

-- Crear base de datos
-- CREATE DATABASE proyecto_SistemaYRedes;

USE bonnnebwnn4sjw9twogv;

-- Insertando tablas
CREATE TABLE administradores (
    id_admin integer(11) NOT NULL PRIMARY KEY UNIQUE,
    nom_admin varchar(100) NOT NULL,
    cor_admin varchar(50) NOT NULL,
    con_admin varchar(20) NOT NULL,
    car_admin varchar(100) NOT NULL
);

CREATE TABLE tecnicos (
    ce_tec integer(11) NOT NULL PRIMARY KEY UNIQUE,
    nom_tec varchar(100) NOT NULL,
    car_tec varchar(100) NOT NULL,
    cor_tec varchar(50) NOT NULL,
    equ_tec varchar(50) NOT NULL
);

CREATE TABLE equipos (
    id_equ integer(10) NOT NULL PRIMARY KEY,
    nom_equ varchar(100) NOT NULL,
    dep_equ varchar(50),
    des_equ varchar(500)
);

CREATE TABLE orden_trabajo (
    id_ord integer(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_tec_ord integer(11),
    id_equ_ord integer(10),
    est_ord varchar(50) NOT NULL,
    fec_ord date NOT NULL,
    dep_ord varchar(50) NOT NULL,
    des_ord varchar(500),
    cost_ord integer(20),
    CONSTRAINT fk_id_tec FOREIGN KEY (id_tec_ord) REFERENCES tecnicos (ce_tec),
    CONSTRAINT fk_id_equ FOREIGN KEY (id_equ_ord) REFERENCES equipos (id_equ)
);

-- Insertando informacion en las tablas
-- administradores
INSERT INTO
    administradores (
        id_admin,
        nom_admin,
        cor_admin,
        con_admin,
        car_admin
    )
VALUES
    (
        01006742683,
        'daniel tisoy',
        'danieltisoy2001@gmail.com',
        '12345678',
        'coordinador general'
    );

INSERT INTO
    administradores (
        id_admin,
        nom_admin,
        cor_admin,
        con_admin,
        car_admin
    )
VALUES
    (
        01006742694,
        'luis andrade',
        'danieltisoy2001@gmail.com',
        '12345678',
        'Director equipo de redes'
    );

INSERT INTO
    administradores (
        id_admin,
        nom_admin,
        cor_admin,
        con_admin,
        car_admin
    )
VALUES
    (
        01006742693,
        'clara rodrigez',
        'danieltisoy2001@gmail.com',
        '12345678',
        'Director equipo de diseño'
    );

-- Tecnicos
INSERT INTO
    tecnicos (ce_tec, nom_tec, car_tec, cor_tec, equ_tec)
VALUES
    (
        27469745,
        'laura lopez',
        'dibujo técnico',
        'lau13@gmail.com',
        'diseño'
    );

INSERT INTO
    tecnicos (ce_tec, nom_tec, car_tec, cor_tec, equ_tec)
VALUES
    (
        27469765,
        'andrea arteaga',
        'tecnico en sistemas',
        'andrea23@gmail.com',
        'redes'
    );

INSERT INTO
    tecnicos (ce_tec, nom_tec, car_tec, cor_tec, equ_tec)
VALUES
    (
        28479745,
        'Mary benavides',
        'marketing',
        'mary@gmail.com',
        'diseño'
    );

INSERT INTO
    tecnicos (ce_tec, nom_tec, car_tec, cor_tec, equ_tec)
VALUES
    (
        37469745,
        'carlos enriquez',
        'desarrollo de software',
        'carlsagan@gmail.com',
        'diseño'
    );

-- equipos
INSERT INTO
    equipos (id_equ, nom_equ, dep_equ, des_equ)
VALUES
    (
        01,
        'portatil asus 4030',
        'recursos humanos',
        'computador portatil, cargador, mouse, mousepad'
    );

INSERT INTO
    equipos (id_equ, nom_equ, dep_equ, des_equ)
VALUES
    (
        02,
        'mesa',
        'recursos humanos',
        'mesa rimax'
    );

INSERT INTO
    equipos (id_equ, nom_equ, dep_equ, des_equ)
VALUES
    (
        03,
        'silla',
        'recursos humanos',
        'silla ejecutiva'
    );

INSERT INTO
    equipos (id_equ, nom_equ, dep_equ, des_equ)
VALUES
    (
        11,
        'portatil dell',
        'mantenimiento',
        'computador portatil dell n4030, cargador, mouse, mousepad'
    );

INSERT INTO
    equipos (id_equ, nom_equ, dep_equ, des_equ)
VALUES
    (
        12,
        'escritorio',
        'mantenimiento',
        'escritorio de madera'
    );

INSERT INTO
    equipos (id_equ, nom_equ, dep_equ, des_equ)
VALUES
    (
        21,
        'router wifi',
        'inventario',
        'router wifi etb'
    );

INSERT INTO
    equipos (id_equ, nom_equ, dep_equ, des_equ)
VALUES
    (
        31,
        'computador',
        'coordinación',
        'computador de escritorio dell, mause, teclado'
    );

-- orden de trabajo
INSERT INTO
    orden_trabajo (
        id_tec_ord,
        id_equ_ord,
        est_ord,
        fec_ord,
        dep_ord,
        des_ord,
        cost_ord
    )
VALUES
    (
        27469745,
        01,
        'realizando',
        '26/01/21',
        'recursos humanos',
        'diseño de planos arquitectonios baño',
        1000000
    );

INSERT INTO
    orden_trabajo (
        id_tec_ord,
        id_equ_ord,
        est_ord,
        fec_ord,
        dep_ord,
        des_ord,
        cost_ord
    )
VALUES
    (
        27469745,
        01,
        'programado',
        '11/10/21',
        'recursos humanos',
        'diseño fachada proyecto Casa clara',
        3000000
    );

INSERT INTO
    orden_trabajo (
        id_tec_ord,
        id_equ_ord,
        est_ord,
        fec_ord,
        dep_ord,
        des_ord,
        cost_ord
    )
VALUES
    (
        27469765,
        11,
        'terminado',
        '26/06/20',
        'mantenimiento',
        'mantenimiento del computador',
        200000
    );

