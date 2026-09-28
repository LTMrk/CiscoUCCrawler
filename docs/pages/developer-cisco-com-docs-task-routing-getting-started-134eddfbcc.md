---
doc_id: developer-cisco-com-docs-task-routing-getting-started-134eddfbcc
source_url: https://developer.cisco.com/docs/task-routing/getting-started/
retrieved_at: 2026-08-25T21:02:55.251736+00:00
---

# Getting started with Task Routing APIs

## Get an Enterprise Deployment

Starting with 11.5(1), Task Routing is available with the Enterprise platforms – Packaged CCE, Unified CCE, and Hosted CC.

In order to use the Task Routing APIs, you will need one of the above enterprise deployments as well as Customer Collaboration Platform (CCP) installed and added to the inventory.

### I already have an Enterprise deployment

If you already have an Enterprise deployment with Customer Collaboration Platform installed, then please proceed to the Getting started with using the Task Routing APIs section.

If you have an Enterprise deployment, but need to install the Customer Collaboration Platform, please refer to the Cisco Customer Collaboration Platform Installation and Upgrade Guide . Then add Customer Collaboration Platform to the inventory by following the Add Customer Collaboration Platform as an External Machine section of the Enterprise features guide.

### I need an Enterprise deployment

DevNet provides FREE 24 X 7 hosted labs for integrating and working with Cisco technologies such as PCCE. The Task Routing APIs are available in the reservation based Packaged Contact Center Enterprise DevNet Sandbox .

Reservation based sandboxes are private preconfigured lab with all resources dedicated to you for the duration of the reservation. You have the ability to install your own application and share the lab with other users.

## Getting started with using the Task Routing APIs

Task Routing APIs are a set of RESTful APIs , which enables task injection and their handling programmatically. These REST APIs are easy to use, modeled after HTTP, and works in thick and thin client integrations. Details of these APIs can be found in the:

- Task creation (injection)

- Task status query, cancellation

- Agent login/logout, ready/not-ready state

- Task accept, pause/resume, complete, transfer

The APIs for Task Routing work alongside other APIs from the respective products and also their XMPP Notification mechanisms.

XMPP Notifications are a more efficient mechanism where simple API based polling does not suffice. These notifications are events that are sent to client(s) who are subscribed to the resource(s).

As an example, the customer side application would need information of an injected task like its queued status, expected wait time in queue, or assigned agent. This can be achieved in two ways:

- By periodically polling the status of the Task object.

- By subscribing to the Customer Collaboration Platform Task change events.

The notification mechanism is evidently more efficient where volumes are more than minimal.

Similarly, on the Finesse side, if a client is subscribed to agentA's User notifications and AgentA signs in via the Sign-In to Finesse REST API request, the client will receive a 200 OK as a response from the REST API request as well as an event to AgentA's User notification subscription notifying that the User signed in successfully or unsuccessfully. Notifications are sent when information in the object (User, Dialog, etc.) changes. For more details about Cisco Finesse Notifications and the supported resources, see the Finesse Developer Guide .

Besides the Task Routing APIs, other APIs from the underlying Enterprise platforms can also be made use of as the integration might necessitate. Please visit the below links for additional information on the allied APIs and SDKs, which are all available via Cisco DevNet .

- Customer Collaboration Platform

- Finesse

- Packaged Contact Center Enterprise

### Try them out!

The best way to learn about the Task Routing APIs is to use them and see how easy it is. Before diving into programmatically calling the REST APIs, it is good to get a better understanding of the APIs by trying them out manually using a REST client. There are many REST client tools available, and you can use whichever tool you are most comfortable with, but Postman will be used for the examples on this page.

Install a REST client :

- Download and install Postman by going to https://www.postman.com .

- In Postman, at the upper-right corner, click the wrench icon and choose Settings from the drop-down menu.

- In the Request section, set SSL certificate verification to OFF .

- Dismiss the Settings window by clicking X in the upper-right corner of the window.

Install a XMPP client :

Windows : Download and install Pidgin by going to https://pidgin.im/install .

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

MacOS : Download and install Adium by going to http://www.adium.im .

