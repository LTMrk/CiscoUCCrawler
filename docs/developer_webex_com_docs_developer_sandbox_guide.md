[](https://developer.webex.com/)
[Getting Started](https://developer.webex.com/create/docs)Documentation![](https://developer.webex.com/admin/docs/developer-sandbox-guide)[AI in Webex](https://developer.webex.com/mcp/docs/webex-mcp-server-overview)Blog![](https://developer.webex.com/admin/docs/developer-sandbox-guide)[Support](https://developer.webex.com/explore/support)Resources![](https://developer.webex.com/admin/docs/developer-sandbox-guide)
[Log in](https://developer.webex.com/login)[Sign up](https://developer.webex.com/signup)
[Home](https://developer.webex.com/)/Suite Sandbox
Webex Admin
  * [Overview](https://developer.webex.com/admin/docs/admin)
  * [Authentication](https://developer.webex.com/admin/docs/authentication)
  * Service Apps
  * Guides
  * API REFERENCE
  * All APIs
  * [Changelog](https://developer.webex.com/admin/docs/api/changelog/webex-admin)
  * [AI Assistant for Developers](https://developer.webex.com/admin/docs/webex-aI-assistant-for-developers)
  * [Troubleshoot the API](https://developer.webex.com/admin/docs/api/guides/troubleshooting)
  * [Suite Sandbox](https://developer.webex.com/admin/docs/developer-sandbox-guide)


## Webex Admin
### Suite Sandbox
Access your very own Webex Sandbox for building and testing new bots, integrations, and embedded apps. 
[Request a Sandbox](https://developer.webex.com/admin/docs/developer-sandbox-guide)[Need a Guest to Guest Sandbox?](https://developer.webex.com/docs/g2g-sandbox)
If you're creating a sandbox in the Webex for Government (FedRAMP) portal, please be aware that the sandbox supports commercial APIs rather than FedRAMP-only APIs.
####  anchorIntroduction
anchor
A Developer Sandbox provides you with administrator access to a licensed Webex organization you manage using [Webex Control Hub](https://admin.webex.com) . A licensed org lets you create and test capabilities of the Webex platform not available with [Webex free plans](https://help.webex.com/en-us/article/vyuo1j/Webex-free-plans-|-Supported-countries-and-regions#id_133759) (see [Do I need a Developer Sandbox?](https://developer.webex.com/docs/developer-sandbox-guide#do-i-need-a-developer-sandbox) for details).
####  anchorSandbox Quick Start
anchor
If you are [signed in](https://developer.webex.com/login) to the Developer Portal when you request a sandbox, the credentials for your new account are sent to the email associated with your Webex account; if you are not signed in you will be prompted to provide an email.
**To request a Sandbox Organization** :
  1. Click **Request a Sandbox** at the top of this page.
If you want your sandbox to be configured with the all the features of the new **Webex Suite Meeting Platform** , please contact [support](https://developer.webex.com/support) requesting that configuration. This is particularly important if you want to test and execute the [space meeting migration flows](https://developer.webex.com/docs/space-meetings-migration). The standard sandboxes are configured with the legacy meetings platform. Please also refer to [this document](https://developer.webex.com/docs/app-programming-interface-behavior-changes) for differences.
  2. Click **Accept** in the dialog box that appears. Enter your email address, if prompted, then click **Submit**.
If the Submit button doesn't work try signing out of your Webex account and then trying again, providing your email address when prompted.
  3. Check your email for the account credentials for your admin account. The email will be titled "Collab Toolbox Provisioning Notification".


####  anchorSign in to Your Account
anchor
The provisioning email you receive contains the following information for your sandbox organization:
  * Organization name: (e.g. jdoessandboxtest-1xep)
  * Username/email: (e.g. admin@jdoessandboxtest-1xep.wbx.ai)
  * Password
  * Webex Site URL: (e.g. jdoesandboxtest-1xep.webex.com)


To avoid any potential conflicts with your primary Webex account it's recommended that you use a private or incognito browser window to perform the sign in.
**To sign in to Control Hub for your org** :
  1. Open a new browser window, or open a private/incognito window (Ctrl+Shift+N or Cmd+Shift+N on Chrome for Windows or MacOS, or Ctrl+Shift+P or Cmd+Shift+P on Firefox for Windows or MacOS).
We recommend using the latest desktop version of Google Chrome or Mozilla Firefox. Other browsers may produce unexpected results. Webex Control Hub is not designed for mobile devices.
  2. In the new/private browser window open [Webex Control Hub](https://admin.webex.com). You may need to copy and paste the URL (`https://admin.webex.com`) into your browser if the link doesn't open in the new/private window.
  3. In the sign in form enter the username/email address from the provisioning email.
  4. Enter the password from the provisioning email.
  5. Click **Accept** to agree to the terms of service.


And that's it! You now have your very own Sandbox for testing your Webex apps. See [Next Steps and Learn More](https://developer.webex.com/docs/developer-sandbox-guide#next-steps-and-learn-more) to learn what you can do.
####  anchorNext Steps and Learn More
anchor
This section contains details about how to use your Developer Sandbox.
**Using Webex Control Hub** — [Webex Control Hub](https://admin.webex.com) is how you manage and monitor all aspects of your Webex organization. See [Get Started with Webex Control Hub ](https://help.webex.com/en-US/article/nkhozs6/Get-Started-with-Control-Hub) for an introduction to what you can do with Control Hub.
**Adding Users to your Organization** — You'll likely want to invite users to join your sandbox organization. The easiest way is to [manualy add users](https://help.webex.com/en-us/article/v71ztb/Add-Users-Manually-in-Control-Hub). You can also [assign roles to your users](https://help.webex.com/en-us/article/fs78p5/Assign-organization-account-roles-in-Control-Hub).
Users invited to join your sandbox organization must **not** use an email associated with an existing Webex account. Admins should use alternate email addresses to invite users with existing Webex accounts. 
**Making Admin API calls** — To use the [Admin](https://developer.webex.com/docs/admin) or [Compliance](https://developer.webex.com/docs/compliance) APIs you'll need to generate authentication tokens using your sandbox administrator account, or other admin user you've added to your organization. Similarly, to use the **Try It** feature in the [interactive API reference](https://developer.webex.com/docs/api/v1/meetings/create-a-meeting) as an admin, you will need to [sign in to the Developer Portal](https://developer.webex.com/login) with your sandbox's administrator account credentials.
**Create and Manage Embedded Apps** — Any user in your sandbox organization can [create an embedded app](https://developer.webex.com/my-apps/new/embedded-app) via the Developer Portal. Users must [sign in](https://developer.webex.com/login) using their sandbox org credentials, not with their main Webex account.
To make embedded apps available to other users in your sandbox organization, the app must be [submitted for approval](https://developer.webex.com/docs/embedded-apps-guide#request_approval) by the user who created the app, and [approved](https://help.webex.com/en-us/article/y1eqyd/Embedded-apps-in-Webex#Cisco_Task_in_List_GUI.dita_embeddedapp1) by an organization admin. See the following links for more information.
  * [Creating an Embedded App in the Developer Portal](https://developer.webex.com/docs/embedded-apps-guide#creating-an-embedded-app-in-the-developer-portal)
  * [Submitting an Embedded App for Approval](https://developer.webex.com/docs/embedded-apps-guide#request_approval)
  * See [Managing Embedded Apps](https://help.webex.com/en-us/article/y1eqyd/Embedded-apps-in-Webex) to learn how to approve embedded apps.


Other resources:
  * [Get Started with the Webex App](https://help.webex.com/en-US/article/n3xx7vcb/Get-Started-with-Webex-App)
  * [Webex Help Resources](https://help.webex.com/en-us)


####  anchorDo I need a Developer Sandbox?
anchor
A Developer Sandbox provides you with admin access to a licensed Webex organization. A licensed org is required if you need to test features of the Webex platform not available to [Webex free plans](https://help.webex.com/en-us/article/vyuo1j/Webex-free-plans-|-Supported-countries-and-regions#id_133759). Specifically, access to a licensed organization is required to perform the following development and testing tasks:
  * Create and test [Webex Embedded Apps](https://developer.webex.com/docs/embedded-apps).
  * Create integrations that require [admin](https://developer.webex.com/docs/admin) and [compliance](https://developer.webex.com/docs/compliance) API testing.
  * Test Webex Messaging bots and integrations in locked (moderated) spaces.


If you aren't developing these types of apps or features you don't necessarily need a Developer Sandbox to develop and test your code.
Each Webex Developer Sandbox use is limited to a maximum of 10 account users for validation and test purposes only. Cisco may from time to time audit Webex Developer Sandbox accounts and reserves the right to remove users in excess of 10 account users, or terminate the Webex Developer Sandbox environment for any Developer resource misuse.
####  anchorAsk the Experts
anchor
  * If you're having trouble accessing your new Sandbox, please reach out to Devsupport@webex.com or go to [Developer Support](https://developer.webex.com/support)


####  anchorTerms and Conditions
anchor
Please see [Terms of Service](https://developer.webex.com/terms-of-service) for the Webex developer terms and conditions.
##### In This Article
  * [Introduction](https://developer.webex.com/admin/docs/developer-sandbox-guide#introduction)
  * [Sandbox Quick Start](https://developer.webex.com/admin/docs/developer-sandbox-guide#sandbox-quick-start)
  * [Sign in to Your Account](https://developer.webex.com/admin/docs/developer-sandbox-guide#sign-in-to-your-account)
  * [Next Steps and Learn More](https://developer.webex.com/admin/docs/developer-sandbox-guide#next-steps-and-learn-more)
  * [Do I need a Developer Sandbox?](https://developer.webex.com/admin/docs/developer-sandbox-guide#do-i-need-a-developer-sandbox)
  * [Ask the Experts](https://developer.webex.com/admin/docs/developer-sandbox-guide#ask-the-experts)
  * [Terms and Conditions](https://developer.webex.com/admin/docs/developer-sandbox-guide#terms-and-conditions)


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
