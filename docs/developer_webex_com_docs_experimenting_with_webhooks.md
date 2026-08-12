[](https://developer.webex.com/)
[Getting Started](https://developer.webex.com/create/docs)Documentation![](https://developer.webex.com/docs/experimenting-with-webhooks)[AI in Webex](https://developer.webex.com/mcp/docs/webex-mcp-server-overview)Blog![](https://developer.webex.com/docs/experimenting-with-webhooks)[Support](https://developer.webex.com/explore/support)Resources![](https://developer.webex.com/docs/experimenting-with-webhooks)
[Log in](https://developer.webex.com/login)[Sign up](https://developer.webex.com/signup)
## Experimenting with Webhooks
### Experimenting with Webhooks
Webhooks allow your app to be notified via HTTP when a specific event occurs in Webex. An event could be triggered by a message being posted to a space, or a user joining or leaving a space, or a meeting that started or stopped. Events trigger in near real-time allowing your app and backend IT systems to stay in sync with new content and room activity.
You can think of webhooks as "reverse APIs" where the Webex cloud platform posts data to your application (instead of the other way around.) For example, you can register a webhook so that your application receives a notification every time a new message is posted in a particular Webex space.
![Webhooks diagram](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltdbb3cc4d55c85298/6349e0791e79f1285f68717f/webhooks_img.png)
Webhooks require a publicly reachable URL, where you application will be listening for inbound HTTP requests.
To make learning about creating and using webhooks easier, you'll use [ngrok](https://ngrok.com), an HTTP tunneling tool, running on your local system as a quick and easy way to inspect the contents of webhook messages without having to create and deploy a new backend service. 
Of course, in a production situation, you would set up the webhook so that Webex sends the notification to an actual running application that you have coded (ngrok's main function is actually to forward such requests to a web app running on a local PC). Today, we are just using ngrok by itself so that you can see how a webhook works without having to write an application first.
####  anchorObjectives
anchor
  * Understand how Webex webhooks work
  * Create a webhook
  * View a webhook in action


####  anchorPrerequisites
anchor
To complete this tutorial you'll need the following:
  * **A Webex account** — If you don't have a Webex account go to <https://cart.webex.com/sign-up> and follow the instructions to create one.
  * **ngrok** — A public HTTP proxy service and client: <https://ngrok.com/>.


####  anchorStep 1: Create a Space for Testing
anchor
For the purpose of this tutorial we'll capture events fired every time new messages are created in a space called "Marketing Campaign". You'll use the Webex app to create the space.
  1. Open the Webex desktop app and press Ctrl+Shift+N or Cmd+Shift+N to open the new space page.
  2. Give the space a name like ""Marketing Campaign", then click **Create**.
![Creating a test space](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltce2f9e122c40d608/623b9827549d685f55b5a3c0/create-space-in-webex.png)


####  anchorStep 2: Get the ID of the Space
anchor
As most Webex users have many spaces, we will use the **filter** parameter in our webhook request to restrict webhook notifications only for message events from the "Marketing Campaign" space. To do this we first need to determine the unique identifier (`id`) of the space. We'll use the **Try It** feature in the Webex interactive API reference to retrieve the names and IDs of all of the spaces where your user is a member, using the `/rooms` resource. 
**To obtain the ID of the new space** :
  1. [Sign in](https://developer.webex.com/login) to the Developer Portal if you're not already signed in.
  2. Open the [List rooms](https://developer.webex.com/docs/api/v1/rooms/list-rooms) API reference and make sure the **Use Personal Access Token** option is enabled.
  3. Click **Run**.
![](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt260dca94a427e159/623b546b714afc639a7b23e0/try-it-list-rooms.png)
  4. Scroll down to view the results and locate the "Marketing Campaign" item in the JSON results.
![](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltb13d31c2c5b905b8/623b546bbe82216394d3eb94/try-it-results-list-rooms.png)
  5. Copy the value of the `id` field to your clipboard.


####  anchorStep 3: Setup ngrok to capture web requests
anchor
Next you'll download and start ngrok on your local system and obtain its public HTTPS URL. You'll provide this URL when you create the webhook that will listen for events.
**To set up ngrok service and retrieve its unique URL:**
  1. [Download the ngrok client](https://ngrok.com/download) and unzip it. (It's not necessary to sign up to use ngrok.)
  2. Open a terminal window and navigate to the download directory.
  3. Launch `ngrok` to listen for HTTP requests on port 5000:


  * **Mac/Linux** : `./ngrok http 5000`
  * **Windows** : `ngrok http 5000`
When ngrok starts up it will display some information about the service, including its public HTTPS URL:
![ngrok screenshot](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt87bbbb380ff73470/623a6654159fc76504c175c3/ngrokscreenshot.png)


  1. Copy and save this HTTPS URL for use in the next steps.
  2. Open a web browser and browse to `http://localhost:4040` to view the ngrok request inspector:
![ngrok screenshot](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt6153691a0c221034/623a6654483e2c64fe287a7c/ngrokinspector.png)
This is where you will observe JSON payloads for each webhook event later in the tutorial.


####  anchorStep 4: Register a new webhook
anchor
To begin receiving events you need to register a webhook with Webex. To do this you make an HTTP **POST** to the `/webhooks` resource URL, passing it information about the webhook, including the URL that should be notified when the event occurs. You also specify the type of API resource you want the webhook to monitor ('messages'), the kind of event ('created'), and a filter to limit events for the room ID you obtained in the previous step. For details about the types of resources, events, and filters available for webhooks, see the [Filtering Webhooks](https://developer.webex.com/docs/api/guides/webhooks#filtering-webhooks).
**To register a new webhook** :
  1. Open the [Create a Webhook](https://developer.webex.com/docs/api/v1/webhooks/create-a-webhook) API reference and make sure the **Use Personal Access Token** option is enabled. 
  2. In the **Body** section of the request form, fill out the fields with the following information, replacing **< ngrok-url>** and **< room-ID>** with the ngrok URL and room ID obtained in steps 2 and 3.  
| Input field  | Value  |  
| --- | --- |  
| name  | **Messages webhook**  |  
| targetURL  | **< ngrok-url>**  |  
| resource  | **messages**  |  
| event  | **created**  |  
| filter  | **roomId= <room-ID>**  |  
  3. Click **Run** to create the new webhook. 
A successful HTTP response contains a JSON representation of the newly created webhook.
![Webhook Response](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltf1ccd875c9efeea9/623b946b5fa15f0a668450e6/webhookresponse.png)


Next you'll observe JSON payloads being send to your ngrok endpoint when new messages are created in the Marketing Campaign space.
####  anchorStep 5: Observe the Webhook in Action
anchor
Let's put it all together so we can see the webhook in action. Any new message that is added to the Marketing Campaign space will trigger the webhook, which will cause Webex to send a notification to the target ngrok URL. Each notification is a JSON object that includes the ID of the new message, and other information about what caused the notification. See [Handling Requests from Webex](https://developer.webex.com/docs/api/guides/webhooks#handling-requests-from-webex) for details about all the fields returned by the webhook.
**To view webhook events:**
  1. Open the Webex app and post a message in the "Marketing Campaign" space. 
![Sending a message to space](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt9310ff688a78a093/623b8ceb549d685f55b5a3a0/send-message-webex.png)
  2. In your browser open the ngrok inspector URL at <http://localhost:4040> to see the Webex webhook notification message details, which will look like the following:
![ngrok screenshot](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blte1acd9c1ad2a70e0/623a6654e6c8cf4de6f6dace/messagedetails.png)
The `502 Bad Gateway` message is expected, as ngrok is not configured to point to an actual listening app
Here's an example JSON body formatted for easier reading:

```
{
  "id":"Y2lzY29zcGFyazovL3VzL1dFQkhPT0svZjRlNjA1NjAtNjYwMi00ZmIwLWEyNWEtOTQ5ODgxNjA5NDk3",
  "name":"Guild Chat to http://requestb.in/1jw0w3x1",
  "resource":"messages",
  "event":"created",
  "filter":"roomId=Y2lzY29zcGFyazovL3VzL1JPT00vY2RlMWRkNDAtMmYwZC0xMWU1LWJhOWMtN2I2NTU2ZDIyMDdi",
  "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8xZWI2NWZkZi05NjQzLTQxN2YtOTk3NC1hZDcyY2FlMGUxMGY",
  "createdBy": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8xZjdkZTVjYi04NTYxLTQ2NzEtYmMwMy1iYzk3NDMxNDQ0MmQ",
  "appId": "Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OL0MyNzljYjMwYzAyOTE4MGJiNGJkYWViYjA2MWI3OTY1Y2RhMzliNjAyOTdjODUwM2YyNjZhYmY2NmM5OTllYzFm",
  "ownedBy": "creator",
  "status": "active",
  "actorId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8xZjdkZTVjYi04NTYxLTQ2NzEtYmMwMy1iYzk3NDMxNDQ0MmQ",
  "data":{
    "id":"Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMzIzZWUyZjAtOWFhZC0xMWU1LTg1YmYtMWRhZjhkNDJlZjlj",
    "roomId":"Y2lzY29zcGFyazovL3VzL1JPT00vY2RlMWRkNDAtMmYwZC0xMWU1LWJhOWMtN2I2NTU2ZDIyMDdi",
    "personId":"Y2lzY29zcGFyazovL3VzL1BFT1BMRS9lM2EyNjA4OC1hNmRiLTQxZjgtOTliMC1hNTEyMzkyYzAwOTg",
    "personEmail":"person@example.com",
    "created":"2015-12-04T17:33:56.767Z"
  }
}

```

The JSON object's `data` field contains a JSON representation of the message resource that triggered the webhook, including the ID of the message, the room ID, as well as the ID and email of the person who sent the message. To get the actual message text, you make another request to the `GET /messages` API, passing the ID of the message as parameter.
  3. Copy the value of the `data` object's `id` field to your clipboard, which is the ID of the newly created message.


**To get the message text:**
To see the new message in our webhook request, we'll make a request to the [Get Message Details](https://developer.webex.com/docs/api/v1/messages/get-message-details) API.
  1. Open the [Get Message Details](https://developer.webex.com/docs/api/v1/messages/get-message-details) API reference page.
  2. Click on the `messageId` URL fragment and paste in the message ID you obtained in the previous steps.
![Adding message ID to request URL](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt1a29cddfa6677a3a/623b90ef714afc639a7b24d6/get-message-details.png)
  3. Click **Run**. The message details are displayed in the **Results** area.
![Response](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blta3a7813ca25f6ba4/623b91d3714afc639a7b24da/message-contents.png)


####  anchorGoing further
anchor
To learn more about the **Webhooks API** , check out [Webhooks](https://developer.webex.com/docs/webhooks) in the Webex documentation.
At the end of the day, webhooks are leverage by developers to create interactive chat bots. The labs below will drive you through the steps to build your first bots:
  * Node.js tutorial: <a


href="<https://developer.cisco.com/learning/modules/spark-apps>" target="_blank">Creating Chatbots for Webex
  * Python tutorial: <a


href="<https://developer.cisco.com/learning/tracks/devnet-express-cloud-collab-it-pro/creating-spark-bots-itp/collab-spark-botl-itp/step/1>" target="_blank">Run a Webex bot locally
##### In This Article
  * [Objectives](https://developer.webex.com/docs/experimenting-with-webhooks#objectives)
  * [Prerequisites](https://developer.webex.com/docs/experimenting-with-webhooks#prerequisites)
  * [Step 1: Create a Space for Testing](https://developer.webex.com/docs/experimenting-with-webhooks#step-1-create-a-space-for-testing)
  * [Step 2: Get the ID of the Space](https://developer.webex.com/docs/experimenting-with-webhooks#step-2-get-the-id-of-the-space)
  * [Step 3: Setup ngrok to capture web requests](https://developer.webex.com/docs/experimenting-with-webhooks#step-3-setup-ngrok-to-capture-web-requests)
  * [Step 4: Register a new webhook](https://developer.webex.com/docs/experimenting-with-webhooks#step-4-register-a-new-webhook)
  * [Step 5: Observe the Webhook in Action](https://developer.webex.com/docs/experimenting-with-webhooks#step-5-observe-the-webhook-in-action)
  * [Going further](https://developer.webex.com/docs/experimenting-with-webhooks#going-further)


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
