# Gráficas 

## Gráficas Básicas

### Representación de Datos Tabulares

La organización (distribución) espacial es la de mayor peso de las opciones de diseño porque domina el *mapa mental* del dataset.  
Una primera guía está en función del número de **llaves** y **valores** que tiene el dataset:

| Número de Llaves | Número de valores | Gráfica |
| --- | --- | --- |
| 0 | 2 | Scatter plot | 
| 1 | 1 | Barras |
| 2 | 1 | Heatmap |
| n | n | Matriz de scatter plots | 

### Scatterplot

Gráfica de dispersión.

- Basada en el sistema cartesiano, es quizá la más usada en estadística
- Dos atributos cuantitativos, uno codificado espacialmente en el eje vertical y el otro en el horizontal
- El **marcador** necesariamente es un **punto**
- Atributos adicionales pueden codificarse con otros canales visuales, como color y tamaño
   - Si es con tamaño, se llama **bubble plot**
- Útiles para observar:
   - Tendencias
   - Agrupamientos
   - Correlaciones
   - Valores atípicos o extremos

Si mostrar o analizar la correlación es importante, se suele agregar una línea de regresión lineal

<div align='right'><b>Ejemplo</b></div>

~~~r
migraf <- ggplot(data = mtcars, aes(x = wt, y = mpg))
migraf + 
   geom_point(size = 2) +
   geom_smooth(method = "lm", se = False)
~~~

### Bubbple Plot  
- La posición también se fija en ejes cartesianos y permite graficar dos atributos cuantitativos (o uno cuantitativo y uno ordenado) pero se puede asignar uno o dos más con el tamaño y el color
- Muy útil para comparar relaciones, detectar patrones, relaciones, proporciones y evolución en el tiempo.

<div align='right'><b>Ejemplo</b></div>

~~~r
ggplot(mtcars, aes(wt, mpg, size=disp)) + 
   geom_point(alpha = 0.5) + 
   scale_size(range = c(1, 10))
~~~

### Gráfica de puntos y líneas

- Se utilizan para desplegar valores cuantitativos sobre un intervalo continuo o periodo de tiempo (gráfica de líneas), o sobre variables categóricas (gráficas de puntos), quizás en vez de gráfica de barras
   - Atributo categórico $\Rightarrow$ Usar gráfica de barras
   - Atributo ordenado $\Rightarrow$ Usar gráfica de líneas
      - Una línea sugiere **fuertemente** una tendencia que no existe en atributos categóricos
- Muy útiles para identificar tendencias y analizar cambios en el tiempo, comparar y detectar patrones

<div align='right'><b>Ejemplo</b></div>

~~~r
library(dplyr)
library(hrbrthemes)

ggplot(data, aes(x = date, y = value)) +
   # Esto es nuevo
   geom_line(color = "grey") +
   geom_point(shape = 21, color = "black", fill = "blue", size = 6) +
   # Esto es un nuevo tema. No es necesario
   theme_ipsum() +
   # Agregamos título
   ggtitile("My graph")
~~~

### Gráfica de Barras
- Típicamente la llave es una categoría y el atributo una magnitud
- Cada barra en una región separada del espacio
- Barras alineadas para poder comparar fácilmente
- Muy útiles para mostrar comparaciones entre items
   - Pocos items $\Rightarrow$ columnas verticales
   - Muchos items $\Rightarrow$ columnas horizontales

~~~r
ggplot(mpg, aes(x = class)) +
   # Esto es nuevo
   geom_bar(fill = "cyan")
~~~

Si queremos que la gráfica sea de barras horizontales

~~~r
ggplot(mpg, aes(x = class)) +
   geom_bar(fill = "cyan") +
   # Esto es nuevo 
   coord_flip()
~~~

### Barras Apiladas
- Dos atributos categóricos y uno cuantitativo
   - Se requiere de una leyenda
- El marcador es un *glifo*, un objeto compuesto por más de un marcador
- La longitud de la barra condifica un valor, pero está compuesto por los subcomponentes de la barra
- Muy útiles para mostrar diferencias relativas y absolutas
   - Solo diferencias absolutas, barras apiladas a 100%


