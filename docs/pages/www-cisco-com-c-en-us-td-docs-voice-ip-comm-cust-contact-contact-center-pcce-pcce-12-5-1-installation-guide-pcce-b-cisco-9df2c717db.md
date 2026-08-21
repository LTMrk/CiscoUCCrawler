---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-5-1-installation-guide-pcce-b-cisco-9df2c717db
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_5_1/installation/guide/pcce_b_cisco-pcce-installationandupgrade-guide-12_5/pcce_m_125_scenarios.html
retrieved_at: 2026-08-21T16:38:43.646673+00:00
---

Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.5(1) and 12.5(2)

# Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.5(1) and 12.5(2)

Updated: May 11, 2022

Chapter: Scenarios

## Chapter: Scenarios

- Scenarios

- Installation Scenario

# Scenarios

Cisco Unified Contact Center Enterprise (Unified CCE) is supported only in a virtualized
                        environment.

This Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide provides
                                    the Install and Upgrade details and procedures for both 12.5(1) release and 12.5(2)
                                    maintenance release.

## Installation Scenario

The Unified CCE components are supported on the following platform in 12.5(1) release.

Microsoft Windows Server 2016 and Microsoft SQL Server 2017

The CCE components are supported on the following platforms in 12.5(2) release.

Microsoft Windows Server 2016 and Microsoft SQL Server 2017

Microsoft Windows Server 2019 and Microsoft SQL Server 2019

In a virtualized environment, you can run Unified CCE on a VMware ESXi platform. Run the virtual machines (VMs) on Cisco
                           Unified Computing System (UCS) C-series servers, or equivalent third-party servers.

Install the Unified CCE components after you configure the VMs.

You can use the OVA template to deploy the VMs before beginning with the installation of Unified CCE components.

Deploying VM with Guest Operating System ‘Microsoft Windows Server 2019’ on ESXi 7.0 using CCE OVA template displays a warning
                                       message, “The configured guest OS (Microsoft Windows Server 2016 or later (64-bit)) for this virtual machine does not match
                                       the guest that is currently running (Microsoft Windows Server 2019 (64-bit)). You should specify the correct guest OS to allow
                                       for guest-specific optimization”. This warning message is informational only and has no detrimental effect on the system.
                                       This warning message is displayed only once and can be ignored.

The Unified CCE 12.5(2) installer is available as an add-on release to Unified CCE 12.5(1). Therefore, complete the installation
                           of the base Unified CCE 12.5(1) before applying Unified CCE 12.5(2).

During Unified CCE installation on Windows Server 2019 and SQL Server 2019, SQL Server Security Hardening optional configuration
                                       should not be selected as part of the installation steps. Unified CCE services should be started only after installing Unified
                                       CCE 12.5(2) for Windows Server 2019 and SQL Server 2019 support. The SQL Security Hardening can be applied post installation
                                       using the Security Wizard tool.

Common Ground Upgrade is not supported if the platform upgrade from Windows Server
                                       				2016 and SQL Server 2017 to Windows Server 2019 and SQL Server 2019 is planned as
                                       				part of upgrade process.

Technology Refresh Upgrade is the supported upgrade option for platform upgrade.
                                       				Fresh Install on Windows Server 2019 and SQL Server 2019 is supported. Fresh
                                       				Install, Common Ground Upgrade, and Technology Refresh Upgrade is supported for
                                       				Microsoft Windows Server 2016 and Microsoft SQL Server 2017 platform, where platform
                                       				upgrade is not planned.

| Note | This Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide provides
                                    the Install and Upgrade details and procedures for both 12.5(1) release and 12.5(2)
                                    maintenance release. |
|---|---|

| Note | The cross combination of platforms is not
                                    			supported. For example, Windows Server 2016 with SQL Server 2019 or Windows Server 2019
                                    			with SQL Server 2017. |
|---|---|

| Note | Deploying VM with Guest Operating System ‘Microsoft Windows Server 2019’ on ESXi 7.0 using CCE OVA template displays a warning
                                       message, “The configured guest OS (Microsoft Windows Server 2016 or later (64-bit)) for this virtual machine does not match
                                       the guest that is currently running (Microsoft Windows Server 2019 (64-bit)). You should specify the correct guest OS to allow
                                       for guest-specific optimization”. This warning message is informational only and has no detrimental effect on the system.
                                       This warning message is displayed only once and can be ignored. |
|---|---|

| Note | During Unified CCE installation on Windows Server 2019 and SQL Server 2019, SQL Server Security Hardening optional configuration
                                       should not be selected as part of the installation steps. Unified CCE services should be started only after installing Unified
                                       CCE 12.5(2) for Windows Server 2019 and SQL Server 2019 support. The SQL Security Hardening can be applied post installation
                                       using the Security Wizard tool. Common Ground Upgrade is not supported if the platform upgrade from Windows Server
                                       				2016 and SQL Server 2017 to Windows Server 2019 and SQL Server 2019 is planned as
                                       				part of upgrade process. Technology Refresh Upgrade is the supported upgrade option for platform upgrade.
                                       				Fresh Install on Windows Server 2019 and SQL Server 2019 is supported. Fresh
                                       				Install, Common Ground Upgrade, and Technology Refresh Upgrade is supported for
                                       				Microsoft Windows Server 2016 and Microsoft SQL Server 2017 platform, where platform
                                       				upgrade is not planned. |
|---|---|