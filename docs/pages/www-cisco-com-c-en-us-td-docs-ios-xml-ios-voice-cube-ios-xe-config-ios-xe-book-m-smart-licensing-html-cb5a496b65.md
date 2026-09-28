---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-smart-licensing-html-cb5a496b65
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_smart_licensing.html
retrieved_at: 2026-08-16T15:44:43.636960+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Smart Licensing

## Chapter: Smart Licensing

# Smart Licensing

## Overview

Cisco Smart Licensing using Policy is a software licensing model that provides visibility of ownership and usage through the
                           Cisco Smart Software Manager (CSSM) portal. CSSM is a central license repository that manages licenses across all Cisco products
                           that you own, including CUBE. Devices send license usage to CSSM either directly or use an on-premises application. Your Smart
                           Account Administrator controls your access to CSSM. Use your Cisco credentials to access the CSSM portal through htttp://software.cisco.com .

Smart Licensing applies to all platform technology (UCK9, Security, DNA) and CUBE feature licenses that the platform uses.

CSSM shows license usage across all devices that are registered to a virtual account. A Virtual Account License Inventory
                           displays the quantity of licenses that are purchased, those licenses in use, and a balance. An Insufficient Licenses alert is displayed if the license balance is below 0.

For example, consider a smart account in CSSM with 50 CUBE trunk session licenses. If you have a single registered CUBE router using 20 trunk sessions, the CSSM licenses page shows Purchased as 50, In Use as 20, and Balance as 30.

For more information on Smart Software Manager, see the Cisco Smart Software Manager User Guide .

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

CUBE reports smart licensing flex subscription entitlement tag

Cisco IOS XE 17.18.1a

Enables CUBE to report flex subscription entitlement tag on all the supported platforms.

To maintain the continued support and entitlements in the future CUBE releases, purchase a collaboration flex subscription.

Smart Licensing Using Policy

Cisco IOS XE Amsterdam 17.3.2

Cisco IOS XE Bengaluru 17.4.1a

Support for tracking license usage based on the historical usage data. Initial registration is no longer required to use features.
                                          License usage is reported periodically based on account policy. Evaluation mode and license reservation are deprecated from
                                          this release.

CUBE Smart License usage is based on dynamic call counting.

Cisco IOS XE Amsterdam 17.2.1r

CUBE Smart Licensing is enhanced to periodically request licenses based on recent call load.

Cisco Smart Licensing Reservation for for CUBE

Cisco IOS XE Gibraltar 16.12.1a

Licenses may be reserved for a CUBE platform, allowing it to be used without an ongoing connection to CSSM.

Cisco Smart Licensing for CUBE

Cisco IOS XE Gibraltar Release 16.11.1a

License requirements for the usage of CUBE trunk sessions are reported to Cisco Smart Licensing.

The smart licensing functionality remains unchanged. For ongoing requirements and continued support, purchase Collaboration
                                             Flex subscription.

## Smart License Operation

Smart Licensing using Policy (SLP) introduces a new paradigm for tracking license usage across your business. In earlier releases,
                           license authorization was forward- looking, binding licenses to a device until the next authorization request. Actual license
                           use during the proceeding reporting period is now sent to Cisco Smart Software Manager (CSSM), allowing you to plan ongoing
                           license requirements based on historical usage data.

Each time a change in license usage is detected, the account policy defines how soon this should be reported to CSSM. Typically,
                           this means that CUBE must send a report at least every 90 days, although it is recommended that reports are sent more frequently.
                           CSSM acknowledges each submitted Resource Utilization Monitoring (RUM) report to ensure that the use is recorded reliably.
                           If the router does not receive an acknowledgment within the minimum reporting period, call processing may be disabled. Call
                           processing is resumed when a valid acknowledgment is received.

Submit the reports to CSSM directly or through a Smart Software Manager On-Prem server. The Cisco Smart Licensing Utility
                           (CSLU) application can also collect usage reports, providing more flexibility in managing your license usage. When a device
                           is not able to communicate directly with a licensing server, a signed usage report can be generated and manually uploaded
                           to CSSM. The CSSM generated acknowledgment must be uploaded to the device within the license reporting policy period to ensure
                           continued use.

Cisco routers configured to process calls between voice ports and IP destinations will report the use of these sessions to
                                       CSSM, where they are listed as a "CUBE v14 Voice Gateway Session" . This usage is reported using the CUBE_T_VGW Smart entitlement tag, which may also be viewed using the show license all command and is provided for your information only. This reporting feature does not enforce voice port or IP sessions and
                                       there would be no service interruption if the router is not registered to CSSM.

A quantity of purchased licenses equal to the number of reported sessions is automatically displayed in CSSM to avoid compliance
                                       warnings. There is no requirement or option to purchase CUBE v14 Voice Gateway Session licenses.

Cisco Smart Software Manager On-Prem Version 8 Release 202102 or later is required for any device using SLP. Refer to the
                                       SLP feature documentation for further information ( Smart Licensing Using Policy for Cisco Enterprise Routing Platforms ).

Warning

When using any of the following Smart Licensing using Policy (SLP) releases, CUBE shuts down if the router does not receive a report acknowledgment from CSSM before the acknowledgment deadline set by the
                                       account policy: 17.3.2, 17.3.3, 17.3.4a, 17.6.1a, or any 17.4 or 17.5 release. CUBE does not shut down in this way with later releases.

