---
doc_id: webex-contact-center-get-v1-ewt
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /v1/ewt
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.959711+00:00
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
- `queueId` [query] (string) **(requerido)**: Id of the queue for which the EWT is to be returned
- `lookbackMinutes` [query] (integer) **(requerido)**: Integer between 5 and 240 (4 hours) signifying how long back to look at the data points to determine EWT for this queue
- `maxCV` [query] (integer): This an optional parameter. Maximum value of Coefficient of Variance in a subset of samples (wait times for tasks that got connected to agent in one minute interval) to determine whether the average of such values should be treated as a valid sample for EWT computation. If its not passed it takes the default value of 40 %
- `minValidSamples` [query] (integer): This an optional parameter. Minimum value of percentage of valid samples (with respect to total number of samples) in the specified lookbackMinutes minutes. If its not passed it takes the default value of 40 %
- `TrackingId` [header] (string): Tracking ID to use for this operation, for traceability, debugging, and error reporting purposes.
- `orgId` [query] (string): Organization ID to use for this operation. If unspecified, inferred from token. Token must have permission to interact with this organization.

## Respuestas
- **200**: OK
  - `estimatedWaitTime` (number): The estimated wait time in milli seconds.
- **204**: Not enough valid samples were found to compute the estimate wait time. Refer the parameters, lookbackMinutes, maxCV and minValidSamples to tune the API behavior   Note : For an Invalid queue value we return a 204
- **400**: Validation Error
- **401**: Unauthorized Operation
- **403**: Forbidden
- **422**: Unprocessable Entity
- **500**: An Unexpected Error Occurred
- **503**: The service is currently unavailable to serve the requests

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
