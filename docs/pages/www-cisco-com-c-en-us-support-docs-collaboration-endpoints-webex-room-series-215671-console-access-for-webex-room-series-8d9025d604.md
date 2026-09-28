---
doc_id: www-cisco-com-c-en-us-support-docs-collaboration-endpoints-webex-room-series-215671-console-access-for-webex-room-series-8d9025d604
source_url: https://www.cisco.com/c/en/us/support/docs/collaboration-endpoints/webex-room-series/215671-console-access-for-webex-room-series-dev.html
retrieved_at: 2026-09-01T19:34:56.193977+00:00
---

Console Access for WebEx Room Series Devices and Quad Camera

# Console Access for WebEx Room Series Devices and Quad Camera

### Download Options

Updated: June 18, 2020

Document ID: 215671

Contents

## Contents

## Introduction

This document describes how to do console access to WebEx Room Series devices and Quad Camera.

Contributed by Seeta Rama Raju K, Cisco TAC Engineer.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of WebEx Room Series devices and Quad Camera.

### Components Used

The information in this document is based on these software and hardware versions:

- Windows Laptop/Dektop.

- Drivers to take the serial connection from USB. ( http://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers )

- Putty application

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

Step 1. Connect the USB to micro USB Cable between Endpoint/Quad Camera and Windows system.

Step 2. Open the PuTTY application. The PuTTY Configuration window opens as shown in the image.

Step 3. Under the Connection Type field, select Serial radio button as shown in the image.

Step 4. In theCategory navigation field, select Serial as shown in the image.

The Options controlling local serial lines page opens as in the image.

Step 5. In the serial line to connect to field, enter the COM port that your device is connected to (for example, You can enter default COM port is COM1).

Step 6. In the Speed (baud) field, enter the digital transmission speed that is compatible with the switch as shown in the image. For most of the endpoints, the speed can be set to 115200 .

Step 7. In the Data bits field, enter the number of data bits used for each character as shown in the image. The recommended value is 8.

Step 8. In the Stop bits field, enter the number of bits to be sent at the end of every character as shown in the image. The stop bit informs the machine that it has reached the end of a byte. The recommended value is 1.

Step 9. In the Parity drop-down menu, select the method in order to detect errors in transmission as shown in the image. The recommended method in order to detect errors in the transmission is None .

Step 10. In the Flow Control drop-down menu, select the method in order to prevent data overflow as shown in the image. The recommended method in order to prevent data overflow is None .

Step 11. (Optional) In order to save the connection settings for future use, navigate to theCategorynavigation pane, and select Session . If you do not wish to save the connection settings, skip to Step 14.

Step 12. Under the Saves Sessions field, enter a name for the settings to be saved as.

Step 13. Select Save as shown in the image.

Step 14 . Select Open .

The COM1 – PuTTY console window opens.

Step 15. Hit Enter on the keyboard in order to activate the Command Line Interface (CLI). The log in prompt is displayed:

Step 16. Enter the User Name. The default username is admin .

Step 14. Enter the Password. The default password is cisco .

### Revision History

1.0

23-Jun-2020

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 23-Jun-2020 | Initial Release |