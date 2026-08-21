---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-5-installation-guid-e5ba29422b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_5/installation/guide/ccvp_b_install_and_upgrade_12-5/ccvp_b_install_and_upgrade_12-5_chapter_01.html
retrieved_at: 2026-08-21T03:07:14.951910+00:00
---

Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.5(1)

# Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.5(1)

Updated: January 31, 2020

Chapter: Pre-Installation

## Chapter: Pre-Installation

# Pre-Installation

This chapter provides the tasks that you must perform prior to
                        installing the Unified CVP software.

Important

You
                                    must stop any third-party services and applications running on the server prior
                                    to running the Unified CVP Installer. Some third party services and
                                    applications can lock files required by the installer, resulting in an install
                                    error.

Prior to installing the Unified OAMP server, increase the virtual memory of the 12.5(1) CVP OAMP server from 4 GB to 6 GB.
                                    To increase the virtual memory, see Upgrade Virtual Memory .

## Unified CVP
                        	 Components

Unified CVP Server

Unified CVP Call Server

Unified CVP VXML Server

Media
                                                						  Server

SNMP
                                                						  Monitoring service

Operations
                                          					 Console

Remote
                                          					 Operations

Unified CVP Reporting Server

The IBM Informix database is installed as a part of the Reporting Server. The license of IBM Informix comes bundled as a part
                                                      of Reporting Server.

Unified Call Studio

## Requirements

This section describes the platform and software requirements for Cisco Unified Customer Voice Portal (CVP).

Unified CVP Server

Unified Operations Console

Unified Reporting Server

Unified Call Studio

4GB+ RAM

Microsoft Windows 10

Virtualized Platform

Cisco Unified Computing System (UCS) B-Series and C-Series

Access the open virtualization archive (OVA) template at: https://software.cisco.com/download/type.html?mdfid=270563413&flowid=5229 .

For information about hardware requirements and compatibility, see the Unified CCE Solution Compatibility Matrix available at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

### Unified CVP
                           	 Server

Category

Requirements

Operating System

See the Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

To apply the latest Operating System Service Upgrade Release, go to Microsoft upgrade website.

Additional Items

A minimum of 10MB should be available for Unified CVP system media files. Cisco provides .wav files for numbers, days, months,
                                          currency types in American English and Latin American Spanish.

Any additional media files will require additional space.

By default, the Call Server and the VXML Server are on the same physical machine. For more information, see Solution Design Guide for Cisco Unified Contact Center Enterprise , available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html .

On Windows platforms, Call Servers require Simple Network Management Protocol and WMI Windows Installer Provider to be installed.

Restriction

Although supported third-party virus scan software can be enabled on the Call Server, full fixed disk virus scans must take
                                          place either offline while calls have been diverted to a different system or during a period of low call volume. Do not run
                                          a full fixed disk scan while the Call Server is under load.

### Unified CVP
                           	 Operations Console

Category

Requirements

Operating System

See the Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

To apply the latest Operating System Service Upgrade
                                                      						Release, go to the Microsoft upgrade web site.

### [Optional] Unified CVP Reporting Server

Category

Requirements

Operating System

See the Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

To apply the latest Operating System Service Upgrade Release, go to Microsoft upgrade website.

Restriction

Although supported third-party virus scan software can be enabled on the Reporting Server, full fixed disk virus scans must
                                          take place either offline while calls have been diverted to a different system or during a period of low call volume. Do not
                                          run a full fixed disk scan while the Reporting Server is under load.

### [Optional] Unified Call Studio

Category

Requirements

Supported Hardware

4GB+ RAM required

### Configure Secure
                           	 Passwords

To configure a secure password for Reporting Server users (cvp_dbadmin, cvp_dbuser) and the Operations Console Administrator
                              user, your password must comply with the following rules:

The password must contain characters only from the ASCII character set:

Uppercase and lowercase letters of the English alphabets

Numeric characters [0-9]

Special characters from this set: !#$&()*+./<?@[\]^_`{}~

The password length must be 12 characters or more.

The password must meet the following password complexity:

The password must use three of four of the following four types of characters:

At least one uppercase letter [A-Z]

At least one lowercase letter [a-z]

At least one numeric character [0-9]

At least one special character from this set: !#$&()*+./<?@[\]^_`{}~

The characters in the password must not be repeated more than three times consecutively.

The password must not be "cisco", "ocsic", or any variant obtained by changing the capitalization of letters therein.

## Additional
                        	 Components

You can use the following components that are not part of the Unified CVP software but may be used with Unified CVP for a
                              complete contact center solution.

Automatic
                                    				Speech Recognition (ASR) Server/ Text-to-speech (TTS) Server

Cisco Unified
                                    				Contact Center Enterprise

Cisco Unified
                                    				Communications Manager

Cisco Unified
                                    				SIP Proxy

Ingress
                                    				Gateway

Egress Gateway

Voice XML Gateway

Cisco Unified
                                    				Border Element (CUBE)

Cisco Unified Intelligence Center (CUIC)

Cisco Virtualized Voice Browser

## Unified CVP Installation Modes

Production

In production mode, you can install only one Unified CVP component on a virtual machine server at a time. If you need to install
                                          additional components, you must install these components on a different virtual machine server.

Lab only

Use this mode to install Unified CVP for learning and testing.

To use lab only mode, launch the installer from the command line, browse to the setup.exe folder, and enter setup.exe labonly .

In lab only mode, the Call Server, OAMP Server, and Reporting Server can be installed together but you cannot selectively
                                                      uninstall one of them. For example, if you want to remove the Reporting Server you must reinstall Unified CVP.

## Pre-Installation
                        	 Tasks

### Install Microsoft
                           	 Windows Server

Complete the following procedure to install Microsoft Windows Server 2016 on all virtual machines for server-based applications.

#### Before you begin

Ensure that VMware Tools software is installed. You cannot install VMXNET3 driver without VMware Tools.

Ensure that ESXi version of the host is ESXi 6.5 with VMFS 5, ESXi 6.5 U2 and later updates with VMFS 6, or ESXi 6.7 with
                                       VMFS 6.

Ensure that the length of the host name for CVP server is not more than 15 characters.

Ensure that you have deployed the OVA template for the respective CVP components.

Step 1

Mount Microsoft Windows Server 2016 ISO image to the virtual machine.

Step 2

Power on the virtual machine.

Step 3

Enter the Language, Time and Currency Format, and Keyboard settings. Click Next .

Step 4

Click Install Now .

Step 5

Select the appropriate version of the windows server with Desktop Experience option that meets your organization’s needs,
                                          and then click Next . Make sure that you have chosen an appropriate edition of Windows server with Desktop Experience.

Step 6

Accept the license terms and click Next .

Step 7

Select the Custom: Install Windows only (advanced) option for clean installation.

Step 8

Select the hard drive that you want to install the windows server on, and then click on the New button to do the partitions.

Step 9

Specify the amount of the drive based on MB and then click on the Apply button. A warning appears to give the permission to system to create a drive for system files.

Click Cancel . It is recommended not to change the size of the drive.

The installation begins. After the installation is complete, the system restarts without prompting.

Step 10

Enter and confirm the password for the administrator account, and then click Finish .

### Fresh
                           	 Installation

#### Fresh
                              	 Install

Step 1

Obtain the
                                             			 Unified CVP ISO image to install Unified CVP.

Step 2

Obtain the supported virtualization hardware and software that are required for the virtualization of Unified CVP.

Step 3

Identify the components for the required deployment model. For information about hardware requirements compatibility, see
                                             the Unified CCE Solution Compatibility Matrix available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

Step 4

Ensure that
                                             			 the servers are listed as supported hardware and sized appropriately.

Step 5

Verify that
                                             			 the any new server hardware, such as hard drive, is working properly.

Step 6

Stop any third-party services and applications that are running on the server before you run the Unified CVP Installer. Some
                                             third-party services and applications can lock files that are required by the installer resulting in an installation error.

#### Verification of the Downloaded ISO

Perform the following procedure to validate the downloaded ISO  signed by
                                    Cisco, to ensure that it is authorized.

Step 1

Install OpenSSL on Microsoft Windows.

Step 2

Add the OpenSSL installation path to System variables in the Environment Variables of the system.

Step 3

Add the downloaded ISO Image , ISO Image signature file  and the Public key.der file in the same folder for the specific
                                             product component.

Step 4

Launch Command Prompt on the system.

Step 5

Run the following CLI (Command Line Interface) command to verify the files:

openssl dgst -sha512 -keyform der -verify <PUBLIC key.der>
                                                   -signature <ISO Image.iso.signature <ISO Image

If the verification fails do not proceed with the installation, contact Cisco Support for a valid ISO .

### Multiple Ethernet Interfaces

The machine that you are using for the Unified CVP Call Server must have only one Ethernet interface enabled. When installing
                                 Unified CVP on a machine with two or more Ethernet interfaces, the additional interface(s) must be disabled, even if they
                                 are not configured. Refer to Windows documentation for information on enabling/disabling an Ethernet interface.

| Important | You
                                    must stop any third-party services and applications running on the server prior
                                    to running the Unified CVP Installer. Some third party services and
                                    applications can lock files required by the installer, resulting in an install
                                    error. |
|---|---|

| Note | Prior to installing the Unified OAMP server, increase the virtual memory of the 12.5(1) CVP OAMP server from 4 GB to 6 GB.
                                    To increase the virtual memory, see Upgrade Virtual Memory . |
|---|---|

| Unified CVP Component | Description |
|---|---|
| Unified CVP Server | This server consists of: Unified CVP Call Server Unified CVP VXML Server Media
                                                						  Server SNMP
                                                						  Monitoring service |
| Operations
                                          					 Console | The Operations Console (OAMP and NOAMP) is a web-based interface that enables you to configure and manage individual components of Unified CVP. |
| Remote
                                          					 Operations | This component allows
                                       				  remote administration of Unified CVP solution components. It includes
                                       				  Operations and Resource Module (ORM). |
| Unified CVP Reporting Server | This server provides a historical repository, which can be used for reporting, for a call center. It receives reporting data
                                       from one or more Unified CVP Call Servers and Unified CVP VXML Servers, and stores that data in a database. Note The IBM Informix database is installed as a part of the Reporting Server. The license of IBM Informix comes bundled as a part
                                                      of Reporting Server. | Note | The IBM Informix database is installed as a part of the Reporting Server. The license of IBM Informix comes bundled as a part
                                                      of Reporting Server. |
| Note | The IBM Informix database is installed as a part of the Reporting Server. The license of IBM Informix comes bundled as a part
                                                      of Reporting Server. |
| Unified Call Studio | This component provides design and syntax for developing call flow for VXML-based execution. Unified Call Studio also supports
                                       debugger for application. This helps validate Unified Call Studio application. |

| Note | The IBM Informix database is installed as a part of the Reporting Server. The license of IBM Informix comes bundled as a part
                                                      of Reporting Server. |
|---|---|

| Unified CVP Component/Task | Platform Requirement |
|---|---|
| Unified CVP Server | Note Refer to the Cisco Collaboration Virtualization page at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html . | Note | Refer to the Cisco Collaboration Virtualization page at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html . |
| Note | Refer to the Cisco Collaboration Virtualization page at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html . |
| Unified Operations Console |
| Unified Reporting Server |
| Unified Call Studio | 4GB+ RAM Microsoft Windows 10 |
| Virtualized Platform | Cisco Unified Computing System (UCS) B-Series and C-Series Note Access the open virtualization archive (OVA) template at: https://software.cisco.com/download/type.html?mdfid=270563413&flowid=5229 . | Note | Access the open virtualization archive (OVA) template at: https://software.cisco.com/download/type.html?mdfid=270563413&flowid=5229 . |
| Note | Access the open virtualization archive (OVA) template at: https://software.cisco.com/download/type.html?mdfid=270563413&flowid=5229 . |

| Note | Refer to the Cisco Collaboration Virtualization page at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html . |
|---|---|

| Note | Access the open virtualization archive (OVA) template at: https://software.cisco.com/download/type.html?mdfid=270563413&flowid=5229 . |
|---|---|

| Category | Requirements |
|---|---|
| Operating System | See the Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html . Note To apply the latest Operating System Service Upgrade Release, go to Microsoft upgrade website. | Note | To apply the latest Operating System Service Upgrade Release, go to Microsoft upgrade website. |
| Note | To apply the latest Operating System Service Upgrade Release, go to Microsoft upgrade website. |
| Additional Items | A minimum of 10MB should be available for Unified CVP system media files. Cisco provides .wav files for numbers, days, months,
                                          currency types in American English and Latin American Spanish. Note Any additional media files will require additional space. By default, the Call Server and the VXML Server are on the same physical machine. For more information, see Solution Design Guide for Cisco Unified Contact Center Enterprise , available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html . On Windows platforms, Call Servers require Simple Network Management Protocol and WMI Windows Installer Provider to be installed. | Note | Any additional media files will require additional space. |
| Note | Any additional media files will require additional space. |
| Restriction | Although supported third-party virus scan software can be enabled on the Call Server, full fixed disk virus scans must take
                                          place either offline while calls have been diverted to a different system or during a period of low call volume. Do not run
                                          a full fixed disk scan while the Call Server is under load. |

| Note | To apply the latest Operating System Service Upgrade Release, go to Microsoft upgrade website. |
|---|---|

| Note | Any additional media files will require additional space. |
|---|---|

| Category | Requirements |
|---|---|
| Operating System | See the Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html . Note To apply the latest Operating System Service Upgrade
                                                      						Release, go to the Microsoft upgrade web site. | Note | To apply the latest Operating System Service Upgrade
                                                      						Release, go to the Microsoft upgrade web site. |
| Note | To apply the latest Operating System Service Upgrade
                                                      						Release, go to the Microsoft upgrade web site. |

| Note | To apply the latest Operating System Service Upgrade
                                                      						Release, go to the Microsoft upgrade web site. |
|---|---|

| Category | Requirements |
|---|---|
| Operating System | See the Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html . Note To apply the latest Operating System Service Upgrade Release, go to Microsoft upgrade website. | Note | To apply the latest Operating System Service Upgrade Release, go to Microsoft upgrade website. |
| Note | To apply the latest Operating System Service Upgrade Release, go to Microsoft upgrade website. |
| Restriction | Although supported third-party virus scan software can be enabled on the Reporting Server, full fixed disk virus scans must
                                          take place either offline while calls have been diverted to a different system or during a period of low call volume. Do not
                                          run a full fixed disk scan while the Reporting Server is under load. |

| Note | To apply the latest Operating System Service Upgrade Release, go to Microsoft upgrade website. |
|---|---|

| Category | Requirements |
|---|---|
| Supported Hardware | 4GB+ RAM required |

| Installation Mode | Description |
|---|---|
| Production | In production mode, you can install only one Unified CVP component on a virtual machine server at a time. If you need to install
                                          additional components, you must install these components on a different virtual machine server. |
| Lab only | Use this mode to install Unified CVP for learning and testing. To use lab only mode, launch the installer from the command line, browse to the setup.exe folder, and enter setup.exe labonly . Note In lab only mode, the Call Server, OAMP Server, and Reporting Server can be installed together but you cannot selectively
                                                      uninstall one of them. For example, if you want to remove the Reporting Server you must reinstall Unified CVP. | Note | In lab only mode, the Call Server, OAMP Server, and Reporting Server can be installed together but you cannot selectively
                                                      uninstall one of them. For example, if you want to remove the Reporting Server you must reinstall Unified CVP. |
| Note | In lab only mode, the Call Server, OAMP Server, and Reporting Server can be installed together but you cannot selectively
                                                      uninstall one of them. For example, if you want to remove the Reporting Server you must reinstall Unified CVP. |

| Note | In lab only mode, the Call Server, OAMP Server, and Reporting Server can be installed together but you cannot selectively
                                                      uninstall one of them. For example, if you want to remove the Reporting Server you must reinstall Unified CVP. |
|---|---|

| Step 1 | Mount Microsoft Windows Server 2016 ISO image to the virtual machine. |
|---|---|
| Step 2 | Power on the virtual machine. |
| Step 3 | Enter the Language, Time and Currency Format, and Keyboard settings. Click Next . |
| Step 4 | Click Install Now . |
| Step 5 | Select the appropriate version of the windows server with Desktop Experience option that meets your organization’s needs,
                                          and then click Next . Make sure that you have chosen an appropriate edition of Windows server with Desktop Experience. |
| Step 6 | Accept the license terms and click Next . |
| Step 7 | Select the Custom: Install Windows only (advanced) option for clean installation. |
| Step 8 | Select the hard drive that you want to install the windows server on, and then click on the New button to do the partitions. |
| Step 9 | Specify the amount of the drive based on MB and then click on the Apply button. A warning appears to give the permission to system to create a drive for system files. Click Cancel . It is recommended not to change the size of the drive. The installation begins. After the installation is complete, the system restarts without prompting. |
| Step 10 | Enter and confirm the password for the administrator account, and then click Finish . |

| Step 1 | Obtain the
                                             			 Unified CVP ISO image to install Unified CVP. |
|---|---|
| Step 2 | Obtain the supported virtualization hardware and software that are required for the virtualization of Unified CVP. |
| Step 3 | Identify the components for the required deployment model. For information about hardware requirements compatibility, see
                                             the Unified CCE Solution Compatibility Matrix available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html . |
| Step 4 | Ensure that
                                             			 the servers are listed as supported hardware and sized appropriately. |
| Step 5 | Verify that
                                             			 the any new server hardware, such as hard drive, is working properly. |
| Step 6 | Stop any third-party services and applications that are running on the server before you run the Unified CVP Installer. Some
                                             third-party services and applications can lock files that are required by the installer resulting in an installation error. |

| Step 1 | Install OpenSSL on Microsoft Windows. |
|---|---|
| Step 2 | Add the OpenSSL installation path to System variables in the Environment Variables of the system. |
| Step 3 | Add the downloaded ISO Image , ISO Image signature file  and the Public key.der file in the same folder for the specific
                                             product component. |
| Step 4 | Launch Command Prompt on the system. |
| Step 5 | Run the following CLI (Command Line Interface) command to verify the files: openssl dgst -sha512 -keyform der -verify <PUBLIC key.der>
                                                   -signature <ISO Image.iso.signature <ISO Image The system displays Verified OK on successful verification and Verification failed on verification failure. Note If the verification fails do not proceed with the installation, contact Cisco Support for a valid ISO . | Note | If the verification fails do not proceed with the installation, contact Cisco Support for a valid ISO . |
| Note | If the verification fails do not proceed with the installation, contact Cisco Support for a valid ISO . |

| Note | If the verification fails do not proceed with the installation, contact Cisco Support for a valid ISO . |
|---|---|