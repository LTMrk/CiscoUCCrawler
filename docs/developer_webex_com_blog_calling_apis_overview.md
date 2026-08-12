[](https://developer.webex.com/)
[Getting Started](https://developer.webex.com/create/docs)Documentation![](https://developer.webex.com/blog/calling-apis-overview)[AI in Webex](https://developer.webex.com/mcp/docs/webex-mcp-server-overview)Blog![](https://developer.webex.com/blog/calling-apis-overview)[Support](https://developer.webex.com/explore/support)Resources![](https://developer.webex.com/blog/calling-apis-overview)
[Log in](https://developer.webex.com/login)[Sign up](https://developer.webex.com/signup)
# Calling APIs Overview
October 31, 2022
![Phil Bellanti](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltcaa16bd81f3da66a/6153919e8440e97ef5829e0b/Phil_at_Cisco_Live.png?width=100&height=100&fit=crop)
Phil BellantiSenior Webex Developer Evangelist
![Calling APIs Overview](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt1c45f95913765c4d/63595ae9ee9f81106afcdf83/webex-calling.jpg?width=900&height=317&fit=crop)
[Webex Calling](https://www.webex.com/cloud-calling.html) is a cloud-based phone system that contains a comprehensive set of business calling and PBX functionality right out of the box. With customizable plan options and a high level of security, Webex Cloud Calling decreases the cost and difficulty of administering an on-premises phone system. The [Webex Calling platform](https://developer.webex.com/docs/webex-calling) also provide developers an assortment of APIs to automate and extend functionality for administrator provisioning, end-user call controls, generating reports and more.
To get a better lay of the land, let’s take a high-level look at what APIs are available for each area of Webex Calling and how they can be leveraged to power some great integration applications.
### Calling APIs for Administrator Integrations
The first group of Calling APIs we’ll focus on are exclusively for [Webex Administrators](https://developer.webex.com/docs/admin), to extend Control Hub functionality for user provisioning and call reports. When testing these endpoints, pay close attention that the correct admin-level scopes are configured, as noted in the linked API documentation below. 
#### Provisioning APIs
The Webex Calling APIs can automate all the bulk provisioning tasks needed to deliver solutions reliably and efficiently. These provisioning tools can be leveraged to create Webex Calling integrations that automates the creation and management of users and locations, as well as the configuration of custom organizational settings. Let’s take a closer look at the provisioning-specific APIs for Webex Calling administrators.
  * [People API](https://developer.webex.com/docs/api/v1/people): In this context, ‘people’ refers to registered users of Webex. These endpoints allow the creation and management of users in a Webex organization. To do this within the context of Webex Calling, administrators need to specify the `callingData` parameter as `true` in their API calls.
  * [Locations API](https://developer.webex.com/docs/api/v1/locations): These _read-only_ endpoints are used to organize Webex Calling features within physical locations, configured within Control Hub. The responses essentially provide name and mailing address data for the location. 
  * [Organization Settings API](https://developer.webex.com/docs/api/v1/ucm-profile): This powerful set of endpoints support reading and writing of Webex Calling settings for a specific organization, including call routing & forwarding, hunt groups, dial plans, route lists & groups, phone numbers, paging groups, auto attendants, and more.
  * [Calling Person Settings API](https://developer.webex.com/docs/api/v1/user-call-settings): Settings for individual users are configured and managed within this grouping of APIs, similar to the organization-specific ones mentioned above. These settings include calling behaviors, privacy, permissions, barge-ins, intercepts, recordings, caller ID, DND, schedules, call waiting, and more.
  * [Workplace Settings with Numbers API](https://developer.webex.com/docs/api/v1/workspace-call-settings-with-numbers): Workspaces in Webex represent physical rooms inside organizational locations, like conference rooms, meeting spaces, lobbies, and lunchrooms. This is a read-only endpoint for Webex Calling, to retrieve a list of phone numbers assigned to a particular workspace.


For more efficiency, developers can also utilize the [Provisioning SDK](https://github.com/jeokrohn/wxc_sdk) to further streamline these API methods. Check out the helpful [SDK documentation](https://wxc-sdk.readthedocs.io/en/latest/) to learn more.
#### Webex Calling Report APIs
Reports help you track and analyze the performance of Webex services in your organization. You can use these reports to see details for each meeting, how often users are messaging each other, details for Webex Calling calls and call queues, how often Webex devices are used, onboarding information, and more. These reports are generated through templates that are managed [in Control Hub](https://callinghelp.webex.com/calling-admin-portal-reports/). The [Webex Calling report templates](https://help.webex.com/en-us/article/nmug598/Reports-for-Your-Cloud-Collaboration-Portfolio#Cisco_Concept.dita_6136cd51-f6a4-427f-9da9-0cfb89be6330) can generate reports for call quality, engagement, and historical details. These templates can also be used to produce and download reports via the Webex API. A great example integration that utilizes these APIs can be found on the Webex App Hub– [Microcall CDR Reporting](https://apphub.webex.com/applications/microcall-cdr-reporting-micro-tel-inc). They use the information in the call detail records (CDRs) to populate information in management dashboards.
It’s also worth noting that this group of APIs are in the process of being updated and expanded, with many new enhancements on the way, so stay tuned for future announcements. However, developers can still leverage the following APIs today to generate reports automatically and synchronize with their workflows.
  * [Report Templates API](https://developer.webex.com/docs/api/v1/report-templates/list-report-templates): This is a single, _read-only_ API to list all the available report templates (Calling included) that can be generated. 
  * [Reports API](https://developer.webex.com/docs/api/v1/reports): This set of APIs allows the creation and management of reports that are generated through the report templates that are configured in an organization.


Do note, developers can obtain a licensed Webex organization to test the Provisioning and Calling Reports APIs (as an administrator), by requesting a [Webex Developer Sandbox](https://developer.webex.com/blog/developer-sandbox-now-available). The sandbox provides administrator access to a test Webex organization that is managed through Control Hub. Once the sandbox is all setup, this [help desk article](https://help.webex.com/en-us/article/njvdjf2/Configure-Webex-Calling-for-your-organization) provides insight into how Webex Calling is configured in an organization.
### Calling APIs for End User Actions
Outside of administration, there are also Webex Calling APIs for end-user actions, like real-time telephony controls and voice messaging. Keep in mind, integrations that use these APIs will require a different set of user scopes that are separate from the administrator level. These APIs also have a great [Postman collection](https://github.com/webex/postman-webex-calling) to give developers a head start.
#### Call Control APIs
[Call Controls](https://developer.webex.com/docs/api/v1/call-controls) can be used to perform calling actions and provide information about active calls in 3rd party applications. These can be used to integrate a custom call interface or automate other in-call workflows. There are a broad list of intuitive calling control APIs available, such as [dial](https://developer.webex.com/docs/api/v1/call-controls/dial), [answer](https://developer.webex.com/docs/api/v1/call-controls/answer), [hangup](https://developer.webex.com/docs/api/v1/call-controls/hangup), [transfer](https://developer.webex.com/docs/api/v1/call-controls/transfer), and [start](https://developer.webex.com/docs/api/v1/call-controls/start-recording)/[stop recording](https://developer.webex.com/docs/api/v1/call-controls/stop-recording) for initiating and managing active calls. Additionally, read-only endpoints for listing past [calls](https://developer.webex.com/docs/api/v1/call-controls/list-calls), [details](https://developer.webex.com/docs/api/v1/call-controls/get-call-details), and [history](https://developer.webex.com/docs/api/v1/call-controls/list-call-history) are provided. These conceivably can be used to populate data in 3rd party widgets, dashboards, CRMs and more.
A good example integration that leverages these end-user Calling APIs is the aptly named– [Call Control](https://apphub.webex.com/applications/call-control-call-control-llc), which is listed on the Webex App Hub. This integration utilizes these Control APIs to block unwanted calls and spammers, helping teams stay more productive. 
#### Voice Messaging APIs
Webex Calling includes Voice Messaging services, which can be controlled and managed via user-level [REST APIs](https://developer.webex.com/docs/api/v1/user-call-settings). These actions include [list messages](https://developer.webex.com/docs/api/v1/user-call-settings/list-messages), [delete message](https://developer.webex.com/docs/api/v1/user-call-settings/delete-message), [mark as read](https://developer.webex.com/docs/api/v1/user-call-settings/mark-as-read)/[unread](https://developer.webex.com/docs/api/v1/user-call-settings/mark-as-unread), and [get messages summary](https://developer.webex.com/docs/api/v1/user-call-settings/get-message-summary), making it possible for developers to create a custom voicemail interface in a very streamlined way.
### Calling Events (Webhooks)
The Webex Calling platform also provides user level webhooks to notify integrations of changes in call status, such as answered, disconnected, forwarded, resumed, recording stop/start, and more. The JSON payload for call event webhooks contain a variety of retrievable data that can be acted on. For reference, a webhook for a disconnected call would return something like this example JSON payload:

```
 {
    "id": "Y21zY29zcGFyazovL3VzL1",
    "name": "Ni0xMWVILTKYTYEM5YTUZ...",
    "targetUrl": "https://example.com/calls/",
    "resource": "telephony_calls",
    "event": "deleted",
    "orgId": "OWM5LTRINWQtYjZiOCO5NDZ3MGI...",
    "createdBy": "YzOC1jODQwLTMmU...",
    "appId": "Y21zY29zcGFyazovLY...",
    "ownedBy": "creator",
    "status": "active",
    "created": "2022-09-14T18:03:25.829Z",
    "actorId": "Y21zY29zcGFyazovL3VzL1...",
    "data ": {
        "eventType": "disconnected",
        "actorPersonId": "RS84MWNhZjUzOC1j...",
        "orgId": "OWM5LTRINWQtYjZiOCO5NDZ3MGI...",
        "eventTimestamp": "2022-10-15T18:06:20.7817",
        "callId": "Y21zY29zcGFyazovL3Vz...",
        "call SessionId": "OGQ3YzhkNzgtZjIxZib...",
        "personality": "terminator",
        "state": "disconnected",
        "remoteParty": {
            "name": "agent x",
            "number": "1012",
            "personId": "Y21zY29zcGFyazovL3V...",
            "privacyEnabled": false,
            "callType": "location"
        },
        "created": "2022-09-15T18:06:10.2692",
        "answered": "2022-09-15T18:06:17.2117",
        "disconnected": "2022-9-15T18:06:20.781Z"
    }
}
 

```

### Note about Webex for Cisco Broadworks APIs
Another set of APIs found under the Calling banner is [Webex for BroadWorks](https://developer.webex.com/docs/api/guides/webex-for-broadworks-developers-guide). In a nutshell, [BroadWorks](https://www.cisco.com/c/en/us/products/unified-communications/webex-broadworks/index.html) is a call control system and VoIP application server hosted by Service Providers (SP). An SP can wrap Broadworks up with other telephony services (PSTN, ordering, billing, support, etc.) to offer to a complete solution to their end customers. BroadWorks is also the core call control system for [Cisco BroadCloud](https://www.cisco.com/c/en/us/solutions/collaboration/broadcloud-calling/index.html) and is similar to [Cisco HCS](https://www.cisco.com/c/en/us/solutions/collaboration/hosted-collaboration-solution/index.html), in the sense that it's a partner hosted platform.
The Broadworks platform has APIs that are distinct from the Webex Calling APIs. Any endpoints that are noted as BroadWorks, such as [BW Billing Reports](https://developer.webex.com/docs/api/v1/broadworks-billing-reports), [BW Workspaces](https://developer.webex.com/docs/api/v1/broadworks-workspaces), [BW Enterprises](https://developer.webex.com/docs/api/v1/broadworks-enterprises), and [BW Subscribers](https://developer.webex.com/docs/api/v1/broadworks-subscribers), are exclusively for those Service Providers that partner with the BW service.
### Need Any Help?
Don’t forget that the [Webex Developer Support Team](https://developer.webex.com/support) is standing by to assist. On top of that, anyone can ask a question, start a conversation, or join an existing discussion on the Webex for [Developers Community Forum](https://community.cisco.com/t5/webex-for-developers/bd-p/disc-webex-developers). We can also be reached on Twitter via [@WebexDevs](https://twitter.com/WebexDevs) for questions or feedback.
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
