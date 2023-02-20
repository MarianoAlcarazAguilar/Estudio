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
**Definición**
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

**Definición**
~~~
Es el significado de esos datos en el mundo real
~~~

Con frecuencia esta información se añade como metadata. Ejemplo de ellos son los diccionarios que se agregan a las tablas para explicar sus significados.

### Items y Atributos

**Item**
~~~
Entidad individual, discreta
Un renglón en una tabla
~~~

**Atributo**
~~~
Variable o dimensión
Propiedad que es observada, medible o registrada
Una columna en una tabla
~~~