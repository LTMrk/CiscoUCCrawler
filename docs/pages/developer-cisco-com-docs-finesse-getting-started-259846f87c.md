---
doc_id: developer-cisco-com-docs-finesse-getting-started-259846f87c
source_url: https://developer.cisco.com/docs/finesse/getting-started/
retrieved_at: 2026-08-25T21:02:13.842524+00:00
---

# Getting started with Cisco Finesse

## Get a Finesse system

Finesse has versions for both Unified Contact Center Enterprise (UCCE) and Unified Contact Center Express (UCCX) . For the common features between the two deployments, the REST API and the JavaScript Library API are the same. Therefore, applications or gadgets developed using the Finesse APIs will work on both deployments.

### I already have a Finesse system

If you already have a working Finesse system, you can skip this section.

### I need a Finesse system

DevNet provides FREE 24 X 7 hosted labs for integrating and working with Cisco technologies such as Cisco Finesse. Finesse is available as a reservation based DevNet Sandboxes for the following deployments:

- Packaged Contact Center Enterprise

- Unified Contact Center Express

Reservation based sandboxes are private preconfigured labs where the resources are dedicated to you for the duration of the reservation. You have the ability to install your own application and share the lab with other users.

The Cisco Finesse sandboxes are installed with premium licenses, which means that all of the APIs and features are available for use.

## Getting started with using the Finesse REST APIs

Cisco Finesse provides robust RESTful APIs for performing agent and supervisor actions programmatically. These REST APIs are easy to use, modeled after HTTP, and works in thick and thin client integrations. The Finesse Developer Guide explains the details for each of the APIs.

The Finesse REST API handles request-response. Alongside the Finesse REST APIs are the Cisco Finesse Notifications. The Finesse notifications are events that are sent to clients who are subscribed to the resource(s). For example, if a client is subscribed to agentA's User notifications and agentA signs in via the Sign In to Finesse REST API request, the client will receive a 200 OK as a response from the REST API request as well as an event to agentA's User notification subscription that the User signed in either successfully or unsuccessfully. Notifications are sent when information in the object (User, Dialog, etc.) changes. For more details about Cisco Finesse Notifications and the supported resources, see the Finesse Developer Guide .

The Finesse REST APIs and notifications can be used to:

- Integrate agent and supervisor actions into existing thick or thin applications

- Build a custom agent and supervisor desktop

- Build a custom gadget for a web application

### Try them out!

The best way to learn about the Finesse REST APIs is to use them and see how easy it is. Before diving into programmatically calling the REST APIs, it is good to get a better understanding of the APIs by trying them out manually using a REST client. There are many REST client tools available, and you can use whichever tool you are most comfortable with, but Postman will be used for the examples on this page.

- Download and install Postman by going to https://www.getpostman.com .

- In Postman, at the upper-right corner, click the wrench icon and choose Settings from the drop-down menu.

- In the Request section, set SSL certificate verification to OFF .

- Dismiss the Settings window by clicking X in the upper-right corner of the window.

Windows : Download and install Pidgin by going to https://www.pidgin.im/download/windows .

- In Pidgin, go to Tools > Plugins to open the Plugins dialog box.

- Check the XMPP Console and XMPP Service Discovery check boxes.

- Add an account for your XMPP server. Go to Pidgin > Accounts > Manage Accounts > Add Account . The Add Account dialog box opens.

- For Protocol, select XMPP .

- For Username, enter the username for an agent.

- For Domain, enter the fully-qualified domain name of the Finesse server.

- For Resource, enter any text.

- For Password, enter the password of the agent.

- Click Save .

- Click the Advanced tab.

- Check the Allow plaintext auth over unencrypted streams check box.

- For Connect Server, enter the IP address of the Finesse server.

- If the Connection Security drop-down menu is present, choose Use encryption if available .

- Click Save .

- The XMPP logo next to the agent's name becomes active (is no longer dimmed). To see event messages in Pidgin, open the XMPP Console.

MacOS : Download and install Adium by going to https://www.adium.im .

- In Adium go to Preferences > Account > '+' > XMPP (Jabber) .

- For Jabber ID, enter the username for the agent followed by '@' along with the fully qualified domain name of the Cisco Finesse server.

- For Password, enter the password of the agent.

- Enable XMPP Advanced Features (Default: Off). To enable the XML Console menu run the following command in Terminal: defaults write com.adiumX.adiumX AMXMPPShowAdvanced -bool YES

- To see event messages in Adium, go to File > Logged in User > XML Console .

