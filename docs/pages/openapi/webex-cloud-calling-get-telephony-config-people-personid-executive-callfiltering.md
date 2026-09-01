---
doc_id: webex-cloud-calling-get-telephony-config-people-personid-executive-callfiltering
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/{personId}/executive/callFiltering
operation_id: getPersonExecutiveCallFilteringSettings
tags: User Call Settings (2/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.774715+00:00
---

# GET /telephony/config/people/{personId}/executive/callFiltering

**API:** Webex Cloud Calling
**Área:** User Call Settings (2/2)
**operationId:** `getPersonExecutiveCallFilteringSettings`

## Resumen
Get Person Executive Call Filtering Settings

## Descripción
Retrieve the executive call filtering settings for the specified person.

Executive Call Filtering in Webex allows you to control which calls are allowed to reach the executive assistant based on custom criteria, such as specific phone numbers or call types. You can enable or disable call filtering and configure filter rules to manage incoming calls.

This API requires a full, user, read-only or location administrator auth token with a scope of `spark-admin:telephony_config_read`

## Parámetros
- `personId` [path] (string) (**requerido**): A unique identifier for the person.
- `orgId` [query] (string): Organization ID for the user.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/<personId>/executive/callFiltering' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: The person executive call filtering settings were retrieved successfully.
- `enabled` (boolean) (**requerido**): Indicates whether executive call filtering is enabled.
- `filterType` (string) (**requerido**): * `CUSTOM_CALL_FILTERS` - Choose this option to ensure that only specific calls are sent to the executive assistant.  * `ALL_CALLS` - Choose this option to send both internal and external calls to the executive assistant.  * `ALL_INTERNAL_CALLS` - Choose this option to send all internal calls to the executive assistant.  * `ALL_EXTERNAL_CALLS` - Choose this option to send all external calls to the executive assistant. Valores: CUSTOM_CALL_FILTERS, ALL_CALLS, ALL_INTERNAL_CALLS, ALL_EXTERNAL_CALLS.
- `criteria` (array): The list of call filtering criteria configured for executive call filtering.
  - `id` (string) (**requerido**): Unique identifier for the filter criteria.
  - `filterName` (string) (**requerido**): Name of the criteria.
  - `source` (string) (**requerido**): * `ANY_PHONE_NUMBER` - The criteria applies to any phone number.  * `SELECT_PHONE_NUMBERS` - The criteria applies to selected phone numbers.  * `ANY_INTERNAL` - The criteria applies to any internal number.  * `ANY_EXTERNAL` - The criteria applies to any external number. Valores: ANY_PHONE_NUMBER, SELECT_PHONE_NUMBERS, ANY_INTERNAL, ANY_EXTERNAL.
  - `activationEnabled` (boolean) (**requerido**): Controls whether this filter criteria is active. When `true`, the criteria is evaluated for incoming calls. When `false`, the criteria is completely ignored and has no effect on call filtering.
  - `filterEnabled` (boolean) (**requerido**): Controls the action when this criteria matches a call. When `true`, matching calls are filtered and will alert the executive's assistants. When `false`, matching calls are not filtered and will not alert the executive's assistants. Criteria with `filterEnabled` as `false` take precedence over other filtering criteria with `filterEnabled` as `true`, allowing exceptions where certain calls are not filtered to the executive's assistants.

### Ejemplo — respuesta 200
```json
{
  "enabled": true,
  "filterType": "CUSTOM_CALL_FILTERS",
  "criteria": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0NSSVRFUklBL1FtVjNORE15TXc9PQ",
      "filterName": "VIP Callers",
      "source": "SELECT_PHONE_NUMBERS",
      "activationEnabled": true,
      "filterEnabled": true
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