# Color

| Contenido | Notas | 
| --------- | ----- | 
| Foreground Color | Color del texto |
| Background Color | Color del fondo | 
| Opacity | Opacidad | 


<br>  

## Foreground Color&nbsp;&nbsp;&nbsp;`color`
La propiedad *color* te permite especificar el color del texto adentro del elemento.
| RGB | HEX | Name |
| --- | --- | ---- |
| rgb(100, 100, 90) | #000000 | DarkCyan |

~~~css
h1 {
    color: DarkCyan;
}

h2 {
    color: #000000;
}
p {
    color: rgb(100, 100, 90);
}
~~~

<br>  

## Background Color &nbsp;&nbsp;&nbsp;`background-color`
Dado que CSS trata cada elemento como si estuviera en una caja, podemos cambiar el color del fondo de la caja en cuestión.  Si no especificas un color, será transparente.

~~~css
p {
    background-color: white;
}
~~~

<br>

## Opacity  &nbsp;&nbsp;&nbsp;`opacity, rgba`
Puedes usar **opacity** y poner un número entre 0 y 1.  
O puedes usar **rgba** que agrega un valor adicional, la *a* de *alpha*. Es mejor usar el primero.

~~~css
p.one {
    background-color: rgb(0,0,0);
    opacity: 0.5;
}
p.two {
    background-color: rgba(0,0,0,0.5,);
}
~~~