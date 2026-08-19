---
doc_id: webex-cloud-calling-put-telephony-config-workspaces-workspaceid-emergencycallbacknumber
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/workspaces/{workspaceId}/emergencyCallbackNumber
operation_id: Update a Workspace Emergency Callback Number
tags: Emergency Services Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.012278+00:00
---

# PUT /telephony/config/workspaces/{workspaceId}/emergencyCallbackNumber

**API:** Webex Cloud Calling
**Área:** Emergency Services Settings
**operationId:** `Update a Workspace Emergency Callback Number`

## Resumen
Update a Workspace Emergency Callback Number

## Descripción
Update the emergency callback number settings for a workspace.

Emergency Callback Configurations can be enabled at the organization level, Users without individual telephone numbers, such as extension-only users, must be set up with accurate Emergency Call Back Numbers (ECBN) to enable them to make emergency calls. These users can either utilize the default ECBN for their location or be assigned another specific telephone number from that location for emergency purposes.

To update an emergency callback number requires a full, location, user, or read-only administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Updating Emergency Callback Number attributes for this workspace.
- `orgId` [query] (string): Updating Emergency Callback Number attributes for this organization.

## Cuerpo de la petición (application/json)
- `selected` (string): * `DIRECT_LINE` - Returned calls from the Public Safety Answering Point go directly to the member. The Emergency Service Address configured by the PSTN to the member's phone is specific to the member’s location.  * `LOCATION_ECBN` - Each location can have an ECBN configured that is different from the location’s main number. Location Default ECBN is typically configured for users without dedicated telephone numbers or with only an extension.  * `LOCATION_MEMBER_NUMBER` - Configure one user with another user’s telephone number as an ECBN. This option is used in place of a location’s main number when the location has multiple floors or buildings. This allows the ECBN assigned to have a more accurate Emergency Service Address associated with it. Valores: DIRECT_LINE, LOCATION_ECBN, LOCATION_MEMBER_NUMBER.
- `locationMemberId` (string): Member ID of person/workspace/virtual line/hunt group within the location. Required when `selected` is `LOCATION_MEMBER_NUMBER`.
- `elinEnabled` (boolean): Indicates whether this workspace is allowed to use an Emergency Location Identification Number (ELIN) for emergency calls made from one of its devices.

### Ejemplo — petición
```json
{
  "selected": "LOCATION_MEMBER_NUMBER",
  "locationMemberId": "Y2lzY29zcGFyazovL3VzL1BMQUNFLzExYTNmOTkwLWE2ODktNDc3ZC1iZTZiLTcxMjAwMjVkOGFiYg",
  "elinEnabled": true
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/workspaces/<workspaceId>/emergencyCallbackNumber' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**204**: No Content

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