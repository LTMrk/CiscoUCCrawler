---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x15-0-ip-port-exwy-b-cisco-expressway-ip-port-usage--675a680009
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X15-0/ip-port/exwy_b_cisco-expressway-ip-port-usage-configuration-guide-x15/exwy_m_how-to-use-this-guide.html
retrieved_at: 2026-08-16T15:14:49.926514+00:00
---

Cisco Expressway IP Port Usage Configuration Guide (Includes X14.3 and X15.0 releases)

# Cisco Expressway IP Port Usage Configuration Guide (Includes X14.3 and X15.0 releases)

Updated: January 11, 2024

Chapter: How To Use This Guide

## Chapter: How To Use This Guide

- How To Use This Guide

- Change History

- Related Documentation

# How To Use This Guide

The purpose of this guide is to help you configure and troubleshoot connections between infrastructure components related
                        to Expressway deployments.

There is a section for each of the popular Expressway deployments. Each has a diagram showing the major infrastructure components
                        and the connections between them, and also lists the connections in a table format.

The deployments build on each other where necessary. For example, if you want to implement Mobile and Remote Access (MRA),
                        you first configure a traversal pair. These relationships are described in the relevant deployment guides.

References in the guide to TLS (transport layer security protocol) as transport, in the context of Expressway effectively
                        mean the same thing as the underlying TCP transport protocol on which TLS is built.

This chapter explains the following:

## Change History

Date

Change

Reason

January 2024

Addressed CDETS - Includes updates for X14.3 and X15.0

X15.0 release

May 2020

Updated for X12.6

X12.6 release

April 2020

Correction

Fix entry for Tunneled media in Web Proxy for Meeting Server Port Reference table from port 443 to 3478. Also clarify TLS
                                          as transport is the same thing as TCP in context of this guide.

March 2020

Correction

Add missing Webbridge signaling entries to Web Proxy for Meeting Server Port Reference table.

February 2020

Correction

MRA connection for Headset Configuration file fixed to HTTPS/TLS.

December 2019

Update

In the Point to Point Microsoft Interoperability Using Meeting Server diagram, show media paths both with and without Meeting
                                          Server load balancing.

July 2019

Update

Updated the MRA Connections for Headset Management.

May 2019

Update

NAT reflection is not needed for Web Proxy for CMS connection (only for standalone Expressways).

February 2019

Update

Added details on how to configure NAT reflection on firewall for Web Proxy for Meeting Server.

January 2019

Updated for X12.5

X12.5 release. ACME certificates, SIP OAuth, and ICE passthrough for MRA.

September 2018

Update

Updated software version from X8.11 to X8.11.1 (version X8.11 withdrawn).

August 2018

Corrections

Errors in IM&P Federation with Microsoft Clients and Web Proxy for Cisco Meeting Server connections.

July 2018

Updated for X8.11

X8.11 release

April 2018

Corrections

Errors in SIP Edge for CMS media connections.

December 2017

Corrections

For SIP traversal calls, B2BUA on Expressway-C may need to make TURN requests to Expressway-E.

November 2017

Corrections

Errors in Web Proxy media connections.

July 2017

Update

X8.10 release. TURN listening port configurable to 443.

April 2017

New document

New format for information previously held in Expressway IP Port Usage for Firewall Traversal .

## Related Documentation

Support Videos

Videos provided by Cisco TAC engineers about certain common Expressway configuration procedures are available on the Expressway/VCS Screencast Video List page.

Installation - Virtual Machines

Cisco Expressway on Virtual Machine Installation Guide on the Expressway install and upgrade guides page

Installation - Physical Appliances

Cisco Expressway CE1200 Appliance Installation Guide on the Expressway install and upgrade guides page

Basic configuration for registrar / single systems

Cisco Expressway Registrar Deployment Guide on the Expressway configuration guides page

Basic configuration for firewall traversal / paired systems

Cisco Expressway-E and Expressway-C Basic Configuration Deployment Guide on the Expressway configuration guides page

Administration and maintenance

Cisco Expressway Administrator Guide on the Expressway maintain and operate guides page

Cisco Expressway Serviceability Guide on the Expressway maintain and operate guides page

Clusters

Cisco Expressway Cluster Creation and Maintenance Deployment Guide on the Expressway configuration guides page

Certificates

Cisco Expressway Certificate Creation and Use Deployment Guide on the Expressway configuration guides page

MRA

Mobile and Remote Access Through Cisco Expressway on the Expressway configuration guides page

Cisco Meeting Server

Cisco Meeting Server with Cisco Expressway Deployment Guide on the Expressway configuration guides page

Cisco Meeting Server API Reference Guide on the Cisco Meeting Server programming guides page

Other Cisco Meeting Server guides are available on the Cisco Meeting Server configuration guides page

Cisco Webex Hybrid Services

