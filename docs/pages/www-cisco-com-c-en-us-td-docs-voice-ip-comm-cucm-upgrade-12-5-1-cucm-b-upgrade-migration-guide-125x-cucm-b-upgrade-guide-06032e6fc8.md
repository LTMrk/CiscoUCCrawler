---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-upgrade-12-5-1-cucm-b-upgrade-migration-guide-125x-cucm-b-upgrade-guide-06032e6fc8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/upgrade/12_5_1/cucm_b_upgrade-migration-guide-125x/cucm_b_upgrade-guide-1251su2_chapter_00.html
retrieved_at: 2026-08-17T00:06:23.256948+00:00
---

Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1)

# Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1)

Updated: July 25, 2025

Chapter: Upgrade Planning

## Chapter: Upgrade Planning

# Upgrade Planning

## Revision History

Date

Revision

September 7, 2021

Removed the followings sections from respective chapters as we need not perform them for upgrade scenarios:

Pre-upgrade Tasks—Deactivate TFTP services

Post-upgrade Tasks—Restart TFTP Services

## Upgrade and Migration Overview

The procedures in this guide describe how to upgrade Cisco Unified Communications Manager (Unified Communications Manager)
                              and Cisco Unified Communications Manager IM and Presence Service (IM and Presence Service) from an earlier version to the
                              current version.

Use the procedures in this guide as a starting point for all upgrades and migration paths. Note these upgrade usage terminologies
                              when you read the term 'upgrade' used in this guide:

The term "upgrade" refers to the scenario where all the cluster nodes complete the steps required for end-to-end processes.
                                    As an outcome, the entire cluster runs on the upgraded destination version. Then, the upgrade is considered to be 'complete/done.'
                                    The end-to-end process for "upgrade" is defined as all nodes completing upgrade-inactive versions, all nodes completing switch-version-reboot,
                                    and database replication completion across all the cluster nodes. Refer to the Switch Version Manually (Clusterwide) section for information on checking the upgrade status.

The term "inactive version" or "upgrade inactive version" refers to only upgrading the inactive version, without or before
                                    performing switch-version-reboot, on one or more cluster nodes.

### Recommended Upgrade Considerations:

Choose a "direct upgrade" method. We recommend you choose Simple Upgrades, but you can still perform the legacy Single-Node
                                    upgrade method. See "Upgrade Methods".

Regardless of the upgrade method chosen, all the cluster nodes must complete the following:

upgrade inactive version

switch version and reboot

After all nodes are on the new version, wait for the database replication to complete across all nodes in the cluster before
                                    proceeding.

You must ensure that the points mentioned in step 2 of the upgrade plan follow the node sequencing rules as mentioned in the
                                    "Sequencing Rules and Time Requirements" chapter.

Upgrade is not complete unless all the requirements in Step 2 are finished. You can view the upgrade status from the Cisco
                                    Unified OS Administration user interface or use the CLI commands to monitor status. You can also see banner messages in the
                                    user interface to warn about potential blocks to cluster nodes and add/update/delete functionalities until all the conditions
                                    in Step 2 are complete across all the clusters.

## Upgrade Methods

The following table explains the types of upgrades that you can complete with Unified Communications Manager and the IM and
                              Presence Service and the upgrade tools that you can use to complete the upgrade.

Upgrade Type

Description

Upgrade Tools

Direct Standard Upgrade

A standard upgrade is a direct upgrade where you need to upgrade the application software, but not the underlying operating
                                          system. This is usually the simplest form of upgrade and would typically apply to upgrades from within the same major-minor
                                          release category, where the OS is the same for both releases.

For release 12.5 or higher, direct standard upgrades have substantially improved durations, simpler procedures and reduced
                                          service impact.

Example : Upgrades from 12.5(1) to 12.5(1)SU1.

The following tools are used to complete standard upgrades:

Unified OS Admin

CLI

PCD Upgrade task

Direct Refresh Upgrade

A direct refresh upgrade is a direct upgrade where you need to upgrade both the application software and the underlying operating
                                          system software. This would typically be used if you're upgrading from one major-minor release to another where the OS is
                                          different for the two releases.

Example : Upgrades from 11.5(1) or 12.0(1) to 12.5(1)

The following tools are used to complete refresh upgrades:

Unified OS Admin

CLI

PCD Upgrade task

Direct migration

A direct migration involves a 'repave' where multiple factors exist that can't address with just a direct upgrade. Direct
                                          Migration is used in the following cases:

Site moves

The desired upgrade requires you to change the infrastructure hardware and platform.

Example : Upgrades from Unified CM 10.5(x) on ESXi 5.5 and Cisco UCS M3 generation hardware to 12.5(x) on ESXi 7.0 and Cisco UCS M5
                                                generation hardware.

ESXi upgrade and/or Unified CM virtual machine configuration change

Unified CM address/hostname change

The desired upgrade requires a direct upgrade path that does not exist for the source release.

Example : Unified CM 8.5(1) on ESXi to 12.5(x) on ESXi—no direct upgrade path exists making a migration mandatory.

"Virtual to Virtual (V2V)" migration, where even if a direct upgrade path exists, direct migration is preferred to mitigate
                                                upgrade path complexity factors such as duration, service impact, and a short outage window.

The following tool is used to complete migrations:

PCD Migration

Fresh Install with Data Import

Migration from legacy releases

A legacy release is a release that is so old that no direct upgrade or direct migration path exists to the current release.
                                          The only option is a direct upgrade to a later release that supports PCD migration followed by a PCD migration to the current
                                          release.

Example : Any upgrade from a pre-6.1(5) Unified CM or a pre-8.5(4) Cisco Unified IM and Presence.

For details, see Upgrading from Legacy Releases .

## Take Record of Your Current System

Before you begin the upgrading, take a record of the versioning within your current system setup. After you know the versions
                              that your current system uses, you can begin planning your upgrade. This includes:

Pre-upgrade versions for Unified Communications Manager and the IM and Presence Service

Current Hardware version

VMware Versioning

You can obtain versioning by running the Pre-upgrade Upgrade Readiness COP File. For details, see Run Upgrade Readiness COP File (Pre-upgrade) .

## Supported Upgrade and Migration Paths

The following table highlights supported upgrade paths to upgrade to 12.5(x) releases of Unified Communications Manager and
                              the IM and Presence Service.

Source

Destination

Supported Upgrade Method

Version Switching* (Source to Destination and Vice Versa)

Cisco Unified Communications Manager Upgrade Paths

Unified CM 10.0(x)

12.5(x)

PCD Migration**

Version switching not supported

Unified CM 10.5(x), 11.x, 12.0(x)

12.5(x)

Unified OS Admin upgrade (direct refresh)

CLI upgrade (direct refresh)

PCD Upgrade (direct refresh)**

PCD Migration**

Fresh Install with Data Import only to destination 12.5(1)SU5 or later.

If the source release is 10.5(x) and the destination release is 12.5(1) through 12.5(1)SU5, PCD Upgrade Task is supported.

If the source release is 10.5(x) and the destination release is 12.5(1)SU6 and above, PCD Upgrade Task is not supported.

Version switching supported for upgrades, but not for migrations

Unified CM 12.5(x)

12.5(y)

Unified OS Admin upgrade (direct standard)

CLI upgrade (direct standard)

PCD Upgrade (direct standard)**

Fresh Install with Data Import only to destination 12.5(1)SU5 or later.

Version switching supported for upgrades, but not for migrations

IM and Presence Service Upgrade Paths

IM and Presence 10.0(x)

IM and Presence 12.5(x)

PCD Migration**

Version switching not supported

IM and Presence 10.5(x), 11.x or 12.0(x)

12.5(x)

Unified OS Admin upgrade (direct refresh)

CLI upgrade (direct refresh)

PCD upgrade (direct refresh)**

PCD Migration**

Fresh Install with Data Import only to destination 12.5(1)SU5 or later.

Version switching supported for upgrades, but not supported for migrations.

IM and Presence 12.5(x)

12.5(y)

Unified OS Admin upgrade (direct standard)

CLI upgrade (direct standard)

PCD upgrade (direct standard)**

Fresh Install with Data Import only to destination 12.5(1)SU5 or later.

Version switching supported for upgrades, but not supported for migrations.

* Version switching refers to the ability to install the new version as an inactive version and switch to the new version,
                              and revert to the old version, whenever you want. This capability is supported with most direct upgrades, but not with migrations.

** PCD Upgrades and Migrations—Use Cisco Prime Collaboration Deployment Release 12.6 or later for all PCD tasks. If you want
                              to upgrade or migrate to Unified CM Release 12.5(1)SU6 and above, ensure that you use the Release 14 version of the Cisco
                              Prime Collaboration Deployment.

## Choose Your Upgrade Tool

Refer to the table below for information that can help you to decide which upgrade tool to use when there are multiple mechanisms
                              available to choose from.

Upgrade Method

Support

When to use this method...

How to complete the Upgrade or Migration

Unified OS Admin or CLI upgrades

Direct upgrades (standard or refresh) via the Cisco Unified OS Administration GUI or CLI.

Consider this tool for:

For simplified clusterwide upgrades

You are only changing the application software and are not updating hardware or VMware.

A direct upgrade path exists.

You are only upgrading Unified CM and IM and Presence Service. There are no other UC applications.

You are upgrading a single Unified CM cluster and a single IM and Presence subcluster.

Go to Upgrade Tasks

PCD Upgrades

Handles direct upgrades (standard or refresh) via Cisco Prime Collaboration Deployment's upgrade task.

Consider this tool when:

You have multiple clusters to upgrade.

Your cluster has a large number of nodes, and you need help orchestrating the upgrade to forward the schedule.

You need to upgrade other applications, such as Cisco Unity Connection or Cisco Unified Contact Center Express.

From Release is 10.x or later

Run Upgrade Readiness COP File (Pre-upgrade) .

Refer to the Cisco Prime Collaboration Deployment Administration Guide to run an upgrade or migration task.

Run Upgrade Readiness COP File (Post-upgrade)

PCD Migrations

Handles migrations via Cisco Prime Collaboration Deployment.

Consider this tool when:

You are upgrading from an earlier release that did not use VMware.

Your source release is so old that it does not support VMware.

In addition to upgrading application versions, you must make ESXi updates as well.

You are changing infrastructure hardware and platform.

Your source release has previously direct upgraded from a pre-11.5 version and is having out of disk space issues. You may
                                                need to reinstall to the latest stack to maximize usable disk space.

You have available infrastructure for temporary duplicate VMs and their required hardware.

## Required COP Files

The tables below lists the upgrade paths that require COP files. You must install COP files on each node before you begin
                              an upgrade using the Cisco Unified OS Administration interface, or before you begin an upgrade or migration using the Prime
                              Collaboration Deployment (PCD) tool. If you are using PCD, you can perform a bulk installation of the COP files before you
                              begin the upgrade.

You can download COP files for Cisco Unified Communications Manager and the IM and Presence Service at https://software.cisco.com/download/home/268439621 . After you select the destination version for the upgrade, choose Unified Communications Manager Utilities to see the list of COP files.

You should run the Upgrade Readiness COP file prior to the upgrade in order to maximize upgrade success. If you do not run
                                          this COP file, you increase the risk of an unsuccessful upgrade due to undetected issues on the source release. Cisco TAC
                                          may require that you run this COP file to provide effective technical support.

From

To

COP Files

Unified Communications Manager Upgrades

Unified CM 10.5(x), 11.0(x)

12.5(x)

Direct Refresh upgrade

Required COP file: ciscocm.enable-sha512sum-2021-signingkey-v1.0.cop.sgn. See the COP file for more information.

Unified CM 11.5(x)

12.5(x)

Direct Refresh upgrade; COP file is required to increase the disk space.

ciscocm.free_common_space_v<latest_version>.cop.sgn. To download the COP files and the Readme files, go to https://software.cisco.com , click Software Download link under Download & Upgrade section, and navigate to the Unified Communications > Call Control > Cisco Unified Communications Manager (CallManager) > <Version> > Unified Communications Manager/CallManager/Cisco Unity Connection Utilities .

Required COP file: ciscocm.enable-sha512sum-2021-signingkey-v1.0.cop.sgn. See the COP file for more information.

Unified CM 12.0(1)

12.5(x)

PCD Migrations require a COP file:

ciscocm-slm-migration.k3.cop.sgn

This requirement applies only for Prime Collaboration Deployment migrations from Release 12.0(1) of Unified Communications
                                                      Manager (build 12.0.1.10000-10). If you are migrating from a higher release, such as Unified Communications Manager 12.0(1)SU1,
                                                      you don't need to install the COP file.

Required COP file: ciscocm.enable-sha512sum-2021-signingkey-v1.0.cop.sgn. See the COP file for more information.

Unified CM 12.5(x)

12.5(y)

Direct Standard upgrade

Required COP file: ciscocm.enable-sha512sum-2021-signingkey-v1.0.cop.sgn. See the COP file for more information.

IM and Presence Service Upgrades

10.5(x), 11.x, 12.x

12.5(x)

No COP files required

## Requirements and Limitations

The following sections describe requirements and limitations for upgrades to this release.

### Hardware Requirements

You can install Unified Communications Manager and IM and Presence Service on a virtual server hosted on the following types of hardware. If your current deployment does not use one of these servers,
                                 then you must migrate to a supported hardware platform:

Cisco Business Edition 6000 or 7000 appliance

Virtualized Cisco hardware (such as Cisco UCS or Cisco HyperFlex) with VMware vSphere ESXi

Virtualized Third-party hardware with VMware vSphere ESXi

The requirements and support policies are different for each of these options. Before you begin an upgrade, verify that your
                                 current hardware meets the requirements of the new release. You can find detailed information about the requirements by going
                                 to https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html and following the links for the Unified Communications Manager and IM and Presence Service applications.

#### Virtual Machine Configuration

Before you begin an upgrade or migration, verify that your current virtual machine (VM) software meets the requirements of
                                    the new release.

Item

Description

OVA templates

OVA files provide a set of predefined templates for virtual machine configuration. They cover items such as supported capacity
                                                levels and any required OS/VM/SAN alignment. You must use a VM configuration from the OVA file provided for the Unified Communications Manager and IM and Presence Service applications.

The correct VM configuration to use from the OVA file is based on the size of the deployment. For information about OVA files,
                                                search for the topic "Unified Communications Virtualization Sizing Guidelines" at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/collaboration-virtualization-sizing.html .

VMware vSphere ESXi

You must install a version of vSphere ESXi hypervisor that meets the compatibility and support requirements for the release.

If you use Cisco Prime Collaboration Deployment (PCD) to perform an upgrade or migration, you must also ensure that you install
                                                vSphere ESXi with the correct license type. PCD is not compatible with all the license types of vSphere ESXi because some
                                                of these licenses do not enable required VMware APIs.

VMware vCenter

VMware vCenter is optional when you deploy Unified Communications Manager or IM and Presence Service on Business Edition 6000/7000 appliances, or on UC on UCS tested reference configuration hardware.

VMware vCenter is mandatory when you deploy on
                                                UC on UCS specs-based and third-party
                                                server specs-based hardware.

VM configuration virtual hardware specifications

Verify whether you need to change the virtual hardware specifications on your VM in order to upgrade to a new release of Unified Communications Manager or IM and Presence Service . For example, verify the requirements for vCPU, vRAM, vNIC adaptor type, and vDisk size, as well as other specifications.

Any changes to a VM must align with the OVA configuration. VM changes that result in an unsupported OVA configuration are
                                                not allowed. For information about VM requirements, see  Readme file with the OVA template that supports your release.

If Unified Communications Manager is upgraded to 12.5 or higher versions from release 11.5 or higher, using 80GB OVA it is
                                                            expected to have a higher active partition up to 98%. We can correct this by a system rebuilt with HDD 90GB/110GB. Use a default
                                                            110GB OVA template and rebuilt the node. Or on current 80GB OVA, prior to clean install, go to VM > Edit Settings , and increase the HDD size from 80GB to 90GB/110GB. Other specs remain the same. Adding HDD disk to the system already installed
                                                            only adds additional HDD space to common partition.

##### VMware Upgrade Requirements

If the upgrade requires you to update your VMware, go to Virtual Machine Configuration Tasks .

#### Deprecated Phone Models

The following table lists all the phone models that are deprecated for this release of Cisco Unified Communications Manager , along with the Unified CM release where the phone model first became deprecated. For example, a phone model that was first
                                    deprecated in Release 11.5(1) is deprecated for all later releases, including all 12.x releases.

If you are upgrading to the current release of Cisco Unified Communications Manager and you have any of these phone models deployed, the phone will not work after the upgrade.

Deprecated Phone Models for this Release

First Deprecated as of...

Cisco Unified IP Phone 7970G

Cisco Unified IP Phone 7971G-GE

Cisco Unified Wireless IP Phone 7921G

12.0(1) and later releases

Cisco IP Phone 12 SP+ and related models

Cisco IP Phone 30 VIP and related models

Cisco Unified IP Phone 7902

Cisco Unified IP Phone 7905

Cisco Unified IP Phone 7910

Cisco Unified IP Phone 7910SW

Cisco Unified IP Phone 7912

Cisco Unified Wireless IP Phone 7920

Cisco Unified IP Conference Station 7935

11.5(1) and later releases

For additional information, refer to Field Notices.

##### Upgrades that
                                    		  Involve Deprecated Phones

If you are using
                                    		  any of these phones on an earlier release and you want to upgrade to this
                                    		  release, do the following:

Confirm
                                          				whether the phones in your network will be supported in this release.

Identify any
                                          				non-supported phones.

For any
                                          				non-supported phones, power down the phone and disconnect the phone from the
                                          				network.

Provision a supported phone for the phone user. You can use the Migration FX tool to migrate from older model to newer model
                                          phones. For details, go to: https://www.unifiedfx.com/products/unifiedfx-migrationfx#endpoint_refresh_tool .

Once all the
                                          				phones in your network are supported by this release, upgrade your system.

Deprecated phones can also be removed after the upgrade. When the administrator logs in to Unified Communications Manager
                                                after completing the upgrade, the system displays a warning message notifying the administrator of the deprecated phones.

##### Licensing

You do not need to purchase a new device license to replace a deprecated phone with a supported phone. The device license
                                    becomes available for a new phone when you either remove the deprecated phone from the system, or when you switch to the new Unified Communications Manager version, and the deprecated phone fails to register.

### Network
                           	 Requirements

This section lists the requirements that your network must meet before you can deploy Unified Communications Manager and the IM and Presence Service .

#### IP Address
                              	 Requirements

A complete collaboration solution relies on DNS in order to function correctly for a number of services and thus requires
                                    a highly available DNS structure in place. If you have a basic IP telephony deployment and do not want to use DNS, you can
                                    configure Unified Communications Manager and IM and Presence Service to use IP addresses rather than hostnames to communicate with gateways and endpoint devices.

You must configure the server to use static IP addressing to ensure that the server obtains a fixed IP address. Using a static
                                    IP address also ensures that Cisco Unified IP Phones can register with the application when you plug the phones into the network.

#### DNS
                              	 requirements

Note the
                                    		  following requirements:

Mixed-mode DNS deployments not supported—Cisco does not support mixed-mode deployments. Both Unified Communications Manager and IM and Presence Service must either use or not use DNS.

If your deployment uses DNS— Unified Communications Manager and IM and Presence Service should use the same DNS server. If you use different DNS servers between IM and Presence Service and Unified Communications Manager , it is likely to cause abnormal system behavior.

If your deployment does not use DNS, you will need to edit the following Host Name/IP Address fields:

Server—In the Cisco Unified CM Administration Server Configuration window, set IP addresses for your cluster nodes.

IM and Presence UC Service—In the Cisco Unified CM Administration UC Service Configuration window, create an IM and Presence UC service that points to the IP address of the IM and Presence database publisher node.

CCMCIP Profiles—In the Cisco Unified CM IM and Presence Administration CCMCIP Profile Configuration window, point any CCMCIP profiles to the IP address of the host.

Multinode considerations—If you are using the multinode feature in IM and Presence Service , see the section regarding multinode deployments in the Configuration and Administration of the IM and Presence Service Guide for DNS configuration options.

#### Firewall Requirements

Ensure that you configure your firewall so that connections to port 22 are open, and aren't throttled. During the installation
                                    of Unified Communications Manager and IM and Presence subscriber nodes, multiple connections to the Unified Communications
                                    Manager publisher node are opened in quick succession. Throttling these connections could lead to a failed installation. For
                                    general security considerations, see the Security Guide for Cisco Unified Communications Manager .

For more information on the port usage, see the chapter 'Cisco Unified Communications Manager TCP and UDP Port Usage' in the System Configuration Guide for Cisco Unified Communications Manager .

#### SFTP Server Support

Use the information in the following table to determine which SFTP server solution to use in your system.

SFTP Server

Information

SFTP Server on Cisco Prime Collaboration Deployment

This server is the only SFTP server that is provided and tested by Cisco, and fully supported by Cisco TAC.

Version compatibility depends on your version of Unified Communications Manager and Cisco Prime Collaboration Deployment.
                                                See the Cisco Prime Collaboration Deployment Administration Guide before you upgrade its version (SFTP) or Unified Communications Manager to ensure that the versions are compatible.

SFTP Server from a Technology Partner

These servers are third party provided and third party tested. Version compatibility depends on the third party test. See
                                                the Technology Partner page if you upgrade their SFTP product and/or upgrade Unified Communications Manager for which versions
                                                are compatible:

https://developer.cisco.com/ecosystem/cpp/services/

SFTP Server from another Third Party

These servers are third party provided and are not officially supported by Cisco TAC.

Version compatibility is on a best effort basis to establish compatible SFTP versions and Unified Communications Manager versions.

#### Subnet
                              	 Limitations

Do not install Unified Communications Manager in a large Class A or Class B subnet that contains a large number of devices. For more information, see Cisco Collaboration System 12.x Solution Reference Network Designs (SRND) .

#### Cluster
                              	 Size

The number of Unified Communications Manager subscriber nodes in a cluster cannot exceed 4 subscriber nodes and 4 standby nodes, for a total of 8 subscribers. The total
                                    number of servers in a cluster, including the Unified Communications Manager publisher node, TFTP server, and media servers, cannot exceed 21.

The maximum number of IM and Presence Service nodes in a cluster is 6.

For more information, see "Cisco Collaboration Solutions Design Guidance" at http://www.cisco.com/go/ucsrnd .

#### IP Subnet Mask

If you are using a 24-bit IP subnet mask, ensure
                                    				  that you use the following format: 255.255.255.0 .
                                    				  Do not use the format 255.255.255.000 . Although 255.255.255.000 is a valid format, it may cause problems during the upgrade process. We recommend that you change the format before you begin
                                    an upgrade to avoid possible problems. You can change the subnet mask by executing the set network ip eth0
                                          						<server_IP_address> 255.255.255.0 command.

Other formats are supported for subnet masks and this limitation applies to 24-bit subnet masks only.

### Software Requirements

This section refers to application software requirements for Cisco Unified Communications Manager and the IM and Presence
                                 Service upgrades and migrations.

#### Device Name for Cisco Unified Mobile Communicator

Ensure
                                    				  that the device name for the Cisco Unified Mobile Communicator device contains
                                    				  15 or fewer characters. If the device name contains more than 15 characters for
                                    				  the Cisco Unified Mobile Communicator, the device does not migrate during the
                                    				  upgrade.

#### Export Restricted and Export
                              	 Unrestricted Software

This release of Unified Communications Manager and IM and Presence Service supports an export unrestricted (XU) version, in addition to the export restricted (K9) version.

Export unrestricted versions differs from restricted versions as follows:

Encryption of user payload (information exchange) is not supported.

External SIP interdomain federation with Microsoft OCS/Lync or AOL is not supported.

After you install an unrestricted release, you can never upgrade to a restricted version. A fresh install of a restricted
                                          version on a system that contains an unrestricted version is also not supported.

All nodes within a single cluster must be in the same mode. For example, Unified Communications Manager and IM and Presence Service in the same cluster must either all be in unrestricted mode or all be in restricted mode.

IP Phone security configurations are modified to disable signaling and media encryption (including encryption provided by
                                          the VPN phone feature).

For all Graphical User Interfaces (GUIs) and Command Line Interfaces (CLIs), the Administrator can view the product version
                                    (restricted or export unrestricted).

The following table describes the GUI items that are not available for the export unrestricted version of Unified Communications Manager and IM and Presence Service .

GUI Item

Location

Description

Cisco Unified CM Administration

VPN Configuration

Advanced Features > VPN

This menu and its options are not available.

Phone Security Profile Configuration

System > Security > Phone Security Profile

The Device Security Mode is set to Non Secure and is not configurable.

Cisco
                                                   						Unified CM IM and Presence Administration

Security Settings

You
                                                      						cannot check the Enable XMPP Client to IM/P Service Secure Mode setting.

You
                                                      						cannot check the Enable XMPP Router-to-Router Secure Mode setting.

You
                                                      						cannot check the Enable Web Client to IM/P Service Secure Mode setting.

The option to set SIP intra-cluster Proxy-to-Proxy Transport Protocol to TLS have been removed.

Service Parameter Configuration for Cisco SIP Proxy service

System > Service Parameters and choose Cisco SIP Proxy as the Service

All TLS
                                                      						options have been removed for the Transport Preferred Order parameter.

The TLS option have been removed from the SIP Route Header Transport Type parameter.

SIP Federated Domains

Presence > Inter-domain
                                                      						  Federation > SIP Federation

When you
                                                						configure interdomain federation to OCS/Lync, you will receive warning popup to
                                                						indicate that it is only possible to directly federate with another OCS/Lync
                                                						within the enterprise. Interdomain federation to OCS/Lync outside the
                                                						enterprise is not supported in unrestricted mode.

XMPP Federation Settings

Presence > Inter-domain
                                                      						  Federation > XMPP Federation > Settings

You cannot configure the security mode. It is set to NO TLS .

Proxy Configuration Settings

Presence > Routing > Settings

You
                                                						cannot set any TLS or HTTPS listeners as the preferred proxy listener.

#### Upgrades from Unified CM 9.x

Upgrades from Unified Communications Manager version 9.x to version 10.x or higher fail if you have a SIP Profile with any of the following names on version 9.x:

Standard SIP Profile

Standard SIP Profile For Cisco VCS

Standard SIP Profile For TelePresence Conferencing

Standard SIP Profile For TelePresence Endpoint

Standard SIP Profile for Mobile Device

If you have a SIP Profile with any of these names, you need to rename or delete it before proceeding with the upgrade.

#### OS Admin Account Required for CLI-Initiated IM and Presence Upgrades

If you are using the utils system upgrade CLI command to upgrade IM and Presence Service nodes, you must use the default OS admin account, as opposed to a user with
                                    administrator privileges. Otherwise, the upgrade will not have the required privilege level to install essential services,
                                    thereby causing the upgrade to fail. You can confirm the account’s privilege level by running the show myself CLI command. The account must have privilege level 4.

Note that this limitation exists for CLI-initiated upgrades of IM and Presence Service only and does not apply to Unified Communications Manager . Also note that this limitation may be fixed for newer ISO files. See your ISO Readme file for details on your specific ISO
                                    file. For-up-to date information on this limitation, see CSCvb14399 .

#### Upgrades from 11.5(1)SU2 with Push Notifications Enabled

If you are upgrading from the 11.5(1)SU2
                                    release and you had Push Notifications enabled in the old release,
                                    you must disable Push Notifications in the current release and then
                                    follow the onboarding process to enable Push Notifications once
                                    again. This is required due to API changes in this release that
                                    were not a part of the 11.5(1)SU2 release. Your upgraded system
                                    will not be able to send troubleshooting logs to the Cisco Cloud
                                    unless you disable Push Notifications and then follow the
                                    onboarding process for this release.

After you upgrade your system, do the
                                    following:

Step 1

Disable Push Notifications

Follow these steps:

From Cisco Unified CM Administration, choose Advanced Features > Cisco Cloud Onboarding .

Uncheck the following check boxes:

Enable Push Notifications

Send Troubleshooting information to the Cisco Cloud

Send encrypted PII to the Cisco Cloud for troubleshooting

Click Save .

Step 2

Add a Unified Communications Manager product instance into the Smart Licensing system.

See the "Smart Software Licensing" chapter at System Configuration Guide for Cisco Unified Communications Manager .

Step 3

Enable Push Notifications for this release.

For the full onboarding process, see the "Configure Push Notifications for Cisco Jabber on iPhone and iPad" chapter at System Configuration Guide for Cisco Unified Communications Manager .

#### Database Migration Required for Upgrades with Microsoft SQL Server

If you have Microsoft SQL Server deployed as an external database with the IM and Presence Service and you are upgrading from 11.5(1), 11.5(1)SU1, or 11.5(1)SU2, you must create a new SQL Server database and migrate
                                    to the new database. This is required due to enhanced data type support in this release. If you don't migrate your database,
                                    schema verification failure will occur on the existing SQL Server database and services that rely on the external database,
                                    such as persistent chat, will not start.

After you upgrade your IM and Presence Service, use this procedure to create a new SQL Server database and migrate data to the new database.

This migration is not required for Oracle or PostgreSQL external databases.

##### Before You Begin

The database migration is dependent on the MSSQL_migrate_script.sql script. Contact Cisco TAC to obtain a copy.

Step

Task

Step 1

Create a snapshot of your external Microsoft SQL Server database.

Step 2

Create a new (empty) SQL Server database. For details, see the following chapters in the Database Setup Guide for the IM and Presence Service :

"Microsoft SQL Installation and Setup"—See this chapter for details on how to create your new SQL server database on your
                                                      upgraded IM and Presence Service.

"IM and Presence Service External Database Setup"—After your new database is created, refer to this chapter to add the database
                                                      as an external database in the IM and Presence Service.

Step 3

Run the System Troubleshooter to confirm that there are no errors with the new database.

From Cisco Unified CM IM and Presence Administration, choose Diagnostics > System Troubleshooter .

Verify that no errors appear in the External Database Troubleshooter section.

Step 4

Restart the Cisco XCP Router on all IM and Presence Service cluster nodes:

From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Network Services .

From the Server menu, select an IM and Presence Service node and click Go .

Under IM and Presence Services , select Cisco XCP Router , and click Restart .

Step 5

Turn off services that depend on the external database:

From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Feature Services .

From the Server menu, select an IM and Presence node and click Go .

Under IM and Presence Services , select the following services:.

Cisco XCP Text Conference Manager

Cisco XCP File Transfer Manager

Cisco XCP Message Archiver

Click Stop .

Step 6

Run the following script to migrate data from the old database to the new database MSSQL_migrate_script.sql .

Contact Cisco TAC to obtain  a copy of this script

Step 7

Run the System Troubleshooter to confirm that there are no errors with the new database.

From Cisco Unified CM IM and Presence Administration, choose Diagnostics > System Troubleshooter .

Verify that no errors appear in the External Database Troubleshooter section.

Step 8

Start the services that you stopped previously.

From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Feature Services .

From the Server menu, select an IM and Presence node and click Go .

Under IM and Presence Services , select the following services:

Cisco XCP Text Conference Manager

Cisco XCP File Transfer Manager

Cisco XCP Message Archiver

Click Start .

Step 9

Confirm that the external database is running and that all chat rooms are visible from a Cisco Jabber client.  Delete the
                                                old database only after you're confident that the new database is working.

#### Upgrade Considerations for Upgrades from 12.0(1) to 12.5(1)

The following section provide information about the upgrades from 12.0(1) to 12.5(1) that your system must meet, and limitations
                                    that apply when you install or upgrade IM and Presence Service.

Please select the Reboot Option as “Reboot to upgraded partition” (switch version “Yes”) instead of default Reboot option
                                                as "Do not reboot after upgrade" (switch-version as “No”). Hence, the IM and Presence Service 12.5 will be compatible with the Unified Communications Manager 12.5 version.

Refresh upgrade from Unified Communications Manager 12.0.1. to 12.5 or from Unified Communications Manager previous release upgrade to 12.5 release:

#### IPsec Requirements

If you have IPsec configured with certificate-based authentication, make sure that the IPsec policy uses a CA-signed certificate.
                                    If you attempt to upgrade Unified Communications Manager with IPsec configured to use certificate-based authentication with
                                    self-signed certificates, the upgrade fails. Reconfigure the IPsec policy to use a CA-signed certificate.

Before starting the migration, disable the IPsec policy on all the nodes in the cluster.

#### Support for Intercluster Peers

The IM and Presence Service supports intercluster peers to clusters that are running different software versions. To find the interdomain federations
                                    that are supported, see the "Intercluster Peering Support" section in the Compatibility Matrix for Cisco Unified Communications Manager and IM and Presence Service .

#### Spectre/Meltdown Vulnerabilities During Upgrade

This release of Unified Communications Manager, Cisco IM and Presence Service, Cisco Emergency Responder, and Cisco Prime
                                    Collaboration Deployment contain software patches to address the Meltdown and Spectre microprocessor vulnerabilities.

Before you upgrade to Release 12.5(1) or above, we recommend that you work with your channel partner or account team to use
                                    the Cisco Collaboration Sizing Tool to compare your current deployment to an upgraded deployment. If required, change VM resources
                                    to ensure that your upgraded deployment provides the best performance.

### Licensing Requirements

The following sections provide information about the licensing requirements for Unified Communications Manager and the IM and Presence Service .

As of Unified Communications Manager Release 12.0(1), Smart Licensing replaces Prime License Manager . Smart Licensing requires you to have a Smart Account created and configured before you upgrade or migrate the Unified Communications Manager server.

Several deployment options through which Unified Communications Manager can connect to Cisco Smart Software Manager or Cisco Smart Software Manager satellite are:

Direct— Unified Communications Manager sends usage information directly over the internet. No additional components are needed.

Cisco Smart Software Manager satellite— Unified Communications Manager sends usage information to an on-premise Smart Software Manager. Periodically, an exchange of information is performed to
                                       keep the databases in synchronization. For more information on installation or configuration of the Smart Software Manager
                                       satellite, go to this URL: https://www.cisco.com/c/en/us/buy/smart-accounts/software-manager.html .

Proxy Server— Unified Communications Manager sends usage information over the internet through a proxy server.

#### Unified Communications Manager License Requirements

Cisco Smart Software Licensing is a new way of thinking about licensing. It adds flexibility to your licensing and simplifies
                                    it across the enterprise. It also delivers visibility into your license ownership and consumption.

Cisco Smart Software Licensing helps you to procure, deploy, and manage licenses easily where devices self-register and report
                                    license consumption, removing the need for product activation keys (PAK). It pools license entitlements in a single account
                                    and allows you to move licenses freely through the network, wherever you need them. It is enabled across Cisco products and
                                    managed by a direct cloud-based or mediated deployment model.

The Cisco Smart Software Licensing service registers the product instance, reports license usage, and obtains the necessary
                                    authorization from Cisco Smart Software Manager or Cisco Smart Software Manager satellite.

Cisco Smart Software Manager replaces Prime License Manager in Unified Communications Manager Release 12.0(1) and later versions. Cisco Prime License Manager is no longer used as of Release 12.0(1) and no longer appears
                                    in the Installed Applications pre-login screen.

If you have enabled the mixed-mode before upgrade and have not registered to Cisco Smart Software Manager or Cisco Smart
                                    Software Manager satellite then,

You see the warning message in the Cisco Unified CM Administration page and Cisco Unified OS Administration page as stated
                                          below:

Caution

The system is currently running Mixed mode. To continue running Mixed mode, please ensure Smart Licensing registration is
                                                      completed using the Registration Token received from the Smart/Virtual Account that has Allow export-controlled functionality
                                                      checked.

An alert named SmartLicenseExportControlNotAllowed is sent, when the Unified Communications Manager is not registered with the Registration Token.

For details on how to configure Cisco Smart Software Licensing, see the "Smart Software Licensing" chapter, located within
                                    the "Configure Initial Parameters for the System" at System Configuration Guide for Cisco Unified Communications Manager .

For more details on Cisco Smart Software Manager satellite, including the Smart Software Manager satellite Installation Guide , see http://www.cisco.com/go/smartsatellite .

##### Migration of
                                    		  PLM Licenses to Smart Entitlement

If you are
                                    		  eligible to upgrade to the Smart Licensing version of the product, then you are
                                    		  able to initiate the migration through the License Registration
                                       			 Portal or Cisco Smart Software
                                       			 Manager . You can self-initiate this process by downloading and
                                    		  installing the Smart Licensing version of the software and registering the
                                    		  device to a Smart Account using a Registration Token. The migration of any
                                    		  entitlements tracked by Cisco automatically migrates to the Customers Smart
                                    		  Account. You will also be able to initiate the migration of unused classic PAKs
                                    		  to Smart Accounts for future consumption by products in Smart Mode. This
                                    		  process is available through the License Registration
                                       			 Portal or Cisco Smart Software
                                       			 Manager .

Unified Communications Manager 9.0x and later version of 12.0(1)

If you are
                                          				holding an active Cisco Software Support Service (SWSS) contract, then you can
                                          				convert the classic licenses to smart entitlements through the Cisco Smart
                                          				Software Manager at https://software.cisco.com/#SmartLicensing-LicenseConversion .

Two types of
                                          				Migration are supported:

PAK
                                                					 based—Supported for already fulfilled, partially fulfilled and unfilled PAKs

Device
                                                					 based

Partial Conversion supports mixed environment of older and Unified Communications Manager 12.0(1) clusters.

##### Upgrade to
                                    		  Smart Entitlement

Unified Communications Manager Pre 9.0x (Device based) to 12.0(1)

You may contact
                                    		  Cisco Global Licensing Operations (GLO) for helping with migrating Device-based
                                    		  licenses to Smart Entitlement.

Customer may establish equivalent user-based licensing required by running License Count Utility (LCU). For more details,
                                    see http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/upgrade/uct/CUCM_BK_UCT_Admin_Guide/CUCM_BK_UCT_Admin_Guide_chapter_01.html .

From the LCU
                                    		  report, Customer may order respective quantity of Upgrade Licenses through
                                    		  Cisco Commerce Workspace. Beyond this, they would have to buy additional new
                                    		  licenses. For more details, see the Ordering Guide at http://www.cisco.com/c/en/us/partners/tools/collaboration-ordering-guides.html .

#### Specific License Reservation

Specific License Reservation (SLR) allows the customer to reserve licenses from their virtual account, tie them to a devices
                                 UDI and use their device with these reserved licenses in a disconnected mode. The customer reserves specific licenses and
                                 counts for a UDI from their virtual account. The following options describe the new functionality and design elements for
                                 Specific Reservation.

Command

Description

license smart reservation enable

Use this command to enable the license reservation feature.

license smart reservation disable

Use this command to disable the license reservation feature.

license smart reservation request

Use this command to generate reservation request code.

license smart reservation cancel

Use this command to cancel the reservation process before the authorization code is installed.

license smart reservation install "<authorization-code>"

Use this command to install the license reservation authorization-code generated on the Cisco Smart Software Manager.

license smart reservation return

Use this command to remove the license reservation authorization code that is installed and list of reserved entitlements.
                                             The device transitions back to an unregistered state.

license smart reservation return-authorization "<authorization code>"

Use this command to remove the license reservation authorization code that is entered by the user.

If you are upgrading from 12.0 to higher versions and enable license reservation feature on upgraded server, you should download ciscocm-ucm-resetudi.k3.cop.sgn from CCO and install on the upgraded CUCM before enabling reservation feature.

If you are upgrading the 12.5 system which is license reservation enabled to 14, see System Configuration Guide for Cisco Unified Communications Manager .

#### IM and Presence Service License Requirements

The IM and Presence Service does not require a server license or software version license. However, you must assign users and enable the IM and Presence Service for each assigned user.

With the Jabber for Everyone offer, no end user licenses are required to enable IM and Presence Service functionality. For
                                                more information, see Jabber for Everyone Quick Start Guide .

You can assign IM and Presence Service on a per user basis, regardless of the number of clients you associate with each user. When you assign IM and Presence Service to a user, this enables the user to send and receive IMs and availability updates. If users are not enabled for IM and Presence Service , they will not be able to log in to the IM and Presence Service server to view the availability of other users, send or receive IMs, and other users will not see their availability status.

You can enable a user for IM and Presence Service using any of the following options:

The End User Configuration window in Unified Communications Manager . For more information, see the Administration Guide for Cisco Unified Communications Manager .

The Bulk
                                          				Administration Tool (BAT)

Assign IM and Presence Service to a feature group template which you can reference from the Quick User/Phone Add window in Unified Communications Manager .

For more information, see the System Configuration Guide for Cisco Unified Communications Manager .

IM and Presence Service capabilities are included within both User Connect Licensing (UCL) and Cisco Unified Workspace Licensing (CUWL). IM and Presence Service capabilities can also be acquired for users that are not Unified Communications Manager IP Telephony users through the Jabber for Everyone Offer. For more information, see Jabber for Everyone Quick Start Guide .

## Supporting Documentation

The following documents contain additional supporting information that helps you to upgrade in specific cases.

Task

Setup virtualized Cisco hardware.

Refer to Cisco Collaboration on Virtual Servers in order to set up your virtualized platform. For details, see https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html .

Setup Cisco Business Edition 6000/7000 appliances

Refer to:

Installation Guide for Cisco Business Edition 6000 and 7000 — https://www.cisco.com/c/en/us/support/unified-communications/business-edition-6000/tsd-products-support-series-home.html

Installation Guide for Cisco Business Edition 6000 and 7000 — https://www.cisco.com/c/en/us/support/unified-communications/business-edition-7000/tsd-products-support-series-home.html

Replace existing hardware while preserving the configuration

Replace a Single Server or Cluster for Cisco Unified Communications Manager at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html .

Review VMware requirements

For VMware requirements and best practices, go to https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html .

For VMware vendor documentation, go to http://www.VMware.com .

Additional Planning and Sizing Resources

These documents also contain information that may help you to plan and size your upgraded system:

Cisco Collaboration Systems Solution Reference Network Designs (SRND) for at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-system/products-implementation-design-guides-list.html .

Cisco Preferred Architecture guides and Cisco Validated Design guides at http://www.cisco.com/c/en/us/solutions/enterprise/design-zone-collaboration/index.html .

Collaboration Virtual Machine Replacement Tool at http://ucs.cloudapps.cisco.com/ .

Cisco Quote Collab Tool at http://www.cisco.com/go/quotecollab .

Cisco Collaboration Sizing Tool at http://tools.cisco.com/cucst .

| Date | Revision |
|---|---|
| September 7, 2021 | Removed the followings sections from respective chapters as we need not perform them for upgrade scenarios: Pre-upgrade Tasks—Deactivate TFTP services Post-upgrade Tasks—Restart TFTP Services |

| Upgrade Type | Description | Upgrade Tools |
|---|---|---|
| Direct Standard Upgrade | A standard upgrade is a direct upgrade where you need to upgrade the application software, but not the underlying operating
                                          system. This is usually the simplest form of upgrade and would typically apply to upgrades from within the same major-minor
                                          release category, where the OS is the same for both releases. For release 12.5 or higher, direct standard upgrades have substantially improved durations, simpler procedures and reduced
                                          service impact. Example : Upgrades from 12.5(1) to 12.5(1)SU1. Note For standard upgrades where the preupgrade release is 12.5(1) or later, you can use the simplified clusterwide upgrade to
                                                   upgrade your entire cluster. | Note | For standard upgrades where the preupgrade release is 12.5(1) or later, you can use the simplified clusterwide upgrade to
                                                   upgrade your entire cluster. | The following tools are used to complete standard upgrades: Unified OS Admin CLI PCD Upgrade task |
| Note | For standard upgrades where the preupgrade release is 12.5(1) or later, you can use the simplified clusterwide upgrade to
                                                   upgrade your entire cluster. |
| Direct Refresh Upgrade | A direct refresh upgrade is a direct upgrade where you need to upgrade both the application software and the underlying operating
                                          system software. This would typically be used if you're upgrading from one major-minor release to another where the OS is
                                          different for the two releases. Example : Upgrades from 11.5(1) or 12.0(1) to 12.5(1) | The following tools are used to complete refresh upgrades: Unified OS Admin CLI PCD Upgrade task |
| Direct migration | A direct migration involves a 'repave' where multiple factors exist that can't address with just a direct upgrade. Direct
                                          Migration is used in the following cases: Site moves The desired upgrade requires you to change the infrastructure hardware and platform. Example : Upgrades from Unified CM 10.5(x) on ESXi 5.5 and Cisco UCS M3 generation hardware to 12.5(x) on ESXi 7.0 and Cisco UCS M5
                                                generation hardware. ESXi upgrade and/or Unified CM virtual machine configuration change Unified CM address/hostname change The desired upgrade requires a direct upgrade path that does not exist for the source release. Example : Unified CM 8.5(1) on ESXi to 12.5(x) on ESXi—no direct upgrade path exists making a migration mandatory. "Virtual to Virtual (V2V)" migration, where even if a direct upgrade path exists, direct migration is preferred to mitigate
                                                upgrade path complexity factors such as duration, service impact, and a short outage window. | The following tool is used to complete migrations: PCD Migration Fresh Install with Data Import |
| Migration from legacy releases | A legacy release is a release that is so old that no direct upgrade or direct migration path exists to the current release.
                                          The only option is a direct upgrade to a later release that supports PCD migration followed by a PCD migration to the current
                                          release. Example : Any upgrade from a pre-6.1(5) Unified CM or a pre-8.5(4) Cisco Unified IM and Presence. | For details, see Upgrading from Legacy Releases . |

| Note | For standard upgrades where the preupgrade release is 12.5(1) or later, you can use the simplified clusterwide upgrade to
                                                   upgrade your entire cluster. |
|---|---|

| Note | VMware was introduced as an optional deployment in Unified CM 8.x and 9.x. From Release 10.x forward, VMware became mandatory. |
|---|---|

| Note | Unless indicated otherwise, each release category includes the SU releases within that category. For example, 12.5(x) includes
                                       12.5(1)SU releases. In addition, releases like 10.5(x) and 11.x include any SU releases within those categories as well. |
|---|---|

| Source | Destination | Supported Upgrade Method | Version Switching* (Source to Destination and Vice Versa) |
|---|---|---|---|
| Cisco Unified Communications Manager Upgrade Paths |
| Unified CM 10.0(x) | 12.5(x) | PCD Migration** | Version switching not supported |
| Unified CM 10.5(x), 11.x, 12.0(x) | 12.5(x) | Unified OS Admin upgrade (direct refresh) CLI upgrade (direct refresh) PCD Upgrade (direct refresh)** PCD Migration** Fresh Install with Data Import only to destination 12.5(1)SU5 or later. Note If the source release is 10.5(x) and the destination release is 12.5(1) through 12.5(1)SU5, PCD Upgrade Task is supported. If the source release is 10.5(x) and the destination release is 12.5(1)SU6 and above, PCD Upgrade Task is not supported. | Note | If the source release is 10.5(x) and the destination release is 12.5(1) through 12.5(1)SU5, PCD Upgrade Task is supported. If the source release is 10.5(x) and the destination release is 12.5(1)SU6 and above, PCD Upgrade Task is not supported. | Version switching supported for upgrades, but not for migrations |
| Note | If the source release is 10.5(x) and the destination release is 12.5(1) through 12.5(1)SU5, PCD Upgrade Task is supported. If the source release is 10.5(x) and the destination release is 12.5(1)SU6 and above, PCD Upgrade Task is not supported. |
| Unified CM 12.5(x) | 12.5(y) | Unified OS Admin upgrade (direct standard) CLI upgrade (direct standard) PCD Upgrade (direct standard)** Fresh Install with Data Import only to destination 12.5(1)SU5 or later. | Version switching supported for upgrades, but not for migrations |
| IM and Presence Service Upgrade Paths |
| IM and Presence 10.0(x) | IM and Presence 12.5(x) | PCD Migration** | Version switching not supported |
| IM and Presence 10.5(x), 11.x or 12.0(x) | 12.5(x) | Unified OS Admin upgrade (direct refresh) CLI upgrade (direct refresh) PCD upgrade (direct refresh)** PCD Migration** Fresh Install with Data Import only to destination 12.5(1)SU5 or later. | Version switching supported for upgrades, but not supported for migrations. |
| IM and Presence 12.5(x) | 12.5(y) | Unified OS Admin upgrade (direct standard) CLI upgrade (direct standard) PCD upgrade (direct standard)** Fresh Install with Data Import only to destination 12.5(1)SU5 or later. | Version switching supported for upgrades, but not supported for migrations. |

| Note | If the source release is 10.5(x) and the destination release is 12.5(1) through 12.5(1)SU5, PCD Upgrade Task is supported. If the source release is 10.5(x) and the destination release is 12.5(1)SU6 and above, PCD Upgrade Task is not supported. |
|---|---|

| Note | For legacy upgrades, refer to Upgrading from Legacy Releases . This is required if you are upgrading from a pre-6.1(5) version of Cisco Unified Communications Manager, or from Cisco Unified
                                       Presence 8.0(x). |
|---|---|

| Upgrade Method | Support | When to use this method... | How to complete the Upgrade or Migration |
|---|---|---|---|
| Unified OS Admin or CLI upgrades | Direct upgrades (standard or refresh) via the Cisco Unified OS Administration GUI or CLI. | Consider this tool for: For simplified clusterwide upgrades You are only changing the application software and are not updating hardware or VMware. A direct upgrade path exists. You are only upgrading Unified CM and IM and Presence Service. There are no other UC applications. You are upgrading a single Unified CM cluster and a single IM and Presence subcluster. Note CLI upgrades provide the same support as Unified OS Admin upgrades, but from a different interface. | Note | CLI upgrades provide the same support as Unified OS Admin upgrades, but from a different interface. | Go to Upgrade Tasks |
| Note | CLI upgrades provide the same support as Unified OS Admin upgrades, but from a different interface. |
| PCD Upgrades | Handles direct upgrades (standard or refresh) via Cisco Prime Collaboration Deployment's upgrade task. | Consider this tool when: You have multiple clusters to upgrade. Your cluster has a large number of nodes, and you need help orchestrating the upgrade to forward the schedule. You need to upgrade other applications, such as Cisco Unity Connection or Cisco Unified Contact Center Express. | From Release is 10.x or later Run Upgrade Readiness COP File (Pre-upgrade) . Refer to the Cisco Prime Collaboration Deployment Administration Guide to run an upgrade or migration task. Run Upgrade Readiness COP File (Post-upgrade) Note If the From release is prior to 9.x, the Upgrade Readiness COP files do not work. You will need to complete the manual pre-upgrade
                                                   tasks and post-upgrade tasks in the Appendix. | Note | If the From release is prior to 9.x, the Upgrade Readiness COP files do not work. You will need to complete the manual pre-upgrade
                                                   tasks and post-upgrade tasks in the Appendix. |
| Note | If the From release is prior to 9.x, the Upgrade Readiness COP files do not work. You will need to complete the manual pre-upgrade
                                                   tasks and post-upgrade tasks in the Appendix. |
| PCD Migrations | Handles migrations via Cisco Prime Collaboration Deployment. | Consider this tool when: You are upgrading from an earlier release that did not use VMware. Your source release is so old that it does not support VMware. In addition to upgrading application versions, you must make ESXi updates as well. You are changing infrastructure hardware and platform. Your source release has previously direct upgraded from a pre-11.5 version and is having out of disk space issues. You may
                                                need to reinstall to the latest stack to maximize usable disk space. You have available infrastructure for temporary duplicate VMs and their required hardware. |

| Note | CLI upgrades provide the same support as Unified OS Admin upgrades, but from a different interface. |
|---|---|

| Note | If the From release is prior to 9.x, the Upgrade Readiness COP files do not work. You will need to complete the manual pre-upgrade
                                                   tasks and post-upgrade tasks in the Appendix. |
|---|---|

| Note | You should run the Upgrade Readiness COP file prior to the upgrade in order to maximize upgrade success. If you do not run
                                          this COP file, you increase the risk of an unsuccessful upgrade due to undetected issues on the source release. Cisco TAC
                                          may require that you run this COP file to provide effective technical support. |
|---|---|

| From | To | COP Files |
|---|---|---|
| Unified Communications Manager Upgrades |
| Unified CM 10.5(x), 11.0(x) | 12.5(x) | Direct Refresh upgrade Required COP file: ciscocm.enable-sha512sum-2021-signingkey-v1.0.cop.sgn. See the COP file for more information. |
| Unified CM 11.5(x) | 12.5(x) | Direct Refresh upgrade; COP file is required to increase the disk space. ciscocm.free_common_space_v<latest_version>.cop.sgn. To download the COP files and the Readme files, go to https://software.cisco.com , click Software Download link under Download & Upgrade section, and navigate to the Unified Communications > Call Control > Cisco Unified Communications Manager (CallManager) > <Version> > Unified Communications Manager/CallManager/Cisco Unity Connection Utilities . Required COP file: ciscocm.enable-sha512sum-2021-signingkey-v1.0.cop.sgn. See the COP file for more information. |
| Unified CM 12.0(1) | 12.5(x) | PCD Migrations require a COP file: ciscocm-slm-migration.k3.cop.sgn Note This requirement applies only for Prime Collaboration Deployment migrations from Release 12.0(1) of Unified Communications
                                                      Manager (build 12.0.1.10000-10). If you are migrating from a higher release, such as Unified Communications Manager 12.0(1)SU1,
                                                      you don't need to install the COP file. Required COP file: ciscocm.enable-sha512sum-2021-signingkey-v1.0.cop.sgn. See the COP file for more information. | Note | This requirement applies only for Prime Collaboration Deployment migrations from Release 12.0(1) of Unified Communications
                                                      Manager (build 12.0.1.10000-10). If you are migrating from a higher release, such as Unified Communications Manager 12.0(1)SU1,
                                                      you don't need to install the COP file. |
| Note | This requirement applies only for Prime Collaboration Deployment migrations from Release 12.0(1) of Unified Communications
                                                      Manager (build 12.0.1.10000-10). If you are migrating from a higher release, such as Unified Communications Manager 12.0(1)SU1,
                                                      you don't need to install the COP file. |
| Unified CM 12.5(x) | 12.5(y) | Direct Standard upgrade Required COP file: ciscocm.enable-sha512sum-2021-signingkey-v1.0.cop.sgn. See the COP file for more information. |
| IM and Presence Service Upgrades |
| 10.5(x), 11.x, 12.x | 12.5(x) | No COP files required |

| Note | This requirement applies only for Prime Collaboration Deployment migrations from Release 12.0(1) of Unified Communications
                                                      Manager (build 12.0.1.10000-10). If you are migrating from a higher release, such as Unified Communications Manager 12.0(1)SU1,
                                                      you don't need to install the COP file. |
|---|---|

| Item | Description |
|---|---|
| OVA templates | OVA files provide a set of predefined templates for virtual machine configuration. They cover items such as supported capacity
                                                levels and any required OS/VM/SAN alignment. You must use a VM configuration from the OVA file provided for the Unified Communications Manager and IM and Presence Service applications. The correct VM configuration to use from the OVA file is based on the size of the deployment. For information about OVA files,
                                                search for the topic "Unified Communications Virtualization Sizing Guidelines" at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/collaboration-virtualization-sizing.html . |
| VMware vSphere ESXi | You must install a version of vSphere ESXi hypervisor that meets the compatibility and support requirements for the release. If you use Cisco Prime Collaboration Deployment (PCD) to perform an upgrade or migration, you must also ensure that you install
                                                vSphere ESXi with the correct license type. PCD is not compatible with all the license types of vSphere ESXi because some
                                                of these licenses do not enable required VMware APIs. |
| VMware vCenter | VMware vCenter is optional when you deploy Unified Communications Manager or IM and Presence Service on Business Edition 6000/7000 appliances, or on UC on UCS tested reference configuration hardware. VMware vCenter is mandatory when you deploy on
                                                UC on UCS specs-based and third-party
                                                server specs-based hardware. |
| VM configuration virtual hardware specifications | Verify whether you need to change the virtual hardware specifications on your VM in order to upgrade to a new release of Unified Communications Manager or IM and Presence Service . For example, verify the requirements for vCPU, vRAM, vNIC adaptor type, and vDisk size, as well as other specifications. Any changes to a VM must align with the OVA configuration. VM changes that result in an unsupported OVA configuration are
                                                not allowed. For information about VM requirements, see  Readme file with the OVA template that supports your release. Note If Unified Communications Manager is upgraded to 12.5 or higher versions from release 11.5 or higher, using 80GB OVA it is
                                                            expected to have a higher active partition up to 98%. We can correct this by a system rebuilt with HDD 90GB/110GB. Use a default
                                                            110GB OVA template and rebuilt the node. Or on current 80GB OVA, prior to clean install, go to VM > Edit Settings , and increase the HDD size from 80GB to 90GB/110GB. Other specs remain the same. Adding HDD disk to the system already installed
                                                            only adds additional HDD space to common partition. | Note | If Unified Communications Manager is upgraded to 12.5 or higher versions from release 11.5 or higher, using 80GB OVA it is
                                                            expected to have a higher active partition up to 98%. We can correct this by a system rebuilt with HDD 90GB/110GB. Use a default
                                                            110GB OVA template and rebuilt the node. Or on current 80GB OVA, prior to clean install, go to VM > Edit Settings , and increase the HDD size from 80GB to 90GB/110GB. Other specs remain the same. Adding HDD disk to the system already installed
                                                            only adds additional HDD space to common partition. |
| Note | If Unified Communications Manager is upgraded to 12.5 or higher versions from release 11.5 or higher, using 80GB OVA it is
                                                            expected to have a higher active partition up to 98%. We can correct this by a system rebuilt with HDD 90GB/110GB. Use a default
                                                            110GB OVA template and rebuilt the node. Or on current 80GB OVA, prior to clean install, go to VM > Edit Settings , and increase the HDD size from 80GB to 90GB/110GB. Other specs remain the same. Adding HDD disk to the system already installed
                                                            only adds additional HDD space to common partition. |

| Note | If Unified Communications Manager is upgraded to 12.5 or higher versions from release 11.5 or higher, using 80GB OVA it is
                                                            expected to have a higher active partition up to 98%. We can correct this by a system rebuilt with HDD 90GB/110GB. Use a default
                                                            110GB OVA template and rebuilt the node. Or on current 80GB OVA, prior to clean install, go to VM > Edit Settings , and increase the HDD size from 80GB to 90GB/110GB. Other specs remain the same. Adding HDD disk to the system already installed
                                                            only adds additional HDD space to common partition. |
|---|---|

| Deprecated Phone Models for this Release | First Deprecated as of... |
|---|---|
| Cisco Unified IP Phone 7970G Cisco Unified IP Phone 7971G-GE Cisco Unified Wireless IP Phone 7921G | 12.0(1) and later releases |
| Cisco IP Phone 12 SP+ and related models Cisco IP Phone 30 VIP and related models Cisco Unified IP Phone 7902 Cisco Unified IP Phone 7905 Cisco Unified IP Phone 7910 Cisco Unified IP Phone 7910SW Cisco Unified IP Phone 7912 Cisco Unified Wireless IP Phone 7920 Cisco Unified IP Conference Station 7935 | 11.5(1) and later releases |

| Note | Deprecated phones can also be removed after the upgrade. When the administrator logs in to Unified Communications Manager
                                                after completing the upgrade, the system displays a warning message notifying the administrator of the deprecated phones. |
|---|---|

| Note | We recommend that you disable the "Intruder/Intrusion Detection" and/or "Brut Force Attack" features during upgrade and installs
                                             because these Firewall features are known to cause upgrades and installations to fail. |
|---|---|

| SFTP Server | Information |
|---|---|
| SFTP Server on Cisco Prime Collaboration Deployment | This server is the only SFTP server that is provided and tested by Cisco, and fully supported by Cisco TAC. Version compatibility depends on your version of Unified Communications Manager and Cisco Prime Collaboration Deployment.
                                                See the Cisco Prime Collaboration Deployment Administration Guide before you upgrade its version (SFTP) or Unified Communications Manager to ensure that the versions are compatible. |
| SFTP Server from a Technology Partner | These servers are third party provided and third party tested. Version compatibility depends on the third party test. See
                                                the Technology Partner page if you upgrade their SFTP product and/or upgrade Unified Communications Manager for which versions
                                                are compatible: https://developer.cisco.com/ecosystem/cpp/services/ |
| SFTP Server from another Third Party | These servers are third party provided and are not officially supported by Cisco TAC. Version compatibility is on a best effort basis to establish compatible SFTP versions and Unified Communications Manager versions. Note These products have not been tested by Cisco and we cannot guarantee functionality. Cisco TAC does not support these products.
                                                         For a fully tested and supported SFTP solution, use Cisco Prime Collaboration Deployment or a Technology Partner. | Note | These products have not been tested by Cisco and we cannot guarantee functionality. Cisco TAC does not support these products.
                                                         For a fully tested and supported SFTP solution, use Cisco Prime Collaboration Deployment or a Technology Partner. |
| Note | These products have not been tested by Cisco and we cannot guarantee functionality. Cisco TAC does not support these products.
                                                         For a fully tested and supported SFTP solution, use Cisco Prime Collaboration Deployment or a Technology Partner. |

| Note | These products have not been tested by Cisco and we cannot guarantee functionality. Cisco TAC does not support these products.
                                                         For a fully tested and supported SFTP solution, use Cisco Prime Collaboration Deployment or a Technology Partner. |
|---|---|

| Note | Unrestricted versions of software are intended only for a specific set of customers who do not want various security capabilities;
                                             unrestricted versions are not intended for general deployments. |
|---|---|

| Note | Be aware that after you install an unrestricted release, you can never upgrade to a restricted version. You are not allowed
                                             to perform a fresh installation of a restricted version on a system that contains an unrestricted version. |
|---|---|

| GUI Item | Location | Description |
|---|---|---|
| Cisco Unified CM Administration |
| VPN Configuration | Advanced Features > VPN | This menu and its options are not available. |
| Phone Security Profile Configuration | System > Security > Phone Security Profile | The Device Security Mode is set to Non Secure and is not configurable. |
| Cisco
                                                   						Unified CM IM and Presence Administration |
| Security Settings | System > Security > Settings | You
                                                      						cannot check the Enable XMPP Client to IM/P Service Secure Mode setting. You
                                                      						cannot check the Enable XMPP Router-to-Router Secure Mode setting. You
                                                      						cannot check the Enable Web Client to IM/P Service Secure Mode setting. The option to set SIP intra-cluster Proxy-to-Proxy Transport Protocol to TLS have been removed. |
| Service Parameter Configuration for Cisco SIP Proxy service | System > Service Parameters and choose Cisco SIP Proxy as the Service | All TLS
                                                      						options have been removed for the Transport Preferred Order parameter. The TLS option have been removed from the SIP Route Header Transport Type parameter. |
| SIP Federated Domains | Presence > Inter-domain
                                                      						  Federation > SIP Federation | When you
                                                						configure interdomain federation to OCS/Lync, you will receive warning popup to
                                                						indicate that it is only possible to directly federate with another OCS/Lync
                                                						within the enterprise. Interdomain federation to OCS/Lync outside the
                                                						enterprise is not supported in unrestricted mode. |
| XMPP Federation Settings | Presence > Inter-domain
                                                      						  Federation > XMPP Federation > Settings | You cannot configure the security mode. It is set to NO TLS . |
| Proxy Configuration Settings | Presence > Routing > Settings | You
                                                						cannot set any TLS or HTTPS listeners as the preferred proxy listener. |

| Step 1 | Disable Push Notifications Follow these steps: From Cisco Unified CM Administration, choose Advanced Features > Cisco Cloud Onboarding . Uncheck the following check boxes: Enable Push Notifications Send Troubleshooting information to the Cisco Cloud Send encrypted PII to the Cisco Cloud for troubleshooting Click Save . |
|---|---|
| Step 2 | Add a Unified Communications Manager product instance into the Smart Licensing system. See the "Smart Software Licensing" chapter at System Configuration Guide for Cisco Unified Communications Manager . |
| Step 3 | Enable Push Notifications for this release. For the full onboarding process, see the "Configure Push Notifications for Cisco Jabber on iPhone and iPad" chapter at System Configuration Guide for Cisco Unified Communications Manager . |

| Note | This migration is not required for Oracle or PostgreSQL external databases. |
|---|---|

| Step | Task |
|---|---|
| Step 1 | Create a snapshot of your external Microsoft SQL Server database. |
| Step 2 | Create a new (empty) SQL Server database. For details, see the following chapters in the Database Setup Guide for the IM and Presence Service : "Microsoft SQL Installation and Setup"—See this chapter for details on how to create your new SQL server database on your
                                                      upgraded IM and Presence Service. "IM and Presence Service External Database Setup"—After your new database is created, refer to this chapter to add the database
                                                      as an external database in the IM and Presence Service. |
| Step 3 | Run the System Troubleshooter to confirm that there are no errors with the new database. From Cisco Unified CM IM and Presence Administration, choose Diagnostics > System Troubleshooter . Verify that no errors appear in the External Database Troubleshooter section. |
| Step 4 | Restart the Cisco XCP Router on all IM and Presence Service cluster nodes: From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Network Services . From the Server menu, select an IM and Presence Service node and click Go . Under IM and Presence Services , select Cisco XCP Router , and click Restart . |
| Step 5 | Turn off services that depend on the external database: From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Feature Services . From the Server menu, select an IM and Presence node and click Go . Under IM and Presence Services , select the following services:. Cisco XCP Text Conference Manager Cisco XCP File Transfer Manager Cisco XCP Message Archiver Click Stop . |
| Step 6 | Run the following script to migrate data from the old database to the new database MSSQL_migrate_script.sql . Note Contact Cisco TAC to obtain  a copy of this script | Note | Contact Cisco TAC to obtain  a copy of this script |
| Note | Contact Cisco TAC to obtain  a copy of this script |
| Step 7 | Run the System Troubleshooter to confirm that there are no errors with the new database. From Cisco Unified CM IM and Presence Administration, choose Diagnostics > System Troubleshooter . Verify that no errors appear in the External Database Troubleshooter section. |
| Step 8 | Start the services that you stopped previously. From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Feature Services . From the Server menu, select an IM and Presence node and click Go . Under IM and Presence Services , select the following services: Cisco XCP Text Conference Manager Cisco XCP File Transfer Manager Cisco XCP Message Archiver Click Start . |
| Step 9 | Confirm that the external database is running and that all chat rooms are visible from a Cisco Jabber client.  Delete the
                                                old database only after you're confident that the new database is working. |

| Note | Contact Cisco TAC to obtain  a copy of this script |
|---|---|

| Note | Please select the Reboot Option as “Reboot to upgraded partition” (switch version “Yes”) instead of default Reboot option
                                                as "Do not reboot after upgrade" (switch-version as “No”). Hence, the IM and Presence Service 12.5 will be compatible with the Unified Communications Manager 12.5 version. |
|---|---|

| Note | Before upgrading, run the pre-upgrade Upgrade Readiness COP File. The COP file will run a series of tests to check the pre-upgrade
                                             health and connectivity of your system. If the COP file highlights issues that need to be addressed, fix them before proceeding
                                             with the upgrade. |
|---|---|

| Note | Before starting the migration, disable the IPsec policy on all the nodes in the cluster. |
|---|---|

| Note | As of Unified Communications Manager Release 12.0(1), Smart Licensing replaces Prime License Manager . Smart Licensing requires you to have a Smart Account created and configured before you upgrade or migrate the Unified Communications Manager server. |
|---|---|

| Note | Cisco Smart Software Manager satellite is an on-premises collector similar to a standalone Prime License Manager . |
|---|---|

| Caution | The system is currently running Mixed mode. To continue running Mixed mode, please ensure Smart Licensing registration is
                                                      completed using the Registration Token received from the Smart/Virtual Account that has Allow export-controlled functionality
                                                      checked. |
|---|---|

| Command | Description |
|---|---|
| license smart reservation enable | Use this command to enable the license reservation feature. |
| license smart reservation disable | Use this command to disable the license reservation feature. |
| license smart reservation request | Use this command to generate reservation request code. |
| license smart reservation cancel | Use this command to cancel the reservation process before the authorization code is installed. |
| license smart reservation install "<authorization-code>" | Use this command to install the license reservation authorization-code generated on the Cisco Smart Software Manager. |
| license smart reservation return | Use this command to remove the license reservation authorization code that is installed and list of reserved entitlements.
                                             The device transitions back to an unregistered state. |
| license smart reservation return-authorization "<authorization code>" | Use this command to remove the license reservation authorization code that is entered by the user. |

| Note | If you are upgrading from 12.0 to higher versions and enable license reservation feature on upgraded server, you should download ciscocm-ucm-resetudi.k3.cop.sgn from CCO and install on the upgraded CUCM before enabling reservation feature. |
|---|---|

| Note | If you are upgrading the 12.5 system which is license reservation enabled to 14, see System Configuration Guide for Cisco Unified Communications Manager . |
|---|---|

| Note | With the Jabber for Everyone offer, no end user licenses are required to enable IM and Presence Service functionality. For
                                                more information, see Jabber for Everyone Quick Start Guide . |
|---|---|

| Task |  |
|---|---|
| Setup virtualized Cisco hardware. | Refer to Cisco Collaboration on Virtual Servers in order to set up your virtualized platform. For details, see https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html . |
| Setup Cisco Business Edition 6000/7000 appliances | Refer to: Installation Guide for Cisco Business Edition 6000 and 7000 — https://www.cisco.com/c/en/us/support/unified-communications/business-edition-6000/tsd-products-support-series-home.html Installation Guide for Cisco Business Edition 6000 and 7000 — https://www.cisco.com/c/en/us/support/unified-communications/business-edition-7000/tsd-products-support-series-home.html |
| Replace existing hardware while preserving the configuration | Replace a Single Server or Cluster for Cisco Unified Communications Manager at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html . |
| Review VMware requirements | For VMware requirements and best practices, go to https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html . For VMware vendor documentation, go to http://www.VMware.com . |
| Additional Planning and Sizing Resources | These documents also contain information that may help you to plan and size your upgraded system: Cisco Collaboration Systems Solution Reference Network Designs (SRND) for at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-system/products-implementation-design-guides-list.html . Cisco Preferred Architecture guides and Cisco Validated Design guides at http://www.cisco.com/c/en/us/solutions/enterprise/design-zone-collaboration/index.html . Collaboration Virtual Machine Replacement Tool at http://ucs.cloudapps.cisco.com/ . Cisco Quote Collab Tool at http://www.cisco.com/go/quotecollab . Cisco Collaboration Sizing Tool at http://tools.cisco.com/cucst . |