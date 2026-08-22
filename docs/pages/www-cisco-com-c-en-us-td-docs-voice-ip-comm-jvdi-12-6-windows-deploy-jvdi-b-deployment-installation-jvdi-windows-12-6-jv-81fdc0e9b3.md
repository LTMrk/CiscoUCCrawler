---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-12-6-windows-deploy-jvdi-b-deployment-installation-jvdi-windows-12-6-jv-81fdc0e9b3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/12_6/windows/deploy/jvdi_b_deployment-installation-jvdi-windows-12-6/jvdi_b_deployment-installation-jvdi-windows-12-6_chapter_010.html
retrieved_at: 2026-08-22T00:38:06.364998+00:00
---

Deployment and Installation Guide for Cisco Jabber Softphone for VDI—Windows Release 12.6

# Deployment and Installation Guide for Cisco Jabber Softphone for VDI—Windows Release 12.6

Updated: April 9, 2019

Chapter: Installation and Deployment

## Chapter: Installation and Deployment

# Installation and Deployment

## Deployment and Installation Workflow

The Cisco Jabber for Windows and Cisco JVDI Agent versions must always match. The Cisco JVDI Client version can be the same, or up to two
                                          releases earlier. The available feature set is determined by the earlier software version.

You must install both Cisco JVDI Agent and Cisco JVDI Client; otherwise, the softphone fails to register.

We recommend that you read the Release Notes for Cisco Jabber Softphone for VDI—Windows for your release. Review the requirements to confirm that all required hardware and software meet them. Failure to meet all
                              requirements can result in a nonfunctional deployment.

Follow the instructions to deploy Cisco Jabber for Windows, up to the installation of the Jabber client.

You must create CSF devices for Cisco Jabber Softphone for VDI users, and add each user to the following Access Control Groups:

Standard CCM End Users

Standard CTI Enabled

See On-Premises Deployment for Cisco Jabber for your release.

For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release.

Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html .

Create and set up the hosted virtual desktops in the data center.

Ensure that a hosted virtual desktop (HVD) is ready for you to install Cisco JVDI Agent .

Set up and configure the thin clients. Documentation for thin clients is available from the original equipment manufacturer
                                       (OEM).

Configure the network. See Port Requirements .

Install the Cisco Jabber Softphone for VDI components on the thin clients and the hosted virtual desktops. See Install the Components Workflow .

After you install all required software on the HVD, you can clone the HVD.

## Set up the Hosted Virtual Desktops Workflow

Log in to the Microsoft Windows HVD as the new user, with administration rights.

Join the HVD to the corporate domain.

You must have domain administration rights.

Set up Citrix or VMware access to the HVDs.

Install Cisco JVDI Agent on the HVD.

Install Cisco Jabber on the HVD.

See the installation guide for your release: http://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html

Clone the HVD image.

For best practices for cloning Microsoft Windows HVD images, consult the documentation for your Citrix or VMware product.

## Install the Components Workflow

The Cisco Jabber for Windows and Cisco JVDI Agent versions must always match. The Cisco JVDI Client version can be the same, or up to two
                                          releases earlier. The available feature set is determined by the earlier software version.

Download the Cisco JVDI Client .

Download the Cisco JVDI Agent .

Have all users log out of the hosted virtual desktops.

On the thin client, install the Cisco JVDI Client .

See Cisco JVDI Client Installation .

On the HVD, uninstall any previously installed versions of Cisco JVDI Agent or Cisco JVDI Agent . Also uninstall Cisco Unified Communications clients, such as Cisco Jabber .

On the HVD, install Cisco JVDI Agent .

On the HVD, install Cisco Jabber .

Double-click CiscoJabberSetup.msi and follow the installation wizard steps. For detailed information about how to install
                                          Jabber for Windows, see On-Premises Deployment for Cisco Jabber for your release.

For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release.

Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html .

## Download the Cisco JVDI Client

Visit the following URL:

Go to Products > Unified Communications > Unified Communications Applications > Messaging > Cisco Jabber Softphone for VDI for Windows .

From the list, choose the file for your release.

Click Download or Add to cart and follow the prompts.

## Download the Cisco JVDI Agent

Install Cisco JVDI Agent on the hosted virtual desktops (HVD), before you install Cisco Jabber for Windows.

Visit the following URL:

Go to Products > Unified Communications > Unified Communications Applications > Messaging > Cisco Jabber Softphone for VDI for Windows .

From the list, choose the file for your release.

Click Download or Add to cart and follow the prompts.

## Cisco JVDI Client Installation

### Prerequisites

Before you install Cisco JVDI Client on the thin clients, complete the following tasks:

Install and set up the Citrix Receiver or VMware Horizon View Client.

Ensure that you are using a supported version of your Citrix or VMware product. For more information, see Release Notes for Cisco Jabber Softphone for VDI for Windows for your release.

The JVDI Client is available as a 32– or 64–bit application. When you install VMware Horizon View Client, and you want to
                                                install the 32–bit version of the JVDI Client, choose Customize Installation and configure the following settings:

Uncheck the Virtualization Pack for Skype for Business check box.

Check the Install 32-bit Core remote Experience on this 64-bit machine check box.

Do not perform the preceding configuration if you want to install the 64–bit version of JVDI Client.

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

| Important | The Cisco Jabber for Windows and Cisco JVDI Agent versions must always match. The Cisco JVDI Client version can be the same, or up to two
                                          releases earlier. The available feature set is determined by the earlier software version. You must install both Cisco JVDI Agent and Cisco JVDI Client; otherwise, the softphone fails to register. |
|---|---|

| Step 1 | Follow the instructions to deploy Cisco Jabber for Windows, up to the installation of the Jabber client. Important You must create CSF devices for Cisco Jabber Softphone for VDI users, and add each user to the following Access Control Groups: Standard CCM End Users Standard CTI Enabled See On-Premises Deployment for Cisco Jabber for your release. For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release. Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html . | Important | You must create CSF devices for Cisco Jabber Softphone for VDI users, and add each user to the following Access Control Groups: Standard CCM End Users Standard CTI Enabled |
|---|---|---|---|
| Important | You must create CSF devices for Cisco Jabber Softphone for VDI users, and add each user to the following Access Control Groups: Standard CCM End Users Standard CTI Enabled |
| Step 2 | Create and set up the hosted virtual desktops in the data center. Ensure that a hosted virtual desktop (HVD) is ready for you to install Cisco JVDI Agent . |
| Step 3 | Set up and configure the thin clients. Documentation for thin clients is available from the original equipment manufacturer
                                       (OEM). |
| Step 4 | Configure the network. See Port Requirements . |
| Step 5 | Install the Cisco Jabber Softphone for VDI components on the thin clients and the hosted virtual desktops. See Install the Components Workflow . After you install all required software on the HVD, you can clone the HVD. |

| Important | You must create CSF devices for Cisco Jabber Softphone for VDI users, and add each user to the following Access Control Groups: Standard CCM End Users Standard CTI Enabled |
|---|---|

| Step 1 | Log in to the Microsoft Windows HVD as the new user, with administration rights. |
|---|---|
| Step 2 | Join the HVD to the corporate domain. You must have domain administration rights. |
| Step 3 | Set up Citrix or VMware access to the HVDs. |
| Step 4 | Install Cisco JVDI Agent on the HVD. |
| Step 5 | Install Cisco Jabber on the HVD. See the installation guide for your release: http://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html |
| Step 6 | Clone the HVD image. For best practices for cloning Microsoft Windows HVD images, consult the documentation for your Citrix or VMware product. |

| Important | The Cisco Jabber for Windows and Cisco JVDI Agent versions must always match. The Cisco JVDI Client version can be the same, or up to two
                                          releases earlier. The available feature set is determined by the earlier software version. |
|---|---|

| Step 1 | Download the Cisco JVDI Client . |
|---|---|
| Step 2 | Download the Cisco JVDI Agent . |
| Step 3 | Have all users log out of the hosted virtual desktops. |
| Step 4 | On the thin client, install the Cisco JVDI Client . See Cisco JVDI Client Installation . |
| Step 5 | On the HVD, uninstall any previously installed versions of Cisco JVDI Agent or Cisco JVDI Agent . Also uninstall Cisco Unified Communications clients, such as Cisco Jabber . |
| Step 6 | On the HVD, install Cisco JVDI Agent . |
| Step 7 | On the HVD, install Cisco Jabber . Double-click CiscoJabberSetup.msi and follow the installation wizard steps. For detailed information about how to install
                                          Jabber for Windows, see On-Premises Deployment for Cisco Jabber for your release. For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release. Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html . |

| Step 1 | Visit the following URL: http://www.cisco.com/cisco/software/navigator.html |
|---|---|
| Step 2 | Go to Products > Unified Communications > Unified Communications Applications > Messaging > Cisco Jabber Softphone for VDI for Windows . |
| Step 3 | From the list, choose the file for your release. |
| Step 4 | Click Download or Add to cart and follow the prompts. |

| Step 1 | Visit the following URL: http://www.cisco.com/cisco/software/navigator.html |
|---|---|
| Step 2 | Go to Products > Unified Communications > Unified Communications Applications > Messaging > Cisco Jabber Softphone for VDI for Windows . |
| Step 3 | From the list, choose the file for your release. |
| Step 4 | Click Download or Add to cart and follow the prompts. |

| Important | The JVDI Client is available as a 32– or 64–bit application. When you install VMware Horizon View Client, and you want to
                                                install the 32–bit version of the JVDI Client, choose Customize Installation and configure the following settings: Uncheck the Virtualization Pack for Skype for Business check box. Check the Install 32-bit Core remote Experience on this 64-bit machine check box. Do not perform the preceding configuration if you want to install the 64–bit version of JVDI Client. |
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