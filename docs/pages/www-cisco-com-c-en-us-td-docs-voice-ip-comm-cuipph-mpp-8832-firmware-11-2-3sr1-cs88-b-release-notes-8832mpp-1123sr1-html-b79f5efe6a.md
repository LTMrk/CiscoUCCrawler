---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-8832-firmware-11-2-3sr1-cs88-b-release-notes-8832mpp-1123sr1-html-b79f5efe6a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/8832/firmware/11-2-3sr1/cs88_b_release-notes-8832mpp-1123sr1.html
retrieved_at: 2026-08-21T13:43:24.455797+00:00
---

Cisco IP Conference Phone 8832 Multiplatform Phones Release Notes for Firmware Release 11.2(3)SR1

# Cisco IP Conference Phone 8832 Multiplatform Phones Release Notes for Firmware Release 11.2(3)SR1

### Download Options

Updated: April 26, 2019

First Published: April 26, 2019

# Introduction

Use these release notes with the Cisco IP Conference Phone 8832 Multiplatform Phones running SIP Firmware Release 11.2(3)SR1.

The following table describes the individual phone requirements.

Phone

Support Requirements

Cisco IP Conference Phone 8832 Multiplatform Phones

BroadSoft BroadWorks 22.0

MetaSphere CFS version 9.4

Asterisk 11.0

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Conference Phone 8832 Documentation

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

Cisco IP Conference Phone 8832 Multiplatform Phones Administration Guide

Cisco IP Conference Phone 8832 Multiplatform Phones User Guide

Cisco IP Phone 8800 Series and Cisco IP Conference Phone 8832 Multiplatform Phones Provisioning Guide

## Upgrade the Firmware

The Cisco IP Conference Phone 8832 Multiplatform Phones support a single image upgrade using TFTP, HTTP, or HTTPS protocols with a URL.

After the firmware upgrade completes, the phone reboots automatically.

Click the following URL:

https://software.cisco.com/download/home/286311392

In the middle pane, select IP Phone 8800 Series With Multiplatform Firmware .

Select IP Conference Phone 8832 With Multiplatform Firmware in the right pane.

Under Latest Release , select 11.2.3 MSR1-1 .

(Optional) Place your mouse pointer on the file name in the right pane, to see the file details and checksum values.

Download the cmterm-8832.11-2-3MSR1-1_REL.zip file.

Click Accept License Agreement .

Unzip the files.

Place the files in the TFTP, HTTP, or HTTPS download directory.

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
https://10.74.10.225/admin/upgrade?https://10.73.10.223/firmware/ sip8832.11-2-3MSR1-1.loads
```

Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Anything that degrades network performance can affect phone voice and in some cases can cause a call to drop. Sources of
                        network degradation can include, but are not limited to, the following activities:

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

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .

| Phone | Support Requirements |
|---|---|
| Cisco IP Conference Phone 8832 Multiplatform Phones | BroadSoft BroadWorks 22.0 MetaSphere CFS version 9.4 Asterisk 11.0 |

| Step 1 | Click the following URL: https://software.cisco.com/download/home/286311392 |
|---|---|
| Step 2 | In the middle pane, select IP Phone 8800 Series With Multiplatform Firmware . |
| Step 3 | Select IP Conference Phone 8832 With Multiplatform Firmware in the right pane. |
| Step 4 | Under Latest Release , select 11.2.3 MSR1-1 . |
| Step 5 | (Optional) Place your mouse pointer on the file name in the right pane, to see the file details and checksum values. |
| Step 6 | Download the cmterm-8832.11-2-3MSR1-1_REL.zip file. |
| Step 7 | Click Accept License Agreement . |
| Step 8 | Unzip the files. |
| Step 9 | Place the files in the TFTP, HTTP, or HTTPS download directory. |
| Step 10 | Upgrade the phone firmware with one of these methods. Upgrade the phone firmware from the phone administration web page: On the phone administration web page, go to Admin Login > Advanced > Voice > Provisioning tab, Firmware Upgrade section. In the Upgrade Rule field, enter the load file URL as described below. Load file URL format: <upgrade protocol>://<server ip address>[:<port>]>/<path>/<file name>.loads Example: https://10.73.10.223/firmware/sip8832.11-2-3MSR1-1.loads Click Submit All Changes . Upgrade the phone firmware directly from your web browser: In the address bar of your web browser, enter the phone upgrade URL as described below. Phone upgrade URL format: <phone protocol>://<phone ip address[:port]>/admin/upgrade?<load file URL> Load file URL format: <upgrade protocol>://<server ip address>[:<port>]>/<path>/<file name>.loads Example: https://10.74.10.225/admin/upgrade?https://10.73.10.223/firmware/ sip8832.11-2-3MSR1-1.loads Note Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. | Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |

| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
|---|---|

| Step 1 | Perform one of the following actions: To find all caveats, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319904&sb=anfr&bt=custV To find all open caveats, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319904&sb=anfr&sts=open&bt=custV To find all resolved caveats, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319904&sb=anfr&sts=fd&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter . |