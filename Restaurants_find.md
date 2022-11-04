# Ejercicios find()

**1. Escribe una función find() para mostrar todos los documentos de la colección de restaurantes.**
```
db.restaurants.find()
```
**2. Escribe una función find() para mostrar los campos restaurant_id, nombre, municipio y cocina para todos los documentos en el restaurante de la colección.**
```
db.restaurants.find({},{"restaurant_id":1,"name":1,"borough":1,"cuisine":1,"_id":1})
```
**3. Escribe una función find() para mostrar los campos restaurant_id, nombre, municipio y cocina, pero excluya el campo \_id para todos los documentos de la colección restaurant.**
```
db.restaurants.find({},{"restaurant_id":1,"name":1,"borough":1,"address.zipcode":1,"_id":0})
```
**4. Escribe una función find() para mostrar todos los restaurantes que se encuentran en el distrito del Bronx.**
```
db.restaurants.find({"borough":"Bronx"})
```
**5. Escribe una función find() para mostrar los primeros 5 restaurantes que se encuentran en el condado del Bronx.**
```
db.restaurants.find({"borough":"Bronx"}).limit(5).count()
```
**6.Escribe una función find() para mostrar los siguientes 5 restaurantes después de omitir los primeros 5 que se encuentran en el condado del Bronx.**
```
db.restaurants.find({"borough":"Bronx"}).skip(5).limit(5)
```
**7. Escribe una función find() para encontrar los restaurantes que obtuvieron una puntuación de más de 90.**
```
db.restaurants.find({"grades.score":{$gt:90}})
```
**8. Escribe una función find() para encontrar los restaurantes que obtuvieron una puntuación, más de 80 pero menos de 100.**
```
db.restaurants.find({"grades":{$elemMatch:{"score": {$gt:80,$lt:100}}}})
```
**9. Escribe una función find() para encontrar los restaurantes que se ubican en un valor de latitud menor que -95.754168.**
```
db.restaurants.find({"address.coord.0": {$lt: -95.754168}})
```
**10. Escribe una función find() para encontrar los restaurantes que no preparan ningún tipo de cocina de ‘estadounidense’ y su puntuación de calificación es superior a 70 y latitud inferior a -65.754168.** 
```
db.restaurants.distinct("cuisine")
db.restaurants.find({"cuisine": {$ne: "American "},"address.coord.0": {$lt: -65.754168}, "grades.score":{$gt:70}})
```
**11. Escribe una función find() para encontrar los restaurantes que no preparan ninguna cocina del continente americano y lograron una puntuación superior a 70 y se ubicaron en la longitud inferior a -65.754168.**
```
db.restaurants.distinct("cuisine")
db.restaurants.find({"cuisine": {$nin: ["American ", "Brazilian","Caribbean","Latin (Cuban, Dominican, Puerto Rican, South & Central American)", "Mexican", "Tex-Mex"]},"address.coord.0": {$lt: -65.754168}, "grades.score":{$gt:70}})
```
**12.Escribe una función find() para encontrar los restaurantes que no preparan ninguna cocina del continente americano y obtuvieron una calificación de ‘A’ que no pertenece al distrito de Brooklyn. El documento debe mostrarse según la cocina en orden descendente.**
```
db.restaurants.find({"cuisine": {$nin: ["American ", "Brazilian","Caribbean","Latin (Cuban, Dominican, Puerto Rican, South & Central American)", "Mexican", "Tex-Mex"]},"borough": {$ne: "Brooklyn"}, "grades.grade":"A"}).sort({"cuisine":-1})
```
**13. Escribe una función find() para encontrar el ID del restaurante, el nombre, el municipio y la cocina de aquellos restaurantes que contienen ‘Wil’ como las primeras tres letras de su nombre.**
```
db.restaurants.find({"name":/^Wil/},{"restaurant_id":1,"name":1,"borough":1,"cuisine":1,"_id":0})
```
**14. Escribe una función find() para encontrar el ID del restaurante, el nombre, el municipio y la cocina de aquellos restaurantes que contienen “ces” como las últimas tres letras de su nombre.**
```
db.restaurants.find({"name":/ces$/},{"restaurant_id":1,"name":1,"borough":1,"cuisine":1,"_id":0})
```
**15. Escribe una función find() para encontrar el ID del restaurante, el nombre, el municipio y la cocina de aquellos restaurantes que contienen ‘Reg’ como tres letras en algún lugar de su nombre.**
```
db.restaurants.find({"name":/Reg/},{"restaurant_id":1,"name":1,"borough":1,"cuisine":1,"_id":0})
```
**16. Escribe una función find() para encontrar los restaurantes que pertenecen al municipio del Bronx y que prepararon platos estadounidenses o chinos.**
```
db.restaurants.find({"borough": "Bronx","cuisine": {$in: ["American ","Chinese"]}})
```
**17. Escribe una función find() para encontrar la identificación del restaurante, el nombre, el municipio y la cocina de los restaurantes que pertenecen al municipio de Staten Island o Queens o Bronx o Brooklyn.**
```
db.restaurants.find({"borough":{$in: ["Staten Island","Queens","Bronx","Brooklyn"]}},{"restaurant_id":1,"name":1,"borough":1,"cuisine":1,"_id":0})
```
**18. Escribe una función find() para encontrar el ID del restaurante, el nombre, el municipio y la cocina de aquellos restaurantes que no pertenecen al municipio de Staten Island o Queens o Bronx o Brooklyn.**
```
db.restaurants.find({"borough":{$nin: ["Staten Island","Queens","Bronx","Brooklyn"]}},{"restaurant_id":1,"name":1,"borough":1,"cuisine":1,"_id":0})
```
**Otra forma:**
```
db.restaurants.distinct("borough")
db.restaurants.find({"borough":"Manhattan"},{"restaurant_id":1,"name":1,"borough":1,"cuisine":1,"_id":0})
```
**19. Escribe una función find() para encontrar el ID del restaurante, el nombre, el municipio y la cocina de aquellos restaurantes que obtuvieron una puntuación que no sea superior a 10.**
```
db.restaurants.find({"grades.score": {$lt: 10}},{"restaurant_id":1,"name":1,"borough":1,"cuisine":1,"_id":0})
```
**20. Escribe una función find() para encontrar el ID del restaurante, el nombre, el municipio y la cocina de aquellos restaurantes que prepararon platos excepto ‘Americano’ y ‘Chinese’ o el nombre del restaurante comienza con la letra ‘Wil’.**
```
db.restaurants.find({$or:[{"name":/^Wil/},{"cuisine": {$in: ["American ","Chinese"]}}]},{"restaurant_id":1,"name":1,"borough":1,"cuisine":1,"_id":0})
```
**21.Escribe una función find() para encontrar el ID del restaurante, el nombre y las calificaciones de los restaurantes que obtuvieron una calificación de “A” y obtuvieron una puntuación de 11 en un ISODate “2014-08-11T00: 00: 00Z” entre muchas de las fechas de la encuesta.**
```
db.restaurants.find({"grades.date":ISODate(“2014-08-11T00: 00: 00Z”),"grades.grade": "A", "grades.score": 11})
```
**22. Escribe una función find() para encontrar el ID del restaurante, el nombre y las calificaciones de aquellos restaurantes donde el segundo elemento de la matriz de calificaciones contiene una calificación de “A” y una puntuación de 9 en un ISODate “2014-08-11T00: 00: 00Z”.**
```
db.restaurants.find({"grades.date":ISODate(“2014-08-11T00: 00: 00Z”),"grades.grade": "A", "grades.score": 9})
```
**23.Escribe una función find() para encontrar el ID del restaurante, el nombre, la dirección y la ubicación geográfica para aquellos restaurantes donde el segundo elemento de la matriz de coordenadas contiene un valor que sea más de 42 y hasta 52.**
```
db.restaurants.find({"address":{$elemMatch:{"coord.1": {$gt:42,$lt:52}}}},{"restaurant_id":1,"name":1,"address":1,"_id":0})
```
**24. Escribe una función find() para organizar el nombre de los restaurantes en orden ascendente junto con todas las columnas.**
```
db.restaurants.find().sort({"name":1})
```
**25. Escribe una función find() para organizar el nombre de los restaurantes en orden descendente junto con todas las columnas.**
```
db.restaurants.find().sort({"name":-1})
```
**26. Escribe una función find() para organizar el nombre de la cocina en orden ascendente y para ese mismo distrito de cocina debe estar en orden descendente.**
```

```
**27. Escribe una función find() para saber si todas las direcciones contienen la calle o no.**
```
db.restaurants.find().count()
db.restaurants.find({"address.street":{$exists:true}},{"address":1}).count()
```
**28. Escribe una función find() que seleccionará todos los documentos de la colección de restaurantes donde el valor del campo coord es Double.**
```
db.restaurants.find({"address.coord": {$type: "double"}})
```
**29. Escribe una función find() que seleccionará el ID del restaurante, el nombre y las calificaciones para esos restaurantes que devuelve 0 como resto después de dividir la puntuación por 7.**
```
```
**30.Escribe una función find() para encontrar el nombre del restaurante, el municipio, la longitud y la latitud y la cocina de aquellos restaurantes que contienen “mon” como tres letras en algún lugar de su nombre.**
```
db.restaurants.find({"name":/mon/},{"name":1,"borough":1,"address.coord":1,"cuisine":1,"_id":0})
```
**31. Escribe una función find() para encontrar el nombre del restaurante, el distrito, la longitud y la latitud y la cocina de aquellos restaurantes que contienen ‘Mad’ como las primeras tres letras de su nombre.**
```
db.restaurants.find({"name":/^Mad/},{"name":1,"borough":1,"address.coord":1,"cuisine":1,"_id":0})
```
