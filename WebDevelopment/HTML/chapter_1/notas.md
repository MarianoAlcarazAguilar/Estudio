# Structure HTML
La estructura de HTML describe la página web.
|Contenidos| Notas |
|------------|----|
|Elementos|\<open>\</close>|
|Atributos|name="value"|
|Estructura Básica|\<html>\<head>\<body>|


## Elementos
Son aquellas cosas que están adentro de `<>`. Usualmente están conformados por dos tags: uno que abre y uno que cierra.
~~~html
<p> Este es un párrfo </p>
~~~
Estos son usados para describir la esturctura de la página web.

## Atributos
Nos dicen más sobre los elementos; aparecen en el tag de apertura.  
Están hechos por dos partes:
- nombre (name)
- valor (value)
~~~html
<p lang="en-us">Paragraph in English</p>
~~~

## Estructura Básica
`<html>` Es donde se contien todo.  
`<head>` Contien información sobre la página. Nunca se ve desplegada.  
`<body>` Es o que el usuario ve en la página del buscador.
~~~html
<html>
    <head>
        Esto no lo ve el usuario.
    </head>
    <body>
        Esto sí lo ve el usuario.
    </body>
</html>
~~~
