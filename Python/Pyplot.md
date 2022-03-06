# Pyplot

Imports you may need

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
```

### Basic Charts
```python
x=[1,2,3,4,5]
y=[2,4,6,8,10]

#Resize the graph
plt.figure(figsize=(6,6), dpi=100)

#Line Number one
plt.plot(x,y, label='2x', color='#ababab', linewidth=2, marker='.', markersize=10, markeredgecolor='blue', linestyle='--')

#Line Number two
x2 = np.arange(1,5.5,0.5)
plt.plot(x2, x2**2, color = '#bbbbbb', label='x^2')

#Line Number three
x3 = np.arange(1,5.5,0.5)
plt.plot(x3[:6], x3[:6]+2, color='y')
plt.plot(x3[5:], x3[5:]+2, color = 'y', linestyle='--')

#Esto agrega título
plt.title('Our first Graph!', fontdict={'fontname':'Comic Sans MS', 'fontsize':20})

#Esto cambia los valores de los ejers
plt.xticks([1,2,3,4,5])

#Add a legend
plt.legend()

#Esto agrega el título de cada axis
plt.xlabel('X axis', fontdict={'fontname':'Times New Roman', 'fontsize':20})
plt.ylabel('Y axis')

#Save the graph
plt.savefig('firstGraph.png')

plt.show()
```
![firstGraph](https://user-images.githubusercontent.com/88745754/156943953-9aada547-e1d4-491d-9c58-e16795b919df.png)

### Bar Chart
```python
labels = ['A','B','C']
values = [1,4,2]

bars = plt.bar(labels, values)

bars[0].set_hatch('/')
bars[1].set_hatch('O')
bars[2].set_hatch('*')

plt.savefig('firstGraph.png')

plt.show()
```

![secondGraph](https://user-images.githubusercontent.com/88745754/156943987-1cfadf42-2d9f-404b-96c4-c0a83dff47a5.png)



