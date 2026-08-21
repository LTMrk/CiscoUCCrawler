---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-6901-6911-firmware-9-0-2-english-release-notes-69x1-902-html-39ac970a9d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/6901_6911/firmware/9_0_2/english/release/notes/69x1_902.html
retrieved_at: 2026-08-21T06:23:53.287615+00:00
---

Cisco Unified IP Phone 6901 and 6911 (SCCP) Release Notes for Firmware Release 9.0(2)

# Cisco Unified IP Phone 6901 and 6911 (SCCP) Release Notes for Firmware Release 9.0(2)

### Download Options

Updated: April 15, 2016

## Table of Contents

Cisco Unified IP Phone 6901 and 6911 (SCCP) Release Notes for Firmware Release 9.0(2)

Contents

Introduction

Related Documentation

New and Changed Information

Adaptive LLDP-MED

Installation Notes

Installing Cisco Unified Communications Manager

Installing Cisco Unified Communications Manager Express

Installing Firmware Release 9.0(2)

Caveats

Using Bug Toolkit

Open Caveats

Resolved Caveats

Obtaining Documentation and Submitting a Service Request

Published: March 31, 2010 Updated: April 15, 2016

Use these release notes with a Cisco Unified IP Phone running SCCP firmware release 9.0(2). This version of firmware release 9.0(2) is compatible with Cisco Unified Communications Manager 8.0.

Note Firmware release 9.0(2) is compatible with Cisco Unified Communications Manager 7.1(3) by using a device pack.

## Contents

These release notes provide the following information. You might need to notify your users about some of the information provided in this document.

## Introduction

The Cisco Unified IP Phone 6901 and 6911 are new, easy-to-use, cost effective IP phones that provide high-quality voice services over IP. These IP phones are suitable for use in elevators, lobbies, hallways, hotel bathrooms and any other location where a basic phone is needed. These IP phones offer a variety of features including:

- Cisco Unified IP Phone 6901—Dedicated buttons for Hold, Redial, and Volume

- Cisco Unified IP Phone 6911—Dedicated buttons for Hold, Redial, Volume, Conference, Transfer, Messages, and Speaker

- Single line—Simplifies user interaction with traditional telephony-like experience

- Interactive Voice Response (IVR)—Enables access to some features such as voicemail

## Related Documentation

Cisco Unified IP Phone Documentation

Refer to publications that are specific to your language, phone model and Cisco Unified Communications Manager release. Navigate from the following documentation URL:

http://www.cisco.com/en/US/products/ps10326/tsd_products_support_series_home.html

Cisco Unified Communications Manager Documentation

Refer to the Cisco Unified Communications Manager Documentation Guide and other publications specific to your Cisco Unified Communications Manager release. Navigate from the following URL:

http://www.cisco.com/en/US/products/sw/voicesw/ps556/tsd_products_support_series_home.html

Cisco Unified Communications Manager Business Edition Documentation

Refer to the Cisco Unified Communications Manager Business Edition Documentation Guide and other publications that are specific to your Cisco Unified Communications Manager release. Navigate from the following URL:

http://www.cisco.com/en/US/products/ps7273/tsd_products_support_series_home.html

Cisco Unified Communications Manager Express Documentation

Refer to the Cisco Unified Communications Manager Express Documentation Guide and other publications specific to your Cisco Unified Communications Manager Express release. Navigate from the following URL:

http://www.cisco.com/en/US/products/sw/voicesw/ps4625/tsd_products_support_series_home.html

## New and Changed Information

This section contains these topics:

- Adaptive LLDP-MED

### Adaptive LLDP-MED

The Adaptive Link Layer Discovery Protocol–Media Endpoint Device (Adaptive LLDP-MED) feature delays transmitting LLDP packets at IP phone startup until the system verifies that LLDP messaging is supported. During this period, the voice-VLAN phone configuration is available through valid Cisco Discovery Protocol (CDP) messaging. The duration of the verification is typically about 6 to 30 seconds.

The Adaptive implementation was added to the LLDP-MED feature two reasons:

- Some customers enable Cisco Catalyst Port Security features on the Cisco Catalyst switches that do not support LLDP-MED, which may cause switch ports to shut down and the IP phones to be disabled when port security is enabled.

- Some legacy Cisco IOS switches do not recognize the LLDP multicast address, which may cause connectivity problems with the IP phones.

The feature affects only the network (switch) port-state machine of the IP phone.

After both CDP and LLDP packets have been received on the SW port, LLDP becomes the preferred protocol. (Even with the Adaptive implementation, some exceptions may cause a port to shut down.)

