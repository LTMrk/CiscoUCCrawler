---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-sip-update-html-6b400fadd2
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-sip-update.html
retrieved_at: 2026-08-16T15:47:23.322169+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: SIP UPDATE Message per RFC 3311

## Chapter: SIP UPDATE Message per RFC 3311

# SIP UPDATE Message per RFC 3311

## SIP UPDATE Message per RFC
                        	 3311

The SIP UPDATE
                           		Message per RFC 3311 feature provides Session Description Protocol (SDP)
                           		support for Session Initiation Protocol (SIP)-to-SIP calls. The SIP Service
                           		Provider Interface (SPI) is modified to support the following media changes
                           		using the UPDATE message:

Early dialog
                                 			 SIP-to-SIP media changes.

Mid dialog
                                 			 SIP-to-SIP media changes.

The Support for SIP
                           		UPDATE Message Per RFC 3311 feature is enabled by default on the Cisco Unified
                           		Border Element (UBE) and no configuration is required.

### Feature Information for the SIP UPDATE Message per RFC 3311

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

Support for SIP UPDATE Message per RFC 3311

Baseline Functionality

The Support for SIP UPDATE Message per RFC 3311 feature provides Session Description Protocol (SDP) support for Session Initiation
                                             Protocol (SIP)-to-SIP calls. The SIP Service Provider Interface (SPI) is modified to support the following media changes using
                                             the UPDATE message:

Early dialog SIP-to-SIP media changes

Mid dialog SIP-to-SIP media changes

### Prerequisites for SIP UPDATE
                           	 Message per RFC 3311

At least one offer or answer negotiation must be completed for Cisco UBE to handle the UPDATE message with SDP.

An early dialog UPDATE message with SDP is processed only when both endpoints support the UPDATE message.

For early dialog, both SIP endpoints must support PRACK and UPDATE
                                    			 method. Initial Offer-Answer must be completed with reliable provisional
                                    			 responses.

### Restrictions for SIP UPDATE
                           	 Message per RFC 3311

An UPDATE message
                                    			 with SDP is not supported for SIP-to-H323 calls.

An UPDATE message
                                    			 with SDP with a fully qualified domain name (FQDN) is not supported.

Contact
                                    			 information in the UPDATE message is not supported.

A retransmitted
                                    			 UPDATE message with SDP is ignored by the SIP stack. No response is sent for
                                    			 retransmitted UPDATE messages.

CUBE rejects UPDATE with SDP in early dialog when peer SIP leg does
                                    			 not support UPDATE.

### Information About
                           	 SIP UPDATE Message per RFC 3311

The SIP Update per
                              		RFC 3311 feature uses existing mid-call SDP processing logic to negotiate the
                              		Offer-Answer with UPDATE, so all media features supported in CUBE with
                              		Re-INVITE are supported with UPDATE.

The images below
                              		illustrate the call flows when one call-leg supports UPDATE and the other leg
                              		does not support UPDATE in early dialog and mid-call dialog.

| Feature Name | Releases | Feature Information |
|---|---|---|
| Support for SIP UPDATE Message per RFC 3311 | Baseline Functionality | The Support for SIP UPDATE Message per RFC 3311 feature provides Session Description Protocol (SDP) support for Session Initiation
                                             Protocol (SIP)-to-SIP calls. The SIP Service Provider Interface (SPI) is modified to support the following media changes using
                                             the UPDATE message: Early dialog SIP-to-SIP media changes Mid dialog SIP-to-SIP media changes |