---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-dx-series-rel-notes-1023sr1-dx00-bk-r1761000-00-release-notes-dx-series-1023-e8ff67df13
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/dx/series/rel-notes/1023sr1/DX00_BK_R1761000_00_release-notes-dx-series-1023sr.html
retrieved_at: 2026-08-22T00:57:26.936711+00:00
---

Release Notes for Cisco DX Series Firmware Release 10.2(3)SR1

# Release Notes for Cisco DX Series Firmware Release 10.2(3)SR1

### Download Options

Updated: January 29, 2015

First Published: January 29, 2015

Last Updated: April 24, 2015

# Release Notes

## New and Changed Features

There are no new or changed features for this release.

### Installation Notes

#### System Requirements

Cisco DX Series devices are supported by Cisco Unified Communications Manager Release 8.5(1), 8.6(1), 8.6(2), 9.1(2), 10.5(1) and later.

The initial release of Cisco DX Series devices requires the latest device pack installed on each Cisco Unified Communications Manager release.

#### Install Firmware Release on Cisco Unified Communications Manager

Before using the Cisco DX Series  firmware release on the Cisco Unified Communications Manager, you must install the latest Cisco Unified Communications Manager firmware on all Cisco Unified Communications Manager servers in the cluster.

- For Cisco DX70: cmterm-dx70.10-2-3-33.cop.sgn

- For Cisco DX80: cmterm-dx80.10-2-3-33.cop.sgn

- For Cisco DX650:  cmterm-dx650.10-2-3-33.cop.sgn

- For all Cisco DX Series devices: cmterm-dxseries.10-2-3-33.cop.sgn

#### Install Firmware ZIP Files

If a Cisco Unified Communications Manager is not available to load the installer program, the following .zip files are available to load the firmware.

Firmware upgrades over the WLAN interface may take longer than upgrades that use  a wired connection. Upgrade times over the WLAN interface may take more than an hour, depending on the quality and bandwidth of the wireless connection.

- For Cisco DX70: cmterm-dx70.10-2-3-33.zip

- For Cisco DX80: cmterm-dx80.10-2-3-33.zip

- For Cisco DX650:  cmterm-dx650.10-2-3-33.zip

### Important Note

#### Cisco Virtual Office Setup

In a Cisco Virtual Office setup, Cisco  recommends the use of a Cisco 881 Integrated Services Router instead of the Cisco 871 router.

### Limitations and Restrictions

When a user is sharing their computer desktop in a Cisco DX70 or Cisco DX80 presentation call, any audio from the desktop is not shared.

Users should only pair their mobile phone with one Cisco DX Series device at a time.

The only supported external cameras for Cisco DX650 are the Logitech C920-C Webcam and Logitech C930e.

Cisco DX Series devices do not support Android apps that require  portrait mode, GPS, or Accelerometer. However, apps that support both portrait and landscape are supported in landscape mode.

Use the Google Play Store to find and add applications to your phone. Depending on your security settings, the Google Play Store may not be available. Cisco does not guarantee that an application that you download from a third-party site will work.

For Cisco DX70 ,  the HDMI Out port is enabled. However, the HDMI Out port only supports mirror mode.

For Cisco DX80 , the HDMI Out port is disabled.

To prevent unauthorized copying of Digital Rights Management (DRM) protected HD video through the HDMI port, an HDMI monitor (or any HDMI sink device) that is connected to a Cisco DX650 or a Cisco DX70 must be HDCP compliant.

- Cisco DX650 devices labeled with TAN 68-5217-xx cannot be downgraded below version 10.2(2)

#### Device Redistribution

When an administrator redistributes a device (that is, gives the device  to a different user), the administrator should execute a factory reset of the device to remove any user data that was previously stored on the device.

If an administrator changes the user ID of a device  from user A to user B, none of the data that is associated with user A will be available to user B. The new user must download apps and other data. This scenario may apply to a single user that changes from an old  user ID to a new user ID.

#### Behavior During Times of Network Congestion

Anything that degrades network performance can
affect  voice
and video quality, and in some cases, can
cause a call to drop. Sources of
network degradation can include, but are not limited to, the
following activities:

Administrative
tasks, such as an internal port scan or security scan

Attacks that
occur on your network, such as a Denial of Service
attack

To reduce or eliminate any adverse effects, schedule administrative network tasks during a
time when the devices are not being used or exclude the devices
from testing.

### Supported Languages

### View Caveats

You can search for
		  problems by using the Cisco Bug Search. 
		To access Cisco Bug
		  Search, you need a Cisco.com user
				ID and password.

Known caveats
		  (bugs) are graded according to severity level, and can either be open or resolved.

