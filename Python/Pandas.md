# Pandas

Librería para hacer análisis de datos. Permite usarlos como una hoja de excel pero mucho más rápido.

```python
import pandas as pd
```


## DataFrames
Básicamente son tablas de excel. Está compuesto por filas y columnas. Cada columna tiene un tipo de dato, y solo uno.
Cada columna es identificada por un nombre y un índice, empezando en 0.
Cada fila es identificada por un índice.

### Abrir Documentos

En este caso crea los índices para las filas automáticamente empezando desde cero.
```python
df = pd.read_csv('titleName.csv')
```

Ahora le especificamos que los índices están dados por la columna 'id' y ya no los hace automáticamente.
Head muestra las primeras 5 filas
Tail muestra las últimas 5 filas
```python
df = pd.read_csv('titleName.csv', index_col='id')
df.head()
df.tail()
```

Describe devuelve estadísticos descriptivos de la información. Regresa otro dataFrame con la información.
```python
df.describe()
```

### Limpieza de Datos

Cuando tenemos valores nulos se pueden quitar usando dropna. Elimina los valores que tengan NaN. 
Si queremos sustituir los NaN por un valor fijo podemos especificarlo con fillna. En este caso estamos llenando con 0.
Para el llenado de NaN se puede pasar un diccionario especificando el llenado para cada columna.
```python
df_filtrado = df.dropna()
df_llenado = df.fillna(0)
df_llenado_esp = df.fillna({'columna1':0, 'columna2': 'no'})
```

```python

```

### Filtrado de Datos

#### Traer datos de solo una columna (también regresa los ínidces)
```python
df['columna1']
df[['columna1','columna2']]
```

#### Para hacer filtrado por filas mediante índices.
El primero regresa los valores de la primera fila.
El segundo regresa los valores de las filas 0 a 2
El tercero regresa los valores de las filas 0, 2 y 4
```python
df.iloc[0]
df.iloc[0:3]
df.iloc[[0,2,4]]
```

#### Filtrado por indicadores (Cuando especificamos que los índices están dados por una columna)
```python
df.loc[['id1','id2']]
```

#### Filtrado de filas y columnas
El siguiente regresa las filas del 0 al 2, y solo las columnas 2 y 4
```python
df.iloc[[0:3],['columna2','columna4']]
```

#### Filtrado por condiciones
El primero es para buscar aquellos cuyo valor en la columna1 sea mayor a 50
El segundo es para poner varias condiciones.
Cuando la columna tiene palabras eg. (contains regresa no matches exactos, por ejemplo, regresaria Programas, Programación, Programa televisivo...)
```python
df[df['columna1'] > 50]
df[(df['columna1'] > 50) & (df['columna2'] > 90)]
df[df['textColumn'].str.contains('Programa')]
```

### Transformación de Datos
Por ejemplo para convertir una columna que está en centímetros a metros.
```python
def convierteMetros(cm):
  metros = cm/100
  return metros

df['nuevaColumna'] = df['columnaCm'].apply(convierteMetros)
```

Si la columna creada necesita usar más de dos columnas del dataFrame.
Por ejemplo calcular ganancias.
```python
def ganancias(fila):
  resp = fila['precio']*fila['cantidad']
  return resp

df['nuevaColumna'] = df.apply(ganancias, axis=1)
```

### Agrupación de Datos
Agrupemos por país, y apliquemos promedio a las otras columnas
```python
df.groupby('country').mean()
```

Aplicar diferentes acciones sobre diferentes columnas cuando están agrupadas.
```python
df.groupby('country').agg({'columna1':'sum', 'columna2': 'mean', 'columna3': 'max'})
```

Para filtrar sobre agrupaciones
```python
grouped = df.groupby('country').agg({'columna1':'sum', 'columna2': 'mean', 'columna3': 'max'})
grouped[grouped['columna1'] > 100]
```

### Guardado de archivos
```python
grouped.to_csv('title_output.csv')
```
