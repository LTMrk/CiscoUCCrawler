---
doc_id: developer-cisco-com-site-im-and-presence-discover-api-overviews-sip-simple-overview-2837d9d5f8
source_url: https://developer.cisco.com/site/im-and-presence/discover/api_overviews/sip-simple_overview/
retrieved_at: 2026-09-01T17:45:34.372453+00:00
---

# About the Session Initiation Protocol (SIP) and SIP for Instant Messaging and Presence Leveraging
                    Extensions (SIMPLE) Interface

The Session Initiation Protocol (SIP) and SIP for Instant Messaging and Presence Leveraging Extension (SIMPLE) based interfaces for Cisco Unified Presence provide the following functionality:

- The publication and subscription of presence status

- UC Change Notification (UCCN) subscription of user profile and system settings

- Instant Message via pager mode MESSAGE request

## SIP/SIMPLE Industry Standards

The industry standards that describe the SIP/SIMPLE interface that is supported by Cisco Unified Presence are:

- RFC-3261 -- SIP: Session
                            Initiation Protocol

- RFC-3265 -- SIP-Specific
                            Event Notification

- RFC-3856 -- A Presence
                            Event Package for SIP

- RFC-3863 -- Presence
                            Information Data Format (PIDF)

- RFC-3903 -- SIP Extension
                            for Event State Publication

- RFC-4479 -- A Data Model
                            for Presence

- RFC-4480 -- RPID: Rich
                            Presence: Extensions to the Presence Information Data Format (PIDF)

- draft-ietf-simple-prescaps-ext-03 -- User Agent Capability Extension to Presence Information Data Format (PIDF)

- RFC-4662 -- A Session
                            Initiation Protocol (SIP) Event Notification Extension for Resource Lists

- draft-ietf-sip-subnot-etags-02 -- An Extension to Session Initiation Protocol (SIP) Events for Conditional Event
                            Notification

- RFC-3428 -- Session
                            Initiation Protocol (SIP) Extension for Instant Message

Cisco Unified Presence is agnostic to pidf extensions; any Presence User Agent Client (UAC) or  Presence User Agent Server (UAS) that interfaces with the Cisco Unified Presence Engine must handle these extensions.

About SIP/SIMPLE Presence

The SIP/SIMPLE Presence interface allows Third Party (client) applications to subscribe to Cisco Unified Presence to receive presence status notifications from Cisco Unified Presence, and to publish presence states to Cisco Unified Presence.

The client application sends a SUBSCRIBE request to Cisco Unified Presence to subscribe to the presence of a user or a group of users. Cisco Unified Presence authorizes the subscription policy. Cisco Unified Presence then transmits the presence status of the user or group of users to the subscriber in a NOTIFY message. The client application can transmit presence states to Cisco Unified Presence using the PUBLISH message.

About SIP/SIMPLE Unified Communicator Change Notifier (UCCN)

The Unified Communicator Change Notifier (UCCN) Interface notifies a client of changes to the provisioning data that is stored in the Cisco Unified Presence database. The Unified Communicator Change Notifier Interface detects changes within the Cisco Unified Presence database, and communicates these changes to the client using a SIP Subscribe/Notify exchange.

This interface is deprecated from Cisco Unified CM IM & Presence 10.5.1 onwards.

About SIP/SIMPLE Instant Messaging

RFC-3428 (Session Initiation Protocol (SIP) Extension for Instant Messaging) provides the basis for the Cisco Unified Presence SIMPLE instant messaging interface.  Cisco Unified Presence supports pager mode MESSAGE request. In order for Cisco Unified Presence to forward incoming MESSAGE requests properly, SIP/SIMPLE instant message applications or clients are required to register to Cisco Unified Presence by sending SIP REGISTER request using port 5060 by default.

# More Information on SIP/SIMPLE Interface

For more information on the Cisco Unified Presence SIP/SIMPLE interface, including protocol messaging flows and protocol syntax examples, please refer to the "Developer Guide for Cisco Unified Presence" for the particular version of Cisco Unified Presence which you have deployed.

Download Developer Guide