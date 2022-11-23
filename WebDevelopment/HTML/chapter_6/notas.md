# Tables

| Contenidos | Notas |
| ---------- | ----- |
| Basic Table Structure | \<table>\</table><br>&nbsp;&nbsp;&nbsp;&nbsp;\<tr>\</tr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\<td>\</td> |
| Table Headings | \<th>\</th> |
| Spanning Columns | colspan="" |
| Spanning Rows | rowsapn="" |
| Long Tables | \<thead>\</thead><br>\<tbody>\</tbody><br>\<tfoot>\</tfoot> |


## Basic Table Structure
Para la siguiente gráfica se usó el código mostrado
<table>
    <tr>
        <td>Característica uno</td>
        <td>Característica dos</td>
    </tr>
    <tr>
        <td>Elemento uno</td>
        <td>Elemento dos</td>
    </tr>
</table>

~~~html
<table>
    <tr>
        <td>Característica uno</td>
        <td>Característica dos</td>
    </tr>
    <tr>
        <td>Elemento uno</td>
        <td>Elemento dos</td>
    </tr>
</table>
~~~

## Table Heading
Ahora hacemos que la primera línea se vea como heading
<table>
    <tr>
        <th>Característica uno</th>
        <th>Característica dos</th>
    </tr>
    <tr>
        <td>Elemento uno</td>
        <td>Elemento dos</td>
    </tr>
</table>

~~~html
<table>
    <tr>
        <th>Característica uno</th>
        <th>Característica dos</th>
    </tr>
    <tr>
        <td>Elemento uno</td>
        <td>Elemento dos</td>
    </tr>
</table>
~~~

## Spanning Columns
Cuando necesitas que la entrada de una línea se alargue más de una columna.
<table>
    <tr>
        <th>Característica uno</th>
        <th>Característica dos</th>
    </tr>
    <tr>
        <td colspan="2">Elemento uno y dos están dentro de la misma línea</td>
    </tr>
</table>

~~~html
<table>
    <tr>
        <th>Característica uno</th>
        <th>Característica dos</th>
    </tr>
    <tr>
        <td colspan="2">Elemento uno y dos están dentro de la misma línea</td>
    </tr>
</table>
~~~

## Spanning rows
Lo mismo que arriba pero en alargamiento de líneas.
<table>
    <tr>
        <th rowspan="2">Características</th>
        <th>Característica uno</th>
        <td> Elemento uno </td>
    </tr>
    <tr>
        <th>Característica dos</th>
        <td>Elemento dos</td>
    </tr>
</table>

~~~html
<table>
    <tr>
        <th rowspan="2">Características</th>
        <th>Característica uno</th>
        <td> Elemento uno </td>
    </tr>
    <tr>
        <th>Característica dos</th>
        <td>Elemento dos</td>
    </tr>
</table>
~~~

## Long Tables
Básicamente solo sirve para después darle merjor foramto con CSS.
<table>
    <thead>
        <tr>
            <th></th>
            <th>Característica uno</th>
            <th>Característica dos</th>
            <th>Característica tres</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Línea 1</td>
            <td>11</td>
            <td>12</td>
            <td>13</td>
        </tr>
        <tr>
            <td>Línea 2</td>
            <td>21</td>
            <td>22</td>
            <td>23</td>
        </tr>
        <tr>
            <td>Línea 3</td>
            <td>31</td>
            <td>32</td>
            <td>33</td>
        </tr>
    </tbody>
    <tfoot>
        <td></td>
        <td colspan="3">Este es el pie de la tabla</td>
    </tfoot>
</table>

~~~html
<table>
    <thead>
        <tr>
            <th></th>
            <th>Característica uno</th>
            <th>Característica dos</th>
            <th>Característica tres</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Línea 1</td>
            <td>11</td>
            <td>12</td>
            <td>13</td>
        </tr>
        <tr>
            <td>Línea 2</td>
            <td>21</td>
            <td>22</td>
            <td>23</td>
        </tr>
        <tr>
            <td>Línea 3</td>
            <td>31</td>
            <td>32</td>
            <td>33</td>
        </tr>
    </tbody>
    <tfoot>
        <td></td>
        <td colspan="3">Este es el pie de la tabla</td>
    </tfoot>
</table>
~~~