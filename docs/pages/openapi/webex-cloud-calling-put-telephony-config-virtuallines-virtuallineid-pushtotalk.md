---
doc_id: webex-cloud-calling-put-telephony-config-virtuallines-virtuallineid-pushtotalk
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: PUT
path: /telephony/config/virtualLines/{virtualLineId}/pushToTalk
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.661737+00:00
---

# PUT /telephony/config/virtualLines/{virtualLineId}/pushToTalk

**API:** Webex Cloud Calling
**Área:** Virtual Line Call Settings
**operationId:** `Configure Push-to-Talk Settings for a Virtual Line`

## Resumen
Configure Push-to-Talk Settings for a Virtual Line

## Descripción
Configure a virtual line's Push-to-Talk settings.

Push-to-Talk allows the use of desk phones as either a one-way or two-way intercom that connects people in different parts of your organization.

Updating the Push-to-Talk settings for a virtual line requires a full, user, or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `virtualLineId` [path] (string) **(requerido)**: Retrieve settings for a virtual line with the matching ID.
- `orgId` [query] (string): ID of the organization in which the virtual line resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.

## Cuerpo de la petición (application/json)
- `allowAutoAnswer` (boolean): `true` if Push-to-Talk feature is enabled.
- `connectionType` (string): * `ONE_WAY` - Push-to-Talk initiators can chat with this workspace but only in one direction. The workspace you enable Push-to-Talk for cannot respond.  * `TWO_WAY` - Push-to-Talk initiators can chat with this workspace in a two-way conversation. The workspace you enable Push-to-Talk for can respond. Valores: ONE_WAY, TWO_WAY.
- `accessType` (string): * `ALLOW_MEMBERS` - List of people/workspaces that are allowed to use the Push-to-Talk feature to interact with the workspace being configured.  * `BLOCK_MEMBERS` - List of people/workspaces that are disallowed to interact using the Push-to-Talk feature with the workspace being configured. Valores: ALLOW_MEMBERS, BLOCK_MEMBERS.
- `members` (array): List of people that are allowed or disallowed to interact using the Push-to-Talk feature.

### Ejemplo de petición
```json
{
  "allowAutoAnswer": true,
  "connectionType": "ONE_WAY",
  "accessType": "ALLOW_MEMBERS",
  "members": [
    "Y2lzY29zcGFyazovL3VzL1BFT1BMRS82MWU3MDlkNy1hM2IxLTQ2MDctOTBiOC04NmE5MDgxYWFkNmE",
    "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jMTQzMzhkNS02YTdjLTRiZjYtOTFiMS0zYmM2ZWMzMGJiMTE"
  ]
}
```

## Respuestas
- **204**: No Content
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
