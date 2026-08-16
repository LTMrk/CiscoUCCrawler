---
doc_id: webex-wholesale-post-wholesale-customers-validate
source: webex-openapi-specs/public-spec/webex-wholesale.json
api: Webex Wholesale
method: POST
path: /wholesale/customers/validate
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.732198+00:00
---

# POST /wholesale/customers/validate

**API:** Webex Wholesale
**Área:** Wholesale Provisioning
**operationId:** `Precheck a Wholesale Customer Provisioning`

## Resumen
Precheck a Wholesale Customer Provisioning

## Descripción
Allows the Partner sales team to verify likely success of provisioning a Wholesale customer.

**packages Note:**

* `cisco_calling_plan` is dependent on: `common_area_calling`, `webex_calling`, `webex_suite`, `webex_voice`, `cx_essentials`, `webex_calling_standard`

* `attendant_console` is dependent on: `webex_calling`, `webex_suite`, `cx_essentials`, `webex_voice`

<div>
<Callout type='info'>
The Prerequisite for using this API is to have `wxc-wholesale` entitlement or `webex-wholesale-partner-testing` setting enabled for the Partner Organization. The Provisioning Precheck APIs supports two variants of Wholesale Customer Provisioning Precheck Requests. Please refer to [Using the Provisioning Precheck APIs](/docs/api/guides/webex-for-wholesale#using-the-precheck-provisioning-api) section in [Webex for Wholesale](/docs/api/guides/webex-for-wholesale) guide for more information.
</Callout>
</div>

## Parámetros
- `onBehalfOfSubPartnerOrgId` [query] (string): The encoded organization ID for the sub partner.

## Cuerpo de la petición (application/json)
- `provisioningId` (string): Defines how this wholesale customer is to be provisioned for Cisco Webex Services.  Each Customer Template will have its unique Provisioning ID. This ID will be displayed under the chosen Customer Template on Cisco Webex Control Hub.
- `packages` (array): The complete list of Webex Wholesale packages to be assigned to the Wholesale customer.
- `orgId` (string): The organization ID of the enterprise in Cisco Webex.
- `externalId` (string): External ID of the Wholesale customer.
- `address` (object) **(requerido)**: Billing address of the Wholesale customer. (There is a 50 character limit on each address line)
  - `addressLine1` (string) **(requerido)**: Address line 1.
  - `addressLine2` (string): Address line 2.
  - `city` (string) **(requerido)**: Customer's city.
  - `stateOrProvince` (string): State or Province of the Wholesale customer. This attribute may be required in specific geographies. Please refer to [Wholesale Customer Address Requirement](/docs/api/guides/webex-for-wholesale#wholesale-customer-address-requirement) for more information.
  - `zipOrPostalCode` (string): Postal/Zip code of the Wholesale customer. This attribute may be required in specific geographies. Please refer to [Wholesale Customer Address Requirement](/docs/api/guides/webex-for-wholesale#wholesale-customer-address-requirement) for more information.
  - `country` (string) **(requerido)**: ISO2 country code of the Wholesale customer size = 2.
- `customerInfo` (object):
  - `name` (string): The name of the Wholesale customer.
  - `primaryEmail` (string) **(requerido)**: The primary email address of the Wholesale customer.
- `provisioningParameters` (object):
  - `calling` (object):
    - `location` (object) **(requerido)**:
      - `name` (string) **(requerido)**: Name of the wholesale customer office.
      - `address` (object) **(requerido)**: Address of the wholesale customer.(There is a 50 character limit on each address line)
        - `addressLine1` (string) **(requerido)**:
        - `addressLine2` (string):
        - `city` (string) **(requerido)**:
        - `stateOrProvince` (string): State or Province of the Wholesale customer in ISO 3166 format. This attribute may be required in specific geographies. Please refer to [Wholesale Customer Address Requirement](/docs/api/guides/webex-for-wholesale#wholesale-customer-address-requirement) for more information.
        - `zipOrPostalCode` (string): Postal/Zip code of the Wholesale customer. This attribute may be required in specific geographies. Please refer to [Wholesale Customer Address Requirement](/docs/api/guides/webex-for-wholesale#wholesale-customer-address-requirement) for more information.
        - `country` (string) **(requerido)**:
      - `timezone` (string) **(requerido)**: Customer timezone for calling package. The full list of supported timezones can be found at [List of Time Zones for Wholesale Provisioning](https://help.webex.com/en-us/article/nuh0amab/List-of-Time-Zones-for-Wholesale-Provisioning).
      - `language` (string) **(requerido)**: Determine language for all generated emails and voice announcements.
      - `emergencyLocationIdentifier` (string): SIP Header for any emergency calls from this location.
  - `meetings` (object):
    - `timezone` (string): Wholesale Customer timezone for meetings package.
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

### Ejemplo de petición
```json
{
  "address": {
    "addressLine1": "771 Alder Drive",
    "addressLine2": "Cisco Site 5",
    "city": "Milpitas",
    "stateOrProvince": "CA",
    "zipOrPostalCode": "95035",
    "country": "US"
  },
  "customerInfo": {
    "primaryEmail": "john.anderson@acme.com"
  }
}
```

## Respuestas
- **200**: OK
  - `message` (string): A textual representation of the Precheck response message containing the `infoCode` object in the case of a success response and the `errorCode` object in the case of failure.
  - `info` (object): A list of `ProvisioningPreCheckResponseInfo` objects.
    - `infoCode` (number): Provisioning Precheck `infoCode`.
    - `description` (string): A textual description of the `infoCode`.
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
