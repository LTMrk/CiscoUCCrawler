---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-push-notifications-cucm-b-push-notifications-deployment-guide-cucm-b-pu-f97c69eac3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/push_notifications/cucm_b_push-notifications-deployment-guide/cucm_b_push-notifications-deployment-guide_chapter_00.html
retrieved_at: 2026-08-16T16:07:31.051836+00:00
---

Push Notifications Deployment Guide

# Push Notifications Deployment Guide

Updated: August 20, 2024

Chapter: Preface

## Chapter: Preface

- Preface

- Purpose of this Document

- Apple Push Notification Service Upgrade Requirements

# Preface

## Purpose of this Document

This document describes how to configure Push Notifications on Cisco Unified Communications Manager and the IM and Presence
                              Service for compatible Cisco Jabber and Cisco Webex clients that run on iOS or Android devices. With Push Notifications, your
                              deployment uses Google or Apple's cloud-based Push Notification service to push voice call, video call, and instant message notifications to Cisco Jabber and Cisco Webex for iOS and Android clients that are running in the background.
                              You must enable Push Notifications to maintain persistent communication with clients that are running in the backgound.

This document describes how to enable Push Notifications for the following deployment types:

On-Premise Deployments of Cisco Unified Communications Manager and the IM and Presence Service —For on-premises deployments of Cisco Unified Communications Manager and the IM and Presence Service, refer to Chapter 2 for
                                    instructions on how to enable the cluster for Push Notifications. This includes deployments where the clients register via
                                    Expressway's Mobile and Remote Access (MRA) feature.

Cloud Deployments with Webex Messenger —For cloud deployments with Webex Messenger, refer to Chapter 3 for deployment requirements.

## Apple Push Notification Service Upgrade Requirements

In alignment with Apple's changes to the iOS notification architecture, Cisco Jabber and Cisco Webex clients on iOS are implementing
                              Apple Push Notification support for notifications. We highly recommend that customers upgrade Cisco Unified Communications Manager , IM and Presence Service , Cisco Expressway, Cisco Jabber, and Cisco Webex as soon as possible. Failure to upgrade on time will result in loss of voice
                              notification for Cisco Webex users using Unified Communications Manager and IM notifications for Cisco Jabber and Cisco Webex
                              iOS users.

Important

If Apple Push Notification Service (APNS) is enabled on the CUCM/IM and Presence clusters and if the Expressway is upgraded
                                          to a version that supports Push:3 protocol, first upgrade all CUCM/IM and Presence clusters to the version that supports push:3
                                          protocol.

This means that if your existing CUCM/IM and Presence version is 11.5(1)SU8 or 12.5(1)SU3 or below (that supports Push:2),
                                          however you have upgraded the Expressway to 12.7 (that supports Push:3), the APNS will not work in such deployment scenario.
                                          In such case, you must upgrade your CUCM/IM and Presence cluster to a version that supports Push:3, such as 11.5(1)SU9.

Apple Push Notification Service needs HTTPS and will not work with unrestricted software.

For up to date support information that is related to Push Notifications with iOS13 and above versions, including upgrade
                              requirements, refer to Apple Push Notification Service Updates .

| Note | The Webex Messenger cloud retires end of 2020. For more information, see https://blogs.cisco.com/collaboration/making-the-move-to-modern-messaging . |
|---|---|

| Important | If Apple Push Notification Service (APNS) is enabled on the CUCM/IM and Presence clusters and if the Expressway is upgraded
                                          to a version that supports Push:3 protocol, first upgrade all CUCM/IM and Presence clusters to the version that supports push:3
                                          protocol. This means that if your existing CUCM/IM and Presence version is 11.5(1)SU8 or 12.5(1)SU3 or below (that supports Push:2),
                                          however you have upgraded the Expressway to 12.7 (that supports Push:3), the APNS will not work in such deployment scenario.
                                          In such case, you must upgrade your CUCM/IM and Presence cluster to a version that supports Push:3, such as 11.5(1)SU9. Apple Push Notification Service needs HTTPS and will not work with unrestricted software. |
|---|---|