---
doc_id: webex-cloud-calling-get-telephony-config-premisepstn-trunks-trunkid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/premisePstn/trunks/{trunkId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.556126+00:00
---

# GET /telephony/config/premisePstn/trunks/{trunkId}

**API:** Webex Cloud Calling
**Área:** Call Routing
**operationId:** `Get a Trunk`

## Resumen
Get a Trunk

## Descripción
Get a Trunk for the organization.

A Trunk is a connection between Webex Calling and the premises, which terminates on the premises with a local gateway or other supported device.
The trunk can be assigned to a Route Group - a group of trunks that allow Webex Calling to distribute calls over multiple trunks or to provide redundancy.

Retrieving a trunk requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `trunkId` [path] (string) **(requerido)**: ID of the trunk.
- `orgId` [query] (string): Organization to which trunk belongs.

## Respuestas
- **200**: OK
  - `name` (string) **(requerido)**: A unique name for the trunk.
  - `customer` (object) **(requerido)**:
    - `id` (string) **(requerido)**: ID of the customer/organization.
    - `name` (string) **(requerido)**: Name of the customer/organization.
  - `location` (object): Location associated with the hot desking member.
    - `id` (string) **(requerido)**: Unique identifier for the location.
    - `name` (string) **(requerido)**: Name of the location.
  - `otgDtgId` (string): Unique Outgoing and Destination trunk group associated with the dial plan.
  - `linePort` (string): The Line/Port identifies a device endpoint in standalone mode or a SIP URI public identity in IMS mode.
  - `locationsUsingTrunk` (array): Locations using trunk.
    - `id` (string) **(requerido)**: Unique identifier for the location.
    - `name` (string) **(requerido)**: Name of the location.
  - `pilotUserId` (string): User ID.
  - `outboundProxy` (object): Contains the body of the HTTP response received following the request to Console API and will not be set if the response has no body.
  - `sipAuthenticationUserName` (string): User's authentication service information.
  - `status` (string) **(requerido)**: * `ONLINE` - Device is online  * `OFFLINE` - Device is offline  * `UNKNOWN` - Unknown. Default Valores: ONLINE, OFFLINE, UNKNOWN.
  - `errorCodes` (array): Error codes.
  - `responseStatus` (object):
    - `code` (number) **(requerido)**: Error Code. 25013 for error retrieving the outbound proxy. 25014 for error retrieving the status
    - `type` (string) **(requerido)**: * `ERROR` - Error  * `WARNING` - Warning Valores: ERROR, WARNING.
    - `summaryEnglish` (string) **(requerido)**: Error summary in English.
    - `detail` (array) **(requerido)**: Error Details.
    - `trackingId` (string) **(requerido)**: Error Tracking ID.
  - `dualIdentitySupportEnabled` (boolean): Determines the behavior of the From and PAI headers on outbound calls.
  - `trunkType` (string) **(requerido)**: * `REGISTERING` - For Cisco CUBE Local Gateway.  * `CERTIFICATE_BASED` - For Cisco Unified Border Element, Oracle ACME Session Border Controller, AudioCodes Session Border Controller, Ribbon Session Border Controller. Valores: REGISTERING, CERTIFICATE_BASED.
  - `deviceType` (string): Device type assosiated with trunk.
  - `address` (string): FQDN or SRV address. Required to create a static certificate-based trunk.
  - `domain` (string): Domain name. Required to create a static certificate based trunk.
  - `port` (number) **(requerido)**: FQDN port. Required to create a static certificate-based trunk.
  - `maxConcurrentCalls` (number): Max Concurrent call. Required to create a static certificate based trunk.
  - `isRestrictedToDedicatedInstance` (boolean): Flag to indicate if the trunk is restricted to a dedicated instance.
  - `pChargeInfoSupportPolicy` (string) **(requerido)**: * `DISABLED` - The P-Charge-Info header support policy is disabled.  * `ASSERTED_IDENTITY` - The P-Charge-Info header is always included in outbound PSTN calls using Webex Calling primary number or location’s main number.  * `CONFIGURABLE_CHARGE_NUMBER` - The P-Charge-Info header is included in outbound PSTN calls using the originating or redirecting Webex Calling entity's location charge number if set, else the entity's primary number if set and not toll-free, else the main number of the entity's location if set and not toll-free. If none of these are set or not toll-free, it uses the same number as the ASSERTED_IDENTITY option. Valores: DISABLED, ASSERTED_IDENTITY, CONFIGURABLE_CHARGE_NUMBER.
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
