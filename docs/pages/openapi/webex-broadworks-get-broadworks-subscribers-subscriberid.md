---
doc_id: webex-broadworks-get-broadworks-subscribers-subscriberid
source: webex-openapi-specs/public-spec/webex-broadworks.json
api: Webex Broadworks Calling
method: GET
path: /broadworks/subscribers/{subscriberId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.285390+00:00
---

# GET /broadworks/subscribers/{subscriberId}

**API:** Webex Broadworks Calling
**Área:** BroadWorks Subscribers
**operationId:** `Get a BroadWorks Subscriber`

## Resumen
Get a BroadWorks Subscriber

## Descripción
This API lets a Service Provider retrieve details of a provisioned BroadWorks subscriber on Webex.

## Parámetros
- `subscriberId` [path] (string) **(requerido)**: A unique identifier for the subscriber in question.

## Respuestas
- **200**: OK
  - `id` (string): A unique Cisco identifier for the subscriber.
  - `personId` (string): The Person Id of the subscriber on Webex. To be used when referencing this subscriber on other Webex APIs. Only presented when status is `provisioned`.
  - `userId` (string): The user ID of the subscriber on BroadWorks.
  - `spEnterpriseId` (string): The Service Provider supplied unique identifier for the subscriber's enterprise.
  - `firstName` (string): The first name of the subscriber.
  - `lastName` (string): The last name of the subscriber.
  - `email` (string): The email address of the subscriber.
  - `primaryPhoneNumber` (string): The primary phone number configured against the subscriber on BroadWorks.
  - `mobilePhoneNumber` (string): The mobile phone number configured against the subscriber on BroadWorks.
  - `extension` (string): The extension number configured against the subscriber on BroadWorks.
  - `package` (string): The Webex for BroadWorks Package assigned to the subscriber.  * `softphone` - Softphone package.  * `basic` - Basic package.  * `standard` - Standard package.  * `premium` - Premium package. Valores: softphone, basic, standard, premium.
  - `status` (string): The provisioning status of the user.  * `pending_email_input` - Subscriber Provisioning is paused, pending input of email address.  * `pending_email_validation` - Subscriber Provisioning is paused. The subscriber has entered an email address but has yet to complete validation.  * `pending_user_migration` - Subscriber Provisioning is paused. An automated email is sent to the subscriber, waiting for the subscriber's consent.  * `provisioning` - Subscriber provisioning is in progress.  * `provisioned` - The subscriber is fully provisioned on Webex.  * `updating` - An update is in progress for a provisioned subscriber.  * `error` - An error occurred provisioning the subscriber on Webex. Valores: pending_email_input, pending_email_validation, pending_user_migration, provisioning, provisioned, updating, error.
  - `errors` (array): List of errors that occurred during that last attempt to provision/update this subscriber.   *Note:*  + This list captures errors that occurred during *asynchronous or background* provisioning of the subscriber, *after* the API has been accepted and 200 OK response returned.  + Any errors that occur during initial API request validation will be captured directly in error response with appropriate HTTP status code.
    - `errorCode` (number): An error code that identifies the reason for the error.
    - `description` (string): A description of the error.
  - `created` (string): The date and time the subscriber was provisioned.
  - `lastStatusChange` (string): The date and time the provisioning status of the subscriber last changed.
  - `provisioningId` (string): This Provisioning ID associated with this subscriber.
  - `selfActivated` (boolean): Indicates if the subscriber was self activated, rather than provisioned via these APIs.
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
