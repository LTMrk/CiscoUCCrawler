---
doc_id: developer-cisco-com-site-im-and-presence-discover-api-overviews-caxl-overview-b4edee4ae0
source_url: https://developer.cisco.com/site/im-and-presence/discover/api_overviews/caxl_overview/
retrieved_at: 2026-09-01T17:45:43.073196+00:00
---

# What is it?

The Cisco AJAX XMPP Library (CAXL) is an API designed to simplify and accelerate the development of client applications. The client library provides a jump start for developers writing Extensible Messaging and Presence Protocol ( XMPP ) enabled web applications or clients from scratch.

CAXL is ideal for companies looking to leverage Cisco Unified Presence and integrate presence and messaging into their own custom web-based applications.

With the Cisco AJAX XMPP Library developers can:

- Embed a customer support portal into a company website

- Add instant messaging capabilities into a gaming application

- Add presence information and messaging capability to custom applications

# CAXL Functionality

CAXL provides the following functionality:

1-to-1 Instant Messaging

- Ability to initiate and receive P2P IM

- Supports XHTML-IM rich-text.

Multi-user chat room (including Persistent Chat)

- Ability to create adhoc and persistent chat rooms

- Ability to invite and be invited to chat rooms.

- Ability to search for existing chat rooms

Pub/Sub Applications (e.g. for GeoLocation)

- Personal Eventing Protocol - Ability to create/publish/subscribe to pub/sub service nodes on a server.

User Authentication Roster Presence and Roster (Contacts List) management

- Ability to Add/Update/Remove Contacts.

- Ability to move contacts between groups.

My Presence

- Ability to set device presence.

- When integrated with CUP, SDK can be configured to set CAXL device presence to be the same as Presence
              engine composed presence.

Temporary Presence Subscriptions

- Ability to create temporary subscriptions to users who are not on your roster ("Quick Contacts")

- Ability to do bulk subscribe/unsubscribe of temporary subscriptions. Useful in multi-page applications
              where each page may have a different list of users.

# Technical Overview

The Cisco AJAX XMPP Library (CAXL) provides a foundation for developing web-based applications that utilize the XMPP protocol. For detailed information on the XMPP standard, please visit http://xmpp.org

The AJAX library is a JavaScript XMPP client library for integration of instant messaging, availabiliyt and roster services from the Cisco Unified Presence.

The Cisco AJAX XMPP Library is comprised of the following modules:

- jQuery: an open-source library for searching, traversing, and manipulating the browser's
              DOM

- Cisco AJAX XMPP Library Minimal API: a high-level API for sending and receiving XMPP
              stanzas

- Cisco AJAX XMPP Library Core API: a high-level API for messaging and presence

- Cisco AJAX XMPP Library UI API: HTML UI components built on top of the core Cisco AJAX
              XMPP Library API

The library can be used purely as an API or as a web UI or both. The core CAXL API is not dependant on the CAXL UI being used. The internals of the library utilize jQuery for low-level JavaScript tasks but there is no dependency on any JavaScript UI framework for the UI components.

Cisco provides a minimal distribution of the core library for applications that do not need typical IM functionality.The minimal library provides client session management, authentication, stanza sending and eventing when a stanza is received. IM centric functionality like 1-1 chat sessions, text conferencing rooms and publish/subscribe is not available. A list of classes included in the minimal library can be found in the API documentation delivered with the library.

The Cisco AJAX XMPP library is an object-oriented, client-side library which communicates to a BOSH server component. BOSH (Bidirectional-streams Over Synchronous HTTP) technology is used as an HTTP binding for XMPP communications that is useful in situations where a device or client is unable to maintain a long-lived TCP connection to an XMPP server, e.g. in a web browser.

# Architecture

The Cisco AJAX XMPP Library uses a model-view-controller framework. The top-level base class for all Cisco AJAX XMPP Library objects is the JWBase class. JWBase defines the object-oriented structure of the classes and also the common object behaviors and properties.

### Views

Views represent the UI features in the library. The UI features include components for IM, group chat, availability and roster management. The jabberwerx.ui.JWView has no explicit dependency on any JavaScript UI framework. The jabberwerx.ui namespace contains all the view objects.

### Controllers

The controllers allow for actions to be invoked by the user, and translate these action into model logic. They can also listen for changes in the model, and notify those changes to the subscribers. Finally, controllers are the "handles" that control the application-level setup and tear down. All controller classes extend from the base Controller class. The jabberwerx namespace contains all the model objects.

### Model

The model is a graph of jabberwerx.JWModel objects, and is self-contained. The model objects represent the individual items in the domain e.g. users, contacts, JIDs. They represent the data in the system but they do not contain display information. All model objects derive from the jabberwerx.JWModel class (and subsequently JWBase) and are contained in the jabberwerx namespace.

# Download CAXL SDK

Download CAXL SDK