# Forms

| Contenidos | Notas |
| ---------- | ----- |
| Form Structure | \<form> \</form> |
| Text  | \<input type="text"> |
| Password | \<input type="password"> |
| Text Area | \<textarea> \</textarea> |
| Radio Button | \<input type="radio"> |
| Checkbox |  \<input type="checkbox" name="" value="">
| Drop Down List Box | \<select name=""><br>&nbsp;&nbsp;&nbsp;&nbsp;\<option value=""> \</option><br>\</select>
| File | \<input type="file"> |
| Submit Button | \<input type="submit"> | 
| Image Button | \<input type="image" src="direccion"> |
| Grouping Form Elements | \<filedset> \</filedset><br>\<legend> \</legend> |


## Form Structure
Los controles del form viven dentro del elemento `<form action="">`, y siempre tiene el atributo action, y normalmente también tendrá el atributo method. 

- **action**: El url de la página que recibirá la información que se suba.
- **method**: Lo que pasará después de subir el archivo.
  - *get*: El valor que se suba se agrega al final de la url de *action*. Bueno para pequeños forms, búsquedas.
  - *post*: La inforamción se sube en HTTP readers. Agrega o elimina datos de una base de datos.

## Entradas de texto
### Text Input
<input type="text" name='username'>
<br><br>

Lo de arriba se creó usando el elemento vacío `input`.  
El atributo **name** es necesario para que el servidor sepa qué se le está enviando.  
Se puede usar el atributo **maxlength** para limitar el tamaño.

~~~html
<input type="text" name='username'>
~~~ 

### Password Input
<input type='password' name='contrasena'>
<br><br>

Es básicamente lo mismo pero se cambia el tipo.
~~~html
<input type="password" name="username">
~~~

### Text Area
<textarea name='area' cols='40' rows='5'>Este texto se muestra adentro</textarea><br><br>

Se usa para crear multi-line input. Lo que está adentro también se envía, pero se usa JavaScript para limpiarlo al dar click.
~~~html
<textarea name='area' cols='30' rows='5'>Este texto se muestra adentro</textarea>
~~~

## Buttons
### Radio Button
<input type="radio" name="genre" value="male">male
<input type="radio" name="genre" value="female">female
<input type="radio" name="genre" value="other">other
<br>

Una vez quye se selecciona una opción ya no se puede deseleccionar. Se usó el siguiente código.
~~~html
<input type="radio" name="genre" value="male">male
<input type="radio" name="genre" value="female">female
<input type="radio" name="genre" value="other">other
~~~

### Checkbox
<input type="checkbox" name="device" value="headphones">headphone
<input type="checkbox" name="device" value="speaker">speaker
<input type="checkbox" name="device" value="none">none
<br>

Este sí se puede deseleccionar, además de que puedes elegir varias a la vez.
~~~html
<input type="checkbox" name="device" value="headphones">headphone
<input type="checkbox" name="device" value="speaker">speaker
<input type="checkbox" name="device" value="none">none
~~~

### Dropdown List Box
<select name="devices" id="something">
    <option value="iPod">iPod</option>
    <option value="Radio">Radio</option>
    <option value="Computer">Computer</option>
</select>
<br><br>

Permite al usuario seleccionar una opción de la lista dada.
~~~html
<select name="devices" id="something">
    <option value="iPod">iPod</option>
    <option value="Radio">Radio</option>
    <option value="Computer">Computer</option>
</select>
~~~

### File Input Box
<input type='file' name='user-song'>
<br><br>

Permite al usuario subir un archivo.
~~~html
<input type='file' name='user-song'>
~~~

### Submit Button
<input type='submit' value='subscribe'>
<br><br>

En este caso el **value** es lo que se muestra adentro del botón.
~~~html
<input type='submit' value='subscribe'>
~~~

### Image Button
<br>
<input type='image' src='click-here.png' width='100' height='100'>
<br><br>

La verdad no sé como hacer que haga algo. Pero pues ahí está y se ve bonito.
~~~html
<input type='image' src='click-here.png' width='100' height='100'>
~~~

## Button & Hidden Controls
`<button> </button>` permite mostrar de distintas formas los botones. Por ejemplo, agregarles imágenes, pero la verdad no sé cómo funciona.
<br>
`<input type='hidden'>` este se puede usar si, por ejemplo, el desarrollador quiere enviar información adicional al final.

## Labeling Controls
`<label for=''></label>` Puede ir con for e ir después del input o dentro de la label tener el input. En ese caso no se necesita el atributo for.

## Grouping Form Elements
<form action="link.com" method="get">
    <fieldset>
        <legend>Your Details:</legend>
        <label >Name: <input type="text" name="name"></label>
        <br>
        <label >Email: <input type="text" name="email"></label>
    </fieldset>
    <fieldset>
        <legend>Your review:</legend>
        <textarea name="review" id="Review" cols="30" rows="10">How was the movie?</textarea>
    </fieldset>
</form>
<br>

Se usan los siguientes elementos: `<fieldset></fieldset>` y `<legend></legend>`. Legend va adentro de fieldset, y es correspondencia uno a uno. 

~~~html
<form action="link.com" method="get">
    <fieldset>
        <legend>Your Details:</legend>
        <label >Name: <input type="text" name="name"></label>
        <br>
        <label >Email: <input type="text" name="email"></label>
    </fieldset>
    <fieldset>
        <legend>Your review:</legend>
        <textarea name="review" id="Review" cols="30" rows="10">How was the movie?</textarea>
    </fieldset>
</form>
~~~