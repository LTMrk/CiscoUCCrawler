---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/locations/{locationId}
operation_id: Update Location Webex Calling Details
tags: Location Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.061705+00:00
---

# PUT /telephony/config/locations/{locationId}

**API:** Webex Cloud Calling
**Área:** Location Call Settings
**operationId:** `Update Location Webex Calling Details`

## Resumen
Update Location Webex Calling Details

## Descripción
Update Webex Calling details for a location, by ID.

Specifies the location ID in the `locationId` parameter in the URI.

Modifying the `connection` via API is only supported for the local PSTN types of `TRUNK` and `ROUTE_GROUP`.

Updating a location in your organization requires an administrator auth token with the `spark-admin:telephony_config_write` scope.

## Parámetros
- `locationId` [path] (string) (**requerido**): Updating Webex Calling location attributes for this location.
- `orgId` [query] (string): Updating Webex Calling location attributes for this organization.

## Cuerpo de la petición (application/json)
- `announcementLanguage` (string): Location's phone announcement language.
- `callingLineId` (object): Location calling line information.
  - `name` (string): Group calling line ID name. By default the org name.
  - `phoneNumber` (string): Directory Number / Main number in E.164 Format.
- `connection` (object): Connection details can only be modified to and from local PSTN types of `TRUNK` and `ROUTE_GROUP`.
  - `type` (string): * `ROUTE_GROUP` - Route group must include at least one trunk with a maximum of 10 trunks per route group.  * `TRUNK` - Connection between Webex Calling and the premises. Valores: ROUTE_GROUP, TRUNK.
  - `id` (string): A unique identifier of route type.
- `externalCallerIdName` (string): External caller ID name value. Unicode characters.
- `pAccessNetworkInfo` (string): Emergency Location Identifier for a location. The `pAccessNetworkInfo` is set only when the location's country is Belgium(`BE`), Germany(`DE`), or France(`FR`).
- `outsideDialDigit` (string): Must dial to reach an outside line. Default is none.
- `enforceOutsideDialDigit` (boolean): True when enforcing outside dial digit at location level to make PSTN calls.
- `routingPrefix` (string): Must dial a prefix when calling between locations having same extension within same location, should be numeric.
- `chargeNumber` (string): Set the chargeable number for the line placing the call.  When set and [useChargeNumberForPChargeInfo field (GET location)](/docs/api/v1/beta-location-call-settings-with-p-charge-info-support/get-location-webex-calling-details) is true for the location, all PSTN calls placed from this location will include a P-Charge-Info header with this specified number in the SIP INVITE.

### Ejemplo — petición
```json
{
  "announcementLanguage": "fr_fr",
  "outsideDialDigit": "12",
  "routingPrefix": "212",
  "callingLineId": {
    "name": "Denver Incoming",
    "phoneNumber": "+12145555698"
  },
  "connection": {
    "type": "TRUNK",
    "id": "Y2lzY29zcGFyazovL3VzL1RSVU5LL2M1MGIxZjY2LTRjODMtNDAzNy04NjM1LTg2ZjlkM2VkZDQ5MQ"
  },
  "externalCallerIdName": "Big Corp-Denver",
  "pAccessNetworkInfo": "Richardson-TX",
  "chargeNumber": "+14158952369",
  "enforceOutsideDialDigit": true
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/locations/<locationId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: OK
- `batchJobId` (string): Admin Batch Job ID returned if a routing prefix change occurs.
- `failureReason` (string): Error message if the admin batch job is not triggered if a routing prefix change occurs.

### Ejemplo — respuesta 200
```json
{
  "batchJobId": "Y2lzY29zcGFyazovL3VzL0pPQl9JRC8wOThmNTg5MC05MTA4LTQ0YWMtODIxMy1lYmE4MGI4YzJkMjA"
}
```
**204**: No Content
**206**: Partial Content
- `batchJobId` (string): Admin Batch Job ID returned if a routing prefix change occurs.
- `failureReason` (string): Error message if the admin batch job is not triggered if a routing prefix change occurs.

### Ejemplo — respuesta 206
```json
{
  "failureReason": "UpdateRoutingPrefix batch job not triggered for Location: c7e4wasdfgjfec5c52. OldRoutingPrefix : 111. NewRoutingPrefix: 212."
}
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **409**: Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
  Ejemplo:
```json
{
  "failureReason": "UpdateRoutingPrefixJob failed as another one is already in progress."
}
```
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