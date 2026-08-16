---
doc_id: webex-cloud-calling-get-telephony-config-devices-availablemembers
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/devices/availableMembers
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.546881+00:00
---

# GET /telephony/config/devices/availableMembers

**API:** Webex Cloud Calling
**Área:** DECT Devices Settings
**operationId:** `Search Available Members`

## Resumen
Search Available Members

## Descripción
List the members that are available to be assigned to DECT handset lines.

DECT handset lines can be assigned to people, places, or virtual lines within the organization. This API helps administrators identify which members are eligible for assignment to DECT devices.

This requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): Search members in this organization.
- `start` [query] (number): Specifies the offset from the first result that you want to fetch.
- `max` [query] (number): Specifies the maximum number of records that you want to fetch.
- `memberName` [query] (string): Search (Contains) numbers based on member name.
- `phoneNumber` [query] (string): Search (Contains) based on number.
- `extension` [query] (string): Search (Contains) based on extension.
- `order` [query] (string): Sort the list of available members on the device in ascending order by name, using either last name `lname` or first name `fname`. Default sort is the last name in ascending order.
- `locationId` [query] (string): List members for the location ID.
- `excludeVirtualLine` [query] (boolean): If true, search results will exclude virtual lines in the member list. NOTE: Virtual lines cannot be assigned as the primary line.
- `usageType` [query] (string): Search for members eligible to become the owner of the device, or share line on the device.

## Respuestas
- **200**: OK
  - `members` (array):
    - `id` (string) **(requerido)**: Unique identifier for the member.
    - `firstName` (string): First name of the member.
    - `lastName` (string): Last name of the member.
    - `phoneNumber` (string): Phone Number of the member.
    - `extension` (string): Extension of the member.
    - `lineType` (string) **(requerido)**: * `PRIMARY` - Primary line for the member.  * `SHARED_CALL_APPEARANCE` - Shared line for the member. A shared line allows users to receive and place calls to and from another user's extension, using their own device. Valores: PRIMARY, SHARED_CALL_APPEARANCE.
    - `memberType` (string) **(requerido)**: * `PEOPLE` - Indicates the associated member is a person.  * `PLACE` - Indicates the associated member is a workspace. Valores: PEOPLE, PLACE.
    - `location` (object) **(requerido)**:
      - `id` (string) **(requerido)**: Location identifier associated with the members.
      - `name` (string) **(requerido)**: Location name associated with the member.
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
