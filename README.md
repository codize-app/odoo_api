**English** | [Spanish](https://github.com/codize-app/odoo_api/blob/master/README_es.md)

# odoo_api
Odoo API XMLRPC Style

The module odoo_api allows you make REST API calls with a sintax similar to XMLRPC calls. The benefit of this is, you do not have to  do a lot of development on the backend side. The downside of that is you still have to do a lot of coding, on the frontend side. Plus, you will need to know the inner workings of Odoo. 

This module has no requirements for its installation. You only need to download it form the github repository and install it in your Odoo. Please, keep in mind that the dbfilter setting needs to be set to a database for the REST interface to work.

Check wiki: [odoo_api wiki](https://github.com/codize-app/odoo_api/wiki)

## Table of contents

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

## Documentation

### Odoo Version

```POST /odoo-api/common/version```

#### Parameters

None

#### Examples

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

#### Parameters

Attribute | Type | Required | Description
--- | --- | --- | ---
`db` | string | yes | Odoo server DB name
`login` | string | yes | Odoo User
`password` | string | yes | Odoo User Password

#### Examples

### Odoo Fields Get

```POST /odoo-api/object/fields_get```

#### Parameters

Attribute | Type | Required | Description
--- | --- | --- | ---
`model` | string | yes | Odoo model
`db` | string | yes | Odoo server DB name
`login` | string | yes | Odoo User
`password` | string | yes | Odoo User Password

#### Examples

### Odoo Search Count

```POST /odoo-api/object/search_count```

#### Parameters

Attribute | Type | Required | Description
--- | --- | --- | ---
`model` | string | yes | Odoo model
`filters` | array | no | Odoo filter for records in search
`db` | string | yes | Odoo server DB name
`login` | string | yes | Odoo User
`password` | string | yes | Odoo User Password

#### Examples

### Odoo Search

```POST /odoo-api/object/search```

#### Parameters

Attribute | Type | Required | Description
--- | --- | --- | ---
`model` | string | yes | Odoo model
`filters` | array | no | Odoo filter for records in search
`keys` | object | no | Odoo key arguments
`db` | string | yes | Odoo server DB name
`login` | string | yes | Odoo User
`password` | string | yes | Odoo User Password

#### Examples

### Odoo Read

```POST /odoo-api/object/read```

#### Parameters

Attribute | Type | Required | Description
--- | --- | --- | ---
`model` | string | yes | Odoo model
`ids` | number array | yes | Odoo number array of record IDS
`db` | string | yes | Odoo server DB name
`login` | string | yes | Odoo User
`password` | string | yes | Odoo User Password

#### Examples

### Odoo Search Read

```POST /odoo-api/object/search_read```

#### Parameters

Attribute | Type | Required | Description
--- | --- | --- | ---
`model` | string | yes | Odoo model
`filters` | array | no | Odoo filter for records in search
`keys` | object | no | Odoo key arguments
`db` | string | yes | Odoo server DB name
`login` | string | yes | Odoo User
`password` | string | yes | Odoo User Password

#### Examples

### Odoo Write

```POST /odoo-api/object/write```

#### Parameters

Attribute | Type | Required | Description
--- | --- | --- | ---
`model` | string | yes | Odoo model
`id` | number | yes | Odoo record ID
`vals` | object | yes | Odoo object of values to write
`db` | string | yes | Odoo server DB name
`login` | string | yes | Odoo User
`password` | string | yes | Odoo User Password

#### Examples

### Odoo Create

```POST /odoo-api/object/create```

#### Parameters

Attribute | Type | Required | Description
--- | --- | --- | ---
`model` | string | yes | Odoo model
`vals` | object | no | Odoo object of values to create on record
`db` | string | yes | Odoo server DB name
`login` | string | yes | Odoo User
`password` | string | yes | Odoo User Password

#### Examples

### Odoo Delete

```POST /odoo-api/object/unlink```

#### Parameters

Attribute | Type | Required | Description
--- | --- | --- | ---
`model` | string | yes | Odoo model
`id` | number | yes | Odoo record ID to delete
`db` | string | yes | Odoo server DB name
`login` | string | yes | Odoo User
`password` | string | yes | Odoo User Password

#### Examples

___

Originally developed for Codize App

Developer: Ignacio Buioli <<ibuioli@gmail.com>>
