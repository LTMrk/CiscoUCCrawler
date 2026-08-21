---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cuii-api-b-cuii-api-b-cuii-api-chapter-00-html-227b4b9728
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUII_API/b_CUII_API/b_CUII_API_chapter_00.html
retrieved_at: 2026-08-21T08:07:30.571509+00:00
---

Cisco Unity Connection Imaging Interface (CUII) API

# Cisco Unity Connection Imaging Interface (CUII) API

Updated: December 28, 2018

Chapter: Cisco Unity
	 Connection Imaging Interface (CUII) API

## Chapter: Cisco Unity
	 Connection Imaging Interface (CUII) API

# Cisco Unity
                     	 Connection Imaging Interface (CUII) API

Links to Other API pages: Cisco Unity Connection APIs

## Cisco Unity
                        	 Connection Imaging Interface (CUII) API

Links to Other API pages: Cisco Unity Connection APIs

### Benefits

The Cisco Unity Connection Imaging Interface (CUII) API provides the
                              		ability to view message state and mailbox information visually using graphics
                              		icons. The CUII API allows users to view voice messages information visually,
                              		which can be leveraged in a cross-functional environment and can be integrated
                              		with other applications.

By using CUII, you can get the icon based representation for the
                              		following information:

- Unread messages count

- Urgent unread messages count

- Read messages count

- Urgent read messages count

- MWI status and the
                                    		  corresponding image

Note: All the above functions associated with CUII API support both the
                              		IPv4 and IPv6 addresses. However, the IPv6 address works only when Connection
                              		platform is configured in Dual (IPv4/IPv6) mode.

For more information see the chapter "Adding or Changing the IPv6
                              		Addresses of Cisco Unity Connection Servers" at the following link http://www.cisco.com/en/US/docs/voice_ip_comm/connection/9x/upgrade/guide/9xcucrug051.html .

Note: With Cisco Unity Connection 9.1(1), the single sign-on feature is
                              		enabled for all the Connection Rest APIs. For more information, see the "Single
                              		Sign-On in Cisco Unity Connection" chapter in Security Guide for Cisco Unity
                              		Connection 9.x http://www.cisco.com/en/US/docs/voice_ip_comm/connection/9x/security/guide/9xcucsec061.html .

### Technical Details

CUII allows notification templates to dynamically display the
                              		information like MWI state, message count, current state of a specific message
                              		(like read, unread, deleted) about a specific user's inbox and/or specific
                              		message.

CUII is a REST-based interface that provides standard CRUD operations.
                              		The XML and JSON interfaces are annotated with information about what is in
                              		them.

As a web-based interface, CUII is independent of operating system and
                              		programming language and does not require any client libraries to use.

### Getting Started

In order to begin developing with the Cisco Unity Connection CUII API,
                              		the following hardware and software requirement must be met:

Hardware

- For detailed hardware
                                    		  requirements, see the Cisco Unity Connection 9.x Supported Platforms List

Software

- Cisco Unity Connection
                                    		  Software Ordering

- Not for Resale Kits (Must be
                                    		  eligible to purchase)

- Communications System
                                    		  Release Kit

Discounts for some of the required hardware and software may be
                              		available for participants in the Cisco Technology Developer Program.

We recommend that all developers have an up-to-date Cisco Developer
                              		Services support agreement. This provides the developer with access to
                              		professional support and assistance for application development.

### Other CUII
                           	 Resources

Additional information about CUII is also available on the Cisco
                              		Developer Network ( link to CDN ). Note, however, that the documentation here
                              		on the DocWiki is the most up-to-date documentation available for CUII.

To participate in the CUII forum, see the CUPI forum on CDN .

On the CUII page on CDN, you will also find links to the CUII WADL and
                              		CUII XML schema.

### Troubleshooting

See the following for information on troubleshooting all Connection
                              		APIs:

Troubleshooting (applies to all Connection APIs)

The error handling for CUII APIs is same as it is done for CUPI API. For
                              		more information on how error handling done in CUPI API, refer to Cisco Unity Connection Provisioning Interface (CUPI) API -- Error
                                 		  Handling