### Where do I download a sample web application?

Cisco provides a NonGadgetSampleWithStropheAndWebsocket to demonstrate how to build a web application that uses the Finesse REST APIs and the Finesse notifications. It makes requests to the Finesse server using the Finesse REST APIs and establishes a WebSocket connection to subscribe to and receive Finesse event notifications. You can use any JavaScript XMPP library as long as it meets the XMPP standards. More information on XMPP, including a list of XMPP supported libraries, can be found at https://xmpp.org .

The NonGadgetSample uses the Strophe Library to establish the WebSocket connection to the Finesse server.

Using Finesse REST APIs in a web application requires a proxy to be set up to get around the Cross-domain scripting restrictions of most browsers. Steps to configure the proxy can be found in the NonGadgetSampleWithStropheAndWebsocket download.

The NonGadgetSampleWithStropheAndWebsocket contains a sample web application and a sample httpd.conf file to show how to configure an Apache web server to proxy both the Finesse REST API requests and the BOSH/XMPP connection. The NonGadget sample demonstrates how to:

- Sign in

- Sign out

- Change agent state

- Make a call

- Answer the call

- Hold the call

- Retrieve the call

- End the call

Disclaimer The NonGadgetSample is only a sample and is NOT guaranteed to be bug free and production quality .
It is meant to:

- Serve as an example of the step by step process of building a web page that is not a gadget using the Finesse REST APIs.

- Provided as a guide for a developer to see how to use the Cisco Ajax XMPP Library and jQuery to make Finesse REST API requests and process the Finesse notifications.

## Getting started with your own Finesse Gadgets

Finesse Gadgets are OpenSocial gadgets, which is an XML document that defines metadata for an OpenSocial Gadget container . The gadget includes HTML, JavaScript, and CSS, which essentially makes them mini web pages. Cisco provides a Finesse JavaScript Library API (also referred to as finesse.js) for developers to build Finesse gadgets. This library is a JavaScript wrapper around the Finesse REST APIs and is used in the Finesse out of the box desktop.

Finesse gadgets can be used to:

- Add custom features/functionality that does not exist in the Finesse desktop

- Add existing non-Finesse applications to the Finesse desktop

- Add screen pops to automate browser and database searches

- And many more!

### Try them out!

The best way to learn about Finesse gadgets and the Finesse JavaScript Library API is to build a gadget. Cisco provides sample gadgets and a Finesse JavaScript Library API to use to create your custom gadgets. While gadgets are quite simple, the easiest way to get started is to download a sample gadget , deploy it to the Finesse server, and see it in action!

To learn how to write your own custom gadgets to run in the Finesse desktop, you should start with the Learning Sample Gadget . This gadget was specifically written to walk you through the process of starting with a small skeleton gadget and adding supporting code to demonstrate some of the most common Finesse capabilities. Step by step instructions are included in the Learning Sample Gadget download.

The learning sample gadget uses the Finesse JavaScript Library API and demonstrates how to use the User and Dialog objects. It provides step-by-step instructions on how to instantiate the User and Dialog objects, get User and Dialog data, change the user's state, place a call, and create a screen pop in an iframe by building a url using a Dialog's call variable.

After following the instructions and making the code changes, you will need to host the gadget on either the Finesse server or on an external server. Finesse provides a mechanism for you to upload third-party gadgets (such as the learning sample gadget) to the Finesse server. In order to upload gadget files to the Finesse server, you must set the 3rdpartygadget account's password once by using the CLI utils reset_3rdpartygadget_password . More information about the 3rdpartygadget account can be found in the Finesse Developer Guide .

#### Where do I download more sample gadgets?

Cisco provides a variety of sample gadgets . Each sample gadget contains a document explaining the purpose of the gadget, how to use the gadget, and instructions for modifying the Finesse Desktop Layout in order for the gadget to appear in the Finesse desktop. These gadgets are release specific, so make sure you download the gadget version that matches your Finesse product version.

Disclaimer

The sample gadgets are only samples and is NOT guaranteed to be bug free and production quality . They are meant to:

- Serve as an example of the step by step process of building a gadget using the Finesse JavaScript Library API

- Provided as a guide for a developer to see how to initialize a gadget and set up handlers for User and Dialog updates.

## How do I get help?

### Finesse FAQs

Take a look at the Finesse Frequently Asked Questions to see if your question is already answered.

### Finesse Forums

If you have questions about developing with the Finesse APIs (REST or JavaScript), post your question to the DevNet Finesse forum .

Next