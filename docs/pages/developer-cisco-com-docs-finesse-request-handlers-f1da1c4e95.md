---
doc_id: developer-cisco-com-docs-finesse-request-handlers-f1da1c4e95
source_url: https://developer.cisco.com/docs/finesse/request-handlers/
retrieved_at: 2026-09-07T14:08:03.557626+00:00
---

# Request Handlers

Class finesse.interfaces.RequestHandlers(handlers)

Defines the REST object callback handlers that are passed as arguments while creating the REST object. Retrieves the methods when the object is created.

Parameters

Name

Type

Description

Required

handlers

Object

An object containing callback functions which are invoked when the callback scenario is triggered.

The following are the request handlers (see below for details):

success(rsp)

error(rsp)

Optional

success(rsp)

Function

Callback function that is invoked upon a successful request. The initialized object is then passed to the callback function as a parameter.

Optional

error(rsp)

Function

Callback function that is invoked upon an unsuccessful request. The initialized object is then passed to the callback function as a parameter.

Optional

status Number The HTTP status code of the succeeded request. Optional content String The raw string response of the succeeded request. Optional object Object The parsed object response of the succeeded request. Optional error Object The error details from the failed request. Optional errorType String The type of error. Optional errorMessage String The message that is associated with the error. Optional

| Name | Type | Description | Required |
|---|---|---|---|
| handlers | Object | An object containing callback functions which are invoked when the callback scenario is triggered. The following are the request handlers (see below for details): success(rsp) error(rsp) | Optional |
| success(rsp) | Function | Callback function that is invoked upon a successful request. The initialized object is then passed to the callback function as a parameter. | Optional |
| error(rsp) | Function | Callback function that is invoked upon an unsuccessful request. The initialized object is then passed to the callback function as a parameter. | Optional |