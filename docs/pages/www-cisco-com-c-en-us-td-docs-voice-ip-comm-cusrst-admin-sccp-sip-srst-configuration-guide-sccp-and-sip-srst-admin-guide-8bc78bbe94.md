---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cusrst-admin-sccp-sip-srst-configuration-guide-sccp-and-sip-srst-admin-guide-8bc78bbe94
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusrst/admin/sccp_sip_srst/configuration/guide/SCCP_and_SIP_SRST_Admin_Guide/enhanced_srst.html
retrieved_at: 2026-08-21T02:48:58.421571+00:00
---

Cisco Unified SRST Administration Guide (All Versions)

# Cisco Unified SRST Administration Guide (All Versions)

Updated: April 25, 2026

Chapter: Enhanced SRST

## Chapter: Enhanced SRST

# Enhanced SRST

This chapter describes the Unified Enhanced Survivable Remote Site Telephony (Unified E-SRST) feature which is an enhancement
                        of the SRST feature that provides advanced services compared to the classic Unified SRST.

## Migration from Cisco Unified SRST Manager to Unified E-SRST

Cisco Unified Survivable Remote Site Telephony Manager is End-of-Life (EOL). Hence, provisioning for Unified E-SRST through
                           Cisco Unified SRST Manager is not supported for Unified E-SRST Release 12.2 and later releases. Unified E-SRST is provisioned
                           only using CLI commands (manual provisioning) to support fall back of phones registered to Cisco Unified Communications Manager.
                           For more information on configuring Unified E-SRST see SIP: Configure Unified E-SRST and SCCP: Configure Unified E-SRST .

For information on Cisco Unified Survivable Remote Site Telephony Manager End-of-Life announcement, see Cisco Unified Survivable Remote Site Telephony Manager Product Bulletin .

Cisco Unified SRST Manager is a GUI-based tool that helps to monitor, report, and troubleshoot remote sites. It performs automatic
                           sync up between the Cisco Unified Communications Manager and the Unified E-SRST gateway that helps in adding, deleting, and
                           modifying the users and phones including dial-plan mapping. It also provides centralized management and control of all remote
                           sites. For more information on the Cisco Unified SRST Manager that is End-of-Life, see Administration Guide for Cisco Unified SRST Manager .

### Benefits

When you configure Unified E-SRST, it provides the following feature benefits in comparison to the classic Cisco Unified SRST:

Voice Hunt Group

Shared Lines

Mixed Shared Lines (SIP and SCCP Phones)

Hunt Statistics Collection

Mixed Deployment (SIP and SCCP Phones)

Shared Line

BLF

Video

B-ACD

For more information on configuring VHG with Unified E-SRST, see Unified E-SRST with Support for Voice Hunt Group .

For more information on configuring Shared Line, BLF, and Video with Unified E-SRST, see SIP: Configure Unified E-SRST .

### Restrictions

Supports the Version Negotiation feature only on the Cisco Unified 9951, 9971, 8961 SIP IP phones, Cisco IP Phone 7800, and
                                    8800 Series.

The phone firmware version is version 9.4.1 or later versions.

This feature supports video calls only between the local Cisco Unified SIP IP phones and the No Time-Division Multiplexing
                                    (TDM) video calls during the SRST failovers.

To enable phone-specific features like shared-line & BLF work, configure the individual voice register Pools.

#### Restrictions for Unified E-SRST, Release 12.2

The Unified E-SRST deployment with the voice hunt group has the following restrictions:

Does not support the auto logout.

Does not support Programmable Line Keys (PLK).

Does not support HLog Softkey.

The existing support for Cisco Jabber is now End of Life (EOL). Hence, does not support Cisco Jabber on Cisco Unified SRST,
                                             Unified E-SRST.

### Support for Cisco Unified IP Phones and Platforms

The following section provides information about platform support for Cisco Unified IP Phones:

Unified E-SRST support on C8375-E-G2 secure router with Cisco IOS XE 17.18.2 and later releases.

Unified E-SRST is supported on Cisco 1100 Series Integrated Services Router (ISR) Platforms with Cisco IOS XE Bengaluru 17.5.1a
                                    and later releases.

Unified E-SRST is supported on Cisco 4000 Series ISR Platforms (4321, 4331, 4351, 4431, and 4451) on  all Cisco IOS XE releases.

Unified E-SRST is supported on Cisco 4461 Series ISR Platforms with Cisco IOS XE 16.10.1a and later releases.

Unified E-SRST is supported on Cisco Catalyst 8300 Series Edge Platforms with Cisco IOS XE Amsterdam 17.3.2 and later releases.

Unified E-SRST is supported on Cisco Catalyst 8200 Series Edge Platforms with Cisco IOS XE Bengaluru 17.4.1a and later releases.

Unified E-SRST is supported on Cisco Catalyst 8200L Series Edge Platforms with Cisco IOS XE Bengaluru 17.5.1a and later releases.

## Licensing

This section provides information on licensing of Cisco Unified Enhanced Survivable Remote Site Telephony (Unified E-SRST).

### Cisco Smart Licensing for Unified E-SRST

Cisco Smart Licensing is a software licensing model that provides visibility of ownership and usage through the Cisco Smart
                              Software Manager (CSSM) portal. CSSM is a central license repository that manages licenses across all Cisco products that
                              you own, including Unified E-SRST. Devices send license usage to CSSM either directly or use an on-premises satellite. Your
                              Smart Account Administrator controls your access to CSSM. Use your Cisco credentials to access the CSSM portal using http://software.cisco.com .

Smart Licensing applies to all platform technology (DNA subscription) and Unified E-SRST feature licenses that the router
                              uses. Unified E-SRST requires one license entitlement (SRST_E_EP) for each configured SIP or SCCP phone.

Starting from Cisco IOS XE 17.18.1a release, the Cisco Smart Licensing is updated to report with flex subscription entitlement tag (SRST_EP_SUB) across all the
                              supported platforms. To maintain the continued support and entitlements to the future application versions, purchase a collaboration
                              flex subscription.

CSSM shows license usage across all registered devices to a virtual account. A Virtual Account License Inventory displays
                              the quantity of licenses that are purchased, those licenses in use, and a balance. An Insufficient Licenses alert is displayed if the license balance is below 0.

For example, consider a smart account in CSSM with 50 SRST_E_EP licenses. If you have a single registered Unified E-SRST router
                              with 20 configured phones, the CSSM licenses page shows Purchased as 50, In Use as 20 and Balance as 30.

For more information on Smart Software Manager, see the Cisco Smart Software Manager User Guide .

The SRST_E_EP license count reflects the total phone count for both the ephones and voice register Pools that are configured
                                          in the Unified E-SRST irrespective of registered or nonregistered phones. Reports license usage three minutes after the last
                                          configuration change, to avoid unnecessary reporting while configuring Unified E-SRST.

Unified E-SRST Smart Licenses also provide RTU entitlement for routers that are not configured for Smart Licensing.

### Smart License Operation

#### Cisco IOS XE 17.18.1a Release Onwards

Starting from Cisco IOS XE 17.18.1a release, the Cisco Smart Licensing is updated to report with flex subscription entitlement tag ( SRST_EP_SUB ) across all the supported platforms.

To maintain the continued support and entitlements to the future application versions, purchase a collaboration flex subscription.

#### Cisco IOS XE Everest 16.5.1 Release to Cisco IOS XE Fuji 16.9.1 Release

Cisco 4000 Series Integrated Services Routers support Smart Licensing as an alternative to Cisco Software RTU Licensing. Use
                                 the license smart enable command to enable Smart Licensing. To disable Smart Licensing, use the no form of the command and re-accept the EULA using the license accept end user agreement command.

#### Cisco IOS XE Gibraltar 16.10.1 Release Onwards

The Cisco RTU Licensing and the CLI license smart enable command are deprecated. Smart Licensing is mandatory from this release.

#### Cisco IOS XE Everest 16.5.1 Release to Cisco IOS XE Amsterdam 17.3.1a Release

Routers configured to use Smart Licensing offer a 90-day evaluation period, during which you can use all the features without
                                 registering to CSSM. A Unified E-SRST device is associated with CSSM using a registration token. You can obtain the registration
                                 token from the virtual CSSM account or from an on-premises satellite. Once registered, the evaluation period pauses and you
                                 can use the balance later. You cannot renew the evaluation period on its expiry.

