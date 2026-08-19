---
doc_id: webex-cloud-calling-get-telephony-config-people-me-countries-countrycode
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/me/countries/{countryCode}
operation_id: getCountryTelephonyConfigRequirements
tags: Beta Call Settings For Me With Userhub Phase1
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:07.967511+00:00
---

# GET /telephony/config/people/me/countries/{countryCode}

**API:** Webex Cloud Calling
**Área:** Beta Call Settings For Me With Userhub Phase1
**operationId:** `getCountryTelephonyConfigRequirements`

## Resumen
Get country-specific telephony configuration requirements

## Descripción
Retrieve country-specific telephony configuration requirements for the authenticated user.

Webex Calling supports multiple regions and time zones to validate and present the information using the local date and time, as well as localized dialing rules.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Parámetros
- `countryCode` [path] (string) (**requerido**): The ISO country code for which configuration requirements are requested.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/me/countries/<countryCode>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Country-specific telephony configuration requirements retrieved successfully.
- `stateRequired` (boolean): If `stateRequired` should be a Mandatory field in UI
- `zipCodeRequired` (boolean): If `zipCodeRequired` should be a Mandatory field in UI
- `states` (array):
  - `code` (string): State Code
  - `name` (string): State Name
- `timeZones` (array): List of supported timezones for the country.

### Ejemplo — respuesta 200
```json
{
  "stateRequired": true,
  "zipCodeRequired": false,
  "states": [
    {
      "code": "CA",
      "name": "California"
    },
    {
      "code": "NY",
      "name": "New York"
    }
  ],
  "timeZones": [
    "America/Los_Angeles",
    "America/New_York"
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