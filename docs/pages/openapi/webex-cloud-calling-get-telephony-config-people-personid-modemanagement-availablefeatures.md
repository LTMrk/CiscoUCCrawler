---
doc_id: webex-cloud-calling-get-telephony-config-people-personid-modemanagement-availablefeatures
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/{personId}/modeManagement/availableFeatures
operation_id: getListOfAvailableFeatures
tags: User Call Settings (2/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.161197+00:00
---

# GET /telephony/config/people/{personId}/modeManagement/availableFeatures

**API:** Webex Cloud Calling
**Área:** User Call Settings (2/2)
**operationId:** `getListOfAvailableFeatures`

## Resumen
Retrieve the List of Available Features

## Descripción
Retrieve a list of feature identifiers that can be assigned to a user for `Mode Management`. Feature identifiers reference feature instances like `Auto Attendants`, `Call Queues`, and `Hunt Groups`.

Features with mode-based call forwarding enabled can be assigned to a user for `Mode Management`.

Retrieving this list requires a full, read-only, or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `personId` [path] (string) (**requerido**): A unique identifier for the user.
- `name` [query] (string): List features whose `name` contains this string.
- `phoneNumber` [query] (string): List features whose phoneNumber contains this matching string.
- `extension` [query] (string): List features whose `extension` contains this matching string.
- `max` [query] (number): Maximum number of features to return in a single page.
- `start` [query] (number): Start at the zero-based offset in the list of matching objects.
- `order` [query] (string): Sort the list of features based on `name`, `phoneNumber`, or `extension`, either `asc`, or `desc`.
- `orgId` [query] (string): Retrieve features list from this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/<personId>/modeManagement/availableFeatures' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `features` (array) (**requerido**): Array of features.
  - `id` (string) (**requerido**): A unique identifier for the feature.
  - `name` (string) (**requerido**): Unique name for the feature.
  - `type` (string) (**requerido**): * `AUTO_ATTENDANT` - Specifies the feature is an Auto Attendant.  * `CALL_QUEUE` - Specifies the feature is a Call Queue.  * `HUNT_GROUP` - Specifies the feature is a Hunt Group. Valores: AUTO_ATTENDANT, CALL_QUEUE, HUNT_GROUP.
  - `phoneNumber` (string): The primary phone number configured for the feature.
  - `extension` (string): The extension configured for the feature.

### Ejemplo — respuesta 200
```json
{
  "features": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0FVVE9fQVRURU5EQU5ULzA1NTJmNjdiLTU5YTktNDFiYi04NzM2LTFiMDQxZDFkZGQ1ZQ",
      "name": "Test Auto Attendant",
      "type": "AUTO_ATTENDANT",
      "phoneNumber": "+19705550028",
      "extension": "0028"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0NBTExfUVVFVUUvNWMwZmYzZjctZjY2YS00NGQwLTlhODktZGY5N2U5MThkNjcw",
      "name": "Test Call Queue",
      "type": "CALL_QUEUE",
      "phoneNumber": "+2055552221",
      "extension": "0007"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0hVTlRfR1JPVVAvOTExNmRmZDMtZGQ4ZS00YTk5LTg1MmYtMjFiYmMxOGNkNzcy",
      "name": "Test Hunt Group",
      "type": "HUNT_GROUP",
      "phoneNumber": "+2055552221",
      "extension": "0023"
    }
  ]
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