Warning

Unified E-SRST shuts down when the router is unregistered and allowed to pass into the Evaluation Expired state.

To register the Unified E-SRST router with CSSM, use license smart register idtoken command. For information on registering the device with CSSM, see Software Activation Configuration Guide .

Upon successful registration, the device sends an authorization request to CSSM for the licenses in use. For each license
                                 type requested, if the Smart Account has sufficient licenses, CSSM responds with Authorized . If the Smart Account does not have sufficient licenses, CSSM responds with Out of Compliance .

Post successful authorization of the request, licenses are bound to the requesting device until the next authorization request
                                 submission. An authorization request is sent every 30 days or when there is any change in license consumption, to maintain
                                 the registration with CSSM. The authorization expires if you do not update the license request for the router within 90 days.
                                 The certificate issued to identify the router at the time of registration is valid for one year and renewed every six months.

```
Router# show license summary Smart Licensing is ENABLED
Registration:
Status: REGISTERED
Smart Account: ABC
Virtual Account: XYZ
Export-Controlled Functionality: Not Allowed
Last Renewal Attempt: None
Next Renewal Attempt: Jun 07 12:08:10 2017 UTC
License Authorization:
Status: AUTHORIZED
Last Communication Attempt: SUCCESS
Next Communication Attempt: Apr 13 07:11:48 2017 UTC
License Usage:
License                   Entitlement tag         Count     Status
-----------------------------------------------------------------------------
ISR_4351_UnifiedCommun.. (ISR_4351_UnifiedCommun..) 1       AUTHORIZED
SRST v12 Endpoint Li...  (SRST_EP)                  4       AUTHORIZED
```

#### Cisco IOS XE Gibraltar 16.12.1 Release to Cisco IOS XE Amsterdam 17.3.1a Release

Cisco 4000 Series Integrated Services Routers supports Specific License Reservation (SLR). SLR allows reservation and utilization
                                 of Cisco Smart Licenses without communicating the license information to CSSM. To reserve specific licenses for a device,
                                 generate the request code from the device. Enter the request code in CSSM along with the required licenses and their quantity,
                                 and generate authorization code. Enter the authorization code on the device to map the license to the Unique Device identifier
                                 (UDI).

#### Cisco IOS XE Amsterdam 17.3.2 and Cisco IOS XE Bengaluru 17.4.1a Release Onwards

This release introduces a new paradigm for tracking license usage across your business. In earlier releases, license authorization
                                 was forward looking, binding licenses to a device until the next authorization request. Actual license usage during the proceeding
                                 reporting period is sent to CSSM, allowing you to plan ongoing license requirements based on historical usage data. Initial
                                 device registration is no longer required to use most platform functionality and deprecates the evaluation period.

Submits the license usage reports periodically according to a minimum reporting policy set for your account. Typically, this
                                 period could be once per year. However, you can generate reports more frequently if the use of licensed features varies over
                                 time. CSSM acknowledges each Resource Utilization Monitoring (RUM) report to ensure reliable recording of the usage. If the
                                 router does not receive an acknowledgment within the minimum reporting period, disables the call processing. Resumes the call
                                 processing on receiving a valid acknowledgment.

Submit the reports directly to the CSSM or through a satellite. Cisco Smart Licensing Utility (CSLU) applications can also
                                 receive usage reports, providing you with more flexibility in managing your license usage. Also, when a device is not able
                                 to communicate directly with a licensing server, a signed usage report can be generated and manually uploaded to CSSM. The
                                 acknowledgment generated by CSSM must be uploaded to the device within the license reporting policy period to ensure continued
                                 use.

As license reporting is now based on historical usage, the registration process used previously has been replaced with a trust
                                 association that also defines the reporting policy set in your account. Establishing trust with CSSM or Cisco Smart Software
                                 Manager Satellite uses an identity token similar to earlier registrations. Use the license smart trust idtoken token command to establish the trust relationship within the initial reporting period set for the device. The CLI license smart register command is deprecated from this release.

Current license usage for Unified E-SRST is displayed using the show license summary command:

```
Router# sh license summary
                License Usage: License         Entitlement tag             Count     Status
        ----------------------------------------------------------------------------
        securityk9     (ISR_4400_Security)            1        IN USE
        AdvUCSuiteK9   (ISR_4400_AdvancedUCSuite)     1        IN USE
        uck9           (ISR_4400_UnifiedCommun...)    1        IN USE
        SRST_E_EP      (SRST_E_EP)                    8        IN USE
        SRST_EP        (SRST_EP)                      592      IN USE
```

## Toll Fraud Prevention for SIP Line Side on Unified E-SRST

Unified E-SRST Release 12.6 enhances the existing Toll Fraud Prevention feature by enforcing security on the SIP line side
                           of Unified E-SRST. The feature enhancement secures the Unified E-SRST system against potential toll fraud exploitation by
                           unauthorized users from the SIP line side.

The configuration and characteristics of toll fraud prevention offered on the SIP line side of Unified E-SRST is same as the
                           support available on Cisco Unified SRST. For more information on the feature, see Toll Fraud Prevention for SIP Line Side on Cisco Unified SRST .

## Unified E-SRST with Support for Voice Hunt Group

The Unified E-SRST Release 12.2 supports the Voice Hunt Group with Cisco Unified Enhanced Survivable Remote Site Telephony
                           (Unified E-SRST). The deployment supports the SIP and SCCP phones. The Cisco IP Phone 7800 and 8800 Series are the supported
                           SIP phones for this deployment. The Unified E-SRST deployment introduces the voice hunt group enhancement on the Cisco 4000
                           Series Integrated Services Routers.

As part of the enhancement, supports the voice hunt group features in the E-SRST mode. The Unified E-SRST 12.2 and later releases
                           supports the voice hunt group deployments with Sequential, Parallel, Longest idle, and Peer call blasting.

During a WAN outage, the SIP phones on the Cisco Unified Communications Manager (Cisco Unified Communications Manager) fallback
                           to Unified E-SRST router in mode esrst . By default, logs the SIP phones in to the hunt group. However, if the CLI command members logout is configured under the voice hunt group configuration mode, the phones are in logged out state. In the Unified E-SRST mode,
                           the phone that falls back on Unified E-SRST can toggle state. It can also log in (or log out) to the voice hunt group using
                           HLog in Feature Access Code (FAC). Displays the DN status (logged in or logged out) on the registered phones with Unified
                           E-SRST. The following FAC codes are available as part of the enhancement introduced on Unified E-SRST:

FAC Standard (Code: *5)

FAC Custom (Code: Customizable, with  maximum character string length of 10. For example, *89, 8888888888)

When the user inputs FAC from a phone with multiple lines, the log out behavior is different across a deployment with the
                           common voice register Pool configuration and the individual voice register Pool configuration.

Common Voice Register Pool Configuration: The DN's log out individually, and not at the phone level.

Individual Voice Register Pool Configuration: The DN's log out at the phone level, irrespective of the user providing the
                                 DN (primary, secondary, and so on) from which FAC input.

When the WAN is available, the phones register back with Cisco Unified Communications Manager. For a sample configuration
                           of Unified E-SRST with voice hunt group enhancements, see Example for configuring Unified E- SRST with Voice Hunt Group Enhancements .

The Unified E-SRST 12.2 Release introduces support for the voice hunt group with shared lines and mixed shared lines (SCCP
                           and SIP phones). For a mixed shared line supported with the voice hunt group, configure only individual voice register Pools.
                           Does not support the common voice register Pools. For a sample configuration of mixed shared lines configured for a voice
                           hunt group on Unified E-SRST, see Example for Configuring Shared Line with Voice Hunt Group on Unified E-SRST .

Also, supports hunt statistic collection for Unified E-SRST 12.2 and later releases.

A mixed deployment of SIP and SCCP phones supports the Unified E-SRST, Release 12.2. Supports Hunt Group Logout from a mixed
                           deployment of SIP and SCCP phones using:

FAC

Feature Button, or DND

Supports Line level logout and phone level log out using FAC (*4).

Does not support Hunt Group logout for shared lines. Shared lines retain their logged in status.

### Support for B-ACD in Unified E-SRST

The Unified E-SRST Release 12.2 enhancement supports B-ACD. For SIP phones that fall back to Unified E-SRST router in mode esrst , you must ensure that the CLI command members logout is configured. The Members Logout functionality handles the login back from the phones using FAC. It also supports call Delivery
                              to Voice Hunt Group from B-ACD.

For a sample configuration, see Example for Configuring B-ACD with Unified E-SRST .

### Recommendations for Configuring Voice Hunt Group on Unified E-SRST

The Unified E-SRST Release with Support for voice hunt group has the following design characteristics:

For all the directory numbers falling back from Cisco Unified Communications Manager, a common voice register Pool configuration
                                    and an individual voice register Pool configuration is supported for this deployment. An individual voice register pool configured with the CLI command id device-id-name , along with voice register dn configuration, is recommended.

Ensure that the CLI command mode esrst is configured under voice register global configuration mode for phones to fall back to Unified E-SRST.

Ensure that the CLI command id ip or id device-id-name is configured under voice register pool configuration mode, along with voice register dn configuration, for a deployment with individual voice register Pool configuration. For a sample configuration, see Example for configuring Unified E- SRST with Voice Hunt Group Enhancements .

Ensure that the CLI command id device-id-name is preferred over id ip as the CLI command to configure under voice register pool configuration mode. This scenario occurs where the IP address of the phone changes due to the DHCP configured on the phone.

Ensure that the CLI command id network is configured under voice register pool configuration mode for a deployment with common voice register Pool configuration. The recommended configuration is id network 8.55.0.0 255.255.0.0 so as to facilitate registration of phones falling back on Unified E-SRST from Cisco Unified Communications Manager.

Ensure that the CLI command members logout is configured under voice hunt-group configuration mode. The CLI is applied by default when the SIP phones fall back to Unified E-SRST from Cisco Unified Communications
                                    Manager.

Ensure that the CLI command fac standard is configured under telephony-service configuration mode. If you want to configure a FAC code other than *5, you must configure the CLI command fac custom under telephony-service configuration mode.

Ensure that the CLI commands call-park system application and hunt-group logout hlog are configured under telephony-service configuration mode. The CLI commands are mandatory configuration for FAC functionality to work.

For steps on configuring voice hunt groups on Unified E-SRST, see Configure Voice Hunt Groups on Unified E-SRST .

For a sample configuration of voice hunt groups on Unified E-SRST, see Example for configuring Unified E- SRST with Voice Hunt Group Enhancements .

## SIP: Configure Unified E-SRST

The Enhanced SRST for Cisco Unified SIP IP Phones feature supports version negotiation between the SIP phones and ESRST to
                           enable more features in the Cisco Unified E-SRST mode. In the current scenario, when the SIP phones fall back to the SRST
                           mode, disables features such as Shared-Line, Busy-Lamp-Field (BLF), and Video call on the phones. The SRST mode does not support
                           these features. However, with the Enhanced Survivable Remote Site Telephony (E-SRST) deployment, you can enable the basic
                           and supplementary call features. Also, you can enable the following features using version negotiation:

Shared-Line

Busy-Lamp-Field (BLF)

Video Calls

The following table contains a list of supported features and the expected behavior of the features in the E-SRST mode.

Feature

Supported Features

Expected Behavior in the E-SRST Mode

Shared-Line

cBarge

Not Supported (After the failover, the phone does not retain the key.)

Privacy-on-hold

Supported

Transfer

Supported

Conference

Supported

BLF

BLF DN monitoring

Supported

BLF device-based monitoring

Not supported (Not supported in RT phones)

BLF call-list monitoring

Supported

Monitoring of a Call-park slot

Not supported

Monitoring of Paging DN

Not supported

Monitoring of Conference DN

Not supported

To enable version negotiation feature between ESRST & phone, you must configure "mode esrst" under the voice register global
                                 mode.

We recommended using the SRST manager to automate the CLI provisioning of ESRST branch routers.

For more information on SRST, see the Cisco Unified SRST Manager Administration Guide .

### Restrictions

Supports the Version Negotiation feature only on the Cisco Unified 9951, 9971, 8961 SIP IP phones, Cisco IP Phone 7800, and
                                    8800 Series.

The phone firmware version is version 9.4.1 or later versions.

This feature supports video calls only between the local Cisco Unified SIP IP phones and the No Time-Division Multiplexing
                                    (TDM) video calls during the SRST failovers.

To enable phone-specific features like shared-line & BLF work, configure the individual voice register Pools.

### Enable the E-SRST Mode

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- mode esrst

- exit

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

voice register global

#### Example:

```
Router(config)# voice register global
```

Enters the voice register global configuration mode to set the parameters for all the supported SIP phones in Cisco Unified
                                             Communications Manager Express.

Step 4

mode esrst

#### Example:

```
Router(config-register-global)# mode esrst
```

Configures the E-SRST mode under the voice register global mode.

Step 5

exit

#### Example:

```
Router(config-register-global)# exit
```

Exits the voice register-global configuration mode.

### Configure SIP shared-line

To configure SIP shared-line, perform the following procedure:

### SUMMARY STEPS

- enable

- configure terminal

- voice register dn dn-tag

- shared-line [ max-calls number-of-calls ]

- huntstop channel number-of-channels

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

voice register dn dn-tag

Step 4

shared-line [ max-calls number-of-calls ]

Step 5

huntstop channel number-of-channels

Step 6

end

Returns to privileged EXEC mode.

### Configure BLF

#### Before you begin

### SUMMARY STEPS

- enable

- configure terminal

- sip-ua

- presence enable

- exit

- max-subscription number

- presence call-list

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

sip-ua

Step 4

presence enable

Step 5

exit

Step 6

max-subscription number

Step 7

presence call-list

Step 8

end

### Enable a SIP Directory Number to Be Watched

To enable a directory number to be watched, perform the following procedure:

### SUMMARY STEPS

- enable

- configure terminal

- voice register dn dn-tag

- number number

- allow watch

- end

### DETAILED STEPS

Step 1

enable

Step 2

configure terminal

Step 3

voice register dn dn-tag

Step 4

number number

Step 5

allow watch

Step 6

end

### Enable BLF on a Voice Register Pool

To enable BLF on a voice register pool , perform the following steps:

For configuration information, see the Cisco Unified Communications Manager Administration Guide .

### SUMMARY STEPS

- enable

- configure terminal

- voice register pool pool-tag

- number tag dn dn-tag ]

- blf-speed-dial tag number label string [device]

- presence call-list (To enable Presence feature for all the missed/received/placed calls)

- end

### DETAILED STEPS

Step 1

enable

Step 2

configure terminal

Step 3

voice register pool pool-tag

Step 4

number tag dn dn-tag ]

Step 5

blf-speed-dial tag number label string [device]

Step 6

presence call-list (To enable Presence feature for all the missed/received/placed calls)

Step 7

end

#### Example: ESRST Mode

The following example shows how to enable the E-SRST mode:

```
Router# configure terminal
Router(config)# voice register global
Router(config-register-global)# mode esrst
```

#### Example: Configuring Shared Line

The following example shows how to configure shared-line:

```
Router(config)#voice register dn 1
Router (config-register-dn)#number 1111
Router (config-register-dn)#shared-line max-calls 7
```

```
Router(config)#voice register pool 1
Router(config-register-pool)#Id mac 002D.264E.54FA
Router(config-register-pool)#type 9971
Router(config-register-pool)#number 1 dn 1
```

```
Router(config)#voice register pool 2
Router(config-register-pool)#id mac 000D.39F9.3A58
Router(config-register-pool)#type 7965
Router(config-register-pool)#number 1 dn 1
```

#### Example: Configuring BLF

The following example shows how to configure BLF:

```
Router(config)#voice register dn  1 Router (config-register-dn)#number 1111 Router (config-register-dn)#allow watch Router(config)#voice register dn  1 Router (config-register-dn)#number 2222 Router(config)#voice register pool 1 Router(config-register-pool)#id mac 0015.6247.EF90 Router(config-register-pool)#type 7971 Router(config-register-pool)#number 1 dn 1 Router(config)#voice register pool 2 Router(config-register-pool)#id mac 0012.0007.8D82 Router(config-register-pool)#type 7912 Router(config-register-pool)#number 1 dn 2 Router(config-register-pool)#blf-speed-dial 1 1111 label "1111"
```

If the phone and the Unified E-SRST router are in different subnets and you are using id mac in the voice register pool configuration mode. Configure the digest credentials on Cisco Unified Communications Manager, and username password configuration
                                                under voice register pool on Unified E-SRST. Digest Configuration is not required with the id device-id-name CLI command in Cisco Unified SRST Release 12.2.

### Configure Unified E-SRST

The mode esrst under telephony-service and voice register global configuration mode supports SCCP and SIP phones respectively to enable the enhanced services in Unified E-SRST mode. While
                                 Cisco Unified SRST supports only the basic voice hunt group features, Unified E-SRST supports the advanced voice hunt group
                                 features such as HLog, shared lines, and B-ACD. To configure the basic Unified E-SRST, perform the following procedure:

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- mode esrst

- max-ephones max-phones

- max-dn max-directory-numbers

- ip source-address ip-address [ port port ] [ any-match | strict-match ]

- call-park system {application |redirect}

- hunt-group logout {DND | HLog}

- transfer-system full-consult

- transfer-pattern transfer-pattern

- fac { standard | custom { alias alias-tag | feature } }

- create cnf-files

- exit

- voice register global

- mode esrst

- max-dn max-directory-numbers

- max-pool max-phones

- exit

- voice register dn dn-tag

- number number

- exit

- voice register pool pool-tag

- id [{ network address mask mask | ip address mask mask | mac address }] [ device-id-name devicename ]

- dtmf-relay rtp-nte

- exit

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters telephony-service configuration mode.

Step 4

mode esrst

#### Example:

```
Router(config)# telephony-service
```

Configures the E-SRST mode under the telephony-service configuration mode.

Step 5

max-ephones max-phones

#### Example:

```
Router(config-telephony)# max-ephones 40
```

Configures the maximum supported IP phones by the router. The default is 0.

The maximum number is platform-dependent.

Step 6

max-dn max-directory-numbers

#### Example:

```
Router(config-telephony)# max-dn 15
```

Sets the maximum supported directory numbers (DNs) by the router.

Max-directory-numbers: Maximum supported directory numbers (DNS) or virtual voice ports by the router. The maximum number
                                                   is platform-dependent. The default is 0.

Step 7

ip source-address ip-address [ port port ] [ any-match | strict-match ]

#### Example:

```
Router(config-telephony)# ip source-address 8.39.23.24 port 2000
```

Enables the router to receive messages from the Cisco IP phones through the specified IP addresses and supports strict IP
                                             address verification. The default port number is 2000.

Step 8

call-park system {application |redirect}

#### Example:

```
Router(config-telephony)# call-park system application
```

Defines system parameters for the Call Park feature.

application : Enables the Call Park features supported in Cisco Unified SRST.

Step 9

hunt-group logout {DND | HLog}

#### Example:

```
Router(config-telephony)# hunt-group logout HLog
```

Sets the hunt-group logout options with Hlog in telephony-service configuration mode.

Step 10

transfer-system full-consult

#### Example:

```
Router(config-telephony)# transfer-system full-consult
```

Specifies the Call Transfer method.

full-consult —Calls are transferred with consultation using H.450.2 standard methods and a second phone line if available. Calls fall back
                                                   to full-blind if the second line is unavailable.

Step 11

transfer-pattern transfer-pattern

#### Example:

```
Router(config-telephony)# transfer-pattern .T
```

Allows transfer of the phone calls by Cisco Unified IP phones to specified phone number patterns. If you have set no transfer
                                             pattern, defaults to other local IP phones.

transfer-pattern —A string of digits for permitted Call Transfers.

Step 12

fac { standard | custom { alias alias-tag | feature } }

#### Example:

```
Router(config-telephony)# fac standard
```

Enables all standard feature access codes (FACs) or creates and enables individual custom FACs in telephony-service configuration
                                             mode.

Step 13

create cnf-files

#### Example:

```
Router(config-telephony)# create cnf-files version-stamp
```

Builds the required XML configuration files for IP phones in the telephony-service configuration mode.

Step 14

exit

#### Example:

```
Router(config-telephony)# exit
```

Exits the telephony-service configuration mode

Step 15

voice register global

#### Example:

```
Router(config)# voice register global
```

Enter the voice register global configuration mode.

Step 16

mode esrst

#### Example:

```
Router(config-register-global)# mode esrst
```

Configures the E-SRST mode under the voice register global mode.

Step 17

max-dn max-directory-numbers

#### Example:

```
Router(config-register-global)# max-dn 40
```

Set the maximum supported SIP phone directory numbers (extensions) by a Cisco router in the voice register global configuration
                                             mode.

Step 18

max-pool max-phones

#### Example:

```
Router(config-register-global)# max-pool 40
```

Sets maximum supported SIP phones by the Cisco Unified SRST router.

Version- and platform-dependent; type? For range.

Step 19

exit

#### Example:

```
Router(config-register-global)# exit
```

Exits the voice register global configuration mode.

Step 20

voice register dn dn-tag

#### Example:

```
Router(config)# voice register dn 17
```

Enter the voice register directory number configuration mode to define a directory number for a SIP phone.

Use the same directory number (DN) configured in Cisco Unified Communications Manager to configure the voice register directory
                                             number in Unified E-SRST.

Step 21

number number

#### Example:

```
Router(config-register-dn)# number 7001
```

Defines a valid number for a directory number.

Step 22

exit

#### Example:

```
Router(config-register-dn)# exit
```

Exits the voice register directory number configuration mode.

Step 23

voice register pool pool-tag

#### Example:

```
Router(config)# voice register pool 1
```

Enters the voice register Pool configuration mode to set phone-specific parameters for a SIP phone.

Step 24

id [{ network address mask mask | ip address mask mask | mac address }] [ device-id-name devicename ]

#### Example:

```
Router(config-register-pool)# id network 8.55.0.0 mask 255.255.0.0
```

Explicitly identifies a locally available individual or set of SIP IP phones. The keywords and arguments are defined as follows:

network address mask mask : The network address mask mask keyword/argument combination is used to accept SIP Register messages for the indicated phone numbers from any IP phone within
                                                   the indicated IP subnet.

ip address mask mask : The ip address mask mask keyword/argument combination is used to identify an individual phone.

mac address : MAC address of a particular Cisco Unified IP Phone.

device-id-name devicename : Defines the device name to be used to download the phone’s configuration file.

Step 25

dtmf-relay rtp-nte

#### Example:

```
Router(config-register-pool)# dtmf-relay rtp-nte
```

Forwards DTMF tones by using Real-Time Transport Protocol (RTP) with the Named phone Event (NTE) payload type and enables
                                             the DTMF relay using the RFC 2833 standard method.

Step 26

exit

#### Example:

```
Router(config-register-pool)# exit
```

Exits the voice register Pool configuration mode.

### Configure Voice Hunt Groups on Unified E-SRST

### SUMMARY STEPS

- enable

- configure terminal

- voice hunt-group hunt-tag {longest-idle | parallel | peer | sequential}

- members logout

- list number [, number...]

- timeout seconds

- statistics collect

- exit

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

voice hunt-group hunt-tag {longest-idle | parallel | peer | sequential}

#### Example:

```
Router(config)# voice hunt-group 1 sequential
```

Enters voice hunt-group configuration mode to define a hunt group.

Hunt-tag—Unique sequence number for configuring the hunt group. Range is 1–100.

Longest idle—Hunt group in which calls go to the directory number that has been idle for the longest time.

Sequential—Hunt group in which directory numbers ring in the order in which they are listed, left to right.

Parallel—Hunt group in which all directory numbers ring simultaneously.

Peer—Hunt group in which the call placed to a directory number rings for the next directory number in line.

Step 4

members logout

#### Example:

```
Router(config-voice-hunt-group)# members logout
```

(optional) Configures a Cisco Unified SRST system for all non-shared static members or agents in a voice hunt group with the
                                             Hlogout initial state.

Step 5

list number [, number...]

#### Example:

```
Router(config-voice-hunt-group)# list 1812, 1813, 1814
```

Defines a list of extensions that are members of a voice hunt group.

Step 6

timeout seconds

#### Example:

```
Router(config-voice-hunt-group)# timeout 30
```

Defines the number of seconds after which directs the unanswered calls to the next number in a voice hunt-group list.

Step 7

statistics collect

#### Example:

```
Router(config-voice-hunt-group)# statistics collect
```

Enables the collection of call statistics for a voice hunt group.

Step 8

exit

#### Example:

```
Router(config-voice-hunt-group)# exit
```

Exits the voice hunt group configuration mode.

### Example for Configuring Unified E-SRST with Voice Hunt Group Enhancements

The following is a sample configuration for Unified E-SRST Release 12.2 under telephony-service , voice register global , voice register pool , and voice hunt-group configuration modes, for a deployment with common voice register Pool configuration.

```
Router#
telephony-service
call-park system application
hunt-group logout HLog
transfer-system full-consult
fac standard
```

```
Router#sh run | sec global
voice register global
mode esrst
max-dn 40
max-pool 40
```

```
Router#
voice register pool 1
id network 8.55.0.0 mask 255.255.0.0
dtmf-relay rtp-nte
Router#
telephony-service
max-ephones 40
max-dn 50
ip source-address 8.39.23.24 port 2000
call-park system application
transfer-system full-consult
transfer-pattern .T
fac standard
create cnf-files version-stamp Jan 01 2002 00:00:00
```

```
Router#sh run | sec hunt
voice hunt-group 1 sequential
members logout
list 1812,1813,1814
timeout 30
statistics collect
pilot 1111
```

The following is a sample configuration for Unified E-SRST Release 12.2, for a deployment with individual voice register Pool
                              configuration, with the CLI command id ip configured.

```
voice register dn 2
number 4000
!
voice register dn 3
number 4002
!
voice register pool 2
busy-trigger-per-button 2
id ip 8.55.0.241 mask 255.255.0.0
type 8811
number 1 dn 2
dtmf-relay rtp-nte
codec g711ulaw
!
voice register pool 3
busy-trigger-per-button 2
id ip 8.55.0.242 mask 255.255.0.0
type 7861
number 1 dn 3
dtmf-relay rtp-nte
codec g711ulaw
```

The following is a sample configuration for Unified E-SRST Release 12.2, for a deployment with individual voice register Pool
                              configuration, with the CLI command id device-id-name configured.

```
voice register dn 2
number 4000
!
voice register dn 3
number 4002
!
voice register pool 2
busy-trigger-per-button 2
id device-id-name SEP00EBD5CD77ED
type 8811
number 1 dn 2
dtmf-relay rtp-nte
codec g711u;aw
voice register pool 3
busy-trigger-per-button 2
id device-id-name SEP0076861A7EDC
type 7861
number 1 dn 3
dtmf-relay rtp-nte
codec g71ulaw
```

### Example for Configuring B-ACD with Unified E-SRST

The following is a sample configuration for B-ACD functionality supported with Unified E-SRST:

```
application
service aa-bcd bootflash:/app-b-acd-aa-3.0.0.4_thd_v4.tcl
paramspace english index 0
param second-greeting-time 60
param welcome-prompt _bacd_welcome.au
param call-retry-timer 8
param voice-mail 1811
paramspace english language en
param max-time-call-retry 16param service-name callq
param number-of-hunt-grps 2
param handoff-string aa-bcd
paramspace english location flash:
param max-time-vm-retry 2
param aa-pilot 1117
!
service clid_col_npw_npw
param uid-length 4
!
service aa-ccd bootflash:/app-b-acd-aa-3.0.0.4_thd_v4.tcl
paramspace english index 0
param drop-through-prompt _bacd_welcome.au
param second-greeting-time 60
paramspace english language en
param call-retry-timer 8
param voice-mail 1811
param max-time-call-retry 16
param service-name callq
param number-of-hunt-grps 1
param drop-through-option 1
paramspace english location flash:
param handoff-string aa-ccd
param max-time-vm-retry 2
param aa-pilot 1118
!
service callq bootflash:/imanage-b-acd-3.0.0.4_Q60.tcl
param queue-len 1
param aa-hunt1 1111
param number-of-hunt-grps 4
param queue-manager-debugs 1
!
call-park system application
```

### Example for Configuring Shared Line with Voice Hunt Group on Unified E-SRST

The following is a sample configuration of Unified E-SRST, Release 12.2 with support for mixed shared lines (SIP and SCCP
                              Phones) in a voice hunt group deployment.

```
Router# sh run | sec global
voice register global
mode esrst
no allow-hash-in-dn
max-dn 40
max-pool 40
Router# sh run | sec pool
max-pool 40
voice register pool 1
busy-trigger-per-button 2
id device-id-name SEP00CCFC4AA4DC
type 8811
number 1 dn 1
number 2 dn 21
dtmf-relay rtp-nte
username xxxx password uvwx
codec g711ulaw
no vad
voice register pool 2
busy-trigger-per-button 2
id device-id-name SEP00CCFC177A4E
type 8841
number 1 dn 2
dtmf-relay rtp-nte
username xxxx password uvwx
codec g711ulaw
no vad
voice register pool 3
busy-trigger-per-button 2
id device-id-name SEP0076861ADEF0
type 7841
number 1 dn 3
number 2 dn 22
dtmf-relay rtp-nte
username xxxx password uvwx
codec g711ulaw
no vad
voice register pool 4
busy-trigger-per-button 2
id device-id-name SEP00EBD5CD270C
type 8811
number 1 dn 4
number 2 dn 22
dtmf-relay rtp-nte
username xxxx password uvwx
codec g711ulaw
no vad
voice register pool 5
busy-trigger-per-button 2
id device-id-name SEP94D4692A2553
type 8841
number 1 dn 5
dtmf-relay rtp-nte
username xxxx password uvwx
codec g711ulaw
no vad
voice register pool 6
busy-trigger-per-button 2
id device-id-name SEP00CAE540C4B5
type 8811
number 1 dn 6
number 2 dn 21
dtmf-relay rtp-nte
username xxxx password uvwx
codec g711ulaw
no vad
alias exec pool show voice register pool all br
```

```
Router# sh run | sec dn
no allow-hash-in-dn
max-dn 40
voice register dn 1
voice-hunt-groups login
number 1811
voice register dn 2
voice-hunt-groups login
number 1812
voice register dn 3
voice-hunt-groups login
number 1813
voice register dn 4
voice-hunt-groups login
number 1814
voice register dn 5
voice-hunt-groups login
number 1815
voice register dn 6
voice-hunt-groups login
number 1816
voice register dn 21
voice-hunt-groups login
number 1821
shared-line
voice register dn 22
voice-hunt-groups login
number 1822
shared-line
```

```
Router# sh run | sec ephone
max-ephones 40
ephone-dn 11
number 1911
ephone-dn 12
number 1912
ephone-dn 13
number 1913
ephone-dn 14
number 1914
ephone-dn 21
number 1921
ephone-dn 22
number 1822
shared-line sip
ephone 11
device-security-mode none
mac-address 1111.1111.1911
feature-button 1 HLog
type 7970
button 1:11
ephone 12
device-security-mode none
mac-address 1111.1111.1912
feature-button 1 HLog
type 7970
button 1:12 2:21
ephone 13
device-security-mode none
mac-address 1111.1111.1913
feature-button 1 HLog
type 7970
button 1:13 2:21
ephone 14
device-security-mode none
mac-address 1111.1111.1914
feature-button 1 HLog
type 7970
button 1:14 2:22
alias ephone show ephone summary brief
alias exec ephone show ephone summary brief
```

```
Router# sh run | sec tele
telephony-service
conference transfer-pattern
mode esrst
max-ephones 40
max-dn 50
ip source-address 8.39.23.24 port 2000
service phone sshAccess 0
service phone webAccess 0
max-conferences 8 gain -6
call-park system application
hunt-group logout HLog
transfer-system full-consult
fac standard
```

## SCCP: Configure Unified E-SRST

### Before you begin

Cisco Unified Communications Manager Express 10.5 or later version

Configure the telephony-services command.

For SCCP phones, CME-as-SRST mode is provisioned using the SRST mode autoprovision command. From 10.5 release onwards, deprecates
                                          this command. When you try to configure CME-as-SRST mode, displays the following message: “Note: This configuration is being deprecated. Please configure "mode esrst" to use the enhanced SRST mode.”

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- mode esrst

- max-ephones max-phones

- max-dn max-directory-numbers [preference preference-order] [no-reg primary | both]

- ip source-address ip-address [port port] [any-match | strict-match]

- exit

- ephone-dn dn-tag [dual-line]

- number number [secondary number] [no-reg [both |primary]]

- (Optional) name name

- exit

- ephone phone-tag

- mac-address [mac-address]

- type phone-type [addon 1 module-type [2 module-type]]

- button button-number{separator}dn-tag [,dn-tag...][button-number{x}overlay-button-number] [button-number...]

- end

### DETAILED STEPS

Step 1

enable

### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

telephony-service

### Example:

```
Router(config)# telephony-service
```

Enters telephony-service configuration mode.

Step 4

mode esrst

### Example:

```
Router(config-telephony)# mode esrst
```

Enters telephony-service configuration mode.

Step 5

max-ephones max-phones

### Example:

```
Router(config-telephony)# max-ephones 24
```

Enters telephony-service configuration mode.

Step 6

max-dn max-directory-numbers [preference preference-order] [no-reg primary | both]

### Example:

```
Router(config-telephony)# max-dn 24 no-reg primary
```

Limits the number of directory numbers supported by this router.

Maximum number is the platform and version-specific. Type? For value.

Step 7

ip source-address ip-address [port port] [any-match | strict-match]

### Example:

```
Router(config-telephony)# ip source-address 192.168.11.1 port 2000
```

Identifies the IP address and port number that the Cisco Unified SRST router uses for IP phone registration.

port port—(Optional) TCP/IP port number to use for SCCP. Range is 2000–9999. Default is 2000.

Any-match—(Optional) Disables the strict IP address checking for registration. It is the default setting.

Strict-match—(Optional) Instructs the router to reject IP phone registration attempts if the IP server address used by the
                                                phone does not exactly match the source address.

Step 8

exit

### Example:

```
Router(config-telephony)# exit
```

Exits telephony-service configuration mode.

Step 9

ephone-dn dn-tag [dual-line]

### Example:

```
Router(config)# ephone-dn 1
```

Enters ephone dn configuration mode to define a directory number for an IP phone, intercom line, voice port, or a message-waiting
                                          indicator (MWI).

Dn-tag—Identifies a particular directory number during configuration tasks. Range is 1 to the maximum number of directory
                                                numbers allowed on the router platform. Type? To display  range.

Step 10

number number [secondary number] [no-reg [both |primary]]

### Example:

```
Router(config-ephone-dn)# number 1001
```

Associates an extension number with this directory number.

Number—String of up to 16 digits that represents an extension or E.164 phone number.

Step 11

(Optional) name name

### Example:

```
Router(config-ephone-dn)# name Smith, John
```

Associates a name with this directory number.

Uses the Name for caller-ID displays and in the local directory listings.

Follows the name order in the directory command.

Step 12

exit

### Example:

```
Router(config-telephony)# end
```

Exits ephone-dn configuration mode.

Step 13

ephone phone-tag

### Example:

```
Router(config)# ephone 1
```

Enters ephone configuration mode to set ephone specific parameters.

Phone-tag—Unique sequence number that identifies the phone. Range is version and platform-dependent; type? To display range.

Step 14

mac-address [mac-address]

### Example:

```
Router(config-ephone)# mac-address 0022.555e.00f1
```

Associates the MAC address of a Cisco IP phone with an ephone configuration in a Unified E-SRST system.

Mac-address—Identifying MAC address of an IP phone found on a sticker on the bottom of the phone.

Step 15

type phone-type [addon 1 module-type [2 module-type]]

### Example:

```
Router(config-ephone)# type 7960
```

Specifies the type of phone.

Step 16

button button-number{separator}dn-tag [,dn-tag...][button-number{x}overlay-button-number] [button-number...]

### Example:

```
Router(config-ephone)# button 1:7
```

Associates a button number and line characteristics with an ephone-dn. Determines the maximum number of buttons by phone type.

Step 17

end

### Example:

```
Router(config-telephony)# end
```

Returns to privileged EXEC mode.

### Example

The following example shows the status of the device in E-SRST mode:

```
show telephony-service
CONFIG (Version=10.5)
=====================
Version 10.5
Max phoneload sccp version 17
Max dspfarm sccp version 18 Cisco Unified Enhanced SRST
```

For SCCP phones, switching the mode from CME to ESRST and vice versa, results in wiping out the entire CME or ESRST configurations
                                          (including ephone, DNs, templates etc.).

### Configure Mixed Shared Lines with SCCP Phones

To configure mixed shared lines between SCCP and SIP IP Phones on Unified E-SRST, perform the following procedure:

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag [dual-line]

