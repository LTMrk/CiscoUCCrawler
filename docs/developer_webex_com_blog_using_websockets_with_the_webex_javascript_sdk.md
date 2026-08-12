[](https://developer.webex.com/)
[Getting Started](https://developer.webex.com/create/docs)Documentation![](https://developer.webex.com/blog/using-websockets-with-the-webex-javascript-sdk)[AI in Webex](https://developer.webex.com/mcp/docs/webex-mcp-server-overview)Blog![](https://developer.webex.com/blog/using-websockets-with-the-webex-javascript-sdk)[Support](https://developer.webex.com/explore/support)Resources![](https://developer.webex.com/blog/using-websockets-with-the-webex-javascript-sdk)
[Log in](https://developer.webex.com/login)[Sign up](https://developer.webex.com/signup)
# Using Websockets with the Webex JavaScript SDK
August 1, 2025
![Janos Benyovszki](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltf1a11d59afde7c75/617175c0da02001d99f29106/cisco-webex-devs-avatar.png?width=100&height=100&fit=crop)
Janos BenyovszkiSoftware Engineer, Webex for Developers
![Using Websockets with the Webex JavaScript SDK](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blte4bd71f4d740504e/5d8b6c07d6a10e0cc7a9fd20/WebexDevBlog_HowTo_F_R1.jpg?width=900&height=317&fit=crop)
This blog post was originally published in September 2019 and has now been updated for 2025.
Most developers who have created applications for Webex are familiar with the concept of [Webhooks](https://developer.webex.com/docs/api/guides/webhooks). Webhooks are registered on resources like ‘messages’ or ‘memberships’ to notify applications of events on these resources. When the registered event has occurred - for example a message was created or a membership was deleted - an HTTP POST event with a JSON payload is sent and your application can react to it accordingly.
When your application runs as a web server using a publicly-accessible URL, you don’t need to do much else beyond creating a webhook and having an app running at the webhook's `targetUrl` to process the webhook payload. This approach can be a problem though if your app needs to run behind a corporate firewall or in restrictive environments. To get around this problem, we recently introduced functionality in the Webex JavaScript SDK that allows applications to "listen" for Webex messaging events using websockets, a technology that does not require a web server running on a public IP address.
Websockets are persistent connections established over HTTP that allow direct communication between servers (the Webex API in this case) and clients (the Webex JavaScript SDK). In this post, we will walk you through creating and using websockets to listen for events sent from Webex.
### Websocket example
Websockets are not created by sending a POST request to the API like you would to create a webhook. Websockets are created programmatically with the help of the JavaScript SDK, as they're a unique concept that requires additional behind the scenes setup.
Websocket listeners can be created for **memberships** , **rooms** , **messages** , or **attachmentActions**. Each of these resources has a `listen()` method in the JavaScript SDK, which you need to call in order to start your websocket. Once the listener is started, you can specify the type of event you would like to be notified about, by calling the `on()` method. As mentioned earlier, there is no need for a `targetURL`, like you need for a webhook, because the events from the server are not sent via HTTP. Instead, they're routed through the websocket, and any `on()` handlers you have registered for the event are called directly by the SDK.
Applications which use the Webex JavaScript SDK can make use of websockets today! Additionally, support for websockets has been added to the [Node Flint framework](https://www.npmjs.com/package/node-flint).
If your application isn't written in JavaScript, don't worry, you can still take advantage of websockets. In the following sections, we will go through each step of creating a node.js based websocket listener app, built specifically to forward Webex events to another locally running application. In this sample, we will listen for "message:created" events and forward them to a specified localhost/PORT. On the other side of it, we will have a sample Java app listening on localhost/PORT, interpreting the request and sending a reply to the room the message was sent from.
### Requirements
  

#### The node.js app
Before getting started with websockets, make sure you have everything that's needed to get up and running with Node.js and NPM - more information can be found in the [Node.js SDK documentation](https://developer.webex.com/messaging/docs/sdks/node) and the [JavaScript SDK's GitHub repo](https://github.com/webex/webex-js-sdk/blob/master/README.md). Once you have that covered, go the [hookbuster example repo](https://github.com/WebexSamples/hookbuster) and follow the instructions for installation.
#### The Java app
Our app uses Maven to build the project, so you will need that set up before you can run the example. You will also need Java 1.6 or higher installed. Once both are functional, open the [GitHub repo](https://github.com/WebexSamples/javabot) and follow the instructions to install and run it.
#### Everything else
You will also need a bot access token (it's much easier and simpler to test with a bot token vs an integration token accessing your personal data). Even though you won't need the token in the application code itself, it will be necessary later to run the demo. To create one, see our [Bots Guide](https://developer.webex.com/create/docs/bots) and hang onto the access token for now.
### Creating a Websocket listener -- the node.js app
  

#### Step 1: Authentication
Once the node.js app is up and running, per the instructions mentioned in the Github repo earlier, you'll need to provide it with an access token. This will be entered in the console and we need to use it to make the demo functional. The token is then used to initialize a Webex object, which is used to communicate with the Webex API. Here is the code where we retrieve the access token provided in the Console:

```
function _initializeWebex(accessToken) {
    webex = Webex.init({
        config: {
            logger: {
                level: 'error'
            }
        },
        credentials: {
            access_token: accessToken
        }
    });
    webex.once('ready', () => {
        console.log(fonts.info('Webex Initialized'));
    })
}

```

To make sure the access token is valid, we do a call to the Webex API's `/people/me` endpoint:

```
return new Promise((resolve, reject) => {

    webex.people.get('me').then(person => {
        resolve(person);

    }).catch(() => {
            reject('not authenticated');
        }
    );
});

```

We use this call to do the validation because everyone has access to view the "person" associated with the token they're using; it will rarely fail for any other reason besides the access token being invalid.
#### Step 2: Start listening
The app will then ask for a destination and a port that it will use for forwarding the incoming websocket events to via POST request; in our example, we will use port 5000 but you can set that to whichever port you prefer.
After that, we will be prompted to select our resource and event. We will select **messages** and **created** , respectively. This will start the websocket listener and it will then listen for incoming messages. Please note - only messages where our bot is mentioned will be triggered; this is because bots are restricted and can only access messages where the bot is explicitly mentioned. Here is a screenshot showing both steps 1 and 2:
![Hookbuster example](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt32748a2df56c1965/5d8a8f045624367917a5d6e9/websockets-hookbuster-example.png)
This is the node.js code triggered by the above console commands for the resource and event selection:

```
webex.messages.listen().then(() => {

    //logging a formatted info message in the console
    console.log(fonts.info(
        'listener is running for ') +
        fonts.highlight(` ${resource.toUpperCase()}:${event.toUpperCase()} `)
    );

    webex.messages.on(event, request => {

        let request_string = JSON.stringify(request);
        _forwardRequest(request_string);

});


}).catch(reason => {
    console.log(fonts.error(reason));
});

```

#### Step 3: Forward the request
Make sure the Java application for the bot is also running, and then send a simple message to the bot via Webex. Since **'hello'** is all our Java bot is built to understand, we will only send that command. We're sending the test via a group space, but a direct message would work as well:
![Webex message](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt8aacdaa0ea527a9a/5d8a8f03f38cef798fc9fca5/websockets-hookbuster-example-message.png)
As soon as the message is posted, the server triggers a POST request, the same way it would for a webhook. The difference is, instead of a public `targetURL`, the message is sent to our websocket because we registered a listener for all messages created for our bot (we told the system to listen for our bots messages specifically, when we entered our bot access token in the node.js app earlier). Once the message reaches our running code, it is directly forwarded to localhost:5000, as shown below:

```
function _forwardRequest(request) {

    //logging info to the console
    console.log(fonts.info('request received'));

    //gathering some details
    const options = {
        hostname: 'localhost',
        port: specifications.port,
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Content-Length': request.length
        }
    };

    //creating the forward request
    const req = http.request(options, res => {
        console.log(`statusCode: ${res.statusCode}`);
    });

    req.on('error', error => {
        console.log(fonts.error(error.message));
    });

    //sending the request
    req.write(request);
    req.end();

    console.log(fonts.info(`request forwarded to localhost:${specifications.port}`));
    console.log(fonts.info(request));
}

```

![Hookbuster sample output](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt79f9e38b1c5b0196/5d8a8f03f0e07b2dd96a50e8/websockets-hookbuster-sample-message.png)
#### Step 4: Stop listening
This might seem like we're getting a little ahead of ourselves, but it is important to note - if we do not clean up the listener after it is no longer needed, we might run into trouble later. This is why our node.js app stops all listeners once you exit the app. The following code handles the clean up process:

```
webex.messages.stopListening();
webex.messages.off(event);

```

### Listen to incoming request -- the Java bot application
  

#### Step 1: Authentication
Just like our node.js websocket listener app, our [Javabot](https://github.com/WebexSamples/javabot) application needs an access token to function. After you start up the app, it will ask for the token. Here we use the same bot token as before, because we want to post our simple replies with the same identity. After entering the token, it is verified with the below code:

```
private static boolean verifyAccount(String accessToken) {

    boolean isValid = false;
    Bot bot = new Bot(accessToken);

    try {
        Console.printInfo("Verifying account");
        Person me = bot.getMyDetails();
        isValid = true;
        Console.printInfo("Account verified as " + me.getDisplayName().toUpperCase());

    } catch (Exception e) {
        Console.printError("Access token invalid");
    }

    return isValid;
}

```

The verification is done by our Bot object, which is actually a wrapper for the Java SDK's Spark object:

```
public Person getMyDetails() {
    return spark.people().path("/me").get();
}

```

#### Step 2: Start listening
The only other parameter needed for our Java app is a port to listen on. We will use the same 5000 port, that we used with the node.js app.
This is all we need to start listening for incoming requests on localhost:5000. With the parameters gathered and verified, we can now instantiate the socket and begin accepting incoming messages using the following code:

```
public void run() {

    Console.printInfo("Service listening on localhost:" + port);

    try {
        ServerSocket serverSocket = new ServerSocket(port);

        while (true) {

            try {
                //waits for incoming request
                Socket socket = serverSocket.accept();

                JSONObject requestBody = getRequestBodyFromInput(socket);
                evaluateRequest(requestBody);

            } catch (Exception e) {
                Console.printError(e.getMessage());
            }
        }
    } catch (IOException e) {
        //socket already in use
        Console.printError(e.getMessage());
        Console.printError("Service not running");
    }
}

```

Here is a screenshot showing the Console workflow for the above code:
![Javabot example output](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/bltb6d64d1b9edcf18d/5d8a8f0476c2640d16348c44/websockets-javabot-example.png)
#### Step 3: Evaluating the request
Once we receive our "hello" message from the node.js app, the request is interpreted using the below code:

```
private void evaluateRequest(JSONObject requestBody) {

    //print info to the console
    Console.printInfo("Request received");
    Console.printInfo(requestBody.toString());

    String resource = (String) requestBody.get("resource");
    JSONObject data = getDataObjectFromJson(requestBody);
    String roomId = (String) data.get("roomId");

    if (resource.equals("messages")) {
        String messageId = (String) data.get("id");
        Message message = bot.getMessageById(messageId);

        if (!message.getPersonEmail().contains("@webex.bot")) {
            //split the message along spaces
            String[] trimmedMessage = message.getText().split("\\s");
            //convert the message array into a searchable list
            ArrayList<String> messageList = new ArrayList<>(Arrays.asList(trimmedMessage));

            if (messageList.contains("hello")) {
                bot.sayHello(roomId);
            }
        }
    }
}

```

#### Step 4: Sending a reply
The Java SDK includes prebuilt methods we then call to send the actual reply back to the space/room where the original "hello" originated:

```
void sayHello(String roomId) {

    Message message = new Message();
    message.setRoomId(roomId);
    message.setMarkdown("hello there \uD83D\uDC4B" );
    spark.messages().post(message);
}

```

This is how it looks like, back in Webex:
![Webex sample message - hello](https://images.contentstack.io/v3/assets/bltd74e2c7e18c68b20/blt27e5f19e1811ebbd/5d8a8f022d73960d2a506ec3/websockets-javabot-sample-message.png)
If you have any questions, please don't hesitate to contact our [Webex Developer Support team](https://developer.webex.com/support).
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
