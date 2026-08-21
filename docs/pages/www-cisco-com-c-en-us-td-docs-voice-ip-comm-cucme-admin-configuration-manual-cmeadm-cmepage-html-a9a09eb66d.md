---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmepage-html-a9a09eb66d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmepage.html
retrieved_at: 2026-08-21T07:23:52.781442+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Paging

## Chapter: Paging

# Paging

## Restrictions for Paging

Paging is not supported on IP phones without speaker phones.

Paging is not supported on Cisco Unified 3905 SIP IP phones.

Paging is only supported on G711ulaw codec.

Cisco Unified IP Conference Phone 8831 does not support paging when busy.

Paging Group is supported in Unified CME, but not in Unified SRST.

Paging is not supported on Cisco Unified 3905 SIP IP phones.

Cisco Unified SCCP IP phones do not support Whisper Paging. Only idle IP phones can receive paging requests.

## Information About Paging

### Audio
                           	 Paging

A paging number can
                              		be defined to relay audio pages to a group of designated phones. When a caller
                              		dials the paging number (ephone-dn), each idle IP phone that has been
                              		configured with the paging number automatically answers using its speaker-phone
                              		mode. Displays on the phones that answer the page show the caller ID that has
                              		been set using the name command
                              		under the paging ephone-dn. When the caller finishes speaking the message and
                              		hangs up, the phones are returned to their idle states.

Audio paging
                              		provides a one-way voice path to the phones that have been designated to
                              		receive paging. It does not have a press-to-answer option like the intercom
                              		feature. A paging group is created using a dummy ephone-dn, known as the paging
                              		ephone-dn, that can be associated with any number of local IP phones. The
                              		paging ephone-dn can be dialed from anywhere, including on-net.

After you have
                              		created two or more simple paging groups, you can unite them into combined
                              		paging groups. By creating combined paging groups, you provide phone users with
                              		the flexibility to page a small local paging group (for example, paging four
                              		phones in a store’s jewelry department) or to page a combined set of several
                              		paging groups (for example, by paging a group that consists of both the jewelry
                              		department and the accessories department).

The paging mechanism
                              		supports audio distribution using IP multicast, replicated unicast, and a
                              		mixture of both (so that multicast is used where possible, and unicast is used
                              		for specific phones that cannot be reached using multicast).

Paging
                                 		  Group shows a paging group with two phones.

### Paging Group
                           	 Support for Cisco Unified SIP IP Phones

Paging provides a
                              		one-way voice path from the paging phone to the paged phone. The paged phone
                              		automatically answers the page in speaker-phone mode with Mute activated.

The paged phone
                              		receives a page when it is idle or busy. When it is busy with a connected call,
                              		the user of the paged phone can hear both the active conversation and whisper
                              		paging.

Before Cisco Unified
                              		CME 9.0, you can specify a paging-dn tag and dial the paging extension number
                              		to page the Cisco Unified SCCP IP phone associated with the paging-dn tag or
                              		paging group using the paging-dn command in ephone or ephone-template configuration mode. You can also page a
                              		combined paging group composed of two or more previously established paging
                              		groups of Cisco Unified SCCP IP phone directory numbers using the paging group command in ephone-dn configuration mode.

In Cisco Unified CME
                              		9.0 and later versions, support is extended so that you can specify a paging-dn
                              		tag and dial the paging extension number to page the Cisco Unified SIP IP phone
                              		associated with the paging-dn tag or paging group using the paging-dn command in voice register pool or voice
                              		register template configuration mode. Paging on Cisco Unified SIP IP phones
                              		support both unicast and multicast paging in the same way that these features
                              		are supported on Cisco Unified SCCP IP Phones.

In Cisco Unified CME
                              		9.0 and later versions, support is also extended so that you can create a
                              		combined paging group composed of two or more previously established paging
                              		groups of ephone and voice register directory numbers using the same paging group command used for paging groups of Cisco Unified SCCP IP phone directory
                              		numbers.

The paging port
                                          		  for Cisco Unified SIP IP phones is an even number from 20480 to 32768. If you
                                          		  enter a wrong port number, a SIP REFER message request is sent to the IP phone
                                          		  but the Cisco Unified SIP IP phone is not paged.

With a paging-dn,
                              		there is only one paging endpoint and there is only one paging number for both
                              		Cisco Unified SCCP and Cisco Unified SIP IP phones. However, when paging to a
                              		Cisco Unified SIP shared line, each phone on the shared line is treated
                              		separately.

A phone that can be
                              		paged by two paging-dns receives the page from the first paging-dn and ignores
                              		the page from the second paging-dn. When the first paging-dn is disconnected,
                              		the phone can receive the page from the second paging-dn.

The paging group
                              		support for Cisco Unified SIP IP phones uses an ephone paging-dn to dial the
                              		paging number before branching out to each Cisco Unified SCCP and Cisco Unified
                              		SIP IP phone.

The show ephone-dn
                                    			 paging command displays which paging-dn is specified and which
                              		phone is being paged.

Because paging is
                              		not considered a call, a paging phone that is in a connected state can press
                              		another line to make a call using the phone’s softkeys.

The Cisco Unified
                              		SIP IP phone Paging feature also supports:

multicast paging
                                    			 (default)

unicast paging

For more
                              		information, see Configure Paging Group Support for SIP IP Phones .

## Configure Paging

### Configure a Simple
                           	 Paging Group on SCCP Phones

To set up a paging
                                 		  number that relays incoming pages to a group of phones, perform the following
                                 		  steps.

Restriction

IP phones do not
                                             			 support multicast at 224.x.x.x addresses.

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn paging-dn-tag

- number number

- name name

- paging [ ip multicast-address port udp-port-number ]

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

ephone-dn paging-dn-tag

#### Example:

```
Router(config)# ephone-dn 42
```

Enters
                                             				ephone-dn configuration mode.

paging-dn-tag —A unique sequence number that
                                                   					 identifies this paging ephone-dn during all configuration tasks. This is the
                                                   					 ephone-dn that is dialed to initiate a page. This ephone-dn is not associated
                                                   					 with a physical phone. Range is 1 to 288.

Do not use
                                                         				  the dual-line keyword with this command. Paging ephone-dns cannot be dual-line.

Step 4

number number

#### Example:

```
Router(config-ephone-dn)# number 3556
```

Defines an
                                             				extension number associated with the paging ephone-dn. This is the number that
                                             				people call to initiate a page.

Step 5

name name

#### Example:

```
Router(config-ephone-dn)# name paging4
```

Assigns to the
                                             				paging number a name to appear in caller-ID displays and directories.

Step 6

paging [ ip multicast-address port udp-port-number ]

#### Example:

```
Router(config-ephone-dn)# paging ip 239.1.1.10 port 2000
```

Specifies that
                                             				this ephone-dn is to be used to broadcast paging messages to the idle IP phones
                                             				that are associated with the paging dn-tag. If the optional keywords and
                                             				arguments are not used, IP phones are paged individually using IP unicast
                                             				transmission (to a maximum of ten IP phones). The optional keywords and
                                             				arguments are as follows:

ip multicast-address port udp-port-number —Specifies multicast broadcast
                                                   					 using the specified IP address and UDP port. When multiple paging numbers are
                                                   					 configured, each paging number must use a unique IP multicast address. We
                                                   					 recommend port 2000 because it is already used for normal non-multicast RTP
                                                   					 media streams between phones and the Cisco Unified CME router.

IP phones do
                                                         				  not support multicast at 224.x.x.x addresses.

The correct
                                                         				  paging port for the paging-dn of Cisco Unified SIP IP phones is an even number
                                                         				  from 20480 to 32768. If you enter a wrong port number, a SIP REFER message
                                                         				  request is sent to the IP phone but the Cisco Unified SIP IP phone is not
                                                         				  paged.

Step 7

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

### Configure a
                           	 Combined Paging Group for SCCP Phones

To set up a
                                 		  combined paging group consisting of two or more simple paging groups, perform
                                 		  the following steps.

#### Before you begin

Simple paging
                                 		  groups must be configured. See Configure a Simple Paging Group on SCCP Phones .

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn paging-dn-tag

- number number

- name name

- paging group paging-dn-tag , paging-dn-tag [ [ , paging-dn-tag ] ... ]

- exit

- ephone phone-tag

- paging-dn paging-dn-tag { multicast | unicast }

- exit

- Repeat
                                 			 Step 8 to Step 10 to add additional IP phones to a paging group.

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

ephone-dn paging-dn-tag

#### Example:

```
Router(config)# ephone-dn 42
```

Enters
                                             				ephone-dn configuration mode to create a paging number for a combined paging
                                             				group.

paging-dn-tag —A unique sequence number that
                                                   					 identifies this paging ephone-dn during all configuration tasks. This is the
                                                   					 ephone-dn that is dialed to initiate a page. This ephone-dn is not associated
                                                   					 with a physical phone. Range is 1 to 288.

Do not use
                                                         				  the dual-line keyword with this command. Paging ephone-dns cannot be dual-line.

Step 4

number number

#### Example:

```
Router(config-ephone-dn)# number 3556
```

Defines an
                                             				extension number associated with the combined group paging ephone-dn. This is
                                             				the number that people call to initiate a page to the combined group.

Step 5

name name

#### Example:

```
Router(config-ephone-dn)# name paging4
```

(Optional)
                                             				Assigns to the combined group paging number a name to appear in caller-ID
                                             				displays and directories.

Step 6

paging group paging-dn-tag , paging-dn-tag [ [ , paging-dn-tag ] ... ]

#### Example:

```
Router(config-ephone-dn)# paging group 20,21
```

Sets the
                                             				paging directory number for a combined group. This command combines the
                                             				individual paging group ephone-dns that you specify into a combined group so
                                             				that a page can be sent to more than one paging group at a time.

paging-dn-tag —Unique sequence number associated
                                                   					 with the paging number for an individual paging group. Lists the paging-dn-tags
                                                   					 of all the individual groups that you want to include in this combined group,
                                                   					 separated by commas. You can include up to ten paging ephone-dn tags in this
                                                   					 command.

Configure
                                                         				  the paging command for all ephone-dns in a paging group before configuring the
                                                         				  paging group command for that group.

Step 7

exit

#### Example:

```
Router(config-ephone-dn)# exit
```

Exits
                                             				ephone-dn configuration mode.

Step 8

ephone phone-tag

#### Example:

```
Router(config)# ephone 2
```

Enters ephone
                                             				configuration mode to add IP phones to the paging group.

phone-tag —Unique sequence number of a phone to
                                                   					 receive audio pages when the paging ephone-dn is called.

Step 9

paging-dn paging-dn-tag { multicast | unicast }

#### Example:

```
Router(config-ephone)# paging-dn 42 multicast
```

Associates
                                             				this ephone with an ephone-dn tag that is used for a paging ephone-dn (the
                                             				number that people call to deliver a page). Note that the paging ephone-dn tag
                                             				is not associated with a line button on this ephone.

The paging
                                             				mechanism supports audio distribution using IP multicast, replicated unicast,
                                             				and a mixture of both (so that multicast is used where possible and unicast is
                                             				allowed to specific phones that cannot be reached through multicast).

paging-dn-tag —Unique sequence number for a paging
                                                   					 ephone-dn.

multicast —(Optional) Multicast paging for groups.
                                                   					 By default, paging is transmitted to the Cisco Unified IP phone using
                                                   					 multicast.

unicast —(Optional) Unicast paging for a single
                                                   					 Cisco Unified IP phone. This keyword indicates that the Cisco Unified IP phone
                                                   					 is not capable of receiving paging through multicast and requests that the
                                                   					 phone receive paging through a unicast transmission directed to the individual
                                                   					 phone.

The number
                                                         				  of phones supported through unicast is limited to a maximum of ten phones.

Step 10

exit

#### Example:

