# Data Frames

Básicamente son tablas de excel. Está compuesto por filas y columnas. Cada columna tiene un tipo de dato, y solo uno.
Cada columna es identificada por un nombre y un índice, empezando en 0.
Cada fila es identificada por un índice.

## Making a Data Frame
Esto es cuando tienes los datos y les quieres dar formato de DataFrame
```python
nombres = ['mariano','ximena',rodrigo','jose','esna']
edades = [20,20,21,21,20]
datos = {'nombre':nombres, 'edad':edades}
dataFrame = pd.DataFrame(datos)
```
![Screenshot from 2022-04-21 00-08-19](https://user-images.githubusercontent.com/88745754/164376327-2e8e304e-0485-4dbd-bbb6-64017332502a.png)


## Opening Files
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
Si queremos acceder a información descriptiva de nuestros datos, podemos usar la función **describe**.  
Describe devuelve estadísticos descriptivos de la información. Regresa otro dataFrame con la información.
```python
df.describe()
```
![Screenshot from 2022-04-21 00-09-15](https://user-images.githubusercontent.com/88745754/164376397-b6155cbf-6ff7-497c-810c-43a165103d91.png)
