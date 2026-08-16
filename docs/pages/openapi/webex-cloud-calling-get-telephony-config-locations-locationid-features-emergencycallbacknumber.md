---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-features-emergencycallbacknumber
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/locations/{locationId}/features/emergencyCallbackNumber
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.622073+00:00
---

# GET /telephony/config/locations/{locationId}/features/emergencyCallbackNumber

**API:** Webex Cloud Calling
**Área:** Location Call Settings
**operationId:** `Get a Location Emergency callback number`

## Resumen
Get a Location Emergency callback number

## Descripción
Get location emergency callback number.

* To retrieve location callback number requires a full, user or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) **(requerido)**: Update location attributes for this location.
- `orgId` [query] (string): Update location attributes for this organization.

## Respuestas
- **200**: OK
  - `locationInfo` (object) **(requerido)**: Data relevant to this location.
    - `phoneNumber` (string): The location DN.
    - `name` (string): The name of the location.
    - `effectiveLevel` (string): * `LOCATION_NUMBER` - Location TN.  * `LOCATION_MEMBER_NUMBER` - Assigned number of a user, workspace, virtual line or hunt group in the location.  * `NONE` - When no other option is selected. Valores: LOCATION_NUMBER, LOCATION_MEMBER_NUMBER, NONE.
    - `effectiveValue` (string) **(requerido)**: Location calling line ID (CLID) number. Avaliable only when number is present and quality would be invalid.
    - `quality` (string) **(requerido)**: * `RECOMMENDED` - An activated number, associated with a User or Workspace.  * `NOT_RECOMMENDED` - An activated number, associated with anything else, like Auto Attendant or Hunt Group.  * `INVALID` - An inactive or non-existent number. Valores: RECOMMENDED, NOT_RECOMMENDED, INVALID.
  - `locationMemberInfo` (object) **(requerido)**: Data relevant to the user/place/virtual line/hunt group (member) selected for ECBN.
    - `phoneNumber` (string): The member DN.
    - `firstName` (string): The member first name.
    - `lastName` (string): The member last name.
    - `memberId` (string): Member ID of user/place/virtual line/hunt group within the location.
    - `memberType` (string): * `PEOPLE` - Associated member is a person.  * `PLACE` - Associated member is a workspace.  * `VIRTUAL_LINE` - Associated member is a virtual line.  * `HUNT_GROUP` - Associated member is a hunt group. Valores: PEOPLE, PLACE, VIRTUAL_LINE, HUNT_GROUP.
    - `effectiveLevel` (string): * `LOCATION_NUMBER` - Location TN.  * `LOCATION_MEMBER_NUMBER` - Assigned number of a user, workspace, virtual line or hunt group in the location.  * `NONE` - When no other option is selected. Valores: LOCATION_NUMBER, LOCATION_MEMBER_NUMBER, NONE.
    - `effectiveValue` (string) **(requerido)**: Location CLID number. Avaliable only when number is present and quality would be invalid.
    - `quality` (string) **(requerido)**: * `RECOMMENDED` - An activated number, associated with a User or Workspace.  * `NOT_RECOMMENDED` - An activated number, associated with anything else, like Auto Attendant or Hunt Group.  * `INVALID` - An inactive or non-existent number. Valores: RECOMMENDED, NOT_RECOMMENDED, INVALID.
  - `selected` (string) **(requerido)**: * `LOCATION_NUMBER` - Location TN.  * `LOCATION_MEMBER_NUMBER` - Assigned number of a user, workspace, virtual line or hunt group in the location. Valores: LOCATION_NUMBER, LOCATION_MEMBER_NUMBER.
  - `elinExpiryTimeMinutes` (integer) **(requerido)**: ELIN (Emergency Location Identification Number) provides location-specific callback information to emergency responders. This field indicates the time in minutes that the ELIN association remains active after being established. The default value is 60 minutes, and the valid values range from 10 to 1440 minutes.
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