```
Router(config-ephone)# exit
```

Exits ephone
                                             				configuration mode.

Step 11

Repeat
                                          			 Step 8 to Step 10 to add additional IP phones to a paging group.

—

Step 12

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

### Configure Paging
                           	 Group Support for SIP IP Phones

To configure Paging group support for Unified SIP IP Phones, perform the following steps.

#### Before you begin

Cisco Unified CME
                                 		  9.0 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag

- number number

- paging [ ip multicast-address port udp-port-number ]

- Repeat Step 3
                                 			 to Step 5 to add more Cisco Unified SCCP IP phones to the paging group. Skip
                                 			 Step 7 for each IP phone except for the last one.

- paging group paging-dn-tag , paging-dn-tag

- exit

- voice register dn dn-tag

- number number

- exit

- Repeat
                                 			 Step 9 to Step 11 to associate more telephone or extension numbers with Cisco
                                 			 Unified SIP IP phones.

- voice register pool pool-tag

- id mac address

- type phone-type

- number tag dn dn-tag

- paging-dn paging-dn-tag

- Repeat
                                 			 Step 13 to Step 17 to register additional Cisco Unified SIP IP phones to
                                 			 ephone-dn paging directory numbers. Exit from voice register pool configuration
                                 			 mode after each additional phone is registered. After the last phone is added,
                                 			 go directly to Step 19.

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

ephone-dn dn-tag

#### Example:

```
Router(config)# ephone-dn 20
```

Enters
                                             				ephone-dn configuration mode.

dn-tag —Unique number that identifies an ephone-dn
                                                   					 during configuration tasks. Range is 1 to the number set by the max-dn command.

Step 4

number number

#### Example:

```
Router(config-ephone-dn)# number 2000
```

Associates a
                                             				telephone or extension number with this ephone-dn.

number —String of up to 16 characters that
                                                   					 represents an E.164 telephone number. Normally, the string is composed of
                                                   					 digits, but the string may contain alphabetic characters when the number is
                                                   					 dialed only by the router, as with an intercom number. One or more periods (.)
                                                   					 can be used as wildcard characters.

Step 5

paging [ ip multicast-address port udp-port-number ]

#### Example:

```
Router(config-ephone-dn)# paging ip 239.0.1.20 port 20480
```

Defines an
                                             				extension (ephone-dn) as a paging extension that can be called to broadcast an
                                             				audio page to a set of Cisco Unified IP phones.

ip multicast-address —(Optional) Uses an IP multicast
                                                   					 address to multicast voice packets for audio paging; for example, 239.0.1.1.

IP phones do
                                                         				  not support multicast at 224.x.x.x addresses. Default is that multicast is not
                                                         				  used and IP phones are paged individually using IP unicast transmission (up to
                                                         				  ten phones).

port udp-port-number —(Optional) Uses this UDP port for
                                                   					 the multicast. Range: 2000 to 65535.

If any of
                                                         				  the paged phones is a Cisco Unified SIP IP phone, the correct paging port for
                                                         				  the paging-dn is an even number from 20480 to 32768. If you enter a wrong port
                                                         				  number, a SIP REFER message request is sent to the IP phone but the Cisco
                                                         				  Unified SIP IP phone is not paged.

Step 6

Repeat Step 3
                                          			 to Step 5 to add more Cisco Unified SCCP IP phones to the paging group. Skip
                                          			 Step 7 for each IP phone except for the last one.

—

Step 7

paging group paging-dn-tag , paging-dn-tag

#### Example:

```
Router(config-ephone-dn)# paging group 20
```

Creates a
                                             				combined paging group from two or more previously established paging sets.

paging-dn-tag —Comma-separated list of
                                                   					 paging-dn-tags that have previously been associated with the paging extension
                                                   					 of a paging set using the paging-dn command. You can include up to ten paging-dn-tags separated by commas; for
                                                   					 example, 4, 6, 7, 8.

Step 8

exit

#### Example:

```
Router(config-ephone-dn)# exit
```

Exits
                                             				ephone-dn configuration mode.

Step 9

voice register dn dn-tag

#### Example:

```
Router(config)# voice register dn 1
```

Enters voice
                                             				register dn configuration mode.

dn-tag —Unique sequence number that identifies a
                                                   					 particular directory number during configuration tasks. Range is 1 to 150 or
                                                   					 the maximum defined by the max-dn command.

Step 10

number number

#### Example:

```
Router(config-register-dn)# number 1201
```

Associates a
                                             				telephone or extension number with a Cisco Unified SIP IP phone in a Cisco
                                             				Unified CME system.

number —String of up to 16 characters that
                                                   					 represents an E.164 telephone number. Normally, the string is composed of
                                                   					 digits, but the string may contain alphabetic characters when the number is
                                                   					 dialed only by the router, as with an intercom number.

Step 11

exit

#### Example:

```
Router(config-register-dn)# exit
```

Exits voice
                                             				register dn configuration mode.

Step 12

Repeat
                                          			 Step 9 to Step 11 to associate more telephone or extension numbers with Cisco
                                          			 Unified SIP IP phones.

—

Step 13

voice register pool pool-tag

#### Example:

```
Router(config)# voice register pool 1
```

Enters voice
                                             				register pool configuration mode and creates a pool configuration for a Cisco
                                             				Unified SIP IP phone in Cisco Unified CME.

pool-tag —Unique number assigned to the pool.
                                                   					 Range: 1 to 100.

For Cisco
                                                         				  Unified CME systems, the upper limit for this argument is defined by the max-pool command.

Step 14

id mac address

#### Example:

```
Router(config-register-pool)# id mac 0019.305D.82B8
```

identifies a
                                             				locally available Cisco Unified SIP IP phone.

mac address —identifies the MAC address of a particular
                                                   					 Cisco Unified SIP IP phone.

Step 15

type phone-type

#### Example:

```
Router(config-register-pool)# type 7961
```

Defines a
                                             				phone type for a Cisco Unified SIP IP phone.

phone-type —Type of Cisco Unified SIP IP phone that
                                                   					 is being defined.

Step 16

number tag dn dn-tag

#### Example:

```
Router(config-register-pool)# number 1 dn 1
```

Indicates
                                             				the E.164 phone numbers that the registrar permits to handle the Register
                                             				message from the Cisco Unified SIP IP phone.

tag —identifies the telephone number when there are
                                                   					 multiple number commands. Range: 1 to 10.

dn dn-tag —identifies the directory number tag for
                                                   					 this phone number as defined by the voice register
                                                         						  dn command. Range: 1 to 150.

Step 17

paging-dn paging-dn-tag

#### Example:

```
Router(config-register-pool)# paging-dn 20
```

Registers a
                                             				Cisco Unified SIP IP phone to an ephone-dn paging directory number.

paging-dn-tag —Ephone-dn tag designated as the
                                                   					 paging ephone-dn to which a Cisco Unified SIP IP phone is registered.

Step 18

Repeat
                                          			 Step 13 to Step 17 to register additional Cisco Unified SIP IP phones to
                                          			 ephone-dn paging directory numbers. Exit from voice register pool configuration
                                          			 mode after each additional phone is registered. After the last phone is added,
                                          			 go directly to Step 19.

—

Step 19

end

#### Example:

```
Router(config-register-pool)# end
```

Exits voice
                                             				register pool configuration mode and enters privileged EXEC mode.

#### Troubleshooting Tips

Use the debug ephone paging command to collect
                                 		debugging information on paging for both Cisco Unified SIP IP and Cisco Unified
                                 		SCCP IP phones.

### Verify Paging

Step 1

Use the show running-config command to display the
                                          			 running configuration. Paging ephone-dns are listed in the ephone-dn portion of
                                          			 the output. Phones that belong to paging groups are listed in the ephone part
                                          			 of the output.

```
Router# show running-config ephone-dn  48
 number 136
 name PagingCashiers
 paging ip 239.1.1.10 port 2000 

ephone  2
 headset auto-answer line 1
 headset auto-answer line 4
 ephone-template 1
 username "FrontCashier"
 mac-address 011F.2A0.A490
 paging-dn 48
 type 7960
 no dnd feature-ring
 no auto-line
 button  1f43 2f44 3f45 4:31
```

Step 2

Use the show telephony-service ephone-dn and show telephony-service ephone commands to
                                          			 display only the configuration information for ephone-dns and ephones.

## Configuration Examples for Paging

### Example for Configuring Simple Paging Group

The following example sets up an ephone-dn for multicast paging. This
                                 		  example creates a paging number for 5001 on ephone-dn 22 and adds ephone 4 as a
                                 		  member of the paging set. Multicast is set for the paging-dn.

```
ephone-dn 22 
 name Paging Shipping 
 number 5001 
 paging ip 239.1.1.10 port 2000 

ephone 4 
 mac-address 0030.94c3.8724 
 button 1:1 2:2 
 paging-dn 22 multicast
```

In this example, paging calls to 2000 are multicast to
                                 		  Cisco Unified IP phones 1 and 2, and paging calls to 2001 go to
                                 		  Cisco Unified IP phones 3 and 4. Note that the paging ephone-dns (20 and 21)
                                 		  are not assigned to any phone buttons.

```
ephone-dn 20
 number 2000
 paging ip 239.0.1.20 port 2000

ephone-dn 21
 number 2001
 paging ip 239.0.1.21 port 2000

ephone 1
 mac-address 3662.024.6ae2
 button 1:1
 paging-dn 20

ephone 2
 mac-address 9387.678.2873
 button 1:2
 paging-dn 20

ephone 3
 mac-address 0478.2a78.8640
 button 1:3
 paging-dn 21

ephone 4
 mac-address 4398.b694.456
 button 1:4
 paging-dn 21
```

### Example for Configuring Combined Paging Groups

This example sets the following paging behavior:

When extension 2000 is dialed, a page is sent to ephones 1 and 2
                                       				(single paging group).

When extension 2001 is dialed, a page is sent to ephones 3 and 4
                                       				(single paging group).

When extension 2002 is dialed, a page is sent to ephones 1, 2, 3,
                                       				4, and 5 (combined paging group).

Ephones 1 and 2 are included in paging ephone-dn 22 through the
                                 		  membership of ephone-dn 20 in the combined paging group. Ephones 3 and 4 are
                                 		  included in paging ephone-dn 22 through membership of ephone-dn 21 in the
                                 		  combined paging group. Ephone 5 is directly subscribed to paging-dn 22.

```
ephone-dn 20 
 number 2000 
 paging ip 239.0.1.20 port 2000 

ephone-dn 21 
 number 2001 
 paging ip 239.0.1.21 port 2000 

ephone-dn 22 
 number 2002 
 paging ip 239.0.2.22 port 2000 
 paging group 20,21 

ephone-dn 6 
 number 1103
 name user3

ephone-dn 7 
 number 1104 
 name user4 

ephone-dn 8 
 number 1105 
 name user5

ephone-dn 9 
 number 1199 

ephone-dn 10 
 number 1198 

ephone 1 
 mac-address 1234.8903.2941
 button 1:6
 paging-dn 20 

ephone 2 
 mac-address CFBA.321B.96FA
 button 1:7
 paging-dn 20 

ephone 3 
 mac-address CFBB.3232.9611
 button 1:8
 paging-dn 21 

ephone 4 
 mac-address 3928.3012.EE89
 button 1:9
 paging-dn 21 

ephone 5 
 mac-address BB93.9345.0031
 button 1:10
 paging-dn 22
```

### Example for Configuring a Combined Paging Group of Cisco Unified SIP
                           	 IP Phones and Cisco Unified SCCP IP Phones

The following example shows how to configure a combined paging group
                                 		  composed of Cisco Unified SIP IP phones and Cisco Unified SCCP IP phones.

In the following configuration tasks, paging sets 20 and 21 are
                                 		  defined and then combined into paging group 22. Paging set 20 has a paging
                                 		  extension of 2000. When someone dials extension 2000 to deliver a page, the
                                 		  page is sent to Cisco Unified SCCP IP phones (ephones) 1 and 2. Paging set 21
                                 		  has a paging extension of 2001. When someone dials extension 2001 to deliver a
                                 		  page, the page is sent to ephones 3 and 4. Paging group 22 combines sets 20 and
                                 		  21, and when someone dials its paging extension, 2002, the page is sent to all
                                 		  the phones in both sets and to ephone 5, which is directly subscribed to the
                                 		  combined paging group.

```
ephone-dn 20
 number 2000
 paging ip 239.0.1.20 port 2000

ephone-dn 21
 number 2001
 paging ip 239.0.1.21 port 2000

ephone-dn 22
 number 2002
 paging ip 239.0.2.22 port 2000
 paging group 20,21

ephone 1
 button 1:1
 paging-dn 20

ephone 2
 button 1:2
 paging-dn 20

ephone 3
 button 1:3
 paging-dn 21

ephone 4
 button 1:4
 paging-dn 21

ephone 5
 button 1:5
 paging-dn 22
```

The following configuration tasks show how to configure a combined
                                 		  paging group composed of Cisco Unified SCCP IP phone directory numbers only.

When extension 2000 is dialed, a page is sent to ephones 1 and 2
                                 		  (first single paging group). When extension 2001 is dialed, a page is sent to
                                 		  ephones 3 and 4 (second single paging group). Finally, when extension 2002 is
                                 		  dialed, a page is sent to ephones 1, 2, 3, 4, and 5, producing the combined
                                 		  paging group (composed of the first single paging group, the second single
                                 		  paging group, and ephone 5).

Ephones 1 and 2 are included in paging ephone-dn 22 through the
                                 		  membership of ephone-dn 20 as paging group 20 in the combined paging group.
                                 		  Ephones 3 and 4 are included in paging ephone-dn 22 through membership of
                                 		  ephone-dn 21 as paging group 21 in the combined paging group. Ephone 5 is
                                 		  directly subscribed to paging-dn 22.

```
ephone-dn 20
 number 2000
 paging ip 239.0.1.20 port 20480

ephone-dn 21
 number 2001
 paging ip 239.1.1.21 port 20480

ephone-dn 22
 number 2002
 paging ip 239.1.1.22 port 20480
 paging group 20,21

ephone-dn 6
 number 1103

ephone-dn 7
 number 1104

ephone-dn 8
 number 1105

ephone-dn 9
 number 1199

ephone-dn 10
 number 1198

ephone 1
 mac-address 1234.8903.2941
 button 1:6
 paging-dn 20

ephone 2
 mac-address CFBA.321B.96FA
 button 1:7
 paging-dn 20

ephone 3
 mac-address CFBB.3232.9611
 button 1:8
paging-dn 21

ephone 4
 mac-address 3928.3012.EE89
 button 1:9
 paging-dn 21

ephone 5
 mac-address BB93.9345.0031
 button 1:10
 paging-dn 22
```

In the following configuration tasks, the paging group command is used to configure
                                 		  combined paging groups composed of ephone and voice register directory numbers.

When extension 2000 is dialed, a page is sent to ephones 1 and 2 and
                                 		  voice register pools 1 and 2 (new first single paging group). When extension
                                 		  2001 is dialed, a page is sent to ephones 3 and 4 and voice register pools 3
                                 		  and 4 (new second single paging group). Finally, when extension 2002 is dialed,
                                 		  a page is sent to ephones 1, 2, 3, 4, and 5 and voice register pools 1, 2, 3,
                                 		  4, and 5 (new combined paging group).

Ephones 1 and 2 and voice register pools 1 and 2 are included in
                                 		  paging ephone-dn 22 through the membership of ephone-dn 20 as paging group 20
                                 		  in the combined paging group. Ephones 3 and 4 and voice register pools 3 and 4
                                 		  are included in paging ephone-dn 22 through membership of ephone-dn 21 as
                                 		  paging group 21 in the combined paging group. Ephone 5 and voice register pool
                                 		  5 are directly subscribed to paging-dn 22.

```
voice register dn 1
 number 1201

voice register dn 2
 number 1202

voice register dn 3
 number 1203

voice register dn 4
 number 1204

voice register dn 5
 number 1205

voice register pool 1
 id mac 0019.305D.82B8
 type 7961
 number 1 dn 1
paging-dn 20

voice register pool  2
 id mac 0019.305D.2153
 type 7961
 number 1 dn 2
 paging-dn 20

voice register pool  3
 id mac 1C17.D336.58DB
 type 7961
 number 1 dn 3
 paging-dn 21

voice register pool  4
 id mac 0017.9437.8A60
 type 7961
 number 1 dn 4
 paging-dn 21

voice register pool  5
 id mac 0016.460D.E469
 type 7961
 number 1 dn 5
 paging-dn 22
```

## Where to Go
                        	 Next

### Intercom

The intercom
                              		  feature is similar to paging because it allows a phone user to deliver an audio
                              		  message to a phone without the called party having to answer. The intercom
                              		  feature is different than paging because the audio path between the caller and
                              		  the called party is a dedicated audio path and because the called party can
                              		  respond to the caller. See Intercom Lines .

### Speed Dial

Phone users who make frequent pages may want to include the paging ephone-dn numbers in their list of speed-dial numbers.
                              See Speed Dial .

## Feature
                        	 Information for Paging

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature
                                             					 Name

Cisco Unified CME Version

Feature
                                             					 Information

Paging

2.0

Paging was
                                             					 introduced.

Paging
                                             					 Group Support for Cisco Unified SIP IP Phones

9.0

Allows you
                                             					 to specify a paging-dn tag and dial the paging extension number to page the
                                             					 Cisco Unified SIP IP phone associated with the paging-dn tag or paging group
                                             					 using the paging-dn command in voice register pool or voice
                                             					 register template configuration mode.

