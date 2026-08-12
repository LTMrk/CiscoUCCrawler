  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-http2-reset-d8Kf32vZ.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-http2-reset-d8Kf32vZ.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-http2-reset-d8Kf32vZ.html)


  * [Cisco.com Worldwide](https://www.cisco.com/site/us/en/index.html)
  * [Products and Services](https://www.cisco.com/site/us/en/products/index.html)
  * [Solutions](https://www.cisco.com/site/us/en/solutions/index.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Learn](https://www.cisco.com/site/us/en/learn/index.html)
  * [Explore Cisco](https://www.cisco.com/site/us/en/about/sitemap.html)
  * [How to Buy](https://www.cisco.com/site/us/en/buy/index.html)
  * [Partners Home](https://www.cisco.com/site/us/en/partners/index.html)
  * [Partner Program](https://www.cisco.com/site/us/en/partners/360-partner-program/partner-program/index.html)
  * [Support](https://www.cisco.com/site/us/en/partners/support-help/index.html)
  * [Tools](https://www.cisco.com/site/us/en/partners/360-partner-program/tools-training/index.html)
  * [Find a Cisco Partner](https://locatr.cloudapps.cisco.com/WWChannels/LOCATR/pf/index.jsp#/)
  * [Meet our Partners](https://www.cisco.com/site/us/en/partners/connect-with-a-partner/index.html)
  * [Become a Cisco Partner](https://www.cisco.com/site/us/en/partners/index.html)


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-http2-reset-d8Kf32vZ.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# HTTP/2 Rapid Reset Attack Affecting Cisco Products: October 2023
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-http2-reset-d8Kf32vZ.html) to Save Content 
Print
### Available Languages
Updated:December 21, 2023
Document ID:1697474309029108
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg)](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory 
# HTTP/2 Rapid Reset Attack Affecting Cisco Products: October 2023
High
Advisory ID: 
cisco-sa-http2-reset-d8Kf32vZ
First Published:
2023 October 16 16:00 GMT
Last Updated: 
2023 December 21 17:09 GMT
Version 1.11: 
[Final](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
No workarounds available
CVE-2023-44487
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-http2-reset-d8Kf32vZ.html)
CWE-400
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-http2-reset-d8Kf32vZ.html)
CVSS Score:
[ Base 7.5](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.1&vector=CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H)[![](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png)](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H/E:X/RL:X/RC:X
CVE-2023-44487
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-http2-reset-d8Kf32vZ.html)
CWE-400
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-http2-reset-d8Kf32vZ.html)
[ Download CSAF ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-http2-reset-d8Kf32vZ/csaf/cisco-sa-http2-reset-d8Kf32vZ.json)
Email 
## 
Summary 
  * On October 10, 2023, the following HTTP/2 protocol-level weakness, which enables a novel distributed denial of service (DDoS) attack technique, was disclosed:
CVE-2023-44487: HTTP/2 Rapid Reset 
For a description of this vulnerability, see the following publications:
    * [How it works: The novel HTTP/2 'Rapid Reset' DDoS attack](https://cloud.google.com/blog/products/identity-security/how-it-works-the-novel-http2-rapid-reset-ddos-attack) (Google)
    * [HTTP/2 Zero-Day vulnerability results in record-breaking DDoS attacks](https://blog.cloudflare.com/zero-day-rapid-reset-http2-record-breaking-ddos-attack/) (Cloudflare)
    * [ CVE-2023-44487 - HTTP/2 Rapid Reset Attack](https://aws.amazon.com/security/security-bulletins/AWS-2023-011/) (AWS)
This advisory is available at the following link:  
<https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-http2-reset-d8Kf32vZ>


## 
Affected Products 
  * Cisco investigated its product line to determine which products may be affected by this vulnerability.
The [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-http2-reset-d8Kf32vZ.html#vp) section includes Cisco bug IDs for each affected product. The bugs are accessible through the [Cisco Bug Search Tool](https://bst.cloudapps.cisco.com/bugsearch) and contain additional platform-specific information, including workarounds (if available) and fixed software releases.
Any product not listed in the Vulnerable Products section of this advisory is to be considered not vulnerable.
Cisco cloud-based offering have been remediated as required.
##  Vulnerable Products 
The following table lists Cisco products that are affected by the vulnerability that is described in this advisory. If a future release date is indicated for software, the date provided represents an estimate based on all information known to Cisco as of the Last Updated date at the top of the advisory. Availability dates are subject to change based on a number of factors, including satisfactory testing results and delivery of other priority features and fixes. Customers should refer to the associated Cisco bug(s) for further details.  
| Product  | Cisco Bug ID  | [Fixed Release Availability](https://tools.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes)  |  
| --- | --- | --- |  
| Network and Content Security Devices  |  
| Firepower Threat Defense (FTD) (Streaming Telemetry DIAL-IN mode feature)  | [CSCwi12388](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwi12388)  | 7.4.2 (Apr 2024)  |  
| Secure Dynamic Attribute Connector (CSDAC)  | [CSCwh89890](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh89890)  | 2.2.0  
2.3.0  |  
| Secure Malware Analytics Appliance, formerly Threat Grid Appliance  | [CSCwh88721](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88721)  | 2.19.2 (Feb 2024)  |  
| Secure Web Appliance, formerly Web Security Appliance (WSA)  | [CSCwh88595](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88595)  | 15.1.0 GA (Dec 2023)  
15.2.0  |  
| Network Management and Provisioning  |  
| Business Process Automation  | [CSCwh88580](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88580)  | 3.2.003.009 (Nov 2023)  
4.0.001.003 (Nov 2023)  
4.0.002.003 (Nov 2023)  |  
| Crosswork Data Gateway  | [CSCwh88729](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88729)  | 4.1.3 (Dec 2023)  
5.0.2 (Dec 2023)  
6.0.0  |  
| Crosswork Situation Manager  | [CSCwh88658](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88658)  | Contact Cisco TAC for upgrade options  |  
| Crosswork Zero Touch Provisioning (ZTP)  | [CSCwh88727](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88727)  | 6.0.0 (Dec 2023)  |  
| Data Center Network Manager (DCNM) - SAN Deployments on Windows or Linux  | [CSCwh88607](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88607)  | Apply [Workaround](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88607)  |  
| IoT Field Network Director, formerly Connected Grid Network Management System  | [CSCwh88604](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88604)  | 4.11.0  |  
| Prime Access Registrar  | [CSCwh88632](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88632)  | 9.3.3 (Feb 2024)  |  
| Prime Cable Provisioning  | [CSCwh91177](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh91177)  | 7.2.1 (Nov 2023)  |  
| Prime Infrastructure  | [CSCwh84581](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh84581)  | 3.10.4  |  
| Prime Network Registrar  | [CSCwh88631](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88631)  | 11.2  |  
| Routing and Switching - Enterprise and Service Provider  |  
| IOS XE Software (gNMI Server feature)  | [CSCwi23471](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwi23471)  | 17.15.1 (Aug 2024)  |  
| IOS XR Software (gRPC Protocol server feature)  | [CSCwi23456](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwi23456)  | 7.11.2 (Feb 2024)  
24.1.1 (Feb 2024)  |  
| IOx Fog Director  | [CSCwh89927](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh89927)  | 1.22 (Nov 2023)  |  
| Nexus 3000 Series Switches (NX-API feature)  | [CSCwh88614](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88614)  | 10.2(7) (Feb 2024)  
10.3(5) (May 2024)  
10.4(2)  |  
| Nexus 3000 Series Switches (gRPC Agent feature)  | [CSCwi13890](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwi13890)  | 10.4(3) (Mar 2024)  |  
| Nexus 9000 Series Switches in standalone NX-OS mode (NX-API feature)  | [CSCwh88614](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88614)  | 10.2(7) (Feb 2024)  
10.3(5) (May 2024)  
10.4(2)  |  
| Nexus 9000 Series Switches in standalone NX-OS mode (gRPC Agent feature)  | [CSCwi13890](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwi13890)  | 10.4(3) (Mar 2024)  |  
| Ultra Cloud Core - Policy Control Function  | [CSCwh88574](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88574)  | 2024.01.0 (Feb 2024)  |  
| Ultra Cloud Core - Serving Gateway Function  | [CSCwi11657](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwi11657)  | 2024.02.0 (May 2024)  |  
| Ultra Cloud Core - Session Management Function  | [CSCwh88576](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88576)  | 2024.02.0 (May 2024)  |  
| Voice and Unified Communications Devices  |  
| Enterprise Chat and Email  | [CSCwh88749](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88749)  | Apply Microsoft Windows Update or [Workaround](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88749)  |  
| Unified Attendant Console Advanced  | [CSCwh88736](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88736)  | Apply Microsoft Windows Update or [Workaround](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88736)  |  
| Unified Contact Center Domain Manager (CCDM)  | [CSCwh88737](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88737)  | Apply Microsoft Windows Update or [Workaround](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88737)  |  
| Unified Contact Center Enterprise (UCCE)  | [CSCwh88584](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88584)  | Apply Microsoft Windows Update or [Workaround](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88584)  |  
| Unified Contact Center Enterprise - Live Data server  | [CSCwh88583](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88583)  | 12.6.2 (Nov 2023)  |  
| Unified Contact Center Management Portal (CCMP)  | [CSCwh88737](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88737)  | Apply Microsoft Windows Update or [Workaround](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88737)  |  
| Video, Streaming, TelePresence, and Transcoding Devices  |  
| Expressway Series  | [CSCwh88665](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88665)  | X14.3.3  |  
| TelePresence Video Communication Server (VCS)  | [CSCwh88665](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh88665)  | X14.3.3  |  
| Wireless  |  
| Connected Mobile Experiences  | [CSCwh89894](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwh89894)  | 11.1 (Feb 2024)  |  
##  Products Confirmed Not Vulnerable 
Only products listed in the [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-http2-reset-d8Kf32vZ.html#vp) section of this advisory are known to be affected by this vulnerability.
Cisco has confirmed that this vulnerability does not affect the following Cisco products:
**Cable Devices**
    * GS7000 Nodes
    * RF Gateway 1 (RFGW-1)
    * RF Gateway 10
    * Remote PHY 120
**Collaboration and Social Media**
    * Customer Collaboration Platform, formerly SocialMiner
**Meraki Products**
    * Meraki Go Series
    * Meraki MR Series Cloud-Managed Wireless Access Points
    * Meraki MS Series Switches
    * Meraki MT Series Sensors
    * Meraki MV Series Cloud-Managed Smart Cameras
    * Meraki MX Series Cloud-Managed Security and SD-WAN
    * Meraki Z-Series Cloud-Managed Teleworker Gateway
**Network Application, Service, and Acceleration**
    * Cloud Services Platform 2100
    * Cloud Services Platform 5000 Series
    * Industrial Network Director
    * Nexus Dashboard Data Broker, formerly Nexus Data Broker
    * Nexus Dashboard Insights
    * Secure Workload, formerly Tetration
    * Smart Software Manager On-Prem
    * Wide Area Application Services (WAAS)
**Network and Content Security Devices**
    * Adaptive Security Appliance (ASA) Software
    * Adaptive Security Device Manager (ASDM)
    * Advanced Web Security Reporting Application
    * FXOS Firepower Chassis Manager
    * Firepower Device Manager (FDM)
    * Firepower Management Center (FMC)
    * Identity Services Engine (ISE)
    * Secure Email and Web Manager, formerly Content Security Management Appliance (SMA)
    * Secure Email, formerly Email Security Appliance (ESA)
    * Secure Endpoint Private Cloud, formerly AMP Virtual Private Cloud Appliance
    * Secure Firewall Cloud Native (SFCN)
    * Secure Network Analytics, formerly Stealthwatch
    * Secure Services Proxy
    * Security Manager
    * Umbrella Virtual Appliance
    * Virtual Security Gateway
**Network Management and Provisioning**
    * Application Policy Infrastructure Controller (APIC)
    * Business Wireless (CBW)
    * CX Test Manager (CXTM)
    * Cisco Container Platform
    * Cisco Evolved Programmable Network Manager (EPNM)
    * Cisco Telemetry Broker
    * CloudCenter Action Orchestrator
    * CloudCenter Cost Optimizer
    * CloudCenter Suite Admin
    * CloudCenter Workload Manager
    * Collaboration Audit and Assessments
    * Common Services Platform Collector (CSPC)
    * Crosswork Change Automation
    * Crosswork Health Insights
    * Crosswork Network Controller - Topology
    * Crosswork Network Controller
    * Crosswork Optimization Engine
    * Crosswork Service Health
    * Cyber Vision
    * DNA Spaces Connector
    * Elastic Services Controller (ESC)
    * FindIT Network Manager
    * Intelligent Node (iNode) Manager
    * Managed Services Accelerator
    * Modeling Labs
    * Network Change and Configuration Management
    * Network Services Orchestrator (NSO)
    * Network Services Orchestrator - SMI
    * Nexus Dashboard Fabric Controller (NDFC)
    * Nexus Dashboard Orchestrator (NDO), formerly ACI Multi-Site Orchestrator (MSO)
    * Nexus Dashboard, formerly Application Services Engine
    * Optical Network Planner
    * Policy Suite
    * Prime Collaboration Assurance
    * Prime Collaboration Deployment
    * Prime Collaboration Provisioning
    * Prime IP Express
    * Prime License Manager
    * Prime Network Services Controller
    * Prime Network
    * Prime Performance Manager
    * Prime Service Catalog
    * Process Orchestrator
    * Smart PHY
    * Software-Defined AVC (SD-AVC)
    * ThousandEyes Enterprise Agent
    * Virtual Topology System - Virtual Topology Controller (VTC) VM
    * Virtualized Infrastructure Manager
    * WAN Automation Engine (WAE)
**Routing and Switching - Enterprise and Service Provider**
    * ACI Virtual Edge
    * ASR 5000 Series Routers
    * Application Policy Infrastructure Controller Enterprise Module (APIC-EM)
    * CGR 1000 Compute Module
    * Catalyst Center, formerly Cisco DNA Center
    * GGSN Gateway GPRS Support Node
    * IP Services Gateway (IPSG)
    * MDS 9000 Series Multilayer Switches
    * ME 1200 Series Carrier Ethernet Access Devices
    * MME Mobility Management Entity
    * NCS 2000 Shelf Virtualization Orchestrator (SVO)
    * Network Convergence System 1004
    * Network Convergence System 2000 Series
    * Nexus 5500 Platform Switches
    * Nexus 5600 Platform Switches
    * Nexus 6000 Series Switches
    * Nexus 7000 Series Switches
    * Nexus 9000 Series Fabric Switches in ACI mode
    * ONS 15454 Series Multiservice Provisioning Platforms
    * Optical Network Controller
    * PDSN/HA Packet Data Serving Node and Home Agent
    * PGW Packet Data Network Gateway
    * System Architecture Evolution Gateway (SAEGW)
    * Ultra Cloud Core - Access and Mobility Management Function
    * Ultra Cloud Core - Redundancy Configuration Manager
    * Ultra Cloud Core - Subscriber Microservices Infrastructure
    * Ultra Cloud Core - User Plane Function
    * Ultra Packet Core
    * Ultra Services Platform
**Routing and Switching - Small Business**
    * 220 Series Smart Plus Switches
    * 250 Series Smart Switches
    * 300 Series Managed Switches
    * 350/350X/550X Series Switches
    * Business 220 Series Smart Switches
    * Business 250 Series Smart Switches
    * Business 350 Series Managed Switches
    * Cisco Business Dashboard
    * RV042 Dual WAN VPN Router
    * RV042G Dual Gigabit WAN VPN Router
    * RV110W Wireless-N VPN Firewall
    * RV130 Series VPN Routers
    * RV132W ADSL2+ Wireless-N VPN Router
    * RV134W VDSL2 Wireless-AC VPN Router
    * RV160 VPN Router
    * RV160W Wireless-AC VPN Router
    * RV160x VPN Router
    * RV215W Wireless-N VPN Router
    * RV260 VPN Routers
    * RV260P VPN Router with PoE
    * RV260W Wireless-AC VPN Router
    * RV260x VPN Router
    * RV320 Dual Gigabit WAN VPN Router
    * RV325 Dual WAN VPN Router
    * RV340W Dual WAN Gigabit Wireless-AC VPN Router
**Unified Computing**
    * Enterprise NFV Infrastructure Software (NFVIS)
    * HxBench
    * HyperFlex Storage Replication Adapter
    * HyperFlex System
    * HyperFlex Workload Profiler
    * Integrated Management Controller (IMC) Supervisor
    * Intersight Virtual Appliance
    * UCS C-Series Rack Servers and S-Series Storage Servers - Integrated Management Controller (CIMC)
    * UCS Central Software
    * UCS Director Bare Metal Agent
    * UCS Director
    * UCS E-Series Servers
    * UCS Manager
**Voice and Unified Communications Devices**
    * ATA 190 Analog Telephone Adapter
    * ATA 190 Series Multiplatform Analog Telephone Adapters
    * ATA 191 Analog Telephone Adapter
    * BroadWorks
    * Cloud Connect
    * Emergency Responder
    * Finesse
    * Hosted Collaboration Mediation Fulfillment
    * IP Conference Phone 7832
    * IP Conference Phone 8832
    * IP Conference Phone 8832 with Multiplatform Firmware
    * IP DECT 110 Repeater with Multiplatform Firmware
    * IP DECT 110 Single-Cell Base Station with Multiplatform Firmware
    * IP DECT 210 Multi-Cell Base Station with Multiplatform Firmware
    * IP DECT 6823 with Multiplatform Firmware
    * IP DECT 6825 with Multiplatform Firmware
    * IP Phone 6800 Series with Multiplatform Firmware
    * IP Phone 7800 Series
    * IP Phone 7800 Series with Multiplatform Firmware
    * IP Phone 8800 Series
    * IP Phone 8800 Series with Multiplatform Firmware
    * Jabber Guest
    * Paging Server
    * SPA112 2-Port Phone Adapter
    * SPA122 Analog Telephone Adapter (ATA) with Router
    * SPA232D Multi-Line DECT Analog Telephone Adapter (ATA)
    * SPA300 Series IP Phones
    * SPA8800 IP Telephony Gateway
    * Unified Attendant Consoles (except Advanced Version)
    * Unified Communications Manager
    * Unified Communications Manager IM & Presence Service
    * Unified Communications Manager Session Management Edition
    * Unified Contact Center Express (UCCX)
    * Unified Customer Voice Portal
    * Unified IP Conference Phone 8831
    * Unified IP Conference Phone 8831 for Third-Party Call Control
    * Unified IP Phone 3905
    * Unified IP Phone 6901
    * Unified IP Phone 6911
    * Unified Intelligence Center
    * Unified SIP Proxy Software
    * Unity Connection
    * Unity Express
    * Video Phone 8875
    * Virtualized Voice Browser
    * Webex Hybrid Data Security Node
    * Webex Room Phone
    * Webex Share
    * Webex Video Mesh
    * Webex Wireless Phones 840 and 860
    * Wireless IP Phone 8821
**Video, Streaming, TelePresence, and Transcoding Devices**
    * Board Series
    * Cisco Meeting Management
    * Cisco Meeting Server
    * Cisco Vision Dynamic Signage Director
    * Desk Series
    * Room Series
    * TelePresence ISDN Link
    * TelePresence Management Suite
    * Webex Board
    * Webex DX80
**Wireless**
    * Aironet 1700 Series Access Points
    * Aironet 1800 Series Access Points
    * Aironet 1810 Series OfficeExtend Access Points
    * Aironet 2700 Series Access Points
    * Aironet 2800 Series Access Points
    * Aironet 3700 Series Access Points
    * Aironet 3800 Series Access Points
    * Industrial Wireless 3700 Series Access Points
    * Mobility Services Engine Software
    * Ultra-Reliable Wireless Backhaul
    * WAP121 Wireless-N Access Point with Single Point Setup
    * WAP125 Wireless-AC Dual Band Desktop Access Point with PoE
    * WAP150 Wireless-AC/N Dual Radio Access Point with PoE
    * WAP361 Wireless-AC/N Dual Radio Wall Plate Access Point with PoE
    * WAP371 Wireless-AC/N Access Point with Single Point Setup
    * WAP571 Wireless-AC/N Premium Dual Radio Access Point with PoE
    * WAP571E Wireless-AC/N Premium Dual Radio Outdoor Access Point
    * WAP581 Wireless-AC Dual Radio Wave 2 Access Point with 2.5GbE LAN
    * WRP500 Wireless-AC Broadband Router
    * Wireless Gateway for LoRaWAN
    * Wireless LAN Controller


## 
Workarounds 
  * For potential workarounds on a specific Cisco product, refer to the Cisco bug ID, available from the [Cisco Bug Search Tool](https://bst.cloudapps.cisco.com/bugsearch).


## 
Fixed Software 
  * For information about [fixed software releases](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes), consult the Cisco bugs identified in the [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-http2-reset-d8Kf32vZ.html#vp) section of this advisory.
When [considering software upgrades](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes), customers are advised to regularly consult the advisories for Cisco products, which are available from the [Cisco Security Advisories](https://www.cisco.com/go/psirt) page, to determine exposure and a complete upgrade solution.
In all cases, customers should ensure that the devices to be upgraded contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the Cisco Technical Assistance Center (TAC) or their contracted maintenance providers.


## 
Exploitation and Public Announcements 
  * The Cisco Product Security Incident Response Team (PSIRT) is aware of attempted exploitation of this vulnerability in the wild.


## 
Source 
  * This vulnerability was publicly disclosed by [Google](https://cloud.google.com/blog/products/identity-security/how-it-works-the-novel-http2-rapid-reset-ddos-attack), [Cloudflare](https://blog.cloudflare.com/zero-day-rapid-reset-http2-record-breaking-ddos-attack/), and [AWS](https://aws.amazon.com/security/security-bulletins/AWS-2023-011/) on October 10, 2023.


## 
Cisco Security Vulnerability Policy 
  * To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](http://www.cisco.com/web/about/security/psirt/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.


## 
Subscribe to Cisco Security Notifications
  * [Subscribe](https://www.cisco.com/c/en/us/support/web/tools/cns/notifications.html)


## 
Action Links for This Advisory 
  * [Snort Rule 62519](https://www.snort.org)


## 
Related to This Advisory 
## 
URL 
  * <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-http2-reset-d8Kf32vZ>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.11  | Changed the advisory status to Final. Updated the lists of vulnerable products and products confirmed not vulnerable and fixed releases availability.  | Header, Summary, Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable  | Final  | 2023-DEC-21  |  
| 1.10  | Updated the lists of vulnerable products and products confirmed not vulnerable and fixed releases availability.  | Vulnerable Products and Products Confirmed Not Vulnerable  | Interim  | 2023-DEC-05  |  
| 1.9  | Updated the lists of vulnerable products and products confirmed not vulnerable.  | Vulnerable Products and Products Confirmed Not Vulnerable  | Interim  | 2023-NOV-17  |  
| 1.8  | Updated the lists of vulnerable products and products confirmed not vulnerable.  | Vulnerable Products and Products Confirmed Not Vulnerable  | Interim  | 2023-NOV-09  |  
| 1.7  | Updated the lists of vulnerable products and products confirmed not vulnerable and fixed releases availability.  | Vulnerable Products and Products Confirmed Not Vulnerable  | Interim  | 2023-NOV-02  |  
| 1.6  | Updated the lists of vulnerable products and products confirmed not vulnerable.  | Vulnerable Products and Products Confirmed Not Vulnerable  | Interim  | 2023-OCT-31  |  
| 1.5  | Updated the lists of vulnerable products and products confirmed not vulnerable.  | Vulnerable Products and Products Confirmed Not Vulnerable  | Interim  | 2023-OCT-26  |  
| 1.4  | Updated the lists of vulnerable products and products confirmed not vulnerable.  | Vulnerable Products and Products Confirmed Not Vulnerable  | Interim  | 2023-OCT-24  |  
| 1.3  | Updated the lists of vulnerable products and products confirmed not vulnerable.  | Vulnerable Products and Products Confirmed Not Vulnerable  | Interim  | 2023-OCT-20  |  
| 1.2  | Corrected bugs.  | —  | Interim  | 2023-OCT-19  |  
| 1.1  | Updated the lists of vulnerable products and products confirmed not vulnerable.  | Vulnerable Products and Products Confirmed Not Vulnerable  | Interim  | 2023-OCT-19  |  
| 1.0  | Initial public release.  | —  | Interim  | 2023-OCT-16  |  
Show Complete History...


* * *
## 
Legal Disclaimer 
  * THIS DOCUMENT IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR USE. YOUR USE OF THE INFORMATION ON THE DOCUMENT OR MATERIALS LINKED FROM THE DOCUMENT IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS DOCUMENT AT ANY TIME.
A standalone copy or paraphrase of the text of this document that omits the distribution URL is an uncontrolled copy and may lack important information or contain factual errors. The information in this document is intended for end users of Cisco products.


## 
Feedback 
  * [Leave additional feedback](javascript:openNewWindow\(\);)


## 
Cisco Security Vulnerability Policy 
  * To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](http://www.cisco.com/web/about/security/psirt/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.


## 
Subscribe to Cisco Security Notifications
  * [Subscribe](https://www.cisco.com/c/en/us/support/web/tools/cns/notifications.html)


## 
Action Links for This Advisory 
  * [Snort Rule 62519](https://www.snort.org)


## 
Related to This Advisory 
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-http2-reset-d8Kf32vZ.html "Back to Top")
By continuing to use our website, you acknowledge the use of cookies. 
[Privacy Statement](https://www.cisco.com/c/en/us/about/legal/privacy-full.html) Change Settings
![Company Logo](https://cdn.cookielaw.org/logos/03fc55fe-0057-4b2f-817d-763e7ecdb316/a7f4c642-c43c-4666-acea-858c0449029c/cisco-logo-transparent.png)
## Consent Manager
Your opt out preference signal is honored.
## Consent Manager
  * ### Your Privacy
  * ### Strictly Necessary Cookies
  * ### Performance Cookies
  * ### Targeting Cookies
  * ### Functional Cookies


#### Your Privacy
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. From the list on left, please choose whether this site may use Performance and/or Targeting Cookies. By selecting Strictly Necessary Cookies only, you are requesting Cisco not to sell or share your personal data. Note, blocking some types of cookies may impact your experience on the site and the services we are able to offer.
#### Strictly Necessary Cookies
Always Active
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.
Cookies Details
#### Performance Cookies
Performance Cookies
These cookies provide metrics related to the performance and usability of our site. They are primarily focused on gathering information about how you interact with our site, including: page load times, response times, error messages, and allowing a replay of a visitor’s interactions with our site, which enables us to review and analyze visitor behavior, helping to improve site usability and functionality. These cookies also allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. If you do not allow these cookies we will not know when you have visited our site and will not be able to monitor its performance.
Cookies Details
#### Targeting Cookies
Targeting Cookies
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.
Cookies Details
#### Functional Cookies
Functional Cookies
These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.
Cookies Details
Back Button
### Cookie List
Filter Button
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Clear
  * checkbox label label


Apply Cancel
Save Settings
Allow All
[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/solutions/consent-and-preferences/)