If the customer’s network configuration does not support LLDP messaging, it is recommended that LLDP be disabled permanently in the Cisco Unified CM Administration application in the Phone Configuration window. Failing to disable LLDP when it is not supported may cause issues for customers that are using older or legacy switches with port security enabled.

To disable LLDP in the Cisco Unified CM Administration application, choose Device > Phone , select the appropriate IP phones, and scroll to the Product Specific Configuration Layout pane.

The Adaptive LLDP-MED feature is supported on the following IP phones:

- Cisco Unified IP Phone 6901

- Cisco Unified IP Phone 6911

Where to Find More Information

- Cisco Unified IP Phone Guide

- Cisco Unified IP Phone Administration Guide

## Installation Notes

This section contains these sections:

### Installing Cisco Unified Communications Manager

Before using the Cisco Unified IP Phone with Cisco Unified Communications Manager, you must install the latest firmware on all Cisco Unified Communications Manager servers in the cluster.

Note You must install the QED file on Cisco Unified Communications Manager before installing the phone firmware.

To download and install the Cisco Unified Communications Manager version, follow these steps:

Step 1 Go to the following URL:

http://tools.cisco.com/support/downloads/pub/Redirect.x?mdfid=278875240

Step 2 Log in to the Tools and Resources Download Software page.

Step 3 Click + and choose the IP Telephony folder.

Step 4 Choose Call Control > Cisco Unified Communications Manager (CallManager) .

Step 5 Choose your Cisco Unified Communications Manager version.

### Installing Cisco Unified Communications Manager Express

To download and install the Cisco Unified Communications Manager Express version, follow these steps:

Step 1 Go to the following URL:

http://tools.cisco.com/support/downloads/pub/Redirect.x?mdfid=278875240

Step 2 Log in to the Tools and Resources Download Software page.

Step 3 Click + and choose the IP Telephony folder.

Step 4 Choose Call Control > Cisco Unified Communications Manager Express .

Step 5 Choose your Cisco Unified Communications Manager Express version from the Select a File to Download section.

### Installing Firmware Release 9.0(2)

To download and install the phone firmware, follow these steps:

Step 1 Go to the following URL:

http://tools.cisco.com/support/downloads/go/Redirect.x?mdfid=278875240

Step 2 Log in to the Tools and Resources Download Software page.

Step 3 Click + and choose the IP Telephony folder.

Step 4 Choose your phone type.

Step 5 Choose 9.0(2) under the Latest Releases folder.

Step 6 To download the SCCP firmware for the Cisco Unified IP Phone, click the Download Now or Add to cart button and follow the prompts:

cmterm-6901_6911-sccp.9-0-2-0.cop.sgn

Note If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file.

Step 7 Click the + next to the firmware file name in the Download Cart section to access additional information about this file.The hyperlink for the Readme file is in the Additional Information section, which contains installation instructions for the corresponding firmware:

cmterm-6901_6911-sccp.9-0-2-0-readme.html

Step 8 Follow the instructions in the Readme file to install the firmware.

## Caveats

This section contains these topics:

### Using Bug Toolkit

Known problems (bugs) are graded according to severity level. These release notes contain descriptions of:

- All severity level 1 or 2 bugs.

- Significant severity level 3 bugs.

You can search for problems by using the Cisco Software Bug Toolkit.

To access Bug Toolkit, you need the following items:

- Internet connection

- Web browser

- Cisco.com user ID and password

To use the Software Bug Toolkit, follow these steps:

Step 1 To access the Bug Toolkit, go

http://tools.cisco.com/Support/BugToolKit/action.do?hdnAction=searchBugs.

Step 2 Log on with your Cisco.com user ID and password.

Step 3 To look for information about a specific problem, enter the bug ID number in the “Search for bug ID” field, then click Go .

### Open Caveats

There are no open caveats for firmware release 9.0(2).

### Resolved Caveats

There are no resolved caveats for firmware release 9.0(2).

## Obtaining Documentation and Submitting a Service Request

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http://www.cisco.com/en/US/docs/general/whatsnew/whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application. The RSS feeds are a free service and Cisco currently supports RSS version 2.0.

Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks . Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1110R)

### Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks . Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1110R)

Any Internet Protocol (IP) addresses used in this document are not intended to be actual addresses. Any examples, command display output, and figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses in illustrative content is unintentional and coincidental.

### Any Internet Protocol (IP) addresses used in this document are not intended to be actual addresses. Any examples, command display output, and figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses in illustrative content is unintentional and coincidental.

© 2010 Cisco Systems, Inc. All rights reserved.

### © 2010 Cisco Systems, Inc. All rights reserved.