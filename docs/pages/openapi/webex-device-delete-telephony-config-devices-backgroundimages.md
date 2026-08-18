---
doc_id: webex-device-delete-telephony-config-devices-backgroundimages
source: webex-openapi-specs/public-spec/webex-device.json
api: Webex Device
api_version: 1.0.0
method: DELETE
path: /telephony/config/devices/backgroundImages
operation_id: deleteDeviceBackgroundImages
tags: Device Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.202569+00:00
---

# DELETE /telephony/config/devices/backgroundImages

**API:** Webex Device
**Área:** Device Call Settings
**operationId:** `deleteDeviceBackgroundImages`

## Resumen
Delete Device Background Images

## Descripción
Delete the list of designated device background images for an organization. Maximum is 10 images per request.

Deleting a device background image requires a full or device administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `orgId` [query] (string): Deletes the list of images in this organization.

## Cuerpo de la petición (application/json)
- `backgroundImages` (array) (**requerido**): Array of images to be deleted.
  - `fileName` (string) (**requerido**): The name of the image file to be deleted.
  - `forceDelete` (boolean): Flag to force delete the image. When `forceDelete` = true, if any device, location, or org level custom background URL is configured with the `backgroundImageURL` containing the filename being deleted, the background image is set to `None`.

### Ejemplo — petición
```json
{
  "backgroundImages": [
    {
      "fileName": "CompanyLogoBlue",
      "forceDelete": true
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X DELETE '/telephony/config/devices/backgroundImages' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"backgroundImages": []}'
```

## Respuestas correctas
**200**: OK
- `items` (array) (**requerido**): Array of deleted images.
  - `fileName` (string) (**requerido**): The name of the image file.
  - `result` (object) (**requerido**): The result of the deletion.
    - `status` (number) (**requerido**): The status of the deletion.
- `count` (string): The total number of images in the org after deletion.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "fileName": "CompanyLogoBlue",
      "result": {
        "status": 200
      }
    }
  ],
  "count": 2
}
```
**206**: Partial Content
- `items` (array) (**requerido**): Array of deleted images.
  - `fileName` (string) (**requerido**): The name of the image file.
  - `result` (object) (**requerido**): The result of the deletion.
    - `status` (number) (**requerido**): The status of the deletion.
    - `error` (object): The error message if the deletion failed.
      - `message` (string) (**requerido**): The error message.
      - `errorCode` (number) (**requerido**): The error code.
- `count` (string): The total number of images in the org after deletion.

### Ejemplo — respuesta 206
```json
{
  "items": [
    {
      "fileName": "CompanyLogoBlue",
      "result": {
        "status": 200
      }
    },
    {
      "fileName": "CompanyLogoRed",
      "result": {
        "status": 400,
        "error": {
          "message": "The image could not be deleted.",
          "errorCode": 4305
        }
      }
    }
  ],
  "count": 2
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
The Webex Device APIs provide endpoints for managing and monitoring Webex devices, including registration, configuration, status retrieval, workspace assignment, and firmware management. These APIs support automation of device onboarding, health monitoring, remote troubleshooting, and bulk configuration updates. Integration scenarios include custom device dashboards, proactive alerting, and seamless workspace management for meeting rooms and shared spaces. The APIs are essential for IT teams managing large fleets of Webex devices across distributed environments.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs