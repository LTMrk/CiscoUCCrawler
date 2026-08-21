---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmeclid-html-2b9b1ab145
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeclid.html
retrieved_at: 2026-08-21T07:25:05.971112+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Caller ID Blocking

## Chapter: Caller ID Blocking

# Caller ID Blocking

## Restrictions for Caller ID Blocking

Caller ID blocking on outbound calls does not apply to PSTN calls
                           		through foreign exchange office (FXO) ports. Caller ID features on
                           		FXO-connected subscriber lines are under the control of the PSTN service
                           		provider, who may require you to subscribe to their caller ID blocking service.

## Information About Caller ID Blocking

### Caller ID Blocking on Outbound Calls

Phone users can block caller-ID displays on calls from a particular
                              		ephone-dn, or you can selectively choose to block the name or number on
                              		outbound calls from a particular dial peer.

The display of caller ID information for outgoing calls
                              		from a particular ephone-dn can be blocked on a per-call basis, allowing users
                              		to maintain their privacy when necessary. The system administrator defines a
                              		code for caller ID blocking in Cisco Unified CME. Users then dial the code
                              		before making any call on which they do not want their number displayed on the
                              		called-party phone. The caller ID is sent, but its presentation parameter is
                              		set to “restricted” so that the caller ID is not displayed.

Blocking CLID displays for local calls from a particular extension tells
                              		the far-end gateway device to block display of calling-party information for
                              		the calls received from this ephone-dn.

Alternatively, you can allow the local display of CLID information and
                              		independently block the CLID name or number on outbound VoIP calls. This
                              		configuration has the benefit of allowing caller-ID display for local calls
                              		while preventing caller-ID display for external calls going over VoIP. This
                              		feature can be used for PSTN calls that go out over ISDN.

## Configure Caller ID Blocking

### Block Caller ID
                           	 For All Outbound Calls on SCCP Phones

To block the CLID
                                 		  name or number on outbound VoIP calls from a particular dial peer, perform the
                                 		  following steps.

Restriction

Caller ID
                                                   				  continues to be displayed for local calls. To block caller ID display on all
                                                   				  outbound calls from a particular directory number, use the caller-id block command. See Block Caller ID From a Directory Number on SCCP Phones or Verify Caller ID Blocking .

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice tag [ pots | voip ]

- clid strip

- clid strip name

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

dial-peer voice tag [ pots | voip ]

#### Example:

```
Router(config)# dial-peer voice 3 voip
```

Enters
                                             				dial-peer configuration mode.

You can
                                                         				  configure caller-ID blocking on POTS dial peers if the POTS interface is ISDN.
                                                         				  This feature is not available on FXO/CAS lines.

Step 4

clid strip

#### Example:

```
Router(config-dial-peer)# clid strip
```

(Optional)
                                             				Removes the calling-party number from the CLID information being sent with VoIP
                                             				calls.

Step 5

clid strip name

#### Example:

```
Router(config-dial-peer)# clid strip name
```

(Optional)
                                             				Removes the calling-party name from the CLID information being sent with VoIP
                                             				calls.

Step 6

end

#### Example:

```
Router(config-dial-peer)# end
```

Returns to
                                             				privileged EXEC mode.

### Block Caller ID
                           	 From a Directory Number on SCCP Phones

To define a code
                                 		  that phone users can dial to block caller ID display on selected outbound calls
                                 		  from a particular directory number or to block caller ID display on all calls
                                 		  from a directory number, perform the following steps.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- caller-id block code code-string

- exit

- ephone-dn dn-tag

- caller-id block

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router# enable
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

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 4

caller-id block code code-string

#### Example:

```
Router(config-telephony)# caller-id block code *1234
```

(Optional)
                                             				Defines a code that users can enter before making calls on which the caller ID
                                             				should not be displayed.

code-string —Digit string of up to 16 characters.
                                                   					 The first character must be an asterisk (*).

Step 5

exit

#### Example:

```
Router(config-telephony)# exit
```

Exits
                                             				telephony-service configuration mode.