Glifo
~~~
Un objeto compuesto por más de un marcador
~~~

~~~r
ggplot(mpg, aes(x = class, fill = drv)) +
   geom_bar()
~~~

Otra opción, ordenando además las barras
~~~r
library(forcats)
ggplot(mpg, aes(x = fct_infreq(class))) +
   geom_bar(aes(fill = drv)) +
   # Esto cambia la paleta de colores
   scale_fill_brewer(palette = "Pastel1")
~~~

### Streamgraph

También se le llama ThemeRiver

- Es una variación de áreas apiladas.
   - Los valores no son fijos sino que se desplazan de una base central
- Enfatizan la idea de continuidad horizontal
   - Despliegan bien los cambios en el tiempo de distintas categorías con formas órganicas, por lo que son agradables a la vista
- Tamaño de cada flujo proporcional a valores de cada categoría
- Muy buenas para datasets con muchos datos, para descubrir tendencias y cambio de patrones
   - Por ejemplo, se observa con facilidad si hay estacionalidad en los datos
- Tienen problemas de legibilidad sobre todo para categorías proporcionalmente más pequeñas
- Para quien no a pasar demasiado tiempo descirfrándolas

Lo que se necesita para que jale esto es lo siguiente:
- Una llave categórica
- Una llave ordenada
- Un atributo cuantitativo

<div align='right'><b>Ejemplo</b></div>

~~~r
ggplot(blockbusters, aes(year, box_office, fill = genre)) +
   geom_stream()
~~~

### Gráficas de pendientes (Slope Charts)

Son excelentes para comparar la evolución de un atributo (de un ítem) en dos instancias de tiempo.  
Se espera que el dataset cuente con,

- Dos atributos cuantitativos (los valores en $t1$ y $t2$)
- Un atributo cualitativo (que identifica al item)
- Se genera un **dato derivado**: el cambio en la magnitud (la pendiente)

<div align='right'><b>Ejemplo</b></div>

~~~r
library(CGPfunctions)

newggslopegraph(dataframe = df, Times = Year, Measurement = GDP, Grouping = Country)
~~~

### Mapas de Calor

- En general, las filas muestran una categoría, las columnas otra (dos llaves) y el color de la celda es proporcional a la magnitud de un atributo cuantitativo, aunque también pueden representar un dato categórico
- Muy útiles para examinar datos multivariados, mostrar varianzas entre múltiples variables, correlaciones, revelar patrones y similitud, identificar agrupaciones y valores atípicos
- Muestran una vista general de la informacion pues se pierde precisión, pero son valiosos cuando se tiene una gran densidad de información

***Nota***: para desplegar un mapa de calor en R, los datos deben estar en *formato long* (llave, valor)
   - Muchas menos columnas (2), la llave (primera columna) se repita muchas veces

~~~r
mtdf$car <- rep(row.names(mtcars), 11)

# Tenemos que rescalar (0 a 1) porque los valores de un atributo son mucho mayores que los demás
library(plyr)
library(scales)

mtdf <- ddply(mtdf, .(key), transform, rescale = rescale(value))

# Creamos el mapa
ggplot(mtdf, aes(key, car)) +
   # Esto es nuevo
   geom_tile(aes(fill = rescale), colour = "white") + 
   scale_fill_gradient(low = "white", high = "steelblue")
~~~

- Podemos utilizar los mapas de calor para mostrar correlaciones. A la gráfica resultante se le llama **heatmap correlation matrix**

Esta gráfica puede reordenarse para enfatizar las variables que están altamente correlacionadas

~~~r
library(reshape2)

cormat = round(cor(mtcars), 2)
mtcormat = melt(cormat)
ggplot(mtcormat, aes(Var1, Var2, fill = value)) + 
   geom_tile() +
   scale_fill_gradient(low = "white", high = "stellblue", limit = c(-1,1))

# Usamos hcclust para agrupamiento jerárquico
# Usando corr como distancia
dd = as.dist((1-cormat)/2)
# Esto es nuevo
hc = hclust(dd)
cm2 = cormat[hc$order, hc$order]
mtcm2 = melt(cm2)
ggplot(mtcm2, aes(Var1, Var2, fill = value)) + 
   geom_tile() +
   scale_fill_gradient(low = "white", high = "steelblue", limit = c(-1,1))
