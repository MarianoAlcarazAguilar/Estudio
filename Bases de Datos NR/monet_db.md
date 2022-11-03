# MonetDB

MonetDb es una base de datos columnar.  
<br>
- Buenas para leer; malas para escribir
- Son el destino final de los cubos de datos; son como vistas
- Cuando las bases de datos relacionales no son suficientes (ni con índices) las vistas las llevamos a bases de datos columnares.

## Construcción de BD columnaes

Por dentro se crean de la siguiente forma:

<img src='./images/bd_columnares_1.png' alt='imagen de creacion de bases de datos columnares'>

Posterior a la creación de estos archivos viene la compresión.

En las bases de datos columnares las operaciones **INSERT**, **DELETE** o **UPDATE** o no son soportadas o son parcialmente soportadas, o tardan muchísimo más que una base de datos relacional.

En lugar de meter tabla por tabla en una BD columnar, mejor insertamos una BIG TABLE.

Lo más óptimo para crear una big table es básicamente hacer joins de todas las tablas que queramos meter y luego esa la pasamos a columnar.

~~~sql
select *
  from actor a join film_actor fa using (actor_id)
       join film f using (film_id)
       join film_category fc using (film_id)
       join category c using (category_id)
       join inventory i using (film_id)
       join rental r using (inventory_id)
       join payment p using (rental_id);

~~~ 

## Instalar MonetDB

Con lo siguiente bajamos monetdb y lo tenemos corriendo en un contenedor de nombre monetdb

~~~sh
docker volumne create monet-data
doker stop monetdb
docker rm monetdb
docker run \
       -v monet-data:/var/monetdb5/dbfarm \
       -p 50001:50000 \
       --name monetdb \
       -d monetdb/monetdb:latest
~~~

Ahroa para correr comandos sobre la base de datos
~~~sh
docker exec -it monetdb /bin/bash
# Y adentro podemos crear una base de datos que se llame ITAM
monetdb create -p monetdb ITAM
~~~

Ahora, para entrar en el shell de monetdb, corremos el siguiente comando
~~~sh
docker exec -it monetdb mclient ITAM
~~~


    