The Smart Software Manager Satellite (SSMS) On-prem currently does not support the display of the CUBE High Availability (HA)
                                       device pair (Active-Standby) for devices configured with Smart Licensing using Policy (SLP). The functionality of CUBE remains
                                       unaffected. Future updates will incorporate this capability into SSMS.

License usage is calculated dynamically in the same way as earlier releases, with measurements recorded periodically based
                           on the periodicity timer. Measurements are stored locally until they are submitted to CSSM. This historical usage reporting
                           allows for more accurate aggregation of use across multiple devices over time. The minimum value for the periodicity timer
                           is increased to 8 hours.

The system records the changes every eight hours. It reports these changes to CSSM as soon as it detects any variations from
                           the previous value. However, note that this report is limited to a maximum frequency of once per 24 hours.

If the peak license usage for the current period is different by more or less than 25% of the previously reported value, it
                           is reported and periodicity interval is reset. Use of CUBE Standard Trunk and CUBE Enhanced Trunk licenses are monitored separately.

Smart License Reservation (SLR) for CUBE licenses is not compatible with SLP. Even if a reservation is in place when upgrading, license use reporting will still be
                                       required in accordance with the device policy. Reservations should therefore be returned immediately before or after upgrading
                                       to a release that uses SLP.

From Cisco IOS XE Bengaluru 17.6.1a onwards, calls that are forked using WebSockets are marked as consuming an Enhanced session license.

## Smart Software Licensing Task Flow

IOS XE license use reports may either be pushed to or pulled by a licensing server. Refer to the workflows in Smart Licensing Using Policy for Cisco Enterprise routing Platforms for more details.

### Obtain the Registration ID Token

#### Detailed Steps

Log in to your Smart Account in either CSSM or satellite.

Navigate to the Virtual Account to register the CUBE .

Generate a registration ID token.

### Configure Smart Licensing Transport Settings

Step 1

hostname hostname

#### Example:

```
Device(config)# hostname cube
cube(config)#
```

Ensure that hostname and the PID of the platform are not the same. For example, if the hostname of an ASR1006 router is configured
                                             as "ASR1006," registration is unsuccessful.

Step 2

ip name-server IP Address

#### Example:

```
cube(config)#  ip name-server 10.0.0.1 10.0.0.10
```

Configures valid DNS servers to ensure the correct resolution of the CSSM hostname.

Step 3

ip http client source-interface interface name

#### Example:

```
cube(config)#  ip http client source-interface GigabitEthernet0/0/0
```

Binds the platform HTTP client to the interface used to access the CSSM.

Step 4

license smart transport smart

#### Example:

```
cube(config)#  license smart transport smart
```

Smart transport is the preferred method for sending usage reports.

Step 5

license smart proxy address host-name

#### Example:

```
cube(config)#  license smart proxy address proxy.cisco.com
```

If necessary, configure a proxy-server for the platform when a direct HTTP connection to CSSM is not permitted.

Step 6

license smart proxy port port-number

#### Example:

```
cube(config)# license smart proxy port 80
```

If using an internet proxy, configure a proxy-server port number.

Step 7

license smart url default

#### Example:

```
cube(config)# license smart url default
```

Use the default URL for sending reports to CSSM.

### Associate the Host Platform with CSSM

From Cisco IOS XE Everest 16.11.1a to Cisco IOS XE Amsterdam 17.3.1a, you must register the host platform to either CSSM or
                                 SSM On-Prem to report license usage. From Cisco IOS XE Amsterdam 17.3.2 onwards, license use must be reported to CSSM or SSM On-Prem in accordance with the Smart Account reporting policy.

#### Before you begin

Obtain the registration ID token from your Smart Account.

Configure Smart Licensing transport settings.

Use the following command to register the CUBE platform with CSSM.

license smart trust id_token id_token...local [force]

#### Example:

```
Router# license smart trust id_token ZDEwZDFiODktNWF.............
```

### Configure CUBE Licensed Features

Step 1

voice service voip

#### Example:

```
Device(config)# voice service voip
```

Enters global VoIP cofiguration mode.

Step 2

mode border-element [ license periodicity { hours <8-23> | days <1-30> }]

The periodicity keyword configures the CUBE measurement interval for license usage. If you do not configure the periodicity keyword, license usage is measured once every
                                             7 days.

## Verify Smart License Operation

This section shows CUBE license usage status and license usage history.

Use the following commands to verify the platform license usage:

show cube status —Displays CUBE license status.

The following sample output is for Cisco IOS XE 17.15.1a release:

```
router# show cube status
CUBE-Version : 14.10
SW-Version : 17.15.20250122.183200, Platform CSR8000V
HA-Type : none
Dynamic License Usage Count : 30
```

The following sample output is for Cisco IOS XE 17.18.1a release:

```
Router# show cube status
CUBE-Version : 15
SW-Version : 17.18.20250519.021045, Platform C8000V
HA-Type : none
Dynamic License Usage Count : 0
```

show license status —Displays the license policy and reporting status.

The acknowledgment deadline is presented in this output. Ensure that an acknowledgment is received before this time to ensure
                                                continued operation of the SIP service.

The following sample output is for Cisco IOS XE 17.18.1a release:

```
router# show license status
Utility:
  Status: DISABLED

Smart Licensing Using Policy:
  Status: ENABLED

Account Information:
  Smart Account: <none>
  Virtual Account: <none>

Data Privacy:
  Sending Hostname: yes
    Callhome hostname privacy: DISABLED
    Smart Licensing hostname privacy: DISABLED
  Version privacy: DISABLED

Transport:
  Type: cslu
  Cslu address: <empty>
  Proxy:
    Not Configured
  VRF: <empty>

Policy:   
  Policy in use: Merged from multiple sources.
  Reporting ACK required: yes (CISCO default)
  Unenforced/Non-Export Perpetual Attributes:
    First report requirement (days): 365 (CISCO default)
    Reporting frequency (days): 0 (CISCO default)
    Report on change (days): 90 (CISCO default)
  Unenforced/Non-Export Subscription Attributes:
    First report requirement (days): 90 (CISCO default)
    Reporting frequency (days): 90 (CISCO default)
    Report on change (days): 90 (CISCO default)
  Enforced (Perpetual/Subscription) License Attributes:
    First report requirement (days): 0 (CISCO default)
    Reporting frequency (days): 0 (CISCO default)
    Report on change (days): 0 (CISCO default)
  Export (Perpetual/Subscription) License Attributes:
    First report requirement (days): 0 (CISCO default)
    Reporting frequency (days): 0 (CISCO default)
    Report on change (days): 0 (CISCO default)
          
Miscellaneous:
  Custom Id: <empty>
          
Usage Reporting:
  Last ACK received: <none>
  Next ACK deadline: Mar 18 08:00:01 2025 UTC
  Reporting push interval: 30  days
  Next ACK push check: <none>
  Next report push: Mar 06 09:29:58 2025 UTC
  Last report push: <none>
  Last report file write: <none>
          
Trust Code Installed: <none>
          
Device Telemetry Report Summary:
================================
Data Channel: AVAILABLE
Reports on disk: 0
```

show voice sip license stats —Displays CUBE trunk license usage history.

License usage is recorded in tabular and graphical format for all the three types of trunk call count (Enhanced, Standard,
                                    and Aggregate). Usage is recorded based on the peak value of concurrent calls for a defined interval of time:

Seconds Table—This table stores concurrent calls at every second for the last 60 seconds.

Minutes Table—This table stores regularized peak value of concurrent calls at every minute for the last 60 minutes. Regularized
                                          peak for a minute is the average of top 3 peak values that occurs in a minute.

Hours Table—This table stores peak value for each hour for the last 72 hours.

Days Table—This table stores peak value for each day for the last 72 days.

The following example outputs are truncated to display 60-second and 60-minute tables only.

```
cube#show voice sip license stats table 

        02:50:16 PM Wednesday Nov 13 2019 UTC

CUBE Trunk License Usage  (last 60 seconds)
Period     Average       Max
----------------------------
 1-5           0          0
 6-10          0          0
11-15          0          0
16-20          0          0
21-25          0          0
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0          0
46-50          0          0
51-55          0          0
56-60          0          0

CUBE Trunk License Usage  (last 60 minutes)
Period     Average       Max
----------------------------
 1-5           0          0
 6-10          0          0
11-15          0          0
16-20          0          0
21-25          0          0
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0          0
46-50        324        900
51-55        343        899
56-60        292        600
```

```
cube#show voice sip license stats 

          11:01:01 AM Thursday Aug 29 2019 IST                                                        
                                                                  
                                                                  
                                                           
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Trunk License Usage (last 60 seconds)         
          

                                                                  
                                                                  
                                                     369863146641 
                                                    8880900440044 
                                                    3330922440011 
  910                                                  **         
  820                                                  #*         
  730                                                  ##         
  640                                                 *##*   **   
  550                                                 ###*   ##   
  460                                                 ####  *##*  
  370                                                *####  *##*  
  280                                                #####* ####  
  190                                                ###### ####  
  100                                               *######*####* 
   10                                               ############# 
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          CUBE Trunk License Usage (last 60 minutes)
          * = maximum     # = average
```

show voice sip license status —Displays the license status.

```
Router#show voice sip license status
Host Name: Router
Current Time: Mar 30 2021 00:32:35 UTC
SIP service: Up
License use recorded every: 8 Hour(s)
Next record at: Mar 30 2021 07:00:00 UTC
Recent use of license(s) for CUBE Standard Trunk
Verify Smart License Operation
----------------------------------------------------------------------------
Timestamp Count
----------------------------------------------------------------------------
Mar 29 2021 23:00:00 UTC 0
Mar 29 2021 22:00:00 UTC 9
Mar 29 2021 21:00:00 UTC 24
Mar 29 2021 20:00:00 UTC 13
Mar 29 2021 11:00:00 UTC 0
Mar 29 2021 09:00:00 UTC 2
Recent use of license(s) for CUBE Enhanced Trunk
----------------------------------------------------------------------------
Timestamp Count
----------------------------------------------------------------------------
Mar 29 2021 21:00:00 UTC 0
Mar 29 2021 20:00:00 UTC 2
Mar 29 2021 11:00:00 UTC 0
Mar 29 2021 09:00:00 UTC 8
```

show license usage —Displays the license usage.

The following sample output command is for Cisco IOS XE 17.15.1a release:

