---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-19x-3pcc-firmware-11-3-1-releasenotes-at9x-b-ata-191-192-rn-1131-html-c09954d69b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/19x/3PCC/firmware/11-3-1/releasenotes/at9x_b_ata-191_192-rn-1131.html
retrieved_at: 2026-08-21T12:50:00.595784+00:00
---

Cisco ATA 191 and 192 Analog Telephone Adapter Release Notes for Multiplatform Firmware Release 11.3(1)

# Cisco ATA 191 and 192 Analog Telephone Adapter Release Notes for Multiplatform Firmware Release 11.3(1)

### Download Options

Updated: April 10, 2025

First Published: April 10, 2025

# Release Notes

These release notes support the Cisco ATA 191 and 192 Analog Telephone Adapter for Multiplatform Firmware Release 11.3(1).

The following table lists the support and protocol compatibility for the Cisco ATA.

Cisco IP Phone

Protocol

Support Requirements

Cisco ATA 191 and 192

SIP

BroadSoft BroadWorks 24.0

Asterisk 13.1

## Cisco ATA 190 Series Documentation

Refer to publications that are specific to your language and call control system. Navigate from the following documentation
                     URL:

https://www.cisco.com/c/en/us/products/unified-communications/ata-190-series-analog-telephone-adapters/index.html

## Upgrade the Firmware

The Cisco ATA 191 and 192 Multiplatform support dual image upgrades by TFTP, HTTP, or HTTPS.

Step 1

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=286282490&flowid=83468

Step 2

Choose Cisco ATA 190 Series Analog Telephone Adapters .

Step 3

Choose your ATA model.

Step 4

In the Latest Releases folder, choose 11.3.1 .

Step 5

Download the file ATA19x.11-3-1MPP0001-191.zip.

Step 6

Unzip the files.

Step 7

Put the files on the TFTP/HTTP/HTTPS download directory.

Step 8

Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. The format is:

<schema>://<serv_ip[:port]>/filepath/ATA19x.xxxx.img

Here is an example,

http://192.168.1.100/firmware/ATA19x.11-3-1MPP0001-191.img

After the firmware upgrade completes, the phone reboots automatically.

## New and Changed Features

### Media Plane Security Negotiations

Your ATA now supports to initiate media plane security negotiations with a server. Your ATA can also work as a server to handle
                        the media plane security negotiations from a remote server.

The transport of negotiations between the ATA and the server can use SIP protocol over UDP, TCP, and TLS. You can limit that
                        the ATA initiates or handles media plane security negotiation only with SIP over TLS.

To configure this feature, use the fields MediaSec Request and MediaSec over TLS Only under the section SIP Settings from Voice > Line (n) in the ATA administration web page.

To use this feature, make sure that Secure Call Serv (under the section Supplementary Service Subscription ) is set to Yes , and Secure Call Option (under the section Call Feature Settings ) isn't set to Strict .

#### Where to Find More Information

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Provisioning Guide for Multiplatform Firmware

### MIC Certificate Renewal by SUDI Service

You can renew the ATA's Manufacture Installed Certificate (MIC) by a Cisco-hosted Secure Unique Device Identifier (SUDI) renewal
                        service. The MIC involves features that are related to SSL/TLS protocol. If the MIC expires, these features don't work until
                        you renew the certificate.

When this feature is configured, the ATA can download the renewed MIC certificate from a specified SUDI renewal service, and
                        will try to renew the MIC certificate if necessary.

To use this feature, use the fields MIC Cert Refresh Enable and MIC Cert Refresh Rule under the section MIC Cert Settings from Voice > Provisioning in the ATA administration web page.

#### Where to Find More Information

Cisco ATA 191 and ATA 192 Analog Telephone Adapter User Guide for Multiplatform Firmware

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Provisioning Guide for Multiplatform Firmware

### Password Changing Required

During your first-time login to the Phone Adapter Configuration Utility by using the default username and password, you are
                        required to change the existing password. Typically, this operation is required during the Out-Of-Box (OOB) or after the ATA
                        is reset to factory settings.

#### Where to Find More Information

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

### TLS 1.3 Support

Now the ATA can support the version 1.3 of the Transport Layer Security (TLS) protocol which can enhance the security and
                        performance.

You can configure the minimum version of TLS for the TLS connections on the ATA. To use the feature, configure the field TLS Min Version under the section Security Settings from Voice > System .

#### Where to Find More Information

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Provisioning Guide for Multiplatform Firmware

### Webex Calling Outbound Proxy Survivability Support

ATA can now register to the Local Survivable Gateway (LSG) nodes when Webex Calling SSE nodes are unreachable. When the ATA
                        connects to LSG nodes, it supports only limited set of calling features. When an SSE node is reachable, the ATA will fallback
                        to it after the specified interval (by default, 30 seconds).

To enable this feature from the ATA web page, use Survivability Proxy , Survivability Proxy Fallback Intvl fields under the Proxy and Registration section from Voice > Line (n) and Survivability Test Mode field under the Miscellaneous Settings section from Voice System .

#### Where to Find More Information

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Provisioning Guide for Multiplatform Firmware

Caveats

## View Caveats

You can search for caveats using the Cisco Bug Search.

Known caveats (bugs) are graded according to severity level, and can be either open or resolved.

Before you begin

### Before you begin

To view caveats, you need the following items:

Cisco.com user ID and password

Step 1

Use this URL for all and resolved caveats: https://bst.cloudapps.cisco.com/bugsearch?pf=prdNm&sb=fr&bt=custV&rls=11.3(1)MPP0001

Step 2

When prompted, log in with your Cisco.com user ID and password.

Step 3

(Optional) Enter the bug ID number in the Search for field, then press Enter .

## Open Caveats

There are no open caveats in this release.

## Resolved Caveats

The following list contains severity 1, 2, and 3 defects that are resolved for the Cisco ATA 191 and 192 Analog Telephone
                     Adapter Multiplatform Phones for Firmware Release 11.3(1)

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                     You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time this
                     report was compiled. For an updated view of open defects, access Bug Toolkit as described in View Caveats .

CSCwn07843: ATA 191 MPP does not honor the <Proxy_Fallback_Intvl> tag value

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Anything that degrades network performance can affect phone audio and, in some cases, can cause a call to drop. Sources of
                        network degradation can include, but are not limited to, the following activities:

Administrative tasks, such as an internal port scan or security scan.

Attacks that occur on your network, such as a Denial of Service attack.

### Caller Identification and Other Phone Functions

Caller identification or other phone functions have not been verified with third-party applications for the visually or hearing
                        impaired.

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see the Cisco IP Phone Firmware Support Policy .

| Cisco IP Phone | Protocol | Support Requirements |
|---|---|---|
| Cisco ATA 191 and 192 | SIP | BroadSoft BroadWorks 24.0 Asterisk 13.1 |

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=286282490&flowid=83468 |
|---|---|
| Step 2 | Choose Cisco ATA 190 Series Analog Telephone Adapters . |
| Step 3 | Choose your ATA model. |
| Step 4 | In the Latest Releases folder, choose 11.3.1 . |
| Step 5 | Download the file ATA19x.11-3-1MPP0001-191.zip. |
| Step 6 | Unzip the files. |
| Step 7 | Put the files on the TFTP/HTTP/HTTPS download directory. |
| Step 8 | Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. The format is: <schema>://<serv_ip[:port]>/filepath/ATA19x.xxxx.img Here is an example, http://192.168.1.100/firmware/ATA19x.11-3-1MPP0001-191.img After the firmware upgrade completes, the phone reboots automatically. |

| Step 1 | Use this URL for all and resolved caveats: https://bst.cloudapps.cisco.com/bugsearch?pf=prdNm&sb=fr&bt=custV&rls=11.3(1)MPP0001 |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) Enter the bug ID number in the Search for field, then press Enter . |