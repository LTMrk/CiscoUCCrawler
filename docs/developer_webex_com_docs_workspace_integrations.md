[](https://developer.webex.com/)
[Getting Started](https://developer.webex.com/create/docs)Documentation![](https://developer.webex.com/create/docs/workspace-integrations)[AI in Webex](https://developer.webex.com/mcp/docs/webex-mcp-server-overview)Blog![](https://developer.webex.com/create/docs/workspace-integrations)[Support](https://developer.webex.com/explore/support)Resources![](https://developer.webex.com/create/docs/workspace-integrations)
[Log in](https://developer.webex.com/login)[Sign up](https://developer.webex.com/signup)
[Home](https://developer.webex.com/)/Overview
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
    * [Overview](https://developer.webex.com/create/docs/workspace-integrations)
    * [Technical Details](https://developer.webex.com/create/docs/workspace-integration-technical-details)
    * [Control Hub Features](https://developer.webex.com/create/docs/integration-provided-features-in-control-hub)
    * Webex Assistant Skills
  * Bring Your Own Datasource
  * [Suite Sandbox](https://developer.webex.com/create/docs/developer-sandbox-guide)
  * [Contact Center Sandbox](https://developer.webex.com/create/docs/sandbox_cc)
  * [Guest to Guest Sandbox](https://developer.webex.com/create/docs/g2g-sandbox)
  * [Submit Your App](https://developer.webex.com/create/docs/app-hub-submission-process)
  * [Tutorials](https://developer.webex.com/create/docs/tutorials)


## Getting Started
### Overview
Workspace Integrations provide a framework for services to access [Webex developer APIs](https://developer.webex.com/docs/getting-started), with a focus on extending the capabilities of Workspaces and Webex devices. These integrations can be **public** (built by third party vendors that engage with Cisco to provide all customers access to the integration), or they can be **private** (built by and available only to the customers themselves).
![Workspaces](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt8bf2173753bd4050/64526bc54bb7677c0819cf9e/poster.jpeg)
For customer Control Hub full administrator users, the integrations framework provides a way to enable a third party vendor to interact with the Webex APIs, and especially the Webex device [xAPI](https://roomos.cisco.com/docs/Introduction.md#the-xapi), in a transparent and controlled manner. It's easy to activate and deactivate integrations, understand what permissions they have been granted, and be in control of changes to these permissions as the integrations evolve.
This article describes how to develop and deploy these integrations, for both third party vendors and customers that want to build private integrations.
####  anchorExamples
anchor
Here are a couple of examples of what Workspace Integrations can be used for:
  * Office map, showing whether meeting rooms are currently occupied or vacant, based on actual people presence from the video device's sensors and AI.
  * Controlling the lights and shades in the meeting room from custom UI controls on the device's touch interface.
  * Report issues in the meeting room from the touch interface (forward to Service Now or similar service).
  * Un-book a booked meeting room when it is detected that nobody showed up.
  * Collect feedback on quality of video calls by asking users after the call has ended with a rating dialog.
  * Keep track of how much meeting rooms have been used, and when it was last cleaned.


####  anchorRequirements
anchor
The requirements and skills needed for this integration type is:
  * Webex or Webex Edge registered endpoints.
  * The knowledge and infrastructure to host a private/internal or public web service that can talk with the Webex APIs, for example a Node.js web server or a Python web server.


####  anchorWhat's the difference between workspaces and devices?
anchor
In Webex, **workspaces** typically mean a place where people work, such as an office, a meeting room, a huddle area or a reception. Often, one workspace contains one **collaboration device** , but it can also contain zero or multiple devices.
A device must always belong to one, and only workspace. Note that the device id will change if the device is factory reset, whereas the workspace id will be permanent throughout the lifetime of that space.
A **location** is a physical location that can contain many workspaces. Examples of a typical location is a floor in the building, or an entire building, depending on how the admin would like to logically group the organization.
Workspace integrations can optionally be activated for only selected locations. For example, you can enable catering service integration for only the top floor meeting rooms in a building. The integration will then not have xAPI access to the other devices in that organization.
The following diagram illustrates the topology, where a workspace integration has been enabled for a single location, that contains three workspaces, each with one device.
![Topology](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt3e9c38f3c7498467/64526bc5b7de36333cb4ae77/topology.png)
####  anchorComparison with HTTP API Integrations
anchor
Workspace Integrations are _not_ the same as the integrations described in [Integrations](https://developer.webex.com/docs/integrations). They have things in common, specifically using the same underlying [OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc6749) framework, but differ in a few ways:
  1. Workspace integrations are exclusively managed from Control Hub under Workspaces > Integrations.
  2. The workspace integration framework was designed to support service to service interaction. The integration runs with the identity of a machine account created in the customer organization, rather than on behalf of a Webex user.
  3. Workspace integrations support fine-grained access to the Webex devices xAPI and webhook or message queue change notifications for select xAPI statuses.


####  anchorComparison with on-device integrations (macros)
anchor
Unlike [device macros](https://roomos.cisco.com/doc/TechDocs/MacroIntroduction), the integration is external, so the individual devices do not need any provisioning. Support for workspace integrations is built into RoomOS, and as soon as an admin activates the integration in Control Hub, the devices will start sending data that the integration is subscribing too. Similarly, the integration will be able to invoke actions on the video device, such as starting a call or showing a message to the users in the room, without needing to configure access rules for each individual device. Adding a new feature to the integration or fixing a bug simply requires the central integration to be updated, no action is required for each device.
In addition, the granular API control means that each integration can be limited to which APIs and sensor data it can and cannot use. For example, one integration might allow people in a meeting room to order snacks, and thus only require access to user interface extension APIs. Another integration might just require to count the number of people in the room. The admin can then add the third party integrations, safe in the knowledge that they don't have access to more sensitive APIs such as the call history or the meeting calendar.
For a more detailed comparison with other integration types, see the [Integrations Guide on roomos.cisco.com](https://roomos.cisco.com/doc/TechDocs/Integrations).
####  anchorPrivate and public integrations
anchor
A workspace integration can be either private or public. Private means that the integration is only available within your organization. An example can be an integration that allows you to order catering to your meeting rooms. You create the custom user interface on the touch panels, and react to user requests by making requests in your organization's internal ordering system. In this case the integration is usually deployed to Control Hub and activated in the same go, by the same person. The integration is developed by people within the organization to solve internal use cases.
A public integration, on the other hand, is available to all Webex customers. An example can be a third party issue reporting system that is available as a paid service. It can be leveraged as workspace integration by the service provider / vendor, by adding user interfaces to the devices and creating issues in the enterprise system when user's report issues. In this case, the vendor creates the app and requests approval from Cisco. If approved, Cisco will deploy the public integration on Control Hub, where it will be available to all Webex customers. Org admins can now discover the integration and activate it without any coding themselves. When activated for an org, the vendor will receive notification and can redirect the customer to their own web page for creating a user, setting up payment details etc. with the vendor.
![Public integrations](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt50834f81842dbe07/64526bc563c7dd1138106487/public-integrations.png)
####  anchorWeb hooks and long polling
anchor
Workspace integrations support notifications, which means that Webex will tell you when a device status changes (for example when a room goes from being empty to detecting a person it it), or when device events occur (such as a user tapping a custom UI extension button.). These can be delivered to you in two different ways: Web hooks or long polling.
Web hooks means that you need to host a public web service, and tell the URL to Control Hub. Webex will then send the notifications to this URL any time an event occurs.
![Web hooks](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt930fe8f0560442e1/64526bc5d54b2910e833f013/how-it-works.png)
Long polling is the "don't call us, we'll call you" approach, meaning that your integration is constantly asking Webex if any new notifications have occurred. Whenever a device reports a notification, Webex will respond to your query. You will then need to ask again for more notifications.
![Long polling](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt1544946a45a554fc/64526bc5b4fe3e118d4170d9/workspace-long-polling.png)
The advantage with long polling is that the integration can run on your internal network, and therefore have access to other restricted resources in your building, such as smart building gateways. In addition, it does not require you to host a public web service with HTTPS certification, which can be technically more difficult, or hard due to your company's security policies and restrictions.
It's also easy to develop and test the integration using long polling, since you can run your developer integration straight from your laptop. It's possible to develop using long polling, then run the production app with web hooks. But be aware that you cannot do long polling and web hooks on the same integration at the same time. Webex notifications can only be delivered to a single listener.
####  anchorxAPI access rules
anchor
In addition to traditional OAuth scopes, Workspace Integrations support fine grained access control for xAPI. This allows admin to inspect and approve with device APIs the integration has access to. This applies to **commands** , **events** and **statuses**. Note that for statuses, the API list both specifies which xStatus you will be able to query, and which you will receive notifications about when it changes.
It is highly recommended to specify each API directly rather than using wild cards. The fewer APIs your integration uses, the less dangerous it feels for an admin to approve it.
Note that for **xConfigurations** there are currently no such granular control, it's all or nothing based on the `spark-admin:devices_read` and`spark-admin:devices_write` scopes.
Note also that for both scopes and xAPI rules, as a developer you can set whether the requested permission is required or not. If not required, the admin may choose to not accept the optional permissions. This is typically for enhancement features that are nice to have but not strictly necessary. If you have optional permissions, you will need to check at runtime whether or not it has been accepted by the admin before using that API.
####  anchorThe integration manifest
anchor
When you create an integration, you must provide a **manifest** to Control Hub to tell what your integration does, and what API scopes and device APIs it needs access to.
You can create the manifest file yourself or use a visual editor available on [GitHub](https://cisco-ce.github.io/workspace-integrations-editor/).
For details, see the technical overview for Workspace Integrations.
![Control Hub Manifest](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltea3a7c98898ec5ee/64526bc5f1b32a119f435022/control-hub-manifest.png)
####  anchorLimitations
anchor
Workspace Integrations is a powerful and flexible integration type that allows you to do almost anything the devices have to offer. There are a few limitations worth being aware of:
  * For **xEvent** and **xStatus** notifications, there is only a small subset of the statuses and events you can subscribe to, such as room analytics, custom UI events, boot events and a few more. For xStatus you will still be able to query all of the public statuses though. See Control Hub > Workspaces for an up-to-date list.
  * For devices in personal mode, the integration will not be able to invoke commands that are defined as **privacy impacting**. You can check this for each API on the [roomos.cisco.com API details page](https://roomos.cisco.com/xapi/).
  * Even if you limit an integration to a specific location, it will still be able to access configuration for all devices in the organization, if those scopes are set.
  * Since all traffic between the devices and the integration go via the Webex cloud, it will be slower than a direct integration such as macros. For most events, including UI events, it should still be ok, but some actions that require direct feedback, such as manual camera control, may not be optimal for this integration type.


####  anchorQuick Start
anchor
To quickly get started, you can look at the [SDK for Node.js](https://github.com/cisco-ce/workspace-integrations-nodejs). To try it out, you will need:
  * A laptop with **Node.js** and **npm** installed
  * Some basic Node.js / JavaScript knowledge
  * Admin access to Control Hub
  * One or more Cisco devices


There is also the [SDK for Java](https://github.com/cisco-ce/workspace-integrations-java). To test it, you will need:
  * A laptop with **Java** and preferably **IntelliJ IDEA** installed
  * Some basic Java knowledge
  * Admin access to Control Hub
  * One or more Cisco devices


####  anchorUseful links
anchor
  * [Node.js SDK](https://github.com/cisco-ce/workspace-integrations-nodejs) - Takes care of token handling and low-level HTTP calls for you with a simple, object oriented JavaScript API
  * [Java SDK](https://github.com/cisco-ce/workspace-integrations-java) - Takes care of token handling and low-level HTTP calls for you with a simple, object oriented Java API
  * [Online manifest editor](https://cisco-ce.github.io/workspace-integrations-editor/) - Visual editor for creating and editing manifests, with completions for scopes and xAPIs
  * [xAPI reference docs](https://roomos.cisco.com/xapi) - Browse and search the device's xAPI for commands, status, and configs that your integration will use
  * [Webex Device APIs](https://developer.webex.com/docs/api/guides/device-developers-guide) - Webex APIs you need to use to talk to the device xAPI from your integration


##### In This Article
  * [Examples](https://developer.webex.com/create/docs/workspace-integrations#examples)
  * [Requirements](https://developer.webex.com/create/docs/workspace-integrations#requirements)
  * [What's the difference between workspaces and devices?](https://developer.webex.com/create/docs/workspace-integrations#whats-the-difference-between-workspaces-and-devices)
  * [Comparison with HTTP API Integrations](https://developer.webex.com/create/docs/workspace-integrations#comparison-with-http-api-integrations)
  * [Comparison with on-device integrations (macros)](https://developer.webex.com/create/docs/workspace-integrations#comparison-with-ondevice-integrations-macros)
  * [Private and public integrations](https://developer.webex.com/create/docs/workspace-integrations#private-and-public-integrations)
  * [Web hooks and long polling](https://developer.webex.com/create/docs/workspace-integrations#web-hooks-and-long-polling)
  * [xAPI access rules](https://developer.webex.com/create/docs/workspace-integrations#xapi-access-rules)
  * [The integration manifest](https://developer.webex.com/create/docs/workspace-integrations#the-integration-manifest)
  * [Limitations](https://developer.webex.com/create/docs/workspace-integrations#limitations)
  * [Quick Start](https://developer.webex.com/create/docs/workspace-integrations#quick-start)
  * [Useful links](https://developer.webex.com/create/docs/workspace-integrations#useful-links)


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
