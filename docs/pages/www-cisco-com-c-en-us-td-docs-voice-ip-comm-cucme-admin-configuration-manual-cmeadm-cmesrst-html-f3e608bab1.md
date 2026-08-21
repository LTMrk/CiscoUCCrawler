---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmesrst-html-f3e608bab1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmesrst.html
retrieved_at: 2026-08-21T07:25:29.809437+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: SRST Fallback Mode

## Chapter: SRST Fallback Mode

# SRST Fallback Mode

## Prerequisites for
                        	 SRST Fallback Mode

The IP address of the Cisco Unified CME router must be registered as the SRST reference on the Cisco Unified Communications
                                 Manager device pool.

Cisco Unified CME 4.0 or a later version must be installed on the Cisco Unified CME router that is configured in SRST mode.

Following tasks must be completed:

Generate Configuration Files for Phones

Configure System-Level Parameters . Note that the max-dn command must be explicity configured with the preference keyword to support calls between PSTN and IP phones during SRST fallback mode.

Configure Call Transfer and Forwarding

## Restrictions for
                        	 SRST Fallback Mode

SRST Fallback Mode is applicable only for SCCP phones. SIP phones are not supported.

The call-manager-fallback command, which is used to configure Cisco Unified SRST, cannot be used on a router that is configured for Cisco Unified CME.

The telephony-service setup command and auto assign command must not be enabled on a Cisco Unified CME router configured for SRST fallback mode. If you used the telephony-service setup command before configuring the router for SRST fallback support, you must remove any unwanted ephone directory numbers created
                                 by the setup process.

The number of phones that fall back to a Cisco Unified CME router in SRST mode cannot exceed the maximum number of phones
                                 that is supported by the router. To find the maximum number of phones for a particular router and Cisco Unified CME version,
                                 see the appropriate Cisco CME Supported Firmware, Platforms, Memory, and Voice Products document at http://www.cisco.com/en/us/products/sw/voicesw/ps4625/products_device_support_tables_list.html .

The ephone-dns and ephones that are created from fallback may have less information associated with them than appears in their
                                 original configuration on a Cisco Unified Communications Manager or on an active Cisco Unified CME system. This situation
                                 occurs because the Cisco Unified CME router in SRST mode is designed to learn only a limited amount of information from the
                                 fallback IP phones. For example, if an ephone-dn has in its configuration the command number 4888 no-reg (to keep that extension from registering under its E.164 address), after fallback the no-reg part of this command will be lost because this information cannot be learned from the IP phones.

The order of the SRST fallback ephone-dns and ephones will be different from the order of the active Cisco Unified Communications
                                 Manager or Cisco Unified CME ephone-dns and ephones. For example, ephone 1 on an active Cisco Unified Communications Manager
                                 might be numbered ephone 5 on the Cisco Unified CME router in SRST mode, because the order of learned ephone-dns and ephones
                                 is determined by the sequence of the ephone fallback occurrence, which is random.

## Information About SRST Fallback Mode

### SRST Fallback Mode
                           	 Using Cisco Unified CME

This feature enables
                              		routers to provide call-handling support for Cisco Unified IP phones if they
                              		lose connection to remote primary, secondary, or tertiary
                              		Cisco Unified Communications Manager installations or if the WAN connection is
                              		down. When Cisco Unified SRST functionality is provided by Cisco Unified CME,
                              		provisioning of phones is automatic and most Cisco Unified CME features are
                              		available to the phones during periods of fallback, including hunt-groups, call
                              		park and access to Cisco Unity voice messaging services using SCCP protocol.
                              		The benefit is that Cisco Unified Communications Manager users will gain access
                              		to more features during fallback without any additional licensing costs.

This feature offers
                              		a limited telephony feature set during fallback mode. Customers who require the
                              		following features should continue to use Cisco Unified SRST, because these
                              		features are not supported with SRST fallback support using Cisco Unified CME.

More than 240
                                       			 phones during fallback service

Cisco VG 248
                                       			 Analog Phone Gateway support

Secure voice
                                       			 fallback during SRST fallback service

Simple, one-time
                                       			 configuration for SRST fallback service

Cisco Unified Communications Manager supports Cisco Unified IP
                              		phones at remote sites attached to Cisco Integrated Services Routers across the
                              		WAN. This new feature combines the many features available in Cisco Unified CME
                              		with the ability to automatically detect IP phone configurations that is
                              		available in Cisco Unified SRST to provide seamless call handling when
                              		communication with the Cisco Unified Communications Manager is interrupted.

When the system
                              		automatically detects a failure, Cisco Unified SRST uses Simple Network Auto
                              		Provisioning (SNAP) technology to auto-configure a branch office router to
                              		provide call processing for the Cisco Unified IP phones that are registered
                              		with the router. When the WAN link or connection to the primary
                              		Cisco Unified Communications Manager is restored, call handling returns to the
                              		primary Cisco Unified Communications Manager.

A limited number of
                              		phone features are automatically detected at the time that call processing
                              		falls back to Cisco Unified CME in SRST Fallback Mode, and an advantage of SRST
                              		fallback support using Cisco Unified CME is that you can choose to prebuild a
                              		Cisco Unified CME configuration that contains a number of extensions
                              		(ephone-dns) with additional features that you want them to have for some or
                              		all of your extensions. The configurations will contain ephone-dn
                              		configurations but will not identify which phones (which MAC addresses) will be
                              		associated with which ephone-dns (extension numbers).

By copying and
                              		pasting a prebuilt configuration onto Cisco Unified CME routers at several
                              		locations, you can use the same overall configuration for sites that are
                              		identically laid out. For example, if you have a number of retail stores, each
                              		with five to ten checkout registers, you can use the same overall configuration
                              		in each store. You might use a range of extensions from 1101 to 1110. Stores
                              		with fewer than ten registers will simply not use some of the ephone-dn entries
                              		you provide in the configuration. Stores with more extensions than you have
                              		prebuilt will use the auto-provisioning feature to populate their extra phones.
                              		The only configuration variations from store to store will be the specific MAC
                              		addresses of the individual phones, which are added to the configurations at
                              		the time of fallback.

When a phone
                              		registers for SRST service with a Cisco Unified CME router and the router
                              		discovers that the phone was configured with a specific extension number, the
                              		router searches for an existing prebuilt ephone-dn with that extension number
                              		and then assigns that ephone-dn number to the phone. If there is no prebuilt
                              		ephone-dn with that extension number, the Cisco Unified CME system
                              		automatically creates one. In this way, extensions without prebuilt
                              		configurations are automatically populated with extension numbers and features
                              		as the numbers and features are “learned” by the Cisco Unified CME router in
                              		SRST mode when the phone registers to the router after a WAN link fails.

The SRST fallback
                              		support using Cisco Unified CME feature is able to interrogate phones to learn
                              		their MAC addresses and the extension-to-ephone relationships associated with
                              		each phone. This information is used to dynamically create and execute the
                              		Cisco Unified CME button command for each phone and automatically provision each phone with the
                              		extensions and features you want it to have.

The following
                              		sequence describes how Cisco Unified CME provides SRST services for
                              		Cisco Unified Communications Manager phones when they lose connectivity with
                              		the Cisco Unified Communications Manager and fall back to the Cisco Unified CME
                              		router in SRST mode:

Before
                                 		  Fallback

Phones are
                                       			 configured as usual in Cisco Unified Communications Manager.

The IP address
                                       			 of the Cisco Unified CME router is registered as the SRST reference on the
                                       			 Cisco Unified Communications Manager device pool.

SRST mode is
                                       			 enabled on the Cisco Unified CME router.

(Optional)
                                       			 Ephone-dns and features are prebuilt on the Cisco Unified CME router.

During Fallback

Phones that are enabled for fallback register to the default
                                    			 Cisco Unified CME router that has SRST mode enabled. Each display-enabled IP
                                    			 phone displays the message that has been defined using the system message command under
                                    			 telephony-service configuration mode. By default, this message is “Cisco Unified CME .”

MAC address

Number of lines or buttons

Ephone-dn-to-button relationship

Speed-dial numbers

The option defined with the srst mode auto-provision command determines
                                    			 whether Cisco Unified CME adds the learned phone and extension information to
                                    			 its running configuration. If the information is added, it appears in the
                                    			 output when you use the show running-config command and is saved to
                                    			 NVRAM when you use the write command.

Use the srst mode auto-provision none command
                                             				  to enable the Cisco Unified CME router to provide SRST fallback services for
                                             				  Cisco Unified Communications Manager.

If you use the srst mode auto-provision dn or srst mode auto-provision all commands, the Cisco Unified CME
                                             				  router includes the phone configuration it learns from
                                             				  Cisco Unified Communications Manager in its running configuration. If you then
                                             				  save the configuration, the fallback phones are treated as locally configured
                                             				  phones on the Cisco Unified CME-SRST router which could adversely impact the
                                             				  fallback behavior of those phones.

