# Regex

It's a way to search through text.

## Format
`/cat/g`

- Always starts with `/` and ends like that as well.
- The `g` are flags. There are many.


### Flags

- `g` is Global. 
  - Matches anywhere in the string. If you remove it, then it only finds the first match.
- `i` is case Insensitive
- `m` is Multiline
- `s` is Single line
- `u` is Unicode
- `y` is stickY

### Special Characters

- `+` Quantifier. Matches 1 or more of the preceding token.
- `?` Optional. The preceding token is optional.
- `*` Quantifier. Matches 0 or more of the preceding token.
- `.` Wild card. Except new line.
- `\` Will skip the next character (if it is special).
- `\w` Matches any word character or, numbers?
- `\s` Matches any space.
- `\W` Is the negative of \w. So matches everything but words.
- `\S` Negative of \s. Matches everything but spaces.
- `\d` Matches digits. It also has negative.
- `\b` Que lo siguiente esté al inicio de la línea. Si el \b lo pones al final entonces matchea lo anterior que esté al final.
- `{}` To specify the minimum and maximum of how large you want the previous thing.
- `[]` Matches any character specified inside them.
- `()` To create groups.
- `|` Or 
- `^` Matches the beggining of the line. For every line you should use multiline. If it's in [] it makes it negative.
- `$` Matches the end of the statement.
- `(?<=)` Positive look behind. Matches the next thing that comes right after what you specify inside the group.
- `(?<!)` Negative look behind. Matches averything except whatever has the specified text before it.
- `(?=)` Positive look ahead.
- `(?!)` Negative look ahead.

## Explanations

- `[abc]` Finds a,b or c
- `[^abc]` Any character except a,b or c
- `[a-z]` a to z
- `[A-Z]` A to Z
- `[a-zA-Z]` a to z, A to Z
- `[0-9]` 0 to 9

- `[]?` 0 or 1 time
- `[]+` 1 or more
- `[]*` 0 or more
- `[]{n}` excatly n times
- `[]{n,}` n or more
- `[]{n,m}` between n and m times

- `\d` is like `[0-9]`
- `\D` is like `[^0-9]`
- `\w` is like `[a-zA-Z0-9_]`
- `\W` is like `[^\w]`

## Examples

`/[0-9]{3}/g`  
Busca exactamente 3 números

`/^[\s]*(.*?)[\s]*$/g`  
Regresa cadenas de texto sin espacios en blanco al inicio ni al final.

`/<([a-z0-6]+)([^<]+)*(?:>(.*)>\/\1>|\s+\/>)/g`  
Regresa etiquetas HTML

`/\B#(?:[a-f0-9A-F]{3}|[a-f0-9A-F]{6})\b/g`  
Busca colores exadecimales. Las b ayudan a encapsular para que solo haya 3 o 6 pero no más dígitos. Es cuando buscas solo la parte encontrada y no todo el string

`/\b[\w]+@[\w-]+(\.[\w]+)+\b/g`  
Valida correos electrónicos

`/^[a-z0-9_-]{3,16}$/g`  
Valida nombres de usuarios

`/(?=^.{6,}$)((?=.*\w)(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[|!"$%&\/\(\)\?\^\'\\\+\-\*]))^.*/g`  
Valida un password: Al menos 1 mayúscula, 1 minúscula, 1 número y 1 caracter especial.  
Primer grupo: que al menos sea de 6 caracteres  







