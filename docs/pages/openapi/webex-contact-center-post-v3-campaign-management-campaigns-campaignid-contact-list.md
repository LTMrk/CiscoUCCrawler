---
doc_id: webex-contact-center-post-v3-campaign-management-campaigns-campaignid-contact-list
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v3/campaign-management/campaigns/{campaignId}/contact-list
operation_id: createContactList
tags: Contact List Management
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-21T15:48:41.823107+00:00
---

# POST /v3/campaign-management/campaigns/{campaignId}/contact-list

**API:** Webex Contact Center
**Área:** Contact List Management
**operationId:** `createContactList`

## Resumen
Create contact list

## Descripción
Creates and activates a contact list for a campaign. The system can activate a contact list even if there are no contact records within it.

## Parámetros
- `campaignId` [path] (string) (**requerido**): Campaign ID to which the contact list belongs.

## Cuerpo de la petición (application/json)
- `supportedChannels` (array) (**requerido**): Supported channels for the contact list
- `activationTimeLagMinutes` (integer): Contact list activation time lag in minutes (0 = immediate activation, 180 = 3 hours delay). Required if activationDateTime is not provided.
- `activationDateTime` (string): Contact list activation DateTimeStamp (format: YYYY-MM-DDTHH:MM). Required if activationTimeLagMinutes is not provided.

### basic — petición
```json
{
  "supportedChannels": [
    "Voice",
    "SMS"
  ],
  "activationTimeLagMinutes": 180
}
```

### withTimestamp — petición
```json
{
  "supportedChannels": [
    "Email"
  ],
  "activationDateTime": "2025-09-24T18:47:00Z"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/v3/campaign-management/campaigns/<campaignId>/contact-list' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"supportedChannels": []}'
```

## Respuestas correctas
**201**: Contact list created successfully
- `outcome` (string): Outcome of the operation Valores: Success, Failure.
- `statusCode` (integer): 0 for success, non-zero for failure or validation failure
- `contactListId` (string): Contact List ID within the campaign (number only)

### success — respuesta 201
```json
{
  "outcome": "Success",
  "statusCode": 0,
  "contactListId": "501"
}
```

## Respuestas de error
- **400**: Invalid request
  Ejemplo:
```json
{
  "code": "InvalidRequest",
  "message": "The campaign ID is missing"
}
```

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs