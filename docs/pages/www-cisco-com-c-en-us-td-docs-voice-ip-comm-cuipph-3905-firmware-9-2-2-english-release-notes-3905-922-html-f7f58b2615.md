---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-3905-firmware-9-2-2-english-release-notes-3905-922-html-f7f58b2615
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/3905/firmware/9_2_2/english/release/notes/3905_922.html
retrieved_at: 2026-08-21T06:25:23.143328+00:00
---

Cisco Unified SIP Phone 3905 Release Notes for Firmware Release 9.2(2)

# Cisco Unified SIP Phone 3905 Release Notes for Firmware Release 9.2(2)

### Download Options

Updated: October 2, 2013

## Table Of Contents

Cisco Unified SIP Phone 3905 Release Notes for Firmware Release 9.2(2)

Contents

Related Documentation

New and Changed Information

Configurable Call Features: Call Forwarding, Call Pickup, and Group Pickup

Additional Locale Support

Installation Notes

Installing Cisco Unified Communications Manager

Installing Cisco Unified Communications Manager Express

Installing Firmware Release 9.2(2) on Cisco Unified Communications Manager

Firmware Installation Procedure

Limitations and Restrictions

Call Admission Control with Cisco Unified Communications Manager

Caveats

Using Bug Toolkit

Open Caveats

Resolved Caveats

Obtaining Documentation and Submitting a Service Request

## Cisco Unified SIP Phone 3905 Release Notes for Firmware Release 9.2(2)

Updated: October 2, 2013

Use these release notes with the Cisco Unified SIP Phone 3905 running Firmware Release 9.2(2).

Firmware Release 9.2(2) is supported by Cisco Unified Communications Manager (Unified CM) Releases 7.1.5 and later.

Firmware Release 9.2(2) is designed and tested to interoperate with Cisco call control, most notably Unified CM Releases 7.1.5 and later. Although SIP firmware is RFC 3261 compliant, it is not supported by the Cisco Technical Assistance Centre (TAC) or by Cisco Engineering for use with non-Cisco call control systems.

## Contents

These release notes provide the following information:

• Related Documentation

• New and Changed Information

• Installation Notes

• Limitations and Restrictions

• Caveats

• Obtaining Documentation and Submitting a Service Request

## Related Documentation

Cisco Unified IP Phone Documentation

Refer to publications that are specific to your language, phone model and Cisco Unified Communications Manager release. Navigate from the following documentation URL:

http://www.cisco.com/en/US/products/ps7193/tsd_products_support_series_home.html

Cisco Unified Communications Manager Documentation

Refer to the Cisco Unified Communications Manager Documentation Guide and other publications specific to your Cisco Unified Communications Manager release. Navigate from the following URL:

http://www.cisco.com/en/US/products/sw/voicesw/ps556/tsd_products_support_series_home.html

Cisco Unified Communications Manager Business Edition Documentation

Refer to the Cisco Unified Communications Manager Business Edition Documentation Guide and other publications that are specific to your Cisco Unified Communications Manager release. Navigate from the following URLs:

http://www.cisco.com/en/US/products/ps7273/tsd_products_support_series_home.html and http://www.cisco.com/en/US/products/ps11370/tsd_products_support_series_home.html

## New and Changed Information

This section contains the following topics:

• Configurable Call Features: Call Forwarding, Call Pickup, and Group Pickup

• Additional Locale Support

### Configurable Call Features: Call Forwarding, Call Pickup, and Group Pickup

In the previous firmware release, Call Forwarding, Call Pickup, and Group Pickup were hard-coded features available on the Cisco Unified SIP Phone 3905.

In Release 9.2(2), you can specify whether these features are enabled or disabled on a phone using the softkey template in Cisco Unified Communications Manager. While softkeys are not supported on the Cisco Unified SIP Phone 3905, the phone downloads the softkey template from Cisco Unified Communications Manager and uses the settings contained in the template to determine whether to enable or disable these features. All three features are enabled by default.

The softkey template settings affect only the three features listed here. The phone ignores any other feature settings in the softkey template.

### Additional Locale Support

The Cisco Unified SIP Phone 3905 Release 9.2(2) provides support for additional locales. For the complete list of supported locales, see the readme file available with the Locale Installer on Cisco.com.

Note The Cisco Unified SIP Phone 3905 does not currently support the Japanese locale, but is scheduled to support it in December, 2011.

## Installation Notes

This section contains the following topics:

• Installing Cisco Unified Communications Manager

• Installing Cisco Unified Communications Manager Express

• Installing Firmware Release 9.2(2) on Cisco Unified Communications Manager

### Installing Cisco Unified Communications Manager

Before using the Cisco Unified IP Phone with Cisco Unified Communications Manager, you must install the latest firmware on all Cisco Unified Communications Manager servers in the cluster.

To download and install the Cisco Unified Communications Manager version, follow these steps:

Step 1 Go to the following URL:

http://tools.cisco.com/support/downloads/pub/Redirect.x?mdfid=278875240

Step 2 Log in to the Products > Voice and Unified Communications > IP Telephony .

Step 3 Choose Call Control > Cisco Unified Communications Manager (CallManager) .

Step 4 Choose your Cisco Unified Communications Manager version.

### Installing Cisco Unified Communications Manager Express

To download and install the Cisco Unified Communications Manager Express version, follow these steps:

Step 1 Go to the following URL:

http://tools.cisco.com/support/downloads/pub/Redirect.x?mdfid=278875240

Step 2 Log in to the Products > Voice and Unified Communications > IP Telephony .

Step 3 Choose Call Control > Cisco Unified Communications Manager Express .

Step 4 Choose your Cisco Unified Communications Manager Express version from the Select a File to Download section.

### Installing Firmware Release 9.2(2) on Cisco Unified Communications Manager

This section describes how to install Firmware Release 9.2(2) on Cisco Unified Communications Manager.

### Firmware Installation Procedure

Before using the Cisco Unified SIP Phone 3905 with Cisco Unified Communications Manager, you must install the latest firmware on all Cisco Unified Communications Manager servers in the cluster.

To download and install the firmware, follow these steps:

Step 1 To access the firmware files, go to this URL:

http://tools.cisco.com/support/downloads/pub/Redirect.x?mdfid=278875240 .

Step 2 Log in to the Tools and Resources Download page.

Step 3 Choose the IP Telephony folder.

Step 4 Choose IP Phones > Cisco Unified SIP Phones 3900 Series .

Step 5 Choose your phone type.

Step 6 In the Latest Releases folder, choose 9.2(2) .

Step 7 To download the SIP firmware for the Cisco Unified IP Phone, click the Download Now or Add to cart button and follow the prompts.

cmterm-3905.9-2-2-0.cop.sgn

Note If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file.

Step 8 Click the + next to the firmware file name in the Download Cart section to access additional information about this file.The hyperlink for the Readme file is in the Additional Information section, which contains installation instructions for the corresponding firmware.

cmterm-3905.9-2-2-0-Readme.html

Step 9 Follow the instructions in the Readme file to install the firmware.

## Limitations and Restrictions

### Call Admission Control with Cisco Unified Communications Manager

We recommend that you do not configure the Cisco Unified Communications Manager to apply Call Admission Control (CAC) to the Cisco Unified SIP Phone 3905. Ensure that the phone is not part of the CAC locations or CAC gatekeepers and trunks. For more information on CAC, see the Cisco Unified Communications Manager System Guide .

## Caveats

This section contains these topics:

• Using Bug Toolkit

• Open Caveats

• Resolved Caveats

### Using Bug Toolkit

Known problems (bugs) are graded according to severity level. These release notes contain descriptions of:

• All severity level 1 or 2 bugs.

• Significant severity level 3 bugs.

You can search for problems by using the Cisco Software Bug Toolkit.

To access Bug Toolkit, you need the following items:

• Internet connection

• Web browser

• Cisco.com user ID and password

To use the Software Bug Toolkit, follow these steps:

Step 1 To access the Bug Toolkit, go to http://tools.cisco.com/Support/BugToolKit/action.do?hdnAction=searchBugs.

Step 2 Log on with your Cisco.com user ID and password.

Step 3 To look for information about a specific problem, enter the bug ID number in the Search for bug ID field, then click Go .

### Open Caveats

No severity 1, 2, or 3 defects exist for the Cisco Unified SIP Phone 3905 Firmware Release 9.2(2).

Because defect status continually changes, be aware that this reflects a snapshot of the defects that were open at the time this report was compiled. For an updated view of open defects, access Bug Toolkit as described in Using Bug Toolkit . You must be a registered Cisco.com user to access this online information.

### Resolved Caveats

Table 1 lists severity 1, 2, and 3 defects that are resolved for the Cisco Unified SIP Phone 3905 Firmware Release 9.2(2).

For more information about an individual defect, you can access the online record for the defect by clicking the Identifier or going to the URL shown. You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, be aware that Table 1 reflects a snapshot of the defects that were resolved at the time this report was compiled. For an updated view of resolved defects, access Bug Toolkit as described in Using Bug Toolkit .

Table 1 Resolved Caveats for the Cisco Unified SIP Phone 3905 Firmware Release 9.2(2)

Identifier

Headline and Bug Toolkit Link

CSCtq01228

Phone MWI will not light until back to idle screen

CSCtq12036

Incoming call fails when caller ID and display name exceeds 48

## Obtaining Documentation and Submitting a Service Request

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What's New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http://www.cisco.com/en/US/docs/general/whatsnew/whatsnew.html

Subscribe to the What's New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application. The RSS feeds are a free service and Cisco currently supports RSS version 2.0.

### Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks . Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1110R)

### © 2013 Cisco Systems, Inc. All rights reserved.

| Identifier | Headline and Bug Toolkit Link |
|---|---|
| CSCtq01228 | Phone MWI will not light until back to idle screen |
| CSCtq12036 | Incoming call fails when caller ID and display name exceeds 48 |