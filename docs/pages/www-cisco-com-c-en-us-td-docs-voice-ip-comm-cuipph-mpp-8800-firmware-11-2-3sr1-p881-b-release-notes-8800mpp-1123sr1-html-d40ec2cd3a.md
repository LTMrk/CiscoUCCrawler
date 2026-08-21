---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-8800-firmware-11-2-3sr1-p881-b-release-notes-8800mpp-1123sr1-html-d40ec2cd3a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/8800/firmware/11-2-3sr1/p881_b_release-notes-8800mpp-1123sr1.html
retrieved_at: 2026-08-21T13:44:56.168473+00:00
---

Cisco IP Phone 8800 Series Multiplatform Phones Release Notes for Firmware Release 11.2(3)SR1

# Cisco IP Phone 8800 Series Multiplatform Phones Release Notes for Firmware Release 11.2(3)SR1

### Download Options

Updated: April 26, 2019

First Published: April 26, 2019

# Introduction

Use these release notes with the Cisco IP Phone 8800 Series Multiplatform Phones running SIP Firmware Release 11.2(3)SR1.

The following table describes the individual phone requirements.

Phone

Support Requirements

Cisco IP Phone 8800 Series Multiplatform Phones

BroadSoft BroadWorks 22.0

MetaSphere CFS version 9.4

Asterisk 11.0

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Phone 8800 Series Documentation

Refer to publications that are specific to your language and call control system. Navigate from the following documentation
                        URL:

https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-8800-series-multiplatform-firmware/tsd-products-support-series-home.html

## New and Changed Features

### Activation Code Onboarding

If your network is configured for Activation Code Onboarding, your administrator generates and provides each user with a unique
                        16-digit activation code. The user enters the activation code, and the phone automatically registers.

Activation codes can be used only once, and expire after a certain time. If a user enters an expired code, the phone displays Invalid activation code on the screen. If this happens, the administrator provides the user with a new code.

This feature keeps your network secure because the phone can't register until the user enters a valid activation code.

You can change existing phones to use this feature. To do this, reset the phone to the factory settings. After the factory
                        reset and bootup, the phone registers when the user enters the activation code.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

Cisco IP Phone 8800 Series and Cisco IP Conference Phone 8832 Multiplatform Phones Provisioning Guide

### Audio Performance for Overload Point 9dB

Audio overload point specifies the signal level at which the audio codec is overloaded. For a phone that supports audio performance
                        for 9dB overload point for G.722 codec, you can configure the phone using the Audio_Overload_Point_9dB parameter. Locate the parameter in your phone's configuration file. The default setting is No . For the phones that use ETSI standards and are required to support overload point of 9dB for G.722 codec, set this parameter
                        to Yes . Otherwise, keep the default setting. When set to No, the audio overload point is 3.17dB acrosss the network for consistent
                        power for both the narrow band and the wide band.

Settings example:

The Audio_Overload_Point_9dB parameter is available for the following phones:

Cisco IP Phone 8811 Multiplatform Phones

Cisco IP Phone 8841 Multiplatform Phones

Cisco IP Phone 8851 Multiplatform Phones

Cisco IP Phone 8861 Multiplatform Phones

## Upgrade the Firmware

Two firmware images are available for Cisco IP Phone 8800 Series Multiplatform Phones :

Firmware for Cisco IP Phone 8811, 8841, 8851, and 8861 Multiplatform Phones (Audio only)

Firmware for Cisco IP Phone 8845 and 8865 Multiplatform Phones (Video)

After the firmware upgrade completes, the phone reboots automatically.

Click the following URL:

https://software.cisco.com/download/home/286311392

In the middle pane, select IP Phone 8800 Series With Multiplatform Firmware .

Select your phone model in the right pane.

On the next page that is displayed, select Multiplatform Firmware .

Under Latest Release , select 11.2.3 MSR1-1 .

(Optional) Place your mouse pointer on the file name in the right pane, to see the file details and checksum values.

Download the file:

For Cisco IP Phone 8811, 8841, 8851, and 8861 Multiplatform Phones: cmterm-88xx.11-2-3MSR1-1_REL.zip

For Cisco IP Phone 8845 and 8865 Multiplatform Phones: cmterm-8845_65.11-2-3MSR1-1_REL.zip

Click Accept License Agreement .

Unzip the files.

Place the files in the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the upgrade.

Upgrade the phone firmware with one of these methods.

Upgrade the phone firmware from the phone administration web page:

On the phone administration web page, go to Admin Login > Advanced > Voice > Provisioning tab, Firmware Upgrade section. In the Upgrade Rule field, enter the load file URL as described below.

Load file URL format:

<upgrade protocol>://<server ip address>[:<port>]>/<path>/<file name>.loads

Example:

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

Load file URL format:

<upgrade protocol>://<server ip address>[:<port>]>/<path>/<file name>.loads

Example:

```
https://10.74.10.225/admin/upgrade?https://10.73.10.223/firmware/ sip88xx.11-2-3MSR1-1.loads
```

Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Anything that degrades network performance can affect phone voice and video quality, and in some cases, can cause a call to
                        drop. Sources of network degradation can include, but are not limited to, the following activities:

Administrative
                              				tasks, such as an internal port scan or security scan

Attacks that
                              				occur on your network, such as a Denial of Service attack

### Caller Identification and Other Phone Functions

Caller identification or other phone functions have not been verified with third-party applications for the visually or hearing
                        impaired.

## View Caveats

You can search for caveats using the Cisco Bug Search tool.

Known caveats (bugs) are graded according to severity level, and are either open or resolved.

Before you begin

### Before you begin

To view the caveats, you need the following items:

Internet connection

Web browser

Cisco.com user ID and password

Perform one of the following actions:

To find all caveats, use this URL:

To find all open caveats, use this URL:

To find all resolved caveats, use this URL:

When prompted, log in with your Cisco.com user ID and password.

(Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter .

### Open Caveats

The following list contains the severity 1, 2, and 3 caveats that are open for the Cisco IP Phone 8800 Series Multiplatform Phones that use the firmware release 11.2(3)SR1.

This list reflects a snapshot of the caveats that were open at the time this report was compiled. The status of caveats may
                        have changed since then. For an updated view of the open caveats, or to view details or history for specific caveats, access
                        the Bug Search Toolkit as described in View Caveats . You must be a registered Cisco.com user to access this information.

CSCvo46210 Multiplatform Phones have only 25 BLF entries

CSCvo88578 Turning Call forward ON causes Station Display Name on LCD to change to user id of selected line

### Resolved Caveats

The following list contains the severity 1, 2, and 3 caveats that are resolved for the Cisco IP Phone 8800 Series Multiplatform Phones that use Firmware Release 11.2(3)SR1.

This list reflects a snapshot of the caveats that were resolved at the time this report was compiled. The status of caveats
                        may have changed since then. For an updated view of the resolved caveats, or to view details or history for specific caveats,
                        access the Bug Search Toolkit as described in View Caveats . You must be a registered Cisco.com user to access this information.

CSCvo62040 TR 069 defaults to Yes

CSCvo43984 CP-8851-3PCC , TR-069 issue

CSCvo47648 CP-8841-3PCC//11.2.3 FW does not receive audio from Meet-Me Conference

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .

| Phone | Support Requirements |
|---|---|
| Cisco IP Phone 8800 Series Multiplatform Phones | BroadSoft BroadWorks 22.0 MetaSphere CFS version 9.4 Asterisk 11.0 |

| Step 1 | Click the following URL: https://software.cisco.com/download/home/286311392 |
|---|---|
| Step 2 | In the middle pane, select IP Phone 8800 Series With Multiplatform Firmware . |
| Step 3 | Select your phone model in the right pane. |
| Step 4 | On the next page that is displayed, select Multiplatform Firmware . |
| Step 5 | Under Latest Release , select 11.2.3 MSR1-1 . |
| Step 6 | (Optional) Place your mouse pointer on the file name in the right pane, to see the file details and checksum values. |
| Step 7 | Download the file: For Cisco IP Phone 8811, 8841, 8851, and 8861 Multiplatform Phones: cmterm-88xx.11-2-3MSR1-1_REL.zip For Cisco IP Phone 8845 and 8865 Multiplatform Phones: cmterm-8845_65.11-2-3MSR1-1_REL.zip |
| Step 8 | Click Accept License Agreement . |
| Step 9 | Unzip the files. |
| Step 10 | Place the files in the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the upgrade. |
| Step 11 | Upgrade the phone firmware with one of these methods. Upgrade the phone firmware from the phone administration web page: On the phone administration web page, go to Admin Login > Advanced > Voice > Provisioning tab, Firmware Upgrade section. In the Upgrade Rule field, enter the load file URL as described below. Load file URL format: <upgrade protocol>://<server ip address>[:<port>]>/<path>/<file name>.loads Example: https://10.73.10.223/firmware/sip88xx.11-2-3MSR1-1.loads Click Submit All Changes . Upgrade the phone firmware directly from your web browser: In the address bar of your web browser, enter the phone upgrade URL as described below. Phone upgrade URL format: <phone protocol>://<phone ip address[:port]>/admin/upgrade?<load file URL> Load file URL format: <upgrade protocol>://<server ip address>[:<port>]>/<path>/<file name>.loads Example: https://10.74.10.225/admin/upgrade?https://10.73.10.223/firmware/ sip88xx.11-2-3MSR1-1.loads Note Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. | Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |

| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
|---|---|

| Step 1 | Perform one of the following actions: To find all caveats, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286311392&sb=anfr&bt=custV To find all open caveats, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286311392&sb=anfr&sts=open&bt=custV To find all resolved caveats, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286311392&sb=anfr&sts=fd&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter . |