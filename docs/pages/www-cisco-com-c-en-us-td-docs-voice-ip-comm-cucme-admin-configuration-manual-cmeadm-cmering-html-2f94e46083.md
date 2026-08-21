---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmering-html-2f94e46083
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmering.html
retrieved_at: 2026-08-21T07:24:01.205785+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Ringtones

## Chapter: Ringtones

# Ringtones

## Information About
                        	 Ringtones

### Distinctive Ringing

Distinctive ring is used to identify internal and external incoming
                              		calls. An internal call is defined as a call originating from any
                              		Cisco Unified  IP phone that is registered in Cisco Unified CME or is routed
                              		through the local FXS port.

In Cisco CME 3.4 and earlier versions, the standard ring pattern is
                              		generated for all calls to local SCCP endpoints. In Cisco Unified CME 4.0, the
                              		following distinctive ring features are supported for SCCP endpoints:

Specify one of three ring patterns to be used for all types of
                                    			 incoming calls to a particular directory number, on all phones on which the
                                    			 directory number appears. If a phone is already in use, an incoming call is
                                    			 presented as a call-waiting call and uses a distinctive call-waiting beep.

Specify whether the distinctive ring is used only if the incoming
                                    			 called number matches the primary or secondary number defined for the
                                    			 ephone-dn. If no secondary number is defined for the ephone-dn, the secondary
                                    			 ring option has no effect.

Associate a feature ring pattern with a specific button on a phone
                                    			 so that different phones that share the same directory number can use a
                                    			 different ring style.

For local SIP endpoints, the type of ring sound requested is signaled to
                              		the phone using an alert-info signal. If distinctive ringing is enabled,
                              		Cisco Unified CME generates the alert-info for incoming calls from any phone
                              		that is not registered in Cisco Unified CME, to the local endpoint. Alert-info
                              		from an incoming leg can be relayed to an outgoing leg with the internally
                              		generated alert-info taking precedence.

Cisco Unified IP phones use the standard Telcordia Technologies
                              		distinctive ring types.

### Customized
                           	 Ringtones

Cisco Unified IP
                              		Phones have two default ring types: Chirp1 and Chirp2. Cisco Unified CME also
                              		supports customized ringtones using pulse code modulation (PCM) files.

An XML file called
                              		RingList.xml specifies the ringtone options available for the default ring on
                              		an IP phone registered to Cisco Unified CME. An XML file called
                              		DistinctiveRingList.xml specifies the ringtones available on each individual
                              		line appearance on an IP phone registered to Cisco Unified CME.

### On-Hold
                           	 Indicator

On-hold indicator is
                              		an optional feature that generates a ring burst on idle IP phones that have
                              		placed a call on hold. An option is available to generate call-waiting beeps
                              		for occupied phones that have placed calls on hold. This feature is disabled by
                              		default. For configuration information, see Configure On-Hold Indicator .

LED color display
                              		for hold state, also known as I-Hold, is supported in Cisco Unified CME 4.0(2)
                              		and later versions. The I-Hold feature provides a visual indicator for
                              		distinguishing a local hold from a remote hold on shared lines on supported
                              		phones, such as the Cisco Unified IP Phone 7931G. This feature requires no
                              		additional configuration.

## Configure
                        	 Ringtones

### Configure
                           	 Distinctive Ringing

To set the ring
                                 		  pattern for all incoming calls to a directory number, perform the following
                                 		  steps.

#### Before you begin

Cisco Unified CME
                                 		  4.0 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag [ dual-line ]

- number number [ secondary number ] [ no-reg [ both | primary ] ]

- ring { external | internal | feature } [ primary | secondary ]

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone-dn dn-tag [ dual-line ]

#### Example:

```
Router(config)# ephone-dn 29
```

Enters
                                             				ephone-dn configuration mode, creates an ephone-dn, and optionally assigns it
                                             				dual-line status.

Step 4

number number [ secondary number ] [ no-reg [ both | primary ] ]

#### Example:

```
Router(config-ephone-dn)# number 2333
```

Configures a
                                             				valid extension number for this ephone-dn.

Step 5

ring { external | internal | feature } [ primary | secondary ]

#### Example:

```
Router(config-ephone-dn)# ring internal
```

Designates
                                             				which ring pattern to be used for all types of incoming calls to this directory
                                             				number, on all phones on which the directory number appears.

Step 6

end

#### Example:

```
Router(config-ephone-dn)# end
```

Returns to
                                             				privileged EXEC mode.

### Configure
                           	 Customized Ringtones

To create a
                                 		  customized ringtone, perform the following steps.

#### Before you begin

Cisco Unified CME
                                 		  4.0 or a later version.

Step 1

Create a PCM
                                          			 file for each customized ringtone (one ring per file). The PCM files must
                                          			 comply with the following format guidelines.

Raw PCM
                                                   					 (no header)

8000
                                                   					 samples per second

8 bits per
                                                   					 sample

mLaw
                                                   					 compression

Maximum
                                                   					 ring size—16080 samples

Minimum
                                                   					 ring size—240 samples

Number of
                                                   					 samples in the ring must be evenly divisible by 240

Ring
                                                   					 should start and end at the zero crossing

Use an audio
                                             				editing package that supports these file format requirements to create PCM
                                             				files for customized phone rings.

Sample ring files are in the ringtone.tar file at https://software.cisco.com/download/home/277641082

Step 2

Edit the
                                          			 RingList.xml and DistinctiveRingList.xml files using a text editor.

The
                                             				RingList.xml and DistinctiveRingList.xml files contain a list of phone ring
                                             				types. Each file shows the PCM file used for each ring type and the text that
                                             				is displayed on the Ring Type menu on a Cisco Unified IP Phone for each ring.

Sample XML files are in the ringtone.tar file at https://software.cisco.com/download/home/277641082

The
                                             				RingList.xml and DistinctiveRingList.xml files use the following format to
                                             				specify customized rings:

```
<CiscoIPPhoneRingList>
 <Ring>
  <DisplayName/>
  <FileName/>
 </Ring>
</CiscoIPPhoneRingList>
```

The XML ring
                                             				files use the following tag definitions:

Ring files
                                                   					 contain two fields, DisplayName and FileName, which are required for each phone
                                                   					 ring type. Up to 50 rings can be listed.

DisplayName defines the name of the customized ring for the
                                                   					 associated PCM file that will be displayed on the Ring Type menu of the Cisco
                                                   					 Unified IP Phone.

FileName
                                                   					 specifies the name of the PCM file for the customized ring to associate with
                                                   					 DisplayName.

The
                                                   					 DisplayName and FileName fields can not exceed 25 characters.

The following
                                             				sample RingList.xml file defines two phone ring types:

```
<CiscoIPPhoneRingList>
<Ring>
  <DisplayName>Piano1</DisplayName>
  <FileName>Piano1.raw</FileName>
  </Ring>
<Ring>
  <DisplayName>Chime</DisplayName>
  <FileName>Chime.raw</FileName>
  </Ring>
</CiscoIPPhoneRingList>
```

Step 3

Copy the PCM
                                          			 and XML files to system Flash on the Cisco Unified CME router. For example:

```
copy tftp://192.168.1.1/RingList.xml flash: copy tftp://192.168.1.1/DistinctiveRingList.xml flash: copy tftp://192.168.1.1/Piano1.raw flash: copy tftp://192.168.1.1/Chime.raw flash:
```

Step 4

Use the tftp-server command to enable access to the files. For example:

```
tftp-server flash:RingList.xml tftp-server flash:DistinctiveRingList.xml tftp-server flash:Piano1.raw tftp-server flash:Chime.raw
```

Step 5

Reboot the IP
                                          			 phones. After reboot, the IP phones download the XML and ringtone files. Select
                                          			 the customized ring by pressing the Settings button followed by the Ring Type
                                          			 menu option on a phone.

### Configure On-Hold
                           	 Indicator

The Call Hold
                                 		  feature is available by default. To define an audible indicator as a reminder
                                 		  that a call is waiting on hold, perform the following steps.

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag [ dual-line ]

- hold-alert timeout { idle | originator | shared | shared-idle } [ recurrence recurrence-timeout ] [ ring-silent-dn ]

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone-dn dn-tag [ dual-line ]

#### Example:

```
Router(config)# ephone-dn 20
```

Enters
                                             				ephone-dn configuration mode, creates an ephone-dn, and optionally assigns it
                                             				dual-line status.

Step 4

hold-alert timeout { idle | originator | shared | shared-idle } [ recurrence recurrence-timeout ] [ ring-silent-dn ]

#### Example:

```
Router(config-ephone-dn)# hold-alert 15 idle recurrence 3
```

Sets audible
                                             				alert notification on the Cisco Unified IP phone for alerting the user about
                                             				on-hold calls.

From the
                                                         				  perspective of the originator of the call on hold, the originator and shared keywords provide the same functionality.

Step 5

end

#### Example:

```
Router(config-ephone-dn)# end
```

Returns to
                                             				privileged EXEC mode.

### Enable Distinctive
                           	 Ringing on SIP Phones

To set the ring
                                 		  pattern for distinguishing between external and internal incoming calls,
                                 		  perform the following steps.

Restriction

bellcore-dr1 to
                                             			 bellcore-dr5 are the only Telcordia options that are supported for SIP phones.

#### Before you begin

Cisco Unified CME
                                 		  3.4 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- external-ring { bellcore-dr1 | bellcore-dr2 | bellcore-dr3 | bellcore-dr4 | bellcore-dr5 }

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice register global

#### Example:

```
Router(config)# voice register global
```

Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME.

Step 4

external-ring { bellcore-dr1 | bellcore-dr2 | bellcore-dr3 | bellcore-dr4 | bellcore-dr5 }

#### Example:

```
Router(config-register-global)# external-ring bellcore-dr3
```

Specifies the
                                             				type of audible ring sound to be used for external calls

Default—Internal ring sound is used for all incoming calls.

Step 5

end

#### Example:

```
Router(config-register-global)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

## Configuration
                        	 Examples for Ringtones

### Example for Configuring Distinctive Ringing for Internal Calls

The following example sets distinctive ringing for internal calls on
                                 		  extension 2333.

```
ephone-dn 34 number 2333 ring internal
```

### Example for Configuring On-Hold Indicator

In the following example, extension 2555 is configured to not forward
                                 		  local calls that are internal to the Cisco Unified CME system. Extension 2222
                                 		  dials extension 2555. If 2555 is busy, the caller hears a busy tone. If 2555
                                 		  does not answer, the caller hears ringback. The internal call is not forwarded.

```
ephone-dn 25 number 2555 no forward local-calls call-forward busy 2244 call-forward noan 2244 timeout 45
```

## Feature
                        	 Information for Ringtones

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature
                                          					 Name

Cisco Unified CME Version

Feature
                                          					 Information

Distinctive Ringing

4.0

Supports
                                          					 ringtone choices for all incoming calls to an individual directory number, for
                                          					 all SCCP phones on which the directory number appears.

3.4

Generate
                                          					 the alert-info for incoming calls from any phone that is not registered in
                                          					 Cisco Unified CME, to local SIP endpoints.

Customized
                                          					 Ringtones

4.0

Customized
                                          					 Ringtones feature was introduced.

On-Hold
                                          					 Indictor

4.0(2)

Controls
                                          					 LED color display for hold state to provide visual indicator for distinguishing
                                          					 a local hold from a remote hold on shared lines on supported phones, such as
                                          					 the Cisco Unified IP Phone 7931G.

2.0

Audible
                                          					 on-hold indicator was introduced.

1.0

Call Hold
                                          					 was introduced.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn dn-tag [ dual-line ] Example: Router(config)# ephone-dn 29 | Enters
                                             				ephone-dn configuration mode, creates an ephone-dn, and optionally assigns it
                                             				dual-line status. |
| Step 4 | number number [ secondary number ] [ no-reg [ both \| primary ] ] Example: Router(config-ephone-dn)# number 2333 | Configures a
                                             				valid extension number for this ephone-dn. |
| Step 5 | ring { external \| internal \| feature } [ primary \| secondary ] Example: Router(config-ephone-dn)# ring internal | Designates
                                             				which ring pattern to be used for all types of incoming calls to this directory
                                             				number, on all phones on which the directory number appears. |
| Step 6 | end Example: Router(config-ephone-dn)# end | Returns to
                                             				privileged EXEC mode. |

| Step 1 | Create a PCM
                                          			 file for each customized ringtone (one ring per file). The PCM files must
                                          			 comply with the following format guidelines. Raw PCM
                                                   					 (no header) 8000
                                                   					 samples per second 8 bits per
                                                   					 sample mLaw
                                                   					 compression Maximum
                                                   					 ring size—16080 samples Minimum
                                                   					 ring size—240 samples Number of
                                                   					 samples in the ring must be evenly divisible by 240 Ring
                                                   					 should start and end at the zero crossing Use an audio
                                             				editing package that supports these file format requirements to create PCM
                                             				files for customized phone rings. Sample ring files are in the ringtone.tar file at https://software.cisco.com/download/home/277641082 |
|---|---|
| Step 2 | Edit the
                                          			 RingList.xml and DistinctiveRingList.xml files using a text editor. The
                                             				RingList.xml and DistinctiveRingList.xml files contain a list of phone ring
                                             				types. Each file shows the PCM file used for each ring type and the text that
                                             				is displayed on the Ring Type menu on a Cisco Unified IP Phone for each ring. Sample XML files are in the ringtone.tar file at https://software.cisco.com/download/home/277641082 The
                                             				RingList.xml and DistinctiveRingList.xml files use the following format to
                                             				specify customized rings: <CiscoIPPhoneRingList>
 <Ring>
  <DisplayName/>
  <FileName/>
 </Ring>
</CiscoIPPhoneRingList> The XML ring
                                             				files use the following tag definitions: Ring files
                                                   					 contain two fields, DisplayName and FileName, which are required for each phone
                                                   					 ring type. Up to 50 rings can be listed. DisplayName defines the name of the customized ring for the
                                                   					 associated PCM file that will be displayed on the Ring Type menu of the Cisco
                                                   					 Unified IP Phone. FileName
                                                   					 specifies the name of the PCM file for the customized ring to associate with
                                                   					 DisplayName. The
                                                   					 DisplayName and FileName fields can not exceed 25 characters. The following
                                             				sample RingList.xml file defines two phone ring types: <CiscoIPPhoneRingList>
<Ring>
  <DisplayName>Piano1</DisplayName>
  <FileName>Piano1.raw</FileName>
  </Ring>
<Ring>
  <DisplayName>Chime</DisplayName>
  <FileName>Chime.raw</FileName>
  </Ring>
</CiscoIPPhoneRingList> |
| Step 3 | Copy the PCM
                                          			 and XML files to system Flash on the Cisco Unified CME router. For example: copy tftp://192.168.1.1/RingList.xml flash: copy tftp://192.168.1.1/DistinctiveRingList.xml flash: copy tftp://192.168.1.1/Piano1.raw flash: copy tftp://192.168.1.1/Chime.raw flash: |
| Step 4 | Use the tftp-server command to enable access to the files. For example: tftp-server flash:RingList.xml tftp-server flash:DistinctiveRingList.xml tftp-server flash:Piano1.raw tftp-server flash:Chime.raw |
| Step 5 | Reboot the IP
                                          			 phones. After reboot, the IP phones download the XML and ringtone files. Select
                                          			 the customized ring by pressing the Settings button followed by the Ring Type
                                          			 menu option on a phone. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn dn-tag [ dual-line ] Example: Router(config)# ephone-dn 20 | Enters
                                             				ephone-dn configuration mode, creates an ephone-dn, and optionally assigns it
                                             				dual-line status. |
| Step 4 | hold-alert timeout { idle \| originator \| shared \| shared-idle } [ recurrence recurrence-timeout ] [ ring-silent-dn ] Example: Router(config-ephone-dn)# hold-alert 15 idle recurrence 3 | Sets audible
                                             				alert notification on the Cisco Unified IP phone for alerting the user about
                                             				on-hold calls. Note From the
                                                         				  perspective of the originator of the call on hold, the originator and shared keywords provide the same functionality. | Note | From the
                                                         				  perspective of the originator of the call on hold, the originator and shared keywords provide the same functionality. |
| Note | From the
                                                         				  perspective of the originator of the call on hold, the originator and shared keywords provide the same functionality. |
| Step 5 | end Example: Router(config-ephone-dn)# end | Returns to
                                             				privileged EXEC mode. |

| Note | From the
                                                         				  perspective of the originator of the call on hold, the originator and shared keywords provide the same functionality. |
|---|---|

| Restriction | bellcore-dr1 to
                                             			 bellcore-dr5 are the only Telcordia options that are supported for SIP phones. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register global Example: Router(config)# voice register global | Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME. |
| Step 4 | external-ring { bellcore-dr1 \| bellcore-dr2 \| bellcore-dr3 \| bellcore-dr4 \| bellcore-dr5 } Example: Router(config-register-global)# external-ring bellcore-dr3 | Specifies the
                                             				type of audible ring sound to be used for external calls Default—Internal ring sound is used for all incoming calls. |
| Step 5 | end Example: Router(config-register-global)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

| Feature
                                          					 Name | Cisco Unified CME Version | Feature
                                          					 Information |
|---|---|---|
| Distinctive Ringing | 4.0 | Supports
                                          					 ringtone choices for all incoming calls to an individual directory number, for
                                          					 all SCCP phones on which the directory number appears. |
| 3.4 | Generate
                                          					 the alert-info for incoming calls from any phone that is not registered in
                                          					 Cisco Unified CME, to local SIP endpoints. |
| Customized
                                          					 Ringtones | 4.0 | Customized
                                          					 Ringtones feature was introduced. |
| On-Hold
                                          					 Indictor | 4.0(2) | Controls
                                          					 LED color display for hold state to provide visual indicator for distinguishing
                                          					 a local hold from a remote hold on shared lines on supported phones, such as
                                          					 the Cisco Unified IP Phone 7931G. |
| 2.0 | Audible
                                          					 on-hold indicator was introduced. |
| 1.0 | Call Hold
                                          					 was introduced. |