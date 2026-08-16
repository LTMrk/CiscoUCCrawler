---
doc_id: webex-broadworks-post-broadworks-subscribers-validate
source: webex-openapi-specs/public-spec/webex-broadworks.json
api: Webex Broadworks Calling
method: POST
path: /broadworks/subscribers/validate
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.285765+00:00
---

# POST /broadworks/subscribers/validate

**API:** Webex Broadworks Calling
**Área:** BroadWorks Subscribers
**operationId:** `Precheck a Broadworks Subscriber Provisioning`

## Resumen
Precheck a Broadworks Subscriber Provisioning

## Descripción
Verify the likely success of provisioning a broadworks subscriber.

<div>
<Callout type='info'>
The Prerequisite for using this API is to have at least one Broadworks Cluster configured against partner using Partner Hub. The Provisioning Precheck APIs supports two variants of Broadworks Provisioning Precheck Requests. Please refer to [Using the Provisioning Precheck API](/docs/api/guides/webex-for-broadworks-developers-guide#using-the-precheck-provisioning-api) section in [Webex for BroadWorks](/docs/api/guides/webex-for-broadworks-developers-guide) guide for more information.
</Callout>
</div>

## Cuerpo de la petición (application/json)
- `provisioningId` (string): Provisioning ID that defines how this subscriber is to be provisioned for Cisco Webex Services. Each Customer Template has its unique Provisioning ID. This ID will be displayed under the chosen Customer Template on Cisco Webex Control Hub.
- `userId` (string): The user ID of the Broadworks subscriber.
- `spEnterpriseId` (string): The Service Provider supplied unique identifier for the subscriber's enterprise.
- `firstName` (string): The first name of the subscriber.
- `lastName` (string): The last name of the subscriber.
- `package` (string): The Webex for BroadWorks package to be assigned to the subscriber.  * `softphone` - Softphone package.  * `basic` - Basic package.  * `standard` - Standard package.  * `premium` - Premium package. Valores: softphone, basic, standard, premium.
- `primaryPhoneNumber` (string): The primary phone number configured for the subscriber on BroadWorks.
- `mobilePhoneNumber` (string): The mobile phone number configured against the subscriber on BroadWorks.
- `extension` (string): The extension number configured against the subscriber on BroadWorks.
- `email` (string) **(requerido)**: The email address of the subscriber.
- `language` (string): The ISO 639-1 language code associated with the subscriber. Reserved for future use. Any value currently specified will be ignored during subscriber provisioning.
- `timezone` (string): The time zone associated with the subscriber. Refer to the [Webex Meetings Site Timezone](/docs/api/guides/webex-for-broadworks-developers-guide#webex-meetings-site-timezone) section of the [Webex for BroadWorks](/docs/api/guides/webex-for-broadworks-developers-guide) guide for more information.
- `customerInfo` (object): The information of the customer into which the subscriber is provisioned. If you are including this parameter, you must include the `primaryEmail` of the customer.
  - `primaryEmail` (string) **(requerido)**: The Customer's primary email address.

### Ejemplo de petición
```json
{
  "provisioningId": "ZjViMzYxODctYzhkZC00NzI3LThiMmYtZjljNDQ3ZjI5MDQ2OjQyODVmNTk0LTViNTEtNDdiZS05Mzk2LTZjMzZlMmFkODNhNQ",
  "userId": "95547321@example.com",
  "spEnterpriseId": "Reseller1+example",
  "firstName": "John",
  "lastName": "Andersen",
  "email": "john.anderson@example.com",
  "primaryPhoneNumber": "+1-240-555-1212",
  "language": "en",
  "package": "standard",
  "customerInfo": {
    "primaryEmail": "alice.anderson@example.com"
  }
}
```

## Respuestas
- **200**: OK
  - `message` (string): A textual representation of the Precheck response message containing the `infoCode` object in the case of a success response and the `errorCode` object in the case of failure.
  - `info` (object): A list of `ProvisioningPreCheckResponseInfo` objects.
    - `infoCode` (number): Provisioning Precheck `infoCode`.
    - `description` (string): A textual description of the `infoCode`.
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
