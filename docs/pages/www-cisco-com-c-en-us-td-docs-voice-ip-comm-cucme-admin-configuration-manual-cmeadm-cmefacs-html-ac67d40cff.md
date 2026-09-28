---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmefacs-html-ac67d40cff
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmefacs.html
retrieved_at: 2026-08-21T07:23:31.360054+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Feature Access Codes

## Chapter: Feature Access Codes

# Feature Access Codes

## Information About Feature Access Codes

### Feature Access
                           	 Codes

Feature Access Codes (FACs) are special patterns of characters for dialing from a phone keypad to invoke particular features.
                              For example, you can press **1, then press 2345 to forward all incoming calls to extension 2345.

Invokes FACs using a short sequence of digits for dialing the keypad on an analog phone. Similarly, on an IP phone you can
                              select softkeys to invoke the same features. In Cisco Unified Communications Manager Express 4.0 and later, enable the same
                              FACs that are available for analog phones on IP phones. It allows you to select a particular feature or activate and deactivate
                              a function in the same manner regardless of the phone type.

Disable FACs on IP phones until they are explicitly enabled. You can enable all standard FACs for all registered SCCP phones
                              in Cisco Unified Communications Manager Express. Similarly you can define a custom FAC or alias to enable one or more individual
                              FACs.

All FACs except the call-park FAC are valid only immediately after a phone is off hook. The call-park FAC is considered transfer
                              to a call-park slot and therefore is only valid after initiating transfer using the Transfer softkey (IP phones) or hookflash
                              (analog phones).

Configured directory numbers on the Cisco Unified Communications Manager Express router cannot overlap with the numbers you
                                          assign for FAC Standard or FAC Custom in a FAC configuration. Also, ensure that the FAC code always starts with an asterisk,
                                          followed by digits.

```
telephony-service fac custom
dnd *54 
ephone-hunt hlog-phone *5432
```

Table 1 Contains a list of the standard predefined FACs.

Standard FAC

Description

**1 plus
                                          				  optional extension number

Call Forward All.

**2

Call forward
                                          				  all cancel.

**3

Select a local group.

**4 plus
                                          				  group number

Select an incoming call in the specified pickup group. Specified pickup group must be already configured in Cisco Unified
                                          Communications Manager Express.

**5 plus
                                          				  extension number

Select a direct extension.

**6 plus
                                          				  optional park-slot number

Call park, if you have an active call and if you press the Transfer softkey (IP phone) or hookflash (analog phone) before
                                          dialing this FAC. Configure the target park slot in Cisco Unified Communications Manager Express.

**7

Do Not Disturb.

**8

Redial.

**9

Dial voicemail number.

*3 plus hunt
                                          				  group pilot number

Join ephone-hunt group. If you have created multiple hunt groups allowing dynamic membership, identify the joining hunt group
                                          by its pilot number.

*4

Activate or deactivate the hunt group logout functionality to toggle between ready or not-ready status of an extension when
                                          the hunt group agent is off-hook.

*5

Activate or deactivate a phone-level hunt group logout to toggle between ready or not-ready status of all extensions on an
                                          individual phone. The individual phone member must be of an ephone hunt group when the phone is idle.

*6

Dials the voicemail number.

#3

Leave ephone-hunt group. Configure the Phone or extension number as a dynamic member of a hunt group.

For FAC feature to work on SIP phones configuring call-park system application under telephony-service is mandatory. The following FAC is supported with SIP phones:

CALL_PICKUP - Allows a phone user to answer a call that is ringing on another phone by pressing the FAC digit **5 and then
                                                dialing the extension.

GROUP_PICKUP - Allows a phone user to answer a call that is ringing phone in any pickup group by pressing the FAC digit **3
                                                and then dialing the pickup group number.

LOCAL_GPICKUP - Allows a phone user to select a call that is ringing on another phone by pressing the FAC digit **4  and then
                                                the asterisk (*) if both phones are in the same pickup group.

DPARK_RETRIEVE - Allows a phone user to retrieve a parked call on an SCCP phone by pressing the FAC digit *0 and dialing the
                                                extension number of the call-park slot.

REGULAR_PARK - Allows a phone user to place a call on hold by pressing the FAC digit **6 at a special extension so it can
                                                be retrieved from any other phone in the system.

VOICE_HUNTGRP_JOIN - Allows a phone user to join to or from voice hunt groups by selecting the Join FAC digit *3 which is
                                                displayed on the voice hunt group page.

VOICE_HUNTGRP_UNJOIN_ALL - Allows a phone user to unjoin from all voice hunt groups by selecting the unJoin FAC digit #4 which
                                                is displayed on the voice hunt group page.

VOICE_HUNTGRP_UNJOIN_PARTICULAR - Allows a phone user to unjoin from a particular voice hunt group by selecting the unJoin
                                                FAC digit #4 which is displayed on the voice hunt group page.

VOICE_HUNTGRP_TEMP_LOGOUT - Allows a phone user to use the HLog FAC digit *5 to change from the ready to not-ready status
                                                or from the not-ready to ready status.

SIP_NIGHT_SERVICE_CODE - Allows a phone user to enter a night-service code to toggle night-service treatment on and off from
                                                any phone that is assigned to the night service.

### Restrictions

DND is not supported for Analog SCCP devices.

## Configure Feature
                        	 Access Codes

To
                              		  enable standard FACs or create custom FACs, perform the following steps:

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- call-park system application

- fac { standard | custom { alias alias-tag
                                    				  custom-fac to existing-fac [ extra-digits ]} | feature custom-fac }}

- end

### DETAILED STEPS

Step 1

enable

### Example:

```
Router> enable
```

Enables
                                          				privileged EXEC mode.

Enter your
                                                					 password if prompted.

Step 2

configure terminal

### Example:

```
Router# configure terminal
```

Enters global
                                          				configuration mode.

Step 3

telephony-service

### Example:

```
Router(config)# telephony-service
```

Enters
                                          				telephony-service configuration mode.

Step 4

call-park system application

### Example:

```
Router(config-telephony)# call-park system application
```

Configure call-park system application for FAC feature to work on SIP phones.

Step 5

fac { standard | custom { alias alias-tag
                                             				  custom-fac to existing-fac [ extra-digits ]} | feature custom-fac }}

### Example:

```
Router(config-telephony)# fac custom callfwd *#5
```

Enables
                                          				standard FACs or creates a custom FAC or alias.

standard —Enables standard FACs for all phones.

custom —Creates a custom FAC for a FAC type.

alias —Creates a custom FAC for an existing FAC or an existing FAC plus extra digits.

alias-tag —Unique identifying number for this
                                                					 alias. Range: 0 to 9.

custom-fac —User-defined code to be dialed using
                                                					 the keypad on an IP or analog phone. Custom FAC can be up to 256 characters
                                                					 long and contain numbers 0 to  9 and * and #.

to —Maps custom FAC to specified target.

existing-fac —Already configured custom FAC that is
                                                					 automatically dialed when the phone user dials the custom FAC being configured.

extra-digits —(Optional) Additional digits that are
                                                					 automatically dialed when the phone user dials the custom FAC being configured.

feature —Predefined alphabetic string that
                                                					 identifies a particular feature or function. Type ? for a list.

Step 6

end

### Example:

```
Router(config-telephony)# end
```

Returns to
                                          				privileged EXEC mode.

## Verify Feature
                        	 Access Codes

To verify the FAC
                              		  configuration, perform the following step.

show telephony-service fac

### Example:

This command
                                          				displays a list of FACs that are configured on the Cisco Unified CME router.
                                          				The following example shows the output when standard FACs are enabled:

```
Router# show telephony-service fac telephony-service fac standard
 callfwd all **1
 callfwd cancel **2
 pickup local **3
 pickup group **4
 pickup direct **5
 park **6
 dnd **7
 redial **8
 voicemail **9
 ephone-hunt join *3
 ephone-hunt cancel #3
 ephone-hunt hlog *4
 ephone-hunt hlog-phone *5
 trnsfvm *6
```

The following
                                          				example shows the output when custom FACs are configured:

```
Router# show telephony-service fac telephony-service fac custom
 callfwd all #45
 alias 0 #1 to **4121
 alias 1 #2 to **4122
 alias 4 #4 to **4124
```

