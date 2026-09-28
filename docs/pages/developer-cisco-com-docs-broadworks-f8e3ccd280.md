---
doc_id: developer-cisco-com-docs-broadworks-f8e3ccd280
source_url: https://developer.cisco.com/docs/broadworks/
retrieved_at: 2026-08-24T22:11:34.938970+00:00
---

## What is BroadWorks?

Cisco BroadWorks is a carrier-grade unified communication software platform, optimized for performance and scale. BroadWorks is hosted by service providers to deploy cloud calling from a common network platform over any type of wired or wireless network architecture.

Cisco BroadWorks can be deployed for use in a single business service, or a combination of cloud UC (IP Centrex), mobile PBX, and business SIP trunk applications.  Service Providers can find the widest range of features from a single, multi-tenant, network-based system, including call control, private voice networking, and unified messaging.

## Cisco BroadWorks at a glance

Standards-based next-generation platform - Deployed at the network core, Cisco BroadWorks provides features through multiple architectures, including Softswitch, Class 5, and IP Multimedia Subsystem (IMS). It provides unmatched interoperability, back office capabilities, redundancy, and scalability.

Industry standard hosting - Cisco BroadWorks operates on Linux or Solaris operating systems and is supported on traditional server hardware, virtual machine or commercial cloud hosted environments. The software architecture accommodates NFV, SDN and OpenCloud with functionality distributed across scalable BroadWorks application, media, network, conferencing, session border, external web, call logging, and element management servers.

Open architecture - Cisco BroadWorks is designed, built and operates on open standards. These include interfaces based on IETF, 3GPP, ETSI, and other industry RFCs as well as open XML-based APIs published and supported by Cisco. This open philosophy ensures the hosting partner has access to the broadest array of network, user devices, applications and back office tools.

Unmatched scale and reliability – The Cisco cloud-scale and micro-services architecture allows scale to hundreds of millions of subscribers in a single managed logical entity.  BroadWorks resilient and distributed designs exceed “5 9s” carrier-grade reliability, delivering service 99.999 % of the time with server elements which can be deployed across cities, states, or even continents.

Multi-tenancy – With BroadWorks, Service Providers can build a true cloud-native service that effectively supports business customers from a single person up to 100,000s of users, on a single call control platform to manage, operate, patch, and integrate into their back office and business processes.

Choice of feature-rich web-based and client apps - BroadWorks supports multiple web-based, PC and mobile applications that enhance collaboration feature use, configuration and user productivity. Users can carry their uniform identity and multimedia services across mobile phones, desk phones, tablets, or PC desktop apps, and even move active calls seamlessly from device to device.

Flexible multitiered administration - System APIs allow the BroadWorks platform to integrate tightly within the Service Provider’s operational workflow and modern digital engagement strategy.  BroadWorks provides web-based service administration hierarchy with six distinct levels. This flexibility allows support for resellers and development of a third-party channel ecosystem.

## Cisco BroadWorks Developer Interfaces

SIP/SIPREC Interface - BroadWorks supports RFC-based SIP and SIPREC signaling methods for deep integration with compatible systems, applications and devices.  Common uses for SIP signaling include IP telephones, calling apps (PC, mobile), attendant consoles apps, analog terminal adapters, SIP media gateways, IP PBX, network core Session Border Controllers (SBC), network edge Session Border Controllers (eSBC), and call recording applications to name a few.

XSI (eXtended Services Interface) – XSI is a family of BroadWorks APIs that allow resources to be addressed over HTTP using simple XML.  XSI can be used to develop distinct applications or middleware services to communication enable existing CRM, HRM, or service desk applications.

XSI is very scalable and designed to be used securely over multiple protocols by different types of applications.  The XSI interface informs external applications when BroadWorks subscriber activity occurs.  The CTI notifications occur when an application subscribes for one or more events from a set of available event packages.

### Types of events include:

• Call Events – Provides notification of real-time call information on active calls.

• Service Events – Provides notification when service configuration has been changed.

• Route Point and ACD Events – Provides notification of real-time information on incoming and queued calls.

OCI-P (Open Client Interface – Provisioning) - OCI-P allows a developer’s application to securely connect and perform provisioning changes to the core BroadWorks system and subscriber data. OCI-P is an extremely comprehensive interface.

CDR Interfaces - The BroadWorks application transmission of accounting data is performed either by sending accounting files with many CDRs over FTP, or by sending CDRs one at a time, in real-time, using the Radius protocol (RFC2866 compliant).

IMS Interfaces - The BroadWorks Application Server (AS) is an IMS Session Initiation Protocol (SIP)
Application Server located within the mobile operator’s IMS application layer. All BroadWorks servers use standard IMS interfaces, including Sh, ISC, Ro, Rf, Mb, and Mr to communicate with other BroadWorks servers and third-party IMS components.

SNMP Interfaces – Individual BroadWorks servers provides notifications and alarms with alarm correlation for external management applications using SNMP v2c and v3.

HID Interfaces - Various BroadWorks PC and mobile device applications take advantage of HID compliant interface signaling for answer, mute, and volume control.

## In summary

Cisco BroadWorks is designed to enable all service providers to rapidly launch new or migrate legacy communications services using next-generation cloud architectures, which offer significant operational and competitive advantages.  Cisco BroadWorks Developers can take advantage of the various open interfaces to create value-added user and operational applications which BroadWorks Service Providers consume.

With well over 600 service provider deployments globally, BroadWorks is acknowledged as the market share leader for cloud-based communications services. That’s why 25 out of the top 30 providers by revenue worldwide have chosen the Cisco BroadWorks call control platform.

For additional information, visit Cloud Calling on cisco.com.

Next