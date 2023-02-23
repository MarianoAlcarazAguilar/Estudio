# Criptografía

## Simétrica
Modifica el contenido de un mensaje de acuerdo a un patrón determinado conocido únicamente por el remitente y el receptor. Tiene como **objetivo** evitar que otros accedan al contenido.

Un mensaje cifrado es:
1. Transformado
2. Transmitido
3. Sin cambios

El patrón determinado (*llave*) debe transmitirse por separado

### Componentes
- Mensaje
- Algoritmo de cifrado
- Llave secreta
- Texto cifrado
- Algoritmo de descifrado

El **éxito depende** de la confidencialidad de la llave y que esta sea compartida únicamente entre el remitente y el destinatario.

### Algoritmo de Feistel

### Data Encryption Standard (DES)

Es un algoritmo de cifrado simétrico basado en bloques:
- 64 bit code
- 56 bit key
- 16 vueltas, por lo tanto, 16 subllaves deben ser generadas
 
**Ventajas**
- No tiene fallas fatales hasta ahora
**Desventajas**
- Se rompió por medio de un ataque de fuerza bruta en 1998.

### Triple DES
Igual que DES, pero usa tres ejecuciones distintas del algoritmo DES con tres llaves distintas.

- Se utiliza en aplicaciones financieras

$$ 
C = E_{K_3}[D_{K_2}[E_{K_1}[P]]]
$$

**Ventajas**
- Llaves efectivas de 128 bits
**Desventaja**
- Más poder de procesamiento

### Advanced Encryption Standard (AES- RinjDael)
AES se pensó como un algoritmo ligero que tiene la misma seguridad que 3DES con menos poder de procesamiento

- Block length de 128 bits
- Soporta llaves de 128, 192 y 256 bits
- NO sigue una estructura de Feistel
- Puede ser implementado en Hardware y software

### Otros algoritmos simétricos

- RC6
- Twofish
- Serpent
- MARS

### Conclusiones
- La información cifrada tiene más probabilidades de permanecer privada
- Los algoritmos de cifrado más comunes utilizan estructuras de Feistel
- La longitud del bloque y de la llave determinan la eficiencia de los algoritmos basados en bloques
- AES resuelve el problema de procesamiento y de tamaño de llaves
- La transmisión de las llaves representa un problema

## Llave Pública
Propuesto por Diffie y Hellman en 1976

- Está basado en funcione matemáticas y no en operaciones de bits
- Se utiliza principalmente para cifrar mensajes
- Otros usos:
   - Confidencialidad
   - Distribución de llaves
   - Autentificación

### Elementos
- Mensaje
- Algoritmo de cifrado
- Llave pública y privada
- Texto cifrado
- Algoritmo de descifrado

### Condiciones para aplicabilidad
Un algoritmo de llave pública debe tener las siguientes características:
- Tener un requerimiento de procesamiento aceptable para generar ambas llaves
- Fácil para un emisor cifrar un mensaje sabiendo la llave pública
- Computacionalmente efectivo descifrar el mensaje usando la llave privada
- Computacionalmente imposible adivinar la llave privada

### Algoritmo RSA
- Desarrollado por **R**ivest, **S**hamir y **A**dleman en 1977
- Es el algoritmo de llave pública más aceptado
- En RSA, el mensaje, texto cifrado y llaves se representan por números enteros

**Operación de RSA**

$$
C = M^e mod (n) \\
M = C^d mod(n) = (M^e)^dmod(n) = M^{ed}mod(n)
$$

con $ 0 < M, C < n$.

Tenemos también que,
- Llava pública $\rightarrow$ e, n
- Llave privada $\rightarrow$ d, n

$e$ y $n$ deben ser enteros grandes para que el algoritmo sea robusto.

**Algoritmo RSA**

1. Seleccionar dos números primos $p$ y $q$ (deben ser primos grandes)
2. $n = p \cdot q$
3. Calcular $\phi (n) = (p-1)(q-1)$
4. Seleccionar un entero $e$, tal que $e$ es un primo relativo de $\phi(n)$
5. Calcular $d$, tal que $d\quad mod \quad (\phi(n) )= 1$
6. Llave privada $\rightarrow$ $e, n$
7. Llave pública $\rightarrow$ $d, n$

### Certificados de llaves públicas

- Las llaves públicas están a la vista de todos, pero deben ser autentificadas
- Los certificados son llaves públicas y una identificación del usuario emitido por una Autoridad Certificadora
- Un usuario que quiera validar la autenticidad de una llave pública puede contactar a la Autoridad Certificadora

### Distribución de llaves simétricas
- Los algoritmos de llave pública pueden ser usados para distribuir llaves simétricas
- Se cifra la llave secreta con una llave de sesión (que se usa una sola vez)
- Se cifra la llave de sesión usando una llave pública certificada
- Se pega la llave de sesión cifrada y se envían ambas

