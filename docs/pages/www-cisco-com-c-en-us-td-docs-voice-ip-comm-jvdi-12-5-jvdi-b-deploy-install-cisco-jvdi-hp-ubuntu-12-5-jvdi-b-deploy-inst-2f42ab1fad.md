---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-12-5-jvdi-b-deploy-install-cisco-jvdi-hp-ubuntu-12-5-jvdi-b-deploy-inst-2f42ab1fad
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/12_5/jvdi_b_deploy-install-cisco-jvdi-hp-ubuntu-12-5/jvdi_b_deploy-install-cisco-jvdi-hp-ubuntu-12-5_chapter_010.html
retrieved_at: 2026-08-22T00:34:56.915060+00:00
---

Deployment and Installation Guide for Cisco Jabber Softphone for VDI—HP Thin Pro and Ubuntu Release 12.5

# Deployment and Installation Guide for Cisco Jabber Softphone for VDI—HP Thin Pro and Ubuntu Release 12.5

Updated: November 29, 2018

Chapter: Installation and Deployment

## Chapter: Installation and Deployment

# Installation and Deployment

## Deployment and Installation Workflow—HP Thin Pro

The Cisco Jabber for Windows version must match your Cisco Jabber Softphone for VDI version. The Cisco JVDI Agent and Cisco JVDI Client versions must be the same.

You must install both Cisco JVDI Agent and Cisco JVDI Client; otherwise, the softphone fails to register.

We recommend that you read the Release Notes for Cisco Jabber Softphone for VDI—HP Thin Pro and Ubuntu for your release. Review requirements to confirm that all required hardware and software meet them. Failure to meet all requirements
                              can result in a nonfunctional deployment.

Follow the instructions to deploy Cisco Jabber for Windows, up to the installation of the Jabber client.

You must create CSF devices for Cisco Jabber Softphone for VDI users, and add each user to the following Access Control Groups:

Standard CCM End Users

Standard CTI Enabled

See On-Premises Deployment for Cisco Jabber for your release.

For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release.

Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html .

Create and set up the hosted virtual desktops in the data center.

Ensure that the hosted virtual desktops (HVD) are ready for you to install Cisco JVDI Agent .

Set up and configure the thin clients.

Configure the network. See Port Requirements .

Install the Cisco Jabber Softphone for VDI components on the thin clients and the hosted virtual desktop. See Install the Components Workflow—HP Thin Pro .

After you install Cisco JVDI Agent and other required software on the HVD, you can clone the HVD.

## Deployment and Installation Workflow—Ubuntu

The Cisco Jabber for Windows version must match your Cisco Jabber Softphone for VDI version. The Cisco JVDI Agent and Cisco JVDI Client versions must be the same.

You must install both Cisco JVDI Agent and Cisco JVDI Client; otherwise, the softphone fails to register.

We recommend that you read the Release Notes for Cisco Jabber Softphone for VDI—HP Thin Pro and Ubuntu for your release. Review the requirements to confirm that all required hardware and software meet them. Failure to meet all
                              requirements can result in a nonfunctional deployment.

Follow the instructions to deploy Cisco Jabber for Windows, up to the installation of the Jabber client.

You must create CSF devices for Cisco Jabber Softphone for VDI users, and add each user to the following Access Control Groups:

Standard CCM End Users

Standard CTI Enabled

See On-Premises Deployment for Cisco Jabber for your release.

For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release.

Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html .

Create and set up the hosted virtual desktops in the data center.

Ensure that a hosted virtual desktop (HVD) is ready for you to install Cisco Jabber Softphone for VDI .

Set up and configure the thin clients.

Have the hardware ready to install Cisco Jabber Softphone for VDI components.

Documentation for Ubuntu thin clients is available from the individual hardware vendors. Documentation for Ubuntu is available
                                          from the Ubuntu website.

Configure the network. See Port Requirements .

Install the Cisco Jabber Softphone for VDI components on the thin clients and the hosted virtual desktop. See Install the Components Workflow—Ubuntu .

After you install Cisco JVDI Agent and other required software on the HVD, you can clone the HVD.

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

## Install the Components Workflow—HP Thin Pro

The Cisco Jabber for Windows version must match your Cisco Jabber Softphone for VDI version. The Cisco JVDI Agent and Cisco JVDI Client versions must be the same.

Obtain the Cisco Jabber Softphone for VDI Debian (.deb) package and cisco-jvdi<xx.x.x>-pre-reqs.xar file from HP.

The <xx.x.x> variable in the filename is the Cisco Jabber Softphone for VDI release number. For assistance locating files on the HP site, contact HP support.

Have the Cisco Jabber Softphone for VDI files on hand and ready to install. If you plan to manually install Cisco JVDI Client on the thin clients, copy the files to a USB stick.

Download the Cisco JVDI Agent .

Have the Cisco JVDI Agent installation file on hand and ready to install on the hosted virtual desktop.

Have all users log out of the hosted virtual desktops.

On the thin client, install the Cisco Jabber Softphone for VDI files in the following order, either manually from a USB stick, or use HP Device Manager for mass deployments.

Order of installation:

Install cisco-jvdi12.0.x-pre-reqs-thinpro6.2.0-hp1d.xar.

Install the Cisco Jabber Softphone for VDI .deb package.

For more information about mass deployment, see the documentation for HP Device Manager 4.7, available from HP.

On the HVD, uninstall any previously installed Cisco JVDI Agent .

On the HVD, uninstall any previously installed Cisco Unified Communications clients, such as Cisco Jabber .

On the HVD, install Cisco JVDI Agent .

Double-click the .msi file, and then follow the installation wizard steps.

On the HVD, install Cisco Jabber for Windows.

Double-click CiscoJabberSetup.msi and follow the installation wizard steps. For detailed information about how to install
                                          Jabber for Windows, see On-Premises Deployment for Cisco Jabber for your release.

For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release.

Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html .

## Install the Components Workflow—Ubuntu

The Cisco Jabber for Windows version must match your Cisco Jabber Softphone for VDI version. The Cisco JVDI Agent and Cisco JVDI Client versions must be the same.

Obtain the Cisco Jabber Softphone for VDI deb package from the Ubuntu software center repository.

Have the Cisco Jabber Softphone for VDI deb package on hand and ready to install. You can place the file on a network share accessible from the thin clients, or
                                          copy it to a USB stick.

Download the Cisco JVDI Agent .

Have the Cisco JVDI Agent installation file on hand and ready to install on the hosted virtual desktop.

Have all users log out of the hosted virtual desktops.

On the thin client, use the terminal emulator to run the following command: sudo apt-get update , and then enter your password at the prompt.

Updates the list of repositories for the Ubuntu Software Center.

After the command finishes reading the package lists, you can close the terminal emulator.

On the thin client, install the Cisco JVDI Client ; enter your password at the authentication prompt.

When you double-click the Cisco Jabber Softphone for VDI deb package, the Ubuntu Software Center opens. After you click Install , the Ubuntu Software Center locates and installs the dependency libraries, and then installs the Cisco JVDI Client .

On the HVD, uninstall any previously installed Cisco JVDI Agent .

On the HVD, uninstall any previously installed Cisco Unified Communications clients, such as Cisco Jabber .

On the HVD, install Cisco JVDI Agent .

Double-click the Cisco JVDI Agent .msi and follow the installation wizard steps.

On the HVD, install Cisco Jabber.

Double-click CiscoJabberSetup.msi and follow the installation wizard steps. For detailed information about how to install
                                          Jabber for Windows, see On-Premises Deployment for Cisco Jabber for your release.

For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release.

Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html .

## Download the Cisco JVDI Client

Visit the following URL:

Go to Products > Unified Communications > Unified Communications Applications > Messaging > Cisco Jabber Softphone for VDI for HP Thin Pro and Ubuntu .

From the list, choose the file for your release.

Click Download or Add to cart and follow the prompts.

## Download the Cisco JVDI Agent

Install Cisco JVDI Agent on the hosted virtual desktops (HVD), before you install Cisco Jabber for Windows.

Visit the following URL:

Go to Products > Unified Communications > Unified Communications Applications > Messaging > Cisco Jabber Softphone for VDI for HP Thin Pro and Ubuntu .

From the list, choose the file for your release.

Click Download or Add to cart and follow the prompts.

| Important | The Cisco Jabber for Windows version must match your Cisco Jabber Softphone for VDI version. The Cisco JVDI Agent and Cisco JVDI Client versions must be the same. You must install both Cisco JVDI Agent and Cisco JVDI Client; otherwise, the softphone fails to register. |
|---|---|

| Step 1 | Follow the instructions to deploy Cisco Jabber for Windows, up to the installation of the Jabber client. Important You must create CSF devices for Cisco Jabber Softphone for VDI users, and add each user to the following Access Control Groups: Standard CCM End Users Standard CTI Enabled See On-Premises Deployment for Cisco Jabber for your release. For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release. Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html . | Important | You must create CSF devices for Cisco Jabber Softphone for VDI users, and add each user to the following Access Control Groups: Standard CCM End Users Standard CTI Enabled |
|---|---|---|---|
| Important | You must create CSF devices for Cisco Jabber Softphone for VDI users, and add each user to the following Access Control Groups: Standard CCM End Users Standard CTI Enabled |
| Step 2 | Create and set up the hosted virtual desktops in the data center. Ensure that the hosted virtual desktops (HVD) are ready for you to install Cisco JVDI Agent . |
| Step 3 | Set up and configure the thin clients. Documentation for HP Thin Pro-based thin clients and for HP Thin Pro is available from the HP website. Ensure that the thin
                                       clients are ready for you to install the Cisco JVDI Client . |
| Step 4 | Configure the network. See Port Requirements . |
| Step 5 | Install the Cisco Jabber Softphone for VDI components on the thin clients and the hosted virtual desktop. See Install the Components Workflow—HP Thin Pro . After you install Cisco JVDI Agent and other required software on the HVD, you can clone the HVD. |

| Important | You must create CSF devices for Cisco Jabber Softphone for VDI users, and add each user to the following Access Control Groups: Standard CCM End Users Standard CTI Enabled |
|---|---|

| Important | The Cisco Jabber for Windows version must match your Cisco Jabber Softphone for VDI version. The Cisco JVDI Agent and Cisco JVDI Client versions must be the same. You must install both Cisco JVDI Agent and Cisco JVDI Client; otherwise, the softphone fails to register. |
|---|---|

| Step 1 | Follow the instructions to deploy Cisco Jabber for Windows, up to the installation of the Jabber client. Important You must create CSF devices for Cisco Jabber Softphone for VDI users, and add each user to the following Access Control Groups: Standard CCM End Users Standard CTI Enabled See On-Premises Deployment for Cisco Jabber for your release. For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release. Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html . | Important | You must create CSF devices for Cisco Jabber Softphone for VDI users, and add each user to the following Access Control Groups: Standard CCM End Users Standard CTI Enabled |
|---|---|---|---|
| Important | You must create CSF devices for Cisco Jabber Softphone for VDI users, and add each user to the following Access Control Groups: Standard CCM End Users Standard CTI Enabled |
| Step 2 | Create and set up the hosted virtual desktops in the data center. Ensure that a hosted virtual desktop (HVD) is ready for you to install Cisco Jabber Softphone for VDI . |
| Step 3 | Set up and configure the thin clients. Have the hardware ready to install Cisco Jabber Softphone for VDI components. Documentation for Ubuntu thin clients is available from the individual hardware vendors. Documentation for Ubuntu is available
                                          from the Ubuntu website. |
| Step 4 | Configure the network. See Port Requirements . |
| Step 5 | Install the Cisco Jabber Softphone for VDI components on the thin clients and the hosted virtual desktop. See Install the Components Workflow—Ubuntu . After you install Cisco JVDI Agent and other required software on the HVD, you can clone the HVD. |

| Important | You must create CSF devices for Cisco Jabber Softphone for VDI users, and add each user to the following Access Control Groups: Standard CCM End Users Standard CTI Enabled |
|---|---|

| Step 1 | Log in to the Microsoft Windows HVD as the new user, with administration rights. |
|---|---|
| Step 2 | Join the HVD to the corporate domain. You must have domain administration rights. |
| Step 3 | Set up Citrix or VMware access to the HVDs. |
| Step 4 | Install Cisco JVDI Agent on the HVD. |
| Step 5 | Install Cisco Jabber on the HVD. See the installation guide for your release: http://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html |
| Step 6 | Clone the HVD image. For best practices for cloning Microsoft Windows HVD images, consult the documentation for your Citrix or VMware product. |

| Important | The Cisco Jabber for Windows version must match your Cisco Jabber Softphone for VDI version. The Cisco JVDI Agent and Cisco JVDI Client versions must be the same. |
|---|---|

| Step 1 | Obtain the Cisco Jabber Softphone for VDI Debian (.deb) package and cisco-jvdi<xx.x.x>-pre-reqs.xar file from HP. The <xx.x.x> variable in the filename is the Cisco Jabber Softphone for VDI release number. For assistance locating files on the HP site, contact HP support. Have the Cisco Jabber Softphone for VDI files on hand and ready to install. If you plan to manually install Cisco JVDI Client on the thin clients, copy the files to a USB stick. |
|---|---|
| Step 2 | Download the Cisco JVDI Agent . Have the Cisco JVDI Agent installation file on hand and ready to install on the hosted virtual desktop. |
| Step 3 | Have all users log out of the hosted virtual desktops. |
| Step 4 | On the thin client, install the Cisco Jabber Softphone for VDI files in the following order, either manually from a USB stick, or use HP Device Manager for mass deployments. Order of installation: Install cisco-jvdi12.0.x-pre-reqs-thinpro6.2.0-hp1d.xar. Install the Cisco Jabber Softphone for VDI .deb package. For more information about mass deployment, see the documentation for HP Device Manager 4.7, available from HP. |
| Step 5 | On the HVD, uninstall any previously installed Cisco JVDI Agent . |
| Step 6 | On the HVD, uninstall any previously installed Cisco Unified Communications clients, such as Cisco Jabber . |
| Step 7 | On the HVD, install Cisco JVDI Agent . Double-click the .msi file, and then follow the installation wizard steps. |
| Step 8 | On the HVD, install Cisco Jabber for Windows. Double-click CiscoJabberSetup.msi and follow the installation wizard steps. For detailed information about how to install
                                          Jabber for Windows, see On-Premises Deployment for Cisco Jabber for your release. For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release. Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html . |

| Important | The Cisco Jabber for Windows version must match your Cisco Jabber Softphone for VDI version. The Cisco JVDI Agent and Cisco JVDI Client versions must be the same. |
|---|---|

| Step 1 | Obtain the Cisco Jabber Softphone for VDI deb package from the Ubuntu software center repository. Have the Cisco Jabber Softphone for VDI deb package on hand and ready to install. You can place the file on a network share accessible from the thin clients, or
                                          copy it to a USB stick. |
|---|---|
| Step 2 | Download the Cisco JVDI Agent . Have the Cisco JVDI Agent installation file on hand and ready to install on the hosted virtual desktop. |
| Step 3 | Have all users log out of the hosted virtual desktops. |
| Step 4 | On the thin client, use the terminal emulator to run the following command: sudo apt-get update , and then enter your password at the prompt. Updates the list of repositories for the Ubuntu Software Center. After the command finishes reading the package lists, you can close the terminal emulator. |
| Step 5 | On the thin client, install the Cisco JVDI Client ; enter your password at the authentication prompt. When you double-click the Cisco Jabber Softphone for VDI deb package, the Ubuntu Software Center opens. After you click Install , the Ubuntu Software Center locates and installs the dependency libraries, and then installs the Cisco JVDI Client . |
| Step 6 | On the HVD, uninstall any previously installed Cisco JVDI Agent . |
| Step 7 | On the HVD, uninstall any previously installed Cisco Unified Communications clients, such as Cisco Jabber . |
| Step 8 | On the HVD, install Cisco JVDI Agent . Double-click the Cisco JVDI Agent .msi and follow the installation wizard steps. |
| Step 9 | On the HVD, install Cisco Jabber. Double-click CiscoJabberSetup.msi and follow the installation wizard steps. For detailed information about how to install
                                          Jabber for Windows, see On-Premises Deployment for Cisco Jabber for your release. For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release. Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html . |

| Step 1 | Visit the following URL: http://www.cisco.com/cisco/software/navigator.html |
|---|---|
| Step 2 | Go to Products > Unified Communications > Unified Communications Applications > Messaging > Cisco Jabber Softphone for VDI for HP Thin Pro and Ubuntu . |
| Step 3 | From the list, choose the file for your release. |
| Step 4 | Click Download or Add to cart and follow the prompts. |

| Step 1 | Visit the following URL: http://www.cisco.com/cisco/software/navigator.html |
|---|---|
| Step 2 | Go to Products > Unified Communications > Unified Communications Applications > Messaging > Cisco Jabber Softphone for VDI for HP Thin Pro and Ubuntu . |
| Step 3 | From the list, choose the file for your release. |
| Step 4 | Click Download or Add to cart and follow the prompts. |