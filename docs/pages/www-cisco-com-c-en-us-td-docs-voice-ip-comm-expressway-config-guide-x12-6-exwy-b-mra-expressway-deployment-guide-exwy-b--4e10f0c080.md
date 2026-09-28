---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x12-6-exwy-b-mra-expressway-deployment-guide-exwy-b--4e10f0c080
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X12-6/exwy_b_mra-expressway-deployment-guide/exwy_b_mra-expressway-deployment-guide_chapter_010000.html
retrieved_at: 2026-08-16T15:34:56.088432+00:00
---

Mobile and Remote Access Through Cisco Expressway Deployment Guide (X12.6)

# Mobile and Remote Access Through Cisco Expressway Deployment Guide (X12.6)

Updated: June 3, 2020

Chapter: Endpoint and Client Requirements

## Chapter: Endpoint and Client Requirements

# Endpoint and Client Requirements

## MRA-Compatible Endpoints

Endpoints

MRA Support

Cisco IP Phone 7800 Series

11.0(1)

Cisco IP Phone 8800 Series except Cisco Wireless IP Phone 8821 and 8821-EX and Cisco Unified IP Conference Phone 8831

11.0(1)

Cisco IP Conference Phone 7832

12.1(1)

Cisco IP Conference Phone 8832

12.1(1)

Cisco TelePresence endpoints: SX Series, EX Series, MX Series, Profile Series, C Series

TC7.0.1

Cisco TelePresence and Cisco WebEx endpoints: DX70, DX80, MX700, MX800, MX800 Dual, SX10, SX20, SX80, MX200 G2, MX300 G2

CE8 or CE9

Cisco WebEx endpoints: Cisco WebEx Room Kit, Cisco WebEx Codec Plus, Cisco WebEx Room 55, Cisco WebEx Room 70 Single, Cisco
                                          WebEx Room 70 Dual

CE 9.0

Android-based Cisco DX650, DX70, and DX80 devices

10.2.4(99)

## EX, MX, and SX Series Endpoints (Running TC Software)

Ensure that the provisioning mode is set to Cisco UCM via Expressway .

These devices must verify the identity of the Expressway-E they are connecting to by validating its server certificate. To
                              do this, they must have the certificate authority that was used to sign the Expressway-E's server certificate in their list
                              of trusted CAs.

The devices ship with a list of default CAs which cover the most common providers (including Verisign and Thawte). If the
                              relevant CA is not included, it must be added (for instructions, see the endpoint administrator guide).

Mutual authentication is optional, and these devices are not required to provide client certificates. If you do want to configure
                              mutual TLS, you cannot use CAPF enrolment to provision the client certificates. Instead, manually apply the certificates to
                              the devices. The client certificates must be signed by an authority that is trusted by the Expressway-E.

## Considerations for Android-based DX650, DX80, and DX70 Devices and Supported IP Phone 7800 and 8800 models

If you deploy these devices to register with Cisco Unified Communications Manager through MRA, be aware of the following points. For DX endpoints, these considerations only apply to Android-based devices
                              and do not apply to DX70 or DX80 devices running CE software:

Trust list : You cannot modify the root CA trust list on Cisco IP Phone 7800 Series and Cisco IP Phone 8800 Series devices. Make sure that the Expressway-E's server certificate is signed by one of the CAs that the devices trust, and that
                                    the CA is trusted by the Expressway-C and the Expressway-E.

Off-hook dialing : The way KPML dialing works between these devices and Unified CM means that you need Cisco Unified Communications Manager 10.5(2)SU2 or later to be able to do off-hook dialing via MRA. You can work around this dependency by using on-hook dialing.

## MRA-Compatible Clients

Jabber

MRA Support

Legacy Authentication (LDAP)

Legacy Authentication with SSO

OAuth with Refresh

OAuth Refresh with SSO

APNS

Cisco Jabber for Windows

9.7

-

10.6

11.9

11.9

NA

Cisco Jabber for iPhone and iPad

9.6.1

-

10.6

11.9

11.9

11.9

Cisco Jabber for Android

(includes Chromebook)

9.6

