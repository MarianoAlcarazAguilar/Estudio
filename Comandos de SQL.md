# Estudio
## Comandos de SQL

### Creación de Tablas

Creemos una tabla llamda doctor.
Definamos el ID como primary key, para luego insertar los atributos.
Si ponemos NOT NULL forzamos a siempre introducir algo.
También pongamos una llave foránea de la tabla llamada área.

```sql
CREATE TABLE doctor (
   id_doctor numeric(4,0) CONSTRAINT pk_doctor PRIMARY KEY,
   nombres varchar(50) NOT NULL,
   apellidos varchar(50) NOT NULL,
   fecha_contratacion date NOT NULL,
   sueldo numeric(8,2) NOT NULL,
   id_area numeric(4) REFERENCES area (id_area)
)
```
Ahora creamos un contador para que las id se agreguen automáticamente.

```sql
create sequence _seq start 1 increment 1;
alter table  alter column _id
set default nextval('_seq');
```

### Creación de tablas intermedias

Insertamos las dos llaves foráneas y les ponemos un ON UPDATE CASCADE para que se 
actualicen automáticamente.
Definimos las dos llaves en conjunto como la llave primaria y le ponemos nombre al constraint.

```sql
CREATE TABLE paciente_doctor (
   id_paciente numeric(4) REFERENCES paciente (id_paciente) ON UPDATE CASCADE,
   id_doctor numeric(4) REFERENCES doctor (id_doctor) ON UPDATE CASCADE,
   CONSTRAINT pk_paciente_doctor PRIMARY KEY (id_paciente, id_doctor)
)
```

### Inserción de datos en tablas

Insertemos en el esquema hospital en la tabla doctor.
Especifiquemos las columnas en las que insertamos, damos los valores. 
Podemos insertar varios a la vez.

```sql
INSERT INTO hospital.doctor (nombres, apellidos, fecha_contratacion, sueldo)
VALUES ('Mariano', 'Alcaraz Aguilar', '2020-07-15', 123456),
('Rodrigo', 'García Gutierrez', '2020-07-15', 123456);
```

### Borrado

Eliminemos del esquema hospital en la tabla paciente a Mariano Alcaraz Aguilar.
No olvidar que tenemos que estar libres de constraints.

```sql
DELETE FROM hospital.paciente
WHERE nombres = 'Mariano'
AND apellidos = 'Alcaraz Aguilar';
```

### Eliminado definitivo

Eliminemos la tabla doctor del esquema hospital sin dejar rastro alguno. 
Esta operación no permite cláusula WHERE.

```sql
TRUNCATE hospital.doctor
```

### Actualizar

Modifiquemos algunos atributos.

```sql
UPDATE hospital.paciente
SET nombres = 'Ximena', apellidos = 'Livera'
WHERE nombres = 'Rodrigo'
AND apellidos = 'García Gutierrez';
```

Otra actualización

```sql
UPDATE paciente_doctor
SET principal = true
FROM paciente JOIN paciente_doctor USING (id_paciente)
JOIN doctor USING (id_doctor)
WHERE nombres = 'Ximena' AND apellidos = 'Livera';
```

