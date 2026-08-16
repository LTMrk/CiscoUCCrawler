---
doc_id: webex-wholesale-post-wholesale-customers
source: webex-openapi-specs/public-spec/webex-wholesale.json
api: Webex Wholesale
method: POST
path: /wholesale/customers
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.731495+00:00
---

# POST /wholesale/customers

**API:** Webex Wholesale
**Área:** Wholesale Provisioning
**operationId:** `Provision a Wholesale Customer`

## Resumen
Provision a Wholesale Customer

## Descripción
Provision a Wholesale customer for Cisco Webex services.

This API will allow a Service Provider to map the Wholesale customer and assign the required licenses and entitlements for Webex, Calling and Meetings.

The Wholesale customer provisioning is asynchronous and thus a background task is created when this endpoint is invoked.

**packages Note:**

* `cisco_calling_plan` is dependent on: `common_area_calling`, `webex_calling`, `webex_suite`, `webex_voice`, `cx_essentials`, `webex_calling_standard`

* `attendant_console` is dependent on: `webex_calling`, `webex_suite`, `cx_essentials`, `webex_voice`

<div>
        <Callout type='info'>After successful invocation of this endpoint a URL will be returned in the `Location` header, which will point to the [Get a Wholesale Customer](/docs/api/v1/wholesale-provisioning/get-a-wholesale-customer) endpoint for this customer.</Callout>
</div>

## Parámetros
- `onBehalfOfSubPartnerOrgId` [query] (string): The encoded organization ID for the sub partner.

## Cuerpo de la petición (application/json)
- `provisioningId` (string) **(requerido)**: This Provisioning ID defines how this customer is to be provisioned for Webex Services.  Each Customer Template will have their own unique Provisioning ID. This ID will be displayed under the chosen Customer Template on [Webex Control Hub](https://admin.webex.com).
- `packages` (array) **(requerido)**: The complete list of Webex Wholesale packages to be assigned to the customer.
- `orgId` (string): The organization ID of the enterprise in Webex. Mandatory for existing customers.
- `externalId` (string) **(requerido)**: External ID of the Wholesale customer.
- `address` (object) **(requerido)**: Billing Address of the customer. (There is a 50 character limit on each address line)
  - `addressLine1` (string) **(requerido)**: Address line 1.
  - `addressLine2` (string): Address line 2.
  - `city` (string) **(requerido)**: Customer's city.
  - `stateOrProvince` (string): State or Province of the customer. This attribute may be required in specific geographies, please refer to address section in the admin guide for more information.
  - `zipOrPostalCode` (string): Postal/Zip code of the customer. This attribute may be required in specific geographies, please refer to address section in the admin guide for more information.
  - `country` (string) **(requerido)**: ISO2 country code of the customer size = 2. This attribute is used to determine the default Dial In number for the Webex Meeting Sites. Refer to the Address section of [help page](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/wholesale_rtm/wbxbw_b_wholesale-rtm-solution-guide/wbxbw_m_overview-of-webex-wholesale.html#Cisco_Reference.dita_7875bb3e-10c0-4214-8173-7845db31c7a6) for more information.
- `customerInfo` (object): Mandatory for new customer. Optional if Organization ID is provided.
  - `name` (string) **(requerido)**: The name of the Wholesale customer. Name cannot include the "%" character.
  - `primaryEmail` (string) **(requerido)**: The primary email address of the customer.
  - `language` (string): The {ISO-639-1}_{ISO-3166} or {ISO-639-1} locale or language code used as preferred language for organization and Webex Meeting Sites. Refer to the [help page](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/wholesale_rtm/wbxbw_b_wholesale-rtm-solution-guide/wbxbw_m_overview-of-webex-wholesale.html#Cisco_Reference.dita_deb994cb-9c48-4488-b352-54495c54ba1e) for more information.
- `provisioningParameters` (object):
  - `calling` (object): Mandatory when provisioning calling packages.
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
  "provisioningId": "ZjViMzYxODctYzhkZC00NzI3LThiMmYtZjljNDQ3ZjI5MDQ2",
  "packages": [
    "common_area_calling"
  ],
  "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi81MmNmNTc2ZC02MGE4LTQwN2EtYjIyYy00NjdjNTE1OTE5MDg",
  "externalId": "c1677a16-557a-4fb4-b48f-24adde57ec99",
  "address": {
    "addressLine1": "\"771 Alder Drive\"",
    "addressLine2": "\"Cisco Site 5\"",
    "city": "\"Milpitas\"",
    "stateOrProvince": "\"CA\"",
    "zipOrPostalCode": "\"95035\"",
    "country": "\"US\""
  },
  "customerInfo": {
    "name": "\"John's Pizza\"",
    "primaryEmail": "\"john.anderson@acme.com\"",
    "language": "'en'"
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
