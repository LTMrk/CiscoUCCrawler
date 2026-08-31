---
doc_id: webex-cloud-calling-get-telephony-config-virtuallines
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/virtualLines
operation_id: Read the List of Virtual Lines
tags: Virtual Line Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.354616+00:00
---

# GET /telephony/config/virtualLines

**API:** Webex Cloud Calling
**Área:** Virtual Line Call Settings
**operationId:** `Read the List of Virtual Lines`

## Resumen
Read the List of Virtual Lines

## Descripción
List all Virtual Lines for the organization.

Virtual line is a capability in Webex Calling that allows administrators to configure multiple lines to Webex Calling users.

Retrieving this list requires a full, user, read-only, or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): List virtual lines for this organization.
- `locationId` [query] (array): Return the list of virtual lines matching these location ids. Example for multiple values - `?locationId=locId1&locationId=locId2`.
- `max` [query] (number): Limit the number of objects returned to this maximum count.
- `start` [query] (number): Start at the zero-based offset in the list of matching objects.
- `id` [query] (array): Return the list of virtual lines matching these virtualLineIds. Example for multiple values - `?id=id1&id=id2`.
- `ownerName` [query] (array): Return the list of virtual lines matching these owner names. Example for multiple values - `?ownerName=name1&ownerName=name2`.
- `phoneNumber` [query] (array): Return the list of virtual lines matching these phone numbers. Example for multiple values - `?phoneNumber=number1&phoneNumber=number2`.
- `locationName` [query] (array): Return the list of virtual lines matching the location names. Example for multiple values - `?locationName=loc1&locationName=loc2`.
- `order` [query] (array): Return the list of virtual lines based on the order. Default sort will be in an Ascending order. Maximum 3 orders allowed at a time. Example for multiple values - `?order=order1&order=order2`.
- `hasDeviceAssigned` [query] (boolean): If `true`, includes only virtual lines with devices assigned. When not explicitly specified, the default includes both virtual lines with devices assigned and not assigned.
- `hasExtensionAssigned` [query] (boolean): If `true`, includes only virtual lines with an extension assigned. When not explicitly specified, the default includes both virtual lines with extension assigned and not assigned.
- `hasDnAssigned` [query] (boolean): If `true`, includes only virtual lines with an assigned directory number, also known as a Dn. When not explicitly specified, the default includes both virtual lines with a Dn assigned and not assigned.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/virtualLines' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `virtualLines` (array) (**requerido**): Array of virtual lines.
  - `id` (string) (**requerido**): A unique identifier for the virtual line.
  - `lastName` (string): The last name of the virtual line.
  - `firstName` (string): The first name of the virtual line.
  - `callerIdLastName` (string): `callerIdLastName` for virtual line.
  - `callerIdFirstName` (string): `callerIdFirstName` for virtual line.
  - `callerIdNumber` (string): `callerIdNumber` for virtual line.
  - `externalCallerIdNamePolicy` (string) (**requerido**): `externalCallerIdNamePolicy` for the virtual line.  * `DIRECT_LINE` - Shows virtual lines Caller ID name.  * `LOCATION` - Shows virtual lines location name.  * `OTHER` - Allow virtual lines first/last name to be configured. Valores: DIRECT_LINE, LOCATION, OTHER.
  - `customExternalCallerIdName` (string): `customExternalCallerIdName` for virtual line.
  - `number` (object) (**requerido**): Calling details of virtual line.
    - `external` (string): Virtual Line external.  Either `external` or `extension` is mandatory.
    - `extension` (string): Virtual Line extension.  Either `external` or `extension` is mandatory.
    - `routingPrefix` (string): Routing prefix of location.
    - `esn` (string): Routing prefix + extension of a person or workspace.
    - `primary` (boolean) (**requerido**): Number is Primary or Alternative Number.
  - `location` (object) (**requerido**): Location details of virtual line.
    - `id` (string) (**requerido**): ID of location associated with virtual line.
    - `name` (string) (**requerido**): Name of location associated with virtual line.
  - `numberOfDevicesAssigned` (number) (**requerido**): Number of devices assigned to a virtual line.
  - `billingPlan` (string): Type of billing plan.

### Ejemplo — respuesta 200
```json
{
  "virtualLines": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1ZJUlRVQUxfUFJPRklMRS84ZDRkMDNlYS03NTUzLTQ0NTgtYmI4OS02YzExNzgyMzA4OWY",
      "lastName": "Smith",
      "firstName": "Bob",
      "callerIdLastName": "Smith",
      "callerIdFirstName": "Bob",
      "callerIdNumber": "+15558675311",
      "externalCallerIdNamePolicy": "DIRECT_LINE",
      "customExternalCallerIdName": "Bob",
      "number": {
        "external": "+15558675311",
        "extension": "6103",
        "routingPrefix": "1234",
        "esn": "12346103",
        "primary": true
      },
      "location": {
        "name": "Denver",
        "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzhmZjMwMjg2LWVhMzMtNDc2Ny1iMTBmLWQ2MWIyNzFhMDVlZg"
      },
      "numberOfDevicesAssigned": 1,
      "billingPlan": "BCOCP1"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1ZJUlRVQUxfUFJPRklMRS81NjMzZjU4OS1iNDQ0LTQ4ODYtODVjNy02MDljYWY3M2U4YzU",
      "lastName": "Smith",
      "firstName": "Charlie",
      "callerIdLastName": "Smith",
      "callerIdFirstName": "Charlie",
      "callerIdNumber": "+15558675312",
      "externalCallerIdNamePolicy": "DIRECT_LINE",
      "customExternalCallerIdName": "Charlie",
      "number": {
        "external": "+15558675312",
        "extension": "6102",
        "routingPrefix": "1234",
        "esn": "12346102",
        "primary": true
      },
      "location": {
        "name": "Denver",
        "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzhmZjMwMjg2LWVhMzMtNDc2Ny1iMTBmLWQ2MWIyNzFhMDVlZg"
    
  ... (truncado)
```
- Cabecera `Link`: 

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