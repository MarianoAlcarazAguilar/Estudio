# Extra Markup

| Contenidos |
|------------|
| Doctypes |
| Comments in HTML |
| ID attribute |
| Class attribute |
| Block Elements |
| Inline Elements |
| Grouping in a Block |
| Grouping Inline |
| Iframes |
| Meta Element |


## Doctypes
Se usa para deirle al buscador qué versión de HTML se está usando.  
Nosotros estaremos usando la siguiente forma por usar HTML 5.

~~~html
<!DOCTYPE html>
~~~

## Comments in HTML
Si quieres agregar un comentario al código y no deseas que sea visible para el usuario, puedes agregar texto entre los siguienes caracteres:
~~~html
<!-- Esto es un comentario en HTML -->
~~~

## ID Attribute
Todos los elementos pueden tener un atributo de **id**. Se usa para identificar de manera única ese elemento de los otros en la página.  
No se pueden tener dos elementos con el mismo id en la misma página.

~~~html
<p id="pullquot">Aquí podrías poner una cita de un libro y luego ponerle estilo usando CSS</p>
~~~

## Class Attribute
Todos los elementos de HTML pueden tenern el atributo **class**. Algunas veces, en vez de querer identificar de manera única un elemento, lo quieres hacer en distintos gurpos

~~~html
<p class="importante">Este párrafo es importante</p>
<p class="general">Este párrafo solo contiene información general</p>
~~~

## Block Elements
Son aquellos que siempre aparecen en una nueva línea en el buscador.  
Ejemplos de ellos son los siguientes elementos:
~~~html
<h1>Headers</h1>
<p>Párrafos</p>
<ul>
    <li>Listas</li>
    <li> Y sus elementos</li>
</ul>
~~~

## Inline Elements
Algunos elementos siempre aparecen en la misma línea que sus vecinos.  
Ejemplos de ellos son:
~~~html
<a> <b> <em> <img>
~~~

## Grouping Text & Elements in a Block
El elemento `div` te permite agrupar elementos juntos en un block-level box.  
  
Por ejemplo, puedes crear un elemento `div` para contener todos los elementos del header. Los elementos del div empiezan en una nueva línea, pero además de esto, no hay ninguna diferencia para el usuario final.
  
La ventaja de esto es que con CSS puedes modificar el estilo de cada bloque por separado al usar los atributros de **id** y **class**.

## Grouping Text & Elements Inline
Puedes usar `span` como el equivalente de *div* en una línea.  
Se usa para:  
1. Contener una sección de texto cuando no hay manera de diferenciarlo de otro texto.
2. Contener una cantidad de inline elementos.
3. Para controlar la apariencia usando CSS.

## Iframes
Es como una pequeña ventana en la página, en la que puedes ver otra página.  
Se puede usar por ejemplo para Google Maps, pero puede ser en realidad cualquier página web.
~~~html
<iframe width="450" height="350" src="http://maps.google.co.uk/maps;output=embded" frameborder="0" scrolling="no"></iframe>
~~~

## Information about your Page
Puedes usar el elemento `meta` adentro del elemento *head* para poner más información de la página.  
Los atributos más comunes que incluyen son:
- name
- content
~~~html
<!DOCTYPE html>
<html>
    <head>
        <title>Information about your pages</title>
        <meta name="description" content="an essay on installation art">
        <meta name="keywords" content="installation, art, opinion">
    </head>
</html>
~~~



