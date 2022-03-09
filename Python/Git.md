# Git

Git es una madre que sirve para un buen de cosas. Te ayuda a ver los cambios que se han ido haciendo  en tu código.

## Basic Commands

- `git init` vamos a empezar a usar en este proyecto git
- `git add <file>` Para mandarlo al staging area
- `git status` Para ver en dónde está
- `git commit` Para subirlo a un repositorio
- `git push` Para subirlo a un repositorio remoto
- `git pull` Para traer los cambios hechos por otros
- `git clone` Hacer una copia a tu computadora

Working Directory --> git add --> Staging area --> git commit --> Repository

## Configuración

```bash
git config --global user.email "marianoaaguilar@hotmail.com"
git config --global user.name "insert name here"
```

### Ejemplos de comandos

Esto comienza como la carpeta
```bash
git init
```

Esto es para ver en que estatus están los archivos de la carpeta
```bash
git status
```

Esto es para seguir el proceso de los archivos
El segundo agrega todos los archivos a la vez
```bash
git add fileName.txt
git add .
```

Esto es para crear un snapshot, un primer punto de partida. Commit es básicamente confirmar los cambios. Pero primero tienes que hacer el add.
Con el segundo te evitas entrar al editor.
```bash
git commit
  escribe comentario para el commit
    :wq
    
git commit -m "mensaje aquí"
```

Si modificas un archivo y lo quieres regresar al estado anterior, entonces usas checkout
```bash
git checkout -- fileName.txt
```

Para ver la diferencia entre el archivo después de los cambios
```bash
git diff fileName.txt
```

Con esto puedes ver todas las versiones del documento
```bash
git log
```

Si tienes archios que no quieres agregar entonces tienes que crear un archivo con el siguiente nombre y adentro agregar el nombre de lo que no quieras
```bash
.gitignore
```

Creo que esto es como para crear varias versiones del archivo
```bash
git branch
git branch "newBranchName"
git checkout newBranchName
```

## Using git with GitHub

Abrir repositorios y agregamos nuevo repositorio.

Para conectarlo a internet primero copias el link del repositorio y luego lo metes en el siguiente comando
El primero crea el repositorio.
Lo segundo le dice que suba los archivos al gitHub. 
```bash
git remote add origin https://github.com/MarianoAlcarazAguilar/...
git push -u origin master
```

Para bajar los datos del repositorio
```bash
git clone https://github.com/MarianoAlcarazAguilar/...
```



