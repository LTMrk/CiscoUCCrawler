---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cuni-api-b-cuc-cuni-api-b-cuc-cuni-api-chapter-00-html-a853380517
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUNI_API/b_CUC_CUNI_API/b_CUC_CUNI_API_chapter_00.html
retrieved_at: 2026-08-21T01:00:40.036225+00:00
---

Cisco Unity Connection Notification Interface (CUNI) API

# Cisco Unity Connection Notification Interface (CUNI) API

Updated: December 27, 2018

Chapter: API Overview

## Chapter: API Overview

# API Overview

## Introduction

The Cisco Unity Connection Notification Interface (CUNI) API is a web
                           		service interface for managing subscriptions to events from Cisco Unity
                           		Connection systems. It provides a way to get asynchronous notifications when
                           		voice mail messages are received, deleted, or changed. CUNI can be used to
                           		integrate Connection into an existing enterprise-wide portal.

CUNI is designed to provide a simple, stable method of accessing the
                           		notification functionality on Connection systems through a standards based
                           		interface using XML and HTTPS.

Through CUNI, you can do the following:

- Subscribe for message events

- Subscribe for one or many
                                 		  users on a single channel

Note: All the above functions associated with CUNI API support both the
                           		IPv4 and IPv6 addresses. However, the IPv6 address works only when Connection
                           		platform is configured in Dual (IPv4/IPv6) mode.

Note that CUNI is intended for use in server-to-server applications
                           		where receiving notifications for many users over a single connection is
                           		required. As such, it is designed to handle a small number of clients that are
                           		each subscribing for notifications on a large set of subscribers. It also
                           		requires Administrative credentials, making it inappropriate for browser
                           		applications to use directly.

CUNI is composed of two parts: a SOAP interface for subscribing, and an
                           		asynchronous piece (the Notifier) that delivers events as XML over HTTP.

## Technical Details

- CUNI is standards-based: it
                              		  implements a standard SOAP-based interface for managing subscriptions. Message
                              		  events are sent as standard XML over HTTP.

- CUNI is easy to use: as a
                              		  web-based interface, CUNI is independent of operating systems and programming
                              		  languages, and does not require any client libraries to use.

## Getting Started
                        	 with CUNI

In order to begin developing with CUNI, you need to obtain the
                           		following:

Hardware

- Cisco Media Convergence Server (MCS) for Cisco Unity Connection.

- For detailed hardware-specification information, see the Supported Platforms List available at https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-installation-guides-list.html .

Software

- Cisco Unity Connection
                                 		  Software Ordering

- Not for Resale Kits (Must
                                 		  for eligible to purchase)

- Select Unified
                                 		  Communications System Release Kit

Discounts for some of the above hardware and software may be available
                           		for participants in the Cisco Technology Developer Program.

We recommend that all developers have an up-to-date Cisco Developer
                           		Services support agreement. This provides the developer with access to
                           		professional support and assistance for application development.

## Other CUNI
                        	 Resources

Additional information about CUNI is also available on the Cisco Developer Network, see the https://developer.cisco.com/site/unity-connection/overview/ .

To participate in the Unity Connection forum, see the https://communities.cisco.com/community/developer/collaboration/voicemail .

## Troubleshooting

See the following for information on troubleshooting all Connection
                           		APIs:

https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/APIs_Pages/b_CUC_API_troubleshooting.html