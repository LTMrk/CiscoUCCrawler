---
doc_id: webex-messaging-post-teams
source: webex-openapi-specs/public-spec/webex-messaging.json
api: Webex Messaging
api_version: 1.0.0
method: POST
path: /teams
operation_id: Create a Team
tags: Teams
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.814418+00:00
---

# POST /teams

**API:** Webex Messaging
**Área:** Teams
**operationId:** `Create a Team`

## Resumen
Create a Team

## Descripción
Creates a team.

The authenticated user is automatically added as a member of the team. See the [Team Memberships API](/docs/api/v1/team-memberships) to learn how to add more people to the team.

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): A user-friendly name for the team.
- `description` (string): The teams description.

### Ejemplo — petición
```json
{
  "name": "Build Squad",
  "description": "The A team"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/teams' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "<name>"}'
```

## Respuestas correctas
**200**: OK
- `id` (string): A unique identifier for the team.
- `name` (string): A user-friendly name for the team.
- `description` (string): The teams description.
- `created` (string): The date and time the team was created.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1RFQU0vMTNlMThmNDAtNDJmYy0xMWU2LWE5ZDgtMjExYTBkYzc5NzY5",
  "name": "Build Squad",
  "description": "The A Team",
  "created": "2015-10-18T14:26:16.000Z"
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
The Webex Messaging APIs offer robust programmatic access to messaging features within Webex, including sending and receiving messages, managing spaces, memberships, attachments, and moderating content. These APIs enable integration with bots, workflow automation, notification systems, and custom messaging solutions to enhance team collaboration and productivity. Use cases include building chatbots, integrating with ticketing or alerting platforms, automating onboarding flows, and creating custom collaboration experiences tailored to business needs.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs