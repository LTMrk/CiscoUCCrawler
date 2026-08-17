---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-error-handling-html-dae4a4d353
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_error-handling.html
retrieved_at: 2026-08-17T03:47:15.184087+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- Error Handling

## Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- Error Handling

- Cisco Unity                              	 Connection Provisioning Interface (CUPI) API -- Error Handling

- Possible                              	 Errors

# Cisco Unity
                     	 Connection Provisioning Interface (CUPI) API -- Error Handling

Links to Other API pages: Cisco_Unity_Connection_APIs

## Possible
                        	 Errors

The HTTP status
                              		  codes themselves provide information about many typical errors. See the
                              		  following list for some of the status codes returned by CUPI:

In addition to the
                              		  error codes, in most cases CUPI will return an XML document that provides more
                              		  information about the error:

```
<xs:complexType name="ErrorDetails">
<xs:all>
<xs:element name="errors" maxOccurs="unbounded">
<xs:complexType>
<xs:all>
<xs:element name="code" type="ErrorCode"/>
<xs:element name="message" type="xs:string"/>
</xs:all>
</xs:complexType>
</xs:element>
</xs:all>
</xs:complexType>
```

| Possible Errors | Explanation |
|---|---|
| 200 OK | Normal
                                       					 response when a page has been successfully fetched. |
| 201 Created | The
                                       					 resource has been created. |
| 301 Moved Permanently | The page has moved permanently. It is usually a response from
                                       					 implementing a 301 redirect. |
| 302 Moved Temporarily | The page has moved temporarily. |
| 400 Bad Request | The request could not be understood by the server, due to
                                       					 incorrect syntax. |
| 401 Unauthorized User | Authentication is required. |
| 403 Forbidden | The server understood the request, but is refusing to fulfill
                                       					 it. |
| 404 Page Not Found | The server has not found anything that matches the Request-URI. |
| 405 Method Not Allowed | The method specified in the Request-Line is not allowed for the
                                       					 resource identified by the Request-URI. |
| 406 Not Acceptable | The server cannot generate a response that the requester is
                                       					 willing to accept. |
| 410 Gone | The requested resource is no longer available at the server, and
                                       					 no forwarding address is known. This condition is similar to 404, except that
                                       					 the 410 error condition is expected to be permanent. |
| 415 Unsupported Media Type | The server is refusing the request, because the request is in a
                                       					 format not supported by the requested resource for the requested method. |
| 500 Server Error | There is an internal web server error. |