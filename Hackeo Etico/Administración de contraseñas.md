# Administración de contraseñas

### Contraseñas robustas

Características:

- Longitud de al menos 10 caracteres para contraseñas de usuarios finales, más para cuentas privilegiadas o de administración
- Combinación de mayúsculas, minúsculas, números y caractéres especiales
- Evitar caracteres en orden alfabético
- Deben ser aleatorias

No deben contener ninguna información personal relacionada con el usuario o el sistema que se quiere proteger.

- Deben cambiarse con la frecuencia adecuada de acuerdo a la información que protege

### Mecanismos de protección

- Almacenamiento y transferencia de contraseñas usando hashes
- Políticas para forzar al usuario a usar contraseñas robustas
- Cifrado en reposo de hashes de contraseñas
- Cifrado de hashes de contraseñas en tránsito
- Notificación al usuario de posibles irregularidades en el almacenamiento, tránsito de las contraseñas
- No permitir la repetición
- Bloquear cuentas al detectar posible ataque

### Ataques a contraseñas

<div align='right'><b>Fuerza Bruta</b></div>

- Es tardado pero efectivo (eventualmente se encontrará la contraseña buscada)
- Consiste en probar todas las combinaciones posibles hasta encontrar la que se busca
- Si el sistema es reactivo, un ataque de fuerza bruta causará el bloqueo de la cuenta y forzará al usuario a utilizar otra contraseña
- Funciona para evaluar la solidez de las contraseñas en un sistema
- Requiere de mucho poder de procesamiento, especialmente si las contraseñas son sólidas

<div align='right'><b>Diccionario</b></div>

- Dados los hábitos de los usuarios para elegir contraseñas, utilizan diccionarios predefinidos y pre-hasheados para adivinar contraseñas
- Es más rápido y efectivo que un ataque de fuerza bruta
- Únicamente se prueban contraseñas probables
- Los diccionarios vienen de ataques previos y de contraseñas comunmente utilizadas

<div align='right'><b>Tablas Arcoíris</b></div>

Idealmente, dado un hash, se generan y almacenan todas las contraseñas posibles y sus respectivos hashes, esto hace el ataque infalible. Sin embargo, el espacio para almacenar las contraseñas es grande.  
<br>
En una tabla arcoíris se crean cadenas de contraseñas transformadas por una función de hash alternadamente por una función de reducción que produce contraseñas.  
<br>
Si la contraseña que se está atacando existe en la cadea, se probará al aplicar alguna función durante la cadena.  
<br>
Se sacrifica velocidad por espacio de almacenamiento. Es posible defenderse de este tipo de ataques con una función generadora de llaves que sua **sales**.

### Uso de sales

~~~
Número aleatorio para incrementar la complejidad de la contraseña sin poner presión en el usuario para pensar en una contraseña más larga
~~~

Sirven para evitar ataques con tablas arcoíris y hacen más lentos los ataques de fuerza bruta.

- Si dos usuarios tienen la misma contraseña, la sal asegura que los hashes sean distintos
- Las sales pueden guardarse en texto claro con la contraseña
- Las sales nunca deben viajar por redes, son para uso local

**Sisema UNIX** 

Durante mucho tiempo, guardaron las contraseñas en texto claro en el archivo `/etc/passwd``

- Al escalar el número de ataques, se empezaron a almacenar las contraseñas en formato has en el archivo `/etc/shadow`
- Seguían siendo vulnerables a ataques de fuerza bruta, diccionario y arcoríris

Se diecidieron las siguientes modificaciones:
- Cifrar contraseñas con crypt: DES modificado con 25 vueltas
- Re-hash usando MD5, Blowfish, SHA-256 o SHA-512
- Guradar id, salt, hased, algoritmo
- La sal se relaciona con la hora en que el usuario creó la contraseña

