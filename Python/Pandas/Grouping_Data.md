# Grouping Data

```py

```

```py
import pandas as pd
import numpy as np
```

First, let us open our data.
```py
data = pd.read_csv('/home/user/Documents/FuentesDeDatos/datasets/weatherTest.csv')
data
```
![g1](https://user-images.githubusercontent.com/88745754/164949303-b4471c2b-3936-4ea7-82ae-fbbb5ad90902.png)

Let us group by city and take the mean of the other columns
```py
data.groupby('city').mean()
```
![g2](https://user-images.githubusercontent.com/88745754/164949313-bf322ecf-d7eb-4f90-9a1f-d8b48884ea2d.png)

Let us group by city and date and take the mean of the other columns
```py
data.groupby(['city', 'date']).mean()
```
![g3](https://user-images.githubusercontent.com/88745754/164949329-3a390ab1-78aa-4a8b-bd7a-3e1b0e05ea68.png)

If we want to apply different functions over different columns we have to use the agg function.  
We can select from: count, sum, mean, median, min, max, mode, std, var.  
```py
data.groupby('city').agg({'temperature': 'mean', 'humidity':'sum'})
```
![g4](https://user-images.githubusercontent.com/88745754/164949353-afd38520-3307-4e87-b153-782da4f3da3b.png)


We can alse use NamedAgg but right now I don't really know how that works
