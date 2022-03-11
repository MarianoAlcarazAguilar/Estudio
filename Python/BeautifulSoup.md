# Beautiful Soup

Este paquete sirve para hacer web scrapping. Está muy padre la verdad. Basicamente hace todo por ti.

##### Imports you may need
```python
from bs4 import BeautifulSoup
import requests
import re
```

## Abrir archivos HTML
La 'r' es de 'read'. Si quisieras escribir el archivo pondrías 'w'.  
Prettify lo hace más bonito, pero no es necesario.  
Esto funciona cuando YA tienes el archivo html en tu computadora.
```python
with open("fileName.html", "r") as f:
  doc = BeautifulSoup(f, "html.parser")
print(doc.prettify())
```

Cuando no tienes el archivo descargado, y más bien quieres llamarlo desde internet, se abre así  
```python
url = "www.link.com"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")
```
El html.parser puede cambiar, ya que har varios parsers. Pero la verdad no sé que sean, ni como funcionan.  

## Searching stuff
### Searching with TAGS
This will only get you the first result.  
The string will bring only the text that the tag has. (Second)  
```python
tag = doc.title
tag.string
```

To modify what a tag says, you do it like this
```python
tag.string = "new text"
```

To get multiple tags at a time.  
The first one brings all the p tags.  
The second one brings all the p and a tags
```python
tags = doc.find_all('p')
tags = doc.find_all(['p','a'])
```

How to access nested tags.  
Básicamente trata el tag como otro html.
```python
nestedTag = tags[0].find_all('b')
```

### Searching with TEXT
Esto se hace cuando no sabes el nombre del tag, pero sabes qué texto estás buscando.  
```python
tags = doc.find_all(text="hola")
```
### Searching with VALUES
La verdad no me acuerdo para qué sirve esto, pero si lo usas a lo mejor te das cuenta.  
```python
tags = doc.find_all('option', text='Undergraduate', value='undergraduate')
```
Esto regresa las etiquetas de tipo option, que tengan en su texto lo especificado y value igual.  
### Searching with CLASSES
En este caso se usa esa notación porque class es una palabra reservada de python.  
```python
tags = doc.find_all(class_="className")
```
### Searching with REGEX
Para cuando no sabes exactamente lo que estás buscando.    
```python
tags = doc.find_all(text=re.compile("\$[0-9]*"))
```
Se utiliza compile para que funcione bien. De seguro hay otra forma de hacerlo, pero así lo mostraron.  
### Searching limiting the amount of results
```python
tags = doc.find_all('a', limit=10)
```

## Using HTML Structure
HTML has a tree structure that we can use in our advantage, so that it's easier to look for things.  
Here you can see how it is designed.
![image](https://user-images.githubusercontent.com/88745754/157805571-5a7114eb-eea0-4fbb-924f-b4926634b25a.png)
  
```python
parent = tag.parent
nextSib = tag.next_sibiling
prevSib = tag.previous_sibiling
```

## Modify Attributes of a Tag
Para modificar atributos ya existentes.  
```python
tag['value'] = 'new value'
```
Para crear nuevos atributos.  
```python
tag['color'] = 'red'
```
Estamos suponiendo que antes no existía el atributo color.  
  
Para cuando necesitemos los atributos de la tag.  
```python
tag.attrs
```
