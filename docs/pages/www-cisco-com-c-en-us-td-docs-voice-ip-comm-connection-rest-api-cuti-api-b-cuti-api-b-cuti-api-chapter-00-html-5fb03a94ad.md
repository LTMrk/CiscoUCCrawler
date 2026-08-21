---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cuti-api-b-cuti-api-b-cuti-api-chapter-00-html-5fb03a94ad
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUTI_API/b_CUTI_API/b_CUTI_API_chapter_00.html
retrieved_at: 2026-08-21T08:06:56.791907+00:00
---

Cisco Unity Connection Telephony Interface (CUTI) API

# Cisco Unity Connection Telephony Interface (CUTI) API

Updated: December 27, 2018

Chapter: API Oveview

## Chapter: API Oveview

# API Oveview

Links to Other API pages: Cisco_Unity_Connection_APIs

## Introduction

The Cisco Unity Connection Telephony Interface (CUTI) API is a web
                           		service interface for telephone record and playback on Cisco Unity Connection
                           		systems. CUTI is designed to provide a simple, stable method of accessing
                           		telephone record and playback functionality on Connection systems through a
                           		standards-based interface using XML and HTTPS.

You can use CUTI to do the following:

- Initiate dialout to a phone
                                 		  device

- Play and record greetings,
                                 		  messages, and other audio

- Control playback speed and
                                 		  volume

- Stop and resume playback and
                                 		  record

Note: All the above functions associated with CUTI API support both the
                           		IPv4 and IPv6 addresses. However, the IPv6 address works only when Connection
                           		platform is configured in Dual (IPv4/IPv6) mode.

For more information see the chapter "Adding or Changing the IPv6
                           		Addresses of Cisco Unity Connection 8.5 and Later Servers" at the following
                           		link
                           		http://www.cisco.com/en/US/docs/voice_ip_comm/connection/9x/upgrade/guide/9xcucrug051.html.

Note: With Cisco Unity Connection 9.1(1), the single sign-on feature is
                           		enabled for all the Connection Rest APIs. For more information, see the "Single
                           		Sign-On in Cisco Unity Connection" chapter in Security Guide for Cisco Unity
                           		Connection 9.x
                           		http://www.cisco.com/en/US/docs/voice_ip_comm/connection/9x/security/guide/9xcucsec061.html

## Benefits

With CUTI, you have the ability to record audio as needed by using a
                           		phone, providing additional functionality besides uploading .wav files. You can
                           		use CUTI to do the following:

- As part of a User or Admin
                                 		  interface, record audio as part of a name, greeting, or message

- Play secure messages

- Record messages using phone
                                 		  as a media device

## Technical Details

CUTI was developed using the latest advances in web-based interfaces: it
                           		is a REST interface that standardizes operations such as add, delete, and
                           		modify. The XML comes with standard XML schema definitions that are annotated
                           		with information about what is in them.

As a web-based interface, CUTI is independent of operating system and
                           		programming language, and does not require any client libraries to use.

## Getting Started
                        	 with CUTI

In order to begin developing with the Cisco Unity Connection CUTI API,
                           		you will need to obtain the following:

### Hardware

- Cisco Media Convergence
                                    			 Server (MCS) for Cisco Unity Connection version 8.0 and later

- For detailed hardware
                                    			 requirements, see the Cisco Unity Connection 8.x Supported Platforms List

### Software

- Cisco Unity Connection
                                    			 Software Ordering

- Not for Resale Kits (Must
                                    			 be eligible to purchase)

- Select Unified
                                    			 Communications System Release Kit

Discounts for some of the required hardware and software may be
                              		  available for participants in the Cisco Technology Developer Program.

We recommend that all developers have an up-to-date Cisco Developer
                              		  Services support agreement. This provides the developer with access to
                              		  professional support and assistance for application development.

## Other CUTI
                        	 Resources

Additional information about CUTI is also available on the Cisco
                           		Developer Network (link to CDN). Note, however, that the documentation here on
                           		the DocWiki is the most up-to-date documentation available for CUTI.

To participate in the CUTI forum, see the CUTI forum on CDN

## Troubleshooting

See the following for information on troubleshooting all Connection
                           		APIs:

Troubleshooting (applies to all Connection APIs)