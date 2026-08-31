---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-huntgroups-alternate-availablenumbers
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/huntGroups/alternate/availableNumbers
operation_id: getHuntGroupAlternateAvailablePhoneNumbers
tags: Features:  Hunt Group
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.283862+00:00
---

# GET /telephony/config/locations/{locationId}/huntGroups/alternate/availableNumbers

**API:** Webex Cloud Calling
**Área:** Features:  Hunt Group
**operationId:** `getHuntGroupAlternateAvailablePhoneNumbers`

## Resumen
Get Hunt Group Alternate Available Phone Numbers

## Descripción
List the service and standard PSTN numbers that are available to be assigned as the hunt group's alternate phone number.
These numbers are associated with the location specified in the request URL, can be active or inactive, and are unassigned.

The available numbers APIs help identify candidate numbers and their owning entities to simplify the assignment or association of these numbers to members or features.

Retrieving this list requires a full, read-only or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Return the list of phone numbers for this location within the given organization. The maximum length is 36.
- `orgId` [query] (string): List numbers for this organization.
- `max` [query] (number): Limit the number of phone numbers returned to this maximum count. The default is 2000.
- `start` [query] (number): Start at the zero-based offset in the list of matching phone numbers. The default is 0.
- `phoneNumber` [query] (array): Filter phone numbers based on the comma-separated list provided in the `phoneNumber` array.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/huntGroups/alternate/availableNumbers' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `phoneNumbers` (array) (**requerido**): Array of phone numbers.
  - `phoneNumber` (string) (**requerido**): A unique identifier for the PSTN phone number.
  - `state` (string) (**requerido**): * `ACTIVE` - Phone number is in the active state.  * `INACTIVE` - Phone number is in the inactive state. Valores: ACTIVE, INACTIVE.
  - `isMainNumber` (boolean) (**requerido**): If `true`, the phone number is used as a location CLID.
  - `tollFreeNumber` (boolean) (**requerido**): If `true`, the phone number is a toll-free number.
  - `telephonyType` (string) (**requerido**): * `PSTN_NUMBER` - The object is a PSTN number. Valores: PSTN_NUMBER.
  - `isServiceNumber` (boolean) (**requerido**): If `true`, the phone number is a service number; otherwise, it is a standard number. Service numbers are high-utilization or high-concurrency PSTN phone numbers that are neither mobile nor toll-free.

### Ejemplo — respuesta 200
```json
{
  "phoneNumbers": [
    {
      "phoneNumber": "+12056350001",
      "state": "ACTIVE",
      "isMainNumber": false,
      "telephonyType": "PSTN_NUMBER",
      "tollFreeNumber": false,
      "isServiceNumber": false
    },
    {
      "phoneNumber": "+12056350002",
      "state": "ACTIVE",
      "isMainNumber": true,
      "telephonyType": "PSTN_NUMBER",
      "tollFreeNumber": false,
      "isServiceNumber": true
    },
    {
      "phoneNumber": "+12056350003",
      "state": "INACTIVE",
      "isMainNumber": false,
      "telephonyType": "PSTN_NUMBER",
      "tollFreeNumber": true,
      "isServiceNumber": false
    }
  ]
}
```

## Respuestas de error
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

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs