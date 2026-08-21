---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-rel-notes-12-5-1-cucm-b-release-notes-cucm-imp-1251-cucm-b-release-note-41c0150718
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/rel_notes/12_5_1/cucm_b_release-notes-cucm-imp-1251/cucm_b_release-notes-cucm-imp-1251_chapter_011.html
retrieved_at: 2026-08-21T01:31:02.253215+00:00
---

Release Notes for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1)

# Release Notes for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1)

Updated: January 22, 2019

Chapter: About this Release

## Chapter: About this Release

# About this Release

## Introduction

These release describe new features, restrictions, and caveats for Cisco Unified Communications Manager (Unified Communications Manager) and Cisco Unified Communications Manager IM & Presence Service (IM and Presence Service) . The release notes are updated for every maintenance release but not for patches or hot fixes.

Unified Communications Manager , the call-processing component of the Cisco Unified Communications System, extends enterprise telephony features and capabilities
                           to IP phones, media processing devices, VoIP gateways, mobile devices, and multimedia applications.

IM and Presence Service collects information about user availability, such as whether users are using communications devices (for example, a phone)
                           at a particular time. IM and Presence Service can also collect information about individual user communication capabilities,
                           such as whether web collaboration or video conferencing is enabled. Applications such as Cisco Jabber and Unified Communications Manager use this information to improve productivity among employees. It helps  employees connect with colleagues more efficiently
                           and determine the most effective way to engage in collaborative communication.

In the past, export licenses, government regulations, and import restrictions have limited our supply of Unified Communications Manager and IM and Presence Service worldwide. We have obtained an unrestricted U.S. export classification to address this issue; IM and Presence Service supports an export unrestricted (XU) version only. The unrestricted version differs from previous releases of IM and Presence Service in that it does not contain strong encryption capabilities.

After you install an unrestricted release, you can never upgrade to a restricted version. You are not allowed to perform a
                                       fresh installation of a restricted version on a system that contains an unrestricted version.

## Supported Versions

The following software versions apply to Release 12.5(1):

Unified Communications Manager 12.5.1.10000-22

IM and Presence Service 12.5.1.10000-22

## Documentation for this Release

For a complete list of the documentation that is available for release 12.5(1), see the Documentation Guide for this release at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-documentation-roadmaps-list.html .

## Upgrade Procedures

For information on upgrading to Release 12.5(1), see the Upgrade and Migration Guide for Cisco Unified Communications Manager and IM and Presence Service at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html .

### Spectre/Meltdown Vulnerabilities During Upgrade

This release of Unified Communications Manager, Cisco IM and Presence Service, Cisco Emergency Responder, and Cisco Prime
                                 Collaboration Deployment contain software patches to address the Meltdown and Spectre microprocessor vulnerabilities.

Before you upgrade to Release 12.5(1) or above, we recommend that you work with your channel partner or account team to use
                                 the Cisco Collaboration Sizing Tool to compare your current deployment to an upgraded deployment. If required, change VM resources
                                 to ensure that your upgraded deployment provides the best performance.

| Note | In the past, export licenses, government regulations, and import restrictions have limited our supply of Unified Communications Manager and IM and Presence Service worldwide. We have obtained an unrestricted U.S. export classification to address this issue; IM and Presence Service supports an export unrestricted (XU) version only. The unrestricted version differs from previous releases of IM and Presence Service in that it does not contain strong encryption capabilities. After you install an unrestricted release, you can never upgrade to a restricted version. You are not allowed to perform a
                                       fresh installation of a restricted version on a system that contains an unrestricted version. |
|---|---|