---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-integration-pimg-b-14cucintpimg-b-14cucintpimg-appendix-010110-6a1b6732db
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/integration/pimg/b_14cucintpimg/b_14cucintpimg_appendix_010110.html
retrieved_at: 2026-08-16T18:38:18.278321+00:00
---

PIMG Integration Guide for Cisco Unity Connection Release 14

# PIMG Integration Guide for Cisco Unity Connection Release 14

Updated: March 25, 2021

Chapter: Settings for PIMG Firmware Version 5.x

## Chapter: Settings for PIMG Firmware Version 5.x

# Settings for PIMG Firmware Version 5.x

## Settings for PIMG Firmware Version 5.x

### Digital PIMG Settings (Firmware Version 5.x)

Do the following steps to set up the Digital PIMG units

### SUMMARY STEPS

- On a Windows workstation, sign in to a PIMG unit.

- In the Configure menu, select System .

- On the System page, enter the following settings.

- Select Apply Changes .

- On the Configure menu, select Gateway .

- On the Gateway page, select the Gateway Routing tab.

- On the Gateway Routing tab, Unity Connection without a cluster, skip to Step 8 . If Unity Connection has a cluster configured, do the following substeps:

- Under VoIP Endpoint ID, enter the following settings.

- Select Apply Changes .

- Select the Gateway Advanced tab.

- On the Gateway Advanced tab, enter the following settings.

- Select Apply Changes .

- Select the Gateway Capabilities tab.

- Depending on how you have planned to use the voice messaging ports, select the applicable setting for each port in the Telephony
                                 Port Capability column.

- Select Apply Changes .

- On the Configure menu, select SIP .

- On the SIP page, enter the following settings.

- Select Apply Changes .

- On the Configure menu, select IP .

- On the IP page, enter the following settings.

- Select Apply Changes .

- On the Configure menu, select Tones .

- On the Tones page, select the Learn tab.

- On the Tones page, for the Dialtone event, confirm that the Acquire Tone check box is checked and leave the Destination Address
                                 field blank.

- On the Tones page, for the Busy Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                 to verify that the tone is correct.

- On the Tones page, in the Destination Address field for Busy Tone, enter the extension that you dialed in Step 25 c. from the third phone.

- On the Tones page, for the Error/Reorder Tone event, confirm that the Acquire Tone check box is checked and do the following
                                 substeps to verify that the tone is correct.

- On the Tones page, in the Destination Address field for Error/Reorder Tone, enter the extension that you dialed in Step 27 a.

- On the Tones page, for the Ringback Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                 to verify that the tone is correct.

- On the Tones page, in the Destination Address field for Ringback Tone, enter the extension that you dialed in Step 29 a.

- Select Learn .

- When the process is complete, check the check box for each newly learned tone and select Apply .

- Hang up the phones that you used in Step 25 .

- On the Configure menu, select Restart .

- On the Restart page, select Restart Unit Now .

- When the PIMG unit has restarted, in the View menu, select Refresh .

- Repeat Step 1 through Step 36 on all remaining PIMG units.

### DETAILED STEPS

Step 1

On a Windows workstation, sign in to a PIMG unit.

Step 2

In the Configure menu, select System .

Step 3

On the System page, enter the following settings.

Field

Setting

Operating Mode

Select SIP .

PBX Type

Select the applicable setting:

For Avaya phone systems, select Lucent .

For NEC phone systems, select NEC_NEAX .

For Nortel phone systems, select M1 .

For Siemens phone systems, select Optiset_300ECS .

PCM Coding

Select uLaw .

Step 4

Select Apply Changes .

Step 5

On the Configure menu, select Gateway .

Step 6

On the Gateway page, select the Gateway Routing tab.

Step 7

On the Gateway Routing tab, Unity Connection without a cluster, skip to Step 8 . If Unity Connection has a cluster configured, do the following substeps:

In the Fault Tolerance Enabled field, select Yes .

In the Load Balancing Enabled field, select No.

Step 8

Under VoIP Endpoint ID, enter the following settings.

To add endpoints, select Add New Endpoint .

Count

VoIP Endpoint ID

1

(Unity Connection without a cluster) Enter the server name of the Unity Connection server.

(Unity Connection with a cluster configured) Enter the server name of the subscriber Unity Connection server.

2

(Unity Connection without a cluster) Enter the server name of the Unity Connection server.

(Unity Connection with a cluster configured) Enter the server name of the publisher server.

Step 9

Select Apply Changes .

Step 10

Select the Gateway Advanced tab.

Step 11

On the Gateway Advanced tab, enter the following settings.

Field

Settings

Call Connect Mode

Select OnAnswer .

Destination for Unroutable PBX Calls

Enter the extension of an attendant who receives calls to Cisco Unity Connection that are unanswered.

Minimum Call Party Delay (msecs)

Enter 500 .

Turn MWI On FAC

For Siemens Hicom 300 E (North American) phone systems, enter Enter #*1 . Otherwise, leave this field blank.

Turn MWI Off FAC

For Siemens Hicom 300 ECS phone systems, enter Enter #*8 . Otherwise, leave this field blank.

Wait for Ringback/Connect on Blind Transfer

Select Yes .

Hunt Group Extension

Enter the pilot number of the Unity Connection voice messaging ports.

Audio Compression

Select the preferred codec for audio compression:

G.711

G.729AB

Signaling Digit Relay Mode

Select Off .

Voice Activity Detection

Select Off .

Frame Size

Select the applicable setting:

G.711— 20

G.729AB— 10

Failure to use the correct setting results in recorded messages containing nothing but silence.

Frames Per Packet

Select the applicable setting:

G.711— 1

G.729AB— 2

Failure to use the correct setting results in recorded messages containing nothing but silence.

Call Control QOS Byte

Enter 104 (equivalent to DSCP AF31).

RTP QOS Byte

Enter 184 (equivalent to DSCP EF).

Step 12

Select Apply Changes .

Step 13

Select the Gateway Capabilities tab.

Step 14

Depending on how you have planned to use the voice messaging ports, select the applicable setting for each port in the Telephony
                                          Port Capability column.

Telephony Port Capability Settings

Voice Messaging Port Usage

Calls-Only

The port answers incoming calls only and cannot dial out (for example, to set MWIs or send message notifications).

MWIs-Only

The port dial out only (for example, to set MWIs or send message notifications) and cannot answer incoming calls.

Both

The port answers incoming calls and also dial out (for example, to set MWIs or send message notifications).

In setting up the PIMG unit, do not send calls to ports in Unity Connection that cannot answer calls (voice messaging ports
                                             that are not set to Answer Calls). For example, if a voice messaging port is set only to Send MWI Requests, do not send calls
                                             to it. Otherwise the integration cannot function correctly.

If a port in Unity Connection is disabled, select No in the Telephony Port Enabled column for the corresponding port on this tab. Note that changing a setting in the Telephony
                                             Port Enabled column requires restarting the PIMG unit.

Step 15

Select Apply Changes .

Step 16

On the Configure menu, select SIP .

Step 17

On the SIP page, enter the following settings.

Field

Setting

Host and Domain Name

Enter the domain name of the PIMG unit.

Server Port

Enter 5060 .

Primary Proxy Server Address

Leave this field blank.

Primary Proxy Server Port

Not applicable. Leave the default setting.

Backup Proxy Server Address

Not applicable. Leave the default setting.

Backup Proxy Server Port

Not applicable. Leave the default setting.

Proxy Query Interval

Enter 10 .

T1 Time

Enter 400 .

T2 Time

Enter 3000 .

Step 18

Select Apply Changes .

Step 19

On the Configure menu, select IP .

Step 20

On the IP page, enter the following settings.

Field

Setting

Client IP Address

Enter the new IP address you want to use for the PIMG unit.

(This is the IP address that you enter in Cisco Unity Connection Administration when you create the integration.)

Client Subnet Mask

Enter the new subnet mask, if the subnet mask is different from the default IP address.

Default Network Gateway Address

Enter the IP address of the default network gateway router that the PIMG units use.

BOOTP Enabled

Select No .

Step 21

Select Apply Changes .

Step 22

On the Configure menu, select Tones .

Step 23

On the Tones page, select the Learn tab.

Destination addresses cannot be duplicated in the same session. Otherwise, the process for learning tones cannot succeed.
                                             If you do not have enough available phones to learn all the tones at one time, you can run multiple sessions to learn tones
                                             individually by checking or unchecking the applicable Acquire Tone check boxes.

Step 24

On the Tones page, for the Dialtone event, confirm that the Acquire Tone check box is checked and leave the Destination Address
                                          field blank.

Step 25

On the Tones page, for the Busy Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                          to verify that the tone is correct.

From a available phone, call a second phone.

Answer the second phone when it rings, and leave both handsets off so that both phones are busy.

From a third phone, dial one of the busy phones.

Confirm that you hear a busy tone.

Hang up the third phone but leave the handsets for the other two phones off.

Step 26

On the Tones page, in the Destination Address field for Busy Tone, enter the extension that you dialed in Step 25 c. from the third phone.

Step 27

On the Tones page, for the Error/Reorder Tone event, confirm that the Acquire Tone check box is checked and do the following
                                          substeps to verify that the tone is correct.

From an available phone, dial an extension that does not exist.

Confirm that you hear the reorder or error tone.

Hang up the phone.

Step 28

On the Tones page, in the Destination Address field for Error/Reorder Tone, enter the extension that you dialed in Step 27 a.

Step 29

On the Tones page, for the Ringback Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                          to verify that the tone is correct.

From an available phone, dial an extension that does exist

Confirm that you hear the ringback tone.

Hang up the phone.

Step 30

On the Tones page, in the Destination Address field for Ringback Tone, enter the extension that you dialed in Step 29 a.

Step 31

Select Learn .

When running learn tones, the PIMG unit restarts after learning the first tone.

Step 32

When the process is complete, check the check box for each newly learned tone and select Apply .

Step 33

Hang up the phones that you used in Step 25 .

Step 34

On the Configure menu, select Restart .

Step 35

On the Restart page, select Restart Unit Now .

Step 36

When the PIMG unit has restarted, in the View menu, select Refresh .

Step 37

Repeat Step 1 through Step 36 on all remaining PIMG units.

### Analog PIMG Settings for DTMF Integration (Firmware Version 5.x)

Do the following steps to set up the analog PIMG units for a DTMF integration

### SUMMARY STEPS

- On a Windows workstation, sign in to a PIMG unit.

- On the Configure menu, select System .

- On the System page, enter the following settings.

- Select Apply Changes .

- On the Configure menu, select Gateway .

- On the Gateway page, select the Gateway Routing tab.

- On the Gateway Routing tab, Unity Connection without a cluster, skip to Step 8 . If Unity Connection has a cluster configured, do the following substeps:

- Under VoIP Endpoint ID, enter the following settings.

- Select Apply Changes .

- Select the Gateway Advanced tab.

- On the Gateway Advanced tab, enter the following settings.

- Select Apply Changes .

- Select the Gateway Capabilities tab.

- Depending on how you have planned to use the voice messaging ports, select the applicable setting for each port in the Telephony
                                 Port Capability column.

- Select Apply Changes .

- On the Configure menu, select SIP .

- On the SIP page, enter the following settings.

- Select Apply Changes .

- On the Configure menu, select IP .

- On the IP page, enter the following settings.

- Select Apply Changes .

- On the Configure menu, select Tones .

- On the Tones page, select the Learn tab.

- On the Tones page, for the Dialtone event, confirm that the Acquire Tone check box is checked and leave the Destination Address
                                 field blank.

- On the Tones page, for the Busy Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                 to verify that the tone is correct.

- On the Tones page, in the Destination Address field for Busy Tone, enter the extension that you dialed in Step 25 c. from the third phone.

- On the Tones page, for the Error/Reorder Tone event, confirm that the Acquire Tone check box is checked and do the following
                                 substeps to verify that the tone is correct.

- On the Tones page, in the Destination Address field for Error/Reorder Tone, enter the extension that you dialed in Step 27 a.

- On the Tones page, for the Ringback Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                 to verify that the tone is correct.

- On the Tones page, in the Destination Address field for Ringback Tone, enter the extension that you dialed in Step 29 a.

- Select Learn .

- When the process is complete, check the check box for each newly learned tone and select Apply .

- Hang up the phones that you used in Step 25 .

- On the Configure menu, select Restart .

- On the Restart page, select Restart Unit Now .

- When the PIMG unit has restarted, in the View menu, select Refresh .

- Repeat Step 1 through Step 36 on all remaining PIMG units.

### DETAILED STEPS

Step 1

On a Windows workstation, sign in to a PIMG unit.

Step 2

On the Configure menu, select System .

Step 3

On the System page, enter the following settings.

Field

Settings

Operating Mode

Select SIP .

PBX Type

Select None .

PCM Coding

Select uLaw .

Step 4

Select Apply Changes .

Step 5

On the Configure menu, select Gateway .

Step 6

On the Gateway page, select the Gateway Routing tab.

Step 7

On the Gateway Routing tab, Unity Connection without a cluster, skip to Step 8 . If Unity Connection has a cluster configured, do the following substeps:

In the Fault Tolerance Enabled field, select Yes .

In the Load Balancing Enabled field, select No.

Step 8

Under VoIP Endpoint ID, enter the following settings.

To add endpoints, select Add New Endpoint .

Count

VoIP Endpoint ID

1

(Unity Connection without a cluster) Enter the server name of the Unity Connection server.

(Unity Connection with a cluster configured) Enter the server name of the subscriber server.

2

(Unity Connection without a cluster) Enter the server name of the Unity Connection server.

(Unity Connection with a cluster configured) Enter the server name of the publisher server.

Step 9

Select Apply Changes .

Step 10

Select the Gateway Advanced tab.

Step 11

On the Gateway Advanced tab, enter the following settings.

Field

Settings

Call Connect Mode

Select OnAnswer .

Destination for Unroutable IP Calls

Leave this field blank.

Destination for Unroutable PBX Calls

Leave this field blank.

Monitor Call Connections

Select No .

Minimum Call Party Delay (msecs)

Enter 500 .

Maximum Call Party Delay (msecs)

Enter 2000 .

Dial Digit on Time (msecs)

Enter 100 .

Dial Inter-Digit Time (msecs)

Enter 100 .

Dial Pause Time (msecs)

Enter 2000 .

Turn MWI On FAC

Enter the code that turns MWIs on.

Turn MWI Off FAC

Enter the code that turns MWIs off.

Outbound Call Connect Timeout (msecs)

Enter 10000 .

Wait for Ringback/Connect on Blind Transfer

Select Yes .

Hunt Group Extension

Enter the pilot number of the Unity Connection voice messaging ports.

Audio Compression

Select the preferred codec for audio compression:

G.711

G.729AB

RTP Digit Relay Mode

Select RFC2833 .

Signaling Digit Relay Mode

Select Off .

Voice Activity Detection

Select Off .

Frame Size

Select the applicable setting:

G.711— 20

G.729AB— 10

Failure to use the correct setting results in recorded messages containing nothing but silence.

Frames Per Packet

Select the applicable setting:

G.711— 1

G.729AB— 2

Failure to use the correct setting results in recorded messages containing nothing but silence.

Call Control QOS Byte

Enter 104 (equivalent to DSCP AF31).

RTP QOS Byte

Enter 184 (equivalent to DSCP EF).

SNMP Traps Enabled

Select No .

E-mail Alarms Enabled

Select No .

Step 12

Select Apply Changes .

Step 13

Select the Gateway Capabilities tab.

Step 14

Depending on how you have planned to use the voice messaging ports, select the applicable setting for each port in the Telephony
                                          Port Capability column.

Telephony Port Capability Settings

Voice Messaging Port Usage

Calls-Only

The port answers incoming calls only and cannot dial out (for example, to set MWIs or send message notifications).

MWIs-Only

The port dial out only (for example, to set MWIs or send message notifications) and cannot answer incoming calls.

Both

The port answers incoming calls and also dial out (for example, to set MWIs or send message notifications).

In setting up the PIMG unit, do not send calls to ports in Unity Connection that cannot answer calls (voice messaging ports
                                             that are not set to Answer Calls). For example, if a voice messaging port is set only to Send MWI Requests, do not send calls
                                             to it. Otherwise the integration cannot function correctly.

If a port in Unity Connection is disabled, select No in the Telephony Port Enabled column for the corresponding port on this tab. Note that changing a setting in the Telephony
                                             Port Enabled column requires restarting the PIMG unit.

Step 15

Select Apply Changes .

Step 16

On the Configure menu, select SIP .

Step 17

On the SIP page, enter the following settings.

Field

Settings

Host and Domain Name

Enter the domain name of the PIMG unit.

Server Port

Enter 5060 .

Transport Type

Select UDP .

Call as Domain Name

Select No .

Registration Server Address

Leave this field blank.

Registration Server Port

Enter 5060 .

Registration Expiration (sec)

Enter 3600 .

Primary Proxy Server Address

Leave this field blank.

Primary Proxy Server Port

Not applicable. Leave the default setting.

Backup Proxy Server Address

Not applicable. Leave the default setting.

Backup Proxy Server Port

Not applicable. Leave the default setting.

Proxy Query Interval

Enter 10 .

T1 Time (msecs)

Enter 400 .

T2 Time (msecs)

Enter 3000 .

Invite Expiration (sec)

Enter 120 .

Step 18

Select Apply Changes .

Step 19

On the Configure menu, select IP .

Step 20

On the IP page, enter the following settings.

Field

Settings

Client IP Address

Enter the new IP address you want to use for the PIMG unit.

(This is the IP address that you enter in Cisco Unity Connection Administration when you create the integration.)

Client Subnet Mask

Enter the new subnet mask, if the subnet mask is different from the default IP address.

Default Network Gateway Address

Enter the IP address of the default network gateway router that the PIMG units use.

BOOTP Enabled

Select No .

Step 21

Select Apply Changes .

Step 22

On the Configure menu, select Tones .

Step 23

On the Tones page, select the Learn tab.

Destination addresses cannot be duplicated in the same session. Otherwise, the process for learning tones cannot succeed.
                                             If you do not have enough available phones to learn all the tones at one time, you can run multiple sessions to learn tones
                                             individually by checking or unchecking the applicable Acquire Tone check boxes.

Step 24

On the Tones page, for the Dialtone event, confirm that the Acquire Tone check box is checked and leave the Destination Address
                                          field blank.

Step 25

On the Tones page, for the Busy Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                          to verify that the tone is correct.

From an available phone, call a second phone.

Answer the second phone when it rings, and leave both handsets off so that both phones are busy.

From a third phone, dial one of the busy phones.

Confirm that you hear a busy tone.

Hang up the third phone but leave the handsets for the other two phones off.

Step 26

On the Tones page, in the Destination Address field for Busy Tone, enter the extension that you dialed in Step 25 c. from the third phone.

Step 27

On the Tones page, for the Error/Reorder Tone event, confirm that the Acquire Tone check box is checked and do the following
                                          substeps to verify that the tone is correct.

From an available phone, dial an extension that does not exist.

Confirm that you hear the reorder or error tone.

Hang up the phone.

Step 28

On the Tones page, in the Destination Address field for Error/Reorder Tone, enter the extension that you dialed in Step 27 a.

Step 29

On the Tones page, for the Ringback Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                          to verify that the tone is correct.

From an available phone, dial an extension that does exist

Confirm that you hear the ringback tone.

Hang up the phone.

Step 30

On the Tones page, in the Destination Address field for Ringback Tone, enter the extension that you dialed in Step 29 a.

Step 31

Select Learn .

When running learn tones, the PIMG unit restarts after learning the first tone.

Step 32

When the process is complete, check the check box for each newly learned tone and select Apply .

Step 33

Hang up the phones that you used in Step 25 .

Step 34

On the Configure menu, select Restart .

Step 35

On the Restart page, select Restart Unit Now .

Step 36

When the PIMG unit has restarted, in the View menu, select Refresh .

Step 37

Repeat Step 1 through Step 36 on all remaining PIMG units.

### Analog PIMG Settings for Serial Integration (Firmware Version 5.x)

Do the following steps to set up the analog PIMG units for a Serial integration

### SUMMARY STEPS

- On a Windows workstation, sign in to a PIMG unit.

- On the Configure menu, select System .

- On the System page, enter the following settings.

- Select Apply Changes .

- On the Configure menu, select Gateway .

- On the Gateway page, select the Gateway Routing tab.

- On the Gateway Routing tab, Unity Connection without a cluster, skip to Step 8 . If Unity Connection has a cluster configured, do the following substeps:

- Under VoIP Endpoint ID, enter the following settings.

- Select Apply Changes .

- Select the Gateway Advanced tab.

- On the Gateway Advanced tab, enter the following settings.

- Select Apply Changes .

- Select the Gateway Capabilities tab.

- Depending on how you have planned to use the voice messaging ports, select the applicable setting for each port in the Telephony
                                 Port Capability column.

- Select Apply Changes .

- On the Configure menu, select Serial Protocol .

- On the Serial Protocol page, enter the following settings.

- Select Apply Changes .

- On the Configure menu, select SIP .

- On the SIP page, enter the following settings.

- Select Apply Changes .

- On the Configure menu, select IP .

- On the IP page, enter the following settings.

- Select Apply Changes .

- On the Configure menu, select Tones .

- On the Tones page, select the Learn tab.

- On the Tones page, for the Dialtone event, confirm that the Acquire Tone check box is checked and leave the Destination Address
                                 field blank.

- On the Tones page, for the Busy Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                 to verify that the tone is correct.

- On the Tones page, in the Destination Address field for Busy Tone, enter the extension that you dialed in Step 28 c. from the third phone.

- On the Tones page, for the Error/Reorder Tone event, confirm that the Acquire Tone check box is checked and do the following
                                 substeps to verify that the tone is correct.

- On the Tones page, in the Destination Address field for Error/Reorder Tone, enter the extension that you dialed in Step 30 a.

- On the Tones page, for the Ringback Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                 to verify that the tone is correct.

- On the Tones page, in the Destination Address field for Ringback Tone, enter the extension that you dialed in Step 32 a.

- Select Learn .

- When the process is complete, check the check box for each newly learned tone and select Apply .

- Hang up the phones that you used in Step 28 .

- On the Configure menu, select Restart .

- On the Restart page, select Restart Unit Now .

- When the PIMG unit has restarted, in the View menu, select Refresh .

- Repeat Step 1 through Step 39 on all remaining PIMG units.

### DETAILED STEPS

Step 1

On a Windows workstation, sign in to a PIMG unit.

Step 2

On the Configure menu, select System .

Step 3

On the System page, enter the following settings.

Field

Setting

Operating Mode

Select SIP .

PCM Coding

Select uLaw .

Serial Port Baud Rate

Select the setting that is configured on the phone system.

The default setting is 9600.

Serial Port Parity

Select the setting that is configured on the phone system.

The default setting is None.

Serial Port Data Bits

Select the setting that is configured on the phone system.

The default setting is 8.

Serial Port Stop Bits

Select the setting that is configured on the phone system.

The default setting is 1.

Step 4

Select Apply Changes .

Step 5

On the Configure menu, select Gateway .

Step 6

On the Gateway page, select the Gateway Routing tab.

Step 7

On the Gateway Routing tab, Unity Connection without a cluster, skip to Step 8 . If Unity Connection has a cluster configured, do the following substeps:

In the Fault Tolerance Enabled field, select Yes .

In the Load Balancing Enabled field, select No.

Step 8

Under VoIP Endpoint ID, enter the following settings.

To add endpoints, select Add New Endpoint .

Count

VoIP Endpoint ID

1

(Unity Connection without a cluster) Enter the server name of the Unity Connection server.

(Unity Connection with a cluster configured) Enter the server name of the subscriber server.

2

(Unity Connection without a cluster) Enter the server name of the Unity Connection server.

(Unity Connection with a cluster configured) Enter the server name of the publisher server.

Step 9

Select Apply Changes .

Step 10

Select the Gateway Advanced tab.

Step 11

On the Gateway Advanced tab, enter the following settings.

Field

Settings

Advanced Call Routing

Call Connect Mode

Select OnAnswer .

Destination for Unroutable IP Calls

Leave this field blank.

Destination for Unroutable PBX Calls

Leave this field blank.

Monitor Call Connections

Select No .

Telephony

Minimum Call Party Delay

Enter 500 .

Maximum Call Party Delay

Enter 2000 .

Dial Digit on Time

Enter 100 .

Dial Inter-Digit Time

Enter 100 .

Dial Pause Time

Enter 2000 .

Turn MWI On FAC

Leave this field blank.

Turn MWI Off FAC

Leave this field blank.

Outbound Call Connect Timeout

Enter 10000 .

Wait for Ringback/Connect on Blind Transfer

Select Yes .

Hunt Group Extension

Enter the pilot number of the Unity Connection voice messaging ports.

Audio

Audio Compression

Select the preferred codec for audio compression:

G.711

G.729AB

RTP Digit Relay Mode

Select RFC2833 .

Signaling Digit Relay Mode

Select Off .

Voice Activity Detection

Select Off .

Frame Size

Select the applicable setting:

G.711— 20

G.729AB— 10

Failure to use the correct setting results in recorded messages containing nothing but silence.

Frames Per Packet

Select the applicable setting:

G.711— 1

G.729AB— 2

Failure to use the correct setting results in recorded messages containing nothing but silence.

Quality of Service

Call Control QOS Byte

Enter 104 (equivalent to DSCP AF31).

RTP QOS Byte

Enter 184 (equivalent to DSCP EF).

Traps and Alarms

E-mail Alarms Enabled

Select No .

SNMP Traps Enabled

Select No .

Step 12

Select Apply Changes .

Step 13

Select the Gateway Capabilities tab.

Step 14

Depending on how you have planned to use the voice messaging ports, select the applicable setting for each port in the Telephony
                                          Port Capability column.

Telephony Port Capability Settings

Voice Messaging Port Usage

Calls-Only

The port answers incoming calls only and cannot dial out (for example, to set MWIs or send message notifications).

MWIs-Only

The port dial out only (for example, to set MWIs or send message notifications) and cannot answer incoming calls.

Both

The port answers incoming calls and also dial out (for example, to set MWIs or send message notifications).

In setting up the PIMG unit, do not send calls to ports in Unity Connection that cannot answer calls (voice messaging ports
                                             that are not set to Answer Calls). For example, if a voice messaging port is set only to Send MWI Requests, do not send calls
                                             to it. Otherwise the integration cannot function correctly.

If a port in Unity Connection is disabled, select No in the Telephony Port Enabled column for the corresponding port on this tab. Note that changing a setting in the Telephony
                                             Port Enabled column requires restarting the PIMG unit.

Step 15

Select Apply Changes .

Step 16

On the Configure menu, select Serial Protocol .

Step 17

On the Serial Protocol page, enter the following settings.

Field

Setting

Serial Mode

Select the applicable setting:

Master —Select this setting when this PIMG unit is connected to the data link serial cable from the phone system. There can be only
                                                               one master PIMG unit in a phone system integration.

Slave —Select this setting when this PIMG unit is not connected to the data link serial cable from the phone system. There can be
                                                               multiple slave PIMG units in a phone system integration.

Serial Interface Protocol

Select the serial protocol that your phone system uses:

SMDI

MCI

MD-110

Cpid Len

Select the applicable setting. Typically, the settings are 7 or 10.

Cpid Padding String

Enter the applicable string or leave this field blank. Typically, the setting is one of the following:

A string of zeros, where the number of zeros matches the setting of the Cpid Len field.

A prefix that is provided by the Centrex service.

Voice Mail Port Len

If the setting of the Serial Interface Protocol field is MD-110, enter 2 . Otherwise, accept the default of 7 .

System Number

Enter the applicable setting. Typically, the setting is 1.

MWI Response Timeout

Enter 2000 .

IP Address of Serial Server

If the PIMG unit is the master, leave this field blank.

If the PIMG unit is a slave, enter the IP address of the master PIMG unit (the PIMG unit that is connected to the data link
                                                         serial cable from the phone system).

Serial Cpid Expiration

Enter 2000 .

Logical Extension Number

If the setting of the Serial Interface Protocol field is MCI or MD-110, enter the extension number for each port on the PIMG
                                                         unit.

If the setting of the Serial Interface Protocol field is SMDI, enter the logical port number. Typically, the setting is 1
                                                         for port 1, 2 for port 2, and so on beginning with the master PIMG unit and continuing through each of the slave PIMG units.

Step 18

Select Apply Changes .

Step 19

On the Configure menu, select SIP .

Step 20

On the SIP page, enter the following settings.

Field

Setting

Host and Domain Name

Enter the domain name of the PIMG unit.

This setting must match the name of the port group in Cisco Unity Connection Administration that has the voice messaging ports
                                                         connecting to the PIMG unit.

Server Port

Enter 5060 .

Primary Proxy Server Address

Leave this field blank.

Primary Proxy Server Port

Not applicable. Leave the default setting.

Backup Proxy Server Address

Not applicable. Leave the default setting.

Backup Proxy Server Port

Not applicable. Leave the default setting.

Proxy Query Interval

Enter 10 .

T1 Time

Enter 400 .

T2 Time

Enter 3000 .

Step 21

Select Apply Changes .

Step 22

On the Configure menu, select IP .

Step 23

On the IP page, enter the following settings.

Field

Setting

Client IP Address

Enter the new IP address you want to use for the PIMG unit.

(This is the IP address that you enter in Cisco Unity Connection Administration when you create the integration.)

Client Subnet Mask

Enter the new subnet mask, if the subnet mask is different from the default IP address.

Default Network Gateway Address

Enter the IP address of the default network gateway router that the PIMG units use.

BOOTP Enabled

Select No .

Step 24

Select Apply Changes .

Step 25

On the Configure menu, select Tones .

Step 26

On the Tones page, select the Learn tab.

Destination addresses cannot be duplicated in the same session. Otherwise, the process for learning tones do not succeed.
                                             If you do not have enough available phones to learn all the tones at one time, you can run multiple sessions to learn tones
                                             individually by checking or unchecking the applicable Acquire Tone check boxes.

Step 27

On the Tones page, for the Dialtone event, confirm that the Acquire Tone check box is checked and leave the Destination Address
                                          field blank.

Step 28

On the Tones page, for the Busy Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                          to verify that the tone is correct.

From a available phone, call a second phone.

Answer the second phone when it rings, and leave both handsets off so that both phones are busy.

From a third phone, dial one of the busy phones.

Confirm that you hear a busy tone.

Hang up the third phone but leave the handsets for the other two phones off.

Step 29

On the Tones page, in the Destination Address field for Busy Tone, enter the extension that you dialed in Step 28 c. from the third phone.

Step 30

On the Tones page, for the Error/Reorder Tone event, confirm that the Acquire Tone check box is checked and do the following
                                          substeps to verify that the tone is correct.

From an available phone, dial an extension that does not exist.

Confirm that you hear the reorder or error tone.

Hang up the phone.

Step 31

On the Tones page, in the Destination Address field for Error/Reorder Tone, enter the extension that you dialed in Step 30 a.

Step 32

On the Tones page, for the Ringback Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                          to verify that the tone is correct.

From an available phone, dial an extension that does exist.

Confirm that you hear the ringback tone.

Hang up the phone.

Step 33

On the Tones page, in the Destination Address field for Ringback Tone, enter the extension that you dialed in Step 32 a.

Step 34

Select Learn .

When running learn tones, the PIMG unit restarts after learning the first tone.

Step 35

When the process is complete, check the check box for each newly learned tone and select Apply .

Step 36

Hang up the phones that you used in Step 28 .

Step 37

On the Configure menu, select Restart .

Step 38

On the Restart page, select Restart Unit Now .

Step 39

When the PIMG unit has restarted, in the View menu, select Refresh .

Step 40

Repeat Step 1 through Step 39 on all remaining PIMG units.

### Digital Mitel PIMG Settings (Firmware Version 5.x)

Do the following steps to set up the digital Mitel PIMG units

### SUMMARY STEPS

- On a Windows workstation, sign in to a PIMG unit.

- On the Configure menu, select System .

- On the System page, enter the following settings.

- Select Apply Changes .

- On the Configure menu, select Gateway .

- On the Gateway page, select the Gateway Routing tab.

- On the Gateway Routing tab, Unity Connection without a cluster, skip to Step 8 . If Unity Connection has a cluster configured, do the following substeps:

- Under VoIP Endpoint ID, enter the following settings.

- Select Apply Changes .

- Select the Gateway Advanced tab.

- On the Gateway Advanced tab, enter the following settings.

- Select Apply Changes .

- Select the Gateway Capabilities tab.

- Depending on how you have planned to use the voice messaging ports, select the applicable setting for each port in the Telephony
                                 Port Capability column.

- Select Apply Changes .

- On the Configure menu, select SIP .

- On the SIP page, enter the following settings.

- Select Apply Changes .

- On the Configure menu, select IP .

- On the IP page, enter the following settings.

- Select Apply Changes .

- On the Configure menu, select Tones .

- On the Tones page, select the Learn tab.

- On the Tones page, for the Dialtone event, confirm that the Acquire Tone check box is checked and leave the Destination Address
                                 field blank.

- On the Tones page, for the Busy Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                 to verify that the tone is correct.

- On the Tones page, in the Destination Address field for Busy Tone, enter the extension that you dialed in Step 25 c. from the third phone.

- On the Tones page, for the Error/Reorder Tone event, confirm that the Acquire Tone check box is checked and do the following
                                 substeps to verify that the tone is correct.

- On the Tones page, in the Destination Address field for Error/Reorder Tone, enter the extension that you dialed in Step 27 a.

- On the Tones page, for the Ringback Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                 to verify that the tone is correct.

- On the Tones page, in the Destination Address field for Ringback Tone, enter the extension that you dialed in Step 29 a.

- Select Learn .

- When the process is complete, check the check box for each newly learned tone and select Apply .

- Hang up the phones that you used in Step 25 .

- On the Configure menu, select Restart .

- On the Restart page, select Restart Unit Now .

- When the PIMG unit has restarted, in the View menu, select Refresh .

- Repeat Step 1 through Step 36 on all remaining PIMG units.

### DETAILED STEPS

Step 1

On a Windows workstation, sign in to a PIMG unit.

Step 2

On the Configure menu, select System .

Step 3

On the System page, enter the following settings.

Field

Setting

Operating Mode

Select SIP .

PBX Type

(This setting does not apply.)

PCM Coding

Select uLaw .

Step 4

Select Apply Changes .

Step 5

On the Configure menu, select Gateway .

Step 6

On the Gateway page, select the Gateway Routing tab.

Step 7

On the Gateway Routing tab, Unity Connection without a cluster, skip to Step 8 . If Unity Connection has a cluster configured, do the following substeps:

In the Fault Tolerance Enabled field, select Yes .

In the Load Balancing Enabled field, select No.

Step 8

Under VoIP Endpoint ID, enter the following settings.

To add endpoints, select Add New Endpoint .

Count

VoIP Endpoint ID

1

(Unity Connection without a cluster) Enter the server name of the Unity Connection server.

(Unity Connection with a cluster configured) Enter the server name of the subscriber server.

2

(Unity Connection without a cluster) Enter the server name of the Unity Connection server.

(Unity Connection with a cluster configured) Enter the server name of the publisher server.

Step 9

Select Apply Changes .

Step 10

Select the Gateway Advanced tab.

Step 11

On the Gateway Advanced tab, enter the following settings.

Field

Settings

Call Connect Mode

Select OnAnswer .

Destination for Unroutable PBX Calls

Enter the extension of an attendant who receive calls to Unity Connection that are unanswered.

Minimum Call Party Delay (msecs)

Enter 500 .

Turn MWI On FAC

Enter the code that turns MWIs on.

Turn MWI Off FAC

Enter the code that turns MWIs off.

Wait for Ringback/Connect on Blind Transfer

Select Yes .

Hunt Group Extension

Enter the pilot number of the Unity Connection voice messaging ports.

Audio Compression

Select the preferred codec for audio compression:

G.711

G.729AB

Signaling Digit Relay Mode

Select Off .

Voice Activity Detection

Select Off .

Frame Size

Select the applicable setting:

G.711— 20

G.729AB— 10

Failure to use the correct setting results in recorded messages containing nothing but silence.

Frames Per Packet

Select the applicable setting:

G.711— 1

G.729AB— 2

Failure to use the correct setting results in recorded messages containing nothing but silence.

Call Control QOS Byte

Enter 104 (equivalent to DSCP AF31).

RTP QOS Byte

Enter 184 (equivalent to DSCP EF).

Step 12

Select Apply Changes .

Step 13

Select the Gateway Capabilities tab.

Step 14

Depending on how you have planned to use the voice messaging ports, select the applicable setting for each port in the Telephony
                                          Port Capability column.

Telephony Port Capability Settings

Voice Messaging Port Usage

Calls-Only

The port answer incoming calls only and cannot dial out (for example, to set MWIs or send message notifications).

MWIs-Only

The port dial out only (for example, to set MWIs or send message notifications) and cannot answer incoming calls.

Both

The port answers incoming calls and also dial out (for example, to set MWIs or send message notifications).

In setting up the PIMG unit, do not send calls to ports in Unity Connection that cannot answer calls (voice messaging ports
                                             that are not set to Answer Calls). For example, if a voice messaging port is set only to Send MWI Requests, do not send calls
                                             to it. Otherwise the integration cannot function correctly.

If a port in Unity Connection is disabled, select No in the Telephony Port Enabled column for the corresponding port on this tab. Note that changing a setting in the Telephony
                                             Port Enabled column requires restarting the PIMG unit.

Step 15

Select Apply Changes .

Step 16

On the Configure menu, select SIP .

Step 17

On the SIP page, enter the following settings.

Field

Setting

Host and Domain Name

Enter the domain name of the PIMG unit.

Server Port

Enter 5060 .

Primary Proxy Server Address

Leave this field blank.

Primary Proxy Server Port

Not applicable. Leave the default setting.

Backup Proxy Server Address

Not applicable. Leave the default setting.

Backup Proxy Server Port

Not applicable. Leave the default setting.

Proxy Query Interval

Enter 10 .

T1 Time

Enter 400 .

T2 Time

Enter 3000 .

Step 18

Select Apply Changes .

Step 19

On the Configure menu, select IP .

Step 20

On the IP page, enter the following settings.

Field

Setting

Client IP Address

Enter the new IP address you want to use for the PIMG unit.

(This is the IP address that you enter in Cisco Unity Connection Administration when you create the integration.)

Client Subnet Mask

Enter the new subnet mask, if the subnet mask is different from the default IP address.

Default Network Gateway Address

Enter the IP address of the default network gateway router that the PIMG units use.

BOOTP Enabled

Select No .

Step 21

Select Apply Changes .

Step 22

On the Configure menu, select Tones .

Step 23

On the Tones page, select the Learn tab.

Destination addresses cannot be duplicated in the same session. Otherwise, the process for learning tones cannot succeed.
                                             If you do not have enough available phones to learn all the tones at one time, you can run multiple sessions to learn tones
                                             individually by checking or unchecking the applicable Acquire Tone check boxes.

Step 24

On the Tones page, for the Dialtone event, confirm that the Acquire Tone check box is checked and leave the Destination Address
                                          field blank.

Step 25

On the Tones page, for the Busy Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                          to verify that the tone is correct.

From a available phone, call a second phone.

Answer the second phone when it rings, and leave both handsets off so that both phones are busy.

From a third phone, dial one of the busy phones.

Confirm that you hear a busy tone.

Hang up the third phone but leave the handsets for the other two phones off.

Step 26

On the Tones page, in the Destination Address field for Busy Tone, enter the extension that you dialed in Step 25 c. from the third phone.

Step 27

On the Tones page, for the Error/Reorder Tone event, confirm that the Acquire Tone check box is checked and do the following
                                          substeps to verify that the tone is correct.

From an available phone, dial an extension that does not exist.

Confirm that you hear the reorder or error tone.

Hang up the phone.

Step 28

On the Tones page, in the Destination Address field for Error/Reorder Tone, enter the extension that you dialed in Step 27 a.

Step 29

On the Tones page, for the Ringback Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                          to verify that the tone is correct.

From an available phone, dial an extension that does exist.

Confirm that you hear the ringback tone.

Hang up the phone.

Step 30

On the Tones page, in the Destination Address field for Ringback Tone, enter the extension that you dialed in Step 29 a.

Step 31

Select Learn .

When running learn tones, the PIMG unit restarts after learning the first tone.

Step 32

When the process is complete, check the check box for each newly learned tone and select Apply .

Step 33

Hang up the phones that you used in Step 25 .

Step 34

On the Configure menu, select Restart .

Step 35

On the Restart page, select Restart Unit Now .

Step 36

When the PIMG unit has restarted, in the View menu, select Refresh .

Step 37

Repeat Step 1 through Step 36 on all remaining PIMG units.

### Digital Rolm PIMG Settings (Firmware Version 5.x)

Do the following steps to set up the digital Rolm PIMG units

### SUMMARY STEPS

- On a Windows workstation, sign in to a PIMG unit.

- On the Configure menu, select System .

- On the System page, enter the following settings.

- Select Apply Changes .

- On the Configure menu, select Gateway .

- On the Gateway page, select the Gateway Routing tab.

- On the Gateway Routing tab, Unity Connection without a cluster, skip to Step 8 . If Unity Connection has a cluster configured, do the following substeps:

- Under VoIP Endpoint ID, enter the following settings.

- Select Apply Changes .

- Select the Gateway Advanced tab.

- On the Gateway Advanced tab, enter the following settings.

- Select Apply Changes .

- Select the Gateway Capabilities tab.

- Depending on how you have planned to use the voice messaging ports, select the applicable setting for each port in the Telephony
                                 Port Capability column.

- Select Apply Changes .

- On the Configure menu, select SIP .

- On the SIP page, enter the following settings.

- Select Apply Changes .

- On the Configure menu, select IP .

- On the IP page, enter the following settings.

- Select Apply Changes .

- On the Configure menu, select Tones .

- On the Tones page, select the Learn tab.

- On the Tones page, for the Dialtone event, confirm that the Acquire Tone check box is checked and leave the Destination Address
                                 field blank.

- On the Tones page, for the Busy Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                 to verify that the tone is correct.

- On the Tones page, in the Destination Address field for Busy Tone, enter the extension that you dialed in Step 25 c. from the third phone.

- On the Tones page, for the Error/Reorder Tone event, confirm that the Acquire Tone check box is checked and do the following
                                 substeps to verify that the tone is correct.

- On the Tones page, in the Destination Address field for Error/Reorder Tone, enter the extension that you dialed in Step 27 a.

- On the Tones page, for the Ringback Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                 to verify that the tone is correct.

- On the Tones page, in the Destination Address field for Ringback Tone, enter the extension that you dialed in Step 29 a.

- Select Learn .

- When the process is complete, check the check box for each newly learned tone and select Apply .

- Hang up the phones that you used in Step 25 .

- On the Configure menu, select Restart .

- On the Restart page, select Restart Unit Now .

- When the PIMG unit has restarted, in the View menu, select Refresh .

- Repeat Step 1 through Step 36 on all remaining PIMG units.

### DETAILED STEPS

Step 1

On a Windows workstation, sign in to a PIMG unit.

Step 2

On the Configure menu, select System .

Step 3

On the System page, enter the following settings.

Field

Setting

Operating Mode

Select SIP .

PBX Type

Depending on your phone system, select one of the following:

Rolm_9751_SW9005

Rolm_9751_SW9006

PCM Coding

Select uLaw .

Step 4

Select Apply Changes .

Step 5

On the Configure menu, select Gateway .

Step 6

On the Gateway page, select the Gateway Routing tab.

Step 7

On the Gateway Routing tab, Unity Connection without a cluster, skip to Step 8 . If Unity Connection has a cluster configured, do the following substeps:

In the Fault Tolerance Enabled field, select Yes .

In the Load Balancing Enabled field, select No.

Step 8

Under VoIP Endpoint ID, enter the following settings.

To add endpoints, select Add New Endpoint .

Count

VoIP Endpoint ID

1

(Unity Connection without a cluster) Enter the server name of the Unity Connection server.

(Unity Connection with a cluster configured) Enter the server name of the subscriber server.

2

(Unity Connection without a cluster) Enter the server name of the Unity Connection server.

(Unity Connection with a cluster configured) Enter the server name of the publisher server.

Step 9

Select Apply Changes .

Step 10

Select the Gateway Advanced tab.

Step 11

On the Gateway Advanced tab, enter the following settings.

Field

Settings

Call Connect Mode

Select OnAnswer .

Destination for Unroutable PBX Calls

Enter the extension of an attendant who receives calls to Unity Connection that are unanswered.

Minimum Call Party Delay (msecs)

Enter 500 .

Turn MWI On FAC

Leave this field blank.

Turn MWI Off FAC

Leave this field blank.

Wait for Ringback/Connect on Blind Transfer

Select Yes .

Hunt Group Extension

Enter the pilot number of the Unity Connection voice messaging ports.

Audio Compression

Select the preferred codec for audio compression:

G.711

G.729AB

Signaling Digit Relay Mode

Select Off .

Voice Activity Detection

Select Off .

Frame Size

Select the applicable setting:

G.711— 20

G.729AB— 10

Failure to use the correct setting results in recorded messages containing nothing but silence.

Frames Per Packet

Select the applicable setting:

G.711— 1

G.729AB— 2

Failure to use the correct setting results in recorded messages containing nothing but silence.

Call Control QOS Byte

Enter 104 (equivalent to DSCP AF31).

RTP QOS Byte

Enter 184 (equivalent to DSCP EF).

Step 12

Select Apply Changes .

Step 13

Select the Gateway Capabilities tab.

Step 14

Depending on how you have planned to use the voice messaging ports, select the applicable setting for each port in the Telephony
                                          Port Capability column.

Telephony Port Capability Settings

Voice Messaging Port Usage

Calls-Only

The port answers incoming calls only and cannot dial out (for example, to set MWIs or send message notifications).

MWIs-Only

The port dial out only (for example, to set MWIs or send message notifications) and cannot answer incoming calls.

Both

The port answers incoming calls and also dial out (for example, to set MWIs or send message notifications).

In setting up the PIMG unit, do not send calls to ports in Unity Connection that cannot answer calls (voice messaging ports
                                             that are not set to Answer Calls). For example, if a voice messaging port is set only to Send MWI Requests, do not send calls
                                             to it. Otherwise the integration cannot function correctly.

If a port in Unity Connection is disabled, select No in the Telephony Port Enabled column for the corresponding port on this tab. Note that changing a setting in the Telephony
                                             Port Enabled column requires restarting the PIMG unit.

Step 15

Select Apply Changes .

Step 16

On the Configure menu, select SIP .

Step 17

On the SIP page, enter the following settings.

Field

Setting

Host and Domain Name

Enter the domain name of the PIMG unit.

Server Port

Enter 5060 .

Primary Proxy Server Address

Leave this field blank.

Primary Proxy Server Port

Not applicable. Leave the default setting.

Backup Proxy Server Address

Not applicable. Leave the default setting.

Backup Proxy Server Port

Not applicable. Leave the default setting.

Proxy Query Interval

Enter 10 .

T1 Time

Enter 400 .

T2 Time

Enter 3000 .

Step 18

Select Apply Changes .

Step 19

On the Configure menu, select IP .

Step 20

On the IP page, enter the following settings.

Field

Setting

Client IP Address

Enter the new IP address you want to use for the PIMG unit.

(This is the IP address that you enter in Cisco Unity Connection Administration when you create the integration.)

Client Subnet Mask

Enter the new subnet mask, if the subnet mask is different from the default IP address.

Default Network Gateway Address

Enter the IP address of the default network gateway router that the PIMG units use.

BOOTP Enabled

Select No .

Step 21

Select Apply Changes .

Step 22

On the Configure menu, select Tones .

Step 23

On the Tones page, select the Learn tab.

Destination addresses cannot be duplicated in the same session. Otherwise, the process for learning tones cannot succeed.
                                             If you do not have enough available phones to learn all the tones at one time, you can run multiple sessions to learn tones
                                             individually by checking or unchecking the applicable Acquire Tone check boxes.

Step 24

On the Tones page, for the Dialtone event, confirm that the Acquire Tone check box is checked and leave the Destination Address
                                          field blank.

Step 25

On the Tones page, for the Busy Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                          to verify that the tone is correct.

From a available phone, call a second phone.

Answer the second phone when it rings, and leave both handsets off so that both phones are busy.

From a third phone, dial one of the busy phones.

Confirm that you hear a busy tone.

Hang up the third phone but leave the handsets for the other two phones off.

Step 26

On the Tones page, in the Destination Address field for Busy Tone, enter the extension that you dialed in Step 25 c. from the third phone.

Step 27

On the Tones page, for the Error/Reorder Tone event, confirm that the Acquire Tone check box is checked and do the following
                                          substeps to verify that the tone is correct.

From an available phone, dial an extension that does not exist.

Confirm that you hear the reorder or error tone.

Hang up the phone.

Step 28

On the Tones page, in the Destination Address field for Error/Reorder Tone, enter the extension that you dialed in Step 27 a.

Step 29

On the Tones page, for the Ringback Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                          to verify that the tone is correct.

From an available phone, dial an extension that does exist.

Confirm that you hear the ringback tone.

Hang up the phone.

Step 30

On the Tones page, in the Destination Address field for Ringback Tone, enter the extension that you dialed in Step 29 a.

Step 31

Select Learn .

When running learn tones, the PIMG unit restarts after learning the first tone.

Step 32

When the process is complete, check the check box for each newly learned tone and select Apply .

Step 33

Hang up the phones that you used in Step 25 .

Step 34

On the Configure menu, select Restart .

Step 35

On the Restart page, select Restart Unit Now .

Step 36

When the PIMG unit has restarted, in the View menu, select Refresh .

Step 37

Repeat Step 1 through Step 36 on all remaining PIMG units.

| Step 1 | On a Windows workstation, sign in to a PIMG unit. |
|---|---|
| Step 2 | In the Configure menu, select System . |
| Step 3 | On the System page, enter the following settings. Table 1. System Page Settings Field Setting Operating Mode Select SIP . PBX Type Select the applicable setting: For Avaya phone systems, select Lucent . For NEC phone systems, select NEC_NEAX . For Nortel phone systems, select M1 . For Siemens phone systems, select Optiset_300ECS . PCM Coding Select uLaw . | Field | Setting | Operating Mode | Select SIP . | PBX Type | Select the applicable setting: For Avaya phone systems, select Lucent . For NEC phone systems, select NEC_NEAX . For Nortel phone systems, select M1 . For Siemens phone systems, select Optiset_300ECS . | PCM Coding | Select uLaw . |
| Field | Setting |
| Operating Mode | Select SIP . |
| PBX Type | Select the applicable setting: For Avaya phone systems, select Lucent . For NEC phone systems, select NEC_NEAX . For Nortel phone systems, select M1 . For Siemens phone systems, select Optiset_300ECS . |
| PCM Coding | Select uLaw . |
| Step 4 | Select Apply Changes . |
| Step 5 | On the Configure menu, select Gateway . |
| Step 6 | On the Gateway page, select the Gateway Routing tab. |
| Step 7 | On the Gateway Routing tab, Unity Connection without a cluster, skip to Step 8 . If Unity Connection has a cluster configured, do the following substeps: In the Fault Tolerance Enabled field, select Yes . In the Load Balancing Enabled field, select No. |
| Step 8 | Under VoIP Endpoint ID, enter the following settings. Note To add endpoints, select Add New Endpoint . Table 2. Gateway Routing Tab Settings Count VoIP Endpoint ID 1 (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the subscriber Unity Connection server. 2 (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the publisher server. | Note | To add endpoints, select Add New Endpoint . | Count | VoIP Endpoint ID | 1 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the subscriber Unity Connection server. | 2 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the publisher server. |
| Note | To add endpoints, select Add New Endpoint . |
| Count | VoIP Endpoint ID |
| 1 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the subscriber Unity Connection server. |
| 2 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the publisher server. |
| Step 9 | Select Apply Changes . |
| Step 10 | Select the Gateway Advanced tab. |
| Step 11 | On the Gateway Advanced tab, enter the following settings. Table 3. Gateway Advanced Tab Settings Field Settings Call Connect Mode Select OnAnswer . Destination for Unroutable PBX Calls Enter the extension of an attendant who receives calls to Cisco Unity Connection that are unanswered. Minimum Call Party Delay (msecs) Enter 500 . Turn MWI On FAC For Siemens Hicom 300 E (North American) phone systems, enter Enter #*1 . Otherwise, leave this field blank. Turn MWI Off FAC For Siemens Hicom 300 ECS phone systems, enter Enter #*8 . Otherwise, leave this field blank. Wait for Ringback/Connect on Blind Transfer Select Yes . Hunt Group Extension Enter the pilot number of the Unity Connection voice messaging ports. Audio Compression Select the preferred codec for audio compression: G.711 G.729AB Signaling Digit Relay Mode Select Off . Voice Activity Detection Select Off . Frame Size Select the applicable setting: G.711— 20 G.729AB— 10 Failure to use the correct setting results in recorded messages containing nothing but silence. Frames Per Packet Select the applicable setting: G.711— 1 G.729AB— 2 Failure to use the correct setting results in recorded messages containing nothing but silence. Call Control QOS Byte Enter 104 (equivalent to DSCP AF31). RTP QOS Byte Enter 184 (equivalent to DSCP EF). | Field | Settings | Call Connect Mode | Select OnAnswer . | Destination for Unroutable PBX Calls | Enter the extension of an attendant who receives calls to Cisco Unity Connection that are unanswered. | Minimum Call Party Delay (msecs) | Enter 500 . | Turn MWI On FAC | For Siemens Hicom 300 E (North American) phone systems, enter Enter #*1 . Otherwise, leave this field blank. | Turn MWI Off FAC | For Siemens Hicom 300 ECS phone systems, enter Enter #*8 . Otherwise, leave this field blank. | Wait for Ringback/Connect on Blind Transfer | Select Yes . | Hunt Group Extension | Enter the pilot number of the Unity Connection voice messaging ports. | Audio Compression | Select the preferred codec for audio compression: G.711 G.729AB | Signaling Digit Relay Mode | Select Off . | Voice Activity Detection | Select Off . | Frame Size | Select the applicable setting: G.711— 20 G.729AB— 10 Failure to use the correct setting results in recorded messages containing nothing but silence. | Frames Per Packet | Select the applicable setting: G.711— 1 G.729AB— 2 Failure to use the correct setting results in recorded messages containing nothing but silence. | Call Control QOS Byte | Enter 104 (equivalent to DSCP AF31). | RTP QOS Byte | Enter 184 (equivalent to DSCP EF). |
| Field | Settings |
| Call Connect Mode | Select OnAnswer . |
| Destination for Unroutable PBX Calls | Enter the extension of an attendant who receives calls to Cisco Unity Connection that are unanswered. |
| Minimum Call Party Delay (msecs) | Enter 500 . |
| Turn MWI On FAC | For Siemens Hicom 300 E (North American) phone systems, enter Enter #*1 . Otherwise, leave this field blank. |
| Turn MWI Off FAC | For Siemens Hicom 300 ECS phone systems, enter Enter #*8 . Otherwise, leave this field blank. |
| Wait for Ringback/Connect on Blind Transfer | Select Yes . |
| Hunt Group Extension | Enter the pilot number of the Unity Connection voice messaging ports. |
| Audio Compression | Select the preferred codec for audio compression: G.711 G.729AB |
| Signaling Digit Relay Mode | Select Off . |
| Voice Activity Detection | Select Off . |
| Frame Size | Select the applicable setting: G.711— 20 G.729AB— 10 Failure to use the correct setting results in recorded messages containing nothing but silence. |
| Frames Per Packet | Select the applicable setting: G.711— 1 G.729AB— 2 Failure to use the correct setting results in recorded messages containing nothing but silence. |
| Call Control QOS Byte | Enter 104 (equivalent to DSCP AF31). |
| RTP QOS Byte | Enter 184 (equivalent to DSCP EF). |
| Step 12 | Select Apply Changes . |
| Step 13 | Select the Gateway Capabilities tab. |
| Step 14 | Depending on how you have planned to use the voice messaging ports, select the applicable setting for each port in the Telephony
                                          Port Capability column. Table 4. Gateway Capabilities Tab Settings Telephony Port Capability Settings Voice Messaging Port Usage Calls-Only The port answers incoming calls only and cannot dial out (for example, to set MWIs or send message notifications). MWIs-Only The port dial out only (for example, to set MWIs or send message notifications) and cannot answer incoming calls. Both The port answers incoming calls and also dial out (for example, to set MWIs or send message notifications). In setting up the PIMG unit, do not send calls to ports in Unity Connection that cannot answer calls (voice messaging ports
                                             that are not set to Answer Calls). For example, if a voice messaging port is set only to Send MWI Requests, do not send calls
                                             to it. Otherwise the integration cannot function correctly. If a port in Unity Connection is disabled, select No in the Telephony Port Enabled column for the corresponding port on this tab. Note that changing a setting in the Telephony
                                             Port Enabled column requires restarting the PIMG unit. | Telephony Port Capability Settings | Voice Messaging Port Usage | Calls-Only | The port answers incoming calls only and cannot dial out (for example, to set MWIs or send message notifications). | MWIs-Only | The port dial out only (for example, to set MWIs or send message notifications) and cannot answer incoming calls. | Both | The port answers incoming calls and also dial out (for example, to set MWIs or send message notifications). |
| Telephony Port Capability Settings | Voice Messaging Port Usage |
| Calls-Only | The port answers incoming calls only and cannot dial out (for example, to set MWIs or send message notifications). |
| MWIs-Only | The port dial out only (for example, to set MWIs or send message notifications) and cannot answer incoming calls. |
| Both | The port answers incoming calls and also dial out (for example, to set MWIs or send message notifications). |
| Step 15 | Select Apply Changes . |
| Step 16 | On the Configure menu, select SIP . |
| Step 17 | On the SIP page, enter the following settings. Table 5. SIP Page Settings Field Setting Host and Domain Name Enter the domain name of the PIMG unit. Server Port Enter 5060 . Primary Proxy Server Address Leave this field blank. Primary Proxy Server Port Not applicable. Leave the default setting. Backup Proxy Server Address Not applicable. Leave the default setting. Backup Proxy Server Port Not applicable. Leave the default setting. Proxy Query Interval Enter 10 . T1 Time Enter 400 . T2 Time Enter 3000 . | Field | Setting | Host and Domain Name | Enter the domain name of the PIMG unit. | Server Port | Enter 5060 . | Primary Proxy Server Address | Leave this field blank. | Primary Proxy Server Port | Not applicable. Leave the default setting. | Backup Proxy Server Address | Not applicable. Leave the default setting. | Backup Proxy Server Port | Not applicable. Leave the default setting. | Proxy Query Interval | Enter 10 . | T1 Time | Enter 400 . | T2 Time | Enter 3000 . |
| Field | Setting |
| Host and Domain Name | Enter the domain name of the PIMG unit. |
| Server Port | Enter 5060 . |
| Primary Proxy Server Address | Leave this field blank. |
| Primary Proxy Server Port | Not applicable. Leave the default setting. |
| Backup Proxy Server Address | Not applicable. Leave the default setting. |
| Backup Proxy Server Port | Not applicable. Leave the default setting. |
| Proxy Query Interval | Enter 10 . |
| T1 Time | Enter 400 . |
| T2 Time | Enter 3000 . |
| Step 18 | Select Apply Changes . |
| Step 19 | On the Configure menu, select IP . |
| Step 20 | On the IP page, enter the following settings. Table 6. IP Page Settings Field Setting Client IP Address Enter the new IP address you want to use for the PIMG unit. (This is the IP address that you enter in Cisco Unity Connection Administration when you create the integration.) Client Subnet Mask Enter the new subnet mask, if the subnet mask is different from the default IP address. Default Network Gateway Address Enter the IP address of the default network gateway router that the PIMG units use. BOOTP Enabled Select No . | Field | Setting | Client IP Address | Enter the new IP address you want to use for the PIMG unit. (This is the IP address that you enter in Cisco Unity Connection Administration when you create the integration.) | Client Subnet Mask | Enter the new subnet mask, if the subnet mask is different from the default IP address. | Default Network Gateway Address | Enter the IP address of the default network gateway router that the PIMG units use. | BOOTP Enabled | Select No . |
| Field | Setting |
| Client IP Address | Enter the new IP address you want to use for the PIMG unit. (This is the IP address that you enter in Cisco Unity Connection Administration when you create the integration.) |
| Client Subnet Mask | Enter the new subnet mask, if the subnet mask is different from the default IP address. |
| Default Network Gateway Address | Enter the IP address of the default network gateway router that the PIMG units use. |
| BOOTP Enabled | Select No . |
| Step 21 | Select Apply Changes . |
| Step 22 | On the Configure menu, select Tones . |
| Step 23 | On the Tones page, select the Learn tab. Destination addresses cannot be duplicated in the same session. Otherwise, the process for learning tones cannot succeed.
                                             If you do not have enough available phones to learn all the tones at one time, you can run multiple sessions to learn tones
                                             individually by checking or unchecking the applicable Acquire Tone check boxes. |
| Step 24 | On the Tones page, for the Dialtone event, confirm that the Acquire Tone check box is checked and leave the Destination Address
                                          field blank. |
| Step 25 | On the Tones page, for the Busy Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                          to verify that the tone is correct. From a available phone, call a second phone. Answer the second phone when it rings, and leave both handsets off so that both phones are busy. From a third phone, dial one of the busy phones. Confirm that you hear a busy tone. Hang up the third phone but leave the handsets for the other two phones off. |
| Step 26 | On the Tones page, in the Destination Address field for Busy Tone, enter the extension that you dialed in Step 25 c. from the third phone. |
| Step 27 | On the Tones page, for the Error/Reorder Tone event, confirm that the Acquire Tone check box is checked and do the following
                                          substeps to verify that the tone is correct. From an available phone, dial an extension that does not exist. Confirm that you hear the reorder or error tone. Hang up the phone. |
| Step 28 | On the Tones page, in the Destination Address field for Error/Reorder Tone, enter the extension that you dialed in Step 27 a. |
| Step 29 | On the Tones page, for the Ringback Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                          to verify that the tone is correct. From an available phone, dial an extension that does exist Confirm that you hear the ringback tone. Hang up the phone. |
| Step 30 | On the Tones page, in the Destination Address field for Ringback Tone, enter the extension that you dialed in Step 29 a. |
| Step 31 | Select Learn . Note When running learn tones, the PIMG unit restarts after learning the first tone. | Note | When running learn tones, the PIMG unit restarts after learning the first tone. |
| Note | When running learn tones, the PIMG unit restarts after learning the first tone. |
| Step 32 | When the process is complete, check the check box for each newly learned tone and select Apply . |
| Step 33 | Hang up the phones that you used in Step 25 . |
| Step 34 | On the Configure menu, select Restart . |
| Step 35 | On the Restart page, select Restart Unit Now . |
| Step 36 | When the PIMG unit has restarted, in the View menu, select Refresh . |
| Step 37 | Repeat Step 1 through Step 36 on all remaining PIMG units. |

| Field | Setting |
|---|---|
| Operating Mode | Select SIP . |
| PBX Type | Select the applicable setting: For Avaya phone systems, select Lucent . For NEC phone systems, select NEC_NEAX . For Nortel phone systems, select M1 . For Siemens phone systems, select Optiset_300ECS . |
| PCM Coding | Select uLaw . |

| Note | To add endpoints, select Add New Endpoint . |
|---|---|

| Count | VoIP Endpoint ID |
|---|---|
| 1 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the subscriber Unity Connection server. |
| 2 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the publisher server. |

| Field | Settings |
|---|---|
| Call Connect Mode | Select OnAnswer . |
| Destination for Unroutable PBX Calls | Enter the extension of an attendant who receives calls to Cisco Unity Connection that are unanswered. |
| Minimum Call Party Delay (msecs) | Enter 500 . |
| Turn MWI On FAC | For Siemens Hicom 300 E (North American) phone systems, enter Enter #*1 . Otherwise, leave this field blank. |
| Turn MWI Off FAC | For Siemens Hicom 300 ECS phone systems, enter Enter #*8 . Otherwise, leave this field blank. |
| Wait for Ringback/Connect on Blind Transfer | Select Yes . |
| Hunt Group Extension | Enter the pilot number of the Unity Connection voice messaging ports. |
| Audio Compression | Select the preferred codec for audio compression: G.711 G.729AB |
| Signaling Digit Relay Mode | Select Off . |
| Voice Activity Detection | Select Off . |
| Frame Size | Select the applicable setting: G.711— 20 G.729AB— 10 Failure to use the correct setting results in recorded messages containing nothing but silence. |
| Frames Per Packet | Select the applicable setting: G.711— 1 G.729AB— 2 Failure to use the correct setting results in recorded messages containing nothing but silence. |
| Call Control QOS Byte | Enter 104 (equivalent to DSCP AF31). |
| RTP QOS Byte | Enter 184 (equivalent to DSCP EF). |

| Telephony Port Capability Settings | Voice Messaging Port Usage |
|---|---|
| Calls-Only | The port answers incoming calls only and cannot dial out (for example, to set MWIs or send message notifications). |
| MWIs-Only | The port dial out only (for example, to set MWIs or send message notifications) and cannot answer incoming calls. |
| Both | The port answers incoming calls and also dial out (for example, to set MWIs or send message notifications). |

| Field | Setting |
|---|---|
| Host and Domain Name | Enter the domain name of the PIMG unit. |
| Server Port | Enter 5060 . |
| Primary Proxy Server Address | Leave this field blank. |
| Primary Proxy Server Port | Not applicable. Leave the default setting. |
| Backup Proxy Server Address | Not applicable. Leave the default setting. |
| Backup Proxy Server Port | Not applicable. Leave the default setting. |
| Proxy Query Interval | Enter 10 . |
| T1 Time | Enter 400 . |
| T2 Time | Enter 3000 . |

| Field | Setting |
|---|---|
| Client IP Address | Enter the new IP address you want to use for the PIMG unit. (This is the IP address that you enter in Cisco Unity Connection Administration when you create the integration.) |
| Client Subnet Mask | Enter the new subnet mask, if the subnet mask is different from the default IP address. |
| Default Network Gateway Address | Enter the IP address of the default network gateway router that the PIMG units use. |
| BOOTP Enabled | Select No . |

| Note | When running learn tones, the PIMG unit restarts after learning the first tone. |
|---|---|

| Step 1 | On a Windows workstation, sign in to a PIMG unit. |
|---|---|
| Step 2 | On the Configure menu, select System . |
| Step 3 | On the System page, enter the following settings. Table 7. System Page Settings Field Settings Operating Mode Select SIP . PBX Type Select None . PCM Coding Select uLaw . | Field | Settings | Operating Mode | Select SIP . | PBX Type | Select None . | PCM Coding | Select uLaw . |
| Field | Settings |
| Operating Mode | Select SIP . |
| PBX Type | Select None . |
| PCM Coding | Select uLaw . |
| Step 4 | Select Apply Changes . |
| Step 5 | On the Configure menu, select Gateway . |
| Step 6 | On the Gateway page, select the Gateway Routing tab. |
| Step 7 | On the Gateway Routing tab, Unity Connection without a cluster, skip to Step 8 . If Unity Connection has a cluster configured, do the following substeps: In the Fault Tolerance Enabled field, select Yes . In the Load Balancing Enabled field, select No. |
| Step 8 | Under VoIP Endpoint ID, enter the following settings. Note To add endpoints, select Add New Endpoint . Table 8. Gateway Routing Tab Settings Count VoIP Endpoint ID 1 (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the subscriber server. 2 (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the publisher server. | Note | To add endpoints, select Add New Endpoint . | Count | VoIP Endpoint ID | 1 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the subscriber server. | 2 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the publisher server. |
| Note | To add endpoints, select Add New Endpoint . |
| Count | VoIP Endpoint ID |
| 1 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the subscriber server. |
| 2 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the publisher server. |
| Step 9 | Select Apply Changes . |
| Step 10 | Select the Gateway Advanced tab. |
| Step 11 | On the Gateway Advanced tab, enter the following settings. Table 9. Gateway Advanced Tab Settings Field Settings Call Connect Mode Select OnAnswer . Destination for Unroutable IP Calls Leave this field blank. Destination for Unroutable PBX Calls Leave this field blank. Monitor Call Connections Select No . Minimum Call Party Delay (msecs) Enter 500 . Maximum Call Party Delay (msecs) Enter 2000 . Dial Digit on Time (msecs) Enter 100 . Dial Inter-Digit Time (msecs) Enter 100 . Dial Pause Time (msecs) Enter 2000 . Turn MWI On FAC Enter the code that turns MWIs on. Turn MWI Off FAC Enter the code that turns MWIs off. Outbound Call Connect Timeout (msecs) Enter 10000 . Wait for Ringback/Connect on Blind Transfer Select Yes . Hunt Group Extension Enter the pilot number of the Unity Connection voice messaging ports. Audio Compression Select the preferred codec for audio compression: G.711 G.729AB RTP Digit Relay Mode Select RFC2833 . Signaling Digit Relay Mode Select Off . Voice Activity Detection Select Off . Frame Size Select the applicable setting: G.711— 20 G.729AB— 10 Failure to use the correct setting results in recorded messages containing nothing but silence. Frames Per Packet Select the applicable setting: G.711— 1 G.729AB— 2 Failure to use the correct setting results in recorded messages containing nothing but silence. Call Control QOS Byte Enter 104 (equivalent to DSCP AF31). RTP QOS Byte Enter 184 (equivalent to DSCP EF). SNMP Traps Enabled Select No . E-mail Alarms Enabled Select No . | Field | Settings | Call Connect Mode | Select OnAnswer . | Destination for Unroutable IP Calls | Leave this field blank. | Destination for Unroutable PBX Calls | Leave this field blank. | Monitor Call Connections | Select No . | Minimum Call Party Delay (msecs) | Enter 500 . | Maximum Call Party Delay (msecs) | Enter 2000 . | Dial Digit on Time (msecs) | Enter 100 . | Dial Inter-Digit Time (msecs) | Enter 100 . | Dial Pause Time (msecs) | Enter 2000 . | Turn MWI On FAC | Enter the code that turns MWIs on. | Turn MWI Off FAC | Enter the code that turns MWIs off. | Outbound Call Connect Timeout (msecs) | Enter 10000 . | Wait for Ringback/Connect on Blind Transfer | Select Yes . | Hunt Group Extension | Enter the pilot number of the Unity Connection voice messaging ports. | Audio Compression | Select the preferred codec for audio compression: G.711 G.729AB | RTP Digit Relay Mode | Select RFC2833 . | Signaling Digit Relay Mode | Select Off . | Voice Activity Detection | Select Off . | Frame Size | Select the applicable setting: G.711— 20 G.729AB— 10 Failure to use the correct setting results in recorded messages containing nothing but silence. | Frames Per Packet | Select the applicable setting: G.711— 1 G.729AB— 2 Failure to use the correct setting results in recorded messages containing nothing but silence. | Call Control QOS Byte | Enter 104 (equivalent to DSCP AF31). | RTP QOS Byte | Enter 184 (equivalent to DSCP EF). | SNMP Traps Enabled | Select No . | E-mail Alarms Enabled | Select No . |
| Field | Settings |
| Call Connect Mode | Select OnAnswer . |
| Destination for Unroutable IP Calls | Leave this field blank. |
| Destination for Unroutable PBX Calls | Leave this field blank. |
| Monitor Call Connections | Select No . |
| Minimum Call Party Delay (msecs) | Enter 500 . |
| Maximum Call Party Delay (msecs) | Enter 2000 . |
| Dial Digit on Time (msecs) | Enter 100 . |
| Dial Inter-Digit Time (msecs) | Enter 100 . |
| Dial Pause Time (msecs) | Enter 2000 . |
| Turn MWI On FAC | Enter the code that turns MWIs on. |
| Turn MWI Off FAC | Enter the code that turns MWIs off. |
| Outbound Call Connect Timeout (msecs) | Enter 10000 . |
| Wait for Ringback/Connect on Blind Transfer | Select Yes . |
| Hunt Group Extension | Enter the pilot number of the Unity Connection voice messaging ports. |
| Audio Compression | Select the preferred codec for audio compression: G.711 G.729AB |
| RTP Digit Relay Mode | Select RFC2833 . |
| Signaling Digit Relay Mode | Select Off . |
| Voice Activity Detection | Select Off . |
| Frame Size | Select the applicable setting: G.711— 20 G.729AB— 10 Failure to use the correct setting results in recorded messages containing nothing but silence. |
| Frames Per Packet | Select the applicable setting: G.711— 1 G.729AB— 2 Failure to use the correct setting results in recorded messages containing nothing but silence. |
| Call Control QOS Byte | Enter 104 (equivalent to DSCP AF31). |
| RTP QOS Byte | Enter 184 (equivalent to DSCP EF). |
| SNMP Traps Enabled | Select No . |
| E-mail Alarms Enabled | Select No . |
| Step 12 | Select Apply Changes . |
| Step 13 | Select the Gateway Capabilities tab. |
| Step 14 | Depending on how you have planned to use the voice messaging ports, select the applicable setting for each port in the Telephony
                                          Port Capability column. Table 10. Gateway Capabilities Tab Settings Telephony Port Capability Settings Voice Messaging Port Usage Calls-Only The port answers incoming calls only and cannot dial out (for example, to set MWIs or send message notifications). MWIs-Only The port dial out only (for example, to set MWIs or send message notifications) and cannot answer incoming calls. Both The port answers incoming calls and also dial out (for example, to set MWIs or send message notifications). In setting up the PIMG unit, do not send calls to ports in Unity Connection that cannot answer calls (voice messaging ports
                                             that are not set to Answer Calls). For example, if a voice messaging port is set only to Send MWI Requests, do not send calls
                                             to it. Otherwise the integration cannot function correctly. If a port in Unity Connection is disabled, select No in the Telephony Port Enabled column for the corresponding port on this tab. Note that changing a setting in the Telephony
                                             Port Enabled column requires restarting the PIMG unit. | Telephony Port Capability Settings | Voice Messaging Port Usage | Calls-Only | The port answers incoming calls only and cannot dial out (for example, to set MWIs or send message notifications). | MWIs-Only | The port dial out only (for example, to set MWIs or send message notifications) and cannot answer incoming calls. | Both | The port answers incoming calls and also dial out (for example, to set MWIs or send message notifications). |
| Telephony Port Capability Settings | Voice Messaging Port Usage |
| Calls-Only | The port answers incoming calls only and cannot dial out (for example, to set MWIs or send message notifications). |
| MWIs-Only | The port dial out only (for example, to set MWIs or send message notifications) and cannot answer incoming calls. |
| Both | The port answers incoming calls and also dial out (for example, to set MWIs or send message notifications). |
| Step 15 | Select Apply Changes . |
| Step 16 | On the Configure menu, select SIP . |
| Step 17 | On the SIP page, enter the following settings. Table 11. SIP Page Settings Field Settings Host and Domain Name Enter the domain name of the PIMG unit. Server Port Enter 5060 . Transport Type Select UDP . Call as Domain Name Select No . Registration Server Address Leave this field blank. Registration Server Port Enter 5060 . Registration Expiration (sec) Enter 3600 . Primary Proxy Server Address Leave this field blank. Primary Proxy Server Port Not applicable. Leave the default setting. Backup Proxy Server Address Not applicable. Leave the default setting. Backup Proxy Server Port Not applicable. Leave the default setting. Proxy Query Interval Enter 10 . T1 Time (msecs) Enter 400 . T2 Time (msecs) Enter 3000 . Invite Expiration (sec) Enter 120 . | Field | Settings | Host and Domain Name | Enter the domain name of the PIMG unit. | Server Port | Enter 5060 . | Transport Type | Select UDP . | Call as Domain Name | Select No . | Registration Server Address | Leave this field blank. | Registration Server Port | Enter 5060 . | Registration Expiration (sec) | Enter 3600 . | Primary Proxy Server Address | Leave this field blank. | Primary Proxy Server Port | Not applicable. Leave the default setting. | Backup Proxy Server Address | Not applicable. Leave the default setting. | Backup Proxy Server Port | Not applicable. Leave the default setting. | Proxy Query Interval | Enter 10 . | T1 Time (msecs) | Enter 400 . | T2 Time (msecs) | Enter 3000 . | Invite Expiration (sec) | Enter 120 . |
| Field | Settings |
| Host and Domain Name | Enter the domain name of the PIMG unit. |
| Server Port | Enter 5060 . |
| Transport Type | Select UDP . |
| Call as Domain Name | Select No . |
| Registration Server Address | Leave this field blank. |
| Registration Server Port | Enter 5060 . |
| Registration Expiration (sec) | Enter 3600 . |
| Primary Proxy Server Address | Leave this field blank. |
| Primary Proxy Server Port | Not applicable. Leave the default setting. |
| Backup Proxy Server Address | Not applicable. Leave the default setting. |
| Backup Proxy Server Port | Not applicable. Leave the default setting. |
| Proxy Query Interval | Enter 10 . |
| T1 Time (msecs) | Enter 400 . |
| T2 Time (msecs) | Enter 3000 . |
| Invite Expiration (sec) | Enter 120 . |
| Step 18 | Select Apply Changes . |
| Step 19 | On the Configure menu, select IP . |
| Step 20 | On the IP page, enter the following settings. Table 12. IP Page Settings Field Settings Client IP Address Enter the new IP address you want to use for the PIMG unit. (This is the IP address that you enter in Cisco Unity Connection Administration when you create the integration.) Client Subnet Mask Enter the new subnet mask, if the subnet mask is different from the default IP address. Default Network Gateway Address Enter the IP address of the default network gateway router that the PIMG units use. BOOTP Enabled Select No . | Field | Settings | Client IP Address | Enter the new IP address you want to use for the PIMG unit. (This is the IP address that you enter in Cisco Unity Connection Administration when you create the integration.) | Client Subnet Mask | Enter the new subnet mask, if the subnet mask is different from the default IP address. | Default Network Gateway Address | Enter the IP address of the default network gateway router that the PIMG units use. | BOOTP Enabled | Select No . |
| Field | Settings |
| Client IP Address | Enter the new IP address you want to use for the PIMG unit. (This is the IP address that you enter in Cisco Unity Connection Administration when you create the integration.) |
| Client Subnet Mask | Enter the new subnet mask, if the subnet mask is different from the default IP address. |
| Default Network Gateway Address | Enter the IP address of the default network gateway router that the PIMG units use. |
| BOOTP Enabled | Select No . |
| Step 21 | Select Apply Changes . |
| Step 22 | On the Configure menu, select Tones . |
| Step 23 | On the Tones page, select the Learn tab. Destination addresses cannot be duplicated in the same session. Otherwise, the process for learning tones cannot succeed.
                                             If you do not have enough available phones to learn all the tones at one time, you can run multiple sessions to learn tones
                                             individually by checking or unchecking the applicable Acquire Tone check boxes. |
| Step 24 | On the Tones page, for the Dialtone event, confirm that the Acquire Tone check box is checked and leave the Destination Address
                                          field blank. |
| Step 25 | On the Tones page, for the Busy Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                          to verify that the tone is correct. From an available phone, call a second phone. Answer the second phone when it rings, and leave both handsets off so that both phones are busy. From a third phone, dial one of the busy phones. Confirm that you hear a busy tone. Hang up the third phone but leave the handsets for the other two phones off. |
| Step 26 | On the Tones page, in the Destination Address field for Busy Tone, enter the extension that you dialed in Step 25 c. from the third phone. |
| Step 27 | On the Tones page, for the Error/Reorder Tone event, confirm that the Acquire Tone check box is checked and do the following
                                          substeps to verify that the tone is correct. From an available phone, dial an extension that does not exist. Confirm that you hear the reorder or error tone. Hang up the phone. |
| Step 28 | On the Tones page, in the Destination Address field for Error/Reorder Tone, enter the extension that you dialed in Step 27 a. |
| Step 29 | On the Tones page, for the Ringback Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                          to verify that the tone is correct. From an available phone, dial an extension that does exist Confirm that you hear the ringback tone. Hang up the phone. |
| Step 30 | On the Tones page, in the Destination Address field for Ringback Tone, enter the extension that you dialed in Step 29 a. |
| Step 31 | Select Learn . Note When running learn tones, the PIMG unit restarts after learning the first tone. | Note | When running learn tones, the PIMG unit restarts after learning the first tone. |
| Note | When running learn tones, the PIMG unit restarts after learning the first tone. |
| Step 32 | When the process is complete, check the check box for each newly learned tone and select Apply . |
| Step 33 | Hang up the phones that you used in Step 25 . |
| Step 34 | On the Configure menu, select Restart . |
| Step 35 | On the Restart page, select Restart Unit Now . |
| Step 36 | When the PIMG unit has restarted, in the View menu, select Refresh . |
| Step 37 | Repeat Step 1 through Step 36 on all remaining PIMG units. |

| Field | Settings |
|---|---|
| Operating Mode | Select SIP . |
| PBX Type | Select None . |
| PCM Coding | Select uLaw . |

| Note | To add endpoints, select Add New Endpoint . |
|---|---|

| Count | VoIP Endpoint ID |
|---|---|
| 1 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the subscriber server. |
| 2 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the publisher server. |

| Field | Settings |
|---|---|
| Call Connect Mode | Select OnAnswer . |
| Destination for Unroutable IP Calls | Leave this field blank. |
| Destination for Unroutable PBX Calls | Leave this field blank. |
| Monitor Call Connections | Select No . |
| Minimum Call Party Delay (msecs) | Enter 500 . |
| Maximum Call Party Delay (msecs) | Enter 2000 . |
| Dial Digit on Time (msecs) | Enter 100 . |
| Dial Inter-Digit Time (msecs) | Enter 100 . |
| Dial Pause Time (msecs) | Enter 2000 . |
| Turn MWI On FAC | Enter the code that turns MWIs on. |
| Turn MWI Off FAC | Enter the code that turns MWIs off. |
| Outbound Call Connect Timeout (msecs) | Enter 10000 . |
| Wait for Ringback/Connect on Blind Transfer | Select Yes . |
| Hunt Group Extension | Enter the pilot number of the Unity Connection voice messaging ports. |
| Audio Compression | Select the preferred codec for audio compression: G.711 G.729AB |
| RTP Digit Relay Mode | Select RFC2833 . |
| Signaling Digit Relay Mode | Select Off . |
| Voice Activity Detection | Select Off . |
| Frame Size | Select the applicable setting: G.711— 20 G.729AB— 10 Failure to use the correct setting results in recorded messages containing nothing but silence. |
| Frames Per Packet | Select the applicable setting: G.711— 1 G.729AB— 2 Failure to use the correct setting results in recorded messages containing nothing but silence. |
| Call Control QOS Byte | Enter 104 (equivalent to DSCP AF31). |
| RTP QOS Byte | Enter 184 (equivalent to DSCP EF). |
| SNMP Traps Enabled | Select No . |
| E-mail Alarms Enabled | Select No . |

| Telephony Port Capability Settings | Voice Messaging Port Usage |
|---|---|
| Calls-Only | The port answers incoming calls only and cannot dial out (for example, to set MWIs or send message notifications). |
| MWIs-Only | The port dial out only (for example, to set MWIs or send message notifications) and cannot answer incoming calls. |
| Both | The port answers incoming calls and also dial out (for example, to set MWIs or send message notifications). |

| Field | Settings |
|---|---|
| Host and Domain Name | Enter the domain name of the PIMG unit. |
| Server Port | Enter 5060 . |
| Transport Type | Select UDP . |
| Call as Domain Name | Select No . |
| Registration Server Address | Leave this field blank. |
| Registration Server Port | Enter 5060 . |
| Registration Expiration (sec) | Enter 3600 . |
| Primary Proxy Server Address | Leave this field blank. |
| Primary Proxy Server Port | Not applicable. Leave the default setting. |
| Backup Proxy Server Address | Not applicable. Leave the default setting. |
| Backup Proxy Server Port | Not applicable. Leave the default setting. |
| Proxy Query Interval | Enter 10 . |
| T1 Time (msecs) | Enter 400 . |
| T2 Time (msecs) | Enter 3000 . |
| Invite Expiration (sec) | Enter 120 . |

| Field | Settings |
|---|---|
| Client IP Address | Enter the new IP address you want to use for the PIMG unit. (This is the IP address that you enter in Cisco Unity Connection Administration when you create the integration.) |
| Client Subnet Mask | Enter the new subnet mask, if the subnet mask is different from the default IP address. |
| Default Network Gateway Address | Enter the IP address of the default network gateway router that the PIMG units use. |
| BOOTP Enabled | Select No . |

| Note | When running learn tones, the PIMG unit restarts after learning the first tone. |
|---|---|

| Step 1 | On a Windows workstation, sign in to a PIMG unit. |
|---|---|
| Step 2 | On the Configure menu, select System . |
| Step 3 | On the System page, enter the following settings. Table 13. System Page Settings Field Setting Operating Mode Select SIP . PCM Coding Select uLaw . Serial Port Baud Rate Select the setting that is configured on the phone system. The default setting is 9600. Serial Port Parity Select the setting that is configured on the phone system. The default setting is None. Serial Port Data Bits Select the setting that is configured on the phone system. The default setting is 8. Serial Port Stop Bits Select the setting that is configured on the phone system. The default setting is 1. | Field | Setting | Operating Mode | Select SIP . | PCM Coding | Select uLaw . | Serial Port Baud Rate | Select the setting that is configured on the phone system. The default setting is 9600. | Serial Port Parity | Select the setting that is configured on the phone system. The default setting is None. | Serial Port Data Bits | Select the setting that is configured on the phone system. The default setting is 8. | Serial Port Stop Bits | Select the setting that is configured on the phone system. The default setting is 1. |
| Field | Setting |
| Operating Mode | Select SIP . |
| PCM Coding | Select uLaw . |
| Serial Port Baud Rate | Select the setting that is configured on the phone system. The default setting is 9600. |
| Serial Port Parity | Select the setting that is configured on the phone system. The default setting is None. |
| Serial Port Data Bits | Select the setting that is configured on the phone system. The default setting is 8. |
| Serial Port Stop Bits | Select the setting that is configured on the phone system. The default setting is 1. |
| Step 4 | Select Apply Changes . |
| Step 5 | On the Configure menu, select Gateway . |
| Step 6 | On the Gateway page, select the Gateway Routing tab. |
| Step 7 | On the Gateway Routing tab, Unity Connection without a cluster, skip to Step 8 . If Unity Connection has a cluster configured, do the following substeps: In the Fault Tolerance Enabled field, select Yes . In the Load Balancing Enabled field, select No. |
| Step 8 | Under VoIP Endpoint ID, enter the following settings. Note To add endpoints, select Add New Endpoint . Table 14. Gateway Routing Tab Settings Count VoIP Endpoint ID 1 (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the subscriber server. 2 (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the publisher server. | Note | To add endpoints, select Add New Endpoint . | Count | VoIP Endpoint ID | 1 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the subscriber server. | 2 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the publisher server. |
| Note | To add endpoints, select Add New Endpoint . |
| Count | VoIP Endpoint ID |
| 1 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the subscriber server. |
| 2 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the publisher server. |
| Step 9 | Select Apply Changes . |
| Step 10 | Select the Gateway Advanced tab. |
| Step 11 | On the Gateway Advanced tab, enter the following settings. Table 15. Gateway Advanced Tab Settings Field Settings Advanced Call Routing Call Connect Mode Select OnAnswer . Destination for Unroutable IP Calls Leave this field blank. Destination for Unroutable PBX Calls Leave this field blank. Monitor Call Connections Select No . Telephony Minimum Call Party Delay Enter 500 . Maximum Call Party Delay Enter 2000 . Dial Digit on Time Enter 100 . Dial Inter-Digit Time Enter 100 . Dial Pause Time Enter 2000 . Turn MWI On FAC Leave this field blank. Turn MWI Off FAC Leave this field blank. Outbound Call Connect Timeout Enter 10000 . Wait for Ringback/Connect on Blind Transfer Select Yes . Hunt Group Extension Enter the pilot number of the Unity Connection voice messaging ports. Audio Audio Compression Select the preferred codec for audio compression: G.711 G.729AB RTP Digit Relay Mode Select RFC2833 . Signaling Digit Relay Mode Select Off . Voice Activity Detection Select Off . Frame Size Select the applicable setting: G.711— 20 G.729AB— 10 Failure to use the correct setting results in recorded messages containing nothing but silence. Frames Per Packet Select the applicable setting: G.711— 1 G.729AB— 2 Failure to use the correct setting results in recorded messages containing nothing but silence. Quality of Service Call Control QOS Byte Enter 104 (equivalent to DSCP AF31). RTP QOS Byte Enter 184 (equivalent to DSCP EF). Traps and Alarms E-mail Alarms Enabled Select No . SNMP Traps Enabled Select No . | Field | Settings | Advanced Call Routing | Call Connect Mode | Select OnAnswer . | Destination for Unroutable IP Calls | Leave this field blank. | Destination for Unroutable PBX Calls | Leave this field blank. | Monitor Call Connections | Select No . | Telephony | Minimum Call Party Delay | Enter 500 . | Maximum Call Party Delay | Enter 2000 . | Dial Digit on Time | Enter 100 . | Dial Inter-Digit Time | Enter 100 . | Dial Pause Time | Enter 2000 . | Turn MWI On FAC | Leave this field blank. | Turn MWI Off FAC | Leave this field blank. | Outbound Call Connect Timeout | Enter 10000 . | Wait for Ringback/Connect on Blind Transfer | Select Yes . | Hunt Group Extension | Enter the pilot number of the Unity Connection voice messaging ports. | Audio | Audio Compression | Select the preferred codec for audio compression: G.711 G.729AB | RTP Digit Relay Mode | Select RFC2833 . | Signaling Digit Relay Mode | Select Off . | Voice Activity Detection | Select Off . | Frame Size | Select the applicable setting: G.711— 20 G.729AB— 10 Failure to use the correct setting results in recorded messages containing nothing but silence. | Frames Per Packet | Select the applicable setting: G.711— 1 G.729AB— 2 Failure to use the correct setting results in recorded messages containing nothing but silence. | Quality of Service | Call Control QOS Byte | Enter 104 (equivalent to DSCP AF31). | RTP QOS Byte | Enter 184 (equivalent to DSCP EF). | Traps and Alarms | E-mail Alarms Enabled | Select No . | SNMP Traps Enabled | Select No . |
| Field | Settings |
| Advanced Call Routing |
| Call Connect Mode | Select OnAnswer . |
| Destination for Unroutable IP Calls | Leave this field blank. |
| Destination for Unroutable PBX Calls | Leave this field blank. |
| Monitor Call Connections | Select No . |
| Telephony |
| Minimum Call Party Delay | Enter 500 . |
| Maximum Call Party Delay | Enter 2000 . |
| Dial Digit on Time | Enter 100 . |
| Dial Inter-Digit Time | Enter 100 . |
| Dial Pause Time | Enter 2000 . |
| Turn MWI On FAC | Leave this field blank. |
| Turn MWI Off FAC | Leave this field blank. |
| Outbound Call Connect Timeout | Enter 10000 . |
| Wait for Ringback/Connect on Blind Transfer | Select Yes . |
| Hunt Group Extension | Enter the pilot number of the Unity Connection voice messaging ports. |
| Audio |
| Audio Compression | Select the preferred codec for audio compression: G.711 G.729AB |
| RTP Digit Relay Mode | Select RFC2833 . |
| Signaling Digit Relay Mode | Select Off . |
| Voice Activity Detection | Select Off . |
| Frame Size | Select the applicable setting: G.711— 20 G.729AB— 10 Failure to use the correct setting results in recorded messages containing nothing but silence. |
| Frames Per Packet | Select the applicable setting: G.711— 1 G.729AB— 2 Failure to use the correct setting results in recorded messages containing nothing but silence. |
| Quality of Service |
| Call Control QOS Byte | Enter 104 (equivalent to DSCP AF31). |
| RTP QOS Byte | Enter 184 (equivalent to DSCP EF). |
| Traps and Alarms |
| E-mail Alarms Enabled | Select No . |
| SNMP Traps Enabled | Select No . |
| Step 12 | Select Apply Changes . |
| Step 13 | Select the Gateway Capabilities tab. |
| Step 14 | Depending on how you have planned to use the voice messaging ports, select the applicable setting for each port in the Telephony
                                          Port Capability column. Table 16. Gateway Capabilities Tab Settings Telephony Port Capability Settings Voice Messaging Port Usage Calls-Only The port answers incoming calls only and cannot dial out (for example, to set MWIs or send message notifications). MWIs-Only The port dial out only (for example, to set MWIs or send message notifications) and cannot answer incoming calls. Both The port answers incoming calls and also dial out (for example, to set MWIs or send message notifications). In setting up the PIMG unit, do not send calls to ports in Unity Connection that cannot answer calls (voice messaging ports
                                             that are not set to Answer Calls). For example, if a voice messaging port is set only to Send MWI Requests, do not send calls
                                             to it. Otherwise the integration cannot function correctly. If a port in Unity Connection is disabled, select No in the Telephony Port Enabled column for the corresponding port on this tab. Note that changing a setting in the Telephony
                                             Port Enabled column requires restarting the PIMG unit. | Telephony Port Capability Settings | Voice Messaging Port Usage | Calls-Only | The port answers incoming calls only and cannot dial out (for example, to set MWIs or send message notifications). | MWIs-Only | The port dial out only (for example, to set MWIs or send message notifications) and cannot answer incoming calls. | Both | The port answers incoming calls and also dial out (for example, to set MWIs or send message notifications). |
| Telephony Port Capability Settings | Voice Messaging Port Usage |
| Calls-Only | The port answers incoming calls only and cannot dial out (for example, to set MWIs or send message notifications). |
| MWIs-Only | The port dial out only (for example, to set MWIs or send message notifications) and cannot answer incoming calls. |
| Both | The port answers incoming calls and also dial out (for example, to set MWIs or send message notifications). |
| Step 15 | Select Apply Changes . |
| Step 16 | On the Configure menu, select Serial Protocol . |
| Step 17 | On the Serial Protocol page, enter the following settings. Table 17. Serial Protocol Page Settings Field Setting Serial Mode Select the applicable setting: Master —Select this setting when this PIMG unit is connected to the data link serial cable from the phone system. There can be only
                                                               one master PIMG unit in a phone system integration. Slave —Select this setting when this PIMG unit is not connected to the data link serial cable from the phone system. There can be
                                                               multiple slave PIMG units in a phone system integration. Serial Interface Protocol Select the serial protocol that your phone system uses: SMDI MCI MD-110 Cpid Len Select the applicable setting. Typically, the settings are 7 or 10. Cpid Padding String Enter the applicable string or leave this field blank. Typically, the setting is one of the following: A string of zeros, where the number of zeros matches the setting of the Cpid Len field. A prefix that is provided by the Centrex service. Voice Mail Port Len If the setting of the Serial Interface Protocol field is MD-110, enter 2 . Otherwise, accept the default of 7 . System Number Enter the applicable setting. Typically, the setting is 1. MWI Response Timeout Enter 2000 . IP Address of Serial Server If the PIMG unit is the master, leave this field blank. If the PIMG unit is a slave, enter the IP address of the master PIMG unit (the PIMG unit that is connected to the data link
                                                         serial cable from the phone system). Serial Cpid Expiration Enter 2000 . Logical Extension Number If the setting of the Serial Interface Protocol field is MCI or MD-110, enter the extension number for each port on the PIMG
                                                         unit. If the setting of the Serial Interface Protocol field is SMDI, enter the logical port number. Typically, the setting is 1
                                                         for port 1, 2 for port 2, and so on beginning with the master PIMG unit and continuing through each of the slave PIMG units. | Field | Setting | Serial Mode | Select the applicable setting: Master —Select this setting when this PIMG unit is connected to the data link serial cable from the phone system. There can be only
                                                               one master PIMG unit in a phone system integration. Slave —Select this setting when this PIMG unit is not connected to the data link serial cable from the phone system. There can be
                                                               multiple slave PIMG units in a phone system integration. | Serial Interface Protocol | Select the serial protocol that your phone system uses: SMDI MCI MD-110 | Cpid Len | Select the applicable setting. Typically, the settings are 7 or 10. | Cpid Padding String | Enter the applicable string or leave this field blank. Typically, the setting is one of the following: A string of zeros, where the number of zeros matches the setting of the Cpid Len field. A prefix that is provided by the Centrex service. | Voice Mail Port Len | If the setting of the Serial Interface Protocol field is MD-110, enter 2 . Otherwise, accept the default of 7 . | System Number | Enter the applicable setting. Typically, the setting is 1. | MWI Response Timeout | Enter 2000 . | IP Address of Serial Server | If the PIMG unit is the master, leave this field blank. If the PIMG unit is a slave, enter the IP address of the master PIMG unit (the PIMG unit that is connected to the data link
                                                         serial cable from the phone system). | Serial Cpid Expiration | Enter 2000 . | Logical Extension Number | If the setting of the Serial Interface Protocol field is MCI or MD-110, enter the extension number for each port on the PIMG
                                                         unit. If the setting of the Serial Interface Protocol field is SMDI, enter the logical port number. Typically, the setting is 1
                                                         for port 1, 2 for port 2, and so on beginning with the master PIMG unit and continuing through each of the slave PIMG units. |
| Field | Setting |
| Serial Mode | Select the applicable setting: Master —Select this setting when this PIMG unit is connected to the data link serial cable from the phone system. There can be only
                                                               one master PIMG unit in a phone system integration. Slave —Select this setting when this PIMG unit is not connected to the data link serial cable from the phone system. There can be
                                                               multiple slave PIMG units in a phone system integration. |
| Serial Interface Protocol | Select the serial protocol that your phone system uses: SMDI MCI MD-110 |
| Cpid Len | Select the applicable setting. Typically, the settings are 7 or 10. |
| Cpid Padding String | Enter the applicable string or leave this field blank. Typically, the setting is one of the following: A string of zeros, where the number of zeros matches the setting of the Cpid Len field. A prefix that is provided by the Centrex service. |
| Voice Mail Port Len | If the setting of the Serial Interface Protocol field is MD-110, enter 2 . Otherwise, accept the default of 7 . |
| System Number | Enter the applicable setting. Typically, the setting is 1. |
| MWI Response Timeout | Enter 2000 . |
| IP Address of Serial Server | If the PIMG unit is the master, leave this field blank. If the PIMG unit is a slave, enter the IP address of the master PIMG unit (the PIMG unit that is connected to the data link
                                                         serial cable from the phone system). |
| Serial Cpid Expiration | Enter 2000 . |
| Logical Extension Number | If the setting of the Serial Interface Protocol field is MCI or MD-110, enter the extension number for each port on the PIMG
                                                         unit. If the setting of the Serial Interface Protocol field is SMDI, enter the logical port number. Typically, the setting is 1
                                                         for port 1, 2 for port 2, and so on beginning with the master PIMG unit and continuing through each of the slave PIMG units. |
| Step 18 | Select Apply Changes . |
| Step 19 | On the Configure menu, select SIP . |
| Step 20 | On the SIP page, enter the following settings. Table 18. SIP Page Settings Field Setting Host and Domain Name Enter the domain name of the PIMG unit. This setting must match the name of the port group in Cisco Unity Connection Administration that has the voice messaging ports
                                                         connecting to the PIMG unit. Server Port Enter 5060 . Primary Proxy Server Address Leave this field blank. Primary Proxy Server Port Not applicable. Leave the default setting. Backup Proxy Server Address Not applicable. Leave the default setting. Backup Proxy Server Port Not applicable. Leave the default setting. Proxy Query Interval Enter 10 . T1 Time Enter 400 . T2 Time Enter 3000 . | Field | Setting | Host and Domain Name | Enter the domain name of the PIMG unit. This setting must match the name of the port group in Cisco Unity Connection Administration that has the voice messaging ports
                                                         connecting to the PIMG unit. | Server Port | Enter 5060 . | Primary Proxy Server Address | Leave this field blank. | Primary Proxy Server Port | Not applicable. Leave the default setting. | Backup Proxy Server Address | Not applicable. Leave the default setting. | Backup Proxy Server Port | Not applicable. Leave the default setting. | Proxy Query Interval | Enter 10 . | T1 Time | Enter 400 . | T2 Time | Enter 3000 . |
| Field | Setting |
| Host and Domain Name | Enter the domain name of the PIMG unit. This setting must match the name of the port group in Cisco Unity Connection Administration that has the voice messaging ports
                                                         connecting to the PIMG unit. |
| Server Port | Enter 5060 . |
| Primary Proxy Server Address | Leave this field blank. |
| Primary Proxy Server Port | Not applicable. Leave the default setting. |
| Backup Proxy Server Address | Not applicable. Leave the default setting. |
| Backup Proxy Server Port | Not applicable. Leave the default setting. |
| Proxy Query Interval | Enter 10 . |
| T1 Time | Enter 400 . |
| T2 Time | Enter 3000 . |
| Step 21 | Select Apply Changes . |
| Step 22 | On the Configure menu, select IP . |
| Step 23 | On the IP page, enter the following settings. Table 19. IP Page Settings Field Setting Client IP Address Enter the new IP address you want to use for the PIMG unit. (This is the IP address that you enter in Cisco Unity Connection Administration when you create the integration.) Client Subnet Mask Enter the new subnet mask, if the subnet mask is different from the default IP address. Default Network Gateway Address Enter the IP address of the default network gateway router that the PIMG units use. BOOTP Enabled Select No . | Field | Setting | Client IP Address | Enter the new IP address you want to use for the PIMG unit. (This is the IP address that you enter in Cisco Unity Connection Administration when you create the integration.) | Client Subnet Mask | Enter the new subnet mask, if the subnet mask is different from the default IP address. | Default Network Gateway Address | Enter the IP address of the default network gateway router that the PIMG units use. | BOOTP Enabled | Select No . |
| Field | Setting |
| Client IP Address | Enter the new IP address you want to use for the PIMG unit. (This is the IP address that you enter in Cisco Unity Connection Administration when you create the integration.) |
| Client Subnet Mask | Enter the new subnet mask, if the subnet mask is different from the default IP address. |
| Default Network Gateway Address | Enter the IP address of the default network gateway router that the PIMG units use. |
| BOOTP Enabled | Select No . |
| Step 24 | Select Apply Changes . |
| Step 25 | On the Configure menu, select Tones . |
| Step 26 | On the Tones page, select the Learn tab. Destination addresses cannot be duplicated in the same session. Otherwise, the process for learning tones do not succeed.
                                             If you do not have enough available phones to learn all the tones at one time, you can run multiple sessions to learn tones
                                             individually by checking or unchecking the applicable Acquire Tone check boxes. |
| Step 27 | On the Tones page, for the Dialtone event, confirm that the Acquire Tone check box is checked and leave the Destination Address
                                          field blank. |
| Step 28 | On the Tones page, for the Busy Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                          to verify that the tone is correct. From a available phone, call a second phone. Answer the second phone when it rings, and leave both handsets off so that both phones are busy. From a third phone, dial one of the busy phones. Confirm that you hear a busy tone. Hang up the third phone but leave the handsets for the other two phones off. |
| Step 29 | On the Tones page, in the Destination Address field for Busy Tone, enter the extension that you dialed in Step 28 c. from the third phone. |
| Step 30 | On the Tones page, for the Error/Reorder Tone event, confirm that the Acquire Tone check box is checked and do the following
                                          substeps to verify that the tone is correct. From an available phone, dial an extension that does not exist. Confirm that you hear the reorder or error tone. Hang up the phone. |
| Step 31 | On the Tones page, in the Destination Address field for Error/Reorder Tone, enter the extension that you dialed in Step 30 a. |
| Step 32 | On the Tones page, for the Ringback Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                          to verify that the tone is correct. From an available phone, dial an extension that does exist. Confirm that you hear the ringback tone. Hang up the phone. |
| Step 33 | On the Tones page, in the Destination Address field for Ringback Tone, enter the extension that you dialed in Step 32 a. |
| Step 34 | Select Learn . Note When running learn tones, the PIMG unit restarts after learning the first tone. | Note | When running learn tones, the PIMG unit restarts after learning the first tone. |
| Note | When running learn tones, the PIMG unit restarts after learning the first tone. |
| Step 35 | When the process is complete, check the check box for each newly learned tone and select Apply . |
| Step 36 | Hang up the phones that you used in Step 28 . |
| Step 37 | On the Configure menu, select Restart . |
| Step 38 | On the Restart page, select Restart Unit Now . |
| Step 39 | When the PIMG unit has restarted, in the View menu, select Refresh . |
| Step 40 | Repeat Step 1 through Step 39 on all remaining PIMG units. |

| Field | Setting |
|---|---|
| Operating Mode | Select SIP . |
| PCM Coding | Select uLaw . |
| Serial Port Baud Rate | Select the setting that is configured on the phone system. The default setting is 9600. |
| Serial Port Parity | Select the setting that is configured on the phone system. The default setting is None. |
| Serial Port Data Bits | Select the setting that is configured on the phone system. The default setting is 8. |
| Serial Port Stop Bits | Select the setting that is configured on the phone system. The default setting is 1. |

| Note | To add endpoints, select Add New Endpoint . |
|---|---|

| Count | VoIP Endpoint ID |
|---|---|
| 1 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the subscriber server. |
| 2 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the publisher server. |

| Field | Settings |
|---|---|
| Advanced Call Routing |
| Call Connect Mode | Select OnAnswer . |
| Destination for Unroutable IP Calls | Leave this field blank. |
| Destination for Unroutable PBX Calls | Leave this field blank. |
| Monitor Call Connections | Select No . |
| Telephony |
| Minimum Call Party Delay | Enter 500 . |
| Maximum Call Party Delay | Enter 2000 . |
| Dial Digit on Time | Enter 100 . |
| Dial Inter-Digit Time | Enter 100 . |
| Dial Pause Time | Enter 2000 . |
| Turn MWI On FAC | Leave this field blank. |
| Turn MWI Off FAC | Leave this field blank. |
| Outbound Call Connect Timeout | Enter 10000 . |
| Wait for Ringback/Connect on Blind Transfer | Select Yes . |
| Hunt Group Extension | Enter the pilot number of the Unity Connection voice messaging ports. |
| Audio |
| Audio Compression | Select the preferred codec for audio compression: G.711 G.729AB |
| RTP Digit Relay Mode | Select RFC2833 . |
| Signaling Digit Relay Mode | Select Off . |
| Voice Activity Detection | Select Off . |
| Frame Size | Select the applicable setting: G.711— 20 G.729AB— 10 Failure to use the correct setting results in recorded messages containing nothing but silence. |
| Frames Per Packet | Select the applicable setting: G.711— 1 G.729AB— 2 Failure to use the correct setting results in recorded messages containing nothing but silence. |
| Quality of Service |
| Call Control QOS Byte | Enter 104 (equivalent to DSCP AF31). |
| RTP QOS Byte | Enter 184 (equivalent to DSCP EF). |
| Traps and Alarms |
| E-mail Alarms Enabled | Select No . |
| SNMP Traps Enabled | Select No . |

| Telephony Port Capability Settings | Voice Messaging Port Usage |
|---|---|
| Calls-Only | The port answers incoming calls only and cannot dial out (for example, to set MWIs or send message notifications). |
| MWIs-Only | The port dial out only (for example, to set MWIs or send message notifications) and cannot answer incoming calls. |
| Both | The port answers incoming calls and also dial out (for example, to set MWIs or send message notifications). |

| Field | Setting |
|---|---|
| Serial Mode | Select the applicable setting: Master —Select this setting when this PIMG unit is connected to the data link serial cable from the phone system. There can be only
                                                               one master PIMG unit in a phone system integration. Slave —Select this setting when this PIMG unit is not connected to the data link serial cable from the phone system. There can be
                                                               multiple slave PIMG units in a phone system integration. |
| Serial Interface Protocol | Select the serial protocol that your phone system uses: SMDI MCI MD-110 |
| Cpid Len | Select the applicable setting. Typically, the settings are 7 or 10. |
| Cpid Padding String | Enter the applicable string or leave this field blank. Typically, the setting is one of the following: A string of zeros, where the number of zeros matches the setting of the Cpid Len field. A prefix that is provided by the Centrex service. |
| Voice Mail Port Len | If the setting of the Serial Interface Protocol field is MD-110, enter 2 . Otherwise, accept the default of 7 . |
| System Number | Enter the applicable setting. Typically, the setting is 1. |
| MWI Response Timeout | Enter 2000 . |
| IP Address of Serial Server | If the PIMG unit is the master, leave this field blank. If the PIMG unit is a slave, enter the IP address of the master PIMG unit (the PIMG unit that is connected to the data link
                                                         serial cable from the phone system). |
| Serial Cpid Expiration | Enter 2000 . |
| Logical Extension Number | If the setting of the Serial Interface Protocol field is MCI or MD-110, enter the extension number for each port on the PIMG
                                                         unit. If the setting of the Serial Interface Protocol field is SMDI, enter the logical port number. Typically, the setting is 1
                                                         for port 1, 2 for port 2, and so on beginning with the master PIMG unit and continuing through each of the slave PIMG units. |

| Field | Setting |
|---|---|
| Host and Domain Name | Enter the domain name of the PIMG unit. This setting must match the name of the port group in Cisco Unity Connection Administration that has the voice messaging ports
                                                         connecting to the PIMG unit. |
| Server Port | Enter 5060 . |
| Primary Proxy Server Address | Leave this field blank. |
| Primary Proxy Server Port | Not applicable. Leave the default setting. |
| Backup Proxy Server Address | Not applicable. Leave the default setting. |
| Backup Proxy Server Port | Not applicable. Leave the default setting. |
| Proxy Query Interval | Enter 10 . |
| T1 Time | Enter 400 . |
| T2 Time | Enter 3000 . |

| Field | Setting |
|---|---|
| Client IP Address | Enter the new IP address you want to use for the PIMG unit. (This is the IP address that you enter in Cisco Unity Connection Administration when you create the integration.) |
| Client Subnet Mask | Enter the new subnet mask, if the subnet mask is different from the default IP address. |
| Default Network Gateway Address | Enter the IP address of the default network gateway router that the PIMG units use. |
| BOOTP Enabled | Select No . |

| Note | When running learn tones, the PIMG unit restarts after learning the first tone. |
|---|---|

| Step 1 | On a Windows workstation, sign in to a PIMG unit. |
|---|---|
| Step 2 | On the Configure menu, select System . |
| Step 3 | On the System page, enter the following settings. Table 20. System Page Settings Field Setting Operating Mode Select SIP . PBX Type (This setting does not apply.) PCM Coding Select uLaw . | Field | Setting | Operating Mode | Select SIP . | PBX Type | (This setting does not apply.) | PCM Coding | Select uLaw . |
| Field | Setting |
| Operating Mode | Select SIP . |
| PBX Type | (This setting does not apply.) |
| PCM Coding | Select uLaw . |
| Step 4 | Select Apply Changes . |
| Step 5 | On the Configure menu, select Gateway . |
| Step 6 | On the Gateway page, select the Gateway Routing tab. |
| Step 7 | On the Gateway Routing tab, Unity Connection without a cluster, skip to Step 8 . If Unity Connection has a cluster configured, do the following substeps: In the Fault Tolerance Enabled field, select Yes . In the Load Balancing Enabled field, select No. |
| Step 8 | Under VoIP Endpoint ID, enter the following settings. Note To add endpoints, select Add New Endpoint . Table 21. Gateway Routing Tab Settings Count VoIP Endpoint ID 1 (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the subscriber server. 2 (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the publisher server. | Note | To add endpoints, select Add New Endpoint . | Count | VoIP Endpoint ID | 1 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the subscriber server. | 2 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the publisher server. |
| Note | To add endpoints, select Add New Endpoint . |
| Count | VoIP Endpoint ID |
| 1 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the subscriber server. |
| 2 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the publisher server. |
| Step 9 | Select Apply Changes . |
| Step 10 | Select the Gateway Advanced tab. |
| Step 11 | On the Gateway Advanced tab, enter the following settings. Table 22. Gateway Advanced Tab Settings Field Settings Call Connect Mode Select OnAnswer . Destination for Unroutable PBX Calls Enter the extension of an attendant who receive calls to Unity Connection that are unanswered. Minimum Call Party Delay (msecs) Enter 500 . Turn MWI On FAC Enter the code that turns MWIs on. Turn MWI Off FAC Enter the code that turns MWIs off. Wait for Ringback/Connect on Blind Transfer Select Yes . Hunt Group Extension Enter the pilot number of the Unity Connection voice messaging ports. Audio Compression Select the preferred codec for audio compression: G.711 G.729AB Signaling Digit Relay Mode Select Off . Voice Activity Detection Select Off . Frame Size Select the applicable setting: G.711— 20 G.729AB— 10 Failure to use the correct setting results in recorded messages containing nothing but silence. Frames Per Packet Select the applicable setting: G.711— 1 G.729AB— 2 Failure to use the correct setting results in recorded messages containing nothing but silence. Call Control QOS Byte Enter 104 (equivalent to DSCP AF31). RTP QOS Byte Enter 184 (equivalent to DSCP EF). | Field | Settings | Call Connect Mode | Select OnAnswer . | Destination for Unroutable PBX Calls | Enter the extension of an attendant who receive calls to Unity Connection that are unanswered. | Minimum Call Party Delay (msecs) | Enter 500 . | Turn MWI On FAC | Enter the code that turns MWIs on. | Turn MWI Off FAC | Enter the code that turns MWIs off. | Wait for Ringback/Connect on Blind Transfer | Select Yes . | Hunt Group Extension | Enter the pilot number of the Unity Connection voice messaging ports. | Audio Compression | Select the preferred codec for audio compression: G.711 G.729AB | Signaling Digit Relay Mode | Select Off . | Voice Activity Detection | Select Off . | Frame Size | Select the applicable setting: G.711— 20 G.729AB— 10 Failure to use the correct setting results in recorded messages containing nothing but silence. | Frames Per Packet | Select the applicable setting: G.711— 1 G.729AB— 2 Failure to use the correct setting results in recorded messages containing nothing but silence. | Call Control QOS Byte | Enter 104 (equivalent to DSCP AF31). | RTP QOS Byte | Enter 184 (equivalent to DSCP EF). |
| Field | Settings |
| Call Connect Mode | Select OnAnswer . |
| Destination for Unroutable PBX Calls | Enter the extension of an attendant who receive calls to Unity Connection that are unanswered. |
| Minimum Call Party Delay (msecs) | Enter 500 . |
| Turn MWI On FAC | Enter the code that turns MWIs on. |
| Turn MWI Off FAC | Enter the code that turns MWIs off. |
| Wait for Ringback/Connect on Blind Transfer | Select Yes . |
| Hunt Group Extension | Enter the pilot number of the Unity Connection voice messaging ports. |
| Audio Compression | Select the preferred codec for audio compression: G.711 G.729AB |
| Signaling Digit Relay Mode | Select Off . |
| Voice Activity Detection | Select Off . |
| Frame Size | Select the applicable setting: G.711— 20 G.729AB— 10 Failure to use the correct setting results in recorded messages containing nothing but silence. |
| Frames Per Packet | Select the applicable setting: G.711— 1 G.729AB— 2 Failure to use the correct setting results in recorded messages containing nothing but silence. |
| Call Control QOS Byte | Enter 104 (equivalent to DSCP AF31). |
| RTP QOS Byte | Enter 184 (equivalent to DSCP EF). |
| Step 12 | Select Apply Changes . |
| Step 13 | Select the Gateway Capabilities tab. |
| Step 14 | Depending on how you have planned to use the voice messaging ports, select the applicable setting for each port in the Telephony
                                          Port Capability column. Table 23. Gateway Capabilities Tab Settings Telephony Port Capability Settings Voice Messaging Port Usage Calls-Only The port answer incoming calls only and cannot dial out (for example, to set MWIs or send message notifications). MWIs-Only The port dial out only (for example, to set MWIs or send message notifications) and cannot answer incoming calls. Both The port answers incoming calls and also dial out (for example, to set MWIs or send message notifications). In setting up the PIMG unit, do not send calls to ports in Unity Connection that cannot answer calls (voice messaging ports
                                             that are not set to Answer Calls). For example, if a voice messaging port is set only to Send MWI Requests, do not send calls
                                             to it. Otherwise the integration cannot function correctly. If a port in Unity Connection is disabled, select No in the Telephony Port Enabled column for the corresponding port on this tab. Note that changing a setting in the Telephony
                                             Port Enabled column requires restarting the PIMG unit. | Telephony Port Capability Settings | Voice Messaging Port Usage | Calls-Only | The port answer incoming calls only and cannot dial out (for example, to set MWIs or send message notifications). | MWIs-Only | The port dial out only (for example, to set MWIs or send message notifications) and cannot answer incoming calls. | Both | The port answers incoming calls and also dial out (for example, to set MWIs or send message notifications). |
| Telephony Port Capability Settings | Voice Messaging Port Usage |
| Calls-Only | The port answer incoming calls only and cannot dial out (for example, to set MWIs or send message notifications). |
| MWIs-Only | The port dial out only (for example, to set MWIs or send message notifications) and cannot answer incoming calls. |
| Both | The port answers incoming calls and also dial out (for example, to set MWIs or send message notifications). |
| Step 15 | Select Apply Changes . |
| Step 16 | On the Configure menu, select SIP . |
| Step 17 | On the SIP page, enter the following settings. Table 24. SIP Page Settings Field Setting Host and Domain Name Enter the domain name of the PIMG unit. Server Port Enter 5060 . Primary Proxy Server Address Leave this field blank. Primary Proxy Server Port Not applicable. Leave the default setting. Backup Proxy Server Address Not applicable. Leave the default setting. Backup Proxy Server Port Not applicable. Leave the default setting. Proxy Query Interval Enter 10 . T1 Time Enter 400 . T2 Time Enter 3000 . | Field | Setting | Host and Domain Name | Enter the domain name of the PIMG unit. | Server Port | Enter 5060 . | Primary Proxy Server Address | Leave this field blank. | Primary Proxy Server Port | Not applicable. Leave the default setting. | Backup Proxy Server Address | Not applicable. Leave the default setting. | Backup Proxy Server Port | Not applicable. Leave the default setting. | Proxy Query Interval | Enter 10 . | T1 Time | Enter 400 . | T2 Time | Enter 3000 . |
| Field | Setting |
| Host and Domain Name | Enter the domain name of the PIMG unit. |
| Server Port | Enter 5060 . |
| Primary Proxy Server Address | Leave this field blank. |
| Primary Proxy Server Port | Not applicable. Leave the default setting. |
| Backup Proxy Server Address | Not applicable. Leave the default setting. |
| Backup Proxy Server Port | Not applicable. Leave the default setting. |
| Proxy Query Interval | Enter 10 . |
| T1 Time | Enter 400 . |
| T2 Time | Enter 3000 . |
| Step 18 | Select Apply Changes . |
| Step 19 | On the Configure menu, select IP . |
| Step 20 | On the IP page, enter the following settings. Table 25. IP Page Settings Field Setting Client IP Address Enter the new IP address you want to use for the PIMG unit. (This is the IP address that you enter in Cisco Unity Connection Administration when you create the integration.) Client Subnet Mask Enter the new subnet mask, if the subnet mask is different from the default IP address. Default Network Gateway Address Enter the IP address of the default network gateway router that the PIMG units use. BOOTP Enabled Select No . | Field | Setting | Client IP Address | Enter the new IP address you want to use for the PIMG unit. (This is the IP address that you enter in Cisco Unity Connection Administration when you create the integration.) | Client Subnet Mask | Enter the new subnet mask, if the subnet mask is different from the default IP address. | Default Network Gateway Address | Enter the IP address of the default network gateway router that the PIMG units use. | BOOTP Enabled | Select No . |
| Field | Setting |
| Client IP Address | Enter the new IP address you want to use for the PIMG unit. (This is the IP address that you enter in Cisco Unity Connection Administration when you create the integration.) |
| Client Subnet Mask | Enter the new subnet mask, if the subnet mask is different from the default IP address. |
| Default Network Gateway Address | Enter the IP address of the default network gateway router that the PIMG units use. |
| BOOTP Enabled | Select No . |
| Step 21 | Select Apply Changes . |
| Step 22 | On the Configure menu, select Tones . |
| Step 23 | On the Tones page, select the Learn tab. Destination addresses cannot be duplicated in the same session. Otherwise, the process for learning tones cannot succeed.
                                             If you do not have enough available phones to learn all the tones at one time, you can run multiple sessions to learn tones
                                             individually by checking or unchecking the applicable Acquire Tone check boxes. |
| Step 24 | On the Tones page, for the Dialtone event, confirm that the Acquire Tone check box is checked and leave the Destination Address
                                          field blank. |
| Step 25 | On the Tones page, for the Busy Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                          to verify that the tone is correct. From a available phone, call a second phone. Answer the second phone when it rings, and leave both handsets off so that both phones are busy. From a third phone, dial one of the busy phones. Confirm that you hear a busy tone. Hang up the third phone but leave the handsets for the other two phones off. |
| Step 26 | On the Tones page, in the Destination Address field for Busy Tone, enter the extension that you dialed in Step 25 c. from the third phone. |
| Step 27 | On the Tones page, for the Error/Reorder Tone event, confirm that the Acquire Tone check box is checked and do the following
                                          substeps to verify that the tone is correct. From an available phone, dial an extension that does not exist. Confirm that you hear the reorder or error tone. Hang up the phone. |
| Step 28 | On the Tones page, in the Destination Address field for Error/Reorder Tone, enter the extension that you dialed in Step 27 a. |
| Step 29 | On the Tones page, for the Ringback Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                          to verify that the tone is correct. From an available phone, dial an extension that does exist. Confirm that you hear the ringback tone. Hang up the phone. |
| Step 30 | On the Tones page, in the Destination Address field for Ringback Tone, enter the extension that you dialed in Step 29 a. |
| Step 31 | Select Learn . Note When running learn tones, the PIMG unit restarts after learning the first tone. | Note | When running learn tones, the PIMG unit restarts after learning the first tone. |
| Note | When running learn tones, the PIMG unit restarts after learning the first tone. |
| Step 32 | When the process is complete, check the check box for each newly learned tone and select Apply . |
| Step 33 | Hang up the phones that you used in Step 25 . |
| Step 34 | On the Configure menu, select Restart . |
| Step 35 | On the Restart page, select Restart Unit Now . |
| Step 36 | When the PIMG unit has restarted, in the View menu, select Refresh . |
| Step 37 | Repeat Step 1 through Step 36 on all remaining PIMG units. |

| Field | Setting |
|---|---|
| Operating Mode | Select SIP . |
| PBX Type | (This setting does not apply.) |
| PCM Coding | Select uLaw . |

| Note | To add endpoints, select Add New Endpoint . |
|---|---|

| Count | VoIP Endpoint ID |
|---|---|
| 1 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the subscriber server. |
| 2 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the publisher server. |

| Field | Settings |
|---|---|
| Call Connect Mode | Select OnAnswer . |
| Destination for Unroutable PBX Calls | Enter the extension of an attendant who receive calls to Unity Connection that are unanswered. |
| Minimum Call Party Delay (msecs) | Enter 500 . |
| Turn MWI On FAC | Enter the code that turns MWIs on. |
| Turn MWI Off FAC | Enter the code that turns MWIs off. |
| Wait for Ringback/Connect on Blind Transfer | Select Yes . |
| Hunt Group Extension | Enter the pilot number of the Unity Connection voice messaging ports. |
| Audio Compression | Select the preferred codec for audio compression: G.711 G.729AB |
| Signaling Digit Relay Mode | Select Off . |
| Voice Activity Detection | Select Off . |
| Frame Size | Select the applicable setting: G.711— 20 G.729AB— 10 Failure to use the correct setting results in recorded messages containing nothing but silence. |
| Frames Per Packet | Select the applicable setting: G.711— 1 G.729AB— 2 Failure to use the correct setting results in recorded messages containing nothing but silence. |
| Call Control QOS Byte | Enter 104 (equivalent to DSCP AF31). |
| RTP QOS Byte | Enter 184 (equivalent to DSCP EF). |

| Telephony Port Capability Settings | Voice Messaging Port Usage |
|---|---|
| Calls-Only | The port answer incoming calls only and cannot dial out (for example, to set MWIs or send message notifications). |
| MWIs-Only | The port dial out only (for example, to set MWIs or send message notifications) and cannot answer incoming calls. |
| Both | The port answers incoming calls and also dial out (for example, to set MWIs or send message notifications). |

| Field | Setting |
|---|---|
| Host and Domain Name | Enter the domain name of the PIMG unit. |
| Server Port | Enter 5060 . |
| Primary Proxy Server Address | Leave this field blank. |
| Primary Proxy Server Port | Not applicable. Leave the default setting. |
| Backup Proxy Server Address | Not applicable. Leave the default setting. |
| Backup Proxy Server Port | Not applicable. Leave the default setting. |
| Proxy Query Interval | Enter 10 . |
| T1 Time | Enter 400 . |
| T2 Time | Enter 3000 . |

| Field | Setting |
|---|---|
| Client IP Address | Enter the new IP address you want to use for the PIMG unit. (This is the IP address that you enter in Cisco Unity Connection Administration when you create the integration.) |
| Client Subnet Mask | Enter the new subnet mask, if the subnet mask is different from the default IP address. |
| Default Network Gateway Address | Enter the IP address of the default network gateway router that the PIMG units use. |
| BOOTP Enabled | Select No . |

| Note | When running learn tones, the PIMG unit restarts after learning the first tone. |
|---|---|

| Step 1 | On a Windows workstation, sign in to a PIMG unit. |
|---|---|
| Step 2 | On the Configure menu, select System . |
| Step 3 | On the System page, enter the following settings. Table 26. System Page Settings Field Setting Operating Mode Select SIP . PBX Type Depending on your phone system, select one of the following: Rolm_9751_SW9005 Rolm_9751_SW9006 PCM Coding Select uLaw . | Field | Setting | Operating Mode | Select SIP . | PBX Type | Depending on your phone system, select one of the following: Rolm_9751_SW9005 Rolm_9751_SW9006 | PCM Coding | Select uLaw . |
| Field | Setting |
| Operating Mode | Select SIP . |
| PBX Type | Depending on your phone system, select one of the following: Rolm_9751_SW9005 Rolm_9751_SW9006 |
| PCM Coding | Select uLaw . |
| Step 4 | Select Apply Changes . |
| Step 5 | On the Configure menu, select Gateway . |
| Step 6 | On the Gateway page, select the Gateway Routing tab. |
| Step 7 | On the Gateway Routing tab, Unity Connection without a cluster, skip to Step 8 . If Unity Connection has a cluster configured, do the following substeps: In the Fault Tolerance Enabled field, select Yes . In the Load Balancing Enabled field, select No. |
| Step 8 | Under VoIP Endpoint ID, enter the following settings. Note To add endpoints, select Add New Endpoint . Table 27. Gateway Routing Tab Settings Count VoIP Endpoint ID 1 (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the subscriber server. 2 (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the publisher server. | Note | To add endpoints, select Add New Endpoint . | Count | VoIP Endpoint ID | 1 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the subscriber server. | 2 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the publisher server. |
| Note | To add endpoints, select Add New Endpoint . |
| Count | VoIP Endpoint ID |
| 1 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the subscriber server. |
| 2 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the publisher server. |
| Step 9 | Select Apply Changes . |
| Step 10 | Select the Gateway Advanced tab. |
| Step 11 | On the Gateway Advanced tab, enter the following settings. Table 28. Gateway Advanced Tab Settings Field Settings Call Connect Mode Select OnAnswer . Destination for Unroutable PBX Calls Enter the extension of an attendant who receives calls to Unity Connection that are unanswered. Minimum Call Party Delay (msecs) Enter 500 . Turn MWI On FAC Leave this field blank. Turn MWI Off FAC Leave this field blank. Wait for Ringback/Connect on Blind Transfer Select Yes . Hunt Group Extension Enter the pilot number of the Unity Connection voice messaging ports. Audio Compression Select the preferred codec for audio compression: G.711 G.729AB Signaling Digit Relay Mode Select Off . Voice Activity Detection Select Off . Frame Size Select the applicable setting: G.711— 20 G.729AB— 10 Failure to use the correct setting results in recorded messages containing nothing but silence. Frames Per Packet Select the applicable setting: G.711— 1 G.729AB— 2 Failure to use the correct setting results in recorded messages containing nothing but silence. Call Control QOS Byte Enter 104 (equivalent to DSCP AF31). RTP QOS Byte Enter 184 (equivalent to DSCP EF). | Field | Settings | Call Connect Mode | Select OnAnswer . | Destination for Unroutable PBX Calls | Enter the extension of an attendant who receives calls to Unity Connection that are unanswered. | Minimum Call Party Delay (msecs) | Enter 500 . | Turn MWI On FAC | Leave this field blank. | Turn MWI Off FAC | Leave this field blank. | Wait for Ringback/Connect on Blind Transfer | Select Yes . | Hunt Group Extension | Enter the pilot number of the Unity Connection voice messaging ports. | Audio Compression | Select the preferred codec for audio compression: G.711 G.729AB | Signaling Digit Relay Mode | Select Off . | Voice Activity Detection | Select Off . | Frame Size | Select the applicable setting: G.711— 20 G.729AB— 10 Failure to use the correct setting results in recorded messages containing nothing but silence. | Frames Per Packet | Select the applicable setting: G.711— 1 G.729AB— 2 Failure to use the correct setting results in recorded messages containing nothing but silence. | Call Control QOS Byte | Enter 104 (equivalent to DSCP AF31). | RTP QOS Byte | Enter 184 (equivalent to DSCP EF). |
| Field | Settings |
| Call Connect Mode | Select OnAnswer . |
| Destination for Unroutable PBX Calls | Enter the extension of an attendant who receives calls to Unity Connection that are unanswered. |
| Minimum Call Party Delay (msecs) | Enter 500 . |
| Turn MWI On FAC | Leave this field blank. |
| Turn MWI Off FAC | Leave this field blank. |
| Wait for Ringback/Connect on Blind Transfer | Select Yes . |
| Hunt Group Extension | Enter the pilot number of the Unity Connection voice messaging ports. |
| Audio Compression | Select the preferred codec for audio compression: G.711 G.729AB |
| Signaling Digit Relay Mode | Select Off . |
| Voice Activity Detection | Select Off . |
| Frame Size | Select the applicable setting: G.711— 20 G.729AB— 10 Failure to use the correct setting results in recorded messages containing nothing but silence. |
| Frames Per Packet | Select the applicable setting: G.711— 1 G.729AB— 2 Failure to use the correct setting results in recorded messages containing nothing but silence. |
| Call Control QOS Byte | Enter 104 (equivalent to DSCP AF31). |
| RTP QOS Byte | Enter 184 (equivalent to DSCP EF). |
| Step 12 | Select Apply Changes . |
| Step 13 | Select the Gateway Capabilities tab. |
| Step 14 | Depending on how you have planned to use the voice messaging ports, select the applicable setting for each port in the Telephony
                                          Port Capability column. Table 29. Gateway Capabilities Tab Settings Telephony Port Capability Settings Voice Messaging Port Usage Calls-Only The port answers incoming calls only and cannot dial out (for example, to set MWIs or send message notifications). MWIs-Only The port dial out only (for example, to set MWIs or send message notifications) and cannot answer incoming calls. Both The port answers incoming calls and also dial out (for example, to set MWIs or send message notifications). In setting up the PIMG unit, do not send calls to ports in Unity Connection that cannot answer calls (voice messaging ports
                                             that are not set to Answer Calls). For example, if a voice messaging port is set only to Send MWI Requests, do not send calls
                                             to it. Otherwise the integration cannot function correctly. If a port in Unity Connection is disabled, select No in the Telephony Port Enabled column for the corresponding port on this tab. Note that changing a setting in the Telephony
                                             Port Enabled column requires restarting the PIMG unit. | Telephony Port Capability Settings | Voice Messaging Port Usage | Calls-Only | The port answers incoming calls only and cannot dial out (for example, to set MWIs or send message notifications). | MWIs-Only | The port dial out only (for example, to set MWIs or send message notifications) and cannot answer incoming calls. | Both | The port answers incoming calls and also dial out (for example, to set MWIs or send message notifications). |
| Telephony Port Capability Settings | Voice Messaging Port Usage |
| Calls-Only | The port answers incoming calls only and cannot dial out (for example, to set MWIs or send message notifications). |
| MWIs-Only | The port dial out only (for example, to set MWIs or send message notifications) and cannot answer incoming calls. |
| Both | The port answers incoming calls and also dial out (for example, to set MWIs or send message notifications). |
| Step 15 | Select Apply Changes . |
| Step 16 | On the Configure menu, select SIP . |
| Step 17 | On the SIP page, enter the following settings. Table 30. SIP Page Settings Field Setting Host and Domain Name Enter the domain name of the PIMG unit. Server Port Enter 5060 . Primary Proxy Server Address Leave this field blank. Primary Proxy Server Port Not applicable. Leave the default setting. Backup Proxy Server Address Not applicable. Leave the default setting. Backup Proxy Server Port Not applicable. Leave the default setting. Proxy Query Interval Enter 10 . T1 Time Enter 400 . T2 Time Enter 3000 . | Field | Setting | Host and Domain Name | Enter the domain name of the PIMG unit. | Server Port | Enter 5060 . | Primary Proxy Server Address | Leave this field blank. | Primary Proxy Server Port | Not applicable. Leave the default setting. | Backup Proxy Server Address | Not applicable. Leave the default setting. | Backup Proxy Server Port | Not applicable. Leave the default setting. | Proxy Query Interval | Enter 10 . | T1 Time | Enter 400 . | T2 Time | Enter 3000 . |
| Field | Setting |
| Host and Domain Name | Enter the domain name of the PIMG unit. |
| Server Port | Enter 5060 . |
| Primary Proxy Server Address | Leave this field blank. |
| Primary Proxy Server Port | Not applicable. Leave the default setting. |
| Backup Proxy Server Address | Not applicable. Leave the default setting. |
| Backup Proxy Server Port | Not applicable. Leave the default setting. |
| Proxy Query Interval | Enter 10 . |
| T1 Time | Enter 400 . |
| T2 Time | Enter 3000 . |
| Step 18 | Select Apply Changes . |
| Step 19 | On the Configure menu, select IP . |
| Step 20 | On the IP page, enter the following settings. Table 31. IP Page Settings Field Setting Client IP Address Enter the new IP address you want to use for the PIMG unit. (This is the IP address that you enter in Cisco Unity Connection Administration when you create the integration.) Client Subnet Mask Enter the new subnet mask, if the subnet mask is different from the default IP address. Default Network Gateway Address Enter the IP address of the default network gateway router that the PIMG units use. BOOTP Enabled Select No . | Field | Setting | Client IP Address | Enter the new IP address you want to use for the PIMG unit. (This is the IP address that you enter in Cisco Unity Connection Administration when you create the integration.) | Client Subnet Mask | Enter the new subnet mask, if the subnet mask is different from the default IP address. | Default Network Gateway Address | Enter the IP address of the default network gateway router that the PIMG units use. | BOOTP Enabled | Select No . |
| Field | Setting |
| Client IP Address | Enter the new IP address you want to use for the PIMG unit. (This is the IP address that you enter in Cisco Unity Connection Administration when you create the integration.) |
| Client Subnet Mask | Enter the new subnet mask, if the subnet mask is different from the default IP address. |
| Default Network Gateway Address | Enter the IP address of the default network gateway router that the PIMG units use. |
| BOOTP Enabled | Select No . |
| Step 21 | Select Apply Changes . |
| Step 22 | On the Configure menu, select Tones . |
| Step 23 | On the Tones page, select the Learn tab. Destination addresses cannot be duplicated in the same session. Otherwise, the process for learning tones cannot succeed.
                                             If you do not have enough available phones to learn all the tones at one time, you can run multiple sessions to learn tones
                                             individually by checking or unchecking the applicable Acquire Tone check boxes. |
| Step 24 | On the Tones page, for the Dialtone event, confirm that the Acquire Tone check box is checked and leave the Destination Address
                                          field blank. |
| Step 25 | On the Tones page, for the Busy Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                          to verify that the tone is correct. From a available phone, call a second phone. Answer the second phone when it rings, and leave both handsets off so that both phones are busy. From a third phone, dial one of the busy phones. Confirm that you hear a busy tone. Hang up the third phone but leave the handsets for the other two phones off. |
| Step 26 | On the Tones page, in the Destination Address field for Busy Tone, enter the extension that you dialed in Step 25 c. from the third phone. |
| Step 27 | On the Tones page, for the Error/Reorder Tone event, confirm that the Acquire Tone check box is checked and do the following
                                          substeps to verify that the tone is correct. From an available phone, dial an extension that does not exist. Confirm that you hear the reorder or error tone. Hang up the phone. |
| Step 28 | On the Tones page, in the Destination Address field for Error/Reorder Tone, enter the extension that you dialed in Step 27 a. |
| Step 29 | On the Tones page, for the Ringback Tone event, confirm that the Acquire Tone check box is checked and do the following substeps
                                          to verify that the tone is correct. From an available phone, dial an extension that does exist. Confirm that you hear the ringback tone. Hang up the phone. |
| Step 30 | On the Tones page, in the Destination Address field for Ringback Tone, enter the extension that you dialed in Step 29 a. |
| Step 31 | Select Learn . Note When running learn tones, the PIMG unit restarts after learning the first tone. | Note | When running learn tones, the PIMG unit restarts after learning the first tone. |
| Note | When running learn tones, the PIMG unit restarts after learning the first tone. |
| Step 32 | When the process is complete, check the check box for each newly learned tone and select Apply . |
| Step 33 | Hang up the phones that you used in Step 25 . |
| Step 34 | On the Configure menu, select Restart . |
| Step 35 | On the Restart page, select Restart Unit Now . |
| Step 36 | When the PIMG unit has restarted, in the View menu, select Refresh . |
| Step 37 | Repeat Step 1 through Step 36 on all remaining PIMG units. |

| Field | Setting |
|---|---|
| Operating Mode | Select SIP . |
| PBX Type | Depending on your phone system, select one of the following: Rolm_9751_SW9005 Rolm_9751_SW9006 |
| PCM Coding | Select uLaw . |

| Note | To add endpoints, select Add New Endpoint . |
|---|---|

| Count | VoIP Endpoint ID |
|---|---|
| 1 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the subscriber server. |
| 2 | (Unity Connection without a cluster) Enter the server name of the Unity Connection server. (Unity Connection with a cluster configured) Enter the server name of the publisher server. |

| Field | Settings |
|---|---|
| Call Connect Mode | Select OnAnswer . |
| Destination for Unroutable PBX Calls | Enter the extension of an attendant who receives calls to Unity Connection that are unanswered. |
| Minimum Call Party Delay (msecs) | Enter 500 . |
| Turn MWI On FAC | Leave this field blank. |
| Turn MWI Off FAC | Leave this field blank. |
| Wait for Ringback/Connect on Blind Transfer | Select Yes . |
| Hunt Group Extension | Enter the pilot number of the Unity Connection voice messaging ports. |
| Audio Compression | Select the preferred codec for audio compression: G.711 G.729AB |
| Signaling Digit Relay Mode | Select Off . |
| Voice Activity Detection | Select Off . |
| Frame Size | Select the applicable setting: G.711— 20 G.729AB— 10 Failure to use the correct setting results in recorded messages containing nothing but silence. |
| Frames Per Packet | Select the applicable setting: G.711— 1 G.729AB— 2 Failure to use the correct setting results in recorded messages containing nothing but silence. |
| Call Control QOS Byte | Enter 104 (equivalent to DSCP AF31). |
| RTP QOS Byte | Enter 184 (equivalent to DSCP EF). |

| Telephony Port Capability Settings | Voice Messaging Port Usage |
|---|---|
| Calls-Only | The port answers incoming calls only and cannot dial out (for example, to set MWIs or send message notifications). |
| MWIs-Only | The port dial out only (for example, to set MWIs or send message notifications) and cannot answer incoming calls. |
| Both | The port answers incoming calls and also dial out (for example, to set MWIs or send message notifications). |

| Field | Setting |
|---|---|
| Host and Domain Name | Enter the domain name of the PIMG unit. |
| Server Port | Enter 5060 . |
| Primary Proxy Server Address | Leave this field blank. |
| Primary Proxy Server Port | Not applicable. Leave the default setting. |
| Backup Proxy Server Address | Not applicable. Leave the default setting. |
| Backup Proxy Server Port | Not applicable. Leave the default setting. |
| Proxy Query Interval | Enter 10 . |
| T1 Time | Enter 400 . |
| T2 Time | Enter 3000 . |

| Field | Setting |
|---|---|
| Client IP Address | Enter the new IP address you want to use for the PIMG unit. (This is the IP address that you enter in Cisco Unity Connection Administration when you create the integration.) |
| Client Subnet Mask | Enter the new subnet mask, if the subnet mask is different from the default IP address. |
| Default Network Gateway Address | Enter the IP address of the default network gateway router that the PIMG units use. |
| BOOTP Enabled | Select No . |

| Note | When running learn tones, the PIMG unit restarts after learning the first tone. |
|---|---|