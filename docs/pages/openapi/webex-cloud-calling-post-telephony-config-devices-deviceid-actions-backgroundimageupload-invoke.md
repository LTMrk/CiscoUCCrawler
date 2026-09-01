---
doc_id: webex-cloud-calling-post-telephony-config-devices-deviceid-actions-backgroundimageupload-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/devices/{deviceId}/actions/backgroundImageUpload/invoke
operation_id: uploadADeviceBackgroundImage
tags: Device Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.665703+00:00
---

# POST /telephony/config/devices/{deviceId}/actions/backgroundImageUpload/invoke

**API:** Webex Cloud Calling
**Área:** Device Call Settings
**operationId:** `uploadADeviceBackgroundImage`

## Resumen
Upload a Device Background Image

## Descripción
Configure a device's background image by uploading an image with file format, `.jpeg` or `.png`, encoded image file. Maximum image file size allowed to upload is 625 KB.

The request must be a multipart/form-data request rather than JSON, using the image/jpeg or image/png content-type.

Webex Calling supports the upload of up to 100 background image files for each org. These image files can then be referenced by MPP phones in that org for use as their background image.

Uploading a device background image requires a full or device administrator auth token with a scope of `spark-admin:telephony_config_write`.

**WARNING:** This API is not callable using the developer portal web interface due to the lack of support for multipart POST. This API can be utilized using other tools that support multipart POST, such as Postman.

## Parámetros
- `deviceId` [path] (string) (**requerido**): Unique identifier for the device.
- `orgId` [query] (string): Uploads the image in this organization.

## Cuerpo de la petición (multipart/form-data)
- `file` (string/binary) (**requerido**): The image file to upload. Must be in `.jpeg` or `.png` format. Maximum file size is 625 KB.
- `fileName` (string) (**requerido**): The name of the image file being uploaded.

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/devices/<deviceId>/actions/backgroundImageUpload/invoke' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"file": "<file>", "fileName": "<fileName>"}'
```

## Respuestas correctas
**201**: Created
- `filename` (string): The name of the uploaded image file.
- `backgroundImageUrl` (string): The URL of the uploaded image file.
- `count` (string): The total number of images in the org after uploading.

### Ejemplo — respuesta 201
```json
{
  "filename": "CompanyLogoBlue",
  "backgroundImageUrl": "\"/dms/Cisco_Phone_Background/background001\"",
  "count": "2"
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