-

10.6

11.9

11.9

NA

Cisco Jabber for Mac

9.6

-

10.6

11.9

11.9

NA

Jabber clients verify the identity of the Expressway-E they are connecting to by validating its server certificate. To do this,
                              they must have the certificate authority that was used to sign the Expressway-E's server certificate in their list of trusted
                              CAs.

Jabber uses the underlying operating system's certificate mechanism:

Windows: Certificate Manager

MAC OS X: Key chain access

IOS: Trust store

Android: Location & Security settings

Jabber client configuration details for MRA are provided in the installation and configuration guide for the relevant client:

### Cisco Webex Teams Clients

Expressway supports calling for MRA-connected Webex Teams clients that are running a compatible software version:

Cisco Webex Teams for Windows

Cisco Webex Teams for Mac

Cisco Webex Teams for iPhone and iPad

Cisco Webex Teams for Android

## Which MRA Features Are Supported

For information about which features are supported over MRA for specific clients and endpoints, refer to the relevant product
                              documentation:

Jabber clients

See the "Supported Services" section of the "Remote Access" chapter, Planning Guide for Cisco Jabber (for your version) on
                                    the Install and Upgrade Guides page.

Cisco IP Phone 7800 Series (desk phones)

See "Phone Features Available for Mobile and Remote Access Through Expressway" in the "Phone Features and Setup" chapter, Cisco IP Phone 7800 Series Administration Guide for Cisco Unified Communications Manager on the Maintain and Operate Guides page.

Cisco IP Conference Phone 7832

See "Phone Features Available for Mobile and Remote Access Through Expressway" in the "Phone Features and Setup" chapter, Cisco IP Conference Phone 7832  Administration Guide for Cisco Unified Communications Manager on the Maintain and Operate Guides page.

Cisco IP Phone 8800 Series (desk phones)

See "Phone Features Available for Mobile and Remote Access Through Expressway" in the "Phone Features and Setup" chapter, Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager on the Maintain and Operate Guides page.

Cisco IP Conference Phone 8832

See "Phone Features Available for Mobile and Remote Access Through Expressway" in the "Phone Features and Setup" chapter, Cisco IP Conference Phone 8832 Administration Guide for Cisco Unified Communications Manager on the Maintain and Operate Guides page.

| Endpoints | MRA Support |
|---|---|
| Cisco IP Phone 7800 Series | 11.0(1) |
| Cisco IP Phone 8800 Series except Cisco Wireless IP Phone 8821 and 8821-EX and Cisco Unified IP Conference Phone 8831 | 11.0(1) |
| Cisco IP Conference Phone 7832 | 12.1(1) |
| Cisco IP Conference Phone 8832 | 12.1(1) |
| Cisco TelePresence endpoints: SX Series, EX Series, MX Series, Profile Series, C Series | TC7.0.1 |
| Cisco TelePresence and Cisco WebEx endpoints: DX70, DX80, MX700, MX800, MX800 Dual, SX10, SX20, SX80, MX200 G2, MX300 G2 | CE8 or CE9 |
| Cisco WebEx endpoints: Cisco WebEx Room Kit, Cisco WebEx Codec Plus, Cisco WebEx Room 55, Cisco WebEx Room 70 Single, Cisco
                                          WebEx Room 70 Dual | CE 9.0 |
| Android-based Cisco DX650, DX70, and DX80 devices | 10.2.4(99) |

| Jabber | MRA Support | Legacy Authentication (LDAP) | Legacy Authentication with SSO | OAuth with Refresh | OAuth Refresh with SSO | APNS |
|---|---|---|---|---|---|---|
| Cisco Jabber for Windows | 9.7 | - | 10.6 | 11.9 | 11.9 | NA |
| Cisco Jabber for iPhone and iPad | 9.6.1 | - | 10.6 | 11.9 | 11.9 | 11.9 |
| Cisco Jabber for Android (includes Chromebook) | 9.6 | - | 10.6 | 11.9 | 11.9 | NA |
| Cisco Jabber for Mac | 9.6 | - | 10.6 | 11.9 | 11.9 | NA |