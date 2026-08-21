---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmereset-html-6e8485a63b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmereset.html
retrieved_at: 2026-08-21T07:22:34.294028+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Reset and Restart
	 Cisco Unified IP Phones

## Chapter: Reset and Restart
	 Cisco Unified IP Phones

# Reset and Restart
                     	 Cisco Unified IP Phones

## Information About Resetting and Restarting Phones

### Differences
                           	 between Resetting and Restarting IP Phones

Cisco Unified IP
                              		phones must be rebooted after configuration changes in order for the changes to
                              		be effective. Configurations for phones in Cisco Unified CME are downloaded
                              		when a phone is rebooted or reset. You can reboot a single phone or you can
                              		reboot all phones in a Cisco Unified CME system. The differences between reboot
                              		types are summarized in Table 1 .

When rebooting
                                          		  multiple IP phones, it is possible for a conflict to occur if too many phones
                                          		  attempt to access changed Cisco Unified CME configuration information via TFTP
                                          		  simultaneously.

reset
                                          				  Command

restart
                                          				  Command

Type of
                                             					 Reboot

Similar to
                                          				  power-off, power-on reboot.

Quick
                                          				  restart.

Phone
                                             					 Configurations

Downloads
                                          				  configurations for IP phones.

Downloads
                                          				  configurations for IP phones.

DHCP and
                                             					 TFTP

Contacts
                                          				  DHCP and TFTP servers for updated configuration information.

This
                                                      					 command was introduced for SIP phones in Cisco CME 3.4.

Phones
                                          				  contact the TFTP server for updated configuration information and reregister
                                          				  without contacting the DHCP server.

This
                                                      					 command was introduced for SIP phones in Cisco Unified CME 4.1.

Processing Time

Takes longer
                                          				  to process when updating multiple phones.

Faster
                                          				  processing for multiple phones.

When
                                             					 Required

Date and
                                                						time settings

Network
                                                						locale

Phone
                                                						firmware

Source
                                                						address

TFTP
                                                						path

URL
                                                						parameters

User
                                                						locale

Voicemail access number

Can be used
                                          				  when updating the following:

Directory numbers

Phone
                                                						buttons

Speed-dial numbers

Directory numbers

Phone
                                                						buttons

Speed-dial numbers

### Cisco Unified CME
                           	 TAPI Enhancement

Before
                              		Cisco Unified CME 7.0(1), the only method to clear a session between a
                              		Microsoft Windows Workstation and an SCCP phone that was out-of-sync was to
                              		reboot the router. In Cisco Unified CME 7.0(1) and later versions, you can
                              		clear a Telephony Application Programming Interface (TAPI) session that is in a
                              		frozen state or out of synchronization by using a Cisco IOS software command.
                              		For configuration information, see Reset a Session Between a TAPI Application and an SCCP Phone .

This enhancement
                              		also automatically handles ephone-TAPI registration error conditions. No
                              		additional configuration is required for this new feature.

## Reset and Restart Phones

If phones are not yet plugged in, resetting or restarting phones is
                                       		  not necessary. Instead, connect your IP phones to your network to boot the
                                       		  phone and download the required configuration files.

### Use the reset
                           	 Command on SCCP Phones

To reboot and
                                 		  reregister one or more SCCP phones, including contacting the DHCP server for
                                 		  updated information, perform the following steps.

#### Before you begin

Phones to be
                                       				rebooted are connected to the Cisco Unified CME router.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service or ephone ephone-tag

- reset { all [ time-interval ] | cancel | mac-address mac-address | sequence-all } or reset

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

telephony-service or ephone ephone-tag

#### Example:

```
Router(config)# telephony-service
```

```
Router(config)# ephone 1
```

Enters
                                             				telephony-service configuration mode.

Enters ephone
                                             				configuration mode.

Step 4

reset { all [ time-interval ] | cancel | mac-address mac-address | sequence-all } or reset

