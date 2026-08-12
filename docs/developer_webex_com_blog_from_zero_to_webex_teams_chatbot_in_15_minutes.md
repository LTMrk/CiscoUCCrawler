[](https://developer.webex.com/)
[Getting Started](https://developer.webex.com/create/docs)Documentation![](https://developer.webex.com/blog/from-zero-to-webex-teams-chatbot-in-15-minutes)[AI in Webex](https://developer.webex.com/mcp/docs/webex-mcp-server-overview)Blog![](https://developer.webex.com/blog/from-zero-to-webex-teams-chatbot-in-15-minutes)[Support](https://developer.webex.com/explore/support)Resources![](https://developer.webex.com/blog/from-zero-to-webex-teams-chatbot-in-15-minutes)
[Log in](https://developer.webex.com/login)[Sign up](https://developer.webex.com/signup)
# From Zero to Webex Chatbot in 15 Minutes
July 19, 2023
![Phil Bellanti](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltcaa16bd81f3da66a/6153919e8440e97ef5829e0b/Phil_at_Cisco_Live.png?width=100&height=100&fit=crop)
Phil BellantiSenior Webex Developer Evangelist
![From Zero to Webex Chatbot in 15 Minutes](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt7ecfa2d750b2af80/64b80a590c8acebcdf02e826/15_min_bot_blog_banner.png?width=900&height=317&fit=crop)
This blog post was originally published in December 2019 and has now been updated for 2023.
If you are looking for the basics on how to create a Webex messaging bot, you have come to the right place. This easy to download, easy to run sample allows would-be developers to get a simple bot up and running in 15 minutes and provides a structure for building more complicated bots.
Webex currently powers thousands of bots with a variety of functionality, ranging from simple chat bots that provide specific information like the current weather, to more sophisticated bots that understand natural language and automate complex business tasks. Perhaps you've been wanting to deploy a handy chatbot of some kind and just haven't gotten a chance to start on it yet. Well, this is your big chance!
![What we're making](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltdbd0d29a323c1901/5dee96c8162f1938620d47e1/bot-starter-example.gif)
Back when Webex (then called Spark) bot functionality was first made available, there were several simple starters. We always liked the old [sparkbotstarter](https://github.com/valgaze/sparkbotstarter) that was created by Victor Algaze, using a framework called [Flint](https://github.com/flint-bot/flint), which was created by Nick Marus. This sample is based on the updated, Webex community library [webex-node-bot-framework](https://github.com/WebexCommunity/webex-node-bot-framework), and adds a few fun new tricks, like posting a message using [Webex Buttons and Cards](https://developer.webex.com/docs/api/guides/cards).
### Getting Started
Even if you don't have any prior knowledge of the Webex APIs, this guide will have you deploy a functioning chatbot application pretty quickly. Then from there, the bot-starter application can serve as a template for creating your own customized bots and can be extended to your heart's content. You might need to be at least a little familiar with node.js and also have the following prerequisites:
  1. [Node & npm](https://nodejs.org/en/) (minimum tested version is node 8.0.0 or higher) and [git](https://git-scm.com/downloads) installed on your machine
  2. A Webex account: <https://web.webex.com/>


### Sign into Webex
The first thing to do is use your regular Webex credentials to log in to Webex for Developers and create a [new bot](https://developer.webex.com/my-apps/new/bot/). When you create the bot account, be sure to jot down the bot’s username & access token before leaving the creation page - we'll need those in a minute.
### Set up the Local Web Server
The bot application has to be hosted on a server where it can communicate over HTTP. For now, we'll use [nGrok](https://ngrok.com/), which is a tool that turns your machine into a web server by opening a local port to the Internet. We're doing this so we can start using our chatbot as quickly as possible without having to think about deployment or hosting. Since we are aiming to start testing now, nGrok uses the least number of steps to get there.
nGrok can open up the machine it is installed on to security risks and needs to be done only in a non-prod setup that is completely distinct from any other production services or systems. Once you’ve customized your chatbot, you should deploy it on a proper cloud hosting service, such as Microsoft Azure or other similar platforms, instead of your machine.
  * Download and setup nGrok here: <https://ngrok.com/>
  * After downloading and unzipping nGrok, from the same directory as the nGrok executable execute this command:
`$ ./ngrok http 7001`
  * If the tunnel has trouble connecting, try adding a region code to the command: `$ ./ngrok http 7001 --region=eu`


Once it's running, write down the web address that's tunneling to your `localhost:7001` (e.g. <https://XXXXXXX.ngrok-free.app>) and keep it handy. 
### Configure and Run the App
Now we just need to download the project, swap in a few values, and start the bot up!
  * Download the [node.js Webex Bot Starter](https://github.com/WebexSamples/webex-bot-starter) template project with this command in your terminal:
`git clone https://github.com/WebexSamples/webex-bot-starter && cd webex-bot-starter`
  * From the `webex-bot-starter` directory, copy the file `.env.local` to a _new file_ with only `.env` as the name. Do note these files might be hidden.
  * Open the new `.env` file in a code or text editor and swap out the following values:


```
  {
    "webhookUrl": "http://XXXXXXX.ngrok.io",
    "token": "BOT_TOKEN_CREATED_FROM_EARLIER",
    "port": 7001
  }

```

Note that if/when you turn off nGrok, when you turn it back on the URL will change and you will need to update the config with the new address.
  * Save the changes to `.env` file.
  * Finally, to install and start the application, run this command:
`$ npm start`
  * If you're using a Mac, you might receive a prompt asking about “node” accepting incoming network connections. If so, click **Allow** to load the server:


![incoming connection](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blte0e65d6d253124f6/5dee96c6aecae93859555d2f/bot-starter-incoming-connections.png)
### Interact with the Bot in Webex
Now that the nGrok server is loaded and the app is running, create a new group space (name the title whatever you want) in the Webex client. Next, add your bot to the space (by the username you created earlier), just as you would add any other Webex user.
If everything was done correctly, your bot should have greeted you with some instructions when it was added to the space. You now have a running chatbot! To go further, open the `index.js` file in an editor and extend functionality as much as you need.
### Helpful Resources
  * This bot starter application is based from the webex-node-bot-framework:
<https://github.com/WebexCommunity/webex-node-bot-framework>
  * Intro to the Webex for Developer platform:
[https://developer.webex.com/docs/platform-introduction](https://developer.webex.com/docs/platform-introduction)
  * Webex Bots explained:
[https://developer.webex.com/docs/bots](https://developer.webex.com/docs/bots)
  * Guide for creating Webex Buttons and Cards in messages:
[https://developer.webex.com/docs/buttons-and-cards](https://developer.webex.com/docs/buttons-and-cards)


Blog Categories
  * [Product Announcements](https://developer.webex.com/blog/categories/product-announcements)
  * [How To](https://developer.webex.com/blog/categories/how-tos)
  * [Events](https://developer.webex.com/blog/categories/events)
  * [Developer Stories](https://developer.webex.com/blog/categories/developer-stories)


Share This Article
Related Articles
![Give Your Webex Bot some $uperpowers](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt6f9b8c20f3a87bb7/61aa2a910ff4f914f4196cbc/speedometer.jpg?width=600&height=300&fit=crop)
How-To
[Give Your Webex Bot some $uperpowers](https://developer.webex.com/blog/give-your-webex-bot-some-superpowers)
Victor Algaze
December 13, 2021
![A Deeper Dive Into the Webex Bot Framework for Node.js](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blte34049b5389fe870/5e431e29c43f006b462745b1/webex-node-framework-tips-header.jpg?width=600&height=300&fit=crop)
How-To
[A Deeper Dive Into the Webex Bot Framework for Node.js](https://developer.webex.com/blog/a-deeper-dive-into-the-webex-bot-framework-for-node-js)
Phil Bellanti
March 5, 2025
![How I Used ChatGPT to Build a Webex Integration](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltc53efe7fb345dd9d/642afd6b0afb1c108e792bce/chatgpt-integration-1.png?width=600&height=300&fit=crop)
How-To
[How I Used ChatGPT to Build a Webex Integration](https://developer.webex.com/blog/how-i-used-chatgpt-to-build-a-webex-integration)
Adam Weeks
April 3, 2023
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
