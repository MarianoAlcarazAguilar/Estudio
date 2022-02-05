# Estudio

## Tablas Transaccionales

Son tablas donde se guardan eventos y transacciones del problema.
Son aquellas propensas a tener cambios constantemente. Como el ingreso de un paciente a un hospital o una venta en una tienda.

Tienen dos atributos importantes: **llave primaria** y **fecha de transacción**.

La frecuencia con la que escribimos en estas tablas nos da una idea de la velocidad de nuestro negocio.

## Tablas de Catálogos

Se caracterizan por tener una frecuencia de actualización lenta o nula. Casi siempre describen **tipos** de algo relevante al problema.

Ejemplos pueden ser:
  1. Elementos geográficos.
  2. Status de algún objeto (e.g. *vivo* o *muerto*)
  3. Tipos o clases de algún objeto (e.g. *tipo de sangre*)

Pueden existir relaciones entre catálogos.