- number [ secondary [number] [ no-reg [ both | primary ]]

- shared-line sip

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

ephone-dn dn-tag [dual-line]

#### Example:

```
Router(config)# ephone-dn 1
```

Enters ephone dn configuration mode to define a directory number for an IP phone, intercom line, voice port, or a message-waiting
                                             indicator (MWI).

Dn-tag—Identifies a particular directory number during configuration task. Range is 1 to the maximum number of directory numbers
                                                   allowed on the router platform. Type? To display the range.

Step 4

number [ secondary [number] [ no-reg [ both | primary ]]

#### Example:

```
Router(config-ephone-dn)# number 1001
```

Associates an extension number with this directory number.

number—String of up to 16 digits that represents an extension or E.164 phone number.

Step 5

shared-line sip

#### Example:

```
Router(config-ephone-dn)# shared-line sip
```

Adds an ephone-dn as a member of a shared directory number for a mixed shared line between Unified SIP and Unified SCCP IP
                                             phones.

Step 6

end

#### Example:

```
Router(config-ephone-dn)# end
```

Returns to privileged EXEC mode.

### Configure BLF for SCCP Phones

#### Before you begin

### SUMMARY STEPS

- enable

- configure terminal

- presence

- max-subscription number

- presence call-list

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

presence

Step 4

max-subscription number

Step 5

presence call-list

(To enable Presence feature for all the missed or received or placed calls)

Step 6

end

### Enable an SCCP Directory Number to Be Watched

To enable a directory number to be watched, perform the following procedure:

### SUMMARY STEPS

- ephone-dn dn-tag

- number number

- allow watch

- end

### DETAILED STEPS

Step 1

ephone-dn dn-tag

Step 2

number number

Step 3

allow watch

Step 4

end

### Enable BLF on an Ephone

To enable BLF on an ephone , perform the following steps:

### SUMMARY STEPS

- enable

- configure terminal

- ephone ephone-tag

- button button-number {separator}dn-tag [,dn-tag...] [button-number{x}overlay-button-number][button-number...]

- blf-speed-dial tag number label string [device]

- presence call-list (To enable Presence feature for all the missed/received/placed calls)

- end

### DETAILED STEPS

Step 1

enable

Step 2

configure terminal

Step 3

ephone ephone-tag

Step 4

button button-number {separator}dn-tag [,dn-tag...] [button-number{x}overlay-button-number][button-number...]

Step 5

blf-speed-dial tag number label string [device]

Step 6

presence call-list (To enable Presence feature for all the missed/received/placed calls)

Step 7

end

## Configure Digest Credentials on Cisco Unified Communications Manager

To configure the username and password with Digest Authentication on Cisco Unified Communications Manager, perform the following
                              steps:

### SUMMARY STEPS

- Log in to Cisco Unified Communications Manager.

- Go to System > Security -> Phone Security Profile.

- Go to User Management > End User.

- Go to the Phone Settings page and associate the user in the Digest User field.

### DETAILED STEPS

Step 1

Log in to Cisco Unified Communications Manager.

Step 2

Go to System > Security -> Phone Security Profile.

Step 3

Go to User Management > End User.

Step 4

Go to the Phone Settings page and associate the user in the Digest User field.

### Configure Digest Credentials on Unified E-SRST for SIP

To configure credentials under a specific voice register pool, perform the following procedure:

Digest authentication does not work with 'id network' configuration in 'voice register pool'. It requires 'id device-id-name'
                                             or 'id Mac' configuration for individual pools. Also DN association on 'voice register pool' is required.

### SUMMARY STEPS

- enable

- configure terminal

- voice register pool <pool-tag>

- username <username> password <password>

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

voice register pool <pool-tag>

Step 4

username <username> password <password>

Step 5

end

#### Example: Configuring Digest Credentials on ESRST

The following example shows how to configure digest credentials on ESRST:

```
Router# conf terminal
Router(config)#voice register pool 10
Router (config-register-pool)# username abc password xyz
```

### Configure Digest Credentials on Unified E-SRST for SCCP

To configure credentials under a specific ephone, perform the following procedure:

### SUMMARY STEPS

- enable

- configure terminal

- ephone ephone tag

- username <username> password <password>

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

ephone ephone tag

Step 4

username <username> password <password>

Step 5

end

| Note | The existing support for Cisco Jabber is now End of Life (EOL). Hence, does not support Cisco Jabber on Cisco Unified SRST,
                                             Unified E-SRST. |
|---|---|

| Note | The SRST_E_EP license count reflects the total phone count for both the ephones and voice register Pools that are configured
                                          in the Unified E-SRST irrespective of registered or nonregistered phones. Reports license usage three minutes after the last
                                          configuration change, to avoid unnecessary reporting while configuring Unified E-SRST. |
|---|---|

| Note | Unified E-SRST Smart Licenses also provide RTU entitlement for routers that are not configured for Smart Licensing. |
|---|---|

| Warning | Unified E-SRST shuts down when the router is unregistered and allowed to pass into the Evaluation Expired state. |
|---|---|

| Note | Does not support Hunt Group logout for shared lines. Shared lines retain their logged in status. |
|---|---|

| Feature | Supported Features | Expected Behavior in the E-SRST Mode |
|---|---|---|
| Shared-Line | cBarge | Not Supported (After the failover, the phone does not retain the key.) |
| Privacy-on-hold | Supported |
| Transfer | Supported |
| Conference | Supported |
| BLF | BLF DN monitoring | Supported |
| BLF device-based monitoring | Not supported (Not supported in RT phones) |
| BLF call-list monitoring | Supported |
| Monitoring of a Call-park slot | Not supported |
| Monitoring of Paging DN | Not supported |
| Monitoring of Conference DN | Not supported |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice register global Example: Router(config)# voice register global | Enters the voice register global configuration mode to set the parameters for all the supported SIP phones in Cisco Unified
                                             Communications Manager Express. |
| Step 4 | mode esrst Example: Router(config-register-global)# mode esrst | Configures the E-SRST mode under the voice register global mode. |
| Step 5 | exit Example: Router(config-register-global)# exit | Exits the voice register-global configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice register dn dn-tag |  |
| Step 4 | shared-line [ max-calls number-of-calls ] |  |
| Step 5 | huntstop channel number-of-channels |  |
| Step 6 | end | Returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | sip-ua |  |
| Step 4 | presence enable |  |
| Step 5 | exit |  |
| Step 6 | max-subscription number |  |
| Step 7 | presence call-list |  |
| Step 8 | end |  |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable |  |
| Step 2 | configure terminal |  |
| Step 3 | voice register dn dn-tag |  |
| Step 4 | number number |  |
| Step 5 | allow watch |  |
| Step 6 | end |  |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable |  |
| Step 2 | configure terminal |  |
| Step 3 | voice register pool pool-tag |  |
| Step 4 | number tag dn dn-tag ] |  |
| Step 5 | blf-speed-dial tag number label string [device] |  |
| Step 6 | presence call-list (To enable Presence feature for all the missed/received/placed calls) |  |
| Step 7 | end |  |

| Note | If the phone and the Unified E-SRST router are in different subnets and you are using id mac in the voice register pool configuration mode. Configure the digest credentials on Cisco Unified Communications Manager, and username password configuration
                                                under voice register pool on Unified E-SRST. Digest Configuration is not required with the id device-id-name CLI command in Cisco Unified SRST Release 12.2. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters telephony-service configuration mode. |
| Step 4 | mode esrst Example: Router(config)# telephony-service | Configures the E-SRST mode under the telephony-service configuration mode. |
| Step 5 | max-ephones max-phones Example: Router(config-telephony)# max-ephones 40 | Configures the maximum supported IP phones by the router. The default is 0. The maximum number is platform-dependent. |
| Step 6 | max-dn max-directory-numbers Example: Router(config-telephony)# max-dn 15 | Sets the maximum supported directory numbers (DNs) by the router. Max-directory-numbers: Maximum supported directory numbers (DNS) or virtual voice ports by the router. The maximum number
                                                   is platform-dependent. The default is 0. |
| Step 7 | ip source-address ip-address [ port port ] [ any-match \| strict-match ] Example: Router(config-telephony)# ip source-address 8.39.23.24 port 2000 | Enables the router to receive messages from the Cisco IP phones through the specified IP addresses and supports strict IP
                                             address verification. The default port number is 2000. |
| Step 8 | call-park system {application \|redirect} Example: Router(config-telephony)# call-park system application | Defines system parameters for the Call Park feature. application : Enables the Call Park features supported in Cisco Unified SRST. |
| Step 9 | hunt-group logout {DND \| HLog} Example: Router(config-telephony)# hunt-group logout HLog | Sets the hunt-group logout options with Hlog in telephony-service configuration mode. |
| Step 10 | transfer-system full-consult Example: Router(config-telephony)# transfer-system full-consult | Specifies the Call Transfer method. full-consult —Calls are transferred with consultation using H.450.2 standard methods and a second phone line if available. Calls fall back
                                                   to full-blind if the second line is unavailable. |
| Step 11 | transfer-pattern transfer-pattern Example: Router(config-telephony)# transfer-pattern .T | Allows transfer of the phone calls by Cisco Unified IP phones to specified phone number patterns. If you have set no transfer
                                             pattern, defaults to other local IP phones. transfer-pattern —A string of digits for permitted Call Transfers. |
| Step 12 | fac { standard \| custom { alias alias-tag \| feature } } Example: Router(config-telephony)# fac standard | Enables all standard feature access codes (FACs) or creates and enables individual custom FACs in telephony-service configuration
                                             mode. |
| Step 13 | create cnf-files Example: Router(config-telephony)# create cnf-files version-stamp | Builds the required XML configuration files for IP phones in the telephony-service configuration mode. |
| Step 14 | exit Example: Router(config-telephony)# exit | Exits the telephony-service configuration mode |
| Step 15 | voice register global Example: Router(config)# voice register global | Enter the voice register global configuration mode. |
| Step 16 | mode esrst Example: Router(config-register-global)# mode esrst | Configures the E-SRST mode under the voice register global mode. |
| Step 17 | max-dn max-directory-numbers Example: Router(config-register-global)# max-dn 40 | Set the maximum supported SIP phone directory numbers (extensions) by a Cisco router in the voice register global configuration
                                             mode. |
| Step 18 | max-pool max-phones Example: Router(config-register-global)# max-pool 40 | Sets maximum supported SIP phones by the Cisco Unified SRST router. Version- and platform-dependent; type? For range. |
| Step 19 | exit Example: Router(config-register-global)# exit | Exits the voice register global configuration mode. |
| Step 20 | voice register dn dn-tag Example: Router(config)# voice register dn 17 | Enter the voice register directory number configuration mode to define a directory number for a SIP phone. Use the same directory number (DN) configured in Cisco Unified Communications Manager to configure the voice register directory
                                             number in Unified E-SRST. |
| Step 21 | number number Example: Router(config-register-dn)# number 7001 | Defines a valid number for a directory number. |
| Step 22 | exit Example: Router(config-register-dn)# exit | Exits the voice register directory number configuration mode. |
| Step 23 | voice register pool pool-tag Example: Router(config)# voice register pool 1 | Enters the voice register Pool configuration mode to set phone-specific parameters for a SIP phone. |
| Step 24 | id [{ network address mask mask \| ip address mask mask \| mac address }] [ device-id-name devicename ] Example: Router(config-register-pool)# id network 8.55.0.0 mask 255.255.0.0 | Explicitly identifies a locally available individual or set of SIP IP phones. The keywords and arguments are defined as follows: network address mask mask : The network address mask mask keyword/argument combination is used to accept SIP Register messages for the indicated phone numbers from any IP phone within
                                                   the indicated IP subnet. ip address mask mask : The ip address mask mask keyword/argument combination is used to identify an individual phone. mac address : MAC address of a particular Cisco Unified IP Phone. device-id-name devicename : Defines the device name to be used to download the phone’s configuration file. |
| Step 25 | dtmf-relay rtp-nte Example: Router(config-register-pool)# dtmf-relay rtp-nte | Forwards DTMF tones by using Real-Time Transport Protocol (RTP) with the Named phone Event (NTE) payload type and enables
                                             the DTMF relay using the RFC 2833 standard method. |
| Step 26 | exit Example: Router(config-register-pool)# exit | Exits the voice register Pool configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice hunt-group hunt-tag {longest-idle \| parallel \| peer \| sequential} Example: Router(config)# voice hunt-group 1 sequential | Enters voice hunt-group configuration mode to define a hunt group. Hunt-tag—Unique sequence number for configuring the hunt group. Range is 1–100. Longest idle—Hunt group in which calls go to the directory number that has been idle for the longest time. Sequential—Hunt group in which directory numbers ring in the order in which they are listed, left to right. Parallel—Hunt group in which all directory numbers ring simultaneously. Peer—Hunt group in which the call placed to a directory number rings for the next directory number in line. |
| Step 4 | members logout Example: Router(config-voice-hunt-group)# members logout | (optional) Configures a Cisco Unified SRST system for all non-shared static members or agents in a voice hunt group with the
                                             Hlogout initial state. |
| Step 5 | list number [, number...] Example: Router(config-voice-hunt-group)# list 1812, 1813, 1814 | Defines a list of extensions that are members of a voice hunt group. |
| Step 6 | timeout seconds Example: Router(config-voice-hunt-group)# timeout 30 | Defines the number of seconds after which directs the unanswered calls to the next number in a voice hunt-group list. |
| Step 7 | statistics collect Example: Router(config-voice-hunt-group)# statistics collect | Enables the collection of call statistics for a voice hunt group. |
| Step 8 | exit Example: Router(config-voice-hunt-group)# exit | Exits the voice hunt group configuration mode. |

| Note | For SCCP phones, CME-as-SRST mode is provisioned using the SRST mode autoprovision command. From 10.5 release onwards, deprecates
                                          this command. When you try to configure CME-as-SRST mode, displays the following message: “Note: This configuration is being deprecated. Please configure "mode esrst" to use the enhanced SRST mode.” |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters telephony-service configuration mode. |
| Step 4 | mode esrst Example: Router(config-telephony)# mode esrst | Enters telephony-service configuration mode. |
| Step 5 | max-ephones max-phones Example: Router(config-telephony)# max-ephones 24 | Enters telephony-service configuration mode. |
| Step 6 | max-dn max-directory-numbers [preference preference-order] [no-reg primary \| both] Example: Router(config-telephony)# max-dn 24 no-reg primary | Limits the number of directory numbers supported by this router. Maximum number is the platform and version-specific. Type? For value. |
| Step 7 | ip source-address ip-address [port port] [any-match \| strict-match] Example: Router(config-telephony)# ip source-address 192.168.11.1 port 2000 | Identifies the IP address and port number that the Cisco Unified SRST router uses for IP phone registration. port port—(Optional) TCP/IP port number to use for SCCP. Range is 2000–9999. Default is 2000. Any-match—(Optional) Disables the strict IP address checking for registration. It is the default setting. Strict-match—(Optional) Instructs the router to reject IP phone registration attempts if the IP server address used by the
                                                phone does not exactly match the source address. |
| Step 8 | exit Example: Router(config-telephony)# exit | Exits telephony-service configuration mode. |
| Step 9 | ephone-dn dn-tag [dual-line] Example: Router(config)# ephone-dn 1 | Enters ephone dn configuration mode to define a directory number for an IP phone, intercom line, voice port, or a message-waiting
                                          indicator (MWI). Dn-tag—Identifies a particular directory number during configuration tasks. Range is 1 to the maximum number of directory
                                                numbers allowed on the router platform. Type? To display  range. |
| Step 10 | number number [secondary number] [no-reg [both \|primary]] Example: Router(config-ephone-dn)# number 1001 | Associates an extension number with this directory number. Number—String of up to 16 digits that represents an extension or E.164 phone number. |
| Step 11 | (Optional) name name Example: Router(config-ephone-dn)# name Smith, John | (Optional) Associates a name with this directory number. Uses the Name for caller-ID displays and in the local directory listings. Follows the name order in the directory command. |
| Step 12 | exit Example: Router(config-telephony)# end | Exits ephone-dn configuration mode. |
| Step 13 | ephone phone-tag Example: Router(config)# ephone 1 | Enters ephone configuration mode to set ephone specific parameters. Phone-tag—Unique sequence number that identifies the phone. Range is version and platform-dependent; type? To display range. |
| Step 14 | mac-address [mac-address] Example: Router(config-ephone)# mac-address 0022.555e.00f1 | Associates the MAC address of a Cisco IP phone with an ephone configuration in a Unified E-SRST system. Mac-address—Identifying MAC address of an IP phone found on a sticker on the bottom of the phone. |
| Step 15 | type phone-type [addon 1 module-type [2 module-type]] Example: Router(config-ephone)# type 7960 | Specifies the type of phone. |
| Step 16 | button button-number{separator}dn-tag [,dn-tag...][button-number{x}overlay-button-number] [button-number...] Example: Router(config-ephone)# button 1:7 | Associates a button number and line characteristics with an ephone-dn. Determines the maximum number of buttons by phone type. |
| Step 17 | end Example: Router(config-telephony)# end | Returns to privileged EXEC mode. |

| Note | For SCCP phones, switching the mode from CME to ESRST and vice versa, results in wiping out the entire CME or ESRST configurations
                                          (including ephone, DNs, templates etc.). |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | ephone-dn dn-tag [dual-line] Example: Router(config)# ephone-dn 1 | Enters ephone dn configuration mode to define a directory number for an IP phone, intercom line, voice port, or a message-waiting
                                             indicator (MWI). Dn-tag—Identifies a particular directory number during configuration task. Range is 1 to the maximum number of directory numbers
                                                   allowed on the router platform. Type? To display the range. |
| Step 4 | number [ secondary [number] [ no-reg [ both \| primary ]] Example: Router(config-ephone-dn)# number 1001 | Associates an extension number with this directory number. number—String of up to 16 digits that represents an extension or E.164 phone number. |
| Step 5 | shared-line sip Example: Router(config-ephone-dn)# shared-line sip | Adds an ephone-dn as a member of a shared directory number for a mixed shared line between Unified SIP and Unified SCCP IP
                                             phones. |
| Step 6 | end Example: Router(config-ephone-dn)# end | Returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | presence |  |
| Step 4 | max-subscription number |  |
| Step 5 | presence call-list | (To enable Presence feature for all the missed or received or placed calls) |
| Step 6 | end |  |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | ephone-dn dn-tag |  |
| Step 2 | number number |  |
| Step 3 | allow watch |  |
| Step 4 | end |  |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable |  |
| Step 2 | configure terminal |  |
| Step 3 | ephone ephone-tag |  |
| Step 4 | button button-number {separator}dn-tag [,dn-tag...] [button-number{x}overlay-button-number][button-number...] |  |
| Step 5 | blf-speed-dial tag number label string [device] |  |
| Step 6 | presence call-list (To enable Presence feature for all the missed/received/placed calls) |  |
| Step 7 | end |  |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Log in to Cisco Unified Communications Manager. |  |
| Step 2 | Go to System > Security -> Phone Security Profile. |  |
| Step 3 | Go to User Management > End User. |  |
| Step 4 | Go to the Phone Settings page and associate the user in the Digest User field. |  |

| Note | Digest authentication does not work with 'id network' configuration in 'voice register pool'. It requires 'id device-id-name'
                                             or 'id Mac' configuration for individual pools. Also DN association on 'voice register pool' is required. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice register pool <pool-tag> |  |
| Step 4 | username <username> password <password> |  |
| Step 5 | end |  |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | ephone ephone tag |  |
| Step 4 | username <username> password <password> |  |
| Step 5 | end |  |