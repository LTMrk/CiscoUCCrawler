---
doc_id: webex-device-get-deviceconfigurations
source: webex-openapi-specs/public-spec/webex-device.json
api: Webex Device
method: GET
path: /deviceConfigurations
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.133424+00:00
---

# GET /deviceConfigurations

**API:** Webex Device
**Área:** Device Configurations
**operationId:** `List Device Configurations for device`

## Resumen
List Device Configurations for device

## Descripción
Lists all device configurations associated with the given device ID. Administrators can list configurations for all devices within an organization.

## Parámetros
- `deviceId` [query] (string) **(requerido)**: List device configurations by device ID.
- `key` [query] (string): This can optionally be used to filter configurations. Keys are composed of segments. It's possible to use absolute paths, wildcards or ranges.  - **Absolute** gives only one configuration as a result. `Conference.MaxReceiveCallRate` for example gives the Conference `MaxReceiveCallRate` configuration.  + **Wildcards** (\*) can specify multiple configurations with shared segments. `Audio.Ultrasound.*` for example will filter on all Audio Ultrasound configurations.  - **Range** ([_number_]) can be used to filter numbered segments. `FacilityService.Service[1].Name` for instance only shows the first `FacilityService` Service Name configuration, `FacilityService.Service[*].Name` shows all, `FacilityService.Service[1..3].Name` shows the first three and `FacilityService.Service[2..n].Name` shows all starting at 2. Note that [RFC 3986 3.2.2](https://www.ietf.org/rfc/rfc3986.html#section-3.2.2) does not allow square brackets in urls outside the host, so to specify range in a configuration key you will need to encode them to %5B for [ and %5D for ].

## Respuestas
- **200**: OK
  - `deviceId` (string) **(requerido)**: ID of the device that the configurations are for.
  - `items` (object):
    - `configuration_key` (object): Key of the configuration.
      - `source` (string): The source of the current value that is applied to the device.  * `default` - Current value comes from the schema default.  * `configured` - Current value comes from configuredValue. Valores: default, configured.
      - `sources` (object):
        - `default` (object):
          - `editability` (object):
        - `configured` (object):
          - `editability` (object):
      - `valueSpace` (object): [JSON Schema](http://json-schema.org/) describing the data format of the configuration as specified by the device.
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