Step 6

ephone-dn dn-tag

#### Example:

```
Router(config)# ephone-dn 3
```

Enters
                                             				ephone-dn configuration mode.

Step 7

caller-id block

#### Example:

```
Router(config-ephone-dn)# caller-id block
```

(Optional)
                                             				Blocks display of caller-ID information for all outbound calls that originate
                                             				from this directory number.

This command
                                             				can also be configured in ephone-dn-template configuration mode and applied to
                                             				one or more directory number. The ephone-dn configuration has priority over the
                                             				ephone-dn-template configuration.

Step 8

end

#### Example:

```
Router(config-dial-peer)# end
```

Returns to
                                             				privileged EXEC mode.

### Verify Caller ID
                           	 Blocking

Use the show
                                                				  running-config command to display caller ID blocking parameters,
                                          			 which may appear in the telephony-service, ephone-dn, or dial-peer portions of
                                          			 the output.

#### Example:

```
Router# show running-config dial-peer voice 450002 voip
		   translation-profile outgoing 457-456
		   destination-pattern 457
		   session target ipv4:10.43.31.81
		   dtmf-relay h245-alphanumeric
		   codec g711ulaw
		   no vad
		   clid strip
		  !
		  telephony-service
		   fxo hook-flash
		   load 7960-7940 P00305000600
		   load 7914 S00103020002
		   max-ephones 100
		   max-dn 500
		   ip source-address 10.115.34.131 port 2000
		   max-redirect 20
		   no service directed-pickup
		   timeouts ringing 10
		   system message XYZ Company
		   voicemail 7189
		   max-conferences 8 gain -6
		   moh music-on-hold.au
		   caller-id block code *1234
		   web admin system name cisco password cisco
		   dn-webedit 
		   time-webedit 
		   transfer-system full-consult
		   transfer-pattern 92......
		   transfer-pattern 91..........
		   transfer-pattern 93......
		   transfer-pattern 94......
		   transfer-pattern 95......
		   transfer-pattern 96......
		   transfer-pattern 97......
		   transfer-pattern 98......
		   transfer-pattern .T
		   secondary-dialtone 9
		   after-hours block pattern 1 91900 7-24
		   after-hours block pattern 2 9976 7-24
		  !
		   create cnf-files version-stamp 7960 Jul 13 2004 03:39:28
		  !
		  ephone-dn  2  dual-line
		   number 126
		   preference 1
		   call-forward busy 500
		   caller-id block
```

## Configuration Examples for Caller ID Blocking

### Example for Configuring Caller ID Blocking Code

The following example defines a code of *1234 for phone users to enter
                                 		  to block caller ID on their outgoing calls:

```
telephony-service
 caller-id block code *1234
```

### Example for Configuring Caller ID Blocking for Outbound Calls from a
                           	 Directory Number on SCCP Phones

The following example sets CLID blocking for the ephone-dn with tag 3.

```
ephone-dn 3
		 number 2345
		 caller-id block
```

The following example blocks the display of CLID name and number on
                                 		  VoIP calls but allows CLID display for local calls:

```
ephone-dn 3
		 number 2345
		dial-peer voice 2 voip
		 clid strip
		 clid strip name
```

## Feature
                        	 Information for Caller ID Blocking

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Cisco Unified CME Version

Feature Information

Caller ID Blocking

3.0

Caller ID blocking per local call was introduced.

1.0

Caller ID blocking for outbound calls was introduced.

| Restriction | Caller ID
                                                   				  continues to be displayed for local calls. To block caller ID display on all
                                                   				  outbound calls from a particular directory number, use the caller-id block command. See Block Caller ID From a Directory Number on SCCP Phones or Verify Caller ID Blocking . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | dial-peer voice tag [ pots \| voip ] Example: Router(config)# dial-peer voice 3 voip | Enters
                                             				dial-peer configuration mode. Note You can
                                                         				  configure caller-ID blocking on POTS dial peers if the POTS interface is ISDN.
                                                         				  This feature is not available on FXO/CAS lines. | Note | You can
                                                         				  configure caller-ID blocking on POTS dial peers if the POTS interface is ISDN.
                                                         				  This feature is not available on FXO/CAS lines. |
| Note | You can
                                                         				  configure caller-ID blocking on POTS dial peers if the POTS interface is ISDN.
                                                         				  This feature is not available on FXO/CAS lines. |
| Step 4 | clid strip Example: Router(config-dial-peer)# clid strip | (Optional)
                                             				Removes the calling-party number from the CLID information being sent with VoIP
                                             				calls. |
| Step 5 | clid strip name Example: Router(config-dial-peer)# clid strip name | (Optional)
                                             				Removes the calling-party name from the CLID information being sent with VoIP
                                             				calls. |
| Step 6 | end Example: Router(config-dial-peer)# end | Returns to
                                             				privileged EXEC mode. |

| Note | You can
                                                         				  configure caller-ID blocking on POTS dial peers if the POTS interface is ISDN.
                                                         				  This feature is not available on FXO/CAS lines. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router# enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 4 | caller-id block code code-string Example: Router(config-telephony)# caller-id block code *1234 | (Optional)
                                             				Defines a code that users can enter before making calls on which the caller ID
                                             				should not be displayed. code-string —Digit string of up to 16 characters.
                                                   					 The first character must be an asterisk (*). |
| Step 5 | exit Example: Router(config-telephony)# exit | Exits
                                             				telephony-service configuration mode. |
| Step 6 | ephone-dn dn-tag Example: Router(config)# ephone-dn 3 | Enters
                                             				ephone-dn configuration mode. |
| Step 7 | caller-id block Example: Router(config-ephone-dn)# caller-id block | (Optional)
                                             				Blocks display of caller-ID information for all outbound calls that originate
                                             				from this directory number. This command
                                             				can also be configured in ephone-dn-template configuration mode and applied to
                                             				one or more directory number. The ephone-dn configuration has priority over the
                                             				ephone-dn-template configuration. |
| Step 8 | end Example: Router(config-dial-peer)# end | Returns to
                                             				privileged EXEC mode. |

| Use the show
                                                				  running-config command to display caller ID blocking parameters,
                                          			 which may appear in the telephony-service, ephone-dn, or dial-peer portions of
                                          			 the output. Example: Router# show running-config dial-peer voice 450002 voip
		   translation-profile outgoing 457-456
		   destination-pattern 457
		   session target ipv4:10.43.31.81
		   dtmf-relay h245-alphanumeric
		   codec g711ulaw
		   no vad
		   clid strip
		  !
		  telephony-service
		   fxo hook-flash
		   load 7960-7940 P00305000600
		   load 7914 S00103020002
		   max-ephones 100
		   max-dn 500
		   ip source-address 10.115.34.131 port 2000
		   max-redirect 20
		   no service directed-pickup
		   timeouts ringing 10
		   system message XYZ Company
		   voicemail 7189
		   max-conferences 8 gain -6
		   moh music-on-hold.au
		   caller-id block code *1234
		   web admin system name cisco password cisco
		   dn-webedit 
		   time-webedit 
		   transfer-system full-consult
		   transfer-pattern 92......
		   transfer-pattern 91..........
		   transfer-pattern 93......
		   transfer-pattern 94......
		   transfer-pattern 95......
		   transfer-pattern 96......
		   transfer-pattern 97......
		   transfer-pattern 98......
		   transfer-pattern .T
		   secondary-dialtone 9
		   after-hours block pattern 1 91900 7-24
		   after-hours block pattern 2 9976 7-24
		  !
		   create cnf-files version-stamp 7960 Jul 13 2004 03:39:28
		  !
		  ephone-dn  2  dual-line
		   number 126
		   preference 1
		   call-forward busy 500
		   caller-id block |
|---|

| Feature Name | Cisco Unified CME Version | Feature Information |
|---|---|---|
| Caller ID Blocking | 3.0 | Caller ID blocking per local call was introduced. |
| 1.0 | Caller ID blocking for outbound calls was introduced. |