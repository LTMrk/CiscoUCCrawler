[](https://developer.webex.com/)
[Getting Started](https://developer.webex.com/create/docs)Documentation![](https://developer.webex.com/docs/getting-your-personal-access-token)[AI in Webex](https://developer.webex.com/mcp/docs/webex-mcp-server-overview)Blog![](https://developer.webex.com/docs/getting-your-personal-access-token)[Support](https://developer.webex.com/explore/support)Resources![](https://developer.webex.com/docs/getting-your-personal-access-token)
[Log in](https://developer.webex.com/login)[Sign up](https://developer.webex.com/signup)
## Getting and Using your Personal Access Token
### Getting and Using your Personal Access Token
Learn how get your personal access token for testing the Webex API.
Webex REST API requests must include an API access token in a request Authorization header that has the proper data access scopes for the requested resource. In a production app, you create a [Webex Integration](https://developer.webex.com/docs/integrations) and use OAuth to obtain an access token. For testing purposes, however, you can get a personal access token from the Developer Portal you can use to make API calls on your own behalf.
Notes about personal access tokens:
  * They should not be used in production apps. Instead, create an [Integration](https://developer.webex.com/docs/integrations) with the desired access scopes to obtain access tokens.
  * Personal access tokens are valid for 12 hours after logging into the Developer Portal.


####  anchorGet your Personal Access Token
anchor
Sign in to the Developer Portal and click the copy icon next to the **Bearer** field below. Click **OK** to copy the token to your clipboard:
###### Your Personal Access Token
Log in required for access token.
Bearer
This limited-duration personal access token is hidden for your security.
  

You can also obtain your personal access token from the Try It section of any API reference page.
![Try it personal access token](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt940cd395b3fb39a0/62ec0d867e18987096ab9ea8/try-it-personal-access-token.png)
####  anchorUse your Personal Access Token
anchor
You use your personal access token like any API access token, for example:

```
$ curl --request GET \
  --header "Authorization: Bearer <YOUR_PERSON_ACCESS_TOKEN>" \
  https://webexapis.com/v1/rooms/

```

####  anchorNext Steps
anchor
For more details on authentication and using the Webex REST API, see [Access the Webex API](https://developer.webex.com/docs/getting-started).
##### In This Article
  * [Get your Personal Access Token](https://developer.webex.com/docs/getting-your-personal-access-token#get-your-personal-access-token)
  * [Use your Personal Access Token](https://developer.webex.com/docs/getting-your-personal-access-token#use-your-personal-access-token)
  * [Next Steps](https://developer.webex.com/docs/getting-your-personal-access-token#next-steps)


##### Related Resources
  * [Real world walkthrough of building an OAuth Webex integration](https://developer.webex.com/blog/real-world-walkthrough-of-building-an-oauth-webex-integration "Real world walkthrough of building an OAuth Webex integration")
  * [Access the Webex API](https://developer.webex.com/docs/getting-started "Access the Webex API")


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
