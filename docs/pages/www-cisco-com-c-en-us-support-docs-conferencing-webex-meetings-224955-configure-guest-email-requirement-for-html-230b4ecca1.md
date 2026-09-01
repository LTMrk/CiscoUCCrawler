---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-meetings-224955-configure-guest-email-requirement-for-html-230b4ecca1
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-meetings/224955-configure-guest-email-requirement-for.html
retrieved_at: 2026-09-01T14:56:24.956290+00:00
---

Configure Guest Email Requirement for Webex Meetings

# Configure Guest Email Requirement for Webex Meetings

### Download Options

Updated: October 10, 2025

Document ID: 224955

Contents

## Contents

## Introduction

This document describes how to enforce email entry for guests before they can join meetings on a specific Webex site.

## Prerequisites

### Requirements

Full administrator access to Control Hub.

### Components Used

The information in this document does not require specific hardware or software.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configuration

### Step 1. Sign in to Control Hub

Navigate to admin.webex.com and sign in with an administrator account.

### Step 2. Select the Meetings Site

- From Services , select Meeting .

Select the Select the Meetings site you want to enforce this rule to.

### Step 3. Navigate to Security Settings

- Click Common Settings tab.

Then, click Security .

### Step 4. Enable the Option To Require Email Address From Guests

- Scroll down to Other section.

Enable the Email Address option.

Click Save .

### Step 5. Refresh Settings

Ask the user to sign out of the Webex application (desktop, mobile, or web) and sign back in to implement the changes.

## Verification

Schedule a test meeting on the selected site.

Confirm by joining as a guest or checking the participant report for guest email enforcement.

### Revision History

2.0

10-Oct-2025

Initial Release

1.0

09-Oct-2025

Initial Release

### Contributed by Cisco Engineers

Mohammad Bakir

Technical Consulting Engineer

### This Document Applies to These Products

- WebEx Meetings

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 10-Oct-2025 | Initial Release |
| 1.0 | 09-Oct-2025 | Initial Release |