---
doc_id: webex-wholesale-post-wholesale-subscribers
source: webex-openapi-specs/public-spec/webex-wholesale.json
api: Webex Wholesale
method: POST
path: /wholesale/subscribers
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.732636+00:00
---

# POST /wholesale/subscribers

**API:** Webex Wholesale
**Área:** Wholesale Provisioning
**operationId:** `Provision a Wholesale Subscriber`

## Resumen
Provision a Wholesale Subscriber

## Descripción
Provision a new Wholesale subscriber for Cisco Webex services.

This API allows a Service Provider to map the Wholesale subscriber to a Cisco Webex Wholesale customer and assign the required licenses and entitlements for Webex, Calling and Meetings.

**Note:**

* If this subscriber is an existing Webex Calling entitled user, the `locationId`, `primaryPhoneNumber` and `extension` are optional and if provided are ignored.

**packages Note:**

* `attendant_console` is dependent on: `webex_calling`, `webex_suite`, `cx_essentials`, `webex_voice`

<div>
<Callout type='info'>
Either `packages` or `package` field is required but not both.
</Callout>
</div>

## Parámetros
- `onBehalfOfSubPartnerOrgId` [query] (string): The encoded organization ID for the sub partner.

## Cuerpo de la petición (application/json)
- `customerId` (string) **(requerido)**: ID of the Provisioned Customer for Webex Wholesale.
- `email` (string) **(requerido)**: The email address of the subscriber (mandatory for the trusted email provisioning flow).
- `package` (string): The Webex Wholesale package to be assigned to the subscriber. **NOTE:** This parameter will be deprecated soon. Please  use `packages` instead.  * `webex_calling` - Calling Basic Package.  * `webex_meetings` - Meetings Package.  * `webex_suite` - Suite Package.  * `webex_voice` - Voice Package.  * `cx_essentials` - Customer Assist Package.  * `webex_calling_standard` - Webex Calling Standard Package. Valores: webex_calling, webex_meetings, webex_suite, webex_voice, cx_essentials, webex_calling_standard.
- `packages` (array): The complete list of Webex Wholesale packages assigned to the subscriber. Currently accepts only one package in the list.
- `provisioningParameters` (object) **(requerido)**:
  - `firstName` (string): The first name of the subscriber.
  - `lastName` (string): The last name of the subscriber.
  - `primaryPhoneNumber` (string): The primary phone number configured for the subscriber. A primary phone number, extension, or both must be supplied when assigning a calling-enabled package, unless the subscriber is an existing Webex Calling entitled user.
  - `extension` (string): The extension configured for the subscriber. An extension, primary phone number or both must be supplied when assigning a calling-enabled package, unless the subscriber is an existing Webex Calling entitled user.
  - `locationId` (string): A unique identifier for the location. This ID should be retrieved via the [List Locations](/docs/api/v1/locations/list-locations) API.

### Ejemplo de petición
```json
{
  "customerId": "ZjViMzYxODctYzhkZC00NzI3LThiMmYtZjljNDQ3ZjI5MDQ2OjQyODVmNTk0LTViNTEtNDdiZS05Mzk2LTZjMzZlMmFkODNhNQ",
  "email": "john.anderson@acme.com",
  "packages": [
    "webex_calling"
  ],
  "provisioningParameters": {
    "firstName": "John",
    "lastName": "Andersen",
    "primaryPhoneNumber": "+12405551212",
    "extension": "51212",
    "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzAxMjM0NTY3LTg5YWItY2RlZi0wMTIzLTQ1Njc4OWFiY2RlZg=="
  }
}
```

## Respuestas
- **200**: OK
  - `id` (string): A unique Cisco identifier for the subscriber.
  - `personId` (string): The person id of the subscriber used in the /people API. Only presented when status is `provisioned`.
  - `email` (string): The email address of the subscriber.
  - `customerId` (string): A unique identifier for the customer.
  - `externalCustomerId` (string): External ID of the Wholesale customer.
  - `package` (string): The Webex Wholesale Package assigned to the subscriber.  * `webex_calling` - Calling Basic Package.  * `webex_meetings` - Meetings Package.  * `webex_suite` - Suite Package.  * `webex_voice` - Voice Package.  * `cx_essentials` - Customer Assist Package.  * `webex_calling_standard` - Webex Calling Standard Package. Valores: webex_calling, webex_meetings, webex_suite, webex_voice, cx_essentials, webex_calling_standard.
  - `packages` (array): The list of Webex Wholesale packages assigned to the subscriber.
  - `status` (string): The provisioning status of the user.  * `provisioned` - The subscriber is fully provisioned on Cisco Webex.  * `pending_user_migration` - The subscriber user migration is pending. Valores: provisioned, pending_user_migration.
  - `errors` (array): List of errors that occurred during that last attempt to provision/update this subscriber.   *Note:*  + This list captures errors that occurred during provisioning of the subscriber.  + Any errors that occur during initial API request validation will be captured directly in error response with appropriate HTTP status code.
    - `errorCode` (number): An error code that identifies the reason for the error.
    - `description` (string): A textual representation of the error code.
  - `created` (string): The date and time the subscriber was provisioned.
  - `lastStatusChange` (string): The date and time the provisioning status of the subscriber last changed.
- **202**: Accepted (returned if an active free account is found, and requires consent based flow to onboard)
  - `id` (string): A unique Cisco identifier for the subscriber.
  - `personId` (string): The person id of the subscriber used in the /people API. Only presented when status is `provisioned`.
  - `email` (string): The email address of the subscriber.
  - `customerId` (string): A unique identifier for the customer.
  - `externalCustomerId` (string): External ID of the Wholesale customer.
  - `package` (string): The Webex Wholesale Package assigned to the subscriber.  * `webex_calling` - Calling Basic Package.  * `webex_meetings` - Meetings Package.  * `webex_suite` - Suite Package.  * `webex_voice` - Voice Package.  * `cx_essentials` - Customer Assist Package.  * `webex_calling_standard` - Webex Calling Standard Package. Valores: webex_calling, webex_meetings, webex_suite, webex_voice, cx_essentials, webex_calling_standard.
  - `packages` (array): The list of Webex Wholesale packages assigned to the subscriber.
  - `status` (string): The provisioning status of the user.  * `provisioned` - The subscriber is fully provisioned on Cisco Webex.  * `pending_user_migration` - The subscriber user migration is pending. Valores: provisioned, pending_user_migration.
  - `errors` (array): List of errors that occurred during that last attempt to provision/update this subscriber.   *Note:*  + This list captures errors that occurred during provisioning of the subscriber.  + Any errors that occur during initial API request validation will be captured directly in error response with appropriate HTTP status code.
    - `errorCode` (number): An error code that identifies the reason for the error.
    - `description` (string): A textual representation of the error code.
  - `created` (string): The date and time the subscriber was provisioned.
  - `lastStatusChange` (string): The date and time the provisioning status of the subscriber last changed.
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
