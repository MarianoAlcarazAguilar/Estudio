# Estudio

## Normalización

Normalizar es aplicar una serie de reglas para evitar inconsistencias en las consultas de datos, anomalías en operaciones de inserción, actualización y borrado.

#### Anomalías evitadas con la normalización

1. Anomalías de `insert`
2. Anomalías de `update`
3. Anomalías de `delete`

### Primera Forma Normal (1NF)

Debe cumplir los siguientes requerimientos:
  
  1. Cada celda debe contener 1 y solo 1 valor.
  2. Cada valor debe ser único.
  3. Eliminar nombres de atributos repetidos.

### Segunda Forma Normal (2NF)

Debe cumplir con los siguientes requerimientos:

  1. Cumplir con 1NF.
  2. Todos los atributos o columnas de una tabla deben pertener a la entidad que representa
        Un atributo X pertenece a una entidad Y sy para saber X podemos depender del PK de Y.
        Básicamente es que en la tabla `paciente` no pongamos el precio de los servicios de limpieza del hospital.
  3. Excepto relaciones N a M, las Primary Keys no deben ser compuestas y debe ser de un solo atributo.

### Tercera Forma Normal (3NF)

Debe cumplir los siguientes requerimientos:

  1. Cumplir con 2NF.
  2. No hay dependencias transitivas
        No hay atributo A que para llegar a él se requiera del atributo B (al que a su vez se llega por la PK).
        Por ejemplo, en una tienda de rentas, el valor de renta de una película no depende de la película *per se*, osea no 
        es un atributo propio de la película. No es como que el director haya dicho: "Quiero que esta película se rente en $$$".
        En ese caso sería mejor hacer otra tabla con precios de renta.


