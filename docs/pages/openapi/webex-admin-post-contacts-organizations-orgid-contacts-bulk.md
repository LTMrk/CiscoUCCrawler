---
doc_id: webex-admin-post-contacts-organizations-orgid-contacts-bulk
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: POST
path: /contacts/organizations/{orgId}/contacts/bulk
operation_id: Bulk Create or Update Contacts
tags: Organization Contacts
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.569544+00:00
---

# POST /contacts/organizations/{orgId}/contacts/bulk

**API:** Webex Admin
**Área:** Organization Contacts
**operationId:** `Bulk Create or Update Contacts`

## Resumen
Bulk Create or Update Contacts

## Descripción
Create or update contacts in bulk. Update an existing contact by specifying the contact ID in the `contactId` parameter in the request body.

## Parámetros
- `orgId` [path] (string) (**requerido**): Webex Identity assigned organization identifier for the user's organization or the organization he manages.

## Cuerpo de la petición (application/json)
- `schemas` (string) (**requerido**): "urn:cisco:codev:identity:contact:core:1.0".
- `contacts` (array) (**requerido**): Contains a list of contacts to be created/updated.
  - `contactId` (string): Use this to update an existing contact.
  - `displayName` (string): The full name of the contact.
  - `firstName` (string): The first name of the contact.
  - `lastName` (string): The last name of the contact.
  - `companyName` (string): The company the contact is working for.
  - `title` (string): The contact's title.
  - `address` (string): Contact's address.
  - `avatarURL` (string): The URL to the person's avatar in PNG format.
  - `primaryContactMethod` (string): The contact's primary contact method. Valores: SIPADDRESS, EMAIL, PHONE, IMS.
  - `source` (string) (**requerido**): Where the data come from. Valores: CH, Webex4Broadworks.
  - `emails` (array): A list of the user's email addresses with an indicator of the user's primary email address.
    - `value` (string): The email address.
    - `type` (string): The type of the email. Valores: work, home, room, other.
    - `primary` (boolean): A Boolean value indicating the email status.
  - `phoneNumbers` (array): A list of user's phone numbers with an indicator of primary to specify the user's main number.
    - `value` (string): The phone number.
    - `type` (string): The types of phone numbers. Valores: work, home, mobile, work_extension, fax, pager, other.
    - `primary` (boolean): A Boolean value indicating the phone number's primary status.
  - `sipAddresses` (array): The sipAddress values for the user.
    - `value` (string) (**requerido**): The sipAddress value.
    - `type` (string): The type of the sipAddress. Valores: enterprise, cloud-calling, personal-room.
    - `primary` (boolean): Designate the primary sipAddress.
  - `ims` (array): Instant messaging addresses for the user.
    - `value` (string): The IMS account value.
    - `type` (string): The type of the IMS. Valores: aim, cucm-jid, gtalk, icq, msn, qq, skype, webex-messenger-jid, webex-squared-jid, xmpp, yahoo, microsoft-sip-uri, xmpp-fed-jid.
    - `primary` (boolean): A Boolean value indicating the IMS account status.

### Ejemplo — petición
```json
{
  "schemas": "urn:cisco:codev:identity:contact:core:1.0",
  "contacts": [
    {
      "contactId": "6847ee0f-5e9c-4403-9f0e-0aa8552f7828",
      "displayName": "John Andersen",
      "firstName": "John",
      "lastName": "Andersen",
      "companyName": "Cisco Systems",
      "title": "GM",
      "address": "{\\\"city\\\" : \\\"Milpitas\\\", \\\"country\\\" : \\\"US\\\", \\\"street\\\" : \\\"1099 Bird Ave.\\\", \\\"zipCode\\\" : \\\"99212\\\"}",
      "avatarURL": "https://avatar-prod-us-east-2.webexcontent.com/default_avatar~1600",
      "primaryContactMethod": "SIPADDRESS",
      "source": "Webex4Broadworks",
      "emails": [
        {
          "value": "user1@example.home.com",
          "type": "home",
          "primary": false
        }
      ],
      "phoneNumbers": [
        {
          "value": "400 123 1234",
          "type": "work",
          "primary": true
        }
      ],
      "sipAddresses": [
        {
          "value": "sipAddress value1",
          "type": "enterprise",
          "primary": true
        }
      ],
      "ims": [
        {
          "value": "aim_account_ID",
          "type": "aim",
          "primary": true
        }
      ]
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X POST '/contacts/organizations/<orgId>/contacts/bulk' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"schemas": "<schemas>", "contacts": []}'
```

## Respuestas correctas
**200**: OK
- `contacts` (array): Array of contact successfully created.
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
- `failedContacts` (array): Array of contacts that failed creation.
  - `id` (string): Bulk ID of the contact object that failed creation.
  - `errorCode` (number): HTTP Response code for the contact creation failure.
  - `errorMessage` (string): Error message for the contact creation failure.
- `orgId` (string): Organization ID in which the contacts were created.

### Ejemplo — respuesta 200
```json
{
  "contacts": [
    {
      "schemas": "urn:cisco:codev:identity:contact:core:1.0",
      "meta": {
        "created": "2023-05-12T06:53:12.141Z",
        "lastModified": "2023-05-12T06:53:12.142Z"
      },
      "contactId": "5a521987-5407-4824-9389-d4ca82b85752",
      "displayName": "simizhan1",
      "emails": [
        {
          "type": "WORK",
          "value": "simizhan1@example.com"
        }
      ],
      "source": "CH",
      "isMigration": false,
      "orgId": "d23736ac-8055-433e-b85a-0fc55c96ead9"
    },
    null,
    null
  ],
  "failedContacts": [
    {
      "id": "1",
      "errorCode": "external.non.privilege",
      "errorMessage": "Caller is not authorized for source null, only sources [CH] are allowed",
      "statusCode": 403
    },
    {
      "id": "2",
      "errorCode": "external.non.privilege",
      "errorMessage": "Caller is not authorized for source null, only sources [CH] are allowed",
      "statusCode": 403
    }
  ],
  "orgId": "d23736ac-8055-433e-b85a-0fc55c96ead9"
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
The Webex Admin APIs provide comprehensive programmatic access to administrative functions for managing Webex organizations, users, licenses, and settings. These APIs enable automation of user provisioning, license assignment, compliance management, and audit event retrieval. Administrators can integrate with enterprise identity systems, enforce security policies, monitor usage, and streamline onboarding/offboarding processes. The APIs support granular control over organizational resources, making them ideal for large-scale deployments and custom admin tooling.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs