---
doc_id: webex-cloud-calling-get-telephony-config-virtuallines-virtuallineid-outgoingpermission
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/virtualLines/{virtualLineId}/outgoingPermission
operation_id: Retrieve a Virtual Line's Outgoing Calling Permissions Settings
tags: Virtual Line Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.574130+00:00
---

# GET /telephony/config/virtualLines/{virtualLineId}/outgoingPermission

**API:** Webex Cloud Calling
**Área:** Virtual Line Call Settings
**operationId:** `Retrieve a Virtual Line's Outgoing Calling Permissions Settings`

## Resumen
Retrieve a Virtual Line's Outgoing Calling Permissions Settings

## Descripción
Retrieve a virtual line's Outgoing Calling Permissions settings.

Outgoing calling permissions regulate behavior for calls placed to various destinations and default to the local level settings. You can change the outgoing calling permissions for a virtual line if you want them to be different from your organization's default.

Retrieving the outgoing permission settings for a virtual line requires a full, user, read-only administrator, or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `virtualLineId` [path] (string) (**requerido**): Retrieve settings for a virtual line with the matching ID.
- `orgId` [query] (string): ID of the organization in which the person resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/virtualLines/<virtualLineId>/outgoingPermission' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `useCustomEnabled` (boolean): When true, indicates that this user uses the shared control that applies to all outgoing call settings categories when placing outbound calls.
- `useCustomPermissions` (boolean) (**requerido**): When true, indicates that this user uses the specified outgoing calling permissions when placing outbound calls.
- `callingPermissions` (array) (**requerido**): Specifies the outbound calling permissions settings.
  - `callType` (string): Designates the action to be taken for each call type and if transferring the call type is allowed.  * `INTERNAL_CALL` - Controls calls within your own company.  * `TOLL_FREE` - Controls calls to a telephone number that is billed for all arriving calls instead of incurring charges to the originating caller, usually free of charge from a landline.  * `INTERNATIONAL` - Controls calls to locations outside of the Long Distance areas that require an international calling code before the number is dialed.  * `OPERATOR_ASSISTED` - Controls calls requiring Operator Assistance.  * `CHARGEABLE_DIRECTORY_ASSISTED` - Controls calls to Directory Assistant companies that require a charge to connect the call.  * `SPECIAL_SERVICES_I` - Controls calls to carrier-specific number assignments to special services or destinations.  * `SPECIAL_SERVICES_II` - Controls calls to carrier-specific number assignments to special services or destinations.  * `PREMIUM_SERVICES_I` - Controls calls used to provide information or entertainment for a fee charged directly to the caller.  * `PREMIUM_SERVICES_II` - Controls calls used to provide information or entertainment for a fee charged directly to the caller.  * `NATIONAL` - Controls calls that are within your country of origin, both within and outside of your local area code. Valores: INTERNAL_CALL, TOLL_FREE, INTERNATIONAL, OPERATOR_ASSISTED, CHARGEABLE_DIRECTORY_ASSISTED, SPECIAL_SERVICES_I, SPECIAL_SERVICES_II, PREMIUM_SERVICES_I, PREMIUM_SERVICES_II, NATIONAL.
  - `action` (string): Action on the given `callType`.  * `ALLOW` - Allow the designated call type.  * `BLOCK` - Block the designated call type.  * `AUTH_CODE` - Allow only via Authorization Code.  * `TRANSFER_NUMBER_1` - Transfer to Auto Transfer Number 1. The answering virtual line can then approve the call and send it through or reject the call.  * `TRANSFER_NUMBER_2` - Transfer to Auto Transfer Number 2. The answering virtual line can then approve the call and send it through or reject the call.  * `TRANSFER_NUMBER_3` - Transfer to Auto Transfer Number 3. The answering virtual line can then approve the call and send it through or reject the call. Valores: ALLOW, BLOCK, AUTH_CODE, TRANSFER_NUMBER_1, TRANSFER_NUMBER_2, TRANSFER_NUMBER_3.
  - `transferEnabled` (boolean) (**requerido**): If `true`, allows transfer and forwarding for the call type.
  - `isCallTypeRestrictionEnabled` (boolean) (**requerido**): Indicates if the restriction is enforced by the system for the corresponding call type and cannot be changed. For example, certain call types (such as `INTERNATIONAL`) may be permanently blocked and this field will be `true` to reflect that the restriction is system-controlled and not editable.

### Ejemplo — respuesta 200
```json
{
  "useCustomEnabled": true,
  "useCustomPermissions": true,
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
      "isCallTypeRestrictionEnabled": false
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
      "isCallTypeRestrictionEnabled": false
    },
    {
      "callType": "PREMIUM_SERVICES_II",
      "action": "BLOCK",
      "transferEnabled": false,
      "isCallTypeRestrictionEnabled": true
    },
    {
      "callType": "NATIONAL",
    
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