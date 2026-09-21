---
doc_id: webex-cloud-calling-get-telephony-pstn-locations-locationid-numbers-availablenumbers
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/pstn/locations/{locationId}/numbers/availableNumbers
operation_id: getModifiableNumbers
tags: PSTN
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-21T08:43:27.098517+00:00
---

# GET /telephony/pstn/locations/{locationId}/numbers/availableNumbers

**API:** Webex Cloud Calling
**Área:** PSTN
**operationId:** `getModifiableNumbers`

## Resumen
Get Modifiable Numbers

## Descripción
Retrieve modifiable numbers for a location based on action type.

The required `action` query parameter specifies the operation used to identify eligible numbers.

This endpoint does not support pagination. Up to a configurable server-side maximum of candidate numbers (default 2000) are retrieved and filtered for eligibility, and all eligible numbers within that candidate window are returned in a single response.

A phone number's usage type determines how it is used within a Webex Calling location. `STANDARD` numbers support regular calling and can be assigned to people, workspaces, or features. `SERVICE` numbers support services such as Auto Attendant, Call Queue, Hunt Groups, and Webex Contact Center. `ELIN` (Emergency Location Identification Number) numbers provide emergency services with accurate caller information and support callbacks to the person or workspace that initiated the emergency call, including people with extension-only lines.

Viewing number availability requires an administrator auth token with a scope of `spark-admin:telephony_pstn_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Location identifier in Webex format.
- `action` [query] (string) (**requerido**): Action type for modifiable numbers. Valores: modifyElin, modifyStandard, modifyService.
- `orgId` [query] (string): Organization ID. If not specified, uses the organization from the OAuth token.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/pstn/locations/<locationId>/numbers/availableNumbers?action=<action>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `phoneNumbers` (array) (**requerido**): All eligible modifiable numbers within the server-side candidate window, returned in a single non-paginated response.
  - `phoneNumber` (string) (**requerido**): Phone number in E.164 format.
  - `state` (string): Phone number state.  - `ACTIVE` — The phone number is active. - `INACTIVE` — The phone number is inactive. Valores: ACTIVE, INACTIVE.
  - `isServiceNumber` (boolean) (**requerido**): Indicates whether this is a service number.
  - `tollFreeNumber` (boolean) (**requerido**): Indicates whether this is a toll-free number.
  - `mainNumber` (boolean) (**requerido**): Indicates whether this is the location main number.
  - `isELIN` (boolean) (**requerido**): Indicates whether this number is currently an ELIN.
  - `isReservedNumber` (boolean) (**requerido**): Indicates whether this is a reserved number.
  - `telephonyType` (string) (**requerido**): Telephony type.  - `PSTN_NUMBER` — A standard PSTN number. - `MOBILE_NUMBER` — A mobile telephone number. Valores: PSTN_NUMBER, MOBILE_NUMBER.

### Ejemplo — respuesta 200
```json
{
  "phoneNumbers": [
    {
      "phoneNumber": "+14155551234",
      "state": "ACTIVE",
      "isServiceNumber": false,
      "tollFreeNumber": false,
      "mainNumber": false,
      "isELIN": true,
      "isReservedNumber": false,
      "telephonyType": "PSTN_NUMBER"
    }
  ]
}
```

## Respuestas de error
- **400**: Bad Request: Invalid or missing action value.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but access is not allowed.
- **404**: Not Found: Location not found or feature not enabled.
- **429**: Too Many Requests: The request was rate-limited.
- **500**: Internal Server Error: Unexpected server-side failure.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs