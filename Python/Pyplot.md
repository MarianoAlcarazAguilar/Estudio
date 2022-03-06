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

### Line Graph
```python
gas = pd.read_csv('gas_prices.csv')

plt.figure(figsize=(8,5))

plt.title('Gas Prices Over Time in USD')

plt.plot(gas.Year, gas.USA, marker='.', markersize=10, markeredgecolor='blue')
plt.plot(gas.Year, gas.Canada, marker='.', markersize=10, markeredgecolor='red')
plt.plot(gas.Year, gas['South Korea'], marker='.', markersize=10, markeredgecolor='green')
plt.plot(gas.Year, gas['Australia'], marker='.', markersize=10, markeredgecolor='red')

plt.xticks(gas.Year[::3])

plt.xlabel('Year')
plt.ylabel('US Dolars per Galon')

plt.legend(['USA','Canada','South Korea'])

plt.savefig('GasPrice.png', dpi=100)

plt.show()
```

![GasPrice](https://user-images.githubusercontent.com/88745754/156946710-ed56cb45-f3e5-433a-8fea-181a6032d5e8.png)

### Histograms
```python
bins= np.arange(40,101,10)

plt.hist(fifa.Overall, bins=bins, color='#f58c58')
plt.xticks(bins)
plt.ylabel('Number of Players')
plt.xlabel('Skill Leves')
plt.title('Distribution of Skills in Fifa 2008')

plt.savefig('DistributionSkills.png', dpi=100)

plt.show()
```

![DistributionSkills](https://user-images.githubusercontent.com/88745754/156946731-7b6da663-ba80-42de-937f-fad790312806.png)

### Pie Charts
```python
left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]
labels=['Left','Right']
colors=['#7b8eab','#335280']
plt.pie([left,right], labels = labels, colors=colors, autopct='%.2f %%')

plt.title('Preferred Foot in Fifa')

plt.savefig('preferredfoot.png', dpi=100)

plt.show()
```

![preferredfoot](https://user-images.githubusercontent.com/88745754/156946746-238698a8-304b-4768-bf9b-29ee12a44b79.png)

### Box Plot
```python
barcelona = fifa.loc[fifa.Club == 'FC Barcelona']['Overall']
madrid = fifa.loc[fifa.Club == 'Real Madrid']['Overall']
revs = fifa.loc[fifa.Club == 'New England Revolution']['Overall']

labels = ['Barcelona', 'Madrid', 'NE Revolution']

plt.figure(figsize=(5,8))
plt.title('Professional Teams Comparison')
plt.ylabel('Overall Rating')
boxes = plt.boxplot([barcelona, madrid, revs], labels = labels, patch_artist=True)

for box in boxes['boxes']:
    box.set(color='#489691', linewidth=3)
    
plt.savefig('comparison.png', dpi=100)

plt.show()
```

![comparison](https://user-images.githubusercontent.com/88745754/156946761-741f627d-cbf7-4579-8dba-55259c839bbc.png)




