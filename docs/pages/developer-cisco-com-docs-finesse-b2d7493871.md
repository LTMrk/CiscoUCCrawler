---
doc_id: developer-cisco-com-docs-finesse-b2d7493871
source_url: https://developer.cisco.com/docs/finesse/
retrieved_at: 2026-08-24T22:12:18.275281+00:00
---

# What is Finesse?

Cisco Finesse is a next-generation agent and supervisor desktop designed to provide a collaborative experience for the various communities that interact with your customer service organization. It also helps improve the customer experience while offering a user-centric design to enhance customer care representative satisfaction.

For IT professionals, Cisco Finesse offers transparent integration with the Cisco Collaboration portfolio. It is standards compliant and offers low cost customization of the agent and supervisor desktops.

Cisco Finesse provides:

- An agent and supervisor desktop that integrates traditional contact center functions into a thin-client desktop.

- A 100 percent browser-based desktop implemented through a web 2.0 interface; no client-side installations required.

- A single, customizable "cockpit", or interface, that gives customer care providers quick and easy access to multiple assets and information sources.

- Open web 2.0 APIs that simplify the development and integration of value-added applications and minimize the need for detailed desktop development expertise.

Cisco Finesse is built to provide the optimal user experience for agents. The key tenets of the Finesse approach are:

- OpenSocial Gadget Container : Agents use multiple applications, often at the same time. The ideal agent user experience supports this way of working. This is accomplished in Finesse via the gadget container. Each application that an agent uses is delivered as a gadget within a single UI framework. Gadgets can communicate with one another as well as backend servers, allowing for a seamless user experience throughout the call.

- Easy-to-use REST API : The easier the API is to use, the lower the cost of developing applications. This means that customers are more likely to want customized agent desktop experiences. Finesse includes a robust REST API for you to create your own applications or gadgets.

- Browser-based Agent Desktop : Finesse is a web application. Customers install Finesse on a server and agents point their browser to Finesse. It's that easy. Finesse doesn't use browser plug-ins, JRE's, or anything else on the client machine that needs to be installed or maintained. This means customers have more flexibility in how and when they roll out updates to the agent desktop. When the tools don't match the business requirements, productivity suffers and this is what we are trying to avoid by using a browser-based approach.

Finesse has versions for both Unified Contact Center Enterprise (UCCE) and Unified Contact Center Express (UCCX) . For the common features between the two deployments, the REST API and the JavaScript Library API are the same. Therefore, applications or gadgets developed using the Finesse APIs will work on both deployments.

## What Are The Business Benefits?

- Customer help time decreases as a result of the Cisco Finesse desktop providing a single, customizable cockpit that enables your customer care representatives to take advantage of multiple assets and information sources to assist customers. Fast, efficient, accurate service results in happy, satisfied, and loyal customers who will return to do business with you again.

- No client-side installations are required since Finesse is 100% browser based.

- Add applications to the Cisco Finesse desktop remotely with a click of a few buttons.

- Iterative approach of making changes to desktop. Applications do not need to be upgraded at the same time and upgrades are automatically reflected on the Cisco Finesse desktop.

- Cisco Finesse is customizable, which simplifies the development and integration of value-added applications and minimize the need for detailed desktop development expertise. The Cisco Finesse solution meets this challenge by creating a personalized desktop work environment using a web-based interface. And it saves operational costs for your business.

For more information about the Finesse product, see https://www.cisco.com/c/en/us/products/contact-center/finesse/index.html

# Technical Overview

## Finesse Architecture in Unified Contact Center Enterprise Deployments

The above diagram shows the relationships between the various components and services between the client, Finesse, and UCCE in an enterprise deployment. There are other components and services that are not shown since they are not of direct relevance. The legend below the diagram depicts the various protocols used in this deployment.

### Finesse Server

#### Cisco Finesse Tomcat

Finesse consists of the following set of web applications that is hosted on its own Tomcat instance, called Cisco Finesse Tomcat:

- WebProxy : the proxy server that performs SSL termination and forwards all requests to the Cisco Tomcat server over HTTP. It also provides caching services.

- finesse : the REST API web application that services the Finesse desktop, third-party applications and gadgets. In addition, it is a CTI client to UCCE.

- desktop : the agent and supervisor desktop web application.

- cfadmin : the Finesse Administration web application.

- 3rdpartygadget : A repository for third-party gadgets.

The Shindig web application from Apache serves the gadget container running on the Finesse desktop. This is a third-party component based on the OpenSocial Gadget specification.

The CCE Realm is an in-memory component that caches credentials and user information for authentication purposes.

#### Cisco Finesse Notification Service

Cisco Finesse Notification Service is an instance of an OpenFire server , running as a separate process on the platform, that provides event notification from the Finesse server to any client that is subscribed to that resource. The Finesse Tomcat server communicates the events that need to be dispatched to the client via XMPP messages to the OpenFire server.

For web applications, a WebSocket channel should be opened to the OpenFire server, which is used to dispatch events from the OpenFire server to the browser.

Please see the Cisco Finesse Notification Service section below for more details.

#### A Cisco DB

A Cisco DB is an Informix relational data service provided by the VOS platform that is used by Finesse for storing its configuration data.

### UCCE

- Agent PG Finesse functions as a CTI client to the CTI server hosted in the Agent PG (peripheral gateway) component of UCCE to request agent and call state changes, as well as to receive asynchronous notifications on agents, calls, queues, and teams. The Finesse to UCCE CTI interface is critical to the operation of Finesse, as all agent (User) and call/task (Dialog's in API parlance) control is initiated and responded to via this interface. In summary, all user and dialog state transitions seen on the agent desktop are a result of the events and notifications communicated to Finesse server via this interface.

#### Agent PG

- AWDB Finesse interacts with AWDB in UCCE via the JDBC protocol, primarily to authenticate users in non-SSO mode and to look up UCCE configuration parameters in certain deployments.

#### AWDB

### UCM

The Unified Communications Manager (UCM) interface is also shown in the above diagram as it provides telephony controls between UCCE and UCM via the JTAPI protocol.

### Finesse Deployment

The above diagram shows the standard deployment of Finesse servers in Enterprise deployments.

The Finesse server is always deployed as a 2-node pair in Enterprise deployments, with each node in the pair configured with the addresses of the PG pair in UCCE that is hosting the CTI service. At any instant in time, both nodes of the Finesse cluster connect to the same side of the PG (either Site A or Site B). It is not possible for the 2 nodes of the Finesse cluster to connect to separate instances of the PG. If the CTI server encounters runtime failures or does not initialize properly, the standby PG will become active. This will cause the Finesse cluster to fail over to the newly active PG. Finesse servers will automatically fail over to the active PG if there are connection failures during initialization or during runtime.

A Finesse desktop client can be instantiated off either one of the Finesse servers. The servers always operate in active-active mode in Enterprise deployments and keep their internal user and dialog state in sync via the events received via the CTI interface. Clients obtain information about both the servers in the Finesse cluster, and monitor the status of the servers throughout the lifetime of the client session. Clients can dynamically initiate failover to the other server and recover their state if they detect connectivity or server issues with the server they are currently connected to.

## Finesse Architecture in Unified Contact Center Express Deployments

In Express deployments, the internal architecture of Finesse is identical to that of Enterprise deployments, except that Finesse does not run on a distinct VM/server. The Cisco Finesse Tomcat service, which hosts all of the web applications delivering Finesse functionality, runs as a co-resident service on the UCCX VM. The Finesse web application still functions as a CTI client to the CTI server that is now hosted on the UCCX engine in the same VM. The OpenFire server that is used to dispatch events to the browser is renamed as the Cisco Unified CCX Notification Service, but provides the same functionality as in Enterprise deployments from the Finesse perspective. However, it is shared with other applications hosted on UCCX.

In Express deployments, user authentication is done via the AXL interface provided by Unified Communications Manager, as user identity and profile information are managed by the UCM. UCM, in turn, may interface with a Microsoft Active Directory server for user management. Therefore, the caching realm for user identity information in this case is a different implementation as compared to Enterprise deployments.

### Finesse Deployment

The above diagram shows the standard deployment of Finesse in Express deployments.

Starting Finesse 11.6(1), Finesse follows an active-active deployment model. At any instant in time, both nodes of the Finesse cluster connect to the same active CCX engine. If a CTI connection failure is detected, that means that the CCX engine is failing over, so both nodes of the Finesse cluster will fail over as well so that it can be connected to the new active CCX engine.

A Finesse desktop client can be instantiated off either one of the Finesse servers. Clients obtain information about both the servers in the Finesse cluster, and monitor the status of the servers throughout the lifetime of the client session. Clients can dynamically initiate failover to the other server and recover their state if they detect connectivity or server issues with the server they are currently connected to.

For Finesse 11.5(1) and below, Finesse mirrors the UCCX active-inactive deployment model. Finesse is active only on the node where CCX engine is Master, and follows the engine mastership. Users can log in only to the Finesse server that is currently active. If they attempt to log in to the inactive Finesse server, they will be automatically redirected back to the active Finesse server. Each Finesse server in this model connects only to its own local CTI server instance. UCCX ensures that CTI server is active and allows client connections only on the node where CCX engine is the master.

## Finesse REST APIs

Cisco Finesse provides REST APIs for performing agent and supervisor actions programmatically. These REST APIs are easy to use, modeled after HTTP, and works in thick and thin client integrations. The Finesse Developer Guide explains the details for each of the API's, but here is a high-level description of the API functionality:

- Get User Details

- Change User state (e.g. Sign In, Sign Out, Ready, Not Ready, etc.)

- Get User's Dialogs

- Get Dialog Details

- Make a call

- Take action on a participant (e.g. Answer, Hold, Retrieve, etc.)

- Take action on a call (e.g. Update call variables, DTMF, Consult, Single Step Transfer, etc.)

- Take a supervisor action on a call (e.g. Silent Monitor, Barge, Start recording, etc.)

- Make outbound related actions (e.g. Accept, close, Reject, Reclassify, Schedule, Cancel, etc.)

- Get Media Details

- Change User state for a MRD (e.g. Sign In, Sign Out, Ready, Not Ready)

- Change User to Routable/Not Routable

- Get List of non-voice Media Routing Domains for a User

- Get Queue Details

- Get List of Queues for a User

- Get Team Details

- Get Reason Codes (Not Ready, Logout, Wrap Up)

- Get User Media Properties Layout

- Get Phonebooks

- Get Workflows

- System Details (e.g. XMPP Server, PubSub Domains, Node IP Addresses, Status, Deployment Type, etc.)

- Send Client logs to the Finesse server

## Cisco Finesse Notification Service

Cisco Finesse Notification service is an instance of OpenFire server , running as a separate process on the platform, that uses XMPP protocol as the data communication channel and encoding mechanism for dispatching user and dialog events to the client via a seemingly asynchronously. Events to be notified to the client from the Finesse Tomcat service are dispatched to OpenFire via the Smack client library using XMPP as the data communication channel.

For web applications, in order to send the events to the browser, which communicates only via the HTTP protocol, the XMPP payload needs to be encapsulated within the HTTP protocol. There are two options for this:

- WebSocket

- BOSH (deprecated starting Finesse 12.6(1))

The Finesse desktop uses the Strophe.js XMPP Library, but any compatible XMPP JavaScript library can be used by other web based clients. The advantage of using WebSocket and BOSH to communicate to the OpenFire Server in a browser environment is that it uses the browser's native communication channel (HTTP) and no other ports need to be opened in the firewall between browser and server.

Gadgets that are built to run on the Finesse desktop don't have to worry about the details of the WebSocket/BOSH communication channel as this is already setup by the Finesse desktop container before the gadgets get loaded. The events are made available to the gadgets via the Cisco OpenAjax Hub, which implements a publish-subscribe mechanism in the browser. The OpenAjax hub can be used by gadgets to communicate with each other in a purely asynchronous manner (Please see the Finesse out-of-the-box Desktop section below for more details).

Third party web applications that run inside a browser context and make use of the Finesse APIs need to setup a WebSocket channel to the Finesse Notification service for the reasons mentioned above. The details of setting up a WebSocket connection using third-party JavaScript libraries can be found in the Finesse Developer Guide .

Third party applications that run as traditional thick clients (Java, Python clients, etc.) can use XMPP directly to the Finesse Notification service for asynchronous reception of events. Examples of using XMPP directly can be found in the Finesse Developer Guide .

### WebSocket

WebSocket is a low overhead communication protocol that enables interaction between a web browser and a web server. Unlike HTTP, WebSockets are stateful (i.e. the connections are persistent - kept alive until either client or server decides to drop it) and is bi-directional. WebSocket connections are established like regular HTTP connections, but using a ws:// or a wss:// URI. The server handshake upgrades the connection to WebSocket protocol and it is treated like a regular TCP connection after this initial handshake. WebSocket connections have lower overhead for its communications since HTTP headers and cookies are avoided. The persistent nature and lower overhead contribute to lower latencies for real time events over WebSockets. This makes it ideal for Finesse Desktop’s real-time notifications and is the preferred/default client protocol for providing real time events from OpenFire. All major browsers support WebSockets.

### BOSH

Bi-directional streams Over Synchronous HTTP, BOSH , is a legacy transport protocol that is used to simulate a real time asynchronous connection between the HTTP client and server.

Since HTTP is a request-response protocol, the BOSH client in the browser works by sending a HTTP request to the BOSH server (OpenFire) asking for any outstanding events. If there are no events to send, the request is kept pending for a certain period of time instead of returning immediately with an error or an empty payload. If events arrive at OpenFire from Finesse during this time, it is sent as a HTTP response to the pending HTTP request. The BOSH client receives these events and immediately fires the next HTTP request to OpenFire for the next set of events. If, on the other hand, the timer expires before any events are available to be dispatched, a HTTP response with a heartbeat message is sent back to indicate the liveness of the OpenFire server to the client. This explains why the event dispatch from the Finesse server to the browser appears to happen in a "seemingly asynchronous manner".

NOTE: BOSH is deprecated starting Finesse 12.6(1). Applications should use WebSocket.

## Finesse out-of-the-box Desktop

The Finesse desktop is an implementation of the OpenSocial Gadget framework ( Shindig ) that serves as a container for hosting OpenSocial gadgets. The container has been significantly enhanced to provide the infrastructure required for communicating with Finesse Notification service via WebSockt/BOSH/XMPP, so that gadgets (whether Cisco or third-party) hosted on the desktop do not have to deal with the intricacies of the WebSocket/BOSH connection setup. The events published via the WebSocket/BOSH tunnel are made available to all gadgets via the publish-subscribe mechanism implemented by the Cisco OpenAjax Hub, which is a JavaScript library.

## Cisco Finesse Gadgets & Finesse JavaScript Library API

Finesse Gadgets are OpenSocial gadgets, which is an XML document that defines metadata for an OpenSocial Gadget container . The gadgets are essentially mini web pages or applications that are placed within the Finesse desktop. This approach is particularly useful for contact center agents because this gives them access to all of the applications that they need to service calls inside of a single application, Cisco Finesse.

Finesse comes with a couple of out of the box gadgets such as the team performance gadget, but often times, customers have specific requirements that are not available on the Finesse desktop. To alleviate that problem, Cisco Finesse provides a Finesse JavaScript Library API to make it easy to build custom gadgets.

There are many sample gadgets available for developers to use as an example and base for their custom gadgets.

Third party gadgets can be hosted on either the Finesse server (via the 3rdpartygadget web application) or on an external web server. Gadgets can also make REST requests to services hosted on external servers using the Finesse JavaScript Library API . To avoid browser cross-origin issues, it is recommended for the third-party server to be configured to allow CORS requests from the Finesse domain by configuring a CA signed certificate or a pre-imported X.509 certificate. This will allow the gadget to directly call a third-party REST API. It is the responsibility of third-party gadgets to implement their own authentication mechanisms for third-party REST services. Third party servers typically use the desktop agent credentials to authenticate the gadget requests by invoking Finesse User GET API requests to authenticate the credentials. Third party servers can also perform a custom database lookup to authenticate CCE agent credentials if they have the access to the AWDB database. Custom authentication mechanisms can also be used if necessary by configuring the gadgets with the required credentials.

# What can a developer do with Finesse?

Finesse is built for developers. It provides two types of APIs:

- REST APIs : These APIs can be used to build custom applications and/or integrate into existing applications. Documentation can be found in the Finesse Developers Guide .

- JavaScript Library APIs : These APIs can be used to build custom gadgets to be added to the Finesse out of the box desktop. Documentation can be found in the Finesse JavaScript Library API JS doc or on the Finesse server at the following URL: http(s)://<FQDN>:<port>/desktop/assets/js/doc/index.html

There are three paths for customization:

- Integrate Finesse into your existing application (whether it is a thick or thin client)

- Create a completely custom agent desktop

- Use the Finesse JavaScript Library API to create gadgets to be added to the Finesse out of the box agent desktop.

- Create gadgets of existing applications to be added to the Finesse out of the box agent desktop without using any Finesse specific APIs.

# Next Steps

The best way to really understand Cisco Finesse is to try it for yourself. Please proceed to the Getting Started page to learn just how easy it is.

Next