---
doc_id: webex-cloud-calling-put-telephony-config-people-me-settings-executive-callfiltering-criteria-id
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/people/me/settings/executive/callFiltering/criteria/{id}
operation_id: updateMyExecutiveCallFilteringCriteria
tags: Beta Call Settings For Me With Userhub Phase1
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.365032+00:00
---

# PUT /telephony/config/people/me/settings/executive/callFiltering/criteria/{id}

**API:** Webex Cloud Calling
**Área:** Beta Call Settings For Me With Userhub Phase1
**operationId:** `updateMyExecutiveCallFilteringCriteria`

## Resumen
Modify User Executive Call Filtering Criteria Settings

## Descripción
Update executive call filtering criteria settings for the authenticated user.

Executive Call Filtering Criteria in Webex allows you to modify detailed configuration for a specific filter rule. This includes updating schedule settings, phone number filters, and call routing preferences for executive call filtering.

This API requires a user auth token with a scope of `spark:telephony_config_write`.

## Parámetros
- `id` [path] (string) (**requerido**): The `id` parameter specifies the unique identifier for the executive call filtering criteria. Example: `Y2lzY29zcGFyazovL3VzL0NSSVRFUklBL2RHVnpkRjltYVd4MFpYST0`.

## Cuerpo de la petición (application/json)
- `scheduleName` (string): Name of the schedule associated with this criteria.
- `scheduleType` (string): * `businessHours` - The schedule type that specifies the business or working hours during the day.  * `holidays` - The schedule type that specifies the day when your organization is not open. Valores: holidays, businessHours.
- `scheduleLevel` (string): * `PEOPLE` - The schedule level that specifies that criteria is of People level.  * `GROUP` - The schedule level that specifies that criteria is of Group (Location) level. Valores: PEOPLE, GROUP.
- `callsFrom` (string): * `ANY_PHONE_NUMBER` - The criteria applies to any phone number.  * `SELECT_PHONE_NUMBERS` - The criteria applies to selected phone numbers.  * `ANY_INTERNAL` - The criteria applies to any internal number.  * `ANY_EXTERNAL` - The criteria applies to any external number. Valores: ANY_PHONE_NUMBER, SELECT_PHONE_NUMBERS, ANY_INTERNAL, ANY_EXTERNAL.
- `anonymousCallersEnabled` (boolean): Set to enable or disable the criteria for anonymous callers.
- `unavailableCallersEnabled` (boolean): Set to enable or disable the criteria for unavailable callers.
- `phoneNumbers` (array): The list of phone numbers that this filtering criteria applies to, when `callsFrom` is set to `SELECT_PHONE_NUMBERS`.
- `filterEnabled` (boolean): Controls the action when this criteria matches a call. When `true`, matching calls are filtered and will alert the executive's assistants. When `false`, matching calls are not filtered and will not alert the executive's assistants. Criteria with `filterEnabled` as `false` take precedence over other filtering criteria with `filterEnabled` as `true`, allowing exceptions where certain calls are not filtered to the executive's assistants.
- `callsToNumbers` (array): List of numbers for the executive that will match the criteria when called. This may include the executive’s primary number and/or extension, as well as secondary (alternate) numbers (and associated extensions). If the list is empty, any number or extension for the executive matches the criteria when called. If the list is not empty, only the specified numbers and their extensions match the criteria.
  - `type` (string): * `PRIMARY` - Number is assigned as primary to executive.  * `ALTERNATE` - Number is assigned as alternate (secondary) to the executive. Valores: PRIMARY, ALTERNATE.
  - `phoneNumber` (string): The phone number assigned to the executive that will be used to match criteria.

### Ejemplo — petición
```json
{
  "filterName": "VIP Callers Updated",
  "scheduleName": "Business Hours",
  "scheduleType": "businessHours",
  "scheduleLevel": "PEOPLE",
  "callsFrom": "SELECT_PHONE_NUMBERS",
  "anonymousCallersEnabled": false,
  "unavailableCallersEnabled": false,
  "phoneNumbers": [
    "+14085551234",
    "+14085551235"
  ],
  "filterEnabled": true,
  "callsToNumbers": [
    {
      "type": "PRIMARY",
      "phoneNumber": "+14085556789"
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/people/me/settings/executive/callFiltering/criteria/<id>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: Executive call filtering criteria updated successfully. Returns the updated criteria ID.
- `id` (string): The unique identifier for the criteria.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1JFU1VSTkFNRV9IRVJF"
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