---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-800-series-adminguide-w800-b-wireless-800-administration-guide-w800-m-83d647a51b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/800-series/adminguide/w800_b_wireless-800-administration-guide/w800_m_maintenance.html
retrieved_at: 2026-08-21T09:58:48.275159+00:00
---

Cisco Wireless Phone 840 and 860 Administration Guide for Cisco Unified Communications Manager

# Cisco Wireless Phone 840 and 860 Administration Guide for Cisco Unified Communications Manager

Updated: August 13, 2026

Chapter: Maintenance

## Chapter: Maintenance

# Maintenance

## Reboot the phone

At times, you may need to manually reboot the phone.

Step 1

Press and hold the Power button.

Step 2

Tap Restart .

## Factory default settings

If necessary, you can restore the factory default settings of the phone.

If you perform a factory reset, the phone software stays on the latest installed version.

We recommend that you enroll your phones through an Enterprise Mobility Management (EMM) application so that you are the Device Owner and you can factory reset the phones through the EMM application .

However, if you do not enroll the phones in an EMM application , you can restore a phone to the factory defaults using the following methods:

If you're able to boot the phone, use the phone Settings method.

If you're not able to boot the phone, use the recovery mode method.

### Reset to factory default through the phone settings

If the phone is not enrolled in an Enterprise Mobility Management (EMM) application , you can restore the factory default settings of the phone through the Settings on the phone.

Caution

If the phone has a Google account or other device ownership, then it has factory wipe protection which prevents the wipe of
                                             certain account details. You must have the Google account information to access the phone after you restore factory defaults.

Step 1

Access the Settings app.

Step 2

Tap System .

Step 3

Select Advanced > Reset options .

Step 4

Tap Erase all data (factory reset) .

Step 5

Tap Erase all data .

Step 6

Tap Erase all data .

### Restore to factory default through recovery mode

You can restore the factory default settings of the phone through recovery mode. However, it is best to follow these steps
                                 as a last resort and only if:

The phone is not enrolled in an Enterprise Mobility Management (EMM) application .

You can't boot the phone to access the Settings .

The phone user has not signed in to a unique Google account.

Caution

If you use recovery mode to reset the factory defaults of a phone that had been signed in to a unique Google account, you
                                             will need the Google account and password. You must work with the phone user, Google account owner, and Google to reset the
                                             phone.

Step 1

Press and hold the Power button.

Step 2

Tap Power off .

Step 3

Press and hold the red Emergency button and press hold the Power button until the phone vibrates, then release the Power button. Continue to hold the Emergency button.

Step 4

Once the bootloader screen is displayed, release the red Emergency button.

Step 5

Press the Volume down button until Recovery mode displays.

Step 6

Press the Power button to select Recovery mode .

Step 7

Press and hold the Power button, then quickly press and release the Volume up button to enter the Recovery Menu screen.

Step 8

When the Recovery Menu displays, release the Power button.

Step 9

Press the Volume down button to highlight Wipe data/factory reset .

Step 10

Press the Power button to select Wipe data/factory reset .

Step 11

Press the Volume down button to highlight Factory data reset .

Step 12

Press the Power button to select Factory data reset .

Step 13

When Reboot system now is highlighted, press the Power button.

## Cisco app software updates

To upgrade the Cisco app software, use one of these methods:

Install the latest signed software COP file to the Cisco Unified
                                       				Communications Manager .

After you upload the COP file, the phone prompts the user to reboot and apply the new software, unless you enabled the Reboot immediately after downloading software updates option in the Product Specific Configuration Layout pane.

Copy the extracted firmware ZIP files contents to the HTTP (port 6970)  load server defined in the Product Specific Configuration Layout pane. Then, update the device default or individual phone load within Cisco Unified
                                       				Communications Manager , so that the phone upgrades after it is restarted.

| Step 1 | Press and hold the Power button. |
|---|---|
| Step 2 | Tap Restart . |

| Note | If you perform a factory reset, the phone software stays on the latest installed version. |
|---|---|

| Caution | If the phone has a Google account or other device ownership, then it has factory wipe protection which prevents the wipe of
                                             certain account details. You must have the Google account information to access the phone after you restore factory defaults. |
|---|---|

| Step 1 | Access the Settings app. |
|---|---|
| Step 2 | Tap System . |
| Step 3 | Select Advanced > Reset options . |
| Step 4 | Tap Erase all data (factory reset) . |
| Step 5 | Tap Erase all data . |
| Step 6 | Tap Erase all data . |

| Caution | If you use recovery mode to reset the factory defaults of a phone that had been signed in to a unique Google account, you
                                             will need the Google account and password. You must work with the phone user, Google account owner, and Google to reset the
                                             phone. |
|---|---|

| Step 1 | Press and hold the Power button. |
|---|---|
| Step 2 | Tap Power off . |
| Step 3 | Press and hold the red Emergency button and press hold the Power button until the phone vibrates, then release the Power button. Continue to hold the Emergency button. |
| Step 4 | Once the bootloader screen is displayed, release the red Emergency button. |
| Step 5 | Press the Volume down button until Recovery mode displays. |
| Step 6 | Press the Power button to select Recovery mode . The phone restarts and returns to a new screen that displays the Android icon. |
| Step 7 | Press and hold the Power button, then quickly press and release the Volume up button to enter the Recovery Menu screen. |
| Step 8 | When the Recovery Menu displays, release the Power button. |
| Step 9 | Press the Volume down button to highlight Wipe data/factory reset . |
| Step 10 | Press the Power button to select Wipe data/factory reset . |
| Step 11 | Press the Volume down button to highlight Factory data reset . |
| Step 12 | Press the Power button to select Factory data reset . |
| Step 13 | When Reboot system now is highlighted, press the Power button. |

| Note | After you upload the COP file, the phone prompts the user to reboot and apply the new software, unless you enabled the Reboot immediately after downloading software updates option in the Product Specific Configuration Layout pane. |
|---|---|