Hybrid services knowledge base

Cisco Hosted Collaboration Solution (HCS)

HCS customer documentation

Microsoft infrastructure

Cisco Expressway with Microsoft Infrastructure Deployment Guide on the Expressway configuration guides page

Cisco Jabber and Microsoft Skype for Business Infrastructure Configuration Cheatsheet on the Expressway configuration guides page

Rest API

Cisco Expressway REST API Summary Guide on the Expressway configuration guides page (high-level information only as the API is self-documented)

Multiway Conferencing

Cisco TelePresence Multiway Deployment Guide on the Expressway configuration guides page

| Date | Change | Reason |
|---|---|---|
| January 2024 | Addressed CDETS - Includes updates for X14.3 and X15.0 | X15.0 release |
| May 2020 | Updated for X12.6 | X12.6 release |
| April 2020 | Correction | Fix entry for Tunneled media in Web Proxy for Meeting Server Port Reference table from port 443 to 3478. Also clarify TLS
                                          as transport is the same thing as TCP in context of this guide. |
| March 2020 | Correction | Add missing Webbridge signaling entries to Web Proxy for Meeting Server Port Reference table. |
| February 2020 | Correction | MRA connection for Headset Configuration file fixed to HTTPS/TLS. |
| December 2019 | Update | In the Point to Point Microsoft Interoperability Using Meeting Server diagram, show media paths both with and without Meeting
                                          Server load balancing. |
| July 2019 | Update | Updated the MRA Connections for Headset Management. |
| May 2019 | Update | NAT reflection is not needed for Web Proxy for CMS connection (only for standalone Expressways). |
| February 2019 | Update | Added details on how to configure NAT reflection on firewall for Web Proxy for Meeting Server. |
| January 2019 | Updated for X12.5 | X12.5 release. ACME certificates, SIP OAuth, and ICE passthrough for MRA. |
| September 2018 | Update | Updated software version from X8.11 to X8.11.1 (version X8.11 withdrawn). |
| August 2018 | Corrections | Errors in IM&P Federation with Microsoft Clients and Web Proxy for Cisco Meeting Server connections. |
| July 2018 | Updated for X8.11 | X8.11 release |
| April 2018 | Corrections | Errors in SIP Edge for CMS media connections. |
| December 2017 | Corrections | For SIP traversal calls, B2BUA on Expressway-C may need to make TURN requests to Expressway-E. |
| November 2017 | Corrections | Errors in Web Proxy media connections. |
| July 2017 | Update | X8.10 release. TURN listening port configurable to 443. |
| April 2017 | New document | New format for information previously held in Expressway IP Port Usage for Firewall Traversal . |

| Support Videos | Videos provided by Cisco TAC engineers about certain common Expressway configuration procedures are available on the Expressway/VCS Screencast Video List page. |
|---|---|
| Installation - Virtual Machines | Cisco Expressway on Virtual Machine Installation Guide on the Expressway install and upgrade guides page |
| Installation - Physical Appliances | Cisco Expressway CE1200 Appliance Installation Guide on the Expressway install and upgrade guides page |
| Basic configuration for registrar / single systems | Cisco Expressway Registrar Deployment Guide on the Expressway configuration guides page |
| Basic configuration for firewall traversal / paired systems | Cisco Expressway-E and Expressway-C Basic Configuration Deployment Guide on the Expressway configuration guides page |
| Administration and maintenance | Cisco Expressway Administrator Guide on the Expressway maintain and operate guides page Cisco Expressway Serviceability Guide on the Expressway maintain and operate guides page |
| Clusters | Cisco Expressway Cluster Creation and Maintenance Deployment Guide on the Expressway configuration guides page |
| Certificates | Cisco Expressway Certificate Creation and Use Deployment Guide on the Expressway configuration guides page |
| MRA | Mobile and Remote Access Through Cisco Expressway on the Expressway configuration guides page |
| Cisco Meeting Server | Cisco Meeting Server with Cisco Expressway Deployment Guide on the Expressway configuration guides page Cisco Meeting Server API Reference Guide on the Cisco Meeting Server programming guides page Other Cisco Meeting Server guides are available on the Cisco Meeting Server configuration guides page |
| Cisco Webex Hybrid Services | Hybrid services knowledge base |
| Cisco Hosted Collaboration Solution (HCS) | HCS customer documentation |
| Microsoft infrastructure | Cisco Expressway with Microsoft Infrastructure Deployment Guide on the Expressway configuration guides page Cisco Jabber and Microsoft Skype for Business Infrastructure Configuration Cheatsheet on the Expressway configuration guides page |
| Rest API | Cisco Expressway REST API Summary Guide on the Expressway configuration guides page (high-level information only as the API is self-documented) |
| Multiway Conferencing | Cisco TelePresence Multiway Deployment Guide on the Expressway configuration guides page |