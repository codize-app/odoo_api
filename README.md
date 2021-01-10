# odoo_api
Odoo API XMLRPC Style

## Documentation

### Odoo Version

```POST /odoo-api/common/version```

#### Parameters

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
