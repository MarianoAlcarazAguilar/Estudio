# Presentaciones
Aquí van a estar todas las presentaciones de mis compañeros porque resulta que también van a venir en el examen

## Tweeter
23 diciembre 2022 $\rightarrow$ $\quad >400,000,000$ usuarios


4 enero 2023 $\rightarrow \quad 200+ \text{millones}$, $56\text{gb}$ sin duplicados, SIN contraseñas

### Acciones
1. $5.4\text M$ de los filtrados en noviembre fueron también expuestos en el ataque de agosto
2. $40\text M$ de datos de la segunda filtración (diciembre) eran independientes a ataques anteriores
3. Un conjunto de $200 \text M$ de datos no estaban relacionados a una explotación de los sistemas de Twitter
4. Los dos conjuntos de datos eran idénticos (diciembre y enero), el segundo solo elimina los duplicados
5. Ninguno de los conjuntos de datos tenía contraseñas o información que vulnerara las mismas

### Precedentes
1. $23/\text{Ago}/22 \rightarrow$ Ex-jefe de seguridad revela ineficiencias y negligencia en Twitter
2. $\text{Ago}/22 \rightarrow$ Ex-empleado de Twitter resulta ser agente secreto de Arabia Saudita
3. $2009 - 2022 \rightarrow$ Al menos 8 diferentes casos de información hackeada por falta de segurdad ($330\text M+$)

### Conclusiones
No hay contraseñas filtradas $\Rightarrow$ Bajo riesgo de perder la cuenta  
Identificar handles de usuarios anónimos  
Presentar información posiblmente relevante para quienes buscan apoderarse de las cuentas  
Personas con más seguidores se pueden volver objetos de phishing o doxeo


## Last Pass

$\text{December }22$. Básicamente los cabrones no dijeron nada. Tan solo dijeron que los habían hackeado como 4 meses después de que esto había pasado.

## Uber

Phishing
~~~
Los atacantes se hacen pasar por una entidad legítima con el objetivo de obtener información confidencial de los usuarios
~~~

Confidencialidad
~~~
Que la información sea accesible de forma única a las personas que se encuentren autorizadas para ello
~~~

Integridad
~~~
Supone que la información solo se podrá modificar mediante autorización de un usuario legítimo o autorizado
~~~

Disponibilidad
~~~
Se refiere a la capacidad de un sistema para estar accesible y operativo en todo momento
~~~

Man in the middle
~~~
Técnica de ciberataque en la que un atacante intercepta y manipula la comunicación entre dos dispositivos o sistemas, creando, por ejemplo, una página idéntica a la página de acceso en una compañía
~~~

### línea de tiempo del incidente

<dl>
<dt>Octubre 2016</dt>
<dd> Hackers ganan acceso al sistema de almacenamiento de datos de Uber al obtener las credenciales de acceso de un ingeniero de la empresa que estaban indebidamente publicadas en Github</dd>


<dl>
<dt>Noviembre 2016</dt>
<dd> Hackers extraen 57 millones de usuarios y conductores de Uber.<br>Uber decide ocultar el incidente</dd>

<dl>
<dt>Diciembre 2016</dt>
<dd> Uber paga 100,000 dólares para que destruyan datos y mantengan silencio</dd>

<dl>
<dt>Noviembre 2017</dt>
<dd> El incidente es revelado por Bloomberg <br>El CEO de Uber renuncia y varios funcionarios claves son despedidos<br>Uber enfrenta multas y demandas legales</dd>

<dl>
<dt>2018</dt>
<dd>Uber paga 148 millones de dólares por encubrir el incidente</dd>

<br>

Hubo también otro inicdente en 2022:
- Un hacker de 18 años entró en Slack y a todas las herramientas de comunicación interna. 
- Uber dijo que un contratista externo fue hackeado y que a partir de ahí ganaron acceso

Básicamente fue un ataque de Man in the middle (que es como phishing pero mucho más elaborado)

## PayPal

Funcionamiento de segurida de PayPal

1. Cifrado SSL
2. Navegadores aprovados
3. Sistema de bóveda única <br> Más fácil proteger una bóveda sola que varias
4. Verificación de dos pasos <br> Se da la opción de habilitar esta autentificación

### Posibles problemas

- Phishing $\rightarrow$ mails con páginas web "copycat"
- Estafas por internet $\rightarrow$ amplía la entrada de estafadores
- Cuentas congeladas $\rightarrow$ accidentalmente puede congelar cuentas

### Incidente

$6 - 8 \text{diciembre }2022$; 35 mil usuarios expuestos; ataque de terceros; fuerza bruta fue la versión oficial

### Posible Credential Stuffing
- Misma contraseña para mismo correo en diferentes aplicaciones
- Subset de un BFA 
- Datos sensibles filtrados:
   - Nombre
   - Dirección
   - Fecha de nacimiento
   - NSS
- ESET afirma que no se filtraron historial de transacciones ni tarjetas vinculadas
- Puede haber fraude o phishing con esa información


## Reddit

Reddit reveló que sufrio una violación de datos el $\text{5 Febrero}$ después de que un empleado cayera en **phishing**

Phishing
~~~
Un ataque informático en el que un estafador intenta engañar a una persona para que revele información confiencial, como contraseñas o números de tarjetas, haciéndose pasar por una entidad de confianza a través de mensajes engañosos
~~~

### Respuesta ante el ataque
Al caer en phishing, el empleado alertó a los encargados de lo que había sucedido. Dicen que su *equipo de seguridad respondió rápidamente, eliminando el acceso del infiltrado y comenzando una investigación interna*.

Actúo de muy buena forma con sus usuarios al alertar oportunamente de lo que había ocurrido, además de hacerlo con mensajes claros.