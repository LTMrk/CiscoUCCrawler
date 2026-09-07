---
doc_id: developer-cisco-com-docs-finesse-managing-notifications-in-third-party-applications-64a135a0ab
source_url: https://developer.cisco.com/docs/finesse/managing-notifications-in-third-party-applications/
retrieved_at: 2026-09-07T14:07:37.211799+00:00
---

# Managing Notifications in Third-Party Applications

For applications that aren’t gadgets in the Cisco Finesse Desktop or in a third-party OpenSocial container, use one of the following methods to establish a connection with the Cisco Finesse Notification Service to subscribe to XMPP events:

Any client-side XMPP library that supports WebSockets such as Strophe.js using the port 8445.

Cisco Finesse Desktop EventTunnel (for browser applications only)

XMPP over TCP based on Smack over port 5222 or 5223 (TLS)

Finesse uses the following base XMPP features:

session establishment

presence

roster management

These are supported over BOSH (http-bind)/WebSocket/smack protocols.

In addition, the only XMPP extension feature supported is (XEP-0060) Pubsub.XMPP extensions natively supported by Openfire. For example, (XEP – 0198) Stream management, (XEP-0163) PEP, (XEP-0256) Last Activity, aren’t used by Finesse and wherever possible are disabled. Custom clients should ensure that only supported features are used when interacting with OpenFire.

Finesse by default uses WebSocket to connect to Cisco Finesse Notification Service. For better performance, third-party XMPP clients should connect to the Cisco Finesse Notification Service over WebSocket.

For all types of connection methods, Cisco Finesse Notification Service expects XMPP client ping every 20 seconds.

This section describes how to use the Cisco Finesse Desktop EventTunnel method. This method requires knowledge of how to use postMessage to pass messages between different frames in the browser.

The EventTunnel.js file is located at https://<hostname>:<port>/tunnel/EventTunnel.js (the hostname is of the Cisco Finesse server and the port is 8445 or 7443 for HTTPS). This class is designed to be loaded within an iframe . This class loads in the browser application and uses postMessage to communicate between frames.

Access BOSH and WebSockets as follows:

BOSH: https://<hostname>:<port>/http-bind

WebSocket: ws(s)://<hostname>:<port>/ws

Cisco Finesse, Release 12.5(1) onward, the 7071 port (BOSH/WebSocket for HTTP) is disabled by default. Use the utils finesse set_property webservices enableInsecureOpenfirePort true command to enable this port.

For more information, see the Service Properties section in the Cisco Finesse Administration Guide .

Using the EventTunnel, the application can perform the following operations:

Establish the XMPP connection

Subscribe to XMPP nodes

Unsubscribe from XMPP nodes

The following is a sample file that you can use to instantiate and initialize the EventTunnel in the iframe:

Code Snippet

```
<! DOCTYPE HTML > < html > < head > < meta http-equiv = " Content-Type " content = " text/html; charset=UTF-8 " /> < meta http-equiv = " X-UA-Compatible " content = " IE=edge " /> < script type = " text/javascript " > //Set the JabberWerx connect to unsecure because the custom authentication //on the XMPP server does not support encrypted credentials. var jabberwerx_config = { unsecureAllowed : true } ; < script type = "text/javascript" > //Set the JabberWerx connect to unsecure because the custom authentication //on the XMPP server does not support encrypted credentials. var jabberwerx_config = { unsecureAllowed : true } ; </ script > < script type = " text/javascript " src = " thirdparty/jquery/jquery-1.5.min.js " > </ script > < script type = " text/javascript " src = " thirdparty/strophe/strophe.js " > </ script > < script type = " text/javascript " src = " thirdparty/strophe/strophe.pubsub.min.js " > </ script > < script type = " text/javascript " src = " thirdparty/util/converter.js " > </ script > < script type = " text/javascript " src = " EventTunnel.js " > </ script > < script type = " text/javascript " > jQuery ( document ) . ready ( function ( ) { var tunnel = new finesse . EventTunnel ( ) ; tunnel . init ( ) ; } ) ; </ script > </ head > </ html >
```

| Note | Finesse by default uses WebSocket to connect to Cisco Finesse Notification Service. For better performance, third-party XMPP clients should connect to the Cisco Finesse Notification Service over WebSocket. For all types of connection methods, Cisco Finesse Notification Service expects XMPP client ping every 20 seconds. |
|---|---|

| Note | Cisco Finesse, Release 12.5(1) onward, the 7071 port (BOSH/WebSocket for HTTP) is disabled by default. Use the utils finesse set_property webservices enableInsecureOpenfirePort true command to enable this port. For more information, see the Service Properties section in the Cisco Finesse Administration Guide . |
|---|---|