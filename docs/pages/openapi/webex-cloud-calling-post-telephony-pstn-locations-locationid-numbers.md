---
doc_id: webex-cloud-calling-post-telephony-pstn-locations-locationid-numbers
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/pstn/locations/{locationId}/numbers
operation_id: performNumbersAction
tags: PSTN
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-21T08:43:27.098769+00:00
---

# POST /telephony/pstn/locations/{locationId}/numbers

**API:** Webex Cloud Calling
**Área:** PSTN
**operationId:** `performNumbersAction`

## Resumen
Perform Numbers Action

## Descripción
Perform number usage action for the specified list of numbers. The required `action` query parameter specifies the operation to apply to the numbers in the request body. The API supports modifying number usage between STANDARD/SERVICE/ELIN.

A phone number's usage type determines how it is used within a Webex Calling location. `STANDARD` numbers support regular calling and can be assigned to people, workspaces, or features. `SERVICE` numbers support services such as Auto Attendant, Call Queue, Hunt Groups, and Webex Contact Center. `ELIN` (Emergency Location Identification Number) numbers provide emergency services with accurate caller information and support callbacks to the person or workspace that initiated the emergency call, including people with extension-only lines.

Executing number actions requires an administrator auth token with a scope of `spark-admin:telephony_pstn_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Location identifier in Webex format.
- `action` [query] (string) (**requerido**): Action to execute. Valores: modifyElin, modifyStandard, modifyService.
- `orgId` [query] (string): Organization ID. If not specified, uses the organization from the OAuth token.

## Cuerpo de la petición (application/json)
- `numbers` (array) (**requerido**): Phone numbers to process.

### Ejemplo — petición
```json
{
  "numbers": [
    "+14155551234",
    "+14155555678"
  ]
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/pstn/locations/<locationId>/numbers?action=<action>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"numbers": []}'
```

## Respuestas correctas
**200**: OK
- `orders` (array) (**requerido**): Number action orders created by the request.
  - `orderId` (string) (**requerido**): Order identifier in Webex format.
  - `status` (string) (**requerido**): Order status.  - `PENDING` — The order is waiting to be processed. - `PARTIAL` — The order completed with only some number actions succeeding. - `COMPLETE` — The order completed successfully. - `PROVISIONED` — The requested number changes were successfully provisioned. - `ERROR` — The order failed. Valores: PENDING, PARTIAL, COMPLETE, PROVISIONED, ERROR.
  - `numbers` (array) (**requerido**): Results for the phone numbers included in the order.
    - `number` (string) (**requerido**): Phone number.
    - `status` (string) (**requerido**): Number-level action status.  - `SUCCESS` — The action completed successfully for the number. - `FAILED` — The action failed for the number. - `PENDING` — The action is still being processed for the number. Valores: SUCCESS, FAILED, PENDING.
    - `usage` (string) (**requerido**): Final number usage type.  - `NONE` — Standard number usage. - `SERVICE` — Service number usage. - `ELIN` — Emergency Location Identification Number usage. Valores: NONE, SERVICE, ELIN.
    - `errors` (array): Validation or execution errors for this number.
      - `number` (string): Phone number associated with the error.
      - `errorType` (string): Category of the error, such as `VERIFICATION` or `FAILED`.
      - `errorCode` (string) (**requerido**): Stable machine-readable error code, such as `ERR.V.TRM.TMN60045`.
      - `errorTitle` (string): Stable symbolic title associated with the error code, such as `NUMBER_HAS_BUSINESS_TEXTING`.
      - `errorMessage` (string): Human-readable explanation of the error. Defaults to the message associated with `errorCode` and may contain more specific runtime detail.
  - `errors` (array): Validation or provisioning errors associated with the order.
    - `number` (string): Phone number associated with the error.
    - `errorType` (string): Category of the error, such as `VERIFICATION` or `FAILED`.
    - `errorCode` (string) (**requerido**): Stable machine-readable error code, such as `ERR.V.TRM.TMN60045`.
    - `errorTitle` (string): Stable symbolic title associated with the error code, such as `NUMBER_HAS_BUSINESS_TEXTING`.
    - `errorMessage` (string): Human-readable explanation of the error. Defaults to the message associated with `errorCode` and may contain more specific runtime detail.

### Ejemplo — respuesta 200
```json
{
  "orders": [
    {
      "orderId": "Y2lzY29zcGFyazovL3VzL09SREVSL2E2NGM5OWM0LTk4MDItNGY0YS04ZWMwLTUzMjIwZDhmZWFiYw",
      "status": "PROVISIONED",
      "numbers": [
        {
          "number": "+14155551234",
          "status": "SUCCESS",
          "usage": "ELIN"
        }
      ]
    }
  ]
}
```

## Respuestas de error
- **400**: Bad Request: Invalid action or invalid number payload.
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