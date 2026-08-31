---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-outgoingpermission
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/outgoingPermission
operation_id: Get Location Outgoing Permission
tags: Location Call Settings: Call Handling
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.302318+00:00
---

# GET /telephony/config/locations/{locationId}/outgoingPermission

**API:** Webex Cloud Calling
**Área:** Location Call Settings: Call Handling
**operationId:** `Get Location Outgoing Permission`

## Resumen
Get Location Outgoing Permission

## Descripción
Retrieve the location's outgoing call settings.

A location's outgoing call settings allow you to determine the types of calls the people/workspaces at the location are allowed to make, as well as configure the default calling permission for each call type at the location.

Retrieving a location's outgoing call settings requires a full, user or read-only administrator or location administrator auth token with a scope of spark-admin:telephony_config_read.

## Parámetros
- `locationId` [path] (string) (**requerido**): Retrieve outgoing call settings for this location.
- `orgId` [query] (string): Retrieve outgoing call settings for this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/outgoingPermission' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `callingPermissions` (array): Array of calling permissions.
  - `callType` (string) (**requerido**): Below are the call type values.  * `INTERNAL_CALL` - Controls calls within your own company.  * `TOLL_FREE` - Controls calls to a telephone number that is billed for all arriving calls instead of incurring charges to the originating caller, usually free of charge from a landline.  * `INTERNATIONAL` - Controls calls to locations outside of the Long Distance areas that require an international calling code before the number is dialed.  * `OPERATOR_ASSISTED` - Controls calls requiring Operator Assistance.  * `CHARGEABLE_DIRECTORY_ASSISTED` - Controls calls to Directory Assistant companies that require a charge to connect the call.  * `SPECIAL_SERVICES_I` - Controls calls to carrier-specific number assignments to special services or destinations.  * `SPECIAL_SERVICES_II` - Controls calls to carrier-specific number assignments to special services or destinations.  * `PREMIUM_SERVICES_I` - Controls calls used to provide information or entertainment for a fee charged directly to the caller.  * `PREMIUM_SERVICES_II` - Controls calls used to provide information or entertainment for a fee charged directly to the caller.  * `NATIONAL` - Controls calls that are National. Valores: INTERNAL_CALL, TOLL_FREE, INTERNATIONAL, OPERATOR_ASSISTED, CHARGEABLE_DIRECTORY_ASSISTED, SPECIAL_SERVICES_I, SPECIAL_SERVICES_II, PREMIUM_SERVICES_I, PREMIUM_SERVICES_II, NATIONAL.
  - `action` (string) (**requerido**): Allows to configure settings for each call type.  * `ALLOW` - Callers at this location can make these types of calls.  * `BLOCK` - Callers at this location can't make these types of calls.  * `AUTH_CODE` - Callers must enter the authorization code that you set before placing an outgoing call.  * `TRANSFER_NUMBER_1` - Calls are transferred automatically to the configured auto transfer number `autoTransferNumber1`.  * `TRANSFER_NUMBER_2` - Calls are transferred automatically to the configured auto transfer number. `autoTransferNumber2`.  * `TRANSFER_NUMBER_3` - Calls are transferred automatically to the configured auto transfer number. `autoTransferNumber3`. Valores: ALLOW, BLOCK, AUTH_CODE, TRANSFER_NUMBER_1, TRANSFER_NUMBER_2, TRANSFER_NUMBER_3.
  - `transferEnabled` (boolean) (**requerido**): If `true`, allows transfer and forwarding for the call type.
  - `isCallTypeRestrictionEnabled` (boolean) (**requerido**): Indicates if the restriction is enforced by the system for the corresponding call type and cannot be changed. For example, certain call types (such as `INTERNATIONAL`) may be permanently blocked and this field will be `true` to reflect that the restriction is system-controlled and not editable.

### Ejemplo — respuesta 200
```json
{
  "callingPermissions": [
    {
      "callType": "INTERNAL_CALL",
      "action": "ALLOW",
      "transferEnabled": true,
      "isCallTypeRestrictionEnabled": false
    },
    {
      "callType": "TOLL_FREE",
      "action": "ALLOW",
      "transferEnabled": true,
      "isCallTypeRestrictionEnabled": false
    },
    {
      "callType": "INTERNATIONAL",
      "action": "BLOCK",
      "transferEnabled": false,
      "isCallTypeRestrictionEnabled": true
    },
    {
      "callType": "OPERATOR_ASSISTED",
      "action": "ALLOW",
      "transferEnabled": true,
      "isCallTypeRestrictionEnabled": false
    },
    {
      "callType": "CHARGEABLE_DIRECTORY_ASSISTED",
      "action": "BLOCK",
      "transferEnabled": true,
      "isCallTypeRestrictionEnabled": false
    },
    {
      "callType": "SPECIAL_SERVICES_I",
      "action": "ALLOW",
      "transferEnabled": true,
      "isCallTypeRestrictionEnabled": false
    },
    {
      "callType": "SPECIAL_SERVICES_II",
      "action": "ALLOW",
      "transferEnabled": true,
      "isCallTypeRestrictionEnabled": false
    },
    {
      "callType": "PREMIUM_SERVICES_I",
      "action": "BLOCK",
      "transferEnabled": false,
      "isCallTypeRestrictionEnabled": true
    },
    {
      "callType": "PREMIUM_SERVICES_II",
      "action": "BLOCK",
      "transferEnabled": false,
      "isCallTypeRestrictionEnabled": true
    },
    {
      "callType": "NATIONAL",
      "action": "ALLOW",
      "transferEnabled": true,
      "isC
  ... (truncado)
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