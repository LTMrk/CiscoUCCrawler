[](https://developer.webex.com/)
[Getting Started](https://developer.webex.com/create/docs)Documentation![](https://developer.webex.com/blog/building-the-vivoh-ontime-for-webex-app)[AI in Webex](https://developer.webex.com/mcp/docs/webex-mcp-server-overview)Blog![](https://developer.webex.com/blog/building-the-vivoh-ontime-for-webex-app)[Support](https://developer.webex.com/explore/support)Resources![](https://developer.webex.com/blog/building-the-vivoh-ontime-for-webex-app)
[Log in](https://developer.webex.com/login)[Sign up](https://developer.webex.com/signup)
# Building the Vivoh OnTime for Webex App
July 26, 2022
![Chris Dawson](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltfc92ad777c2697d9/62d15a2a5648fd328b89e6b8/ChrisDawson.jpeg?width=100&height=100&fit=crop)
Chris DawsonChief Technical Officer, Vivoh
![Building the Vivoh OnTime for Webex App](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blta55a62585f869593/62d15a72a60bcb3773fc441e/vivohbanner.jpg?width=900&height=317&fit=crop)
Vivoh offers an [ultra secure DVR for online meetings](https://apphub.webex.com/applications/vivoh-ontime-vivoh-inc) hosted by financial institutions. As our customers have the highest bar for security requirements, so do we, and this post shares why we used Webex to build our OnTime application with those security considerations in mind. OnTime utilizes Webex OAuth and Webex RTMPS streams to provide an ultra-secure video delivery system perfect for financial institutions.
### No Code is the Most Secure Code
The best security solution is the simplest solution. A hidden corollary to this fact is that the less code your system requires to provide your security features, the safer your system is, and the lower your total cost of maintenance and ownership is. To validate the set of video resources a user has access to, OnTime needs to definitively identify a user. The Webex OAuth flow allows us to delegate the identification of the user to Webex. This means OnTime has no database of users to maintain and protect from attackers. OnTime has no code that facilitates resetting passwords. In whole, we have almost zero custom code preventing attackers: we rely on standard authentication libraries and standards like JWT to secure our users. These technologies have long and proven track records for securing credentials and claims useful between client and server applications. Removing as much custom code to manage these credentials makes our attack surface much smaller and makes auditing our code much easier.
### Five Minutes to a Secure Identity Management via Webex OAuth
Integrating with the Webex OAuth backend was simple. You create a Webex OAuth application. This requires configuration of redirect URIs and scopes. You are then provided with a set of credentials that are used by your application to verify an identity token provided by Webex after the identity flow has finished. This blog post documents the steps to create this OAuth application with Webex.
### Step 1: Creating the Webex OAuth Application
To create an OAuth application, you need to login to the developer console of Webex. Then, select create a new app.
![Image described in surrounding text.](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt358ef2531f8627c2/62d15b10b8a7f1380fcd4448/building-the-vivoh-ontime-for-webex-app--1.png)
Choose “integration” (with the subtitle request OAuth to invoke Webex APIs on behalf of another user). You will then be presented with a screen where you enter information about your application, including name, icon, description, and other pieces of information.
### Step 2: Configure Redirect URIs
To use an OAuth flow, you will need to have a place where your users will go after authenticating. This is termed the redirect URIs: you can have one, but often want to create multiple URIs so you can test against a staging or development environment. The standard flow for OAuth is that the provider will authenticate the user, and then send the user to your Redirect URI with a token. That Redirect URI endpoint should handle that token and verify it against Webex to prove its validity and do whatever is necessary to take next steps for your application. In the case of OnTime, Vivoh takes this token, validates it with Webex to see that this is indeed a token identifying the user, and then generates two JWTs tokens: one, with that user identity and the other with information specific to OnTime. OnTime uses that JWT token for each request to validate that the user is who they say they are and that they have access to the resources they are requesting. Once we have secured the identity that Webex provides to us, we do not have to involve Webex any further until the JWT token expires.
### Step 3: Configure OAuth Scopes
OAuth applications provide a token that permits access to Webex. In our case, we only need to use that to retrieve the identity of the user one time when generating the JWT token. Depending on the needs of the application, you can provide a variety of scopes for that token, which permit access to specific parts of the Webex API. For example, if your OAuth application wants access to the meetings information in a read-only way, then you would select the `meeting:schedules_read` scope.
![Image described in surrounding text.](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt8fb933051ed0b130/62d15b10da4a7837db52961b/building-the-vivoh-ontime-for-webex-app--2.png)
### Step 4: Understanding Client ID and Client Secret
Once you have entered in the Redirect URI and scopes, you can create your OAuth application. An OAuth application will provide you with a client ID and secret. These are secrets that are managed generally behind your Redirect URI: when the redirect URI endpoint receives a redirect after authentication+identification, that redirect URL will include a token. The client ID and secret are used to exchange the token against Webex. Webex will return an access token which can be used to access information in the Webex API on behalf of the user that authenticated in the prior step. OnTime uses the Webex API to retrieve the user email address, however we never store this information. We then generate a JWT token for that user and send that back to the user where it is stored in their browser and passed back and forth between requests of the OnTime application to validate video packets.
### Step 5: The User Journey Through Webex OAuth
Once you have created your Webex OAuth application, you can start having users authenticate against it. Typically, you are only permitted to authenticate with users who are in your organization; this prevents unapproved users from accessing your application before you are ready for them.
![Image described in surrounding text.](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt912141f26b63bf2b/62d15b1030ed0e3641c63b0e/building-the-vivoh-ontime-for-webex-app--3.png)
To authenticate, your users will generally start on your application, and then be redirected to a Webex URL that starts the authentication flow and includes a reference to one of the Redirect URIs (which you configured in Step 2). Webex will send the user to a URI which will verify their login status; if the user is already authenticated, the user will proceed to the next step without being asked for credentials. If the user is not authenticated, then the user will be asked to login. In some cases, Webex might determine that this user will need to be re-authenticated based on a decision made by Webex given the IP from which they are accessing it, the browser user agent, or a whole host of other information that can be used to determine whether this particular login requires additional security measures to assure the user is who they say they are. All of this is handled by Webex, and importantly for Vivoh OnTime, is an opaque process that protects the integrity of the user profile when it reaches us but does not require any alteration to our code. For example, if the original login happened inside a trusted corporate network, and then the same user attempted to authenticate when at a public internet access point in a cafe, Webex could decide that the second login requires more scrutiny. Keeping this complexity outside of the Vivoh OnTime application means our codebase is smaller and more secure, while still benefiting from the plethora of security features Webex OAuth provides us.
Once Webex has authenticated the user, the user will be presented with a screen asking them to accept the OAuth application and display the permissions (referred to as “scopes” in OAuth) that this application will require to operate. For Vivoh OnTime, we ask for user information (specifically just email address) so our application requests the `spark:read_user` scope (again, we never store this information). If your application requires different information about the user that authenticates, you can adjust the scopes. If the user accepts the permissions the application requests, then they proceed to the next step, which will take the user back to your application.
### Step 6: User Journey Post-Webex
Once Webex has authenticated the user, the user is then redirected back to your application, specifically to the redirect URI you provided when you initiated the Webex authentication flow. At that point, Webex provides you with a token. This token needs to be exchanged on the server side of your application for an access token. The token is exchanged by hitting an API at Webex, an API that can only be accessed with a client ID and secret (which were obtained after creating the OAuth application in Step 4). If the client ID and secret are valid, and the token from Webex is valid, then Webex will provide an access token. This access token can be used to access the Webex API and retrieve data about that user. If your application needs information beyond the user information, then you will need to adjust the scopes for your Webex OAuth.
For Vivoh OnTime, we accept the token from the user after they are returned from Webex OAuth. Vivoh OnTime uses this to retrieve one piece of information: the user email. In our case, the scopes we request of the user only permit us to ask for this information of Webex; if we had asked for a list of meetings the user had access to, Webex would decline that information because the scope we asked of the user during the authentication flow did not indicate we would be asking for that information. Vivoh OnTime then uses that validated user information (in the form of an email address) combined with other situational information determined now of authentication to create several JWT tokens which the user passes back and forth as a HTTP cookie. Those JWT tokens use digital signatures managed inside the Vivoh OnTime server application to provide secure credentialing for our users. When a user sends us back a JWT token, we know that their identity is secure.
### Step 7: Adding Video via Webex RTMPS Streams
Any Webex webinar can be configured to distribute live video via RTMPS to a remote service. When a webinar is augmented with Vivoh OnTime DVR functionality, the webinar presenter simply needs to add a remote RTMPS source to their webinar. Video is then converted and streamed by Vivoh OnTime and provided only to authorized users via the Webex OAuth flow. Each video packet is authenticated and authorized using the JWT tokens which were generated in the authentication flow.
![Image described in surrounding text.](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltac2e84112647cfa3/62d15b115648fd328b89e6c0/building-the-vivoh-ontime-for-webex-app--4.png)
Live streaming must be enabled in your Webex Meetings or Events account according to [these instructions](https://help.webex.com/en-us/article/xk37so/Enable-live-streaming-in-Webex-Meetings-and-Webex-Events). Events version WBS40.2 and later is required.
To live stream, you need to configure Webex to broadcast to a destination. Vivoh OnTime is one such destination and enables DVR functionality inside your webinar (to use Vivoh OnTime a subscription is required; contact sales@vivoh.com.
Your streaming service will provide you with a target stream link (RTMPS URL) and a stream key. These two pieces of information are enough to configure the broadcast endpoint. Often the RTMPS (ingress) URL is different from the (egress) URL you will give your viewers; with Vivoh OnTime we provide you with an ingress URL and a stream ID (which is different from the stream key and adds a security layer so you don’t reveal your stream key to participants).
When you have configured your remote stream, you are ready to start broadcasting. Start your Webex Meeting, then click: "Start Live Streaming" and enter the provided Streaming service name, Target stream link, and Target stream key values. If you are using OnTime, these will be OnTime, `rtmps://CUSTOMER_NAME.vivoh.com:443/live` and then a stream key like `xxx123`.
![Image described in surrounding text.](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt9f7c6928c35fb1b5/62d15b1127582a3696ad5472/building-the-vivoh-ontime-for-webex-app--5.png)
![Image described in surrounding text.](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltaa63a683490f04fd/62d15b106a8fb133b0ffa5a6/building-the-vivoh-ontime-for-webex-app--6.png)
Once Webex is configured, you can click: "Start streaming" to initiate the stream. The live video will be pushed from Webex to the streaming service. OnTime accepts this video and provides a DVR service.
If your streaming service permits viewing of the live video, then you will have a view URL. With OnTime this URL will look something like: `https://webex-ontime.vivoh.com/v/customer-01`. Notice how the ingress stream key in our example `111xxx` is different from the stream ID, which is `customer-01` in this example. If you are using Vivoh OnTime, that video feed is converted into a DVR experience where attendees will then be able to rewind the live Webex meeting, pause it, or play it back at 2X speed. And, at any time, they can click "Jump To Live" and re-join the live Webex meeting in progress.
![Image described in surrounding text.](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltd11e43d570047438/62d15b1124c5e237d46f74ec/building-the-vivoh-ontime-for-webex-app--7.png)
### Conclusion
In this article, we walked through the steps to wire together Webex OAuth and Webex RTMPS live streaming to create a full-featured Webex app integration.
Feel free to connect with us and share your experience at engineering@vivoh.com. For more behind-the-scenes systems, processes, and techniques that power Vivoh OnTime, check out our [blog](https://vivoh.com/blog/).
Blog Categories
  * [Product Announcements](https://developer.webex.com/blog/categories/product-announcements)
  * [How To](https://developer.webex.com/blog/categories/how-tos)
  * [Events](https://developer.webex.com/blog/categories/events)
  * [Developer Stories](https://developer.webex.com/blog/categories/developer-stories)


Share This Article
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
