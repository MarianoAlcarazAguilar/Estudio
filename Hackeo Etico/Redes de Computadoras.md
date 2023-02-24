# Redes de Computadoras

Son esenciales en computación, por medio de ellas se transmite la información. Debemos poder garantizar la correcta transmisión.

### Modelo de Redes

Falta entender esta madre

### Medio físico de transmisión

- Cable de combre
- Fibra ótpica
- Ondas de radio
- Microondas

### Capas

**Física**

- Transmisión de bits sobre un medio de comunicación
- Ambos lados deben saber qué representa un 1 y un 0
- Si la transmisión puede ser simultánea o debe haber turnos
- Cuándo termina la transmisión de uno de los lados

**Enlaces de datos**

- Transforma la transmisión sobre el medio físico en un canal libre de errores
- Transmite unidades de información llamadas tramas, con miles de bits de información
- Cuando un receptor recibe una trama, contesta al trasmisor con un recibo
- Regula la velocidad de transmisión entre los participantes de la conexión
- También administra el acceso al medio de transmisión cuando hay varios receptotres/transmisores

**Red**
- Determina la ruta de unidades de información llamadas paquetes del origen al destino final
- Administra la congestión en los nodos de transmisión
- Tiene la habilidad de manejar la calidad del servicio para cada tipo de paquete
- Convierte distintos sistemas de direccionamiento para poder conectar redes heterogéneas

**Transporte**
- Fragmenta la información de la capa superior para que quepa en los paquetes de capa 3
- Normalmente asegura conexiones libres de error, punto a punto y con paquetes entregados en orden
- Es la primera capa punto a punto
- Opera con métodos orientados a conexión (TCP) o con mensajes asíncronos (UDP)

**Aplicación**  
Contiene protocolos utilizados por los usuarios:
- Correo
- Web
- Transferencia de archivos

Asegura la experiencia del usuario:
- Latencia de conexión
- Degradación amable del servicio
- Mensajes de estatus al usuario