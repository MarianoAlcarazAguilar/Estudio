# Pivot Tables, Grouper, pivot

Estas son funciones de pandas que son muy útiles para análisis de datos.

```python
import pandas as pd
import numpy as np
```



## Pivot

Primero abrimos los datos  
```python
data = pd.read_csv("/home/user/Documents/FuentesDeDatos/datasets/weatherTest.csv")
data
```

![Screenshot from 2022-04-20 23-31-27](https://user-images.githubusercontent.com/88745754/164372952-a951db5a-a777-4287-835c-a5364a7c6dd2.png)

Ahora vamos a usar la funión **Pivot**  
Lo que hace es que cambia el tipo de data. Pasa de long data a wide data o algo así.  
Vamos a poner de índice la ciudad y como columnas las fechas. 

```python
data.pivot(index='city', columns='date')
```
![Screenshot from 2022-04-20 23-38-23](https://user-images.githubusercontent.com/88745754/164373126-79b2ac45-f277-443c-96a0-cb60d1f97529.png)

Si solo nos interesan ciertos datos, entonces especificamos los valores.
```python
data.pivot(index='city', columns='date', values='humidity')
```
![Screenshot from 2022-04-20 23-39-54](https://user-images.githubusercontent.com/88745754/164373290-e33bb33c-9d04-42a8-9f0c-f11974df0f13.png)


## Pivot Table
Estas madres son como las de excel.  
Abramos otro dataset.  
```python
data2 = pd.read_csv("/home/user/Documents/FuentesDeDatos/datasets/weatherTest2.csv")
data2
```
![Screenshot from 2022-04-20 23-42-57](https://user-images.githubusercontent.com/88745754/164373609-9db1e8e4-b1ca-4935-812e-cc3df5ef8d62.png)

Ahora hagamos la pivot table. Por default aplica promedio
```python
data2.pivot_table(index='city', columns='date')
```
![Screenshot from 2022-04-20 23-43-48](https://user-images.githubusercontent.com/88745754/164373695-c9077f16-d0b9-4a56-b7f1-ef4fddbfdb48.png)

Cambiemos ahora la operación realizada.  
```python
data2.pivot_table(index='city', columns='date', aggfunc=np.sum)
```
![Screenshot from 2022-04-20 23-44-58](https://user-images.githubusercontent.com/88745754/164373819-b7be9909-f987-441d-936e-d1964a9cb08c.png)

Ahora agreguemos una fila y columna adicional que sume todo por categoría.  
```python
data2.pivot_table(index='city', columns='date', margins=True, aggfunc=np.sum)
```
![Screenshot from 2022-04-20 23-47-27](https://user-images.githubusercontent.com/88745754/164374065-b5143215-69a6-4581-8285-73b611054a60.png)


## Grouper
Esto es claramente una clase o algo así. Funciona especialmente bien con fechas.  
Recordemos que siempre tienen que estar en ese formato para que funcione esto correctamente.  

Abramos otro dataset.  
```python
data3 = pd.read_csv("/home/user/Documents/FuentesDeDatos/datasets/weatherTest3.csv")
data3
```
![Screenshot from 2022-04-20 23-49-16](https://user-images.githubusercontent.com/88745754/164374246-94dbe282-adaf-4c68-a932-b0ec0943f0fb.png)

Cuando la fecha está en un formato incorrecto se necesita castear. Para ello se hace lo siguiente.  
```python
data3['date'] = pd.to_datetime(data3['date'])
data3
```
![Screenshot from 2022-04-20 23-49-16](https://user-images.githubusercontent.com/88745754/164374246-94dbe282-adaf-4c68-a932-b0ec0943f0fb.png)

Hagamos ahora una pivot table, pero es precisamente en los índices donde se usa el Grouper para separar por el tiempo deseado las fechas.  
Aquí cabe recalcar que podemos usar los siguientes lapsos de tiempo: D, W, M, Y.  
Creo que queda muy claro para qué sirve cada uno
```python
data3.pivot_table(index=pd.Grouper(freq='M', key='date'), columns='city')
```
![Screenshot from 2022-04-20 23-52-06](https://user-images.githubusercontent.com/88745754/164374585-a5a9e277-f578-4d38-83a2-7421f053e53f.png)

















