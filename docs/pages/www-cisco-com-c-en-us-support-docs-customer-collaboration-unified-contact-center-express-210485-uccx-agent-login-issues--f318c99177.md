---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-contact-center-express-210485-uccx-agent-login-issues--f318c99177
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-contact-center-express/210485-uccx-agent-login-issues.html
retrieved_at: 2026-08-16T15:07:10.434605+00:00
---

Troubleshoot Agent Log in Issues

# Troubleshoot Agent Log in Issues

### Download Options

Updated: June 29, 2023

Document ID: 210485

Contents

## Contents

## Introduction

This document describes how to solve Agent log in failures on Unified Contact Center Express (UCCX) with Cisco Agent Desktop (CAD) or Finesse.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Contact Center Express (UCCX)

- Cisco Agent Desktop (CAD) or Cisco Finesse

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Problem: UCCX CAD login failure with message "Login failed due to a configuration error with your phone or jtapi or unified CM."

See Solution.

## Problem: UCCX Finesse login failure with message "The device associated with that extension or dial number is invalid."

Note : This message applies to Finesse version 11.5 and earlier.

See Solution.

## Problem: UCCX Finesse login failure with message "Device not accessible. Contact your system administrator."

Note : This message applies to Finesse version 11.6.

See Solution.

## Solution

Step 1: Ensure that the IP Contact Center (IPCC) extension is unique. The Java Telephony Application Programming Interface (JTAPI) component of UCCX does not support shared lines. Log in to Cisco Unified Communications Manager (CUCM) and check the IPCC Directory Number (DN) under Call Routing -> Route Plan Report.

While unsupported, if you have an IPCC extension shared on multiple devices and only one of them is associated to the Resource Manager Contact Manager (RMCM) user, you typically do not experience agent login issues. If you have more than one devices associated to the RMCM user, you can experience login problems, and you must do this procedure to eliminate this issue.

- Remove the shared device from the RMCM user.

- Remove the instance of the shared line from the other device.

- If you still experience problems, remove the actual agent phone from RMCM user, reset the phone and add the device back into the RMCM user.

- If problem persists, restart the Cisco Unified Contact Center Express (CCX) Engine service in a maintenance window.

Note : The RMCM user is created as a part of the UCCX post-installation process with CUCM. UCCX automatically creates this user on CUCM and all agent phones are associated to this user manually from CUCM. Any updates or changes to this user from CUCM is not supported and can lead to problems with the Cisco Unified CCX Engine Service.

Step 2: Ensure that there is only one line instance for the IPCC extension. The IPCC extension must not be a part of line group or shared.

Note : Shared line definition from CUCM perspective means that a line with the same DN can exist in different partitions. The constraints for UCCX Agent Extension is strict where the IPCC extension is not allowed on different partitions. The limitation comes from JTAPI component of UCCX and can lead to intermittent agent login issues if the extension is shared.

Step 3: Check if agents use physical phones or Extension Mobility (EM) to login to CAD or Finesse. If you use EM, then ensure that the IPCC extension is associated with the EM User Device Profile (UDP) and not to the physical phone. The EM profile needs to be associated with the RMCM user.

Step 4: Ensure that the phone or UDP contains the Common Device Configuration (CDC) set to IPV4 only. If not, create a new CDC configuration for UCCX Agents with IPV4 only and associate that with the Agent phones. Go to Device -> Device Settings -> Common Device Configuration . Click Add New .

Step 5: Ensure that IPCC extension is configured on the first four lines of the phone or UDP.

Note : Cisco Unified CCX (UCCX)/JTAPI monitors the first four configured lines on the phone or the UDP. For example, if you have line 1 and line 2 configured and the IPCC extension exists on line 6, the login would work since JTAPI monitors the first four configured lines and in this example lines 3-5 are not configured.

Step 6: Ensure that the phone models are supported with CAD and Finesse. See the Compatibility Information for Cisco Unified Contact Center .

Step 7: Ensure that Standard CTI Enabled , Standard CTI Allow Control of Phones supporting Connected Xfer and conf , and Standard CTI Allow Control of All Devices is present in the RMCM user roles. For Finesse, there are additional roles added for Monitoring and Recording: Standard CTI Allow Call Monitoring and Standard CTI Allow Call Recording.

Note : The groups and roles for the RMCM user are automatically configured by the system when the RMCM user is created initially. This step is only to ensure that these roles are present on the user.

Step 8: Ensure that the Max number of Calls and Busy Trigger on the phone or UDP is set to 2 and 1, respectively.

Step 9: Ensure that you use the Supported and Unsupported Configurations for Agent Phones and CUCM from the Release Notes .

Step 10: Ensure that CTI control is enabled on CUCM under:

- Phone Configuration page - Allow Control of Device from CTI

- End User Configuration page - Allow Control of Device from CTI

- Directory Number Configuration page for IPCC extension - Allow Control of Device from CTI

Step 11: The defect Cisco bug ID CSCvb94130 - "UCCX: Agent unable to login to Finesse after switching phones" could be applicable for intermittent issues.

Note : Only registered Cisco users have access to internal Cisco tools and information.

## Related Information

- Compatibility Information for Cisco Unified Contact Center

- Cisco Technical Support & Downloads

### Revision History

3.0

29-Jun-2023

Edited the disclaimer and Introduction. Recertification.

2.0

06-Jun-2022

Edited the disclaimer and Introduction

1.0

19-Apr-2018

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 3.0 | 29-Jun-2023 | Edited the disclaimer and Introduction. Recertification. |
| 2.0 | 06-Jun-2022 | Edited the disclaimer and Introduction |
| 1.0 | 19-Apr-2018 | Initial Release |