### Documentation, Service Requests, and Additional Information

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​general/​whatsnew/​whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application. The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

#### Related Documentation

##### Cisco Unified Communications Manager

See the Cisco Unified Communications Manager Documentation Guide and other
		  publications that are specific to your Cisco Unified Communications Manager release. Navigate from the following
		  documentation URL:

http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​unified-communications-manager-callmanager/​tsd-products-support-series-home.html

##### Cisco Business Edition 6000

Refer to the Cisco
			 Business Edition 6000 Documentation Guide and other publications that
		  are specific to your Cisco Business Edition 6000 release. Navigate from the
		  following URL:

http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​business-edition-6000/​tsd-products-support-series-home.html

##### Cisco and the Environment

Related
		  publications are available at the following URL:

http:/​/​www.cisco.com/​go/​ptrdocs

### This Document Applies to These Products

- Webex DX80

| Step 1 | Go to the following URL: http:/​/​software.cisco.com/​download/​navigator.html . |
|---|---|
| Step 2 | Choose Collaboration Endpoints > Collaboration Desk Endpoints > Cisco DX Series . |
| Step 3 | Choose your device type. |
| Step 4 | In the Latest Releases folder, choose 10.2(3) . |
| Step 5 | Select one of the following firmware files,  click the Download or Add to cart button, and follow the prompts: For Cisco DX70: cmterm-dx70.10-2-3-33.cop.sgn For Cisco DX80: cmterm-dx80.10-2-3-33.cop.sgn For Cisco DX650:  cmterm-dx650.10-2-3-33.cop.sgn For all Cisco DX Series devices: cmterm-dxseries.10-2-3-33.cop.sgn Note If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. | Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Step 6 | Click the arrow next to the firmware file name in the Download Cart section to access additional information about this file. The link for the readme file is in the Additional Information section. The readme file contains installation instructions for the corresponding firmware. |
| Step 7 | Follow the instructions in the readme file to install the firmware. |

| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
|---|---|

| Step 1 | Go to the following URL: http:/​/​software.cisco.com/​download/​navigator.html . |
|---|---|
| Step 2 | Choose Collaboration Endpoints > Collaboration Desk Endpoints > Cisco DX Series . |
| Step 3 | Choose your device type. |
| Step 4 | In the Latest Releases folder, choose 10.2(3) . |
| Step 5 | Download the relevant zip files. For Cisco DX70: cmterm-dx70.10-2-3-33.zip For Cisco DX80: cmterm-dx80.10-2-3-33.zip For Cisco DX650:  cmterm-dx650.10-2-3-33.zip |
| Step 6 | Unzip the files. |
| Step 7 | Manually copy the unzipped files to the
directory on the TFTP server. See Cisco Unified Communications Operating System
Administration Guide for information about how to manually copy the
firmware files to the server. |

| Arabic, Egypt ( ar_EG ) | French, France ( fr_FR ) | Portuguese, Brazil ( pt_BR ) |
|---|---|---|
| Bulgarian, Bulgaria ( bg_BG ) | German, Germany ( de_DE ) | Portuguese, Portugal ( pt_PT ) |
| Catalan, Spain ( ca_ES ) | Greek, Greece ( el_GR ) | Romanian, Romania ( ro_RO ) |
| Chinese, PRC ( zh_CN ) | Hebrew, Israel ( he_IL ) | Russian ( ru_RU ) |
| Chinese, Taiwan ( zh_TW ) | Hungarian, Hungary ( hu_HU ) | Serbian, Republic of Serbia ( sr_RS ) |
| Croatian, Croatia ( hr_HR ) | Italian, Italy ( it_IT ) | Slovak, Slovakia ( sk_SK ) |
| Czech, Czech Republic ( cs_CZ ) | Japanese ( ja_JP ) | Slovenian, Slovenia ( sl_SI ) |
| Danish, Denmark ( da_DK ) | Korean ( ko_KR ) | Spanish, Spain ( es_ES ) |
| Dutch, Netherlands ( nl_NL ) | Latvian, Latvia ( lv_LV ) | Swedish, Sweden ( sv_SE ) |
| English, Britain ( en_GB ) | Lithuanian, Lithuania ( lt_LT ) | Thai, Thailand ( th_TH ) |
| English, US ( en_US ) | Norwegian bokmål , Norway ( nb_NO ) | Turkish, Turkey ( tr_TR ) |
| Finnish, Finland ( fi_FI ) | Polish ( pl_PL ) |  |

| Step 1 | Perform one of the following actions: |
|---|---|
| Step 2 | Log in with your
			 Cisco.com user ID and password. |
| Step 3 | To look for
			 information about a specific problem, enter the bug ID number in the Search for
			 field, then press Enter . |