## Configuration Examples for Feature Access Codes

### Example for Enabling Standard FACs for All Phones

The following example shows how to enable standard FACs for all
                                 		  phones:

```
Router# telephony-service Router(config-telephony)# fac standard fac standard is set!
Router(config-telephony)#
```

The following example shows how the standard FAC for the Call Forward
                                 		  All feature is changed to a custom FAC (#45). Then an alias is created to map a
                                 		  second custom fac to #45 plus an extension (1111). The custom FAC (#44) allows
                                 		  the phone user to press #44 to forward all calls to extension 1111, without
                                 		  requiring the phone user to dial the extra digits that are the extension
                                 		  number.

```
Router# telephony-service Router(config-telephony)# fac custom callfwd all #45 fac callfwd all code has been configured to #45
Router(config-telephony)# fac custom alias 0 #44 to #451111 fac alias0 code has been configurated to #44!
alias0 map code has been configurated to #451111!
```

The following example shows how to define an alias for the group
                                 		  pickup of group 123. The alias substitutes the digits #4 for the standard FAC
                                 		  for group pickup (**4) and adds the group number (123) to the dial pattern.
                                 		  Using this custom FAC, a phone user can dial #4 to pick up a ringing call in
                                 		  group 123, instead of dialing the standard FAC **4 plus the group number 123.

```
Router# telephony-service Router(config-telephony)# fac custom alias 5 #4 to **4123
```

## Feature
                        	 Information for Feature Access Codes

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature
                                          					 Name

Cisco Unified CME Version

Feature
                                          					 Information

Transfer
                                          					 to Voice Mail.

7.0/4.3

FAC for
                                          					 Transfer to Voice Mail was added.

Feature
                                          					 Access Codes (FACs)

4.0

FACs were
                                          					 introduced.

| Note | Configured directory numbers on the Cisco Unified Communications Manager Express router cannot overlap with the numbers you
                                          assign for FAC Standard or FAC Custom in a FAC configuration. Also, ensure that the FAC code always starts with an asterisk,
                                          followed by digits. |
|---|---|

| Note | For Custom FAC configuration, two FAC codes cannot overlap with one another. A sample configuration (with 54 overlapping)
                                          that you must avoid, is as follows: telephony-service fac custom
dnd *54 
ephone-hunt hlog-phone *5432 |
|---|---|

| Standard FAC | Description |
|---|---|
| **1 plus
                                          				  optional extension number | Call Forward All. |
| **2 | Call forward
                                          				  all cancel. |
| **3 | Select a local group. |
| **4 plus
                                          				  group number | Select an incoming call in the specified pickup group. Specified pickup group must be already configured in Cisco Unified
                                          Communications Manager Express. |
| **5 plus
                                          				  extension number | Select a direct extension. |
| **6 plus
                                          				  optional park-slot number | Call park, if you have an active call and if you press the Transfer softkey (IP phone) or hookflash (analog phone) before
                                          dialing this FAC. Configure the target park slot in Cisco Unified Communications Manager Express. |
| **7 | Do Not Disturb. |
| **8 | Redial. |
| **9 | Dial voicemail number. |
| *3 plus hunt
                                          				  group pilot number | Join ephone-hunt group. If you have created multiple hunt groups allowing dynamic membership, identify the joining hunt group
                                          by its pilot number. |
| *4 | Activate or deactivate the hunt group logout functionality to toggle between ready or not-ready status of an extension when
                                          the hunt group agent is off-hook. |
| *5 | Activate or deactivate a phone-level hunt group logout to toggle between ready or not-ready status of all extensions on an
                                          individual phone. The individual phone member must be of an ephone hunt group when the phone is idle. |
| *6 | Dials the voicemail number. |
| #3 | Leave ephone-hunt group. Configure the Phone or extension number as a dynamic member of a hunt group. |

| Note | For FAC feature to work on SIP phones configuring call-park system application under telephony-service is mandatory. The following FAC is supported with SIP phones: CALL_PICKUP - Allows a phone user to answer a call that is ringing on another phone by pressing the FAC digit **5 and then
                                                dialing the extension. GROUP_PICKUP - Allows a phone user to answer a call that is ringing phone in any pickup group by pressing the FAC digit **3
                                                and then dialing the pickup group number. LOCAL_GPICKUP - Allows a phone user to select a call that is ringing on another phone by pressing the FAC digit **4  and then
                                                the asterisk (*) if both phones are in the same pickup group. DPARK_RETRIEVE - Allows a phone user to retrieve a parked call on an SCCP phone by pressing the FAC digit *0 and dialing the
                                                extension number of the call-park slot. REGULAR_PARK - Allows a phone user to place a call on hold by pressing the FAC digit **6 at a special extension so it can
                                                be retrieved from any other phone in the system. VOICE_HUNTGRP_JOIN - Allows a phone user to join to or from voice hunt groups by selecting the Join FAC digit *3 which is
                                                displayed on the voice hunt group page. VOICE_HUNTGRP_UNJOIN_ALL - Allows a phone user to unjoin from all voice hunt groups by selecting the unJoin FAC digit #4 which
                                                is displayed on the voice hunt group page. VOICE_HUNTGRP_UNJOIN_PARTICULAR - Allows a phone user to unjoin from a particular voice hunt group by selecting the unJoin
                                                FAC digit #4 which is displayed on the voice hunt group page. VOICE_HUNTGRP_TEMP_LOGOUT - Allows a phone user to use the HLog FAC digit *5 to change from the ready to not-ready status
                                                or from the not-ready to ready status. SIP_NIGHT_SERVICE_CODE - Allows a phone user to enter a night-service code to toggle night-service treatment on and off from
                                                any phone that is assigned to the night service. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                          				privileged EXEC mode. Enter your
                                                					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                          				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters
                                          				telephony-service configuration mode. |
| Step 4 | call-park system application Example: Router(config-telephony)# call-park system application | Configure call-park system application for FAC feature to work on SIP phones. |
| Step 5 | fac { standard \| custom { alias alias-tag
                                             				  custom-fac to existing-fac [ extra-digits ]} \| feature custom-fac }} Example: Router(config-telephony)# fac custom callfwd *#5 | Enables
                                          				standard FACs or creates a custom FAC or alias. standard —Enables standard FACs for all phones. custom —Creates a custom FAC for a FAC type. alias —Creates a custom FAC for an existing FAC or an existing FAC plus extra digits. alias-tag —Unique identifying number for this
                                                					 alias. Range: 0 to 9. custom-fac —User-defined code to be dialed using
                                                					 the keypad on an IP or analog phone. Custom FAC can be up to 256 characters
                                                					 long and contain numbers 0 to  9 and * and #. to —Maps custom FAC to specified target. existing-fac —Already configured custom FAC that is
                                                					 automatically dialed when the phone user dials the custom FAC being configured. extra-digits —(Optional) Additional digits that are
                                                					 automatically dialed when the phone user dials the custom FAC being configured. feature —Predefined alphabetic string that
                                                					 identifies a particular feature or function. Type ? for a list. |