```
router#show license usage
prem_250M (ax_250M):
  Description: prem_250M
  Count: 1
  Version: 1.0
  Status: IN USE
  Export status: NOT RESTRICTED
  Feature Name: prem_250M
  Feature Description: prem_250M
  Enforcement type: NOT ENFORCED
  License type: Subscription
CUBE_T_STD (CUBE_T_STD):
  Description: CUBE_T_STD
  Count: 121
  Version: 1.0
  Status: IN USE
  Export status: NOT RESTRICTED
  Feature Name: CUBE_T_STD
  Feature Description: CUBE_T_STD
  Enforcement type: NOT ENFORCED
  License type: Perpetual
```

The following sample output is for Cisco IOS XE 17.18.1a release:

```
router#show license usage
network-essentials_10M (ESR_P_10M_E):
  Description: network-essentials_10M
  Count: 1
  Version: 1.0
  Status: IN USE
  Export status: NOT RESTRICTED
  Feature Name: network-essentials_10M
  Feature Description: network-essentials_10M
  Enforcement type: NOT ENFORCED
  License type: Perpetual

CUBE_TS_ENH (CUBE_TS_ENH):
  Description: CUBE_TS_ENH
  Count: 5
  Version: 1.0
  Status: IN USE
  Export status: NOT RESTRICTED
  Feature Name: CUBE_TS_ENH
  Feature Description: CUBE_TS_ENH
  Enforcement type: NOT ENFORCED
  License type: Perpetual
```

show license summary —Displays the license summary information.

The following sample output is for Cisco IOS XE 17.15.1a release:

```
Device#show license summary
Account Information:
  Smart Account: <none>
  Virtual Account: <none>

License Usage:
  License                  Entitlement tag       Count   Status
  -----------------------------------------------------------------------------
    network-premier_10M     (ESR_P_10M_P)          1     IN USE
    dna-premier_10M         (DNA_P_10M_P)          1     IN USE
    CUBE_T_STD              (CUBE_T_STD)           1     IN USE
```

The following sample output is for Cisco IOS XE 17.18.1a release:

```
Router# show license summary 
Account Information:
  Smart Account: <none>
  Virtual Account: <none>

License Usage:
  License                 Entitlement Tag               Count Status
  -----------------------------------------------------------------------------
  network-essentials_10M  (ESR_P_10M_E)                     1 IN USE
  CUBE_TS_STD             (CUBE_TS_STD)                     1 IN USE
```

### Commands Related to Smart License

show license all —Displays all the information that is related to licensing.

show license tech support —Displays the license technical support information.

show call-home smart-licensing —Displays the destination URL that is configured.

Use the following commands to debug any issues that are related to your Smart License:

debug license feature cube all

```
Request successful for license_type:<license_type_int> and count <usage_count>.
```

Example:

```
*May 18 10:12:45.178: //CUBE-SL/Info/cube_sl_send_entitlement_request: Request successful for license_type: 0 and count 9.
```

```
Request successful for license <license_type_string>
```

Example:

```
*May 18 10:15:45.181: //CUBE-SL/Info/cube_license_request: Request successful for license CUBE_T_STD
```

Example:

```
CUBE Smart Licensing Info/Error/Function debugs enabled
```

## High Availability Configurations

### Smart Licensing with Box-to-Box High Availability

Box-to-Box redundancy uses the Redundancy Group (RG) Infrastructure to form High Availability (high availability) pair of
                                 platforms.

For Smart License configurations on the High Availability pair of platforms, see Smart Software Licensing Task Flow . When reporting license usage, the Smart Agent includes details of its high availability group and, if it is in the active
                                 or standby state. Thus allowing the CSSM to group license requirements for the high availability pair.

The Smart Software Manager Satellite (SSMS) On-prem currently does not support the display of the CUBE High Availability (HA)
                                             device pair (Active-Standby) for devices configured with Smart Licensing using Policy (SLP). The functionality of CUBE remains
                                             unaffected. Future updates will incorporate this capability into SSMS.

Box-to-Box High Availability requires CUBE Trunk Redundant Session licenses. From Cisco IOS XE Amsterdam 17.2.1r onwards, license usage is based on dynamic call counting.

#### Before Failover

Establish a trust relationship for both platforms in the high availability configuration with the same CSSM Smart Virtual
                                       Account.

CSSM sets the reporting policy for each platform.

Only the active platform submits license usage reports to CSSM.

#### After Failover

The platform that switches to the active mode reports license usage to the CSSM.

The new active platform starts a new license measurement interval timer. For example, if a periodicity of five days is configured
                                       and failover occurs after three days, the next measurement will be recorded five days later.

### Verify Smart License Operation for Box-to-Box High Availability

You can use all the commands that are given in the section Verify Smart License Operation to verify the licensing status in High Availability mode. The following commands reflect Smart License information that is
                                 related to Box-to-Box high availability for IOS XE releases:

The following commands reflect Box-to-Box high availability licensing information.

show cube status —Displays CUBE license capacity and the high availability mode.

Following is the sample output from the active instance of CUBE for Cisco IOS XE 17.15.1a release:

```
router#show cube status
CUBE-Version : 14.10
SW-Version : 17.15.3prd3, Platform C8000V
HA-Type : hot-standby-chassis-to-chassis

Dynamic License Usage Count : 10
```

Following is the sample output from the active instance of CUBE for Cisco IOS XE 17.18.1a release:

```
router# sh cube status
CUBE-Version : 15
SW-Version : 17.18.20250519.021045, Platform C8000V
HA-Type : hot-standby-chassis-to-chassis
Dynamic License Usage Count : 50
```

show license usage —Displays license usage.

Following is the sample output from the active instance of CUBE for Cisco IOS XE 17.15.1a release:

```
router#show license usage
prem_250M (ax_250M):
  Description: prem_250M
  Count: 1
  Version: 1.0
  Status: IN USE
  Export status: NOT RESTRICTED
  Feature Name: prem_250M
  Feature Description: prem_250M
  Enforcement type: NOT ENFORCED
  License type: Subscription

CUBE_T_RED (CUBE_T_RED):
  Description: CUBE_T_RED
  Count: 4
  Version: 1.0
  Status: IN USE
  Export status: NOT RESTRICTED
  Feature Name: CUBE_T_RED
  Feature Description: CUBE_T_RED
  Enforcement type: NOT ENFORCED
  License type: Perpetual
```

Following is the sample output from the active instance of CUBE for Cisco IOS XE 17.18.1a release:

```
router#show license usage 
network-premier_10M (ESR_P_10M_P):
  Description: network-premier_10M
  Count: 1
  Version: 1.0
  Status: IN USE
  Export status: NOT RESTRICTED
  Feature Name: network-premier_10M
  Feature Description: network-premier_10M
  Enforcement type: NOT ENFORCED
  License type: Perpetual

CUBE_TS_ENH (CUBE_TS_ENH):
  Description: CUBE_TS_ENH
  Count: 5
  Version: 1.0
  Status: IN USE
  Export status: NOT RESTRICTED
  Feature Name: CUBE_TS_ENH
  Feature Description: CUBE_TS_ENH
  Enforcement type: NOT ENFORCED
  License type: Perpetual
```

show license summary —Displays the license summary information.

Following is the sample output from the active instance of CUBE for Cisco IOS XE 17.15.1a release:

```
Router#sh license summary 
Account Information:
  Smart Account: <none>
  Virtual Account: <none>

License Usage:
  License                 Entitlement tag        Count   Status
  -----------------------------------------------------------------------------
  prem_250M               (ax_250M)                 1    IN USE
  CUBE_T_RED              (CUBE_T_RED)              4    IN USE
```

Following is the sample output from the active instance of CUBE for Cisco IOS XE 17.18.1a release:

```
Router#sh license summary
Account Information:
  Smart Account: <none>
  Virtual Account: <none>

License Usage:
  License                 Entitlement Tag     Count Status
  -----------------------------------------------------------------------------
  network-premier_10M     (ESR_P_10M_P)           1 IN USE
  CUBE_TS_ENH             (CUBE_TS_ENH)          50 IN USE
```

show license all —Displays Active and Standby modes.

Following is the sample output from the active instance of CUBE for Cisco IOS XE 17.15.1a release:

```
router#sh license all
Smart Licensing Status
======================

Smart Licensing is ENABLED

License Conversion:
  Automatic Conversion Enabled: True
  Last Data Push: <none>
  Last File Export: <none>

Export Authorization Key:
  Features Authorized:
    <none>

Utility:
  Status: DISABLED

Smart Licensing Using Policy:
  Status: ENABLED
  Reporting Mode: STANDARD

Account Information:
  Smart Account: <none>
  Virtual Account: <none>

Data Privacy:
  Sending Hostname: yes
    Callhome hostname privacy: DISABLED
    Smart Licensing hostname privacy: DISABLED
  Version privacy: DISABLED

Transport:
  Type: Smart
  URL: https://smartreceiver-stage.cisco.com/licservice/license
  Proxy:
    Not Configured
    VRF: <empty>

Miscellaneous:
  Custom Id: <empty>

Policy:
  Policy in use: Installed On Apr 20 13:26:18 2021 UTC
  Policy name: SLE Policy
  Reporting ACK required: yes (Customer Policy)
  Unenforced/Non-Export Perpetual Attributes:
    First report requirement (days): 30 (Customer Policy)
    Reporting frequency (days): 60 (Customer Policy)
    Report on change (days): 60 (Customer Policy)
  Unenforced/Non-Export Subscription Attributes:
    First report requirement (days): 120 (Customer Policy)
    Reporting frequency (days): 150 (Customer Policy)
    Report on change (days): 120 (Customer Policy)
  Enforced (Perpetual/Subscription) License Attributes:
    First report requirement (days): 0 (CISCO default)
    Reporting frequency (days): 90 (Customer Policy)
    Report on change (days): 60 (Customer Policy)
  Export (Perpetual/Subscription) License Attributes:
    First report requirement (days): 0 (CISCO default)
    Reporting frequency (days): 30 (Customer Policy)
    Report on change (days): 30 (Customer Policy)

Usage Reporting:
  Last ACK received: Oct 08 13:56:07 2021 UTC
  Next ACK deadline: Dec 07 13:56:07 2021 UTC
  Reporting push interval: 1  days
  Next ACK push check: Oct 22 20:44:57 2021 UTC
  Next report push: Oct 23 16:24:52 2021 UTC
  Last report push: Oct 22 16:24:52 2021 UTC
  Last report file write: <none>

Trust Code Installed: Apr 20 13:26:18 2021 UTC

License Usage
=============
prem_250M (ax_250M):
  Description: prem_250M
  Count: 1
  Version: 1.0
  Status: IN USE
  Export status: NOT RESTRICTED
  Feature Name: prem_250M
  Feature Description: prem_250M
  Enforcement type: NOT ENFORCED
  License type: Subscription

CUBE_T_RED (CUBE_T_RED):
  Description: CUBE_T_RED
  Count: 4
  Version: 1.0
  Status: IN USE
  Export status: NOT RESTRICTED
  Feature Name: CUBE_T_RED
  Feature Description: CUBE_T_RED
  Enforcement type: NOT ENFORCED
  License type: Perpetual
  Application HA Info:
    Application Name: CUBE
    Application Id: 1
    Application Role: Active

Product Information
===================
UDI: PID:C8000V,SN:93POM8FF9IZ

Agent Version
=============
Smart Agent for Licensing: 5.1.21_rel/96

License Authorizations
======================
Last Data Push: <none>
Last File Export: <none>

Overall status:
  Active: PID:C8000V,SN:93POM8FF9IZ
      Status: SMART AUTHORIZATION INSTALLED on Sep 21 13:48:56 2021 UTC
      Last Confirmation code: 1fc54c75

Purchased Licenses:
  No Purchase Information Available#      

Derived Licenses:
  Entitlement Tag: regid.2014-05.com.cisco.ax_250M,1.0_b59e576b-91a4-4bf3-9031-5f7543d33912

Usage Report Summary:
=====================
Total: 80,  Purged: 123
Total Acknowledged Received: 0,  Waiting for Ack: 0
Available to Report: 311  Collecting Data: 2  
 
Device Telemetry Report Summary:
================================
Data Channel: AVAILABLE
Reports on disk: 0
```

