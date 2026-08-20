---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-control-hub-220198-configure-business-texting-for-webex-cal-html-95d993a7d7
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-control-hub/220198-configure-business-texting-for-webex-cal.html
retrieved_at: 2026-08-20T21:12:40.500807+00:00
---

Configure Business Texting for Webex Calling Organization

# Configure Business Texting for Webex Calling Organization

### Download Options

Updated: February 15, 2023

Document ID: 220198

Contents

## Contents

## Introduction

This document describes the configuration of Business Texting for Webex Calling Organizations that support this feature.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Control Hub administration of Service Features for the Webex Calling Organization

- Control Hub administration of User Calling Feature for the Webex Calling Organization

- Webex App

### Components Used

There are no specific requirements for this document.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configure

### Requirements and Limitations

- Webex Calling professional license

- Cisco Calling Plans (US and Canada)

- Primary telephone number assigned to the user

- Windows and MAC OS Webex App 42.12 or later

- Apple and Android Webex App 43.2 or later (tentative Feb 2023)

- Online organizations CANNOT enable Business Texting

- There is a limitation of 6 messages/min from each number for outgoing messages. If delivery is delayed it can be one of the causes of slowness.

- Business Texting does not include Phase 4 Federation migration support

### Configurations

Business Texting Organization Configuration in Control Hub

This is how an administrator can enable Business Texting for all Webex Calling users from Control Hub.

Step 1. Navigate to Calling > Service Settings > Scroll to Business texting provisioning.

You can allow any Business Texting capable user to send and receive text through webex app.

Step 2. Turn on Enable Business Texting for all the users at locations with business texting capabilities.

Accept the Enable Business Texting popup.

To disable, Turn off Enable Business Texting for all users at locations with Business Texting capabilities.

Click on the Disable Business Texting button to accept the information in the Disable Business Texting popup.

Business Texting User Configuration in Control Hub

How to provision Business Texting for a user in Control Hub.

Step 1. Navigate to Users > Select User > Calling tab > Business Texting section.

- By default it is set to Use the default configuration for the organization.

- In this case Business Texting is enabled at the Organization level.

Step 2. To Override default Organization configuration, choose Override settings.

- You can disable or enable Business Texting for this particular User within the organization.

- Click save to accept disablement of Business Texting to override the default organization configuration.

Click save to accept the enablement of Business texting to override the default organization configuration.

To return to the default configuration for the organization, choose Use the organization default configuration.

## Verify

Step 1. Verify that Send a text message option is available on webex app on PC.

Step 2. Enter the mobile telephone number in E.164 format to Send a text message.

Note : The mobile telephone number must be in E.164 format: +1 followed by 10 digit Telephone number, such as +12223334444; otherwise, the call fails.

Step 3. Write a text.

Write a text to, for example, +12223334444, to verify Business Texting works.

## Troubleshoot

Business Texting Organization Configuration in Control Hub

Scenarios when administrator cannot enable Business Texting at Organization configuration in Control Hub:

- Enable Business Texting button not available.

- Instead the error message "This organization is not eligible for texting capabilities" is displayed.

- Click Learn more to learn more about all of the pre-requisite to enable Business Texting.

Three Scenarios where the administrator cannot enable Business Texting.

Scenario 1: Must have Cisco Calling Plan in the US or Canada.

There are no users assigned to any US or Canada Locations with US or Canada Cisco Public Switched Telephone Network (PSTN) Provider.

Scenario 2: Data spanning multiple regions.

If your data is in different non-supported regions, you need to open a TAC Case for data migration to resolve this.

Scenario 3: The feature is only available to enterprise organizations.

Online organizations are currently not eligible to use Business Texting.

For all three of these scenarios, the error message "The organization is not eligible for texting capabilities" is visible at Calling > Service Settings for Business texting provisioning.

Business Texting User Configuration in Control Hub

Five possible error or warning scenarios for users where Business Texting provisioning is disabled.

Scenario 1: User Assigned to a Location with Local Gateway PSTN Connection and not Cisco PSTN Provider.

Click on Learn more to learn about all of the prerequisites.

Scenario 2: User Assigned to a Location with Cisco PSTN provider but not in the US or Canada.

In this case, it is the Cisco PSTN Provider in the UK.

Scenario 3: The User has a primary number assigned but this number does not support Business Texting from the carrier.

- Error message "Your primary number does not support texting. Select another number to enable texting" is displayed.

- Assign a number that has texting capabilities to resolve this. Or, you can open a TAC case to determine why this number does not support texting.

Scenario 4: The User is assigned to a Location with Cisco PSTN US or Canada provider but no primary number is assigned.

- Error message "User is not eligible for texting capabilities because there is no primary telephone number found" is displayed.

- To resolve, click on Primary Number and assign a primary number with texting capability.

- Go back to the Calling tab to verify error no longer shows.

Scenario 5: This feature is only available for Enterprise organizations.

- Online organizations are currently not eligible to use Business Texting.

- Error Message "User is not eligible for texting capability" is displayed in the Business texting section of the Calling tab.

### Revision History

2.0

15-Feb-2023

Initial Release

1.0

02-Feb-2023

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 15-Feb-2023 | Initial Release |
| 1.0 | 02-Feb-2023 | Initial Release |