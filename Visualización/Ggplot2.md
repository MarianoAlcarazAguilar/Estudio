# `ggplot2`

- Paquete de R diseñado para crear gráficas de alta calidad
- Muy orientado a gráfcias de datos estadísticos
- Busca enfocarse en lo que se desea presentar, no en la forma (está culeras)
- Está basado en una *Gramática de gráficas*

Las gráficas se crean combinando elementos independientes,
- Compuestas de **datos** que deseamos visualizar 
- a través de un **mapeo** a los *atributos estéticos* de los marcadores y 
- seleccionando el elemento geométrico (**geom**) de la *capa* para desplegar la información

### Componentes

Capa $\quad \rightarrow \quad$ Colección de **geoms** y transformaciones estadísticas **stats**  
Escalas $\quad \rightarrow \quad$ Mapean valores en el espacio de datos a valores en el **espacio estético**
- Incluyen uso de color
- Forma
- Tamaño
- Leyendas que faciliten el mapeo inverso

Coordenadas $\quad \rightarrow \quad$ Sistema de coordenadas **cord** que describe cómo se hace el mapeo de un sistema a otro. Provee ejes y mallas que facilitan la lectura de la gráfica  
Facets $\quad \rightarrow \quad$ Indican cómo dividir y desplegar subconjuntos de datos  
Tema $\quad \rightarrow \quad$ Controla los aspectos finos del desplegado como tipo de fuente, color de fondo, entre otros.

<div align='right'><b>Ejemplo</b></div>

~~~r
# solo necesario la primera vez
library(ggplot2)

# economics -> dataset
# aes -> datos para los ejes
# geom_point() -> el tipo de gráfica que se hará
ggplot(data = economics, aes(x=date, y=unemploy)) +
   geom_point()
~~~

<div align="center">
   <img src="./images/.png">
</div>

<div align='right'><b>Ejemplo</b> <br>Muy detallado</div>

~~~r
library(ggplot2)

ggplot() +
   coord_cartesian() +
   scale_x_continuous() +
   scale_y_continuous() +
   # Agregamos una capa con todas las especificaciones
   layer(
      data = diamonds,
      mapping = aes(x = carat, y = price),
      stat = "identity",
      geom = "point",
      position = position_identity()
   )
~~~

<div align="center">
   <img src="./images/.png">
</div>

<div align='right'><b>Ejemplo</b> <br> Datos categóricos</div>

~~~r
library(ggplot2)

ggplot() +
   coord_cartesian() +
   # Aquí cambia el tipo de coordenadas
   scale_x_discrete() +
   scale_y_continuous() +
   layer(
      data = diamonds, 
      mapping = aes(x = cut, y = price),
      stat = "identity",
      geom = "point",
      position = position_identity()
   )
~~~

<div align="center">
   <img src="./images/.png">
</div>

<div align='right'><b>Ejemplo</b><br>Dispersando Datos</div>

~~~r
ggplot() +
   coord_cartesian() +
   scale_x_discrete() +
   scale_y_continuous() +
   layer(
      data = diamonds,
      mapping = aes(x = cut, y = price),
      stat = "identity",
      geom = "point",
      # Esto es lo nuevo
      position = position_jitter(width = 0.3, height = 0)
   )
~~~ 

<div align="center">
   <img src="./images/.png">
</div>

<div align='right'><b>Ejemplo</b><br>Añadir estadísticas</div>

~~~r
ggplot() +
   coord_cartesian() +
   scale_x_discrete() +
   scale_y_continuous() +
   layer(
      data = diamonds,
      mappping = aes(x = cut, y = price),
      # Especificamos un nuevo tipo de stat
      stat = "boxplot",
      # Nuevo tipo de geom
      geom = "boxplot",
      # nueva posición
      # para que no se empalmen las cajas
      postion = position_dodge()
   )
~~~

<div align="center">
   <img src="./images/.png">
</div>

<div align='right'><b>Ejemplo</b><br>Añadir varias capas</div>

~~~r
ggplot() +
   coord_cartesian() +
   scale_x_discrete() +
   scale_y_continuous() +
   layer(
      data = diamonds,
      mapping = aes(x = cut, y = price),
      stat = "identity",
      geom = "point",
      position = position_jitter(width = 0.2, height = 0)
   ) +
   # Se pone otra layer sobre la anterior
   layer(
      data = diamonds, 
      mapping = aes(x = cut, y = price),
      stat = "boxplot",
      geom = "boxplot",
      list(color = "red", fill = "red", alpha = 0.5),
      position = position_identity()
   )
~~~

<div align="center">
   <img src="./images/.png">
</div>

<div align='right'><b>Ejemplo</b><br>Color por categorías</div>

~~~r
ggplot() +
   coord_cartesian() +
   scale_x_continuous() +
   scale_y_continuous() +
   # Aquí esto es nuevo
   scale_color_hue() +
   layer(
      data = diamonds,
      # En este caso el 'color' de la derecha corresponde a una columna con ese nombre 
      mapping = aes(x = carat, y = price, color = color),
      stat = "identity",
      geom = "point",
      position = position_identity()
   )
~~~

<div align="center">
   <img src="./images/.png">
</div>

<div align='right'><b>Ejemplo</b><br>Añadir Facets</div>

~~~r
ggplot() +
   coord_cartesian() +
   scale_x_continuous() +
   scale_y_continuous() +
   scale_color_hue() +
   # Se crea una faceta para cada tipo de corte distinto
   facet_wrap(~cut)+
   layer(
      data = diamonds,
      mapping = aes(x = carat, y = price, color = color),
      stat = "identity",
      geom = "point",
      position = position_identity()
   )
~~~

<div align="center">
   <img src="./images/.png">
</div>

<div align='right'><b>Ejemplo</b><br>Gráfica de Barras</div>

~~~r
ggplot() +
   coord_cartesian() +
   scale_x_discrete() +
   scale_y_continuous() +
   layer(
      data = diamonds,
      mapping = aes(x = color),
      # Cuenta las observaciones
      stat = "count",
      # Dibuja una barra para cada cuenta
      geom = "bar",
      position = position_identity()
   )
~~~

<div align="center">
   <img src="./images/.png">
</div>

<div align='right'><b>Ejemplo</b><br>Malla Gráficas</div>

~~~r
ggplot() +
   coord_cartesian() +
   scale_x_discrete() +
   scale_y_continuous() +
   # Esto es nuevo
   # Renglones: claridad
   # Columnas: corte
   facet_grid(clarity~cut)+
   layer(
      data = diamonds, 
      mapping = aes(x = color),
      stat = "count",
      geom = "bar",
      position = position_identity()
   )
~~~

<div align="center">
   <img src="./images/.png">
</div>