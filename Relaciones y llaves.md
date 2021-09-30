# Estudio

## Relaciones y llaves

### Relaciones 1 a N

La usamos cuando la `entidad A` puede tener 1 o más objetos del tipo `entidad B`.

La entidad en el extremo **1** copia su llave a la entidad en el extremo **N**
En este caso A tiene relación 1 a N con B. Por lo tanto, copiamos la llave de A y la ponemos en la tabla B.

### Relaciones 1 a 1

Copiamos a llave primara de la entidad primaria como llave foránea a la entidad secundaria. 
Se agrega un **CONSTRAINT** de tipo **UNIQUE**
para que no pueda tener valores repetidos a lo largo de la tabla.

### Relaciones recursivas

Es cuando la referencia es a la llave primaria de la mista tabla. Simplemente se agrega como llave foránea bajo otro nombre.

### Relaciones N a N

Necesitamos hacer una tabla auxiliar en la que agreguemos ambas llaves primarias de las tablas involucradas.
Para más información ver el md de Comandos de SQL.

#### Buenas prácticas para llaves primarias

1. No tener que ver con el objeto
2. No ser repetible
3. De preferencia ser numérica, entera y consecutiva.

#### Uso de llaves compuestas

1. En las tablas intermedias de relaciones N a N.
2. En tablas con información histórica
      Se guarda la llave de la entidad a la que se le hará la tabla y un **timestamp**
     
