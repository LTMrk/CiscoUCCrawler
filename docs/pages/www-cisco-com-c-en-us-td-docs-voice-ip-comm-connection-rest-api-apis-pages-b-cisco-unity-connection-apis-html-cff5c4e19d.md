---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-apis-pages-b-cisco-unity-connection-apis-html-cff5c4e19d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/APIs_Pages/b_Cisco_Unity_Connection_APIs.html
retrieved_at: 2026-08-17T02:20:49.377232+00:00
---

Cisco Unity Connection APIs

# Cisco Unity Connection APIs

### Download Options

Updated: January 2, 2019

# Cisco Unity
            	 Connection APIs

## Introduction

Cisco Unity
                  		Connection is a feature-rich voice messaging platform based on the same Linux
                  		operating system as Cisco Unified Communications Manager. Connection users can
                  		access voice messages by using email, web clients, mobile devices, instant
                  		messaging, and desktop clients such as Cisco Unified Personal Communicator; and
                  		can view, search, sort, and play messages on a Cisco Unified IP Phone display.
                  		Connection also provides comprehensive automated-attendant functions, including
                  		intelligent call routing and easily customizable call screen and message
                  		notification options. For more information see Cisco Unity Connection
                     		  documentation on Cisco.com

Cisco Unity
                  		Connection includes several Representational State Transfer (REST) application
                  		programming interfaces (APIs) that provide provisioning, messaging, and
                  		telephony access to Connection. These APIs provide the ability to integrate
                  		Connection features into existing enterprise-wide provisioning management
                  		systems and messaging clients. The APIs are REST interfaces that standardize
                  		operations such as add, delete, view, and modify.

For more information see the chapter "Adding or Changing the IPv6
                                 			 Addresses of Cisco Unity Connection 8.5 and Later Servers" at the following
                                 			 link http://www.cisco.com/en/US/docs/voice_ip_comm/connection/8x/upgrade/guide/8xcucrug051.html

For all the REST APIs, the special characters in the query
                              		  parameter of a requested URL should be encoded as per the Unicode Standard. For
                              		  example, to search a user with alias "Bob&Smith" the Query which is
                              		  currently "query=(alias%20is%Bob\%26Smith)" should be modified to
                              		  "query=(alias%20is%20Bob%5C%26Smith)". Here a special character "\" is encoded
                              		  to "%5C".

## Available
               	 Connection REST APIs

CUPI : Cisco_Unity_Connection_Provisioning_Interface_(CUPI)_API

The Cisco Unity
                  		Connection Provisioning Interface (CUPI) API provides access to the most
                  		commonly provisioned data on Cisco Unity Connection systems-users, contacts,
                  		distribution lists, and call handlers.

CUPI for End Users : Cisco_Unity_Connection_Provisioning_Interface_(CUPI)_API_--_For_End_Users

The Cisco Unity
                  		Connection Provisioning Interface (CUPI) API includes access for individual
                  		users when authenticating against user credentials. This allows for custom
                  		end-user applications.

CUMI : Cisco_Unity_Connection_Messaging_Interface_(CUMI)_API

The Cisco Unity
                  		Connection Messaging Interface (CUMI) API provides access to user messages.

CUTI : Cisco_Unity_Connection_Telephony_Interface_(CUTI)_API

The Cisco Unity
                  		Connection Telephony Interface (CUTI) API provides the ability to play and
                  		record audio content over the phone.

CUII : Cisco Unity Connection Imaging Interface (CUII) API

Cisco Unity
                  		Connection 9.0(1) and later versions now support the Cisco Unity Connection
                  		Imaging Interface (CUII) API that provides the ability to view message state
                  		and mailbox information visually using graphics icons.

CUNI : Cisco_Unity_Connection_Notification_Interface_(CUNI)_API

The Cisco Unity
                  		Connection Notification Interface (CUNI) API provides notification for one or
                  		more users. CUNI is designed for use in server-to-server applications where
                  		receiving notifications for many users over a single connection is required.

## Other Connection
               	 API Resources

FAQ

Troubleshooting

Draft

| Note | All the REST APIs support both the IPv4 and IPv6 addresses.
                              		  However, the IPv6 address works only when Connection platform is configured in
                              		  Dual (IPv4/IPv6) mode. For more information see the chapter "Adding or Changing the IPv6
                                 			 Addresses of Cisco Unity Connection 8.5 and Later Servers" at the following
                                 			 link http://www.cisco.com/en/US/docs/voice_ip_comm/connection/8x/upgrade/guide/8xcucrug051.html |
|---|---|

| Note | For all the REST APIs, the special characters in the query
                              		  parameter of a requested URL should be encoded as per the Unicode Standard. For
                              		  example, to search a user with alias "Bob&Smith" the Query which is
                              		  currently "query=(alias%20is%Bob\%26Smith)" should be modified to
                              		  "query=(alias%20is%20Bob%5C%26Smith)". Here a special character "\" is encoded
                              		  to "%5C". |
|---|---|