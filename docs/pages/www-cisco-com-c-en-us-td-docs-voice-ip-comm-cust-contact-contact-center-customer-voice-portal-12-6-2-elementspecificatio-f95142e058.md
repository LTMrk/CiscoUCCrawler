---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-12-6-2-elementspecificatio-f95142e058
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/elementspecification/guide/ccvp_b_1262-element-specifications-guide/ccvp_m_rest_client-element.html
retrieved_at: 2026-08-21T17:20:25.510568+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(2)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(2)

Updated: April 28, 2023

Chapter: Rest_Client

## Chapter: Rest_Client

# Rest_Client

## Rest_Client

The Rest_Client element provides a flexible interface in order to
                                       				interact with REST endpoints. The communication between the REST client and
                                       				server is made completely secure using two-way Secure Sockets Layer (SSL). The
                                       				Rest_Client element permits users to send GET, POST, PUT, or DELETE requests to
                                       				application servers.

For more information about Secure Socket Layer Authentication, see the User Guide for Cisco Unified CVP VXML Server and Cisco Unified Call
                              		  Studio at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-user-guide-list.html .

### Settings

Name (Label)

Type

Req'd

Single Setting Value

Substitution Allowed

Default

Notes

Endpoint
                                             						URL

Boolean

Yes

true

false

Blank

This
                                             						settings specifies whether SNMP alert to be generated.

HTTP
                                             						method

Yes

GET

Supported HTTP methods:

GET (Read);

PUT (Update/Replace);

POST (Create)

DELETE (Delete)

Parameters

No

Blank

Any additional parameters will be passed along with URL. (such as specifying the response format or the amount returned).

Header parameters

Path parameters

Query string parameters

Request body parameters. Example: 'Authentication type': 'Preemptive'

Ignore
                                             						Certificate Validation

Yes

true

The SSL
                                             						security setting gets enabled when flag is set to false.

Require
                                             						HTTP authentication

Yes

false

The http authentication (options true/false)

User Name

Yes

Blank

Username of REST end point to be accessed (available if Require HTTP auth is true).

Password

Yes

Blank

Password of REST end point to be accessed (available if Require HTTP auth is true).

Headers

No

Blank

The meta-data associated with the API request and response.

Options:

Authorization : Carries credentials containing the authentication information of the client for the resource being requested.

WWW-Authenticate : This is sent by the server if it needs a form of authentication before it can respond with the actual resource being requested.
                                             Often sent along with a response code of 401, which means ‘unauthorized’.

Accept-Charset : This is a header which is set with the request and tells the server about which character sets are acceptable by the client.

Content-Type : Indicates the media type of the response. Values:

text/html - - Indicates that the request body format is HTML

application/json - Indicates that the request body format is JSON.

application/xml - Indicates that the request body format is XML.

application/x-www-form-urlencoded - Indicates that the request body is URL encoded.

Cache-Control : This is the cache policy defined by the server for this response, a cached response can be stored by the client and re-used
                                             till the time defined by the Cache-Control header.

Body

No

Blank

Use Proxy

Yes

false

Enable/Disable the proxy server (true/false)

Use Host

Yes

false

IP address or hostname of the HTTP proxy server

Use Port

Yes

false

Port of the HTTP proxy server

XPath
                                             						/ JSONPath

No

Blank

XPath expressions
                                             						are used in JavaScript to return the values from the XML.

JSONPath expressions are used in JavaScript to return the
                                             						values from the JSON(JavaScript Object Notation).

For more information about Xpath/JSONPath Expression, see the User Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio

Connect Timeout

Yes

3000
                                             						msec

HTTP request timeout

Read
                                             						Timeout

5000
                                             						msec

### Element
                           	 Data

Name

Type

Notes

response_body

string

This element data carries the REST response that is received
                                             				  from the REST end point.

status_code

string

This element data carries the REST response code received for
                                             				  the REST operation performed.

### Exit
                           	 States

Name

Notes

done

The element is successfully run.

### Events

Name (Label)

Notes

Event Type

Java Exception event handler type can be selected.

| The Rest_Client element provides a flexible interface in order to
                                       				interact with REST endpoints. The communication between the REST client and
                                       				server is made completely secure using two-way Secure Sockets Layer (SSL). The
                                       				Rest_Client element permits users to send GET, POST, PUT, or DELETE requests to
                                       				application servers. |
|---|

| Name (Label) | Type | Req'd | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| Endpoint
                                             						URL | Boolean | Yes | true | false | Blank | This
                                             						settings specifies whether SNMP alert to be generated. |
| HTTP
                                             						method |  | Yes |  |  | GET | Supported HTTP methods: GET (Read); PUT (Update/Replace); POST (Create) DELETE (Delete) |
| Parameters |  | No |  |  | Blank | Any additional parameters will be passed along with URL. (such as specifying the response format or the amount returned). Header parameters Path parameters Query string parameters Request body parameters. Example: 'Authentication type': 'Preemptive' |
| Ignore
                                             						Certificate Validation |  | Yes |  |  | true | The SSL
                                             						security setting gets enabled when flag is set to false. |
| Require
                                             						HTTP authentication |  | Yes |  |  | false | The http authentication (options true/false) |
| User Name |  | Yes |  |  | Blank | Username of REST end point to be accessed (available if Require HTTP auth is true). |
| Password |  | Yes |  |  | Blank | Password of REST end point to be accessed (available if Require HTTP auth is true). |
| Headers |  | No |  |  | Blank | The meta-data associated with the API request and response. Options: Authorization : Carries credentials containing the authentication information of the client for the resource being requested. WWW-Authenticate : This is sent by the server if it needs a form of authentication before it can respond with the actual resource being requested.
                                             Often sent along with a response code of 401, which means ‘unauthorized’. Accept-Charset : This is a header which is set with the request and tells the server about which character sets are acceptable by the client. Content-Type : Indicates the media type of the response. Values: text/html - - Indicates that the request body format is HTML application/json - Indicates that the request body format is JSON. application/xml - Indicates that the request body format is XML. application/x-www-form-urlencoded - Indicates that the request body is URL encoded. Cache-Control : This is the cache policy defined by the server for this response, a cached response can be stored by the client and re-used
                                             till the time defined by the Cache-Control header. |
| Body |  | No |  |  | Blank |  |
| Use Proxy |  | Yes |  |  | false | Enable/Disable the proxy server (true/false) |
| Use Host |  | Yes |  |  | false | IP address or hostname of the HTTP proxy server |
| Use Port |  | Yes |  |  | false | Port of the HTTP proxy server |
| XPath
                                             						/ JSONPath |  | No |  |  | Blank | XPath expressions
                                             						are used in JavaScript to return the values from the XML. JSONPath expressions are used in JavaScript to return the
                                             						values from the JSON(JavaScript Object Notation). For more information about Xpath/JSONPath Expression, see the User Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio |
| Connect Timeout |  | Yes |  |  | 3000
                                             						msec | HTTP request timeout |
| Read
                                             						Timeout |  |  |  |  | 5000
                                             						msec |  |

| Name | Type | Notes |
|---|---|---|
| response_body | string | This element data carries the REST response that is received
                                             				  from the REST end point. |
| status_code | string | This element data carries the REST response code received for
                                             				  the REST operation performed. |

| Name | Notes |
|---|---|
| done | The element is successfully run. |

| Name (Label) | Notes |
|---|---|
| Event Type | Java Exception event handler type can be selected. |