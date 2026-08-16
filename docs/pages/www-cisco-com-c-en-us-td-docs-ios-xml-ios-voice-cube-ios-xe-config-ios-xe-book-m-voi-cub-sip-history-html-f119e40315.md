---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-cub-sip-history-html-f119e40315
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-cub-sip-history.html
retrieved_at: 2026-08-16T15:47:44.112071+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: SIP History INFO

## Chapter: SIP History INFO

- SIP History INFO

- Feature Information for SIP History-info Header

- Configure SIP History INFO

# SIP History INFO

The SIP History-info Header Support feature provides support for the history-info header in SIP INVITE messages only. The
                        SIP gateway generates history information in the INVITE message for all forwarded and transferred calls. The history-info
                        header records the call or dialog history. The receiving application uses the history-info header information to determine
                        how and why the call has reached it.

## Feature Information for SIP History-info Header

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

SIP History-info Header

Baseline Functionality

The SIP History-info feature provides the capability for the SIP TDM gateway to generate History-info messages in the INVITE
                                          dialog for calls that are forwarded or transferred. Cisco Unified Border Element platforms transparently pass the History-info
                                          across SIP legs. The receiving application uses the history-info header information to determine how and why the call has
                                          reached it.

The following commands were introduced or modified: history-info , and voice-class sip history-info

## Configure SIP History INFO

To configure the SIP History INFO feature, see Configuring SIP History-info Header Support .

| Feature Name | Releases | Feature Information |
|---|---|---|
| SIP History-info Header | Baseline Functionality | The SIP History-info feature provides the capability for the SIP TDM gateway to generate History-info messages in the INVITE
                                          dialog for calls that are forwarded or transferred. Cisco Unified Border Element platforms transparently pass the History-info
                                          across SIP legs. The receiving application uses the history-info header information to determine how and why the call has
                                          reached it. The following commands were introduced or modified: history-info , and voice-class sip history-info |