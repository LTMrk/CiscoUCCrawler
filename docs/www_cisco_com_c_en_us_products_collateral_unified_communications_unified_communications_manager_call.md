  * [Skip to content](https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-communications-manager-callmanager/datasheet-c78-739475.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-communications-manager-callmanager/datasheet-c78-739475.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-communications-manager-callmanager/datasheet-c78-739475.html)


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


  * [](https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-communications-manager-callmanager/datasheet-c78-739475.html)
  * [...](https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-communications-manager-callmanager/datasheet-c78-739475.html)Show All Breadcrumbs
  * [Products & Services](https://www.cisco.com/c/en/us/products/index.html)
  * [Unified Communications](https://www.cisco.com/c/en/us/products/unified-communications/index.html)
  * [Call Control](https://www.cisco.com/c/en/us/products/unified-communications/call-control/index.html)
  * [Cisco Unified Communications Manager (CallManager)](https://www.cisco.com/c/en/us/products/unified-communications/unified-communications-manager-callmanager/index.html)
  * [Data Sheets](https://www.cisco.com/c/en/us/products/unified-communications/unified-communications-manager-callmanager/datasheet-listing.html)


# Cisco Unified Communications Manager 12.0 Data Sheet
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/products/collateral/unified-communications/unified-communications-manager-callmanager/datasheet-c78-739475.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-communications-manager-callmanager/datasheet-c78-739475.html)
Download
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/products/collateral/unified-communications/unified-communications-manager-callmanager/datasheet-c78-739475.html)


### Download Options
  * [PDF](https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-communications-manager-callmanager/datasheet-c78-739475.pdf) (300.1 KB)   
View with Adobe Reader on a variety of devices


Updated:July 1, 2026
Document ID:1504191652007283
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
HTML Passthrough Component 
Cisco® Unified Communications Manager is the heart of Cisco collaboration services, enabling session and call control for video, voice, messaging, mobility, instant messaging, and presence.
Product Overview
What if you could collaborate more effectively with customers and partners on any network? With any device? From anywhere? Cost-effectively, reliably, and securely? With Cisco Unified Communications Manager, you can.
Today’s workplace challenges the collaboration environment in unprecedented ways. More mobile workers use more devices than ever before. Web and video conferencing intersect.
We are the industry leader in enterprise call and session management platforms, with more than 200,000 customers worldwide and more than 85 million Cisco IP Phones and tens of millions of soft clients deployed. Cisco Unified Communications Manager is the core of Cisco’s collaboration portfolio. It delivers people-centric user and administrative experiences while supporting the full range of collaboration services, including video, voice, instant messaging and presence, messaging, and mobility on Cisco as well as third-party devices.
New with Cisco Unified Communications Manager Version 12.0
Table 1 lists Major Features in Cisco Unified Communications Manager Version 12.0.
**Table 1.** High-Level Features in Cisco Unified Communications Manager 12.0  
|  Feature  |  Benefits  |  
| --- | --- |  
|  Push notifications  |  ●Cisco Unified Communications Manager and the IM and Presence service use Apple’s cloud-based Push Notification service to push voice and video calls, instant messaging notifications, and Cisco WebEx ® invitations to Cisco Jabber ® for iPhone and iPad clients that are running in suspended mode.  ●Push Notifications in Cisco Unified Communications Manager enable users to maintain a persistent communication with Cisco Jabber.  ●Push Notifications are required both for Cisco Jabber for iPhone and iPad clients that connect from within the enterprise network and for clients that register to an on-premises deployment using Expressway's Mobile and Remote Access (MRA) feature.  ●Push Notifications high availability provide failover and redundancy for Push Notifications–enabled IM and Presence sessions for Cisco Jabber on iPhone and iPad clients. This makes sure that the backup node has the session information and can take over the session without user action from the Jabber user. For voice and video calls, redundancy and failover are handled by Cisco Unified Communications Manager groups.  ●Push Notifications troubleshooting sends the troubleshooting information to the Cisco cloud at regular intervals. Cisco may use this information for proactive debugging of Push Notifications and system components. This speeds up system troubleshooting by making sure that Push Notifications alarms can be accessed quickly by the Cisco TAC.   |  
|  Cisco Spark™ Hybrid Services  |  ●Home Cluster Routing enables the Session Management Edition (SME) to route calls from a Cisco Spark Hybrid Call Service Connect user via Expressway-C/E firewall traversal solution to the caller’s home Cisco Unified Communications Manager cluster, where they anchor on the caller’s Cisco Spark remote device. Calls are routed based on route headers, complying with RFC 3261. In large deployments, this helps in having fewer direct SIP trunks and less call routing configuration.  ●Verified Identity and Call Anchoring feature allow inbound calls to be anchored by caller identity matching a remote destination only when caller identity is trusted. This will prevent fraud by callers attempting to impersonate authorized users of Dial via Office (DVO) or Call Service Connect.  ●Dedicated remote device enables call service connect with no incremental licensing effect for users with at least UCL enhanced licensing.   |  
|  Instant messaging and presence (IM&P)  |  ●Message Archiver can be set to blocking mode to block the message delivery if the compliance database is down. New compliance feature applies to point-to-point chat, ad hoc group chat, and persistent chat messages.  ●Support for Microsoft SQL Server (2014, 2014 SP1, 2012 SP3) as an external database to store information from persistent group chat when it is enabled for high availability.  ●External database cleanup utility in IM&P helps in managing disk space for storing the messages and files in the external database. This feature enables cleaning the records related to persistent chat, managed file transfer, and message archiver functionality. Utility supports both manual and automated delete options.  ●Roster cleanup helps an administrator to view the list of stale contacts accumulated over a period of time and delete them from IM&P database to improve the system performance.  ●Privacy for ad hoc chat room prevents unauthorized users from joining the room, viewing the message history, and interfering with the chat conversation, thus enhancing the security of the ad hoc chat room. Room can be discovered only if the user is an owner or an administrator of the room.  ●Centralized IM&P solution eliminates the need for 1:1 IM&P and Cisco Unified Communications Manager cluster. Centralized IM&P can work with multiple Cisco Unified Communications Manager clusters.  ●Centralized IM&P can be easily overlaid with existing clusters with minimal configuration change. Works seamlessly with existing dial plan.   |  
|  Minimum TLS version control  |  ●Allows organization to deploy stronger security and comply to standards such as PCI DSS by preventing negotiation of a lower TLS version.  ●New CLI command to set the minimum TLS version (TLS 1.0, 1.1, or 1.2) for the Cisco Unified Communications Manager secure TLS interfaces.  ●Includes Cisco Prime ® Collaboration Deployment 11.6 and 12.0.   |  
|  Smart Licensing  |  ●Cisco Smart Software Licensing is a new way of thinking about licensing. It adds flexibility to licensing and simplifies it in the enterprise. Cisco Smart Software Licensing helps the customer procure, deploy, track, and manage licenses easily.  ●Cisco Unified Communications Manager 12.0 onward licenses are managed in Cisco Smart Software Manager or Cisco Smart Satellite.  ●PLM is no longer required. PAK has been eliminated. Licenses are not tied to the Cisco Prime license manager node.  ●Cisco Unified Communications Manager 12.0 SKUs are smart SKUs that fulfill Smart Entitlements in the specified Smart Account.  ●Customers with active SWSS can self-migrate the classic licenses (after assigning to Smart Account) to Smart Entitlements through the [Cisco License Central](https://software.cisco.com/clc).  ●Migration from classic to Smart Licenses is supported for already fulfilled, partially fulfilled, and unfulfilled PAKs and for device based (PLM UUID).  ●Cisco Unified Communications Manager licensing model remains unchanged.  ●Smart Software Licensing deployment option includes direct access from (a) Cisco Unified Communications Manager to Smart Licensing Cloud (b) through an HTTP proxy (c) mediated access through an on-premises collector, or satellite. Satellite requires a separate VM instance. For more information, refer to [the Cisco Unified Communications Solutions Ordering Guide](https://www.cisco.com/c/en/us/partners/tools/collaboration-ordering-guides.html)  |  
|  IPv6-only endpoints   |  ●Supports IPv6-only endpoints deployment with a focus on IPv6-only branch office and dual stack home/central office.  ●Makes sure that IPv6-only endpoints have the same feature parity as that of IPv4-only endpoints such as device mobility, extension mobility, IP phone services, and self-provisioning.  ●Cisco Jabber 11.6 or above operating in IPv6-only mode in an on-premises network can connect to Cisco Unified Communications Manager and IM&P on port 8443.  ●IPv6 support for SNMP (V1/V2C/V3 protocol) includes ability to accept SNMP requests from IPv6-only hosts and to configure IPv6-only SNMP notification destinations.  ●Solution mitigates the IPv4 address exhaustion issue and reduces the complexity of managing the   
dual-stack environment.  ●No changes to existing IPv4 support.   |  
|  Device manageability  |  ●Simplifies the device management with a capability to generate administrative report and BAT update for devices seen earlier (1-day granularity) and not seen now; devices not used (made or answered a call) in a given time period.  ●Enables administrator to locate devices and recover licenses where possible.   |  
|  Extension mobility login experience  |  ●Allows user to log in to extension mobility or Extension Mobility Cross Cluster (EMCC) with primary DN or self-service user ID and PIN.  ●Eliminates the need to enter lengthy alphanumeric credentials using telephone keypad (for example, John2.doe@us.example.com).   |  
|  SAML SSO enhancements   |  ●Administrator can provision long-lived, self-signed internal certificate for SAML IdP trust configuration, thus lowering barrier to deploy SSO while using clusterwide single SAML agreement. This also avoids SAML SSO agreement reconfiguration on Tomcat certificate renewal.  ●Expanded the solution coverage to include SAML SSO support for Cisco Unified Communications Manager platform/DRS users and RTMT application.   |  
|  Administration simplicity  |  ●New wizard for seamless configuration of both Cisco Unified Communications Manager and InformaCast Paging server. Low administrative overhead with automatic setup of panic button (speed dial) on eligible phones.  ●Faster and more stable upgrades with up to 10% speed improvement achieved through streamlined sequencing, parallelization of upgrade tasks, locking configuration changes during upgrades, and database optimizations.  ●Enhanced usability of the User Device Association page to prevent unintentional removal of devices associated with a user.  ●Smaller installation images via dedicated images for Cisco Unified Communications Manager and Cisco Unity ® connection.  ●Cisco Prime Collaboration Deployment install and migration tasks support remote NFS file store to minimize file transfers over the WAN.   |  
|  Security enhancements  |  ●New Jabber authentication support with oAuth Refresh Login framework and self-contained oAuth tokens. Improves Jabber login UX with consistent login behavior in SSO and non-SSO environments, seamless access to resources over life of refresh token, and no authentication caching. Requires compatible unified communications components such as Cisco Expressway and Cisco Unity connection with refresh login enabled.  ●Long-lived phone trust with ITL recovery certificate. Avoids device lock-out because of trust break for scenarios such as host name change and other certificate regeneration.  ●ASA TLS proxy functionality with tokenless CTL. Feature parity with the USB token approach for putting cluster in mixed mode and simplifies ASA TLS proxy deployment.  ●Prevents information exposure by disabling the back button to view admin pages after logoff.  ●Authenticated NTP support allows secure communication channel between NTP server and the Cisco Unified Communications Manager node.   |  
|  Miscellaneous  |  ●Microsoft Active Directory 2016 support for directory integration.  ●Supports customizing your administration and Self-care portal with corporate branding. Branding can be enabled/disabled via Cisco Unified OS Administration Admin interface or through CLI.  ●Allows provisioning of Cisco Meeting Server as a conference bridge.  ●Supports allocation of audio and video bandwidth independently in video calls. Administrator can configure per call bandwidth constraints for audio and video in video calls through service parameter, region and location settings.   |  
Ordering Cisco Unified Communications Manager 12.0
●Starting with Cisco Unified Communications Manager 12.0, Smart Licensing only is supported. Licenses are Smart Entitlements. Customers must create Smart Account.
●Cisco Smart Licensing in Unified Communications Manager Overview: <https://www.cisco.com/c/dam/en/us/products/collateral/unified-communications/unified-communications-licensing/presentation-c97-739389.pptx>
●Cisco Smart Licensing: <https://www.cisco.com/c/en/us/buy/smart-accounts/software-licensing.html>
●[Cisco License Central](https://software.cisco.com/clc).
●Cisco Smart Software: Manager satellite: <https://www.cisco.com/go/smartsatellite>
●Cisco Smart Accounts: <https://www.cisco.com/web/ordering/smart-software-manager/smart-accounts.html>
Table 2 shows a list of top level ordering SKUs. Refer to the [Cisco Unified Communications Solutions Ordering Guide](https://www.cisco.com/c/en/us/partners/tools/collaboration-ordering-guides.html) for a list of all orderable parts
**Table 2.** Cisco Unified Communications Manager Ordering Information  
|  New and Expansion Cisco Unified Communications Manager 12.0 Orders  |  
| --- |  
|  UCL-UCM-LIC-K9  |  Top Level SKU  |  
|  Feature Option SKUs  |  
|  LIC-UCM-12X-ENHP  |  UC Manager-12.x Enh Plus Single User  |  
|  LIC-CUCM-12X-ENH  |  UC Manager-12.x Enhanced Single User  |  
|  LIC-CUCM-12X-BAS  |  UC Manager-12.x Basic Single User  |  
|  LIC-CUCM-12X-ESS  |  UC Manager-12.x Essential User License User  |  
|  LIC-TP-12X-ROOM  |  TelePresence Room Based Endpoint, Single or Multi-Screen  |  
|  Upgrade Order (for customers without SWSS)  |  
|  UCL-UCM-UPG-K9  |  Top Level SKU  |  
|  Feature Option SKUs  |  
|  UPG-CUCM-ENH  |  Migration to UC Manager Plus (Smart Entitlements)  |  
|  UPG-CUCM-USR  |  Migration to UC Manager Enhanced (Smart Entitlements)  |  
|  UPG-CUCM-BASIC  |  Migration to UC Manager Basic (Smart Entitlements)  |  
|  UPG-CUCM-ESS-USR  |  Migration to UC Manager Essential (Smart Entitlements)  |  
|  UPG-TP-ROOM  |  Migration to UC Manager TelePresence Room based endpoint (Smart Entitlements)  |  
Migrating Cisco Unified Communications Manager 9.x and above (PLM-based licenses) to Cisco Unified Communications Manager 12.0
●Customers must create Smart Account. For more details, refer to  . 
●Customers need to first migrate existing classic PAK or PLM to the Smart Account and virtual account.
●Customers with active SWSS will be able to convert classic licenses to Smart Entitlements through the [Cisco License Central](https://software.cisco.com/clc).
●Two types of migration are supported:
◦PAK based: Migration can be done for already fulfilled, partially fulfilled, and unfulfilled PAKs.
◦Device based: This can be used to convert the PLM-based licenses to Smart Entitlements.
For more details, refer to link to new Smart Licensing preso (tbc).
Upgrade to a Smart License–enabled Version without an SWSS Contract
From v9, v10, and v11 (user-based licensing) upgrade to Smart Licenses:
●Order a-la-carte upgrade SKUs along with SWSS
From pre-v9 (DLU) upgrade to Smart Licenses:
●Order a-la-carte upgrade SKUs based on LCU report from classic server. Add SWSS
●Additional new licenses may be ordered
Cisco Capital
Financing to Help You Achieve Your Objectives
Cisco Capital can help you acquire the technology you need to achieve your objectives and stay competitive. We can help you reduce CapEx. Accelerate your growth. Optimize your investment dollars and ROI. Cisco Capital financing gives you flexibility in acquiring hardware, software, services, and complementary third-party equipment. And there’s just one predictable payment. Cisco Capital is available in more than 100 countries. [Learn more](https://www.cisco.com/web/ciscocapital/americas/us/index.html).
For More Information
For more information about installing and upgrading from an older version of Unified Communications Manager, visit <https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html>.
For Unified Communications Preferred Architecture Guides, visit <https://www.cisco.com/c/en/us/solutions/enterprise/design-zone-collaboration/index.html>.
### Contact Cisco
  * [Get a call from Sales](https://www.cisco.com/site/us/en/about/contact-cisco/index.html?linkclickid=luh-contactus)
  * ##### Call Sales:
  * [ 1-800-553-6387 ](tel:18005536387)
  * US/CAN | 5am-5pm PT
  * [Product / Technical Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Training & Certification](https://www.cisco.com/site/us/en/learn/training-certifications/index.html)


### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
