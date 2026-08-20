---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-calling-220377-understand-detailed-call-history-report-h-e3ffe62bc7
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-calling/220377-understand-detailed-call-history-report.html
retrieved_at: 2026-08-20T23:21:36.387277+00:00
---

Understand Detailed Call History Report for Webex Calling

# Understand Detailed Call History Report for Webex Calling

### Download Options

Updated: April 10, 2023

Document ID: 220377

Contents

## Contents

## Introduction

This document describes a single example of a Calling Detailed Call History Report in order to understand the call flow on these reports.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Understand features such as Report templates.

- Understand clearly the call flow of the calls you intend to analyze.

- Understand Webex Calling features such as Auto Attendant and Call Queue, as well as its configuration and terminology.

### Components Used

The information in this document is based on:

- Control Hub

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

This document sets a call scenario in order to understand basic concepts on the call report for Calling Detailed Call History.

Reports help you track and analyze the performance of Webex services in your organization. You can use these reports to see details for each meeting, how often users message each other, details for Webex Calling calls and call queues, how often Webex devices are used, onboard information, and more.

For this document, you are to learn only about Webex Calling reports, specifically the Calling Detailed Call History Report.

Note: The report generated has several columns. Each column description can be read in the Calling Detailed Call History Report information .

## Call Scenario

For this article, the call flow used is an Auto Attendant with main line +12028638111. When called and option 4 is selected, the call is forwarded to a Hunt group with extension 8001, where 30 agents receive the call, and then this call can be answered by an available agent of this Hunt Group. If no one picks up, the call must go to the voicemail extension 8002.

### Call Flow

- The first leg of this call is a Public Switched Telephone Network (PSTN) number (Calling number) that calls the Webex Calling number +12028638111 that belongs to the Auto Attendant.

- Auto Attendant +12028638111 hits the Auto Attendant menu, and if option number 4 is pressed, the caller hear the IVR and is transferred to the extension 8001. This is the second leg of this call.

- If the call is unanswered, it is forwarded to the shared Voicemail on extension 8002. If this scenario is reached, this is the third call leg.

These are the legs that would make the call scenario complete.

Each of these legs have the same Correlation ID, which represents a single call.

Note: Each 1:1 call has two entries. One Originating and the one Terminating. Originating (outbound) in terms of a caller, and Terminating (inbound) for the receiver end.

### Report Rows

This report shows detailed call history data. This information can be used to view trends at a high level or drill down to specific call types, which can be used to understand call behavior.

A complete report for this call scenario throughout a month period has over one thousand entry rows.

It is because of this that it is useful to have calls filtered by Correlation ID, so you can focus and analyze just that single call.

In the next image, you can see a monthly report of this call scenario, where the highlighted section represents a single call:

You can see that a single call (you can see it if you filter the column by Correlation ID), has various rows. This can result overwhelm, furthermore in examples like this, where the call itself has different call legs and plenty agents involved.

It is important to understand that for each leg, you have two entries (rows) on the report for the terminating and the originating.

You can go back to the original scenario, where the call hits 30 agents. For this single call, you have 60 entries for each interaction of this call with every agent on the Hunt Group. The call to a Hunt Group is considered as a single call, and this one has sub-calls which are encapsulated inside the call to the Hunt Group.

## Call Flow on the Report

Based on the example given, this is a portion of the report generated for the Detailed Call history report.

Note: The columns shown are an object of interest for the analysis presented here. There are more columns in reports which can be of interest in your own scenario.

The first field - highlighted in yellow - is the entry for the first leg, when the PSTN (such as Verizon) number +15152905490 hits the Hunt Group +12028638111. You can confirm this if you check the User type column in the report. The value AutomatedAttendantVideo indicates an Auto Attendant.

As you can see, on the second row, the Auto Attendant calls the Hunt Group (extension 8001) - this is highlighted in brown - and the Hunt Group then calls the first agent - this is highlighted in green - (Bruce Wayne with extension 2001). The originating entry indicates this call. Similarly, the terminating entry for the same leg. This is a call between the Hunt Group and the first agent, which generates an originating and terminating entry. The call is not picked up by Bruce Wayne (you can see this on the Answered column, which for this leg, is set to FALSE.

The call then moves towards the next agent based on the routing pattern and reaches extension 3010 - highlighted in blue, and as you can see Diana Prince does not pick up the call either. The call moves towards the next agent and so on.

This continues to extension 5002, which belongs to Thanos - highlighted in black - who picks up the call and establishes the call with the PSTN caller.

Note: The report is based in UTC time zone for standardization across time zones and it is not possible to render data in another time zone.

## Related Information

- Reports for Your Cloud Collaboration Portfolio

### Revision History

1.0

10-Apr-2023

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 10-Apr-2023 | Initial Release |