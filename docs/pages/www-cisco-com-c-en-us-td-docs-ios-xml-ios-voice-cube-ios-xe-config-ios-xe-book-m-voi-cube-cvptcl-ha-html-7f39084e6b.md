---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-cube-cvptcl-ha-html-7f39084e6b
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-cube-cvptcl-ha.html
retrieved_at: 2026-08-16T15:53:41.485402+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: CVP Survivability TCL support with High Availability

## Chapter: CVP Survivability TCL support with High Availability

# CVP Survivability TCL support with High Availability

## Overview

Call survivability
                           		features are supported in Cisco Unified Border Element (CUBE) high availability
                           		mode for all active calls handled by Cisco Voice Portal (CVP).

Contact Center Deployments use call survivability TCL script on CUBE to provide basic Call survivability services when downstream
                           CVP nodes are not reachable. From Cisco IOS Release 15.6(2)T onwards, call survivability features are supported in CUBE High
                           Availability mode. Post switchover, all events received on the calls handled by CVP are posted to Call Survivability TCL application
                           for further processing. Thus, call survivability features are supported in CUBE high availability mode for all active calls
                           handled by CVP.

For more information on CVP Call Survivability TCL, refer to http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp9_0/configuration/guide/cvp-configuration-and-administration-guide.pdf

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature
                                          				  Name

Releases

Feature
                                          				  Information

CVP
                                          				  Survivability TCL support with High Availability

Baseline Functionality

This feature enables CUBE support call survivability features in CUBE high availability mode for all active calls handled by CVP.

## Prerequisites

CVP survivability TCL application is configured on incoming dial-peer.

## Restrictions

If there is a
                                 			 courtesy callback (CCB) registered with CVP, then post switchover, CCB is not
                                 			 supported.

Only call
                                 			 survivability TCL script is supported with CUBE high availability. Other TCL
                                 			 based services are not supported.

Only the active calls will be check pointed. (Calls which are
                                 			 connected - 200OK / ACK transaction completed). Calls in transition state will
                                 			 not be check pointed.

## Recommendations

Configure TCP session transport for the SIP trunk between CUBE and CVP.

## Configure CVP Survivability TCL support with High Availability

Existing configuration of applying the survivability TCL applicationon incoming dial-peer is sufficient. No additional configuration
                           required.

| Feature
                                          				  Name | Releases | Feature
                                          				  Information |
|---|---|---|
| CVP
                                          				  Survivability TCL support with High Availability | Baseline Functionality | This feature enables CUBE support call survivability features in CUBE high availability mode for all active calls handled by CVP. |