# John The Ripper

John the ripper is a popular open source password cracking tool that combines several different cracking programs and runs both in brute force and dictionary attack modes.

It is usually used in enterprise to detect weak passwords that could put network security at risk, as well as other administrative purposes. The software can run a wide variety of password-cracking techniques against the various user accounts on each operating system and can be scripted to run locally or remotely.

## Dictionary Attack

A dictionary attack is based on trying all the strings in a pre-arrenged listing. Such attacks used words found in a dictionary, however, now there are much larger lists available on the open internet containing hundreads of millions of passwords recovered from past data breaches. There is also cracking software that can use such lists and produce common variations (john the ripper can do this).

El comando para ejecutar un ataque de este tipo es el siguiente:
~~~sh
john --pot=modoBase.pot --format=Raw-SHA256 --wordlist=dictionary_words.txt passwords_to_hack.txt
~~~

Donde,
- `--pot`  es la opción que nos permite ir guardando las contraseñas quese van encontrando. Esto es muy útil para no probarlas de nuevo cuando se quiera descifrar un nuevo archivo que pueda contener las mismas contraseñas.
- `--format` especifica el hasheo que tienen las contraseñas objetivo. Si no se especifica, se prueban todos los posibles formato de hash.
- `--wordlist` especifica el nombre del archivo que contiene las palabras que deseamos usar para comparar con las que se buscan.
- Al final se agrega el nombre del archivo sobre el cuál se hará el ataque.

## Brute Force Attack

This type of attack uses trial-and-error to guess login info. You basically work through all possible combinations hoping to guess correctly. This is the most effective attack, since if we had theoretically limitless time, we would be able to guess every single password, although that is a little unreal to believe. A big problem with this type of approach is that if the password that we are trying to guees is really long, then this will take way too long time to find it because the number of possible cominations grows rapidly.

El comando para ejecutar un ataque de este tipo es el siguiente:
~~~sh
john --pot=fuerzaBruta.pot --format=Raw-SHA256 --incremental passwords_to_hack.txt
~~~

Notemos que la única diferencia con este tipo de ataque y el anterior es que en este caso no se necesita el diccionario de palabras, sino que más bien elegimos la opción de `--incremental`, la cual especifica que en este caso será fuerza bruta lo que se usará. Claramente sería buena idea primero intentar con un ataque de diccionario y posteriormente uno de fuerza bruta, pues eliminaríamos muchas opciones que ya no sería necesario intentar de forma aleatoria.