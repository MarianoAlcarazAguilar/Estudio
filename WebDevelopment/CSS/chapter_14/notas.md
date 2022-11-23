# Lists, Tables and Forms

| Contenido | Notas |
| --- | --- | 

## Bullet Point Styles `list-style-type`

Allows you to control the sape or style of a bullet point (also known as **marker**)
It can be used on rules that apply to the `<ol>, <ul> and <li>` elements.

### Unordered Lists
You can use one of the next values:
- none
- disc (cículo coloreado todo de negro)
- circle (círculo con borde negro, sin relleno)
- square (cuadrado coloreado todo de negro)

### Ordered Lists
You can use one of the next values:
- decimal: 1, 2, 3
- decimal-leading-zero: 01, 02, 03
- lower-alpha: a, b, c
- upper-alpha: A, B, C
- lower-roman: i, ii, iii
- upper-roman: I, II, III

### Images for Bullets `list-style-image`
It can be used on rules that apply to the `<ul> and <li>`elements.

~~~css
ul {
   list-style-image: url('images/star.png'):
}
~~~


### Positioning the marker `list-style-position`
Indicates wether the marker should apperar on the inside or the outside of the box containing the main points.

Básicamente sirve para diferenciar si la bolita debe funcionar como margen para el texto de abajo, o si será como un caracter más.

This property can take two values:
- outside: the marker sits to the left of the block text (default)
- inside: the marker sits inside the box of the text (which is indented)

~~~css
ul.one {
   list-style-position: outside;
}
ul.two {
   list-style-position: inside;
}
~~~

## Table Properties
| Property | Explanation |
| --- | --- |
| width | to set the width of the table |
| padding | to set the space between the border of each table cell and its content | 
| text-transform | to convert the content of the table headers to uppercase |
| letter-spacing<br>font-size | to add aditional styling to the content of the table headers | 
| border-top<br>border-botton | to set borders above and below the table headers |
| text-align | to align the writing to the left of some table cells and to the right of others |
| background-color | to change the background color of the alternating table rows |
| :hover | to highlight a table row when a user's mouse goes over it |

~~~css
body {
   font-family: Arial, Verdana, sans-serif;
   color: #111111;
}

table {
   width: 600px;
}

th,
td {
   padding: 7px 10px 10px 10px;
}

th {
   text-transform: uppercase;
   letter-spacing: 0.1 em;
   font-size: 90%;
   border-bottom: 2px solid #111111;
   border-top: 1px solid #999;
   text-align: left;
}

tr.even {
   background-color: #efefef;
}

tr:hover{
   background-color: #c3e6e5;
}

.money{
   text-align: right;
}
~~~

### Border on empty cells `empty-cells`
It can take one of the next three values:
- show: this shows the borders of any empty cells
- hide: this hides the borders of any empty cells
- inherit: if you have one table nested inside another, the *inherit* value instructs the table cells to obey the rules of the containing table

~~~css
td {
   border: 1px solid #0088dd;
   padding: 15px;
}

table.one {
   empty-cells: show;
}

table.two {
   empty-cells: hide;
}
~~~

### Gaps between cells `border-spacing, border-collapse`
The `border-spacing` property allows you to control the distance between adjacent cells. Usually this space is really small.  
<br>
When a border has been used on talbe cells, where to cells meet, the width of lines would be twice that of the outside edges. It is possible to collapse adjacent borders to prevent this using the `border-collapse` property. Possible values are:
- collapse
- separate: borders are detached from each other

~~~css
td {
   background-color: #0088dd;
   padding: 15px;
   border: 2px solid #000000;
}

table.one {
   border-spacing: 5px 15px;
}

table.two {
   border-collapse: collapse;
}
~~~

## Styling Forms
<br>
<br>

### Styling Text Inputs
| Property | Explanation |
| --- | --- |
| font-size | sets the size of the text entered by the user | 
| color | sets the text color | 
| background-color | sets the background color of the input | 
| border | adds a border around the edge of the input box |
| border-radius | can be used to create rounded corners |
| :focus | change the background color of the text input when it is being used | 
| :hover | applies the same styles when the user hovers over them |
| background-image | adds a background image to the box | 

~~~css
input {
   font-size: 120%;
   color: #5a5854;
   background-color: #f2f2f2;
   border: 1px solid #bdbdbd;
   border-radius: 5px;
   padding: 5px 5px 5px 30px;
   background-repeat: no-repeat;
   background-position: 8px  9px;
   display: block;
   margin-bottom: 10px;
}

input:focus {
   background-color: #ffffff;
   border: 1px solid #b1e1e4;
}

input#email {
   background-image: url('images/email.png')
}
~~~

<br>
<br>

### Styling Submit Buttons

| Property | Explanation |
| --- | --- |
| color | change the color of the text on the button | 
| text-shadow | can give a 3D look | 
| border-bottom | has been used to make the bottom border of the button slightly thicker | 
| background-color | can make the submit button stand out from other items | 
| :hover | change the appearance when hovered | 

~~~css
input#submit{
   color: #444444;
   text-shadow: 0px 1px 1px #fff;
}
~~~

<br>
<br>

### Styling Fieldsets & Legends
| Porperty | Explanation |
| --- | --- |
| width | control the width of the fieldset. Forces the form elements to wrap onto a new line in the correct place | 
| color | control the color of the text | 
| background-color | change the color behind the items | 
| border | control the appearance of the border around the fieldset and/or legend |
| border-radius | soften the edges of these elements | 
| padding | add space inside these elements |

<br><br>

## Cursor Styles  `cursor`
Allows you to control the type of mouse cursor that should be displayed to users. You can use one of the next values: 
- auto
- cosshair
- default
- pointer 
- move
- text 
- wait
- help
- url('cursor.gif')

You should use them to make as complicated to understand to the user as possible. If it makes absolutely no sense, then it's a great idea to use it.

~~~css
a {
   cursor: move;
}
~~~

