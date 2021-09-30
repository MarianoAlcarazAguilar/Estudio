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
