---
doc_id: webex-wholesale-put-wholesale-customers-customerid
source: webex-openapi-specs/public-spec/webex-wholesale.json
api: Webex Wholesale
method: PUT
path: /wholesale/customers/{customerId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.731922+00:00
---

# PUT /wholesale/customers/{customerId}

**API:** Webex Wholesale
**Área:** Wholesale Provisioning
**operationId:** `Update a Wholesale Customer`

## Resumen
Update a Wholesale Customer

## Descripción
Updates certain details of a provisioned Wholesale customer for Cisco Webex services.

The Wholesale customer provisioning is asynchronous and thus a background task is created when this endpoint is invoked.

**packages Note:**

* `cisco_calling_plan` is dependent on: `common_area_calling`, `webex_calling`, `webex_suite`, `webex_voice`, `cx_essentials`, `webex_calling_standard`

* `attendant_console` is dependent on: `webex_calling`, `webex_suite`, `cx_essentials`, `webex_voice`

<div>
        <Callout type='info'>After successful invocation of this endpoint a URL will be returned in the `Location` header, which will point to the [Get a Wholesale Customer](/docs/api/v1/wholesale-provisioning/get-a-wholesale-customer) endpoint for this customer.</Callout>
</div>

## Parámetros
- `customerId` [path] (string) **(requerido)**: A unique identifier for the customer to be updated.
- `onBehalfOfSubPartnerOrgId` [query] (string): The encoded organization ID for the sub partner.

## Cuerpo de la petición (application/json)
- `externalId` (string): External ID of the Wholesale customer.
- `packages` (array) **(requerido)**: The complete list of Webex Wholesale packages to be assigned to the customer, including any packages already provisioned. If a package has already been assigned to this customer and is not present in this list, then that package is removed.
- `address` (object): Billing Address of the customer. (There is a 50 character limit on each address line)
  - `addressLine1` (string) **(requerido)**: Address line 1.
  - `addressLine2` (string): Address line 2.
  - `city` (string) **(requerido)**: Customer's city.
  - `stateOrProvince` (string): State or Province of the customer. This attribute may be required in specific geographies, please refer to address section in the admin guide for more information.
  - `zipOrPostalCode` (string): Postal/Zip code of the customer. This attribute may be required in specific geographies, please refer to address section in the admin guide for more information.
  - `country` (string) **(requerido)**: ISO2 country code of the customer size = 2.
- `provisioningParameters` (object): Provisioning parameters are required when updating an existing package.
  - `calling` (object):
    - `location` (object) **(requerido)**:
      - `name` (string) **(requerido)**: Name of the wholesale customer office.
      - `address` (object) **(requerido)**: Address of the wholesale customer. (There is a 50 character limit on each address line)
        - `addressLine1` (string) **(requerido)**:
        - `addressLine2` (string):
        - `city` (string) **(requerido)**:
        - `stateOrProvince` (string): State or Province of the customer in ISO 3166 format. This attribute may be required in specific geographies, please refer to address section in the admin guide for more information.
        - `zipOrPostalCode` (string): Postal/Zip code of the customer. This attribute may be required in specific geographies, please refer to address section in the admin guide for more information.
        - `country` (string) **(requerido)**:
      - `timezone` (string) **(requerido)**: Customer timezone for calling package. The full list of supported timezones can be found at [List of Time Zones for Wholesale Provisioning](https://help.webex.com/en-us/article/nuh0amab/List-of-Time-Zones-for-Wholesale-Provisioning).
      - `language` (string) **(requerido)**: Determine language for all generated emails and voice announcements.
      - `emergencyLocationIdentifier` (string): SIP Header for any emergency calls from this location.
  - `meetings` (object):
    - `timezone` (string): Customer timezone for meetings package.
  - `packages` (object):
    - `limits` (object): Packages followed by their respective limits.
      - `webex_calling` (number):
      - `common_area_calling` (number):
      - `webex_meetings` (number):
      - `webex_suite` (number):
      - `webex_voice` (number):
      - `cx_essentials` (number):
      - `webex_calling_standard` (number):
      - `attendant_console` (number):
- `subPartnerAdminEmail` (string): The email of the sub partner organization admin.

### Ejemplo de petición
```json
{
  "externalId": "c1677a16-557a-4fb4-b48f-24adde57ec99",
  "packages": [
    "common_area_calling"
  ],
  "address": {
    "addressLine1": "\"771 Alder Drive\"",
    "addressLine2": "\"Cisco Site 5\"",
    "city": "\"Milpitas\"",
    "stateOrProvince": "\"CA\"",
    "zipOrPostalCode": "\"95035\"",
    "country": "\"US\""
  },
  "provisioningParameters": {
    "calling": {
      "location": {
        "name": "\"Head Office\"",
        "address": {
          "addressLine1": "\"771 Alder Drive\"",
          "addressLine2": "\"Cisco Site 5\"",
          "city": "\"Milpitas\"",
          "stateOrProvince": "\"CA\"",
          "zipOrPostalCode": "\"95035\"",
          "country": "\"US\""
        },
        "timezone": "\"America/Los_Angeles\"",
        "language": "\"en_us\"",
        "emergencyLocationIdentifier": "\"95547321\""
      }
    },
    "meetings": {
      "timezone": "\"America/Los_Angeles\""
    },
    "packages": {
      "limits": {
        "webex_calling": 50,
        "common_area_calling": 50,
        "webex_meetings": 50,
        "webex_suite": 50,
        "webex_voice": 50,
        "cx_essentials": 50,
        "webex_calling_standard": 50,
        "attendant_console": 50
      }
    }
  },
  "subPartnerAdminEmail": "admin@subpartnerorg.com"
}
```

## Respuestas
- **202**: Accepted
  - `url` (string): A URL which points to the [Get a Wholesale Customer](/docs/api/v1/wholesale-provisioning/get-a-wholesale-customer) endpoint for the provisioned customer.
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **409**: Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **410**: Gone: The requested resource is no longer available.
- **415**: Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **423**: Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **428**: Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
