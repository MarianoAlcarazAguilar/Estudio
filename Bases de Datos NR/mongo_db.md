# Mongo DB

Mongo DB vió la luz por primera vez en 2009. Se diseñó para ser escalable desde un inicio; el desempeño y el fácil acceso a los datos fueron parte desde un inicio.  
<br>
Es una **base de datos documental**, lo cual nos permite guardar objetos anidados, tanto como se desee. No pide ningún tipo de esquema, por lo que los documentos pueden tener campos que ningún otro documento tenga.  
<br>
Aunque la flexibilidad nos llevaría a no tomarlo en serio, realmente hay aplicaciones enormes que lo usan hoy en día.


## Pasos para crear contenedor de docker con mongo
~~~sh
# Creamos un directorio para poder guardar todo ahí
mkdir data
# Creamos el docker en sí
docker run -p 27017:27017 \
      # Esto crea un volumen
       - v ~/data:/data/db \
      # Esto también crea un volumen
       - v ~/mongodb-sample-dataset:/mongodb-sample-dataset \
      # Esto nombra el docker
       --name mongo \
      # No tengo idea de qué haga esto
       -d mongo
~~~

Si queremos parar un docker hacemos los siguiente 

~~~sh
# Esto para el contenedor
docker stop mongo
# Esto elimina el contenedor
docker rm mongo
~~~

Si queremos correr el contenedor desde la terminal hacemos lo siguiente
~~~sh
# Esto nos mete directo a la terminal de mongo
docker exec -it mongo mongosh
# También podemos primero entrar a la máquina de bash
docker exec -it mongo bash
# Ya estando adentro podemos llamar 
mongosh
# Y nos lleva al mismo lugar
~~~

## Usando MongoDB
Usamos `mongosh` para tener una línea de comandos.  
<br>
Creamos una base de datos que se llame books.  
Técnicamente no es una base de datos hasta que no agreguemos documentos.
 ~~~js
 use book
 ~~~

Vamos ahora a insertar un documento:

~~~js
 var documento = {
   name: "New York",
   population: 222222,
   last_census: ISODate("2016-07-01"),
   famous_for: ["The MOMA", "Food", "Statue of Liberty"],
   mayor: {
      name: "Bill de Blasio",
      party: "D"
   }
}

// Ahora sí lo insertamos
db.towns.insertOne(documento)
~~~

Recordemos la estructura de las colecciones en mongo
<br>  
<img src='./images/estructura_documento_mongo.png' alt='estructura_documento_mongo'>
<br>  
Analicemos, pues, lo que está haciendo la última línea del código:

1. **db** es el objeto con el que `mongosh` se refiere a la base de datos, que en este caso es *book*. Se tiene que **towns** es una colección adentro de la base de datos (como se puede ver en la imagen de arriba)
2. La variable que se definió como documento es un *pseudo* json que contiene los datos que nos importan. Es pseudo porque tiene objetos que no son texto plano, como lo es la fecha, con la cual se puede trabajar de manera especial a si fuera solamente texto.

