[](https://developer.webex.com/)
[Getting Started](https://developer.webex.com/create/docs)Documentation![](https://developer.webex.com/blog/word-of-the-hour-bot-on-webex)[AI in Webex](https://developer.webex.com/mcp/docs/webex-mcp-server-overview)Blog![](https://developer.webex.com/blog/word-of-the-hour-bot-on-webex)[Support](https://developer.webex.com/explore/support)Resources![](https://developer.webex.com/blog/word-of-the-hour-bot-on-webex)
[Log in](https://developer.webex.com/login)[Sign up](https://developer.webex.com/signup)
# Word of The Hour Bot on Webex
April 7, 2022
![Michael Wehar](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blte93ee2e8cdc5bc83/624f2b5f21fd967b5ff23029/Michael_Wehar.jpg?width=100&height=100&fit=crop)
Michael WeharFounder, Word of the Hour
![Word of The Hour Bot on Webex](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blte136b7c560049c4d/624f2c39983be97a32ffe078/WOTH_blog_banner.jpg?width=900&height=317&fit=crop)
### Introduction
As an independent developer, I actively seek out new platforms to build and launch applications. If you are an engineer who ventures outside of the common web and mobile development platforms, you will find alternative platforms that need talented independent developers who can help satisfy customer needs, build new brands, and advance new market opportunities.
#### My Question
This need for independent developers led me to the following question: “ _What platforms should independent developers be looking at in 2022 and beyond?”_
#### One Possible Answer
I suggest that the answer may very well be integrations, addons, and bots for chat and messaging platforms. Therefore: “ _With the recent growth in remote and hybrid work opportunities, chat and messaging platforms have become essential within the workplace which has introduced new challenges and opportunities._ * *_If an addon can help increase productivity, improve quality of collaboration, or advance education, then there will be an immediate benefit for a customer or business.”_
### Word of The Hour
For the past five years, I have been developing a multiplatform application called [Word of The Hour](https://wordofthehour.org/) (or WOTH). WOTH allows users to learn 24 new vocabulary words every day (or one word per hour) across over 10+ languages including (Spanish, French, German, Italian, Portuguese, Welsh, Swedish, and more!). WOTH is intended to be a supplement to your language learning experience by providing additional vocabulary practice, notifications, and motivation to stay active with your language education. For more information about WOTH, see our website [here](https://wordofthehour.org/).
Recently, WOTH has started working with world leading messaging platforms to pursue new and innovative opportunities. Naturally, Webex has been a key platform to focus on.
### Developing for Webex Platform
The [Webex](https://www.webex.com/) platform stood out to me because of its focus on professionalism, innovation, and language accessibility. So let us talk briefly about how I got started with developing WOTH for Webex.
For Webex, you can develop Bots or Integrations. A bot is like a Webex user that can communicate with you via messaging. On the other hand, an integration is more like an external application that can connect with your Webex account.
Below I will talk about how I built a bot for the Webex platform:
  1. Go to the [Webex for Developers Website](https://developer.webex.com/). Create a Webex account and then select "Start Building Apps". From there, you can create your bot and obtain a bot username (for example, my bot's username is WordOfTheHour@webex.bot). Users will be able to communicate with the bot directly or by adding the bot to an existing space.
  2. Start building the bot. I decided to build the WOTH bot using [Node.js](https://nodejs.org/). Get started by cloning the Git repository: [Webex Node Bot Framework](https://github.com/WebexCommunity/webex-node-bot-framework). Look at the README.md file for instructions on Installation and Examples. I also decided to have the WOTH bot reply with [Buttons and Cards](https://developer.webex.com/docs/api/guides/cards). When developing your bot, I strongly encourage you to carefully read through Webex's documentation to see how features are supported across all Webex client applications.
  3. Once I had a demo ready, I started testing locally. To do this, I created an account with [nGrok](https://ngrok.com/). Next, I was able to configure the WOTH bot with the appropriate nGrok URL and port number. Then, I could run my Node.js application to see my bot interacting with the Webex platform. Later, I deployed my Node.js application onto a [Heroku](https://www.heroku.com/) server and changed the configuration to use the appropriate Heroku URL and port number.
  4. The final step is to launch your creation to the [AppHub](https://apphub.webex.com/). This will allow Webex users to be able to find your creation and get started using it. As an example, see the AppHub page for Word of The Hour [here](https://apphub.webex.com/applications/wordofthehour-word-of-the-hour-66032). Also, give the WOTH bot a try. It is currently in its initial version, but we are hoping to gain feedback and add additional features soon!


Thank you for reading and I hope that you will consider developing applications for chat and messaging platforms like Webex!
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
