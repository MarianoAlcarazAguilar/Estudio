# Joining Data

It's important to remember that there are different types of joins:
![IMG_3023](https://user-images.githubusercontent.com/88745754/164949692-02514493-c5d1-4df9-ad26-cd4234de5eab.PNG)

```py
import pandas as pd
import numpy as np
```

First, let us open our data.  
This time we will have to open three datasets to showcase how this works. 
```py
age_data = pd.read_csv('/home/user/Documents/FuentesDeDatos/datasets/age_data.csv')
height_data = pd.read_csv('/home/user/Documents/FuentesDeDatos/datasets/height_data.csv')
weight_data = pd.read_csv('/home/user/Documents/FuentesDeDatos/datasets/weight_data.csv')
```
![Archivo_000](https://user-images.githubusercontent.com/88745754/164950396-aa9f5ba2-2a7f-4732-b556-aa6345670baa.png)


Let's say we want to join the data of age and height.  
By default the function merge will apply an inner join.  
Notice how we don't have alondra in this data frame.  
```py
merged1 = pd.merge(age_data, height_data, on='name')
merged1
```
![m1](https://user-images.githubusercontent.com/88745754/164950458-2a918208-8741-4294-801e-c519a4559446.png)

Let's say we want to join the data of age and height but in this case we don't want to lose alondra's data.  
For that case, we use a left join.  
```py
merged2 = pd.merge(age_data, height_data, on='name', how='left')
merged2
```
![m2](https://user-images.githubusercontent.com/88745754/164950472-d70af975-ccfc-470b-86da-b9080ff3409d.png)

Now we want to join age and weight, but notice that name doesn't appear in both data frames.  
In that case, we have to specify the column of each data frame.  
We can get rid of one of the columns that have the same data, but that is not necessary here.
```py
merged3 = pd.merge(age_data, weight_data, left_on='name', right_on='nombre')
merged3
```
![m3](https://user-images.githubusercontent.com/88745754/164950483-1dd93035-5f90-4ce5-94e0-269689a29db5.png)


We can make joins on multiple columns.  
Our data doesn't really allow us to do so, but let's try it anyways.
```py
merged4 = pd.merge(age_data, height_data, left_on=['name','age'], right_on=['name', 'height'], how='outer')
merged4
```
![m4](https://user-images.githubusercontent.com/88745754/164950497-8a8ad99f-49f0-47cf-84d3-e3ba6dbea17c.png)


Now we want to join all the tables.  
```py
merged5 = pd.merge(age_data, height_data, on='name').merge(weight_data, left_on='name', right_on='nombre')
merged5 = merged5.drop(columns='nombre')
merged5
```
![m5](https://user-images.githubusercontent.com/88745754/164950516-c39dda08-f928-4341-99dd-2e4251cef930.png)

