[](https://developer.webex.com/)
[Getting Started](https://developer.webex.com/create/docs)Documentation![](https://developer.webex.com/messaging/docs/bots)[AI in Webex](https://developer.webex.com/mcp/docs/webex-mcp-server-overview)Blog![](https://developer.webex.com/messaging/docs/bots)[Support](https://developer.webex.com/explore/support)Resources![](https://developer.webex.com/messaging/docs/bots)
[Log in](https://developer.webex.com/login)[Sign up](https://developer.webex.com/signup)
[Home](https://developer.webex.com/)/Bots
Webex Messaging
  * [Overview](https://developer.webex.com/messaging/docs/messaging)
  * Guides
    * [Access the API](https://developer.webex.com/messaging/docs/getting-started)
    * [Integrations & Authorization](https://developer.webex.com/messaging/docs/integrations)
    * [Using Webex Service Apps](https://developer.webex.com/messaging/docs/service-apps)
    * [Bots](https://developer.webex.com/messaging/docs/bots)
    * [Webhooks](https://developer.webex.com/messaging/docs/api/guides/webhooks)
    * [Buttons and Cards](https://developer.webex.com/messaging/docs/buttons-and-cards)
    * [Messaging MCP Server](https://developer.webex.com/messaging/docs/messaging-mcp-server)
  * [REST API Basics](https://developer.webex.com/messaging/docs/basics)
  * API REFERENCE
  * All APIs
  * [Changelog](https://developer.webex.com/messaging/docs/api/changelog/webex-messaging)
  * SDK
  * [AI Assistant for Developers](https://developer.webex.com/messaging/docs/webex-aI-assistant-for-developers)
  * [Troubleshoot the API](https://developer.webex.com/messaging/docs/api/guides/troubleshooting)
  * [Widgets](https://developer.webex.com/messaging/docs/widgets)
  * [Tutorials](https://developer.webex.com/messaging/docs/tutorials)
  * [Suite Sandbox](https://developer.webex.com/messaging/docs/developer-sandbox-guide)
  * [Beta Program Overview](https://developer.webex.com/messaging/docs/webex-developer-beta-program)
  * [Webex Status API](https://developer.webex.com/messaging/docs/webex-status-api)


## Webex Messaging
### Bots
Give Webex users access to outside services right from their Webex spaces. Bots help users automate tasks, bring external content into the discussion, and gain efficiencies.
[Create a Bot](https://developer.webex.com/my-apps/new/bot)
####  anchorBots Explained
anchor
Bots are similar to regular Webex users. They can participate in 1-to-1 and group spaces and users can message them directly or add them to a group space. A special badge is added to a bot's avatar in the Webex clients so users know they're interacting with a bot instead of a human.
A bot can only access messages sent to it directly. In group spaces, bots must be [@mentioned](https://help.webex.com/p5k20o/) to access the message. In 1-to-1 spaces, a bot has access to all messages from the user.
Bots do not, however, perform actions within Webex on behalf of a Webex user. If you're creating an application that needs to participate in Webex and perform actions with a user's account, check out [Integrations](https://developer.webex.com/docs/integrations).
####  anchorTypes of Bots
anchor
Bots come in all different shapes and sizes. Here are some ideas for a few different types of bots you can make:
###### Notifiers
Notifier bots typically respond to events in external services and post a summary in Webex. For example, a _GitHub Bot_ may listen for commits on a particular repo and post the committer's name and comment into a Webex space set aside for this purpose. Or a _Deal Bot_ that lives in an account-specific space and posts updates from a CRM along with relevant news about the company like a product launch or earnings report.
###### Controllers
Controller bots act as a text-based remote control for external services. For example, a _Jira Bot_ may allow software engineers and product managers to control or query information from the popular bug tracking system Jira, all from the comfort of a Webex space.
![](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt15175555e3f933b0/5d4ad4ec0331293861b7a626/Bot-Example.png)
Controller bots are generally passive, waiting for someone in the room to issue a command. In group rooms, bots can only see messages in which they are mentioned (1:1 rooms bots can see all messages as they are automatically "mentioned"). Your users are required to mention the bot preceding the command like `@jira find WEBSITE-22` where `@jira` is the bot's name.
Currently, the Webex SDKs do not support extracting commands from messages. You'll need to parse it out after the mention. Future versions of the Webex SDKs will have built-in support for commands. Keep your eyes on the blog for updates.
###### Assistants
Virtual assistants are the holy grail of chatbots. At minimum, an assistant should understand natural language, allowing the user to ask it questions as they would to a human.
Recent advancements in NLP (Natural Language Processing) have made understanding natural language requests not only possible, but quite accessible to the average developer. Most notably, Google launched [Google Cloud Natural Language API](https://cloud.google.com/natural-language/) in the summer of 2016, providing syntax parsing, sentiment analysis and deep noun classification.
Responding to natural language is a good first step but a truly exceptional assistant bot will be conversational, using past interactions to contextualize the most recent query. This is a very complex problem domain; luckily there are companies like [Dialogflow](https://dialogflow.com/) providing a conversational platform built specifically for bots.
####  anchorCreating a Webex Bot
anchor
Creating a Webex Bot is super easy. If you're logged in, select [My Webex Apps](https://developer.webex.com/my-apps) from the menu under your avatar at the top of this page, click "Create a New App" then "Create a Bot" to start the wizard.
You'll be asked to provide some basic information about the bot: bot name, bot username, and an icon. These fields are end-user facing, so make them as descriptive as possible. Only the bot's first name will be shown when mentioned in messages, so try to avoid spaces in the bot name. The description will be shown to users if you submit your bot to the [Webex App Hub](https://developer.webex.com/docs/app-hub-submission-process).
Webex App Hub is not supported for Webex for Government (FedRAMP)
Once you've filled out the registration form click "Add Bot", and if everything goes smoothly you're all set! You'll be given an access token for the new bot. This access token will be used to authenticate your bot with the Webex REST API.
The bot's access token will only be displayed once. Make sure to scroll down on the confirmation page, copy the token and keep it somewhere safe. If you misplace it, you can always generate a new one by finding the bot in [My Webex Apps](https://developer.webex.com/my-apps) and selecting "Regenerate Access Token" from the edit page.
####  anchorResponding to Events
anchor
After creating a bot, you can use its access token with the Webex REST APIs to perform actions as the bot, such as [sending a message](https://developer.webex.com/docs/api/v1/messages/create-a-message) with an interactive [card](https://developer.webex.com/docs/api/guides/cards) to someone. To respond to events within Webex, such as someone sending your bot a message or adding it to a group space, you'll need to configure webhooks. Webhooks will let you know when an activity has occurred so you can take action. Check out the [Webhooks Guide](https://developer.webex.com/docs/api/guides/webhooks) for more information about configuring webhooks.
With cards, you can give your users even more ways to interact with your bot or service, right in the Webex clients. Use the [Buttons and Cards Designer](https://developer.webex.com/buttons-and-cards-designer) to quickly create and prototype cards for your bot. See the [Buttons and Cards Guide](https://developer.webex.com/docs/api/guides/cards) for more information about cards.
####  anchorDifferences Between Bots and People
anchor
One key difference between Webex Bots and regular users is that, in group spaces, bots **only have access to messages in which they are mentioned**. This means that `messages:created` webhooks only fire when the bot is mentioned in a space.
Also, [listing messages](https://developer.webex.com/docs/api/v1/messages/list-messages) requires that you specify a special `?mentionedPeople=me` query parameter.
In addition people have a `personId` that must be resolved via /people, bots have a Bot Id and a `personId`. The Bot Id is shown in the apps page and is usually only known to the developer. The bot's `personId` can be looked up via the bot's email address in /people. 

```
GET /messages?mentionedPeople=me&roomId=SOME_INTERESTING_ROOM
Authorization: Bearer THE_BOTS_ACCESS_TOKEN

```

####  anchorBot Frameworks & Tools
anchor
There are several bot frameworks that can greatly simplify the bot development process by abstracting away the low-level communications with the Webex REST API, such as creating and sending API requests and configuring webhooks. Instead, you can focus on the building the interaction and business logic of your bot.
[Flint](https://github.com/flint-bot/flint) is an open source bot framework with support for regex pattern matching for messages and more.
[Botkit](https://github.com/howdyai/botkit) is a popular open source bot framework with advanced conversational support as well as integrations with a comprehensive array of natural language processing and storage providers. You can get started with Botkit by cloning the Webex [Botkit Starter Kit](https://github.com/howdyai/botkit-starter-ciscospark).
The Cisco Webex Ambassador program has links to several more [open source bot starter kits](https://ciscowebexteamsambassadors.github.io/StarterKits/). Keep your eyes on our [blog](https://developer.webex.com/blog) for updates and news about our community-supported tools!
##### In This Article
  * [Bots Explained](https://developer.webex.com/messaging/docs/bots#bots-explained)
  * [Types of Bots](https://developer.webex.com/messaging/docs/bots#types-of-bots)
  * [Creating a Webex Bot](https://developer.webex.com/messaging/docs/bots#creating-a-webex-bot)
  * [Responding to Events](https://developer.webex.com/messaging/docs/bots#responding-to-events)
  * [Differences Between Bots and People](https://developer.webex.com/messaging/docs/bots#differences-between-bots-and-people)
  * [Bot Frameworks & Tools](https://developer.webex.com/messaging/docs/bots#bot-frameworks--tools)


##### Related Resources
  * [From Zero to Webex Chatbot in 15 Minutes](https://developer.webex.com/blog/from-zero-to-webex-teams-chatbot-in-15-minutes "From Zero to Webex Chatbot in 15 Minutes")
  * [Botkit](https://github.com/howdyai/botkit "Botkit")
  * [Webex Bot Node.js Framework](https://github.com/webex/webex-bot-node-framework "Webex Bot Node.js Framework")
Show more 

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
