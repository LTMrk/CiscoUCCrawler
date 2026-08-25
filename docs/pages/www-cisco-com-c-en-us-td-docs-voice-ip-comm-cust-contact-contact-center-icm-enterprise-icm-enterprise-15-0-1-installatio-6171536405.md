---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-installatio-6171536405
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/installation/guide/ucce_b_150_install_upgrade_guide/preparation.html
retrieved_at: 2026-08-25T00:10:12.893513+00:00
---

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: Preparation

## Chapter: Preparation

# Preparation

## Scenarios

Cisco Unified Contact Center Enterprise (Unified CCE) is supported only in a virtualized
                           			environment.

### Installation Scenario

The CCE components are supported on the following platforms in 15.0(1) release:

Microsoft Windows Server 2019 and Microsoft SQL Server 2019

Microsoft Windows Server 2022 and Microsoft SQL Server 2022

In a virtualized environment, you can run Unified CCE on a VMware ESXi platform. Run the virtual machines (VMs) on Cisco
                              Unified Computing System (UCS) C-series servers, or equivalent third-party servers.

Install the Unified CCE components after you configure the VMs.

You can use the OVA template to deploy the VMs before beginning with the installation of Unified CCE components.

For more information about the complete procedure, see the Installation Task Flow .

If you are planning to deploy VMs with Windows Server 2019, you must change the OVA Guest OS to Windows Server 2019.

The Common Ground upgrade from Windows Server 2016 and SQL Server 2017 is only supported if an in-place platform upgrade is
                                          performed to Windows Server 2022 and SQL Server 2022, and not to Windows Server 2019 and SQL Server 2019.

### Upgrade Scenarios

This release contains an updated database schema. Use the Enhanced Database Migration Tool (EDMT) to perform a schema upgrade
                              during the upgrade process.

You can upgrade from Unified CCE 12.5(2), CCE 12.6(x) to Unified CCE 15.0(1) by using one of the following two methods:

CE 15.0(1) SU1 supports upgrades from 12.6(2) and 15.0(1). CCE VOS components have version 15.0(1) SU1, and Windows components
                                                have ES202603.

It is recommended to follow the Multistage Upgrade Workflow when upgrading from 12.6(2) to 15.0(1) SU1. Upgrades from 15.0(1)
                                                to 15.0(1) SU1 do not require the Multistage Upgrade Workflow; components can be upgraded in any order.

The deployed version displayed on the VOS component CLI does not explicitly display "SU1." Verify the installation by checking
                                                the version string for the 10100 suffix, which identifies the 15.0 SU1 release (for example, 15.0.1.10100-168).

Unified CCE 15.0(1) installer and EDMT 15.0(1) will not allow the upgrade from the supported previous versions configured
                                          with unsupported deployment type. Deployment type need to be updated before the upgrade. For more details, refer to the below
                                          upgrade methods. For the details on the list of unsupported deployment type and replacement, check the Removed and Unsupported Features section in Release Notes for Cisco Contact Center Enterprise Solutions .

Common Ground Upgrades : The Common Ground method is an in-place upgrade performed on your existing virtual machine which involves upgrading the
                                    Cisco Unified Contact Center Enterprise and all other associated software that is hosted on it. If your hardware meets the
                                    requirements for this release, you can perform a Common Ground upgrade without acquiring extra hardware.

The Common Ground upgrade from Windows Server 2016 and SQL Server 2017 is only supported if an in-place platform upgrade is
                                                performed to Windows Server 2022 and SQL Server 2022, and not to Windows Server 2019 and SQL Server 2019.

Unified CCE 15.0(1) EDMT and Installer will block the upgrade from the supported previous versions configured with unsupported
                                                deployment type.

Technology Refresh Upgrades : Use the Technology Refresh upgrade method to upgrade your hardware at the same time as the Cisco Unified Contact Center
                                    Enterprise system. When using the Technology Refresh method, you prepare a destination system on new hardware and then migrate
                                    data from your existing deployment to the new one.

Follow the documented procedures to build a parallel network using new hardware and prestage it with configuration data to
                                    support the existing production network. Use the Enhanced Database Migration Tool (EDMT) to transfer data and perform a schema
                                    upgrade during the upgrade process. Don’t use backup and restore procedures to perform the prestaged configuration on the
                                    parallel network.

During migration of data from source to destination database, if unsupported deployment is configured in the source database
                                    then the EDMT will set the deployment type to Not Specified in destination database. After Unified CCE 15.0(1) installation, administrators can update the deployment type to supported
                                    deployment type from Unified CCE Admin user interface. During cutover, if the source database is configured with unsupported
                                    deployment, and destination database is set with either supported deployment type or Not Specified then the EDMT will retain the deployment type configured in the destination database. The Unified CCE 15.0(1) installer also
                                    detects and blocks the upgrade from unsupported deployment type.

Upgrade scenarios are considered at a component level; you can perform one type of upgrade on one component, and another type
                              of upgrade on another component. However, the A and B sides of any given component must be running on identical hardware.

Follow the task flow and tasks for the upgrade scenario that applies to each individual component involved in the overall
                              upgrade.

While upgrading from previous versions of Unified ICM / Unified CCE using the base installer for the current release, make
                                          sure that there are no other Windows sessions that are active. These sessions may have inadvertently left open some Unified
                                          CCE tools like Configuration Manager. This can prevent the tools from getting upgraded appropriately and this can cause the
                                          tool to malfunction or assert. The installer logs indicate that some files were locked during the upgrade. To resolve the
                                          issue with these tools that weren’t upgraded, you must rerun the base-installer and ensure that no other windows sessions
                                          are open.

## System Requirements

Before you start installation or upgrade activities, plan your Unified CCE contact center installation or upgrade. For system
                              requirements, see the Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

By default, Windows Defender is enabled on Windows Server. For more information on Windows Defender antivirus compatibility,
                              see https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-antivirus/windows-defender-antivirus-compatibility .

Before proceeding with Unified ICM application installation, ensure that you follow the antivirus guidelines specified in
                              the Section, Antivirus Guidelines of the Security Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

Unified ICM installation can also take longer than expected due to scanning of files by Windows Defender. Based on your IT
                              policy, either:

Disable Windows Defender. For more information, see Disable Microsoft Defender Antivirus procedure in Microsoft documentation.

-OR-

Add the Unified ICM product folder <ICM install directory:>\icm to the exclusion list of Windows Defender. For more information, see https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-antivirus/configure-extension-file-exclusions-windows-defender-antivirus .

On Logger, Rogger, AW, and HDS servers, the Unified CCE Installer adds BUILTIN\Administrators to SQL security logins and assigns sysadmin role to it. This is required for Logger and Administration & Data Server services to function appropriately.

Ensure that the system is ready, and meets all requirements for supported hardware and software.

This section provides a summary of the requirements for Unified CCE. If you have not confirmed all the information in this
                              section, complete the planning phase before proceeding further.

For more information, see these documents:

Solution Design Guide for Cisco Unified Contact Center Enterprise at http://www.cisco.com/en/US/products/sw/custcosw/ps1844/products_implementation_design_guides_list.html

Virtualization for Unified Contact Center Enterprise at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html

Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html

### Platform Requirements

Server selection for Unified CCE in  a virtualized environment involves several factors, including:

The server and all related hardware must be  supported for use in a virtualized Unified CCE system

Minimum specifications for processing, memory, and storage

Whether you want a packaged and tested Cisco configuration (Tested Reference Configuration or TRC) or a configuration that
                                       you base on Cisco-defined minimum requirements (Specs-based Configuration)

Compatibility requirements for all hardware, and Cisco and third-party software including the VMware required to run and manage
                                       a virtual environment

Confirm that your hardware selection is supported for Unified CCE and meets all minimum specifications:

UCS C-series (TRC):

VMware vSphere ESXi

VMware vCenter (Optional)

Virtualization for Unified Contact Center Enterprise at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html

UCS C-series (Specs-based):

VMware vCenter

VMware vSphere ESXi

Third-party (Specs-based)

VMware vCenter

VMware vSphere ESXi

In addition to confirming that your servers meet minimum specifications, confirm that your server choice is compatible with
                                 all Cisco and third-party software.

### Network Requirements

Network requirements for virtualized Unified CCE systems vary widely, depending on the size and type of Unified CCE solution
                                 deployment. Confirm that you have clearly established all network requirements before you install or upgrade a Unified CCE
                                 contact center.

For more information, see Virtualization for Unified Contact Center Enterprise at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html .

### Transport Layer
                           	 Security Version 1.2 Required

Contact center enterprise solutions require the use of TLS 1.2 connections in this release. Our services accept incoming TLS
                              connections over TLS 1.2. All outgoing TLS connection use TLS 1.2.

All clients that connect to either our web interfaces or databases must
                              		support TLS 1.2.

For more information see, Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

### Software License
                           	 Requirements

#### Third-Party
                                 		  Products

For detailed information about the software editions and versions supported for this release, see the Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

Before you begin
                                 		  an installation or upgrade of any part of your contact center, confirm the
                                 		  following:

That you have
                                       				all the required software products.

That all the
                                       				software versions are compatible with each other.

That all
                                       				software versions are also compatible with all hardware and VMware.

With the introduction of release CCE 15.0(1), you are no longer required to update Agent licenses for each new major release.
                                             Existing Agent licenses will continue to work after the CCE software is upgraded. Only the CCE Media SKU is release-specific
                                             and can be ordered for each release via Cisco Commerce Workspace (CCW) or downloaded from Cisco.com.

### Virtualization
                           	 Requirements

You run the Unified Contact Center Enterprise solution on VMware ESXi platform.

The following requirements apply to VMware on virtual machines for Unified CCE:

After you install the Unified CCE components on each VM, install the latest VMware Tools from your VMware host using the VMware
                                       Tool default settings.

Update the VMware Tools whenever  you
                                                   				  patch or upgrade  ESXi.

For more information, see Virtualization for Unified Contact Center Enterprise at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html .

### ESXi
                           	 Supportability

For information on
                                 		  supported versions of ESXi for this release see Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

As part of the Common Ground upgrade process, if there are no available overlapping supported ESXi versions, upgrade the Unified
                                 CCE software first if a back-out of the upgrade is required.

If the upgrade is
                                 		  successful and working, you can then proceed to upgrade ESXi to a supported
                                 		  version for final testing and restoring production operation.

### Compatibility
                           	 Requirements

As part of the planning process, ensure that all hardware, Cisco software, third-party software, VMware, and firmware are
                                 compatible. Confirm that you meet all the following compatibility requirements:

VMware Required firmware

See the following:

For more information, see Virtualization for Unified Contact Center Enterprise at http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html .

Cisco Installation and Upgrade Guides at http://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-rack-servers/products-installation-guides-list.html

Cisco software product intercompatibility

Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html

Review the compatibility between different versions of the Cisco components to plan upgrades that occur across multiple maintenance
                                                         windows. Components that are upgraded in one maintenance window must continue to operate with other components that are still
                                                         at the previous version until the full upgrade is completed.

Windows OS and SNMP

SNMP Service

SNMP MI Provider

See the following:

SNMP Guide for Cisco Unified Contact Center Enterprise at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html

Serviceability Guide for Cisco Unified Contact Center Enterprise at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html

Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html

### Java Requirements

CCE components use OpenJDK for Java runtime environment (JRE). The 15.0(1) CCE installer will install the required OpenLogic-OpenJDK
                              JRE 21 (64-bit).

Administration Client machine will remain in OpenLogic-OpenJDK JRE 8 (32-bit).

| Note | If you are planning to deploy VMs with Windows Server 2019, you must change the OVA Guest OS to Windows Server 2019. |
|---|---|

| Note | The Common Ground upgrade from Windows Server 2016 and SQL Server 2017 is only supported if an in-place platform upgrade is
                                          performed to Windows Server 2022 and SQL Server 2022, and not to Windows Server 2019 and SQL Server 2019. |
|---|---|

| Note | CE 15.0(1) SU1 supports upgrades from 12.6(2) and 15.0(1). CCE VOS components have version 15.0(1) SU1, and Windows components
                                                have ES202603. It is recommended to follow the Multistage Upgrade Workflow when upgrading from 12.6(2) to 15.0(1) SU1. Upgrades from 15.0(1)
                                                to 15.0(1) SU1 do not require the Multistage Upgrade Workflow; components can be upgraded in any order. The deployed version displayed on the VOS component CLI does not explicitly display "SU1." Verify the installation by checking
                                                the version string for the 10100 suffix, which identifies the 15.0 SU1 release (for example, 15.0.1.10100-168). |
|---|---|

| Note | Unified CCE 15.0(1) installer and EDMT 15.0(1) will not allow the upgrade from the supported previous versions configured
                                          with unsupported deployment type. Deployment type need to be updated before the upgrade. For more details, refer to the below
                                          upgrade methods. For the details on the list of unsupported deployment type and replacement, check the Removed and Unsupported Features section in Release Notes for Cisco Contact Center Enterprise Solutions . |
|---|---|

| Note | The Common Ground upgrade from Windows Server 2016 and SQL Server 2017 is only supported if an in-place platform upgrade is
                                                performed to Windows Server 2022 and SQL Server 2022, and not to Windows Server 2019 and SQL Server 2019. Unified CCE 15.0(1) EDMT and Installer will block the upgrade from the supported previous versions configured with unsupported
                                                deployment type. |
|---|---|

| Note | While upgrading from previous versions of Unified ICM / Unified CCE using the base installer for the current release, make
                                          sure that there are no other Windows sessions that are active. These sessions may have inadvertently left open some Unified
                                          CCE tools like Configuration Manager. This can prevent the tools from getting upgraded appropriately and this can cause the
                                          tool to malfunction or assert. The installer logs indicate that some files were locked during the upgrade. To resolve the
                                          issue with these tools that weren’t upgraded, you must rerun the base-installer and ensure that no other windows sessions
                                          are open. |
|---|---|

| Server | VMware required | For detailed requirements information, see |
|---|---|---|
| UCS C-series (TRC): | VMware vSphere ESXi VMware vCenter (Optional) | Virtualization for Unified Contact Center Enterprise at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html |
| UCS C-series (Specs-based): | VMware vCenter VMware vSphere ESXi |
| Third-party (Specs-based) | VMware vCenter VMware vSphere ESXi |

| Note | For detailed information about the software editions and versions supported for this release, see the Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html . |
|---|---|

| Note | With the introduction of release CCE 15.0(1), you are no longer required to update Agent licenses for each new major release.
                                             Existing Agent licenses will continue to work after the CCE software is upgraded. Only the CCE Media SKU is release-specific
                                             and can be ordered for each release via Cisco Commerce Workspace (CCW) or downloaded from Cisco.com. |
|---|---|

| Note | Update the VMware Tools whenever  you
                                                   				  patch or upgrade  ESXi. |
|---|---|

| For this compatibility information | See |
|---|---|
| VMware Required firmware | See the following: For more information, see Virtualization for Unified Contact Center Enterprise at http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html . Cisco Installation and Upgrade Guides at http://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-rack-servers/products-installation-guides-list.html |
| Cisco software product intercompatibility | Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html Note Review the compatibility between different versions of the Cisco components to plan upgrades that occur across multiple maintenance
                                                         windows. Components that are upgraded in one maintenance window must continue to operate with other components that are still
                                                         at the previous version until the full upgrade is completed. | Note | Review the compatibility between different versions of the Cisco components to plan upgrades that occur across multiple maintenance
                                                         windows. Components that are upgraded in one maintenance window must continue to operate with other components that are still
                                                         at the previous version until the full upgrade is completed. |
| Note | Review the compatibility between different versions of the Cisco components to plan upgrades that occur across multiple maintenance
                                                         windows. Components that are upgraded in one maintenance window must continue to operate with other components that are still
                                                         at the previous version until the full upgrade is completed. |
| Windows OS and SNMP SNMP Service SNMP MI Provider | See the following: SNMP Guide for Cisco Unified Contact Center Enterprise at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html Serviceability Guide for Cisco Unified Contact Center Enterprise at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html |
| Third party software products | Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html |

| Note | Review the compatibility between different versions of the Cisco components to plan upgrades that occur across multiple maintenance
                                                         windows. Components that are upgraded in one maintenance window must continue to operate with other components that are still
                                                         at the previous version until the full upgrade is completed. |
|---|---|

| Note | Administration Client machine will remain in OpenLogic-OpenJDK JRE 8 (32-bit). |
|---|---|