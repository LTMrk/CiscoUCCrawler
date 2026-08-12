[](https://developer.webex.com/)
[Getting Started](https://developer.webex.com/create/docs)Documentation![](https://developer.webex.com/create/docs/login-with-webex)[AI in Webex](https://developer.webex.com/mcp/docs/webex-mcp-server-overview)Blog![](https://developer.webex.com/create/docs/login-with-webex)[Support](https://developer.webex.com/explore/support)Resources![](https://developer.webex.com/create/docs/login-with-webex)
[Log in](https://developer.webex.com/login)[Sign up](https://developer.webex.com/signup)
[Home](https://developer.webex.com/)/Login with Webex
Getting Started
  * [Getting Started](https://developer.webex.com/create/docs)
  * [Authentication](https://developer.webex.com/create/docs/authentication)
  * [Login with Webex](https://developer.webex.com/create/docs/login-with-webex)
  * [AI Assistant for Developers](https://developer.webex.com/create/docs/webex-aI-assistant-for-developers)
  * Agentic Apps
  * Bots
  * Embedded Apps
  * Integrations
  * Service Apps
  * Instant Connect
  * Workspace Integrations
  * Bring Your Own Datasource
  * [Suite Sandbox](https://developer.webex.com/create/docs/developer-sandbox-guide)
  * [Contact Center Sandbox](https://developer.webex.com/create/docs/sandbox_cc)
  * [Guest to Guest Sandbox](https://developer.webex.com/create/docs/g2g-sandbox)
  * [Submit Your App](https://developer.webex.com/create/docs/app-hub-submission-process)
  * [Tutorials](https://developer.webex.com/create/docs/tutorials)


## Getting Started
### Login with Webex
Login with Webex lets users login to your app or service using their Webex account. 
####  anchorAbout Login with Webex
anchor
Login with Webex is based on [OpenID Connect](https://openid.net/connect/), an identity layer built on the OAuth 2.0 protocol. Standard [Webex Integrations](https://developer.webex.com/docs/integrations) use OAuth flows to obtain access tokens for making API calls on a user's behalf. Login with Webex uses those same flows, with some additional parameters, to obtain ID tokens. ID tokens are signed, Base64-encoded [JSON Web Tokens](https://datatracker.ietf.org/doc/html/rfc7519) (JWTs) that act as proof a user authenticated with Webex, and that contain information ("claims") about the authenticated user, such as their email or name.
####  anchorGetting Started
anchor
The following are the basic steps to get started with Login with Webex.
  1. Decide which of the [available OAuth flows](https://developer.webex.com/docs/login-with-webex#supported-oauth-and-openid-connect-flows) you are going to use. For OAuth clients running on devices with a web browser and keyboard input [Authorization Code Flow with Proof Key of Code Exchange](https://developer.webex.com/docs/login-with-webex#authorization-code-flow-with-proof-key-for-code-exchange) is the recommended flow. For devices without a web browser or limited input abilities (such as smart TVs or set-top boxes) there is the [Device Grant Flow](https://developer.webex.com/docs/login-with-webex#device-grant-flow).
  2. Create a [Webex integration](https://developer.webex.com/my-apps/new/integration), or identify an existing integration. The integration doesn't need to include any particular scopes to use Login with Webex, but it may include other [data access scopes](https://developer.webex.com/docs/integrations#scopes) if you want to also obtain an access token for making API calls. If you are using Device Grant Flow your integration's redirect URIs must include the [OAuth helper service URIs](https://developer.webex.com/docs/login-with-webex#oauth-helper-service-uris).
  3. For either Authorization Code Flow, create a login page that initiates the authorization process by directing the user's web browser to the Webex [Authorization Endpoint](https://developer.webex.com/docs/login-with-webex#authorization-endpoint) (`/v1/authorize`) with the required parameters. For [Device Grant Flows](https://developer.webex.com/docs/login-with-webex#device-grant-flow) there is no need to create a separate page to initiate the authorization process.


####  anchorSupported OAuth and OpenID Connect Flows
anchor
Login with Webex supports the following OAuth flows:
  * [Authorization Code Flow](https://developer.webex.com/docs/login-with-webex#authorization-code-flow) and [Authorization Code Flow with PKCE](https://developer.webex.com/docs/login-with-webex#authorization-code-flow-with-proof-key-for-code-exchange) for devices with a web browser and keyboard. Authorization Code Flow with PKCE is the recommended flow as it provides the best security.
  * [Device Grant Flow](https://developer.webex.com/docs/login-with-webex#device-grant-flow) is designed for smart TVs and other devices without a web browser or with limited input abilities. Note that Device Grant flow does not support [OpenID Connect scopes](https://developer.webex.com/docs/login-with-webex#openid-connect-scopes-and-claims).
  * [Implicit Grant Flow](https://developer.webex.com/docs/login-with-webex#implicit-grant-flow) allows an OAuth client to obtain access and ID tokens directly from the authorization server in a single request. This flow is discouraged from use due to security concerns.


###### Authorization Code Flow
In this authorization flow your app (the OAuth client) first obtains an authorization code from the [authorization endpoint](https://developer.webex.com/docs/login-with-webex#authorization-endpoint), which it then exchanges for an ID token (or access token) from the [access token endpoint](https://developer.webex.com/docs/login-with-webex#access-token-endpoint).
The following diagram illustrates the authorization code flow sequence, which is explained below. Also see [Getting an ID Token with Authorization Code Flow](https://developer.webex.com/docs/login-with-webex#getting-an-id-token-with-authorization-code-flow) for example requests and responses.
![](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltcd94a5de6b00a838/62b3a1631944ac5ac4263f12/auth_code_sequence.png)
  1. User starts authorization flow (by clicking 'Login', for example).
  2. Your app directs the user to the [authorization endpoint](https://developer.webex.com/docs/login-with-webex#authorization-endpoint) with a set of URL query parameters, including `response_type=code`, `client_id`, `scope`, `state`, and the `redirect_uri` to which the authorization server will send the user-agent back once access is granted (or denied). 
  3. The OAuth server redirects the user's browser to the Webex authentication page where the user signs into their Webex account and accepts the requested OpenID scopes.
  4. In response, the OAuth server directs the user to the the specified `redirect_uri`. The server appends a `code` property to the URI fragment whose value is the authorization code.
  5. The client extracts the authorization code from the URI and sends it in a request to the [token endpoint](https://developer.webex.com/docs/login-with-webex#access-token-endpoint), along with the integration's configured client ID and secret.
  6. The server responds with a JSON object containing the ID token (and an access token and refresh token, depending on requested scopes).


###### Authorization Code Flow with Proof Key for Code Exchange
[Proof Key for Code Exchange](https://datatracker.ietf.org/doc/html/rfc7636) (PKCE) is an extension to the Authorization Code flow that's designed to prevent Cross Site Request Forgery (CSRF) attacks. It uses an additional generated secret code in the request for the authorization code and ID or access token. For details see [Getting an ID Token with Authorization Code Flow with Proof Key of Code Exchange](https://developer.webex.com/docs/login-with-webex#getting-an-id-token-with-authorization-code-flow-with-proof-key-for-code-exchange-pkce).
The following diagram, explained below, outlines the process for using Authorization Code flow with PKCE to obtain an ID and/or access token.
![OAuth Flow with PKCE](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt63de4af2163791e8/62b4a210ff0f000f7b263c27/pkce-flow.png)
  1. User starts the authorization process.
  2. Your app generates a **code verifier** and a **code challenge** with the desired **code challenge method**.
  3. Your app sends a request for an authorization code, with the `scope` parameter set to a space-delimited and URL-encoded list of [OpenID Connect](https://developer.webex.com/docs/login-with-webex#openid-connect-scopes-and-claims) scopes and/or data access scopes (see [OpenID Connect Scopes and Claims](https://developer.webex.com/docs/integrations#scopes)), `response_type` set to `code`, and `code_challenge` and `code_challenge_method` parameters.
  4. The OAuth server caches `code_challenge` and `code_challenge_method` for the request.
  5. The OAuth server redirects the user's browser to the Webex authentication page where the user signs into their Webex account and accepts the requested OpenID scopes.
  6. The OAuth server redirects the user to the integration's redirect URI and appends a `code` parameter to the URI fragment that contains the authorization code.
  7. Your app extracts authorization code from the URI and sends it in a request to the token endpoint, along with the `code_verifier`, `client_id`, and `client_secret`.
  8. OAuth server validates `code_verifier` using the cached `code_challenge_method`.
  9. Server's response is a JSON object with an ID token (and access and refresh tokens, depending on the requested scopes).


###### Device Grant Flow
The Device Flow enables OAuth clients devices without a web browser or with limited input ability (smart TVs or media consoles, for example) to obtain user authorization to access protected resources. Instead of interacting directly with the end user's user agent (web browser), the device client instructs the end user to use another computer or device and connect to the authorization server to approve the access request. Clients poll the authorization server repeatedly until the end user completes the approval process.
For a complete sample that illustrates the Device Grant Flow from end to end, see the following GitHub repo, [webex-device-oauth-sample](https://github.com/WebexSamples/webex-device-oauth-sample).
Device Grant flow does not support [OpenID Connect scopes](https://developer.webex.com/docs/login-with-webex#openid-connect-scopes-and-claims).
The following diagram, explained below, outlines the process for using Device Grant Flow. For details see [Getting an Access Token with Device Grant Flow](https://developer.webex.com/docs/login-with-webex#getting-an-access-token-with-device-grant-flow).
![Device grant flow diagram](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltb9fd68869b066ce0/62e32b0312f4cd75109def9d/device-flow.png)
  1. The app running on the device initiates a request to the [Device Authorization Endpoint](https://developer.webex.com/docs/login-with-webex#device-authorization-endpoint), passing client ID and scopes for the associated Webex integration.
  2. The server responds with device code, user code, and two verification URLs, one of which includes a hashed version of the user code.
  3. Device presents the verification URI and user code to the user, or equivalent QR code. User starts authorization process on a mobile device or laptop.
  4. Device begins polling the [Device Token Endpoint](https://developer.webex.com/docs/login-with-webex#device-token-endpoint). The endpoint returns `428 Precondition Required` until the user has finished the authorization process.
  5. Once the user successfully completes the authorization process on another device the next request to the device token endpoint returns a `200 OK` and a JSON object with the access and refresh tokens.


###### Implicit Flow
In the Implicit Flow the client requests ID and access tokens directly from the [authorization endpoint](https://developer.webex.com/docs/login-with-webex#authorization-endpoint).
Use of this flow is generally discouraged for security reasons.
The following diagram illustrates the implicit flow sequence, which is explained below.
![Implicit flow sequence diagram](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt2c0aa9e2047bbe4f/62be29aa9830944e9748710f/implicit-flow.png)
  1. User starts the authorization process.
  2. Your app makes a request to the [authorization endpoint](https://developer.webex.com/docs/login-with-webex#authorization-endpoint) that includes the required `nonce` parameter, the recommended `state` parameter, `scope=openid` (or other scopes), and `response_type` set to one of the following:
     * `id_token` -- To request an ID token, only.
     * `token` -- To request an access token, only
     * `id_token token` -- To request both an access token and ID token.
  3. The user authenticates with Webex and accepts the requested access scopes.
  4. The authorization server redirects the user to your app's redirect URI, which is appended with `id_token` and/or `token` parameters, depending on the specified `response_type`.


For details see [Getting an ID Token with Authorization Code Flow with Implicit Flow](https://developer.webex.com/docs/login-with-webex#getting-an-id-token-or-access-token-with-implicit-flow).
####  anchorOAuth 2.0 and OpenID Connect API Endpoints
anchor
OpenID Connect is built on the OAuth 2.0 protocol, the same protocol used by Webex [Integrations](https://developer.webex.com/docs/integrations) to get permission from a user to make Webex API calls on their behalf. With Webex OAuth 2.0 APIs you can both obtain an ID token that proves the user has authenticated with Webex, and an access token to make API calls.
  * [Authorization Endpoint](https://developer.webex.com/docs/login-with-webex#authorization-endpoint)
  * [Device Authorization Endpoint](https://developer.webex.com/docs/login-with-webex#device-authorization-endpoint)
  * [Access Token Endpoint](https://developer.webex.com/docs/login-with-webex#access-token-endpoint)
  * [Device Token Endpoint](https://developer.webex.com/docs/login-with-webex#access-token-endpoint)
  * [UserInfo Endpoint](https://developer.webex.com/docs/login-with-webex#userinfo-endpoint)
  * [Verification Endpoint](https://developer.webex.com/docs/login-with-webex#verification-endpoint)
  * [Discovery Endpoint](https://developer.webex.com/docs/login-with-webex#discovery-endpoint)
  * [Webfinger Endpoint](https://developer.webex.com/docs/login-with-webex#webfinger-endpoint)


###### Authorization Endpoint
Your app initiates an OAuth 2.0 flow to obtain an ID token and/or an access token. The value of the request's `response_type` query parameter determines which [OAuth grant flow](https://developer.webex.com/docs/login-with-webex#supported-oauth-and-openid-connect-flows) is used.

```
GET https://webexapis.com/v1/authorize

```

To obtain an ID token:
  * The `response_type` parameter must include `id_token`
  * The request's `scope` request parameter must contain `openid`
  * The `nonce` parameter is required


###### Authorization
This endpoint requires no authorization.
###### Authorization Request
Requests to the authorization endpoint have the following query parameters:  
| **Parameter Name**  | **Type**  | **Required**  | **Description**  |  
| --- | --- | --- | --- |  
| `response_type`  | string  | yes  | Type of grant, which determines the authorization flow. Set to `code` to use the [Authorization Code flow](https://developer.webex.com/docs/login-with-webex#supported-oauth-and-openid-connect-flows) flow. Set to `id_token`, `token` or `id_token token` to use the [Implicit Flow](https://developer.webex.com/docs/login-with-webex#supported-oauth-and-openid-connect-flows).  |  
| `client_id`  | string  | yes  | Client ID of your Webex integration.  |  
| `redirect_uri`  | string  | no  | URI where the user's browser is redirected after they complete the authentication process. If the integration has multiple registered redirect URIs, this parameter is required and the `redirect_uri` in the request must match one of the registered redirect URIs. May be omitted from the request if the integration has a single registered redirect URI.  |  
| `scope`  | string  | yes  | URL-encoded list of requested [data access scopes](https://developer.webex.com/docs/integrations#scopes) and/or [OpenID Connect scopes](https://developer.webex.com/docs/login-with-webex#openid-connect-scopes-and-claims) separated by spaces. Specified data access scopes must be registered with your Webex integration. (OpenID Connect scopes do not need to be registered.) If `scope` is missing from the request the server will return an "invalid scope" error.  |  
| `state`  | string  | no  | Any arbitrary string. Its purpose is to prevent Cross-Site Request Forgery attacks by providing a way for your app maintain state between your app's authorization request and the server's response. The server returns the same value you specify as a name=value pair in the URL fragment (#) of the redirect URI.  |  
| `code_challenge`  | string  | no  | Proof Key for Code Exchange (PKCE) code challenge used with Authorization Code flows to prevent Cross-Site Request Forgery attacks. See [Implementing PKCE with Authorization Code Flow](https://developer.webex.com/docs/login-with-webex#implementing-pkce-with-auth-code-flow).  |  
| `code_challenge_method`  | string  | no  | Proof Key for Code Exchange (PKCE) code challenge method used with Authorization Code flows to prevent Cross-Site Request Forgery attacks. See [Implementing PKCE with Authorization Code Flow](https://developer.webex.com/docs/login-with-webex#implementing-pkce-with-auth-code-flow).  |  
| `prompt`  | String  | no  | Specifies whether the authorization server prompts the user to reauthenticate. If set to `select_account` the user is redirected to the Webex authentication dialog with the email field pre-populated. If set to `none` the user is never shown an authentication dialog. If an existing session does not currently exist the server returns a "login_required" error in the URL. This can be used as a way to check for an existing authentication.  |  
| `nonce`  | String  | yes  | Nonce for Login with Webex requests. Required if the `scope` query parameter includes `openid`. The [](https://developer.webex.com/docs/login-with-webex#openid) claim of the ID token returned by Webex will have the same value.  |  
| `max_age`  | long  | no  | The maximum number of seconds since the last time the user was actively authenticated by Webex before they must reauthenticate.  |  
| `login_hint`  | string  | no  | Hint to the server about the login identifier the user might want to use to log on. The value should be specified in email format.  |  
Below is a sample request for an authorization code.

```
GET /v1/authorize?response_type=code
    &client_id=<CLIENT_ID>
    &redirect_uri=https://app.example.com:9443/auth
    &scope=openid profile email
    &state=random-string HTTP/1.1
Host: webexapis.com

```

###### Authorization Response
The response to the authorization endpoint depends on the `response_type` specified in the request. 
  * If the `response_type` was `code` then the [Authorization Code flow](https://developer.webex.com/docs/login-with-webex#getting-an-id-token-with-authorization-code-flow) is inititated and the response contains a `code` URL query parameter that can be exchanged for an ID token, access token, or both at the [Access Token endpoint](https://developer.webex.com/docs/login-with-webex#access-token-endpoint).

```
https://www.example.com/auth?code=<AUTHORIZATION_CODE>&state=<STATE_FROM_REQUEST>

```

  * If the `response_type` was one of `id_token`, `token`, or `id token token`, then `id_token` and/or `access_token` properties are appended to the redirect URI's hash fragment. For example, the following shows a response for a request with `response_type=id_token`.

```
https://www.example.com/redirect/#id_token=<ID_TOKEN>&state=<STATE_FROM_REQUEST>

```



The following lists the possible parameters included in the response to a request to `/v1/authorize`:  
| **Parameter Name**  | **Description**  |  
| --- | --- |  
| `access_token`  | Access token for making API calls. Included if the `response_type` request parameter included `token`.  |  
| `code`  | Authorization code used to obtain an access token from the [access token endpoint](https://developer.webex.com/docs/login-with-webex#access-token-endpoint). Included if `response_type` was set to `code` in the request.  |  
| `expires_in`  | Number of seconds for which the token is valid. Included if the `response_type` request parameter included `token`.  |  
| `id_token`  | Base64-encoded and signed JSON Web Token (JWT). Included if the `response_type` request parameter included `id_token` and the `scope` request parameter included `openid`.  |  
| `token_type`  | Included if the `response_type` request parameter included `token`. Value is always "Bearer".  |  
| `state`  | Included if the `state` parameter was in the request. The same value sent in the request should be in the response. Apps should verify that the the values are the same.  |  
The following response is for a request with `response_type=id_token token`, so the URL contains both `id_token` and `access_token` fields (line breaks added for readability).

```
http://127.0.0.1:8080/#id_token=<ID_TOKEN>
&access_token=<ACCESS_TOKEN>
&token_type=Bearer
&expires_in=<SECONDS_TO_EXPIRE>
&state=<STATE_FROM_REQUEST>

```

###### Device Authorization Endpoint
The device token authorization endpoint is used to initiate an authorization request on input-constrained client devices such as smart TVs or set-top boxes. It returns a URL where the user can authenticate with Webex and approve the authorization request a user code returned in the response.

```
POST https://webexapis.com/v1/device/authorize

```

The following redirect URIs must be added to the [Webex integration](https://developer.webex.com/docs/integrations) associated with the `client_id` used in the request.
  * <https://oauth-helper-a.wbx2.com/helperservice/v1/actions/device/callback>
  * <https://oauth-helper-r.wbx2.com/helperservice/v1/actions/device/callback>
  * <https://oauth-helper-k.wbx2.com/helperservice/v1/actions/device/callback>
  * <https://oauth-helper-d.wbx2.com/helperservice/v1/actions/device/callback>


###### Authorization
This endpoint requires no authorization.
###### Device Authorization Request
The request body is a URL-encoded string with the following parameters:  
| **Parameter Name**  | **Type**  | **Required**  | **Description**  |  
| --- | --- | --- | --- |  
| `client_id`  | string  | yes  | Webex integration client ID. The integration must have the [OAuth helper services URLs](https://developer.webex.com/docs/login-with-webex#service-helper-urls) added as redirect URLs.  |  
| `scope`  | string  | yes  | List of requested scopes separated by spaces.  |  

```
POST /v1/device/authorize HTTP/1.1
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Host: webexapis.com
Content-Length: 106

client_id=C65cbd0361e76a1c07a4f01bf67fffb8b863103dffaa809d3bf752b0d15144ff1&scope=meeting:schedules_read

```

###### Device Authorization Response
The following are possible response codes for the device authorization response:  
| **Response Code**  | **Description**  |  
| --- | --- |  
| `200 OK`  | The request was successfully processed, see the response body for results.  |  
| `400 Bad Request`  | An invalid `client_id` or invalid `scope` parameter was provided in the request.  |  
| `429 Too many requests`  | The client has made too many requests. The `Retry-After` header is included, indicating how long the client should wait before making another request.  |  
A successful response contains a JSON object that has the following properties:  
| **Parameter Name**  | **Description**  |  
| --- | --- |  
| `device_code`  | An unique device code assigned to this device authorization request.  |  
| `expires_in`  | Lifetime in seconds for `device_code` and `user_code` response fields  |  
| `user_code`  | End user's unique, six digit verification code.  |  
| `verification_uri`  | A verification URL (`https://oauth-helper-r.wbx2.com/verify`, for example) that the user navigates to on a separate device and enters the `user_code` from the response.  |  
| `verification_uri_complete`  | A verification URL that has a hashed version of the `user_code` response variable embedded (`https://oauth-helper-r.wbx2.com/verify?userCode=0d3955d418be1de30ef281aaf37939515c8d697b7393d6eda16423c7002497b1`, for example). Apps can use this URL to generate a QR code to present to the user for an easier sign in experience.  |  
| `interval`  | Minimum amount of time in seconds that your device should wait between polling requests to [Device Token Endpoint](https://developer.webex.com/docs/login-with-webex#device-token-endpoint).  |  
###### Examples
**Successful response**

```
HTTP/1.1 200 OK
Content-Type: application/json
{
  "device_code": "5d5cf602-f0dd-49d5-bfd3-915267e4fbe0",
  "expires_in": 300,
  "user_code": "729703",
  "verification_uri": "https://oauth-helper-r.wbx2.com/verify",
  "verification_uri_complete": "https://oauth-helper-r.wbx2.com/verify?userCode=6587b053970a656c29500e6bced0c1c59290a743ad7e34af474a65085860de57",
  "interval": 2
}

```

**Error Response due to Invalid Client ID**

```
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
  "message": "The request could not be understood by the server due to malformed syntax.",
  "errors": [{ "description": "Client Id is invalid" }],
  "trackingId": "ROUTER_62E068B0-FA5E-01BB-1501-0AFE2B641501"
}

```

###### Access Token Endpoint
The token endpoint is used to exchange an authorization code obtained from a previous call to the [Authorization endpoint](https://developer.webex.com/docs/login-with-webex#authorization-endpoint) for an ID token, access token and refresh token.
ID tokens returned by this endpoint only contain claims for the [openid scope](https://developer.webex.com/docs/login-with-webex#openid), regardless of what other OpenID Connect scopes were in the original [Device Authorization request](https://developer.webex.com/docs/login-with-webex#device-authorization-endpoint). To get user claims for all requested OpenID Connect scopes (the "email" or "profile" scopes) you call the [UserInfo Endpoint](https://developer.webex.com/docs/login-with-webex#userinfo-endpoint) with the returned access token.

```
POST https://webexapis.com/v1/access_token

```

###### Authorization
Requests to the access token endpoint must be authorized either with Basic authentication, or by passing `client_id` and `client_secret` in the request body. To use Basic authentication, add an `Authorization` HTTP header whose value is `Basic <credentials>`, where `<credentials>` are a Base64-encoding of `client_id` and `client_secret` separated by a colon (e.g. `Base64("<client-id>:<client-secret>")`), for example:

```
Authorization: Basic ABC1Y2JkMDM2MWU3NmExYzA3YTRmMDFiZjY3ZmZmYjhiODYzMTAzZGZmYWE4MDlkM2JmNzUyYjBkMTUxNDRmZjE6YTcwZjQ0N2UyMzg1Mzg1ZTdkOWExN2Y1ZDE0ZTc3NTAyOTRiOWZhZTE0YzA1NDlkMjNhYmZmY2MxMDEzMjdiYg==

```

See example requests below.
###### Access Token Request
The body sent in the POST request is a URL-encoded string that contains the following parameters:  
| **Parameter Name**  | **Type**  | **Required**  | **Description**  |  
| --- | --- | --- | --- |  
| `client_id`  | string  | yes  | Webex integration client ID  |  
| `client_secret`  | string  | yes  | Webex integration client secret  |  
| `code`  | string  | yes  | Authorization code obtained by a previous call to the [authorization endpoint](https://developer.webex.com/docs/login-with-webex#authorization-endpoint)  |  
| `code_verifier`  | string  | no  | PKCE code verifier, required if the request to the [authorization endpoint](https://developer.webex.com/docs/login-with-webex#authorization-endpoint) included `code_challenge` and `code_challenge_method` parameters. Must be between 43-128 characters and consist only of [unreserved characters](https://datatracker.ietf.org/doc/html/rfc3986#section-2.3). See [Authorization Code Flow with Proof Key for Code Exchange](https://developer.webex.com/docs/login-with-webex#authorization-code-flow-with-proof-key-for-code-exchange-pkce) for more information.  |  
| `grant_type`  | string  | yes  | Must be set to "authorization_code"  |  
| `redirect_uri`  | string  | yes  | Valid URI. Must be the same as the `redirect_uri` specified in the [authorization code request](https://developer.webex.com/docs/login-with-webex#authorization-endpoint).  |  
| `user_info`  | string  | no  | JSON object with additional requested information about the user or resource (for example `{'device_id': 'xxxxxxxx', 'device_name': 'Home-DX80'}`).  |  
The following is an example request for an access token that contains the client ID and secret in the request body.

```
POST /v1/access_token HTTP/1.1
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Host: webexapis.com

grant_type=authorization_code&code=M2ZmNjdlM2MtNzQzNS00MjY1LTlhMzUtZDcxNWQxNDEyNWRhMTAzZGY1NmMtMjM0_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f&client_id=C65cbd0361e76a1c07a4f01bf67fffb8b863103dffaa809d3bf752b0d15144ff1&redirect_uri=https://www.example.com/auth&client_secret=a70f447e2385385e7d9a17f5d14e7750294b9fae14c0549d23abffcc101327bb

```

The following is an equivalent request that uses Basic authentication instead.

```
POST /v1/access_token HTTP/1.1
Authorization: Basic QzY1Y2JkMDM2MWU3NmExYzA3YTRmMDFiZjY3ZmZmYjhiODYzMTAzZGZmYWE4MDlkM2JmNzUyYjBkMTUxNDRmZjE6YTcwZjQ0N2UyMzg1Mzg1ZTdkOWExN2Y1ZDE0ZTc3NTAyOTRiOWZhZTE0YzA1NDlkMjNhYmZmY2MxMDEzMjdiYg==
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Host: webexapis.com

grant_type=authorization_code&code=ZDYxYWZiYmMtYTU0NC00NTQ2LTgwMGEtZjZhNWJjOWQxNGViYzRmMDExNDMtMzE0_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f&redirect_uri=https://www.example.com/auth

```

###### Access Token Response
Successful responses will be accompanied with a body in JSON format with the following properties:  
| **Property Name**  | **Type**  | **Description**  |  
| --- | --- | --- |  
| `expires_in`  | long  | The lifetime in seconds of the access token. For example, the value '5999' denotes that the access token will expire in 5999 seconds from the time the response was generated.  |  
| `token_type`  | string  | The type of access token, currently only "Bearer" is supported.  |  
| `refresh_token`  | string  |  [Refresh token](https://developer.webex.com/docs/integrations#using-the-refresh-token) for obtaining a new access token.  |  
| `refresh_token_expires_in`  | long  | The lifetime in seconds of the refresh token.  |  
| `access_token`  | string  | API access token with scopes specified in initial request to authorization server.  |  
| `id_token`  | string  | OpenID Connect ID token, only present if the original request to the authorization server contained the `openid` scope.  |  
Below is an example JSON response body for a successful request for an access token.

```
{
  "access_token": "NjlhN...",
  "expires_in": 1209599,
  "refresh_token": "Nzc0N...",
  "refresh_token_expires_in": 7775999,
  "token_type": "Bearer"
}

```

###### Device Token Endpoint
Device clients use this endpoint to poll for access and refresh tokens after presenting the verification URL and user code (or equivalent QR code) to the user. The user opens the verification URL and enters the user code (or uses the provided QR code) to authorize the request. Until the user has finished the authorization process the request will return Once the user has completed the authentication using the provided Once the user has authenticated with Webex and granted authorization on another device, the next polling request will be successful and the endpoint will return access and refresh tokens with the requested scopes.

```
POST https://webexapis.com/v1/device/token

```

###### Authorization
This endpoint requires Basic authentication to authenticate the request. The request must contain an `Authorization <credentials>`, where `<credentials>` is a Base64-encoding of your integration's client ID and secret separated by a colon.

```
Authorization: Basic <credentials>

```

###### Device Token Request
The body sent in the POST request is a URL-encoded string that contains the following parameters:  
| **Parameter Name**  | **Type**  | **Required**  | **Description**  |  
| --- | --- | --- | --- |  
| `grant_type`  | string  | yes  | Value must be set to **urn:ietf:params:oauth:grant-type:device_code**  |  
| `device_code`  | string  | yes  | Valid device code received from the [Device Authorization Endpoint](https://developer.webex.com/docs/login-with-webex#device-authorization-endpoint).  |  
| `client_id`  | string  | yes  | Must match client ID used in previous call to the [Device Authorization Endpoint](https://developer.webex.com/docs/login-with-webex#device-authorization-endpoint).  |  
| `self_contained_token`  | string  | no  | Set to `true` to get a self-contained access token. Self-contained access tokens may be significantly quicker and more efficient as the API server doesn't need to look up authorization information for each request.  |  
| `user_info`  | string  | no  | Additional information about the user or resource in JSON-formatted string, for example: `{"device_id": "xxxxxxxx", "device_name": "Home-DX80"}`  |  
Example request:

```
POST /v1/device/token HTTP/1.1
Authorization: Basic QzY1Y2JkMDM2MWU3NmExYzA3YTRmMDFiZjY3ZmZmYjhiODYzMTAzZGZmYWE4MDlkM2JmNzUyYjBkMTUxNDRmZjE6OTMzNDc0ZWQ2NjkxN2QxZWUxMThhMjE4NzBkZDg3ZWMzYzQ5YTkwMmY2MDFiOTYwZDViZDE4MGNjMGY5NDI4Ng==
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Host: webexapis.com

grant_type=urn:ietf:params:oauth:grant-type:device_code&device_code=9c697e89-552c-4b27-bbfc-57a831cdf5fe&client_id=C65cbd0361e76a1c07a4f01bf67fffb8b863103dffaa809d3bf752b0d15144ff1

```

###### Device Token Response
The following are possible response codes for the device token response:  
| **Response Code**  | **Description**  |  
| --- | --- |  
| `200 OK`  | The request was successfully processed, see the response body for results.  |  
| `400 Bad Request`  | An invalid `client_id` or invalid `scope` parameter was provided in the request. Possible error messages: 
  * unsupported_grant_type
  * invalid_request
  * invalid_grant
  * invalid_client
  * access_denied
  * tokenlimit_reached
  * authorization_pending
  * slow_down

 |  
| `428 Precondition Required`  | The authorization request is still pending as the end user hasn't yet completed the authenticating with Webex and approving the request. The device client should poll again after  |  
The response is JSON object with the following properties:  
| **Property Name**  | **Type**  | **Description**  |  
| --- | --- | --- |  
| `scope`  | string  | The scopes associated with the token.  |  
| `expires_in`  | long  | The lifetime in seconds of the access token. For example, the value '5999' denotes that the access token will expire in 5999 seconds from the time the response was generated.  |  
| `token_type`  | string  | The type of access token, currently only "Bearer" is supported Bearer  |  
| `refresh_token`  | string  |  [Refresh token](https://developer.webex.com/docs/integrations#using-the-refresh-token) for obtaining a new access token..  |  
| `refresh_token_expires_in`  | long  | The lifetime in seconds of the refresh token.  |  
| `access_token`  | string  | API access token.  |  
The following is an example successful response.

```
{
  "scope": "meeting:schedules_read",
  "expires_in": 64799,
  "token_type": "Bearer",
  "refresh_token": "MjZmMzcyZWUtMzI2MS00MmE4LTgyZWMtYTVlMWIxYzBjZjhiODJmYzViOTItMGFi_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f",
  "access_token": "eyJhbGciOiJSUzI1NiJ9.eyJjbHVzdGVyIjoiUEY4NCIsInByaXZhdGUiOiJleUpqZEhraU9pSktWMVFpTENKbGJtTWlPaUpCTVRJNFEwSkRMVWhUTWpVMklpd2lZV3huSWpvaVpHbHlJbjAuLll3eWhjUmZ2LTRQU3NlVHdvMkdfQ0EuNmUtcndTYzVqLXBaZ1V1bjgyQUozeVVYY1VhWmxXNm93Nnh4QTZhZWpIY2lxR0lTZEFCUURraS10RDNsWEtSMlZDMENkc1ZQQWxFOWZxT0FqUGpHTmhIUi1WVlF2dzZWMmNRU2ItMFdyR3doS2ZKV08wcWxzYXU3Ym9tcmxCbVFjVlZab1pfRUZtUGp4aUN6XzQtVHQyR0lyNW90OTRZbXhsbmdPblpwcEF6WjViY1dGdkZsd1k1dC05QmZBbldwOFI2bnlCQ3Q4Vjk3Y1IxSjd6OWdiZGJMcU5fVXVpWUhaSHU4QjFvX2c1bUVLNEpIaUltZlh1QTRRY3BRX1RGZ0F4VEVqZ1hzVzFYS0c1a3dVU3ZPaHY0dnI5dzFzbXR5N2kzU1FiNWhIODFCc0Z4Z3FXSEx6eUlFYmtQNzRueEZFZDdOZDV4Rm1YcEhYZEJuMXhmMGxiYlowbFZTbFdxMnJzcVFSQ25XUXRUQzltdjJBV3FqZVBtSzZZVVNRZWFKUnNBMGZNdnhKVFJHYkhOZjdnY0RVT1AyRWxobmNXX21kQW05cVgxb2dNTS5MRk4yMEdtSEl1NTVkY29HOHd2QlFRIiwidXNlcl90eXBlIjoidXNlciIsInRva2VuX2lkIjoiQWFaM3IwTVdReU1URm1OVEl0TUdabE55MDBPVFF3TFdJeE5tWXRPRGsxTURVNFlUUTFORFU1TldJM09XTmpNR1V0WVdZeSIsInJlZmVyZW5jZV9pZCI6ImM0NzkwMGIzLWM1ZDgtNDhmYS1iMGRiLTU1NWIyZDU4NmVlOCIsImlzcyI6Imh0dHBzOlwvXC9pZGJyb2tlci53ZWJleC5jb21cL2lkYiIsInVzZXJfbW9kaWZ5X3RpbWVzdGFtcCI6IjIwMjIwNzI3MDY1MzQyLjUyNloiLCJyZWFsbSI6IjFlYjY1ZmRmLTk2NDMtNDE3Zi05OTc0LWFkNzJjYWUwZTEwZiIsImNpc191dWlkIjoiMzE0OTM3ZDYtYjFiOC00OTA1LWE1OGEtMzI0NDkxN2Y4NTNhIiwidG9rZW5fdHlwZSI6IkJlYXJlciIsImV4cGlyeV90aW1lIjoxNjU5MDA2MDkyNzMxLCJjbGllbnRfaWQiOiJDNjVjYmQwMzYxZTc2YTFjMDdhNGYwMWJmNjdmZmZiOGI4NjMxMDNkZmZhYTgwOWQzYmY3NTJiMGQxNTE0NGZmMSJ9.joqxBEelgwLOzVUER95Tz12A1xKxcUAPnYghHHtO4SDLO9aFLiDO8i6Et0hpAju6UrVGFnO81IqyQDboZrco-lr6-LkqSM7pdHw6NMzMgcOsnBO38_KN-vwvqR8iF_CyMj51A5S5UwWdQs6llYBqH4xFl8gXSgCmEp9P_W2T7SH2du_C23SAdeiijUMQfyrQrv8hJlieFOlrAQ7oTgjH0pJFZpo55w--h5utzF0F5XPQF4QkyeyyBoPkZeAzD9HWAqvwnpR0BN3My4rFRIcfNtLWuyMyHX3Gg9_I1EPbZ50SBZyR3f6gLVF6B4UZ8TgaMkuQt6gKBgDnu9nNThzVog",
  "refresh_token_expires_in": 7697037
}

```

###### UserInfo Endpoint
The UserInfo endpoint returns user claims about the authenticated user as a JSON object. The claims in the response are determined by the [scopes](https://developer.webex.com/docs/login-with-webex#openid-connect-scopes-and-claims) specified in the original request to the [Authorization Endpoint](https://developer.webex.com/docs/login-with-webex#authorization-endpoint) or [Device Authorization Endpoint](https://developer.webex.com/docs/login-with-webex#device-authorization-endpoint).

```
GET https://webexapis.com/v1/userinfo

```

###### Authentication
Requests must include an `Authorization: Bearer` header field whose value is an access token obtained via one of the [supported OpenID Connect authentication flows](https://developer.webex.com/docs/login-with-webex#supported-oauth-and-openid-connect-flows). 
###### UserInfo Request
Requests to `/v1/userinfo` must include an `Authorization: Bearer` header field whose value is an access token obtained via one of the [supported OpenID Connect authentication flows](https://developer.webex.com/docs/login-with-webex#supported-oauth-and-openid-connect-flows). It returns a JSON object whose field names map directly to the claims for the [requested OpenID Connect scopes](https://developer.webex.com/docs/login-with-webex#openid-connect-scopes-and-claims). 

```
GET https://webexapis.com/v1/userinfo

```

The endpoint has no request parameters.
Below is a sample request to `/v1/userinfo`.

```
GET /v1/userinfo HTTP/1.1
Authorization: Bearer NTgxMTA2MWItNTNhZS00NDE4LTkxY2YtZWIzZTlhZThjNmE3MDEzMmNiNjAtODg3_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f
Host: webexapis.com

```

###### UserInfo Response
The response is a JSON object whose available fields are determined by the [Open ID Connect scopes](https://developer.webex.com/docs/login-with-webex#openid-connect-scopes-and-claims) included in the the prior request:  
| **Property Name**  | **Type**  | **Description**  |  
| --- | --- | --- |  
| `sub`  | String  | Unique ID assigned to the user. This can be used to associate the user with a new session, for example,  |  
| `email`  | String  | User's email address.  |  
| `email_verified`  | String  | String that indicates if user has verified their email with Webex.  |  
| `given_name`  | String  | User's full name.  |  
| `name`  | String  | User's given name.  |  
| `family_name`  | String  | User's family name.  |  
| `phone`  | String  | User's phone number.  |  
The following is an sample successful response from a request `/v1/userinfo`. In this case the request included `scope=openid` so the JSON object only contains the `sub` field (claim) from the [openid scope](https://developer.webex.com/docs/login-with-webex#openid).

```
{
  "sub": "ad741856-1234-5678-b34c-bad0bb62d877",
}

```

The following is an sample successful response from a request `/v1/userinfo`. In this case the request included `scope=openid email profile` so the response object contains fields corresponding to those scopes. 

```
{
  "sub": "ad741856-1234-5678-b34c-bad0bb62d877",
  "email": "jsmith@example.com",
  "email_verified": "true",
  "name": "Jane Smith",
  "given_name": "Jane",
  "family_name": "Smith"
}

```

###### Verification Endpoint
The verification endpoint returns a list of [JSON Web Keys](https://datatracker.ietf.org/doc/html/rfc7517) (JWKs)

```
GET https://webexapis.com/v1/verification

```

###### Verification Request
The request has no parameters and doesn't require any authentication.

```
GET /v1/verification HTTP/2
Host: webexapis.com

```

###### Verification Response
The response is a JSON object with a top-level `keys` array consisting of one or more verification key objects. The following lists the properties of each object:  
| **Parameter Name**  | **Type**  | **Description**  |  
| --- | --- | --- |  
| `kty`  | string  | Key type. Identifies the cryptographic algorithm family used with the keyIts value is always "RSA".  |  
| `e`  | string  | The exponent part of the key  |  
| `n`  | string  | The modulus part of the key  |  
| `kid`  | string  | The unique ID of the key  |  
| `use`  | string  | The use of the key. Its value is always "sig".  |  
Below is an example JSON response from the verification endpoint.

```
{
  "keys": [
    {
      "kty": "RSA",
      "e": "AQAB",
      "use": "sig",
      "kid": "19af361a-3ab4-5471-a5b0-72d184294c2f",
      "n": "m2X-dYXa...t8SG711w"
    },
    {
      "kty": "RSA",
      "e": "AQAB",
      "use": "sig",
      "kid": "5f2cf832-cca9-5cd6-9a34-2c12a1c2ee7f",
      "n": "kHJbk0_...veNQg2Q"
    },

```

###### Discovery Endpoint
The [discovery endpoint](https://webexapis.com/v1/.well-known/openid-configuration) returns the information needed for an OAuth client to interact with the Webex authorization server, including its endpoint locations and authorization server capabilities.

```
https://webexapis.com/v1/.well-known/openid-configuration

```

This endpoint requires no authentication.
###### Discovery Request
The following is a request for the Webex OAuth discovery document.

```
GET /v1/.well-known/openid-configuration
Host: webexapis.com

```

###### Discovery Response
The response is a JSON object with the following properties:  
| **Property**  | **Description**  |  
| --- | --- |  
| `issuer`  | The authorization server's issuer identifier.  |  
| `authorization_endpoint`  | URL of the authorization server's authorization endpoint  |  
| `token_endpoint`  | URL of the authorization server's token endpoint  |  
| `userinfo_endpoint`  | URL of the authorization server's UserInfo endpoint  |  
| `jwks_uri`  | URL of the authorization server's [JWK Set](https://www.rfc-editor.org/rfc/rfc7517.html#section-5) document. The referenced document contains the signing key(s) your app uses to validate ID tokens signed by Webex.  |  
| `scopes_supported`  | JSON array containing a list of the [OpenID Connect scope](https://developer.webex.com/docs/login-with-webex#openid-connect-scopes-and-claims) values that the authorization server supports.  |  
| `response_types_supported`  | JSON array containing a list of the OAuth 2.0 "response_type" values that this authorization server supports.  |  
| `id_token_signing_alg_values_supported`  | JSON array containing a list of the JWS signing algorithms ("alg values") supported by the authorization server for encoding the claims in an ID token.  |  
| `code_challenge_methods_supported`  | JSON array containing a list of Proof Key for Code Exchange (PKCE) code challenge methods supported by the authorization server.  |  
| `subject_types_supported`  | JSON array containing a list of the subject identifier types supported by the authorization server.  |  
| `claims_supported`  | JSON array containing a list of the claims that the authorization server supports for ID tokens (JWTs).  |  
| `grant_types_supported`  | JSON array containing a list of the OAuth 2.0 Grant Type values that this OpenID Connect Identity Provider (IDP) supports.  |  
|   |   |  
|  `request_parameter_supported`.  | Boolean value specifying whether the OpenID Connect Identity Provider (IDP) supports use of the request parameter, with true indicating support. If omitted, the default value is false.  |  
|   |   |  
| `request_uri_parameter_supported`  | Boolean value specifying whether the OpenID Connect Provider supports use of the request_uri parameter, with true indicating support. If omitted, the default value is true.  |  
|   |   |  
| `token_endpoint_auth_methods_supported`  | JSON array containing a list of Client Authentication methods supported by this Token_endpoint. The options are: client_secret_post, client_secret_basic, client_secret_jwt, private_key_jwt  |  
|   |   |  
Below is a sample JSON response to a request to the discovery endpoint.

```
{
  "issuer": "https://idbroker-b-us.webex.com/idb",
  "authorization_endpoint": "https://webexapis.com/v1/authorize",
  "token_endpoint": "https://webexapis.com/v1/access_token",
  "userinfo_endpoint": "https://webexapis.com/v1/userinfo",
  "jwks_uri": "https://webexapis.com/v1/verification",
  "response_types_supported": ["code", "id_token"],
  "subject_types_supported": ["public"],
  "id_token_signing_alg_values_supported": ["RS256"],
  "scopes_supported": ["openid", "email", "profile", "phone", "address"],
  "claims_supported": [
    "aud",
    "sub",
    "auth_time",
    "iss",
    "exp",
    "iat",
    "nonce",
    "email",
    "email_verified",
    "name",
    "given_name",
    "family_name",
    "locale",
    "phone",
    "address"
  ],
  "grant_types_supported": [
    "authorization_code",
    "implicit",
    "refresh_token"
  ],
  "request_parameter_supported": false,
  "request_uri_parameter_supported": false,
  "token_endpoint_auth_methods_supported": [
    "client_secret_basic"
  ] 
  "code_challenge_methods_supported": ["plain", "S256"]
}

```

###### Webfinger Endpoint
The Webfinger endpoint is used to discover information about people or other entities on the Internet. It returns a JSON object that describes the person or entity that is queried. The JSON object is referred to as the JSON Resource Descriptor (JRD).

```
https://webexapis.com/v1/.well-known/webfinger

```

This endpoint requires no authentication.
###### Webfinger Request
The request takes a query parameter named `resource` that identifies the target user of the discovery request:  
| **Parameter**  | **Type**  | **Required**  | **Description**  |  
| --- | --- | --- | --- |  
| `resource`  | string  | yes  | Identifier for the target user that is the subject of the discovery request, prefixed with `acct:` (`acct:jdoe@example.com`, for example).  |  

```
GET /v1/.well-known/webfinger?resource=acct:jdoe@example.com
Host: webexapis.com

```

###### Webfinger Response
The response is [JSON Resource Descriptor](https://datatracker.ietf.org/doc/html/rfc7033#section-4.4) that contains information about the requested user.

```
{
    subject: "acct:joe@example.com",
    links: [
        {
            rel: "http://openid.net/specs/connect/1.0/issuer",
            href: "https://idbroker.webex.com/idb"
        }
    ]
}

```

####  anchorGetting an ID Token with Authorization Code Flow
anchor
In this flow your app first requests an authorization code that it then exchanges for an ID token, access token and refresh token.
To start the authorization code flow, your app directs the user's web browser to the [Authorization endpoint](https://developer.webex.com/docs/login-with-webex#authorization-endpoint) with your integration's client ID, the requested scopes, redirect URI, and a state variable. For example, below is an example request to the initiate the authorization process. In this case the `scope` request parameter is set to `openid email profile meeting:schedules_read`. (Line breaks for readability, only.)

```
GET /v1/authorize?redirect_uri=https://www.example.com/auth&scope=openid email profile meeting:schedules_read
&client_id=C7480d953df4816dfe7e1b50fbac7f3b8da6b58efec1846ba47ab357b8ace6cc4
&response_type=code HTTP/1.1
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Host: webexapis.com

```

After the user authenticates with Webex and approves the requested scopes, their browser is redirected to the specified `redirect_uri`. The URI is appended with a `code` query parameter that contains the authorization code and the value of the `state` sent in the request. Below is an example response.

```
https://www.example.com/auth?code=ZDA4MzUyMWYtZmFmOS00MTk2LTkyNTktYTNiMjc4MjZhZGY4ZDkyNmYzMDgtMDlj_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f&state=12345

```

Your app extracts the authorization code from the redirect URI to make a request to the [access token endpoint](https://developer.webex.com/docs/login-with-webex#access-token-endpoint). To authenticate the request, the request body must either contain both `client_id` and `client_secret`, or you must use Basic authentication with the following header, where `<credentials>` is a base-64 encoding of "client_id:client_secret".

```
Authorization: Basic <credentials>

```

For example, below is a sample request to the Access Token Endpoint to exchange an authorization code for an ID token.

```
POST /v1/access_token HTTP/1.1
Authorization: Basic QzY1Y2JkMDM2MWU3NmExYzA3YTRmMDFiZjY3ZmZmYjhiODYzMTAzZGZmYWE4MDlkM2JmNzUyYjBkMTUxNDRmZjE6YTcwZjQ0N2UyMzg1Mzg1ZTdkOWExN2Y1ZDE0ZTc3NTAyOTRiOWZhZTE0YzA1NDlkMjNhYmZmY2MxMDEzMjdiYg==
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Host: webexapis.com

grant_type=authorization_code&code=ZDYxYWZiYmMtYTU0NC00NTQ2LTgwMGEtZjZhNWJjOWQxNGViYzRmMDExNDMtMzE0_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f&redirect_uri=https://www.example.com/auth

```

The following is an example JSON response object containing an ID token, access token, and refresh token. See the [Access Token endpoint reference](https://developer.webex.com/docs/login-with-webex#access-token-endpoint) for field descriptions.

```
{
  "access_token": "ZDk1ZG...ca4d1f",
  "expires_in": 1209599,
  "refresh_token": "MWIyN...ca4d1f",
  "refresh_token_expires_in": 7775999,
  "token_type": "Bearer",
  "id_token": "eyJhbGc...zI1NiJ9",
  "scope": "openid profile email"
}

```

ID tokens returned by this endpoint only contain claims for the [openid scope](https://developer.webex.com/docs/login-with-webex#openid), regardless of other OpenID Connect scopes were requested. To get user claims for all requested [scopes](https://developer.webex.com/docs/login-with-webex#openid-connect-scopes-and-claims) (email, profile, phone, or location), call the [UserInfo Endpoint](https://developer.webex.com/docs/login-with-webex#userinfo-endpoint) with the access token that was returned with the ID token.
####  anchorGetting ID and Access Tokens with Authorization Code Flow with PKCE
anchor
[Proof Key for Code Exchange](https://datatracker.ietf.org/doc/html/rfc7636) (PKCE) is an extension to the [Authorization Code](https://developer.webex.com/docs/login-with-webex#getting-an-id-token-with-authorization-code-grant-flow) flow to prevent Cross-Site Request Forgery (CSRF) and authorization code injection attacks. PKCE adds the following parameters to the standard Authorization Code flow:
  * **code_verifier** — A cryptographically random string used to correlate the authorization request to the token request. The code verifier must be between 43 and 128 characters in length and consist only of numbers (0-9), uppercase and lowercase letters (A-Z, a-z), hyphens (`-`), dots (`.`), underscores (`_`), and tildes (`~`).
  * **code_challenge** — A base64-encoded SHA-256 hash of `code_verifier` value (or the same value as the `code_verifier`, depending on the `code_challenge_method` used. The Webex OAuth server decrypts this value and uses it to verify that the authorization and access token requests are coming from the same client.
  * **code_challenge_method** — The transformation method used to derive the code challenge. Supported values are **S256** (for SHA-256 transforms) and **plain** (if no transform has been applied).


Apps are encouraged to prefer the SHA-256 code challenge method over plain.
For example, if `code_challenge_method` is `S256` the following pseudo-code shows how `code_challenge` is computed from `code_verifier`.

```
code_challenge = BASE64URL-ENCODE(SHA256(ASCII(code_verifier)))

```

If `code_challenge_method` is `plain` then `code_challenge` is equal to `code_verifier`. 

```
code_challenge = code_verifier

```

For example, below is an example request to initiate the Authorization Code flow with PKCE. Before making the call to `/v1/authorize` your app first needs to generate a code verifier from which the code challenge is derived. In this example, the `code_challenge` value (`h5REeLdS914fH3VaOKytjx5VNzHOCKHKYSRbzE0k6BM`) was generated using the SHA256 hashing algorithm indicated by `S256` as the value for `code_challenge_method`.

```
GET /v1/authorize?redirect_uri=https://www.example.com/auth
&scope=openid email profile meeting:schedules_read
&client_id=C7480d953df4816dfe7e1b50fbac7f3b8da6b58efec1846ba47ab357b8ace6cc4
&response_type=code
&code_challenge=h5REeLdS914fH3VaOKytjx5VNzHOCKHKYSRbzE0k6BM
&code_challenge_method=S256 HTTP/1.1
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Host: webexapis.com

```

Once the user authenticates with Webex and accepts the requested scopes, their browser is redirected to the specified `redirect_uri`. The URI is appended with a `code` query parameter that contains the authorization code, as well as the original `state` request parameter value. Your app should verify that the value of the `state` query parameter matches the original value used in the authorization request.

```
https://www.example.com/auth?code=ZDA4MzUyMWYtZmFmOS00MTk2LTkyNTktYTNiMjc4MjZhZGY4ZDkyNmYzMDgtMDlj_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f&state=12345

```

Next, you exchange the authorization code and code verifier for ID and access tokens by calling the [access token endpoint](https://developer.webex.com/docs/login-with-webex#access-token-endpoint). To authenticate the request, the request body must either contain both `client_id` and `client_secret`, or you must use Basic authentication with the following header, where `<credentials>` is a base-64 encoding of "client_id:client_secret".
The following is an example request to exchange an authorization code and code verifier for ID and access tokens.

```
POST /v1/access_token HTTP/1.1
Authorization: Basic Qzc0ODBkOTUzZGY0ODE2ZGZlN2UxYjUwZmJhYzdmM2I4ZGE2YjU4ZWZlYzE4NDZiYTQ3YWIzNTdiOGFjZTZjYzQ6MmIxYzE1YTAzZGM0OWQ1ZGVlNzk4NzVlMzk3NTZiODQ4MjdjMGM2YmQ0M2RhZTdlMDZkOTg0MzNlZWE2N2RhZg==
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Host: webexapis.com

grant_type=authorization_code&code=OTM2OWQ2MDUtMzljMi00YjlhLWIyMWEtNDkyYmVjY2QyZjZmMTk1MDRmN2EtMzg2_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f&redirect_uri=https://www.example.com/auth&code_verifier=forty_three_character_code_verifier_example

```

The Webex REST API responds with a JSON object that contains the ID token and access and refresh token.

```
{
 "access_token":"ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3",
 "id_token":"eyJhbGciOiJSUzI1NiJ9...",
 "expires_in":1209600, //seconds
 "refresh_token":"MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTEyMzQ1Njc4",
 "refresh_token_expires_in":7776000 //seconds
}

```

ID tokens returned by this endpoint only contain claims for the [openid scope](https://developer.webex.com/docs/login-with-webex#openid), regardless of other OpenID Connect scopes were requested. To get user claims for all requested [scopes](https://developer.webex.com/docs/login-with-webex#openid-connect-scopes-and-claims) (email, profile, phone, or location), call the [UserInfo Endpoint](https://developer.webex.com/docs/login-with-webex#userinfo-endpoint) with the access token that was returned with the ID token.
####  anchorGetting an Access Token with Device Grant Flow
anchor
The Device Grant Flow enables OAuth clients to request user authorization on devices that have limited input capabilities or lack a suitable web browser to perform the authentication.
For a complete sample that illustrates the Device Grant Flow from end to end, see the following GitHub repo, [webex-device-oauth-sample](https://github.com/WebexSamples/webex-device-oauth-sample).
**Steps to obtain access and refresh tokens using Device Grant flow** :
  1. The app running on the device requests device and user codes from the [Device Authorization](https://developer.webex.com/docs/login-with-webex#device-authorization-endpoint) endpoint (`/v1/device/authorize`), passing the client ID of your Webex integration and the desired [access scopes](https://developer.webex.com/docs/integrations#scopes).

```
POST /v1/device/authorize HTTP/1.1
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Host: webexapis.com

client_id=C65cbd0361e76a1c07a4f01bf67fffb8b863103dffaa809d3bf752b0d15144ff1&scope=meeting:schedules_read

```

A successful response contains a JSON object that contains a device code, user code, and verification URLs the user opens to authenticate with Webex and enter their user code.

```
{
  "device_code": "992e7fc0-89b8-4cc7-bfd8-0fc9122c1190",
  "expires_in": 300,
  "user_code": "463682",
  "verification_uri": "https://oauth-helper-r.wbx2.com/verify",
  "verification_uri_complete": "https://oauth-helper-r.wbx2.com/verify?userCode=e50621e1029ce4772ed57a61d8aef6cfcdac2867879b8ecbd1a7ea9a7cd09f0a",
  "interval": 2
}

```

  2. Upon receipt of the user code, device code, and verification URLs, the app does one of the following:
     * Presents a QR code that has the `verification_uri_complete` URL encoded in it. The `verification_uri_complete` URL contains a hashed version of the `user_code` so the user doesn't need to manually enter the code. The user captures the QR code with their mobile device which automatically opens the encoded URL. This is the recommended approach as it is easier for users.
     * Presents the `verification_uri` and `user_code` to the user and provides instructions for them to navigate to the URL on another device and enter their user code.
  3. Your app begins polling the [Device Token endpoint](https://developer.webex.com/docs/login-with-webex#device-token-endpoint) at the interval specified by the `interval` field in the JSON response to the [Device Authorization endpoint](https://developer.webex.com/docs/login-with-webex#device-authorization-endpoint).

```
POST /v1/device/token HTTP/1.1
Authorization: Basic QzY1Y2JkMDM2MWU3NmExYzA3YTRmMDFiZjY3ZmZmYjhiODYzMTAzZGZmYWE4MDlkM2JmNzUyYjBkMTUxNDRmZjE6OTMzNDc0ZWQ2NjkxN2QxZWUxMThhMjE4NzBkZDg3ZWMzYzQ5YTkwMmY2MDFiOTYwZDViZDE4MGNjMGY5NDI4Ng==
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Host: webexapis.com

grant_type=urn:ietf:params:oauth:grant-type:device_code&device_code=fe518a17-47c6-4ed3-a29c-a25dcc845f7a&client_id=C65cbd0361e76a1c07a4f01bf67fffb8b863103dffaa809d3bf752b0d15144ff1

```

Before the user has finished the authorization process the HTTP response to each polling request will have a `428 Precondition Required` HTTP error code.

```
HTTP/1.1 428 Precondition Required

```

  4. Once the user has finished the authorization process the app's next polling request will return `200 OK` and the response body will contain the access token and refresh token, for example:

```
Content-Type: application/json
HTTP/1.1 200 OK

{
  "scope": "meeting:schedules_read",
  "expires_in": 64799,
  "token_type": "Bearer",
  "refresh_token": "MjZmMzcyZWUtMzI2MS00MmE4LTgyZWMtYTVlMWIxYzBjZjhiODJmYzViOTItMGFi_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f",
  "access_token": "eyJhbGciOiJSUzI1NiJ9.ueODqA4sremRmI3x9oEHd0oxY.jHbeIn6Sd66TCPb2GUxgYMbgKjNp",
  "refresh_token_expires_in": 7688366
}

```



###### OAuth Helper Service URIs
To use the Device Grant flow your Webex [Integration](https://developer.webex.com/docs/integrations) must include the following as redirect URIs.
  * <https://oauth-helper-a.wbx2.com/helperservice/v1/actions/device/callback>
  * <https://oauth-helper-r.wbx2.com/helperservice/v1/actions/device/callback>
  * <https://oauth-helper-k.wbx2.com/helperservice/v1/actions/device/callback>


####  anchorGetting an ID Token or Access Token with Implicit Flow
anchor
In the implicit OAuth flow the [authorization endpoint](https://developer.webex.com/docs/login-with-webex#authorization-endpoint) returns ID and access tokens directly in the response URL. For example, the following is sample request to `/v1/authorize` with a `response_type` of `id_token` and `scope=openid`, and `state` set to a random string.

```
GET /v1/authorize?response_type=id_token&scope=openid
&state=GA2ZPwXmN3StnxBOw42nG8kJVd4P7uGgRg87xJjttPCfq3jEDD4lMggptNrFfdE
&client_id=Cdb2d3819c88074b69b31552b41b18df7d1bff707fee810d57d73cae92cdc5ee6
&nonce=ZfBEQWKkZXcV2ek6Yryno2YFeyjM7tirn8pMpfOpHD8b8ykaWekSSEK5A9m2tUY
&redirect_uri=https://www.example.com/auth

Host: webexapis.com

```

Once the user has authenticated with Webex and accepted the requested permissions (scopes) they are redirected to the `redirect_uri` specified in the request. The authorization server appends `id_token` to the redirect URL whose value is the signed, encoded [ID token](https://developer.webex.com/docs/login-with-webex#id-tokens) (JWT), and a `state` parameter with the same value as in the request, for example:

```
http://www.example.com/app#id_token=eyJhbGciOi...&state=GA2ZPwXmN...

```

You can extract the ID token from the URL and [decode](https://developer.webex.com/docs/login-with-webex#id-tokens) it to access its [claims](https://developer.webex.com/docs/login-with-webex#openid-connect-scopes-and-claims).
####  anchorID Tokens
anchor
An ID token is a signed, Base64-encoded [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) (JWT). A JWT consists of a header, payload, and signature. The header and signature are used to verify the authenticity of the token, while the payload contains the requested [OpenID Connect claims](https://developer.webex.com/docs/login-with-webex#openid-connect-scopes-and-claims) about the user, such as email, name, and so forth. ID tokens [must be validated](https://developer.webex.com/docs/login-with-webex#validating-id-tokens) before being used.
The specific [user claims](https://developer.webex.com/docs/login-with-webex#openid-connect-scopes-and-claims) in an ID token depends on scopes specified in the initial request to the [authorization endpoint](https://developer.webex.com/docs/login-with-webex#authorization-endpoint). The following is an example of an ID token that was generated with just the ["openid"](https://developer.webex.com/docs/login-with-webex#openid) scope.

```
{
    "aud": "Cece89a8697f5c251a633bbe7a93c7c39c8b963c0b4f181f887e0838e7ca881b0",
    "sub": "314937d6-b1b8-4905-a58a-3244917f853a",
    "auth_time": 1656377597,
    "iss": "https://idbroker.webex.com/idb",
    "exp": 1656385410,
    "iat": 1656378210,
    "nonce": "jIXGCWkXWFoSBDDPuNAqr4OOWd4M91Xe6LJQ2g6m3HYBxWCuyWsJT5hOWbXEo2u"
}

```

The following JSON is an example of a token that was generated with ["openid"](https://developer.webex.com/docs/login-with-webex#openid) and ["email"](https://developer.webex.com/docs/login-with-webex#email) scopes.

```
{
    "aud": "Cbaa02efbfd0b4aed22828ffd0beb6d1fad352811920103085d5e12a04b52f6c5",
    "sub": "ad741856-4062-494a-b34c-bad0bb62d877",
    "email_verified": true,
    "auth_time": 1656710423,
    "iss": "https://idbroker-b-us.webex.com/idb",
    "exp": 1656725790,
    "iat": 1656718590,
    "nonce": "yLEcKOgSgWZxIyukT2vdU6LwIbo8HwPLXW1BCqmSqC8ugeTGVAd0gePSXMSvg8X",
    "email": "user@example.com"
}

```

###### Validating ID Tokens
Before using the information in an ID token (JWT), or using it as proof that a user authenticated with Webex, you **must** validate it. There are many [open-source libraries available](https://jwt.io/libraries) that can validate JWTs.
###### Decoding ID Tokens
Raw ID tokens are Base64-encoded and must be decoded to access the user data they contain. For example, the following Node.js example uses the [jwt_decode](https://github.com/auth0/jwt-decode) Node.js package to decode and print an ID token's claims.

```
import jwt_decode from "jwt-decode";

var token = "eyJhbGciOiJSUzI1NiJ9...<JWT TOKEN>";
var decoded = jwt_decode(token);

console.log(decoded);

// Prints
// {
//   aud: 'Ce7864edfe55...',
//   sub: 'ad741856-4062...',
//   email_verified: true,
//   auth_time: 1653956956,
//   iss: 'https://idbroker-b-us.webex.com/idb',
//   name: 'Jane Smith',
//   exp: 1653983030,
//   given_name: 'Jane',
//   iat: 1653975830,
//   nonce: '0.5782863480185514',
//   family_name: 'Smith',
//   email: 'jsmith@example.com'
// }

```

####  anchorOpenID Connect Scopes and Claims
anchor
OpenID Connect defines a set of valid scopes apps can specify when initiating a login process. The requested scopes determine what claims are contained by the ID token returned after a successful authentication. The only scope required to use Login with Webex is `openid`.
The following scopes are available with Login with Webex.
  * [openid](https://developer.webex.com/docs/login-with-webex#openid)
  * [email](https://developer.webex.com/docs/login-with-webex#email)
  * [profile](https://developer.webex.com/docs/login-with-webex#profile)
  * [phone](https://developer.webex.com/docs/login-with-webex#phone)
  * [address](https://developer.webex.com/docs/login-with-webex#address)


###### openid
Required. The `openid` scope returns a token with the following claims:  
| Claim  | Description  |  
| --- | --- |  
| `aud`  | Client ID of the Webex integration used to make the initial authentication request.  |  
| `sub`  | Unique ID assigned to the user. This can be used to associate the user with a new session, for example,  |  
| `auth_time`  | Time when the user authentication occurred. Its value is a JSON number representing the number of seconds from 1970-01-01T0:0:0Z as measured in UTC until the date/time.  |  
| `iss`  | URL of the Webex identity server that issued the ID token ("<https://idbroker-b-us.webex.com/idb>", for example).  |  
| `exp`  | Expiration time on or after which the ID Token must not be accepted for processing. Its value is a JSON number representing the number of seconds from 1970-01-01T0:0:0Z as measured in UTC until the date/time (see RFC 3339 [RFC3339] for details).  |  
| `iat`  | Time at which the ID Token was issued. Its value is a JSON number representing the number of seconds from 1970-01-01T0:0:0Z as measured in UTC until the date/time.  |  
| `nonce`  | String value used to associate a client session with an ID Token, and to mitigate replay attacks. Its value is sent in the initial authentication request as a query parameter. Clients must verify that the nonce claim value in the ID token is equal to the value of the nonce parameter sent in the authentication request.  |  
###### email
The `email` scope provides access to the user's email and a boolean that indicates if the email address has been verified with Webex:  
| Claim  | Description  |  
| --- | --- |  
| `email`  | User's email address.  |  
| `email_verified`  | Boolean that indicates if user has verified their email with Webex.  |  
###### profile
The `profile` scope provides access to basic user profile information, if available. The following user profile claims are returned:  
| Claim  | Description  |  
| --- | --- |  
| `given_name`  | User's full name.  |  
| `name`  | User's given name.  |  
| `family_name`  | User's family name.  |  
| `locale`  | User's locale.  |  
###### phone
The `phone` scope provides access to the user's phone number, if available:  
| Claim  | Description  |  
| --- | --- |  
| `phone`  | User's phone number.  |  
###### address
The `address` scope provides access to the user's address:  
| Claim  | Description  |  
| --- | --- |  
| `address`  | User's address.  |  
##### In This Article
  * [About Login with Webex](https://developer.webex.com/create/docs/login-with-webex#about-login-with-webex)
  * [Getting Started](https://developer.webex.com/create/docs/login-with-webex#getting-started)
  * [Supported OAuth and OpenID Connect Flows](https://developer.webex.com/create/docs/login-with-webex#supported-oauth-and-openid-connect-flows)
  * [OAuth 2.0 and OpenID Connect API Endpoints](https://developer.webex.com/create/docs/login-with-webex#oauth-20-and-openid-connect-api-endpoints)
  * [Getting an ID Token with Authorization Code Flow](https://developer.webex.com/create/docs/login-with-webex#getting-an-id-token-with-authorization-code-flow)
  * [Getting ID and Access Tokens with Authorization Code Flow with PKCE](https://developer.webex.com/create/docs/login-with-webex#getting-id-and-access-tokens-with-authorization-code-flow-with-pkce)
  * [Getting an Access Token with Device Grant Flow](https://developer.webex.com/create/docs/login-with-webex#getting-an-access-token-with-device-grant-flow)
  * [Getting an ID Token or Access Token with Implicit Flow](https://developer.webex.com/create/docs/login-with-webex#getting-an-id-token-or-access-token-with-implicit-flow)
  * [ID Tokens](https://developer.webex.com/create/docs/login-with-webex#id-tokens)
  * [OpenID Connect Scopes and Claims](https://developer.webex.com/create/docs/login-with-webex#openid-connect-scopes-and-claims)


## Connect
[Support](https://developer.webex.com/support)
[Developer Community](https://community.cisco.com/t5/webex-for-developers/bd-p/disc-webex-developers)
[Developer Events](https://developer.webex.com/blog/categories/events)
[Contact Sales](https://www.webex.com/contact-sales.html?TrackID=1017639&hbxref=&goid=us_contact_sales)
## Handy Links
[Webex Ambassadors](https://www.essentials.webex.com/programs/ambassadors)
[Webex App Hub](https://www.essentials.webex.com/programs/ambassadors)
## Resources
[Open Source Bot Starter Kits](https://ciscowebexteamsambassadors.github.io/StarterKits/)
[Download Webex](https://ciscowebexteamsambassadors.github.io/StarterKits/)
[DevNet Learning Labs](https://www.webex.com)
[Terms of Service](https://developer.webex.com/terms-of-service)
[Privacy Policy](https://www.cisco.com/c/en/us/about/legal/privacy.html)
[Cookie Policy](https://www.cisco.com/c/en/us/about/legal/privacy.html#cookies)
[Trademarks](https://www.cisco.com/c/en/us/about/legal/trademarks.html)
© 2026 Cisco and/or its affiliates. All rights reserved.
[](https://github.com/webex)[](https://www.facebook.com/CiscoCollab/)[](https://twitter.com/webexdevs)[](https://www.youtube.com/playlist?list=PL2k86RlAekM_bIUrvVw4Haq_0xxTez9zU)[](https://www.linkedin.com/company/webex/)
By continuing to use our website, you acknowledge the use of cookies. 
[Privacy Statement](https://www.cisco.com/c/en/us/about/legal/privacy-full.html) Change Settings
![Company Logo](https://cdn.cookielaw.org/logos/03fc55fe-0057-4b2f-817d-763e7ecdb316/a7f4c642-c43c-4666-acea-858c0449029c/cisco-logo-transparent.png)
## Consent Manager
Your opt out preference signal is honored.
## Consent Manager
  * ### Your Privacy
  * ### Strictly Necessary Cookies
  * ### Performance Cookies
  * ### Targeting Cookies
  * ### Functional Cookies


#### Your Privacy
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. From the list on left, please choose whether this site may use Performance and/or Targeting Cookies. By selecting Strictly Necessary Cookies only, you are requesting Cisco not to sell or share your personal data. Note, blocking some types of cookies may impact your experience on the site and the services we are able to offer.
#### Strictly Necessary Cookies
Always Active
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.
Cookies Details
#### Performance Cookies
Performance Cookies
These cookies provide metrics related to the performance and usability of our site. They are primarily focused on gathering information about how you interact with our site, including: page load times, response times, error messages, and allowing a replay of a visitor’s interactions with our site, which enables us to review and analyze visitor behavior, helping to improve site usability and functionality. These cookies also allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. If you do not allow these cookies we will not know when you have visited our site and will not be able to monitor its performance.
Cookies Details
#### Targeting Cookies
Targeting Cookies
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.
Cookies Details
#### Functional Cookies
Functional Cookies
These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.
Cookies Details
Back Button
### Cookie List
Filter Button
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Clear
  * checkbox label label


Apply Cancel
Save Settings
Allow All
[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/solutions/consent-and-preferences/)
