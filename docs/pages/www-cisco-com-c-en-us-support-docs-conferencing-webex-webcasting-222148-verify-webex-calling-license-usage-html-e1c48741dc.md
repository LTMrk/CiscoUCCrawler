---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-webcasting-222148-verify-webex-calling-license-usage-html-e1c48741dc
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-webcasting/222148-verify-webex-calling-license-usage.html
retrieved_at: 2026-08-21T07:15:28.112222+00:00
---

Verify Webex Calling License Usage

# Verify Webex Calling License Usage

### Download Options

Updated: July 18, 2024

Document ID: 222148

Contents

## Contents

## Introduction

This document describes how to verify that the license summary in Control Hub accurately reflects the license usage for Webex Calling services.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Webex Calling

- Webex Control Hub

### Components Used

This document is not restricted to specific hardware and software versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

Webex Control Hub is a web-based, management portal for the Webex portfolio of products. It provides a centralized platform to manage users, licenses, and devices.

Within Control Hub, the License Summary acts as a dashboard that provides a comprehensive view of the license status in the organization. It displays detailed information about the types and quantities of licenses that have been purchased, how many are currently in use, and how many remain available.

By using the License Summary in Control Hub, administrators can ensure that their Webex Calling deployment is aligned with the needs from their organization and compliance requirements.

## Overview of License Type

In order to check the overview of licenses in your organization, navigate to the License Summary section.

Step 1. Under MANAGEMENT > Account , click Subscriptions > License Summary .

Step 2. In the Calling section you can find these licenses for Webex Calling services:

- Professional license (User)

- Professional license (Workspace)

- Standard license (User only)

- Workspace license (Workspace only)

- Cisco Calling Plan license (Outbound calls)

- Webex Go (Bring Your Own Device)

- Webex Go Mobile (Mobile Operator)

- Attendant Console (Add-on for Webex Calling Professional)

## Verification Process

### Check User License Usage

In order to count the number of Standard and Professional licenses assigned in your organization, download the Comma Separated Value (CSV) file containing this information.

Step 1. Under MANAGEMENT > Users , click Manage Users > CSV add or edit .

Step 2. Click Download CSV and wait for the file to be downloaded.

Users CSV File

The downloaded CSV file can be opened with any visualizer. Depending on the visualizer the information can be presented like this. Users CSV Content Sample

In here, the first row contains the names of the different columns, and each one of the other rows represent a user in your organization.

In the first row, search for the columns that represent the Standard and Professional licenses. The Webex Calling VAR Basic [ sub-site name ] column refers to the Standard licenses, and the Webex Calling VAR Professional [ sub-site name ] column refers to the Professional licenses.

The values for these columns can be either TRUE or FALSE. A TRUE value means that the user in that row is assigned with that license.

Finally, filter each one of these columns to show only the rows containing a TRUE value. The Webex Calling VAR Basic [ sub-site name ] column is assigned the total amount of Standard license usage, and the Webex Calling VAR Professional [ sub-site name ] column is assigned the total amount of Professional license usage.

### Check Attendant Console License Usage

In order to count the number of Attendant Console licenses assigned in your organization, access the Attendant Console section and repeat this process for each one of your locations where you have users with the Attendant Console license assigned.

Step 1. Under SERVICES > Calling > Features , click the Attendant Console tab.

Step 2. Select a location in your organization.

Step 3. Review the amount of Attendant Console licenses used for this location.

Attendant Console Usage

Finally, sum the licenses assigned to each location to get the total amount of Attendant Console license usage.

### Check Workspace License Usage

In order to count the number of Professional Workspace and Workspace licenses assigned in your organization, download the CSV file containing this information.

Step 1. Under MANAGEMENT > Workspaces , click the checkbox in the first row.

Step 2. Click Export to CSV .

Workspace CSV File

The downloaded CSV file can be opened with any visualizer. Depending on the visualizer the information can be presented like this.

Workspaces CSV Content Sample

In the CSV file, the first row contains the names of the different columns, and each one of the other rows represent a workspace in your organization.

In the first row, search for the column Calling . The value of this column for Webex Calling services can be either Cisco Webex Calling Professional Workspace or Cisco Webex Calling Workspace, both of which describe the type of license assigned to the workspace in that row.

Finally, filter this column to show only the rows containing the Cisco Webex Calling Professional Workspace value, or the Cisco Webex Calling Workspace value, to get the total amount of Professional Workspace and Workspace license usage, respectively.

### Check Webex Go License Usage

In order to count the number of Webex Go licenses assigned in your organization, access the Devices page.

Step 1. Under MANAGEMENT > Devices , click the search bar > Product > Webex Go Device .

Step 2. Review the total amount of Webex Go devices to get the total amount of Webex Go license usage, as each Webex Go device uses one Webex Go license.

Webex Go Usage

### Check Webex Go Mobile License Usage

In order to count the number of Webex Go Mobile licenses assigned in your organization, access the Numbers section.

Step 1. Under SERVICES > Calling > Numbers , click the filter menu next to the search bar > Webex Mobile .

Step 2. Review the total amount of Webex Go Mobile numbers to get the total amount of Webex Go Mobile license usage, as each Webex Go Mobile number uses one Webex Go Mobile license.

Webex Go Mobile Usage

### Check Cisco Calling Plan License Usage

In order to count the number of Cisco Calling Plan licenses assigned in your organization, check the users, workspaces and virtual lines using a Cisco Calling Plan license. Then, sum all sub-totals to obtain the total Cisco Calling Plan license usage.

#### Check Users with Cisco Calling Plan

In order to count the number of users with a Cisco Calling Plan licenses assigned in your organization, generate the CSV file as described in the Check User license usage section previously described in this article.

In the CSV file, locate the column Calling Plan . The value of this column can be either TRUE or FALSE, in which TRUE means that the user in that row is assigned with the Cisco Calling Plan license.

Users CSV Cisco Calling Plan Content Sample

Finally, filter this column to show only the rows containing a TRUE value, to get the sub-total amount of Cisco Calling Plan license usage for users.

#### Check Workspaces with Cisco Calling Plan

In order to count the number of workspaces with a Cisco Calling Plan licenses assigned in your organization, access the Outgoing Call Permissions page for each workspace.

Step 1. Under MANAGEMENT > Workspaces , click the filter menu next to the search bar .

Step 2. Under CALLING , select Cisco Webex Calling .

Cisco Webex Calling Filter

Step 3. Click the Workspace > Calling .

Step 4. Scroll to Call handling > Outgoing Call Permissions .

Step 5. Check if the Cisco Calling Plan toggle is enabled. If so, the workspace is using one Cisco Calling Plan license.

Cisco Calling Plan Workspace

Step 6. Repeat steps 4 to 6 for each workspace until you get the sub-total amount of Cisco Calling Plan license usage for workspaces.

#### Check Virtual Lines with Cisco Calling Plan

In order to count the number of virtual lines with a Cisco Calling Plan licenses assigned in your organization, access the Outgoing Call Permissions page for each virtual line.

Step 1. Under SERVICES > Calling , click the Virtual Line > Calling .

Step 2. Scroll to Call handling > Outgoing Call Permissions.

Step 3. Check if the Cisco Calling Plan toggle is enabled. If so, the virtual line is using one Cisco Calling Plan license.

Cisco Calling Plan Virtual Line

Step 4. Repeat steps 2 to 4 for each virtual line until you get the sub-total amount of Cisco Calling Plan license usage for virtual lines.

## Recommended Information for a TAC Case

If you find any discrepancies between the License Summary in Control Hub and the license count process described in this article, open a case with TAC.

Cisco recommends you include this information:

- Organization ID

- A description of where the discrepancy resides

- Attach the CSV file and/or screenshots of the evidence about the discrepancies

## Related Information

### Revision History

1.0

18-Jul-2024

Initial Release

### Contributed by Cisco Engineers

Alejandro Gomez Luna

Technical Consulting Engineer

### This Document Applies to These Products

- Webex Calling

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 18-Jul-2024 | Initial Release |