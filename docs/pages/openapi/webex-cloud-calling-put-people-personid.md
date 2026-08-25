---
doc_id: webex-cloud-calling-put-people-personid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /people/{personId}
operation_id: Update a Person
tags: People
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.531414+00:00
---

# PUT /people/{personId}

**API:** Webex Cloud Calling
**Área:** People
**operationId:** `Update a Person`

## Resumen
Update a Person

## Descripción
Update details for a person, by ID.

Specify the person ID in the `personId` parameter in the URI. Only an admin can update a person details.

Include all details for the person. This action expects all user details to be present in the request. A common approach is to first [GET the person's details](/docs/api/v1/people/get-person-details), make changes, then PUT both the changed and unchanged values.

Admin users can include `Webex Calling` (BroadCloud) user details in the response by specifying `callingData` parameter as true.

When doing attendee management, to update a user from host role to an attendee for a site append `#attendee` to the respective `siteUrl` and remove the meeting host license for this site from the license array.
To update a person from an attendee role to a host for a site, add the meeting license for this site in the meeting array, and remove that site from the `siteurl` parameter.

To remove the attendee privilege for a user on a meeting site, remove the `sitename#attendee` from the `siteUrl`s array. The `showAllTypes` parameter must be set to `true`.

**NOTE**:

* When assigning a Webex Calling license, either a telephone number or extension must already be assigned to the person or provided in the request payload.

* When `callingData` is set to `true`, a Webex Calling license must be included in the `licenses` array.

* The `locationId` can only be set when assigning a calling license to a user. It cannot be changed if a user is already an existing calling user.

* The `extension` field should be used to update the Webex Calling extension for a person. The extension value should not include the location routing prefix. The `work_extension` type in the `phoneNumbers` object as seen in the response payload of [List People](/docs/api/v1/people/list-people) or [Get Person Details](/docs/api/v1/people/get-person-details), cannot be used to set the Webex Calling extension for a person.

* When updating a user with multiple email addresses using a PUT request, ensure that the primary email address is listed first in the array. Note that the order of email addresses returned by a GET request is not guaranteed..

* The People API is a combination of several microservices, each responsible for specific attributes of a person. As a result, a PUT request that returns an error response code may still have altered some values of the person's data. Therefore, it is recommended to perform a GET request after encountering an error to verify the current state of the resource. 

* Some licenses are implicitly assigned by the system and cannot be admin controlled. They are necessary for the baseline function of the Webex system. If you get an error about implicitly assigned licensed that cannot be removed, please ensure you have the corresponding license in your PUT request.

* When assigning multiple licenses in a single request, the system will assign all valid and available licenses. If any requested licenses cannot be assigned, the operation will continue with the remaining licenses. As a result, it is possible that not all requested licenses are assigned to the user.

## Parámetros
- `personId` [path] (string) (**requerido**): A unique identifier for the person.
- `callingData` [query] (boolean): Include Webex Calling user details in the response. Por defecto: False.
- `showAllTypes` [query] (boolean): Include additional user data like `#attendee` role.
- `minResponse` [query] (boolean): Set to `true` to improve performance by omitting person details in the response. If unsuccessful the response will have optional error details. Por defecto: False.

## Cuerpo de la petición (application/json)
- `emails` (array): The email addresses of the person. Only one email address is allowed per person.
- `phoneNumbers` (array): Phone numbers for the person. Can only be set for Webex Calling. Needs a Webex Calling license.
  - `type` (string): The type of phone number. Valores: work.
  - `value` (string): The phone number.
- `extension` (string): Webex Calling extension of the person. This is only settable for a person with a Webex Calling license.
- `locationId` (string): The ID of the location for this person.
- `displayName` (string) (**requerido**): The full name of the person.
- `firstName` (string): The first name of the person.
- `lastName` (string): The last name of the person.
- `nickName` (string): The nickname of the person if configured. This cannot be overwritten and instead will be set to the firstName automatically in update requests.
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
- `siteUrls` (array): One or several site names where this user has a role (host or attendee). Append `#attendee` to the site name to designate the attendee role on that site.
- `loginEnabled` (boolean): Whether or not the user is allowed to use Webex. This property is only accessible if the authenticated user is an admin user for the person's organization.

### Ejemplo — petición
```json
{
  "emails": [
    "john.andersen@example.com"
  ],
  "phoneNumbers": [
    {
      "type": "work",
      "value": "408 526 7209"
    }
  ],
  "extension": "133",
  "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzYzNzE1",
  "displayName": "John Andersen",
  "firstName": "John",
  "lastName": "Andersen",
  "nickName": "John",
  "avatar": "https://1efa7a94ed21783e352-c62266528714497a17239ececf39e9e2.ssl.cf1.rackcdn.com/V1~54c844c89e678e5a7b16a306bc2897b9~wx29yGtlTpilEFlYzqPKag==~1600",
  "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
  "roles": [
    "Y2lzY29zcGFyazovL3VzL1JPTEUvOTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh,Y2lzY29zcGFyazovL3VzL1JPTEUvOTZhYmMyYWEtM2RjYy0xMWU1LWIyNjMtMGY0NTkyYWRlZmFi"
  ],
  "licenses": [
    "Y2lzY29zcGFyazovL3VzL0xJQ0VOU0UvOTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh,Y2lzY29zcGFyazovL3VzL0xJQ0VOU0UvOTZhYmMyYWEtM2RjYy0xMWU1LWIyNjMtMGY0NTkyYWRlZmFi"
  ],
  "department": "Sales",
  "manager": "John Duarte",
  "managerId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80ZGEzYTI0OC05YjBhLTQxMDgtODU0NC1iNTQwMzEyZTU2M2E",
  "title": "GM",
  "addresses": [
    {
      "type": "work",
      "country": "US",
      "locality": "Milpitas",
      "region": "California",
      "streetAddress": "1099 Bird Ave.",
      "postalCode": "99212"
    }
  ],
  "siteUrls": [
    "mysite.webex.com#attendee"
  ],
  "loginEnabled": true
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/people/<personId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"displayName": "<displayName>"}'
```

## Respuestas correctas
**200**: OK
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
- `loginEnabled` (string): Whether or not the user is allowed to use Webex. This property is only returned if the authenticated user is an admin user for the person's organization.  * `true` - The person _can_ log into Webex.  * `false` - The person _cannot_ log into Webex. Valores: true, false.
- `type` (string): The type of person account, such as person or bot.  * `person` - Account belongs to a person.  * `bot` - Account is a bot user.  * `appuser` - Account is a [guest user](/docs/guest-issuer). Valores: person, bot, appuser.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
  "emails": [
    "john.andersen@example.com"
  ],
  "phoneNumbers": [
    {
      "type": "work",
      "value": "+1 408 526 7209",
      "primary": true
    }
  ],
  "extension": "133",
  "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzYzNzE1",
  "displayName": "John Andersen",
  "nickName": "John",
  "firstName": "John",
  "lastName": "Andersen",
  "avatar": "https://1efa7a94ed21783e352-c62266528714497a17239ececf39e9e2.ssl.cf1.rackcdn.com/V1~54c844c89e678e5a7b16a306bc2897b9~wx29yGtlTpilEFlYzqPKag==~1600",
  "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
  "roles": [
    "Y2lzY29zcGFyazovL3VzL1JPTEUvOTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh,Y2lzY29zcGFyazovL3VzL1JPTEUvOTZhYmMyYWEtM2RjYy0xMWU1LWIyNjMtMGY0NTkyYWRlZmFi"
  ],
  "licenses": [
    "Y2lzY29zcGFyazovL3VzL0xJQ0VOU0UvOTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh,Y2lzY29zcGFyazovL3VzL0xJQ0VOU0UvOTZhYmMyYWEtM2RjYy0xMWU1LWIyNjMtMGY0NTkyYWRlZmFi"
  ],
  "department": "Sales",
  "manager": "John Duarte",
  "managerId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80ZGEzYTI0OC05YjBhLTQxMDgtODU0NC1iNTQwMzEyZTU2M2E",
  "title": "GM",
  "addresses": [
    {
      "type": "work",
      "country": "US",
      "locality": "Milpitas",
      "region": "California",
      "streetAddress": "1099 Bird Ave.",
      "postalCode": "99212"
    }
  ],
  "created": "2015-10-18T14:26:16.000Z",
  "las
  ... (truncado)
```
**204**: No Content

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
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs