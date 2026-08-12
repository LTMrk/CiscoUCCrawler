[](https://developer.webex.com/)
[Getting Started](https://developer.webex.com/create/docs)Documentation![](https://developer.webex.com/create/docs/instant-connect-meeting-links)[AI in Webex](https://developer.webex.com/mcp/docs/webex-mcp-server-overview)Blog![](https://developer.webex.com/create/docs/instant-connect-meeting-links)[Support](https://developer.webex.com/explore/support)Resources![](https://developer.webex.com/create/docs/instant-connect-meeting-links)
[Log in](https://developer.webex.com/login)[Sign up](https://developer.webex.com/signup)
[Home](https://developer.webex.com/)/Instant Connect Meeting Links
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
    * [Overview](https://developer.webex.com/create/docs/instant-connect)
    * [Instant Connect Meeting Links](https://developer.webex.com/create/docs/instant-connect-meeting-links)
  * Workspace Integrations
  * Bring Your Own Datasource
  * [Suite Sandbox](https://developer.webex.com/create/docs/developer-sandbox-guide)
  * [Contact Center Sandbox](https://developer.webex.com/create/docs/sandbox_cc)
  * [Guest to Guest Sandbox](https://developer.webex.com/create/docs/g2g-sandbox)
  * [Submit Your App](https://developer.webex.com/create/docs/app-hub-submission-process)
  * [Tutorials](https://developer.webex.com/create/docs/tutorials)


## Getting Started
### Instant Connect Meeting Links
This guide shows how you can construct Instant Connect URLs for hosts and guests.
Using a simple REST API, you can easily generate Instant Connect URLs for one or multiple hosts and guests. The API allows for a variety of customizations via its request payload, including:
  * A configurable meeting subject
  * Not before and expiration times for the authorization JWT
  * Device support
  * Parameters to set the number of hosts and guests up to a maximum of 25 each
  * An option to generate short URLs
  * Various advanced encryption options


The guide includes a step by step example using Postman, if you're new to REST APIs. Alternatively, if you're a REST veteran, you can skip directly to the API Reference materials at the end of this document.
####  anchorPrerequisites
anchor
Before you can use Instant Connect, your Webex Admin will need to login to the Instant Connect webpage and choose **Activate Instant Connect** here:<https://instant.webex.com/integrate/>.
You only have to activate Instant Connect once.
Next, you'll need to generate an access token which is required to make the API call to retrieve the encrypted part of the URLs. You've got two options for access tokens:
  * A 12 hour time limited Personal Access token for development purposes
  * A 100 year Bot token for production use


In addition, optionally, to enable adding devices to the meeting, you'll need to configure Instant Rounding as described in the following help.webex.com article [Configure Virtual Rounding](https://help.webex.com/article/6vsdoi/).
###### Retrieve a Personal Access Token for Development
To obtain a Webex Personal Access Token (valid for 12 hours), navigate to the [Webex Developer Portal](https://developer.webex.com/docs/getting-started#accounts-and-authentication), login with your Webex org admin account, and copy the Bearer token value:
![Image described in surrounding text.](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt84e562902cf23694/63c03de3d2d671109381b574/01-personal-token.png)
###### Retrieve a Bot Token for Production Usage
For a production-level implementation, we recommend [creating a new Webex Bot](https://developer.webex.com/my-apps/new/bot) and using the Bot’s access token (valid for 100 years). You can copy the Bot access token once you've created your new bot:
![Image described in surrounding text.](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt8125b962e4bdceda/63c03de3def66d1d64a3b768/02-bot-token.png)
####  anchorStep by Step Instant Connect API Call Using Postman
anchor
With your access token, you use the Instant Connect API to retrieve the encrypted ciphers that you'll append to the base URLs for hosts and guests. In this section we'll use [Postman](https://www.postman.com/) to walk you through an example REST call that generates ciphers for a single host and a single participant using the minimum required request payload.
**NOTE** : This example uses the desktop version of Postman, but the web version works just as well.
To retrieve the encrypted ciphers using Postman:
  1. Open Postman and select **New**.
![Image described in surrounding text.](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt73a64c78866daa17/63c03de398b11c3ccecf6e19/03-postman-new.png)
  2. Choose **Environment**.
![Image described in surrounding text.](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blte1f7779d5e14df7d/63c03de33daf00107c0b94e5/04-postman-new-environment.png)
  3. Name your new environment, in this case _InstantConnect_ and define the two following variables with the corresponding values:
     * **Name** : `mtg-broker-url`; **Value** : `https://mtg-broker-a.wbx2.com`
     * **Name** : `bot-token`; **Value** : your personal access token or bot token
Click **Save**.
![Image described in surrounding text.](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt793604859f72b3ed/63c03de3d2737e13210ed51b/05-postman-environment-setup.png)
  4. Choose your new environment from the drop down list.
![Image described in surrounding text.](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt5f73960f8ff190f4/63c03de3a0db4d3e821f024e/06-postman-choose-environment.png)
  5. Choose **New**.
![Image described in surrounding text.](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blte2e8cc2c3e78ea84/63c03de3bf8ad51208627dc1/07-postman-new-request.png)
  6. Choose **HTTP Request**.
![Image described in surrounding text.](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt73f44f7b080f4b31/63c03de33ae0f31fad3f52d7/08-postman-HTTP-request.png)
  7. Configure the request as follows:
     * Choose **POST** as the request type.
     * Enter `{{mtg-broker-url}}/api/v2/joseencrypt` as the URL.
     * Select **Auth** , choose **Bearer Token** as the **Type** , and enter `{{bot-token}}` as the value for the token.
![Image described in surrounding text.](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltecfa05ea6f7c8018/63c03de35d2483134881cb7c/09-postman-HTTP-request-config-1.png)
  8. Select **Body** , select the type as **raw JSON** and enter the following JSON string (you can change the `sub` (subject) string to whatever you'd like):

```
{
  "jwt": {
  "sub": "Subject goes here."
  },
  "aud": "a4d886b0-979f-4e2c-a958-3e8c14605e51"
}

```

![Image described in surrounding text.](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltfa3b884ff82961e0/63c03de399e03c1edceda614/10-postman-HTTP-request-config-2.png)
  9. Select **Send**. You'll see the response in the **Body** tab of the Postman console.
![Image described in surrounding text.](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt0427f97ba16254c9/63c03deff4a590109efb8aef/11-postman-HTTP-response.png)


Your response will look something like:

```
{
    "host": [
        {
            "cipher": "eyJwMnMiOiJiLVZB...-xtzA"
        }
    ],
    "guest": [
        {
            "cipher": "eyJwMnMiOiJuNmxv...FaqA"
        }
    ]
}

```

You'll notice you've got two `cipher` values, one for the host and one for a single guest. Those are the values that you'll append to the meeting URL after `&data=`.
The `cipher` values are truncated to save space.
For the host URL after appending the cipher, you'll get:
`https://instant.webex.com/gen/v1/login?int=jose&v=1&data=eyJwMnMiOiJiLVZB...-xtzA`
For the guest URL after appending the cipher, you'll get:
`https://instant.webex.com/gen/v1/talk?int=jose&v=1&data=eyJwMnMiOiJuNmxv...FaqA`
The remaining sections describe additional configurations and contain complete reference materials.
####  anchorInstant Connect URL REST API Reference
anchor
This section contains the full reference for all of the Instant Connect URL REST API including example requests and responses.
###### Request Endpoint
The REST API endpoint is:
  * `POST https://mtg-broker-a.wbx2.com/api/v2/joseencrypt`


###### Request Headers
Use the following headers in your request:
  * **Content-Type** : `application/json`
  * **Authorization** : `Bearer <Personal or Bot access token goes here>`


###### Body Parameters
Use the following body parameters to customize your REST request:  
| Parameter  | Description  |  
| --- | --- |  
|  `aud` (**required**)  | String  
Value: `a4d886b0-979f-4e2c-a958-3e8c14605e51`  
Indicates the audience for which the JWT is intended.  |  
|  `jwt` (**required**)  | Object  |  
|  `sub` (**required**) (under `jwt`)  | String  
A unique value in your organization which will be used to place hosts and guests into the same collaboration space.  |  
|  `nbf` (under `jwt`)  | Integer  
The `nbf` (not before) claim identifies the time given as the number of seconds from the Unix Epoch (`1970-01-01T00:00:00Z UTC`) before which the JWT will not be accepted for processing.  |  
|  `exp` (under `jwt`)  | Integer  
The `exp` (expiration time) claim identifies the expiration time given as the number of seconds from the Unix Epoch (`1970-01-01T00:00:00Z UTC`) on or after which the JWT will not be accepted for processing. If not specified, set for 15 minutes later than the time when the request was made.  |  
| `flow`  | Object  |  
|  `id` (under `flow`)  | String  
Takes only one value currently - `sip-no-knock`. If `id` is defined along with data mentioned below, the SIP addresses mentioned in the data object will be called to join the Instant Connect Meeting.  |  
|  `data` (under `flow`)  | Object  
List of Cisco Device SIP addresses that should be added to this meeting automatically.  |  
| `numHost`  | Integer [0 … 25]  
Default: `1`  
Number of encrypted strings to be used by hosts.   
**NOTE** : The maximum number of links, combining both host and guest, that can be requested at one time is 25.  |  
| `numGuest`  | Integer [0 … 25]  
Default: `1`  
Number of encrypted strings to be used by guests.   
**NOTE** : The maximum number of links, combining both host and guest, that can be requested at one time is 25.  |  
| `provideShortUrls`  | Boolean  
Default: `false`  
If set to `true`, the response will have shortened data portions of the meeting URL. It will also contain a shortened base URL  |  
| `verticalType`  | String  
Default: `hc`  
Relevant only if `provideShortUrls` is `true`. Currently takes two values, `gen` (for general flow) and `hc` (for healthcare flow).  |  
| `loginUrlForHost`  | Boolean  
Default: `true`  
Relevant only if `provideShortUrls` is true. If set to `false`, the short URL for hosts will be non-login links which means the host won't have an option to login for the meeting.  |  
| `jweAlg`  | String  
Default: `PBES2-HS512+A256KW`  
Enum: `PBES2-HS256+A128KW PBES2-HS384+A192KW PBES2-HS512+A256KW`   
Algorithm to encrypt the Content Encryption Key, which produces the JWE Encrypted Key.  |  
| `saltLength`  | Integer [8 … 128]  
Default: Random value between `8` and `128` inclusive.  
Length of the salt to be used in conjunction with `jweAlg`.  |  
| `iterations`  | Integer [1000 … 32767]  
Default: A random value between `1000` and `32767` inclusive.  
Number of iterations to be used in conjunction with the `jweAlg`.  |  
| `enc`  | String  
Default: `A256GCM`  
Options: `A128CBC-HS256 A192CBC-HS384 A256CBC-HS512 A128GCM A192GCM A256GCM`  
Algorithm used to encrypt the JWT.  |  
| `jwsAlg`  | String  
Default: `HS512`  
Options: `HS256 HS384 HS512`  
Algorithm used to sign the JWT.  |  
###### Response
A successful request returns:
  * A response message of type `200 OK`
  * A response payload of type`application/json`


###### Request and Response Payload Examples
The following examples show various request payloads as a formatting reference as well as their resultant responses.
The `cipher` values are truncated to save space.
###### Minimum Request Body Payload

```
{
  "jwt": {
    "sub": "Subject goes here."
  },
  "aud": "a4d886b0-979f-4e2c-a958-3e8c14605e51"
}

```

###### Response from the Minimal Request Body

```
{
    "host": [
        {
            "cipher": "eyJwMnMiOiJiLVZB...-xtzA"
        }
    ],
    "guest": [
        {
            "cipher": "eyJwMnMiOiJuNmxv...FaqA"
        }
    ]
}

```

###### Complete Sample JSON Request Payload Without Device Support
To create multiple host and guest URLs in the same response, increase the value of `numHost` and `numGuest` up to a maximum of 25.

```
{
  "jwt": {
    "sub": "Subject goes here.",
    "Nbf": 1671480433000,
    "Exp": 1671480433000
  },
  "aud": "a4d886b0-979f-4e2c-a958-3e8c14605e51",
  "numGuest": 1,
  "numHost": 1,
  "provideShortUrls": false,
  "verticalType": "gen",
  "loginUrlForHost": false,
  "jweAlg": "PBES2-HS512+A256KW",
  "saltLength": 8,
  "iterations": 1000,
  "enc": "A256GCM",
  "jwsAlg": "HS512"
}

```

###### Complete Sample JSON Response Payload Without Device Support
In this case the response will appear similar to the minimal request payload response above. The cipher provided, however will reflect the additional configuration options. In addition, increasing the values for `numHost` and `numGuest` will return multiple cipher instances that you can use to create multiple Instant Connect URLs.
###### Sample Request Payload Generating Short URLs
Adding the parameter `provideShortUrls` generates short URLs in addition to the regular cipher.
**TIP** : When you use the `provideShortUrls` parameter, you can also specify the `loginUrlForHost` parameter which, when set to `false`, disables login for the host.

```
{
  "jwt": {
    "sub": "Subject goes here."
  },
  "aud": "a4d886b0-979f-4e2c-a958-3e8c14605e51",
  "provideShortUrls": true
}

```

###### Short URL Response Payload
The `short` values are combined with the `baseUrl` value in the response payload to generate "short" URLs as described below. The `cipher` values can be used as described below as well.

```
{
    "host": [
        {
            "cipher": "eyJwMnMiOiJQUnJX ... EbZaQ",
            "short": "Kuyqdx3"
        }
    ],
    "guest": [
        {
            "cipher": "eyJwMnMiOiJPamRX ... xVfyA",
            "short": "LCFCNRz"
        }
    ],
    "baseUrl": "https://instant.webex.com/visit/"
}

```

###### Complete Sample JSON Request Payload Including Device Support
To enable device support, add the `flow` element to the `jwt` element in your regular request body.

```
{
  "jwt": {
    "sub": "Subject goes here.",
    "Nbf": 1671480433000,
    "Exp": 1671480433000,
    "flow": {
      "id": "sip-no-knock",
      "data": [
        {
          "uri": "instant_rounding@intadmin.room.wbx2.com"
        }
      ]
    }
  },
  "aud": "a4d886b0-979f-4e2c-a958-3e8c14605e51",
  "numGuest": 1,
  "numHost": 1,
  "provideShortUrls": true,
  "verticalType": "gen",
  "loginUrlForHost": false,
  "jweAlg": "PBES2-HS512+A256KW",
  "saltLength": 8,
  "iterations": 1000,
  "enc": "A256GCM",
  "jwsAlg": "HS512"
}

```

###### Complete Sample JSON Response Payload Including Device Support
As with the other complete payload, the response will appear similar to the minimal request payload response above. The cipher provided, however will reflect the additional configuration options.
####  anchorBuild Instant Connect URLs
anchor
Depending upon whether you've generated regular or "short" URLs you can build final Instant Connect URLs in one of two ways.
###### Build Long URLs
The following URLs are used as bases for the complete host and guest URLs. The API generates a cipher which you then append to the `&data=` portion of the base URL:
  * **Host** : `https://instant.webex.com/gen/v1/login?int=jose&v=1&data=`
  * **Guest** : `https://instant.webex.com/gen/v1/talk?int=jose&v=1&data=`


Append your API response `cipher` values as the `&data=` parameter value to form your Webex Instant Connect meeting for host and guest long URLs.
###### Long URL Examples
  * **Host URL** :`https://instant.webex.com/gen/v1/login?int=jose&v=1&data=eyJwMnMiOiJfRFN ... ufUvar_w`
  * **Guest URL** :`https://instant.webex.com/gen/v1/talk?int=jose&v=1&data=eyJwMnMiOiJYZVp ... dL_GqSw`


###### Build Short URLs
To construct a final short URL, append the `short` key values to the `baseUrl` generated in the response.
###### Short URL Examples
  * **Host URL** : `https://instant.webex.com/visit/m8iHTzH`
  * **Guest URL** : `https://instant.webex.com/visit/oJCP7UY`


##### In This Article
  * [Prerequisites](https://developer.webex.com/create/docs/instant-connect-meeting-links#prerequisites)
  * [Step by Step Instant Connect API Call Using Postman](https://developer.webex.com/create/docs/instant-connect-meeting-links#step-by-step-instant-connect-api-call-using-postman)
  * [Instant Connect URL REST API Reference](https://developer.webex.com/create/docs/instant-connect-meeting-links#instant-connect-url-rest-api-reference)
  * [Build Instant Connect URLs](https://developer.webex.com/create/docs/instant-connect-meeting-links#build-instant-connect-urls)


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
