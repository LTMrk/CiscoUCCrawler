---
doc_id: webex-admin-get-contacts-organizations-orgid-contacts-contactid
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
method: GET
path: /contacts/organizations/{orgId}/contacts/{contactId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.152424+00:00
---

# GET /contacts/organizations/{orgId}/contacts/{contactId}

**API:** Webex Admin
**Área:** Organization Contacts
**operationId:** `Get a Contact`

## Resumen
Get a Contact

## Descripción
Shows details for an organization contact by ID.
Specify the organization ID in the `orgId` parameter in the URI, and specify the contact ID in the `contactId` parameter in the URI.

**NOTE**:
The `orgId` used in the path for this API are the org UUIDs. They follow a xxxx-xxxx-xxxx-xxxx pattern. If you have an orgId in base64 encoded format (starting with Y2.....) you need to base64 decode the id and extract the UUID from the slug, before you use it in your API call.

## Parámetros
- `orgId` [path] (string) **(requerido)**: Webex Identity assigned organization identifier for the user's organization or the organization he manages.
- `contactId` [path] (string) **(requerido)**: The contact ID.

## Respuestas
- **200**: OK
  - `schemas` (string) **(requerido)**: "urn:cisco:codev:identity:contact:core:1.0".
  - `meta` (object) **(requerido)**:
    - `created` (string): The date and time the contact was created.
    - `lastModified` (string): The date and time the contact was last changed.
  - `contactId` (string): The unique identifier for the contact.
  - `displayName` (string): The full name of the contact.
  - `firstName` (string): The first name of the contact.
  - `lastName` (string): The last name of the contact.
  - `companyName` (string): The company the contact is working for.
  - `title` (string): The contact's title.
  - `address` (string): Contact's address.
  - `avatarURL` (string): The URL to the person's avatar in PNG format.
  - `addressInfo` (object): Structured address information.
    - `city` (string): The city.
    - `country` (string): The country.
    - `street` (string): The street address.
    - `zipCode` (string): The ZIP code.
  - `primaryContactMethod` (string): The contact's primary contact method. Valores: SIPADDRESS, EMAIL, PHONE, IMS.
  - `source` (string) **(requerido)**: Where the data come from. Valores: CH, Webex4Broadworks.
  - `emails` (array): A list of the user's email addresses with an indicator of the user's primary email address.
    - `value` (string): The email address.
    - `type` (string): The type of the email. Valores: work, home, room, other.
    - `primary` (boolean): A Boolean value indicating the email status.
  - `phoneNumbers` (array): A list of user's phone numbers with an indicator of primary to specify the user's main number.
    - `value` (string): The phone number.
    - `type` (string): The types of the phone numbers. Valores: work, home, mobile, work_extension, fax, pager, other.
    - `primary` (boolean): A Boolean value indicating the phone number's primary status.
  - `sipAddresses` (array): The sipAddress values for the user.
    - `value` (string) **(requerido)**: The sipAddress value.
    - `type` (string): The type of the sipAddress. Valores: enterprise, cloud-calling, personal-room.
    - `primary` (boolean): Designate the primary sipAddress.
  - `ims` (array): Instant messaging addresses for the user.
    - `value` (string): The IMS account value.
    - `type` (string): The type of the IMS. Valores: aim, cucm-jid, gtalk, icq, msn, qq, skype, webex-messenger-jid, webex-squared-jid, xmpp, yahoo, microsoft-sip-uri, xmpp-fed-jid.
    - `primary` (boolean): A Boolean value indicating the IMS account status.
  - `isMigration` (boolean): Indicates if this contact is part of a migration.
  - `orgId` (string): The organization ID that the contact belongs to.
  - `groupIds` (array): Groups associated with the contact.
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
