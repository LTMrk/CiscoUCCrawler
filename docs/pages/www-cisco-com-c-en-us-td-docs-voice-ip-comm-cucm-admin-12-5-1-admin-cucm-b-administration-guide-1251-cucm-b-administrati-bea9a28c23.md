---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-admin-cucm-b-administration-guide-1251-cucm-b-administrati-bea9a28c23
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/admin/cucm_b_administration-guide-1251/cucm_b_administration-guide-1251_chapter_01100.html
retrieved_at: 2026-08-21T01:08:35.488416+00:00
---

Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: April 8, 2025

Chapter: Manage Enterprise Parameters

## Chapter: Manage Enterprise Parameters

# Manage Enterprise Parameters

## Enterprise Parameters Overview

Enterprise parameters provide default settings that apply to all
                           devices and services across the entire cluster. For example, your system uses the enterprise parameters to
                           set the initial values of its device defaults.

You cannot add or delete
                           enterprise parameters, but you can update existing enterprise
                           parameters.  The configuration window lists enterprise
                           parameters under categories; for example, CCMAdmin parameters, CCMUser
                           parameters, and CDR parameters.

You can view detailed descriptions for enterprise parameters on the Enterprise Parameters Configuration window.

Caution

Many of the enterprise parameters do not require changes. Do not change an enterprise parameter unless you fully understand
                                       the feature that you are changing or unless the Cisco Technical Assistance Center (TAC) advises you on the change.

### View Enterprise Parameter Information

Access information about
                                 				enterprise parameters through embedded content in the Enterprise Parameter Configuration window.

Step 1

From Cisco Unified CM Administration, choose System > Enterprise Parameters .

Step 2

Perform one of the following tasks:

- To view the description of a particular enterprise parameter, click the parameter name.

- To view the descriptions of all the enterprise parameters, click ? .

### Update Enterprise
                           	 Parameters

Use this procedure to open
                                 				the Enterprise Parameter Configuration window and
                                 				configure system-level settings.

Caution

Many of the enterprise parameters do not require changes. Do not change an enterprise parameter unless you fully understand
                                             the feature that you are changing or unless the Cisco Technical Assistance Center (TAC) advises you on the change.

Step 1

From Cisco
                                          			 Unified CM Administration, choose System > Enterprise
                                                				  Parameters .

Step 2

Choose the
                                          			 desired values for the enterprise parameters that you want to change.

Step 3

Click Save .

#### What to do next

Apply Configuration to Devices

### Apply Configuration to Devices

Use this procedure to update all affected devices in the cluster
                                 				with the settings you configured.

#### Before you begin

Update Enterprise Parameters

Step 1

From Cisco Unified CM Administration, choose System > Enterprise Parameters .

Step 2

Verify your changes, and then click Save .

Step 3

Choose one of the following options:

- Click Apply Config if you want your system to determine which devices to reboot. In some cases, a device may not need a reboot.  Calls in progress
                                             may be dropped but connected calls will be preserved unless the device pool includes SIP trunks.

- Click Reset if you want to reboot all devices in your cluster. We recommend that you perform this step during off-peak hours.

Step 4

After you read the confirmation dialog, click OK .

### Restore Default Enterprise Parameters

Use this procedure if you
                                 				want to reset the enterprise parameters to the default settings. Some
                                 				enterprise parameters contain suggested values, as shown in the column on the
                                 				configuration window; this procedure uses these values as the default settings.

Step 1

From Cisco Unified CM Administration, choose System > Enterprise Parameters .

Step 2

Click Set to Default .

Step 3

After you read the confirmation prompt, click OK .

| Caution | Many of the enterprise parameters do not require changes. Do not change an enterprise parameter unless you fully understand
                                       the feature that you are changing or unless the Cisco Technical Assistance Center (TAC) advises you on the change. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose System > Enterprise Parameters . |
|---|---|
| Step 2 | Perform one of the following tasks: To view the description of a particular enterprise parameter, click the parameter name. To view the descriptions of all the enterprise parameters, click ? . |

| Caution | Many of the enterprise parameters do not require changes. Do not change an enterprise parameter unless you fully understand
                                             the feature that you are changing or unless the Cisco Technical Assistance Center (TAC) advises you on the change. |
|---|---|

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose System > Enterprise
                                                				  Parameters . |
|---|---|
| Step 2 | Choose the
                                          			 desired values for the enterprise parameters that you want to change. |
| Step 3 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Enterprise Parameters . |
|---|---|
| Step 2 | Verify your changes, and then click Save . |
| Step 3 | Choose one of the following options: Click Apply Config if you want your system to determine which devices to reboot. In some cases, a device may not need a reboot.  Calls in progress
                                             may be dropped but connected calls will be preserved unless the device pool includes SIP trunks. Click Reset if you want to reboot all devices in your cluster. We recommend that you perform this step during off-peak hours. |
| Step 4 | After you read the confirmation dialog, click OK . |

| Step 1 | From Cisco Unified CM Administration, choose System > Enterprise Parameters . |
|---|---|
| Step 2 | Click Set to Default . |
| Step 3 | After you read the confirmation prompt, click OK . |