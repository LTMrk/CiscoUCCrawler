---
doc_id: webex-admin-patch-licenses-users
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
method: PATCH
path: /licenses/users
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.151730+00:00
---

# PATCH /licenses/users

**API:** Webex Admin
**Área:** Licenses
**operationId:** `Assign_Licenses_to_Users`

## Resumen
Assign Licenses to Users

## Descripción
Assign licenses and attendee `siteUrls` to existing users. Only an admin can assign licenses. Only existing users can be assigned a license. Assign meeting licenses to users outside your organization (Status will be pending until the user accepts the invite)

At least one of the following body parameters is required to assign license to the user: `email`, `personId`. For Calling license assignment, properties `phoneNumber` or `extension` are required. If `phoneNumber` is not provided then `locationId` is mandatory.

When assigning licenses and attendee siteUrls to a user who does not belong to the organization, the licenses and siteUrls remain in pending state until the user accepts them. The `pendingLicenses` and `pendingSiteUrls` are part of the response.

## Cuerpo de la petición (application/json)
- `email` (string): Email address of the user.
- `personId` (string): A unique identifier for the user.
- `orgId` (string): The ID of the organization to which the licenses and siteUrls belong. If not specified, the organization ID from the OAuth token is used.
- `licenses` (array): An array of licenses to be assigned to the user.
  - `id` (string) **(requerido)**: A unique identifier for the license.
  - `operation` (string): Operation type. The default operation is `add` if no operation is specified.  * `remove` - Remove the license from the user  * `add` - Assign the license to the user Valores: remove, add.
  - `properties` (object):
    - `locationId` (string): The ID of the location for this user. Applicable to Webex Calling license.
    - `phoneNumber` (string): Work phone number for the user. Applicable to Webex Calling license.
    - `extension` (string): Webex Calling extension of the user. Applicable to Webex Calling license.
- `siteUrls` (array): An array of siteUrls to be assigned to the user.
  - `siteUrl` (string) **(requerido)**: Attendee access on the site.
  - `accountType` (string) **(requerido)**: Account type. Only `attendee` type is supported. For host account, remove attendee and assign the license on that site.  * `attendee` - Attendee role on the siteUrl Valores: attendee.
  - `operation` (string): Operation type. The default operation is `add` if no operation is specified.  * `remove` - Remove the attendee role from the user.  * `add` - Add the attendee role to the user. Valores: remove, add.

### Ejemplo de petición
```json
{
  "email": "john.andersen@example.com",
  "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
  "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
  "licenses": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0xJQ0VOU0UvOTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh",
      "operation": "add",
      "properties": {
        "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzYzNzE1",
        "phoneNumber": "+14085267209",
        "extension": "133"
      }
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0xJQ0VOU0UvOTZhYmMyYWEtM2RjYy0xMWU1LTU2eTctMGY0NTU2YWRleWhu",
      "operation": "remove"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0xJQ0VOU0UvOTZhYmMyYWEtM2RjYy0xMWU1LTIzNDItMGY0NTU2YWRlZXJm",
      "operation": "add"
    }
  ],
  "siteUrls": [
    {
      "siteUrl": "mysite.webex.com",
      "accountType": "attendee",
      "operation": "add"
    }
  ]
}
```

## Respuestas
- **200**: OK
  - `orgId` (string): The ID of the organization to which this user belongs.
  - `personId` (string): A unique identifier for the user.
  - `email` (string): The email address of this user.
  - `licenses` (array): An array of license strings that are assigned to this user.
  - `siteUrls` (array): An array of `siteUrls` and their `accountType` that are assigned to this user.
    - `siteUrl` (string): `siteUrl` assigned to the user.
    - `accountType` (string): Account Type of the site.  * `attendee` - Attendee account on the site.  * `host` - Host account on the site. Valores: attendee, host.
  - `pendingLicenses` (array): An array of license strings that are in pending state. This is only applicable to users outside the organization.
  - `pendingSiteUrls` (array): An array of `siteUrls` and their `accountType` that are in pending state. This is only applicable to users outside the organization.
    - `siteUrl` (string): `siteUrl` assigned to the user.
    - `accountType` (string): Account Type of the site.  * `attendee` - Attendee account on the site.  * `host` - Host account on the site. Valores: attendee, host.
- **206**: Partial Content: Some licenses were successfully assigned, but others could not be assigned due to various constraints or errors. Compare the returned licenses with the requested licenses to determine which ones failed.
  - `orgId` (string): The ID of the organization to which this user belongs.
  - `personId` (string): A unique identifier for the user.
  - `email` (string): The email address of this user.
  - `licenses` (array): An array of license strings that are assigned to this user.
  - `siteUrls` (array): An array of `siteUrls` and their `accountType` that are assigned to this user.
    - `siteUrl` (string): `siteUrl` assigned to the user.
    - `accountType` (string): Account Type of the site.  * `attendee` - Attendee account on the site.  * `host` - Host account on the site. Valores: attendee, host.
  - `pendingLicenses` (array): An array of license strings that are in pending state. This is only applicable to users outside the organization.
  - `pendingSiteUrls` (array): An array of `siteUrls` and their `accountType` that are in pending state. This is only applicable to users outside the organization.
    - `siteUrl` (string): `siteUrl` assigned to the user.
    - `accountType` (string): Account Type of the site.  * `attendee` - Attendee account on the site.  * `host` - Host account on the site. Valores: attendee, host.
- **400**: Bad Request: The request was invalid or cannot be otherwise served. Specific error codes indicate license assignment issues.
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
