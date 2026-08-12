[](https://developer.webex.com/)
[Getting Started](https://developer.webex.com/create/docs)Documentation![](https://developer.webex.com/docs/run-an-oauth-integration)[AI in Webex](https://developer.webex.com/mcp/docs/webex-mcp-server-overview)Blog![](https://developer.webex.com/docs/run-an-oauth-integration)[Support](https://developer.webex.com/explore/support)Resources![](https://developer.webex.com/docs/run-an-oauth-integration)
[Log in](https://developer.webex.com/login)[Sign up](https://developer.webex.com/signup)
## Run an OAuth Integration
### Run a Webex OAuth Integration Locally
This tutorial shows you how to get a Node.js server running locally that acts as an OAuth client for a Webex [integration](https://developer.webex.com/docs/integrations), obtain an API access token for the authenticating user, and uses it to call a Webex API to get information about the user.
####  anchorOverview
anchor
This tutorial shows you how to get a Node.js server running locally that acts as an OAuth client for a Webex [integration](https://developer.webex.com/docs/integrations) using a [existing application built with Node.js and Express](https://github.com/WebexSamples/webex-oauth-integration). The app presents a button for the user to start the OAuth flow. After the user has authenticated with Webex and accepted the requested [data scopes](https://developer.webex.com/docs/integrations#scopes) they are redirected back to the Node.js app. The app obtains an API access token for the authenticated user from Webex and uses it to call the [Get My Own Details](https://developer.webex.com/docs/api/v1/people/get-my-own-details) endpoint. The user's display name is parsed from the response and displayed on the rendered HTML page. As next steps, suggestions are made for creating a new page that lists the user's spaces.
![Overview](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt79c791c28d707a47/636c28e10b52047adbb942a7/brand_new_flow.png)
The Node.js application uses [Express](https://expressjs.com/) to define HTTP routes and [embedded JavaScript templates](https://ejs.co/) (EJS) to compile and render HTML pages that contain data returned by the Webex API, such as the user's display name. HTTP calls to the Webex API are made using the [node-fetch](https://www.npmjs.com/package/node-fetch) package from NPM.
####  anchorPrerequisites
anchor
To complete this tutorial you will need the following:
  * A Webex account. You can create a [free account](https://cart.webex.com/sign-up) if you don't have one.
  * [Git](https://git-scm.com/downloads) installed locally.
  * [Node.js](https://nodejs.org/en/) installed locally.


####  anchorStep 1: Create the Integration
anchor
First you'll create a Webex [Integration](https://developer.webex.com/docs/integrations), which represents an OAuth client. An OAuth client ID and secret is generated that you'll use to configure the Node.js app. You also specify the redirect URL where the user is sent after they authenticate with Webex and accept the requested data access scopes. In this case the redirect URL is set to **ht tp://localhost:8080** where the Node.js server will be listening for requests from the Webex OAuth server.
**To create the Webex integration** :
  1. Open the [New Integration](https://developer.webex.com/my-apps/new/integration) page on the Developer Portal (you must be [signed in](https://developer.webex.com/login)).
  2. Enter a name and description and select (or upload) an app icon.
The integration's name and icon are displayed on the OAuth consent page where the authenticated user accepts (or denies) your app's request for the requested data scopes. The description is only used if or when you publish your integration to Webex [AppHub](https://apphub.webex.com).
  3. For **Redirect URL** enter **ht tp://localhost:8080/oauth**.
![Redirect URI](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt77ab3c56e98cf675/636060b47a7bad106b9ae831/redirect_uri.png)
This is where the local Node.js app will be listening for requests.
  4. In the **Scopes** section select the **spark:people_read** scope.
![Scopes](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blte51fc07ff661f8a6/6360619757082b10e8175cb8/add-scopes.png)
  5. Click **Add Integration**.
  6. Copy the your integration's generated **Client ID** and **Client Secret** for use in the next step.
![Client ID and secret](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt2135a5986a9d0ebd/636068df882b96108ae799bc/client_id_secret_copy.png)
  7. Copy the **OAuth Authorization URL** string for use in the next step.
![OAuth authorization URL](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt8e73870d76ee936b/6373e69371c75510a0c9e16d/auth-init-url-2.png)
This string contains URL-encoded values for the integration's requested scopes, client ID, redirect URL and state. The Node.js app will compute a new `state` query parameter value and add it to the URL.
You could instead compose this URL in code, but typically the URL won't change much once your integration. This way you can't accidentally forget about including a selected scope.


####  anchorStep 2: Configure and Run the OAuth Server
anchor
To install the server locally you clone an existing [Webex OAuth sample](https://github.com/WebexSamples/webex-oauth-integration) and install the project's dependencies. You also configure the app's .env file with the OAuth's client secret and authorization URL copied from the integration's settings page.
**To run the server locally:**
  1. Clone the OAuth sample project and install its dependencies.

```
git clone https://github.com/WebexSamples/webex-oauth-integration.git
cd webex-integration-sample
npm install

```

  2. Open the project's **.env** file and paste your integration's client secret and initial authorization URL that you copied from the integration's configuration page.
     * Add your client ID and secret to the corresponding environment variables.

```
# Your OAuth integration's client ID/secret
CLIENT_SECRET=<INTEGRATION CLIENT SECRET>

# Initial authorization URL
AUTH_INIT_URL=<AUTH URL>

```

  3. Save your changes to the server.js and .env files and start the server from a terminal.

```
node server.js

```

The output shows the OAuth client's configuration.

```
Debugger attached.
oauth OAuth integration settings:
oauth    - CLIENT_ID    : C909b987b64167258774e532d595702ef864a35f7614678dbe4046056daf67d63
oauth    - REDIRECT_URI : http://localhost:8080/oauth
oauth    - SCOPES       : spark:people_read +0ms
Webex OAuth Integration started on http://localhost:8080

```



####  anchorStep 3: Test the Integration
anchor
Next you'll test the integration by initiating the OAuth flow from your browser, signing in to your Webex account and accepting the requested data scopes on the consent screen.
**To test the integration** :
  1. Open <http://localhost:8080> and click **Start OAuth Flow**.
![Start flow](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt9bbbd652b670c9fd/637681c6d4802c10f7f4ca6b/homepage.png)
  2. Sign in to your Webex account, if prompted, and click **Accept** on the consent page.
![Consent screen](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt36a4934b91dd73dd/637682ba0c4e351095246a53/scope-01.png)
Your browser is redirected to the integration's redirect URI, where the Node.js app [exchanges the authorization code](https://github.com/WebexSamples/webex-oauth-integration/blob/main/server.js#L170-L189) returned by Webex for an API access token, and [stores the token as a session variable](https://github.com/WebexSamples/webex-oauth-integration/blob/main/server.js#L170-L189). The server then uses the access token to call the [Get My Own Details](https://developer.webex.com/docs/api/v1/people/get-my-own-details) endpoint, which returns details about the authenticated user. The server [parses out the user's display name](https://github.com/WebexSamples/webex-oauth-integration/blob/main/server.js#L258-L263) from the response and returns it in a compiled EJS template.
![Authenticated](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt809fe25c401f5f14/637684b1acdace107758f42a/authenticated-new.png)


####  anchorStep 4: List the User's Spaces
anchor
Next you'll add a new scope to your integration that will allow your app to get a list of Webex spaces (called "rooms" in the API) the user has recently visited, and modify the Node app to let the user view a list of their spaces.
**To list the user's spaces** :
  1. Update your [Webex integration](https://developer.webex.com/my-apps) to include the **spark:rooms_read** data scope. 
  2. Save your changes to the integration and copy the new authorization URI paste it into the project's **.env** file for the `AUTH_INIT_URL` variable, as before. This URL contains the newly added scope.
  3. In the Node project uncomment the following line in [www/display-name.ejs](https://github.com/WebexSamples/webex-oauth-integration/blob/main/www/display-name.ejs#L17). An [Express route](https://github.com/WebexSamples/webex-oauth-integration/blob/main/server.js#L215) for this path is pre-defined in server.js.

```
<a href="/listrooms">List my rooms (spaces)</a>

```

  4. Restart the Node.js application and repeat the login and consent process. Note that the consent screen asks for an additional scope ("List titles of spaces that you are in").
![New scope consent screen](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltcd6374456545a34a/63766fb776567a10a7cb8427/accept-new-scope.png)
  5. On the greeting page click **List my Rooms** to display a list of your recently visited rooms.
![List of rooms](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltf0713a92b8e6db49/63768f1e32130110b2799817/list-rooms.png)


##### In This Article
  * [Overview](https://developer.webex.com/docs/run-an-oauth-integration#overview)
  * [Prerequisites](https://developer.webex.com/docs/run-an-oauth-integration#prerequisites)
  * [Step 1: Create the Integration](https://developer.webex.com/docs/run-an-oauth-integration#step-1-create-the-integration)
  * [Step 2: Configure and Run the OAuth Server](https://developer.webex.com/docs/run-an-oauth-integration#step-2-configure-and-run-the-oauth-server)
  * [Step 3: Test the Integration](https://developer.webex.com/docs/run-an-oauth-integration#step-3-test-the-integration)
  * [Step 4: List the User's Spaces](https://developer.webex.com/docs/run-an-oauth-integration#step-4-list-the-users-spaces)


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
