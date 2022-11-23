# Links `<a>`
Los usuarios pueden hacer click sobre cualquier parte entre los tags y los redirecciona a donde sea que **href** diga.  

Si damos click en 
<a href="http://www.google.com">google</a> vamos al buscador, para lo cual se usó el siguiente código: 
~~~html
<a href="http://www.google.com">google</a>
~~~

| Contenidos | Notas | Ejemplo |
| ---------- | ----- | ------- |
| Links to other sites | href="dirección absoluta" | <a href="http://www.google.com">google</a> |
| Links to other pages in same site | href="dirección relativa " | <a href="./links.html">links html file</a> |
| Email links | href="mailto:email_adress.com" | <a href="mailto:marianoaaguilar@hotmail.com">mail mariano</a> |
| Links in new windows | target="_blank" | <a href="http://www.google.com" target="_blank">google</a> | 
| Link to a specific part of the same page | href="#id_value" | <a href="#prueba"> link to my code</a> |
| Link to a specific part of another page | href="direccion_absoluta/relativa#id_vlaue" | <a href="links.html#header">header otra página</a> |

## Links to other sites
~~~html
<a href="http://www.google.com">google</a>
~~~

## Links to other pages in same site
~~~html
<a href="./links.html">links html file</a>
~~~

## Email Links
~~~html
<a href="mailto:marianoaaguilar@hotmail.com">mail mariano</a>
~~~

## Links in new windows
~~~html
<a href="http://www.google.com" target="_blank">google</a>
~~~

<h2 id="prueba"> Links to a specific part of the same page</h2>
Es importante mencionar que es necesario nombrar el tag con un id único para poder hacer referencia a él después.

~~~html
<a href="#prueba"> link to my code</a>
~~~

## Link to a specific part of another page 
~~~html
<a href="links.html#header">header otra página</a>
~~~