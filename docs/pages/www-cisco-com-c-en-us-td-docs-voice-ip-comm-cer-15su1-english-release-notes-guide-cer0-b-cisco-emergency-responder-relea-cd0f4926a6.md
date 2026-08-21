---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-15su1-english-release-notes-guide-cer0-b-cisco-emergency-responder-relea-cd0f4926a6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/15su1/english/release_notes/guide/cer0_b_cisco-emergency-responder-release-notes-15SU1.html
retrieved_at: 2026-08-21T06:39:25.376639+00:00
---

Cisco Emergency Responder Version 15SU1a Release Notes

# Cisco Emergency Responder Version 15SU1a Release Notes

### Download Options

Updated: May 5, 2025

Cisco Emergency Responder Version 15SU1a Release Notes

First Published: March 28, 2024

Last Updated: May 5, 2025

# Introduction

## Support for IPv6 Subnet Configurations

In this release, Emergency Responder introduces support for IPv6 Subnet Configurations for both the dual-stack and single-stack
                  devices. If you want the E911 calls to take precendence of the IPv6 subnet over the IPv4 subnet, you must enable the IPv6 Subnet Configurations have precedence over IPv4 option in the Cisco Emergency Responder Administration user interface. If you do not use this option, the IPv4 subnet is
                  given precedence, and the calls are routed via the IPv4 subnet.

Webex App and Cisco Jabber clients will not work with the IPv6 Subnet tracking feature in Emergency Responder.

## Enhanced Security Considerations

From Cisco Emergency Responder Release 14 onwards, all the certificate-related operations are moved from IPsec to Tomcat certificates.
                  To create a trust between a publisher node and subscriber node, the Tomcat certificate should be exchanged between the publisher
                  and subscriber for any cluster-related operations to work. From Release 14SU2 onwards, if you need to perform manual or scheduled
                  DRS backups or if you must change the subscriber hostname, the tomcat-ecdsa certificate must be exchanged between the publisher
                  and subscriber nodes along with the tomcat certificate.

Any Federal Information Processing Standards (FIPS) or hostname related changes require the same operation procedures.

## Requirements

### Supported Hardware and Software

The information in the following sections discuss Hardware and Software requirements for Cisco Emergency Responder 15SU1a.
                     Read these sections before you perform an upgrade.

#### Required Software

The following table lists required software that you must install to use Emergency Responder.

Item

Supported Software Release

Description

Cisco Unified Communications Manager

Cisco Unified Communications Manager 15

Cisco Unified Communications Manager 14 and SUs

Cisco Unified Communications Manager 12.5(x)

Cisco Unified Communications Manager 11.5(x)

The software that runs the telephony network.

Web browser

Microsoft Edge, Chrome, and Firefox on Windows 10 and 11 (64 bit)

Safari, Chrome, and Firefox on MacOS Ventura 13.4.1

We recommend that you use the latest version for all the web browsers supported.

#### Recommended
                     	 Software

The following table lists optional software that is recommended
                        		for use with Emergency Responder.

Item

Minimum software release

Description

Email server

Any SMTP email server

Used to send email notifications to onsite alert (security)
                                    				  personnel. If you use an SMTP email paging server, personnel are paged instead
                                    				  of emailed.

#### Supported Phones

The following table lists the different types of phones that support Emergency Responder. The support that Emergency Responder
                           supplies differs depending on the type of phone and the type of switch port to which the phone is attached.

Cisco will not issue bug fixes or security enhancements for endpoints that have reached End of Software Maintenance or End
                                       of Support status, regardless of whether those endpoints are deprecated or not deprecated. Cisco will not test Emergency Responder
                                       with End of Life phones. For endpoints that have reached End of Sale (EOS), or End of Software Maintenance, refer to the EOS
                                       link of that respective phone to view support details.

Phones

Description

Phones that are automatically tracked using Switch-port based tracking

Most Cisco IP Phones and Telepresence/Webex devices support Cisco Discovery Protocol (CDP). This includes the Skinny Call
                                       Control Protocol (SCCP) and Session Initiation Protocol (SIP) IP Phones.

Check the data sheets for each Cisco phone model/series to confirm CDP support.

Devices that do not support CDP can potentially be tracked using the MAC table on the switch, to do this you must toggle “Enable
                                       CAM-based Phone Tracking” when you add the network switch to Emergency Responder.

These phones do not require any special Emergency Responder configuration. However, you must enable Cisco Discovery Protocol
                                       on the switches.

Although Cisco Analog Telephone Adapter (ATA) phones support Cisco Discovery Protocol and SCCP, Emergency Responder cannot
                                                automatically track them. You can add ATA phones manually and assign them to an Emergency Response Location (ERL). Emergency
                                                Responder routes calls from ATA phones based on the assigned ERL.

Cisco IP Communicator can be tracked using Cisco Discovery Protocol only when it is installed with the Device ID containing
                                                the MAC address of the wired network interface and operating over a wired network interface.

Phones that you can track using an IP subnet

Any Cisco Unified IP Phone, Telepresence/Webex device, or third-party SIP phone can be tracked using IP subnet based tracking.

Cisco Jabber can be tracked using IP subnet-based tracking.

To track these phones, you must configure the subnet and then assign ERLs to the configured subnets.

Any IP endpoint can be tracked at call time using the IP subnet provided that the Use IP Address from Call Signaling Telephony
                                                setting is enabled.

Phones that you can manually define or track using an IP subnet

Phones that are connected to analog line gateways such as Cisco VG350 or VG224 series or ATA 180 series or ATA 190 series
                                             or ATA 191 series.

Any H.323 endpoints

Cisco Webex App (registered natively to Unified Communications Manager)

These phones are supported only if their calls are routed by Cisco Unified Communications Manager.

Any IP endpoint can be tracked at call time using the IP subnet provided that the Use IP Address From Call Signaling Telephony
                                                setting is enabled.

Cisco Webex client (registered natively to Unified Communications Manager) is represented through the registered Spark RD
                                       (Remote Destination) and needs to be manually defined in Emergency Responder for tracking.

Phones supported for off-premises location confirmation and update with the Remote Worker Emergency Calling feature in Unified
                                          Communications Manager 9.0 and later

Cisco IP Communicator

Cisco Virtual Desktop (VXCC)

Cisco IP Phone 7800 Series

Cisco Unified IP Phone 9841, 9851, 9861, 9871, 9971, 9951, 8961, 8945, 8941, 8865, 8861, 8851, 8845, 8841, 7975, 7971, 7970, 7965, 7962, 7961, 7945, 7942, 7941, 7911, 7910,
                                             and 7906

When configured for off-premises use in Unified Communications Manager 9.0 and later, these phones provide displays for off-premises
                                       users to confirm or update their off-premises location.

If the user dismisses the display before confirming or updating the location, the location can be recovered by selecting Running
                                                Applications from the Services menu or by resetting the phone.

Phones supported for Access Point based tracking with Unified Communications Manager 11.5 and later

Cisco Unified Wireless IP Phone 7925G, 7925G-EX, 7926G , 8821 , Cisco Jabber , and Cisco Webex App

Wireless Access Points need to be defined in Unified Communications Manager 11.5 and later, these phones provide their upstream
                                       infrastructure information (like BSSID) through Station Info messages to Unified Communications Manager. Cisco Emergency Responder
                                       through AXL Change Notification can track these phones through the associated Access Point.

#### Supported Meraki Wireless Access Point for Location Awareness

The following table lists the Meraki Wireless Access Point for Location Awareness that Emergency Responder supports.

Support is limited to the model with this specific OUI. While a model may have multiple OUIs, from the Unified Communications
                                    Manager or Emergency Responder perspective, only those OUIs explicitly mentioned are supported. Any other OUIs for the same
                                    model are not supported within Unified Communications Manager or Emergency Responder.

Meraki Wireless Access Point

Organizationally Unique Identifier (OUI)

MR11

00:18:0A

MR20

4C:C8:A1

MR30H

2C:3F:0B

MR30H

68:3A:1E

MR33

34:56:FE

MR33

98:18:88

MR36

A8:46:9D

MR42

AC:17:C8

MR52

E0:55:3D

MR52

E0:CB:BC

MR56

E4:55:A8

MR70

F8:9E:28

MR72

0C:8D:DB

#### Supported Voice Ready Lan Switches

The following table lists the LAN switch models that Emergency Responder supports. A LAN switch model is supported only if
                           the SNMP System Object ID appears in this table, regardless of the LAN switch configuration or software release.

Emergency Responder requires SNMP Version 1, Version 2, Version 2c, or Version 3 for automatic tracking of Cisco Unified IP
                                    Phones by connected switch ports.

Important

Cisco will not issue bug fixes or security enhancements for devices that have reached End of Software Maintenance or End of
                                       Support status, regardless of whether those devices are deprecated or not deprecated. Cisco will not test Emergency Responder
                                       with End of Life devices. For devices that have reached End of Sale (EOS), or End of Software Maintenance, refer to the EOS
                                       link of that respective device to view support details.

For information on all of the End of Support and End-of-Life products, see https://www.cisco.com/c/en_ca/products/eos-eol-listing.html .

For a list of firmware versions that are used for each Cisco device, see the Cisco Collaboration Systems Release Compatibility
                                       Matrix at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/unified/communications/system/Compatibility/CSR-Compatibility-Matrix.html .

Series

(Ethernet Ports Only)

Supported Device

System Object ID from CISCO-PRODUCTS-MIB or CISCO-STACK-MIB

Catalyst C1000

C1000-8FP-2G-L

1.3.6.1.4.1.9.1.2959

C1000-8P-2G-L

1.3.6.1.4.1.9.1.2959

C1000-8FP-E-2G-L

1.3.6.1.4.1.9.1.2959

C1000-8P-E-2G-L

1.3.6.1.4.1.9.1.2959

C1000-8T-2G-L

1.3.6.1.4.1.9.1.2959

C1000-8T-E-2G-L

1.3.6.1.4.1.9.1.2959

C1000-16FP-2G-L

1.3.6.1.4.1.9.1.2959

C1000-16P-2G-L

1.3.6.1.4.1.9.1.2959

C1000-16P-E-2G-L

1.3.6.1.4.1.9.1.2959

C1000-16T-2G-L

1.3.6.1.4.1.9.1.2897

C1000-16T-E-2G-L

1.3.6.1.4.1.9.1.2959

C1000-24FP-4G-L

1.3.6.1.4.1.9.1.2959

C1000-24FP-4X-L

1.3.6.1.4.1.9.1.2959

C1000-24P-4G-L

1.3.6.1.4.1.9.1.2959

C1000-24P-4X-L

1.3.6.1.4.1.9.1.2897

C1000-24PP-4G-L

1.3.6.1.4.1.9.1.2959

C1000-24T-4X-L

1.3.6.1.4.1.9.1.2897

Catalyst C1000

C1000-48FP-4G-L

1.3.6.1.4.1.9.1.2959

C1000-48FP-4X-L

1.3.6.1.4.1.9.1.2897

C1000-48P-4X-L

1.3.6.1.4.1.9.1.2897

C1000-48PP-4G-L

1.3.6.1.4.1.9.1.2959

C1000-48T-4G-L

1.3.6.1.4.1.9.1.2959

C1000-24T-4G-L

1.3.6.1.4.1.9.1.2959

C1000SM-16FP-2G-L

1.3.6.1.4.1.9.1.2943

C1000SM-16P-2G-L

1.3.6.1.4.1.9.1.2941

C1000SM-16P-E-2G-L

1.3.6.1.4.1.9.1.2942

C1000SM-16T-2G-L

1.3.6.1.4.1.9.1.2939

C1000SM-16T-E-2G-L

1.3.6.1.4.1.9.1.2940

C1000SM-24FP-4G-L

1.3.6.1.4.1.9.1.2947

C1000SM-24FP-4X-L

1.3.6.1.4.1.9.1.2954

C1000SM-24P-4G-L

1.3.6.1.4.1.9.1.2946

C1000SM-24P-4X-L

1.3.6.1.4.1.9.1.2953

C1000SM-24PP-4G-L

1.3.6.1.4.1.9.1.2945

C1000SM-24T-4G-L

1.3.6.1.4.1.9.1.2944

C1000SM-24T-4X-L

1.3.6.1.4.1.9.1.2952

Catalyst C1000

C1000SM-48FP-4G-L

1.3.6.1.4.1.9.1.2951

C1000SM-48FP-4X-L

1.3.6.1.4.1.9.1.2957

C1000SM-48P-4G-L

1.3.6.1.4.1.9.1.2950

C1000SM-48P-4X-L

1.3.6.1.4.1.9.1.2956

C1000SM-48PP-4G-L

1.3.6.1.4.1.9.1.2949

C1000SM-48T-4G-L

1.3.6.1.4.1.9.1.2948

C1000SM-48T-4X-L

1.3.6.1.4.1.9.1.2955

C1000SM-8P-2G-L

1.3.6.1.4.1.9.1.2935

C1000SM-8P-E-2G-L

1.3.6.1.4.1.9.1.2936

C1000-48T-4X-L

1.3.6.1.4.1.9.1.2897

C1000SM-8T-2G-L

1.3.6.1.4.1.9.1.2933

C1000SM-8T-E-2G-L

1.3.6.1.4.1.9.1.2934

C1000-12MP-2X-L

1.3.6.1.4.1.9.1.2897

C1000-24MP-4X-L

1.3.6.1.4.1.9.1.2897

Catalyst C1000

C1000SM-8FP-2G-L

1.3.6.1.4.1.9.1.2937

C1000SM-8FP-E-2G-L

1.3.6.1.4.1.9.1.2938

C1000FE-24T-4G-L

1.3.6.1.4.1.9.1.3021

C1000FE-24P-4G-L

1.3.6.1.4.1.9.1.3022

C1000FE-48T-4G-L

1.3.6.1.4.1.9.1.3023

C1000FE-48P-4G-L

1.3.6.1.4.1.9.1.3024

Connected Grid 2500

CGS-2520-16S-8PC

1.3.6.1.4.1.9.1.1246

Catalyst 2940

2940-8TF

1.3.6.1.4.1.9.1.542

2940-8TT

1.3.6.1.4.1.9.1.540

Catalyst 2950

2950-12

1.3.6.1.4.1.9.1.323

2950-24

1.3.6.1.4.1.9.1.324

2950C-24

1.3.6.1.4.1.9.1.325

2950G-24-EI-DC

1.3.6.1.4.1.9.1.472

2950S-24

1.3.6.1.4.1.9.1.430

2950SX-24

1.3.6.1.4.1.9.1.480

2950SX-48

1.3.6.1.4.1.9.1.560

Catalyst 2960

2960-24LT-L

1.3.6.1.4.1.9.1.951

2960-24PC-L

1.3.6.1.4.1.9.1.950

2960-24-S

1.3.6.1.4.1.9.1.929

2960-24TC-L

1.3.6.1.4.1.9.1.694

2960-24TC-S

1.3.6.1.4.1.9.1.928

2960-24TT-L

1.3.6.1.4.1.9.1.716

2960-48PST-L

1.3.6.1.4.1.9.1.1016

2960-48TC-L

1.3.6.1.4.1.9.1.695

2960-48TC-S

1.3.6.1.4.1.9.1.927

2960-48TT-L

1.3.6.1.4.1.9.1.717

2960-8TC-L

1.3.6.1.4.1.9.1.798

2960-8TC-S

1.3.6.1.4.1.9.1.1006

2960G-24TC-L

1.3.6.1.4.1.9.1.696

2960G-48TC-L

1.3.6.1.4.1.9.1.697

2960G-8TC-L

1.3.6.1.4.1.9.1.799

2960PD-8TT-L

1.3.6.1.4.1.9.1.952

2960-48PST-S

1.3.6.1.4.1.9.1.1148

2960-24LC-S

1.3.6.1.4.1.9.1.1146

2960-24PC-S

1.3.6.1.4.1.9.1.1147

Catalyst 2960-C

2960CPD-8PT-L

1.3.6.1.4.1.9.1.1315

2960C-8PC-L

1.3.6.1.4.1.9.1.1366

2960C-12PC-L

1.3.6.1.4.1.9.1.1367

Catalyst 2960-Plus

2960-Plus 48PST-L

1.3.6.1.4.1.9.1.1748

2960-Plus 24PC-

1.3.6.1.4.1.9.1.1749

2960-Plus 24LC-L

1.3.6.1.4.1.9.1.1750

2960-Plus 48PST-S

1.3.6.1.4.1.9.1.1753

2960-Plus 24PC-S

1.3.6.1.4.1.9.1.1754

2960-Plus 24LC-S

1.3.6.1.4.1.9.1.1755

Catalyst 2960-S

2960S Stack

1.3.6.1.4.1.9.1.1208

2960S-24PD-L

1.3.6.1.4.1.9.1.1261

2960S-24PS-L

1.3.6.1.4.1.9.1.1265

2960S-48FPD-L

1.3.6.1.4.1.9.1.1258

2960S-48FPS-L

1.3.6.1.4.1.9.1.1263

2960S-48LPD-L

1.3.6.1.4.1.9.1.1259

2960S-48LPS-L

1.3.6.1.4.1.9.1.1264

Catalyst 2960L

C2960L24TQLL

1.3.6.1.4.1.9.1.2495

C2960L48TQLL

1.3.6.1.4.1.9.1.2496

C2960L24PQLL

1.3.6.1.4.1.9.1.2497

C2960L48PQLL

1.3.6.1.4.1.9.1.2498

C2960L8PSLL

1.3.6.1.4.1.9.1.2361

Catalyst 2960X

Catalyst 2960X-48LPD-L

1.3.6.1.4.1.9.1.1691

Catalyst 2960X-48TD-L

1.3.6.1.4.1.9.1.1692

Catalyst 2960X-24TD-L

1.3.6.1.4.1.9.1.1694

Catalyst 2960X-48FPS-L

1.3.6.1.4.1.9.1.1695

Catalyst 2960X-48LPS-L

1.3.6.1.4.1.9.1.1696

Catalyst 2960X-48TS-L

1.3.6.1.4.1.9.1.1698

Catalyst 2960X-24TS-L

1.3.6.1.4.1.9.1.1699

Catalyst 2960X-24PSK-L

1.3.6.1.4.1.9.1.1700

Catalyst 2960X-48LPS-S

1.3.6.1.4.1.9.1.1701

Catalyst 2960X-24PS-S

1.3.6.1.4.1.9.1.1702

Catalyst 2960X-48TS-LL

1.3.6.1.4.1.9.1.1703

Catalyst 2960X-24TS-LL

1.3.6.1.4.1.9.1.1704

Catalyst 2960X-24PS-L

1.3.6.1.4.1.9.1.1697

Catalyst 2960X-24PD-L

1.3.6.1.4.1.9.1.1693

Catalyst 2960X-48FPD-L

1.3.6.1.4.1.9.1.1690

Catalyst 2960XR

Catalyst 2960XR-24PD-I

1.3.6.1.4.1.9.1.1800

Catalyst 2960XR-24TD-I

1.3.6.1.4.1.9.1.1801

Catalyst 2960XR-48FPS-I

1.3.6.1.4.1.9.1.1802

Catalyst 2960XR-48LPS-I

1.3.6.1.4.1.9.1.1803

Catalyst 2960XR-48TS-I

1.3.6.1.4.1.9.1.1804

Catalyst 2960XR-24PS-I

1.3.6.1.4.1.9.1.1805

Catalyst 2960XR-24TS-I

1.3.6.1.4.1.9.1.1806

Catalyst 2960XR-48FPD-L

1.3.6.1.4.1.9.1.1807

Catalyst 2960XR-48LPD-L

1.3.6.1.4.1.9.1.1808

Catalyst 2960XR-48PD-L

1.3.6.1.4.1.9.1.1809

Catalyst 2960XR-24PD-L

1.3.6.1.4.1.9.1.1810

Catalyst 2960XR-24TD-L

1.3.6.1.4.1.9.1.1811

Catalyst 2960XR-48FPS-L

1.3.6.1.4.1.9.1.1812

Catalyst 2960XR-48LPS-L

1.3.6.1.4.1.9.1.1813

Catalyst 2960XR-48TS-L

1.3.6.1.4.1.9.1.1814

Catalyst 2960XR-24PS-L

1.3.6.1.4.1.9.1.1815

Catalyst 2960XR-24TS-L

1.3.6.1.4.1.9.1.1816

Catalyst 2960XR-48FPD-I

1.3.6.1.4.1.9.1.1797

Catalyst 2960XR-48LPD-I

1.3.6.1.4.1.9.1.1798

Catalyst 2960XR-48TD-I

1.3.6.1.4.1.9.1.1799

Catalyst 2975

2975GS-48PS-L

1.3.6.1.4.1.9.1.1067

2975GS-48PS-L-Stack

1.3.6.1.4.1.9.1.1068

Catalyst 3550

3550-24-DC

1.3.6.1.4.1.9.1.452

Catalyst 3560

3560-12PC-S

1.3.6.1.4.1.9.1.1015

3560-24PS

1.3.6.1.4.1.9.1.563

3560-24TS

1.3.6.1.4.1.9.1.633

3560-48PS

1.3.6.1.4.1.9.1.564

3560-48TS

1.3.6.1.4.1.9.1.634

3560-8PC

1.3.6.1.4.1.9.1.797

3560G-24PS

1.3.6.1.4.1.9.1.614

3560G-24TS

1.3.6.1.4.1.9.1.615

3560G-48PS

1.3.6.1.4.1.9.1.616

3560G-48TS

1.3.6.1.4.1.9.1.617

3560V2-24PS

1.3.6.1.4.1.9.1.1021

3560V2-48PS

1.3.6.1.4.1.9.1.1025

3560CX-12TC-S

1.3.6.1.4.1.9.1. 2133

3560CX-8XPD-S

1.3.6.1.4.1.9.1.2131

3560CX-8PT-S

1.3.6.1.4.1.9.1.2130

Catalyst 3560-C

3560CG-8PC-S

1.3.6.1.4.1.9.1.1317

3560CPD-8PT-S

1.3.6.1.4.1.9.1.1368

3560C-8PC-S

1.3.6.1.4.1.9.1.1466

3560C-12PC-S

1.3.6.1.4.1.9.1.1465

Catalyst 3560-E

3560E-12D

1.3.6.1.4.1.9.1.930

3560E-12SD

1.3.6.1.4.1.9.1.956

3560E-24PD

1.3.6.1.4.1.9.1.795

3560E-24TD

1.3.6.1.4.1.9.1.793

3560E-48PD

1.3.6.1.4.1.9.1.796

3560E-48TD

1.3.6.1.4.1.9.1.794

Catalyst 3560-X

3560X-24P (-L/S/E)

1.3.6.1.4.1.9.1.1228

3560X-48PF (-L/S/E)

1.3.6.1.4.1.9.1.1229

3560X-48P (-L/S/E)

1.3.6.1.4.1.9.1.1229

3560X-48U

1.3.6.1.4.1.9.1.1710

3560X-48TS

1.3.6.1.4.1.9.1.2066

WS-C3560X-48T-S

1.3.6.1.4.1.9.1.1227

Catalyst 3650

Catalyst C3650-24TS (-L/S/E)

1.3.6.1.4.1.9.1.1823

Catalyst C3650-48TS (-L/S/E)

1.3.6.1.4.1.9.1. 1824

Catalyst C3650-24PS (-L/S/E)

1.3.6.1.4.1.9.1. 1825

Catalyst C3650-48PS (-L/S/E)

1.3.6.1.4.1.9.1. 1826

Catalyst C3650-24TD (-L/S/E)

1.3.6.1.4.1.9.1. 1827

Catalyst C3650-48TD (-L/S/E)

1.3.6.1.4.1.9.1. 1828

Catalyst C3650-24PD (-L/S/E)

1.3.6.1.4.1.9.1. 1829

Catalyst C3650-48PD (-L/S/E)

1.3.6.1.4.1.9.1.1830

Catalyst C3650-Stack (-L/S/E)

1.3.6.1.4.1.9.1.1830

Catalyst C3650-48PQ (-L/S/E)

1.3.6.1.4.1.9.1.1881

Catalyst C3650-48TQ (-L/S/E)

1.3.6.1.4.1.9.1.1882

Catalyst 3750

3750 Stack

1.3.6.1.4.1.9.1.516

3750-24FS

1.3.6.1.4.1.9.1.656

3750-24PS

1.3.6.1.4.1.9.1.536

3750-24TS

1.3.6.1.4.1.9.1.513

3750-48PS

1.3.6.1.4.1.9.1.535

3750-48TS

1.3.6.1.4.1.9.1.512

3750G-12S

1.3.6.1.4.1.9.1.530

3750G-12S-SD

1.3.6.1.4.1.9.1.688

3750G-16TD

1.3.6.1.4.1.9.1.591

3750G-24PS

1.3.6.1.4.1.9.1.602

3750G-24T

1.3.6.1.4.1.9.1.514

3750G-24TS

1.3.6.1.4.1.9.1.511

3750G-24TS-1U

1.3.6.1.4.1.9.1.624

3750G-24WS-S25

1.3.6.1.4.1.9.1.778

3750G-24WS-S50

1.3.6.1.4.1.9.1.779

3750G-48PS

1.3.6.1.4.1.9.1.603

3750G-48TS

1.3.6.1.4.1.9.1.604

3750V2-24PS

1.3.6.1.4.1.9.1.1023

3750V2-48PS

1.3.6.1.4.1.9.1.1027

Catalyst 3750-X

3750X-48P (-L/E)

1.3.6.1.4.1.9.1.1225

3750X-48PF (-L/S/E)

1.3.6.1.4.1.9.1.1225

3750X-48P (-L/S)

1.3.6.1.4.1.9.1.1225

3750X-24P (-L/S/E)

1.3.6.1.4.1.9.1.1224

Catalyst 3750 Metro

3750-24TE-M

1.3.6.1.4.1.9.1.574

Catalyst 3750-E

3750E-24PD

1.3.6.1.4.1.9.1.792

3750E-24TD

1.3.6.1.4.1.9.1.789

3750E-48PD

1.3.6.1.4.1.9.1.791

3750E-48TD-S

1.3.6.1.4.1.9.1.790

Catalyst 3850

Catalyst C3850-24U (-L/S/E)

1.3.6.1.4.1.9.1.1767

Catalyst C3850-48U (-L/S/E)

1.3.6.1.4.1.9.1.1768

3850-48P (-L/S/E)

1.3.6.1.4.1.9.1.1641

3850-24P (-L/S/E)

1.3.6.1.4.1.9.1.1642

3850-48T (-L/S/E)

1.3.6.1.4.1.9.1.1643

3850-24T (-L/S/E)

1.3.6.1.4.1.9.1.1644

Catalyst 3850-12S-S

1.3.6.1.4.1.9.1.1880

Catalyst 3850-12S-E

1.3.6.1.4.1.9.1.1880

Catalyst 3850-24S-S

1.3.6.1.4.1.9.1.1879

Catalyst 3850-24S-E

1.3.6.1.4.1.9.1.1879

Catalyst C3850-12X48U

1.3.6.1.4.1.9.1.1745

Catalyst 4500

4503

1.3.6.1.4.1.9.5.58

4503

1.3.6.1.4.1.9.1.503

4506

1.3.6.1.4.1.9.5.59

4506

1.3.6.1.4.1.9.1.502

4507

1.3.6.1.4.1.9.1.501

4510

1.3.6.1.4.1.9.1.537

Catalyst 4500-E

4503-E

1.3.6.1.4.1.9.1.874

4506-E

1.3.6.1.4.1.9.1.875

4507R-E

1.3.6.1.4.1.9.1.876

4510R-E

1.3.6.1.4.1.9.1.877

4507R+E

1.3.6.1.4.1.9.1.1286

4510R+E

1.3.6.1.4.1.9.1.1287

Catalyst 4900

4948

1.3.6.1.4.1.9.1.626

4948-10GE

1.3.6.1.4.1.9.1.659

Catalyst 6500

6503

1.3.6.1.4.1.9.5.56

6503

1.3.6.1.4.1.9.1.449

6504

1.3.6.1.4.1.9.1.657

6506

1.3.6.1.4.1.9.5.45

6506

1.3.6.1.4.1.9.1.282

6509

1.3.6.1.4.1.9.5.44

6509

1.3.6.1.4.1.9.1.283

6509-NEB

1.3.6.1.4.1.9.5.61

6513

1.3.6.1.4.1.9.5.50

6513

1.3.6.1.4.1.9.1.400

Catalyst 6500-E

6509-E

1.3.6.1.4.1.9.1.283

6506-E

1.3.6.1.4.1.9.1.282

6504-E

1.3.6.1.4.1.9.1.657

6503-E

1.3.6.1.4.1.9.1.449

Catalyst 6800ia

Catalyst 6800ia-48FPD-L

1.3.6.1.4.1.9.1.1866

Catalyst 6800ia-48TD-L

1.3.6.1.4.1.9.1.1867

Catalyst 68xx

Catalyst 68xx Virtual Switch

1.3.6.1.4.1.9.1.1934

Catalyst 6880-X

Catalyst 6880-XLE

1.3.6.1.4.1.9.1.1784

Catalyst 6807-XL

Catalyst 6807-XL

1.3.6.1.4.1.9.1.1765

Catalyst 9200

C9200-24T

1.3.6.1.4.1.9.1.2694

C9200-24P

1.3.6.1.4.1.9.1.2694

C9200-48T

1.3.6.1.4.1.9.1.2694

C9200-48P

1.3.6.1.4.1.9.1.2694

Catalyst 9200CX

C9200CX-8P-2X2G

1.3.6.1.4.1.9.1.3097

C9200CX-12P-2X2G

1.3.6.1.4.1.9.1.3079

C9200CX-12T-2X2G

1.3.6.1.4.1.9.1.3078

C9200CX-12P-2XGH

1.3.6.1.4.1.9.1.3164

C9200CX-8PT-2G

1.3.6.1.4.1.9.1.3098

C9200CX-8UXG-2X

1.3.6.1.4.1.9.1.3099

C9200CX-8P-2XGH

1.3.6.1.4.1.9.1.3195

C9200CX-8UXG-2XH

1.3.6.1.4.1.9.1.3196

Catalyst 9200L

C9200L-24T-4G

1.3.6.1.4.1.9.1.2695

C9200L-24P-4G

1.3.6.1.4.1.9.1.2695

C9200L-48T-4G

1.3.6.1.4.1.9.1.2695

C9200L-48P-4G

1.3.6.1.4.1.9.1.2695

C9200L-24T-4X

1.3.6.1.4.1.9.1.2695

C9200L-24P-4X

1.3.6.1.4.1.9.1.2695

C9200L-48T-4X

1.3.6.1.4.1.9.1.2695

C9200L-48P-4X

1.3.6.1.4.1.9.1.2695

Catalyst 9300

c9300

1.3.6.1.4.1.9.1.2494

c930024T

1.3.6.1.4.1.9.1.2435

c930024P

1.3.6.1.4.1.9.1.2436

c930024U

1.3.6.1.4.1.9.1.2437

c930024X

1.3.6.1.4.1.9.1.2438

c930048T

1.3.6.1.4.1.9.1.2439

c930048P

1.3.6.1.4.1.9.1.2440

c930048U

1.3.6.1.4.1.9.1.2441

c930048UXM

1.3.6.1.4.1.9.1.2442

Catalyst 9300L

C9300L-24T-4X

1.3.6.1.4.1.9.1.2583

C9300L-48T-4X

1.3.6.1.4.1.9.1.2584

C9300L-24P-4G

1.3.6.1.4.1.9.1.2585

C9300L-48P-4G

1.3.6.1.4.1.9.1.2586

C9300L-24T-4G

1.3.6.1.4.1.9.1.2792

C9300L-48T-4G

1.3.6.1.4.1.9.1.2793

C9300L-24P-4X

1.3.6.1.4.1.9.1.2798

Catalyst 9300L

C9300L-24UXG-4X

1.3.6.1.4.1.9.1.2800

C9300L-48UXG-4X

1.3.6.1.4.1.9.1.2801

C9300L-24UXG-2Q

1.3.6.1.4.1.9.1.2802

C9300L-48UXG-2Q

1.3.6.1.4.1.9.1.2803

C9300L-48P-4X

1.3.6.1.4.1.9.1.2804

C9300L-48PF-4X

1.3.6.1.4.1.9.1.2992

C9300L-48PF-4G

1.3.6.1.4.1.9.1.2993

C9300LM-48UX-4Y

1.3.6.1.4.1.9.1.2804

Catalyst 9400

C9407R

1.3.6.1.4.1.9.1.2500

C9410R

1.3.6.1.4.1.9.1.2501

C9404R

1.3.6.1.4.1.9.1.2499

Catalyst 9500

c950012Q

1.3.6.1.4.1.9.1.2418

c950024Q

1.3.6.1.4.1.9.1.2419

c950040X

1.3.6.1.4.1.9.1.2420

Catalyst Express 500

500-24LC

1.3.6.1.4.1.9.1.725

500-24PC

1.3.6.1.4.1.9.1.726

500-24TT

1.3.6.1.4.1.9.1.724

500G-12TC

1.3.6.1.4.1.9.1.727

Catalyst Express 520

520-24LC

1.3.6.1.4.1.9.1.933

520-24PC

1.3.6.1.4.1.9.1.934

520-24TT

1.3.6.1.4.1.9.1.932

520-8PC

1.3.6.1.4.1.9.1.897

520G-24TC

1.3.6.1.4.1.9.1.935

Cisco ME 4900

ME 4924-10GE

1.3.6.1.4.1.9.1.788

Catalyst C6880x

ciscoC6880x

1.3.6.1.4.1.9.1.1936

Catalyst 3560CX

Cisco Catalyst 3560CX-8XPD-S

1.3.6.1.4.1.9.1.2131

Cisco Catalyst 3560CX-8PT-S

1.3.6.1.4.1.9.1.2130

Catalyst C3560

catwsC3560CX12pdS

1.3.6.1.4.1.9.1.2132

catwsC3560CX12pcS

1.3.6.1.4.1.9.1.2134

catwsC3560CX8tcS

1.3.6.1.4.1.9.1.2135

catwsC3560CX8pcS

1.3.6.1.4.1.9.1.2136

Catalyst C2960

catwsC2960CX8tcL

1.3.6.1.4.1.9.1.2137

Catalyst 2960CX

Cisco Catalyst 2960CX-8PC-L

1.3.6.1.4.1.9.1.2191

Series

(Ethernet Ports Only)

Supported Device

System Object ID from CISCO-PRODUCTS-MIB or CISCO-STACK-MIB

Catalyst IE2000

IE-2000-24T67-B

1.3.6.1.4.1.9.1.1842

IE-2000-24T67-B

1.3.6.1.4.1.9.1.1841

IE-2000-24T67-B

1.3.6.1.4.1.9.1.1844

IE-2000-24T67-B

1.3.6.1.4.1.9.1.1843

IE-2000-16T67P-G-E

1.3.6.1.4.1.9.1.1845

IE-2000-4TS-G-L

1.3.6.1.4.1.9.1.1470

IE-2000-4TS-G-B

1.3.6.1.4.1.9.1.1470

IE-2000-4T-G-B

1.3.6.1.4.1.9.1.1471

IE-2000-8TC-B

1.3.6.1.4.1.9.1.1472

IE-2000-16TC-L

1.3.6.1.4.1.9.1.1474

Series

(Ethernet Ports Only)

Supported Device

System Object ID from CISCO-PRODUCTS-MIB or CISCO-STACK-MIB

Catalyst IE2000

IE-2000-16TC-B

1.3.6.1.4.1.9.1.1474

IE-2000-16TC-G-L

1.3.6.1.4.1.9.1.1475

IE-2000-16TC-G-N

1.3.6.1.4.1.9.1.1715

IE-2000-16PTC-G-E

1.3.6.1.4.1.9.1.1730

IE-2000-4S-TS-G-B

1.3.6.1.4.1.9.1.1759

IE-2000-4T-G-L

1.3.6.1.4.1.9.1.1471

IE-2000-16PTC-G-L

1.3.6.1.4.1.9.1.1729

IE-2000-8TC-G-L

1.3.6.1.4.1.9.1.1473

IE-2000-8TC-G-B

1.3.6.1.4.1.9.1.1473

IE-2000-16TC-G-X

1.3.6.1.4.1.9.1.1520

Series

(Ethernet Ports Only)

Supported Device

System Object ID from CISCO-PRODUCTS-MIB or CISCO-STACK-MIB

Catalyst IE2000U

IE-2000U-4S-G

1.3.6.1.4.1.9.1.1839

IE-2000U-4TS-G

1.3.6.1.4.1.9.1.1869

IE-2000U-8TC-G

1.3.6.1.4.1.9.1.1870

IE-2000U-16TC-GP

1.3.6.1.4.1.9.1.1868

IE-2000U-16TC-GP

1.3.6.1.4.1.9.1.1871

IE-2000U-16TC-GP

1.3.6.1.4.1.9.1.1872

IE-2000U-16TC-GP

1.3.6.1.4.1.9.1.1840

Series

(Ethernet Ports Only)

Supported Device

System Object ID from CISCO-PRODUCTS-MIB or CISCO-STACK-MIB

Catalyst IE3x00/IE30x0

IE-3000-4TC

1.3.6.1.4.1.9.1.958

IE-3000-8TC

1.3.6.1.4.1.9.1.959

IE-3010-16S-8PC

1.3.6.1.4.1.9.1.1319

IE-3010-24TC

1.3.6.1.4.1.9.1.1320

IE-3200-8P2S

1.3.6.1.4.1.9.1.2684

IE-3200-8P2S-E

1.3.6.1.4.1.9.1.2684

IE-3200-8T2S

1.3.6.1.4.1.9.1.2683

IE-3300-8T2S

1.3.6.1.4.1.9.1.2685

IE-3300-8P2S

1.3.6.1.4.1.9.1.2686

Series

(Ethernet Ports Only)

Supported Device

System Object ID from CISCO-PRODUCTS-MIB or CISCO-STACK-MIB

Catalyst IE3400/IE3400H

IE-3400-8T2S

1.3.6.1.4.1.9.1.2872

IE-3400-8P2S

1.3.6.1.4.1.9.1.2687

IE-3400H-24FT

1.3.6.1.4.1.9.1.2883

IE-3400H-16FT

1.3.6.1.4.1.9.1.2882

IE-3400H-16T

1.3.6.1.4.1.9.1.2885

IE-3400H-24T

1.3.6.1.4.1.9.1.2886

IE-3400H-8FT

1.3.6.1.4.1.9.1.2881

IE-3400H-8T

1.3.6.1.4.1.9.1.2884

Series

(Ethernet Ports Only)

Supported Device

System Object ID from CISCO-PRODUCTS-MIB or CISCO-STACK-MIB

Catalyst IE4000

IE-4000-8GT8GP4G-E

1.3.6.1.4.1.9.1.2079

IE-4000-4T4P4G-E

1.3.6.1.4.1.9.1.2072

IE-4000-8T4G-E

1.3.6.1.4.1.9.1.2070

IE-4000-16GT4G-E

1.3.6.1.4.1.9.1.2078

IE-4000-16T4G-E

1.3.6.1.4.1.9.1.2073

IE-4000-4GC4GP4G-E

1.3.6.1.4.1.9.1.2077

IE-4000-4GS8GP4G-E

1.3.6.1.4.1.9.1.2080

IE-4000-4S8P4G-E

1.3.6.1.4.1.9.1.2074

IE-4000-4TC4G-E

1.3.6.1.4.1.9.1.2069

IE-4000-8GS4G-E

1.3.6.1.4.1.9.1.2076

Series

(Ethernet Ports Only)

Supported Device

System Object ID from CISCO-PRODUCTS-MIB or CISCO-STACK-MIB

Catalyst IE4000

IE-4000-8GT4G-E i+F45:F48

1.3.6.1.4.1.9.1.2075

IE-4000-8S4G-E

1.3.6.1.4.1.9.1.2071

Catalyst IE4010

IE-4010-4S24P

1.3.6.1.4.1.9.1.2368

IE-4010-16S12P

1.3.6.1.4.1.9.1.2369

Catalyst IE5000

IE-5000-16S12P

1.3.6.1.4.1.9.1.2296

IE-5000-12S12P-10G

1.3.6.1.4.1.9.1.2233

The following table lists the Meraki Switches and Meraki Managed Catalyst Switches that are supported for Switch Port based
                           tracking through SNMP v2.

Series

(Ethernet Ports Only)

Supported Device

System Object ID from CISCO-PRODUCTS-MIB or CISCO-STACK-MIB

Meraki MS120

MS120-8

1.3.6.1.4.1.29671.2.338

MS120-8LP

1.3.6.1.4.1.29671.2.339

MS120-8FP

1.3.6.1.4.1.29671.2.340

MS120-24

1.3.6.1.4.1.29671.2.341

MS120-24P

1.3.6.1.4.1.29671.2.342

MS120-48

1.3.6.1.4.1.29671.2.343

MS120-48LP

1.3.6.1.4.1.29671.2.344

MS120-48FP

1.3.6.1.4.1.29671.2.356

MS120-48FP

1.3.6.1.4.1.29671.2.356

Meraki MS125

MerakiMS125-24

1.3.6.1.4.1.29671.2.371

MerakiMS125-24P

1.3.6.1.4.1.29671.2.372

MerakiMS125-48

1.3.6.1.4.1.29671.2.373

MerakiMS125-48LP

1.3.6.1.4.1.29671.2.374

MerakiMS125-48FP

1.3.6.1.4.1.29671.2.375

Meraki MS210

MS210-24P

1.3.6.1.4.1.29671.2.346

MS210-48LP

1.3.6.1.4.1.29671.2.348

MS210-24

1.3.6.1.4.1.29671.2.345

MS210-48

1.3.6.1.4.1.29671.2.347

MS210-48FP

1.3.6.1.4.1.29671.2.349

Meraki MS220

MerakiMS220-8

1.3.6.1.4.1.29671.2.304

MerakiMS220-8p

1.3.6.1.4.1.29671.2.305

MerakiMS220-24

1.3.6.1.4.1.29671.2.306

MerakiMS220-24p

1.3.6.1.4.1.29671.2.307

MerakiMS220-48

1.3.6.1.4.1.29671.2.308

MerakiMS220-48lp

1.3.6.1.4.1.29671.2.309

MerakiMS220-48fp

1.3.6.1.4.1.29671.2.310

Meraki MS225

MS225-24

1.3.6.1.4.1.29671.2.328

MS225-24p

1.3.6.1.4.1.29671.2.329

MS225-48

1.3.6.1.4.1.29671.2.330

MS225-48lp

1.3.6.1.4.1.29671.2.331

MS225-48fp

1.3.6.1.4.1.29671.2.332

Meraki MS250

MS250-24

1.3.6.1.4.1.29671.2.333

MS250-24p

1.3.6.1.4.1.29671.2.334

MS250-48

1.3.6.1.4.1.29671.2.335

MS250-48lp

1.3.6.1.4.1.29671.2.336

MS250-48fp

1.3.6.1.4.1.29671.2.337

Meraki MS320

MS320-24

1.3.6.1.4.1.29671.2.311

MS320-24p

1.3.6.1.4.1.29671.2.312

MS320-48

1.3.6.1.4.1.29671.2.313

MS320-48lp

1.3.6.1.4.1.29671.2.314

MS320-48fp

1.3.6.1.4.1.29671.2.315

Meraki MS350

MS350-24

1.3.6.1.4.1.29671.2.318

MS350-24p

1.3.6.1.4.1.29671.2.319

MS350-48

1.3.6.1.4.1.29671.2.320

MS350-48lp

1.3.6.1.4.1.29671.2.321

MS350-48fp

1.3.6.1.4.1.29671.2.322

MS350-24x

1.3.6.1.4.1.29671.2.327

Meraki MS355

MS355-24X

1.3.6.1.4.1.29671.2.357

MS355-24X2

1.3.6.1.4.1.29671.2.358

Meraki MS355-48X

1.3.6.1.4.1.29671.2.359

Meraki MS355-48X2

1.3.6.1.4.1.29671.2.360

Meraki MS390

Meraki MS390-24-HW

1.3.6.1.4.1.29671.2.362

Meraki MS390-24P-HW

1.3.6.1.4.1.29671.2.363

Meraki MS390-24U-HW

1.3.6.1.4.1.29671.2.364

Meraki MS390-24UX-HW

1.3.6.1.4.1.29671.2.365

Meraki MS390-48-HW

1.3.6.1.4.1.29671.2.366

Meraki MS390-48P-HW

1.3.6.1.4.1.29671.2.367

Meraki MS390-48U-HW

1.3.6.1.4.1.29671.2.368

Meraki MS390-48UX-HW

1.3.6.1.4.1.29671.2.369

Meraki MS390-48UX2-HW

1.3.6.1.4.1.29671.2.370

Meraki C9300

MerakiC9300-24T-M

1.3.6.1.4.1.29671.2.383

#### Supported Cisco
                     	 Routers

The following table lists the Cisco routers Emergency Responder
                        		supports.

Series (Ethernet Ports Only)

Supported Device

System Object ID from CISCO-PRODUCTS-MIB or CISCO-STACK-MIB

Cisco 891

Cisco C891F-K9

1.3.6.1.4.1.9.1.1858

Cisco C891FWA-K9

1.3.6.1.4.1.9.1.1859

Cisco C891FWE-K9

1.3.6.1.4.1.9.1.1860

Cisco 1100

Cisco C1111-8P

1.3.6.1.4.1.9.1.2443

Cisco C1111-8PWA

1.3.6.1.4.1.9.1.2448

Cisco C1111-8PWB

1.3.6.1.4.1.9.1.2447

Cisco C1111-8PWE

1.3.6.1.4.1.9.1.2446

Cisco 1800

Cisco 1861-SRST-B/K9

1.3.6.1.4.1.9.1.904

Cisco 1861-SRST-C-B/K9

1.3.6.1.4.1.9.1.939

Cisco 1861-SRST-C-F/K9

1.3.6.1.4.1.9.1.940

Cisco 1861-SRST-F/K9

1.3.6.1.4.1.9.1.905

Cisco 1861-UC-2BRI-K9

1.3.6.1.4.1.9.1.902

Cisco 1861-UC-4FXO-K9

1.3.6.1.4.1.9.1.903

Cisco1861

1.3.6.1.4.1.9.1.1065

Cisco 1900

Cisco 1905

1.3.6.1.4.1.9.1.1192

Cisco 1921

1.3.6.1.4.1.9.1.1191

Cisco 1941

1.3.6.1.4.1.9.1.1047

Cisco 2800

Cisco 2811

1.3.6.1.4.1.9.1.576

Cisco 2821

1.3.6.1.4.1.9.1.577

Cisco 2851

1.3.6.1.4.1.9.1.578

Cisco 2900

Cisco 2911

1.3.6.1.4.1.9.1.1045

Cisco 2921

1.3.6.1.4.1.9.1.1044

Cisco 2951

1.3.6.1.4.1.9.1.1043

Cisco 3800

Cisco 3825

1.3.6.1.4.1.9.1.543

Cisco 3845

1.3.6.1.4.1.9.1.544

Cisco 3900

Cisco 3925

1.3.6.1.4.1.9.1.1042

Cisco 3925E

1.3.6.1.4.1.9.1.1144

Cisco 3945

1.3.6.1.4.1.9.1.1041

Cisco 3945E

1.3.6.1.4.1.9.1.1145

### Supported Hardware and Software

The information in the following sections discuss Hardware and Software requirements for Cisco Emergency Responder 15. Read
                     these sections before you perform an upgrade.

### Supported Cisco UCS
                  	 Platforms

For information about supported Cisco Unified Computing System (UCS) platforms, see the Unified Communications Virtualization Supported Applications section of the Cisco Collaboration Virtualization wiki.

### VMware
                  	 Support

For information about VMware, see the Unified Communications VMWare Requirements section of the Cisco documentation wiki at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-software-requirements.html .

### Supported OVAs and
                  	 Capacity

For information about OVAs, administrators should see the
                        		  Virtualization for Cisco Emergency Responder (CER) at http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-emergency-responder.html .

## Related
               	 Documentation

Cisco Emergency Responder Documentation

See the
                  		publications for Cisco Emergency Responder. Navigate from the following
                  		documentation URL:

https://www.cisco.com/c/en/us/support/unified-communications/emergency-responder/series.html

Cisco Unified Communications
                     		  Manager Documentation

See the Cisco Unified Communications Manager Documentation Guide and other publications specific to your Cisco Unified Communications Manager release. Navigate from the following URL:

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/series.html

## Important Notes

### Cisco Emergency Responder 15x Supported Upgrades

Cisco Emergency Responder 10.x and later is supported on Cisco Unified Computing System (UCS) and other virtual platforms
                        only. All existing installations on Media Convergence Servers (MCS) should be migrated to UCS before upgrading to Cisco Emergency
                        Responder 10.x or later.

Direct Refresh Upgrades from Pre-12.5.x source to Release 15 and later is not supported. You should first upgrade your source
                        to Release 12.5.x or 14 and SUs and then upgrade your source to Release 15 and later.

Cisco Emergency Responder 15 and later does not support Install with Data Import.

If the Emergency Responder source is in FIPS mode, see https://www.cisco.com/web/software/286319173/139477/ciscocm.ciscossl7_upgrade_CSCwa48315_CSCwa77974_v1.0.k4.cop-ReadMe.pdf for information on the COP file ciscocm.ciscossl7_upgrade_CSCwa48315_CSCwa77974_v1.0.k4.cop . This document details the pre-requisites required for direct upgrade to the 14SU2 or above destination versions.

Direct upgrades to Cisco Emergency Responder 15 and later are supported only for the following releases:

Cisco Emergency Responder 12.5(1) or Cisco Emergency Responder 12.5(1a) or Cisco Emergency Responder 12.5(1) SU1 or Cisco
                              Emergency Responder 12.5(1) SU2 or Cisco Emergency Responder 12.5(1) SU3 or Cisco Emergency Responder 12.5(1) SU4 or Cisco
                              Emergency Responder 12.5(1) SU5 or Cisco Emergency Responder 12.5(1) SU6 or Cisco Emergency Responder 12.5(1) SU7 or Cisco
                              Emergency Responder 12.5(1) SU8b or Cisco Emergency Responder 12.5(1) SU9

Cisco Emergency Responder 14 or Cisco Emergency Responder 14SU1 or Cisco Emergency Responder 14SU2 or Cisco Emergency Responder
                              14SU3a or Cisco Emergency Responder 14SU4

#### COP Files Required for Upgrades to Release 15 and later

Emergency Responder now improves the encryption for upgrading files. All COP and ISO upgrade files are now signed with the
                        SHA1SUM hash-based signing tool. SHA-1 is now deprecated and has been superseded by SHA-2 (for example SHA-512).

Post-Release 14, all new COP and ISO files are signed with the SHA512SUM hash-based signing tool.

12.5(1), 12.5(1a), 12.5(1) SU1, 12.5(1) SU2, 12.5(1) SU3, 12.5(1) SU4, 12.5(1) SU5, 12.5(1) SU6, 12.5(1)SU7, 12.5(1)SU8b,
                                    and 12.5(1)SU9

15

Apply the required Upgrade Readiness COP File (pre-upgrade): ciscocm.cer_preUpgradeCheck-X.k4.cop.sha512 .

If you want to upgrade Emergency Responder from Release 12.5.x (except for Release 12.5(1)SU6) to 15 and later, you must use
                                             the following COP file: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn .

There are no Direct Refresh Upgrade supported paths for Emergency Responder Release 15 and later. Refresh Upgrades from Pre-12.5.x
                                    source to Release 15 and later is not supported.

Apply the required Upgrade Readiness COP Files (post-upgrade): ciscocm.cer_postUpgradeCheck-X.k4.cop.sha512 .

14, 14SU1, 14SU2, 14SU3a, and 14SU4

15

Apply the required Upgrade Readiness COP File (pre-upgrade): ciscocm.cer_preUpgradeCheck-X.k4.cop.sha512 .

Required COP files:

ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn

ciscocm.cer_V14_CSCwf99494_Intracluster_v1.1.zip

You should apply the following COP file for Release 14SU2 before upgrading your Emergency Responder to Release 15 and later: ciscocm.cer_V14SU2_CSCwc26596-CSCwc76921_C0173-1.zip .

There are no Direct Refresh Upgrade supported paths for Emergency Responder Release 15 and later. Refresh Upgrades from Pre-12.5.x
                                    source to Release 15 and later is not supported.

Apply the required Upgrade Readiness COP Files (post-upgrade): ciscocm.cer_postUpgradeCheck-X.k4.cop.sha512 .

Previous Requirements

Release 15 Requirements

OVA Types

vCPU

RAM

Disk

vCPU

RAM

Disk

20, 000 users

1

4 GB

80 GB

2

6 GB

80 GB

30, 000 users

2

6 GB

110 GB

2

6 GB

110 GB

40, 000 users

4

6 GB

110 GB

4

6 GB

110 GB

In case you are planning to upgrade any of your 12.5.x or 14 and SUs Emergency Responder to Release 15 and later, note the
                        following:

Deployments with 12,000 or 20,000 users having 4GB vRAM should increase the vRAM size to 6GB before upgrading to Release 15
                              and later.

Deployments with 20000 users having 1 vCPU should increase the vCPU to 2 before upgrading to Release 15 and later.

## Caveats

This section
                  		contains information about accessing the Cisco Bug Search to find open caveats
                  		and resolved caveats.

### Access Cisco Bug
                  	 Search

Known problems
                        		  (bugs) are graded according to severity level. These release notes contain
                        		  descriptions of the following:

All severity
                              				level 1 or 2 bugs

Significant
                              				severity level 3 bugs

You can search for
                        		  problems by using Cisco Bug Search.

Before you begin

#### Before you begin

To access Cisco Bug
                        		  Search, you need the following items:

Internet
                              				connection

Web browser

Cisco.com user
                              				ID and password

Step 1

To access Cisco Bug Search, go to:

https://bst.cloudapps.cisco.com/bugsearch

Step 2

Log in with your
                                 			 Cisco.com user ID and password.

Step 3

To look for
                                 			 information about a specific problem, enter the bug ID number in the Search for
                                 			 field, then press Enter .

### Open Caveats

Identifier

Headline

CSCwj11507

911 calls matches defaults ERL due to IPSubnet hashmap rehashing

CSCwk19505

Clustering with IPv6 phone movement is not picking up right ERL when tracked under IPv6 subnet

### Resolved Caveats

Identifier

Headline

CSCwi97789

Restrict X.509 certificate validity periods - Revert of CSCvk20066

CSCwi96690

CER ERL Management API conventional ERL Update failure. COS/TOS fields require text instead of number

CSCwj89638

911 calls matches default ERL after introduction of IPV6 subnet tracking feature

CSCwk02122

911 call from IPv6 Only device is routing through default ERL when using IP Subnet Tracking

CSCwk09485

Telephony Setting Use IP Address from Call Signaling is not taking affect in CER for some cases

### This Document Applies to These Products

- Emergency Responder 15

| Note | Webex App and Cisco Jabber clients will not work with the IPv6 Subnet tracking feature in Emergency Responder. |
|---|---|

| Item | Supported Software Release | Description |
|---|---|---|
| Cisco Unified Communications Manager | Cisco Unified Communications Manager 15 Cisco Unified Communications Manager 14 and SUs Cisco Unified Communications Manager 12.5(x) Cisco Unified Communications Manager 11.5(x) | The software that runs the telephony network. |
| Web browser | Microsoft Edge, Chrome, and Firefox on Windows 10 and 11 (64 bit) Safari, Chrome, and Firefox on MacOS Ventura 13.4.1 | We recommend that you use the latest version for all the web browsers supported. |

| Item | Minimum software release | Description |
|---|---|---|
| Email server | Any SMTP email server | Used to send email notifications to onsite alert (security)
                                    				  personnel. If you use an SMTP email paging server, personnel are paged instead
                                    				  of emailed. |

| Note | Cisco will not issue bug fixes or security enhancements for endpoints that have reached End of Software Maintenance or End
                                       of Support status, regardless of whether those endpoints are deprecated or not deprecated. Cisco will not test Emergency Responder
                                       with End of Life phones. For endpoints that have reached End of Sale (EOS), or End of Software Maintenance, refer to the EOS
                                       link of that respective phone to view support details. |
|---|---|

| Phones | Description |
|---|---|
| Phones that are automatically tracked using Switch-port based tracking Most Cisco IP Phones and Telepresence/Webex devices support Cisco Discovery Protocol (CDP). This includes the Skinny Call
                                       Control Protocol (SCCP) and Session Initiation Protocol (SIP) IP Phones. Check the data sheets for each Cisco phone model/series to confirm CDP support. Devices that do not support CDP can potentially be tracked using the MAC table on the switch, to do this you must toggle “Enable
                                       CAM-based Phone Tracking” when you add the network switch to Emergency Responder. | These phones do not require any special Emergency Responder configuration. However, you must enable Cisco Discovery Protocol
                                       on the switches. Note Although Cisco Analog Telephone Adapter (ATA) phones support Cisco Discovery Protocol and SCCP, Emergency Responder cannot
                                                automatically track them. You can add ATA phones manually and assign them to an Emergency Response Location (ERL). Emergency
                                                Responder routes calls from ATA phones based on the assigned ERL. Note Cisco IP Communicator can be tracked using Cisco Discovery Protocol only when it is installed with the Device ID containing
                                                the MAC address of the wired network interface and operating over a wired network interface. | Note | Although Cisco Analog Telephone Adapter (ATA) phones support Cisco Discovery Protocol and SCCP, Emergency Responder cannot
                                                automatically track them. You can add ATA phones manually and assign them to an Emergency Response Location (ERL). Emergency
                                                Responder routes calls from ATA phones based on the assigned ERL. | Note | Cisco IP Communicator can be tracked using Cisco Discovery Protocol only when it is installed with the Device ID containing
                                                the MAC address of the wired network interface and operating over a wired network interface. |
| Note | Although Cisco Analog Telephone Adapter (ATA) phones support Cisco Discovery Protocol and SCCP, Emergency Responder cannot
                                                automatically track them. You can add ATA phones manually and assign them to an Emergency Response Location (ERL). Emergency
                                                Responder routes calls from ATA phones based on the assigned ERL. |
| Note | Cisco IP Communicator can be tracked using Cisco Discovery Protocol only when it is installed with the Device ID containing
                                                the MAC address of the wired network interface and operating over a wired network interface. |
| Phones that you can track using an IP subnet Any Cisco Unified IP Phone, Telepresence/Webex device, or third-party SIP phone can be tracked using IP subnet based tracking. Cisco Jabber can be tracked using IP subnet-based tracking. | To track these phones, you must configure the subnet and then assign ERLs to the configured subnets. Note Any IP endpoint can be tracked at call time using the IP subnet provided that the Use IP Address from Call Signaling Telephony
                                                setting is enabled. | Note | Any IP endpoint can be tracked at call time using the IP subnet provided that the Use IP Address from Call Signaling Telephony
                                                setting is enabled. |
| Note | Any IP endpoint can be tracked at call time using the IP subnet provided that the Use IP Address from Call Signaling Telephony
                                                setting is enabled. |
| Phones that you can manually define or track using an IP subnet Phones that are connected to analog line gateways such as Cisco VG350 or VG224 series or ATA 180 series or ATA 190 series
                                             or ATA 191 series. Any H.323 endpoints Cisco Webex App (registered natively to Unified Communications Manager) | These phones are supported only if their calls are routed by Cisco Unified Communications Manager. Note Any IP endpoint can be tracked at call time using the IP subnet provided that the Use IP Address From Call Signaling Telephony
                                                setting is enabled. Cisco Webex client (registered natively to Unified Communications Manager) is represented through the registered Spark RD
                                       (Remote Destination) and needs to be manually defined in Emergency Responder for tracking. | Note | Any IP endpoint can be tracked at call time using the IP subnet provided that the Use IP Address From Call Signaling Telephony
                                                setting is enabled. |
| Note | Any IP endpoint can be tracked at call time using the IP subnet provided that the Use IP Address From Call Signaling Telephony
                                                setting is enabled. |
| Phones supported for off-premises location confirmation and update with the Remote Worker Emergency Calling feature in Unified
                                          Communications Manager 9.0 and later Cisco IP Communicator Cisco Virtual Desktop (VXCC) Cisco IP Phone 7800 Series Cisco Unified IP Phone 9841, 9851, 9861, 9871, 9971, 9951, 8961, 8945, 8941, 8865, 8861, 8851, 8845, 8841, 7975, 7971, 7970, 7965, 7962, 7961, 7945, 7942, 7941, 7911, 7910,
                                             and 7906 | When configured for off-premises use in Unified Communications Manager 9.0 and later, these phones provide displays for off-premises
                                       users to confirm or update their off-premises location. Note If the user dismisses the display before confirming or updating the location, the location can be recovered by selecting Running
                                                Applications from the Services menu or by resetting the phone. | Note | If the user dismisses the display before confirming or updating the location, the location can be recovered by selecting Running
                                                Applications from the Services menu or by resetting the phone. |
| Note | If the user dismisses the display before confirming or updating the location, the location can be recovered by selecting Running
                                                Applications from the Services menu or by resetting the phone. |
| Phones supported for Access Point based tracking with Unified Communications Manager 11.5 and later Cisco Unified Wireless IP Phone 7925G, 7925G-EX, 7926G , 8821 , Cisco Jabber , and Cisco Webex App | Wireless Access Points need to be defined in Unified Communications Manager 11.5 and later, these phones provide their upstream
                                       infrastructure information (like BSSID) through Station Info messages to Unified Communications Manager. Cisco Emergency Responder
                                       through AXL Change Notification can track these phones through the associated Access Point. |

| Note | Although Cisco Analog Telephone Adapter (ATA) phones support Cisco Discovery Protocol and SCCP, Emergency Responder cannot
                                                automatically track them. You can add ATA phones manually and assign them to an Emergency Response Location (ERL). Emergency
                                                Responder routes calls from ATA phones based on the assigned ERL. |
|---|---|

| Note | Cisco IP Communicator can be tracked using Cisco Discovery Protocol only when it is installed with the Device ID containing
                                                the MAC address of the wired network interface and operating over a wired network interface. |
|---|---|

| Note | Any IP endpoint can be tracked at call time using the IP subnet provided that the Use IP Address from Call Signaling Telephony
                                                setting is enabled. |
|---|---|

| Note | Any IP endpoint can be tracked at call time using the IP subnet provided that the Use IP Address From Call Signaling Telephony
                                                setting is enabled. |
|---|---|

| Note | If the user dismisses the display before confirming or updating the location, the location can be recovered by selecting Running
                                                Applications from the Services menu or by resetting the phone. |
|---|---|

| Note | Support is limited to the model with this specific OUI. While a model may have multiple OUIs, from the Unified Communications
                                    Manager or Emergency Responder perspective, only those OUIs explicitly mentioned are supported. Any other OUIs for the same
                                    model are not supported within Unified Communications Manager or Emergency Responder. |
|---|---|

| Meraki Wireless Access Point | Organizationally Unique Identifier (OUI) |
|---|---|
| MR11 | 00:18:0A |
| MR20 | 4C:C8:A1 |
| MR30H | 2C:3F:0B |
| MR30H | 68:3A:1E |
| MR33 | 34:56:FE |
| MR33 | 98:18:88 |
| MR36 | A8:46:9D |
| MR42 | AC:17:C8 |
| MR52 | E0:55:3D |
| MR52 | E0:CB:BC |
| MR56 | E4:55:A8 |
| MR70 | F8:9E:28 |
| MR72 | 0C:8D:DB |

| Note | Emergency Responder requires SNMP Version 1, Version 2, Version 2c, or Version 3 for automatic tracking of Cisco Unified IP
                                    Phones by connected switch ports. |
|---|---|

| Important | Cisco will not issue bug fixes or security enhancements for devices that have reached End of Software Maintenance or End of
                                       Support status, regardless of whether those devices are deprecated or not deprecated. Cisco will not test Emergency Responder
                                       with End of Life devices. For devices that have reached End of Sale (EOS), or End of Software Maintenance, refer to the EOS
                                       link of that respective device to view support details. For information on all of the End of Support and End-of-Life products, see https://www.cisco.com/c/en_ca/products/eos-eol-listing.html . For a list of firmware versions that are used for each Cisco device, see the Cisco Collaboration Systems Release Compatibility
                                       Matrix at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/unified/communications/system/Compatibility/CSR-Compatibility-Matrix.html . |
|---|---|

| Series (Ethernet Ports Only) | Supported Device | System Object ID from CISCO-PRODUCTS-MIB or CISCO-STACK-MIB |
|---|---|---|
| Catalyst C1000 | C1000-8FP-2G-L | 1.3.6.1.4.1.9.1.2959 |
| C1000-8P-2G-L | 1.3.6.1.4.1.9.1.2959 |
| C1000-8FP-E-2G-L | 1.3.6.1.4.1.9.1.2959 |
| C1000-8P-E-2G-L | 1.3.6.1.4.1.9.1.2959 |
| C1000-8T-2G-L | 1.3.6.1.4.1.9.1.2959 |
| C1000-8T-E-2G-L | 1.3.6.1.4.1.9.1.2959 |
| C1000-16FP-2G-L | 1.3.6.1.4.1.9.1.2959 |
| C1000-16P-2G-L | 1.3.6.1.4.1.9.1.2959 |
| C1000-16P-E-2G-L | 1.3.6.1.4.1.9.1.2959 |
| C1000-16T-2G-L | 1.3.6.1.4.1.9.1.2897 |
| C1000-16T-E-2G-L | 1.3.6.1.4.1.9.1.2959 |
| C1000-24FP-4G-L | 1.3.6.1.4.1.9.1.2959 |
| C1000-24FP-4X-L | 1.3.6.1.4.1.9.1.2959 |
| C1000-24P-4G-L | 1.3.6.1.4.1.9.1.2959 |
| C1000-24P-4X-L | 1.3.6.1.4.1.9.1.2897 |
| C1000-24PP-4G-L | 1.3.6.1.4.1.9.1.2959 |
| C1000-24T-4X-L | 1.3.6.1.4.1.9.1.2897 |
| Catalyst C1000 | C1000-48FP-4G-L | 1.3.6.1.4.1.9.1.2959 |
| C1000-48FP-4X-L | 1.3.6.1.4.1.9.1.2897 |
| C1000-48P-4X-L | 1.3.6.1.4.1.9.1.2897 |
| C1000-48PP-4G-L | 1.3.6.1.4.1.9.1.2959 |
| C1000-48T-4G-L | 1.3.6.1.4.1.9.1.2959 |
| C1000-24T-4G-L | 1.3.6.1.4.1.9.1.2959 |
| C1000SM-16FP-2G-L | 1.3.6.1.4.1.9.1.2943 |
| C1000SM-16P-2G-L | 1.3.6.1.4.1.9.1.2941 |
| C1000SM-16P-E-2G-L | 1.3.6.1.4.1.9.1.2942 |
| C1000SM-16T-2G-L | 1.3.6.1.4.1.9.1.2939 |
| C1000SM-16T-E-2G-L | 1.3.6.1.4.1.9.1.2940 |
| C1000SM-24FP-4G-L | 1.3.6.1.4.1.9.1.2947 |
| C1000SM-24FP-4X-L | 1.3.6.1.4.1.9.1.2954 |
| C1000SM-24P-4G-L | 1.3.6.1.4.1.9.1.2946 |
| C1000SM-24P-4X-L | 1.3.6.1.4.1.9.1.2953 |
| C1000SM-24PP-4G-L | 1.3.6.1.4.1.9.1.2945 |
| C1000SM-24T-4G-L | 1.3.6.1.4.1.9.1.2944 |
| C1000SM-24T-4X-L | 1.3.6.1.4.1.9.1.2952 |
| Catalyst C1000 | C1000SM-48FP-4G-L | 1.3.6.1.4.1.9.1.2951 |
| C1000SM-48FP-4X-L | 1.3.6.1.4.1.9.1.2957 |
| C1000SM-48P-4G-L | 1.3.6.1.4.1.9.1.2950 |
| C1000SM-48P-4X-L | 1.3.6.1.4.1.9.1.2956 |
| C1000SM-48PP-4G-L | 1.3.6.1.4.1.9.1.2949 |
| C1000SM-48T-4G-L | 1.3.6.1.4.1.9.1.2948 |
| C1000SM-48T-4X-L | 1.3.6.1.4.1.9.1.2955 |
| C1000SM-8P-2G-L | 1.3.6.1.4.1.9.1.2935 |
| C1000SM-8P-E-2G-L | 1.3.6.1.4.1.9.1.2936 |
| C1000-48T-4X-L | 1.3.6.1.4.1.9.1.2897 |
| C1000SM-8T-2G-L | 1.3.6.1.4.1.9.1.2933 |
| C1000SM-8T-E-2G-L | 1.3.6.1.4.1.9.1.2934 |
| C1000-12MP-2X-L | 1.3.6.1.4.1.9.1.2897 |
| C1000-24MP-4X-L | 1.3.6.1.4.1.9.1.2897 |
| Catalyst C1000 | C1000SM-8FP-2G-L | 1.3.6.1.4.1.9.1.2937 |
| C1000SM-8FP-E-2G-L | 1.3.6.1.4.1.9.1.2938 |
| C1000FE-24T-4G-L | 1.3.6.1.4.1.9.1.3021 |
| C1000FE-24P-4G-L | 1.3.6.1.4.1.9.1.3022 |
| C1000FE-48T-4G-L | 1.3.6.1.4.1.9.1.3023 |
| C1000FE-48P-4G-L | 1.3.6.1.4.1.9.1.3024 |
| Connected Grid 2500 | CGS-2520-16S-8PC | 1.3.6.1.4.1.9.1.1246 |
| Catalyst 2940 | 2940-8TF | 1.3.6.1.4.1.9.1.542 |
| 2940-8TT | 1.3.6.1.4.1.9.1.540 |
| Catalyst 2950 | 2950-12 | 1.3.6.1.4.1.9.1.323 |
| 2950-24 | 1.3.6.1.4.1.9.1.324 |
| 2950C-24 | 1.3.6.1.4.1.9.1.325 |
| 2950G-24-EI-DC | 1.3.6.1.4.1.9.1.472 |
| 2950S-24 | 1.3.6.1.4.1.9.1.430 |
| 2950SX-24 | 1.3.6.1.4.1.9.1.480 |
| 2950SX-48 | 1.3.6.1.4.1.9.1.560 |
| Catalyst 2960 | 2960-24LT-L | 1.3.6.1.4.1.9.1.951 |
| 2960-24PC-L | 1.3.6.1.4.1.9.1.950 |
| 2960-24-S | 1.3.6.1.4.1.9.1.929 |
| 2960-24TC-L | 1.3.6.1.4.1.9.1.694 |
| 2960-24TC-S | 1.3.6.1.4.1.9.1.928 |
| 2960-24TT-L | 1.3.6.1.4.1.9.1.716 |
| 2960-48PST-L | 1.3.6.1.4.1.9.1.1016 |
| 2960-48TC-L | 1.3.6.1.4.1.9.1.695 |
| 2960-48TC-S | 1.3.6.1.4.1.9.1.927 |
| 2960-48TT-L | 1.3.6.1.4.1.9.1.717 |
| 2960-8TC-L | 1.3.6.1.4.1.9.1.798 |
| 2960-8TC-S | 1.3.6.1.4.1.9.1.1006 |
| 2960G-24TC-L | 1.3.6.1.4.1.9.1.696 |
| 2960G-48TC-L | 1.3.6.1.4.1.9.1.697 |
| 2960G-8TC-L | 1.3.6.1.4.1.9.1.799 |
| 2960PD-8TT-L | 1.3.6.1.4.1.9.1.952 |
| 2960-48PST-S | 1.3.6.1.4.1.9.1.1148 |
| 2960-24LC-S | 1.3.6.1.4.1.9.1.1146 |
| 2960-24PC-S | 1.3.6.1.4.1.9.1.1147 |
| Catalyst 2960-C | 2960CPD-8PT-L | 1.3.6.1.4.1.9.1.1315 |
| 2960C-8PC-L | 1.3.6.1.4.1.9.1.1366 |
| 2960C-12PC-L | 1.3.6.1.4.1.9.1.1367 |
| Catalyst 2960-Plus | 2960-Plus 48PST-L | 1.3.6.1.4.1.9.1.1748 |
| 2960-Plus 24PC- | 1.3.6.1.4.1.9.1.1749 |
| 2960-Plus 24LC-L | 1.3.6.1.4.1.9.1.1750 |
| 2960-Plus 48PST-S | 1.3.6.1.4.1.9.1.1753 |
| 2960-Plus 24PC-S | 1.3.6.1.4.1.9.1.1754 |
| 2960-Plus 24LC-S | 1.3.6.1.4.1.9.1.1755 |
| Catalyst 2960-S | 2960S Stack | 1.3.6.1.4.1.9.1.1208 |
| 2960S-24PD-L | 1.3.6.1.4.1.9.1.1261 |
| 2960S-24PS-L | 1.3.6.1.4.1.9.1.1265 |
| 2960S-48FPD-L | 1.3.6.1.4.1.9.1.1258 |
| 2960S-48FPS-L | 1.3.6.1.4.1.9.1.1263 |
| 2960S-48LPD-L | 1.3.6.1.4.1.9.1.1259 |
| 2960S-48LPS-L | 1.3.6.1.4.1.9.1.1264 |
| Catalyst 2960L | C2960L24TQLL | 1.3.6.1.4.1.9.1.2495 |
| C2960L48TQLL | 1.3.6.1.4.1.9.1.2496 |
| C2960L24PQLL | 1.3.6.1.4.1.9.1.2497 |
| C2960L48PQLL | 1.3.6.1.4.1.9.1.2498 |
| C2960L8PSLL | 1.3.6.1.4.1.9.1.2361 |
| Catalyst 2960X | Catalyst 2960X-48LPD-L | 1.3.6.1.4.1.9.1.1691 |
| Catalyst 2960X-48TD-L | 1.3.6.1.4.1.9.1.1692 |
| Catalyst 2960X-24TD-L | 1.3.6.1.4.1.9.1.1694 |
| Catalyst 2960X-48FPS-L | 1.3.6.1.4.1.9.1.1695 |
| Catalyst 2960X-48LPS-L | 1.3.6.1.4.1.9.1.1696 |
| Catalyst 2960X-48TS-L | 1.3.6.1.4.1.9.1.1698 |
| Catalyst 2960X-24TS-L | 1.3.6.1.4.1.9.1.1699 |
| Catalyst 2960X-24PSK-L | 1.3.6.1.4.1.9.1.1700 |
| Catalyst 2960X-48LPS-S | 1.3.6.1.4.1.9.1.1701 |
| Catalyst 2960X-24PS-S | 1.3.6.1.4.1.9.1.1702 |
| Catalyst 2960X-48TS-LL | 1.3.6.1.4.1.9.1.1703 |
| Catalyst 2960X-24TS-LL | 1.3.6.1.4.1.9.1.1704 |
| Catalyst 2960X-24PS-L | 1.3.6.1.4.1.9.1.1697 |
| Catalyst 2960X-24PD-L | 1.3.6.1.4.1.9.1.1693 |
| Catalyst 2960X-48FPD-L | 1.3.6.1.4.1.9.1.1690 |
| Catalyst 2960XR | Catalyst 2960XR-24PD-I | 1.3.6.1.4.1.9.1.1800 |
| Catalyst 2960XR-24TD-I | 1.3.6.1.4.1.9.1.1801 |
| Catalyst 2960XR-48FPS-I | 1.3.6.1.4.1.9.1.1802 |
| Catalyst 2960XR-48LPS-I | 1.3.6.1.4.1.9.1.1803 |
| Catalyst 2960XR-48TS-I | 1.3.6.1.4.1.9.1.1804 |
| Catalyst 2960XR-24PS-I | 1.3.6.1.4.1.9.1.1805 |
| Catalyst 2960XR-24TS-I | 1.3.6.1.4.1.9.1.1806 |
| Catalyst 2960XR-48FPD-L | 1.3.6.1.4.1.9.1.1807 |
| Catalyst 2960XR-48LPD-L | 1.3.6.1.4.1.9.1.1808 |
| Catalyst 2960XR-48PD-L | 1.3.6.1.4.1.9.1.1809 |
| Catalyst 2960XR-24PD-L | 1.3.6.1.4.1.9.1.1810 |
| Catalyst 2960XR-24TD-L | 1.3.6.1.4.1.9.1.1811 |
| Catalyst 2960XR-48FPS-L | 1.3.6.1.4.1.9.1.1812 |
| Catalyst 2960XR-48LPS-L | 1.3.6.1.4.1.9.1.1813 |
| Catalyst 2960XR-48TS-L | 1.3.6.1.4.1.9.1.1814 |
| Catalyst 2960XR-24PS-L | 1.3.6.1.4.1.9.1.1815 |
| Catalyst 2960XR-24TS-L | 1.3.6.1.4.1.9.1.1816 |
| Catalyst 2960XR-48FPD-I | 1.3.6.1.4.1.9.1.1797 |
| Catalyst 2960XR-48LPD-I | 1.3.6.1.4.1.9.1.1798 |
| Catalyst 2960XR-48TD-I | 1.3.6.1.4.1.9.1.1799 |
| Catalyst 2975 | 2975GS-48PS-L | 1.3.6.1.4.1.9.1.1067 |
| 2975GS-48PS-L-Stack | 1.3.6.1.4.1.9.1.1068 |
| Catalyst 3550 | 3550-24-DC | 1.3.6.1.4.1.9.1.452 |
| Catalyst 3560 | 3560-12PC-S | 1.3.6.1.4.1.9.1.1015 |
| 3560-24PS | 1.3.6.1.4.1.9.1.563 |
| 3560-24TS | 1.3.6.1.4.1.9.1.633 |
| 3560-48PS | 1.3.6.1.4.1.9.1.564 |
| 3560-48TS | 1.3.6.1.4.1.9.1.634 |
| 3560-8PC | 1.3.6.1.4.1.9.1.797 |
| 3560G-24PS | 1.3.6.1.4.1.9.1.614 |
| 3560G-24TS | 1.3.6.1.4.1.9.1.615 |
| 3560G-48PS | 1.3.6.1.4.1.9.1.616 |
| 3560G-48TS | 1.3.6.1.4.1.9.1.617 |
| 3560V2-24PS | 1.3.6.1.4.1.9.1.1021 |
| 3560V2-48PS | 1.3.6.1.4.1.9.1.1025 |
| 3560CX-12TC-S | 1.3.6.1.4.1.9.1. 2133 |
| 3560CX-8XPD-S | 1.3.6.1.4.1.9.1.2131 |
| 3560CX-8PT-S | 1.3.6.1.4.1.9.1.2130 |
| Catalyst 3560-C | 3560CG-8PC-S | 1.3.6.1.4.1.9.1.1317 |
| 3560CPD-8PT-S | 1.3.6.1.4.1.9.1.1368 |
| 3560C-8PC-S | 1.3.6.1.4.1.9.1.1466 |
| 3560C-12PC-S | 1.3.6.1.4.1.9.1.1465 |
| Catalyst 3560-E | 3560E-12D | 1.3.6.1.4.1.9.1.930 |
| 3560E-12SD | 1.3.6.1.4.1.9.1.956 |
| 3560E-24PD | 1.3.6.1.4.1.9.1.795 |
| 3560E-24TD | 1.3.6.1.4.1.9.1.793 |
| 3560E-48PD | 1.3.6.1.4.1.9.1.796 |
| 3560E-48TD | 1.3.6.1.4.1.9.1.794 |
| Catalyst 3560-X | 3560X-24P (-L/S/E) | 1.3.6.1.4.1.9.1.1228 |
| 3560X-48PF (-L/S/E) | 1.3.6.1.4.1.9.1.1229 |
| 3560X-48P (-L/S/E) | 1.3.6.1.4.1.9.1.1229 |
| 3560X-48U | 1.3.6.1.4.1.9.1.1710 |
| 3560X-48TS | 1.3.6.1.4.1.9.1.2066 |
| WS-C3560X-48T-S | 1.3.6.1.4.1.9.1.1227 |
| Catalyst 3650 | Catalyst C3650-24TS (-L/S/E) | 1.3.6.1.4.1.9.1.1823 |
| Catalyst C3650-48TS (-L/S/E) | 1.3.6.1.4.1.9.1. 1824 |
| Catalyst C3650-24PS (-L/S/E) | 1.3.6.1.4.1.9.1. 1825 |
| Catalyst C3650-48PS (-L/S/E) | 1.3.6.1.4.1.9.1. 1826 |
| Catalyst C3650-24TD (-L/S/E) | 1.3.6.1.4.1.9.1. 1827 |
| Catalyst C3650-48TD (-L/S/E) | 1.3.6.1.4.1.9.1. 1828 |
| Catalyst C3650-24PD (-L/S/E) | 1.3.6.1.4.1.9.1. 1829 |
| Catalyst C3650-48PD (-L/S/E) | 1.3.6.1.4.1.9.1.1830 |
| Catalyst C3650-Stack (-L/S/E) | 1.3.6.1.4.1.9.1.1830 |
| Catalyst C3650-48PQ (-L/S/E) | 1.3.6.1.4.1.9.1.1881 |
| Catalyst C3650-48TQ (-L/S/E) | 1.3.6.1.4.1.9.1.1882 |
| Catalyst 3750 | 3750 Stack | 1.3.6.1.4.1.9.1.516 |
| 3750-24FS | 1.3.6.1.4.1.9.1.656 |
| 3750-24PS | 1.3.6.1.4.1.9.1.536 |
| 3750-24TS | 1.3.6.1.4.1.9.1.513 |
| 3750-48PS | 1.3.6.1.4.1.9.1.535 |
| 3750-48TS | 1.3.6.1.4.1.9.1.512 |
| 3750G-12S | 1.3.6.1.4.1.9.1.530 |
| 3750G-12S-SD | 1.3.6.1.4.1.9.1.688 |
| 3750G-16TD | 1.3.6.1.4.1.9.1.591 |
| 3750G-24PS | 1.3.6.1.4.1.9.1.602 |
| 3750G-24T | 1.3.6.1.4.1.9.1.514 |
| 3750G-24TS | 1.3.6.1.4.1.9.1.511 |
| 3750G-24TS-1U | 1.3.6.1.4.1.9.1.624 |
| 3750G-24WS-S25 | 1.3.6.1.4.1.9.1.778 |
| 3750G-24WS-S50 | 1.3.6.1.4.1.9.1.779 |
| 3750G-48PS | 1.3.6.1.4.1.9.1.603 |
| 3750G-48TS | 1.3.6.1.4.1.9.1.604 |
| 3750V2-24PS | 1.3.6.1.4.1.9.1.1023 |
| 3750V2-48PS | 1.3.6.1.4.1.9.1.1027 |
| Catalyst 3750-X | 3750X-48P (-L/E) | 1.3.6.1.4.1.9.1.1225 |
| 3750X-48PF (-L/S/E) | 1.3.6.1.4.1.9.1.1225 |
| 3750X-48P (-L/S) | 1.3.6.1.4.1.9.1.1225 |
| 3750X-24P (-L/S/E) | 1.3.6.1.4.1.9.1.1224 |
| Catalyst 3750 Metro | 3750-24TE-M | 1.3.6.1.4.1.9.1.574 |
| Catalyst 3750-E | 3750E-24PD | 1.3.6.1.4.1.9.1.792 |
| 3750E-24TD | 1.3.6.1.4.1.9.1.789 |
| 3750E-48PD | 1.3.6.1.4.1.9.1.791 |
| 3750E-48TD-S | 1.3.6.1.4.1.9.1.790 |
| Catalyst 3850 | Catalyst C3850-24U (-L/S/E) | 1.3.6.1.4.1.9.1.1767 |
| Catalyst C3850-48U (-L/S/E) | 1.3.6.1.4.1.9.1.1768 |
| 3850-48P (-L/S/E) | 1.3.6.1.4.1.9.1.1641 |
| 3850-24P (-L/S/E) | 1.3.6.1.4.1.9.1.1642 |
| 3850-48T (-L/S/E) | 1.3.6.1.4.1.9.1.1643 |
| 3850-24T (-L/S/E) | 1.3.6.1.4.1.9.1.1644 |
| Catalyst 3850-12S-S | 1.3.6.1.4.1.9.1.1880 |
| Catalyst 3850-12S-E | 1.3.6.1.4.1.9.1.1880 |
| Catalyst 3850-24S-S | 1.3.6.1.4.1.9.1.1879 |
| Catalyst 3850-24S-E | 1.3.6.1.4.1.9.1.1879 |
| Catalyst C3850-12X48U | 1.3.6.1.4.1.9.1.1745 |
| Catalyst 4500 | 4503 | 1.3.6.1.4.1.9.5.58 |
| 4503 | 1.3.6.1.4.1.9.1.503 |
| 4506 | 1.3.6.1.4.1.9.5.59 |
| 4506 | 1.3.6.1.4.1.9.1.502 |
| 4507 | 1.3.6.1.4.1.9.1.501 |
| 4510 | 1.3.6.1.4.1.9.1.537 |
| Catalyst 4500-E | 4503-E | 1.3.6.1.4.1.9.1.874 |
| 4506-E | 1.3.6.1.4.1.9.1.875 |
| 4507R-E | 1.3.6.1.4.1.9.1.876 |
| 4510R-E | 1.3.6.1.4.1.9.1.877 |
| 4507R+E | 1.3.6.1.4.1.9.1.1286 |
| 4510R+E | 1.3.6.1.4.1.9.1.1287 |
| Catalyst 4900 | 4948 | 1.3.6.1.4.1.9.1.626 |
| 4948-10GE | 1.3.6.1.4.1.9.1.659 |
| Catalyst 6500 | 6503 | 1.3.6.1.4.1.9.5.56 |
| 6503 | 1.3.6.1.4.1.9.1.449 |
| 6504 | 1.3.6.1.4.1.9.1.657 |
| 6506 | 1.3.6.1.4.1.9.5.45 |
| 6506 | 1.3.6.1.4.1.9.1.282 |
| 6509 | 1.3.6.1.4.1.9.5.44 |
| 6509 | 1.3.6.1.4.1.9.1.283 |
| 6509-NEB | 1.3.6.1.4.1.9.5.61 |
| 6513 | 1.3.6.1.4.1.9.5.50 |
| 6513 | 1.3.6.1.4.1.9.1.400 |
| Catalyst 6500-E | 6509-E | 1.3.6.1.4.1.9.1.283 |
| 6506-E | 1.3.6.1.4.1.9.1.282 |
| 6504-E | 1.3.6.1.4.1.9.1.657 |
| 6503-E | 1.3.6.1.4.1.9.1.449 |
| Catalyst 6800ia | Catalyst 6800ia-48FPD-L | 1.3.6.1.4.1.9.1.1866 |
| Catalyst 6800ia-48TD-L | 1.3.6.1.4.1.9.1.1867 |
| Catalyst 68xx | Catalyst 68xx Virtual Switch | 1.3.6.1.4.1.9.1.1934 |
| Catalyst 6880-X | Catalyst 6880-XLE | 1.3.6.1.4.1.9.1.1784 |
| Catalyst 6807-XL | Catalyst 6807-XL | 1.3.6.1.4.1.9.1.1765 |
| Catalyst 9200 | C9200-24T | 1.3.6.1.4.1.9.1.2694 |
| C9200-24P | 1.3.6.1.4.1.9.1.2694 |
| C9200-48T | 1.3.6.1.4.1.9.1.2694 |
| C9200-48P | 1.3.6.1.4.1.9.1.2694 |
| Catalyst 9200CX | C9200CX-8P-2X2G | 1.3.6.1.4.1.9.1.3097 |
| C9200CX-12P-2X2G | 1.3.6.1.4.1.9.1.3079 |
| C9200CX-12T-2X2G | 1.3.6.1.4.1.9.1.3078 |
| C9200CX-12P-2XGH | 1.3.6.1.4.1.9.1.3164 |
| C9200CX-8PT-2G | 1.3.6.1.4.1.9.1.3098 |
| C9200CX-8UXG-2X | 1.3.6.1.4.1.9.1.3099 |
| C9200CX-8P-2XGH | 1.3.6.1.4.1.9.1.3195 |
| C9200CX-8UXG-2XH | 1.3.6.1.4.1.9.1.3196 |
| Catalyst 9200L | C9200L-24T-4G | 1.3.6.1.4.1.9.1.2695 |
| C9200L-24P-4G | 1.3.6.1.4.1.9.1.2695 |
| C9200L-48T-4G | 1.3.6.1.4.1.9.1.2695 |
| C9200L-48P-4G | 1.3.6.1.4.1.9.1.2695 |
| C9200L-24T-4X | 1.3.6.1.4.1.9.1.2695 |
| C9200L-24P-4X | 1.3.6.1.4.1.9.1.2695 |
| C9200L-48T-4X | 1.3.6.1.4.1.9.1.2695 |
| C9200L-48P-4X | 1.3.6.1.4.1.9.1.2695 |
| Catalyst 9300 | c9300 | 1.3.6.1.4.1.9.1.2494 |
| c930024T | 1.3.6.1.4.1.9.1.2435 |
| c930024P | 1.3.6.1.4.1.9.1.2436 |
| c930024U | 1.3.6.1.4.1.9.1.2437 |
| c930024X | 1.3.6.1.4.1.9.1.2438 |
| c930048T | 1.3.6.1.4.1.9.1.2439 |
| c930048P | 1.3.6.1.4.1.9.1.2440 |
| c930048U | 1.3.6.1.4.1.9.1.2441 |
| c930048UXM | 1.3.6.1.4.1.9.1.2442 |
| Catalyst 9300L | C9300L-24T-4X | 1.3.6.1.4.1.9.1.2583 |
| C9300L-48T-4X | 1.3.6.1.4.1.9.1.2584 |
| C9300L-24P-4G | 1.3.6.1.4.1.9.1.2585 |
| C9300L-48P-4G | 1.3.6.1.4.1.9.1.2586 |
| C9300L-24T-4G | 1.3.6.1.4.1.9.1.2792 |
| C9300L-48T-4G | 1.3.6.1.4.1.9.1.2793 |
| C9300L-24P-4X | 1.3.6.1.4.1.9.1.2798 |
| Catalyst 9300L | C9300L-24UXG-4X | 1.3.6.1.4.1.9.1.2800 |
| C9300L-48UXG-4X | 1.3.6.1.4.1.9.1.2801 |
| C9300L-24UXG-2Q | 1.3.6.1.4.1.9.1.2802 |
| C9300L-48UXG-2Q | 1.3.6.1.4.1.9.1.2803 |
| C9300L-48P-4X | 1.3.6.1.4.1.9.1.2804 |
| C9300L-48PF-4X | 1.3.6.1.4.1.9.1.2992 |
| C9300L-48PF-4G | 1.3.6.1.4.1.9.1.2993 |
| C9300LM-48UX-4Y | 1.3.6.1.4.1.9.1.2804 |
| Catalyst 9400 | C9407R | 1.3.6.1.4.1.9.1.2500 |
| C9410R | 1.3.6.1.4.1.9.1.2501 |
| C9404R | 1.3.6.1.4.1.9.1.2499 |
| Catalyst 9500 | c950012Q | 1.3.6.1.4.1.9.1.2418 |
| c950024Q | 1.3.6.1.4.1.9.1.2419 |
| c950040X | 1.3.6.1.4.1.9.1.2420 |
| Catalyst Express 500 | 500-24LC | 1.3.6.1.4.1.9.1.725 |
| 500-24PC | 1.3.6.1.4.1.9.1.726 |
| 500-24TT | 1.3.6.1.4.1.9.1.724 |
| 500G-12TC | 1.3.6.1.4.1.9.1.727 |
| Catalyst Express 520 | 520-24LC | 1.3.6.1.4.1.9.1.933 |
| 520-24PC | 1.3.6.1.4.1.9.1.934 |
| 520-24TT | 1.3.6.1.4.1.9.1.932 |
| 520-8PC | 1.3.6.1.4.1.9.1.897 |
| 520G-24TC | 1.3.6.1.4.1.9.1.935 |
| Cisco ME 4900 | ME 4924-10GE | 1.3.6.1.4.1.9.1.788 |
| Catalyst C6880x | ciscoC6880x | 1.3.6.1.4.1.9.1.1936 |
| Catalyst 3560CX | Cisco Catalyst 3560CX-8XPD-S | 1.3.6.1.4.1.9.1.2131 |
| Cisco Catalyst 3560CX-8PT-S | 1.3.6.1.4.1.9.1.2130 |
| Catalyst C3560 | catwsC3560CX12pdS | 1.3.6.1.4.1.9.1.2132 |
| catwsC3560CX12pcS | 1.3.6.1.4.1.9.1.2134 |
| catwsC3560CX8tcS | 1.3.6.1.4.1.9.1.2135 |
| catwsC3560CX8pcS | 1.3.6.1.4.1.9.1.2136 |
| Catalyst C2960 | catwsC2960CX8tcL | 1.3.6.1.4.1.9.1.2137 |
| Catalyst 2960CX | Cisco Catalyst 2960CX-8PC-L | 1.3.6.1.4.1.9.1.2191 |

| Series (Ethernet Ports Only) | Supported Device | System Object ID from CISCO-PRODUCTS-MIB or CISCO-STACK-MIB |
|---|---|---|
| Catalyst IE2000 | IE-2000-24T67-B | 1.3.6.1.4.1.9.1.1842 |
| IE-2000-24T67-B | 1.3.6.1.4.1.9.1.1841 |
| IE-2000-24T67-B | 1.3.6.1.4.1.9.1.1844 |
| IE-2000-24T67-B | 1.3.6.1.4.1.9.1.1843 |
| IE-2000-16T67P-G-E | 1.3.6.1.4.1.9.1.1845 |
| IE-2000-4TS-G-L | 1.3.6.1.4.1.9.1.1470 |
| IE-2000-4TS-G-B | 1.3.6.1.4.1.9.1.1470 |
| IE-2000-4T-G-B | 1.3.6.1.4.1.9.1.1471 |
| IE-2000-8TC-B | 1.3.6.1.4.1.9.1.1472 |
| IE-2000-16TC-L | 1.3.6.1.4.1.9.1.1474 |

| Series (Ethernet Ports Only) | Supported Device | System Object ID from CISCO-PRODUCTS-MIB or CISCO-STACK-MIB |
|---|---|---|
| Catalyst IE2000 | IE-2000-16TC-B | 1.3.6.1.4.1.9.1.1474 |
| IE-2000-16TC-G-L | 1.3.6.1.4.1.9.1.1475 |
| IE-2000-16TC-G-N | 1.3.6.1.4.1.9.1.1715 |
| IE-2000-16PTC-G-E | 1.3.6.1.4.1.9.1.1730 |
| IE-2000-4S-TS-G-B | 1.3.6.1.4.1.9.1.1759 |
| IE-2000-4T-G-L | 1.3.6.1.4.1.9.1.1471 |
| IE-2000-16PTC-G-L | 1.3.6.1.4.1.9.1.1729 |
| IE-2000-8TC-G-L | 1.3.6.1.4.1.9.1.1473 |
| IE-2000-8TC-G-B | 1.3.6.1.4.1.9.1.1473 |
| IE-2000-16TC-G-X | 1.3.6.1.4.1.9.1.1520 |

| Series (Ethernet Ports Only) | Supported Device | System Object ID from CISCO-PRODUCTS-MIB or CISCO-STACK-MIB |
|---|---|---|
| Catalyst IE2000U | IE-2000U-4S-G | 1.3.6.1.4.1.9.1.1839 |
| IE-2000U-4TS-G | 1.3.6.1.4.1.9.1.1869 |
| IE-2000U-8TC-G | 1.3.6.1.4.1.9.1.1870 |
| IE-2000U-16TC-GP | 1.3.6.1.4.1.9.1.1868 |
| IE-2000U-16TC-GP | 1.3.6.1.4.1.9.1.1871 |
| IE-2000U-16TC-GP | 1.3.6.1.4.1.9.1.1872 |
| IE-2000U-16TC-GP | 1.3.6.1.4.1.9.1.1840 |

| Series (Ethernet Ports Only) | Supported Device | System Object ID from CISCO-PRODUCTS-MIB or CISCO-STACK-MIB |
|---|---|---|
| Catalyst IE3x00/IE30x0 | IE-3000-4TC | 1.3.6.1.4.1.9.1.958 |
| IE-3000-8TC | 1.3.6.1.4.1.9.1.959 |
| IE-3010-16S-8PC | 1.3.6.1.4.1.9.1.1319 |
| IE-3010-24TC | 1.3.6.1.4.1.9.1.1320 |
| IE-3200-8P2S | 1.3.6.1.4.1.9.1.2684 |
| IE-3200-8P2S-E | 1.3.6.1.4.1.9.1.2684 |
| IE-3200-8T2S | 1.3.6.1.4.1.9.1.2683 |
| IE-3300-8T2S | 1.3.6.1.4.1.9.1.2685 |
| IE-3300-8P2S | 1.3.6.1.4.1.9.1.2686 |

| Series (Ethernet Ports Only) | Supported Device | System Object ID from CISCO-PRODUCTS-MIB or CISCO-STACK-MIB |
|---|---|---|
| Catalyst IE3400/IE3400H | IE-3400-8T2S | 1.3.6.1.4.1.9.1.2872 |
| IE-3400-8P2S | 1.3.6.1.4.1.9.1.2687 |
| IE-3400H-24FT | 1.3.6.1.4.1.9.1.2883 |
| IE-3400H-16FT | 1.3.6.1.4.1.9.1.2882 |
| IE-3400H-16T | 1.3.6.1.4.1.9.1.2885 |
| IE-3400H-24T | 1.3.6.1.4.1.9.1.2886 |
| IE-3400H-8FT | 1.3.6.1.4.1.9.1.2881 |
| IE-3400H-8T | 1.3.6.1.4.1.9.1.2884 |

| Series (Ethernet Ports Only) | Supported Device | System Object ID from CISCO-PRODUCTS-MIB or CISCO-STACK-MIB |
|---|---|---|
| Catalyst IE4000 | IE-4000-8GT8GP4G-E | 1.3.6.1.4.1.9.1.2079 |
| IE-4000-4T4P4G-E | 1.3.6.1.4.1.9.1.2072 |
| IE-4000-8T4G-E | 1.3.6.1.4.1.9.1.2070 |
| IE-4000-16GT4G-E | 1.3.6.1.4.1.9.1.2078 |
| IE-4000-16T4G-E | 1.3.6.1.4.1.9.1.2073 |
| IE-4000-4GC4GP4G-E | 1.3.6.1.4.1.9.1.2077 |
| IE-4000-4GS8GP4G-E | 1.3.6.1.4.1.9.1.2080 |
| IE-4000-4S8P4G-E | 1.3.6.1.4.1.9.1.2074 |
| IE-4000-4TC4G-E | 1.3.6.1.4.1.9.1.2069 |
| IE-4000-8GS4G-E | 1.3.6.1.4.1.9.1.2076 |

| Series (Ethernet Ports Only) | Supported Device | System Object ID from CISCO-PRODUCTS-MIB or CISCO-STACK-MIB |
|---|---|---|
| Catalyst IE4000 | IE-4000-8GT4G-E i+F45:F48 | 1.3.6.1.4.1.9.1.2075 |
| IE-4000-8S4G-E | 1.3.6.1.4.1.9.1.2071 |
| Catalyst IE4010 | IE-4010-4S24P | 1.3.6.1.4.1.9.1.2368 |
| IE-4010-16S12P | 1.3.6.1.4.1.9.1.2369 |
| Catalyst IE5000 | IE-5000-16S12P | 1.3.6.1.4.1.9.1.2296 |
| IE-5000-12S12P-10G | 1.3.6.1.4.1.9.1.2233 |

| Series (Ethernet Ports Only) | Supported Device | System Object ID from CISCO-PRODUCTS-MIB or CISCO-STACK-MIB |
|---|---|---|
| Meraki MS120 | MS120-8 | 1.3.6.1.4.1.29671.2.338 |
| MS120-8LP | 1.3.6.1.4.1.29671.2.339 |
| MS120-8FP | 1.3.6.1.4.1.29671.2.340 |
| MS120-24 | 1.3.6.1.4.1.29671.2.341 |
| MS120-24P | 1.3.6.1.4.1.29671.2.342 |
| MS120-48 | 1.3.6.1.4.1.29671.2.343 |
| MS120-48LP | 1.3.6.1.4.1.29671.2.344 |
| MS120-48FP | 1.3.6.1.4.1.29671.2.356 |
| MS120-48FP | 1.3.6.1.4.1.29671.2.356 |
| Meraki MS125 | MerakiMS125-24 | 1.3.6.1.4.1.29671.2.371 |
| MerakiMS125-24P | 1.3.6.1.4.1.29671.2.372 |
| MerakiMS125-48 | 1.3.6.1.4.1.29671.2.373 |
| MerakiMS125-48LP | 1.3.6.1.4.1.29671.2.374 |
| MerakiMS125-48FP | 1.3.6.1.4.1.29671.2.375 |
| Meraki MS210 | MS210-24P | 1.3.6.1.4.1.29671.2.346 |
| MS210-48LP | 1.3.6.1.4.1.29671.2.348 |
| MS210-24 | 1.3.6.1.4.1.29671.2.345 |
| MS210-48 | 1.3.6.1.4.1.29671.2.347 |
| MS210-48FP | 1.3.6.1.4.1.29671.2.349 |
| Meraki MS220 | MerakiMS220-8 | 1.3.6.1.4.1.29671.2.304 |
| MerakiMS220-8p | 1.3.6.1.4.1.29671.2.305 |
| MerakiMS220-24 | 1.3.6.1.4.1.29671.2.306 |
| MerakiMS220-24p | 1.3.6.1.4.1.29671.2.307 |
| MerakiMS220-48 | 1.3.6.1.4.1.29671.2.308 |
| MerakiMS220-48lp | 1.3.6.1.4.1.29671.2.309 |
| MerakiMS220-48fp | 1.3.6.1.4.1.29671.2.310 |
| Meraki MS225 | MS225-24 | 1.3.6.1.4.1.29671.2.328 |
| MS225-24p | 1.3.6.1.4.1.29671.2.329 |
| MS225-48 | 1.3.6.1.4.1.29671.2.330 |
| MS225-48lp | 1.3.6.1.4.1.29671.2.331 |
| MS225-48fp | 1.3.6.1.4.1.29671.2.332 |
| Meraki MS250 | MS250-24 | 1.3.6.1.4.1.29671.2.333 |
| MS250-24p | 1.3.6.1.4.1.29671.2.334 |
| MS250-48 | 1.3.6.1.4.1.29671.2.335 |
| MS250-48lp | 1.3.6.1.4.1.29671.2.336 |
| MS250-48fp | 1.3.6.1.4.1.29671.2.337 |
| Meraki MS320 | MS320-24 | 1.3.6.1.4.1.29671.2.311 |
| MS320-24p | 1.3.6.1.4.1.29671.2.312 |
| MS320-48 | 1.3.6.1.4.1.29671.2.313 |
| MS320-48lp | 1.3.6.1.4.1.29671.2.314 |
| MS320-48fp | 1.3.6.1.4.1.29671.2.315 |
| Meraki MS350 | MS350-24 | 1.3.6.1.4.1.29671.2.318 |
| MS350-24p | 1.3.6.1.4.1.29671.2.319 |
| MS350-48 | 1.3.6.1.4.1.29671.2.320 |
| MS350-48lp | 1.3.6.1.4.1.29671.2.321 |
| MS350-48fp | 1.3.6.1.4.1.29671.2.322 |
| MS350-24x | 1.3.6.1.4.1.29671.2.327 |
| Meraki MS355 | MS355-24X | 1.3.6.1.4.1.29671.2.357 |
| MS355-24X2 | 1.3.6.1.4.1.29671.2.358 |
| Meraki MS355-48X | 1.3.6.1.4.1.29671.2.359 |
| Meraki MS355-48X2 | 1.3.6.1.4.1.29671.2.360 |
| Meraki MS390 | Meraki MS390-24-HW | 1.3.6.1.4.1.29671.2.362 |
| Meraki MS390-24P-HW | 1.3.6.1.4.1.29671.2.363 |
| Meraki MS390-24U-HW | 1.3.6.1.4.1.29671.2.364 |
| Meraki MS390-24UX-HW | 1.3.6.1.4.1.29671.2.365 |
| Meraki MS390-48-HW | 1.3.6.1.4.1.29671.2.366 |
| Meraki MS390-48P-HW | 1.3.6.1.4.1.29671.2.367 |
| Meraki MS390-48U-HW | 1.3.6.1.4.1.29671.2.368 |
| Meraki MS390-48UX-HW | 1.3.6.1.4.1.29671.2.369 |
| Meraki MS390-48UX2-HW | 1.3.6.1.4.1.29671.2.370 |
| Meraki C9300 | MerakiC9300-24T-M | 1.3.6.1.4.1.29671.2.383 |

| Series (Ethernet Ports Only) | Supported Device | System Object ID from CISCO-PRODUCTS-MIB or CISCO-STACK-MIB |
|---|---|---|
| Cisco 891 | Cisco C891F-K9 | 1.3.6.1.4.1.9.1.1858 |
| Cisco C891FWA-K9 | 1.3.6.1.4.1.9.1.1859 |
| Cisco C891FWE-K9 | 1.3.6.1.4.1.9.1.1860 |
| Cisco 1100 | Cisco C1111-8P | 1.3.6.1.4.1.9.1.2443 |
| Cisco C1111-8PWA | 1.3.6.1.4.1.9.1.2448 |
| Cisco C1111-8PWB | 1.3.6.1.4.1.9.1.2447 |
| Cisco C1111-8PWE | 1.3.6.1.4.1.9.1.2446 |
| Cisco 1800 | Cisco 1861-SRST-B/K9 | 1.3.6.1.4.1.9.1.904 |
| Cisco 1861-SRST-C-B/K9 | 1.3.6.1.4.1.9.1.939 |
| Cisco 1861-SRST-C-F/K9 | 1.3.6.1.4.1.9.1.940 |
| Cisco 1861-SRST-F/K9 | 1.3.6.1.4.1.9.1.905 |
| Cisco 1861-UC-2BRI-K9 | 1.3.6.1.4.1.9.1.902 |
| Cisco 1861-UC-4FXO-K9 | 1.3.6.1.4.1.9.1.903 |
| Cisco1861 | 1.3.6.1.4.1.9.1.1065 |
| Cisco 1900 | Cisco 1905 | 1.3.6.1.4.1.9.1.1192 |
| Cisco 1921 | 1.3.6.1.4.1.9.1.1191 |
| Cisco 1941 | 1.3.6.1.4.1.9.1.1047 |
| Cisco 2800 | Cisco 2811 | 1.3.6.1.4.1.9.1.576 |
| Cisco 2821 | 1.3.6.1.4.1.9.1.577 |
| Cisco 2851 | 1.3.6.1.4.1.9.1.578 |
| Cisco 2900 | Cisco 2911 | 1.3.6.1.4.1.9.1.1045 |
| Cisco 2921 | 1.3.6.1.4.1.9.1.1044 |
| Cisco 2951 | 1.3.6.1.4.1.9.1.1043 |
| Cisco 3800 | Cisco 3825 | 1.3.6.1.4.1.9.1.543 |
| Cisco 3845 | 1.3.6.1.4.1.9.1.544 |
| Cisco 3900 | Cisco 3925 | 1.3.6.1.4.1.9.1.1042 |
| Cisco 3925E | 1.3.6.1.4.1.9.1.1144 |
| Cisco 3945 | 1.3.6.1.4.1.9.1.1041 |
| Cisco 3945E | 1.3.6.1.4.1.9.1.1145 |

| Note | Cisco Emergency Responder 15 and later does not support Install with Data Import. |
|---|---|

| Note | If the Emergency Responder source is in FIPS mode, see https://www.cisco.com/web/software/286319173/139477/ciscocm.ciscossl7_upgrade_CSCwa48315_CSCwa77974_v1.0.k4.cop-ReadMe.pdf for information on the COP file ciscocm.ciscossl7_upgrade_CSCwa48315_CSCwa77974_v1.0.k4.cop . This document details the pre-requisites required for direct upgrade to the 14SU2 or above destination versions. |
|---|---|

| From | To | Upgrade Type |
|---|---|---|
| 12.5(1), 12.5(1a), 12.5(1) SU1, 12.5(1) SU2, 12.5(1) SU3, 12.5(1) SU4, 12.5(1) SU5, 12.5(1) SU6, 12.5(1)SU7, 12.5(1)SU8b,
                                    and 12.5(1)SU9 | 15 | Apply the required Upgrade Readiness COP File (pre-upgrade): ciscocm.cer_preUpgradeCheck-X.k4.cop.sha512 . Note If you want to upgrade Emergency Responder from Release 12.5.x (except for Release 12.5(1)SU6) to 15 and later, you must use
                                             the following COP file: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn . There are no Direct Refresh Upgrade supported paths for Emergency Responder Release 15 and later. Refresh Upgrades from Pre-12.5.x
                                    source to Release 15 and later is not supported. Apply the required Upgrade Readiness COP Files (post-upgrade): ciscocm.cer_postUpgradeCheck-X.k4.cop.sha512 . | Note | If you want to upgrade Emergency Responder from Release 12.5.x (except for Release 12.5(1)SU6) to 15 and later, you must use
                                             the following COP file: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn . |
| Note | If you want to upgrade Emergency Responder from Release 12.5.x (except for Release 12.5(1)SU6) to 15 and later, you must use
                                             the following COP file: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn . |
| 14, 14SU1, 14SU2, 14SU3a, and 14SU4 | 15 | Apply the required Upgrade Readiness COP File (pre-upgrade): ciscocm.cer_preUpgradeCheck-X.k4.cop.sha512 . Required COP files: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn ciscocm.cer_V14_CSCwf99494_Intracluster_v1.1.zip Note You should apply the following COP file for Release 14SU2 before upgrading your Emergency Responder to Release 15 and later: ciscocm.cer_V14SU2_CSCwc26596-CSCwc76921_C0173-1.zip . There are no Direct Refresh Upgrade supported paths for Emergency Responder Release 15 and later. Refresh Upgrades from Pre-12.5.x
                                    source to Release 15 and later is not supported. Apply the required Upgrade Readiness COP Files (post-upgrade): ciscocm.cer_postUpgradeCheck-X.k4.cop.sha512 . | Note | You should apply the following COP file for Release 14SU2 before upgrading your Emergency Responder to Release 15 and later: ciscocm.cer_V14SU2_CSCwc26596-CSCwc76921_C0173-1.zip . |
| Note | You should apply the following COP file for Release 14SU2 before upgrading your Emergency Responder to Release 15 and later: ciscocm.cer_V14SU2_CSCwc26596-CSCwc76921_C0173-1.zip . |

| Note | If you want to upgrade Emergency Responder from Release 12.5.x (except for Release 12.5(1)SU6) to 15 and later, you must use
                                             the following COP file: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn . |
|---|---|

| Note | You should apply the following COP file for Release 14SU2 before upgrading your Emergency Responder to Release 15 and later: ciscocm.cer_V14SU2_CSCwc26596-CSCwc76921_C0173-1.zip . |
|---|---|

|  | Previous Requirements | Release 15 Requirements |
|---|---|---|
| OVA Types | vCPU | RAM | Disk | vCPU | RAM | Disk |
| 20, 000 users | 1 | 4 GB | 80 GB | 2 | 6 GB | 80 GB |
| 30, 000 users | 2 | 6 GB | 110 GB | 2 | 6 GB | 110 GB |
| 40, 000 users | 4 | 6 GB | 110 GB | 4 | 6 GB | 110 GB |

| Step 1 | To access Cisco Bug Search, go to: https://bst.cloudapps.cisco.com/bugsearch |
|---|---|
| Step 2 | Log in with your
                                 			 Cisco.com user ID and password. |
| Step 3 | To look for
                                 			 information about a specific problem, enter the bug ID number in the Search for
                                 			 field, then press Enter . |

| Identifier | Headline |
|---|---|
| CSCwj11507 | 911 calls matches defaults ERL due to IPSubnet hashmap rehashing |
| CSCwk19505 | Clustering with IPv6 phone movement is not picking up right ERL when tracked under IPv6 subnet |

| Identifier | Headline |
|---|---|
| CSCwi97789 | Restrict X.509 certificate validity periods - Revert of CSCvk20066 |
| CSCwi96690 | CER ERL Management API conventional ERL Update failure. COS/TOS fields require text instead of number |
| CSCwj89638 | 911 calls matches default ERL after introduction of IPV6 subnet tracking feature |
| CSCwk02122 | 911 call from IPv6 Only device is routing through default ERL when using IP Subnet Tracking |
| CSCwk09485 | Telephony Setting Use IP Address from Call Signaling is not taking affect in CER for some cases |