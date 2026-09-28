---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cumi-api-b-cumi-api-b-cumi-api-chapter-00-html-c3c6fc4886
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUMI_API/b_CUMI-API/b_CUMI-API_chapter_00.html
retrieved_at: 2026-08-21T08:06:10.794022+00:00
---

Cisco Unity Connection Messaging Interface (CUMI) API

# Cisco Unity Connection Messaging Interface (CUMI) API

Updated: December 23, 2018

Chapter: Cisco Unity Connection Messaging
	 Interface (CUMI) API

## Chapter: Cisco Unity Connection Messaging
	 Interface (CUMI) API

# Cisco Unity Connection Messaging
                     	 Interface (CUMI) API

Links to Other API pages: Cisco Unity Connection APIs

## Introduction

The Cisco Unity
                           		Connection Messaging Interface (CUMI) is a messaging API for Cisco Unity
                           		Connection that has been designed to be stable and simple to use. It is based
                           		on leading industry standards for web-based API development, and provides
                           		access to a wide set of Connection messaging functionality.

If you are a
                           		customer or developer who needs the ability to integrate Connection into an
                           		existing enterprise-wide portal, CUMI offers a secure method for doing the
                           		following:

- Sending messages

Receiving
                                    			 messages

Replying to
                                    			 messages

Sending
                                    			 broadcast messages (provided the user account is enabled to send broadcast
                                    			 messages)

Sending dispatch
                                    			 messages

Receiving
                                    			 notifications of new messages

Beginning with
                           		Cisco Unity Connection 10.5 and later, when one or more tenants are configured
                           		on a single installation of Cisco Unity Connection, a user with Mailbox Access
                              		  Delegate Account role and belonging to a particular tenant will be able to
                           		access messages of all the users within the same tenant only.

## How the
                        	 documentation is organized

Accessing Mailboxes and
                                    				Folders

Sending Messages using the
                                    				API

Message Recall API

Working with
                                    				Notifications

Working with Dispatch
                                    				Messages

Working with Broadcast
                                    				Messages

Special Features

Samples

## Technical Details

CUMI is a REST interface that standardizes operations such as add,
                           		delete, and modify. The XML comes with standard XML schema definitions that are
                           		annotated with information about what is in them.

As a web-based interface, CUMI is independent of operating system and
                           		programming language and does not require any client libraries to use.

## Getting started

In order to begin
                           		developing with the Cisco Unity Connection CUMI API, you will need to obtain
                           		the following:

Hardware

Cisco Media
                                 			 Convergence Server (MCS) for Cisco Unity Connection version 12.x and later

For detailed
                                 			 hardware requirements, see the Cisco Unity
                                    				Connection 8.x Supported Platforms List

Software

Cisco Unity
                                 			 Connection Software Ordering

Not for Resale
                                 			 Kits (Must be eligible to purchase)

Select Unified
                                 			 Communications System Release Kit

Discounts for some
                           		of the required hardware and software may be available for participants in the
                           		Cisco Technology Developer Program.

We recommend that
                           		all developers have an up-to-date Cisco Developer Services support agreement.
                           		This provides the developer with access to professional support and assistance
                           		for application development.

## Other CUMI
                        	 Resources

Additional
                           		information about CUMI is also available on the Cisco Developer Network. Note,
                           		however, that the documentation here on the DocWiki is the most up-to-date
                           		documentation available for CUMI.

## Troubleshooting

See the following for information
                           		on troubleshooting all Connection APIs:

Troubleshooting (applies to all Connection APIs)

| Note | By default,
                                       		  API access to playback secure messages is turned off. To enable API access to
                                       		  secure messages, check the Allow Access to Secure Message Recordings Through
                                       		  the Cisco Unity Connection Messaging Interface (CUMI) setting on the System
                                       		  Settings > Advanced > API Settings page in Cisco Unity Connection
                                       		  Administration. |
|---|---|

| Note | All the above
                                       		  functions associated with CUMI API support both the IPv4 and IPv6 addresses.
                                       		  However, the IPv6 address works only when Connection platform is configured in
                                       		  Dual (IPv4/IPv6) mode. |
|---|---|

| Note | With Cisco
                                       		  Unity Connection 9.1(1), the single sign-on feature is enabled for all the
                                       		  Connection Rest APIs. For more information, see the "Single Sign-On in Cisco
                                       		  Unity Connection" chapter in Security Guide for Cisco Unity Connection 9.x https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/9x/security/guide/9xcucsecx/9xcucsec061.html |
|---|---|