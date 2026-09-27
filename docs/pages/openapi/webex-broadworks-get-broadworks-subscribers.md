---
doc_id: webex-broadworks-get-broadworks-subscribers
source: webex-openapi-specs/public-spec/webex-broadworks.json
api: Webex Broadworks Calling
api_version: 1.0.0
method: GET
path: /broadworks/subscribers
operation_id: List BroadWorks Subscribers
tags: BroadWorks Subscribers
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-27T10:51:18.912399+00:00
---

# GET /broadworks/subscribers

**API:** Webex Broadworks Calling
**Área:** BroadWorks Subscribers
**operationId:** `List BroadWorks Subscribers`

## Resumen
List BroadWorks Subscribers

## Descripción
This API lets a Service Provider search for their associated subscribers. There are a number of filter options that can be combined in a single request.

## Parámetros
- `userId` [query] (string): The user ID of the subscriber on BroadWorks.
- `personId` [query] (string): The Person ID of the Webex subscriber.
- `email` [query] (string): The email address of the subscriber.
- `provisioningId` [query] (string): The Provisioning ID associated with this subscriber.
- `spEnterpriseId` [query] (string): The Service Provider supplied unique identifier for the subscriber's enterprise.
- `lastStatusChange` [query] (string): Only include subscribers with a provisioning status change after this date and time. Epoch time (in milliseconds) preferred, but ISO 8601 date format also accepted.
- `status` [query] (string): The provisioning status of the subscriber. This Parameter supports multiple comma separated values. For example : status=error,provisioned,provisioning. Valores: pending_email_input, pending_email_validation, pending_user_migration, provisioning, provisioned, updating, error.
- `after` [query] (string): Only include subscribers created after this date and time. Epoch time (in milliseconds) preferred, but ISO 8601 date format also accepted.
- `selfActivated` [query] (boolean): Indicates if the subscriber was self activated, rather than provisioned via these APIs.
- `max` [query] (integer): Limit the maximum number of subscribers returned in the search response, up to 100 per page. Refer to the [Pagination](/docs/basics#pagination) section of [Webex REST API Basics](/docs/basics). Por defecto: 50.

## Ejemplo de invocación
```bash
curl -X GET '/broadworks/subscribers' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array): An array of Subscriber objects.
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

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1NVQlNDUklCRVIvNjk3MGU2YmItNzQzOS00ZmZiLWFkMzQtZDNmZjAxNjdkZGFk",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
      "userId": "95547321@sp.com",
      "spEnterpriseId": "SP1+acme",
      "firstName": "John",
      "lastName": "Andersen",
      "email": "john.anderson@acme.com",
      "primaryPhoneNumber": "+1-240-555-1212",
      "mobilePhoneNumber": "+1-818-279-1234",
      "extension": "1212",
      "package": "standard",
      "status": "error",
      "errors": [
        {
          "errorCode": 10022,
          "description": "The BroadWorks UserID is already associated with an existing user"
        }
      ],
      "created": "2019-10-18T14:26:16.000Z",
      "lastStatusChange": "2020-03-18T16:05:34.000Z",
      "provisioningId": "ZjViMzYxODctYzhkZC00NzI3LThiMmYtZjljNDQ3ZjI5MDQ2OjQyODVmNTk0LTViNTEtNDdiZS05Mzk2LTZjMzZlMmFkODNhNQ",
      "selfActivated": "false"
    }
  ]
}
```

## Respuestas de error
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

## Contexto de la API
The Webex BroadWorks Calling APIs provide access to advanced calling features and user management for BroadWorks-powered Webex Calling deployments. These APIs support provisioning of users and devices, call control, feature management, device inventory, and detailed reporting. Service providers and enterprises can automate onboarding, integrate with OSS/BSS systems, manage user entitlements, and monitor call quality. The APIs are designed for scalable, multi-tenant environments and support seamless integration with existing telephony infrastructure.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs