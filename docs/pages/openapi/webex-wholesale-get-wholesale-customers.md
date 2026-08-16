---
doc_id: webex-wholesale-get-wholesale-customers
source: webex-openapi-specs/public-spec/webex-wholesale.json
api: Webex Wholesale
method: GET
path: /wholesale/customers
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.731279+00:00
---

# GET /wholesale/customers

**API:** Webex Wholesale
**Área:** Wholesale Provisioning
**operationId:** `List Wholesale Customers`

## Resumen
List Wholesale Customers

## Descripción
Return a list of wholesale customers. There are a number of filter options, which can be combined in a single request.

## Parámetros
- `externalId` [query] (string): Customer external ID.
- `orgId` [query] (string): The encoded Organization ID for the customer.
- `status` [query] (array): Customer API status.
- `offset` [query] (string): Offset value for implementing pagination.
- `max` [query] (string): The maximum number of customers returned in the response.
- `onBehalfOfSubPartnerOrgId` [query] (string): The encoded organization ID for the sub partner.

## Respuestas
- **200**: OK
  - `items` (array): An array of Customer objects.
    - `id` (string): A unique Cisco identifier for the customer. This value should be used for the `customerId` parameter in the Wholesale Customers and Wholesale Subscribers API.
    - `orgId` (string): The Organization ID of the enterprise on Cisco Webex, to be used when referencing this customer on other Cisco Webex APIs. Only presented when status is `provisioned`.
    - `externalId` (string): External ID of the Customer.
    - `address` (object):
      - `addressLine1` (string): Address Line 1.
      - `addressLine2` (string): Address Line 2.
      - `city` (string): Customer's city.
      - `stateOrProvince` (string): State or Province of the customer.
      - `zipOrPostalCode` (string): Postal/Zip code of the customer.
      - `country` (string): ISO2 country code of the customer, 2 characters. This attribute is used to determine the default Dial In number for the Webex Meeting Sites. Refer to the Address section of [help page](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/wholesale_rtm/wbxbw_b_wholesale-rtm-solution-guide/wbxbw_m_overview-of-webex-wholesale.html#Cisco_Reference.dita_7875bb3e-10c0-4214-8173-7845db31c7a6) for more information.
    - `status` (string): The provisioning status of the customer.  * `provisioned` - Customer is fully provisioned on Cisco Webex.  * `provisioned_with_errors` - Customer is provisioned with errors.  * `provisioning` - Customer is provisioning.  * `updating` - Customer is updating.  * `deleting` - Customer is being deleted.  * `error` - An error occurred provisioning the customer on Cisco Webex.  * `pending_rpl_review` - The customer is pending a Denied Party List compliance check. Valores: provisioned, provisioned_with_errors, provisioning, updating, deleting, error, pending_rpl_review.
    - `packages` (array): List of package names provisioned
    - `resourceDetails` (object):
      - `packages` (array):
        - `name` (string): * `common_area_calling` - Webex Common Area Calling Package.  * `webex_calling` - Webex Calling Package.  * `webex_meetings` - Webex Meetings Package.  * `webex_suite` - Webex Suite Package.  * `webex_voice` - Webex Voice Package.  * `cx_essentials` - Customer Assist Package.  * `webex_calling_standard` - Webex Calling Standard Package.  * `cisco_calling_plan` - Cisco Calling Plan Package.  * `attendant_console` - Attendant Console Package.  * `cx_premium_agent` - Contact Center Premium Agent Package.  * `cx_standard_agent` - Contact Center Standard Agent Package.  * `cx_voice_ports` - Contact Center Voice Ports Package.  * `cx_ai_assistant` - Contact Center AI Assistant Package.  * `webex_ai_agent` - Webex AI Agent Package. Valores: common_area_calling, webex_calling, webex_meetings, webex_suite, webex_voice, cx_essentials, webex_calling_standard, cisco_calling_plan, attendant_console, cx_premium_agent, cx_standard_agent, cx_voice_ports, cx_ai_assistant, webex_ai_agent.
        - `status` (string): The provisioning status of the a particular package.  * `provisioned` - Customer is fully provisioned on Cisco Webex.  * `provisioning` - Customer is provisioning.  * `deleting` - Customer is being deleted.  * `error` - An error occurred provisioning the customer on Cisco Webex. Valores: provisioned, provisioning, deleting, error.
        - `warnings` (array): List of warnings that occurred during that last attempt to provision/update this customer.   *Note:*  + This list captures errors that occurred during *asynchronous or background* provisioning of the customer, *after* the API has been accepted and 202 response returned.  + Any errors that occur during initial API request validation will be captured directly in error response with appropriate HTTP status code.
          - `errorCode` (number): An error code that identifies the reason for the error.
          - `description` (string): A textual representation of the error code.
        - `errors` (array): List of errors that occurred during that last attempt to provision/update this customer.   *Note:*  + This list captures errors that occurred during *asynchronous or background* provisioning of the customer, *after* the API has been accepted and 202 response returned.  + Any errors that occur during initial API request validation will be captured directly in error response with appropriate HTTP status code.
          - `errorCode` (number): An error code that identifies the reason for the error.
          - `description` (string): A textual representation of the error code.
        - `licenseIds` (array): List of licenseIds for the package.
    - `errors` (array): List of errors that occurred during that last attempt to provision/update this customer.   *Note:*  + This list captures errors that occurred during *asynchronous or background* provisioning of the customer, *after* the API has been accepted and 202 response returned.  + Any errors that occur during initial API request validation will be captured directly in error response with appropriate HTTP status code.
      - `errorCode` (number): An error code that identifies the reason for the error.
      - `description` (string): A textual representation of the error code.
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
