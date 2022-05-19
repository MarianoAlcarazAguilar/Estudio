# Environments

Esto es solo para crear ambientes.  
En cada uno puedes tener instalados diferentes paquetes de python y así usar solo los que necesites.  

### Creación de un nuevo environment
```bash
conda create -n my_new_env python=3.9
```

### Cambiar de environment
Si primero queremos ver qué ambientes tenemos diponibles, entonces los enlistamos
```bash
conda env list
```

Cuando ya sabemos cuál es el que necesitamos, lo activamos.  
```bash
conda activate my_new_env
```

### Guardar requerimientos del environment
Esto es para que sea replicable después.
```bash
conda freeze > requirements.txt
```
En este caso los estamos guardando en un archivo que se llama requirementes.

