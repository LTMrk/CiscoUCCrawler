---
doc_id: webex-admin-get-people
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
method: GET
path: /people
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.154628+00:00
---

# GET /people

**API:** Webex Admin
**Área:** People
**operationId:** `List People`

## Resumen
List People

## Descripción
List people in your organization. For most users, either the `email` or `displayName` parameter is required. Admin users can omit these fields and list all users in their organization.

Response properties associated with a user's presence status, such as `status` or `lastActivity`, will only be returned for people within your organization or an organization you manage. Presence information will not be returned if the authenticated user has [disabled status sharing](https://help.webex.com/nkzs6wl/). Calling /people frequently to poll `status` information for a large set of users will quickly lead to `429` errors and throttling of such requests and is therefore discouraged.

Admin users can include `Webex Calling` (BroadCloud) user details in the response by specifying `callingData` parameter as `true`. Admin users can list all users in a location. Admin users will receive an enriched payload with additional administrative fields like `licenses`,`roles`, `locations` etc. These fields are shown when accessing a user via GET /people/{id}, not when doing a GET /people?id=

Lookup by `email` is only supported for people within the same org or where a partner admin relationship is in place.

Lookup by `roles` is only supported for Admin users for the people within the same org.

Long result sets will be split into [pages](/docs/basics#pagination).

## Parámetros
- `email` [query] (string): List people with this email address. For non-admin requests, either this or `displayName` are required. With the exception of partner admins and a managed org relationship, people lookup by email is only available for users in the same org.
- `displayName` [query] (string): List people whose name starts with this string. For non-admin requests, either this or email are required.
- `id` [query] (string): List people by ID. Accepts up to 85 person IDs separated by commas. If this parameter is provided then presence information (such as the `lastActivity` or `status` properties) will not be included in the response.
- `orgId` [query] (string): List people in this organization. Only admin users of another organization (such as partners) may use this parameter.
- `roles` [query] (string): List of roleIds separated by commas.
- `callingData` [query] (boolean): Include Webex Calling user details in the response.
- `locationId` [query] (string): List people present in this location.
- `max` [query] (number): Limit the maximum number of people in the response. If `callingData`=true, then `max` will not be more than 100. If `locationId` is specified then `max` will not be more than 50.
- `excludeStatus` [query] (boolean): Omit people status/availability to enhance query performance.

## Respuestas
- **200**: OK
  - `items` (array): An array of person objects.
    - `id` (string): A unique identifier for the person.
    - `emails` (array): The email addresses of the person.
    - `phoneNumbers` (array): Phone numbers for the person.
      - `type` (string): The type of phone number.  * `work` - Work phone number of the person.  * `work_extension` - Work extension of the person. For the Webex Calling person, the value will have a routing prefix along with the extension.  * `mobile` - Mobile number of the person.  * `fax` - FAX number of the person. Valores: work, work_extension, mobile, fax.
      - `value` (string): The phone number.
      - `primary` (boolean): Primary number for the person.
    - `extension` (string): The Webex Calling extension for the person. Only applies to a person with a Webex Calling license.
    - `locationId` (string): The ID of the location for this person retrieved from BroadCloud.
    - `displayName` (string): The full name of the person.
    - `nickName` (string): The nickname of the person if configured. If no nickname is configured for the person, this field will not be present.
    - `firstName` (string): The first name of the person.
    - `lastName` (string): The last name of the person.
    - `avatar` (string): The URL to the person's avatar in PNG format.
    - `orgId` (string): The ID of the organization to which this person belongs.
    - `roles` (array): An array of role strings representing the roles to which this admin user belongs.
    - `licenses` (array): An array of license strings allocated to this person.
    - `department` (string): The business department the user belongs to.
    - `manager` (string): A manager identifier.
    - `managerId` (string): Person ID of the manager.
    - `title` (string): The person's title.
    - `addresses` (array): A person's addresses.
      - `type` (string): The type of address.
      - `country` (string): The user's country.
      - `locality` (string): The user's locality, often city.
      - `region` (string): The user's region, often state.
      - `streetAddress` (string): The user's street.
      - `postalCode` (string): The user's postal or zip code.
    - `created` (string): The date and time the person was created.
    - `lastModified` (string): The date and time the person was last changed.
    - `timezone` (string): The time zone of the person if configured. If no timezone is configured on the account, this field will not be present.
    - `lastActivity` (string): The date and time of the person's last activity within Webex. This will only be returned for people within your organization or an organization you manage. Presence information will not be shown if the authenticated user has [disabled status sharing](https://help.webex.com/nkzs6wl/).
    - `siteUrls` (array): One or several site names where this user has a role (host or attendee).
    - `sipAddresses` (array): The user's SIP addresses. Read-only.
      - `type` (string): The type of SIP address.  * `personal-room` - Personal room address.  * `enterprise` - Enterprise address.  * `cloud-calling` - Cloud calling address. Valores: personal-room, enterprise, cloud-calling.
      - `value` (string): The SIP address.
      - `primary` (boolean): Primary SIP address of the person.
    - `xmppFederationJid` (string): Identifier for intra-domain federation with other XMPP based messenger systems.
    - `status` (string): The current presence status of the person. This will only be returned for people within your organization or an organization you manage. Presence information will not be shown if the authenticated user has [disabled status sharing](https://help.webex.com/nkzs6wl/). Presence status is different from Control Hub's "Last Service Access Time" which indicates the last time an oAuth token was issued for this user.  * `active` - Active within the last 10 minutes.  * `call` - The user is in a call.  * `DoNotDisturb` - The user has manually set their status to "Do Not Disturb".  * `inactive` - Last activity occurred more than 10 minutes ago.  * `meeting` - The user is in a meeting.  * `OutOfOffice` - The user or a Hybrid Calendar service has indicated that they are "Out of Office".  * `pending` - The user has never logged in; a status cannot be determined.  * `presenting` - The user is sharing content.  * `unknown` - The user’s status could not be determined. Valores: active, call, DoNotDisturb, inactive, meeting, OutOfOffice, pending, presenting, unknown.
    - `invitePending` (string): Whether or not an invite is pending for the user to complete account activation. This property is only returned if the authenticated user is an admin user for the person's organization.  * `true` - The person has been invited to Webex but has not created an account.  * `false` - An invite is not pending for this person. Valores: true, false.
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
