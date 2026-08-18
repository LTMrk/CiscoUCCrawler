---
doc_id: webex-device-put-telephony-config-devices-linekeytemplates-templateid
source: webex-openapi-specs/public-spec/webex-device.json
api: Webex Device
api_version: 1.0.0
method: PUT
path: /telephony/config/devices/lineKeyTemplates/{templateId}
operation_id: modifyLineKeyTemplate
tags: Device Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.195650+00:00
---

# PUT /telephony/config/devices/lineKeyTemplates/{templateId}

**API:** Webex Device
**Área:** Device Call Settings
**operationId:** `modifyLineKeyTemplate`

## Resumen
Modify a Line Key Template

## Descripción
Modify a Line Key Template by its template ID in an organization.

Line Keys, also known as Programmable Line Keys (PLK), are the keys found on either side of a typical desk phone display.
A Line Key Template is a definition of actions that will be performed by each of the Line Keys for a particular device model.
This API allows users to modify an existing Line Key Template by its ID in an organization.

Modifying an existing Line Key Template requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `templateId` [path] (string) (**requerido**): Modify line key template with this template ID.
- `orgId` [query] (string): Modify a line key template for this organization.

## Cuerpo de la petición (application/json)
- `userReorderEnabled` (boolean): Indicates whether the user can reorder the line keys.
- `lineKeys` (array) (**requerido**): List of line keys that are being updated.
  - `lineKeyIndex` (number) (**requerido**): An index representing a Line Key. Index starts from 1 representing the first key on the left side of the phone.
  - `lineKeyType` (string) (**requerido**): * `PRIMARY_LINE` - PRIMARY_LINE is the user's primary extension. This is the default assignment for Line Key Index 1 and cannot be modified.  * `SHARED_LINE` - Shows the appearance of other users on the owner's phone.  * `MONITOR` - Enables User and Call Park monitoring.  * `CALL_PARK_EXTENSION` - Enables the configure layout feature in Control Hub to set call park extension implicitly.  * `SPEED_DIAL` - Allows users to reach a telephone number, extension or a SIP URI.  * `OPEN` - An open key will automatically take the configuration of a monitor button starting with the first open key. These buttons are also usable by the user to configure speed dial numbers on these keys.  * `CLOSED` - Button not usable but reserved for future features.  * `MODE_MANAGEMENT` - Allows users to manage call forwarding for features via schedule-based routing. Valores: PRIMARY_LINE, SHARED_LINE, MONITOR, CALL_PARK_EXTENSION, SPEED_DIAL, OPEN, CLOSED, MODE_MANAGEMENT.
  - `lineKeyLabel` (string): This is applicable only when the lineKeyType is `SPEED_DIAL`.
  - `lineKeyValue` (string): Applicable only when the `lineKeyType` is `SPEED_DIAL`. Value must be a valid telephone number, ext, or SIP URI (format: `user@host` using A-Z,a-z,0-9,-_ .+ for `user` and `host`).
  - `sharedLineIndex` (number) (**requerido**): Shared line index is the line label number of the shared or virtual line assigned in the configured lines. Since you can add multiple appearances of the same shared or virtual line on a phone, entering the index number assigns the respective line to a line key. This is applicable only when the `lineKeyType` is SHARED_LINE. `sharedLineIndex` starts at 1 and increments by one for each shared line.

### Ejemplo — petición
```json
{
  "userReorderEnabled": true,
  "lineKeys": [
    {
      "lineKeyIndex": 1,
      "lineKeyType": "PRIMARY_LINE"
    },
    {
      "lineKeyIndex": 2,
      "lineKeyType": "SPEED_DIAL",
      "lineKeyLabel": "Office",
      "lineKeyValue": "4850"
    },
    {
      "lineKeyIndex": 3,
      "lineKeyType": "SHARED_LINE",
      "sharedLineIndex": 1
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/devices/lineKeyTemplates/<templateId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"lineKeys": []}'
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
The Webex Device APIs provide endpoints for managing and monitoring Webex devices, including registration, configuration, status retrieval, workspace assignment, and firmware management. These APIs support automation of device onboarding, health monitoring, remote troubleshooting, and bulk configuration updates. Integration scenarios include custom device dashboards, proactive alerting, and seamless workspace management for meeting rooms and shared spaces. The APIs are essential for IT teams managing large fleets of Webex devices across distributed environments.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs