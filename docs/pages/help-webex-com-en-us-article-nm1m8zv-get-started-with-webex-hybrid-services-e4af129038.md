---
doc_id: help-webex-com-en-us-article-nm1m8zv-get-started-with-webex-hybrid-services-e4af129038
source_url: https://help.webex.com/en-us/article/nm1m8zv/Get-Started-with-Webex-Hybrid-Services
retrieved_at: 2026-09-01T15:31:04.372492+00:00
---

Hybrid Services securely link your on-premises deployment with Webex. This connection lets you keep your existing deployment and make it better:

Simpler administration tasks

Easier meeting scheduling

Better calls

Better resource management

You complete a one-time deployment of each hybrid service. For Expressway-based hybrid services, when you register your environment to the cloud, a software connector is installed automatically on your equipment. For others, like directory and media, you deploy the software on a supported Windows or VM environment. The software (Expressway connectors, Video Mesh nodes, Cisco Directory Connector software) communicates securely with our service in the cloud.

Cisco Directory Connector automatically synchronizes Microsoft Active Directory users into Webex Control Hub (creating, updating, deleting) so that user account information is always current in the cloud. The Active Directory remains the single source for all user account information that is mirrored in Control Hub.

Simplify your day-to-day user administration and management tasks.

Provide accurate and up-to-date directory content for all Webex App users when they click to call, message, or to add people to meetings.

Hybrid Calendar connects your on-premises Microsoft Exchange, Office 365, hybrid Exchange, or Google Calendar deployment to Webex. This service makes it easier to schedule and join Webex meetings and Webex App meetings from your calendar client—especially for mobile users, because no extra plugins are required.

From a calendar client, in the field where meeting location is normally added, users can:

Add @webex or their Personal Room URL to automatically share the host's WebEx Personal Room and join information in the invitation.

Add @meet to automatically create a Webex App space and corresponding join link for the space. This information is shared with all meeting invitees for before, during, and after-meeting information and document sharing.

From Outlook, people can share their out-of-office status in Webex App. As soon as someone sets an automatic reply and date range, others can see the status in Webex App in these locations:

In @mentions directed at the out-of-office user.

In the People space for that user.

In search results for that user's name.

In the expanded People roster for a space.

You can use Hybrid Calling for Webex Devices to provide hybrid call
                            functionality for Room, Desk, and Cisco Webex Board devices that are
                            added to Workspaces or configured as Personal Mode devices in Control
                            Hub. Cisco Webex devices are registered to the cloud, and when they are
                            enabled with Hybrid Calling, they also connect to the enterprise. Webex
                            devices (Workspaces or Personal Mode Devices) become a part of your
                            existing on-premises dial plan, allowing these devices to call user
                            extensions or the PSTN, and receive incoming calls.

With Hybrid Calling, your users can:

Call directly from the device —Although the devices in a place are registered to the cloud, you can provide them with a line and PSTN service that is served through your Unified CM deployment. People can call these devices to join a meeting; people can also use these devices to dial other extensions or numbers.

Call from Webex App while connected to the device —From Webex App, users can also call phone numbers while connected to a cloud-registered Webex device that is enabled for Hybrid Calling. They can call someone's mobile phone number or the local pizza place directly from Webex App and have the call take place on the Webex device.

Video Mesh dynamically finds the optimal mix of on-premises and cloud conferencing resources. On-premises conferences stay on premises when there are enough local resources. When local resources are exhausted, conferences then expand to the cloud.

Video Mesh provides these benefits:

Improves quality and reduces latency by allowing you to keep your calls on premises.

Extends your calls transparently to the cloud when on-premises resources have reached their limit or are unavailable.

