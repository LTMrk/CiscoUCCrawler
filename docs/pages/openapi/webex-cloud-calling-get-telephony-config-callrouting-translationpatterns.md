---
doc_id: webex-cloud-calling-get-telephony-config-callrouting-translationpatterns
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/callRouting/translationPatterns
operation_id: Retrieve the list of Translation Patterns
tags: Call Routing
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.571452+00:00
---

# GET /telephony/config/callRouting/translationPatterns

**API:** Webex Cloud Calling
**Área:** Call Routing
**operationId:** `Retrieve the list of Translation Patterns`

## Resumen
Retrieve the list of Translation Patterns

## Descripción
Retrieve a list of translation patterns for a given organization.

A translation pattern lets you manipulate dialed digits before routing a call and applies to outbound calls only. See [this article](https://help.webex.com/en-us/article/nib9o6h/Translation-patterns-for-outbound-calls) for details about the translation pattern syntax.

Requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): ID of the organization containing the translation patterns.
- `limitToLocationId` [query] (string): When a location ID is passed, then return only the corresponding location level translation patterns.
- `limitToOrgLevelEnabled` [query] (string): When set to be `true`, then return only the organization-level translation patterns.
- `max` [query] (number): Limit the number of objects returned to this maximum count.
- `start` [query] (number): Start at the zero-based offset in the list of matching objects.
- `order` [query] (string): Sort the list of translation patterns according to translation pattern name, ascending or descending.
- `name` [query] (string): Only return translation patterns with the matching `name`.
- `matchingPattern` [query] (string): Only return translation patterns with the matching `matchingPattern`.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/callRouting/translationPatterns' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `translationPatterns` (array) (**requerido**): List of translation pattern information.
  - `id` (string) (**requerido**): Unique identifier for a translation pattern.
  - `name` (string) (**requerido**): Name given to a translation pattern for an organization.
  - `matchingPattern` (string) (**requerido**): Matching pattern given to a translation pattern for an organization.
  - `replacementPattern` (string) (**requerido**): Replacement pattern given to a translation pattern for an organization.
  - `level` (string) (**requerido**): Level at which the translation pattern is created. The level can either be `Organization` or `Location`.
  - `location` (object): Location associated with the hot desking member.
    - `id` (string) (**requerido**): Unique identifier for the location.
    - `name` (string) (**requerido**): Name of the location.

### Ejemplo — respuesta 200
```json
{
  "translationPatterns": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1NDSEVEVUxFL1FWVlVUMEZVVkVWT1JFRk9WQzFDVlZOSlRrVlRVeTFJVDFWU1V3",
      "name": "TranslationPattern1",
      "matchingPattern": "781",
      "replacementPattern": "+91348781",
      "level": "Organization"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1NDSEVEVUxFL1FWVlVUMEZVVkVWT1JFRk9WQzFDVlZOSlRrVlRVeTFJVDFWU1V5",
      "name": "TranslationPattern2",
      "matchingPattern": "2XXX",
      "replacementPattern": "2013",
      "level": "Location",
      "location": {
        "name": "CHN11",
        "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzc4YzU5NDE2LTQ5YWQtNDVlMy04NmIyLTFkZjU5M2IyZDdhYQ"
      }
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