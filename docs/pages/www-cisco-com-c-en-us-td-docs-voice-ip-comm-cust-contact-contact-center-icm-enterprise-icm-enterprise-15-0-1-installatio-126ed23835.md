---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-installatio-126ed23835
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/installation/guide/rcct-b-cce-es-installation-guide--release-15_01_es/rcct-m-manual-es-installation.html
retrieved_at: 2026-08-16T19:57:44.335584+00:00
---

Cisco Unified Contact Center Enterprise Engineering Specials Installation Guide, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Engineering Specials Installation Guide, Release 15.0(1)

Book Contents

- Book Title Page

- Introduction

- Manual ES Installation

Find Matches in This Book

## Results

Updated: August 15, 2025

Chapter: Manual ES Installation

## Chapter: Manual ES Installation

# Manual ES Installation

## Reverse Proxy Installation

To install the Reverse Proxy ES, follow the same procedure as for Reverse Proxy 15.0(1). For more details, see the Cisco Contact Center Enterprise Reverse Proxy Installation and Upgrade Guide, Release 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

## VOS Components ES Installation

The following procedures apply to all the components that are on the VOS servers:

Cloud Connect

Cisco Virtualized Voice Browser

Finesse

Cisco Unified Intelligence Center server

Live Data

Identity Service (IdS)/Single Sign-On(SSO)

### Before you begin

You must perform the following procedure first on the primary node and then on the secondary node(s).

Condition does not apply to Cisco VVB which is on a single node.

You must use CLI to perform this upgrade. Do not use the Cisco Unified Operating System Administration page to perform this
                                    upgrade or the installation may not proceed. Installing this ES or performing a rollback stops and restarts certain services.
                                    To avoid interruption, perform the installation or rollback during a maintenance window.

During ES installation and rollback, ensure that the SSH session is active throughout the installation process. Else, the
                                    installation will not be successful.

Take a DRS backup BEFORE and AFTER applying the ES.

Cisco VVB does not support DRS.

In 2000 Agent deployments with co-resident Unified Intelligence Center, Live Data, and Cisco IdS, all components share the
                                    same VM. Therefore, run the Cisco CUIC Options Package (COP) on the existing co-resident VM to install the ES. For all other
                                    deployments, install the CUIC COP separately on each VM (CUIC, LD, and IdS).

Step 1

Download <VOS component name>.1501.ES<ES number>.<VOS cop number>.cop.sha512 . file to an SFTP server that can be accessed by the component server. For example, download "cloudconnect.1501.ES202508.155.cop.sha512".

Step 2

Use SSH to log in to your system with the platform administration account.

Step 3

Access the CLI and run the following command: utils system upgrade initiate

Step 4

Follow the instructions that appear on your screen. When prompted, provide the location and credentials for the remote file
                                          system (SFTP server).

The COP file performs a check to ensure that Release 15.0(1) version or the previously or after released ES is installed.
                                                      If this release is not found on your system, an error is displayed, and the installation does not proceed.

Step 5

Select the required <vos component name>.1501.ES<ES number>.<cop number>.cop.sha512 .

Step 6

After installation is complete, restart the system using the command: utils system restart

Step 7

To verify if the correct version of VOS component is running, access the CLI by using the Administrator credentials and enter
                                       the following command: show version active

Step 8

Ensure that that the <vos component name>.1501.ES<ES number>.<cop number>.cop.sha512 . you installed is listed. Else, contact Cisco Technical Support.

Step 9

Check if the installation is successful by signing into your VOS server. For example, to check if the Finesse installation
                                       is successful, log into Finesse Desktop .

### What to do next

Ensure to clear the browser cache.

### Uninstall ES from VOS components

f there is a problem with the installation, you can roll back to the base version. The Rollback COP file removes the ES installed
                                 on the system and reverts your system to the base version of your component (in this case, 15.0(1) + previous ES release if
                                 any).

Step 1

Download the file <vos component name>.1501.ES.Rollback.cop.sha512 to an SFTP Server that can be accessed by the VOS component. For example, download "cloudconnect.1501.ES.Rollback.cop.sha512".

Step 2

Use SSH to log in to your VOS component with the platform administration account.

Step 3

Access the CLI and run the following command: utils system upgrade initiate

Step 4

Follow the on-screen instructions. When prompted, provide the location and credentials for the remote file system (SFTP server).

Step 5

When presented with the list of available upgrade options, select <vos component name>.1501.ES.Rollback.cop.sha512 .

Step 6

After rollback is complete, restart the system using the command: utils system restart

Step 7

To verify if the correct version of the VOS component is running, access the CLI using the Administrator credentials and enter
                                          the following command: show version active

Step 8

Ensure that <vos component name>.1501.ES<ES number>.<cop number>.cop.sha512 is listed. Else, contact Cisco Technical Support.

#### What to do next

Ensure to clear the browser cache.

## Unified CVP ES Installation

It is mandatory to install 15.0(1) as a base before installing CVP15.0(1) ES. The ES is a cumulative ES and can be installed
                                    on top of previous ES'es.

Before installing the patch, the audio files must be backed up from the C:\Cisco\CVP\VXMLServer\Tomcat\webapps\CVP\audio folder.

Take backup of all the custom files, if any. The custom files are located in the lib folder of the application-specific directory
                                    in the VXML server. For example, the files for HelloWorld custom application are located in the C:\Cisco\CVP\VXMLServer\Application\Helloworld\lib folder

Take backup of all the files if any customizations have been made to C:\Cisco\CVP\jre folder.

Before installing the patch, stop the following services if they are running. For more details, see the Installation and Upgrade Guide :

AppDynamics Machine Agent

Cisco AMP Orbital service

Windows Defender Advanced Threat Protection Service

Windows Defender Antivirus Network Inspection Service

Windows Defender AntiVirus Service

Step 1

Stop the ongoing services in the server. For example, stop the Operations Console Server (OAMP) service before running the
                                       patch on that server.

Step 2

Run the patch installer.

Step 3

Reboot the machine.

### What to do next

Call Studio ES Installation : Ensure that you install the ES for Call Studio only after completing the ES installation on all other CVP servers and removing
                                    any existing installations. To proceed, run the Call Studio ISO installer and complete the installation. Then reboot the computer.

Ensure that all services are up and running after the patch is installed.

Ensure that the audio folder is created under \Cisco\CVP\VXMLServer\Tomcat\webapps\CVP

Restore the backed-up audio files and the custom files.

Restore all the customizations made to the jre folder.

### Uninstall ES from CVP Servers

To uninstall the ES from Unified CVP Operations Console Server, Unified CVP Reporting Server, and Unified CVP VXML Server/Call
                                 Server:

Step 1

Go to Control Panel .

Step 2

Select Add or Remove Programs .

Step 3

Find the installed patch in the list and select Remove .

#### Example

Remove patches in the reverse order of their installation. For example, if you installed patches 3, then 5, then 10 for a
                                             product, you must uninstall patches 10, 5, and 3, in that order, to remove the patches from that product.

#### What to do next

Call Studio Uninstallation

Ensure that you remove the ES patch for Call Studio only after you’ve uninstalled the ES from all other CVP servers. Use the
                                       same procedure for uninstallation of Call Studio ES as with any other CVP server.

The following changes apply if you have Call Studio installed in the Program Files for the uninstallation process:

Access the settings to modify the system environment variables.

Find the variable named "CS_USER_HOME" and delete it.

## Contact Center Enterprise ES Installation

The Engineering Special (ES) is a cumulative update applied at the Unified Contact Center Enterprise (CCE) server level. Each
                              ES includes all features, security patches, and resolved caveats from the base release, tailored to specific server roles
                              within the system. The ES packages are categorized as follows:

The CCE ES applies to all CCE components including the PGs, Administration Clients, and Central Controller components (Logger,
                              Router, Administration, and Data Server).

The installation and uninstallation of this patch require a planned maintenance window, with an anticipated downtime of a
                                          few seconds to a few minutes. This downtime is necessary due to the synchronous high availability mode of the Router and Peripheral
                                          Gateway (PG). The duplex side of the Router and OPC process must be on the same build. Therefore, before starting the upgraded
                                          side, the older side must be stopped.

Step 1

Using Unified CCE Service Control, stop all the Unified CCE services running on the system for the whole installation process.

Step 2

Launch the installer and follow the instructions on the screen.

Step 3

After the installation of the engineering special, if the Unified CCE services are set to manual, start all the services using
                                       Unified CCE Service Control.

### Uninstall CCE ES

To uninstall Unified CCE ES, follow the steps:

Step 1

Go to Control Panel

Step 2

Select Add or Remove Programs .

Step 3

Find the installed patch and click Remove .

#### Example

Remove patches in the reverse order of their installation. For example, if you installed patches 3, then 5, then 10 for a
                                             product, you must uninstall patches 10, 5, and 3, in that order, to remove the patches from that product.

### Customers Also Viewed

- Implement CA-Signed Certificates in a CCE 12.6 Solution

| Note | Condition does not apply to Cisco VVB which is on a single node. |
|---|---|

| Note | Cisco VVB does not support DRS. |
|---|---|

| Step 1 | Download <VOS component name>.1501.ES<ES number>.<VOS cop number>.cop.sha512 . file to an SFTP server that can be accessed by the component server. For example, download "cloudconnect.1501.ES202508.155.cop.sha512". |
|---|---|
| Step 2 | Use SSH to log in to your system with the platform administration account. |
| Step 3 | Access the CLI and run the following command: utils system upgrade initiate |
| Step 4 | Follow the instructions that appear on your screen. When prompted, provide the location and credentials for the remote file
                                          system (SFTP server). Note The COP file performs a check to ensure that Release 15.0(1) version or the previously or after released ES is installed.
                                                      If this release is not found on your system, an error is displayed, and the installation does not proceed. | Note | The COP file performs a check to ensure that Release 15.0(1) version or the previously or after released ES is installed.
                                                      If this release is not found on your system, an error is displayed, and the installation does not proceed. |
| Note | The COP file performs a check to ensure that Release 15.0(1) version or the previously or after released ES is installed.
                                                      If this release is not found on your system, an error is displayed, and the installation does not proceed. |
| Step 5 | Select the required <vos component name>.1501.ES<ES number>.<cop number>.cop.sha512 . |
| Step 6 | After installation is complete, restart the system using the command: utils system restart |
| Step 7 | To verify if the correct version of VOS component is running, access the CLI by using the Administrator credentials and enter
                                       the following command: show version active |
| Step 8 | Ensure that that the <vos component name>.1501.ES<ES number>.<cop number>.cop.sha512 . you installed is listed. Else, contact Cisco Technical Support. |
| Step 9 | Check if the installation is successful by signing into your VOS server. For example, to check if the Finesse installation
                                       is successful, log into Finesse Desktop . |

| Note | The COP file performs a check to ensure that Release 15.0(1) version or the previously or after released ES is installed.
                                                      If this release is not found on your system, an error is displayed, and the installation does not proceed. |
|---|---|

| Step 1 | Download the file <vos component name>.1501.ES.Rollback.cop.sha512 to an SFTP Server that can be accessed by the VOS component. For example, download "cloudconnect.1501.ES.Rollback.cop.sha512". |
|---|---|
| Step 2 | Use SSH to log in to your VOS component with the platform administration account. |
| Step 3 | Access the CLI and run the following command: utils system upgrade initiate |
| Step 4 | Follow the on-screen instructions. When prompted, provide the location and credentials for the remote file system (SFTP server). |
| Step 5 | When presented with the list of available upgrade options, select <vos component name>.1501.ES.Rollback.cop.sha512 . |
| Step 6 | After rollback is complete, restart the system using the command: utils system restart |
| Step 7 | To verify if the correct version of the VOS component is running, access the CLI using the Administrator credentials and enter
                                          the following command: show version active |
| Step 8 | Ensure that <vos component name>.1501.ES<ES number>.<cop number>.cop.sha512 is listed. Else, contact Cisco Technical Support. |

| Step 1 | Stop the ongoing services in the server. For example, stop the Operations Console Server (OAMP) service before running the
                                       patch on that server. |
|---|---|
| Step 2 | Run the patch installer. |
| Step 3 | Reboot the machine. |

| Step 1 | Go to Control Panel . |
|---|---|
| Step 2 | Select Add or Remove Programs . |
| Step 3 | Find the installed patch in the list and select Remove . |

| Note | Remove patches in the reverse order of their installation. For example, if you installed patches 3, then 5, then 10 for a
                                             product, you must uninstall patches 10, 5, and 3, in that order, to remove the patches from that product. |
|---|---|

| Note | The following changes apply if you have Call Studio installed in the Program Files for the uninstallation process: Access the settings to modify the system environment variables. Find the variable named "CS_USER_HOME" and delete it. |
|---|---|

| Note | The installation and uninstallation of this patch require a planned maintenance window, with an anticipated downtime of a
                                          few seconds to a few minutes. This downtime is necessary due to the synchronous high availability mode of the Router and Peripheral
                                          Gateway (PG). The duplex side of the Router and OPC process must be on the same build. Therefore, before starting the upgraded
                                          side, the older side must be stopped. |
|---|---|

| Step 1 | Using Unified CCE Service Control, stop all the Unified CCE services running on the system for the whole installation process. |
|---|---|
| Step 2 | Launch the installer and follow the instructions on the screen. |
| Step 3 | After the installation of the engineering special, if the Unified CCE services are set to manual, start all the services using
                                       Unified CCE Service Control. |

| Step 1 | Go to Control Panel |
|---|---|
| Step 2 | Select Add or Remove Programs . |
| Step 3 | Find the installed patch and click Remove . |

| Note | Remove patches in the reverse order of their installation. For example, if you installed patches 3, then 5, then 10 for a
                                             product, you must uninstall patches 10, 5, and 3, in that order, to remove the patches from that product. |
|---|---|