---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-8832-firmware-11-2-3-cs88-b-rn-mpp-1123-html-0f76315c2b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/8832/firmware/11-2-3/cs88_b_rn-mpp-1123.html
retrieved_at: 2026-08-21T13:43:28.468978+00:00
---

Cisco IP Conference Phone 8832 Multiplatform Phones Release Notes for Firmware Release 11.2(3)

# Cisco IP Conference Phone 8832 Multiplatform Phones Release Notes for Firmware Release 11.2(3)

### Download Options

Updated: January 30, 2019

First Published: January 30, 2019

# Release Notes

Use these release notes with Cisco IP Conference Phone 8832 Multiplatform Phones running SIP Firmware Release 11.2(3).

The following table describes the individual phone requirements.

Phone

Support Server

BroadSoft BroadWorks 22.0

MetaSphere CFS version 9.4

Asterisk 11.0

## Cisco IP Conference Phone 8832 Multiplatform Phones

The Cisco IP Conference Phone 8832 Multiplatform Phones provides high‑definition (HD) audio performance and 360-degree coverage for medium to large conference rooms and executive
                     offices.

The new phone has the following features:

Wideband (G.722) for crystal-clear audio performance: The conference phone has sensitive microphones that let you speak in
                           a normal voice and be clearly heard from up to 10 feet (2.1 m) away.

360-degree coverage or rooms up to 800 square feet (74.3 square meters) with wired and DECT wireless expansion microphone
                           options: You can connect two wired expansion microphones to the phone to increase coverage in larger conference rooms. The
                           phone also supports an optional set of two wireless expansion microphones. The phone can be used for a 20 x 20 foot (6.1 x
                           6.1 m) room and up to 10 people. When you add the expansion microphones, coverage extends to a 20 x 34 foot (6.1 x 10 m) room
                           and up to 26 people.

Backlit, antiglare, color pixel display eases viewing and navigation

Same easy-to-use call experience as other 8800 Series Multiplatform IP Phones

### Where to Find More Information

Cisco IP Conference Phone 8832 Multiplatform Phones Administration Guide

Cisco IP Conference Phone 8832 Multiplatform Phones User Guide

Cisco IP Conference Phone 8832 Multiplatform Phones Provisioning Guide

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Phone
                  	 8800 Series Documentation

See the publications that are specific to your language, phone model,
                        		  and multiplatform firmware release. Navigate from the following Uniform
                        		  Resource Locator (URL):

https://www.cisco.com/c/en/us/products/collaboration-endpoints/ip-phone-8800-series-multiplatform-firmware/index.html

## Upgrade the Firmware

You can upgrade the phone firmware with TFTP, HTTP, or HTTPS. After the upgrade completes, the phone reboots automatically.

Click this link:

https://software.cisco.com/download/home/286311392

On the Software Download web page that is displayed, ensure that IP Phone 8800 Series with Multiplatform Firmware is selected in the middle pane.

Select your phone model in the right pane.

On the next page that is displayed, select Multiplatform Firmware .

On the next page that is displayed, select 11.2.3 in the All Releases > MPPv11 folder.

(Optional) Place your mouse pointer on the file name to see the file details and checksum values.

Download the firmware cmterm-8832.11-2-3MPP-398_REL.zip file:

For Cisco IP Phone 8832 Multiplatform Phones: cmterm-8832.11-2-3MPP-398_REL.zip

Click Accept License Agreement .

Unzip the file and place the files in the appropriate location on your upgrade server.

The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                 upgrade.

Upgrade the phone firmware with one of these methods.

Upgrade the phone firmware from the phone administration web page:

On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade .

In the Upgrade Rule field, enter the load file URL as described below.

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads

Example:

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads

Example:

https://10.74.10.225/admin/upgrade?https://10.73.10.223/firmware/sip8832.11-2-3MPP-398.loads

Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Administrative
                              				tasks, such as an internal port scan or security scan

Attacks that
                              				occur on your network, such as a Denial of Service attack

## Caveats

No caveats listed for the Firmware Release 11.2(3).

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .

| Phone | Support Server |
|---|---|
| Cisco IP Conference Phone 8832 Multiplatform Phones | BroadSoft BroadWorks 22.0 MetaSphere CFS version 9.4 Asterisk 11.0 |

| Step 1 | Click this link: https://software.cisco.com/download/home/286311392 On the Software Download web page that is displayed, ensure that IP Phone 8800 Series with Multiplatform Firmware is selected in the middle pane. |
|---|---|
| Step 2 | Select your phone model in the right pane. |
| Step 3 | On the next page that is displayed, select Multiplatform Firmware . |
| Step 4 | On the next page that is displayed, select 11.2.3 in the All Releases > MPPv11 folder. |
| Step 5 | (Optional) Place your mouse pointer on the file name to see the file details and checksum values. |
| Step 6 | Download the firmware cmterm-8832.11-2-3MPP-398_REL.zip file: For Cisco IP Phone 8832 Multiplatform Phones: cmterm-8832.11-2-3MPP-398_REL.zip |
| Step 7 | Click Accept License Agreement . |
| Step 8 | Unzip the file and place the files in the appropriate location on your upgrade server. The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                 upgrade. |
| Step 9 | Upgrade the phone firmware with one of these methods. Upgrade the phone firmware from the phone administration web page: On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade . In the Upgrade Rule field, enter the load file URL as described below. Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads Example: https://10.73.10.223/firmware/sip8832.11-2-3MPP-398.loads Click Submit All Changes . Upgrade the phone firmware directly from your web browser: In the address bar of your web browser, enter the phone upgrade URL as described below. Phone upgrade URL format: <phone protocol>://<phone ip address[:port]>/admin/upgrade?<load file URL> Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads Example: https://10.74.10.225/admin/upgrade?https://10.73.10.223/firmware/sip8832.11-2-3MPP-398.loads Note Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. | Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |

| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
|---|---|