While in fallback mode, Cisco Unified IP phones periodically attempt
                                    			 to reestablish a connection with Cisco Unified Communications Manager every 120
                                    			 seconds (default). To manually reestablish a connection to
                                    			 Cisco Unified Communications Manager you can reboot the Cisco Unified IP phone.

- When a connection is
                                 		  reestablished with Cisco Unified Communications Manager, Cisco Unified IP
                                 		  phones automatically cancel their registration with the Cisco Unified CME
                                 		  router in SRST mode. However, if a WAN link is unstable, Cisco Unified IP
                                 		  phones can bounce between Cisco Unified Communications Manager and the
                                 		  Cisco Unified CME router in SRST mode.

An IP phone
                              		connected to the Cisco Unified CME-SRST router over a WAN reconnects itself to
                              		Cisco Unified Communications Manager as soon as it can establish a connection
                              		to Cisco Unified Communications Manager over the WAN link. However, if the WAN
                              		link is unstable, the IP phone switches back and forth between
                              		Cisco Unified CME-SRST and Cisco Unified Communications Manager, causing
                              		temporary loss of phone service (no dial tone). These reconnect attempts, known
                              		as WAN link flapping issues, continue until the IP phone successfully
                              		reconnects itself back to Cisco Unified Communications Manager.

WAN link disruptions
                              		can be classified into two types: infrequent random outages that occur on an
                              		otherwise stable WAN, and sporadic, frequent disruptions that last a few
                              		minutes.

To resolve WAN-link
                              		flapping issues between Cisco Unified Communications Manager and SRST,
                              		Cisco Unified Communications Manager provides an enterprise parameter and a
                              		setting in the Device Pool Configuration window called Connection Monitor
                              		Duration. (Depending on system requirements, the administrator decides which
                              		parameter to use.) The value of the parameter is delivered to the IP phone in
                              		the XML configuration file.

Use the enterprise parameter to change the connection duration monitor value for all IP phones in the Cisco Unified Communications Manager
                                    cluster. The default for the enterprise parameter is 120 seconds.

Use the Device Pool Configuration window to change the connection duration monitor value for all IP phones in a specific device
                                    pool.

A Cisco Unified IP phone will not reestablish a connection with the primary Cisco Unified Communications Manager at the central
                              office if it is engaged in an active call.

After the First
                                 		  Fallback

Additional features
                              		can be set up, such as ephone hunt groups, which can contain learned extensions
                              		and prebuilt extensions. The complete core set of Cisco Unified CME phone
                              		features is available to the IP phones and extensions, whether they are learned
                              		or configured.

Figure 51-1 shows a branch office with
                              		several Cisco Unified IP phones connected to a Cisco Unified CME router in SRST
                              		fallback mode. The router provides connections to both a WAN link and the PSTN.
                              		The Cisco Unified IP phones connect to their primary
                              		Cisco Unified Communications Manager at the central office via this WAN link.
                              		Cisco Unified CME provides SRST services for the phones when connectivity over
                              		the WAN link is interrupted.

### Prebuilding
                           	 Cisco Unified CME Phone Configurations

Prebuilding Cisco
                              		Unified CME ephone-dns allows you to create a set of directory numbers with
                              		extension numbers and some features, which will provide service during fallback
                              		that is similar to the service that is provided during normal operation. You
                              		can prebuild all of your normal extensions, a limited set of your extensions,
                              		or none of your extensions. Directory numbers that are not prebuilt will be
                              		populated with extension numbers and features as they are “learned” by the
                              		Cisco Unified CME router in SRST mode at the time of fallback.

An ephone-dn is the IP equivalent of a normal phone line in most cases. It represents a potential call connection and is associated
                              with a virtual voice port and virtual dial peer. An ephone-dn has one or more extension or telephone numbers associated with
                              it, which allow call connections to be made. An ephone-dn can be single-line, which allows one call connection to be made
                              at a time, or dual-line, which allows two simultaneous call connections. Dual-line ephone-dns are useful for features such
                              as call transfer or call waiting, in which one call is put on hold to connect to another. Single-line ephone-dns are required
                              for certain features such as intercom, paging, and message-waiting indication (MWI). For more information, see Cisco Unified CME Overview .

If an ephone-dn is
                              		manually configured in Cisco Unified CME, incoming calls will always route to
                              		the manually configured ephone-dn in Cisco Unified CME rather than to
                              		Cisco Unified Communications Manager using the voip dial peer. To avoid
                              		incorrect routing, configure a higher preference for the voip dial peer than
                              		the preference for the prebuilt directory number. For configuration example,
                              		see Example for Prebuilding DNs .

