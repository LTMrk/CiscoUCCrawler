---
doc_id: webex-admin-get-report-templates
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: GET
path: /report/templates
operation_id: List Report Templates
tags: Report Templates
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.577424+00:00
---

# GET /report/templates

**API:** Webex Admin
**Área:** Report Templates
**operationId:** `List Report Templates`

## Resumen
List Report Templates

## Descripción
List all the available report templates that can be generated.

CSV (comma separated value) reports for Webex services are only supported for organizations based in the North American region. Organizations based in other regions will return blank CSV files for any Webex reports.

#### Validation Fields

Each template includes validation rules that specify which fields are required when generating a report using the [Reports API](/docs/api/v1/reports). The possible validation field values are:

- **templateId**: The unique identifier of the report template to use. This is always required when creating a report.
- **siteList**: A comma-separated list of Webex sites (e.g., "cisco.webex.com"). Required for site-based templates, typically for Webex Meetings reports.
- **subIds**: Subscription IDs for the report. Required for certain enterprise agreement templates, particularly for Webex Onboarding service reports.
- **startDate**: The start date for the report data range in YYYY-MM-DD format. Required for date-range based templates.
- **endDate**: The end date for the report data range in YYYY-MM-DD format. Required for date-range based templates.

When creating a report, ensure you provide all fields marked as "required": "yes" in the template's validation rules.

## Ejemplo de invocación
```bash
curl -X GET '/report/templates' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- (array de:)
  - `id` (string): Unique identifier representing a report.
  - `title` (string): Name of the template.
  - `service` (string): The service to which the report belongs.
  - `maxDays` (number): Maximum date range for reports belonging to this template.
  - `identifier` (string): Generated reports belong to which field.
  - `validations` (object):
    - `validations` (array): An array of validation rules
      - `field` (string): Field on which validation rule is applied
      - `required` (string): Whether the above field is required

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "Id": 130,
      "title": "Client Version Prod",
      "service": "Teams",
      "maxDays": 31,
      "identifier": "orgWithoutDate",
      "validations": [
        {
          "field": "templateId",
          "required": "yes"
        }
      ]
    }
  ],
  "numberOfTemplate": 1
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