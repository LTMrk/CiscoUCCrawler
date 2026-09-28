---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-courtesy-callback-support-for-srtp-html-61c88e294e
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_courtesy-callback-support-for-srtp.html
retrieved_at: 2026-08-16T23:12:54.517508+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Advanced Features for Cisco Contact Center

## Chapter: Advanced Features for Cisco Contact Center

# Advanced Features for Cisco Contact Center

## Overview

Using the survivability.tcl script, CUBE can complement the Cisco Contact Center Enterprise solution with several unique features.

Courtesy Call Back: With the Cisco Voice Portal (CVP) application, a caller may request an automated callback, rather than
                                 wait in a queue for an extended period. When an agent becomes available, CVP sends a request to place a call to the original
                                 caller. When the call is answered, the agent is connected.

Contact Center Survivability: If there is a failure when connecting to an agent, the script takes control of the call and
                                 redirects it to a preconfigured destination. If the call cannot be redirected, a pre-recorded announcement from a local file
                                 is played out to the caller before disconnecting the call.

Before Cisco IOS XE Cupertino
                                 17.9.1a , these features were only available for unencrypted PSTN trunks. From Cisco IOS XE Cupertino
                                 17.9.1a , they may also be used with encrypted (SRTP) trunks.

For more information about CCB and callback criteria, see Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(1) .

## Feature Information Survivability.tcl Script for Contact Center

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

## Restrictions

SRTP passthru cannot be used with Courtesy Call Back.

| Feature Name | Releases | Feature Information |
|---|---|---|