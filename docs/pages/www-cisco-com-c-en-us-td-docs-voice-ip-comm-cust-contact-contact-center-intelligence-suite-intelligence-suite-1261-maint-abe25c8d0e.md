---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-1261-maint-abe25c8d0e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_1261/maintain_and_operate/guide/cuic_b_1261-admin-console-user-guide/cuic_m_control-center-1261.html
retrieved_at: 2026-08-21T04:39:17.806824+00:00
---

Administration Console User Guide for Cisco Unified Intelligence Center, Release 12.6(1)

# Administration Console User Guide for Cisco Unified Intelligence Center, Release 12.6(1)

Updated: May 14, 2021

Chapter: Control Center

## Chapter: Control Center

- Control Center

- Control Center

# Control Center

## Control Center

Choose Control Center from the navigation menu to open the Control Center page, where you can check the status of each device, and start, stop, or restart devices.

As soon as you add a device on the Device Configuration page (see Device Configuration ), this Control Center page also shows a row for that Cisco Unified Intelligence Center Reporting Server device.

Field

Description

Name

The name of the device.

For the Controller, this field is populated by default.

For each member, this field shows the name of the device from the Device Management page.

Host Address

The IP address for the device.

Device Type

A description of the device (Controller or Member).

Status

The current state of the device. Possible values are:

Starting - the server is in the process of starting up.

Unknown - the server or subsystem that communicates with the Administration Console could not be reached.

Stopped - the server is not running.

Running (in service) - the server is running and active.

Running (partial service) - the server is running, but is not ready to work. The server may be starting up.

Stopping - the server is in the process of stopping.

Actions from this page

To

Do This

Start

Start the device.

Shutdown

Shut down the device. Respond OK or Cancel to the confirmation message.

Restart

Restart the device.

| Field | Description |
|---|---|
| Name | The name of the device. For the Controller, this field is populated by default. For each member, this field shows the name of the device from the Device Management page. |
| Host Address | The IP address for the device. |
| Device Type | A description of the device (Controller or Member). |
| Status | The current state of the device. Possible values are: Starting - the server is in the process of starting up. Unknown - the server or subsystem that communicates with the Administration Console could not be reached. Stopped - the server is not running. Running (in service) - the server is running and active. Running (partial service) - the server is running, but is not ready to work. The server may be starting up. Stopping - the server is in the process of stopping. |

| Note | Start, Shutdown, and Restart refer to the application process running on the server, and not the hardware or operating system. |
|---|---|

| To | Do This |
|---|---|
| Start | Start the device. |
| Shutdown | Shut down the device. Respond OK or Cancel to the confirmation message. |
| Restart | Restart the device. |