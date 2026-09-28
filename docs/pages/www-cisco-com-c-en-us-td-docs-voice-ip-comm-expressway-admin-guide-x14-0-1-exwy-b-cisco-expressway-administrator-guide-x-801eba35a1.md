---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-admin-guide-x14-0-1-exwy-b-cisco-expressway-administrator-guide-x-801eba35a1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/admin_guide/X14-0-1/exwy_b_cisco-expressway-administrator-guide-x14-0-1/exwy_m_introduction.html
retrieved_at: 2026-08-16T22:41:20.375938+00:00
---

Cisco Expressway Administrator Guide (X14.0.1)

# Cisco Expressway Administrator Guide (X14.0.1)

Updated: June 2, 2021

Chapter: Introduction

## Chapter: Introduction

# Introduction

## About the Expressway

Cisco Expressway Series (Expressway) is designed specifically for comprehensive
                           			collaboration services. It features established firewall-traversal technology and helps
                           			to redefine traditional enterprise collaboration boundaries, to support our Cisco vision
                           			of any-to-any collaboration.

Expressway offers the following primary features and benefits:

Provides proven, highly secure, firewall-traversal technology.

Facilitates connections for business-to-business, business-to-consumer, and
                                 					business-to-cloud-service-provider.

Facilitates session-based access to collaboration services for remote workers,
                                 					with no need for a separate VPN client.

Supports a wide range of devices, including Cisco Jabber for smartphones,
                                 					tablets, and desktops.

Complements bring-your-own-device strategies and policies for remote and mobile
                                 					workers.

A typical Expressway system is deployed as a pair: an Expressway-C with a trunk and
                           			line-side connection to Unified CM, and an Expressway-E deployed in the DMZ and
                           			configured with a traversal zone to an Expressway-C.

Expressway is available on a dedicated physical appliance such as a CE12100, or as a
                           			virtual machine (VM) on a Cisco UCS server.

### Expressway Types

Each Expressway can be configured as one of two types, which offer different
                                 				capabilities.

#### Expressway-C

Expressway-C delivers any-to-any enterprise wide conference and session management
                                 				and interworking capabilities. It extends the reach of telepresence conferences by
                                 				enabling interworking between Session Initiation Protocol (SIP)- and H.323-compliant
                                 				endpoints, interworking with third-party endpoints; it integrates with Unified CM
                                 				and supports third-party IP private branch exchange (IP PBX) solutions. Expressway-C
                                 				implements the tools required for creative session management, including definition
                                 				of aspects such as routing, dial plans, and bandwidth usage, while allowing
                                 				organizations to define call-management applications, customized to their
                                 				requirements.

#### Expressway-E

The Expressway-E deployed with the Expressway-C enables smooth video communications
                                 				easily and securely outside the enterprise. It enables business-to-business video
                                 				collaboration, improves the productivity of remote and home-based workers, and
                                 				enables service providers to provide video communications to customers. The
                                 				application performs securely through standards-based and secure firewall traversal
                                 				for all SIP and H.323 devices. As a result, organizations benefit from increased
                                 				employee productivity and enhanced communication with partners and customers.

It uses an intelligent framework that allows endpoints behind firewalls to discover
                                 				paths through which they can pass media, verify peer-to-peer connectivity through
                                 				each of these paths, and then select the optimum media connection path, eliminating
                                 				the need to reconfigure enterprise firewalls.

The Expressway-E is built for high reliability and scalability, supporting
                                 				multivendor firewalls, and it can traverse any number of firewalls regardless of SIP
                                 				or H.323 protocol.

### Standard Features

Standard features on Expressway include the following:

Secure firewall traversal and session-based access to Cisco Unified
                                       						Communications Manager for remote workers, without the need for a separate
                                       						VPN client

Endpoint registration support.

SIP Registrar (requires Room or Desktop SIP Proxy. Note that SIP and H.323 protocols are
                                       						disabled by default on new installs, and can be enabled from Configuration > Protocols Registration licenses.)

SIP and H.323 support, including SIP / H.323 interworking

IPv4 and IPv6 support, including IPv4 / IPv6 interworking

TURN relay licenses

Advanced networking

Device provisioning and FindMe services

H.323 gatekeeper

QoS tagging

Bandwidth management on both a per-call and a total usage basis, configurable
                                       						separately for calls within the local subzones and to external systems and
                                       						zones

Automatic downspeeding option for calls that exceed the available
                                       						bandwidth

URI and ENUM dialing via DNS, enabling global connectivity

Rich media session (RMS) support

1000 external zones with up to 2000 matches

1000 subzones and supporting up to 3000 membership rules

Flexible zone configuration with prefix, suffix and regex support

Can function as a standalone Expressway, or be neighbored with other systems
                                       						such as other Expressways, gatekeepers and SIP proxies

Can be clustered with up to 6 Expressways to provide n+1 redundancy, and up
                                       						to 4 x individual capacity.

Intelligent Route Director for single number dialing and network failover
                                       						facilities

Optional endpoint authentication

Control over which endpoints are allowed to register

Call Policy (also known as Administrator Policy) including support for
                                       						CPL

Support for external policy servers

Can be managed with Cisco TelePresence Management Suite 13.2 or later

Active Directory authentication

Pre-configured neighbor zone defaults for Cisco Unified Communications
                                       						Manager and for Nortel Communication Server

Embedded setup wizard using a serial port for initial configuration

System administration using a web interface or SSH, or via the CIMC port for a CE nnnn physical appliance

Intrusion protection

### Do Not Install Other Cisco or Third-Party Software onto Expressway

Cisco does not support the installation of any additional Cisco or third-party
                                 				software, applications, or agents on Expressway (VMs or physical appliances), unless
                                 				we state explicitly otherwise. Non-Expressway products may corrupt the Expressway
                                 				code and must not be installed.

### Hardware Appliance and Virtual Machine Options

Expressway supports on-premises and cloud applications and is available as a
                                 				dedicated appliance or as a virtualized application on VMware, with additional
                                 				support for Cisco Unified Computing System (Cisco UCS) platforms.

#### Virtual Machine Options

Expressway has these virtualized application deployment types:

Small (for Cisco Business Edition 6000 or supported VMware ESXi platforms,
                                       						subject to the required minimum hardware specification)

Medium (standard installation)

Large (extra performance and scalability capabilities)

See Cisco Expressway Virtual Machine Installation Guide on the Expressway Installation Guides page.

#### Hardware CE Series Appliances

The Expressway is also available as a dedicated CE Series appliance based on UCS
                                 				hardware. For example, the CE1200 appliance based on a UCS C220 M5L, operates as a
                                 				medium capacity or large capacity Expressway.

The Cisco VCS series is not supported on CE1200 appliances.

Changing the default system size

For appliances deployed as Expressway-E you can manually change the default system
                                 				size of appliances from Large to Medium, or the other way round. This capability was
                                 				introduced to mitigate an issue with demultiplexing ports for media traversal on
                                 				appliances with a 1 Gbps NIC (SFP module) that are configured as Medium systems.

To change the size of the appliance, go to System > Administration settings page and select the required size from the Deployment Configuration list.

#### Installation information

See Cisco Expressway CE1200 Appliance Installation Guide on the Expressway Installation Guides page.

## About This Guide

This guide describes the various features, services, and capabilities of Expressway. It
                           			assumes a fully equipped version of Expressway, so your deployment may not support all
                           			of the items described.

The guide only applies to the Cisco Expressway Series product. For information about Cisco VCS, please refer to the X12.5.x Cisco VCS Administrator Guide on the Cisco TelePresence Video Communication Server Maintain and Operate Guides page.

Most configuration tasks on Expressway can be done through the web user interface or the
                           			command line interface (CLI). The guide mainly describes how to use the web user
                           			interface. Some features are only available through the CLI, and these are described
                           			where relevant.

Web user interface directions are shown in the format Menu > Submenu followed by the Name of the page that you will be
                           			taken to.

CLI commands where provided, are shown in the format:

```
xConfiguration <Element> <SubElement>
xCommand <Command>
```

### Training

Training is available online and at our training locations. For more information on all the training we provide and where
                                 our training offices are located, visit www.cisco.com/go/telepresencetraining .

### Glossary

A glossary of TelePresence terms is available at: https://tp-tools-web01.cisco.com/start/glossary/ .

### Accessibility Notice

Cisco is committed to designing and delivering accessible products and
                                 				technologies.

The Voluntary Product Accessibility Template (VPAT) for Cisco Expressway is available
                                 				here:

http://www.cisco.com/web/about/responsibility/accessibility/legal_regulatory/vpats.html#telepresence

You can find more information about accessibility here:

http://www.cisco.com/web/about/responsibility/accessibility/index.html

### Related Documentation

Support videos

Videos provided by Cisco TAC engineers about certain common Expressway configuration procedures are available on the Expressway/VCS Screencast Video List page (search for "Expressway videos" )

Installation - virtual machines

Cisco Expressway Virtual Machine Installation Guide on the Expressway Installation Guides page

Installation - physical appliances

Cisco Expressway CE1200 Appliance Installation Guide on the Expressway Installation Guides page.

Basic configuration for single-box systems

Cisco Expressway Registrar Deployment Guide on the Expressway Configuration Guides page

Basic configuration for paired-box systems (firewall
                                             									traversal)

Cisco Expressway-E and Expressway-C Basic Configuration Deployment Guide on the Expressway Configuration Guides page

Administration and maintenance

CiscoExpressway Administrator Guide on the Expressway Maintain and Operate Guides page (includes Serviceability information)

Clustering

Cisco Expressway Cluster Creation and Maintenance Deployment Guide on the Expressway Configuration Guides page

Certificates

Cisco Expressway Certificate Creation and Use Deployment Guide on the Expressway Configuration Guides page

Ports

Cisco Expressway IP Port Usage Configuration Guide on the Expressway Configuration Guides page

Unified Communications

Mobile and Remote Access Through Cisco Expressway on the Expressway configuration guides page

Cisco Meeting Server

Cisco Meeting Server with Cisco Expressway Deployment Guide on the Expressway Configuration Guides page

Cisco Meeting Server API Reference Guide on the Cisco Meeting Server Programming Guides page

Other Cisco Meeting Server guides are available on the Cisco Meeting Server Configuration Guides page

Cisco Webex Hybrid Services

Hybrid services knowledge base

Cisco Hosted Collaboration Solution (HCS)

HCS customer documentation

Microsoft infrastructure

Cisco Expressway with Microsoft Infrastructure Deployment Guide on the Expressway Configuration Guides page

Cisco Jabber and Microsoft Skype for Business Infrastructure Configuration Cheatsheet on the Expressway configuration guides page

Rest API

Cisco Expressway REST API Summary Guide on the Expressway Configuration Guides page (high-level information only as the API is self-documented)

Multiway Conferencing

Cisco TelePresence Multiway Deployment Guide on the Expressway Configuration Guides page

## About the Service Setup Wizard (Service Selection Page)

The Service Setup Wizard makes it easier to configure Expressway for its chosen purpose in your environment, and simplifies
                           the web user interface. As well as running the wizard for initial configuration you can subsequently access its service selection
                           page at any time ( Status > Overview ). For more details about using the wizard, see the Cisco Expressway-E and Expressway-C - Basic Configuration guide on the Expressway Configuration Guides page.

