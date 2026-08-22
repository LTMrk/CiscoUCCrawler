---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-12-9-dig-jvdi-b-deploy-install-jvdi-12-9-jvdi-b-deploy-install-jvdi-12--5d5f1ca6a1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/12_9/dig/jvdi_b_deploy-install-jvdi-12-9/jvdi_b_deploy-install-jvdi-12-9_chapter_0100.html
retrieved_at: 2026-08-22T00:32:02.163471+00:00
---

Deployment and Installation Guide for Cisco Jabber Softphone for VDI Release 12.9

# Deployment and Installation Guide for Cisco Jabber Softphone for VDI Release 12.9

Updated: July 8, 2020

Chapter: Installation

## Chapter: Installation

# Installation

## Set up the Hosted Virtual Desktops Workflow

The Virtual Machines for the HVDs can be either Citrix-, or VMware-provisioned. Citrix-provisioned virtual machines can be
                              dedicated, or have multiple users connected over multiple remote sessions. To support multiple remote sessions, the virtual
                              machine must be running a supported Microsoft Windows Server operating system.

Log in to the Microsoft Windows HVD as the new user, with administration rights.

Join the HVD to the corporate domain.

You must have domain administration rights.

Set up Citrix or VMware access to the HVDs.

## Install the Components Workflow—HP Thin Pro

### Before you begin

Ensure that you have all of the required files on hand. If you plan to manually install Cisco JVDI Client on the thin clients, copy the files to a USB stick.

Follow the guidelines in the Version Support Strategy .

Download the Cisco JVDI Agent

Download the Cisco JVDI Client

Starting with Thin Pro7.1 SP3, the prerequisites file is pre-installed with Thin Pro. For Thin Pro 6.2, you can obtain the
                                          prerequisites file directly from HP.

On the thin client, install the Cisco Jabber Softphone for VDI files in the following order, either manually from a USB stick, or use HP Device Manager for mass deployments.

Order of installation:

Prerequisites

Cisco Jabber Softphone for VDI .deb package.

For more information about mass deployment, see the documentation for HP Device Manager 4.7, available from HP.

On the HVD, install Cisco JVDI Agent .

Double-click the .msi file, and then follow the installation wizard steps.

On the HVD, install Cisco Jabber for Windows.

Double-click CiscoJabberSetup.msi and follow the installation wizard steps. For detailed information about how to install Cisco Jabber for Windows, see On-Premises Deployment for Cisco Jabber for your release.

For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release.

Cisco Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html .

### What to do next

Clone the HVD. For best practices for cloning Microsoft Windows HVD images, consult the documentation for your Citrix or VMware
                              product.

Create an image for the thin clients. See the documentation for HP Device Manager 4.7, available from HP.

## Install the Components Workflow—MacOS

### Before you begin

Follow the guidelines in the Version Support Strategy .

Download the Cisco JVDI Agent

Download the Cisco JVDI Client

On the HVD, install Cisco JVDI Agent .

On the HVD, install Cisco Jabber .

Double-click CiscoJabberSetup.msi and follow the installation wizard steps. For detailed information about how to install Cisco Jabber for Windows, see On-Premises Deployment for Cisco Jabber for your release.

For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release.

Cisco Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html .

On the thin client, install the Cisco JVDI Client .

See Run the MacOS Installer .

### Run the MacOS Installer

Run the MacOS installer (PKG) to install Cisco JVDI Client .

Double-click the Install_Cisco_JVDI_Client.pkg file.

Read the EULA and, if you agree, click Continue .

Click Install , and if a prompt appears that Citrix Viewer must be closed first, click Close Application and Install .

You can also click Install Later if you cannot close Citrix at the time.

Click through the remaining screens to complete the installation.

### Accept Permissions

When users launch the Cisco JVDI Client on Mac OS for the first time, accept the following required permissions:

Permission

Description

Access Camera

Uses the camera in a video call, or trying to open the camera in Settings.

Access Microphone

Uses the microphone for voice in a call.

Record Screen

Uses the camera in a video call, or trying to open the camera in Settings.

Access Accessibility

Required for matching the Cisco JVDI Client to the Citrix viewer. After maximizing the application on Mac OS, the application window is put into a new virtual desktop
                                                         (or space). If users maximize the Citrix viewer, Jabber's video overlay window joins the space of the Citrix viewer. To do
                                                         this, JVDI need request to access the system’s Accessibility. User would see this pop-up in the first time of running JVDI.

## Install the Components Workflow—Ubuntu

### Before you begin

Ensure that you have all of the required files on hand. If you plan to manually install Cisco JVDI Client on the thin clients, copy the files to a USB stick.

Follow the guidelines in the Version Support Strategy .

Download the Cisco JVDI Agent

Obtain the Cisco Jabber Softphone for VDI deb package from the Ubuntu software center repository.

On the thin client, use the terminal emulator to run the following command: sudo apt-get update , and then enter your password at the prompt. The list of repositories for the Ubuntu Software Center updates. After the command
                                    finishes reading the package lists, you can close the terminal emulator. You can place the file on a network share accessible
                                    from the thin clients, or copy it to a USB stick.

On the HVD, install Cisco JVDI Agent .

Double-click the Cisco JVDI Agent .msi and follow the installation wizard steps.

On the HVD, install Cisco Jabber ; double-click CiscoJabberSetup.msi and follow the installation wizard steps.

For detailed information about how to install Cisco Jabber for Windows, see On-Premises Deployment for Cisco Jabber for your release.

For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release.

Cisco Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html .

On the thin client, install the Cisco JVDI Client ; enter your password at the authentication prompt.

When you double-click the Cisco Jabber Softphone for VDI deb package, the Ubuntu Software Center opens. After you click Install , the Ubuntu Software Center locates and installs the dependency libraries, and then installs the Cisco JVDI Client .

### What to do next

Clone the HVD image. For best practices for cloning Microsoft Windows HVD images, consult the documentation for your Citrix
                              or VMware product.

Create an image for the thin clients.

## Install the Components Workflow—Unicon eLux

### Before you begin

Follow the guidelines in the Version Support Strategy .

Download the Cisco JVDI Agent

Download the Cisco JVDI Client

Download Cisco AnyConnect—Unicon eLux (Optional, required only if users need VPN connectivity.)

On the HVD, install Cisco Jabber for Windows.

Double-click CiscoJabberSetup.msi and follow the installation wizard steps. For detailed information about how to install Cisco Jabber for Windows, see On-Premises Deployment for Cisco Jabber for your release.

For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release.

Cisco Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html .

On the HVD, install Cisco JVDI Agent .

Double-click the MSI file and follow the installation wizard steps.

On the thin client, install the Cisco JVDI Client and if required, deploy Cisco AnyConnect at the same time.

### What to do next

Clone the HVD image. For best practices for cloning Microsoft Windows HVD images, consult the documentation for your Citrix
                              or VMware product.

Use the Elias tool to create an image that contains Cisco JVDI Client . Deploy the image to the thin clients. For more information about how to create an image or how to update the thin client,
                              see the Elias documentation available from the Unicon website.

## Install the Components Workflow—Windows

### Before you begin

Follow the guidelines in the Version Support Strategy .

Download the Cisco JVDI Agent

Download the Cisco JVDI Client

On the HVD, install Cisco JVDI Agent .

On the HVD, install Cisco Jabber .

Double-click CiscoJabberSetup.msi and follow the installation wizard steps. For detailed information about how to install Cisco Jabber for Windows, see On-Premises Deployment for Cisco Jabber for your release.

For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release.

Cisco Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html .

On the thin client, install the Cisco JVDI Client .

See Cisco JVDI Client Installation .

### Cisco JVDI Client Installation

#### Prerequisites

Before you install Cisco JVDI Client on the thin clients, complete the following tasks:

Install and set up the Citrix Receiver or VMware Horizon View Client.

The JVDI Client is available as a 32– or 64–bit application.

Obtain the Cisco JVDI Client zip file, and extract the contents.

Use one of the following methods to install Cisco JVDI Client :

Run the Microsoft Installer

Use the Command Line

Use the Group Policy Editor

### Run the Microsoft Installer

Run the Microsoft Installer (MSI) to install Cisco JVDI Client .

Double-click the CiscoJVDIClientSetup.msi file.

To open the executable file, click OK .

If the Open File - Security Warning appears, click Run .

Read the EULA and, if you agree, click Accept and Install .

http://www.cisco.com/go/eula .

To complete the installation, click Finish .

### Use the Command Line

Open a command window.

Enter the following command: start /wait msiexec.exe /i <path to MSI>\CiscoJVDIClientSetup.msi /quiet .

The /quiet switch specifies a silent installation.

### Use the Group Policy Editor

Use the Group Policy Management console to deploy Cisco JVDI Client to supported thin clients that are running a supported Microsoft Windows operating system.

#### Before you begin

Use Microsoft Orca to set the language code to 1033.

Copy the modified Microsoft Installer (MSI) to a software distribution point for deployment. All computers to which you plan
                                       to deploy Cisco JVDI Client must be able to access the MSI on the distribution point.

Select Start > Run .

At the prompt, enter the following command: GPMC.msc .

Right-click on the appropriate domain in the left section.

Select Create a GPO in this Domain, and Link it here .

In the New GPO window, Name field, enter a name for the group policy object.

Leave the default value or select an option from the Source Starter GPO list, and then select OK .

The new group policy appears in the list of group policies for the domain.

Select the group policy object under the domain in the left section.

From the Security Filtering section of the Scope tab, select Add .

Specify the computers and users to which you want to deploy Cisco JVDI Client .

Specify the MSI file.

Right-click the group policy object in the left section and then select Edit .

The Group Policy Management Editor opens.

Select Computer Configuration and then select Policies > Software Settings .

Right-click Software Installation and then select New > Package .

Next to File Name , enter the location of the MSI file.

#### Example:

Select the MSI file, and then select Open .

In the Deploy Software dialog box, select Assigned , and then select OK .

| Step 1 | Log in to the Microsoft Windows HVD as the new user, with administration rights. |
|---|---|
| Step 2 | Join the HVD to the corporate domain. You must have domain administration rights. |
| Step 3 | Set up Citrix or VMware access to the HVDs. |

| Note | Starting with Thin Pro7.1 SP3, the prerequisites file is pre-installed with Thin Pro. For Thin Pro 6.2, you can obtain the
                                          prerequisites file directly from HP. |
|---|---|

| Step 1 | On the thin client, install the Cisco Jabber Softphone for VDI files in the following order, either manually from a USB stick, or use HP Device Manager for mass deployments. Order of installation: Prerequisites Cisco Jabber Softphone for VDI .deb package. For more information about mass deployment, see the documentation for HP Device Manager 4.7, available from HP. |
|---|---|
| Step 2 | On the HVD, install Cisco JVDI Agent . Double-click the .msi file, and then follow the installation wizard steps. |
| Step 3 | On the HVD, install Cisco Jabber for Windows. Double-click CiscoJabberSetup.msi and follow the installation wizard steps. For detailed information about how to install Cisco Jabber for Windows, see On-Premises Deployment for Cisco Jabber for your release. For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release. Cisco Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | On the HVD, install Cisco JVDI Agent . |  |
| Step 2 | On the HVD, install Cisco Jabber . | Double-click CiscoJabberSetup.msi and follow the installation wizard steps. For detailed information about how to install Cisco Jabber for Windows, see On-Premises Deployment for Cisco Jabber for your release. For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release. Cisco Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html . |
| Step 3 | On the thin client, install the Cisco JVDI Client . | See Run the MacOS Installer . |

| Step 1 | Double-click the Install_Cisco_JVDI_Client.pkg file. |
|---|---|
| Step 2 | Read the EULA and, if you agree, click Continue . |
| Step 3 | Click Install , and if a prompt appears that Citrix Viewer must be closed first, click Close Application and Install . You can also click Install Later if you cannot close Citrix at the time. |
| Step 4 | Click through the remaining screens to complete the installation. |

| When users launch the Cisco JVDI Client on Mac OS for the first time, accept the following required permissions: Table 1. Required Permissions Permission Description Access Camera Uses the camera in a video call, or trying to open the camera in Settings. Access Microphone Uses the microphone for voice in a call. Record Screen Uses the camera in a video call, or trying to open the camera in Settings. Access Accessibility Required for matching the Cisco JVDI Client to the Citrix viewer. After maximizing the application on Mac OS, the application window is put into a new virtual desktop
                                                         (or space). If users maximize the Citrix viewer, Jabber's video overlay window joins the space of the Citrix viewer. To do
                                                         this, JVDI need request to access the system’s Accessibility. User would see this pop-up in the first time of running JVDI. | Permission | Description | Access Camera | Uses the camera in a video call, or trying to open the camera in Settings. | Access Microphone | Uses the microphone for voice in a call. | Record Screen | Uses the camera in a video call, or trying to open the camera in Settings. | Access Accessibility | Required for matching the Cisco JVDI Client to the Citrix viewer. After maximizing the application on Mac OS, the application window is put into a new virtual desktop
                                                         (or space). If users maximize the Citrix viewer, Jabber's video overlay window joins the space of the Citrix viewer. To do
                                                         this, JVDI need request to access the system’s Accessibility. User would see this pop-up in the first time of running JVDI. |
|---|---|---|---|---|---|---|---|---|---|---|
| Permission | Description |
| Access Camera | Uses the camera in a video call, or trying to open the camera in Settings. |
| Access Microphone | Uses the microphone for voice in a call. |
| Record Screen | Uses the camera in a video call, or trying to open the camera in Settings. |
| Access Accessibility | Required for matching the Cisco JVDI Client to the Citrix viewer. After maximizing the application on Mac OS, the application window is put into a new virtual desktop
                                                         (or space). If users maximize the Citrix viewer, Jabber's video overlay window joins the space of the Citrix viewer. To do
                                                         this, JVDI need request to access the system’s Accessibility. User would see this pop-up in the first time of running JVDI. |

| Permission | Description |
|---|---|
| Access Camera | Uses the camera in a video call, or trying to open the camera in Settings. |
| Access Microphone | Uses the microphone for voice in a call. |
| Record Screen | Uses the camera in a video call, or trying to open the camera in Settings. |
| Access Accessibility | Required for matching the Cisco JVDI Client to the Citrix viewer. After maximizing the application on Mac OS, the application window is put into a new virtual desktop
                                                         (or space). If users maximize the Citrix viewer, Jabber's video overlay window joins the space of the Citrix viewer. To do
                                                         this, JVDI need request to access the system’s Accessibility. User would see this pop-up in the first time of running JVDI. |

| Step 1 | On the HVD, install Cisco JVDI Agent . Double-click the Cisco JVDI Agent .msi and follow the installation wizard steps. |
|---|---|
| Step 2 | On the HVD, install Cisco Jabber ; double-click CiscoJabberSetup.msi and follow the installation wizard steps. For detailed information about how to install Cisco Jabber for Windows, see On-Premises Deployment for Cisco Jabber for your release. For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release. Cisco Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html . |
| Step 3 | On the thin client, install the Cisco JVDI Client ; enter your password at the authentication prompt. When you double-click the Cisco Jabber Softphone for VDI deb package, the Ubuntu Software Center opens. After you click Install , the Ubuntu Software Center locates and installs the dependency libraries, and then installs the Cisco JVDI Client . |

| Step 1 | On the HVD, install Cisco Jabber for Windows. Double-click CiscoJabberSetup.msi and follow the installation wizard steps. For detailed information about how to install Cisco Jabber for Windows, see On-Premises Deployment for Cisco Jabber for your release. For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release. Cisco Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html . |
|---|---|
| Step 2 | On the HVD, install Cisco JVDI Agent . Double-click the MSI file and follow the installation wizard steps. |
| Step 3 | On the thin client, install the Cisco JVDI Client and if required, deploy Cisco AnyConnect at the same time. |

| Step 1 | On the HVD, install Cisco JVDI Agent . |
|---|---|
| Step 2 | On the HVD, install Cisco Jabber . Double-click CiscoJabberSetup.msi and follow the installation wizard steps. For detailed information about how to install Cisco Jabber for Windows, see On-Premises Deployment for Cisco Jabber for your release. For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release. Cisco Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html . |
| Step 3 | On the thin client, install the Cisco JVDI Client . See Cisco JVDI Client Installation . |

| Note | The JVDI Client is available as a 32– or 64–bit application. |
|---|---|

| Step 1 | Double-click the CiscoJVDIClientSetup.msi file. |
|---|---|
| Step 2 | To open the executable file, click OK . |
| Step 3 | If the Open File - Security Warning appears, click Run . |
| Step 4 | Read the EULA and, if you agree, click Accept and Install . http://www.cisco.com/go/eula . |
| Step 5 | To complete the installation, click Finish . |

| Step 1 | Open a command window. |
|---|---|
| Step 2 | Enter the following command: start /wait msiexec.exe /i <path to MSI>\CiscoJVDIClientSetup.msi /quiet . The /quiet switch specifies a silent installation. |

| Step 1 | Select Start > Run . |
|---|---|
| Step 2 | At the prompt, enter the following command: GPMC.msc . |
| Step 3 | Right-click on the appropriate domain in the left section. |
| Step 4 | Select Create a GPO in this Domain, and Link it here . |
| Step 5 | In the New GPO window, Name field, enter a name for the group policy object. |
| Step 6 | Leave the default value or select an option from the Source Starter GPO list, and then select OK . The new group policy appears in the list of group policies for the domain. |
| Step 7 | Select the group policy object under the domain in the left section. |
| Step 8 | From the Security Filtering section of the Scope tab, select Add . |
| Step 9 | Specify the computers and users to which you want to deploy Cisco JVDI Client . |
| Step 10 | Specify the MSI file. |
| Step 11 | Right-click the group policy object in the left section and then select Edit . The Group Policy Management Editor opens. |
| Step 12 | Select Computer Configuration and then select Policies > Software Settings . |
| Step 13 | Right-click Software Installation and then select New > Package . |
| Step 14 | Next to File Name , enter the location of the MSI file. Example: \\server\software_distribution Important Enter the Uniform Naming Convention (UNC) path for the location of the MSI file. If you do not enter the UNC path, Group Policy
                                                      cannot deploy Cisco JVDI Client . | Important | Enter the Uniform Naming Convention (UNC) path for the location of the MSI file. If you do not enter the UNC path, Group Policy
                                                      cannot deploy Cisco JVDI Client . |
| Important | Enter the Uniform Naming Convention (UNC) path for the location of the MSI file. If you do not enter the UNC path, Group Policy
                                                      cannot deploy Cisco JVDI Client . |
| Step 15 | Select the MSI file, and then select Open . |
| Step 16 | In the Deploy Software dialog box, select Assigned , and then select OK . |

| Important | Enter the Uniform Naming Convention (UNC) path for the location of the MSI file. If you do not enter the UNC path, Group Policy
                                                      cannot deploy Cisco JVDI Client . |
|---|---|