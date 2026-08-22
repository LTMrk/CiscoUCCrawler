---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-12-5-jvdi-b-deploy-install-cisco-jvdi-elux-12-5-jvdi-b-deploy-install-c-a272cb12d0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/12_5/jvdi_b_deploy-install-cisco-jvdi-elux-12-5/jvdi_b_deploy-install-cisco-jvdi-elux-12-5_chapter_010.html
retrieved_at: 2026-08-22T00:37:07.295433+00:00
---

Deployment and Installation Guide for Cisco Jabber Softphone for VDI—Unicon eLux Release 12.5

# Deployment and Installation Guide for Cisco Jabber Softphone for VDI—Unicon eLux Release 12.5

Updated: November 29, 2018

Chapter: Installation and Deployment

## Chapter: Installation and Deployment

# Installation and Deployment

## Deployment and Installation Workflow

The Cisco Jabber for Windows version must match your Cisco Jabber Softphone for VDI version. The Cisco JVDI Agent and Cisco JVDI Client versions must be the same.

You must install both Cisco JVDI Agent and Cisco JVDI Client; otherwise, the softphone fails to register.

We recommend that you read the Release Notes for Cisco Jabber Softphone for VDI—Unicon eLux for your release. Review the requirements to confirm that all required hardware and software meet them. Failure to meet all
                              requirements can result in a nonfunctional deployment.

Follow the instructions to deploy Cisco Jabber for Windows, up to the installation of the Jabber client.

You must create CSF devices for Cisco Jabber Softphone for VDI users, and add each user to the following Access Control Groups:

Standard CCM End Users

Standard CTI Enabled

See On-Premises Deployment for Cisco Jabber for your release.

For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release.

Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html .

Create and set up the hosted virtual desktops in the data center.

Ensure that the hosted virtual desktops (HVD) are ready for you to install Cisco Jabber Softphone for VDI .

Set up and configure the thin clients. Documentation for Unicon eLux thin clients is available from the individual hardware
                                       vendors. Documentation for Unicon eLux is available from www.unicon-software.com/udocs .

Configure the network. See Port Requirements .

Install the Cisco Jabber Softphone for VDI components on the thin clients and the hosted virtual desktop. See Install the Components Workflow .

After you install Cisco JVDI Agent and other required software on the HVD, you can clone the HVD.

Use the Elias tool to create an image that contains Cisco JVDI Client . Deploy the image to the thin clients. For more information about how to create an image or how to update the thin client,
                                          see the Elias documentation available from the Unicon website.

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

The Cisco Jabber for Windows version must match your Cisco Jabber Softphone for VDI version. The Cisco JVDI Agent and Cisco JVDI Client versions must be the same.

Download the Cisco JVDI Client

Download the Cisco JVDI Agent

(Optional) Download Cisco AnyConnect

Perform this step only if users require VPN connectivity.

Have all users log out of the hosted virtual desktops.

On the thin client, install the Cisco JVDI Client . If users require VPN connectivity, deploy Cisco AnyConnect at the same time.

On the HVD, uninstall any previously installed version of Cisco VXME Agent or Cisco JVDI Agent .

On the HVD, uninstall any previously installed Cisco Unified Communications clients such as Cisco Jabber .

On the HVD, install Cisco JVDI Agent .

Double-click the MSI file and follow the installation wizard steps.

On the HVD, install Cisco Jabber for Windows.

Double-click CiscoJabberSetup.msi and follow the installation wizard steps. For detailed information about how to install
                                          Jabber for Windows, see On-Premises Deployment for Cisco Jabber for your release.

For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release.

Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html .

## Download the Cisco JVDI Client

Visit the following URL:

Go to Products > Unified Communications > Unified Communications Applications > Messaging > Cisco Jabber Softphone for VDI for Unicon eLux .

From the list, choose the file for your release.

Click Download or Add to cart and follow the prompts.

## Download the Cisco JVDI Agent

Install Cisco JVDI Agent on the hosted virtual desktops (HVD), before you install Cisco Jabber for Windows.

Visit the following URL:

Go to Products > Unified Communications > Unified Communications Applications > Messaging > Cisco Jabber Softphone for VDI for Unicon eLux .