| Note | The paging port
                                          		  for Cisco Unified SIP IP phones is an even number from 20480 to 32768. If you
                                          		  enter a wrong port number, a SIP REFER message request is sent to the IP phone
                                          		  but the Cisco Unified SIP IP phone is not paged. |
|---|---|

| Restriction | IP phones do not
                                             			 support multicast at 224.x.x.x addresses. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn paging-dn-tag Example: Router(config)# ephone-dn 42 | Enters
                                             				ephone-dn configuration mode. paging-dn-tag —A unique sequence number that
                                                   					 identifies this paging ephone-dn during all configuration tasks. This is the
                                                   					 ephone-dn that is dialed to initiate a page. This ephone-dn is not associated
                                                   					 with a physical phone. Range is 1 to 288. Note Do not use
                                                         				  the dual-line keyword with this command. Paging ephone-dns cannot be dual-line. | Note | Do not use
                                                         				  the dual-line keyword with this command. Paging ephone-dns cannot be dual-line. |
| Note | Do not use
                                                         				  the dual-line keyword with this command. Paging ephone-dns cannot be dual-line. |
| Step 4 | number number Example: Router(config-ephone-dn)# number 3556 | Defines an
                                             				extension number associated with the paging ephone-dn. This is the number that
                                             				people call to initiate a page. |
| Step 5 | name name Example: Router(config-ephone-dn)# name paging4 | Assigns to the
                                             				paging number a name to appear in caller-ID displays and directories. |
| Step 6 | paging [ ip multicast-address port udp-port-number ] Example: Router(config-ephone-dn)# paging ip 239.1.1.10 port 2000 | Specifies that
                                             				this ephone-dn is to be used to broadcast paging messages to the idle IP phones
                                             				that are associated with the paging dn-tag. If the optional keywords and
                                             				arguments are not used, IP phones are paged individually using IP unicast
                                             				transmission (to a maximum of ten IP phones). The optional keywords and
                                             				arguments are as follows: ip multicast-address port udp-port-number —Specifies multicast broadcast
                                                   					 using the specified IP address and UDP port. When multiple paging numbers are
                                                   					 configured, each paging number must use a unique IP multicast address. We
                                                   					 recommend port 2000 because it is already used for normal non-multicast RTP
                                                   					 media streams between phones and the Cisco Unified CME router. Note IP phones do
                                                         				  not support multicast at 224.x.x.x addresses. Note The correct
                                                         				  paging port for the paging-dn of Cisco Unified SIP IP phones is an even number
                                                         				  from 20480 to 32768. If you enter a wrong port number, a SIP REFER message
                                                         				  request is sent to the IP phone but the Cisco Unified SIP IP phone is not
                                                         				  paged. | Note | IP phones do
                                                         				  not support multicast at 224.x.x.x addresses. | Note | The correct
                                                         				  paging port for the paging-dn of Cisco Unified SIP IP phones is an even number
                                                         				  from 20480 to 32768. If you enter a wrong port number, a SIP REFER message
                                                         				  request is sent to the IP phone but the Cisco Unified SIP IP phone is not
                                                         				  paged. |
| Note | IP phones do
                                                         				  not support multicast at 224.x.x.x addresses. |
| Note | The correct
                                                         				  paging port for the paging-dn of Cisco Unified SIP IP phones is an even number
                                                         				  from 20480 to 32768. If you enter a wrong port number, a SIP REFER message
                                                         				  request is sent to the IP phone but the Cisco Unified SIP IP phone is not
                                                         				  paged. |
| Step 7 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

| Note | Do not use
                                                         				  the dual-line keyword with this command. Paging ephone-dns cannot be dual-line. |
|---|---|

| Note | IP phones do
                                                         				  not support multicast at 224.x.x.x addresses. |
|---|---|

| Note | The correct
                                                         				  paging port for the paging-dn of Cisco Unified SIP IP phones is an even number
                                                         				  from 20480 to 32768. If you enter a wrong port number, a SIP REFER message
                                                         				  request is sent to the IP phone but the Cisco Unified SIP IP phone is not
                                                         				  paged. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn paging-dn-tag Example: Router(config)# ephone-dn 42 | Enters
                                             				ephone-dn configuration mode to create a paging number for a combined paging
                                             				group. paging-dn-tag —A unique sequence number that
                                                   					 identifies this paging ephone-dn during all configuration tasks. This is the
                                                   					 ephone-dn that is dialed to initiate a page. This ephone-dn is not associated
                                                   					 with a physical phone. Range is 1 to 288. Note Do not use
                                                         				  the dual-line keyword with this command. Paging ephone-dns cannot be dual-line. | Note | Do not use
                                                         				  the dual-line keyword with this command. Paging ephone-dns cannot be dual-line. |
| Note | Do not use
                                                         				  the dual-line keyword with this command. Paging ephone-dns cannot be dual-line. |
| Step 4 | number number Example: Router(config-ephone-dn)# number 3556 | Defines an
                                             				extension number associated with the combined group paging ephone-dn. This is
                                             				the number that people call to initiate a page to the combined group. |
| Step 5 | name name Example: Router(config-ephone-dn)# name paging4 | (Optional)
                                             				Assigns to the combined group paging number a name to appear in caller-ID
                                             				displays and directories. |
| Step 6 | paging group paging-dn-tag , paging-dn-tag [ [ , paging-dn-tag ] ... ] Example: Router(config-ephone-dn)# paging group 20,21 | Sets the
                                             				paging directory number for a combined group. This command combines the
                                             				individual paging group ephone-dns that you specify into a combined group so
                                             				that a page can be sent to more than one paging group at a time. paging-dn-tag —Unique sequence number associated
                                                   					 with the paging number for an individual paging group. Lists the paging-dn-tags
                                                   					 of all the individual groups that you want to include in this combined group,
                                                   					 separated by commas. You can include up to ten paging ephone-dn tags in this
                                                   					 command. Note Configure
                                                         				  the paging command for all ephone-dns in a paging group before configuring the
                                                         				  paging group command for that group. | Note | Configure
                                                         				  the paging command for all ephone-dns in a paging group before configuring the
                                                         				  paging group command for that group. |
| Note | Configure
                                                         				  the paging command for all ephone-dns in a paging group before configuring the
                                                         				  paging group command for that group. |
| Step 7 | exit Example: Router(config-ephone-dn)# exit | Exits
                                             				ephone-dn configuration mode. |
| Step 8 | ephone phone-tag Example: Router(config)# ephone 2 | Enters ephone
                                             				configuration mode to add IP phones to the paging group. phone-tag —Unique sequence number of a phone to
                                                   					 receive audio pages when the paging ephone-dn is called. |
| Step 9 | paging-dn paging-dn-tag { multicast \| unicast } Example: Router(config-ephone)# paging-dn 42 multicast | Associates
                                             				this ephone with an ephone-dn tag that is used for a paging ephone-dn (the
                                             				number that people call to deliver a page). Note that the paging ephone-dn tag
                                             				is not associated with a line button on this ephone. The paging
                                             				mechanism supports audio distribution using IP multicast, replicated unicast,
                                             				and a mixture of both (so that multicast is used where possible and unicast is
                                             				allowed to specific phones that cannot be reached through multicast). paging-dn-tag —Unique sequence number for a paging
                                                   					 ephone-dn. multicast —(Optional) Multicast paging for groups.
                                                   					 By default, paging is transmitted to the Cisco Unified IP phone using
                                                   					 multicast. unicast —(Optional) Unicast paging for a single
                                                   					 Cisco Unified IP phone. This keyword indicates that the Cisco Unified IP phone
                                                   					 is not capable of receiving paging through multicast and requests that the
                                                   					 phone receive paging through a unicast transmission directed to the individual
                                                   					 phone. Note The number
                                                         				  of phones supported through unicast is limited to a maximum of ten phones. | Note | The number
                                                         				  of phones supported through unicast is limited to a maximum of ten phones. |
| Note | The number
                                                         				  of phones supported through unicast is limited to a maximum of ten phones. |
| Step 10 | exit Example: Router(config-ephone)# exit | Exits ephone
                                             				configuration mode. |
| Step 11 | Repeat
                                          			 Step 8 to Step 10 to add additional IP phones to a paging group. | — |
| Step 12 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

| Note | Do not use
                                                         				  the dual-line keyword with this command. Paging ephone-dns cannot be dual-line. |
|---|---|

| Note | Configure
                                                         				  the paging command for all ephone-dns in a paging group before configuring the
                                                         				  paging group command for that group. |
|---|---|

| Note | The number
                                                         				  of phones supported through unicast is limited to a maximum of ten phones. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn dn-tag Example: Router(config)# ephone-dn 20 | Enters
                                             				ephone-dn configuration mode. dn-tag —Unique number that identifies an ephone-dn
                                                   					 during configuration tasks. Range is 1 to the number set by the max-dn command. |
| Step 4 | number number Example: Router(config-ephone-dn)# number 2000 | Associates a
                                             				telephone or extension number with this ephone-dn. number —String of up to 16 characters that
                                                   					 represents an E.164 telephone number. Normally, the string is composed of
                                                   					 digits, but the string may contain alphabetic characters when the number is
                                                   					 dialed only by the router, as with an intercom number. One or more periods (.)
                                                   					 can be used as wildcard characters. |
| Step 5 | paging [ ip multicast-address port udp-port-number ] Example: Router(config-ephone-dn)# paging ip 239.0.1.20 port 20480 | Defines an
                                             				extension (ephone-dn) as a paging extension that can be called to broadcast an
                                             				audio page to a set of Cisco Unified IP phones. ip multicast-address —(Optional) Uses an IP multicast
                                                   					 address to multicast voice packets for audio paging; for example, 239.0.1.1. Note IP phones do
                                                         				  not support multicast at 224.x.x.x addresses. Default is that multicast is not
                                                         				  used and IP phones are paged individually using IP unicast transmission (up to
                                                         				  ten phones). port udp-port-number —(Optional) Uses this UDP port for
                                                   					 the multicast. Range: 2000 to 65535. Note If any of
                                                         				  the paged phones is a Cisco Unified SIP IP phone, the correct paging port for
                                                         				  the paging-dn is an even number from 20480 to 32768. If you enter a wrong port
                                                         				  number, a SIP REFER message request is sent to the IP phone but the Cisco
                                                         				  Unified SIP IP phone is not paged. | Note | IP phones do
                                                         				  not support multicast at 224.x.x.x addresses. Default is that multicast is not
                                                         				  used and IP phones are paged individually using IP unicast transmission (up to
                                                         				  ten phones). | Note | If any of
                                                         				  the paged phones is a Cisco Unified SIP IP phone, the correct paging port for
                                                         				  the paging-dn is an even number from 20480 to 32768. If you enter a wrong port
                                                         				  number, a SIP REFER message request is sent to the IP phone but the Cisco
                                                         				  Unified SIP IP phone is not paged. |
| Note | IP phones do
                                                         				  not support multicast at 224.x.x.x addresses. Default is that multicast is not
                                                         				  used and IP phones are paged individually using IP unicast transmission (up to
                                                         				  ten phones). |
| Note | If any of
                                                         				  the paged phones is a Cisco Unified SIP IP phone, the correct paging port for
                                                         				  the paging-dn is an even number from 20480 to 32768. If you enter a wrong port
                                                         				  number, a SIP REFER message request is sent to the IP phone but the Cisco
                                                         				  Unified SIP IP phone is not paged. |
| Step 6 | Repeat Step 3
                                          			 to Step 5 to add more Cisco Unified SCCP IP phones to the paging group. Skip
                                          			 Step 7 for each IP phone except for the last one. | — |
| Step 7 | paging group paging-dn-tag , paging-dn-tag Example: Router(config-ephone-dn)# paging group 20 | Creates a
                                             				combined paging group from two or more previously established paging sets. paging-dn-tag —Comma-separated list of
                                                   					 paging-dn-tags that have previously been associated with the paging extension
                                                   					 of a paging set using the paging-dn command. You can include up to ten paging-dn-tags separated by commas; for
                                                   					 example, 4, 6, 7, 8. |
| Step 8 | exit Example: Router(config-ephone-dn)# exit | Exits
                                             				ephone-dn configuration mode. |
| Step 9 | voice register dn dn-tag Example: Router(config)# voice register dn 1 | Enters voice
                                             				register dn configuration mode. dn-tag —Unique sequence number that identifies a
                                                   					 particular directory number during configuration tasks. Range is 1 to 150 or
                                                   					 the maximum defined by the max-dn command. |
| Step 10 | number number Example: Router(config-register-dn)# number 1201 | Associates a
                                             				telephone or extension number with a Cisco Unified SIP IP phone in a Cisco
                                             				Unified CME system. number —String of up to 16 characters that
                                                   					 represents an E.164 telephone number. Normally, the string is composed of
                                                   					 digits, but the string may contain alphabetic characters when the number is
                                                   					 dialed only by the router, as with an intercom number. |
| Step 11 | exit Example: Router(config-register-dn)# exit | Exits voice
                                             				register dn configuration mode. |
| Step 12 | Repeat
                                          			 Step 9 to Step 11 to associate more telephone or extension numbers with Cisco
                                          			 Unified SIP IP phones. | — |
| Step 13 | voice register pool pool-tag Example: Router(config)# voice register pool 1 | Enters voice
                                             				register pool configuration mode and creates a pool configuration for a Cisco
                                             				Unified SIP IP phone in Cisco Unified CME. pool-tag —Unique number assigned to the pool.
                                                   					 Range: 1 to 100. Note For Cisco
                                                         				  Unified CME systems, the upper limit for this argument is defined by the max-pool command. | Note | For Cisco
                                                         				  Unified CME systems, the upper limit for this argument is defined by the max-pool command. |
| Note | For Cisco
                                                         				  Unified CME systems, the upper limit for this argument is defined by the max-pool command. |
| Step 14 | id mac address Example: Router(config-register-pool)# id mac 0019.305D.82B8 | identifies a
                                             				locally available Cisco Unified SIP IP phone. mac address —identifies the MAC address of a particular
                                                   					 Cisco Unified SIP IP phone. |
| Step 15 | type phone-type Example: Router(config-register-pool)# type 7961 | Defines a
                                             				phone type for a Cisco Unified SIP IP phone. phone-type —Type of Cisco Unified SIP IP phone that
                                                   					 is being defined. |
| Step 16 | number tag dn dn-tag Example: Router(config-register-pool)# number 1 dn 1 | Indicates
                                             				the E.164 phone numbers that the registrar permits to handle the Register
                                             				message from the Cisco Unified SIP IP phone. tag —identifies the telephone number when there are
                                                   					 multiple number commands. Range: 1 to 10. dn dn-tag —identifies the directory number tag for
                                                   					 this phone number as defined by the voice register
                                                         						  dn command. Range: 1 to 150. |
| Step 17 | paging-dn paging-dn-tag Example: Router(config-register-pool)# paging-dn 20 | Registers a
                                             				Cisco Unified SIP IP phone to an ephone-dn paging directory number. paging-dn-tag —Ephone-dn tag designated as the
                                                   					 paging ephone-dn to which a Cisco Unified SIP IP phone is registered. |
| Step 18 | Repeat
                                          			 Step 13 to Step 17 to register additional Cisco Unified SIP IP phones to
                                          			 ephone-dn paging directory numbers. Exit from voice register pool configuration
                                          			 mode after each additional phone is registered. After the last phone is added,
                                          			 go directly to Step 19. | — |
| Step 19 | end Example: Router(config-register-pool)# end | Exits voice
                                             				register pool configuration mode and enters privileged EXEC mode. |

| Note | IP phones do
                                                         				  not support multicast at 224.x.x.x addresses. Default is that multicast is not
                                                         				  used and IP phones are paged individually using IP unicast transmission (up to
                                                         				  ten phones). |
|---|---|

| Note | If any of
                                                         				  the paged phones is a Cisco Unified SIP IP phone, the correct paging port for
                                                         				  the paging-dn is an even number from 20480 to 32768. If you enter a wrong port
                                                         				  number, a SIP REFER message request is sent to the IP phone but the Cisco
                                                         				  Unified SIP IP phone is not paged. |
|---|---|

| Note | For Cisco
                                                         				  Unified CME systems, the upper limit for this argument is defined by the max-pool command. |
|---|---|

| Step 1 | Use the show running-config command to display the
                                          			 running configuration. Paging ephone-dns are listed in the ephone-dn portion of
                                          			 the output. Phones that belong to paging groups are listed in the ephone part
                                          			 of the output. Router# show running-config ephone-dn  48
 number 136
 name PagingCashiers
 paging ip 239.1.1.10 port 2000 

ephone  2
 headset auto-answer line 1
 headset auto-answer line 4
 ephone-template 1
 username "FrontCashier"
 mac-address 011F.2A0.A490
 paging-dn 48
 type 7960
 no dnd feature-ring
 no auto-line
 button  1f43 2f44 3f45 4:31 |
|---|---|
| Step 2 | Use the show telephony-service ephone-dn and show telephony-service ephone commands to
                                          			 display only the configuration information for ephone-dns and ephones. |

| Feature
                                             					 Name | Cisco Unified CME Version | Feature
                                             					 Information |
|---|---|---|
| Paging | 2.0 | Paging was
                                             					 introduced. |
| Paging
                                             					 Group Support for Cisco Unified SIP IP Phones | 9.0 | Allows you
                                             					 to specify a paging-dn tag and dial the paging extension number to page the
                                             					 Cisco Unified SIP IP phone associated with the paging-dn tag or paging group
                                             					 using the paging-dn command in voice register pool or voice
                                             					 register template configuration mode. |