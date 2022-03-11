from bs4 import BeautifulSoup
import requests
import re

#Esto es para abrir el archivo
with open("index.html","r") as fi:
    doc = BeautifulSoup(fi , "html.parser")

#Prettify hace más bonito el archivo
#print(doc.prettify())

#How to find things by their tag name
#This will only get you the first result
tag = doc.title
#print(tag)

#If you use string then you only get the text from the tag
#print(tag.string)

#To modify tags you do it like this
tag.string = "hola"
#print(tag)

#To access multiple tags at a time. Este regresa todas las que tengan p en una lista
tags = doc.find_all("p")
#print(tags)

#To access a nested tag (inside another one) you just treat the previous tag as an html file
nestedTag = tags[0].find_all('b')
#print(nestedTag)

#How to read from an HTML file
#We need to have installed requests
#We are going to get the price from
# https://www.newegg.ca/black-kanto-dm1000-monitor-arm/p/N82E16886549006?Item=9SIA4F74757417&
# cm_sp=Homepage_SS-_-P1_9SIA4F74757417-_-03102022

url = "https://www.newegg.ca/black-kanto-dm1000-monitor-arm/p/N82E16886549006?Item=9SIA4F74757417&cm_sp=Homepage_SS-_-P1_9SIA4F74757417-_-03102022"
result = requests.get(url) #Result holds the html or text, but now we'll read it with BeautifulSoup
ndoc = BeautifulSoup(result.text, "html.parser")
prices = ndoc.find_all(text="$")

#print(prices)
#Tags have parents, and we can use them to move around, like in a tree structure
parent = prices[0].parent
#print(parent)
#Cuando ya estás trabajando con un tag, no se necesita text="". Olvídalo, text es para cuando no es el nombre
#del tag
strong = parent.find("strong")
dollars = strong.string
sup = parent.find("sup")
cents = sup.string
#print(dollars, cents)


#Now we are working with another file
with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

#Modifie attributes of a tag
tag = doc.find("option")
#En este caso tag se ve así: <option selected="" value="course-type">Course type*</option>
tag['value'] = "NEW VALUE"
#Y ahora se ve así: <option selected="" value="NEW VALUE">Course type*</option>
#To add atributes you just type them
tag['color'] = "red"
#Now: <option color="red" selected="" value="NEW VALUE">Course type*</option>
#To show all the attributes you do this. Esto regresa un diccionario
attributes = tag.attrs
#print(attributes)

#To look for multiple tags you put them in a list
tags = doc.find_all(['p','div','li'])

#Ahora queremos encontrar los tags de tipo 'option' que tengan de texto 'Undergraduate', con value 'undergraduate'
tags = doc.find_all('option', text='Undergraduate', value='undergraduate')

#How to find different class names
#The problem is tha class is a reserved name in python
tags = doc.find_all(class_="btn-item")

#Using regular expressions
#For this you need to import re
tags = doc.find_all(text=re.compile("\$[0-9]*"))
#This is just to get it nice
#for tag in tags:
    #print(tag.strip())

#How to limit the amount of tags you get
tags = doc.find_all(text=re.compile("\$[0-9]*"), limit=1)
#print(tags)

#Now we will download the name and prices of criptocurrencies from the next page:
#https://coinmarketcap.com/
#La tabla en donde están todos los datos es tbody
#Loading data
url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

#Note that tbody is the parent of al tr (table rows) which are all at the same level
#You can go from one sibiling to the next one
tbody = doc.find('tbody')
#This gives you a list of all the tags that are inside of tbody
trs = tbody.contents
nextSib = trs[0].next_sibling
prevSib = trs[1].previous_sibling
#This returns to the tbody
parent = prevSib.parent
prices = {}
for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string
    prices[fixed_name] = fixed_price
print(prices)

