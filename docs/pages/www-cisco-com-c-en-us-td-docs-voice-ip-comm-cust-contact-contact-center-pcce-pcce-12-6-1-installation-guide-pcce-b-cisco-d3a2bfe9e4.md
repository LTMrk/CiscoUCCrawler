---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-1-installation-guide-pcce-b-cisco-d3a2bfe9e4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_1/installation/guide/pcce_b_cisco_pcce_installationandupgrade_guide_12_6_1/pcce_b_cisco_pcce_installationandupgrade_guide_12_5_2_chapter_010.html
retrieved_at: 2026-08-21T16:39:53.489417+00:00
---

Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(1)

# Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(1)

Updated: May 14, 2021

Chapter: Prepare Customer Site Servers

## Chapter: Prepare Customer Site Servers

# Prepare Customer Site Servers

## Prepare Customer
                        	 Site Servers

Perform all the procedures in this section on the Side A and the Side B
                           		servers.

## Prepare Cisco UCS
                        	 C-Series Customer Site Servers

### Configure RAID for Cisco UCS C240 M4SX

Using Cisco Integrated Management Controller, check that the following settings are configured correctly:

Virtual Drive Info: RAID 5 with 5 (Physical Disks) * 4 (Virtual Drives/Datastores)

Stripe Size: 128KB

Write Policy: Write Back with BBU

Read Policy: Read Ahead Always

For more information regarding RAID configuration for Cisco UCS C240 M4SX in Configure RAID with GUI (UCS C-Series M4 Servers)
                                 section, refer to Cisco Collaboration on Virtual Servers Guide .

### Configure RAID for Cisco UCS C240 M5SX and Cisco UCS C240 M6SX

The disk array configuration for the Cisco UCS C240 M5SX and Cisco UCS C240 M6SX is already set up to match the requirements. Verify the settings as follows:

Using Cisco Integrated Management Controller, check that the following settings are configured correctly:

Virtual Drive Info: RAID 5 with 6 (Physical Disks) * 4 (Virtual Drives or Datastores)

Stripe Size: 128KB

Write Policy: Write Back with BBU

Read Policy: Read Ahead Always

For more information regarding RAID configuration for Cisco UCS C240 M5SX or Cisco UCS C240 M6SX , see the Installation and Configuration section of the Cisco Collaboration on Virtual Servers Guide .

### Install VMware
                           	 vSphere ESXi

Packaged CCE uses standard VMware vSphere ESXi installation procedures. For installation procedures to install the supported
                                 version of  vSphere ESXi that you are installing, see the VMware documentation at https://www.vmware.com/support/pubs/ .

For Packaged CCE, you must install the ESXi on the first drive as the default boot drive for the server.

#### Add the Datastores
                              	 to the Host Server

After installing
                                 		vSphere ESXi, add the remaining datastores. Refer to the vSphere
                                    		  Storage Guide for the vSphere ESXi version in your
                                 		deployment, available at https://www.vmware.com/support/pubs/ .

Required datastores are dictated by the hardware platform used. Cisco UCS C-Series servers require a fixed and validated configuration.

See the Virtualization for Cisco Packaged CCE at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/pcce_virt_index.html for IOPs requirements.

#### Add the Customer
                              	 ESXi Host to the vCenter

Refer to the vCenter Server and Host Management documentation at https://www.vmware.com/support/pubs/

Customers without vCenter can install on management desktops to
                                 		administer the Packaged CCE servers.

## Prepare HyperFlex M5 series Customer Site Servers

Cisco HyperFlex HX-Series System provides a unified view of the storage across all nodes of the HyperFlex HX cluster via the
                           HX Data Controller Platform. For optimal performance, it is recommended that all VMs are mapped to the single unified datastore.
                           This mapping enables the HX Data Platform to optimize storage access based on the workload and other operating parameters.

For more information, see the documentation on Cisco HyperFlex HX Data Platform at https://www.cisco.com/c/en/us/support/hyperconverged-systems/hyperflex-hx-data-platform-software/products-installation-guides-list.html .

For information on installing collaboration software, see the Cisco Collaboration on Virtual Servers at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html .

## NTP and Time
                        	 Synchronization

Packaged CCE requires that all parts of the solution have the same time. While time drift occurs naturally, it is critical
                              to configure NTP to keep solution components synchronized.

To prevent time drifts on Live Data reports, the NTP settings on the Rogger VMs, the PG VMs, the AW VMs, and on the Cisco
                              Unified Intelligence Center Publisher and Subscriber VMs must be synchronized.

Important

Microsoft periodically releases cumulative time zone updates. These updates include worldwide changes to time zone names,
                                          bias (the amount of time in minutes that a time zone is offset from Coordinated Universal Time (UTC)), and observance of daylight
                                          saving time. These patches update the information in the Windows registry. When these updates are available, apply them to
                                          all virtual machines in the deployment that are running a Microsoft Windows operating system.

### Windows Active
                              		  Directory Domain

The Windows Active Directory Primary Domain Controller (PDC) emulator for the forest in which the Packaged CCE domain resides
                              (whether same, parent, or peer) must be properly configured to use an external time source. This external time source should
                              be a trusted and reliable NTP provider, and if already configured for the customer's forest, must be used (and useable) as
                              same source for all other applications as detailed in this section for the Packaged CCE solution.

See the following references for properly configuring Windows Active Directory Domain for NTP external time source:

How to configure an authoritative time server in Windows Server .

AD DS: The PDC emulator in this forest should be configured to correctly synchronize time from a valid time source .

Microsoft Windows Server Domains do not automatically recover or fail over the authoritative internal time source for the
                              domain when the PDC emulator server is lost, due to hardware failure or otherwise. This article, Time Service Configuration on the DCwith PDC Emulator FSMO Role , helps describe how you must additionally configure the new target server to be the authoritative internal time source for
                              the domain. It also covers manual intervention to recover and seize or reassign the PDC FSMO role to another domain controller.

### Windows
                              		  Components in the Domain

Windows hosts in the domain are automatically configured to synch their time with a PDC emulator, whether by the PDC emulator
                              with authoritative internal time source or chained from same in the domain forest hierarchy.

### Windows
                              		  Components Not in the Domain

Use the following steps to set NTP time source for a Windows Server that is not joined to a domain:

Log in as a user with administrative privileges.

In the Command Prompt window, type the following line and press ENTER: w32tm /config /manualpeerlist:PEERS /syncfromflags:MANUAL

Restart the w32time service: net stop w32time && net start w32time .

Synch w32time service with peers: w32tm /resync .

Use the following Service Control command to ensure proper start of the w32time service on any reboot of the server: sc triggerinfo w32time start/networkon stop/networkoff .

### Cisco
                              		  Integrated Service Routers

Cisco IOS Voice
                              		  Gateways must be configured to use the same NTP source for the solution in
                              		  order to provide accurate time for logging and debugging. See Basic System Management
                                 			 Configuration Guide, Cisco IOS Release 15M&T: Setting Time and Calendar
                                 			 Services .

### VOS
                              		  Components

Components such as Unified Intelligence Center, Finesse, Customer Collaboration Platform , and Unified Communications Manager must point to the same NTP servers as the domain authoritative internal time source.

CLI commands for NTP
                                 			 Servers

While NTP servers are typically specified at install time, here a few commands you can use from the platform cli of the above
                              listed components, to list, add and remove ntp servers. From the platform CLI:

To list existing ntp servers: utils ntp servers list

To add an additional ntp server: utils ntp server add <host or ip address to add>

To delete an existing ntp server: utils ntp server delete (row number of the item to delete) . Press Enter .

### ESXi
                              		  Hosts

All Packaged CCE ESXi hosts (including those for optional components), must point to the same NTP server(s) used by the Windows
                              domain PDC emulator as the their external time source.

For details on configuring NTP on ESXi hosts, see the VMware documentation at https://www.vmware.com/support/pubs/ .

## Global Catalog
                        	 Requirements

Packaged CCE uses
                              		  the Global Catalog for Active Directory Lookup. All domains in the AD Forest in
                              		  which the Packaged CCE Hosts reside must publish the Global Catalog for that
                              		  domain. This includes all domains with which your solution interacts, for
                              		  example, Authentication, user lookup, and group lookup.

In a multi-domain forest, a Global Catalog is required at each AD
                              		site. Global Catalog is a central repository of domain information in an AD
                              		forest. A significant performance degradations and failure occur without local
                              		or Global Catalog. It is important for every AD query to search each domain in
                              		the forest. The multi-site deployments are required to query across WAN links.

This does not
                                          				imply cross-forest operation. Cross-forest operation is not supported.

| Using Cisco Integrated Management Controller, check that the following settings are configured correctly: Virtual Drive Info: RAID 5 with 6 (Physical Disks) * 4 (Virtual Drives or Datastores) Stripe Size: 128KB Write Policy: Write Back with BBU Read Policy: Read Ahead Always For more information regarding RAID configuration for Cisco UCS C240 M5SX or Cisco UCS C240 M6SX , see the Installation and Configuration section of the Cisco Collaboration on Virtual Servers Guide . |
|---|

| Important | Microsoft periodically releases cumulative time zone updates. These updates include worldwide changes to time zone names,
                                          bias (the amount of time in minutes that a time zone is offset from Coordinated Universal Time (UTC)), and observance of daylight
                                          saving time. These patches update the information in the Windows registry. When these updates are available, apply them to
                                          all virtual machines in the deployment that are running a Microsoft Windows operating system. |
|---|---|

| Note | Do not use the "Fix it for me" function in this article. |
|---|---|

| Note | Replace peers with a comma-separated list of NTP servers. |
|---|---|

| Note | This does not
                                          				imply cross-forest operation. Cross-forest operation is not supported. |
|---|---|