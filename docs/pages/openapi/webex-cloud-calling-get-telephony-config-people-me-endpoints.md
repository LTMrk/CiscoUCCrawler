---
doc_id: webex-cloud-calling-get-telephony-config-people-me-endpoints
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/me/endpoints
operation_id: getMyEndpointsList
tags: Call Settings For Me
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.576497+00:00
---

# GET /telephony/config/people/me/endpoints

**API:** Webex Cloud Calling
**Área:** Call Settings For Me
**operationId:** `getMyEndpointsList`

## Resumen
Read the List of My Endpoints

## Descripción
Retrieve the list of endpoints associated with the authenticated user.

Endpoints are devices, applications, or hotdesking guest profiles. Endpoints can be owned by an authenticated user or have the user as a secondary line.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/me/endpoints' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `endpoints` (array) (**requerido**): List of endpoints.
  - `id` (string) (**requerido**): Unique identifier of the endpoint.
  - `type` (string) (**requerido**): * `CALLING_DEVICE` - Endpoint is a calling device.  * `APPLICATION` - Endpoint is an application.  * `HOTDESKING_GUEST` - Endpoint is a hotdesking guest. Valores: CALLING_DEVICE, APPLICATION, HOTDESKING_GUEST.
  - `name` (string) (**requerido**): Display name of the endpoint.
  - `autoAndForcedAnswerEnabled` (boolean) (**requerido**): If `true`, the endpoint can be remotely controlled, allowing actions such as mute, hold, resume and answer.
  - `ownerId` (string) (**requerido**): Unique identifier of the endpoint owner.
  - `ownerType` (string) (**requerido**): * `PEOPLE` - Indicates the associated member is a person.  * `PLACE` - Indicates the associated member is a workspace. Valores: PEOPLE, PLACE.
  - `secondaryLines` (array): List of secondary lines. The secondary line information is not returned for the endpoint owned by an entity other than the authenticated user.
    - `id` (string) (**requerido**): Unique identifier for the member.
    - `memberType` (string) (**requerido**): * `PEOPLE` - Indicates the associated member is a person.  * `PLACE` - Indicates the associated member is a workspace. Valores: PEOPLE, PLACE.
  - `mobilitySettings` (object): Mobility settings of the endpoint.
    - `phoneNumber` (string) (**requerido**): Phone number of the mobile device endpoint.
    - `alertingEnabled` (boolean) (**requerido**): If `true`, alerting is enabled for the endpoint.
  - `host` (object): `HOTDESKING_GUEST` endpoints include the `host` element when the user has an active hotdesking session on a host.
    - `id` (string) (**requerido**): Unique identifier of the endpoint.
    - `type` (string) (**requerido**): * `CALLING_DEVICE` - Endpoint is a calling device.  * `APPLICATION` - Endpoint is an application.  * `HOTDESKING_GUEST` - Endpoint is a hotdesking guest. Valores: CALLING_DEVICE, APPLICATION, HOTDESKING_GUEST.
    - `name` (string) (**requerido**): Name of the endpoint.
    - `autoAndForcedAnswerEnabled` (boolean) (**requerido**): If `true`, the endpoint can be remotely controlled, allowing actions such as mute, hold, resume and answer.
    - `ownerId` (string): Unique identifier of the endpoint owner.
    - `ownerType` (string): * `PEOPLE` - Indicates the associated member is a person.  * `PLACE` - Indicates the associated member is a workspace. Valores: PEOPLE, PLACE.
    - `secondaryLines` (array): List of secondary lines. The secondary line information is not returned for the endpoint owned by an entity other than the authenticated user.
      - `id` (string) (**requerido**): Unique identifier for the member.
      - `memberType` (string) (**requerido**): * `PEOPLE` - Indicates the associated member is a person.  * `PLACE` - Indicates the associated member is a workspace. Valores: PEOPLE, PLACE.

### Ejemplo — respuesta 200
```json
{
  "endpoints": [
    {
      "id": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMV9pbnQxMy9DQUxMSU5HX0RFVklDRS85MGQyMmM0Yy0wMGI3LTQ4YzAtYjUwNi0yM2UwY2E2MTlkYmM=",
      "type": "CALLING_DEVICE",
      "name": "Webex Go Device",
      "autoAndForcedAnswerEnabled": false,
      "ownerId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9kNTlkYzFkOC00NjdkLTRhNGUtOTRlNi1jOTYyZjEyMmY5YWM",
      "ownerType": "PEOPLE",
      "mobilitySettings": {
        "phoneNumber": "+13374831660",
        "alertingEnabled": false
      }
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OLzIyNjBkMDYxLWViNDUtNDJhMi05MmY3LWFkZDMyMzRiYzI0Yw",
      "type": "APPLICATION",
      "name": "Webex Tablet Application",
      "autoAndForcedAnswerEnabled": false,
      "ownerId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9kNTlkYzFkOC00NjdkLTRhNGUtOTRlNi1jOTYyZjEyMmY5YWM",
      "ownerType": "PEOPLE",
      "secondaryLines": [
        {
          "id": "Y2lzY29zcGFyazovL3VzL1ZJUlRVQUxfTElORS82NDhjYjBkMC1kODU2LTQzNzQtYmI4My0zNWFhNTIxZDhiZmI",
          "memberType": "VIRTUAL_LINE"
        }
      ]
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0hPVERFU0tJTkdfR1VFU1QvN2FmYTFlNWMtOTFiYS00NzRkLWEzODMtZTAyMDgxZDU3YmE5",
      "type": "HOTDESKING_GUEST",
      "name": "Cisco HotDesking",
      "autoAndForcedAnswerEnabled": false,
      "ownerId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9kNTlkYzFkOC00NjdkLTRhNGUtOTRlNi1jOTYyZjEyMmY5YWM",
      "ownerType": "PEOPLE",
      "secondaryLines": [
        {
          "id": "Y2lzY29zcGFyazovL3VzL1
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