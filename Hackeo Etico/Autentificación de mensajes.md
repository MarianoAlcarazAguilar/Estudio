# Autentificación de mensajes

La autentificación de mensajes es necesaria para:
- Asegurar que el mensaje se transmitió de forma arpopiada
- El contenido no fue alterado o borrado durante su transmisión
- Proteje a los usuarios contra ataques activos

### Estrategias

<div align='right'><b>Autentificación y cifrado simétrico</b></div>

- Simplemente se cifra un mensaje usando encriptación simétrica
- Se asume que solo el emisor y el receptor tienen la llave

Ventajas:
- Se mantiene la confidencialidad del mensaje  

Desventajas:
- Es caro en poder de procesamiento

Usos:
- Transmisión de información crítica

<div align='right'><b>Digests</b></div>

También conocido como *message digests*:

- Un resumen -digest- es un código generado a partir del contenido del mensaje y que se agrega al final de este
- Cuando el mensaje es recibido, el resumen se genera y es comparado con el enviado
- Los digests usualmente viajan cifrados

Ventajas:
- Es barato en términos de procesamiento

Desventajas:
- No asegura la confidencialidad del mensaje

Usos:
- Transmisión de información no crítica o pública
- Transmisión de informaicón sensible a retrasos de transferencia

<div align='right'><b>Código de autentificación</b></div>

Message Autentification Code (MAC)

- El contenido del mensaje y una llave secreta se usan para generar un bloque de datos que se agrega al final del mensaje
- Se utiliza DES para cifrar el mensaje y los últimos bits del mensaje actúan como MAC

Ventajas:
- No se requiere descifrar el mensaje

Desventajas:
- Necesita el mismo poder de procesamiento que DES

### Funciones de Hash seguras

~~~
Huella digital de un mensaje, archivo o bloque de datos
~~~

Una función de hash que se usa para autentificación debe tener las siguientes propiedades:
- Poder aplicarse a mensajes de cualquier tamaño
- Producir una longitud fija a pesar del tamaño del mensaje
- Complejidad computacional razonable
- Hash siempre diferente del mensaje
- Para un mensaje dado, debe ser computacionalmente imposible encontrar otro mensaje con el mismo hash
- Para un par de mensajes, debe ser computacionalmente imposible encontrar un hash idéntico

<div align='right'><b>SHA-1</b></div>

- Desarrollado por NIST en 1993.  
- Tamaño máximo del mensaje: $2^{64}$ bits
- Message digest de 160 bit
- La información se procesa en bloques de 512 bits

<div align='right'><b>MD5</b></div>

- Especificado en el RFC1321
- No hay longitud máxima del mensaje
- Message digest de 128 bit
- La información se procesa en bloques de 512 bits

<div align='right'><b>RIPEMD-160</b></div>

- Desarrollado por investigadores europeos que trataban de romper el MD4 y MD5
- No hay longitud máxima del mensaje
- Message disgest de 160 bit
- Información procesada en bloques de 512 bit

<div align='right'><b>HMAC</b></div>

- Función de hash criptográfica (combinación de MAC y SHA-1)
- Tiene la misma complejidad computacional que SHA-1