- In Adium go to Preferences > Account > '+' > XMPP (Jabber) .

- For Jabber ID, enter the username for the agent followed by '@' along with the fully qualified domain name of the Cisco Finesse server.

- For Password, enter the password of the agent.

- Enable XMPP Advanced Features (Default: Off). To enable the XML Console menu run the following command in Terminal: defaults write com.adiumX.adiumX AMXMPPShowAdvanced -bool YES

- To see event messages in Adium, go to File > Logged in User > XML Console .

As a prerequisite to creating a task using the Task Creation REST API , you need the Task Feed Id. Use the List Feed REST API to get a list of Feeds in the system:

- Open Postman to make the REST API requests.

- In the field marked Enter request URL here , put the URL: http://<server>:<port>/ccp-webapp/ccp/feed?summary=false where <server>:<port> is the FQDN and port of the Customer Collaboration Platform.

- From the request method dropdown menu, select GET .

- Select the Authorization tab, and select Basic Auth . A form containing username and password fields appear.

- For the Basic Auth username value, enter the Administrator's username

- For the Basic Auth password value, enter the Administrator's password

- Click the Update request button to generate an authorization header.

- Click the Send button to launch the request.

- If the request is successful, you should see a HTTP status of 202 OK. The response body should list out the different Feeds that are in the system. Look for a Feed with with the tag of cisco_task_tag

- Copy the value in the <pushFeedURL> . This will be the url of the Task Creation REST API. The numeric number at the end of the URL is the Task Feed Id.

Another prerequisite for creating a task is to get the scriptSelector (dialed number string).

- On your browser, go to the U/PCCE Administration page: https://<U/PCCE FQDN>/cceadmin

- Log in with the U/PCCE administrator username/password.

- Navigate to Manage > Dialed Number

- Copy down one of the "Dialed Number String" that has a Call Type of "TaskCallType". This will be the Task queue the task will be sent to.

- If a script with a call type of "TaskCallType" is not listed, follow the configuration steps to create the script selector.

Now, we are ready to call the Task Creation REST API . Open a new tab in Postman and build the Task Creation REST API request:

In the field marked Enter request URL here , put the value of the <pushFeedURL> that you had copied from the Feed List response.

From the request method dropdown menu, select POST .

Select the Body tab, and select the raw radio button. A dropdown menu containing the type of raw data appears.

Select XML (application/xml) from the dropdown menu.

In the large body text box, put the following XML data, where the value of the scriptSelector is the "Dialed Number String" you had copied from the U/PCCE Administration page:

xml

```
< Task > < name > John Doe </ name > < title > Help with my phone </ title > < description > This is my description </ description > < scriptSelector > xxxxxxx </ scriptSelector > < requeueOnRecovery > true </ requeueOnRecovery > < tags > < tag > phone </ tag > < tag > error </ tag > </ tags > </ Task >
```

Click the Send button to launch the request.

If the request is successful, you should see a HTTP status of 201 Created and an empty body text box.

Congratulations! You have made your first Task Routing REST API request! You can find additional Task Routing REST APIs by looking at the Task Routing Developer Guide .

### Where do I download sample code?

Cisco provides sample code to demonstrate how to build the various parts of an application that uses Task Routing APIs. These are available in the “Find sample code and scripts” section of the DevNet Task Routing page. Each sample is accompanied with ReadMe files. Please refer back to the sample code section as more samples will be added.

To see some of the sample code in use, the Packaged Contact Center Enterprise sandbox is already configured for Task Routing. It includes a Customer Collaboration Platform form to create/inject Tasks and a sample Finesse gadget to handle tasks.

Disclaimer

Note that the sample code is available as is and is NOT guaranteed to be bug free and production quality . They are meant to serve as an example of the step by step process of building the functionality as described.

## How do I get help?

### Task Routing Forum

The DevNet Task Routing forum is the place for you to:

- post your questions to the community backed by Cisco engineers

- engage, collaborate, share with fellow experts

### DevNet Support

If you have a DevNet support contract, you can open a developer support ticket for one-on-one assistance from a DevNet engineer.

Next