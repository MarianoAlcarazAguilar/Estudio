# Images &nbsp;

| Contenido | Notas |
| --------- | ----- |
| Inserción | \<img> |
| Height & Width | height="" &nbsp;&nbsp;&nbsp; width="" |
| Figure & Caption | \<figure> & \<figcaption>

## Adding images
Se pueden poner literalmente en cualquier lugar.
~~~html
<img src="referencia" alt="descripción" title="título" height="" width="">
~~~
Atributos:
- **src**: Referencia a la imagen, normalmente es relativa.
- **alt**: Descripción de la imagen.
- **title**: Título que los browsers muestran cuando pasas el mouse sobre la imagen.
- **height**: Es bueno usarlo para que el buscador sepa cuando espacio reservar.
- **width**: Same as above.

## Figure & Caption
Como en pyplot, puedes tener un eleemnto figure en el que haya varias imágenes, u luego estas tengan una caption *(caption es única por figura)*.
~~~html
<figure>
    <img src ="referencia" alt="descripción">
    <p>
        <figcaption>
            Caption
        </figcaption>
    </p>
</figure>