### Auto provision Directory Numbers in SRST Fallback Mode

Cisco Unified CME 4.3 and later versions support octo-line directory
                              		numbers in SRST fallback mode. You can specify whether Cisco Unified CME in
                              		SRST fallback mode creates octo-line or dual-line directory numbers based on
                              		the phone type. For the Cisco Unified IP Phone 7902 or 7920, or an analog phone
                              		connected to the Cisco VG224 or Cisco ATA, the system creates a dual-line
                              		directory number; it creates an octo-line directory number for all other phone
                              		types. This applies only to the ephone-dns that are “learned” automatically
                              		from ephone configuration information, and not to ephone-dns that are manually
                              		configured in Cisco Unified CME.

## Configure SRST Fallback Mode

### Enable SRST
                           	 Fallback Mode

Restriction

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- srst mode auto-provision { all | dn | none }

- srst dn line-mode { dual | dual-octo | octo | single }

- srst dn template template-tag

- srst ephone template template-tag

- srst ephone description string

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

Enter your password if prompted.

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

srst mode auto-provision { all | dn | none }

#### Example:

```
Router(config-telephony)# srst mode auto-provision none
```

Enables SRST mode for a Cisco Unified CME router.

all —Includes information for learned ephones and ephone-dns in the running configuration.

dn —Includes information for learned ephone-dns in the running configuration.

none —Does not include information for learned ephones or learned ephone-dns in the running configuration. Use this keyword when
                                                   you want Cisco Unified CME to provide SRST fallback services for Cisco Unified Communications Manager.

Step 5

srst dn line-mode { dual | dual-octo | octo | single }

#### Example:

```
Router(config-telephony)# srst dn line-mode dual-octo
```

(Optional) Specifies the line mode for ephone-dns in SRST mode on a Cisco Unified CME router.

dual —SRST fallback ephone-dns are dual-line ephone-dns.

dual-octo —SRST fallback ephone-dns are dual-line or octo-line, depending on the phone type. This keyword is supported in Cisco Unified CME 4.3
                                                   and later versions.

octo —SRST fallback ephone-dns are octo-line. This keyword is supported in Cisco Unified CME 4.3 and later versions.

single —SRST fallback ephone-dns are single-line ephone-dns. Default value.

Step 6

srst dn template template-tag

#### Example:

```
Router(config-telephony)# srst dn template 3
```

(Optional)
                                             				Specifies an ephone-dn template to be used in SRST mode on a Cisco Unified CME
                                             				router. The template includes features that were specified when the template
                                             				was created. See Example for Configuring Templates for Fallback Support: Example .

template-tag —identifying number of an existing ephone-dn template. Range is 1 to 15.

Step 7

srst ephone template template-tag

#### Example:

```
Router(config-telephony)# srst ephone template 5
```

(Optional)
                                             				Specifies an ephone template to be used in SRST mode on a Cisco Unified CME
                                             				router.

template-tag —identifying number of an existing ephone template. Range is 1 to 20.

Step 8

srst ephone description string

#### Example:

```
Router(config-telephony)# srst ephone description Cisco Unified CME SRST Fallback
```

(Optional)
                                             				Specifies a description to be associated with an ephone learned in SRST mode on
                                             				a Cisco Unified CME router.

string —Description to be associated with an ephone. Maximum string length is 100 characters.

Step 9

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

### Verify SRST
                           	 Fallback Mode

Step 1

Use the show telephony-service
                                                				  all or the show
                                                				  running-config command to verify that SRST fallback mode has been
                                          			 set on this router.

#### Example:

```
telephony-service
 srst mode auto-provision all
 srst ephone template 5
 srst ephone description srst fallback auto-provision phone : Jul 07 2005 17:45:08
 srst dn template 8
 srst dn line-mode dual
 load 7960-7940 P00305000600
 max-ephones 30
 max-dn 60 preference 0
 ip source-address 10.1.68.78 port 2000
 max-redirect 20
 system message "SRST Mode: Cisco Unified CME’
 keepalive 10
 max-conferences 8 gain -6
 moh welcome.au
 create cnf-files version-stamp Jan 01 2002 00:00:00
```

Step 2

Use the show telephony-service
                                                				  ephone-dn command during fallback to review ephone-dn
                                          			 configurations. Learned ephone-dns are noted by a line stating that they were
                                          			 learned during SRST fallback.

Learned
                                                         				  ephone-dns do not appear in the output for the show
                                                               						running-config command if the none keyword
                                                         				  is used in the srst mode
                                                               						auto-provision command.

#### Example:

```
ephone-dn 1 dual-line
 number 4008
 name 4008
 description 4008
 preference 0 secondary 9
 huntstop
 no huntstop channel
 call-waiting beep
 ephone-dn-template 8
 This DN is learned from srst fallback ephones
```

Step 3

Use the show telephony-service
                                                				  ephone command during fallback to review ephone configurations.
                                          			 Learned ephones are noted by a line stating that they were learned during SRST
                                          			 fallback.

Learned
                                                         				  ephones do not appear in the output for the show
                                                               						running-config command if the none keyword
                                                         				  is used in the srst mode
                                                               						auto-provision command.

#### Example:

```
ephone 1
 mac-address 0112.80B3.9C16
 button 1:1
 multicast-moh
 ephone-template 5
 Always send media packets to this router: No
 Preferred codec: g711ulaw
 user-locale JP
 network-locale US
 Description: "YOUR Description" : Oct 11 2005 09:58:27
 This is a srst fallback phone
```

### Prebuilding Cisco
                           	 Unified CME Phone Configurations

You can optionally
                              		create a set of ephone-dns that are preconfigured with extension numbers and
                              		some features to provide service during fallback that is similar to the service
                              		that is provided during normal operation. Extensions that are not prebuilt are
                              		populated with extension numbers and features as they are “learned” by the
                              		Cisco Unified CME router in SRST mode at the time of fallback.

To avoid incorrect
                                          		  routing when you prebuild ephone-dns for Cisco Unified Communications Manager
                                          		  phones in Cisco Unified CME, use the preference command in ephone-dn and voip-dial-peer configuration mode to create a higher
                                          		  preference (0 being the highest) for the voip dial peer than the preference for
                                          		  the prebuilt directory number. For configuration example, see Example for Prebuilding DNs .

Create Directory Numbers for SCCP Phones

Enable Call Park or Directed Call Park

Create an Ephone Template

Create an Ephone-dn Template

Configure Ephone-Hunt Groups on SCCP Phones

Note that the dial-peer
                                                         					 hunt command must be configured for hunt-selection order of
                                                   				explicit preference to support hunt groups during SRST fallback mode.

### Modify Call Pickup for Fallback Support

An especially useful feature for fallback phones is modifying the
                                 		  behavior of the Pickup soft key in Cisco Unified CME to match that of the
                                 		  Pickup soft key in Cisco Unified Communications Manager. To modify the call
                                 		  pickup feature for fallback support, perform the following steps.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- no service directed-pickup

- create cnf-files

- reset all

- exit

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters telephony-service configuration mode.

Step 4

no service directed-pickup

#### Example:

```
Router(telephony)# no service directed-pickup
```

(Optional) Disables directed call pickup and changes the behavior
                                             				of the PickUp soft key so that a user pressing it invokes local group pickup
                                             				rather than directed call pickup. This behavior is consistent with that of the
                                             				PickUp soft key in Cisco Unified Communications Manager.

For changes to the service-phone settings to be effective, the
                                                         				  Sep*.conf.xml file must be updated with the create cnf-files command and the phone units must rebooted with
                                                         				  the reset command.

Step 5

create cnf-files

#### Example:

```
Router(telephony)# create cnf-files
```

Builds XML configuration files for Cisco Unified IP phones.

Step 6

reset all

#### Example:

```
Router(telephony)# reset all
```

Resets all phones.

Step 7

exit

#### Example:

```
Router(telephony)# exit
```

Exits dial-peer configuration mode.

## Configuration Examples for SRST Fallback Mode

### Example for Enabling SRST Mode

The following example enables SRST mode on the Cisco Unified CME
                                 		  router. It specifies that learned fallback ephone-dns should be created in
                                 		  dual-line mode and use ephone-dn template 3 for their configuration parameters.
                                 		  Learned ephones will use the parameters in ephone template 5 and a description
                                 		  will be associated with the phones.

```
telephony-service
		   max-ephones 30 
		   max-dn 60 preference 0
		   srst mode auto-provision all
		   srst dn line-mode dual
		   srst dn template 3
		   srst ephone description srst fallback auto-provision phone
		   srst ephone template 5
		  .
		  .
		  .
```

The following excerpt from the show running-config command displays the
                                 		  configuration of ephone 1, which was learned during fallback; the description
                                 		  is stamped with the date and time that the show running-config command was used. The
                                 		  configuration of ephone 2, which was prebuilt rather than learned, is shown for
                                 		  comparison.

