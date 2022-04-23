# Data Cleaning

```py
import pandas as pd
```

Abramos los datos primero
```python
data = pd.read_csv('/home/user/Documents/FuentesDeDatos/datasets/weatherTest.csv')
data
```
![Screenshot from 2022-04-21 00-15-59](https://user-images.githubusercontent.com/88745754/164377142-74f24321-32bb-4af7-b8de-b881c9960007.png)

Ahora quitemos todos los NaN con la función `dropna`
```python
data.dropna()
```
![Screenshot from 2022-04-21 00-17-49](https://user-images.githubusercontent.com/88745754/164377707-179cff3d-af9a-4baa-a653-5c3ded27b9f6.png)

Si queremos sustituir los NaN por otros, también podemos hacerlo con `fillna`
```python
data.fillna('HOLA')
```
![Screenshot from 2022-04-21 00-19-17](https://user-images.githubusercontent.com/88745754/164378160-48fd3b7a-9738-4811-9062-7976fe751be3.png)


También podemos pasar un diccionario especificando con qué queremos llenar cada columna en el caso de que haya NaN.  
```python
data.fillna({'date':'10-10-2010', 'temperature':100})
```
![Screenshot from 2022-04-21 00-22-41](https://user-images.githubusercontent.com/88745754/164379039-e64ff84d-e577-4a32-8670-76835b6954a7.png)