| Step 6 | end Example: Router(config-telephony)# end | Returns to
                                          				privileged EXEC mode. |

| show telephony-service fac Example: This command
                                          				displays a list of FACs that are configured on the Cisco Unified CME router.
                                          				The following example shows the output when standard FACs are enabled: Router# show telephony-service fac telephony-service fac standard
 callfwd all **1
 callfwd cancel **2
 pickup local **3
 pickup group **4
 pickup direct **5
 park **6
 dnd **7
 redial **8
 voicemail **9
 ephone-hunt join *3
 ephone-hunt cancel #3
 ephone-hunt hlog *4
 ephone-hunt hlog-phone *5
 trnsfvm *6 The following
                                          				example shows the output when custom FACs are configured: Router# show telephony-service fac telephony-service fac custom
 callfwd all #45
 alias 0 #1 to **4121
 alias 1 #2 to **4122
 alias 4 #4 to **4124 |
|---|

| Feature
                                          					 Name | Cisco Unified CME Version | Feature
                                          					 Information |
|---|---|---|
| Transfer
                                          					 to Voice Mail. | 7.0/4.3 | FAC for
                                          					 Transfer to Voice Mail was added. |
| Feature
                                          					 Access Codes (FACs) | 4.0 | FACs were
                                          					 introduced. |