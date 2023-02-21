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

