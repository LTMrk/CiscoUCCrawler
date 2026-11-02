---
doc_id: help-webex-com-en-us-article-17uew1-dd2ac2e8b4
source_url: https://help.webex.com/en-us/article/17uew1
retrieved_at: 2026-11-02T13:06:19.437801+00:00
---

## Configure line key labels

In Control Hub, you can choose a predefined number or name format to display as the line label for configured lines.

The configurations are also applicable for Key Expansion Module (KEM).

The following example shows the positions of the configurable line key labels:

It also supports the multiple appearances for a same line (suffixed with a -1, -2, and so on).

From the customer view in Control Hub , go to Devices , and then select your phone.

Ensure that the value of Line Label is set to default or empty.

Select Configure Lines in the Device Management section to access the Configured Lines page.

Clear the value of Line Label for the configured lines.

The parameter Line Label takes precedence over Line Key Label . If Line Label is
                configured, the phone will show the configured line label instead.

Click Save .

On the device details page, select All Configurations in the Configurations section.

In the Phone section, configure the parameters Display Name , Line Key Label , and Line Key Secondary Label .

For more information about the parameters, see Parameters for configurable line key labels on Control Hub .

Click Next , review your changes, and then click Apply .

## Parameters for configurable line key labels on Control Hub

User Phone Number / Location Number / User Extension

User Name (First Name Last Name)

Options:

- User Phone Number / Location Number / User Extension

- User Name (First Name Last Name)

- User Name (Last Name First Name)

For the option User Phone Number / Location Number / User Extension , the display priority is:

User Phone Number > Location Number > User Extension.

If  User Phone Number is empty, then the phone will display Location Number.
                  Meanwhile, if the Location Number is also empty, then the phone will display User
                  Extension.

If the actual values of "Display Name" and "Line Key Label" are identical, the secondary line label on the primary line doesn't display.

Options:

- User Extension / First Name

- User Name (First Name Last Name)

- User Name (Last Name First Name)

For the option User Extension / First Name , the display priority is:

User Extension > First Name

If  User Extension is empty, then the phone will display First Name.

If a line is configured with multiple appearances, the suffix (-1, -2, and so on) is appended to the Line Key Label.

Options:

- User Extension / First Name

- User Name (First Name Last Name)

- User Name (Last Name First Name)

- User Phone Number / Location Number / User Extension

- None

If the actual values of "Line Key Label" and "Line Key Secondary Label" are identical, the secondary label on the line key will only display the string "Line".

## Set multiple appearances for a line

You can configure multiple appearances for the same line on the phone. After the configuration, the line will appear multiple times on the phone screen, with each appearance suffixed with "-1", "-2", and so on, according to the number you specify in Control Hub.

From the customer view in Control Hub , go to Devices , and then select your phone.

On the device details page, select Configure Lines in the Device Management section.

On the Configured Lines tab, configure the parameter Appearances with a value greater than 1.

The same line will appear multiple times according to the number of the configured appearances.

The Line Key Labels appear with suffixes like -1, -2.

If you configure the Line Label with a non-default value, the configured Line Label will take precedence over Line Key Label (under Devices > All Configurations > Phone ). In this case, the suffixes (-1, -2) will be appended to the Line Label.

Click Save .

This configuration is also applicable for Key Expansion Module (KEM).

| Index | Label Name | Description |
|---|---|---|
| 1 | Display Name | For the primary line only. It shows on the top left of the phone screen. |
| 2 | Line Key Label | For any other lines (except for the primary line) on the phone with multiple lines. It's the first line when the secondary label is enabled. It also supports the multiple appearances for a same line (suffixed with a -1, -2, and so on). |
| 3 | Line Key Secondary Label | For all lines. It shows as the second line label for the primary line and line keys. |

| 1 | From the customer view in Control Hub , go to Devices , and then select your phone. |
|---|---|
| 2 | Ensure that the value of Line Label is set to default or empty. Select Configure Lines in the Device Management section to access the Configured Lines page. Clear the value of Line Label for the configured lines. The parameter Line Label takes precedence over Line Key Label . If Line Label is
                configured, the phone will show the configured line label instead. Click Save . |
| 3 | On the device details page, select All Configurations in the Configurations section. |
| 4 | In the Phone section, configure the parameters Display Name , Line Key Label , and Line Key Secondary Label . For more information about the parameters, see Parameters for configurable line key labels on Control Hub . |
| 5 | Click Next , review your changes, and then click Apply . |

| Parameter | Default and options | Description |
|---|---|---|
| Display Name | Default: User Phone Number / Location Number / User Extension User Name (First Name Last Name) Options: User Phone Number / Location Number / User Extension User Name (First Name Last Name) User Name (Last Name First Name) | For the option User Phone Number / Location Number / User Extension , the display priority is: User Phone Number > Location Number > User Extension. If  User Phone Number is empty, then the phone will display Location Number.
                  Meanwhile, if the Location Number is also empty, then the phone will display User
                  Extension. If the actual values of "Display Name" and "Line Key Label" are identical, the secondary line label on the primary line doesn't display. |
| Line Key Label | Default: User Name (First Name Last Name) Options: User Extension / First Name User Name (First Name Last Name) User Name (Last Name First Name) | For the option User Extension / First Name , the display priority is: User Extension > First Name If  User Extension is empty, then the phone will display First Name. If a line is configured with multiple appearances, the suffix (-1, -2, and so on) is appended to the Line Key Label. |
| Line Key Secondary Label | Default: User Phone Number / Location Number / User Extension Options: User Extension / First Name User Name (First Name Last Name) User Name (Last Name First Name) User Phone Number / Location Number / User Extension None | If set to None, the phone doesn't display the secondary label on the line key. In this case, only one line label displays on the phone (including the primary line on the upper left corner of the phone screen). If the actual values of "Line Key Label" and "Line Key Secondary Label" are identical, the secondary label on the line key will only display the string "Line". |

| 1 | From the customer view in Control Hub , go to Devices , and then select your phone. |
|---|---|
| 2 | On the device details page, select Configure Lines in the Device Management section. |
| 3 | On the Configured Lines tab, configure the parameter Appearances with a value greater than 1. The same line will appear multiple times according to the number of the configured appearances. The Line Key Labels appear with suffixes like -1, -2. If you configure the Line Label with a non-default value, the configured Line Label will take precedence over Line Key Label (under Devices > All Configurations > Phone ). In this case, the suffixes (-1, -2) will be appended to the Line Label. |
| 4 | Click Save . This configuration is also applicable for Key Expansion Module (KEM). |

## Figuras

![Example: Configurable line key labels on Cisco Desk Phone 9861 with multiple lines](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/489001-490000/489273.png)

![Example: Multiple appearances display for a line on Desk Phone 9871](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/490001-500000/490001-491000/490816.png)