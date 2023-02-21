# Conceptos Básicos

### Visualización de información

- La **comunicación** de información utilizando **representaciones gráficas**
- Los sistemas de cómputo para visualización proveen **representaciones visuales** de conjuntos de datos diseñadas para ayudar a la gente a realizar sus **tareas de manera más eficiente**

Pero, ¿para qué usar visualizaciones?

- Para **validar** hipótesis
- Para **analizar** información
- Para **reconocer** patrones y tendencias
- Para **descubrir** y crear nueva información
- Para **comunicar** más claramente información

En resumen, para **contar** historias con datos y para **tomar mejores** decisiones.

### Razones para visualizar

- El sistema visual ocupa aproximadamente 50% del cerebro. 
- Es un canal enorme con ancho de banda hacia el cerebro. 
- Además, la interpretación de una imagen se procesa en paralelo.

### Gráfica

~~~
Valores desplegados en un área delimitada por uno o más ejes

Valores codificados como objetos visuales en relación a los ejes

Los ejes proporcionan escalas (cuantitativas y categóricas) usadas para etiquetar y asignar valores a los objetos
~~~

Por su naturaleza visual, son ideales para **revelar patrones** en los datos y para hacer **comparaciones cualitativas**.

## Tipos de datos

### En función de atributos

$$
\text{Categóricos / Nominales \quad}
\begin{cases}
\cdot \quad \text{Permiten comparar y agrupar}\\
\cdot \quad \text{No hay ordenamiento implícito, pero con frecuencia tienen jerarquías}\\
\cdot \quad \text{No es posible realizar operaciones aritméticas}
\end{cases}
$$

<br>

$$
\text{Ordenados} \quad
\begin{cases}
   \text{Ordinales} 
   \begin{cases} 
      \cdot \quad \text{Ordenamiento implícito o explícito}\\
      \cdot \quad \text{Permiten hacer comparaciones y relaciones tipo} \geq = \leq \\
   \end{cases}\\
   \\
   \text{Cuantitativos}
   \begin{cases}
      \cdot \quad \text{La magnitud tiene sentido y con base en ella se pueden hacer ordenamientos y comparaciones}\\
      \cdot \quad \text{Permiten realizar operaciones aritméticas}\\
   \end{cases}\\
\end{cases}
$$

### Relaciones cuantitativas

$$
\text{Tipos de datos}
\begin{cases}
   \cdot \quad \text{Categóricos }(qué)\\
   \cdot \quad \text{Cuantitativos }(cuánto)
\end{cases}
$$

<br>

$$
\text{Asociaciones\\ categoría-valor}
\begin{cases}
   \text{Relaciones entre datos categóricos}
   \begin{cases}
      \cdot \quad \text{Nominal}\\
      \cdot \quad \text{Ordinal}\\
      \cdot \quad \text{Intervalo}\\
      \cdot \quad \text{Jerárquica}\\
   \end{cases}
   \\
   \\
   \text{Relaciones entre datos cuantitativos}
   \begin{cases}
      \cdot \quad \text{Ranking}\\
      \cdot \quad \text{Tasa}\\
      \cdot \quad \text{Correlación}\\
   \end{cases}
\end{cases}
$$

### Datos cuantitativos

- Binarios, continuos o discretos
- Escalares
   - Un número o atributo en un registro (celda)
- Vectores
   - Varios números en un registro
- Tensores
   - Muchos números en un registro. Se definen por su rango y dimensionalidad, representados por un arreglo o matriz

### Semántica
Los datos aislados no tienen sentido.

~~~
Es el significado de esos datos en el mundo real
~~~

Con frecuencia esta información se añade como metadata. Ejemplo de ellos son los diccionarios que se agregan a las tablas para explicar sus significados.

### Items y Atributos

Item
~~~
Entidad individual, discreta
Un renglón en una tabla
~~~

Atributo
~~~
Variable o dimensión
Propiedad que es observada, medible o registrada
Una columna en una tabla
~~~

