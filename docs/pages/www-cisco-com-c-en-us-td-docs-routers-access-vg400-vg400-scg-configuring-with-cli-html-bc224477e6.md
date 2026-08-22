---
doc_id: www-cisco-com-c-en-us-td-docs-routers-access-vg400-vg400-scg-configuring-with-cli-html-bc224477e6
source_url: https://www.cisco.com/c/en/us/td/docs/routers/access/vg400/vg400-scg/configuring-with-cli.html
retrieved_at: 2026-08-22T01:13:22.975271+00:00
---

Cisco VG400 Voice Gateway Software Configuration Guide

# Cisco VG400 Voice Gateway Software Configuration Guide

Updated: August 27, 2024

Chapter: Configuring with the Command-Line Interface

## Chapter: Configuring with the Command-Line Interface

# Configuring with the Command-Line Interface

This chapter describes how to use the Cisco IOS software CLI to configure the basic Cisco VG400 analog functionality.

Follow the procedures described in this chapter to configure the Cisco VG400 Voice Gateway. Note that you can change the
                        configuration after you have run the setup command facility.

This chapter does not describe every configuration possible—only a small portion of the most commonly used configuration procedures.
                        For advanced configuration topics, refer to the respective technology configuration guides.

This chapter consists of the following major topics:

## Configuring the Host Name and Password

One of the first configuration tasks you might want to do is to configure the host name and set an encrypted password. Configuring
                           a host name allows you to distinguish a router from another. Setting an encrypted password helps pevent unauthorized configuration
                           changes.

### Summary Steps

- enable

- configure terminal

- hostname 450

- enable secret guessme

- line con 0

- exec-timeout 0 0

- exit

### Detailed Steps

### SUMMARY STEPS

- Router> enable

- Router# configure terminal

- Router(config)# hostname 450

- Router(config)# enable secret guessme

- Router(config)# line con 0Router(config-line)# exec-timeout 0 0

- Router(config-line)# exit

### DETAILED STEPS

Step 1

Router> enable

#### Example:

```
Password: password
```

#### Example:

```
Router#
```

Enables privileged EXEC mode.

- Enter your password, if prompted.

Step 2

Router# configure terminal

#### Example:

```
Enter configuration commands, one per line. End with CNTL/Z.
```

#### Example:

```
Router(config)#
```

Enters global configuration mode.

Step 3

Router(config)# hostname 450

#### Example:

Changes the name of Cisco VG400 to a meaningful name. Substitutes the host name to Router.

Step 4

Router(config)# enable secret guessme

Enters an enable secret password. This password provides access to privileged EXEC mode. When you enter enable at the user
                                             EXEC prompt ( Router> ), you must enter the enable secret password to gain access to configuration mode. Substitute your enable
                                             secret password for guessme.

Step 5

Router(config)# line con 0Router(config-line)# exec-timeout 0 0

Enters line configuration mode to configure the console port.

- Prevents the Cisco VG400, EXEC mode from timing out when you do not enter any information on the console screen for an extended
                                                period.

Step 6

Router(config-line)# exit

Exits from the config-line mode and enters into the global configuration mode.

## Verifying the Host Name and Password

To verify that you configured the correct host name and password, perform the following steps:

### SUMMARY STEPS

- Enter the show config command:

- Exit global configuration mode and attempt to re-enter it using the new enable password:

### DETAILED STEPS

Step 1

Enter the show config command:

### Example:

```
Router# show config Using 2745 out of 262136 bytes
!
version XX.X
.
.
.
!
hostname 450
!
enable secret 5 $1$60L4$X2JYOwoDc0.kqa1loO/w8/
.
.
.
```

Check the host name and encrypted password displayed near the top of the command output.

Step 2

Exit global configuration mode and attempt to re-enter it using the new enable password:

### Example:

```
Router# exit .
.
.
Router con0 is now available
Press RETURN to get started.
Router> enable Password: guessme Router#
```

If you face any issues, check whether:

- Caps Lock is off.

- You entered the correct password. Passwords are case sensitive.

## Configuring a Gigabit Ethernet Interfaces

To configure a Gigabit Ethernet interface, use the configuration software provided with your Cisco VG400 Voice Gateway or
                              network module, if any. Otherwise, for high power and flexibility, use the configuration mode (manual configuration).

This section describes a basic configuration, including enabling the interface and specifying IP routing. Depending on your
                              requirements and the protocols that you plan to route, you might have to enter other configuration commands.

