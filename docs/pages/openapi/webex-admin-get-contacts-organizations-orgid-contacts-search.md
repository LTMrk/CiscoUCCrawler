---
doc_id: webex-admin-get-contacts-organizations-orgid-contacts-search
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: GET
path: /contacts/organizations/{orgId}/contacts/search
operation_id: List Contacts
tags: Organization Contacts
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.569172+00:00
---

# GET /contacts/organizations/{orgId}/contacts/search

**API:** Webex Admin
**Área:** Organization Contacts
**operationId:** `List Contacts`

## Resumen
List Contacts

## Descripción
List contacts in the organization. The default limit is `100`.

`keyword` can be the value of "displayName", "firstName", "lastName", "email". An empty string of `keyword` means get all contacts.

`groupIds` is a comma separated list group IDs. Results are filtered based on those group IDs.

Long result sets will be split into [pages](/docs/basics#pagination).

## Parámetros
- `orgId` [path] (string) (**requerido**): The organization ID.
- `keyword` [query] (string): List contacts with a keyword.
- `source` [query] (string): List contacts with source.
- `limit` [query] (number): Limit the maximum number of contact in the response.         + Default: 100
- `groupIds` [query] (array): Filter contacts based on groups.

## Ejemplo de invocación
```bash
curl -X GET '/contacts/organizations/<orgId>/contacts/search' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `result` (array): An array of contact objects.
  - `schemas` (string) (**requerido**): "urn:cisco:codev:identity:contact:core:1.0".
  - `meta` (object) (**requerido**):
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
  - `source` (string) (**requerido**): Where the data come from. Valores: CH, Webex4Broadworks.
  - `emails` (array): A list of the user's email addresses with an indicator of the user's primary email address.
    - `value` (string): The email address.
    - `type` (string): The type of the email. Valores: work, home, room, other.
    - `primary` (boolean): A Boolean value indicating the email status.
  - `phoneNumbers` (array): A list of user's phone numbers with an indicator of primary to specify the user's main number.
    - `value` (string): The phone number.
    - `type` (string): The types of the phone numbers. Valores: work, home, mobile, work_extension, fax, pager, other.
    - `primary` (boolean): A Boolean value indicating the phone number's primary status.
  - `sipAddresses` (array): The sipAddress values for the user.
    - `value` (string) (**requerido**): The sipAddress value.
    - `type` (string): The type of the sipAddress. Valores: enterprise, cloud-calling, personal-room.
    - `primary` (boolean): Designate the primary sipAddress.
  - `ims` (array): Instant messaging addresses for the user.
    - `value` (string): The IMS account value.
    - `type` (string): The type of the IMS. Valores: aim, cucm-jid, gtalk, icq, msn, qq, skype, webex-messenger-jid, webex-squared-jid, xmpp, yahoo, microsoft-sip-uri, xmpp-fed-jid.
    - `primary` (boolean): A Boolean value indicating the IMS account status.
  - `isMigration` (boolean): Indicates if this contact is part of a migration.
  - `orgId` (string): The organization ID that the contact belongs to.
  - `groupIds` (array): Groups associated with the contact.
- `start` (number): Start at the zero-based offset in the list of matching contacts.
- `limit` (number): Limit the number of contacts returned to this maximum count.
- `total` (number): Total number of contacts returned in search results.

### Ejemplo — respuesta 200
```json
{
  "result": [
    {
      "schemas": "urn:cisco:codev:identity:contact:core:1.0",
      "meta": {
        "created": "2023-05-11T01:59:38.398Z",
        "lastModified": "2023-05-11T01:59:38.398Z"
      },
      "contactId": "441d0fa5-7fa0-491e-b27a-f017896c0bab",
      "firstName": "Simic",
      "lastName": "Zhang",
      "companyName": "Cisco Systems",
      "title": "Product Manager",
      "address": "{\"city\" : \"Milpitas\", \"country\" : \"US\", \"street\" : \"1099 Bird Ave.\", \"zipCode\" : \"99212\"}",
      "avatarURL": "https://avatar-prod-us-east-2.webexcontent.com/default_avatar~1600",
      "displayName": "Logan",
      "addressInfo": {
        "city": "Milpitas",
        "country": "US",
        "street": "1099 Bird Ave.",
        "zipCode": "99212"
      },
      "primaryContactMethod": "EMAIL",
      "phoneNumbers": [
        {
          "type": "work",
          "value": "20134319"
        }
      ],
      "emails": [
        {
          "type": "work",
          "value": "simizhan@example.com"
        }
      ],
      "sipAddresses": [
        {
          "type": "work",
          "value": "sip://mysip1231233"
        }
      ],
      "ims": [
        {
          "type": "work",
          "value": "87003922"
        }
      ],
      "source": "CH",
      "isMigration": false,
      "orgId": "d23736ac-8055-433e-b85a-0fc55c96ead9",
      "groupIds": [
        "b3e594aa-19ea-488a-9d42-f811e272f4bd"
      ]
    }
  ],
  "start": 0,
  "limit": 1000,
  "total":
  ... (truncado)
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
The Webex Admin APIs provide comprehensive programmatic access to administrative functions for managing Webex organizations, users, licenses, and settings. These APIs enable automation of user provisioning, license assignment, compliance management, and audit event retrieval. Administrators can integrate with enterprise identity systems, enforce security policies, monitor usage, and streamline onboarding/offboarding processes. The APIs support granular control over organizational resources, making them ideal for large-scale deployments and custom admin tooling.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs