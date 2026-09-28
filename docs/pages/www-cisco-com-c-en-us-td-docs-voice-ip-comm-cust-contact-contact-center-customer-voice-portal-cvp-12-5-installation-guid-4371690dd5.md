---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-5-installation-guid-4371690dd5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_5/installation/guide/ccvp_b_install_and_upgrade_12-5/ccvp_b_install_and_upgrade_12-5_chapter_010.html
retrieved_at: 2026-08-21T03:07:19.162917+00:00
---

Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.5(1)

# Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.5(1)

Updated: January 31, 2020

Chapter: Unified CVP
	 Installation

## Chapter: Unified CVP
	 Installation

# Unified CVP
                     	 Installation

Cisco Unified Customer Voice Portal (CVP) ISO image contains the setup files for all the CVP components in the CVP folder.

Only a local administrator must install the Unified CVP software.

Before you install Unified CVP, refer to the licensing information in the Unified CVP Licensing chapter.

Ensure that the server chosen for Reporting Server is part of a workgroup.

Important

A new 12.5(1b) base installer is available for customers, which has OpenJDK JRE as the supporting Java runtime for the Unified CVP application.
                                    It is the same as the preceding 12.5(1) installer, except that in the 12.5(1b) base installer, the Java runtime environment
                                    is installed on the Unified CVP virtual machines (VMs).

You can continue to use Oracle JRE if you have installed CVP 12.5(1). Further, you can download and install the Java security
                                    updates from the Oracle website.

For JRE update post installation of 12.5(1b), refer to the OpenLogic OpenJDK site to download the JREs.

Customers who are not installing 12.5(1b) and staying on 12.5(1) release can install the CVP ES to migrate from Oracle JRE
                                    to OpenJDK JRE. All subsequent ESs would be supported on top of this ES.

Upon installation of ES 33, the JRE in the CVP is updated with OpenLogic JRE. Any specific changes in configuration files
                                    of the JRE folder should be backed up and reconfigured after the JRE update.

Important

In the new Unified CVP 12.5(1b) release, CVP Reporting Server has support for IBM Informix version 14.10 FC8.

For migrating the Reporting Server from 12.5(1) to 12.5(1b), see Migrate Unified CVP Reporting Server .

If you are testing with the self-signed TLS certificates that are generated as a part of the installation, ensure that you
                                    map the CN/SANs on the certificate to the corresponding IP through DNS or host file entries.

## Install Unified
                        	 CVP on Virtual Machines

### Before you begin

Disable large receive offload (LRO) for ESXi for virtualization
                                       				platform for Unified CVP.

Install and configure the Unified Computing System (UCS).

Install and boot VMware ESXi.

Ensure that ESXi is configured and reachable over the network.

Download the OVA template.

Step 1

Create the Unified CVP virtual machines using the OVA template.

Step 2

Select the CVP components, as required.

Step 3

Install Windows Server.

Step 4

Install the selected CVP components.

## Install Unified CVP Server

Fresh installation of Unified CVP includes the following voice prompt encode format types—u-law, A-law, and G729 for media
                              files. Default applications also get installed along with media files. Choose the format type as per requirement.

Step 1

Mount Unified CVP ISO, and run setup.exe.

Step 2

Review and
                                       			 accept the license agreement, and click Next .

Step 3

On the Select Package screen, choose the Unified CVP component to install on your computer, and click Next .

Internet Information Server (IIS) is the default Media Server supported by Unified CVP. For details on IIS configuration,
                                                      see the Microsoft documentation.

Step 4

At the Voice
                                          				Prompt Encode Format Type screen, select one of the following
                                       			 options:

U-Law Encoded Wave
                                                   						Format

A-Law Encoded Wave
                                                   						Format

G729 Encoded Wave Format

Step 5

On the Choose Destination Location screen, select the folder where setup will install files. By default, it is C:\Cisco\CVP .

Step 6

On the X.509
                                          				Certificate screen, enter the required information in the form, and
                                       			 click Next .

In Common Name field, enter FQDN.

Step 7

