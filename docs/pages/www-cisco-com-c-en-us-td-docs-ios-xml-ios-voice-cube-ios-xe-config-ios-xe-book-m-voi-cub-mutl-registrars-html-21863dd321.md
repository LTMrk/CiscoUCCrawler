---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-cub-mutl-registrars-html-21863dd321
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-cub-mutl-registrars.html
retrieved_at: 2026-08-16T15:47:48.371760+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Multiple Registrars on SIP Trunks

## Chapter: Multiple Registrars on SIP Trunks

# Multiple Registrars on SIP Trunks

The support for Multiple Registrars on SIP Trunks on a Cisco Unified Border Element, on Cisco IOS SIP TDM Gateways, and on
                        a Cisco Unified Communications Manager Express feature allows configuration of multiple registrars on Session Initiation Protocol
                        (SIP) trunks, each simultaneously registered using its respective authentication instance. The support for this feature is
                        expanded to include the Cisco ASR 1000 Series Router. This feature allows a redundant registrar for each of the SIP trunks,
                        which provides SIP trunk redundancy across multiple service providers.

## Feature Information for the Multiple Registrars on SIP Trunks Feature

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

Multiple Registrars on SIP Trunks

Baseline Functionality

This feature provides support for multiple registrars on SIP trunks on Cisco IOS SIP TDM gateways, Cisco Unified CME, and
                                          Cisco UBEs. This feature allows for a redundant registrar for each SIP trunk and enables registrar redundancy across multiple
                                          service providers.

The following commands were new or modified: credentials , localhost , registrar , voice-class sip localhost

## Restrictions for Multiple Registrars on SIP Trunks

The Support for Multiple Registrars on SIP trunks feature has the following restrictions:

Old and new forms of the registrar command are mutually exclusive: the registrar can be configured in either primary/secondary mode or multiple registrar mode--not
                                 both.

Dynamic Host Configuration Protocol (DHCP) support is not available with multiple registrars (available for primary/secondary
                                 mode only).

Only one authentication configuration per username can be configured at any one time.

A maximum of six registrars can be configured at any given time.

A maximum of 12 different realms can be configured for each endpoint.

You cannot restrict the registration of specific endpoints with specific registrars--once a new registrar is configured, all
                                 endpoints will begin registering to the new registrar.

You cannot remove multiple configurations of credentials simultaneously--only one credential can be removed at a time.

## Configure Multiple Registrars on SIP Trunks

For information about the Support for Multiple Registrars on SIP Trunks feature and for detailed procedures for enabling this feature, see Configure Multiple Registrars on SIP Trunks .

| Feature Name | Releases | Feature Information |
|---|---|---|
| Multiple Registrars on SIP Trunks | Baseline Functionality | This feature provides support for multiple registrars on SIP trunks on Cisco IOS SIP TDM gateways, Cisco Unified CME, and
                                          Cisco UBEs. This feature allows for a redundant registrar for each SIP trunk and enables registrar redundancy across multiple
                                          service providers. The following commands were new or modified: credentials , localhost , registrar , voice-class sip localhost |