Manage your Video Mesh clusters from the cloud with a single interface: Control Hub ( https://admin.webex.com ).

Optimize resources and scale capacity, as needed.

Combines the features of cloud and on-premises conferencing in one seamless user experience.

Reduces capacity concerns, because the cloud is always available when additional conferencing resources are needed. No need to do capacity planning for the worst case scenario.

Provides advanced reporting on capacity and usage in https://admin.webex.com .

Uses local media processing when users dial in to a Webex meeting or Webex App meeting from on-premises standards-based SIP endpoints and clients:

SIP based endpoints and clients (Cisco endpoints, Jabber, 3rd party SIP), registered to on-premises call control (Cisco Unified Communications Manager or Expressway), that call into a Webex meeting or Webex App meeting.

Webex App app (including paired with room devices) that join a Webex meeting.

Webex room and desk devices (including Webex Board) that directly join a Webex meeting.

Provides optimized audio and video interactive voice response (IVR) to on-net SIP based endpoints and clients.

Webex clients (internal and external) continue to join meetings from the cloud.

H.323, IP dial-in, and Skype for Business (S4B) endpoints continue to join meetings from the cloud.

Supports 1080p 30fps high definition video as an option for meetings, if meeting participants that can support 1080p are hosted through the local on-premises Hybrid Media Nodes. (If a participant joins an in-progress meeting from the cloud, on-premises users continue to experience 1080p 30fps on supported endpoints.)

From day one, data security has been the primary focus in designing the Webex. The cornerstone of this security is end-to-end content encryption, enabled by Webex App clients interacting with the Key Management Service (KMS). The KMS is responsible for creating and managing the cryptographic keys that clients use to dynamically encrypt and decrypt messages and files.

By default, all Webex customers get end-to-end encryption with dynamic keys stored in the cloud KMS, Cisco's security realm. Hybrid Data Security moves the KMS and other security-related functions to your enterprise data center, so nobody but you holds the keys to your encrypted content.

Hybrid Services data sheet

Open Source in Cisco Products

Use these documents to help you plan your Hybrid Services deployments:

Things to Prepare Before You
                                                  Deploy Hybrid Services

This document lists and details prerequisite
                                                  items that may take some time to configure.
                                                  Understand these networking and security concepts
                                                  up front, so that your Hybrid Services deployment
                                                  goes smoothly.

Preferred Architecture Guides for Hybrid Services

Design Overview

Cisco Validated Design (CVD)

These
                                                  preferred architecture guides provide an overview
                                                  of Hybrid Services, as well as Cisco Validated
                                                  Design and deployment guidance for enterprises.
                                                  They contain an architecture overview that
                                                  introduces the components involved, a deeper
                                                  technical discussion of the architecture covering
                                                  the various connectors and software, how they
                                                  function, the components involved, and best
                                                  practices in deployment of the connectors.

Hybrid Services HCS Integration Reference Guide (HCS deployments only)

This
                                                  document is designed to answer the questions that
                                                  arise when you plan and implement Hybrid Services
                                                  in a Cisco HCS deployment.

The deployment guides contain overviews of each hybrid service, system requirements, prerequisites, deployment steps (including how to register nodes to the cloud), and supplementary information such as feature testing, system management, and troubleshooting steps.

## Hybrid Calendar Service

Deployment Guide for Webex Hybrid Calendar Service

## Hybrid Calling for Webex Devices

Deployment Guide for Hybrid Calling for Webex Devices (Device
                    Connector)

Hybrid Call Service on the Call Connector architecture is End of Life
                        (EOL).

## Hybrid Directory Service (Cisco Directory Connector)

Deployment Guide for Cisco Directory Connector

## Hybrid Data Security

Deployment Guide for Webex Hybrid Data Security

## Hybrid Message Service

Deployment Guide for Webex Hybrid Message Service

## Serviceability Connector

Deployment Guide for Webex Serviceability Connector

## Webex Video Mesh

Deployment Guide for Webex Video Mesh

If you encounter issues after you configure any Hybrid Services, see these articles for troubleshooting help and to better understand the known issues.

See these release notes for information about connector updates, past and present.

Manage Hybrid Services Resources

From the resource view page, you can manage the settings on your clusters that are registered to the cloud.

Add new Hybrid Services resources.

Schedule an upgrade time for connectors on your resources.

Deactivate any Hybrid Services that are hosted on a resources.

Rename the resources.

Remove the resource, if no other Hybrid Services are hosted on it.

Move a node in to maintenance mode.

Configure Email Notifications for Hybrid Services

After you set up any Hybrid Services, you and other administrators in your organization may want to receive email notifications about the service status, alarms, software upgrades, and so on.