From the list, choose the file for your release.

Click Download or Add to cart and follow the prompts.

## Download Cisco AnyConnect

The supported vpnsystem package is available from Unicon.

Visit the Unicon web site: http://www.myelux.com .

Locate and download the package.

| Important | The Cisco Jabber for Windows version must match your Cisco Jabber Softphone for VDI version. The Cisco JVDI Agent and Cisco JVDI Client versions must be the same. You must install both Cisco JVDI Agent and Cisco JVDI Client; otherwise, the softphone fails to register. |
|---|---|

| Step 1 | Follow the instructions to deploy Cisco Jabber for Windows, up to the installation of the Jabber client. Important You must create CSF devices for Cisco Jabber Softphone for VDI users, and add each user to the following Access Control Groups: Standard CCM End Users Standard CTI Enabled See On-Premises Deployment for Cisco Jabber for your release. For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release. Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html . | Important | You must create CSF devices for Cisco Jabber Softphone for VDI users, and add each user to the following Access Control Groups: Standard CCM End Users Standard CTI Enabled |
|---|---|---|---|
| Important | You must create CSF devices for Cisco Jabber Softphone for VDI users, and add each user to the following Access Control Groups: Standard CCM End Users Standard CTI Enabled |
| Step 2 | Create and set up the hosted virtual desktops in the data center. Ensure that the hosted virtual desktops (HVD) are ready for you to install Cisco Jabber Softphone for VDI . |
| Step 3 | Set up and configure the thin clients. Documentation for Unicon eLux thin clients is available from the individual hardware
                                       vendors. Documentation for Unicon eLux is available from www.unicon-software.com/udocs . |
| Step 4 | Configure the network. See Port Requirements . |
| Step 5 | Install the Cisco Jabber Softphone for VDI components on the thin clients and the hosted virtual desktop. See Install the Components Workflow . After you install Cisco JVDI Agent and other required software on the HVD, you can clone the HVD. Use the Elias tool to create an image that contains Cisco JVDI Client . Deploy the image to the thin clients. For more information about how to create an image or how to update the thin client,
                                          see the Elias documentation available from the Unicon website. |

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

| Step 1 | Download the Cisco JVDI Client |
|---|---|
| Step 2 | Download the Cisco JVDI Agent |
| Step 3 | (Optional) Download Cisco AnyConnect Perform this step only if users require VPN connectivity. |
| Step 4 | Have all users log out of the hosted virtual desktops. |
| Step 5 | On the thin client, install the Cisco JVDI Client . If users require VPN connectivity, deploy Cisco AnyConnect at the same time. |
| Step 6 | On the HVD, uninstall any previously installed version of Cisco VXME Agent or Cisco JVDI Agent . |
| Step 7 | On the HVD, uninstall any previously installed Cisco Unified Communications clients such as Cisco Jabber . |
| Step 8 | On the HVD, install Cisco JVDI Agent . Double-click the MSI file and follow the installation wizard steps. |
| Step 9 | On the HVD, install Cisco Jabber for Windows. Double-click CiscoJabberSetup.msi and follow the installation wizard steps. For detailed information about how to install
                                          Jabber for Windows, see On-Premises Deployment for Cisco Jabber for your release. For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release. Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html . |

| Step 1 | Visit the following URL: http://www.cisco.com/cisco/software/navigator.html |
|---|---|
| Step 2 | Go to Products > Unified Communications > Unified Communications Applications > Messaging > Cisco Jabber Softphone for VDI for Unicon eLux . |
| Step 3 | From the list, choose the file for your release. |
| Step 4 | Click Download or Add to cart and follow the prompts. |

| Step 1 | Visit the following URL: http://www.cisco.com/cisco/software/navigator.html |
|---|---|
| Step 2 | Go to Products > Unified Communications > Unified Communications Applications > Messaging > Cisco Jabber Softphone for VDI for Unicon eLux . |
| Step 3 | From the list, choose the file for your release. |
| Step 4 | Click Download or Add to cart and follow the prompts. |

| Step 1 | Visit the Unicon web site: http://www.myelux.com . |
|---|---|
| Step 2 | Locate and download the package. |