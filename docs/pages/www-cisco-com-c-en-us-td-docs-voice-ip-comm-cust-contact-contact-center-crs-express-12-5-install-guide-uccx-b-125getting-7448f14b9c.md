---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-install-guide-uccx-b-125getting-7448f14b9c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/install/guide/uccx_b_125getting-started-ip-ivr/uccx_b_125getting-started-ip-ivr_chapter_00.html
retrieved_at: 2026-08-16T21:14:48.340369+00:00
---

Getting Started with IP IVR Guide, Release 12.5(1)

# Getting Started with IP IVR Guide, Release 12.5(1)

Updated: February 10, 2020

Chapter: About Unified IP IVR

## Chapter: About Unified IP IVR

# About Unified IP IVR

## Product Names

The following product name conventions are used in this guide:

Cisco Unified IP IVR is abbreviated as Unified IP IVR.

Cisco Unified Communications Manager is abbreviated as Unified CM.

Cisco Unified Contact Center Express is abbreviated as Unified CCX.

Cisco Unified Intelligent Contact Management Enterprise is abbreviated as Unified ICME.

## Summary Description of Unified IP IVR

The Unified IP IVR (Interactive Voice Response) is a Unified CCX product package that provides IP call queuing and IP intelligent
                              voice response functionality for a contact center.

The Unified IP IVR uses the script editor and it can be configured to play static or dynamic prompts, to offer menus to callers,
                              queue a call, play music, and so on.

## More than One
                        	 Unified CCX Product Installed on a Server

All Unified
                              		  CCX product packages are mutually exclusive. This means that only one of them
                              		  can be installed at any point in time on a Unified CCX server. If multiple
                              		  licenses are installed, then priority is given to the package with the highest
                              		  number at the left in the following list:

Unified IP IVR

Unified CCX
                                    				Enhanced

Unified CCX
                                    				Premium

## Unified IP IVR
                        	 Features Supported in Each Product

The
                              		  following table lists the Unified CCX features supported in each product.

Feature

Unified IP
                                          					 IVR

Hardware
                                          					 configuration

Cisco UCS
                                          					 and Cisco approved partner servers

Software
                                          					 configuration

Client-server software

Vendor
                                          					 systems

Unified CM
                                          					 8.x, Unified CM 9.x

Operating
                                          					 systems

Runs on
                                          					 Unified Communication Operating System (Red Hat Enterprise Linux)

Maximum
                                          					 number of CTI ports per server

400

CTI
                                          					 (Computer Telephony Integration) option

Included

Email

Included

Database

Included

Read data
                                          					 from HTTP and XMLpages

Included

MRCP ASR/TTS

Optional
                                          					 using Media Resource Control Protocol (MRCP)-order from a 3rd party vendor

For the currently supported MRCP ASR/TTS vendors, see the current at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html .

Play
                                          					 messages to callers—music

Included
                                          					 using Unified CM Music On Hold server or .wav file

Play
                                          					 messages to callers—prompts

Included
                                          					 using .wav file

Play
                                          					 messages to callers—combine prompts, music and messages

Included and
                                          					 fully customizable

Capture
                                          					 and process caller Dual Tone Multifrequency (DTMF) input

Included
                                          					 and fully customizable

Capture
                                          					 and process caller DTMF input under VXML control

Included

Automated
                                          					 attendant support

Included
                                          					 and fully customizable

All
                                          					 languages

Included,
                                          					 if installed.

Inbound
                                          					 HTTP request

Included

Historical
                                          					 reporting

Included,
                                          					 but limited to Unified IP IVR reports

From Unified CCX 10.0(1),
                                          					 access the Historical reports using Unified Intelligence Center. Historical
                                          					 Reporting Client (HRC) is not available.

Custom
                                          					 scripting using Unified CCX Drag and Drop Editor

Included.
                                          					 Has full editing features. All types of applications including ICM, Busy, and
                                          					 RNA are available.

JTAPI
                                          					 Telephony triggers

Included

HTTP
                                          					 triggers

Included

Conditional routing (time of day, day of week, custom variables,
                                          					 and so on.)

Included

Overflow,
                                          					 interflow, intraflow routing

Included

Run
                                          					 defined workflow using HTTP request

Included

Integrated
                                          					 self-service application support

Included

To check for the current versions of the preceding software supported by your version of Unified IP IVR, see the at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html .

## Unified IP IVR Package Description

The following table  summarizes the description of the Unified IP IVR package

Product Package

Available Licensed Components

Purpose

Unified IP IVR

- Unified IP IVR Server Software (required)

- Unified IP IVR Ports (at least one is a must)

- Automatic Speech Recognition (obtained through a separate Vendor)

- Text To Speech (obtained through a separate Vendor)

- VoiceXML

Allows contact-center applications to handle "typical" questions by letting callers interact directly with back-end databases without agent intervention.

This includes integration with Unified CCE if needed.

This also includes three subsystems and three corresponding editor pallets:

- The HTTP subsystem (which enables both incoming and outgoing HTTP support)

- Outgoing email support

- Database support

Three basic Historical Reports (IVR Traffic Analysis Report, IVR Application Performance Analysis Report, and the Detailed
                                          Call by Call CCDR Report) are available with both packages without needing a separate license. All supported Unified CCX languages
                                          are included in both packages; it is up to you to install the languages you want.

## Unified IP IVR
                        	 Feature Summary

Unified IP
                              		  IVR software is a multimedia (voice, data, web) IP-enabled interactive voice
                              		  response solution that automates call handling by autonomously interacting with
                              		  contacts.

Using
                              		  Unified IP IVR, you can create applications to do the following:

Interpret voice
                                    				data (as well as keyboard data).

Translate text
                                    				to speech.

Send and respond
                                    				to HTTP requests.

Send email.

Enable Unified
                                    				CCX to interact directly with back-end databases through ODBC (Open Database
                                    				Connectivity) support without agent intervention.

Unified IP IVR
                                    				applications have ODBC support. Unified IP IVR applications can access
                                    				Microsoft Structured Query Language (SQL) servers and Oracle, Sybase, and IBM
                                    				DB2 databases.

To check for the current versions of the preceding software supported by your version of Unified IP IVR, see the at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html .

## Unified CCX
                        	 Subsystems that Unified IP IVR Supports

Unified IP
                              		  IVR supports the following subsystems:

Subsystem
                                          					 Type

Purpose

MRCP
                                          					 Automatic Speech Recognition (ASR)

- ASR Server Software
                                             						(Required)

- ASR ports (at least one is
                                             						required)

The number
                                          					 of ASR ports should be less than or equal to the number of IVR ports. If there
                                          					 are more ASR ports than IVR ports, then the excess ports are automatically
                                          					 disabled.

Allows a
                                          					 script to respond to voice input in addition to DTMF (Dual Tone
                                          					 Multi-Frequency), the signal to the telephone company that is generated when
                                          					 you press a key on a telephone keypad.

This allows
                                          					 a caller to verbally convey information to the system for processing instead of
                                          					 pressing keys on a touch-tone telephone.

MRCP Text To
                                          					 Speech (TTS)

- TTS Server Software
                                             						(Required)

- TTS Ports (at least one is
                                             						required)

Composes
                                          					 voice prompts that are generated in real time from text, such as speaking the
                                          					 words in the text of an email message.

TTS is
                                          					 primarily used to convey information obtained from a database or other source
                                          					 that is non-repetitive. Examples of such information include name and address
                                          					 verification. Repetitive information, such as numbers comprising an account
                                          					 balance, normally is not conveyed using TTS.

Although
                                          					 text to speech technology has improved greatly since its inception, the tone
                                          					 still sounds mechanical. So it is best used only when the information
                                          					 possibilities make wave file generation impossible.

EMail

Adds
                                          					 components to the Unified CCX Engine that allows it to send email messages.

Database

Handles the
                                          					 connections between the Unified CCX server and the enterprise database.

Also
                                          					 provides Open Database Connectivity (ODBC) support.

See Compatibility Information for the latest versions of the database software that are supported at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html .

Inbound HTTP
                                          					 Request

Adds
                                          					 components to the Unified CCX Engine that allow it to respond to HTTP requests.

Voice
                                          					 Browser

Manages
                                          					 Voice Browser functionality.

## Sample Default Unified IP IVR Scripts

The following table describes the sample Unified IP IVR scripts automatically included with your Unified IP IVR system.

Sample Script Template

Description

Auto Attendant

Allows a caller to call an agent by entering an extension number or the first few characters of an associated username. If
                                          ASR is enabled, the caller may simply speak the extension or the user name.

Spoken Name Upload

Enables Unified CM users to call in, authenticate their identities, and replace their spoken names with newly recorded announcements
                                          on their telephones

Voice Browser

Uses ASR functionality to allow a caller to access information from VoiceXML-enabled web sites.

| Feature | Unified IP
                                          					 IVR |
|---|---|
| Hardware
                                          					 configuration | Cisco UCS
                                          					 and Cisco approved partner servers |
| Software
                                          					 configuration | Client-server software |
| Vendor
                                          					 systems | Unified CM
                                          					 8.x, Unified CM 9.x |
| Operating
                                          					 systems | Runs on
                                          					 Unified Communication Operating System (Red Hat Enterprise Linux) |
| Maximum
                                          					 number of CTI ports per server | 400 |
| CTI
                                          					 (Computer Telephony Integration) option | Included |
| Email | Included |
| Database | Included |
| Read data
                                          					 from HTTP and XMLpages | Included |
| MRCP ASR/TTS | Optional
                                          					 using Media Resource Control Protocol (MRCP)-order from a 3rd party vendor For the currently supported MRCP ASR/TTS vendors, see the current at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html . |
| Play
                                          					 messages to callers—music | Included
                                          					 using Unified CM Music On Hold server or .wav file |
