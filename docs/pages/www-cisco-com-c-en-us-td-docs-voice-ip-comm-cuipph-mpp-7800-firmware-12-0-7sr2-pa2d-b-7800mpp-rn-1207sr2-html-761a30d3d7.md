---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-7800-firmware-12-0-7sr2-pa2d-b-7800mpp-rn-1207sr2-html-761a30d3d7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/7800/firmware/12-0-7sr2/pa2d_b_7800mpp-rn-1207sr2.html
retrieved_at: 2026-08-17T01:09:54.564667+00:00
---

Cisco IP Phone 7800 Series Multiplatform Phones Release Notes for Firmware Release 12.0(7)SR2

# Cisco IP Phone 7800 Series Multiplatform Phones Release Notes for Firmware Release 12.0(7)SR2

### Download Options

Updated: June 26, 2025

First Published: June 26, 2025

# Release Notes

Use these release notes with the Cisco IP Phone 7800 Series Multiplatform Phones running SIP Firmware Release 12.0(7)SR2.

The following table describes the individual phone requirements.

Phone

Support Requirements

Cisco IP Phone 7800 Series Multiplatform Phones

Cisco BroadWorks RI

Asterisk 20

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Phone 7800 Series Documentation

See the publications that are specific to your language, phone model, and multiplatform firmware release. Navigate from the
                        following Uniform Resource Locator (URL):

https://www.cisco.com/c/en/us/products/collaboration-endpoints/ip-phone-7800-series-multiplatform-firmware/index.html

## New and Changed Features

### Set password on first login

As of Firmware Release 12.0(7)SR2, it's mandatory to set up the passwords before the phone's initial registration (Out-Of-Box)
                        when both the user and admin passwords are empty. It is also required to set up the passwords after a factory reset. Anyone
                        who accesses the phone web page is requested to set passwords for both the administrator and the user during the OOB stage.
                        The passwords must comply with the password rules.

Sometimes it may be difficult to enter user passwords on a phone since a password may consist of capital letters, small letters,
                                 numbers, and special characters. Despite the complex password defined on the phone web interface, a system administrator can
                                 provide a simple or even blank password to a user through provisioning as a workaround.

#### Where to Find More Information

Cisco IP Desk Phone with Multiplatform Firmware (MPP) - Administration Guide

### Update TLS Minimum Value

With Firmware Release 12.0(7)SR2, the default minimum TLS value of the phone is TLS 1.2.

When the phone functions as a client, the legacy option of TLS Min Version is now renamed to TLS Client Min Version . The corresponding XML parameter in the phone configuration file (cfg.xml) is updated to <TLS_Client_Min_Version>.

If you are working with your own configuration file, the previous <TLS_Min_Version> parameter still works. However, avoid
                                 using both <TLS_Client_Min_Version> and <TLS_Min_Version> in the same configuration file.

When the phone functions as a server, you can control the minimum TLS value with the new TLS Server Min Version option under Voice > System > Security Settings on the phone administration web page.

#### Where to Find More Information

Cisco IP Desk Phone with Multiplatform Firmware (MPP) - Administration Guide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

### Generate Log Information for Certain Activities

As of Firmware Release 12.0(7)SR2, your phone generates and sends logging messages for the following events to a syslog server.

Web

Admin/user successful login/logout

Admin/user rejected login attempt

Admin/user password change

Web  server service on/off

Personal directory

Create/Update/Delete on LCD or web

Call history

Delete call history on LCD or web

LCD PIN

Successful unlock

Rejected unlock attempt

## Upgrade the Firmware

You can upgrade the phone firmware with TFTP, HTTP, or HTTPS. After the upgrade completes, the phone reboots automatically.

### SUMMARY STEPS

- Click this link:

- Select your phone model in the right pane.

- On the next page that is displayed, select Multiplatform Firmware .

- Under Latest Release , select 12.0.7SR2 .

- (Optional) Place your mouse pointer on the file name to see the file details and checksum values.

- Download the corresponding file.

- Click Accept License Agreement .

- Unzip the file and place the files in the appropriate location on your upgrade server.

- Upgrade the phone firmware with one of these methods.

Upgrade the phone firmware from the phone administration web page:

On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade .

In the Upgrade Rule field, enter the load file URL as described below.

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads

Examples:

http://10.73.10.223/firmware/sip78xx.12-0-7MPP0201-66.loads

https://server.domain.com/firmware/sip78xx.12-0-7MPP0201-66.loads

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads

Examples:

http://10.74.10.225/admin/upgrade?http://10.73.10.223/firmware/sip78xx.12-0-7MPP0201-66.loads

https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip78xx.12-0-7MPP0201-66.loads

### DETAILED STEPS

Step 1

Click this link:

https://software.cisco.com/download/home/286311392

On the Software Download web page that is displayed, ensure that IP Phone 7800 Series with Multiplatform Firmware is selected in the middle pane.

Step 2

Select your phone model in the right pane.

Step 3

On the next page that is displayed, select Multiplatform Firmware .

Step 4

Under Latest Release , select 12.0.7SR2 .

Step 5

(Optional) Place your mouse pointer on the file name to see the file details and checksum values.

Step 6

Download the corresponding file.

cmterm-78xx.12-0-7MPP0201-66_REL.zip

Step 7

Click Accept License Agreement .

Step 8

Unzip the file and place the files in the appropriate location on your upgrade server.

The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                 upgrade.

Step 9

Upgrade the phone firmware with one of these methods.

Upgrade the phone firmware from the phone administration web page:

On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade .

In the Upgrade Rule field, enter the load file URL as described below.

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads

Examples:

http://10.73.10.223/firmware/sip78xx.12-0-7MPP0201-66.loads

https://server.domain.com/firmware/sip78xx.12-0-7MPP0201-66.loads

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads

Examples:

http://10.74.10.225/admin/upgrade?http://10.73.10.223/firmware/sip78xx.12-0-7MPP0201-66.loads

https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip78xx.12-0-7MPP0201-66.loads

Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Administrative tasks, such as an internal port scan or security scan.

Attacks that occur on your network, such as a Denial of Service attack.

Caveats

## View Caveats

You can search for caveats (bugs) with the Cisco Bug Search tool.

Known caveats are graded according to severity level, and are either open or resolved.

Before you begin

### Before you begin

### SUMMARY STEPS

- Click one of the following links:

- When prompted, log in with your Cisco.com user ID and password.

- (Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter .

### DETAILED STEPS

Step 1

Click one of the following links:

To view all caveats that affect this release:

To view open caveats that affect this release:

To view resolved caveats that affect this release:

Step 2

When prompted, log in with your Cisco.com user ID and password.

Step 3

(Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter .

## Open Caveats

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Phone 7800 Series Multiplatform Phones that use Firmware Release 12.0(7)SR2.

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                     tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                     this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                     as described in the View Caveats .

CSCwf10956—Macro $SERVIP is not expanded in Log Request Msg in syslog.

CSCwb46008—Many PRTs with logs missing for around 5 seconds.

## Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 7800 Series Multiplatform Phones that use Firmware Release 12.0(7)SR2.

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                     tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                     this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                     as described in View Caveats .

CSCwo65986—MPP phones rejecting INVITEs with specific headers.

CSCwn74481—MPP missing the beginning audio from a voicemail server.

CSCwn84785—MPP Phones nightly resync is not rebooting the phones - Changes work only after a reboot.

CSCwm05273—A slight clicking sound can be heard when resuming a held call.

CSCwo34585—MPP // Web Proxy is Ignored for GDS Onboarding.

CSCwp37769—Broadworks MPP, Crash on Incoming Call for long Call-ID.

## Cisco IP Phone Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .

| Phone | Support Requirements |
|---|---|
| Cisco IP Phone 7800 Series Multiplatform Phones | Cisco BroadWorks RI Asterisk 20 |

| Note | Sometimes it may be difficult to enter user passwords on a phone since a password may consist of capital letters, small letters,
                                 numbers, and special characters. Despite the complex password defined on the phone web interface, a system administrator can
                                 provide a simple or even blank password to a user through provisioning as a workaround. |
|---|---|

| Note | If you are working with your own configuration file, the previous <TLS_Min_Version> parameter still works. However, avoid
                                 using both <TLS_Client_Min_Version> and <TLS_Min_Version> in the same configuration file. |
|---|---|

| Step 1 | Click this link: https://software.cisco.com/download/home/286311392 On the Software Download web page that is displayed, ensure that IP Phone 7800 Series with Multiplatform Firmware is selected in the middle pane. |
|---|---|
| Step 2 | Select your phone model in the right pane. |
| Step 3 | On the next page that is displayed, select Multiplatform Firmware . |
| Step 4 | Under Latest Release , select 12.0.7SR2 . |
| Step 5 | (Optional) Place your mouse pointer on the file name to see the file details and checksum values. |
| Step 6 | Download the corresponding file. cmterm-78xx.12-0-7MPP0201-66_REL.zip |
| Step 7 | Click Accept License Agreement . |
| Step 8 | Unzip the file and place the files in the appropriate location on your upgrade server. The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                 upgrade. |
| Step 9 | Upgrade the phone firmware with one of these methods. Upgrade the phone firmware from the phone administration web page: On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade . In the Upgrade Rule field, enter the load file URL as described below. Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads Examples: http://10.73.10.223/firmware/sip78xx.12-0-7MPP0201-66.loads https://server.domain.com/firmware/sip78xx.12-0-7MPP0201-66.loads Click Submit All Changes . Upgrade the phone firmware directly from your web browser: In the address bar of your web browser, enter the phone upgrade URL as described below. Phone upgrade URL format: <phone protocol>://<phone ip address[:port]>/admin/upgrade?<load file URL> Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads Examples: http://10.74.10.225/admin/upgrade?http://10.73.10.223/firmware/sip78xx.12-0-7MPP0201-66.loads https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip78xx.12-0-7MPP0201-66.loads Note Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. | Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |

| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
|---|---|

| Step 1 | Click one of the following links: To view all caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?pf=prdNm&sb=anfr&prdNam=Cisco%20IP%20Phone%207800%20Series%20with%20Multiplatform%20Firmware&kw=*&bt=custV&rls=12.0(7) To view open caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?pf=prdNm&sb=afr&kw=*&bt=custV&rls=12.0(7)&prdNam=Cisco%20IP%20Phone%207800%20Series%20with%20Multiplatform%20Firmware To view resolved caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?pf=prdNm&sb=fr&kw=*&bt=custV&rls=12.0(7)&prdNam=Cisco%20IP%20Phone%207800%20Series%20with%20Multiplatform%20Firmware |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter . |