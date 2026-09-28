---
doc_id: www-cisco-com-c-en-us-td-docs-routers-access-vg410-software-configuration-vg410-software-config-guide-configuring-sip-li-f95b1ac7d0
source_url: https://www.cisco.com/c/en/us/td/docs/routers/access/vg410/software-configuration/vg410-software-config-guide/configuring-sip-line-features-manually.html
retrieved_at: 2026-08-22T01:18:26.373393+00:00
---

Cisco VG410 Voice Gateway Software Configuration Guide

# Cisco VG410 Voice Gateway Software Configuration Guide

Updated: August 27, 2024

Chapter: Configuring SIP Line Features Manually

## Chapter: Configuring SIP Line Features Manually

# Configuring SIP Line Features Manually

This chapter explains how to configure voice gateway SIP Line features manually. If you're using a Cisco Voice Gateway VG400
                        Series device which is running on Cisco IOS XE version before 17.15.1, perfrom the tasks specified in this chapter to configure
                        SIP Line features manually.

To provision these features, you must configure outbound VOIP Dial-peer, Pots Dial-peer, Voice Card, and SIP as described
                        in this chapter.

Use this configuration only for devices running on releases earlier than Cisco IOS XE 17.15.1a. From Cisco IOS XE 17.15.1a, Auto Configuration is enabled and you do not have to manually perform this configuration.

## Restrictions

The following restrictions and limitations are applicable for this configuration:

Only one line number per FXS port is supported, and shared line is not supported.

The line side SIP endpoints are controlled by one CUCM only. Switch over and switch back are not supported.

Non-DSAPP-controlled devices are not supported. You must configure 'service dsapp' before you configure pots dial-peer and
                                 voip dial-peer.

You cannot combine IPv4 and IPv6 in this configuration.

The SIP analog calls go through the CUCM, and hairpin calls are not supported.

SIP analog ports signaling for failover between the CUCMs is not supported.

3-way conference only supports G711 codec.

Media recording, overlap dialing, secure calls, failover, and fallback are not supported.

In the CUCM web interface, you can add more than one line under Phone Configuration . However, only the first line will be associated with the phone, and the rest of the lines will not be applied

## Configure FXS Ports for Supplementary Services

To handle supplementary services for Foreign Exchange Station (FXS) ports, the event handler handles the hookflash or onhook
                           events. Additionally, the event handler also sends events to call control and triggers the supplementary service on SIP SPI.
                           However, currently, FXS ports do not register on CUCM as SIP endpoints. To ensure the FXS port are registered as a SIP endpoints,
                           make sure that:

Each configured FXS ports is registered to CUCM. The CUCM creates the database for proper call routing based on the registered
                                 endpoint.

The SIP stack adds or modifies SIP headers content to a proper interface with CUCM and enables new features such as directed
                                 call retrieval, call pick-up, and so on.

The FXS ports for Supplementary Services supports CUCM verions 14SU3, version 15, and later. However, CUCM-controlled endpoints
                           with auto configuration can be enabled only on CUCM version 15 and later.

You must use the no local-bypass command for all the media in this configuration.

## Configuring the Device Control Session Application

Step 1

enable

### Example:

```
vg410> enable
```

Enables privileged EXEC mode. Enter the password, if prompted.

Step 2

configure terminal

### Example:

```
vg410# configure terminal
```

Enters the global configuration mode.

Step 3

application global service default dsapp

### Example:

```
vg410(config)# application
vg410(config-app)# global
vg410(app-global)# service default dsapp
```

(Optional) Enables the new hookflash functionality globally. Device Control Session Application (DSAPP) application global
                                          service default drives these hookflash features and it must be configured for new bookflash functionality for an application
                                          framework module in IOS. DSAPP can be configured globally or on a dial-peer basis.

This is a global configuration command. After you configure this command, all the calls are impacted. Even a FXO call will
                                                      be controlled by DSAPP application which can lead to a failure. If the gateway is controlled by a DSAPP application, it is
                                                      not recommended to make DSAPP as the default call controler.

Step 4

param dial-peer <number>

### Example:

```
vg410(config)# application
vg410(config-app)# service dsapp
vg410(app-global)# param dial-peer 100
```

If multiple dial-peer matches are made for the destination-pattern, dial-peer 100 command is used.

When you configure DSAPP on a dial-peer basis,specify a VOIP dial-peer for any outbound call. If all outbound calls that use
                                                      the hookflash functionality are on the same server, it is recommended to use the param dial-peer command.

Step 5

param callWaiting <string>

### Example:

```
vg410(config)#application
vg410(config-app)# service dsapp
vg410(app-global)# param dial-peer 100
vg410(app-global)# param callWaiting TRUE
```

Enables the call waiting feature.

Step 6

param callConference <string>

### Example:

```
vg410(config)# application
vg410(config-app)# service dsapp
vg410(app-global)# param dial-peer 100
vg410(app-global)# param callWaiting TRUE
vg410(app-global)# param callConference TRUE
```

Enables the call conference feature.

Step 7

param callTransfer <string>

### Example:

```
vg410(config)# application
vg410(config-app)# service dsapp
vg410(app-global)# param dial-peer 100
vg410(app-global)# param callWaiting TRUE
vg410(app-global)# param callConference TRUE
vg410(app-global)# param callTransfer TRUE
```

Enables the call transfer feature.

### Configuring the Outbound Voip Dial-peer

Outbound dial-peer is configured like regular voip dial-peer for SIP. In addition to the parameters required, the following
                              configurations are required:

service dsapp: Specifies that the dial-peer is controlled by a DSAPP application

session transport tcp: Specifies that only TCP signaling is supported

voice-class sip extension gw-ana: Indicates that this parameter is used to interop with CUCM

voice-class sip bind control source-interface GigabitEthernetx/y/z: Indicates that this interface’s mac address is the base
                                    mac.

dual tone multifrequency (DTMF): Specifies how a Session Initiation Protocol (SIP) gateway relays dual tone multifrequency
                                    (DTMF) tones between telephony interfaces and an IP network. This feature supports rtp-nte DTMF relay mechanisms for the SIP dial peers.

Here is a sample outbound voip dial-peer configuration:

```
dial-peer voice 714281111 voip
service dsapp
destination-pattern .+
session protocol sipv2
session target ipv4:172.16.0.0
incoming called-number 7141116...
voice-class sip bind control source-interface GigabitEthernet0/0/0
codec g711ulaw
```

G711 is the only codec supported for conference calls. Hence it is recommended that you add this codec for conference calls.

The following is a sample configuration for DTMF relay:

```
dtmf-relay method1 [...[method6]]
dtmf-relay rtp-nte
```

### Configuring POTS Dial-peer

Plain Old Telephone Service (POTS) dial peers retain the characteristics of a traditional telephony network connection. POTS
                              dial peers map a dialed string to a specific voice port on the local router, normally the voice port connecting the router
                              to the local PSTN, PBX, or telephone.

You can configure the POTS dial-peer feature by using the dial-peer voice command. In addition to the parameters required, you can also configure the following commands under POTS dial-peer to interpret
                              hookflash (HF) and to interop with CUCM:

service dsapp: Specifies this dial-peer is to be controlled by the DSAPP application

voice-class sip extension gw-ana: Indicates that this parameter is used to interop with CUCM

See the following sample configuration of the POTS dial-peer feature here:

```
dial-peer voice 19993000 pots
service dsapp
destination-pattern 2124506300
voice-class sip extension gw-ana
port 3/0/0
```

### Configuring Voice-card and SIP

When you configure the voice-card, all the traffic should go through the CUCM. Hairpin calls are not supported. You have to
                              execute the no local-bypass command for the voice-card that have FXS SIP endpoints.

For FXS SIP endpoints to register, configure the registrar IP address command under the sip-ua mode and use the TCP as the transport type. Note that UDP protocal is not supported.

```
!
voice-card 3/0
no local-bypass
no watchdog
!
!
sip-ua
registrar ipv4:172.16.0.0 expires 3600 tcp
protocol mode dual-stack
!
```

### Enabling Device Control Session Application Line features

To register to CUCM as a SIP endpoint, and to distinguish line feature from trunk, you should configure the dsapp line command.

Step 1

enable

#### Example:

```
vg410> enable
```

Enters the privileged EXEC mode. Enter the password, if prompted.

Step 2

configure terminal

#### Example:

```
vg410# configure terminal
```

Enters the global configuration mode.

Step 3

dsapp line

#### Example:

```
vg410(config)#
vg410(config)#dsapp line
vg410(config)#
```

Specifies the format of each call feature.

If you do not configure the dsapp line command, the gateway acts like a SIP trunk and the analog phones might not register as SIP endpoints. Further, you cannot
                                                         configure the Feature Access Code (FAC). You must run the dsapp line command to use the SIP line features.

### Configuring Feature Access Code

The dsapp line feature access-code command invokes the feature to translate the Feature Access Code (FAC) to the format that the CUCM understands. If you do
                              not configure this command, the whole FAC digits are sent to the CUCM and may not invoke features. You can also change the
                              default FAC in the sub-mode.

