---
doc_id: webex-wholesale-get-wholesale-subpartners
source: webex-openapi-specs/public-spec/webex-wholesale.json
api: Webex Wholesale
method: GET
path: /wholesale/subPartners
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.732322+00:00
---

# GET /wholesale/subPartners

**API:** Webex Wholesale
**Área:** Wholesale Provisioning
**operationId:** `List Wholesale Sub-partners`

## Resumen
List Wholesale Sub-partners

## Descripción
Lists all of the associated sub-partners. There are a number of filter and pagination options that can be combined in a single request.

## Parámetros
- `provisioningState` [query] (string): Status to filter sub-partners based on provisioning state.
- `offset` [query] (string): Offset value for implementing pagination.
- `max` [query] (string): The maximum number of sub-partners returned in the response.

## Respuestas
- **200**: OK
  - `items` (array): An array of `SubPartner` objects.
    - `orgId` (string): The Organization ID for the sub-partner.
    - `subscriptionId` (string): The Wholesale Subscription ID of the partner.
    - `provisioningState` (string): The provisioning status of the sub-partner.  * `active` - Sub-partner can provision new customers and subscribers or update, delete existing ones.  * `suspended` - Sub-partner cannot provision, update customers and subscribers but can delete existing ones. Valores: active, suspended.
    - `created` (string): 02-16T14:10:18.855Z' (string) - The date and time the sub-partner was created.
    - `billingStartDate` (string): 02-22T13:43:41.117Z' (string) - The date and time from which new billing for the sub-partner started.
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