Click Install .

You cannot
                                                      				  cancel the installation when it is in progress.

Step 8

Choose to restart the computer right after the upgrade or to restart it later, and click Finish .

After successful installation, the CVP Call Server Service Startup Type is set to Automatic by default.

### What to do next

Install Operations Console

## Install Operations
                        	 Console

Step 1

Perform Steps 1 to 6 of the Install CVP Server procedure.

Step 2

From the Ready
                                          				to Install the Program screen, review the component that you
                                       			 selected, and click Install .

Step 3

On the Ops
                                          				Console Password screen, in the Password and Password (for
                                          				verification) fields, enter a password and re-enter it for
                                       			 confirmation, and click Next .

Adhere to
                                                      				  the password formation criteria that are listed on the Operations Console
                                                      				  Password screen section.

Operations
                                                      				  Console Administrator and Web Services Administrator (wsmadmin) use the
                                                      				  Operations Console password.

Step 4

Select one of
                                       			 the options to either restart the computer right after installation or later,
                                       			 and click Finish .

### What to do next

Install Remote Operations

## Install Remote
                        	 Operations

Step 1

Perform Steps 1 to 4 of the Install Operations Console procedure.

Step 2

Choose to restart the computer right after the upgrade or to restart it later, and click Finish .

### What to do next

Install Reporting Server

## Install Second Drive on Reporting Server Virtual Machine

Step 1

Right-click My Computer > Manage .

Step 2

In Storage section, click Disk Management .

Step 3

Select the unformatted partition, which is usually Disk 1 .

Step 4

Right-click Online , and initialize the disk.

Step 5

Click Format , and follow the formatting process with NTFS.

## Install Unified CVP Reporting Server

IBM Informix database server 14.10 FC1 is installed as part of the Unified CVP Reporting Server.

The ImagePath for CVP Reporting Informix IDS Service in Windows registry is set to c:\db\Informix\bin\onscpah cvp . Because of this, when security scanners are run, the ImagePath changes to "c:\db\Informix\bin\onscpah cvp" . This results in the CVP Reporting Informix IDS Service not starting.

Workaround : Set ImagePath for CVP Reporting Informix IDS Service in Windows registry to "c:\db\Informix\bin\onscpah" cvp .

### Before you begin

Only the actual Local Administrator (should not be renamed) of this system can install CVP Reporting Server.

Ensure that Unified CVP Reporting Server is not part of any domain and is part of a work group.

Do not create Informix user in the Local Users and Group, this will impact the installation. Once installation is completed,
                                    Informix user can be created for the database operation.

Step 1

Mount the Unified CVP ISO image, and run setup.exe file.

Step 2

Review and accept the license agreement, and click Next .

Step 3

On the Select Package screen, select Reporting Server , and click Next .

Step 4

Select the root drive on which you want the Reporting database data and backup data to reside, and click Next .

The Database Size Selection screen appears, providing the following options:

Standard: Requires a minimum of 250GB of free disk space.

Premium: Requires a minimum of 375GB of free disk space.

Step 5

Choose the appropriate database size for the license that you purchased, and click Next .

Step 6

From the Ready to Install the Program window, review the component that you have selected, and click Install .

Step 7

On the Reporting Password window, enter a password and re-enter it for confirmation, and click Next .

Adhere to the password formation criteria that are listed on the Operations Console Password screen section.

The Reporting password requires that the Minimum Password Age parameter be set to 0 days for both the local and/or domain security policy and is subject to both the Unified CVP password
                                                            policy and the password policy enforced by the operating system of the computer on which the Reporting Server resides. For
                                                            each aspect of the password, the Reporting password must meet the requirement of the more restrictive policy. If you are installing
                                                            CVP Reporting Server please ensure that your local and/or domain security policy for MINIMUM PASSWORD AGE are set to 0 days
                                                            for the installation of the CVP Reporting Server component (In Windows, Control Panel > Administrative Tools > Local Security Policy > Account Policy > Password Policy ). If the reporting password you enter is rejected, review the list of password requirements displayed by the installer and
                                                            consider your operating system's password requirements. You can reconfigure this password repeatedly until an acceptable password
                                                            is found.

After installation, add the Unified CVP Reporting Server to the domain, if necessary.

Step 8

Choose to restart the computer right after installation or to restart it later, and click Finish .

## Install Unified
                        	 Call Studio

Important

A new 12.5(1b) base installer is available for customers, which has OpenJDK JRE as the supporting Java runtime for the Unified CVP application.
                                          It is the same as the preceding 12.5(1) installer, except that in the 12.5(1b) base installer, the Java runtime environment
                                          is installed on the Unified CVP virtual machines (VMs).

Step 1

Mount the Unified CVP software (including CVP Studio) installer ISO image (under the Installer_Windows folder), and run setup.exe .

Step 2

On the Welcome screen, click Next .

If you click Cancel here or on the dialog screens that follow before the Ready to Install the Program screen, the installation is canceled. The Exit Setup dialog box appears.

Step 3

Review Copyrights to Products used by Call Studio and click Next .

Step 4

Review and accept the license agreement, and click Next .

Step 5

On the Choose Destination Location screen, select the folder where setup will install files. By default, it is C:\Cisco\CallStudio .

Step 6

On the InstallShield Wizard Complete screen, click Install .

Step 7

Click Finish to exit the wizard.

The Call Studio software is installed on your computer.

The SolarWinds TFTP software and AnyConnect (while a VPN connection is enabled) are the known causes for the Call Studio debugger
                                          errors. To resolve the Call Studio debugger errors:

If you are using SolarWinds, stop the SolarWinds TFTP software and run the debugger.

If you are using AnyConnect, disconnect the VPN connection and run the debugger.

| Note | Before you install Unified CVP, refer to the licensing information in the Unified CVP Licensing chapter. Ensure that the server chosen for Reporting Server is part of a workgroup. |
|---|---|

| Important | A new 12.5(1b) base installer is available for customers, which has OpenJDK JRE as the supporting Java runtime for the Unified CVP application.
                                    It is the same as the preceding 12.5(1) installer, except that in the 12.5(1b) base installer, the Java runtime environment
                                    is installed on the Unified CVP virtual machines (VMs). You can continue to use Oracle JRE if you have installed CVP 12.5(1). Further, you can download and install the Java security
                                    updates from the Oracle website. For JRE update post installation of 12.5(1b), refer to the OpenLogic OpenJDK site to download the JREs. Customers who are not installing 12.5(1b) and staying on 12.5(1) release can install the CVP ES to migrate from Oracle JRE
                                    to OpenJDK JRE. All subsequent ESs would be supported on top of this ES. |
|---|---|

| Note | Upon installation of ES 33, the JRE in the CVP is updated with OpenLogic JRE. Any specific changes in configuration files
                                    of the JRE folder should be backed up and reconfigured after the JRE update. |
|---|---|

| Important | In the new Unified CVP 12.5(1b) release, CVP Reporting Server has support for IBM Informix version 14.10 FC8. For migrating the Reporting Server from 12.5(1) to 12.5(1b), see Migrate Unified CVP Reporting Server . |
|---|---|

| Note | If you are testing with the self-signed TLS certificates that are generated as a part of the installation, ensure that you
                                    map the CN/SANs on the certificate to the corresponding IP through DNS or host file entries. |
|---|---|

| Step 1 | Create the Unified CVP virtual machines using the OVA template. |
|---|---|
| Step 2 | Select the CVP components, as required. |
| Step 3 | Install Windows Server. |
| Step 4 | Install the selected CVP components. |

| Step 1 | Mount Unified CVP ISO, and run setup.exe. |
|---|---|
| Step 2 | Review and
                                       			 accept the license agreement, and click Next . |
| Step 3 | On the Select Package screen, choose the Unified CVP component to install on your computer, and click Next . Note Internet Information Server (IIS) is the default Media Server supported by Unified CVP. For details on IIS configuration,
                                                      see the Microsoft documentation. | Note | Internet Information Server (IIS) is the default Media Server supported by Unified CVP. For details on IIS configuration,
                                                      see the Microsoft documentation. |
| Note | Internet Information Server (IIS) is the default Media Server supported by Unified CVP. For details on IIS configuration,
                                                      see the Microsoft documentation. |
| Step 4 | At the Voice
                                          				Prompt Encode Format Type screen, select one of the following
                                       			 options: U-Law Encoded Wave
                                                   						Format A-Law Encoded Wave
                                                   						Format G729 Encoded Wave Format |
| Step 5 | On the Choose Destination Location screen, select the folder where setup will install files. By default, it is C:\Cisco\CVP . |
| Step 6 | On the X.509
                                          				Certificate screen, enter the required information in the form, and
                                       			 click Next . Note In Common Name field, enter FQDN. | Note | In Common Name field, enter FQDN. |
| Note | In Common Name field, enter FQDN. |
| Step 7 | Click Install . Note You cannot
                                                      				  cancel the installation when it is in progress. | Note | You cannot
                                                      				  cancel the installation when it is in progress. |
| Note | You cannot
                                                      				  cancel the installation when it is in progress. |
| Step 8 | Choose to restart the computer right after the upgrade or to restart it later, and click Finish . Note After successful installation, the CVP Call Server Service Startup Type is set to Automatic by default. | Note | After successful installation, the CVP Call Server Service Startup Type is set to Automatic by default. |
| Note | After successful installation, the CVP Call Server Service Startup Type is set to Automatic by default. |

| Note | Internet Information Server (IIS) is the default Media Server supported by Unified CVP. For details on IIS configuration,
                                                      see the Microsoft documentation. |
|---|---|

| Note | In Common Name field, enter FQDN. |
|---|---|

| Note | You cannot
                                                      				  cancel the installation when it is in progress. |
|---|---|

| Note | After successful installation, the CVP Call Server Service Startup Type is set to Automatic by default. |
|---|---|

| Step 1 | Perform Steps 1 to 6 of the Install CVP Server procedure. |
|---|---|
| Step 2 | From the Ready
                                          				to Install the Program screen, review the component that you
                                       			 selected, and click Install . |
| Step 3 | On the Ops
                                          				Console Password screen, in the Password and Password (for
                                          				verification) fields, enter a password and re-enter it for
                                       			 confirmation, and click Next . Note Adhere to
                                                      				  the password formation criteria that are listed on the Operations Console
                                                      				  Password screen section. Note Operations
                                                      				  Console Administrator and Web Services Administrator (wsmadmin) use the
                                                      				  Operations Console password. | Note | Adhere to
                                                      				  the password formation criteria that are listed on the Operations Console
                                                      				  Password screen section. | Note | Operations
                                                      				  Console Administrator and Web Services Administrator (wsmadmin) use the
                                                      				  Operations Console password. |
| Note | Adhere to
                                                      				  the password formation criteria that are listed on the Operations Console
                                                      				  Password screen section. |
| Note | Operations
                                                      				  Console Administrator and Web Services Administrator (wsmadmin) use the
                                                      				  Operations Console password. |
| Step 4 | Select one of
                                       			 the options to either restart the computer right after installation or later,
                                       			 and click Finish . |

| Note | Adhere to
                                                      				  the password formation criteria that are listed on the Operations Console
                                                      				  Password screen section. |
|---|---|

| Note | Operations
                                                      				  Console Administrator and Web Services Administrator (wsmadmin) use the
                                                      				  Operations Console password. |
|---|---|

| Step 1 | Perform Steps 1 to 4 of the Install Operations Console procedure. |
|---|---|
| Step 2 | Choose to restart the computer right after the upgrade or to restart it later, and click Finish . |

| Step 1 | Right-click My Computer > Manage . |
|---|---|
| Step 2 | In Storage section, click Disk Management . |
| Step 3 | Select the unformatted partition, which is usually Disk 1 . |
| Step 4 | Right-click Online , and initialize the disk. |
| Step 5 | Click Format , and follow the formatting process with NTFS. |

| Note | The ImagePath for CVP Reporting Informix IDS Service in Windows registry is set to c:\db\Informix\bin\onscpah cvp . Because of this, when security scanners are run, the ImagePath changes to "c:\db\Informix\bin\onscpah cvp" . This results in the CVP Reporting Informix IDS Service not starting. Workaround : Set ImagePath for CVP Reporting Informix IDS Service in Windows registry to "c:\db\Informix\bin\onscpah" cvp . |
|---|---|

| Step 1 | Mount the Unified CVP ISO image, and run setup.exe file. |
|---|---|
| Step 2 | Review and accept the license agreement, and click Next . |
| Step 3 | On the Select Package screen, select Reporting Server , and click Next . Note This step takes approximately 30 seconds before moving to the Choose Destination Location window. | Note | This step takes approximately 30 seconds before moving to the Choose Destination Location window. |
| Note | This step takes approximately 30 seconds before moving to the Choose Destination Location window. |
| Step 4 | Select the root drive on which you want the Reporting database data and backup data to reside, and click Next . Note Choose the E drive or the second drive, whose size is more than 400GB, to store the Reporting database data and to keep the
                                                   backup of data. The Database Size Selection screen appears, providing the following options: Standard: Requires a minimum of 250GB of free disk space. Premium: Requires a minimum of 375GB of free disk space. | Note | Choose the E drive or the second drive, whose size is more than 400GB, to store the Reporting database data and to keep the
                                                   backup of data. |
| Note | Choose the E drive or the second drive, whose size is more than 400GB, to store the Reporting database data and to keep the
                                                   backup of data. |
| Step 5 | Choose the appropriate database size for the license that you purchased, and click Next . |
| Step 6 | From the Ready to Install the Program window, review the component that you have selected, and click Install . |
| Step 7 | On the Reporting Password window, enter a password and re-enter it for confirmation, and click Next . Note Adhere to the password formation criteria that are listed on the Operations Console Password screen section. The Reporting password requires that the Minimum Password Age parameter be set to 0 days for both the local and/or domain security policy and is subject to both the Unified CVP password
                                                            policy and the password policy enforced by the operating system of the computer on which the Reporting Server resides. For
                                                            each aspect of the password, the Reporting password must meet the requirement of the more restrictive policy. If you are installing
                                                            CVP Reporting Server please ensure that your local and/or domain security policy for MINIMUM PASSWORD AGE are set to 0 days
                                                            for the installation of the CVP Reporting Server component (In Windows, Control Panel > Administrative Tools > Local Security Policy > Account Policy > Password Policy ). If the reporting password you enter is rejected, review the list of password requirements displayed by the installer and
                                                            consider your operating system's password requirements. You can reconfigure this password repeatedly until an acceptable password
                                                            is found. After installation, add the Unified CVP Reporting Server to the domain, if necessary. | Note | Adhere to the password formation criteria that are listed on the Operations Console Password screen section. The Reporting password requires that the Minimum Password Age parameter be set to 0 days for both the local and/or domain security policy and is subject to both the Unified CVP password
                                                            policy and the password policy enforced by the operating system of the computer on which the Reporting Server resides. For
                                                            each aspect of the password, the Reporting password must meet the requirement of the more restrictive policy. If you are installing
                                                            CVP Reporting Server please ensure that your local and/or domain security policy for MINIMUM PASSWORD AGE are set to 0 days
                                                            for the installation of the CVP Reporting Server component (In Windows, Control Panel > Administrative Tools > Local Security Policy > Account Policy > Password Policy ). If the reporting password you enter is rejected, review the list of password requirements displayed by the installer and
                                                            consider your operating system's password requirements. You can reconfigure this password repeatedly until an acceptable password
                                                            is found. After installation, add the Unified CVP Reporting Server to the domain, if necessary. |
