---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-213294-configure-cu-69dd310f78
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/213294-configure-custom-alert-in-cisco-real-tim.html
retrieved_at: 2026-08-21T13:57:05.986217+00:00
---

Configure Custom Alert in Cisco Real Time Monitoring Tool

# Configure Custom Alert in Cisco Real Time Monitoring Tool

Updated: April 28, 2018

Document ID: 213294

Contents

## Contents

## Introduction

This document describes how to configure customer alert in Cisco Real Time Monitoring Tool (RTMT). Contributed by Sankalp Jain, TAC Engineer.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Call Manager (CUCM)

- RTMT

### Components Used

The information in this document is based on the RTMT version 11.5. The information in this document was created from devices and applications in a specific lab environment. All of the devices and applications used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any action.

## Background Information

Alert central section on RTMT organises the alerts under different tabs such as System, Voice/Video, and Custom. Under System and Voice/Video. Pre-configured alerts are found that cannot be deleted but can still be disabled or modified. The customs tab is empty by default and administrator can configure any required alert based on counters available under the performance section of the RTMT.

## Configure

1. On the RTMT, navigate to System > Performance > Open Performance Monitoring as shown in the image.

2. Select the node for which the alert needs to be configured as shown in the image.

3. Select the specific device, endpoint, process or feature for wich the alert needs to be configured and expand it.

Right click on the specific counter and select Counter Monitoring or Counter Instance depending upon the counter.

4. Select the instance from the list of object instances.

5. The specific instance/counter will now be visible on the right side panel.

Right click on the instance and select Set Alert/Properties.

5. Select the Enable Alert checkbox, specify the severity and then click Next .

6: Specify the frequency and schedule and then click Next .

7: Enable email alert (if required) and specify the email address in order to receive alerts.

Once done click on Save .

## Verify

Use this section in order to confirm that your configuration works properly.

Once the custom is configured it will be visible under Custom in Alert Central on RTMT.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.