Following is the sample output from the active instance of CUBE for Cisco IOS XE 17.18.1a release:

```
router#show license all

Smart Licensing Status
======================

Smart Licensing is ENABLED

License Conversion:
  Automatic Conversion Enabled: True
  Status: Not started
  Last Data Push: <none>
  Last File Export: <none>

Export Authorization Key:
  Features Authorized:
    <none>

Utility:
  Status: DISABLED

Smart Licensing Using Policy:
  Status: ENABLED
  Reporting Mode: STANDARD

Account Information:
  Smart Account: BU Production Test As of Jan 30 06:27:46 2025 IST
  Virtual Account: CUBE Regression Mirabile

Data Privacy:
  Sending Hostname: yes
    Callhome hostname privacy: DISABLED
    Smart Licensing hostname privacy: DISABLED
  Version privacy: DISABLED

Transport:
  Type: cslu
  Cslu address: http://8.39.22.48/cslu/v1/pi/CUBE%20Regression%20Mirabile-1
  Proxy:
    Not Configured
  VRF: <empty>

Miscellaneous:
  Custom Id: <empty>

Policy:
  Policy in use: Installed On Dec 06 14:35:24 2024 IST
  Policy name: SLE Policy
  Reporting ACK required: yes (Customer Policy)
  Unenforced/Non-Export Perpetual Attributes:
    First report requirement (days): 30 (Customer Policy)
    Reporting frequency (days): 60 (Customer Policy)
    Report on change (days): 60 (Customer Policy)
  Unenforced/Non-Export Subscription Attributes:
    First report requirement (days): 120 (Customer Policy)
    Reporting frequency (days): 111 (Customer Policy)
    Report on change (days): 111 (Customer Policy)
  Enforced (Perpetual/Subscription) License Attributes:
    First report requirement (days): 30 (Customer Policy)
    Reporting frequency (days): 90 (Customer Policy)
    Report on change (days): 60 (Customer Policy)
  Export (Perpetual/Subscription) License Attributes:
    First report requirement (days): 30 (Customer Policy)
    Reporting frequency (days): 30 (Customer Policy)
    Report on change (days): 30 (Customer Policy)

Usage Reporting:
  Last ACK received: Jan 30 23:57:03 2025 IST
  Next ACK deadline: Mar 31 23:57:03 2025 IST
  Reporting push interval: 30  days
  Next ACK push check: <none>
  Next report push: Feb 28 23:53:28 2025 IST
  Last report push: Jan 29 23:53:28 2025 IST
  Last report file write: <none>

Trust Code Installed: Apr 08 12:56:59 2021 IST

License Usage
=============

network-premier_10M (ESR_P_10M_P):
  Description: network-premier_10M
  Count: 1
  Version: 1.0
  Status: IN USE
  Export status: NOT RESTRICTED
  Feature Name: network-premier_10M
  Feature Description: network-premier_10M
  Enforcement type: NOT ENFORCED
  License type: Perpetual

dna-premier_10M (DNA_P_10M_P):
  Description: dna-premier_10M
  Count: 1
  Version: 1.0
  Status: IN USE
  Export status: NOT RESTRICTED
  Feature Name: dna-premier_10M
  Feature Description: dna-premier_10M
  Enforcement type: NOT ENFORCED
  License type: Subscription

CUBE_TS_ENH (CUBE_TS_ENH):
  Description: CUBE_TS_ENH
  Count: 1
  Version: 1.0
  Status: IN USE
  Export status: NOT RESTRICTED
  Feature Name: CUBE_TS_ENH
  Feature Description: CUBE_TS_ENH
  Enforcement type: NOT ENFORCED
  License type: Perpetual
  Application HA Info:
    Application Name: CUBE
    Application Id: 1
    Application Role: Standby
    Peer Info:
      Application Name: CUBE
      Application Id: 1
      Application Role: Active
      Hostname: Promethium-L1
      PIID: 7261db73-a8b6-490c-a1b6-94790a871e7e
      UDI: P:C8200L-1N-4T,S:FGL2435LHLH
      Smart Account Name: 'nullPtr'
      Virtual Account Name: 'nullPtr'

Product Information
===================
UDI: PID:C8200L-1N-4T,SN:FGL2435LHP5

Agent Version
=============
Smart Agent for Licensing: 6.2.0/11094e344

License Authorizations
======================
Last Data Push: <none>
Last File Export: <none>

Overall status:
  Active: PID:C8200L-1N-4T,SN:FGL2435LHP5
    Status: NOT INSTALLED

Purchased Licenses:
  No Purchase Information Available

Derived Licenses:
  Entitlement Tag: regid.2018-12.com.cisco.ESR_P_10M_E,1.0_328a8b3c-4a0e-49d3-82a0-acb83c7b83a3

Usage Report Summary:
=====================
Total: 666,  Purged: 562
Total Acknowledged Received: 162,  Waiting for Ack: 0
Available to Report: 147  Collecting Data: 5  
 
Device Telemetry Report Summary:
================================
Data Channel: AVAILABLE
Reports on disk: 0
```

### Smart Licensing with Inbox High Availability

You can configure a Cisco ASR 1000 Series Router platform with two Route Processors for Inbox High Availability using Stateful Switchover (SSO). In this configuration, one
                                 Route Processor is active while the other is in standby mode.

For Smart License configuration, see Smart Software Licensing Task Flow . Only the active Route Processor in the SSO configuration reports license usage, so CSSM reserves one set of licenses for
                                 the platform.

Inbox High Availability requires CUBE Trunk Standard Session licenses.

#### Before Failover

Smart License configuration is synchronized between the two Route Processors. Only the active Route Processor registers with
                                       CSSM or satellite.

The CSSM or satellite authorizes license usage requests for the active Route Processor.

For Smart License using Policy, the CSSM or satellite license usage requests for the active Route Processor.

#### After Failover

The Route Processor that switches to active mode, reports license usage to the CSSM or satellite.

As the new report appears to come from the same device, the CSSM or satellite retains the original reservation for the platform.

### Verify Smart License Operation for Inbox High Availability

You can use all the commands that are given in the section Verify Smart License Operation to verify the licensing status in the High Availability mode.

The following commands reflect Inbox High Availability (HA) licensing information:

show cube status —Displays CUBE license capacity and the high availability mode.

```
cube-1#sh cube status
CUBE-Version : 14.4
SW-Version : 17.6.1a, Platform ASR1006-X
HA-Type : hot-standby-card-to-card
cube-2#sh cube status
CUBE-Version : 14.4
SW-Version : 17.6.1a, Platform ASR1006-X
HA-Type : hot-standby-card-to-card
```

show redundancy states —Displays the redundancy state of the Route Processors.

```
cube-1#sh redundancy states
       my state = 13 -ACTIVE 
     peer state = 8  -STANDBY HOT 
           Mode = Duplex
           Unit = Primary
        Unit ID = 48

Redundancy Mode (Operational) = sso
Redundancy Mode (Configured)  = sso
Redundancy State              = sso
     Maintenance Mode = Disabled
    Manual Swact = enabled
 Communications = Up

   client count = 135
 client_notification_TMR = 30000 milliseconds
           RF debug mask = 0x0   
Gateway monitoring interval  = 0 secs
cube-1#
cube-2#sh redundancy states 
       my state = 8  -STANDBY HOT 
     peer state = 13 -ACTIVE 
           Mode = Duplex
           Unit = Secondary
        Unit ID = 49

Redundancy Mode (Operational) = sso
Redundancy Mode (Configured)  = sso
Redundancy State              = sso
     Maintenance Mode = Disabled
    Manual Swact = cannot be initiated from this the standby unit
 Communications = Up

   client count = 135
 client_notification_TMR = 30000 milliseconds
           RF debug mask = 0x0   
Gateway monitoring interval  = 0 secs
cube-2#
```

show license summary —Displays license summary information.

```
cube-1#sh license summary (active) 
License Usage:
  License                 Entitlement tag               Count Status
  -----------------------------------------------------------------------------
  adventerprise           (ASR_1000_AdvEnterprise)          1 IN USE
  ipbase                  (ASR_1000_Ipbase)                 1 IN USE
  CUBE_Standard_Session   (CUBE_T_STD)                     10 IN USE
 
cube-1#

cube-2#sh license summary (standby)
License Usage:
  License                 Entitlement tag               Count Status
  -----------------------------------------------------------------------------
  adventerprise           (ASR_1000_AdvEnterprise)          1 IN USE
  ipbase                  (ASR_1000_Ipbase)                 1 IN USE
cube-2#
```

## Syslog Messages

In B2BHA mode, syslog messages are generated by the active CUBE router and not the standby router. The following is a syslog output for an active CUBE router in B2BHA mode:

```
%CUBE-5-LICENSE_INFO: Requesting for 3 CUBE Enhanced trunk licenses
```

| Feature Name | Releases | Feature Information |
|---|---|---|
| CUBE reports smart licensing flex subscription entitlement tag | Cisco IOS XE 17.18.1a | Enables CUBE to report flex subscription entitlement tag on all the supported platforms. To maintain the continued support and entitlements in the future CUBE releases, purchase a collaboration flex subscription. |
| Smart Licensing Using Policy | Cisco IOS XE Amsterdam 17.3.2 Cisco IOS XE Bengaluru 17.4.1a | Support for tracking license usage based on the historical usage data. Initial registration is no longer required to use features.
                                          License usage is reported periodically based on account policy. Evaluation mode and license reservation are deprecated from
                                          this release. |
