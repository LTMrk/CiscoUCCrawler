---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-server-213816-troubleshoot-cisco-meeting-server-cms-html-ff9d01ce4f
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/213816-troubleshoot-cisco-meeting-server-cms.html
retrieved_at: 2026-08-16T14:22:27.369362+00:00
---

Troubleshoot Cisco Meeting Server (CMS) 2.0.3 Message Board Chat Disabled by Default For New Installation

# Troubleshoot Cisco Meeting Server (CMS) 2.0.3 Message Board Chat Disabled by Default For New Installation

Log in to Save Content

### Download Options

Updated: October 11, 2018

Document ID: 213816

Contents

## Contents

## Introduction

This document describes the problem of Message Board chat disabled by default in CMS version 2.0.3 and onwards.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Meeting Server (CMS) - version 2.0.3 and onwards

- Cisco Meeting Apps (any versions used with CMS 2.0.3 and later)

### Components Used

The information in this document is based on these software and hardware versions:

- Cisco Meeting Server (CMS) - version 2.0.3 and onwards

- Cisco Meeting Apps (any versions used with CMS 2.0.3 and later)

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Problem: Message Board Chat is not Enabled By Default

From CMS Version 2.0.3, Message-Board chat is no longer enabled by default for new installs. This affects chat in space message boards. Chat in point-to-point calls remain unaffected.  This is an intentional change and the release notes for CMS 2.0.3 clearly explains this new change. If you install CMS 2.0.3 (or later) and found that message-board chat is no longer enabled by default on the server. This does not affect you if you upgrade from a previous version of CMS to 2.0.3 (or later), and had previously used the message board chat functionality. For such cases, the message board chat remains enabled. However, if you upgrade from a previous version to 2.0.3 (or later), but had never used the message board chat functionality, then upgrade disables message board chat.

## Solution

Section 2.7 of CMS 2.0.3 release notes explains the feature. In order to use the message board chat feature in Cisco Meeting Apps, you can enable it via the Application Programming Interface (API). The setting is retained after upgrade as well. In order to enable chat in message boards, use the API to create a callProfile with parameter messageBoardEnabled set to True . Set this callProfile as the Default Global Profile to be used for all calls after you copy the callProfile id and use an HTTP PUT towards this API path: /api/v1/system/profiles .

## Related Information

- Technical Support & Documentation - Cisco Systems

### Contributed by Cisco Engineers

Sateesh Katukam

Cisco TAC Engineer

### Contact Cisco

- Open a Support Case

- (Requires a Cisco Service Contract )

### This Document Applies to These Products

- Meeting Server