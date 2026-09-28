---
doc_id: developer-cisco-com-docs-finesse-single-sign-on-e2-80-94get-user-authentication-mode-7438499052
source_url: https://developer.cisco.com/docs/finesse/single-sign-on%e2%80%94get-user-authentication-mode/
retrieved_at: 2026-09-07T14:07:09.503771+00:00
---

# Single Sign-On—Get User Authentication Mode

This API allows a client to get the authentication mode of a user in a Unified CCE deployment that is in hybrid mode (SSO and non-SSO). This API uses either the username or userId and it does not require authentication.

This API does not require HTTP authentication. The third-party integrations must configure this API to determine which authentication mode (SSO or non-SSO) is configured for the user. If required, this API can be disabled using CLI. By default, the CLI sets the value of this property as true .

utils finesse set_property webservices enableUserAuthMode { true|false }

For more information, see Service Properties section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

URI:

https://<FQDN>/finesse/api/UserAuthMode/<username>

https://<FQDN>/finesse/api/UserAuthMode/<userId>

Example URI:

https://finesse1.xyz.com/finesse/api//UserAuthMode/myName

https://finesse1.xyz.com/finesse/api//UserAuthMode/1234

Security Constraints:

All users can use this API without authentication.

HTTP Method:

GET

Content Type:

—

Input/Output Format:

XML

HTTP Request:

—

Request Parameters:

—

HTTP Response:

200: Success

403: Forbidden

Example Response

Code Snippet

```
< UserAuthMode > < authMode > NON_SSO </ authMode > </ UserAuthMode >
```

Example Failure Response:

Code Snippet

```
< ApiErrors > < ApiError > < ErrorType > Forbidden </ ErrorType > < ErrorMessage > UserAuthModeService is disabled </ ErrorMessage > < ApiError > </ ApiErrors >
```

| Note | This API does not require HTTP authentication. The third-party integrations must configure this API to determine which authentication mode (SSO or non-SSO) is configured for the user. If required, this API can be disabled using CLI. By default, the CLI sets the value of this property as true . utils finesse set_property webservices enableUserAuthMode { true\|false } For more information, see Service Properties section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html . |
|---|---|---|

| URI: | https://<FQDN>/finesse/api/UserAuthMode/<username> https://<FQDN>/finesse/api/UserAuthMode/<userId> |
|---|---|
| Example URI: | https://finesse1.xyz.com/finesse/api//UserAuthMode/myName https://finesse1.xyz.com/finesse/api//UserAuthMode/1234 |
| Security Constraints: | All users can use this API without authentication. |
| HTTP Method: | GET |
| Content Type: | — |
| Input/Output Format: | XML |
| HTTP Request: | — |
| Request Parameters: | — |
| HTTP Response: | 200: Success 403: Forbidden |
| Example Response | Code Snippet < UserAuthMode > < authMode > NON_SSO </ authMode > </ UserAuthMode > |
| Example Failure Response: | Code Snippet < ApiErrors > < ApiError > < ErrorType > Forbidden </ ErrorType > < ErrorMessage > UserAuthModeService is disabled </ ErrorMessage > < ApiError > </ ApiErrors > |