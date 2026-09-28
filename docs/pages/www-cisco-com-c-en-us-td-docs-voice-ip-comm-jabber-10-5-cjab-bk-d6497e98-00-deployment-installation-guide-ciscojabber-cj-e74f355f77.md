---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-10-5-cjab-bk-d6497e98-00-deployment-installation-guide-ciscojabber-cj-e74f355f77
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/10_5/CJAB_BK_D6497E98_00_deployment-installation-guide-ciscojabber/CJAB_BK_D6497E98_00_deployment-installation-guide-ciscojabber_chapter_01.html
retrieved_at: 2026-08-21T05:09:49.295585+00:00
---

Deployment and Installation Guide for Cisco Jabber, Release 10.5

# Deployment and Installation Guide for Cisco Jabber, Release 10.5

Updated: August 14, 2014

Chapter: Cisco Jabber Overview

## Chapter: Cisco Jabber Overview

# Cisco Jabber Overview

## About Cisco
                        	 Jabber

Cisco Jabber is a suite of Unified Communications applications that allow seamless interaction with your contacts from anywhere.
                              Cisco Jabber offers IM, presence, audio and video calling, voicemail, and conferencing.

The applications in the Cisco Jabber family of products are:

Cisco Jabber for Android

Cisco Jabber for iPhone and iPad

Cisco Jabber for Mac

Cisco Jabber for Windows

For more information about the Cisco Jabber suite of products, see https://www.cisco.com/go/jabber .

## Cisco Jabber
                        	 Features

Cisco Jabber has a
                              		  broad range of features across all clients. These common features include:

Instant
                                    				Messaging

Presence

Voice and
                                    				Video Calling

Voicemail

Cisco WebEx
                                    				Meetings integration

Predictive
                                    				Contact Search

Single Sign-On

Automatic
                                    				Upgrades

Instant
                                    				Messaging Encryption

Voice and
                                    				Video Encryption

Multiple
                                    				Resource Login

Expressway
                                    				Mobile and Remote Access

Service
                                    				Discovery

URI Dialing

Telemetry

Individual clients
                              		  also have specific features that are not available in all clients. These
                              		  include:

Cisco Jabber
                                    				for Windows

Persistent
                                          					 Chat

Hunt Group

Call
                                          					 Pickup

Custom
                                          					 Contact

Video
                                          					 Desktop Share (BFCP)

Cisco Jabber
                                    				for Android and Cisco Jabber for iPhone and iPad

Dial via
                                          					 Office - Reverse

Send to
                                          					 Mobile

Cisco Jabber
                                    				for Mac

Video
                                          					 Desktop Share (BFCP)

### Telemetry

#### Cisco Jabber
                                 		  Analytics

Applies to: All clients

To improve your
                                 		  experience and product performance, Cisco Jabber may collect and send non-personally
                                 		  identifiable usage and performance data to Cisco. The aggregated data is used
                                 		  by Cisco to understand trends in how Jabber clients are being used and how they
                                 		  are performing.

You must install
                                 		  the following root certificate to use the telemetry feature: GoDaddy
                                    			 Class 2 Certification Authority Root Certificate . The telemetry
                                 		  server certificate name is "metrics-a.wbx2.com". To resolve any warnings about
                                 		  this certificate name, install the required GoDaddy certificate. 
                                 		For more
                                 		  information about certificates, see the Planning Guide.

Telemetry_Enabled —Specifies whether analytics data
                                          				is gathered. The default value is true.

TelemetryEnabledOverCellularData —Specifies whether
                                          				analytics data is sent over cellular data and Wi-Fi (true), or Wi-Fi only
                                          				(false). The default value is true.

TelemetryCustomerID —This optional parameter
                                          				specifies the source of analytic information. This ID can be a string that
                                          				explicitly identifies an individual customer, or a string that identifies a
                                          				common source without identifying the customer. We recommend using a tool that
                                          				generates a Global
                                             				  Unique Identifier (GUID) to create a 36 character unique identifier, or
                                          				to use a reverse domain name.

For more
                                 		  information about these parameters, see the Parameters Reference Guide .

Full details on what analytics data Cisco Jabber does and does not collect can be found in the Cisco Jabber Supplement to Cisco’s On-Line Privacy Policy at https://www.cisco.com/web/siteassets/legal/privacy_02Jun10.html .