# CSS Rules
CSS funciona asociando reglas con los elementos de HTML. Cada regla consta de dos partes:
- **Selector**
- **Declaration**: Property and Value

~~~css
p { 
    font-family: Arial;
}
~~~
En este caso, *p* es el selector y *font-family* es la declaration. Lo que aquí se quizo especificar es que todos los elementos `<p>`  deben mostrarse con letra Arial.

Puedes especificar varias reglas y varios elementos a la vez.

~~~css
h1,
h2,
h3 {
    font-family: Arial;
    color: yellow;
}
~~~

## Linking CSS file
Básicamente, el css lo haces en otro lado y usas un `<link>` para conectarlos.
~~~html
<html>
    <head>
        <link href='path/to/file.css' type='text/css' rel='stylesheet'>}
    </head>
</html>
~~~

## CSS selectors
| Selector | Meaning | Example |
| -------- | ------- | ------- |
|UNIVERSAL  | Applies to all elements in a document | **\*** {  } |
| TYPE  | Matches element names | **h1,<br> h2,<br> h3** { } |
| CLASS  | Matches an element whose *class* attribute has a value that matches the one specified after the period | **.note** { } <br> Any element whose class is *note*. <br><br>**p.note** { }<br>Only `<p>` elements whose class es *note*. |
| ID  | Matches an element whose id attribute has a specified value | **#id_value** { } |
|CHILD  | Matches an element that is a direct child of another | **li>a** { }<br> Any `<a>` elements that are childern of an `<li>` element. |
| DESCENDANT  | Matches an element that is a descendent of antoher specified element | **p a** { }<br>Any `<a>` elements that sit inside a `<p>` element, even if they are nested in other elements | 
| ADJACENT SIBILING | Matches an element that is the next sibiling of another | **h1+p** { } <br>The first `<p>` element after any `<h1>` element |
| GENERAL SIBILING | Matches an element that is a sibiling of another, although it doesn't have to be the directly preceding element | **h1~p** { } <br> If you had two `<p>` elements that are sibilings of an `<h1>` element, this rule would apply on both |
| EXISTENCE | Matches a specific attribute (whatever the value is) | **p[class]** { }<br>Targets any `<p>` element with an attribute called *class* |
| EQUALITY | Matches a specific attribute with a specific value | **p[class='dog']** { }<br>Targets any `<p>` element with an attribute class whose value is dog |
| LIST OF VALUES | Matches a specific attribute whose value appears in a space-separated list of words | **p[class~='dog']** { }<br>Targets any `<p>` element with an attribute called class whose value is a list of space-separated words, one of which is dog |
| PREFIX | Matches a specific attribute whose value begins with a specific string | **p[attr^'d']** { } <br> Targets any `<p>` element with an attribute whose value begins with the letter *d* |
| SUBSTRING | Matches a specific attribute whose value contains a specific substring | **p[attr\*'do']** { } <br> Targets any `<p>` element with an attribute whose value contains the letters *do* | 
| SUFFIX | Matches a specific attribute whose value ends with a specific string | **p[attr$'g']** { }<br>Targets any `<p>` element with an attribute whose value ends with the letter *g* | 

## CSS Rules Cascade
Si hay dos o más reglas que aplican al mismo elemento, es importante saber cuál va a proceder.<br>
Esto es bueno de saber, pues puedes crear reglas generales y después sobreescribirlas con reglas más específicas.<br><br>

**LAST RULE**  
Si ambos selectors son idénticos, el último es el que procede.
~~~css
i {
    color: green;
}

i {
    color: red;
}
~~~
En este caso el color final será rojo.  
<br>

**SPECIFICITY**  
Si un selector es más específico que otros, el más específico procederá sobre el más general.

Example:
- h1 > *
- p b > p
- p#intro > p

**IMPORTANT**  
Puedes agregar **!important** después de cualquier regla para indicar que esa deberá ser la elegida.

## Inheritance
Si específcas *font-family* en el `<body>`, esta aplicará para la mayoría de los hijos, pues estos la heredan.