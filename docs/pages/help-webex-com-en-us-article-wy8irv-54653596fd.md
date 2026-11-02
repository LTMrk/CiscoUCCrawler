---
doc_id: help-webex-com-en-us-article-wy8irv-54653596fd
source_url: https://help.webex.com/en-us/article/wy8irv
retrieved_at: 2026-11-02T13:05:21.892547+00:00
---

## Overview

ThousandEyes Agent integration for phones supports the following models:

### Supported features

On ThousandEyes portal, you can view the following information related to phones:

- Scheduled tests

- Dynamic tests for Webex meetings via hybrid calendar

- Dynamic tests for SIP calls

- Local networks

### Limitations

- Network path isn't available for ICE-optimized calls.

- Phone Wi-Fi stats aren't available on the ThousandEyes portal.

- Supports only synthetic tests for SIP calls to STUN servers.

- Real user tests are not supported for phones.

## Enable ThousandEyes for your organization

When you enable ThousandEyes Agent integration at the organization level, any devices that are ThousandEyes-enabled and added to the organization will automatically integrate with ThousandEyes.

The setting at the organization level will default to the locations and devices within the organization. You can also modify location-specific or device-specific settings later, without affecting the other locations or devices.

Before you begin

Get ThousandEyes Endpoint Agent licenses (either essential or advantage) You need one endpoint license per device.

Get the connection string from the ThousandEyes application.

From the customer view in Control Hub , go to Devices > Settings .

Scroll down to the ThousandEyes section and toggle on Enable ThousandEyes Agent .

Click Add and paste the connection string that you copied from ThousandEyes portal.

If you don't want to integrate all devices, leave the connection string field empty and enter it in the device-level settings instead.

Click Save in the popup window.

## Enable ThousandEyes for a location

When the ThousandEyes Agent is enabled at the location level, any new devices added later will automatically have the ThousandEyes Agent activated.

Before you begin

Get ThousandEyes Endpoint Agent licenses (either essential or advantage). You need one endpoint license per device.

Get the account group token and connection string from the ThousandEyes application.

From the customer view in Control Hub , go to Devices > Settings > Configuration Defaults .

Click Set defaults on location , then select the desired location and click Next .

Search for ThousandEyes > Enable and set the configuration value to True .

Search for ThousandEyes > Account Token and enter the token.

Search for ThousandEyes > Connection String and paste the connection string.

Click Next and review your changes.

Click Apply changes .

## Configure ThousandEyes on multiple phones

Before you begin

Get ThousandEyes Endpoint Agent licenses (either essential or advantage). You need one endpoint license per device.

Get the connection string from the ThousandEyes application.

Enable ThousandEyes integration for your organization or location before you set up this feature for your device. In device configurations, you can only enter the connection string.

From the customer view in Control Hub , go to Devices , and then select the phones that you want to configure.

Click Edit in the top right of the device list.

Click All configurations .

In the ThousandEyes section, paste the connection string that you get from the ThousandEyes portal.

Click Next .

Review your changes and click Apply .

Click Close to close the page.

## Configure ThousandEyes on an individual device

Before you begin

Get ThousandEyes Endpoint Agent licenses (either essential or advantage). You need one endpoint license per device.

Get the connection string from the ThousandEyes application.

Enable ThousandEyes integration for your organization or location before you set up this feature for your device. In device configurations, you can only enter the connection string.

From the customer view in Control Hub , go to Devices > Settings .

On the Devices page, search for and select the device that you want to configure.

On the device details page, select All configurations in the Configurations section.

Paste the connection string that you get from ThousandEyes portal into the Connection string field in the ThousandEyes section.

Click Next .

Review your change and click Apply .

Click Close to close the page.

## Disable ThousandEyes for your devices

You can disable ThousandEyes for all deployed devices or for an individual device without affecting the others.

Choose one of the following actions as needed:

Go to Devices > Settings .

Toggle off Enable ThousandEyes Agent .

On the Devices page,  find your device and open the device details page.

Go to All configurations .

Clear the Connection string field in the ThousandEyes section.

Select Next and Apply .

| Phone model | Firmware version |
|---|---|
| Cisco Video Phone 8875 | 5.0.1 and later |
| Cisco Desk Phone 9861 | 3.2.1 and later |
| Cisco Desk Phone 9871 | 3.2.1 and later |

| 1 | From the customer view in Control Hub , go to Devices > Settings . |
|---|---|
| 2 | Scroll down to the ThousandEyes section and toggle on Enable ThousandEyes Agent . |
| 3 | Click Add and paste the connection string that you copied from ThousandEyes portal. If you don't want to integrate all devices, leave the connection string field empty and enter it in the device-level settings instead. |
| 4 | Click Save in the popup window. |

| 1 | From the customer view in Control Hub , go to Devices > Settings > Configuration Defaults . |
|---|---|
| 2 | Click Set defaults on location , then select the desired location and click Next . |
| 3 | Search for ThousandEyes > Enable and set the configuration value to True . |
| 4 | Search for ThousandEyes > Account Token and enter the token. |
| 5 | Search for ThousandEyes > Connection String and paste the connection string. |
| 6 | Click Next and review your changes. |
| 7 | Click Apply changes . |

| 1 | From the customer view in Control Hub , go to Devices , and then select the phones that you want to configure. |
|---|---|
| 2 | Click Edit in the top right of the device list. |
| 3 | Click All configurations . |
| 4 | In the ThousandEyes section, paste the connection string that you get from the ThousandEyes portal. |
| 5 | Click Next . |
| 6 | Review your changes and click Apply . |
| 7 | Click Close to close the page. |

| 1 | From the customer view in Control Hub , go to Devices > Settings . |
|---|---|
| 2 | On the Devices page, search for and select the device that you want to configure. |
| 3 | On the device details page, select All configurations in the Configurations section. |
| 4 | Paste the connection string that you get from ThousandEyes portal into the Connection string field in the ThousandEyes section. |
| 5 | Click Next . |
| 6 | Review your change and click Apply . |
| 7 | Click Close to close the page. |

| Choose one of the following actions as needed: For all devices Go to Devices > Settings . Toggle off Enable ThousandEyes Agent . For an individual device On the Devices page,  find your device and open the device details page. Go to All configurations . Clear the Connection string field in the ThousandEyes section. Select Next and Apply . |
|---|