Before you begin configuring the interfaces, perform the following tasks:

- Connect a console to Cisco VG400.

- Power on Cisco VG400.

### SUMMARY STEPS

- Router> enable

- Router# configure terminal

- Router# ip routing

- Router(config)# interface gigabitEthernet 0/0/0

- Router(config-if)# ip address 172.16.74.3 255.255.255.0

- Router(config-if)# exit

- Router(config-if)# Ctrl-z

### DETAILED STEPS

Step 1

Router> enable

### Example:

```
Password: password
```

### Example:

```
Router#
```

Enables privileged EXEC mode.

- Enter your password, if prompted.

Step 2

Router# configure terminal

### Example:

```
Enter configuration commands, one per line. End with CNTL/Z.
```

### Example:

```
Router(config)#
```

Enters global configuration mode.

Step 3

Router# ip routing

### Example:

```
Router# ip?
```

### Example:

```
ip ipc iphc-profile ipv6
```

Enables routing protocols as required for your global configuration. This example uses IP routing.

Step 4

Router(config)# interface gigabitEthernet 0/0/0

### Example:

```
Router(config-if)#
```

Enters interface configuration mode. If the prompt changes to Router(config-if)#, it implies that you have entered the interface
                                          configuration mode.

Step 5

Router(config-if)# ip address 172.16.74.3 255.255.255.0

Assigns an IP address and subnet mask to the interface.

Step 6

Router(config-if)# exit

Exits back to global configuration mode.

Repeat Step 4 through Step 6 if your Cisco VG400 has more than one interface that you need to configure.

Step 7

Router(config-if)# Ctrl-z

### Example:

```
Router#
```

Returns to enable mode when you finish configuring interfaces.

## TLS 1.2 support on SCCP Gateways

The TLS 1.2 support on SCCP Gateways feature details the configuration of TLS 1.2 on SCCP protocol for digital signal processor
                           (DSP) farm including Unicast conference bridge

(CFB), Media Termination Point (MTP), and SCCP telephony control (STC) application (STCAPP).

DSP on gateways can be used as media resources for transrating or transcoding. Each media resource uses Secure Skinny Client
                           Control Protocol (SCCP) to communicate with Cisco Unified Communications Manager. Currently SSL 3.1, which is equivalent to
                           TLS1.0, is used for sending secure signals. This feature enhances the support to TLS 1.2. From Cisco IOS XE Cupertino 17.7.1a,
                           TLS 1.2 is enhanced to support the Next-Generation Encryption (NGE) cipher suites.

Cisco Unified Communications Manager (CUCM) Version 14SU2 has been enhanced to support Secured SCCP gateways with the Subject
                                       Name field (CN Name) with or without colons, for example, AA:22:BB:44:55 or AA22BB4455.

CUCM checks the CN field of the incoming certificate from the SCCP Gateway and verifies it against the DeviceName configured
                                       in CUCM for this gateway. DeviceName contains MAC address of the gateway. CUCM converts the MAC address in the DeviceName
                                       to MAC address with colons (for example: AA:22:BB:44:55) and validates with the CN name in the Gateway's certificate. Therefore,
                                       CUCM mandates Gateway to use MAC address with colons for the CN field in the certificate, that is, subject name.

Due to new guidelines from Defense Information Systems Agency (DISA), it is a requirement not to use colons for the subject
                                       name field CN. For example, AA22BB4455.

### SCCP TLS connection

CiscoSSL is based on OpenSSL. SCCP uses CiscoSSL to secure the communication signals.

If a resource is configured in the secure mode, the SCCP application initiates a process to complete Transport Layer Security
                              (TLS) handshaking. During the handshake, the server sends information to CiscoSSL about the TLS version and cipher suites
                              supported. Previously, only SSL3.1 was supported for SCCP secure signalling. SSL3.1 is equivalent to TLS 1.0. The TLS 1.2
                              Support feature introduces TLS1.2 support to SCCP secure signalling.

After TLS handshaking is complete, SCCP is notified and SCCP kills the process.

If the handshaking is completed successfully, a REGISTER message is sent to Cisco Unified Communications Manager through the
                              secure tunnel. If handshaking fails and a retry is needed, a new process is initiated.

For SCCP-based signalling, only TLS_RSA_WITH_AES_128_CBC_SHA cipher suite is supported.

### Cipher Suites

For SCCP-based signaling, TLS_RSA_WITH_AES_128_CBC_SHA cipher suite is supported.

From Cisco IOS XE Cupertino 17.7.1a, the following NGE cipher suites are also supported:

ECDHE-RSA-AES128-GCM-SHA256

ECDHE-RSA-AES256-GCM-SHA384

These cipher suites enable secure voice signaling for both STCAPP analog phone and SCCP DSPFarm conferencing service. The
                              cipher suite selection is negotiated between GW and CUCM.

The following prerequisites are applicable for using NGE cipher suites:

Configure TLS 1.2. For more information, see Configuring TLS .

Use the CUCM Release 14.1 SU1 or later, and Voice Gateways or platforms that support TLS 1.2.

From CUCM Web UI, navigate to Cipher Management and set the CIPHER switch as NGE. For more information, Cipher Management .

For more information about verifying these cipher suites, see Verifying TLS version and Cipher Suites .

For the SRTP encrypted media, you can use higher-grade cipher suites: AEAD-AES-128-GCM or AEAD-AES-256-GCM. These cipher suites
                              selection is automatically negotiated between GW and CUCM for both secure analog voice and hardware conference bridge voice
                              media. Authenticated Encryption with Associated Data (AEAD) ciphers simultaneously provide confidentiality, integrity, and
                              authenticity, without built-in SHA algorithms to validate message integrity.

### Supported Platforms

The TLS 1.2 support on SCCP Gateways feature is supported on the following platforms:

Cisco VG400, VG420, and VG450 Analog Voice Gateways

### Configuring TLS version for STC application

Perform the following task to configure a TLS version for the STC application:

```
enable
configure terminal
stcapp security tls-version v1.2
exit
```

The stcapp security tls command sets the TLS version to v.1.0, v1.1, or v1.2 only. If not configured explicitly, TLS v1.0
                                          is selected by default.

### Configuring TLS version in Secure Mode for DSP Farm Profile

```
enable
configure terminal
dspfarm profile 7 conference security
  tls-version v1.2
  exit
```

Note: The tls command can be configured only in security mode.

### Verifying TLS version and Cipher Suites

Perform the following task to verify the TLS version and cipher suite:

```
# show dspfarm profile 100 Dspfarm Profile Configuration

 Profile ID = 100, Service = CONFERENCING, Resource ID = 2   
 Profile Service Mode : secure 
 Trustpoint : Overlord_DSPFarm_GW TLS Version  : v1.2
 TLS Cipher   : ECDHE-RSA-AES256-GCM-SHA384 Profile Admin State : UP 
 Profile Operation State : ACTIVE 
 Application : SCCP   Status : ASSOCIATED 
 Resource Provider : FLEX_DSPRM   Status : UP 
 Total Number of Resources Configured : 10 
 Total Number of Resources Available : 10 
 Total Number of Resources Out of Service : 0 
 Total Number of Resources Active : 0
 Maximum conference participants : 8
 Codec Configuration: num_of_codecs:6 
 Codec : g711ulaw, Maximum Packetization Period : 30 , Transcoder: Not Required 
 Codec : g711alaw, Maximum Packetization Period : 30 , Transcoder: Not Required 
 Codec : g729ar8, Maximum Packetization Period : 60 , Transcoder: Not Required 
 Codec : g729abr8, Maximum Packetization Period : 60 , Transcoder: Not Required 
 Codec : g729r8, Maximum Packetization Period : 60 , Transcoder: Not Required 
 Codec : g729br8, Maximum Packetization Period : 60 , Transcoder: Not Required
```

### Verifying STCAPP Application TLS version

Perform the following tasks to verify TLS version of the STCAPP application:

