[English](https://github.com/codize-app/odoo_api/blob/master/README.md) | **Spanish**

# odoo_api
Odoo API estilo XMLRPC

El módulo odoo_api permite hacer llamadas REST API con una sintaxis similar a las llamadas XMLRPC. En beneficio de esto es no tener que realizar mucho desarrollo desde el backend. La contraparte es que debe realizarse desarrollo pero desde el frontend. Además, necesitará conocer el funcionamiento interno de Odoo.

Este módulo no tiene requerimientos para su instalación. Solo se necesita descargar del respositorio de github e instarlarlo en un Odoo. Por favor, tenga en cuenta que la configuración de dbfilter debe establecerse en una base de datos para que funcione la interfaz REST.

## Índice de Contenidos

- [Documentación](#documentación)
  * [Odoo Version](#odoo-version)
    * [Parámetros](#parámetros)
    * [Ejemplos](#ejemplos)
      + [Python](#python)
  * [Odoo Login](#odoo-login)
    * [Parámetros](#parámetros-2)
    * [Ejemplos](#ejemplos-2)
  * [Odoo Fields Get](#odoo-fields-get)
    * [Parámetros](#parámetros-3)
    * [Ejemplos](#ejemplos-3)
  * [Odoo Search Count](#odoo-search-count)
    * [Parámetros](#parámetros-4)
    * [Ejemplos](#ejemplos-4)
  * [Odoo Search](#odoo-search)
    * [Parámetros](#parámetros-5)
    * [Ejemplos](#ejemplos-5)
  * [Odoo Read](#odoo-read)
    * [Parámetros](#parámetros-6)
    * [Ejemplos](#ejemplos-6)
  * [Odoo Write](#odoo-write)
    * [Parámetros](#parámetros-7)
    * [Ejemplos](#ejemplos-7)
  * [Odoo Create](#odoo-create)
    * [Parámetros](#parámetros-8)
    * [Ejemplos](#ejemplos-8)
  * [Odoo Delete](#odoo-delete)
    * [Parámetros](#parámetros-9)
    * [Ejemplos](#ejemplos-9)

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
`db` | string | si | Nombre de BD del servidor Odoo
`login` | string | si | Usuario Odoo
`password` | string | si | Contraseña del Usuario Odoo

#### Ejemplos

### Odoo Fields Get

```POST /odoo-api/object/fields_get```

#### Parámetros

Atributo | Tipo | Requerido | Descripción
--- | --- | --- | ---
`model` | string | si | Modelo de Odoo
`db` | string | si | Nombre de BD del servidor Odoo
`login` | string | si | Usuario Odoo
`password` | string | si | Contraseña del Usuario Odoo

#### Ejemplos

### Odoo Search Count

```POST /odoo-api/object/search_count```

#### Parámetros

Atributo | Tipo | Requerido | Descripción
--- | --- | --- | ---
`model` | string | si | Modelo de Odoo
`filters` | array | no | Filtro de Odoo para la búsqueda de registros
`db` | string | si | Nombre de BD del servidor Odoo
`login` | string | si | Usuario Odoo
`password` | string | si | Contraseña del Usuario Odoo

#### Ejemplos

### Odoo Search

```POST /odoo-api/object/search```

#### Parámetros

Atributo | Tipo | Requerido | Descripción
--- | --- | --- | ---
`model` | string | si | Modelo de Odoo
`filters` | array | no | Filtro de Odoo para la búsqueda de registros
`keys` | object | no | Argumentos de Odoo
`db` | string | si | Nombre de BD del servidor Odoo
`login` | string | si | Usuario Odoo
`password` | string | si | Contraseña del Usuario Odoo

#### Ejemplos

### Odoo Read

```POST /odoo-api/object/read```

#### Parámetros

Atributo | Tipo | Requerido | Descripción
--- | --- | --- | ---
`model` | string | si | Modelo de Odoo
`ids` | number array | si | Array de números con los IDs de los registros
`db` | string | si | Nombre de BD del servidor Odoo
`login` | string | si | Usuario Odoo
`password` | string | si | Contraseña del Usuario Odoo

#### Ejemplos

### Odoo Search Read

```POST /odoo-api/object/search_read```

#### Parámetros

Atributo | Tipo | Requerido | Descripción
--- | --- | --- | ---
`model` | string | si | Modelo de Odoo
`filters` | array | no | Filtro de Odoo para la búsqueda de registros
`keys` | object | no | Argumentos de Odoo
`db` | string | si | Nombre de BD del servidor Odoo
`login` | string | si | Usuario Odoo
`password` | string | si | Contraseña del Usuario Odoo

#### Ejemplos

### Odoo Write

```POST /odoo-api/object/write```

#### Parámetros

Atributo | Tipo | Requerido | Descripción
--- | --- | --- | ---
`model` | string | si | Modelo de Odoo
`id` | number | si | ID del registro de Odoo
`vals` | object | si | Valores nuevos a escribir
`db` | string | si | Nombre de BD del servidor Odoo
`login` | string | si | Usuario Odoo
`password` | string | si | Contraseña del Usuario Odoo

#### Ejemplos

### Odoo Create

```POST /odoo-api/object/create```

#### Parámetros

Atributo | Tipo | Requerido | Descripción
--- | --- | --- | ---
`model` | string | si | Modelo de Odoo
`vals` | object | no | Valores nuevos en el registro a crear
`db` | string | si | Nombre de BD del servidor Odoo
`login` | string | si | Usuario Odoo
`password` | string | si | Contraseña del Usuario Odoo

#### Ejemplos

### Odoo Delete

```POST /odoo-api/object/unlink```

#### Parámetros

Atributo | Tipo | Requerido | Descripción
--- | --- | --- | ---
`model` | string | si | Modelo de Odoo
`id` | number | si | ID del registro a eliminar
`db` | string | si | Nombre de BD del servidor Odoo
`login` | string | si | Usuario Odoo
`password` | string | si | Contraseña del Usuario Odoo

#### Ejemplos
___

Originalmente desarrollado para Codize App

Desarrollador: Ignacio Buioli <<ibuioli@gmail.com>>
