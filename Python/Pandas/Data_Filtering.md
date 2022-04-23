# Filtering Data

```py
import pandas as pd
import numpy as np
import re
```

First, let us read our data
```py
data = pd.read_csv('/home/user/Documents/FuentesDeDatos/datasets/articles_data.csv')
data.head()
```
![Screenshot from 2022-04-23 16-41-30](https://user-images.githubusercontent.com/88745754/164946840-7e81e405-13ef-4d35-8641-8b739a297ec6.png)


If we want to get the names of our columns, we can do it like this
```py
list(data.columns.values)
```
![Screenshot from 2022-04-23 16-42-50](https://user-images.githubusercontent.com/88745754/164946873-4181d86e-4598-40c8-a3de-8ea3af6ee26f.png)


#### Droping Columns
```py
data = data.drop(columns=['Unnamed: 0', 'url', 'url_to_image'])
data.head()
```
![Screenshot from 2022-04-23 16-43-47](https://user-images.githubusercontent.com/88745754/164946893-fa0db61d-8add-4386-a5ad-a02c3ac943ac.png)


### Selecting specific columns
```py
data['source_id']
```
![Screenshot from 2022-04-23 16-45-31](https://user-images.githubusercontent.com/88745754/164946948-e69b6179-a794-41bd-8e65-f38b90ac9de3.png)

```py
data.source_id
```
![Screenshot from 2022-04-23 16-45-31](https://user-images.githubusercontent.com/88745754/164946948-e69b6179-a794-41bd-8e65-f38b90ac9de3.png)

To get multiple columns you have to give a list of columns
```py
data[['source_id', 'title']]
```
![Screenshot from 2022-04-23 16-46-57](https://user-images.githubusercontent.com/88745754/164946976-e79f2bee-d3c9-4ce9-afc9-db451d8eb58b.png)


### Filtering by index
To get the data of the first row, you have to specify the index
```py
data.iloc[0]
```
![Screenshot from 2022-04-23 16-48-10](https://user-images.githubusercontent.com/88745754/164947007-789dc43d-4633-4a56-8e2a-4481498b0701.png)

To get the data of a range of rows you specify it.  
Notice here, the index 3 is not included.
```py
data.iloc[0:3]
```
![Screenshot from 2022-04-23 16-49-19](https://user-images.githubusercontent.com/88745754/164947048-4896e144-ff03-45a7-8744-99b0290c3c0f.png)

To get specific rows, you need a list.  
```py
data.iloc[[3,2,5]]
```
![Screenshot from 2022-04-23 16-50-31](https://user-images.githubusercontent.com/88745754/164947067-8eafc563-9f30-4319-8e3c-9ff9129c78fc.png)


#### Reseting index
To reset the index we can do this.  
Notice here the old index has now become a new column
```py
data.iloc[[3,2,5]].reset_index()
```
![Screenshot from 2022-04-23 16-52-03](https://user-images.githubusercontent.com/88745754/164947106-bc3c44af-58f3-45fc-a0ea-53655dde1deb.png)

If you want to completely dismiss the old index, you have to specify it
```py
data.iloc[[3,2,5]].reset_index(drop=True)
```
![Screenshot from 2022-04-23 16-52-52](https://user-images.githubusercontent.com/88745754/164947127-fbb2d781-9e11-4b78-a2ad-fc5a0a3d5073.png)



### Filtering with conditions

Busquemos aquellos registros en los que el engagement_comment_count sea mayor a 10
```py
data[data['engagement_comment_count'] > 10]
```
![Screenshot from 2022-04-23 16-54-21](https://user-images.githubusercontent.com/88745754/164947169-aac25b76-ff25-4ad5-b6b6-ef5fa8190e45.png)

Busquemos aquellos registros en los que el engagement_comment_count sea mayor a 10 y menor a 50
```py
data[(data['engagement_comment_count'] > 10) & (data['engagement_comment_count'] < 50)]
```
![Screenshot from 2022-04-23 16-55-12](https://user-images.githubusercontent.com/88745754/164947214-d95321b2-76df-43fd-bfac-2697b4ca7c48.png)

We can alse use loc
```py
data[data['source_id'] == 'the-new-york-times']
```
![Screenshot from 2022-04-23 16-56-36](https://user-images.githubusercontent.com/88745754/164947246-9c5c34b6-c5b8-4228-b0e3-5a25b840bb96.png)


#### Using contains and match
We want to find those ones where the title contains Phone.  
In this case we have to use na=False, because there are some NaN in our data.  
```py
data[data['title'].str.contains('Phone', na=False)]
```
![Screenshot from 2022-04-23 16-58-19](https://user-images.githubusercontent.com/88745754/164947292-8a661d5d-b46b-4df9-bd5f-ae312ea0ff74.png)

Now we want everything that starts with Phone.  
This would normally bring only an exact match, but here we are using Regex.
```py
data[data['title'].str.match(r'^Phone', na=False)]
```
![Screenshot from 2022-04-23 16-59-40](https://user-images.githubusercontent.com/88745754/164947324-3857442e-a79b-4929-9765-b6631620344f.png)

Now we want to remove the ones that contain phone in title
```py
data[~data['title'].str.contains('Phone', na=False)]
```
![Screenshot from 2022-04-23 17-00-33](https://user-images.githubusercontent.com/88745754/164947339-27e290fb-d920-43a3-a29f-6a39f202d6a9.png)

We can also use contains in conjunction with regex
```py
data[data['title'].str.contains('hello|bye', na=False, regex=True, flags=re.I)]
```
![Screenshot from 2022-04-23 17-01-19](https://user-images.githubusercontent.com/88745754/164947355-5c65e705-fd93-4127-81d6-b5258cf57b8c.png)
























































































