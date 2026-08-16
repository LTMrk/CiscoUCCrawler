---
doc_id: webex-cloud-calling-post-convergedrecordings-restore
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: POST
path: /convergedRecordings/restore
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.580926+00:00
---

# POST /convergedRecordings/restore

**API:** Webex Cloud Calling
**Área:** Converged Recordings
**operationId:** `restore_recordings_from_recycle_bin`

## Resumen
Restore Recordings from Recycle Bin

## Descripción
Restore recordings from the recycle bin with recording IDs or restore all the recordings that are in the recycle bin.

Only the following two entities can use this API

* Administrator: A user or an application with the scope `spark-admin:recordings_write`.

* User: An authenticated user who does not have the scope `spark-admin:recordings_write` but has `spark:recordings_write`.

As an `administrator`, you can restore a list of recordings or all recordings of a particular user within the org you manage from the recycle bin.

As a `user`, you can restore a list of your own recordings or all your recordings from the recycle bin.

* If `restoreAll` is `true`:
  * `recordingIds` should be empty.
  * If the caller of this API is an `administrator`, `ownerEmail` should not be empty and all recordings owned by the `ownerEmail` will be restored from the recycle bin.
  * If the caller of this API is a `user`, `ownerEmail` should be empty and all recordings owned by the caller will be restored from the recycle bin.

* If `restoreAll` is `false`:
  * `ownerEmail` should be empty.
  * `recordingIds` should not be empty and its maximum size is `100`.

## Cuerpo de la petición (application/json)
- `restoreAll` (boolean): If not specified or `false`, restores the recordings specified by `recordingIds` from the recycle bin. If `true`, restores all recordings owned by the caller in case of `user`, and all recordings owned by `ownerEmail` in case of `administrator` from the recycle bin.
- `ownerEmail` (string): Email address for the recording owner. This parameter is only used if `restoreAll` is set to `true` and the user or application calling the API has the required administrator scope `spark-admin:recordings_write`. The administrator may specify the email of a user from an org they manage and the API will restore all the recordings of that user from the recycle bin.
- `recordingIds` (array): Recording IDs for restoring recordings from the recycle bin in batch.

### Ejemplo de petición
```json
{
  "restoreAll": false,
  "recordingIds": [
    "81bb582c-e93e-40aa-abf6-962b620f6db4"
  ]
}
```

## Respuestas
- **204**: No Content
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