If you use Smart Licensing, you cannot change the Series setting from the Service Selection page/wizard (to convert an Expressway to a VCS
                                       				product). Instead this process must start with a factory reset (to disable Smart
                                       				Licensing because it's not supported on VCS). Some of the other settings shown in
                                       				this example are unnecessary with Smart Licensing and do not appear in the wizard on
                                       				Expressways that use Smart Licensing.

### Services that can be Hosted Together

Some services are incompatible and cannot be selected together. The following table
                                 				provides a matrix of compatible services. The matrix specifies which services you
                                 				can use together on the same system or cluster.

Cisco Webex Hybrid Services (Connectors

Mobile and Remote Access

Jabber

Microsoft gateway server

Registrat

CMR Cloud

Business to Business calling (includes Hybrid Call Service)

Cisco Webex Hybrid Services (Connectors)

Y

N

N

N

N

Y

Y

Mobile and Remote Access and/or (from X8.9) Meeting Servere Web
                                             									Proxy

N

Y

N

N

Y

Y

Y*

Jabber Guest Services

N

N

Y

N

Y

Y

Y

Microsoft gateway service

N

N

N

Y

N

N

N

Registrar

N

Y

Y

N

Y

Y

Y

CMR Cloud

Y

Y

Y

N

Y

Y

Y

Business to Business calling (includes Hybrid Call Service)

Y

Y*

Y

N

Y

Y

Y

Key to Table

Y: Yes, these services can be hosted on the same system or cluster

N: No, these services may not be hosted on the same system or cluster

Rules

Hybrid Services connectors may co-reside with the Expressway-C of a traversal
                                       						pair used for Call Service, subject to user number limitations.

* If your Hybrid Call Service (or B2B) traversal pair is also used for MRA,
                                       						then the Hybrid Services connectors must be on a separate Expressway-C. This
                                       						is because we do not support the connectors being hosted on the Expressway-C
                                       						that is used for MRA.

Microsoft gateway service requires a dedicated VCS Control or Expressway-C (called "Gateway VCS" or "Gateway Expressway" in the help and documentation)

Jabber Guest cannot work with MRA (technical limitation)

MRA is currently not supported in IPv6 only mode. If you want IPv6 B2B
                                       						calling to co-reside with IPv4 MRA on the same Expressway traversal pair,
                                       						the Expressway-E and Expressway-C must both be in dual stack mode.

| Note | The Cisco VCS series is not supported on CE1200 appliances. |
|---|---|

| Support videos | Videos provided by Cisco TAC engineers about certain common Expressway configuration procedures are available on the Expressway/VCS Screencast Video List page (search for "Expressway videos" ) |
|---|---|
| Installation - virtual machines | Cisco Expressway Virtual Machine Installation Guide on the Expressway Installation Guides page |
| Installation - physical appliances | Cisco Expressway CE1200 Appliance Installation Guide on the Expressway Installation Guides page. |
| Basic configuration for single-box systems | Cisco Expressway Registrar Deployment Guide on the Expressway Configuration Guides page |
| Basic configuration for paired-box systems (firewall
                                             									traversal) | Cisco Expressway-E and Expressway-C Basic Configuration Deployment Guide on the Expressway Configuration Guides page |
| Administration and maintenance | CiscoExpressway Administrator Guide on the Expressway Maintain and Operate Guides page (includes Serviceability information) |
| Clustering | Cisco Expressway Cluster Creation and Maintenance Deployment Guide on the Expressway Configuration Guides page |
| Certificates | Cisco Expressway Certificate Creation and Use Deployment Guide on the Expressway Configuration Guides page |
| Ports | Cisco Expressway IP Port Usage Configuration Guide on the Expressway Configuration Guides page |
| Unified Communications | Mobile and Remote Access Through Cisco Expressway on the Expressway configuration guides page |
| Cisco Meeting Server | Cisco Meeting Server with Cisco Expressway Deployment Guide on the Expressway Configuration Guides page Cisco Meeting Server API Reference Guide on the Cisco Meeting Server Programming Guides page Other Cisco Meeting Server guides are available on the Cisco Meeting Server Configuration Guides page |
| Cisco Webex Hybrid Services | Hybrid services knowledge base |
| Cisco Hosted Collaboration Solution (HCS) | HCS customer documentation |
| Microsoft infrastructure | Cisco Expressway with Microsoft Infrastructure Deployment Guide on the Expressway Configuration Guides page Cisco Jabber and Microsoft Skype for Business Infrastructure Configuration Cheatsheet on the Expressway configuration guides page |
| Rest API | Cisco Expressway REST API Summary Guide on the Expressway Configuration Guides page (high-level information only as the API is self-documented) |
| Multiway Conferencing | Cisco TelePresence Multiway Deployment Guide on the Expressway Configuration Guides page |

| Note | If you use Smart Licensing, you cannot change the Series setting from the Service Selection page/wizard (to convert an Expressway to a VCS
                                       				product). Instead this process must start with a factory reset (to disable Smart
                                       				Licensing because it's not supported on VCS). Some of the other settings shown in
                                       				this example are unnecessary with Smart Licensing and do not appear in the wizard on
                                       				Expressways that use Smart Licensing. |
|---|---|

|  | Cisco Webex Hybrid Services (Connectors | Mobile and Remote Access | Jabber | Microsoft gateway server | Registrat | CMR Cloud | Business to Business calling (includes Hybrid Call Service) |
|---|---|---|---|---|---|---|---|
| Cisco Webex Hybrid Services (Connectors) | Y | N | N | N | N | Y | Y |
| Mobile and Remote Access and/or (from X8.9) Meeting Servere Web
                                             									Proxy | N | Y | N | N | Y | Y | Y* |
| Jabber Guest Services | N | N | Y | N | Y | Y | Y |
| Microsoft gateway service | N | N | N | Y | N | N | N |
| Registrar | N | Y | Y | N | Y | Y | Y |
| CMR Cloud | Y | Y | Y | N | Y | Y | Y |
| Business to Business calling (includes Hybrid Call Service) | Y | Y* | Y | N | Y | Y | Y |