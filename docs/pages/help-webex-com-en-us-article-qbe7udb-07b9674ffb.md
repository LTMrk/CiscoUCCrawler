---
doc_id: help-webex-com-en-us-article-qbe7udb-07b9674ffb
source_url: https://help.webex.com/en-us/article/qbe7udb
retrieved_at: 2026-11-02T12:57:30.805239+00:00
---

## ActiveControl overview

ActiveControl is a solution that bridges conferencing information between the Webex cloud and the premises. Before this solution, Webex App app users in multiparty calls were already seeing information on which other participants are present, who's currently speaking, and who's presenting.

Conference information from the cloud to the premises happens through the XCCP gateway component. The gateway's function is to translate this information between both sides, so that (in call scenarios involving both the Webex cloud and on-premises components), both the Webex App cloud and on-premises environments have similar access to conferencing information.

## ActiveControl benefits

ActiveControl benefits users who use on-premises endpoints running recent CE software or Jabber clients to call in to or get a callback from a Webex App-hosted meeting.

In this scenario, the XCCP gateway translate the roster (participant list) meeting information to the on-premises endpoint or Jabber client.

## Architecture for ActiveControl

From the top of the diagram, left to right shows the secure on-premises connection out to the Webex cloud, and the example indicates two cloud users (one in Webex App, one in Webex Meetings) joining the meeting.

The bottom shows a conference room endpoint that is registered to the Unified CM and a Video Mesh node cluster where meeting media can land.

The participant list experience is captured; the user accesses the list on the endpoint itself and the list looks the same as it would in Webex App or Webex Meetings.

## Configure ActiveControl

Before you begin

When the ActiveControl solution includes a Video Mesh node in the meeting flows, the only working scenario is an endpoint registered to Unified CM. An endpoint directly registered to Expressway does not work with Video Mesh at this time.

The following illustration summarizes the steps to configure ActiveControl for on-premises registered devices that join a meeting in the cloud. Some steps are covered directly in this article, some are covered in separate documentation.

## Requirements for ActiveControl

Component

Requirements

Cisco Unified Communications Manager

Edge Video Mesh

Minimum —Release 11.5(1) or later in mixed security mode.

Recommended —Release 12.5(1) SU1 or later to support non-secure endpoints registered on-premises or over Mobile and Remote Access (MRA). Unified CM mixed security mode is not required.

Video Mesh nodes registered to the cloud, secured with SIP TLS, and configured as per the steps in the deployment guide at https://www.cisco.com/go/video-mesh .

Cisco Expressway-C or E

Minimum —Release X8.11.4 or later. See the Important Information section in the Expressway X8.11.4 Release Notes for more information.

Recommended —Release X12.5 or later for MRA devices configured with a Unified CM non-secure device security mode.

Video Mesh does not currently support secure SIP trunks for devices that are registered directly to Expressway for call control.

Webex Devices: Desk, Room, MX, and SX Series

CE 9.15 or later, or RoomOS 10.3 or later, when securely registered to one of the above call control platforms.

Cisco Jabber

Release 12.5 or later

Encryption

On releases earlier than 12.5 —The entire call path from the endpoint to cloud must be secured with TLS 1.2.

On releases 12.5 and later —TLS is not required between the endpoint and Unified CM.

## Unified CM tasks

Configure Unified CM

These steps ensure that devices are securely registered to Unified CM and the media is encrypted.

Configure iX support in Unified CM by following the steps in the Enabling iX support in Cisco Unified Communications Manager section of the ActiveControl Deployment Guide .

Configure the device security profiles:

This step is not required if you're using 12.5 releases of Unified CM and Expressway.

Cisco Unified Communications Manager groups security-related settings (such as device security mode) for a device type and protocol into security profiles to allow you to assign a single security profile to multiple devices. You apply the configured settings to a phone when you choose the security profile in the Phone Configuration window.

From Cisco Unified CM Administration, go to Device > Phone and then find the endpoint as described in Configure Phones in the System Configuration Guide for Cisco Unified Communications Manager .

For the endpoint, under Protocol Specific Information , set Device Security Profile to a secure SIP profile, such as Universal Device Template - Model-Independent Encryption Security Profile .

Save the changes on the endpoint.

For additional information, see Phone Security Profile Setup in the Security Guide For Cisco Unified Communications Manager .

Configure the service parameter for secure call icon display:

Go to System > Service Parameters , choose the Unified CM server and Cisco CallManager service.

Scroll to Clusterwide Parameters (Feature - Call Secure Status Policy) , and then change the value for the Secure Call Icon Display Policy Required Field service parameter to All media except BFCP must be encrypted .

This change is required for the lock icon to show on CE endpoints. For more information, click the service parameter name to view the online help.

Encrypt Unified CM-registered endpoints

Do these steps on the endpoints themselves to ensure that the secure TLS connection is established.

These steps are not required if you use 12.5 versions of Unified CM and Expressway.

On the endpoint administrative interface, go to SIP and confirm the following settings:

Field

Setting

ANAT

On

DefaultTransport

Tls

Line

Private

ListenPort

Off

PreferredIPMedia

PreferredIPSignaling

IPv4

Proxy Address

Enter the IP address of the Unified CM publisher that the device is registered to.

TlsVerify

On

Type

Cisco

Save your changes.

Under Security , verify that Unified CM certificates are installed.

## Expressway tasks

Configure Expressway

Follow these steps to configure the zone between Expressway where the device is registered and the upstream Expressway pair zone that connects out to the cloud.

Under Advanced settings for the zone between the Expressway call control and the Expressway pair, ensure that SIP UDP/IX filter mode is set to Off , the default option.

Set Zone profile to Custom and then save your changes.

Encrypt Expressway-registered endpoints

Do these steps on the Expressway-registered endpoints themselves to ensure that the secure TLS connection is established.

On the endpoint administrative interface, go to SIP and confirm the following settings:

Field

Setting

ANAT

Off

DefaultTransport

Tls

Line

Private

ListenPort

On

MinimumTLSVersion

TLSv1.0

PreferredIPMedia

PreferredIPSignaling

IPv4

Proxy Address

Enter the IP address of the Expressway that the device is registered to.

TlsVerify

Off

Type

Standard

Save your changes.

## Secure Cloud-Based Meetings

Use these steps to create a SIP profile with iX enabled and secure traffic from Unified CM to Expressway.

Configure a SIP profile for this trunk with the following options:

Set Early Offer support for voice and video calls to Best Effort (No MTP Needed) .

Check Allow iX Application Media . (This was done in the earlier iX support step).

For the SIP trunk, apply the SIP profile that you created.

Under Destination , enter the Expressway-C IP address or FQDN in the Destination Address and enter 5061 for Destination Port .

What to do next

For the TLS connection to work, certificates between Unified CM and Expressway must be exchanged or both must have certificates signed by the same certificate authority. See Ensure Certificate Trust Between Unified CM and Expressway in the Cisco Expressway and CUCM via SIP Trunk Deployment Guide for more information.

On the Expressway-C (the next hop from Unified CM), under Advanced settings for the zone between Expressway and Unified CM, ensure that SIP UDP/IX filter mode is set to Off (the default setting). See Filtering iX in Cisco VCS in the ActiveControl Deployment Guide for more information.

## Secure Video Mesh-based meetings

If you deployed Video Mesh in your organization, you can secure the Video Mesh nodes for clusters that you registered to the cloud.

Configure encryption by following the steps in the deployment guide at https://www.cisco.com/go/video-mesh .

## Verify the meeting experience on the secure endpoint

Use these steps to verify that the endpoints are securely registered and the correct meeting experience appears.

Join a meeting from the secured endpoint.

Verify that the meeting roster list appears on the device.

This example shows how the meeting list looks on an endpoint with a touch panel:

During the meeting, access the Webex Conference information from Call Details .

Verify that Encryption section shows the Type as AES-128 and the Status as On .

| The following illustration summarizes the steps to configure ActiveControl for on-premises registered devices that join a meeting in the cloud. Some steps are covered directly in this article, some are covered in separate documentation. |
|---|

| Component | Requirements |
|---|---|
|  |
| Cisco Unified Communications Manager Edge Video Mesh | Minimum —Release 11.5(1) or later in mixed security mode. Recommended —Release 12.5(1) SU1 or later to support non-secure endpoints registered on-premises or over Mobile and Remote Access (MRA). Unified CM mixed security mode is not required. Video Mesh nodes registered to the cloud, secured with SIP TLS, and configured as per the steps in the deployment guide at https://www.cisco.com/go/video-mesh . |
| Cisco Expressway-C or E | Minimum —Release X8.11.4 or later. See the Important Information section in the Expressway X8.11.4 Release Notes for more information. Recommended —Release X12.5 or later for MRA devices configured with a Unified CM non-secure device security mode. Video Mesh does not currently support secure SIP trunks for devices that are registered directly to Expressway for call control. |
| Webex Devices: Desk, Room, MX, and SX Series | CE 9.15 or later, or RoomOS 10.3 or later, when securely registered to one of the above call control platforms. |
| Cisco Jabber | Release 12.5 or later |
| Encryption | On releases earlier than 12.5 —The entire call path from the endpoint to cloud must be secured with TLS 1.2. On releases 12.5 and later —TLS is not required between the endpoint and Unified CM. |

| 1 | Configure iX support in Unified CM by following the steps in the Enabling iX support in Cisco Unified Communications Manager section of the ActiveControl Deployment Guide . |
|---|---|
| 2 | Configure the device security profiles: This step is not required if you're using 12.5 releases of Unified CM and Expressway. Cisco Unified Communications Manager groups security-related settings (such as device security mode) for a device type and protocol into security profiles to allow you to assign a single security profile to multiple devices. You apply the configured settings to a phone when you choose the security profile in the Phone Configuration window. From Cisco Unified CM Administration, go to Device > Phone and then find the endpoint as described in Configure Phones in the System Configuration Guide for Cisco Unified Communications Manager . For the endpoint, under Protocol Specific Information , set Device Security Profile to a secure SIP profile, such as Universal Device Template - Model-Independent Encryption Security Profile . Save the changes on the endpoint. For additional information, see Phone Security Profile Setup in the Security Guide For Cisco Unified Communications Manager . |
| 3 | Configure the service parameter for secure call icon display: Go to System > Service Parameters , choose the Unified CM server and Cisco CallManager service. Scroll to Clusterwide Parameters (Feature - Call Secure Status Policy) , and then change the value for the Secure Call Icon Display Policy Required Field service parameter to All media except BFCP must be encrypted . This change is required for the lock icon to show on CE endpoints. For more information, click the service parameter name to view the online help. |

| 1 | On the endpoint administrative interface, go to SIP and confirm the following settings: Table 2. Endpoint configuration Field Setting ANAT On DefaultTransport Tls Line Private ListenPort Off PreferredIPMedia PreferredIPSignaling IPv4 Proxy Address Enter the IP address of the Unified CM publisher that the device is registered to. TlsVerify On Type Cisco | Field | Setting | ANAT | On | DefaultTransport | Tls | Line | Private | ListenPort | Off | PreferredIPMedia PreferredIPSignaling | IPv4 | Proxy Address | Enter the IP address of the Unified CM publisher that the device is registered to. | TlsVerify | On | Type | Cisco |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Field | Setting |
| ANAT | On |
| DefaultTransport | Tls |
| Line | Private |
| ListenPort | Off |
| PreferredIPMedia PreferredIPSignaling | IPv4 |
| Proxy Address | Enter the IP address of the Unified CM publisher that the device is registered to. |
| TlsVerify | On |
| Type | Cisco |
| 2 | Save your changes. |
| 3 | Under Security , verify that Unified CM certificates are installed. |

| Field | Setting |
|---|---|
| ANAT | On |
| DefaultTransport | Tls |
| Line | Private |
| ListenPort | Off |
| PreferredIPMedia PreferredIPSignaling | IPv4 |
| Proxy Address | Enter the IP address of the Unified CM publisher that the device is registered to. |
| TlsVerify | On |
| Type | Cisco |

| 1 | Under Advanced settings for the zone between the Expressway call control and the Expressway pair, ensure that SIP UDP/IX filter mode is set to Off , the default option. |
|---|---|
| 2 | Set Zone profile to Custom and then save your changes. |

| 1 | On the endpoint administrative interface, go to SIP and confirm the following settings: Table 3. Endpoint configuration Field Setting ANAT Off DefaultTransport Tls Line Private ListenPort On MinimumTLSVersion TLSv1.0 PreferredIPMedia PreferredIPSignaling IPv4 Proxy Address Enter the IP address of the Expressway that the device is registered to. TlsVerify Off Type Standard | Field | Setting | ANAT | Off | DefaultTransport | Tls | Line | Private | ListenPort | On | MinimumTLSVersion | TLSv1.0 | PreferredIPMedia PreferredIPSignaling | IPv4 | Proxy Address | Enter the IP address of the Expressway that the device is registered to. | TlsVerify | Off | Type | Standard |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Field | Setting |
| ANAT | Off |
| DefaultTransport | Tls |
| Line | Private |
| ListenPort | On |
| MinimumTLSVersion | TLSv1.0 |
| PreferredIPMedia PreferredIPSignaling | IPv4 |
| Proxy Address | Enter the IP address of the Expressway that the device is registered to. |
| TlsVerify | Off |
| Type | Standard |
| 2 | Save your changes. |

| Field | Setting |
|---|---|
| ANAT | Off |
| DefaultTransport | Tls |
| Line | Private |
| ListenPort | On |
| MinimumTLSVersion | TLSv1.0 |
| PreferredIPMedia PreferredIPSignaling | IPv4 |
| Proxy Address | Enter the IP address of the Expressway that the device is registered to. |
| TlsVerify | Off |
| Type | Standard |

| 1 | Configure a SIP profile for this trunk with the following options: Set Early Offer support for voice and video calls to Best Effort (No MTP Needed) . Check Allow iX Application Media . (This was done in the earlier iX support step). |
|---|---|
| 2 | For the SIP trunk, apply the SIP profile that you created. |
| 3 | Under Destination , enter the Expressway-C IP address or FQDN in the Destination Address and enter 5061 for Destination Port . |

| Configure encryption by following the steps in the deployment guide at https://www.cisco.com/go/video-mesh . |
|---|

| 1 | Join a meeting from the secured endpoint. |
|---|---|
| 2 | Verify that the meeting roster list appears on the device. This example shows how the meeting list looks on an endpoint with a touch panel: |
| 3 | During the meeting, access the Webex Conference information from Call Details . |
| 4 | Verify that Encryption section shows the Type as AES-128 and the Status as On . |

## Figuras

![Webex Conference meeting window displaying three participants](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/430001-440000/433001-434000/433504.jpg)

![Webex Conference secure endpoint meeting information displaying details and encryption box selected with Type AES-128 and Status as ON](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/430001-440000/433001-434000/433503.jpg)