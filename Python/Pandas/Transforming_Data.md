# Transforming Data


```py
import pandas as pd
```

First we open our data
```py
data = pd.read_csv('/home/user/Documents/FuentesDeDatos/datasets/weatherTest.csv')
data
```
![t1](https://user-images.githubusercontent.com/88745754/164948218-e79aa8ae-66e1-46af-af31-bdb3d7bf8fac.png)

Suppose we want to multiply temperature by a factor of 10
```py
data['temperature'] = data.temperature * 10
data
```
![t2](https://user-images.githubusercontent.com/88745754/164948230-f0b600a0-f664-4a68-b997-15dbe11b7e79.png)

If we want to have the multiplied column in a new one, we specify the new name.
```py
data['new_temp'] = data.temperature * 10
data
```
![t3](https://user-images.githubusercontent.com/88745754/164948245-8fc70d63-13c8-45b6-a8a3-d45e575380eb.png)

If what we want to do needs more than one column of our data frame, then we have to first write a function.  
Let's imagine we want to add temperature and humidity
```py
def addTempHum(line):
    return line.temperature + line.humidity
```

Now we use the apply function. We use axis=1 to make sure it will be horizontally applied.
```py
data['added'] = data.apply(addTempHum, axis=1)
data
```
![t4](https://user-images.githubusercontent.com/88745754/164948263-0d346f9b-983f-4ed9-8ec6-8ed775041873.png)

## Conditional Changes
Imagine we have made an error and all the humidity in London was always 100, then we can do it like this.
```py
data.loc[data.city == 'London', 'humidity'] = 100
data
```
![t5](https://user-images.githubusercontent.com/88745754/164948315-25bdbfd0-391c-468b-8d17-d8e2badf8c13.png)

Now suppose not only was the humidity wrong but also the temperature, which should have also been 100.
```py
data.loc[data.city == 'London', ['temperature','humidity']] = [100,100]
data
```
![t6](https://user-images.githubusercontent.com/88745754/164948327-218f9c16-8beb-476d-a21b-2ed7dc41eeb7.png)
