---
doc_id: developer-cisco-com-site-im-and-presence-discover-api-overviews-presence-web-service-0f3b2a6e8c
source_url: https://developer.cisco.com/site/im-and-presence/discover/api_overviews/presence_web_service/
retrieved_at: 2026-09-01T17:45:51.871429+00:00
---

# Cisco Unified Presence Guides

The Presence Web Service is an open interface that allows third party applications to share user presence information with Cisco Unified Presence. This interface is used by developers to build third party applications that can send and receive user presence state updates.

The Presence Web Service supports the exchange of user presence information from a Cisco Unified Presence node using the following interfaces:

- SOAP Interface -- This interface, based on the Simple Object Access Protocol (SOAP), passes
                            XML request and response messages. A third party application sends a SOAP request; the web
                            service processes the request and sends a response.

- REST Interface -- This REST interface, short for Representational State Transfer, passes XML
                            data over HTTP. The data is transferred using a HTTP query parameter or by putting XML in
                            the message body.

The Presence Web Service sends all messages securely over HTTPS; it can also be accessed over HTTP.

The Presence Web Service is available over the following ports:

- over HTTPS on port 8083 (SOAP and REST)

- over HTTP on port 8082 (SOAP and REST)

All SOAP requests for the Presence Web Service must be sent to the following URL:

http://<cuphost>:<port>/presence-service/soap

All REST requests for the Presence Web Service must be sent to the following URL:

http://<cup_host>:<cup_port>/presence-service

## Login and Authentication

A third party application logs in to Cisco Unified Presence as an application user using a valid username and password. On successful login, the application user is passed a unique session key from Cisco Unified Presence.

A registered application user can log in multiple end users of the third party application to Cisco Unified Presence. An application user logs in an end user by passing the session key of the application user and the username of the end user; a unique session key for the end user is returned. This login method is authenticated only if the session key that is passed back belongs to an application user, and the username of the end user is configured in the database on Cisco Unified Presence.

On successful login, the session key is passed as a parameter of all subsequent request messages to Cisco Unified Presence.

Each third party application should have its own application user configured on Cisco Unified Presence. If an application user is disconnected, any associated end users are automatically logged out.

## Set Presence Status

The Presence Web Service manages user presence on a Cisco Unified Presence server. Users can set their own presence states and receive notifications of changes to the presence state of their contacts. There are two types of presence supported, basic presence and rich presence. Rich presence is exchanged by passing a PIDF file in the message.

The following basic presence states are supported:

- Available

- Busy

- Do Not Disturb

- Away

- Unavailable

- Vacation

- Unknown

Note! The "Unknown" state cannot be set through the Presence Web Service.

## Accessing Presence

The Presence web Service provides two mechanisms to access presence: a real-time eventing model and a polling model.

Real-time Eventing Model

The real-time eventing model uses an application user on Cisco Unified Presence to establish an administrative session, which allows for end users to log in with that session key. Once the end user has logged in, the user registers and subscribes for presence updates. The following diagram highlights the Presence Web Service real-time eventing model interaction with Cisco Unified Presence.

The call flow in the following diagram illustrates the following sequence of events:

- The application initiates a SOAP login request to Cisco Unified Presence via the super-user
                            application user (APIUser), and Cisco Unified Presence returns a session key. The
                            application can then log in the end-user with this session key (essentially, the end-user
                            logs in via the application).

- The end user registers the endpoint using the application-user session key.

- The application initiates a subscribe request (using the session key) on behalf of the end
                            user to retrieve user information, contact list, and presence rules.

- Cisco Unified Presence sends a notification - unsecured.

- The application requests the user's presence status.

Polling Model

The polling model uses an application user on Cisco Unified Presence to establish an administrative session, which allows for end users to log in with that session key. Once the end user has logged in, the application requests presence updates periodically. The diagram which follows highlights the Presence Web Service polling model interaction with Cisco Unified Presence.

The call flow in the following diagram illustrates the following sequence of events:

The application initiates a SOAP login request to Cisco Unified Presence via the super-user application user (APIUser), and Cisco Unified Presence returns a session key. The application can then log in the end-user with this session key (essentially, the end-user logs in via the application).

The application requests presence state and bypasses the eventing model.

The application requests presence state and bypasses the eventing model.

# More Information on Presence Web Service

For more information on the Cisco Unified Presence Presence Web Service, including protocol messaging flows and protocol syntax examples, please refer to the "Developer Guide for Cisco Unified Presence" for the particular version of Cisco Unified Presence which you have deployed.

Download Developer Guide