# Sorting Data

```py
import pandas as pd
import numpy as np
```

First, we open our data.
```py
data = pd.read_csv('/home/user/Documents/FuentesDeDatos/datasets/weatherTest.csv')
data
```
![Screenshot from 2022-04-23 17-10-08](https://user-images.githubusercontent.com/88745754/164947550-7bcb587d-08b0-473e-a324-f8762a568bd4.png)

Sorting values by temperature
```py
data.sort_values('temperature')
```
![s1](https://user-images.githubusercontent.com/88745754/164947590-4a02d271-888e-4a54-a0dc-fe717be71050.png)

Sorting values by date in descending order
```py
data.sort_values('date', ascending=False)
```
![s2](https://user-images.githubusercontent.com/88745754/164947610-ec792544-fe39-4736-8566-36b814f8dda1.png)

Sorting values by date and temperature.  
If there are two values with the same date, then the one with the lowest temperature will be placed first.
```py
data.sort_values(['date', 'temperature'])
```
![s3](https://user-images.githubusercontent.com/88745754/164947640-3047009d-c326-4103-86d8-34776ad358ad.png)

Sorting values by date in descending order and temperature in ascending order
```py
data.sort_values(['date', 'temperature'], ascending=[0,1])
```
![s4](https://user-images.githubusercontent.com/88745754/164947663-96816965-25a3-48f8-84a8-18cd3258f0ac.png)
