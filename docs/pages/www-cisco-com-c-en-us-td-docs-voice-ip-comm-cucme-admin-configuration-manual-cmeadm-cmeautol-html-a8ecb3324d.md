---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmeautol-html-a8ecb3324d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeautol.html
retrieved_at: 2026-08-21T07:24:28.799116+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Automatic Line
	 Selection

## Chapter: Automatic Line
	 Selection

# Automatic Line
                     	 Selection

This chapter
                        		describes automatic line selection feature in Cisco Unified Communications
                        		Manager Express (Cisco Unified CME).

This feature is
                                    		  applicable for SCCP phones only. For newer SIP phones (Cisco Unified IP Phone
                                    		  7800, 8800 series) with new user interface, this feature is not applicable. The
                                    		  user selects the line and the focus would be on that selected line. Both
                                    		  incoming and outgoing calls changes the focus based on the line selected or
                                    		  line answered.

## Information About Automatic Line Selection

### Automatic Line Selection for Incoming and Outgoing Calls

On multiline IP phones, lifting the handset automatically selects the
                              		first ringing line on the phone or, if no line is ringing, selects the first
                              		available idle line for outgoing calls. This is the default behavior for all
                              		multiline IP phones.

Under some circumstances, however, you might want to require that a line
                              		button be explicitly pressed to select an outgoing line or to answer an
                              		incoming call. In Cisco CME 3.0 and later, you have the flexibility to assign
                              		the type of line selection that each IP phone uses.

The Automatic Line Selection feature allows you to specify, on a
                              		per-phone basis, the line that is selected when you pick up a phone handset.

Any of the following behaviors can be assigned on a per-phone basis:

Automatic line selection—Picking up the handset answers the first
                                    			 ringing line or, if no line is ringing, selects the first idle line. Use the auto-line command with no keyword or
                                    			 argument. This is the default.

Manual line selection (no automatic line selection)—Pressing the
                                    			 Answer soft key answers the first ringing line, and pressing a line button
                                    			 selects a line for an outgoing call. Picking up the handset does not answer
                                    			 calls or provide dial tone. Use the no auto-line command.

Automatic line selection for incoming calls only—Picking up the
                                    			 handset answers the first ringing line, but if no line is ringing, it does not
                                    			 select an idle line for an outgoing call. Pressing a line button selects a line
                                    			 for an outgoing call. Use the auto-line incoming command.

Automatic line selection for outgoing calls only—Picking up the
                                    			 handset for an outgoing call selects the line associated with the button-number argument. If a button number
                                    			 is specified and the line associated with that button is unavailable (because
                                    			 it is a shared line in use on another phone), no dial tone is heard when the
                                    			 handset is lifted. You must press an available line button to make an outgoing
                                    			 call. Incoming calls must be answered by pressing the Answer soft key or
                                    			 pressing a ringing line button. Use the auto-line command with the button-number argument.

Automatic line selection for incoming and outgoing calls—Pressing
                                    			 the Answer soft key or picking up the handset answers an incoming call on the
                                    			 line associated with the specified button. Picking up the handset for outgoing
                                    			 calls selects the line associated with the specified button. Use the auto-line command with the button-number argument and answer-incoming keyword.

## Configure Automatic Line Selection

### Enable Automatic
                           	 Line Selection

To enable
                                 		  automatic line selection for answering incoming calls or making outgoing calls,
                                 		  perform the following steps:

Restriction

Automatic line
                                             			 selection is bypassed if it is configured for a trunk directory number and the
                                             			 line is seized by pressing the Park or Callfwd soft keys. The first available
                                             			 directory number is seized.

### SUMMARY STEPS

- enable

- configure terminal

- ephone phone-tag

- auto-line [ button-number [ answer-incoming ] | incoming ]

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

ephone phone-tag

#### Example:

```
Router(config)# ephone 24
```

Enters ephone
                                             				configuration mode.

phone-tag —Unique sequence number for the phone on
                                                   					 which you want to configure automatic line selection.

Step 4

auto-line [ button-number [ answer-incoming ] | incoming ]

#### Example:

```
Router(config-ephone)# auto-line 5 answer-incoming
```

Assigns a type
                                             				of line selection behavior to this phone.

auto-line —Picking up the handset answers the first
                                                   					 ringing line or, if no line is ringing, selects the first idle line. This is
                                                   					 the default.

auto-line button-number —Picking up the handset for an
                                                   					 outgoing call selects the line associated with the specified button. The
                                                   					 default if this argument is not used is the topmost available line.

auto-line button-number answer-incoming —Picking up the handset answers the
                                                   					 incoming call on the line associated with the specified button.

auto-line incoming —Picking up the handset answers
                                                   					 the first ringing line but, if no line is ringing, does not select an idle line
                                                   					 for an outgoing call. Pressing a line button selects a line for an outgoing
                                                   					 call.

no auto-line —Disables automatic line selection.
                                                   					 Pressing the Answer soft key answers the first ringing line, and pressing a
                                                   					 line button selects a line for an outgoing call. Picking up the handset does
                                                   					 not answer calls or provide dial tone.

Step 5

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

### Verify Automatic
                           	 Line Selection

Step 1

Use the show
                                                				  running-config command to verify your configuration. Automatic
                                          			 line selection is listed in the ephone portion of the output.

#### Example:

```
Router# show running-config ephone  2
headset auto-answer line 1
headset auto-answer line 4
ephone-template 1
mac-address 011F.9010.1790
paging-dn 48
type 7960
no dnd feature-ring
no auto-line
```

Step 2

Use the show
                                                				  telephony-service ephone command to display only ephone
                                          			 configuration information.

#### Example:

```
Router# show telephony-service ephone ephone 4
 device-security-mode none
 username "Accounting"
 mac-address FF0E.4857.5E91
 button 1c34,35
 no auto-line
```

## Configuration Examples for Automatic Line Selection

### Example for
                           	 Automatic Line Selection

The following
                                 		  example assigns no automatic line selection to phones 1 and 2 and assigns
                                 		  automatic line selection for incoming calls only to phone 3:

```
ephone 1
mac-address 00e0.8646.9242
button 1:1 2:4 3:16
no auto-line
!
ephone 2
mac-address 01c0.4612.7142
button 1:5 2:4 3:16
no auto-line
!
ephone 3
mac-address 10b8.8945.3251
button 1:6 2:4 3:16
auto-line incoming
```

The following
                                 		  example enables automatic selection of line button 1 when the handset is lifted
                                 		  to answer incoming calls or to make outgoing calls.

```
ephone  1
mac-address 0001.0002.0003
type 7960
auto-line 1 answer-incoming
button  1:1 2:2 3:3
```

## Feature
                        	 Information for Automatic Line Selection

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature
                                          					 Name

Cisco Unified CME Version

Feature
                                          					 Information

Automatic
                                          					 Line Selection

4.0

The answer-incoming keyword was added to the auto-line command.

3.1

The button-number argument was added to the auto-line command.

3.0

Automatic
                                          					 line selection was introduced.

| Note | This feature is
                                    		  applicable for SCCP phones only. For newer SIP phones (Cisco Unified IP Phone
                                    		  7800, 8800 series) with new user interface, this feature is not applicable. The
                                    		  user selects the line and the focus would be on that selected line. Both
                                    		  incoming and outgoing calls changes the focus based on the line selected or
                                    		  line answered. |
|---|---|

| Restriction | Automatic line
                                             			 selection is bypassed if it is configured for a trunk directory number and the
                                             			 line is seized by pressing the Park or Callfwd soft keys. The first available
                                             			 directory number is seized. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone phone-tag Example: Router(config)# ephone 24 | Enters ephone
                                             				configuration mode. phone-tag —Unique sequence number for the phone on
                                                   					 which you want to configure automatic line selection. |
| Step 4 | auto-line [ button-number [ answer-incoming ] \| incoming ] Example: Router(config-ephone)# auto-line 5 answer-incoming | Assigns a type
                                             				of line selection behavior to this phone. auto-line —Picking up the handset answers the first
                                                   					 ringing line or, if no line is ringing, selects the first idle line. This is
                                                   					 the default. auto-line button-number —Picking up the handset for an
                                                   					 outgoing call selects the line associated with the specified button. The
                                                   					 default if this argument is not used is the topmost available line. auto-line button-number answer-incoming —Picking up the handset answers the
                                                   					 incoming call on the line associated with the specified button. auto-line incoming —Picking up the handset answers
                                                   					 the first ringing line but, if no line is ringing, does not select an idle line
                                                   					 for an outgoing call. Pressing a line button selects a line for an outgoing
                                                   					 call. no auto-line —Disables automatic line selection.
                                                   					 Pressing the Answer soft key answers the first ringing line, and pressing a
                                                   					 line button selects a line for an outgoing call. Picking up the handset does
                                                   					 not answer calls or provide dial tone. |
| Step 5 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

| Step 1 | Use the show
                                                				  running-config command to verify your configuration. Automatic
                                          			 line selection is listed in the ephone portion of the output. Example: Router# show running-config ephone  2
headset auto-answer line 1
headset auto-answer line 4
ephone-template 1
mac-address 011F.9010.1790
paging-dn 48
type 7960
no dnd feature-ring
no auto-line |
|---|---|
| Step 2 | Use the show
                                                				  telephony-service ephone command to display only ephone
                                          			 configuration information. Example: Router# show telephony-service ephone ephone 4
 device-security-mode none
 username "Accounting"
 mac-address FF0E.4857.5E91
 button 1c34,35
 no auto-line |

| Feature
                                          					 Name | Cisco Unified CME Version | Feature
                                          					 Information |
|---|---|---|
| Automatic
                                          					 Line Selection | 4.0 | The answer-incoming keyword was added to the auto-line command. |
| 3.1 | The button-number argument was added to the auto-line command. |
| 3.0 | Automatic
                                          					 line selection was introduced. |