Analog phones do not have soft keys. The required supplementary service features are invoked through FAC. By default, the
                              FAC has ‘**’ prefix which can be changed using the CLI command.

```
vg410(config)#dsapp line feature access-code
vg410(config-dsappline-fac)#prefix *#
vg410(config-dsappline-fac)#cancel-call-waiting **4
vg410(config-dsappline-fac)#exit
vg410# show dsapp line feature codes
dsapp line feature access-code
prefix *#
call forward all *#1
call forward cancel *#2
pickup local *#5
pickup group *#7
pickup direct *#6
cancel-call-waiting **4
last-redial *#3
```

If you don't configure the dsapp line feature access-code , the voice gateway does not translate the FAC to the format that the CUCM understands. The whole FAC digits is sent to the
                              CUCM.

After the FAC is disabled and re-enabled, all the FAC and prefix are rolled back to the default values.

```
vg410(config)#no dsapp line feature access-code
Feature access-code disabled
vg410(config)# do show dsapp line feature codes
dsappline feature access-code disabled
vg410(config)# dsapp line feature access-code
vg410(config-dsappline-fac)#do show dsapp line feature codes
dsapp line feature access-code
prefix **
call forward all **1
call forward cancel **2
pickup local **5
pickup group **7
pickup direct **6
cancel-call-waiting **9
last-redial **3
vg410(config-dsappline-fac)# do show run | b dsapp line
dsapp line
!
dsapp line feature access-code
!
```

### Verifying the Device Control Session Application Configuration

Use the following commands to verify the the DSAPP configuration:

show dsapp line device summary

show dsapp line feature codes

show ccm-manager config-download

The show dsapp line device summary command shows whether the FXS ports are successfully registered to the CUCM as SIP endpoints.

```
vg410# show dsapp line device summary
Total Devices: 3
Port Device Registration Dev Directory Last Number
Identifier Name           State        Type  Number     Dialed
---------- --------------- ------------- ------- ----------- -----------
0/0/xx    ANDD309DD761600 REGISTERED   ALG   2124506300 Not Avail
0/0/xx    ANDD309DD761601 REGISTERED   ALG   2124506301 Not Avail
0/0/xx    ANDD309DD761602 UNREGISTERED ALG   2124506302 Not Avail
router#
```

The show dsapp line feature codes command shows whether FAC is enabled and displays the feature codes.

```
vg410# show dsapp line feature codes
dsapp line feature access-code
prefix **
call forward all **1
call forward cancel **2
pickup local **5
pickup group **7
pickup direct **6
cancel-call-waiting **9
last-redial **3
```

The show ccm-manager config-download command provides download status and history of the auto-configuration.

```
vg410# show ccm-manager config-download
SIP Line Side Analog auto-configuration status
===============================================================
Registered with Call Manager: Yes
Local interface: GigabitEthernet0/0/0 (2c5a.0fc8.8b70)
Current version-id: 1541004382-f60b9ac2-ce5b-439e-92e5-02b62e26d15c
Current config applied at: 16:47:40 UTC Aug 18 2023
Gateway downloads succeeded: 2
Gateway download attempts: 2
Last gateway download attempt: 16:47:40 UTC Aug 18 2023
Last successful gateway download: 16:47:40 UTC Aug 18 2023
Current TFTP server: 172.19.156.84
Gateway resets: 1
Managed endpoints: 3
Endpoint downloads succeeded: 6
Endpoint download attempts: 6
Last endpoint download attempt: 16:47:40 UTC Aug 18 2023
Last successful endpoint download: 16:47:40 UTC Aug 18 2023

Endpoint resets: 0
Endpoint restarts: 0
Configuration Error History:
```

| Note | Use this configuration only for devices running on releases earlier than Cisco IOS XE 17.15.1a. From Cisco IOS XE 17.15.1a, Auto Configuration is enabled and you do not have to manually perform this configuration. |
|---|---|

| Note | You must use the no local-bypass command for all the media in this configuration. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: vg410> enable | Enables privileged EXEC mode. Enter the password, if prompted. |
| Step 2 | configure terminal Example: vg410# configure terminal | Enters the global configuration mode. |
| Step 3 | application global service default dsapp Example: vg410(config)# application
vg410(config-app)# global
vg410(app-global)# service default dsapp | (Optional) Enables the new hookflash functionality globally. Device Control Session Application (DSAPP) application global
                                          service default drives these hookflash features and it must be configured for new bookflash functionality for an application
                                          framework module in IOS. DSAPP can be configured globally or on a dial-peer basis. Note This is a global configuration command. After you configure this command, all the calls are impacted. Even a FXO call will
                                                      be controlled by DSAPP application which can lead to a failure. If the gateway is controlled by a DSAPP application, it is
                                                      not recommended to make DSAPP as the default call controler. | Note | This is a global configuration command. After you configure this command, all the calls are impacted. Even a FXO call will
                                                      be controlled by DSAPP application which can lead to a failure. If the gateway is controlled by a DSAPP application, it is
                                                      not recommended to make DSAPP as the default call controler. |
| Note | This is a global configuration command. After you configure this command, all the calls are impacted. Even a FXO call will
                                                      be controlled by DSAPP application which can lead to a failure. If the gateway is controlled by a DSAPP application, it is
                                                      not recommended to make DSAPP as the default call controler. |
| Step 4 | param dial-peer <number> Example: vg410(config)# application
vg410(config-app)# service dsapp
vg410(app-global)# param dial-peer 100 | If multiple dial-peer matches are made for the destination-pattern, dial-peer 100 command is used. Note When you configure DSAPP on a dial-peer basis,specify a VOIP dial-peer for any outbound call. If all outbound calls that use
                                                      the hookflash functionality are on the same server, it is recommended to use the param dial-peer command. | Note | When you configure DSAPP on a dial-peer basis,specify a VOIP dial-peer for any outbound call. If all outbound calls that use
                                                      the hookflash functionality are on the same server, it is recommended to use the param dial-peer command. |
| Note | When you configure DSAPP on a dial-peer basis,specify a VOIP dial-peer for any outbound call. If all outbound calls that use
                                                      the hookflash functionality are on the same server, it is recommended to use the param dial-peer command. |
| Step 5 | param callWaiting <string> Example: vg410(config)#application
vg410(config-app)# service dsapp
vg410(app-global)# param dial-peer 100
vg410(app-global)# param callWaiting TRUE | Enables the call waiting feature. |
| Step 6 | param callConference <string> Example: vg410(config)# application
vg410(config-app)# service dsapp
vg410(app-global)# param dial-peer 100
vg410(app-global)# param callWaiting TRUE
vg410(app-global)# param callConference TRUE | Enables the call conference feature. |
| Step 7 | param callTransfer <string> Example: vg410(config)# application
vg410(config-app)# service dsapp
vg410(app-global)# param dial-peer 100
vg410(app-global)# param callWaiting TRUE
vg410(app-global)# param callConference TRUE
vg410(app-global)# param callTransfer TRUE | Enables the call transfer feature. |

| Note | This is a global configuration command. After you configure this command, all the calls are impacted. Even a FXO call will
                                                      be controlled by DSAPP application which can lead to a failure. If the gateway is controlled by a DSAPP application, it is
                                                      not recommended to make DSAPP as the default call controler. |
|---|---|

| Note | When you configure DSAPP on a dial-peer basis,specify a VOIP dial-peer for any outbound call. If all outbound calls that use
                                                      the hookflash functionality are on the same server, it is recommended to use the param dial-peer command. |
|---|---|

| Note | G711 is the only codec supported for conference calls. Hence it is recommended that you add this codec for conference calls. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: vg410> enable | Enters the privileged EXEC mode. Enter the password, if prompted. |
| Step 2 | configure terminal Example: vg410# configure terminal | Enters the global configuration mode. |
| Step 3 | dsapp line Example: vg410(config)#
vg410(config)#dsapp line
vg410(config)# | Specifies the format of each call feature. Note If you do not configure the dsapp line command, the gateway acts like a SIP trunk and the analog phones might not register as SIP endpoints. Further, you cannot
                                                         configure the Feature Access Code (FAC). You must run the dsapp line command to use the SIP line features. | Note | If you do not configure the dsapp line command, the gateway acts like a SIP trunk and the analog phones might not register as SIP endpoints. Further, you cannot
                                                         configure the Feature Access Code (FAC). You must run the dsapp line command to use the SIP line features. |
| Note | If you do not configure the dsapp line command, the gateway acts like a SIP trunk and the analog phones might not register as SIP endpoints. Further, you cannot
                                                         configure the Feature Access Code (FAC). You must run the dsapp line command to use the SIP line features. |

| Note | If you do not configure the dsapp line command, the gateway acts like a SIP trunk and the analog phones might not register as SIP endpoints. Further, you cannot
                                                         configure the Feature Access Code (FAC). You must run the dsapp line command to use the SIP line features. |
|---|---|