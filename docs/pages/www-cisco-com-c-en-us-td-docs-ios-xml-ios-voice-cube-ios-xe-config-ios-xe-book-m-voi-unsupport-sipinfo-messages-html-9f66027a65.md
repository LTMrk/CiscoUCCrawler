---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-unsupport-sipinfo-messages-html-9f66027a65
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi_unsupport_sipinfo_messages.html
retrieved_at: 2026-08-16T15:48:33.683444+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Pass-Through of Unsupported Content Types in SIP INFO Messages

## Chapter: Pass-Through of Unsupported Content Types in SIP INFO Messages

# Pass-Through of Unsupported Content Types in SIP INFO Messages

## Overview

This feature allows the CUBE to pass-through all unsupported content types in a SIP INFO message.

The Support for Pass-Through of Unsupported Content Types in SIP INFO Messages feature allows the CUBE to pass-through all unsupported content types in a SIP INFO message.

Upon receipt of a SIP INFO message with unsupported content type, CUBE triggers a SIP INFO message on the outgoing peer call leg. The response received for this SIP INFO message is triggered on
                           the incoming peer call leg and information flows end-to-end.

Supported content types include the following:

application/sdp

application/qsig

application/media-control+xml

application/x-q931

application/gtd

application/simple-message-summary

application/kpml-response+xml

application/dtmf-relay

application/broadsoft

message/sipfrag

audio/telephone-event

multpart/mixed

application/x-cisco-record+json

## Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Releases

Feature
                                       					 Information

Support
                                       					 for pass-through of unsupported content types in SIP INFO messages

Baseline functionality

This feature allows CUBE to pass-through SIP INFO methods or request message types with unsupported content types. Media negotiation and media exchange
                                       is completely end-to-end.

## Configure to Pass-through All Unsupported Content Types in a SIP INFO Messages

You must enable the pass-thru content
                                 			 unsupp command to pass-through all unsupported content types in a
                           		SIP INFO message. There is no additional configuration task required for this
                           		feature.

| Feature Name | Releases | Feature
                                       					 Information |
|---|---|---|
| Support
                                       					 for pass-through of unsupported content types in SIP INFO messages | Baseline functionality | This feature allows CUBE to pass-through SIP INFO methods or request message types with unsupported content types. Media negotiation and media exchange
                                       is completely end-to-end. |