~~~

## Gráficas Para Sumarización de Datos

En muchas ocasiones, sobre todo para análisis estadístico, nos interesa tener una idea de la distribución de los datos, más que de su correlación, tendencia o ranking

Para ello, utilizamos gráficas que procesan los datos y nos entregan una síntesis de ellos.

- Histogramas
- Gráficas de densidad
- Gráficas de caja
- Gráficas de violín

### Histograma
 - Un gráfico sumamente popular para sumarizar items
 - A partir de los datos originales, se generan datos derivados:
   - La llave (ordenada) son las casillas (bins)
   - Los valores son las cuentas que se muestran en el eje $y$
   - Es de esperar que la llave pueda dividirse en intervalos continuos, de lo contrario, es más lógico usar una gráfica de barras
- El tamaño de las casillas es crucial
   - Podemos modificar el *ancho* de las columnas o el número de columnas (bins), lo que no se puede con `geom_bar()`
   - La forma de la distrubución cambia dramáticamente dependiendo del nivel de agregación
- Permite mostrar dónde se concentran los valores, máximos y mínimos, valores inusuales, la distribucón de los ítems y encontrar patrones.

~~~r
mg1 <- ggplot(iris, aes(Sepal.Width)) +
      # Esto es nuevo
      geom_histogram(binwidth = 0.1) + 
      ggtitle("Binwidth=0.1")

mg2 <- ggplot(iris, aes(Sepal.Width)) +
      # Esto es nuevo
      geom_histogram(binwidth = 0.3) + 
      ggtitle("Binwidth=0.3")

# Esta librería es para poder ponerlas una junto a las otras
library(patchwork)
mg1 + mg2
~~~

**Notas**
- Variable categórica $\Rightarrow$ Utilizar `geom_bar()`, o bien, `geom_histogram()`pero especificando `stat = "count"`
- En esos casos, claramente no se puede modificar `binwidth` o número de bins

~~~r
ggplot(mpg, aes(manufacturer)) +
   geom_histogram(stat = "count", aes(fill = class))
~~~

### Gráfica de Densidad
- Permite visualizar la distribución de los datos sobre un intervalo continuo o sobre un periodo de tiempo
- Se diferencia del histograma porque utiliza promedios ponderados para "suavizar" la cura (kernel smoothing)
- Son más precisos para determinar la forma de la distribución de los datos porque no dependen del número de bins

~~~r
ggplot(mpg, aes(cty, group = cyl, fill = factor(cyl))) +
   # Esto es nuevo
   geom_density(alpha = 0.8, adjust = 1.5)
~~~

### Gráfica de caja
- Muestra una síntesis estadística de las variables cuantitativas
   - Mediana $\rightarrow$ línea central
   - Cuartiles menor $25\%$ y mayor $75\%$ $\rightarrow$ límites de la caja
   - Barras o bigotes superior e inferior $\rightarrow$ puntos máximo y mínimo a $1.5$ x el largo de la caja
   - Valores fuera de esos puntos $\rightarrow$ valores atípicos, outliers
- Más compacto que un histograma o una gráfica de densidad

~~~r
ggplot(mpg, aes(class, cty)) +
   # esto es nuevo
   geom_boxplot(varwidth = True, fill = "pink") + 
   labs(
      title = "BoxPlot",
      subtitle = "Consumo en ciudad por tipo de vehículo",
      caption = "Fuente: mpg",
      x = "Tipo de Vehículo",
      y = "Consumo en la ciudad"
   )
~~~

### Gráfica de violín

- Las gráficas de caja no muestran la distribución de los datos
   - Un dataset con distribución normal y uno multinomial podrían generar la misma gráfica de caja
- Las gráficas de violín añaden una gráfica de densidad (KDE) girada a cada lado de las estimaciones de una gráfica
- Al igual que las gráficas de caja, se utilizan para identificar patrones, rangos, sesgos, además de la distribución

~~~r
ggplot(mpg, aes(class, cty)) +
   # Esto es nuevo
   geom_violin(fill = "pink")
~~~