```
ephone 1
		   description srst fallback auto-provision phone : Jul 07 2005 17:45:08
		   ephone-template 5
		   mac-address 100A.7052.2AAE
		   button 1:1 2:2
		  
		  ephone 2
		   mac-address 1002.CD64.A24A
		   type 7960
		   button  1:3
```

The following excerpt from the show running-config command displays the
                                 		  configuration of ephone-dn 1 through ephone-dn 3. All three ephones are learned
                                 		  ephone-dns that are configured in dual-line mode and use ephone-dn template 5,
                                 		  as specified in the telephony-service configuration mode commands.

```
ephone-dn  1 dual-line
		   number 7001
		   description 7001
		   name 7001
		   ephone-dn-template 5
		   This DN is learned from srst fallback ephones
		  !
		  !
		  ephone-dn  2 dual-line
		   number 4005
		   name 4005
		   ephone-dn-template 5
		   This DN is learned from srst fallback ephones
		  !
		  !
		  ephone-dn  3 dual-line
		   number 4002
		   label 4002
		   name 4002
		   ephone-dn-template 5
		   This DN is learned from srst fallback ephones
```

### Example for Provisioning Directory Numbers for Fallback
                           	 Support

The following example sets up five ephone-dns and two call-park slots
                                 		  that are used for fallback phones.

```
ephone-dn 1
		   number 1101
		   name Register 1
		 
		  ephone-dn 2
		   number 1102
		   name Register 2
		  
		  ephone-dn 3
		   number 1103
		   name Register 3
		  
		  ephone-dn 4
		   number 1104
		   name Register 4
		  
		  ephone-dn 5
		   number 1105
		   name Register 5
		  
		  ephone-dn 21
		   number 1121
		   name Park Slot 1
		   park-slot timeout 60 limit 3 recall alternate 1100
		  
		  ephone-dn 22
		   number 1122
		   name Park Slot 2
		   park-slot timeout 60 limit 3 recall alternate 1100
```

### Example for Configuring Templates for Fallback Support:
                           	 Example

The following example creates ephone-dn template 3 and ephone template
                                 		  5 that will be used with the SRST fallback support using Cisco Unified CME
                                 		  feature. Ephone-dn template 3 adds the fallback phones to pickup group 24 and
                                 		  specifies call forwarding for busy and no-answer conditions to extension 1100.
                                 		  Ephone template 5 defines two fastdial numbers that will appear as menu entries
                                 		  displayed from the Directories > Local
                                       				Services > Personal Speed Dials option on the fallback phones, and also specifies the softkey layouts for the
                                 		  fallback phones.

```
ephone-dn-template 3
		 pickup-group 24
		 call-forward busy 1100
		 call-forward noan 1100 timeout 45
		 
		ephone-template 5
		 fastdial 1 1101 name Front Register
		 fastdial 2 918005550111 Headquarters
		 softkeys idle Newcall Cfwdall Pickup
		 softkeys seized Endcall Cfwdall Pickup 
		 softkeys alerting Endcall
		 softkeys connected Endcall Hold Park Trnsfer
```

### Example for Enabling Hunt Groups for Fallback Support

The following example configures the dial peers to hunt in the
                                 		  following order: (1) explicit preference, (2) longest match in phone number,
                                 		  and (3) random selection. The dial-peer hunt command must be configured for hunt-selection order of
                                 		  explicit preference to support hunt groups during SRST fallback mode.

```
dial-peer hunt 2
```

The following example creates a peer hunt group with the pilot number
                                 		  1111.

```
ephone-hunt 3 peer
		   pilot 1111
		   list 1101, 1102, 1103
		   hops 3
		   timeout 25
		   final 1100
```

### Example for Modifying Call Pickup for Fallback Support

The following example changes the behavior of the Pickup soft key to
                                 		  be like the one in Cisco Unified Communications Manager.

```
telephony-service
		   no service directed-pickup
		   create cnf-files
```

### Example for
                           	 Prebuilding DNs

In the following
                                 		  partial example, the preference command in ephone-dn and voip-dial-peer configuration mode is configured to
                                 		  create a voip dial peer with a higher preference (0) than the preference (1) of
                                 		  the manually-configured directory number (ephone-dn 1).

```
dial-peer voice 1002 
  voip destination-pattern 1019 . 
  .
  .
  preference 0 <<=====This dial peer has precedence and will match first. ephone-dn 1 
  number 1019 preference 1 <<======Configure lower preference for prebuilt DN.
```

