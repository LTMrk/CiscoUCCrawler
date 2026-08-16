---
doc_id: webex-admin-get-identity-scim-v2-users-me
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
method: GET
path: /identity/scim/v2/Users/me
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.162643+00:00
---

# GET /identity/scim/v2/Users/me

**API:** Webex Admin
**Área:** SCIM 2 Users
**operationId:** `Get Me`

## Resumen
Get Me

## Descripción
<br/>

**Authorization**

OAuth token rendered by Identity Broker.

<br/>

One of the following OAuth scopes is required:

- `identity:people_rw`

- `identity:people_read`

<br/>

The API can be used by any user to retrieve user information using their own access token.

<br/>

## Respuestas
- **200**: OK
  - `schemas` (array) **(requerido)**: Input JSON schemas.
  - `id` (string) **(requerido)**: Webex Identity assigned user identifier.
  - `userName` (string) **(requerido)**: A unique identifier for the user and authenticates the user in Webex.  This must be set to the user's primary email address.  No other user in Webex may have the same `userName` value and thus this value is required to be unique within Webex.
  - `active` (boolean): A boolean value of "true" or "false" indicating whether the user is allowed to login in Webex.
  - `roles` (array): List of roles assigned to the user.
    - `value` (string): CI Role
    - `type` (string): name
    - `display` (string): A human-readable name, primarily used for display purposes.
  - `name` (object): The components of the user's real name.
    - `givenName` (string): The given name of the user, or first name in most Western languages (e.g., "Sarah" given the full name "Ms. Sarah J Henderson, III").
    - `familyName` (string): The family name of the user, or last name in most Western languages (e.g., "Henderson" given the full name "Ms. Sarah J Henderson, III").
    - `middleName` (string): The middle name(s) of the user (e.g., "Jane" given the full name "Ms. Sarah J Henderson, III").
    - `honorificPrefix` (string): The honorific prefix(es) of the user, or title in most Western languages (e.g., "Ms." given the full name "Ms. Sarah J Henderson, III").
    - `honorificSuffix` (string): The honorific suffix(es) of the user, or suffix in most Western languages (e.g., "III" given the full name "Ms. Sarah J Henderson, III").
  - `displayName` (string): The name displayed for the user in Webex.
  - `nickName` (string): A casual name of the user. For example, Bob when the user's formal name is Robert.
  - `emails` (array): A list of the user's email addresses, including primary and alternative emails. The primary work email address must match the value of the user's username.
    - `value` (string): The email address.
    - `type` (string): The type of the email. Valores: work, home, room, other.
    - `display` (string): A human-readable description, primarily used for display purposes.
    - `primary` (boolean): Email status boolean value. If the type is work and primary is true, the value must equal `userName`.
  - `userType` (string) **(requerido)**:  Valores: user, room, external_calling, calling_service.
  - `profileUrl` (string): A fully qualified URL pointing to a page representing the user's online profile.
  - `title` (string): The user's business title.  Examples of a title is "Business Manager". "Senior Accountant", "Engineer" etc.
  - `preferredLanguage` (string): User's preferred language. Acceptable values for this field are based on the [ISO-696](http://www.loc.gov/standards/iso639-2/php/code_list.php) and [ISO-3166](https://www.iso.org/obp/ui/#search) with the 2 letter language code followed by an _ and then the 2 letter country code.  Examples are:                                      en_US : for United States English or fr_FR for Parisian French.
  - `locale` (string): The user's locale which represents the user's currency, time format, and numerical representations.  Acceptable values for this field are based on the [ISO-696](http://www.loc.gov/standards/iso639-2/php/code_list.php) and [ISO-3166](https://www.iso.org/obp/ui/#search) with the 2 letter language code followed by an _ and then the 2 letter country code.  Examples are:                           en_US : for United States English or fr_FR for Parisian French.
  - `externalId` (string): User identifier provided by an external provisioning source.
  - `timezone` (string): The user's time zone specified in the [IANA timezone](https://nodatime.org/timezones) timezone format, for example, "America/Los_Angeles".
  - `phoneNumbers` (array): A list of user's phone numbers.
    - `value` (string): phone number.
    - `type` (string): We support the following phone number types: 'mobile', 'work', 'fax', 'work_extension', 'alternate1', 'alternate2'.  Alternate 1 and Alternate 2 are types inherited from Webex meeting sites. Valores: work, home, mobile, work_extension, fax, pager, other.
    - `display` (string): A human-readable name, primarily used for display purposes.
    - `primary` (boolean): A Boolean value for phone number's primary status.
  - `photos` (array): A list of photo objects for the user.
    - `value` (string): photo link.
    - `type` (string): The type of the photo Valores: photo, thumbnail, resizable.
    - `display` (string): A human-readable description, primarily used for display purposes.
    - `primary` (boolean): A Boolean value for the photo usage status.
  - `addresses` (array): User's physical mailing address.
    - `type` (string): The type of the address.
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
