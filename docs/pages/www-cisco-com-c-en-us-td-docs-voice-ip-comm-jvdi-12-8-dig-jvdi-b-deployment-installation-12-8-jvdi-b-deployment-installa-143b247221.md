---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-12-8-dig-jvdi-b-deployment-installation-12-8-jvdi-b-deployment-installa-143b247221
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/12_8/dig/jvdi_b_deployment-installation-12-8/jvdi_b_deployment-installation-12-8_chapter_010.html
retrieved_at: 2026-08-22T00:32:47.034239+00:00
---

Deployment and Installation Guide for Cisco Jabber Softphone for VDI Release 12.8

# Deployment and Installation Guide for Cisco Jabber Softphone for VDI Release 12.8

Updated: January 21, 2020

Chapter: Deployment Overview

## Chapter: Deployment Overview

- Deployment Overview

- Deployment Overview Workflow

# Deployment Overview

## Deployment Overview Workflow

We recommend that you read the release notes document for your platform. Review the requirements to confirm that all  hardware
                              and software meet them. Failure to meet all requirements can result in a nonfunctional deployment.

The Cisco Jabber for Windows and Cisco JVDI Agent versions must always match. We recommend that the Cisco JVDI Client version be the same, but we also support up to two releases earlier. The earlier software version of the client determines
                                          the available feature set.

You must install both Cisco JVDI Agent and Cisco JVDI Client; otherwise, the softphone fails to register.

Follow the instructions to deploy Cisco Jabber for Windows, up to the installation of the Jabber client.

You must create CSF devices for Cisco Jabber Softphone for VDI users, and add each user to the following Access Control Groups:

Standard CCM End Users

Standard CTI Enabled

Standard CTI Allow Call Recording (Required for ad-hoc recording/Built in Bridge functionality)

See On-Premises Deployment for Cisco Jabber for your release.

For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release.

Cisco Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html .

Create and set up the hosted virtual desktops in the data center.

Ensure that the hosted virtual desktops (HVD) are ready for you to install the Cisco JVDI Agent . See Set up the Hosted Virtual Desktops Workflow .

Set up and configure the thin clients.

See the documentation for the thin clients.

Install the Cisco Jabber Softphone for VDI components on the thin clients and the HVDs.

| Important | The Cisco Jabber for Windows and Cisco JVDI Agent versions must always match. We recommend that the Cisco JVDI Client version be the same, but we also support up to two releases earlier. The earlier software version of the client determines
                                          the available feature set. You must install both Cisco JVDI Agent and Cisco JVDI Client; otherwise, the softphone fails to register. |
|---|---|

| Step 1 | Follow the instructions to deploy Cisco Jabber for Windows, up to the installation of the Jabber client. Important You must create CSF devices for Cisco Jabber Softphone for VDI users, and add each user to the following Access Control Groups: Standard CCM End Users Standard CTI Enabled Standard CTI Allow Call Recording (Required for ad-hoc recording/Built in Bridge functionality) See On-Premises Deployment for Cisco Jabber for your release. For hybrid deployments, see Cloud and Hybrid Deployments for Cisco Jabber for your release. Cisco Jabber deployment guides are available from: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html . | Important | You must create CSF devices for Cisco Jabber Softphone for VDI users, and add each user to the following Access Control Groups: Standard CCM End Users Standard CTI Enabled Standard CTI Allow Call Recording (Required for ad-hoc recording/Built in Bridge functionality) |
|---|---|---|---|
| Important | You must create CSF devices for Cisco Jabber Softphone for VDI users, and add each user to the following Access Control Groups: Standard CCM End Users Standard CTI Enabled Standard CTI Allow Call Recording (Required for ad-hoc recording/Built in Bridge functionality) |
| Step 2 | Create and set up the hosted virtual desktops in the data center. Ensure that the hosted virtual desktops (HVD) are ready for you to install the Cisco JVDI Agent . See Set up the Hosted Virtual Desktops Workflow . |
| Step 3 | Set up and configure the thin clients. See the documentation for the thin clients. |
| Step 4 | Install the Cisco Jabber Softphone for VDI components on the thin clients and the HVDs. |

| Important | You must create CSF devices for Cisco Jabber Softphone for VDI users, and add each user to the following Access Control Groups: Standard CCM End Users Standard CTI Enabled Standard CTI Allow Call Recording (Required for ad-hoc recording/Built in Bridge functionality) |
|---|---|