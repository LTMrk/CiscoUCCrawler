---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-6800-firmware-11-1-1sr3-p680-b-release-notes-for-6800mpp-1111sr3--9913d21809
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/6800/firmware/11-1-1sr3/p680_b_release-notes-for-6800mpp-1111sr3.html
retrieved_at: 2026-08-21T23:14:33.500310+00:00
---

Cisco IP Phone 6800 Series Multiplatform Phones Release Notes for Firmware Release 11.1(1)SR3

# Cisco IP Phone 6800 Series Multiplatform Phones Release Notes for Firmware Release 11.1(1)SR3

### Download Options

Updated: December 18, 2018

First Published: December 18, 2018

# Release Notes

Use these release notes with the following Cisco IP Phone 6800 Series Multiplatform Phones running SIP Firmware Release 11.1(1)SR3.

Cisco IP Phone 6841 Multiplatform Phones

Cisco IP Phone 6851 Multiplatform Phones

The following table describes the individual phone requirements.

Phone

Support Requirements

Cisco IP Phone 6841 and 6851 Multiplatform Phones

BroadSoft BroadWorks 21.0

MetaSphere CFS version 9.4

Asterisk 13.1

Related Documentation

## Cisco IP Phone 6800 Documentation

See the publications that are specific to your language, phone model, and multiplatform firmware release. Navigate from the
                     following Uniform Resource Locator (URL):

https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-6800-series-multiplatform-firmware/tsd-products-support-series-home.html

New and Changed Features

## Handset on Cisco IP Phone 6841 and 6851 Multiplatform Phones

For Cisco IP Phone 6841 and 6851 Multiplatform Phones , the WideBand Handset Enable field enables or disables the phone to use a wideband handset. By default, the system configures this field against the phone's
                     hardware version. The default setting is No for hardware version 00 and 01, and Yes for hardware version 02.

You can also change the setting as needed. If your phone is using a wideband handset, set this field to Yes .

The WideBand Handset Enable field is located in the General section of the Voice > Phone tab on the phone administration web page.

This feature has no user impact.

## Upgrade the Firmware

The Cisco IP Phone 6800 Series Multiplatform Phones support a single image upgrade using the TFTP, HTTP, or HTTPS protocols with a URL.

After the firmware upgrade completes, the phone reboots automatically.

Click the following URL:

https://software.cisco.com/download/navigator.html?mdfid=286318380&i=rm

Choose IP Phone 6800 Series with Multiplatform Firmware in the middle pane.

Choose your phone model in the right pane.

Choose the Multiplatform Firmware software type.

Under Latest , choose the 11.1.1 MSR3 folder.

(Optional) Place your mouse pointer on the filename to display the file details and checksum values.

Download the cp-68xx.11-1-1MSR3-1_REL.zip file.

Click Accept License Agreement when you accept the Cisco End User License.

Unzip the firmware files.

Put the files in the TFTP, HTTP, or HTTPS download directory.

Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL.

Use the URL format— <protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads

You can also upgrade the third-party call control by using a URL in the web browser—

<protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads

Example

https://10.74.10.225/firmware/sip68xx.11-1-1MSR3-1.loads

Use the *.loads file in the URL. The *.zip file contains other files.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Administrative
                              				tasks, such as an internal port scan or security scan

Attacks that
                              				occur on your network, such as a Denial of Service attack

### Caller Identification and Other Phone Functions

Caller identification or other phone functions have not been verified with third-party applications for the visually or hearing
                        impaired.

Caveats

## View Caveats

You can search for caveats using the Cisco Bug Search tool.

Known caveats (bugs) are graded according to severity level, and can be either open or resolved.

Before you begin

### Before you begin

To view the caveats, you need the following items:

Internet connection

Web browser

Cisco.com user ID and password

Perform one of the following actions:

To find all caveats, use this URL:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286318380&rls=11.1(1)&sb=anfr&bt=custV

To find all open caveats, use this URL:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286318380&rls=11.1(1)&sb=anfr&sts=open&bt=custV

To find all resolved caveats, use this URL:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286318380&rls=11.1(1)&sb=anfr&sts=fd&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional) To look for information about a specific problem, enter the bug ID number in the Search for field, and press Enter .

## Open Caveats

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Phone 6800 Series Multiplatform Phones that use Firmware Release 11.1(1)SR3.

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                     tool and entering the Identifier. You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were open at the time this
                     report was compiled. For an updated view of the open defects or to view specific bugs, access the Bug Search Toolkit as described
                     in the View Caveats .

CSCvg00958 Phone doesn't send 420 Bad Extension when it receives INVITE with unsupported value

CSCvg10304 Dual Mode and IP Pref is IPv4, Phone does not fallback to IPv4 when IPv4 is up

CSCvg42260 Sometimes packet capture may not be terminated

CSCvg59538 No record in reboot reason when the reboot is triggered by vlan change in IPv6 only mode

CSCvg61600 Geolocation status messages show up in English words with other locale

CSCvg63918 Phone still uses the old device after changing preferred audio device in ringback status

CSCvg70042 Wrong LED when DUT is configured call park shared-line ext function with wrong IP as PROXY

CSCvg75579 Resync failed while using Digest Authentication with valid long password and username

CSCvg77675 Select line key fail when barge fail

CSCvg83031 Call center queue states can not show "full", when queue threshold is exceeded.

CSCvg84786 Provisioning Status shows incorrect while use no <flat-profile> in resync file

CSCvg96811 Hoteling subscribe will not retry after server unreachable or response error.

CSCvh02982 Initiate Paging call during upgrade, and the upgrade will fail after the call is terminated

CSCvh13556 Parameter RTP Packet Size validation does not work

CSCvh16152 MOS data is all zeroes in first second, phone should not send out this invalid data

CSCvh17328 Recent call xmpp status is not updated when change xmpp presence to offline

CSCvh17346 Configuration, "Login Invisible" does not work when user login

CSCvh19488 Generate PRT will make phone reboot when "PRT Upload Rule" can't be queried by DNS in HK locale

CSCvh23468 RFC2833 DTMF digits failing with AMR-WB mode

CSCvh29624 Phone does not preserve the existing call when on secondary SBC and failover to primary SBC

CSCvh52720 Ignore group paging on active call cannot work

CSCvh52884 Paging call can be answered when paging service disabled

CSCvh66529 Phone reboots - Not handling multipart/mixed and multipart/related MIME type properly

CSCvh69377 The max name length of Auto defined sd is inconsistent with normal sd

CSCvh71029 Change of Hold Reminder Timer by resync will cause phone reboot

CSCvh71043 Phone will reboot after received illegal value % for parameter

CSCvh72506 Phone doesn't use the last DNS cached record if TTL expire and no response from DNS server

CSCvh76496 Phone cannot get the correct content from HTTP 301 response

CSCvh76520 Phone will always report download fail when receive 301 after reboot

CSCvh76689 Phone cannot handle the content from HTTP 302 response

CSCvh76791 Provisioning Status is wrong when receive 500/501/503

CSCvh78587 Phone can't accept a long realm in 401 when upgrade

## Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 6800 Series Multiplatform Phones that use Firmware Release 11.1(1)SR3.

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                     tool and entering the Identifier. You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                     this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                     as described in the View Caveats .

CSCvm04387 494 Security Agreement Required: Error not handled

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .

| Phone | Support Requirements |
|---|---|
| Cisco IP Phone 6841 and 6851 Multiplatform Phones | BroadSoft BroadWorks 21.0 MetaSphere CFS version 9.4 Asterisk 13.1 |

| Step 1 | Click the following URL: https://software.cisco.com/download/navigator.html?mdfid=286318380&i=rm |
|---|---|
| Step 2 | Choose IP Phone 6800 Series with Multiplatform Firmware in the middle pane. |
| Step 3 | Choose your phone model in the right pane. |
| Step 4 | Choose the Multiplatform Firmware software type. |
| Step 5 | Under Latest , choose the 11.1.1 MSR3 folder. |
| Step 6 | (Optional) Place your mouse pointer on the filename to display the file details and checksum values. |
| Step 7 | Download the cp-68xx.11-1-1MSR3-1_REL.zip file. |
| Step 8 | Click Accept License Agreement when you accept the Cisco End User License. |
| Step 9 | Unzip the firmware files. |
| Step 10 | Put the files in the TFTP, HTTP, or HTTPS download directory. |
| Step 11 | Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. Use the URL format— <protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads You can also upgrade the third-party call control by using a URL in the web browser— <protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads Example https://10.74.10.225/firmware/sip68xx.11-1-1MSR3-1.loads Note Use the *.loads file in the URL. The *.zip file contains other files. | Note | Use the *.loads file in the URL. The *.zip file contains other files. |
| Note | Use the *.loads file in the URL. The *.zip file contains other files. |

| Note | Use the *.loads file in the URL. The *.zip file contains other files. |
|---|---|

| Step 1 | Perform one of the following actions: To find all caveats, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286318380&rls=11.1(1)&sb=anfr&bt=custV To find all open caveats, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286318380&rls=11.1(1)&sb=anfr&sts=open&bt=custV To find all resolved caveats, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286318380&rls=11.1(1)&sb=anfr&sts=fd&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) To look for information about a specific problem, enter the bug ID number in the Search for field, and press Enter . |