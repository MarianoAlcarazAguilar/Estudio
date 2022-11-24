# Incializar una máquina en la nube

Para esto usaremos [Amazon Web Services](https://aws.amazon.com).  


### Paso 1
Crea o ingresa a tu cuenta de AWS.

<div align='center'>
<img src='./images/aws_1.jpeg' alt='imagen de aws inicio' width='500px'>
</div>

<hr>

### Paso 2
En la barra de búsqueda introduce el nombre **EC2** y selecciónalo.

<div align='center'>
<img src='./images/aws_2.jpeg' alt='imagen de busqueda aws' width='600px'>
</div>
<hr>

### Paso 3
Ahora crearemos la nueva instancia (esta es la computadora).  
Busca la sección llamada ***Launch Instance***

<div align='center'>
<img src='./images/launch_instance.jpeg' alt='sección de creación de instancia' width='300px'>
</div>
<hr>

### Paso 4

Ahora, es momento de especificar todo lo que deseemos.

1. Nombre

<div align='center'>
<img src='./images/nombre_1.jpeg' alt='elegir nombre' width='500px'>
</div>

2. Selecciona el sistema operativo. Yo siempre uso ubuntu.
<div align='center'>
<img src='./images/sistema_operativo_2.jpeg' alt='elegir os' width='400px'>
</div>

3. Elige el tipo de instancia. Yo siempre uso la que es elegible para **free tier**.
<div align='center'>
<img src='./images/tipo_instancia_3.jpeg' alt='elegir tipo de instancia' width='450px'>
</div>

4. Elige la **SSH** key que vas a usar. Yo ya tengo una que se llama test.pem, pero para crear el tuyo ver el siguiente link <a href='./create_key_pair.md'>create_key_pair</a>

<div align='center'>
<img src='./images/key_pair_4.jpeg' alt='elegir llave' width='400px'>
</div>

5. Especifica los ajustes de conexión. Yo ya tengo un grupo de seguridad hecho, pero básicamente solo elegí que se pudiera acceder desde cualquier dirección IP porque sino sería un pedo estar modificando eso cada vez.
 <div align='center'>
<img src='./images/network_settings_5.jpeg' alt='elegir tipo de instancia' width='450px'>
</div>

6. Elige el almacenamiento.

<div align='center'>
<img src='./images/storage_6.jpeg' alt='elegir tipo de instancia' width='400px'>
</div>

7. Activa la instancia

<div align='center'>
<img src='./images/activar_instancia_7.jpeg' alt='elegir tipo de instancia' width='300px'>
</div>