| Note | Adhere to the password formation criteria that are listed on the Operations Console Password screen section. The Reporting password requires that the Minimum Password Age parameter be set to 0 days for both the local and/or domain security policy and is subject to both the Unified CVP password
                                                            policy and the password policy enforced by the operating system of the computer on which the Reporting Server resides. For
                                                            each aspect of the password, the Reporting password must meet the requirement of the more restrictive policy. If you are installing
                                                            CVP Reporting Server please ensure that your local and/or domain security policy for MINIMUM PASSWORD AGE are set to 0 days
                                                            for the installation of the CVP Reporting Server component (In Windows, Control Panel > Administrative Tools > Local Security Policy > Account Policy > Password Policy ). If the reporting password you enter is rejected, review the list of password requirements displayed by the installer and
                                                            consider your operating system's password requirements. You can reconfigure this password repeatedly until an acceptable password
                                                            is found. After installation, add the Unified CVP Reporting Server to the domain, if necessary. |
| Step 8 | Choose to restart the computer right after installation or to restart it later, and click Finish . |

| Note | This step takes approximately 30 seconds before moving to the Choose Destination Location window. |
|---|---|

| Note | Choose the E drive or the second drive, whose size is more than 400GB, to store the Reporting database data and to keep the
                                                   backup of data. |
|---|---|

| Note | Adhere to the password formation criteria that are listed on the Operations Console Password screen section. The Reporting password requires that the Minimum Password Age parameter be set to 0 days for both the local and/or domain security policy and is subject to both the Unified CVP password
                                                            policy and the password policy enforced by the operating system of the computer on which the Reporting Server resides. For
                                                            each aspect of the password, the Reporting password must meet the requirement of the more restrictive policy. If you are installing
                                                            CVP Reporting Server please ensure that your local and/or domain security policy for MINIMUM PASSWORD AGE are set to 0 days
                                                            for the installation of the CVP Reporting Server component (In Windows, Control Panel > Administrative Tools > Local Security Policy > Account Policy > Password Policy ). If the reporting password you enter is rejected, review the list of password requirements displayed by the installer and
                                                            consider your operating system's password requirements. You can reconfigure this password repeatedly until an acceptable password
                                                            is found. After installation, add the Unified CVP Reporting Server to the domain, if necessary. |
|---|---|

| Important | A new 12.5(1b) base installer is available for customers, which has OpenJDK JRE as the supporting Java runtime for the Unified CVP application.
                                          It is the same as the preceding 12.5(1) installer, except that in the 12.5(1b) base installer, the Java runtime environment
                                          is installed on the Unified CVP virtual machines (VMs). |
|---|---|

| Step 1 | Mount the Unified CVP software (including CVP Studio) installer ISO image (under the Installer_Windows folder), and run setup.exe . |
|---|---|
| Step 2 | On the Welcome screen, click Next . Note If you click Cancel here or on the dialog screens that follow before the Ready to Install the Program screen, the installation is canceled. The Exit Setup dialog box appears. | Note | If you click Cancel here or on the dialog screens that follow before the Ready to Install the Program screen, the installation is canceled. The Exit Setup dialog box appears. |
| Note | If you click Cancel here or on the dialog screens that follow before the Ready to Install the Program screen, the installation is canceled. The Exit Setup dialog box appears. |
| Step 3 | Review Copyrights to Products used by Call Studio and click Next . |
| Step 4 | Review and accept the license agreement, and click Next . |
| Step 5 | On the Choose Destination Location screen, select the folder where setup will install files. By default, it is C:\Cisco\CallStudio . |
| Step 6 | On the InstallShield Wizard Complete screen, click Install . |
| Step 7 | Click Finish to exit the wizard. |

| Note | If you click Cancel here or on the dialog screens that follow before the Ready to Install the Program screen, the installation is canceled. The Exit Setup dialog box appears. |
|---|---|

| Note | The SolarWinds TFTP software and AnyConnect (while a VPN connection is enabled) are the known causes for the Call Studio debugger
                                          errors. To resolve the Call Studio debugger errors: If you are using SolarWinds, stop the SolarWinds TFTP software and run the debugger. If you are using AnyConnect, disconnect the VPN connection and run the debugger. |
|---|---|