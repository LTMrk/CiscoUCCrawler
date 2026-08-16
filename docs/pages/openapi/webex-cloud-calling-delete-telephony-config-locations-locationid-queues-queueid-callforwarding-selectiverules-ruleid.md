---
doc_id: webex-cloud-calling-delete-telephony-config-locations-locationid-queues-queueid-callforwarding-selectiverules-ruleid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: DELETE
path: /telephony/config/locations/{locationId}/queues/{queueId}/callForwarding/selectiveRules/{ruleId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.604203+00:00
---

# DELETE /telephony/config/locations/{locationId}/queues/{queueId}/callForwarding/selectiveRules/{ruleId}

**API:** Webex Cloud Calling
**Área:** Features:  Call Queue
**operationId:** `deleteCallQueueSelectiveCallForwardingRule`

## Resumen
Delete a Selective Call Forwarding Rule for a Call Queue

## Descripción
Delete a Selective Call Forwarding Rule for the designated Call Queue.

A selective call forwarding rule for a call queue allows calls to be forwarded or not forwarded to the designated number, based on the defined criteria.

Note that the list of existing call forward rules is available in the call queue's call forwarding settings.

Deleting a selective call forwarding rule for a call queue requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

**NOTE**: The Call Forwarding Rule ID will change upon modification of the Call Forwarding Rule name.

## Parámetros
- `locationId` [path] (string) **(requerido)**: Location in which this call queue exists.
- `queueId` [path] (string) **(requerido)**: Delete the rule for this call queue.
- `ruleId` [path] (string) **(requerido)**: Call queue rule you are deleting.
- `orgId` [query] (string): Delete call queue rule from this organization.

## Respuestas
- **204**: No Content
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

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