#### Example:

```
Router(config-telephony)# reset all
```

```
Router(config-ephone)# reset
```

Performs a
                                             				complete reboot of the specified or all phones running SCCP, including
                                             				contacting the DHCP and TFTP servers for the latest configuration information.

Performs a
                                             				complete reboot of the individual SCCP phone being configured.

Step 5

end

#### Example:

```
Router(config-telephony)# end
```

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

### Use the restart
                           	 Command on SCCP Phones

To fast reboot and
                                 		  reregister one or more SCCP phones, perform the following steps.

#### Before you begin

Phones to be
                                       				rebooted are connected to the Cisco Unified CME router.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service or ephone ephone-tag

- restart { all [ time-interval ] | mac-address } or restart

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

telephony-service or ephone ephone-tag

#### Example:

```
Router(config)# telephony-service
or
Router(config)# ephone 1
```

Enters
                                             				telephony-service configuration mode.

Enters ephone
                                             				configuration mode.

Step 4

restart { all [ time-interval ] | mac-address } or restart

#### Example:

```
Router(config-telephony)# restart all
```

```
Router(config-ephone)# restart
```

Performs a
                                             				fast reboot of the specified phone or all phones running SCCP associated with
                                             				this Cisco Unified CME router. Does not contact the DHCP server for updated
                                             				information.

Performs a
                                             				fast reboot of the individual SCCP phone being configured.

Step 5

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

### Reset a Session
                           	 Between a TAPI Application and an SCCP Phone

To clear a TAPI
                                 		  session that is in a frozen state or out of synchronization, perform the
                                 		  following steps.

#### Before you begin

Cisco Unified CME 7.0(1) or a later version

### SUMMARY STEPS

- enable

- configure terminal

- ephone phone-tag

- reset tapi

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
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone phone-tag

#### Example:

```
Router(config)# ephone 36
```

Enters ephone
                                             				configuration mode.

phone-tag —Unique sequence number that identifies
                                                   					 this ephone during configuration tasks.

Step 4

reset tapi

#### Example:

```
Router(config-ephone)# reset tapi
```

Resets the
                                             				connection between a Telephony Application Programmer's Interface (TAPI)
                                             				application and the SCCP phone.

Step 5

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

### Use the reset
                           	 Command on SIP Phones

To reboot and
                                 		  reregister one or more SIP phones, including contacting the DHCP server for
                                 		  updated information, perform the following steps.

#### Before you begin

Cisco Unified CME 3.4 or later.

The mode cme
                                       				command must be enabled in Cisco Unified CME.

Phones to be
                                       				rebooted are connected to the Cisco Unified CME router.

### SUMMARY STEPS

- enable

- configure terminal

- voice register
                                       				  global or voice register pool pool-tag

- reset

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

voice register
                                                				  global or voice register pool pool-tag

#### Example:

```
Router(config)# voice register global
```

```
Router(config)# voice register pool 1
```

Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME.

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for SIP
                                             				phones

Step 4

reset

#### Example:

```
Router(config-register-global)# reset
```

```
Router(config-register-pool)# reset
```

Performs a
                                             				complete reboot of all phones connected to this router that are running SIP,
                                             				including contacting the DHCP and TFTP servers for the latest configuration
                                             				information.

Performs a
                                             				complete reboot of the individual SIP phone being configured.

Step 5

end

#### Example:

```
Router(config-register-global)# end
```

```
Router(config-register-pool)# end
```

Exits to
                                             				privileged EXEC mode.

### Use the restart
                           	 Command on SIP Phones

To fast reboot and
                                 		  reregister one or more SIP phones, perform the following steps.

#### Before you begin

Cisco Unified CME 4.1 or later.

The mode cme
                                       				command must be enabled in Cisco Unified CME.

Phones to be
                                       				rebooted are connected to the Cisco Unified CME router.

### SUMMARY STEPS

- enable

- configure terminal

- voice register
                                       				  global or voice register
                                       				  pool pool-tag

- restart

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

voice register
                                                				  global or voice register
                                                				  pool pool-tag

#### Example:

```
Router(config)# voice register global
```

```
Router(config)# voice register pool 1
```

Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME.

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for SIP
                                             				phones.

Step 4

restart

#### Example:

```
Router(config-register-global)# restart
```

```
Router(config-register-pool)# restart
```

Performs a
                                             				fast reboot all SIP phones associated with this Cisco Unified CME router. Does
                                             				not contact the DHCP server for updated information.

Performs a
                                             				fast reboot of the individual SIP phone being configured.

Step 5

end

#### Example:

```
Router(config-register-global)# end
```

```
Router(config-register-pool)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

### Verify Basic Call

To verify that Cisco IP phones in Cisco Unified CME can place and
                                 		  receive calls through the voice ports, perform the following steps.

Step 1

Test local phone operation. Make calls between phones on the
                                          			 Cisco Unified CME router.

Step 2

Place a call from a phone in Cisco Unified CME to a number in the local
                                          			 calling area.

Step 3

Place a call to a phone in Cisco Unified CME from a phone outside this
                                          			 Cisco Unified CME system.

## Feature
                        	 Information for Reset and Restart Phones

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature
                                             					 Name

Cisco Unified CME Version

Feature
                                             					 Information

Cisco Unified CME TAPI Enhancement

7.0(1)

Disassociates and reestablishes a TAPI session that is in a
                                             					 frozen state or out of synchronization by using a Cisco IOS command. This
                                             					 enhancement also automatically handles ephone-TAPI registration error
                                             					 conditions.

| Note | When rebooting
                                          		  multiple IP phones, it is possible for a conflict to occur if too many phones
                                          		  attempt to access changed Cisco Unified CME configuration information via TFTP
                                          		  simultaneously. |
|---|---|

|  | reset
                                          				  Command | restart
                                          				  Command |
|---|---|---|
| Type of
                                             					 Reboot | Similar to
                                          				  power-off, power-on reboot. | Quick
                                          				  restart. |
| Phone
                                             					 Configurations | Downloads
                                          				  configurations for IP phones. | Downloads
                                          				  configurations for IP phones. |
| DHCP and
                                             					 TFTP | Contacts
                                          				  DHCP and TFTP servers for updated configuration information. Note This
                                                      					 command was introduced for SIP phones in Cisco CME 3.4. | Note | This
                                                      					 command was introduced for SIP phones in Cisco CME 3.4. | Phones
                                          				  contact the TFTP server for updated configuration information and reregister
                                          				  without contacting the DHCP server. Note This
                                                      					 command was introduced for SIP phones in Cisco Unified CME 4.1. | Note | This
                                                      					 command was introduced for SIP phones in Cisco Unified CME 4.1. |
| Note | This
                                                      					 command was introduced for SIP phones in Cisco CME 3.4. |
| Note | This
                                                      					 command was introduced for SIP phones in Cisco Unified CME 4.1. |
| Processing Time | Takes longer
                                          				  to process when updating multiple phones. | Faster
                                          				  processing for multiple phones. |
| When
                                             					 Required | Date and
                                                						time settings Network
                                                						locale Phone
                                                						firmware Source
                                                						address TFTP
                                                						path URL
                                                						parameters User
                                                						locale Voicemail access number Can be used
                                          				  when updating the following: Directory numbers Phone
                                                						buttons Speed-dial numbers | Directory numbers Phone
                                                						buttons Speed-dial numbers |

| Note | This
                                                      					 command was introduced for SIP phones in Cisco CME 3.4. |
|---|---|

| Note | This
                                                      					 command was introduced for SIP phones in Cisco Unified CME 4.1. |
|---|---|

| Note | If phones are not yet plugged in, resetting or restarting phones is
                                       		  not necessary. Instead, connect your IP phones to your network to boot the
                                       		  phone and download the required configuration files. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service or ephone ephone-tag Example: Router(config)# telephony-service or Router(config)# ephone 1 | Enters
                                             				telephony-service configuration mode. or Enters ephone
                                             				configuration mode. |
| Step 4 | reset { all [ time-interval ] \| cancel \| mac-address mac-address \| sequence-all } or reset Example: Router(config-telephony)# reset all or Router(config-ephone)# reset | Performs a
                                             				complete reboot of the specified or all phones running SCCP, including
                                             				contacting the DHCP and TFTP servers for the latest configuration information. or Performs a
                                             				complete reboot of the individual SCCP phone being configured. |
| Step 5 | end Example: Router(config-telephony)# end or Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service or ephone ephone-tag Example: Router(config)# telephony-service
or
Router(config)# ephone 1 | Enters
                                             				telephony-service configuration mode. or Enters ephone
                                             				configuration mode. |
| Step 4 | restart { all [ time-interval ] \| mac-address } or restart Example: Router(config-telephony)# restart all or Router(config-ephone)# restart | Performs a
                                             				fast reboot of the specified phone or all phones running SCCP associated with
                                             				this Cisco Unified CME router. Does not contact the DHCP server for updated
                                             				information. or Performs a
                                             				fast reboot of the individual SCCP phone being configured. |
| Step 5 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone phone-tag Example: Router(config)# ephone 36 | Enters ephone
                                             				configuration mode. phone-tag —Unique sequence number that identifies
                                                   					 this ephone during configuration tasks. |
| Step 4 | reset tapi Example: Router(config-ephone)# reset tapi | Resets the
                                             				connection between a Telephony Application Programmer's Interface (TAPI)
                                             				application and the SCCP phone. |
| Step 5 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register
                                                				  global or voice register pool pool-tag Example: Router(config)# voice register global or Router(config)# voice register pool 1 | Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME. or Enters voice
                                             				register pool configuration mode to set phone-specific parameters for SIP
                                             				phones |
| Step 4 | reset Example: Router(config-register-global)# reset or Router(config-register-pool)# reset | Performs a
                                             				complete reboot of all phones connected to this router that are running SIP,
                                             				including contacting the DHCP and TFTP servers for the latest configuration
                                             				information. or Performs a
                                             				complete reboot of the individual SIP phone being configured. |
| Step 5 | end Example: Router(config-register-global)# end or Router(config-register-pool)# end | Exits to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register
                                                				  global or voice register
                                                				  pool pool-tag Example: Router(config)# voice register global or Router(config)# voice register pool 1 | Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME. or Enters voice
                                             				register pool configuration mode to set phone-specific parameters for SIP
                                             				phones. |
| Step 4 | restart Example: Router(config-register-global)# restart or Router(config-register-pool)# restart | Performs a
                                             				fast reboot all SIP phones associated with this Cisco Unified CME router. Does
                                             				not contact the DHCP server for updated information. or Performs a
                                             				fast reboot of the individual SIP phone being configured. |
| Step 5 | end Example: Router(config-register-global)# end or Router(config-register-pool)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

| Step 1 | Test local phone operation. Make calls between phones on the
                                          			 Cisco Unified CME router. |
|---|---|
| Step 2 | Place a call from a phone in Cisco Unified CME to a number in the local
                                          			 calling area. |
| Step 3 | Place a call to a phone in Cisco Unified CME from a phone outside this
                                          			 Cisco Unified CME system. |

| Feature
                                             					 Name | Cisco Unified CME Version | Feature
                                             					 Information |
|---|---|---|
| Cisco Unified CME TAPI Enhancement | 7.0(1) | Disassociates and reestablishes a TAPI session that is in a
                                             					 frozen state or out of synchronization by using a Cisco IOS command. This
                                             					 enhancement also automatically handles ephone-TAPI registration error
                                             					 conditions. |