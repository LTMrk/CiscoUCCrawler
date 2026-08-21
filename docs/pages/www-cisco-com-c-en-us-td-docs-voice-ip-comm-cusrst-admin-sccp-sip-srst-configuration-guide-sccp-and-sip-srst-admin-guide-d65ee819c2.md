---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cusrst-admin-sccp-sip-srst-configuration-guide-sccp-and-sip-srst-admin-guide-d65ee819c2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusrst/admin/sccp_sip_srst/configuration/guide/SCCP_and_SIP_SRST_Admin_Guide/srst_41.html
retrieved_at: 2026-08-21T02:49:06.722102+00:00
---

Cisco Unified SRST Administration Guide (All Versions)

# Cisco Unified SRST Administration Guide (All Versions)

Updated: April 25, 2026

Chapter: Cisco Unified SIP SRST

## Chapter: Cisco Unified SIP SRST

# Cisco Unified SIP SRST

This chapter describes the features and provides the configuration information for Cisco Unified SIP SRST 4.1:

Out-of-Dialog REFER(OOD-R)

Digit Collection on SIP Phones

Caller ID Display

Disabling SIP Supplementary Services for Call Forward and Call Transfer

Idle Prompt Status

With Cisco IOS Release 12.4(15)T, the number of SIP phones supported on each platform is now equivalent to the number of SCCP
                                    phones supported. For example, 3845 now supports 720 phones regardless of whether these are SIP or SCCP.

## Prerequisites for Cisco Unified SIP SRST 4.1

Cisco IOS Release 12.4(15)T or a later release.

Cisco Unified IP Phones 7911G, 7941G, 7941GE, 7961G, 7961GE, 7970G, and 7971GE require firmware load 8.2(1) or a later version.

For the prerequisites for the Enhanced 911 Services for Cisco Unified SRST feature introduced in Version 4.1, see Prerequisites for Enhanced 911 Services. .

## Restrictions for Cisco Unified SIP SRST 4.1

Cisco Unified SRST does not support line status speed-dial notification, Call Forward All synchronization, dial plans, directory
                                 services, or Music On Hold (MOH).

Before SIP phone load 8.0, SIP phones maintained dual registration with both Cisco Unified Communications Manager and Cisco
                                 Unified SRST simultaneously. In SIP phone load 8.0 and later versions, SIP phones use keepalive to maintain a connection with
                                 Cisco Unified SRST during active registration with Cisco Unified Communications Manager. Every 2 minutes, a SIP phone sends
                                 a keepalive message to Cisco Unified SRST. Cisco Unified SRST responds to this keepalive with a 404 message. This process
                                 repeats until fallback to Cisco Unified SRST occurs. After fallback, SIP phones send a keepalive message every two minutes
                                 to Cisco Unified Communications Manager while the phones are registered with Cisco Unified SRST. Cisco Unified SRST continues
                                 to support dual registration for SIP phone loads older than 8.0.

### Information About Cisco Unified SIP SRST 4.1

## Out-of-Dialog REFER

Out-of-dialog REFER (OOD-R) enables remote applications to establish calls by sending a REFER message to Cisco Unified SRST
                           without an initial INVITE. After the REFER is sent, the remainder of the call setup is independent of the application and
                           the media stream does not flow through the application. The application using OOD-R triggers a call setup request that specifies
                           the Referee address in the Request-URI and the Refer-Target in the Refer-To header. The SIP messaging used to communicate
                           with Cisco Unified SRST is independent of the end-user device protocol, which can be H.323, plain old telephone service (POTS),
                           SCCP, or SIP. Click-to-dial is an example of an application that can be created using OOD-R.

A click-to-dial application enables users to combine multiple steps into one click for a call setup. For example, a user can
                           click a web-based directory application from his or her PC to look up a phone number, off-hook the desk phone, and dial the
                           called number. The application initiates the call setup without the user having to outdial from his or her own phone. The
                           directory application sends a REFER message to Cisco Unified SRST, which sets up the call between both parties based on this
                           REFER.

For more information about OOD-R, see Out-of-Dialog REFER from the Cisco Unified Communications Manager Express System Administrator Guide .

## Digit Collection on SIP Phones

When you dial a phone, the digit strings must be collected and matched against predefined patterns to place calls to the destination
                           corresponding to your input. Previously, SIP phones in a Cisco Unified SRST system required you to press the DIAL softkey
                           or # key, or wait for the interdigit-timeout to trigger the call processing. This could cause delays in processing the call.

Two new methods of collecting and matching digits are supported for SIP phones depending on the model of the phone:

KPML Digit Collection

SIP Dial Plans

### KPML Digit Collection

The Key Press Markup Language (KPML) uses SIP SUBSCRIBE and NOTIFY methods to report a user input digit by digit. Each digit
                              you dial generates its own signaling message to Cisco Unified SRST. Cisco Unified SRST performs a pattern recognition by matching
                              the destination pattern to the dial peer as it collects the dialed digits. This process of relaying each digit immediately
                              is similar to the process used by SCCP phones. It eliminates the need to press the dial softkey or wait for the interdigit
                              timeout before the digits are sent to the Cisco Unified SRST for processing.

KPML is supported on Cisco Unified IP Phones 7911G, 7941G, 7941GE, 7961G, 7961GE, 7970G, and 7971GE. For configuration information,
                              see Enabling KPML for SIP Phones section.

### SIP Dial Plans

A dial plan is a set of dial patterns that SIP phones use to determine when a digit collection is complete after you go off-hook
                              and dial a destination number. Dial plans enable SIP phones to perform local digit collection and recognize dial patterns
                              that you have keyed. After a pattern is recognized, the SIP phone sends an INVITE message to Cisco Unified SRST to initiate
                              the call to the number matching your input. All the digits entered by the user are presented as a block to Cisco Unified SRST
                              for processing. Because digit collection is done by the phone, dial plans reduce signaling messages overhead compared to KPML
                              digit collection.

SIP dial plans eliminate the need for a user to press the Dial softkey or # key or to wait for the interdigit timeout to trigger
                              an outgoing INVITE. You configure a SIP dial plan and associate the dial plan with a SIP phone. The dial plan is downloaded
                              to the phone in the configuration file.

You can configure SIP dial plans and associate them with the following SIP phones:

Cisco Unified IP Phone 7911G, 7941G, 7941GE, 7961G, 7961GE, 7970G, and 7971GE: These phones use dial plans and support KPML.
                                    If both a dial plan and KPML are enabled, the dial plan has priority.

If a matching dial plan is not found and KPML is disabled, the user must wait for the interdigit timeout before the SIP NOTIFY
                                    message is sent to Cisco Unified SRST. Unlike other SIP phones, these phones do not have a Dial softkey to indicate the end
                                    of dialing, except when on-hook dialing is used.

Cisco Unified IP Phone 7905, 7912, 7940, and 7960: These phones use dial plans and do not support KPML. If you do not configure
                                    a SIP dial plan for these phones, or if the dialed digits do not match a dial plan, the user must press the Dial softkey or
                                    wait for the interdigit timeout before digits are sent to Cisco Unified SRST for processing.

When you reset a phone, the phone requests its configuration files from the TFTP server, which builds the appropriate configuration
                              files depending on the type of phone.

Cisco Unified IP Phone 7905 and 7912: The dial plan is a field in their configuration files.

Cisco Unified IP Phone 7911G, 7940, 7941G, 7941GE, 7960, 7961G, 7961GE, 7970G, and 7971GE: The dial plan is a separate XML
                                    file that is pointed to from the normal configuration file.

The Cisco Unified SRST supports SIP dial plans if they are provisioned in Cisco Unified Communications Manager. You cannot
                              configure dial plans in Cisco Unified SRST.

## Caller ID Display

The Caller ID display includes the name and number of the caller on the Cisco Unified IP Phone 7911G, 7941G, 7941GE, 7961G,
                           7961GE, 7970G, and 7971GE. Other SIP phones display only the number of the caller. Also, the caller ID information is updated
                           on the destination phone when there is a change in the caller ID. The change in the caller ID is of the originating party
                           such as with the call forwarding or Call Transfer. No new configuration is required to support these enhancements.

## Disabling SIP Supplementary Services for Call Forward and Call Transfer

Perform the following steps to disable REFER messages for Call Transfers and redirect responses for call forwarding from being
                              sent to the destination by Cisco Unified SRST. You can disable these supplementary features if the destination gateway does
                              not support them.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip OR dial-peer voice tag voip

