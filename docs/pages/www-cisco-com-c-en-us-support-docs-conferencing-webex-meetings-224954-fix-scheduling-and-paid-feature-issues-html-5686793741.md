---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-meetings-224954-fix-scheduling-and-paid-feature-issues-html-5686793741
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-meetings/224954-fix-scheduling-and-paid-feature-issues.html
retrieved_at: 2026-09-01T14:56:58.619166+00:00
---

Fix Scheduling and Paid Feature Issues after Activation (.My)

# Fix Scheduling and Paid Feature Issues after Activation (.My)

### Download Options

Updated: September 18, 2025

Document ID: 224954

Contents

## Contents

## Introduction

This document describes cases where users cannot schedule or use paid features right after subscription purchase or reactivation.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics.

Full administrator access to Control Hub.

### Components Used

The information in this document does not require specific hardware or software.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Cause

Required session types (site features) are not enabled for the user on the correct Webex Meetings site.

## Resolution

### Step 1. Sign in to Control Hub

Navigate to admin.webex.com and sign in with an administrator account.

### Step 2. Open the User Record

- Navigate to Management > Users .

- Select the affected user . Control Hub (Users)

### Step 3. Select the Meetings Site

- Open the Meetings tab in the user's profile.

- In the Settings apply to drop-down menu, choose the relevant Webex site (for example: yourcompany.my.webex.com).

### Step 4. Enable Required Session Types

- Ensure the appropriate types are enabled for the user (for example: Webex Meetings / paid entitlements).

- Click Save . Control Hub (Meeting Session Types)

### Step 5. Refresh User Entitlements

Ask the user to sign out of the Webex application (desktop, mobile, or web) and sign back in to refresh their permissions.

## Verification

Have the user schedule a test meeting on the selected site.

Confirm that scheduling is available and that meeting duration aligns with the paid plan (no 40-minute limit, if applicable).

## If the Issue Persists

In the user’s profile, confirm that the correct Meetings license is assigned.

Re-check Settings apply to to ensure changes were made on the intended site.

Toggle the affected session type(s) off > Save > on > Save to force an update.

If your process allows, remove and reassign the Meetings license from the user’s Summary tab.

### Revision History

1.0

18-Sep-2025

Initial Release

### Contributed by Cisco Engineers

Mohammad Bakir

Technical Consulting Engineer

### This Document Applies to These Products

- WebEx Meetings

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 18-Sep-2025 | Initial Release |