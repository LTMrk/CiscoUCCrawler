---
doc_id: developer-cisco-com-docs-finesse-connect-to-xmpp-over-http-boshwebsocket-using-finesse-eventtunnel-248651dc59
source_url: https://developer.cisco.com/docs/finesse/connect-to-xmpp-over-http-boshwebsocket-using-finesse-eventtunnel/
retrieved_at: 2026-09-07T14:07:46.176923+00:00
---

# Connect to XMPP over HTTP (BOSH/WebSocket) using Finesse EventTunnel

To initialize the
		  XMPP connection, the following information must be passed to the EventTunnel
		  before it can proceed:

Agent ID

XMPP Domain

Agent Password

XMPP PubSub
				Domain

Agent XMPP
				Resource (Optional)

The postMessage
		  payload has the following message structure:

where type is a
		  number that has the following mapping:

CONNECT_REQ

10

Attempt to establish a WebSocket connection with the XMPP server using Strophe. The message should be an XML string that outlines a connInfo object, which includes the id, password, and xmppDomain elements.

NOTIFICATION_CONNECTION_TYPE

12

Notification Service connection type used for XMPP requests.

Possible values: bosh, websocket

Default value: websocket

LOGGING

13

Logs the message.

SUBSCRIPTIONS_REQ

14

Retrieves the list of subscriptions to other nodes.

Code Snippet

```
* @return
* JSON Array with objects like below:
 {
       "node": "/finesse/api/User/1001050/Media",
       "jid": " < userid > @ < host > ",
       "status": "subscribed"
 }
```

XMPP_DISCONNECT_PROPERTIES

15

Configures a set of XMPP properties, such as xmppRequestTimeout, xmppFailoverDetectionPingInterval, and xmppFailoverRequestMaxRetry. The message should be a JSON stringified object containing these properties.

Example:

Code Snippet

```
var xmppProperties = JSON.stringify({

    xmppRequestTimeout: '10000',

    xmppFailoverDetectionPingInterval: '10000',

    xmppFailoverRequestMaxRetry: '2'

});
```

FINESSE_CONTAINER_CONFIG

16

Sends Finesse configuration properties to the tunnel. Currently, this is used solely for the enableConsoleTraceLogging property. The message should be a JSON stringified object containing the enableConsoleTraceLogging property. If this property is not specified, it defaults to 'false'.

For example, a
		  postMessage call to send the agent ID is as follows:

Code Snippet

```
message = "1|1001001"                               // 1 - type: ID, 1001001 - agent ID
tunnelFrame.postMessage(message, tunnelOrigin);     // where tunnelFrame is the frame
                                                    // corresponding to the iframe hosting
                                                    // the EventTunnel and tunnelOrigin is
                                                    // the URL of the EventTunnel i.e.
                                                    // http:// < host > : < port > where host is
                                                    // the host of the Cisco Finesse
                                                    // server and port is the port of
                                                    // the Cisco Finesse Notification
                                                    // Service, either 7071 for http or 
                                                    // 7443 for https
```

Be sure to also
		  wire up a callback to receive messages using postMessage from the EventTunnel
		  frame, for example:

Code Snippet

```
if (window.addEventListener) { //Firefox, Opera, Chrome, Safari
    window.addEventListener("message", cb, false);
} else { //Internet Explorer
    window.attachEvent("onmessage", cb);
}
```

where cb is the
		  callback that handles any messages received using postMessage and that can
		  parse the messages sent by the EventTunnel.

| Message Type | Value | Description |
|---|---|---|
| EVENT | 0 | XMPP
					 events received by the EventTunnel and published out to the parent frame |
| ID | 1 | Agent
					 XMPP ID |
| PASSWORD | 2 | Agent
					 XMPP password |
| RESOURCEID | 3 | Agent
					 XMPP resource |
| STATUS | 4 | Status of the XMPP connection published by the EventTunnel |
| XMPPDOMAIN | 5 | Domain of the XMPP service |
| PUBSUBDOMAIN | 6 | PubSub domain of the XMPP service |
| SUBSCRIBE | 7 | Request to subscribe to an XMPP node |
| UNSUBSCRIBE | 8 | Request to unsubscribe form an XMPP node |
| PRESENCE | 9 | Request to subscribe to XMPP presence |
| CONNECT_REQ | 10 | Attempt to establish a WebSocket connection with the XMPP server using Strophe. The message should be an XML string that outlines a connInfo object, which includes the id, password, and xmppDomain elements. |
| DISCONNECT_REQ | 11 | Request to disconnect the XMPP connection. This request attempts
					 to unsubscribe the application from all nodes to which it subscribed during the
					 session and then disconnects the session. |
| NOTIFICATION_CONNECTION_TYPE | 12 | Notification Service connection type used for XMPP requests. Possible values: bosh, websocket Default value: websocket |
| LOGGING | 13 | Logs the message. |
| SUBSCRIPTIONS_REQ | 14 | Retrieves the list of subscriptions to other nodes. Code Snippet * @return
* JSON Array with objects like below:
 {
       "node": "/finesse/api/User/1001050/Media",
       "jid": " < userid > @ < host > ",
       "status": "subscribed"
 } |
| XMPP_DISCONNECT_PROPERTIES | 15 | Configures a set of XMPP properties, such as xmppRequestTimeout, xmppFailoverDetectionPingInterval, and xmppFailoverRequestMaxRetry. The message should be a JSON stringified object containing these properties. Example: Code Snippet var xmppProperties = JSON.stringify({

    xmppRequestTimeout: '10000',

    xmppFailoverDetectionPingInterval: '10000',

    xmppFailoverRequestMaxRetry: '2'

}); |
| FINESSE_CONTAINER_CONFIG | 16 | Sends Finesse configuration properties to the tunnel. Currently, this is used solely for the enableConsoleTraceLogging property. The message should be a JSON stringified object containing the enableConsoleTraceLogging property. If this property is not specified, it defaults to 'false'. |