## Feature
                        	 Information for SRST Fallback Mode

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Cisco Unified CME Version

Feature Information

Octo-Line Directory Numbers

4.3

Support for octo-line directory numbers was added.

SRST Fallback Support Using Cisco Unified CME

4.0

SRST fallback support using Cisco Unified CME was introduced.

| Restriction | Do not enable the telephony-service setup command or auto assign command on a Cisco Unified CME router that you are configuring for SRST fallback mode. If you used the telephony-service setup command previously on the router, you must remove any unwanted ephone directory numbers created by the setup process. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 4 | srst mode auto-provision { all \| dn \| none } Example: Router(config-telephony)# srst mode auto-provision none | Enables SRST mode for a Cisco Unified CME router. all —Includes information for learned ephones and ephone-dns in the running configuration. dn —Includes information for learned ephone-dns in the running configuration. none —Does not include information for learned ephones or learned ephone-dns in the running configuration. Use this keyword when
                                                   you want Cisco Unified CME to provide SRST fallback services for Cisco Unified Communications Manager. |
| Step 5 | srst dn line-mode { dual \| dual-octo \| octo \| single } Example: Router(config-telephony)# srst dn line-mode dual-octo | (Optional) Specifies the line mode for ephone-dns in SRST mode on a Cisco Unified CME router. dual —SRST fallback ephone-dns are dual-line ephone-dns. dual-octo —SRST fallback ephone-dns are dual-line or octo-line, depending on the phone type. This keyword is supported in Cisco Unified CME 4.3
                                                   and later versions. octo —SRST fallback ephone-dns are octo-line. This keyword is supported in Cisco Unified CME 4.3 and later versions. single —SRST fallback ephone-dns are single-line ephone-dns. Default value. Note This command is used only when ephone-dns are learned at the time of fallback. It is ignored when you prebuild ephone-dn configurations. | Note | This command is used only when ephone-dns are learned at the time of fallback. It is ignored when you prebuild ephone-dn configurations. |
| Note | This command is used only when ephone-dns are learned at the time of fallback. It is ignored when you prebuild ephone-dn configurations. |
| Step 6 | srst dn template template-tag Example: Router(config-telephony)# srst dn template 3 | (Optional)
                                             				Specifies an ephone-dn template to be used in SRST mode on a Cisco Unified CME
                                             				router. The template includes features that were specified when the template
                                             				was created. See Example for Configuring Templates for Fallback Support: Example . template-tag —identifying number of an existing ephone-dn template. Range is 1 to 15. |
| Step 7 | srst ephone template template-tag Example: Router(config-telephony)# srst ephone template 5 | (Optional)
                                             				Specifies an ephone template to be used in SRST mode on a Cisco Unified CME
                                             				router. template-tag —identifying number of an existing ephone template. Range is 1 to 20. |
| Step 8 | srst ephone description string Example: Router(config-telephony)# srst ephone description Cisco Unified CME SRST Fallback | (Optional)
                                             				Specifies a description to be associated with an ephone learned in SRST mode on
                                             				a Cisco Unified CME router. string —Description to be associated with an ephone. Maximum string length is 100 characters. |
| Step 9 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

| Note | This command is used only when ephone-dns are learned at the time of fallback. It is ignored when you prebuild ephone-dn configurations. |
|---|---|

| Step 1 | Use the show telephony-service
                                                				  all or the show
                                                				  running-config command to verify that SRST fallback mode has been
                                          			 set on this router. Example: telephony-service
 srst mode auto-provision all
 srst ephone template 5
 srst ephone description srst fallback auto-provision phone : Jul 07 2005 17:45:08
 srst dn template 8
 srst dn line-mode dual
 load 7960-7940 P00305000600
 max-ephones 30
 max-dn 60 preference 0
 ip source-address 10.1.68.78 port 2000
 max-redirect 20
 system message "SRST Mode: Cisco Unified CME’
 keepalive 10
 max-conferences 8 gain -6
 moh welcome.au
 create cnf-files version-stamp Jan 01 2002 00:00:00 |
