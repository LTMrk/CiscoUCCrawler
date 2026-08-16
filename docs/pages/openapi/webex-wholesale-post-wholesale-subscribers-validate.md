---
doc_id: webex-wholesale-post-wholesale-subscribers-validate
source: webex-openapi-specs/public-spec/webex-wholesale.json
api: Webex Wholesale
method: POST
path: /wholesale/subscribers/validate
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.733139+00:00
---

# POST /wholesale/subscribers/validate

**API:** Webex Wholesale
**Área:** Wholesale Provisioning
**operationId:** `Precheck a Wholesale Subscriber Provisioning`

## Resumen
Precheck a Wholesale Subscriber Provisioning

## Descripción
Allows the Partner sales team to verify likely success of provisioning a wholesale subscriber.
**packages Note:**

* `attendant_console` is dependent on: `webex_calling`, `webex_suite`, `cx_essentials`, `webex_voice`

<div>
<Callout type='info'>
The Prerequisite for using this API is to have `wxc-wholesale` entitlement or `webex-wholesale-partner-testing` setting enabled for the Partner Organization. The Provisioning Precheck APIs supports three variants of Wholesale Subscriber Provisioning Precheck Requests. Please refer to [Using the Provisioning Precheck API](/docs/api/guides/webex-for-wholesale#using-the-precheck-provisioning-api) section in [Webex for Wholesale](/docs/api/guides/webex-for-wholesale) guide for more information.
</Callout>
</div>

<div>
<Callout type='info'>
Either `packages` or `package` field is required but not both.
</Callout>
</div>

## Parámetros
- `onBehalfOfSubPartnerOrgId` [query] (string): The encoded organization ID for the sub partner.

## Cuerpo de la petición (application/json)
- `provisioningId` (string): Defines how this wholesale subscriber is to be provisioned for Cisco Webex Services.  Each Customer template has its unique provisioning ID. This ID is displayed under the chosen customer template on Cisco Webex Control Hub.
- `customerId` (string): ID of the Provisioned Customer for Webex Wholesale.
- `email` (string) **(requerido)**: The email address of the subscriber.
- `package` (string): The Webex Wholesale package to be assigned to the subscriber. **NOTE:** This parameter will be deprecated soon. Please  use `packages` instead.  * `webex_calling` - Calling Basic Package.  * `webex_meetings` - Meetings Package.  * `webex_suite` - Suite Package.  * `webex_voice` - Voice Package.  * `cx_essentials` - Customer Assist Package.  * `webex_calling_standard` - Webex Calling Standard Package. Valores: webex_calling, webex_meetings, webex_suite, webex_voice, cx_essentials, webex_calling_standard.
- `packages` (array): The complete list of Webex Wholesale packages assigned to the subscriber. Currently accepts only one package in the list.
- `provisioningParameters` (object):
  - `firstName` (string): The first name of the subscriber.
  - `lastName` (string): The last name of the subscriber.
  - `primaryPhoneNumber` (string): The primary phone number configured for the subscriber.
  - `extension` (string): The extension configured for the subscriber. An extension, primary phone number or both must be supplied when creating a subscriber.
  - `locationId` (string): A unique identifier for the location. This ID should be retrieved via the Locations API - List Locations.
- `customerInfo` (object):
  - `primaryEmail` (string) **(requerido)**: The primary email address of the customer.

### Ejemplo de petición
```json
{
  "customerId": "ZjViMzYxODctYzhkZC00NzI3LThiMmYtZjljNDQ3ZjI5MDQ2OjQyODVmNTk0LTViNTEtNDdiZS05Mzk2LTZjMzZlMmFkODNhNQ",
  "email": "alice.anderson@acme.com"
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