- no supplementary-service sip { moved-temporarily | refer }

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

voice service voip OR dial-peer voice tag voip

### Example:

```
Router(config)# voice service voip
```

OR

```
Router(config)# dial-peer voice 99 voip
```

Enters voice-service configuration mode to set global parameters for VoIP features.

OR

Enters dial peer configuration mode to set parameters for a specific dial peer.

Step 4

no supplementary-service sip { moved-temporarily | refer }

### Example:

```
Router(conf-voi-serv)# no supplementary-service
sip refer
```

OR

```
Router(config-dial-peer)# no
supplementary-service sip refer
```

Disables SIP call forwarding or Call Transfer supplementary services globally or for a dial peer.

Moved-temporarily: SIP redirect response for call forwarding.

Refer: SIP REFER message for Call Transfers.

Sending REFER and redirect messages to the destination is the default behavior.

This command is supported for calls between SIP phones and calls between SCCP phones. It is not supported for a mixture of
                                                      SCCP and SIP endpoints.

Step 5

end

### Example:

```
Router(config-voi-serv)# end
```

OR

```
Router(config-dial-peer)# end
```

Exits to privileged EXEC mode.

## Idle Prompt Status

A message displays on the status line of a SIP phone after the phone registers to Cisco Unified SRST to indicate that Cisco
                           Unified SRST is providing fallback support for the Cisco Unified Communications Manager. This message informs the user that
                           the phone is operating in fallback mode and that not all features are available. The default message that displays CM Fallback Service Operating is taken from the phone dictionary file. You can customize the message by using the system message command on the Cisco Unified SRST router. Cisco Unified SRST updates the idle prompt message when you register a SIP phone
                           or when you modify the message through the configuration. The message displays until a phone switches back to the Cisco Unified
                           Communications Manager.

The idle prompt status message supports the Cisco Unified IP Phone 7911G, 7941G, 7941GE, 7961G, 7961GE, 7970G, and 7971GE
                           with Cisco Unified SRST 4.1 onwards. For versions earlier than Cisco Unified SRST 4.1, the phones display the default message
                           from the dictionary file.

## Enhanced 911 Services

Enhanced 911 Services for Cisco Unified SRST enable 911 operators to:

Immediately pinpoint the location of the 911 caller based on the calling number.

Call back the 911 caller if a disconnect occurs.

Before this feature was introduced, Cisco Unified SRST supported only outbound calls to 911. With basic 911 functionality,
                           calls were routed to a Public Safety Answering Point (PSAP). The 911 operator at the PSAP would then have to verbally gather
                           the emergency information and location from the caller, before dispatching a response team from the ambulance service, fire
                           department, or police department. Calls could not be routed to different PSAPs, based on the specific geographic areas that
                           they cover.

With Enhanced 911 Services, emergency calls are selectively routed to the closest PSAP based on the caller’s location. In
                           addition, the caller’s phone number and address automatically display on a terminal at the PSAP. Therefore, the PSAP can quickly
                           dispatch emergency help, even if the caller is unable to communicate the location. Also, if the caller disconnects prematurely,
                           the PSAP has the information to contact the 911 caller.

See Configuring Enhanced 911 Services from Cisco Unified Communications Manager Express System Administrator Guide for more information .

### How to Configure Cisco Unified SIP SRST 4.1 Features

## Enabling KPML for SIP Phones

Perform the following steps to enable KPML digit collection on a SIP phone.

### Before you begin

This feature is supported only on Cisco Unified IP Phone 7911G, 7941G, 7941GE, 7961G, 7961GE, 7970G, and 7971GE.

A dial plan assigned to a phone has priority over KPML.

### SUMMARY STEPS

- enable

- configure terminal

- voice register pool pool-tag

- digit collect kpml

- end

- show voice register dial-peers

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

voice register pool pool-tag

### Example:

```
Router(config)# voice register pool 4
```

Enters voice register Pool configuration mode to set phone-specific parameters for a SIP phone.

pool-tag : Unique sequence number of the SIP phone to be configured. Range is version and platform-dependent; type ? to display range. You can modify the upper limit for this argument with the max-pool command.

Step 4

digit collect kpml

### Example:

```
Router(config-register-pool)# digit collect
kpml
```

Enables KPML digit collection for the SIP phone.

This command is enabled by default for supported phones in Cisco Unified Communications Manager Express and Cisco Unified
                                                      SRST.

Step 5

end

### Example:

```
Router(config-register-pool)# end
```

Exits to privileged EXEC mode.

Step 6

show voice register dial-peers

### Example:

```
Router# show voice register dial-peers
```

Displays details of all dynamically created VoIP dial peers associated with the Cisco Unified Communications Manager Express
                                          SIP register including the defined digit collection method.

### What to do next

After changing the KPML configuration in Cisco Unified SRST, you do not need to create new configuration profiles and restart
                              the phones. Enabling or disabling KPML is effective immediately in Cisco Unified SRST.

## Disabling SIP Supplementary Services for Call Forward and Call Transfer

Perform the following steps to disable REFER messages for Call Transfers and redirect responses for call forwarding from being
                              sent to the destination by Cisco Unified SRST. You can disable these supplementary features if the destination gateway does
                              not support them.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip OR dial-peer voice tag voip

- no supplementary-service sip { moved-temporarily | refer }

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

voice service voip OR dial-peer voice tag voip

### Example:

```
Router(config)# voice service voip
```

OR

```
Router(config)# dial-peer voice 99 voip
```

Enters voice-service configuration mode to set global parameters for VoIP features.

OR

Enters dial peer configuration mode to set parameters for a specific dial peer.

Step 4

no supplementary-service sip { moved-temporarily | refer }

### Example:

```
Router(conf-voi-serv)# no supplementary-service
sip refer
```

OR

```
Router(config-dial-peer)# no
supplementary-service sip refer
```

Disables SIP call forwarding or Call Transfer supplementary services globally or for a dial peer.

Moved-temporarily: SIP redirect response for call forwarding.

Refer: SIP REFER message for Call Transfers.

Sending REFER and redirect messages to the destination is the default behavior.

This command is supported for calls between SIP phones and calls between SCCP phones. It is not supported for a mixture of
                                                      SCCP and SIP endpoints.

Step 5

end

### Example:

```
Router(config-voi-serv)# end
```

OR

```
Router(config-dial-peer)# end
```

Exits to privileged EXEC mode.

## Configuring Idle Prompt Status for SIP Phones

Perform the following steps to customize the message that displays on SIP phones after the phones failover to Cisco Unified
                              SRST.

### Before you begin

Cisco Unified SRST 4.1 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- system message string

- end

- show voice register global

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

voice register global

### Example:

```
Router(config)# voice register global
```

Enters voice register global configuration mode to set global parameters for all supported SIP phones in a Cisco Unified Communications
                                          Manager Express environment.

Step 4

system message string

### Example:

```
Router(config-register-global)# system message
fallback active
```

Defines a status message that displays on SIP phones registered to Cisco Unified SRST.

String: Up to 32 alphanumeric characters. Default value is CM Fallback Service Operating .

Step 5

end

### Example:

```
Router(config-register-global)# end
```

Exits to privileged EXEC mode.

Step 6

show voice register global

### Example:

```
Router# show voice register global
```

Displays all global configuration parameters associated with SIP phones.

### What to do next

The next step is configuring Cisco Unified IP phones using SCCP. For instructions, see Setting Up Cisco Unified IP Phones using SCCP section.

| Note | With Cisco IOS Release 12.4(15)T, the number of SIP phones supported on each platform is now equivalent to the number of SCCP
                                    phones supported. For example, 3845 now supports 720 phones regardless of whether these are SIP or SCCP. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip OR dial-peer voice tag voip Example: Router(config)# voice service voip OR Router(config)# dial-peer voice 99 voip | Enters voice-service configuration mode to set global parameters for VoIP features. OR Enters dial peer configuration mode to set parameters for a specific dial peer. |
| Step 4 | no supplementary-service sip { moved-temporarily \| refer } Example: Router(conf-voi-serv)# no supplementary-service
sip refer OR Router(config-dial-peer)# no
supplementary-service sip refer | Disables SIP call forwarding or Call Transfer supplementary services globally or for a dial peer. Moved-temporarily: SIP redirect response for call forwarding. Refer: SIP REFER message for Call Transfers. Sending REFER and redirect messages to the destination is the default behavior. Note This command is supported for calls between SIP phones and calls between SCCP phones. It is not supported for a mixture of
                                                      SCCP and SIP endpoints. | Note | This command is supported for calls between SIP phones and calls between SCCP phones. It is not supported for a mixture of
                                                      SCCP and SIP endpoints. |
| Note | This command is supported for calls between SIP phones and calls between SCCP phones. It is not supported for a mixture of
                                                      SCCP and SIP endpoints. |
| Step 5 | end Example: Router(config-voi-serv)# end OR Router(config-dial-peer)# end | Exits to privileged EXEC mode. |

| Note | This command is supported for calls between SIP phones and calls between SCCP phones. It is not supported for a mixture of
                                                      SCCP and SIP endpoints. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice register pool pool-tag Example: Router(config)# voice register pool 4 | Enters voice register Pool configuration mode to set phone-specific parameters for a SIP phone. pool-tag : Unique sequence number of the SIP phone to be configured. Range is version and platform-dependent; type ? to display range. You can modify the upper limit for this argument with the max-pool command. |
| Step 4 | digit collect kpml Example: Router(config-register-pool)# digit collect
kpml | Enables KPML digit collection for the SIP phone. Note This command is enabled by default for supported phones in Cisco Unified Communications Manager Express and Cisco Unified
                                                      SRST. | Note | This command is enabled by default for supported phones in Cisco Unified Communications Manager Express and Cisco Unified
                                                      SRST. |
| Note | This command is enabled by default for supported phones in Cisco Unified Communications Manager Express and Cisco Unified
                                                      SRST. |
| Step 5 | end Example: Router(config-register-pool)# end | Exits to privileged EXEC mode. |
| Step 6 | show voice register dial-peers Example: Router# show voice register dial-peers | Displays details of all dynamically created VoIP dial peers associated with the Cisco Unified Communications Manager Express
                                          SIP register including the defined digit collection method. |

| Note | This command is enabled by default for supported phones in Cisco Unified Communications Manager Express and Cisco Unified
                                                      SRST. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip OR dial-peer voice tag voip Example: Router(config)# voice service voip OR Router(config)# dial-peer voice 99 voip | Enters voice-service configuration mode to set global parameters for VoIP features. OR Enters dial peer configuration mode to set parameters for a specific dial peer. |
| Step 4 | no supplementary-service sip { moved-temporarily \| refer } Example: Router(conf-voi-serv)# no supplementary-service
sip refer OR Router(config-dial-peer)# no
supplementary-service sip refer | Disables SIP call forwarding or Call Transfer supplementary services globally or for a dial peer. Moved-temporarily: SIP redirect response for call forwarding. Refer: SIP REFER message for Call Transfers. Sending REFER and redirect messages to the destination is the default behavior. Note This command is supported for calls between SIP phones and calls between SCCP phones. It is not supported for a mixture of
                                                      SCCP and SIP endpoints. | Note | This command is supported for calls between SIP phones and calls between SCCP phones. It is not supported for a mixture of
                                                      SCCP and SIP endpoints. |
| Note | This command is supported for calls between SIP phones and calls between SCCP phones. It is not supported for a mixture of
                                                      SCCP and SIP endpoints. |
| Step 5 | end Example: Router(config-voi-serv)# end OR Router(config-dial-peer)# end | Exits to privileged EXEC mode. |

| Note | This command is supported for calls between SIP phones and calls between SCCP phones. It is not supported for a mixture of
                                                      SCCP and SIP endpoints. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice register global Example: Router(config)# voice register global | Enters voice register global configuration mode to set global parameters for all supported SIP phones in a Cisco Unified Communications
                                          Manager Express environment. |
| Step 4 | system message string Example: Router(config-register-global)# system message
fallback active | Defines a status message that displays on SIP phones registered to Cisco Unified SRST. String: Up to 32 alphanumeric characters. Default value is CM Fallback Service Operating . |
| Step 5 | end Example: Router(config-register-global)# end | Exits to privileged EXEC mode. |
| Step 6 | show voice register global Example: Router# show voice register global | Displays all global configuration parameters associated with SIP phones. |