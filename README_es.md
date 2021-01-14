# odoo_api
Odoo API estilo XMLRPC

## Índice de Contenidos

- [Documentation](#documentation)
  * [Odoo Version](#odoo-version)
    * [Parameters](#parameters)
    * [Examples](#examples)
      + [Python](#python)
  * [Odoo Login](#odoo-login)
    * [Parameters](#parameters-2)
    * [Examples](#examples-2)
  * [Odoo Fields Get](#odoo-fields-get)
    * [Parameters](#parameters-3)
    * [Examples](#examples-3)
  * [Odoo Search Count](#odoo-search-count)
    * [Parameters](#parameters-4)
    * [Examples](#examples-4)
  * [Odoo Search](#odoo-search)
    * [Parameters](#parameters-5)
    * [Examples](#examples-5)
  * [Odoo Read](#odoo-read)
    * [Parameters](#parameters-6)
    * [Examples](#examples-6)
  * [Odoo Write](#odoo-write)
    * [Parameters](#parameters-7)
    * [Examples](#examples-7)
  * [Odoo Create](#odoo-create)
    * [Parameters](#parameters-8)
    * [Examples](#examples-8)
  * [Odoo Delete](#odoo-delete)
    * [Parameters](#parameters-9)
    * [Examples](#examples-9)

## Documentación

### Odoo Version

```POST /odoo-api/common/version```

#### Parámetros

Ninguno

#### Ejemplos

##### Python
```python
import requests
import json

url = 'http://localhost:8069/odoo-api/common/version'
data = {'params': {}}
headers = {'Content-type': 'application/json'}

r = requests.post(url, data=json.dumps(data), headers=headers)

print(r.text)
```
### Odoo Login

```POST /odoo-api/common/login```

#### Parámetros

Atributo | Tipo | Requerido | Descripción
--- | --- | --- | ---
`db` | string | yes | Nombre de BD del servidor Odoo
`login` | string | yes | Usuario Odoo
`password` | string | yes | Contraseña del Usuario Odoo

#### Ejemplos

### Odoo Fields Get

```POST /odoo-api/object/fields_get```

#### Parámetros

Atributo | Tipo | Requerido | Descripción
--- | --- | --- | ---
`model` | string | yes | Modelo de Odoo
`db` | string | yes | Nombre de BD del servidor Odoo
`login` | string | yes | Usuario Odoo
`password` | string | yes | Contraseña del Usuario Odoo

#### Ejemplos

### Odoo Search Count

```POST /odoo-api/object/search_count```

#### Parámetros

Atributo | Tipo | Requerido | Descripción
--- | --- | --- | ---
`model` | string | yes | Modelo de Odoo
`filters` | array | no | Filtro de Odoo para la búsqueda de registros
`db` | string | yes | Nombre de BD del servidor Odoo
`login` | string | yes | Usuario Odoo
`password` | string | yes | Contraseña del Usuario Odoo

#### Ejemplos

### Odoo Search

```POST /odoo-api/object/search```

#### Parámetros

Atributo | Tipo | Requerido | Descripción
--- | --- | --- | ---
`model` | string | yes | Modelo de Odoo
`filters` | array | no | Filtro de Odoo para la búsqueda de registros
`keys` | object | no | Argumentos de Odoo
`db` | string | yes | Nombre de BD del servidor Odoo
`login` | string | yes | Usuario Odoo
`password` | string | yes | Contraseña del Usuario Odoo

#### Ejemplos

### Odoo Read

```POST /odoo-api/object/read```

#### Parámetros

Atributo | Tipo | Requerido | Descripción
--- | --- | --- | ---
`model` | string | yes | Modelo de Odoo
`ids` | number array | yes | Array de números con los IDs de los registros
`db` | string | yes | Nombre de BD del servidor Odoo
`login` | string | yes | Usuario Odoo
`password` | string | yes | Contraseña del Usuario Odoo

#### Ejemplos

### Odoo Search Read

```POST /odoo-api/object/search_read```

#### Parámetros

Atributo | Tipo | Requerido | Descripción
--- | --- | --- | ---
`model` | string | yes | Modelo de Odoo
`filters` | array | no | Filtro de Odoo para la búsqueda de registros
`keys` | object | no | Argumentos de Odoo
`db` | string | yes | Nombre de BD del servidor Odoo
`login` | string | yes | Usuario Odoo
`password` | string | yes | Contraseña del Usuario Odoo

#### Ejemplos

### Odoo Write

```POST /odoo-api/object/write```

#### Parámetros

Atributo | Tipo | Requerido | Descripción
--- | --- | --- | ---
`model` | string | yes | Modelo de Odoo
`id` | number | yes | ID del registro de Odoo
`vals` | object | yes | Valores nuevos a escribir
`db` | string | yes | Nombre de BD del servidor Odoo
`login` | string | yes | Usuario Odoo
`password` | string | yes | Contraseña del Usuario Odoo

#### Ejemplos

### Odoo Create

```POST /odoo-api/object/create```

#### Parámetros

Atributo | Tipo | Requerido | Descripción
--- | --- | --- | ---
`model` | string | yes | Modelo de Odoo
`vals` | object | no | Valores nuevos en el registro a crear
`db` | string | yes | Nombre de BD del servidor Odoo
`login` | string | yes | Usuario Odoo
`password` | string | yes | Contraseña del Usuario Odoo

#### Ejemplos

### Odoo Delete

```POST /odoo-api/object/unlink```

#### Parámetros

Atributo | Tipo | Requerido | Descripción
--- | --- | --- | ---
`model` | string | yes | Modelo de Odoo
`id` | number | yes | ID del registro a eliminar
`db` | string | yes | Nombre de BD del servidor Odoo
`login` | string | yes | Usuario Odoo
`password` | string | yes | Contraseña del Usuario Odoo

#### Ejemplos