| Play
                                          					 messages to callers—prompts | Included
                                          					 using .wav file |
| Play
                                          					 messages to callers—combine prompts, music and messages | Included and
                                          					 fully customizable |
| Capture
                                          					 and process caller Dual Tone Multifrequency (DTMF) input | Included
                                          					 and fully customizable |
| Capture
                                          					 and process caller DTMF input under VXML control | Included |
| Automated
                                          					 attendant support | Included
                                          					 and fully customizable |
| All
                                          					 languages | Included,
                                          					 if installed. |
| Inbound
                                          					 HTTP request | Included |
| Historical
                                          					 reporting | Included,
                                          					 but limited to Unified IP IVR reports From Unified CCX 10.0(1),
                                          					 access the Historical reports using Unified Intelligence Center. Historical
                                          					 Reporting Client (HRC) is not available. |
| Custom
                                          					 scripting using Unified CCX Drag and Drop Editor | Included.
                                          					 Has full editing features. All types of applications including ICM, Busy, and
                                          					 RNA are available. |
| JTAPI
                                          					 Telephony triggers | Included |
| HTTP
                                          					 triggers | Included |
| Conditional routing (time of day, day of week, custom variables,
                                          					 and so on.) | Included |
| Overflow,
                                          					 interflow, intraflow routing | Included |
| Run
                                          					 defined workflow using HTTP request | Included |
| Integrated
                                          					 self-service application support | Included |

| Note | To check for the current versions of the preceding software supported by your version of Unified IP IVR, see the at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html . |
|---|---|

| Product Package | Available Licensed Components | Purpose |
|---|---|---|
| Unified IP IVR | Unified IP IVR Server Software (required) Unified IP IVR Ports (at least one is a must) Automatic Speech Recognition (obtained through a separate Vendor) Text To Speech (obtained through a separate Vendor) VoiceXML | Allows contact-center applications to handle "typical" questions by letting callers interact directly with back-end databases without agent intervention. This includes integration with Unified CCE if needed. This also includes three subsystems and three corresponding editor pallets: The HTTP subsystem (which enables both incoming and outgoing HTTP support) Outgoing email support Database support |

| Note | Three basic Historical Reports (IVR Traffic Analysis Report, IVR Application Performance Analysis Report, and the Detailed
                                          Call by Call CCDR Report) are available with both packages without needing a separate license. All supported Unified CCX languages
                                          are included in both packages; it is up to you to install the languages you want. |
|---|---|

| Note | To check for the current versions of the preceding software supported by your version of Unified IP IVR, see the at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html . |
|---|---|

| Subsystem
                                          					 Type | Purpose |
|---|---|
| MRCP
                                          					 Automatic Speech Recognition (ASR) ASR Server Software
                                             						(Required) ASR ports (at least one is
                                             						required) The number
                                          					 of ASR ports should be less than or equal to the number of IVR ports. If there
                                          					 are more ASR ports than IVR ports, then the excess ports are automatically
                                          					 disabled. | Allows a
                                          					 script to respond to voice input in addition to DTMF (Dual Tone
                                          					 Multi-Frequency), the signal to the telephone company that is generated when
                                          					 you press a key on a telephone keypad. This allows
                                          					 a caller to verbally convey information to the system for processing instead of
                                          					 pressing keys on a touch-tone telephone. |
| MRCP Text To
                                          					 Speech (TTS) TTS Server Software
                                             						(Required) TTS Ports (at least one is
                                             						required) | Composes
                                          					 voice prompts that are generated in real time from text, such as speaking the
                                          					 words in the text of an email message. TTS is
                                          					 primarily used to convey information obtained from a database or other source
                                          					 that is non-repetitive. Examples of such information include name and address
                                          					 verification. Repetitive information, such as numbers comprising an account
                                          					 balance, normally is not conveyed using TTS. Although
                                          					 text to speech technology has improved greatly since its inception, the tone
                                          					 still sounds mechanical. So it is best used only when the information
                                          					 possibilities make wave file generation impossible. |
| EMail | Adds
                                          					 components to the Unified CCX Engine that allows it to send email messages. |
| Database | Handles the
                                          					 connections between the Unified CCX server and the enterprise database. Also
                                          					 provides Open Database Connectivity (ODBC) support. See Compatibility Information for the latest versions of the database software that are supported at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html . |
| Inbound HTTP
                                          					 Request | Adds
                                          					 components to the Unified CCX Engine that allow it to respond to HTTP requests. |
| Voice
                                          					 Browser | Manages
                                          					 Voice Browser functionality. |

| Sample Script Template | Description |
|---|---|
| Auto Attendant | Allows a caller to call an agent by entering an extension number or the first few characters of an associated username. If
                                          ASR is enabled, the caller may simply speak the extension or the user name. |
| Spoken Name Upload | Enables Unified CM users to call in, authenticate their identities, and replace their spoken names with newly recorded announcements
                                          on their telephones |
| Voice Browser | Uses ASR functionality to allow a caller to access information from VoiceXML-enabled web sites. |