```
Device# show call application voice stcapp App Status: Active
CCM Status: UP
CCM Group: 120
Registration Mode: CCM
Total Devices: 0
Total Calls in Progress: 0
Total Call Legs in Use: 0
ROH Timeout: 45 TLS Version: v1.2 # show stcapp dev voice 0/1/0
Port Identifier:  0/1/0
Device Type:      ALG 
Device Id:        585
Device Name:      ANB3176C85F0080 Device Security Mode : Encrypted TLS version        : TLS version 1.2
  TLS cipher         : ECDHE-RSA-AES256-GCM-SHA384 Modem Capability: None
Device State:     IS
Diagnostic:       None
Directory Number: 80010
Dial Peer(s):     100 
Dialtone after remote onhook feature: activated
Busytone after remote onhook feature: not activated
Last Event:       STCAPP_CC_EV_CALL_MODIFY_DONE
Line State:       ACTIVE
Line Mode:        CALL_CONF
Hook State:       OFFHOOK
mwi:              DISABLE
vmwi:             OFF
mwi config:       Both
Privacy:          Not configured
HG Status:        Unknown
PLAR:             DISABLE
Callback State:   DISABLED
CWT Repetition Interval: 0 second(s) (no repetition)
Number of CCBs:   1
Global call info:
    Total CCB count      = 3
    Total call leg count = 6

Call State for Connection 2 (ACTIVE): TsConnected
Connected Call Info:
   Call Reference: 33535871
   Call ID (DSP):  187
   Local IP Addr:  172.19.155.8
   Local IP Port:  8234
   Remote IP Addr: 172.19.155.61
   Remote IP Port: 8154
   Calling Number: 80010
   Called Number:  
   Codec:          g711ulaw SRTP:           on
   RX Cipher:      AEAD_AES_256_GCM
   TX Cipher:      AEAD_AES_256_GCM
```

Perform the following task to verify the sRTP cipher suite for the DSPfarm connection.

```
# show sccp connection detail bridge-info(bid, cid) - Normal bridge information(Bridge id, Calleg id)
mmbridge-info(bid, cid) - Mixed mode bridge information(Bridge id, Calleg id)

sess_id    conn_id    call-id    codec   pkt-period dtmf_method    type        bridge-info(bid, cid)   mmbridge-info(bid, cid) srtp_cryptosuite          dscp      
                      call_ref   spid       conn_id_tx

16778224   -          125        N/A     N/A        rfc2833_pthru     confmsp   All RTPSPI Callegs      All MM-MSP Callegs      N/A                       N/A       
                      -          -          -         

16778224   16777232   126        g711u   20         rfc2833_pthru  s- rtpspi    (101,125)                N/A                     AEAD_AES_256_GCM          184       
                      30751576   16777219   -         

16778224   16777231   124        g711u   20         rfc2833_pthru  s- rtpspi    (100,125)                N/A                     AEAD_AES_256_GCM          184       
                      30751576   16777219   -         

Total number of active session(s) 1, connection(s) 2, and callegs 3
```

### Verifying Call Information

To display call information for TDM and IVR calls stored in the Forwarding Plane Interface (FPI), use the show voip fpi calls command. You can select a call ID and verify the cipher suite using the command show voip fpi calls confID call_id_number . In this example, cipher suite 6 is AES_256_GCM.

```
# show voip fpi calls Number of Calls : 2
---------- ---------- ---------- ----------- --------------- ---------------
    confID correlator    AcallID     BcallID           state           event
---------- ---------- ---------- ----------- --------------- ---------------
         1          1         87         88       ALLOCATED DETAIL_STAT_RSP
        21         21         89         90       ALLOCATED DETAIL_STAT_RSP

# show voip fpi calls confID 1 ---------------------------------------------------------------------------
VoIP-FPI call entry details:
---------------------------------------------------------------------------
Call Type        :           TDM_IP     confID           :                1
correlator       :                1     call_state       :        ALLOCATED 
last_event       :  DETAIL_STAT_RSP     alloc_start_time :       1796860810 
modify_start_time:                0     delete_start_time:                0 
Media Type(SideA):             SRTP     cipher suite     :                6 
---------------------------------------------------------------------------
FPI State Machine Stats:
------------------------
create_req_call_entry_inserted              :         1
………
```

Feature Name

Releases

Feature Information

Support for NGE Cipher Suites

Cisco IOS XE Cupertino 17.7.1a

This feature supports NGE cipher suites for secure voice signaling and secure media. These cipher suites are applicable for
                                          both STCAPP analog phone and SCCP DSPFarm conferencing service.

## Saving Configuration Changes

To prevent the loss of the Cisco VG400 configuration, save the configuration changes to NVRAM.

### SUMMARY STEPS

- Router> enable

- Router# copy running-config startup-config

- Router(config-if)# Ctrl-z

### DETAILED STEPS

Step 1

Router> enable

### Example:

```
Password: password
```

### Example:

```
Router#
```

Enables privileged EXEC mode.

- Enter your password, if prompted.

Step 2

Router# copy running-config startup-config

Saves the configuration changes to NVRAM so that the changes are not lost during resets, power cycles, or power outages.

Step 3

Router(config-if)# Ctrl-z

### Example:

```
Router#
```

### Example:

```
%SYS-5-CONFIG_I: Configured from console by console
```

Returns to user EXEC mode.

### Enabling UC License

To enable the UC license in the Cisco VG400 Voice Gateway, perform the following steps:

#### Summary Steps

- enable

- configure terminal

- license accept end user agreement

- license boot level uck9

- exit

- save

- reload

#### Detailed Steps

### SUMMARY STEPS

- enable

- configure terminal

- license accept end user agreement

- license boot level uck9

- exit

- write

- reload

### DETAILED STEPS

Step 1

enable

##### Example:

```
Router>enable
```

Enables privileged EXEC mode.

- Enter your password, if prompted.

Step 2

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

license accept end user agreement

##### Example:

```
Router(config)# license accept end user agreement
```

Configures a one-time acceptance of the UC license.

- Accept the UC license by typing YES.

Step 4

license boot level uck9

##### Example:

```
Router(config)# license boot level uck9
```

Enables the Unified Communication License Level license.

Step 5

exit

##### Example:

```
Router(config)# exit
```

Returns to privileged EXEC mode.

Step 6

write

##### Example:

```
Router# write
```

Saves the configuration.

Step 7

reload

##### Example:

```
Router# reload
```

Reloads the router.

### Configuring the Voice Port

### SUMMARY STEPS

- enable

- configure terminal

- voice-port slot / bay / port

- description string

- no shutdown

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

- Enter your password, if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

voice-port slot / bay / port

#### Example:

```
Router(config)# voice-port 1/0/8
```

Enters voice-port configuration mode.

Step 4

description string

#### Example:

```
Router(config-voiceport)# description Voice Port One
```

Attaches a text string to the configuration that describes the connection for this voice port. This description appears in
                                             various displays and is useful for tracking purpose or use of the voice port. The string argument is a character string from
                                             1 to 255 characters in length. By default, there is no text string (describing the voice port) attached to the configuration.

Step 5

no shutdown

#### Example:

```
Router(config-voiceport)# no shutdown
```

Activates the voice port. If a voice port is not being used, shut down the voice port by using the shutdown command.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Router> enable Example: Password: password Example: Router# | Enables privileged EXEC mode. Enter your password, if prompted. |
| Step 2 | Router# configure terminal Example: Enter configuration commands, one per line. End with CNTL/Z. Example: Router(config)# | Enters global configuration mode. |
| Step 3 | Router(config)# hostname 450 Example: | Changes the name of Cisco VG400 to a meaningful name. Substitutes the host name to Router. |
| Step 4 | Router(config)# enable secret guessme | Enters an enable secret password. This password provides access to privileged EXEC mode. When you enter enable at the user
                                             EXEC prompt ( Router> ), you must enter the enable secret password to gain access to configuration mode. Substitute your enable
                                             secret password for guessme. |
| Step 5 | Router(config)# line con 0Router(config-line)# exec-timeout 0 0 | Enters line configuration mode to configure the console port. Prevents the Cisco VG400, EXEC mode from timing out when you do not enter any information on the console screen for an extended
                                                period. |
| Step 6 | Router(config-line)# exit | Exits from the config-line mode and enters into the global configuration mode. |

| Step 1 | Enter the show config command: Example: Router# show config Using 2745 out of 262136 bytes
!
version XX.X
.
.
.
!
hostname 450
!
enable secret 5 $1$60L4$X2JYOwoDc0.kqa1loO/w8/
.
.
. Check the host name and encrypted password displayed near the top of the command output. |
|---|---|
| Step 2 | Exit global configuration mode and attempt to re-enter it using the new enable password: Example: Router# exit .
.
.
Router con0 is now available
Press RETURN to get started.
Router> enable Password: guessme Router# If you face any issues, check whether: Caps Lock is off. You entered the correct password. Passwords are case sensitive. |

| Note | Before you begin, disconnect all the WAN cables from Cisco VG400 to prevent it from running the AutoInstall process. Cisco
                                       VG400 attempts to run AutoInstall whenever you power the Voice Gateway on and there is a WAN connection on both ends. Cisco
                                       VG400 does not have a valid configuration file stored in NVRAM (for instance, when you add a new interface). It can take several
                                       minutes for Cisco VG400 to determine that AutoInstall is not connected to a remote TCP/IP host. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Router> enable Example: Password: password Example: Router# | Enables privileged EXEC mode. Enter your password, if prompted. |
