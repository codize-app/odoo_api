# odoo_api
Odoo API XMLRPC Style

## Documentation

### Odoo Version

```POST /odoo-api/common/version```

#### Parameters

None

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
