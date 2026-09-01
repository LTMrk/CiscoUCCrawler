---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-hcs-12-5-hcs-solution-operation-guide-chcs-b-hcs-smart-licensing-operational-096beb45e9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/hcs/12_5/HCS_Solution/Operation_Guide/chcs_b_hcs-smart-licensing-operational-guide/chcs_b_hcs-smart-licensing-operational-guide_chapter_00.html
retrieved_at: 2026-09-01T20:56:00.717953+00:00
---

Cisco Hosted Collaboration Solution Smart Licensing Operation Guide, Release 12.5

# Cisco Hosted Collaboration Solution Smart Licensing Operation Guide, Release 12.5

Updated: April 23, 2020

Chapter: Overview

## Chapter: Overview

# Overview

## About the Guide

This guide describes steps to migrate an existing partner with Flex Hosted Calling and Cisco Hosted Collaboration Solution
                           (HCS) Perpetual license Model to Smart Licensing Model.

## Audience

This guide assumes that you are familiar with the traditional commercial model with HCS Perpetual licenses. Familiarize yourself
                           with the knowledge and experience to deploy and manage the Smart Licensing for HCS.

## Overview of Smart Licensing

Smart Licensing is a cloud-based, software license management solution that enables you to automate time-consuming, manual
                           licensing tasks. The Smart Licensing solution allows you to easily track the status of your license and software usage trends.

It is a Cisco initiative to move all the licenses to the cloud. The purpose of this initiative is to simplify the license
                           management for HCS partners and enable them to adopt Cisco’s cloud-based license management system. Smart Licensing helps
                           in overcoming most of the limitations with the traditional PAK-based licenses. Most of the Cisco products including routing,
                           switching, security, collaboration, and so on supports smart licensing.

Smart Licensing in HCS depends on Cisco Smart Software Manager (CSSM), Satellite, and HCM-F. In CSSM and satellite you can activate and manage all Cisco licenses. HCM-F simplifies the complexities of registration or activation of UC Applications
                           with CSSM or Satellite , management of Smart Licenses, generate licensing reports for inventory, and billing purposes. HCM-F also provides licensing
                           dashboards for consumption details and compliance status.

PLM is not supported for UC applications cluster versions higher than 11.x. Register all the 12.x UC applications cluster
                           to CSSM.

HCM-F currently supports registration of UC Applications to Prime License Manager (PLM) for consuming the traditional PAK-based
                           licenses. UC application versions 11.x or earlier supports registration through PLM. For more information about PLM, see Cisco Hosted Collaboration Solution License Management .

Smart Licensing helps simplify three core functions:

Purchasing: The software that you have installed in your network can automatically self-register themselves, without Product Activation
                                 Keys (PAKs).

Management: You can automatically track activations against your license entitlements. Also, you do not need to install the license file
                                 on every node. You can create License Pools (logical grouping of licenses) to reflect your organization structure. Smart Licensing
                                 offers you Cisco Smart Software Manager, a centralized portal that enables you to manage all your Cisco software licenses
                                 from one centralized website.

Reporting: Through the portal, Smart Licensing offers an integrated view of the licenses you purchased and the licenses that are deployed
                                 in your network. You can use this data to make better purchase decisions, based on your consumption.

Cisco Smart Software Licensing helps you to procure, deploy, and manage licenses easily, where devices register and report
                           license consumption, removing the need for product activation keys (PAK). It Pools license entitlements in a single account
                           and allow you to move licenses freely through the network, wherever you need them. It is enabled across Cisco products and
                           managed by a direct cloud-based or mediated deployment model.

The Cisco Smart Software Licensing service registers the product instance, reports license usage, and obtains the necessary
                           authorization from Cisco Smart Software Manager and/or Satellite .

HCM-F enables the user to perform multiple tasks, such as, change the license deployment to Hosted Collaboration Solution
                           (HCS), setting the transport mode to UC Applications, create token in CSSM, register the UC applications and validate the
                           same, and so on. If there is a failure while performing the tasks, HCM-F collects the error messages from the UC application
                           or CSSM, and updates the HCM-F Job entry with the issue details.

CSSM reports at smart account-level and product level. However, user information is not available at these levels. HCM-F provides
                           the Service Inventory report and the HLM report of license usage at customer-level and virtual account level. It also provides
                           Licensing dashboards to display the usage.

You can use Smart Licensing to:

See the license usage and count.

See the status of each license type.

See the product licenses registered on Cisco Smart Software Manager and/or Cisco Smart Software Manager satellite .

Renew License Authorization with Cisco Smart Software Manager and/or Cisco Smart Software Manager satellite .

Renew the License Registration.

Deregister with Cisco Smart Software Manager and/or Cisco Smart Software Manager satellite .

The deployment option for Smart Licensing:

Manage and track licenses.

Move licenses across virtual account.

Remove registered product instance.

To track smart account-related alerts, change the preference settings, and configure email notification. Navigate to Smart Software Licensing in Cisco Smart Software Manager .

For additional information, go to https://software.cisco.com .

Connected—Used when there is connectivity to cisco.com directly from the Smart Software Manager satellite. Smart account synchronization
                                       occurs automatically.

Disconnected—Used when there is no connectivity to cisco.com from the Satellite. Smart Account synchronization must be manually
                                       uploaded and downloaded. You can specify the sync schedule in CSSM. By default, the sync with CSSM should be within 30 days.

HCM-F does not support Smart Software Manager satellite Classic Edition (CE).

| Note | HCM-F does not support Smart Software Manager satellite Classic Edition (CE). |
|---|---|