| CUBE Smart License usage is based on dynamic call counting. | Cisco IOS XE Amsterdam 17.2.1r | CUBE Smart Licensing is enhanced to periodically request licenses based on recent call load. |
| Cisco Smart Licensing Reservation for for CUBE | Cisco IOS XE Gibraltar 16.12.1a | Licenses may be reserved for a CUBE platform, allowing it to be used without an ongoing connection to CSSM. |
| Cisco Smart Licensing for CUBE | Cisco IOS XE Gibraltar Release 16.11.1a | License requirements for the usage of CUBE trunk sessions are reported to Cisco Smart Licensing. |

| Note | The smart licensing functionality remains unchanged. For ongoing requirements and continued support, purchase Collaboration
                                             Flex subscription. |
|---|---|

| Note | Cisco routers configured to process calls between voice ports and IP destinations will report the use of these sessions to
                                       CSSM, where they are listed as a "CUBE v14 Voice Gateway Session" . This usage is reported using the CUBE_T_VGW Smart entitlement tag, which may also be viewed using the show license all command and is provided for your information only. This reporting feature does not enforce voice port or IP sessions and
                                       there would be no service interruption if the router is not registered to CSSM. A quantity of purchased licenses equal to the number of reported sessions is automatically displayed in CSSM to avoid compliance
                                       warnings. There is no requirement or option to purchase CUBE v14 Voice Gateway Session licenses. |
|---|---|

| Note | Cisco Smart Software Manager On-Prem Version 8 Release 202102 or later is required for any device using SLP. Refer to the
                                       SLP feature documentation for further information ( Smart Licensing Using Policy for Cisco Enterprise Routing Platforms ). |
|---|---|

| Warning | When using any of the following Smart Licensing using Policy (SLP) releases, CUBE shuts down if the router does not receive a report acknowledgment from CSSM before the acknowledgment deadline set by the
                                       account policy: 17.3.2, 17.3.3, 17.3.4a, 17.6.1a, or any 17.4 or 17.5 release. CUBE does not shut down in this way with later releases. |
|---|---|

| Note | The Smart Software Manager Satellite (SSMS) On-prem currently does not support the display of the CUBE High Availability (HA)
                                       device pair (Active-Standby) for devices configured with Smart Licensing using Policy (SLP). The functionality of CUBE remains
                                       unaffected. Future updates will incorporate this capability into SSMS. |
|---|---|

| Note | Smart License Reservation (SLR) for CUBE licenses is not compatible with SLP. Even if a reservation is in place when upgrading, license use reporting will still be
                                       required in accordance with the device policy. Reservations should therefore be returned immediately before or after upgrading
                                       to a release that uses SLP. |
|---|---|

| Note | From Cisco IOS XE Bengaluru 17.6.1a onwards, calls that are forked using WebSockets are marked as consuming an Enhanced session license. |
|---|---|

| Step 1 | hostname hostname Example: Device(config)# hostname cube
cube(config)# Ensure that hostname and the PID of the platform are not the same. For example, if the hostname of an ASR1006 router is configured
                                             as "ASR1006," registration is unsuccessful. |
|---|---|
| Step 2 | ip name-server IP Address Example: cube(config)#  ip name-server 10.0.0.1 10.0.0.10 Configures valid DNS servers to ensure the correct resolution of the CSSM hostname. |
| Step 3 | ip http client source-interface interface name Example: cube(config)#  ip http client source-interface GigabitEthernet0/0/0 Binds the platform HTTP client to the interface used to access the CSSM. |
| Step 4 | license smart transport smart Example: cube(config)#  license smart transport smart Smart transport is the preferred method for sending usage reports. |
| Step 5 | license smart proxy address host-name Example: cube(config)#  license smart proxy address proxy.cisco.com If necessary, configure a proxy-server for the platform when a direct HTTP connection to CSSM is not permitted. |
| Step 6 | license smart proxy port port-number Example: cube(config)# license smart proxy port 80 If using an internet proxy, configure a proxy-server port number. |
| Step 7 | license smart url default Example: cube(config)# license smart url default Use the default URL for sending reports to CSSM. |

| Use the following command to register the CUBE platform with CSSM. license smart trust id_token id_token...local [force] Example: Router# license smart trust id_token ZDEwZDFiODktNWF............. |
|---|

| Step 1 | voice service voip Example: Device(config)# voice service voip Enters global VoIP cofiguration mode. |
|---|---|
| Step 2 | mode border-element [ license periodicity { hours <8-23> \| days <1-30> }] The periodicity keyword configures the CUBE measurement interval for license usage. If you do not configure the periodicity keyword, license usage is measured once every
                                             7 days. |

| Note | The acknowledgment deadline is presented in this output. Ensure that an acknowledgment is received before this time to ensure
                                                continued operation of the SIP service. |
|---|---|

| Note | The Smart Software Manager Satellite (SSMS) On-prem currently does not support the display of the CUBE High Availability (HA)
                                             device pair (Active-Standby) for devices configured with Smart Licensing using Policy (SLP). The functionality of CUBE remains
                                             unaffected. Future updates will incorporate this capability into SSMS. |
|---|---|

| Note | For Smart License using Policy, the CSSM or satellite license usage requests for the active Route Processor. |
|---|---|