### Tipos de conjuntos de datos

**Tabla**
- Un item por fila
- Cada columna es un atributo
- Celda $=$ valor para un item/atributo
- Una sola llave (puede ser implícita)

**Tabla Multidimensional**
- Llaves múltiples
- El valor de una celda sigue representando una asociación item/atributo

**Redes y árboles**
- Atributos pueden estar asociados a los enlaces o a los nodos
- Un árbol no tiene ciclos

**Espaciales**
- Campos
- Geográficos

## Marcadores y Canales Visuales

### Marcadores

~~~
Elementos geométricos utilizados para representar ítems, grafos o listas
~~~

Se utilizan para mapear en un espacio de dos dimensiones los ítems o enlaces/vínculos que deseamos mostrar.  

- Se trata de elementos geométricos básicos:
   - Puntos
   - Líneas
   - Áreas
   - Los volúmenes se utilizan muy raramente

### Canales Visuales

~~~
Propiedades de los marcadores para representar atributos. 
Controlan la apariencia de los marcadores.
~~~

- Posición
- Color
- Forma
- Orientación
- Tamaño
- Volumen

### Cuándo usar qué canal

**Expresividad**

- Tratar de alinear el tipo de canal con el tipo de dato
- La codificación seleccionada debe permitir mostrar toda (y solamente) la información de los atributos del dataset
   - Datos no ordenados NO deberían insinuar orden pero sí una categoría

**Efectividad**

- Algunos canales simplemente son mejores que otros para transmitir el mensaje que deseamos comunicar
- La importancia del atributo debe coincidir con la prominencia del canal

| Tipo | Atributo | Capacidad para representar una cantidad |
| --- | --- | --- |
| Forma | Longitud <br> Anchura <br> Orientación <br> Tamaño <br> Forma <br> Bordeado | Sí <br> Sí, pero limitado <br> Sí, pero limitado <br> Sí, pero limitado <br> No <br> No |
| Color | Tonalidad <br> Intensidad | No (Discutible) <br> Sí, pero limitado |
| Posición | Posición 2D | Sí |

### Efectividad de los canales

Es importante destacar que el sistema perceptua opera con **juicios relativos**, no absolutos. Además, distintos canales visuales se perciben con diferente precisión.  

<br>

Hay que tomar en cuenta los siguientes criterios:
- **Exactitud**: Qué tan precisamente podemos identificar e interpretar la diferencia entre ítems codificados
   - Factores que la afectan: 
      - distractores
      - alineación
      - distancia
- **Discriminación**: Cuántos pasos únicos podemos percibir. Indica si se pueden distinguir valores de los atributos con los pasos o niveles que ofrece el canal
   - Al menos tantos niveles como valores pueda tener el atributo
- **Separabilidad**: Qué tanto nuestra habilidad para utilizar un canal es modificada por otros canales
   - Muy pocos canales son ortogonales y no interfieren entre sí. Ejemplo: color y posición
   - Si interfieren entre sí, debe minimizarse el uso de cada canal para distintos atributos
- **Resaltado**: Cómo puede resaltar algo utilizando cierto canal
   - Muchos canales permiten resaltar un ítem en particular
   - Factores que lo favorecen:
      - Longitud
      - Ancho
      - Orientación
      - Dirección
      - Forma
      - Tamaño
      - Bordeado
      - Sombra

### Algunas recomendaciones

**Atributos Ordenados** 

<img src=".png">

**Atributos Categóricos**

<img src='.png'>

Lamentablemente, la efectividad es altamente subjetiva y depende, entre otros:

- Antecedentes y madurez analítica
- Habilidades perceptuales
- Gustos
- Contexto

Lo que sí es cierto, es que el tener una **escala común** permite aumentar la exactitud de las comparaciones subjetivas.

### Luminancia y juicio relativo

La percepción de luminancia es contextual y basada en el contraste de los objetos circundantes