| Step 2 | Router# configure terminal Example: Enter configuration commands, one per line. End with CNTL/Z. Example: Router(config)# | Enters global configuration mode. |
| Step 3 | Router# ip routing Example: Router# ip? Example: ip ipc iphc-profile ipv6 | Enables routing protocols as required for your global configuration. This example uses IP routing. |
| Step 4 | Router(config)# interface gigabitEthernet 0/0/0 Example: Router(config-if)# | Enters interface configuration mode. If the prompt changes to Router(config-if)#, it implies that you have entered the interface
                                          configuration mode. |
| Step 5 | Router(config-if)# ip address 172.16.74.3 255.255.255.0 | Assigns an IP address and subnet mask to the interface. |
| Step 6 | Router(config-if)# exit | Exits back to global configuration mode. Repeat Step 4 through Step 6 if your Cisco VG400 has more than one interface that you need to configure. |
| Step 7 | Router(config-if)# Ctrl-z Example: Router# | Returns to enable mode when you finish configuring interfaces. |

| Note | Cisco Unified Communications Manager (CUCM) Version 14SU2 has been enhanced to support Secured SCCP gateways with the Subject
                                       Name field (CN Name) with or without colons, for example, AA:22:BB:44:55 or AA22BB4455. CUCM checks the CN field of the incoming certificate from the SCCP Gateway and verifies it against the DeviceName configured
                                       in CUCM for this gateway. DeviceName contains MAC address of the gateway. CUCM converts the MAC address in the DeviceName
                                       to MAC address with colons (for example: AA:22:BB:44:55) and validates with the CN name in the Gateway's certificate. Therefore,
                                       CUCM mandates Gateway to use MAC address with colons for the CN field in the certificate, that is, subject name. Due to new guidelines from Defense Information Systems Agency (DISA), it is a requirement not to use colons for the subject
                                       name field CN. For example, AA22BB4455. |
|---|---|

| Note | For SCCP-based signalling, only TLS_RSA_WITH_AES_128_CBC_SHA cipher suite is supported. |
|---|---|

| Note | The stcapp security tls command sets the TLS version to v.1.0, v1.1, or v1.2 only. If not configured explicitly, TLS v1.0
                                          is selected by default. |
|---|---|

| Note | Note: The tls command can be configured only in security mode. |
|---|---|

| Feature Name | Releases | Feature Information |
|---|---|---|
| Support for NGE Cipher Suites | Cisco IOS XE Cupertino 17.7.1a | This feature supports NGE cipher suites for secure voice signaling and secure media. These cipher suites are applicable for
                                          both STCAPP analog phone and SCCP DSPFarm conferencing service. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Router> enable Example: Password: password Example: Router# | Enables privileged EXEC mode. Enter your password, if prompted. |
| Step 2 | Router# copy running-config startup-config | Saves the configuration changes to NVRAM so that the changes are not lost during resets, power cycles, or power outages. |
| Step 3 | Router(config-if)# Ctrl-z Example: Router# Example: %SYS-5-CONFIG_I: Configured from console by console | Returns to user EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router>enable | Enables privileged EXEC mode. Enter your password, if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | license accept end user agreement Example: Router(config)# license accept end user agreement | Configures a one-time acceptance of the UC license. Accept the UC license by typing YES. |
| Step 4 | license boot level uck9 Example: Router(config)# license boot level uck9 | Enables the Unified Communication License Level license. |
| Step 5 | exit Example: Router(config)# exit | Returns to privileged EXEC mode. |
| Step 6 | write Example: Router# write | Saves the configuration. |
| Step 7 | reload Example: Router# reload | Reloads the router. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password, if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice-port slot / bay / port Example: Router(config)# voice-port 1/0/8 | Enters voice-port configuration mode. |
| Step 4 | description string Example: Router(config-voiceport)# description Voice Port One | Attaches a text string to the configuration that describes the connection for this voice port. This description appears in
                                             various displays and is useful for tracking purpose or use of the voice port. The string argument is a character string from
                                             1 to 255 characters in length. By default, there is no text string (describing the voice port) attached to the configuration. |
| Step 5 | no shutdown Example: Router(config-voiceport)# no shutdown | Activates the voice port. If a voice port is not being used, shut down the voice port by using the shutdown command. |