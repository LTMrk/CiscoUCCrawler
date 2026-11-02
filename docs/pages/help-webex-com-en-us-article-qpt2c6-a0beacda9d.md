---
doc_id: help-webex-com-en-us-article-qpt2c6-a0beacda9d
source_url: https://help.webex.com/en-us/article/qpt2c6
retrieved_at: 2026-11-02T13:06:47.036565+00:00
---

## Reset your phones on Unified CM

A factory reset removes the phone's current registration and erases all configurations and
        user data on the phone. Use this option only when troubleshooting major issues or preparing
        phones for reassignments.

Before you begin

Prepare your phone as follows:

Ensure your phone is running PhoneOS 3.5 or later.

For details on upgrading firmware, see Firmware installation (Unified CM) .

Your Unified CM (UCM) cluster must be running version 14 or a later version and with
            the appropriate device package installed.

Log in to Cisco Unified Communications Manager Administration.

Do one of the following actions as needed:

- To configure all deployed phones, go to System > Enterprise Phone Configuration .

- To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile .

- To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page.

The configuration follows a hierarchical structure:

- Individual device settings take precedence over settings in the common phone
                  profile and enterprise level

- Common phone profile settings override enterprise-level settings

Check the Perform Factory Reset option.

Click OK on the pop-up message to acknowledge the change.

Select Save .

Select Apply Config .

The phone will reboot and begin the registration process.

What to do next

- If you are troubleshooting an issue, deselect the Perform Factory
            Reset option after the reset to allow the phone to register back to UCM and
          prevent it from repeatedly resetting.

- Register Cisco Desk Phone 9800 Series

- Register Cisco Video Phone 8875

| 1 | Log in to Cisco Unified Communications Manager Administration. |
|---|---|
| 2 | Do one of the following actions as needed: To configure all deployed phones, go to System > Enterprise Phone Configuration . To configure phones sharing the same phone profile, go to Device > Device Settings > Common Phone Profile . To configure an individual phone, go to Device > Phone . Then find your phone and open the Phone Configuration page. The configuration follows a hierarchical structure: Individual device settings take precedence over settings in the common phone
                  profile and enterprise level Common phone profile settings override enterprise-level settings |
| 3 | Check the Perform Factory Reset option. |
| 4 | Click OK on the pop-up message to acknowledge the change. |
| 5 | Select Save . |
| 6 | Select Apply Config . The phone will reboot and begin the registration process. |