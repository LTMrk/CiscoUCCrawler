---
doc_id: webex-contact-center-get-datasources
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /dataSources/
operation_id: Retrieve All Data Sources
tags: Data Sources
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T15:03:57.702313+00:00
---

# GET /dataSources/

**API:** Webex Contact Center
**Área:** Data Sources
**operationId:** `Retrieve All Data Sources`

## Resumen
Retrieve All Data Sources

## Descripción
Lists all data sources registered by the Service App. Requires the `spark-admin:datasource_read` scope.

## Ejemplo de invocación
```bash
curl -X GET '/dataSources/' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array):

### response — respuesta 200
```json
{
  "items": [
    {
      "DataSource": "",
      "applicationId": "Cf2e954e018f2de8c1403e2618323551df65",
      "createdAt": "2022-01-01T00:00:00Z",
      "createdBy": "3e4d3b27-1bf1-4916-8d0c-d27fd765fa52",
      "jwsToken": "eyJraWQiOiIxOWFmMzYxYS0zYWI0LTU0NzEtYTViMC03MmQxODQyOTRjMmYiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJNeUFwcDIiLCJzdWIiOiJNeUFwcHNQdXJwb3NlMiIsImlzcyI6Imh0dHBzOlwvXC9pZGJyb2tlci53ZWJleC5jb21cL2lkYiIsImV4cCI6MTcyOTIyMDUxNSwiY29tLmNpc2NvLmRhdGFzb3VyY2UudXJsIjoiaHR0cHM6XC9cL3NjaGlmZmVydC5tZVwvZHMyIiwiY29tLmNpc2NvLmRhdGFzb3VyY2Uuc2NoZW1hLnV1aWQiOiI3OGVmYzc3NS1kY2NiLTQ1Y2EtOWFjZi05ODlhNGE1OWY3ODgiLCJpYXQiOjE3MjkyMTMzMTUsImNvbS5jaXNjby5vcmcudXVpZCI6ImNlODYxZmJhLTZlMmYtNDlmOS05YTg0LWIzNTQwMDhmYWM5ZSIsImp0aSI6IjEyMzQ1NiJ9.QxWYQCXOTLTNBx1Mr8qtd1rpx5uqHYcow1l_oiqMQ_2LorPor3wnEW9_dmMFUs-yAizpayTB4XJpU0ga9E-GY3XaiXz4CGW0G5f3566j3AvmfviMVCFgQFnMd0LpwgPIHhQGX-z2Y6KgzjTCLqm76WpSylAomOPEpgs8dqChfuC9aVHyuB2FfV77J265q-pLp8RSJa_EoSZ_05tpQHxxrDrB-qnn-WQoCFFlb88f3kKdyzPqQhvdWQuouyaP4YyMd_C8a6N_F1dk3cBUjSOtnHDm9WoGwYd8wUcjtZVk5g-z7coc656OooRvDQ0-JRdh7TVUfkzdQS79d4UfmRAhYQ",
      "orgId": "63b02f90-9cc6-43b8-aa6d-cad425ac554c"
    }
  ]
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
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs