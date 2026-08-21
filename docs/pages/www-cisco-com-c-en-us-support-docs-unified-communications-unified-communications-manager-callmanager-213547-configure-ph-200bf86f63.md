---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-213547-configure-ph-200bf86f63
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/213547-configure-phone-button-template-in-cucm.html
retrieved_at: 2026-08-21T13:57:48.050232+00:00
---

Configure Phone Button Template in CUCM

# Configure Phone Button Template in CUCM

Updated: November 21, 2018

Document ID: 213547

Contents

## Contents

## Introduction

This document describes how to configure phone button template in Cisco Unified Communications Manager (CUCM).

It contains information on Phone Button Template Configuration Settings

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of Cisco CallManager Administration.

### Components Used

The information in this document is based on Cisco CallManager 11.x and later.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

Creation and usage of templates provides a fast way to assign a common button configuration to a large number of phones. For example, if users in your company do not use the conference feature, you can create a template that reassigns this button to a different feature, such as speed dial.

Ensure that all phones have at least one line that is assigned. Normally, use button 1 for this. You can assign additional lines to a phone, depending on the Cisco Unified IP Phone model. Phones also generally have several features, such as speed dial and call forward, that are assigned to the remaining buttons.

## Phone Button Template Configuration Settings

CUCM includes default templates for each Cisco Unified IP Phone model. When phones are added, one of these templates can be assigned to the phone or a template is created. You can make changes to the custom, nonstandard templates that are created, and can change the label of the custom phone button template as well. You cannot change the function of the buttons in the default templates.

If a template for a Cisco Unified IP Phone is created, the default template for that phone can be changed during an auto-registration.

In order to create a custom phone button template, follow these steps:

Step 1. Login to Cisco Unified CM administration.

Step 2. Navigate to Device > Device Settings > Phone Button Template .

Step 3. Click Add New and select the required Phone model from the dropdown. Now click on Copy , as shown in the image.

Step 4. Modify the name of Phone Button Template and click Save .

Step 5. Modify the line configuration as per your requirement.

Phone Button Template Configuration Settings

Field

Description

Phone Button Template Information

Button Template Name

Enter a unique name that Cisco Unified Communications Manager uses to identify the template.

Button Information

Feature

Choose the function of the phone button that you want to specify in the template. The programmable line key feature provides multiple features that can be assigned to line buttons; for example, MCID, DND, Call Park, Call Pickup, and many more.

Note You cannot change the function of buttons in default phone button templates.

Label

Enter a description of the button.

Step 6. Click Save .

Step 7. Navigate to Device > Phone and locate the phone where you want to configure this Phone button template and select the template that you have just created.

Step 8.Click on Save and Reset the Phone.

## Delete Phone Button Templates

Phone templates that are not currently assigned to any phone in the system can be deleted. Template assigned to one or more devices or device profiles or the default template for a model (which is specified in the Device Defaults Configuration window) cannot be deleted.

To find out which devices use the phone button template, choose Dependency Records link from the Related Links drop-down list box in the Phone Button Template Configuration window and click on Go . If the dependency records are not enabled for the system, the dependency records summary window displays a message

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

After custom phone button template is applied, sometimes you may see the phone as partial registered.

This issue is seen when we have created more lines in the Phone Button template configuration than the actual button physical phone has.

Delete the extra lines from phone button template, it fixes the issue.

| Field | Description |
|---|---|
| Phone Button Template Information |
| Button Template Name | Enter a unique name that Cisco Unified Communications Manager uses to identify the template. |
| Button Information |
| Feature | Choose the function of the phone button that you want to specify in the template. The programmable line key feature provides multiple features that can be assigned to line buttons; for example, MCID, DND, Call Park, Call Pickup, and many more. Note You cannot change the function of buttons in default phone button templates. |
| Label | Enter a description of the button. |