|---|---|
| Step 2 | Use the show telephony-service
                                                				  ephone-dn command during fallback to review ephone-dn
                                          			 configurations. Learned ephone-dns are noted by a line stating that they were
                                          			 learned during SRST fallback. Note Learned
                                                         				  ephone-dns do not appear in the output for the show
                                                               						running-config command if the none keyword
                                                         				  is used in the srst mode
                                                               						auto-provision command. Example: ephone-dn 1 dual-line
 number 4008
 name 4008
 description 4008
 preference 0 secondary 9
 huntstop
 no huntstop channel
 call-waiting beep
 ephone-dn-template 8
 This DN is learned from srst fallback ephones | Note | Learned
                                                         				  ephone-dns do not appear in the output for the show
                                                               						running-config command if the none keyword
                                                         				  is used in the srst mode
                                                               						auto-provision command. |
| Note | Learned
                                                         				  ephone-dns do not appear in the output for the show
                                                               						running-config command if the none keyword
                                                         				  is used in the srst mode
                                                               						auto-provision command. |
| Step 3 | Use the show telephony-service
                                                				  ephone command during fallback to review ephone configurations.
                                          			 Learned ephones are noted by a line stating that they were learned during SRST
                                          			 fallback. Note Learned
                                                         				  ephones do not appear in the output for the show
                                                               						running-config command if the none keyword
                                                         				  is used in the srst mode
                                                               						auto-provision command. Example: ephone 1
 mac-address 0112.80B3.9C16
 button 1:1
 multicast-moh
 ephone-template 5
 Always send media packets to this router: No
 Preferred codec: g711ulaw
 user-locale JP
 network-locale US
 Description: "YOUR Description" : Oct 11 2005 09:58:27
 This is a srst fallback phone | Note | Learned
                                                         				  ephones do not appear in the output for the show
                                                               						running-config command if the none keyword
                                                         				  is used in the srst mode
                                                               						auto-provision command. |
| Note | Learned
                                                         				  ephones do not appear in the output for the show
                                                               						running-config command if the none keyword
                                                         				  is used in the srst mode
                                                               						auto-provision command. |

| Note | Learned
                                                         				  ephone-dns do not appear in the output for the show
                                                               						running-config command if the none keyword
                                                         				  is used in the srst mode
                                                               						auto-provision command. |
|---|---|

| Note | Learned
                                                         				  ephones do not appear in the output for the show
                                                               						running-config command if the none keyword
                                                         				  is used in the srst mode
                                                               						auto-provision command. |
|---|---|

| Note | To avoid incorrect
                                          		  routing when you prebuild ephone-dns for Cisco Unified Communications Manager
                                          		  phones in Cisco Unified CME, use the preference command in ephone-dn and voip-dial-peer configuration mode to create a higher
                                          		  preference (0 being the highest) for the voip dial peer than the preference for
                                          		  the prebuilt directory number. For configuration example, see Example for Prebuilding DNs . |
|---|---|

| Note | Note that the dial-peer
                                                         					 hunt command must be configured for hunt-selection order of
                                                   				explicit preference to support hunt groups during SRST fallback mode. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters telephony-service configuration mode. |
| Step 4 | no service directed-pickup Example: Router(telephony)# no service directed-pickup | (Optional) Disables directed call pickup and changes the behavior
                                             				of the PickUp soft key so that a user pressing it invokes local group pickup
                                             				rather than directed call pickup. This behavior is consistent with that of the
                                             				PickUp soft key in Cisco Unified Communications Manager. Note For changes to the service-phone settings to be effective, the
                                                         				  Sep*.conf.xml file must be updated with the create cnf-files command and the phone units must rebooted with
                                                         				  the reset command. | Note | For changes to the service-phone settings to be effective, the
                                                         				  Sep*.conf.xml file must be updated with the create cnf-files command and the phone units must rebooted with
                                                         				  the reset command. |
| Note | For changes to the service-phone settings to be effective, the
                                                         				  Sep*.conf.xml file must be updated with the create cnf-files command and the phone units must rebooted with
                                                         				  the reset command. |
| Step 5 | create cnf-files Example: Router(telephony)# create cnf-files | Builds XML configuration files for Cisco Unified IP phones. |
| Step 6 | reset all Example: Router(telephony)# reset all | Resets all phones. |
| Step 7 | exit Example: Router(telephony)# exit | Exits dial-peer configuration mode. |

| Note | For changes to the service-phone settings to be effective, the
                                                         				  Sep*.conf.xml file must be updated with the create cnf-files command and the phone units must rebooted with
                                                         				  the reset command. |
|---|---|

| Feature Name | Cisco Unified CME Version | Feature Information |
|---|---|---|
| Octo-Line Directory Numbers | 4.3 | Support for octo-line directory numbers was added. |
| SRST Fallback Support Using Cisco Unified CME | 4.0 | SRST fallback support using Cisco Unified CME was introduced. |