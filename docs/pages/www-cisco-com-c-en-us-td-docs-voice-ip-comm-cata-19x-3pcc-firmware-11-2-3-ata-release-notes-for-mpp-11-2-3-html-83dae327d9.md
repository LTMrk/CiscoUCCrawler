---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-19x-3pcc-firmware-11-2-3-ata-release-notes-for-mpp-11-2-3-html-83dae327d9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/19x/3PCC/firmware/11-2-3/ATA-Release-Notes-for-MPP-11-2-3.html
retrieved_at: 2026-08-21T12:50:17.630269+00:00
---

Cisco ATA 191 and 192 Analog Telephone Adapter Release Notes for Multiplatform Firmware Release 11.2(3)

# Cisco ATA 191 and 192 Analog Telephone Adapter Release Notes for Multiplatform Firmware Release 11.2(3)

### Download Options

Updated: November 3, 2022

What’s new in this release . 3

Resolved bugs . 3

Bug Search Tool 4

Upgrade the Firmware . 4

Related Documentation . 5

These release notes support Cisco ATA 191 and 192 Analog Telephone Adapter for Multiplatform Firmware Release 11.2(3).

The following table lists the support and protocol compatibility for Cisco ATA.

Cisco IP Phone

Protocol

Support Requirements

Cisco ATA 191 and 192

SIP

BroadSoft BroadWorks 24.0

Asterisk 13.1

What’s new in this release

Http Proxy Support

You can set up the ATA to connect to the Internet through a specified HTTP proxy server. Choose the Auto or Manual proxy mode to specify the target proxy server.

To enable this feature, configure the fields from Network > Application > HTTP Proxy in the ATA administration web page.

#### Where to Find More Information

· Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

· Cisco ATA 191 and ATA 192 Analog Telephone Adapter Provisioning Guide for Multiplatform Firmware

Resolved bugs

Bug number

Severity

Affected product area

Description

C SCwd13310

3

Voice

ATA19x Audio lost or delayed during the first few seconds after answering call from hunt group

C SCwd13332

3

On boarding

ATA19x will not onboard over EDOS server when invalid DHCP provisioning server is detected

CSCwd03677

3

Voice

MPP ATA19x Gain setting doesn't take effect

CSCwc99394

3

On boarding

MPP ATA19x SIP line doesn’t register automatically if first DNS query is failed

CSCwc43262

3

Fax

MPP ATA19x T38 Incoming Fax failure due to CFR isn’t properly relayed

Bug Search Tool

We report open and resolved customer-found bugs of severity 1 to 3. You can find details about listed bugs and search for other bugs by using the Cisco Bug Search Tool. For more info on using the Bug Search, see Bug Search Tool Help .

### Before you begin

To view caveats, you need the following items:

· Cisco.com user ID and password

· Step 1 Use this URL for all and resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=ata11.2.3&pf=prdNm&sb=fr&sts=fd&svr=6nH&bt=custV

· Step 2 When prompted, log in with your Cisco.com user ID and password.

· Step 3 (Optional) E nter the bug ID number in the Search for field, then press Enter .

Upgrade the Firmware

The Cisco ATA 191 and 192 support dual image upgrades by TFTP, HTTP, or HTTPS.

Step 1

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=286282490&flowid=83468

Step 2

Choose Cisco ATA 190 Series Analog Telephone Adapters .

Step 3

Choose your ATA model.

Step 4

In the Latest Releases folder, choose 11.2.3 .

Step 5

Download the file ATA19x.11-2-3MPP0001-028.zip.

Step 6

Unzip the files.

Step 7

Put the files on the tftp/http/https download directory.

Step 8

Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. The format is:

<schema>://<serv_ip[:port]>/filepath/ATA19x.xxxx.img

Here is an example,

http://192.168.1.100/firmware/ATA19x.11-2-3MPP0001-028.img

After the firmware upgrade completes, the phone reboots automatically.

Related Documentation

Use the following sections to obtain related information.

### Cisco ATA 190 Series Documentation

Refer to publications that are specific to your language and call control system. Navigate from the following documentation URL:

https://www.cisco.com/c/en/us/products/unified-communications/ata-190-series-analog-telephone-adapters/index.html

| Cisco IP Phone | Protocol | Support Requirements |
|---|---|---|
| Cisco ATA 191 and 192 | SIP | BroadSoft BroadWorks 24.0 Asterisk 13.1 |

| Bug number | Severity | Affected product area | Description |
|---|---|---|---|
| C SCwd13310 | 3 | Voice | ATA19x Audio lost or delayed during the first few seconds after answering call from hunt group |
| C SCwd13332 | 3 | On boarding | ATA19x will not onboard over EDOS server when invalid DHCP provisioning server is detected |
| CSCwd03677 | 3 | Voice | MPP ATA19x Gain setting doesn't take effect |
| CSCwc99394 | 3 | On boarding | MPP ATA19x SIP line doesn’t register automatically if first DNS query is failed |
| CSCwc43262 | 3 | Fax | MPP ATA19x T38 Incoming Fax failure due to CFR isn’t properly relayed |

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=286282490&flowid=83468 |
|---|---|
| Step 2 | Choose Cisco ATA 190 Series Analog Telephone Adapters . |
| Step 3 | Choose your ATA model. |
| Step 4 | In the Latest Releases folder, choose 11.2.3 . |
| Step 5 | Download the file ATA19x.11-2-3MPP0001-028.zip. |
| Step 6 | Unzip the files. |
| Step 7 | Put the files on the tftp/http/https download directory. |
| Step 8 | Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. The format is: <schema>://<serv_ip[:port]>/filepath/ATA19x.xxxx.img Here is an example, http://192.168.1.100/firmware/ATA19x.11-2-3MPP0001-028.img After the firmware upgrade completes, the phone reboots automatically. |