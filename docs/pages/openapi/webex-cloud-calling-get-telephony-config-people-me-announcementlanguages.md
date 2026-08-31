---
doc_id: webex-cloud-calling-get-telephony-config-people-me-announcementlanguages
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/me/announcementLanguages
operation_id: getAnnouncementLanguagesForMe
tags: Beta Call Settings For Me With Userhub Phase1
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.156985+00:00
---

# GET /telephony/config/people/me/announcementLanguages

**API:** Webex Cloud Calling
**Área:** Beta Call Settings For Me With Userhub Phase1
**operationId:** `getAnnouncementLanguagesForMe`

## Resumen
Get announcement languages for the authenticated user

## Descripción
Retrieve the list of available announcement languages for the authenticated user's telephony configuration.

Announcement languages determine the language used for system prompts and announcements during calls.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/me/announcementLanguages' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Announcement languages retrieved successfully.
- `languages` (array):
  - `name` (string): Language Name
  - `code` (string): Language Code

### A list of announcement languages — respuesta 200
```json
{
  "languages": [
    {
      "name": "English",
      "code": "en"
    },
    {
      "name": "Spanish",
      "code": "es"
    }
  ]
}
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs