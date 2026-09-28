---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-7-0-english-release-notes-cer-70-html-6371f53a65
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/7_0/english/release/notes/cer_70.html
retrieved_at: 2026-08-21T08:30:05.824422+00:00
---

Release Notes for Cisco Emergency Responder 7.0(1)

# Release Notes for Cisco Emergency Responder 7.0(1)

### Download Options

Updated: September 16, 2008

## Table Of Contents

Release Notes for Cisco Emergency Responder 7.0(1)

Contents

Hardware and Software Requirements

Related Documentation

New and Changed Information

Interoperability with Intrado V9-1-1® for Enterprise Service for On-Premise and Off-Premise Phones

Cisco Emergency Responder Administration UI Enhancements

Support for Canadian French

Accessibility Features

Installation Notes

Supported Upgrades

Apply the COP File Before Upgrade from Cisco ER 2.0(x)

Important Upgrade Notes

Important Notes

Additional Open Caveats in Cisco ER 7.0(1)

Installing Upgrade Software on a Cisco MCS 7815-I2

Information for the Last Time of an Emergency Call is not Displayed if Call Record has been Purged

Updating the Database on the Cisco Emergency Responder when CER services on the Publisher Stops

Retrieving the Object ID for Switch Modules on the Switch

Cisco Emergency Responder Detects a Duplicate IP Address or Hostname on a Switch

Removing a Switch from the Network

Caveats

Using Bug Toolkit

Open Caveats

Resolved Caveats

Documentation Updates

Reconciling ALI Discrepancies

View ALI Discrepancies for a Specific ELIN

Migrating Conventional ERL Data to Intrado ERL Data

Migrating Intrado ERL Data to Conventional ERL Data

ERL Migration Tool

Off-Premise Support for IP Phones

Configuring SNMP on a Cisco Unified Communications Manager

Obtaining Documentation and Submitting a Service Request

## Release Notes for Cisco Emergency Responder 7.0(1)

Revised: April 16, 2010

These release notes describe the feature enhancement and caveats for Cisco Emergency Responder (Cisco ER) 7.0(1).

## Contents

These release notes provide the following information:

• Hardware and Software Requirements

• Related Documentation

• New and Changed Information

• Installation Notes

• Important Notes

• Caveats

• Documentation Updates

• Obtaining Documentation and Submitting a Service Request

## Hardware and Software Requirements

Cisco ER 7.0(1) supports a variety of hardware and software components, as shown in the following tables.

Note The type of support can differ between types of hardware; read the tables carefully to determine how Cisco ER will work with the devices you use.

Table 1 lists other software that you must install to use Cisco ER 7.0(1).

Table 1 Required Software

Item

Supported Software Version

Description

Cisco Unified CallManager and Cisco Unified Communications Manager

• Cisco Unified CallManager 4.1

• Cisco Unified CallManager 4.2

• Cisco Unified CallManager 4.3

• Cisco Unified Communications Manager 5.0

• Cisco Unified Communications Manager 5.1

• Cisco Unified Communications Manager 6.0

• Cisco Unified Communications Manager 6.1

• Cisco Unified Communications Manager 7.0

The software that runs the telephony network.

Web browser

• Microsoft Internet Explorer 6.0

• Microsoft Internet Explorer 7.0

Table 2 contains optional software that is recommended for use with Cisco ER 7.0(1).

Table 2 Recommended Software

Item

Minimum Software Version

Description

E-mail server

Any SMTP e-mail server

Used to send e-mail notifications to onsite alert (security) personnel. If you use an SMTP e-mail paging server, personnel are paged instead of e-mailed.

Cisco Unified Operations Manager

Note CiscoWorks IP Telephony Environment Monitor (ITEM) 2.0 is also supported.

Version 1.0

Used to monitor the health and functionality of Cisco ER.

Table 3 lists the different types of phones that support Cisco ER 7.0(1). The type of support Cisco ER 7.0(1) supplies differs depending on the type of phone and the type of switch port to which the phone is attached.

Table 3 Supported Phones

Phones

Description

Phones automatically tracked using CDP

• Cisco Unified IP Phones using SCCP protocol, including 7985, 7975, 7971, 7970, 7965, 7962, 7961, 7960, 7945, 7942, 7941, 7940, 7937, 7936, 7935, 7931, 7912, 7911, 7910, 7906, 7905, 7902, but not including ATA gateways

• Cisco Unified IP Phones using SIP protocol, including 7975, 7971, 7970, 7965, 7962, 7961, 7960, 7945, 7942, 7941, 7940, 7931, 7912, 7911, 7906, 7905, 3911, but not including ATA gateways

• Cisco IP Communicator

These phones do not require special Cisco ER configuration. However, ensure that you enable Cisco Discovery Protocol (CDP) on the switches.

Note Although ATA gateways support CDP and SCCP, Cisco ER cannot automatically track them using CDP. You can track ATA gateways by IP address, or manually assign them to an Emergency Response Location (ERL).

Phones that you can track using IP subnet

• Wireless phones, such as Cisco Unified Wireless IP Phone 7920/7921, and Cisco IP Communicator running on 802.11b

• Supported Cisco Unified IP Phones connected to Cisco or third-party switches that are not discovered or recognized by Cisco ER

• Cisco Unified Personal Communicator

• Third-party SIP phones

• Any phone otherwise supported for automatic tracking that is connected to an unsupported switch port

To track these phones, you must configure the subnet and then assign ERLs to the configured subnets.

Note The use of CAM table tracking can result in the inadvertent discovery and unsupported use of wireless IP phone MACs for tracking purposes. To avoid mis-tracking of wireless IP phones, if CAM table tracking is enabled for a switch, the ERL configured for any switch port connected to a wireless access point must agree with the ERL configured for the IP subnet that will contain the phones connected to that access point.

Phones that you can manually define or track using IP subnet

• Analog phones, for example, phones connected to VG 224/248 and ATA devices

• Generic H.323 endpoints. Supported H.323 phones include Microsoft NetMeeting and video-enabled H.323 endpoints

These phones are only supported if their calls are routed by Cisco Unified Communications Manager.

Note Phones behind analog gateways must be added as manual phones even if a subnet is configured using Cisco ER where the gateway IP address is in that subnet. Phones behind Analog Telephony Adapters (ATAs) are not added as manual phones; they may show as unlocated phones if they are not located behind a switch port.

Note Cisco ER supports SNMP version 1, version 2, and version 2c of a LAN switch.

Table 4 lists the switches that are supported for automatic tracking. You can use other switches, but you might have to manually define phones attached to those switches.

Table 4 Supported Voice-Ready LAN Switches

Series

(Ethernet ports only)

Notes

Device Supported

From CISCO-PRODUCTS-MIB or CISCO-STACK-MIB

Catalyst 500 Express Switch

500-24TT

1.3.6.1.4.1.9.1.724

500-24LC

1.3.6.1.4.1.9.1.725

500-24PC

1.3.6.1.4.1.9.1.726

500G-12TC

1.3.6.1.4.1.9.1.727

Catalyst 520

520-8PC

1.3.6.1.4.1.9.1.897

520-24TT

1.3.6.1.4.1.9.1.932

520-24LC

1.3.6.1.4.1.9.1.933

520-24PC

1.3.6.1.4.1.9.1.934

520G-24TC

1.3.6.1.4.1.9.1.935

Catalyst 2900 XL

12.01.5.WE12 and later

2908 XL

1.3.6.1.4.1.9.1.170

2916 MXL

1.3.6.1.4.1.9.1.171

2924 XL

1.3.6.1.4.1.9.1.183

2924 CXL

1.3.6.1.4.1.9.1.184

2924 XLV

1.3.6.1.4.1.9.1.217

2924 CXLV

1.3.6.1.4.1.9.1.218

2912 XL

1.3.6.1.4.1.9.1.219

2924 MXL

1.3.6.1.4.1.9.1.220

2912 MXFL

1.3.6.1.4.1.9.1.221

2900

1.3.6.1.4.1.9.5.12

2926

1.3.6.1.4.1.9.5.35

2948 G

1.3.6.1.4.1.9.5.42

Catalyst 2940

Cisco IOS 12.1(22)EA1

2940-8TT-S

1.3.6.1.4.1.9.1.540

2940-8TF-S

1.3.6.1.4.1.9.1.542

Catalyst 2948

CatOS

2948G-GE-TX

1.3.6.1.4.1.9.5.62

Catalyst 2950

12.1.9.EA1 and later

2950-12

1.3.6.1.4.1.9.1.323

2950-24

1.3.6.1.4.1.9.1.324

2950-24SX

1.3.6.1.4.1.9.1.480

2950-48SX

1.3.6.1.4.1.9.1.560

2950-48T

1.3.6.1.4.1.9.1.559

2950C-24

1.3.6.1.4.1.9.1.325

2950T-24

1.3.6.1.4.1.9.1.359

2950G-12

1.3.6.1.4.1.9.1.427

2950G-24

1.3.6.1.4.1.9.1.428

2950G-48

1.3.6.1.4.1.9.1.429

2950S-24

1.3.6.1.4.1.9.1.430

2950G-24DC

1.3.6.1.4.1.9.1.472

Catalyst 2960

Cisco IOS 12.2(25)SED

2960-24TC-L

1.3.6.1.4.1.9.1.694

2960-48TC-L

1.3.6.1.4.1.9.1.695

2960G-24TC-L

1.3.6.1.4.1.9.1.696

2960G-48TT-L

1.3.6.1.4.1.9.1.697

2960-24TT-L

1.3.6.1.4.1.9.1.716

2960-48TT-L

1.3.6.1.4.1.9.1.717

2960-8TC-L

1.3.6.1.4.1.9.1.798

2960G-8TC-L

1.3.6.1.4.1.9.1.799

Catalyst 3500 XL

Cisco IPS 12.0(5)XU or later

If you are using Catalyst 3500 clusters, you must assign an IP address to each Catalyst 3500 switch.

3508 GXL

1.3.6.1.4.1.9.1.246

3512 XL

1.3.6.1.4.1.9.1.247

3524 XL

1.3.6.1.4.1.9.1.248

3548 XL

1.3.6.1.4.1.9.1.278

3524 PWR XL

1.3.6.1.4.1.9.1.287

Catalyst 3550

12/1/6/EA1a or later

3550-24

1.3.6.1.4.1.9.1.366

3550-24PWR

1.3.6.1.4.1.9.1.485

3550-48

1.3.6.1.4.1.9.1.367

3550-12T

1.3.6.1.4.1.9.1.368

3550-12G

1.3.6.1.4.1.9.1.431

3550-24DC

1.3.6.1.4.1.9.1.452

Catalyst 3560

Cisco IOS 12.2(20)SE or later

3560-24PS

1.2.6.1.4.1.9.1.563

3560-48PS

1.2.6.1.4.1.9.1.564

3560-24TS-S/-E

1.2.6.1.4.1.9.1.633

3560-48TS-S/-E

1.2.6.1.4.1.9.1.615

3560G-24TS-S/-E

1.2.6.1.4.1.9.1.634

3560G-48TS-S/-E

1.2.6.1.4.1.9.1.617

3560G-24PS-S/-E

1.2.6.1.4.1.9.1.614

3560G-48PS-S/-E

1.2.6.1.4.1.9.1.616

3560-8PC-S

1.3.6.1.4.1.9.1.797

Catalyst 3560E

Cisco IOS Release 12.2(35)SE2 or later

3560E-48TD-S

1.3.6.1.4.1.9.1.794

3560E-48TD-E

1.3.6.1.4.1.9.1.794

3560E-48PD-SF

1.3.6.1.4.1.9.1.796

3560E-48PD-S

1.3.6.1.4.1.9.1.796

3560E-48PD-EF

1.3.6.1.4.1.9.1.796

3560E-48PD-E

1.3.6.1.4.1.9.1.796

3560E-24TD-S

1.3.6.1.4.1.9.1.793

3560E-24TD-E

1.3.6.1.4.1.9.1.793

3560E-24PD-S

1.3.6.1.4.1.9.1.795

3560E-24PD-E

1.3.6.1.4.1.9.1.795

Catalyst 3750

Cisco IOS 12.2(20)SE or later

3750-24

1.3.6.1.4.1.9.1.511

3750-24FS-S

1.3.6.1.4.1.9.1.656

3750-48

1.3.6.1.4.1.9.1.512

3750-24TS

1.3.6.1.4.1.9.1.513

3750-24T

1.3.6.1.4.1.9.1.514

37XX Stack

1.3.6.1.4.1.9.1.516

3750G-12Sfp

1.3.6.1.4.1.9.1.530

3750-48PS

1.3.6.1.4.1.9.1.535

3750-24PS

1.3.6.1.4.1.9.1.536

3750G-16TD

1.3.6.1.4.1.9.1.591

3750G-24PS

1.3.6.1.4.1.9.1.602

3750G-48PS

1.3.6.1.4.1.9.1.603

3750G-48TS

1.3.6.1.4.1.9.1.604

3750G-24TS1U

1.3.6.1.4.1.9.1.624

3750G-24TS1U/-EIU

1.3.6.1.4.1.9.1.624

Catalyst 3750E

Cisco IOS Release 12.2(35)SE2 or later

3750E-48TD-S

1.3.6.1.4.1.9.1.790

3750E-48TD-E

1.3.6.1.4.1.9.1.790

3750E-48PD-SF

1.3.6.1.4.1.9.1.791

3750E-48PD-S

1.3.6.1.4.1.9.1.791

3750E-48PD-EF

1.3.6.1.4.1.9.1.791

3750E-48PD-E

1.3.6.1.4.1.9.1.791

3750E-24TD-S

1.3.6.1.4.1.9.1.789

3750E-24TD-E

1.3.6.1.4.1.9.1.789

3750E-24PD-S

1.3.6.1.4.1.9.1.792

3750E-24PD-E

1.3.6.1.4.1.9.1.792

Catalyst 3750ME

Cisco IOS 12.2(25)EY

3750-24TE-M

1.3.6.1.4.1.9.1.574

Catalyst 4000

Cisco IOS 12.1(13)EW

4000 C

1.3.6.1.4.1.9.1.448

4503

1.3.6.1.4.1.9.1.503

4506

1.3.6.1.4.1.9.1.502

4507

1.3.6.1.4.1.9.1.501

4510R

1.3.6.1.4.1.9.1.537

4948-S-S/-E

1.3.6.1.4.1.9.1.626

4948-10GE-S/-E

1.3.6.1.4.1.9.1.627

Catalyst 4000/4500

Catalyst OS 5.5 or later

4003

1.3.6.1.4.1.9.5.40

4912 G

1.3.6.1.4.1.9.5.41

4006

1.3.6.1.4.1.9.5.46

4500

1.3.6.1.4.1.9.1.14

4503

1.3.6.1.4.1.9.5.58

4503-E

1.3.6.1.4.1.9.1.874

4507R-E

1.3.6.1.4.1.9.1.876

4510R-E

1.3.6.1.4.1.9.1.877

4506

1.3.6.1.4.1.9.5.59

4506-E

1.3.6.1.4.1.9.1.875

Catalyst 4900 Metro

ME-4924-10GE

1.3.6.1.4.1.9.1.706

Catalyst 4948

Cisco IOS 12.2(20)EWA

4948

1.3.6.1.4.1.9.1.626

4948-10GE

1.3.6.1.4.1.9.1.627

Catalyst 5000

Catalyst OS 6.x

5000

1.3.6.1.4.1.9.5.7

5002

1.3.6.1.4.1.9.5.29

Catalyst 5500

5500

1.3.6.1.4.1.9.5.17

5505

1.3.6.1.4.1.9.5.34

5509

1.3.6.1.4.1.9.5.36

Catalyst 6500

Catalyst OS

6503

1.3.6.1.4.1.9.5.56

6509 NEB-A chassis

1.3.6.1.4.1.9.5.61

Catalyst OS 5.5 or later

If using an MSFC module, Cisco IOS 12.1(3a)XL

6006

1.3.6.1.4.1.9.5.38

6009

1.3.6.1.4.1.9.5.39

6509

1.3.6.1.4.1.9.5.44

6506

1.3.6.1.4.1.9.5.45

6509 SP

1.3.6.1.4.1.9.5.47

6509-V-E

1.3.6.1.4.1.9.1.832

6513-E

1.3.6.1.4.1.9.1.400

6513

1.3.6.1.4.1.9.5.50

Catalyst 6500

Cisco IOS

6503

1.3.6.1.4.1.9.1.449

6006

1.3.6.1.4.1.9.1.280

6009

1.3.6.1.4.1.9.1.281

6506

1.3.6.1.4.1.9.1.282

6509

1.3.6.1.4.1.9.1.283

6509 NEB-A chassis

1.3.6.1.4.1.9.1.534

6509 SP

1.3.6.1.4.1.9.1.310

6513

1.3.6.1.4.1.9.1.400

Cisco 2800 Integrated Services Routers

Cisco IOS 12.3(8)T4

Cisco 2811

Cisco 2821

Cisco 2851

1.3.6.1.4.1.9.1.576

1.3.6.1.4.1.9.1.577

1.3.6.1.4.1.9.1.578

Cisco 3725 Multiservice Access Router

Image version: IOS 12.2(8)T5

1.3.6.1.4.1.9.1.414

Cisco 3745 Multiservice Access Router

Image version: IOS 12.2(13)T

1.3.6.1.4.1.9.1.436

Cisco 3800 Integrated Services Routers

Cisco IOS

Cisco 3825

1.3.6.1.4.1.9.1.543

Cisco 3845

1.3.6.1.4.1.9.1.544

ISR 1861

1.3.6.1.4.1.9.1.903

Table 5 lists the network modules and HWICs that are supported in Cisco ER 7.0(1).

Note The Network Modules (NM) and the High-Speed WAN Interface Cards (HWIC) use the System Object IDs of the routers into which they are inserted.

Table 5 Supported Network Modules and HWICs

Network Modules and HWICs

System Object ID from CISCO-PRODUCTS-MIB

NM-16ESW

Refer to above Note

NM-16ESW-1GIG

Refer to above Note

NM-16ESW-PWR

Refer to above Note

NM-16ESW-PWR-1GIG

Refer to above Note

NM-36ESW

Refer to above Note

NM-36ESW-2GIG

Refer to above Note

NM-36ESW-PWR

Refer to above Note

NM-36ESW-PWR-2GIG

Refer to above Note

NME-16ES-1G

1.3.6.1.4.1.9.1.702

NME-16ES-1G-P

1.3.6.1.4.1.9.1.663

NME-X-23ES-1G

1.3.6.1.4.1.9.1.703

NME-X-23ES-1G-P

1.3.6.1.4.1.9.1.664

NME-XD-24ES-1S-P

1.3.6.1.4.1.9.1.665

NME-XD-48ES-2S-P

1.3.6.1.4.1.9.1.666

HWIC-4ESW

Refer to above Note

HWIC-4ESW-POE

Refer to above Note

HWIC-D-9ESW

Refer to above Note

HWIC-D-9ESW-POE

Refer to above Note

Cisco ER 7.0(1) supports the Cisco MCS Unified Communications Manager Appliance platforms shown in Table 6 ; Table 8 lists capacity for these platforms.

Note The number of ERLs that can be deployed is determined by the number of route patterns and translation patterns configurable in Cisco Unified Communications Manager.

Note Cisco ER does not support Cisco Integrated Communications System (ICS) 7750 servers.

Table 6 lists the supported Media Convergence Server (MCS) platforms.

Note You must upgrade servers with less than 2 GB memory or less than 72 GB hard disk drive space.

Table 6 Supported MCS Platforms

Cisco MCS Server

Equivalent OEM Server

CPU

MCS-7816-H3-IPC1

3.2 GHz

MCS-7816-I3-IPC1

3.2 GHz

MCS-7825H-3.0-IPC1

HP DL320-G2

3.06 GHz

MCS-7825H-3.0-IPC2

HP DL320-G2

3.06 GHz

MCS 7825I-3.0-IPC1

IBM x306

3.06 GHz

MCS-7825-H1-IPC1

HP DL320-G3

3.4 GHz

MCS-7825-I1-IPC1

IBM x306

3.4 GHz

MCS-7825-H2-IPC1

HP DL320-G4

2.8 GHz

MCS-7825-I2-IPC1

IBM x306m

2.8 GHz

MCS-7825-H2-IPC2

HP DL320-G4

3.4 GHz

MCS-7825-I2-IPC2

IBM x306m

3.4 GHz

MCS-7825-H3-IPC1

HP DL320-G5

2.13 GHz

MCS-7825-I3-IPC1

IBM x3250

2.13 GHz

MCS-7835H-3.0-IPC1

HP DL380-G3 (1 CPU)

3.06 GHz

MCS-7835I-3.0-IPC1

IBM x345 (1 CPU)

3.06 GHz

MCS-7835-H1-IPC1

HP DL380-G4 (1 CPU)

3.4 GHz

MCS-7835-I1-IPC1

IBM x346 (1 CPU)

3.4 GHz

MCS-7835-H2-IPC1

HP DL380-G5 (1 CPU)

2.33 GHz

MCS-7835-H2-IPC2

HP DL380-G5 (1 CPU)

2.33 GHz

MCS-7835-I2-IPC1

IBM x3650 (1 CPU)

2.33 GHz

MCS-7835-I2-IPC2

IBM x3650 (1 CPU)

2.33 GHz

MCS-7845H-3.0-IPC1

HP DL380-G3 (2 CPUs)

3.06 GHz

MCS-7845I-3.0-IPC1

IBM x345 (2 CPUs)

3.06 GHz

MCS-7845-H1-IPC1

HP DL380-G4 (2 CPUs)

3.4 GHz

MCS-7845-I1-IPC1

IBM x346/x346r (2 CPUs)

3.4 GHz

MCS-7845-H2-IPC1

HP DL380-G5 (2 CPUs)

2.33 GHz

MCS-7845-H2-IPC2

HP DL380-G5 (2 CPUs)

2.33 GHz

MCS-7845-I2-IPC1

IBM x3650 (2 CPUs)

2.33 GHz

MCS-7845-I2-IPC2

IBM x3650 (2 CPUs)

2.33 GHz

Table 7 lists the supported Media Convergence Server (MCS) platforms for upgrades from Cisco ER 1.3 or Cisco ER 7.0(1) only. These servers are not supported for new installations.

Table 7 Supported MCS Platforms for Upgrades from Cisco ER 1.3 or Cisco ER 7.0(1) Only

Cisco MCS Server

Equivalent OEM Server

CPU

MCS-7815I-3.0-IPC1

3.06 GHz

MCS-7815I-3.0-IPC2

3.06 GHz

MCS-7815-I1-IPC1

3.4 GHz

MCS-7815-I1-IPC2

3.4 GHz

MCS-7815-I1-IPC3

3.4 GHz

MCS-7815-I1-IPC4

3.4 GHz

MCS-7815-I2-IPC1

2.8 GHz

Table 8 gives capacity information for Cisco Emergency Responder, assuming one synthetic voice alert per emergency call.

Table 8 Supported Cisco ER 7.0(1) MCS Platforms and Scalability

Cisco 7816

Cisco 7825

Cisco 7835

Cisco 7845

Automatically tracked phones

6,000

12,000

20,000

30,000

Manually configured phones

1,000

2,500

5,000

10,000

Roaming phones (per Cisco Emergency Responder cluster)

600

1,200

2,000

3,000

Switches

200

500

1,000

2,000

Switch ports

12,000

30,000

60,000

120,000

ERLs

1,000

3,000

7,500

10,000

## Related Documentation

Cisco Emergency Responder Documentation

Refer to the publications for Cisco ER 7.0. Navigate from the following documentation URL:

http://www.cisco.com/en/US/products/sw/voicesw/ps842/tsd_products_support_series_home.html

Cisco Unified Communications Manager Documentation

Refer to the Cisco Unified Communications Manager Documentation Guide and other publications specific to your Cisco Unified Communications Manager release. Navigate from the following URL:

http://www.cisco.com/en/US/products/sw/voicesw/ps556/tsd_products_support_series_home.html

Cisco Unified Communications Manager Business Edition Documentation

Refer to the Cisco Unified Communications Manager Business Edition Documentation Guide and other publications that are specific to your Cisco Unified Communications Manager release. Navigate from the following URL:

http://www.cisco.com/en/US/products/ps7273/tsd_products_support_series_home.html

## New and Changed Information

The topics below contain new and changed information that are introduced in Cisco Emergency Responder release 7.0(1):

• Interoperability with Intrado V9-1-1® for Enterprise Service for On-Premise and Off-Premise Phones

• Cisco Emergency Responder Administration UI Enhancements

• Support for Canadian French

• Accessibility Features

### Interoperability with Intrado V9-1-1® for Enterprise Service for On-Premise and Off-Premise Phones

Cisco Emergency Responder 7.0(1) provides interoperability support for Intrado V9-1-1 for Enterprise Service in the Cisco Unified Communications environment. Cisco Emergency Responder and Intrado V9-1-1 for Enterprise Service provides emergency services to phones that are located on the corporate network (on-premise) and phones that are located away from the corporate network (off-premise).

• On-Premise phone — Cisco Emergency Responder 7.0(1) working with Intrado provides for the automation of the PS-ALI update interface, a single point-of-contact for PS-ALI updates, and a single source for emergency call delivery.

• Off-Premise phone — Cisco Emergency Responder 7.0(1) working with Intrado provides support to process user-entered PS-ALI updates and to complete emergency calls on phones that are in jurisdictions where the enterprise has no local PSTN gateway.

### Cisco Emergency Responder Administration UI Enhancements

Cisco Emergency Responder 7.0(1) provides the following Cisco Emergency Responder Administration enhancements:

• Enhancements to the search utility on Switch Port Details

• Customization of email alert, refer to http://www.cisco.com/en/US/docs/voice_ip_comm/cer/7_0/english/administration/guide/e911page.html#wp1052283

• Display of switch port details in explorer view

• Remembering switch port table display across sessions

• Per switch ERL assignment

• Displaying of switch port description in the switch port details page and using switch port description as switch port locations

• Purging of Call History data

• Customization of pager alerts

• Include event viewer contents in email alerts

### Support for Canadian French

Cisco Emergency Responder 7.0(1) supports the localization of the Cisco Emergency Responder User (Security End User) web pages into French (Canadian). The localization support includes voice, web, and email alerts.

### Accessibility Features

The Cisco Emergency Responder User (Security End User) web pages and Cisco Emergency Off-Premise User web pages include accessibility features that assist visually impaired or blind attendants.

## Installation Notes

This section describes upgrade information for Cisco ER 7.0(1) and includes these topics:

• Supported Upgrades

• Apply the COP File Before Upgrade from Cisco ER 2.0(x)

• Important Upgrade Notes

### Supported Upgrades

You must upgrade to Cisco ER 1.3.x or later before you can upgrade to Cisco ER 7.0(1). You cannot upgrade directly to Cisco ER 7.0(1) from earlier versions of Cisco ER.

### Apply the COP File Before Upgrade from Cisco ER 2.0(x)

The Cisco Options Package (cop) file—ciscocm.cerisorename.cop—must be applied to the Cisco ER 2.0(x) release before a Linux upgrade to Cisco ER 7.0(1). You can download the cop file from the following URL: http://tools.cisco.com/support/downloads/go/Redirect.x?mdfid=272877967.

Note You must apply this cop file to Cisco ER 2.0(x) before an attempt to upgrade to Cisco ER 7.0(1). If the cop file is not applied to Cisco ER 2.0(x), you will not see the Cisco ER 7.0(1) image as a valid upgrade option.

To download and install the cop file using Cisco Unified Operating System (OS) Administration, follow these steps:

Step 1 Login to the Cisco Unified OS Administration website on the Cisco ER system.

a. Enter the following URL: https://<CER-server>/cmplatform .

b. Use the navigation pull down menu in the upper right-hand corner to select Cisco Unified OS Administration .

Step 2 Go to Software Upgrades > Install/Upgrade .

Step 3 Enter the required details to access the cop file and click Next .

Step 4 Select the cop file and wait for the system to display the MD5 checksum for validation. Wait for the installation to complete.

Step 5 Go to Show > Software , to verify the cop file name is in the table.

To download and install the cop file using Command Line Interface (CLI), follow these steps:

Step 1 Login to CLI from the console or Secure Shell (SSH).

Step 2 Use the utils system upgrade list remote/local command to select the location of the cop file.

Step 3 Use the utils system upgrade get remote/local command to download the cop file. The CLI terminal will display the MD5 checksum of the cop file.

Step 4 Use the utils system upgrade start command to install the cop file. After the installation is complete, control will be returned to the CLI terminal.

Step 5 Use the show version active command to verify the cop file is on the Cisco ER system.

### Important Upgrade Notes

The following upgrade notes apply to Cisco ER 7.0(1) and earlier:

• If you upgrade your system to Cisco ER 7.0(1) from Cisco ER 2.0(3), you can downgrade to Cisco ER 2.0(3).

• If you upgrade your system to Cisco ER 7.0(1) from Cisco ER 2.0(2), you can downgrade to Cisco ER 2.0(2).

• If you upgrade your system to Cisco ER 7.0(1) from Cisco ER 2.0(1), you should not downgrade to Cisco ER 2.0(1) because of known issues with Cisco ER 2.0(1).

• If you upgrade your system to Cisco ER 7.0(1) from Cisco ER 1.3(2) or an earlier release, you cannot downgrade to the earlier release.

## Important Notes

The following section contains important information that may have been unavailable upon the initial release of documentation.

### Additional Open Caveats in Cisco ER 7.0(1)

The following minor caveats are open in Cisco ER 7.0(1):

• CSCsq29150 —Cisco ER subscriber has incorrect Unified version following new installation

• CSCsr99836— Change of language causes call time formats to differ in Web Alert

• CSCsu07870— After Windows upgrade, the GUI shows `Onsite Alert Pager Address' as null

• CSCso75277— Applying cop file `ciscocm.cerisorename.cop' shows error in GUI

• CSCsr02315— Incorrect information in ERL audit trail after using ERL migration tool

• CSCsu04052— Intrado functionality—TN update, LOS, and MSAG queries fail and result in an error

• CSCsr53381— Cisco ER off-premises end users are not differentiated based on Unified CM 'ClusterID'

• CSCsu03792— After Disaster Recovery System (DRS) Restore, the schedule is always disabled; enabling schedule results in error

• CSCsu22955— Location association using an invalid location returns blank page

• CSCsu22918— Need to enter non-mandatory fields while adding locations in Off-Premise (OFP) website

• CSCsu25909— Issues with 'View ALI Discrepancies' page

### Installing Upgrade Software on a Cisco MCS 7815-I2

For Cisco MCS server 7815-I2, the installation software does not display a reboot option at the end of the installation of Cisco Emergency Responder upgrade software, version 2.x and later. Cisco MCS server 7815-I2 has a motorized DVD player that automatically closes the tray when the machine boots up and this can have the undesired effect of Cisco Emergency Responder not starting up.

After completing the upgrade, take out the DVD from the DVD drive and restart Cisco Emergency Responder on Cisco Unified OS Administration or from the command line interface.

### Information for the Last Time of an Emergency Call is not Displayed if Call Record has been Purged

Be aware that the administrator can schedule a purge or manually purge recent call history records. When you view the details of a phone search for a shared line, CER displays a "No Emergency Call in last 2 months" message if the purge utility has already deleted the call record.

### Updating the Database on the Cisco Emergency Responder when CER services on the Publisher Stops

When the CER service on the publisher stops, and the CER Service on the subscriber takes over, the Cisco Emergency Responder Administration allows you to make updates on the subscriber because the publisher database is active and can be updated.

### Retrieving the Object ID for Switch Modules on the Switch

When you use the snmpget command to query a switch for the Object Identifier (OID) of the switch modules and it returns a generic sysobjectid of 1.3.6.1.4.1.9.1.516, you can specify the switch to return the OID for the switch modules by using the no snmp-server sysobjectid type stack-oid command, saving the switch configuration, and reloading the switch module. After reloading the switch module, the snmpget command returns the specific OID for the switch module.

### Cisco Emergency Responder Detects a Duplicate IP Address or Hostname on a Switch

When Cisco Emergency Responder detects a duplicate IP Address or Hostname entries for a single chassis switch, it displays a CER detected duplicate seed message in the event log viewer. This can be caused when two IP addresses are entered for the same switch in Cisco ER Administration or when Cisco ER is not able to access the chassis group MIB on the switch via SNMP.

If there are two IP addresses entered for the same switch, you must delete the duplicate IP address in CER Administration.

If Cisco ER cannot access the chassis group MIB on the switch, you must apply the chassis group MIB to the SNMP view and perform a selective discovery for the switch.

### Removing a Switch from the Network

When you remove a switch from the network, you must also delete the switch on Cisco Emergency Administration. Failure to delete the switch will increase the time that Cisco ER takes to complete a phone discovery scan. Cisco ER performs a complete discovery scan on all switches when the server is rebooted or when the server is upgraded. The Cisco ER administrator must ensure that all switches that are entered in Cisco ER can be reached by Cisco ER via SNMP.

## Caveats

This section includes these topics:

• Using Bug Toolkit

• Open Caveats

• Resolved Caveats

### Using Bug Toolkit

Known problems (bugs) are graded according to severity level. These release notes contain descriptions of:

• All severity level 1 or 2 bugs.

• Significant severity level 3 bugs.

You can search for problems by using the Cisco Software Bug Toolkit.

To access Bug Toolkit, you need the following items:

• Internet connection

• Web browser

• Cisco.com user ID and password

To use the Software Bug Toolkit, follow these steps:

Step 1 To access the Bug Toolkit, go to http://tools.cisco.com/Support/BugToolKit/action.do?hdnAction=searchBugs .

Step 2 Log in with your Cisco.com user ID and password.

Step 3 To look for information about a specific problem, enter the bug ID number in the "Search for Bug ID" field, then click Go .

### Open Caveats

Table 9 lists Severity 1, 2 and 3 defects that are open for Cisco ER 7.0(1).

For more information about an individual defect, you can access the online record for the defect by clicking the Identifier or going to the URL shown. You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, be aware that Table 9 reflects a snapshot of the defects that were open at the time this report was compiled. For an updated view of open defects, access Bug Toolkit as described in the Using Bug Toolkit .

Table 9 Open Caveats for Cisco ER 7.0(1)

Identifier

Headline and Bug Toolkit Link

CSCsk71390

Computer Telephony Interface (CTI) route point and CTI ports take four minutes to failover to CER subscriber

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk71390

CSCsq02189

Cisco ER GUI shows `Publisher database is down' after restarting database services

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsq02189

CSCsq40146

`Cerserver' process results in a core dump

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsq40146

CSCsq50526

Cisco ER subscriber license page shows `Permanent' before uploading licenses

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsq50526

CSCsr95474

After L2 upgrade from Cisco ER 2.0 to Cisco ER 7.0(1), incorrect IP Phones show up in unlocated list

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsr95474

CSCsr99349

Cisco ER 7.0(1) server reports 200% CPU usage due to incorrect Unified CM configuration

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsr99349

CSCsu30894

Cisco Database Layer Monitor service appears as stopped in `sysAppl' MIIB

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsu30894

CSCtf90741

Cisco ER with Unified CM 7.0 default ERL failover fails due to incorrect redirect CSS

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCtf90741

### Resolved Caveats

Table 10 lists Severity 1, 2 and 3 defects that are resolved for Cisco ER 7.0(1).

For more information about an individual defect, you can access the online record for the defect by clicking the Identifier or going to the URL shown. You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, be aware that Table 10 reflects a snapshot of the defects that were resolved at the time this report was compiled. For an updated view of resolved defects, access Bug Toolkit as described in the Using Bug Toolkit .

Table 10 Resolved Caveats for Cisco ER 7.0(1)

Identifier

Headline and Bug Toolkit Link

CSCsj05687

Cisco ER shows evaluation period is complete after license upload to publisher

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsj05687

CSCsj10748

Cisco Unified Wireless IP Phone 7920 gets discovered behind switchport

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsj10748

CSCsj24030

Unable to upload publisher license due to hostname mismatch after Windows upgrade

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsj24030

CSCsj26242

Cisco ER diagnostic alerts do not have the originating server details

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsj26242

CSCsj79951

Cisco ER Disaster Recovery System (DRS) backup page shows password in clear text

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsj79951

CSCsj99048

Phone Type is shown as `unknown' in a cluster environment

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsj99048

CSCsk00917

Cannot login to Cisco ER publisher after deleting the publisher from GUI

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk00917

CSCsk01164

Logging fails and eventually causes the Cisco ER server to crash

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk01164

CSCsk09741

Changing the IP address of Cisco ER publisher breaks the communication between publisher and subscriber

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk09741

CSCsk13915

Incorrect Cisco ER version is shown in `sysapplpkg' version

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk13915

CSCsk19645

Cisco ER has no audio on emergency call alert to onsite security.

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk19645

CSCsk24266

Tracked IP Phone is shown as unlocated if manual ERL was previously assigned earlier

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk24266

CSCsk27392

Computer Telephony Interface (CTI) ports do not re-register with primary Cisco ER server after failover or fallback

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk27392

CSCsk37388

Need a way to delete the licenses

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk37388

CSCsk42033

ERL name greater than 20 characters cannot be assigned to IPSubnets, Manual, or Synthetic Phones

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk42033

CSCsk50703

Deadlock on route point configurations make the system unusable

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk50703

CSCsk62157

Cisco ER cannot discover and display phones when Cisco ER starts earlier than Unified CM

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk62157

CSCsk62485

Need to be able to delete driver and JTAPI logs from CLI without root access

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk62485

CSCsk70640

The effective ERL is set to `default' for phones located in remote Cisco ER

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk70640

CSCsk71428

`Suppress IP Communicator location change reporting' email alert for Cisco Unified Personal Communicator (CUPC)

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk71428

CSCsk80936

Cisco ER incorrect GUI mapping of publisher and subscriber

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk80936

CSCsl35791

Public Safety Answering Point (PSAP) cannot call back 911 caller if secondary Cisco ER server routed the call

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl35791

CSCsl36003

Cannot add more than six host IP addresses to SNMP Cisco ER

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl36003

CSCsl47746

Cisco ER Unified CM page shows password in plain text

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl47746

CSCsl47834

Cisco ER server logs the user out during upload of license

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl47834

CSCsl54306

911 route points and CTI ports do not register after reboot of Cisco ER followed by Unified CM

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl54306

CSCsl58663

Backup emergency number is not generated correctly for non-911 primary number

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl58663

CSCsl69996

Hostname field in the SNMP settings page does not accept greater than 20 characters

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl69996

CSCsl74024

On the operating system administration page, the years from 2005 to 2009 are incorrectly displayed using Internet Explorer version 7

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl74024

CSCsl76038

`cm-log4jinit-servlet-0.0.0.1-0.i386.rpm' is not installed on Cisco ER

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl76038

CSCsl76561

Files in import and export folder do not get copied during Windows installation

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl76561

CSCsl76574

Cisco ER does not reflect user input primary route point after Windows-to-Linux upgrade

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl76574

CSCsl89792

Primary route point does not get stored after new installation using the SKIP option

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl89792

CSCsl95303

Cisco Tomcat service on Cisco ER is reported as stopped in `SYS-APPL-MIB'

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl95303

CSCsl96739

Linux upgrade from earlier version of Cisco ER to version 2.0(3) results in an error

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl96739

CSCsl96745

Windows upgrade from earlier version of Cisco ER to version 2.0(3) results in an error

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl96745

CSCsm66367

Cluster database host configuration is not migrated during Windows upgrade from Cisco ER version 1.3(2 ) to version 2.0(3)

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsm66367

CSCsm68614

After new installation of Cisco ER publisher and subscriber, Cisco ER publisher shows that subscriber is active

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsm68614

CSCsm80871

Provide rotation on stack trace and system out log files in Cisco ER

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsm80871

CSCso35554

Subscriber installation error connecting to publisher during Cisco ER version 1.3 to version 2.0 upgrade

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCso35554

CSCso73890

Memory leak in Cisco Database Layer Monitor service

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCso73890

CSCso85341

Cannot import third-party signed certificate

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCso85341

CSCsq18956

Log memory usage data at regular intervals and inform administrator of high usage

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsq18956

CSCsq81366

Alerts and call history fails if called address starts with `ELINDigitStrip' pattern

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsq81366

CSCsq82358

Cisco ER should allow Unified CM version downgrade after installation

http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsq82358

## Documentation Updates

This section provides documentation changes that were unavailable when the Cisco Emergency Responder 7.0(1) documentation was released:

• Reconciling ALI Discrepancies

• View ALI Discrepancies for a Specific ELIN

• Migrating Conventional ERL Data to Intrado ERL Data

• Migrating Intrado ERL Data to Conventional ERL Data

• ERL Migration Tool

• Off-Premise Support for IP Phones

• Configuring SNMP on a Cisco Unified Communications Manager

### Reconciling ALI Discrepancies

The Reconciling ALI Discrepancies procedure in the Using Cisco Emergency Responder with Intrado V9-1-1 Enterprise Services chapter has been updated to provide clarification on the data that CER is saving in the database.

You can use Cisco Emergency Responder to compare the records from Intrado VUI with the records in it's database and displays ALI records that have discrepancies. You can examine each record and choose to update the local record with information from Intrado or to update the ALI data in your local CER database with the data obtained from the Intrado VUI.

To reconcile ALI discrepancy records, follow these steps:

Step 1 In Cisco Emergency Responder Administration, choose ERL  > Intrado  ERL > View ALI Discrepancies.

The View Intrado ALI Discrepancies page appears.

Step 2 Enter search criteria to find any specific ELINS and click Find , or click Find without any search criteria to display all Intrado ALI discrepancies. The search results appear.

Step 3 Click on the radio button next to the ELIN that you want to view or click on the V iew ALI Discrepancies button to launch the View Intrado ALI discrepancies for a particular ELIN.

The View Intrado ALI Discrepancies for a particular ELIN window appears.

Step 4 Choose the correct data from either the local Cisco ER database or from Intrado.

To save changes to the local Cisco ER database, click Save . To update the ALI data in your local CER database with the data obtained from the Intrado VUI, click Save Intrado ALI Info .

Step 5 To close this window, click Close .

### View ALI Discrepancies for a Specific ELIN

The description for the fields of the View ALI Discrepancies for a Specific ELIN page includes an updated description for the Save Intrado ALI Info button.

Choose ERL > Intrado  ERL > View ALI Discrepancies and search for discrepancies. The View ALI Discrepancies for a specific ELIN page appears when you select a specific ELIN from the results.

Authorization Requirements

You must have system administrator or ERL administrator authority to access this page.

Description

Use the View ALI Discrepancies for a Specific ELIN page to view discrepancies in the records between the ALI data that is stored in the local CER database and the ALI data for this ELIN in the Intrado database.

Table 11 describes the Find ALI Discrepancies for a specific ELIN page.

Table 11 ALI Discrepancies for Specific ELIN

Field

Description

View Intrado ALI Discrepancies

ALI Fields

List of ALI field information from the local CER database and from Intrado database:

• House Number

• House Suffix

• Street Name

• Prefix Directional

• Street Suffix

• Post Directional

• Community Name

• State

• Main NPA

• Class of Service

• Type of Service

• Exchange

• Customer Name

• Order Number

• Extract Date

• County ID

• Company ID

• Zip Code

• Zip Code Extension

• Customer Code

• Comments

• Longitude

• Latitude

• Elevation

• TAR Code

• Location

• Reserved

Save button

Click Save to save your changes in the local CER database.

Save Intrado ALI Info button

Click Save Intrado ALI Info to update the ALI data in your local CER database with the data obtained from the Intrado VUI.

Cancel Changes button

Click Cancel Changes to change the fields on this page back to the last saved settings.

Close button

Click Close to close the window.

### Migrating Conventional ERL Data to Intrado ERL Data

The Migrating Conventional ERL Data to Intrado ERL Data procedure in the Using Cisco Emergency Responder with Intrado V9-1-1 Enterprise Services chapter has been updated to include the TYS (Type of Service) and CLS (Class of Service) value selection.

To migrate conventional ERLs to Intrado ERLs, follow these steps:

Step 1 In Cisco Emergency Responder Administration, choose ERL >  ERL Migration Tool.

The ERL Migration Tool page appears.

Step 2 Choose Conventional ERL in the search parameter drop-down box, enter the search criteria, and click Find .

Step 3 Select the ERLs that you wish to migrate by checking the checkbox next to the ERL name.

The Enter values for ERL Migration window appears.

Step 4 Choose the proper values for route pattern, CLS (Class of Service) and TYS (Type of Service) from the drop-down lists.

Step 5 Click on Migrate to Intrado ERL.

### Migrating Intrado ERL Data to Conventional ERL Data

The Migrating Intrado ERL Data to Conventional ERL Data procedure in the Using Cisco Emergency Responder with Intrado V9-1-1 Enterprise Services chapter has been updated to include the TYS (Type of Service) and CLS (Class of Service) value selection.

To migrate Intrado ERLs to conventional ERLs, follow these steps:

Step 1 In Cisco Emergency Responder Administration, choose ERL  >  ERL Migration Tool.

The ERL Migration Tool page appears.

Step 2 Choose Intrado ERL in the search parameter drop-down box, enter the search criteria, and click Find .

Step 3 Select the ERLs that you wish to migrate by checking the checkbox next to the ERL name.

The Enter values for ERL Migration window appears.

Step 4 Enter a route/pattern translation pattern.

Step 5 Choose the proper values for CLS (Class of Service) and TYS (Type of Service) from the drop-down lists.

Step 6 Click on Migrate to Conventional ERL.

### ERL Migration Tool

The ERL Migration Tool includes updated TYS (Type of Service) and CLS (Class of Service) value selection information.

The ERL Migration Tool page appears when you choose ERL  > ERL Migration Tool .

Authorization Requirements

You must have system administrator or ERL administrator authority to access this page.

Description

Use the ERL Migration Tool page to migrate ERLs from conventional ERL data to Intrado ERL data and vice versa.

Table 12 describes the ERL Migration Tool page.

Table 12 ERL Migration Tool

Field

Description

Status

Displays status messages

ERL Search Parameter

Find

Select search criteria and click Find to list either existing Conventional ERLs or Intrado ERLs.

From the search results list, you can select the ERLs that you wish to migrate

Migrate to Intrado ERL Button

When you search for Conventional ERLs, you can select the ERLs that you wish to migrate to Intrado.

When you click on the Migrate to Intrado ERL button, you can choose the following.

• Intrado route point for all the selected ERLs.

• Class of Service value for all the selected ERLs.

• Type of Service value for all the selected ERLs.

Migrate to Regular ERL

When you search for Intrado ERLs, you can select the ERLs that you wish to migrate to a conventional ERL data.

When you click on the Migrate to Regular ERL button, you will have the option to enter a route point, specify whether the ERL is a test ER, and Test the ERL. Also, you can choose the following:

• Class of Service value for all the selected ERLs.

• Type of Service value for all the selected ERLs.

### Off-Premise Support for IP Phones

Cisco Emergency Responder Off-Premise Location Management User guide includes the following updated information.

The Cisco Emergency Responder Off-Premise User page allows you to verify the location status of your phones and the directory number assigned to that phone. The location status of your phones are categorized as follows:

• On-Premise—The phone is located on the corporate network. Your administrator specifies a location that you cannot change.

• Off-Premise—The phone is located outside of the corporate network. You must enter your address in the location page and associate a location to the phone

• Unlocated—The phone is registered and has been assigned an ERL, but there is no location associated to phone. Contact your administrator for more information.

• Not Discovered—Either the phone is not registered or Cisco ER has not discovered the location of the phone on the system, and it has not been assigned an ERL. Contact your administrator for more information.

### Configuring SNMP on a Cisco Unified Communications Manager

In order for Cisco ER to work in your telephone network, you must configure SNMP on the Cisco Unified Communications Manager. Verify that all Cisco Unified Communications Managers are SNMP-reachable and that the SNMP settings are correct.

Step 1 Log in to the Cisco ER Administration command line interface and use the following command to ping the Cisco Unified Communications Manager server:

```
utils network ping < ipaddress of CUCM >
```

Step 2 If you successfully ping the Cisco Unified Communications Manager, verify that the SNMP settings are correct on Cisco Unified Communications Manager, as follows:

• If you are using Cisco Unified Communications Manager release 6.0 or later, log in to Cisco Unified Serviceability and choose SNMP > V1/V2c > Community String to check the SNMP community string settings.

• If you are using a Windows-based version of Cisco Unified CallManager, open the services on Cisco Unified Communications Manager and choose:

Start > Settings > Control Panel > Administrative Tools > Services Properties > SNMP > Properties > Security Tab

Step 3 Check to see if Cisco Unified CM is SNMP-reachable by running the following CLI command on the Cisco ER server:

utils snmp get <ccm ip-address/host name> <snmp-read-community-string> .1.3.6.1.2.1.1.2.0

If the Cisco Unified CM is SNMP-reachable, the output of the above command should be similar to the following:

Variable = .1.3.6.1.2.1.1.2.0

value = OBJECT IDENTIFIER <sys-oid-of-ccm>

## Obtaining Documentation and Submitting a Service Request

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What's New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http://www.cisco.com/en/US/docs/general/whatsnew/whatsnew.html

Subscribe to the What's New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application. The RSS feeds are a free service and Cisco currently supports RSS version 2.0.

### Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks . Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1110R)

### Any Internet Protocol (IP) addresses used in this document are not intended to be actual addresses. Any examples, command display output, and figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses in illustrative content is unintentional and coincidental.

### © 2010 Cisco Systems, Inc. All rights reserved.

### This Document Applies to These Products

- Emergency Responder

| Item | Supported Software Version | Description |
|---|---|---|
| Cisco Unified CallManager and Cisco Unified Communications Manager | • Cisco Unified CallManager 4.1 • Cisco Unified CallManager 4.2 • Cisco Unified CallManager 4.3 • Cisco Unified Communications Manager 5.0 • Cisco Unified Communications Manager 5.1 • Cisco Unified Communications Manager 6.0 • Cisco Unified Communications Manager 6.1 • Cisco Unified Communications Manager 7.0 | The software that runs the telephony network. |
| Web browser | • Microsoft Internet Explorer 6.0 • Microsoft Internet Explorer 7.0 |  |

| Item | Minimum Software Version | Description |
|---|---|---|
| E-mail server | Any SMTP e-mail server | Used to send e-mail notifications to onsite alert (security) personnel. If you use an SMTP e-mail paging server, personnel are paged instead of e-mailed. |
| Cisco Unified Operations Manager Note CiscoWorks IP Telephony Environment Monitor (ITEM) 2.0 is also supported. | Version 1.0 | Used to monitor the health and functionality of Cisco ER. |

| Phones | Description |
|---|---|
| Phones automatically tracked using CDP • Cisco Unified IP Phones using SCCP protocol, including 7985, 7975, 7971, 7970, 7965, 7962, 7961, 7960, 7945, 7942, 7941, 7940, 7937, 7936, 7935, 7931, 7912, 7911, 7910, 7906, 7905, 7902, but not including ATA gateways • Cisco Unified IP Phones using SIP protocol, including 7975, 7971, 7970, 7965, 7962, 7961, 7960, 7945, 7942, 7941, 7940, 7931, 7912, 7911, 7906, 7905, 3911, but not including ATA gateways • Cisco IP Communicator | These phones do not require special Cisco ER configuration. However, ensure that you enable Cisco Discovery Protocol (CDP) on the switches. Note Although ATA gateways support CDP and SCCP, Cisco ER cannot automatically track them using CDP. You can track ATA gateways by IP address, or manually assign them to an Emergency Response Location (ERL). |
| Phones that you can track using IP subnet • Wireless phones, such as Cisco Unified Wireless IP Phone 7920/7921, and Cisco IP Communicator running on 802.11b • Supported Cisco Unified IP Phones connected to Cisco or third-party switches that are not discovered or recognized by Cisco ER • Cisco Unified Personal Communicator • Third-party SIP phones • Any phone otherwise supported for automatic tracking that is connected to an unsupported switch port | To track these phones, you must configure the subnet and then assign ERLs to the configured subnets. Note The use of CAM table tracking can result in the inadvertent discovery and unsupported use of wireless IP phone MACs for tracking purposes. To avoid mis-tracking of wireless IP phones, if CAM table tracking is enabled for a switch, the ERL configured for any switch port connected to a wireless access point must agree with the ERL configured for the IP subnet that will contain the phones connected to that access point. |
| Phones that you can manually define or track using IP subnet • Analog phones, for example, phones connected to VG 224/248 and ATA devices • Generic H.323 endpoints. Supported H.323 phones include Microsoft NetMeeting and video-enabled H.323 endpoints | These phones are only supported if their calls are routed by Cisco Unified Communications Manager. Note Phones behind analog gateways must be added as manual phones even if a subnet is configured using Cisco ER where the gateway IP address is in that subnet. Phones behind Analog Telephony Adapters (ATAs) are not added as manual phones; they may show as unlocated phones if they are not located behind a switch port. |

| Series (Ethernet ports only) | Notes | Device Supported | From CISCO-PRODUCTS-MIB or CISCO-STACK-MIB |
|---|---|---|---|
| Catalyst 500 Express Switch |  | 500-24TT | 1.3.6.1.4.1.9.1.724 |
| 500-24LC | 1.3.6.1.4.1.9.1.725 |
| 500-24PC | 1.3.6.1.4.1.9.1.726 |
| 500G-12TC | 1.3.6.1.4.1.9.1.727 |
| Catalyst 520 | 520-8PC | 1.3.6.1.4.1.9.1.897 |
| 520-24TT | 1.3.6.1.4.1.9.1.932 |
| 520-24LC | 1.3.6.1.4.1.9.1.933 |
| 520-24PC | 1.3.6.1.4.1.9.1.934 |
| 520G-24TC | 1.3.6.1.4.1.9.1.935 |
| Catalyst 2900 XL | 12.01.5.WE12 and later | 2908 XL | 1.3.6.1.4.1.9.1.170 |
| 2916 MXL | 1.3.6.1.4.1.9.1.171 |
|  | 2924 XL | 1.3.6.1.4.1.9.1.183 |
| 2924 CXL | 1.3.6.1.4.1.9.1.184 |
| 2924 XLV | 1.3.6.1.4.1.9.1.217 |
| 2924 CXLV | 1.3.6.1.4.1.9.1.218 |
| 2912 XL | 1.3.6.1.4.1.9.1.219 |
| 2924 MXL | 1.3.6.1.4.1.9.1.220 |
| 2912 MXFL | 1.3.6.1.4.1.9.1.221 |
| 2900 | 1.3.6.1.4.1.9.5.12 |
| 2926 | 1.3.6.1.4.1.9.5.35 |
| 2948 G | 1.3.6.1.4.1.9.5.42 |
| Catalyst 2940 | Cisco IOS 12.1(22)EA1 | 2940-8TT-S | 1.3.6.1.4.1.9.1.540 |
| 2940-8TF-S | 1.3.6.1.4.1.9.1.542 |
| Catalyst 2948 | CatOS | 2948G-GE-TX | 1.3.6.1.4.1.9.5.62 |
| Catalyst 2950 | 12.1.9.EA1 and later | 2950-12 | 1.3.6.1.4.1.9.1.323 |
| 2950-24 | 1.3.6.1.4.1.9.1.324 |
| 2950-24SX | 1.3.6.1.4.1.9.1.480 |
| 2950-48SX | 1.3.6.1.4.1.9.1.560 |
| 2950-48T | 1.3.6.1.4.1.9.1.559 |
| 2950C-24 | 1.3.6.1.4.1.9.1.325 |
| 2950T-24 | 1.3.6.1.4.1.9.1.359 |
| 2950G-12 | 1.3.6.1.4.1.9.1.427 |
| 2950G-24 | 1.3.6.1.4.1.9.1.428 |
| 2950G-48 | 1.3.6.1.4.1.9.1.429 |
| 2950S-24 | 1.3.6.1.4.1.9.1.430 |
| 2950G-24DC | 1.3.6.1.4.1.9.1.472 |
| Catalyst 2960 | Cisco IOS 12.2(25)SED | 2960-24TC-L | 1.3.6.1.4.1.9.1.694 |
| 2960-48TC-L | 1.3.6.1.4.1.9.1.695 |
| 2960G-24TC-L | 1.3.6.1.4.1.9.1.696 |
| 2960G-48TT-L | 1.3.6.1.4.1.9.1.697 |
| 2960-24TT-L | 1.3.6.1.4.1.9.1.716 |
| 2960-48TT-L | 1.3.6.1.4.1.9.1.717 |
|  | 2960-8TC-L | 1.3.6.1.4.1.9.1.798 |
| 2960G-8TC-L | 1.3.6.1.4.1.9.1.799 |
| Catalyst 3500 XL | Cisco IPS 12.0(5)XU or later If you are using Catalyst 3500 clusters, you must assign an IP address to each Catalyst 3500 switch. | 3508 GXL | 1.3.6.1.4.1.9.1.246 |
| 3512 XL | 1.3.6.1.4.1.9.1.247 |
| 3524 XL | 1.3.6.1.4.1.9.1.248 |
| 3548 XL | 1.3.6.1.4.1.9.1.278 |
| 3524 PWR XL | 1.3.6.1.4.1.9.1.287 |
| Catalyst 3550 | 12/1/6/EA1a or later | 3550-24 | 1.3.6.1.4.1.9.1.366 |
| 3550-24PWR | 1.3.6.1.4.1.9.1.485 |
| 3550-48 | 1.3.6.1.4.1.9.1.367 |
| 3550-12T | 1.3.6.1.4.1.9.1.368 |
| 3550-12G | 1.3.6.1.4.1.9.1.431 |
| 3550-24DC | 1.3.6.1.4.1.9.1.452 |
| Catalyst 3560 | Cisco IOS 12.2(20)SE or later | 3560-24PS | 1.2.6.1.4.1.9.1.563 |
| 3560-48PS | 1.2.6.1.4.1.9.1.564 |
| 3560-24TS-S/-E | 1.2.6.1.4.1.9.1.633 |
| 3560-48TS-S/-E | 1.2.6.1.4.1.9.1.615 |
| 3560G-24TS-S/-E | 1.2.6.1.4.1.9.1.634 |
| 3560G-48TS-S/-E | 1.2.6.1.4.1.9.1.617 |
| 3560G-24PS-S/-E | 1.2.6.1.4.1.9.1.614 |
| 3560G-48PS-S/-E | 1.2.6.1.4.1.9.1.616 |
| 3560-8PC-S | 1.3.6.1.4.1.9.1.797 |
| Catalyst 3560E | Cisco IOS Release 12.2(35)SE2 or later | 3560E-48TD-S | 1.3.6.1.4.1.9.1.794 |
| 3560E-48TD-E | 1.3.6.1.4.1.9.1.794 |
| 3560E-48PD-SF | 1.3.6.1.4.1.9.1.796 |
| 3560E-48PD-S | 1.3.6.1.4.1.9.1.796 |
| 3560E-48PD-EF | 1.3.6.1.4.1.9.1.796 |
| 3560E-48PD-E | 1.3.6.1.4.1.9.1.796 |
| 3560E-24TD-S | 1.3.6.1.4.1.9.1.793 |
| 3560E-24TD-E | 1.3.6.1.4.1.9.1.793 |
| 3560E-24PD-S | 1.3.6.1.4.1.9.1.795 |
| 3560E-24PD-E | 1.3.6.1.4.1.9.1.795 |
| Catalyst 3750 | Cisco IOS 12.2(20)SE or later | 3750-24 | 1.3.6.1.4.1.9.1.511 |
| 3750-24FS-S | 1.3.6.1.4.1.9.1.656 |
| 3750-48 | 1.3.6.1.4.1.9.1.512 |
| 3750-24TS | 1.3.6.1.4.1.9.1.513 |
| 3750-24T | 1.3.6.1.4.1.9.1.514 |
| 37XX Stack | 1.3.6.1.4.1.9.1.516 |
| 3750G-12Sfp | 1.3.6.1.4.1.9.1.530 |
| 3750-48PS | 1.3.6.1.4.1.9.1.535 |
| 3750-24PS | 1.3.6.1.4.1.9.1.536 |
| 3750G-16TD | 1.3.6.1.4.1.9.1.591 |
| 3750G-24PS | 1.3.6.1.4.1.9.1.602 |
| 3750G-48PS | 1.3.6.1.4.1.9.1.603 |
| 3750G-48TS | 1.3.6.1.4.1.9.1.604 |
| 3750G-24TS1U | 1.3.6.1.4.1.9.1.624 |
| 3750G-24TS1U/-EIU | 1.3.6.1.4.1.9.1.624 |
| Catalyst 3750E | Cisco IOS Release 12.2(35)SE2 or later | 3750E-48TD-S | 1.3.6.1.4.1.9.1.790 |
| 3750E-48TD-E | 1.3.6.1.4.1.9.1.790 |
| 3750E-48PD-SF | 1.3.6.1.4.1.9.1.791 |
| 3750E-48PD-S | 1.3.6.1.4.1.9.1.791 |
| 3750E-48PD-EF | 1.3.6.1.4.1.9.1.791 |
| 3750E-48PD-E | 1.3.6.1.4.1.9.1.791 |
| 3750E-24TD-S | 1.3.6.1.4.1.9.1.789 |
| 3750E-24TD-E | 1.3.6.1.4.1.9.1.789 |
| 3750E-24PD-S | 1.3.6.1.4.1.9.1.792 |
| 3750E-24PD-E | 1.3.6.1.4.1.9.1.792 |
| Catalyst 3750ME | Cisco IOS 12.2(25)EY | 3750-24TE-M | 1.3.6.1.4.1.9.1.574 |
| Catalyst 4000 | Cisco IOS 12.1(13)EW | 4000 C | 1.3.6.1.4.1.9.1.448 |
| 4503 | 1.3.6.1.4.1.9.1.503 |
| 4506 | 1.3.6.1.4.1.9.1.502 |
| 4507 | 1.3.6.1.4.1.9.1.501 |
| 4510R | 1.3.6.1.4.1.9.1.537 |
| 4948-S-S/-E | 1.3.6.1.4.1.9.1.626 |
| 4948-10GE-S/-E | 1.3.6.1.4.1.9.1.627 |
| Catalyst 4000/4500 | Catalyst OS 5.5 or later | 4003 | 1.3.6.1.4.1.9.5.40 |
| 4912 G | 1.3.6.1.4.1.9.5.41 |
| 4006 | 1.3.6.1.4.1.9.5.46 |
| 4500 | 1.3.6.1.4.1.9.1.14 |
| 4503 | 1.3.6.1.4.1.9.5.58 |
| 4503-E | 1.3.6.1.4.1.9.1.874 |
| 4507R-E | 1.3.6.1.4.1.9.1.876 |
| 4510R-E | 1.3.6.1.4.1.9.1.877 |
| 4506 | 1.3.6.1.4.1.9.5.59 |
| 4506-E | 1.3.6.1.4.1.9.1.875 |
| Catalyst 4900 Metro |  | ME-4924-10GE | 1.3.6.1.4.1.9.1.706 |
| Catalyst 4948 | Cisco IOS 12.2(20)EWA | 4948 | 1.3.6.1.4.1.9.1.626 |
| 4948-10GE | 1.3.6.1.4.1.9.1.627 |
| Catalyst 5000 | Catalyst OS 6.x | 5000 | 1.3.6.1.4.1.9.5.7 |
| 5002 | 1.3.6.1.4.1.9.5.29 |
| Catalyst 5500 |  | 5500 | 1.3.6.1.4.1.9.5.17 |
| 5505 | 1.3.6.1.4.1.9.5.34 |
| 5509 | 1.3.6.1.4.1.9.5.36 |
| Catalyst 6500 | Catalyst OS | 6503 | 1.3.6.1.4.1.9.5.56 |
| 6509 NEB-A chassis | 1.3.6.1.4.1.9.5.61 |
| Catalyst OS 5.5 or later If using an MSFC module, Cisco IOS 12.1(3a)XL | 6006 | 1.3.6.1.4.1.9.5.38 |
| 6009 | 1.3.6.1.4.1.9.5.39 |
| 6509 | 1.3.6.1.4.1.9.5.44 |
| 6506 | 1.3.6.1.4.1.9.5.45 |
| 6509 SP | 1.3.6.1.4.1.9.5.47 |
| 6509-V-E | 1.3.6.1.4.1.9.1.832 |
| 6513-E | 1.3.6.1.4.1.9.1.400 |
| 6513 | 1.3.6.1.4.1.9.5.50 |
| Catalyst 6500 | Cisco IOS | 6503 | 1.3.6.1.4.1.9.1.449 |
| 6006 | 1.3.6.1.4.1.9.1.280 |
| 6009 | 1.3.6.1.4.1.9.1.281 |
| 6506 | 1.3.6.1.4.1.9.1.282 |
| 6509 | 1.3.6.1.4.1.9.1.283 |
| 6509 NEB-A chassis | 1.3.6.1.4.1.9.1.534 |
| 6509 SP | 1.3.6.1.4.1.9.1.310 |
| 6513 | 1.3.6.1.4.1.9.1.400 |
| Cisco 2800 Integrated Services Routers | Cisco IOS 12.3(8)T4 | Cisco 2811 Cisco 2821 Cisco 2851 | 1.3.6.1.4.1.9.1.576 |
| 1.3.6.1.4.1.9.1.577 |
| 1.3.6.1.4.1.9.1.578 |
| Cisco 3725 Multiservice Access Router | Image version: IOS 12.2(8)T5 |  | 1.3.6.1.4.1.9.1.414 |
| Cisco 3745 Multiservice Access Router | Image version: IOS 12.2(13)T |  | 1.3.6.1.4.1.9.1.436 |
| Cisco 3800 Integrated Services Routers | Cisco IOS | Cisco 3825 | 1.3.6.1.4.1.9.1.543 |
| Cisco 3845 | 1.3.6.1.4.1.9.1.544 |
| ISR 1861 |  |  | 1.3.6.1.4.1.9.1.903 |

| Network Modules and HWICs | System Object ID from CISCO-PRODUCTS-MIB |
|---|---|
| NM-16ESW | Refer to above Note |
| NM-16ESW-1GIG | Refer to above Note |
| NM-16ESW-PWR | Refer to above Note |
| NM-16ESW-PWR-1GIG | Refer to above Note |
| NM-36ESW | Refer to above Note |
| NM-36ESW-2GIG | Refer to above Note |
| NM-36ESW-PWR | Refer to above Note |
| NM-36ESW-PWR-2GIG | Refer to above Note |
| NME-16ES-1G | 1.3.6.1.4.1.9.1.702 |
| NME-16ES-1G-P | 1.3.6.1.4.1.9.1.663 |
| NME-X-23ES-1G | 1.3.6.1.4.1.9.1.703 |
| NME-X-23ES-1G-P | 1.3.6.1.4.1.9.1.664 |
| NME-XD-24ES-1S-P | 1.3.6.1.4.1.9.1.665 |
| NME-XD-48ES-2S-P | 1.3.6.1.4.1.9.1.666 |
| HWIC-4ESW | Refer to above Note |
| HWIC-4ESW-POE | Refer to above Note |
| HWIC-D-9ESW | Refer to above Note |
| HWIC-D-9ESW-POE | Refer to above Note |

| Cisco MCS Server | Equivalent OEM Server | CPU |
|---|---|---|
| MCS-7816-H3-IPC1 |  | 3.2 GHz |
| MCS-7816-I3-IPC1 |  | 3.2 GHz |
| MCS-7825H-3.0-IPC1 | HP DL320-G2 | 3.06 GHz |
| MCS-7825H-3.0-IPC2 | HP DL320-G2 | 3.06 GHz |
| MCS 7825I-3.0-IPC1 | IBM x306 | 3.06 GHz |
| MCS-7825-H1-IPC1 | HP DL320-G3 | 3.4 GHz |
| MCS-7825-I1-IPC1 | IBM x306 | 3.4 GHz |
| MCS-7825-H2-IPC1 | HP DL320-G4 | 2.8 GHz |
| MCS-7825-I2-IPC1 | IBM x306m | 2.8 GHz |
| MCS-7825-H2-IPC2 | HP DL320-G4 | 3.4 GHz |
| MCS-7825-I2-IPC2 | IBM x306m | 3.4 GHz |
| MCS-7825-H3-IPC1 | HP DL320-G5 | 2.13 GHz |
| MCS-7825-I3-IPC1 | IBM x3250 | 2.13 GHz |
| MCS-7835H-3.0-IPC1 | HP DL380-G3 (1 CPU) | 3.06 GHz |
| MCS-7835I-3.0-IPC1 | IBM x345 (1 CPU) | 3.06 GHz |
| MCS-7835-H1-IPC1 | HP DL380-G4 (1 CPU) | 3.4 GHz |
| MCS-7835-I1-IPC1 | IBM x346 (1 CPU) | 3.4 GHz |
| MCS-7835-H2-IPC1 | HP DL380-G5 (1 CPU) | 2.33 GHz |
| MCS-7835-H2-IPC2 | HP DL380-G5 (1 CPU) | 2.33 GHz |
| MCS-7835-I2-IPC1 | IBM x3650 (1 CPU) | 2.33 GHz |
| MCS-7835-I2-IPC2 | IBM x3650 (1 CPU) | 2.33 GHz |
| MCS-7845H-3.0-IPC1 | HP DL380-G3 (2 CPUs) | 3.06 GHz |
| MCS-7845I-3.0-IPC1 | IBM x345 (2 CPUs) | 3.06 GHz |
| MCS-7845-H1-IPC1 | HP DL380-G4 (2 CPUs) | 3.4 GHz |
| MCS-7845-I1-IPC1 | IBM x346/x346r (2 CPUs) | 3.4 GHz |
| MCS-7845-H2-IPC1 | HP DL380-G5 (2 CPUs) | 2.33 GHz |
| MCS-7845-H2-IPC2 | HP DL380-G5 (2 CPUs) | 2.33 GHz |
| MCS-7845-I2-IPC1 | IBM x3650 (2 CPUs) | 2.33 GHz |
| MCS-7845-I2-IPC2 | IBM x3650 (2 CPUs) | 2.33 GHz |

| Cisco MCS Server | Equivalent OEM Server | CPU |
|---|---|---|
| MCS-7815I-3.0-IPC1 |  | 3.06 GHz |
| MCS-7815I-3.0-IPC2 |  | 3.06 GHz |
| MCS-7815-I1-IPC1 |  | 3.4 GHz |
| MCS-7815-I1-IPC2 |  | 3.4 GHz |
| MCS-7815-I1-IPC3 |  | 3.4 GHz |
| MCS-7815-I1-IPC4 |  | 3.4 GHz |
| MCS-7815-I2-IPC1 |  | 2.8 GHz |

|  | Cisco 7816 | Cisco 7825 | Cisco 7835 | Cisco 7845 |
|---|---|---|---|---|
| Automatically tracked phones | 6,000 | 12,000 | 20,000 | 30,000 |
| Manually configured phones | 1,000 | 2,500 | 5,000 | 10,000 |
| Roaming phones (per Cisco Emergency Responder cluster) | 600 | 1,200 | 2,000 | 3,000 |
| Switches | 200 | 500 | 1,000 | 2,000 |
| Switch ports | 12,000 | 30,000 | 60,000 | 120,000 |
| ERLs | 1,000 | 3,000 | 7,500 | 10,000 |

| Identifier | Headline and Bug Toolkit Link |
|---|---|
| CSCsk71390 | Computer Telephony Interface (CTI) route point and CTI ports take four minutes to failover to CER subscriber http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk71390 |
| CSCsq02189 | Cisco ER GUI shows `Publisher database is down' after restarting database services http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsq02189 |
| CSCsq40146 | `Cerserver' process results in a core dump http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsq40146 |
| CSCsq50526 | Cisco ER subscriber license page shows `Permanent' before uploading licenses http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsq50526 |
| CSCsr95474 | After L2 upgrade from Cisco ER 2.0 to Cisco ER 7.0(1), incorrect IP Phones show up in unlocated list http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsr95474 |
| CSCsr99349 | Cisco ER 7.0(1) server reports 200% CPU usage due to incorrect Unified CM configuration http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsr99349 |
| CSCsu30894 | Cisco Database Layer Monitor service appears as stopped in `sysAppl' MIIB http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsu30894 |
| CSCtf90741 | Cisco ER with Unified CM 7.0 default ERL failover fails due to incorrect redirect CSS http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCtf90741 |

| Identifier | Headline and Bug Toolkit Link |
|---|---|
| CSCsj05687 | Cisco ER shows evaluation period is complete after license upload to publisher http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsj05687 |
| CSCsj10748 | Cisco Unified Wireless IP Phone 7920 gets discovered behind switchport http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsj10748 |
| CSCsj24030 | Unable to upload publisher license due to hostname mismatch after Windows upgrade http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsj24030 |
| CSCsj26242 | Cisco ER diagnostic alerts do not have the originating server details http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsj26242 |
| CSCsj79951 | Cisco ER Disaster Recovery System (DRS) backup page shows password in clear text http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsj79951 |
| CSCsj99048 | Phone Type is shown as `unknown' in a cluster environment http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsj99048 |
| CSCsk00917 | Cannot login to Cisco ER publisher after deleting the publisher from GUI http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk00917 |
| CSCsk01164 | Logging fails and eventually causes the Cisco ER server to crash http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk01164 |
| CSCsk09741 | Changing the IP address of Cisco ER publisher breaks the communication between publisher and subscriber http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk09741 |
| CSCsk13915 | Incorrect Cisco ER version is shown in `sysapplpkg' version http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk13915 |
| CSCsk19645 | Cisco ER has no audio on emergency call alert to onsite security. http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk19645 |
| CSCsk24266 | Tracked IP Phone is shown as unlocated if manual ERL was previously assigned earlier http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk24266 |
| CSCsk27392 | Computer Telephony Interface (CTI) ports do not re-register with primary Cisco ER server after failover or fallback http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk27392 |
| CSCsk37388 | Need a way to delete the licenses http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk37388 |
| CSCsk42033 | ERL name greater than 20 characters cannot be assigned to IPSubnets, Manual, or Synthetic Phones http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk42033 |
| CSCsk50703 | Deadlock on route point configurations make the system unusable http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk50703 |
| CSCsk62157 | Cisco ER cannot discover and display phones when Cisco ER starts earlier than Unified CM http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk62157 |
| CSCsk62485 | Need to be able to delete driver and JTAPI logs from CLI without root access http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk62485 |
| CSCsk70640 | The effective ERL is set to `default' for phones located in remote Cisco ER http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk70640 |
| CSCsk71428 | `Suppress IP Communicator location change reporting' email alert for Cisco Unified Personal Communicator (CUPC) http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk71428 |
| CSCsk80936 | Cisco ER incorrect GUI mapping of publisher and subscriber http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk80936 |
| CSCsl35791 | Public Safety Answering Point (PSAP) cannot call back 911 caller if secondary Cisco ER server routed the call http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl35791 |
| CSCsl36003 | Cannot add more than six host IP addresses to SNMP Cisco ER http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl36003 |
| CSCsl47746 | Cisco ER Unified CM page shows password in plain text http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl47746 |
| CSCsl47834 | Cisco ER server logs the user out during upload of license http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl47834 |
| CSCsl54306 | 911 route points and CTI ports do not register after reboot of Cisco ER followed by Unified CM http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl54306 |
| CSCsl58663 | Backup emergency number is not generated correctly for non-911 primary number http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl58663 |
| CSCsl69996 | Hostname field in the SNMP settings page does not accept greater than 20 characters http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl69996 |
| CSCsl74024 | On the operating system administration page, the years from 2005 to 2009 are incorrectly displayed using Internet Explorer version 7 http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl74024 |
| CSCsl76038 | `cm-log4jinit-servlet-0.0.0.1-0.i386.rpm' is not installed on Cisco ER http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl76038 |
| CSCsl76561 | Files in import and export folder do not get copied during Windows installation http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl76561 |
| CSCsl76574 | Cisco ER does not reflect user input primary route point after Windows-to-Linux upgrade http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl76574 |
| CSCsl89792 | Primary route point does not get stored after new installation using the SKIP option http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl89792 |
| CSCsl95303 | Cisco Tomcat service on Cisco ER is reported as stopped in `SYS-APPL-MIB' http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl95303 |
| CSCsl96739 | Linux upgrade from earlier version of Cisco ER to version 2.0(3) results in an error http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl96739 |
| CSCsl96745 | Windows upgrade from earlier version of Cisco ER to version 2.0(3) results in an error http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsl96745 |
| CSCsm66367 | Cluster database host configuration is not migrated during Windows upgrade from Cisco ER version 1.3(2 ) to version 2.0(3) http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsm66367 |
| CSCsm68614 | After new installation of Cisco ER publisher and subscriber, Cisco ER publisher shows that subscriber is active http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsm68614 |
| CSCsm80871 | Provide rotation on stack trace and system out log files in Cisco ER http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsm80871 |
| CSCso35554 | Subscriber installation error connecting to publisher during Cisco ER version 1.3 to version 2.0 upgrade http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCso35554 |
| CSCso73890 | Memory leak in Cisco Database Layer Monitor service http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCso73890 |
| CSCso85341 | Cannot import third-party signed certificate http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCso85341 |
| CSCsq18956 | Log memory usage data at regular intervals and inform administrator of high usage http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsq18956 |
| CSCsq81366 | Alerts and call history fails if called address starts with `ELINDigitStrip' pattern http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsq81366 |
| CSCsq82358 | Cisco ER should allow Unified CM version downgrade after installation http://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsq82358 |

| Field | Description |
|---|---|
| View Intrado ALI Discrepancies |
| ALI Fields | List of ALI field information from the local CER database and from Intrado database: • House Number • House Suffix • Street Name • Prefix Directional • Street Suffix • Post Directional • Community Name • State • Main NPA • Class of Service • Type of Service • Exchange • Customer Name • Order Number • Extract Date • County ID • Company ID • Zip Code • Zip Code Extension • Customer Code • Comments • Longitude • Latitude • Elevation • TAR Code • Location • Reserved |
| Save button | Click Save to save your changes in the local CER database. |
| Save Intrado ALI Info button | Click Save Intrado ALI Info to update the ALI data in your local CER database with the data obtained from the Intrado VUI. |
| Cancel Changes button | Click Cancel Changes to change the fields on this page back to the last saved settings. |
| Close button | Click Close to close the window. |

| Field | Description |
|---|---|
| Status | Displays status messages |
| ERL Search Parameter |
| Find | Select search criteria and click Find to list either existing Conventional ERLs or Intrado ERLs. From the search results list, you can select the ERLs that you wish to migrate |
| Migrate to Intrado ERL Button | When you search for Conventional ERLs, you can select the ERLs that you wish to migrate to Intrado. When you click on the Migrate to Intrado ERL button, you can choose the following. • Intrado route point for all the selected ERLs. • Class of Service value for all the selected ERLs. • Type of Service value for all the selected ERLs. |
| Migrate to Regular ERL | When you search for Intrado ERLs, you can select the ERLs that you wish to migrate to a conventional ERL data. When you click on the Migrate to Regular ERL button, you will have the option to enter a route point, specify whether the ERL is a test ER, and Test the ERL. Also, you can choose the following: • Class of Service value for all the selected ERLs. • Type of Service value for all the selected ERLs. |