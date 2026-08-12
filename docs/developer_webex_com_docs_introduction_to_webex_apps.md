[](https://developer.webex.com/)
[Getting Started](https://developer.webex.com/create/docs)Documentation![](https://developer.webex.com/docs/introduction-to-webex-apps)[AI in Webex](https://developer.webex.com/mcp/docs/webex-mcp-server-overview)Blog![](https://developer.webex.com/docs/introduction-to-webex-apps)[Support](https://developer.webex.com/explore/support)Resources![](https://developer.webex.com/docs/introduction-to-webex-apps)
[Log in](https://developer.webex.com/login)[Sign up](https://developer.webex.com/signup)
## Introduction to Webex Apps
### Introduction to Webex Apps
This tutorial provides an introduction to Webex's extensibility.
In this introduction to the Webex REST API, you will use the interactive documentation to experience Webex programmability. The tutorial will then go through a few use-cases, and drill into the fundamentals of Webex Apps.
####  anchorPrerequisites
anchor
You will need a free Webex user account to complete this tutorial. If you're not a Webex user yet, [sign up](https://www.webex.com/manage/myaccount/index.html).
####  anchorAbout Webex Extensibility
anchor
 _NOTE_ : Webex _rooms_ were renamed _Spaces_. However, the REST API still uses the `/rooms` resource, and you may see the 'Space' and 'Room' terms used interchangeably.
Extending Webex enables you to create applications that:
  * Automate tasks such as creating spaces, posting messages, or adding participants to an existing space.
  * Perform actions in response to events in Webex such as participants being added to spaces, or new messages being created.


To automate tasks, custom applications use the [Webex REST API](https://developer.webex.com/docs/api/getting-started).
The API enables you to interact with Webex's main concepts:
  * [Rooms](https://developer.webex.com/docs/api/v1/rooms): Create, update or delete spaces.
  * [Teams](https://developer.webex.com/docs/api/v1/teams): Create, update or delete teams.
  * [People](https://developer.webex.com/docs/api/v1/people): Look for Webex users.
  * [Messages](https://developer.webex.com/docs/api/v1/messages): Create or delete Messages.
  * [Memberships](https://developer.webex.com/docs/api/v1/memberships) and [Team Memberships](https://developer.webex.com/docs/api/v1/team-memberships): Add, remove participants from spaces and teams, and promote participants as moderators.


Moreover, your application can register [Webhooks](https://developer.webex.com/docs/api/v1/webhooks) to be notified of various events, such as new messages being posted, or users joining or leaving spaces.
The documentation listed above enables you to interact with the Webex API straight from your Web browser. Because you will use the interactive documentation throughout these tutorials, you will start by exploring it here. Moreover, doing so will help demonstrate these extensibility concepts!*
####  anchorREST API Documentation
anchor
Documentation for the Webex REST API is available at [Cisco Webex for Developers](https://developer.webex.com/docs/getting-started).
  1. Navigate to ['Webex for Developers'](https://developer.webex.com) site in the browser.
  2. Log in using your Webex credentials. If you don’t have a Webex account, get one by clicking **Sign up**.
  3. Once logged in, you can get a temporary developer access token for your account by navigating to the [](https://developer.webex.com/docs/api/getting-started#accounts-and-authentication) of the **Getting Started** page.
Copy your developer access token and place it in a safe place, as you'll be using it in future steps of this tutorial:
![Developer Access Token](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltd3641d697e7622b7/6202e1371e536a4ac08df255/access_token.png)
_IMPORTANT_ : Your developer access token is provided for test purposes only - never use it in production. It expires 12 hours after being generated, or upon logging out of 'Webex for Developers' site. If your personal token is compromised, simply logout and sign in again on the developer portal to invalidate any previous tokens.
  4. In the left navigation pane, go to **Webex API** and expand the**Full API Reference** section.
This action displays Webex API categories such as people, rooms (aka spaces), memberships, messages, teams, and so on.
![api reference](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt96ae234e8cd38b37/62ebf56318595876bf3166b1/api-ref-left-nav.png)


In the next step, you’ll use this documentation to create a new space.
####  anchorInvoking the REST API
anchor
  1. Navigate to **Full API Reference** >**Rooms** resource in the left-hand navigation pane.
  2. In the left nav, click **POST Create a Room**.
  3. Activate the documentation's **Try It** mode.
![Interactive mode](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blte6306656e48af491/6202f44bc7047b4ac12ee476/step3-interactive-mode.png)
  4. Edit the title of the Room and click **Run**.
The right pane displays the request sent to the Webex API and the response received. ![Response](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltd2c7233d84781dc8/6202f6e1c7047b4ac12ee47a/response.png)
Note the request and response, because the request contains your access token, it is sent **on your behalf**.
  5. Let’s examine the response. The `200 / OK` displayed in green is called the _HTTP status code_ in the REST API terminology. It gives you instant feedback about the success or failure of your API call.
The main HTTP status codes are '2xx' for success, '4xx' for client errors, and '5xx' for server errors. If you scroll down the page, the documentation shows various HTTP status code you may encounter.
  6. Also, observe that the JSON response contains information about the newly created space such as its `id` property.
  7. Now, open your Webex client and view the new room created by the API request. ![NewRoom](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt2f0a1010e962df98/6202f7aeb7731b0ad7717b2d/new_room.png)


Next, let’s look at the potential of Webex extensibility.
####  anchorTypes of Webex Applications
anchor
In previous steps, we covered how Webex REST API makes it simple to create automated interactions against the Cisco Webex Cloud Platform.
Here are various types of applications you could build using the same approach:
  * **Controller** : This type of app listens for events in Webex, such as new messages that contain a specific mention, or a participant being added to a space. When these events happen, the app could send an SMS alert or use Webex to send data to an enterprise back-end.
_NOTE_ : In Webex terminology, an app that listens but does not take any action is called a _watcher_.
  * **Notifier** : This type of app responds to events by sending messages to a Webex space. For example, it could send a message to a "Business Activity" space when new customers sign-in and orders are created or canceled. Employees would monitor new messages in the “Business Activity” space and respond if further actions were needed.
  * **Interactive Assistants** : This type of app asks a customer a set of questions and uses the answers to perform actions such as filling out a form, scheduling an appointment, or simulating the interest on loan. These types of interactive apps are sometimes called "chat bots" or simply "bots."


When extending Webex, one uses the term _applications_ rather than the generic _bots_. As you'll see in next chapter, the concept of a "Webex Bot" is associated with _bot accounts_ and specific behaviors attached to 'Direct' and 'Group' spaces.
###### Create your application
Depending on your technical background and business goals, there are several ways you can go about creating an application:
  * You can design and build an app using a visual integration tool. This approach is like creating software from Lego-like building blocks and requires little to no coding. These blocks perform defined tasks and connect to various back-end services.
Various third-party vendors also offer visual integration tools and services, such as IFTTT, Zapier, Built.io, Gupshup, Stamplay, Workato. These services simplify deploying applications and offer benefits such as pre-configured integrations, natural language processing, voice synthesis, voice recognition, and image analysis.
  * You can write and deploy your code. The Webex API enables you to create an application in any language, and the community has been working on frameworks and examples to help you on this journey.
Delivering apps that are more than prototypes requires allocating effort and resources to meet availability and security requirements. These include setting up and monitoring a DNS, load-balancing, firewalls, traffic monitoring, rate limitations, etc.


In the upcoming Tutorials, you’ll have an opportunity to create apps using code or third-party tools.
####  anchorBots and Integrations
anchor
Here, you will see how your application can run on behalf of other Webex Users.
Suppose you’re building an "Out of Office Assistant" application that automatically responds to Webex messages on behalf of pre-registered users while they are away. Webex users will authorize your app to screen their messages and respond on their behalf when they are mentioned.
This type of application is called as **Webex Integration**. The Webex integrations use the OAuth Grant Flow protocol to issue the access tokens that can act under Webex users' identities. These tokens are scoped: Limited to the set of authorizations granted by the Webex users themselves.
![apps](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt3a045a22da62f6c6/61bb5cebe5a70e7d5276b582/step5-access-tokens.png)
Suppose you want your Out Of Office Assistant to behave a little differently: Any user could invite the assistant into a Webex space and interact with it like this: “@OutOfOffice is Mandy on vacation?” or “@OutOfOffice note that I'll be away for the next 2 weeks”.
In that case, you would want your _Out Of Office_ application to receive and respond to questions using its own identity, not using someone else's identity.
This is where _Bot Accounts_ come into play. Bots are dedicated Webex accounts that act under their identity. They can be added to spaces like any other Webex user. Some differences and restrictions apply. For example, bots MUST be 'mentioned' to receive messages in group spaces.
####  anchorWrapping up
anchor
Webex exposes a REST API that enables you to create various applications such as notifiers, watchers, controllers, and interactive assistants.
Apps are nothing more than code that interacts with Webex using an API access token. Your applications can inherit an identity from an access token and can function:
  * as 'another you' (from a Developer Access Token).
  * on behalf of other users (Webex [OAuth Integrations](https://developer.webex.com/docs/integrations)).
  * or as a well identified machine (Webex [Bot accounts](https://developer.webex.com/docs/bots)).


####  anchorGoing further
anchor
In this tutorial, we covered the [REST API resources](https://developer.webex.com/docs/getting-started) accessible to all Webex Users. If you have administrator privileges for your Webex organization, you might be interested in digging into the [Admin API](https://developer.webex.com/docs/admin): `/events, /metrics, /policies, /licenses, /organizations` and `/roles`. These restricted-access resources will give you the opportunity to automate the provisioning of users, as well as monitor the activity within your organization - or even restrict access to integrations.
Finally, do you know that Webex offers more than REST APIs? Indeed, the Webex SDKs and [Widgets](https://developer.webex.com/docs/widgets) give you access to the broader Media resources, opening a new world of possibilities to embed Video, or place calls from existing [Web](https://developer.webex.com/docs/sdks/browser), [iOS](https://developer.webex.com/docs/sdks/ios) and [Android](https://developer.webex.com/docs/sdks/android) applications.
##### In This Article
  * [Prerequisites](https://developer.webex.com/docs/introduction-to-webex-apps#prerequisites)
  * [About Webex Extensibility](https://developer.webex.com/docs/introduction-to-webex-apps#about-webex-extensibility)
  * [REST API Documentation](https://developer.webex.com/docs/introduction-to-webex-apps#rest-api-documentation)
  * [Invoking the REST API](https://developer.webex.com/docs/introduction-to-webex-apps#invoking-the-rest-api)
  * [Types of Webex Applications](https://developer.webex.com/docs/introduction-to-webex-apps#types-of-webex-applications)
  * [Bots and Integrations](https://developer.webex.com/docs/introduction-to-webex-apps#bots-and-integrations)
  * [Wrapping up](https://developer.webex.com/docs/introduction-to-webex-apps#wrapping-up)
  * [Going further](https://developer.webex.com/docs/introduction-to-webex-apps#going-further)


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
