---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}
operation_id: Get Location Webex Calling Details
tags: Location Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.293409+00:00
---

# GET /telephony/config/locations/{locationId}

**API:** Webex Cloud Calling
**Área:** Location Call Settings
**operationId:** `Get Location Webex Calling Details`

## Resumen
Get Location Webex Calling Details

## Descripción
Shows Webex Calling details for a location, by ID.

Specifies the location ID in the locationId parameter in the URI.

Searching and viewing locations in your organization requires an administrator auth token with the spark-admin:telephony_config_read scope.

## Parámetros
- `locationId` [path] (string) (**requerido**): Retrieve Webex Calling location attributes for this location.
- `orgId` [query] (string): Retrieve Webex Calling location attributes for this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): A unique identifier for the location.
- `name` (string) (**requerido**): The name of the location.
- `announcementLanguage` (string) (**requerido**): Location's phone announcement language.
- `callingLineId` (object) (**requerido**): Location calling line information.
  - `name` (string) (**requerido**): Group calling line ID name. By default the Org name.
  - `phoneNumber` (string) (**requerido**): Directory Number / Main number in E.164 Format.
- `connection` (object) (**requerido**): Connection details are only returned for local PSTN types of `TRUNK` or `ROUTE_GROUP`.
  - `type` (string) (**requerido**): * `ROUTE_GROUP` - Route group must include at least one trunk with a maximum of 10 trunks per route group.  * `TRUNK` - Connection between Webex Calling and the premises. Valores: ROUTE_GROUP, TRUNK.
  - `id` (string) (**requerido**): A unique identifier of route type.
- `subscriptionId` (string): PSTN connection ID given for locations with a PSTN subscription.
- `externalCallerIdName` (string) (**requerido**): External Caller ID Name value. Unicode characters.
- `userLimit` (number) (**requerido**): Limit on the number of people at the location. Read-Only.
- `pAccessNetworkInfo` (string): Emergency Location Identifier for a location. Set this field to provide the SIP access network information to the provider which will be used to populate the SIP P-Access-Network-Info header. This is helpful to establish the location of a device when you make an emergency call.
- `outsideDialDigit` (string) (**requerido**): Must dial to reach an outside line, default is None.
- `enforceOutsideDialDigit` (boolean): True when enforcing outside dial digit at location level to make PSTN calls.
- `routingPrefix` (string) (**requerido**): Must dial a prefix when calling between locations having same extension within same location.
- `defaultDomain` (string) (**requerido**): IP Address, hostname, or domain. Read-Only.
- `chargeNumber` (string): Chargeable number for the line placing the call. When set and useChargeNumberForPChargeInfo is true, all PSTN calls placed from this location will include a P-Charge-Info header with this specified number in the SIP INVITE.
- `useChargeNumberForPChargeInfo` (boolean): Indicates whether the location's chargeNumber (if set) is enabled for use as the P-Charge-Info header in the SIP INVITE for all PSTN calls placed from this location. The field is returned as true if the location's PSTN allows use of the chargeNumber.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OL2M5N2VlMDQ5LTM1OWItNGM3OC04NDU0LTA1OGMyZWRlMjU2Mw",
  "name": "Denver",
  "announcementLanguage": "fr_fr",
  "routingPrefix": "2",
  "callingLineId": {
    "name": "Denver Incoming",
    "phoneNumber": "+12145555698"
  },
  "connection": {
    "type": "TRUNK",
    "id": "Y2lzY29zcGFyazovL3VzL1RSVU5LL2M1MGIxZjY2LTRjODMtNDAzNy04NjM1LTg2ZjlkM2VkZDQ5MQ"
  },
  "subscriptionId": "trial",
  "externalCallerIdName": "Big Corp-Denver",
  "userLimit": 500000,
  "outsideDialDigit": "12",
  "pAccessNetworkInfo": "Richardson-TX",
  "defaultDomain": "98079822.int10.bcld.webex.com",
  "chargeNumber": "+14158952369",
  "enforceOutsideDialDigit": true,
  "useChargeNumberForPChargeInfo": true
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