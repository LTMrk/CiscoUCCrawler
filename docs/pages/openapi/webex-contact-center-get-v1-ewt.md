---
doc_id: webex-contact-center-get-v1-ewt
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /v1/ewt
operation_id: getEwt
tags: Estimated Wait Time
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.742411+00:00
---

# GET /v1/ewt

**API:** Webex Contact Center
**Área:** Estimated Wait Time
**operationId:** `getEwt`

## Resumen
Get Estimated Wait Time

## Descripción
Retrieve Estimated Wait Time information for a specified look back interval for a specific orgId and queueId combination, with ability to customomize maxCV and minValidSamples (See description above).

## Parámetros
- `queueId` [query] (string) (**requerido**): Id of the queue for which the EWT is to be returned
- `lookbackMinutes` [query] (integer/int32) (**requerido**): Integer between 5 and 240 (4 hours) signifying how long back to look at the data points to determine EWT for this queue
- `maxCV` [query] (integer/int32): This an optional parameter. Maximum value of Coefficient of Variance in a subset of samples (wait times for tasks that got connected to agent in one minute interval) to determine whether the average of such values should be treated as a valid sample for EWT computation. If its not passed it takes the default value of 40 %
- `minValidSamples` [query] (integer/int32): This an optional parameter. Minimum value of percentage of valid samples (with respect to total number of samples) in the specified lookbackMinutes minutes. If its not passed it takes the default value of 40 %
- `TrackingId` [header] (string): Tracking ID to use for this operation, for traceability, debugging, and error reporting purposes.
- `orgId` [query] (string): Organization ID to use for this operation. If unspecified, inferred from token. Token must have permission to interact with this organization.

## Ejemplo de invocación
```bash
curl -X GET '/v1/ewt?queueId=<queueId>&lookbackMinutes=<lookbackMinutes>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `estimatedWaitTime` (number/double): The estimated wait time in milli seconds.
**204**: Not enough valid samples were found to compute the estimate wait time. Refer the parameters, lookbackMinutes, maxCV and minValidSamples to tune the API behavior 
 Note : For an Invalid queue value we return a 204

## Respuestas de error
- **400**: Validation Error
- **401**: Unauthorized Operation
- **403**: Forbidden
- **422**: Unprocessable Entity
- **500**: An Unexpected Error Occurred
- **503**: The service is currently unavailable to serve the requests

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs