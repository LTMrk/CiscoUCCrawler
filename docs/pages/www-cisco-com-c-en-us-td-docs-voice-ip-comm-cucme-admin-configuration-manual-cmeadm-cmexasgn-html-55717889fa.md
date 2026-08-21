---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmexasgn-html-55717889fa
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmexasgn.html
retrieved_at: 2026-08-21T07:22:26.224541+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Create Phone Configurations Using Extension Assigner

## Chapter: Create Phone Configurations Using Extension Assigner

# Create Phone Configurations Using Extension Assigner

## Prerequisites for
                        	 Extension Assigner

- Cisco Unified CME 11.6 or a
                              		  later version for SIP phones.

- Cisco Unified CME 4.0(3) or
                              		  a later version for SCCP phones.

- For Extension Assigner
                              		  Synchronization, Cisco Unified CME 4.2(1) or a later version.

- The auto-register-phone command must be enabled
                              		  (default) for SCCP phones, and auto-register must be enabled for SIP phones.

- DHCP must be configured.
                              		  For configuration information, see Defining Network Parameters .

- You have a valid Cisco.com
                              		  account.

- You have access to a TFTP
                              		  server for downloading files.

## Restrictions for
                        	 Extension Assigner

- The number of phones that
                              		  you install cannot exceed the maximum number of phones supported by the router
                              		  chassis. To find the maximum number of phones for a particular router and
                              		  Cisco Unified CME version, see the appropriate Cisco Uniified CME Supported Firmware,
                                 			 Platforms, Memory, and Voice Products for your Cisco IOS release.

- For Extension Assigner
                              		  Synchronization, automatic synchronization only applies to configuration
                              		  changes made by Cisco Unified CME Extension Assigner.

## Information About Extension Assigner

### Extension Assigner
                           	 Overview

From Cisco Unified
                              		CME Release 11.6 onwards, Extension Assigner feature is supported for both SIP
                              		and SCCP phones. This feature enables installation technicians to assign
                              		extension numbers to Cisco Unified CME phones without administrative access to
                              		the server, typically during the installation of new phones or the replacement
                              		of broken phones. However, before an installation technician can use this
                              		feature, the system administrator must first configure Cisco Unified CME to
                              		allow specific extensions to be assigned. The system administrator must also
                              		provide the installation technician with the information necessary for
                              		assigning extension numbers to phones. The installation technician can then
                              		assign extension numbers to phones with access to only the phones themselves
                              		and with no further intervention from the administrator.

To configure this
                              		feature, tasks must be performed on the Cisco router by an administrator and
                              		onsite by installation technicians.

#### Procedure for
                              	 System Administrators

Before an
                                 		installation technician can assign new extension numbers to phones, you must
                                 		complete the following tasks:

- Determine which extension
                                    		  numbers will be assigned to the new phones and plan your configuration.

- Download the appropriate
                                    		  Tcl script and associated audio prompt files and place them in the correct
                                    		  directory.

- Configure and load the
                                          				appropriate Tcl script.

- Specify the extension that
                                          				the installation technician calls to assign extension numbers.

- Optionally specify whether
                                          				the extension used to assign extension numbers is dialed automatically.

- Specify the password that
                                          				the installation technician enters to assign extension numbers.

- Configure the extension
                                          				assigner feature.

- Configure ephone-dns with
                                          				temporary extension numbers (applicable only for SCCP phones).

- Configure ephone-dns and
                                          				voice register dns with the extension numbers that the installation technician
                                          				can assign to phones.

- Configure ephones and voice
                                          				register pools with temporary MAC addresses for each phone that will be
                                          				assigned an extension number by the installation technician.

All
                                                         					 phone configurations such as dn and pool that are generated as part of the auto
                                                         					 registration process are persistent configurations(If the command background save
                                                               						  interval is configured under telephony-service). These phone
                                                         					 configurations are available on Unified CME even after an event of router
                                                         					 reload.

- Provide the installation
                                    		  technician with the information needed to assign extension numbers to the new
                                    		  phones.

Before you can
                                 		configure this feature, you must understand how the extension assigner
                                 		application works and what information the installation technician needs to
                                 		assign extension numbers to phones.

Other information
                                 		you must provide to the installation technician involves the tasks that the
                                 		installation technician must perform. These tasks include:

- Dialing a configurable
                                    		  extension number to access the extension assigner application.

- Entering a configurable
                                    		  password.

- Entering a tag
                                    		  (provision-tag for SIP phones, and ephone-tag or provision-tag for SCCP phones)
                                    		  that identifies the extension number that will be assigned to the phone.

Therefore, you must
                                 		make the following decisions:

- Which extension number must
                                    		  be dialed to access the extension assigner application.

- Whether the number is
                                    		  dialed automatically when a phone goes off hook.

- What password the
                                    		  installation technician must enter to access the extension assigner
                                    		  application.

- What type of tag
                                    		  (provision-tag for SIP phones, and ephone-tag or provision-tag for SCCP phones)
                                    		  numbers to use to identify the extension number to assign to the phone.

- What specific tag numbers
                                    		  to use to identify the extension number to assign to the phone.

The first three
                                 		decisions are straightforward, but the last two tag number decisions require
                                 		some knowledge of how the extension assigner feature works.

This feature is
                                 		implemented using a Tcl script and audio files. To run this script, the
                                 		installation technician plugs in the phone, waits for a random extension number
                                 		to be automatically assigned, and dials a specified extension assigner number
                                 		to invoke the extension assigner service.

After the phones
                                 		have registered and received their temporary extension numbers, the
                                 		installation technician can access extension assigner and enter a tag number.
                                 		This tag number is used to identify the extension number and must match either
                                 		an ephone tag (only for SCCP phones) or a similar new tag called the
                                 		provision-tag (applicable to both SIP and SCCP phones).

For SCCP phones, you
                                 		must decide on which tag you want to use before you configure your ephone and
                                 		ephone-dn entries.

The advantage of
                                 		using the provision-tag is that you can make it easier for the installation
                                 		technician to assign extension numbers because you can configure the tag to
                                 		match the primary extension number or some other unique identifier for the
                                 		phone, such as a jack number. We recommend you to configure provision-tag same
                                 		as the primary extension number.

The disadvantage is
                                 		that you configure an additional keyword for each ephone entry, as shown in the
                                 		following example:

```
ephone 1
 provision-tag 9001
 mac-address 02EA.EAEA.0001
 button 1:1
```

```
voice register pool 1
 provision-tag 1001
 mac-address 02EA.EAEA.0001
 number 1 dn 101
```

For SCCP phones, if
                                 		you decide to use the ephone tag, it requires less configuration. However, the
                                 		installation technician enters an arbitrary tag number instead of the actual
                                 		extension number when configuring a phone. This restriction is because the
                                 		number of ephone tags that you can configure is limited by your license. For
                                 		example, if you use the ephone tag and you have a 100-user license, the
                                 		installation technician cannot enter 9001 for the tag because you can configure
                                 		only ephone 1 to ephone 100.

Note that each
                                 		ephone entry that you configure must also include a temporary MAC address. As
                                 		shown in the above example, this address should begin with 02EA.EAEA and can
                                 		end with any unique number. We strongly recommend that you can configure this
                                 		unique number to match the ephone tag for SCCP phones.

For SCCP phones, you
                                 		do not have to configure any ephone entries for the extension number that are
                                 		randomly assigned. The auto assign feature automatically creates an ephone
                                 		entry for each new phone when it registers. The auto assign feature then
                                 		automatically assigns an ephone-dn entry if there is an available ephone-dn
                                 		that has one of the tag numbers specified by the auto assign command. The resulting ephone pool configurations have the actual MAC address
                                 		of the phone and a button with the first available ephone-dn designated for the
                                 		auto assign feature. For more information, see Configure Temporary Extension Numbers for SCCP Phones That Use Extension Assigner .

For SIP phones, you
                                 		do not have to configure voice register pool or voice register dn. You need to
                                 		configure auto-register command for automatic registration of SIP phones on
                                 		Cisco Unified CME. For more information, see Configure Temporary Extension Numbers for SCCP Phones That Use Extension Assigner .

For manually
                                             		  registered phones, ephone (or voice register pool) and ephone-dn (or voice
                                             		  register dn) are manually created.

As shown in the
                                 		following example, you configure at least one ephone-dn for a temporary
                                 		extension and specify which ephone-dns the autoassign feature will assign to
                                 		the temporary ephone entries:

```
telephony-service
 auto assign 101 to 105
ephone-dn 101
 number 0001
```

When the
                                 		installation technician assigns an extension number to a phone, the temporary
                                 		MAC address is replaced by the actual MAC address and the ephone entry created
                                 		by the auto register feature is deleted. The number of ephone-dns that you
                                 		configure for the auto assign feature determines how many phones you can plug
                                 		in at one time and get an automatically assigned extension. If you define four
                                 		ephone-dns for auto assign and you plug in five phones, one phone will not get
                                 		a temporary extension number until you assign an extension to one of the other
                                 		four phones and reset the fifth phone. You are permitted to set the max-ephone
                                 		value higher than the number of users and phones supported by your Cisco
                                 		Unified CME phone licenses for the purpose of enrolling licensed phones using
                                 		Extension Assigner.

In addition to
                                 		configuring one ephone-dn for each temporary extension number that is assigned
                                 		automatically, you also must configure an ephone-dn entry for each extension
                                 		number that is assigned by the installation technician. For more details on
                                 		configuring extension numbers that technicians can assign to SCCP phones, see Configure Extension Numbers That Installation Technicians Can Assign to SCCP Phones .

For SIP Phones, the
                                 		temporary MAC address is replaced by the actual MAC address and voice register
                                 		pool entry created by the auto-register feature is deleted when the
                                 		installation technician assigns an extension number to a phone. The number of
                                 		voice register dns that you configure for the auto assign feature determines
                                 		how many phones you can plug in at one time and get an automatically assigned
                                 		extension. If you define four voice register dns for auto assign and you plug
                                 		in five phones, one phone will not get a temporary extension number until you
                                 		assign an extension to one of the other four phones and reset the fifth phone.
                                 		You are permitted to set the max-pool value higher than the number of users and
                                 		phones supported by your Cisco Unified CME phone licenses for the purpose of
                                 		enrolling licensed phones using Extension Assigner. For more details on
                                 		configuring extension numbers that technicians can assign to SIP phones, see Configure Extension Numbers That Installation Technicians Can Assign to SIP Phones .

For SIP Phones,
                                             		  you need not create temporary dn if auto registration is used.

To complete the
                                 		configuration, as shown in the following example, you must:

- Specify whether to use the
                                    		  ephone or the provision-tag number to identify the extension number to assign
                                    		  to the phone. Set this when the feature is enabled with the new extension-assigner tag-type command provided with this feature.

- Configure an ephone-dn for
                                    		  each temporary extension number that is assigned automatically.

- Configure an ephone-dn or
                                    		  voice register dn for each extension number that you want the installation
                                    		  technician to assign to a phone.

- Configure an ephone or
                                    		  voice register pool with a temporary MAC address for each phone that is
                                    		  assigned an extension number by the installation technician. Optionally, this
                                    		  ephone definition can include the new provision-tag. For SIP phones, it is
                                    		  necessary to have provision-tag information under voice register pool. For more
                                    		  information, see Configure Ephones with Temporary MAC Addresses .

```
telephony-service
 extension-assigner tag-type provision-tag
 auto assign 101 to 105
ephone-dn 1 dual-line
 number 6001
ephone-dn 101
 number 0001
 label Temp-Line-not assigned yet
ephone 1
 provision-tag 6001
 mac-address 02EA.EAEA.0001
 button 1:1
***********************************
```

```
voice register pool 1
provision-tag 1001
mac-address 02EA.EAEA.0001
number 1 dn 101
```

Because you must
                                 		configure two ephone-dns or voice register dns for each extension number that
                                 		you want to assign, you may exceed your max-dn setting. You are permitted to
                                 		set the max-dn value higher than the number allowed by your license for the
                                 		purpose of enrolling licensed phones using extension assigner.

Assuming that your
                                 		max-dn setting is set high enough, your max-ephone or max-pool setting
                                 		determines how many phones you can plug in at one time. For example, if your
                                 		max-ephone or max-pool setting is ten more than the number of phones to which
                                 		you want to assign extension numbers, then you can plug in ten phones at a
                                 		time. If you plug in eleven phones, one phone will not register or get a
                                 		temporary extension number until you assign an extension to one of the first
                                 		ten phones and reset the eleventh phone.

After you have
                                 		configured your ephone or voice register pool, and ephone-dn or voice register
                                 		dn entries, you can complete your router configuration by optionally
                                 		configuring the router to automatically save your configuration. If the router
                                 		configuration is not saved, any extension assignments made by the installation
                                 		technician will be lost when the router is restarted. The alternative to this
                                 		optional procedure is to have the installation technician connect to the router
                                 		and enter the write memory command to save the router configuration.

The final task of
                                 		the system administrator is to document the information that the installation
                                 		technician needs to assign extension numbers to the new phones. You can also
                                 		use this documentation as a guide when you configure Cisco Unified CME to
                                 		implement this feature. This information includes:

- How many phones the
                                    		  installation technician can plug in at one time

- Which extension number to
                                    		  dial to access the extension assigner application

- Whether the number is
                                    		  dialed automatically when a phone goes off hook

- What password to enter to
                                    		  access the application

- Which tag numbers to enter
                                    		  to assign an extension to each phone

##### Extension Assigner
                                 	 in Mixed Deployment

From Cisco Unified
                                    		CME release 11.6 onwards, extension assigner feature supports mixed deployment
                                    		of SCCP and SIP phones. In a mixed deployment scenario, you sometimes have to
                                    		migrate or replace an SCCP phone with a SIP phone or vice versa. The extension
                                    		assigner functionality ensures a seamless migration experience in this scenario
                                    		by letting you assign extension numbers to the new phone (irrespective of SIP
                                    		or SCCP).

In mixed mode
                                    		deployment, you can reassign any current extension number to a new phone. When
                                    		you dial in to the extension assigner system to perform this task, you are
                                    		redirected to the unassign menu. You need to unassign the current extension
                                    		number so that it is no more assigned to any phone. After successfully
                                    		unassigning the extension number, the call is disconnected. When you dial in to
                                    		the extension assigner again, you can reassign the extension number to your new
                                    		phone. For more information, see Reassign the Current Extension Number .

You cannot
                                                		  unassign the extension number of a phone if it is in use. The phone has to be
                                                		  in idle or unregistered state.

#### Procedures for
                              	 Installation Technicians

This feature is
                                    		  implemented using a Tcl script and audio prompt files that enable the
                                    		  installation technician to assign an extension number to a new
                                    		  Cisco Unified CME phone by performing the following procedure The system
                                    		  administrator provides the installation technician with all of the information
                                    		  required to perform this procedure.

Step 1

Plug in a
                                             			 specified number of new phones.

Step 2

Wait for the
                                             			 phones to be assigned temporary, random extension numbers.

Step 3

Dial a
                                             			 specified number to access the extension assigner application.

Step 4

Enter a
                                             			 specified password.

Step 5

Enter a tag
                                             			 that identifies an extension number and enables the installation technician to
                                             			 perform one of the following tasks:

Assign a
                                                      					 new extension number to a phone.

Unassign
                                                      					 the current extension number.

Reassign
                                                      					 an extension number.

### Files Included in this Release

The app-cme-ea-2.0.0.0.tar or later archive file provided for the
                              		extension assigner feature includes a readme file, a Tcl script, and several
                              		audio prompt files. If you want to replace the audio files with files that use
                              		a language other than English, do not change the name of the files. The Tcl
                              		script is written to use only the following list of the filenames:

- app-cme-ea-2.0.0.0.tcl
                                 		  (script)

- en_cme_tag_assign_phone.au (audio file)

- en_cme_tag_assigned_to_phone.au (audio file)

- en_cme_tag_assigned_to_phone_idle.au (audio file)

- en_cme_tag_assigned_to_phone_inuse.au (audio file)

- en_cme_tag_assigned_to_phone_unreg.au (audio file)

- en_cme_tag_available.au (audio file)

- en_cme_tag_extension.au (audio file)

- en_cme_tag_invalid.au (audio file)

- en_cme_tag_unassign_phone.au (audio file)

- en_cme_tag_action_cancelled.au (audio file)

- en_cme_tag_assign_failed.au (audio file)

- en_cme_tag_assign_success.au (audio file)

- en_cme_tag_contact_admin.au (audio file)

- en_cme_tag_disconnect.au (audio file)

- en_cme_tag_ephone_tagid.au (audio file)

- en_cme_tag_invalid_password.au (audio file)

- en_cme_tag_invalidoption.au (audio file)

- en_cme_tag_noentry.au (audio file)

- en_cme_tag_password.au (audio file)

- en_cme_tag_unassign_failed.au (audio file)

- en_cme_tag_unassign_success.au (audio file)

- en_eight.au (audio file)

- en_five.au (audio file)

- en_four.au (audio file)

- en_nine.au (audio file)

- en_one.au (audio file)

- en_seven.au (audio file)

- en_six.au (audio file)

- en_three.au (audio file)

- en_two.au (audio file)

- en_zero.au (audio file)

- readme.txt

### Extension Assigner
                           	 Synchronization

Extension Assigner
                              		Synchronization enables the secondary backup router to automatically receive
                              		any changes made by Extension Assigner to ephone or voice register pool
                              		mac-addresses in the primary router. The synchronization is performed using the
                              		Cisco Unified CME XML interface. The Cisco Unified CME XML client encapsulates
                              		the configuration changes into an ISexecCLI request and sends it to the secondary backup router using HTTP. The server on
                              		the secondary backup side processes the incoming XML request and calls the
                              		Cisco IOS CLI parser to perform the updates.

For configuration
                              		information, see Configuring Extension Assigner
                                 		  Synchronization .

## Configure
                        	 Extension Assigner

The following tasks
                           		are performed by an administrator or other personnel who is responsible for
                           		configuring Extension Assigner:

### Determine
                           	 Extension Numbers to Assign to the New Phones and Plan Your
                           	 Configuration

After you determine
                              		which extension number to assign to each phone, you must make the following
                              		decisions:

- Which extension number must
                                 		  be dialed to access the extension assigner application.

- Whether the number is dialed
                                 		  automatically when a phone goes off hook.

- What password the installation
                                 		  technician must enter to access the extension assigner application.

- Whether to use ephone-tag (applicable
                                 		  only for SCCP phones) or the provision-tag number to identify the extension
                                 		  number to assign to the phone.

- How many
                                 		  temporary extension numbers to configure. This will determine how many
                                 		  temporary ephone-dns or voice register dns, and temporary MAC addresses to
                                 		  configure.

- What specific tag
                                 		  numbers to use to identify the extension number to assign to the phone.

### Download the Tcl
                           	 Script and Audio Prompt Files

To download the
                                 		  Tcl script and audio prompt files for the extension assigner feature, perform
                                 		  the following steps.

For more information about how to use Tcl scripts, see the Cisco IOS Tcl IVR and Voice XML Application Guide for your Cisco IOS release.

### SUMMARY STEPS

- Go to the
                                 			 Cisco Unified CME software download website at http://software.cisco.com/download/type.html?mdfid=277641082&catid=null .

- Download the
                                 			 Cisco Unified CME extension assigner tar archive to a TFTP server that is
                                 			 accessible to the Cisco Unified CME router.

- enable

- archive tar /xtract source-url
                                       				  destination-url

### DETAILED STEPS

Step 1

Go to the
                                          			 Cisco Unified CME software download website at http://software.cisco.com/download/type.html?mdfid=277641082&catid=null .

Gives you
                                             				access to Cisco Unified CME software downloads.

Step 2

Download the
                                          			 Cisco Unified CME extension assigner tar archive to a TFTP server that is
                                          			 accessible to the Cisco Unified CME router.

- This tar archive contains the extension assigner Tcl script and the default audio files that you need for the extension assigner
                                                service.

Step 3

enable

#### Example:

```
Router> enable
```

Step 4

archive tar /xtract source-url
                                                				  destination-url

#### Example:

```
Router# archive tar /xtract tftp://192.168.1.1/app-cme-ea-2.0.0.0.tar flash:
```

- source-url —URL of the source of the extension
                                                   				  assigner TAR file. Valid URLs can refer to TFTP or HTTP servers or to flash
                                                   				  memory.

- location —URL of the destination of the extension
                                                   				  assigner TAR file, including its Tcl script and audio files. Valid URLs can
                                                   				  refer to TFTP or HTTP servers or to flash memory.

### Configure the Tcl
                           	 Script

To configure and
                                 		  load the Tcl script for the extension assigner feature and create the password
                                 		  that installation technicians enter to access the extension assigner
                                 		  application, perform the following steps.

For more
                                 		  information about how to use Tcl scripts, see the Cisco IOS Tcl IVR and Voice
                                    			 XML Application Guide for your Cisco IOS release.

### SUMMARY STEPS

- enable

- configure terminal

- application

- service service-name
                                       				  location

- param ea-password password

- paramspace english
                                       				  index number

- paramspace english
                                       				  language en

- paramspace english location location

- paramspace english prefix
                                       				  en

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

application

#### Example:

```
Router(config)# application
```

Step 4

service service-name
                                                				  location

#### Example:

```
Router(config-app)# service EA flash:/EA/
```

Enters
                                             				service parameter configuration mode to configure parameters for the call-queue
                                             				service.

service-name —Name of the extension assigner
                                                   					 service. This arbitrary name is used to identify the service during
                                                   					 configuration tasks.

location —URL of the Tcl script for the extension
                                                   					 assigner service. Valid URLs can refer to TFTP or HTTP servers or to flash
                                                   					 memory.

Step 5

param ea-password password

#### Example:

```
Router(config-app-param)# param ea-password 1234
```

Sets the
                                             				password that installation technicians enter to access the extension assigner
                                             				application.

password —Numerical password that installation
                                                   					 technicians enter to access the extension assigner application. Length: 2 to 10
                                                   					 digits.

Step 6

paramspace english
                                                				  index number

#### Example:

```
Router(config-app-param)# paramspace english index 0
```

Defines the
                                             				language of audio files that are used for dynamic prompts by an IVR
                                             				application.

For the
                                                   					 Extension Assigner, language must be English and prefix is en.

Step 7

paramspace english
                                                				  language en

#### Example:

```
Router(config-app-param)# paramspace english language en
```

Defines the
                                             				language of audio files that are used for dynamic prompts by an IVR
                                             				application.

For the
                                                   					 Extension Assigner, language must be English and prefix is en.

Step 8

paramspace english location location

#### Example:

```
Router(config-app-param)# paramspace english location flash:/EA/
```

Defines the
                                             				location of audio files that are used for dynamic prompts by an IVR
                                             				application.

For the
                                                   					 Extension Assigner, language must be English.

location —URL of the Tcl script for the extension
                                                   					 assigner service. Valid URLs can refer to TFTP or HTTP servers or to flash
                                                   					 memory.

Step 9

paramspace english prefix
                                                				  en

#### Example:

```
Router(config-app-param)# paramspace english prefix en
```

Defines the
                                             				prefix of audio files that are used for dynamic prompts by an IVR application.

For the
                                                   					 Extension Assigner, language must be English and prefix is en.

Step 10

end

#### Example:

```
Router(config-app-param)# end
```

Returns to
                                             				privileged EXEC mode.

### Specify the
                           	 Extension for Accessing Extension Assigner Application

To specify the
                                 		  extension number that installation technicians must dial to access the
                                 		  extension assigner application during onsite installation, perform the
                                 		  following steps.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer
                                       				  voice tag voip

- service service-name out-bound

- destination-pattern string

- session protocol sipv2

- session
                                       				  target ipv4: destination-address

- dtmf-relay
                                       				  rtp-nte

- codec g711ulaw

- no vad

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

dial-peer
                                                				  voice tag voip

#### Example:

```
Router(config)# dial-peer voice 5999 voip
```

- tag —Number used during configuration tasks to
                                                				  identify this dial peer.

Step 4

service service-name out-bound

#### Example:

```
Router(config-dial-peer)# service extensionassigner out-bound
```

Loads and
                                             				configures the extension assigner application on a dial peer.

service-name —Name must match the name that you
                                                   					 used to load the extension assigner Tcl script in the Configuring the Tcl Script section.

outbound —Required for Extension Assigner.

Step 5

destination-pattern string

#### Example:

```
Router(config-dial-peer)# destination pattern 1010
```

Specifies
                                             				either the prefix or the full E.164 telephone number (depending on the dial
                                             				plan) for a dial peer.

- string —Number that the installation technician
                                                				  calls when assigning an extension number to a phone.

Step 6

session protocol sipv2

#### Example:

```
Router(config-dial-peer)# session protocol sipv2
```

Designates a SIP loopback trunk for Extension Assigner
                                             				application.

Step 7

session
                                                				  target ipv4: destination-address

#### Example:

```
Router(config-dial-peer)# session target ipv4:172.16.200.200
```

Designates a
                                             				network-specific address to receive calls from a VoIP dial peer.

destination -IP address for the Cisco Unified CME
                                                   					 interface on this router.

Step 8

dtmf-relay
                                                				  rtp-nte

#### Example:

```
Router(config-dial-peer)# dtmf-relay rtp-nte
```

Specifies the
                                             				method for relaying dual tone multifrequency (DTMF) tones between two devices
                                             				as per RFC2833.

Step 9

codec g711ulaw

#### Example:

```
Router(config-dial-peer)# codec g711ulaw
```

Specifies the
                                             				voice coder rate of speech for a dial peer.

- g711ulaw -Option that represents the correct voice
                                                				  decoder rate. g711ulaw is the only codec supported with Extension Assigner
                                                				  application.

Step 10

no vad

#### Example:

```
Router(config-dial-peer)# no vad
```

Disables
                                             				voice activity detection (VAD) for the calls using a particular dial peer.

- Required for Extension
                                                				  Assigner.

Step 11

end

#### Example:

```
Router(config-dial-peer)# end
```

Returns to
                                             				privileged EXEC mode.

### Configure Provision-Tags for the Extension Assigner Feature

To modify Extension Assigner to use provision-tags, perform the
                                 		  following steps. By default, the extension assigner is enabled and uses ephone
                                 		  tags.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- extension-assigner tag-type { ephone-tag | provision-tag }

- end

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

extension-assigner tag-type { ephone-tag | provision-tag }

#### Example:

```
Router(config-telephony)# extension-assigner tag-type provision-tag
```

Specifies tag type to use to identify extension numbers for
                                             				Extension Assigner.

ephone-tag -Specifies that extension
                                                   					 assigner use the ephone tag to identify the extension number that is assigned
                                                   					 to a phone. The installation technician enters this number to assign an
                                                   					 extension number to a phone.

provision-tag -Specifies that
                                                   					 extension assigner use the provision-tag to identify the extension number that
                                                   					 is assigned to a phone. The installation technician enters this number to
                                                   					 assign an extension number to a phone.

Step 5

end

#### Example:

```
Router(config-telephony)# end
```

Returns to privileged EXEC mode.

### Configure
                           	 Temporary Extension Numbers for SCCP Phones That Use Extension Assigner

To create
                                 		  ephone-dn that is used as temporary extension numbers for phones to which an
                                 		  extension number will be assigned by Extension Assigner, perform the following
                                 		  steps for each temporary number to be created.

Tip

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag [ dual-line ]

- number number [ secondary number ] [ no-reg [ both | primary ]]

- trunk digit-string [ timeout seconds ]

- name name

- exit

- telephony-service

- auto assign dn-tag to dn-tag

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
Router(config)# ephone-dn 90
```

Enters
                                             				ephone-dn configuration mode, creates an ephone-dn, and optionally assigns it
                                             				dual-line status.

We recommend
                                                         				  that you use single-line mode for your temporary extension numbers.

Step 4

number number [ secondary number ] [ no-reg [ both | primary ]]

#### Example:

```
Router(config-ephone-dn)# number 9000
```

Configures a
                                             				valid extension number for this ephone-dn instance.

Step 5

trunk digit-string [ timeout seconds ]

#### Example:

```
Router(config-ephone-dn)# trunk 5999
```

(Optional)
                                             				Configures extension number to be automatically dialed for accessing the
                                             				extension assigner application.

digit-string - Must match the number that you
                                                   					 configured in the Specifying the Extension for Accessing Extension
                                                      						Assigner Application section.

Step 6

name name

#### Example:

```
RRouter(config-ephone-dn)# name hardware
```

(Optional)
                                             				Associates a name with this ephone-dn instance. This name is used for caller-ID
                                             				displays and in the local directory listings.

Must
                                                   					 follow the name order that is specified with the directory command.

Step 7

exit

#### Example:

```
Router(config-ephone-dn)# exit
```

Exits
                                             				ephone-dn configuration mode.

Step 8

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 9

auto assign dn-tag to dn-tag

#### Example:

```
Router(config-telephony)# auto assign 90 to 99
```

Automatically assigns ephone-dn tags to Cisco Unified IP phones as they
                                             				register for service with a Cisco Unified CME router.

Must
                                                   					 match the tags that you configured in earlier step.

Step 10

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

### Configure
                           	 Temporary Extension Numbers for SIP Phones That Use Extension Assigner

To create voice
                                 		  register dns to use as temporary extension numbers for phones in which an
                                 		  extension number is assigned by Extension Assigner, perform the following steps
                                 		  for each temporary number to be created.

Tip

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- auto-register

- password string

- auto-assign first dn to last dn

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
                                             				register global configuration mode.

Step 4

auto-register

#### Example:

```
Router(config-register-global)# auto-register
```

Enters
                                             				auto-register configuration mode.

Step 5

password string

#### Example:

```
Router(config-voice-auto-register)# password xxxx
```

Specifies
                                             				default password for auto registered phones.

Step 6

auto-assign first dn to last dn

#### Example:

```
Router(config-voice-auto-register)# auto-assign 90 to 99
```

Automatically
                                             				assigns voice register dn with these extensions to Cisco Unified IP phones as
                                             				they register for service with a Cisco Unified CME router.

Step 7

end

#### Example:

```
Router(config-voice-auto-register)# end
```

Returns to
                                             				privileged EXEC mode.

### Configure
                           	 Extension Numbers That Installation Technicians Can Assign to SCCP
                           	 Phones

To create
                                 		  ephone-dns for an extension numbers that the installation technicians can
                                 		  assign to phones, perform the following steps for each directory number to be
                                 		  created.

Tip

The readme file
                                             			 provided with this feature contains sample entries that you can edit to fit
                                             			 your needs.

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag [ dual-line ]

- number number [ secondary number ] [ no-reg [ both | primary ]]

- trunk digit-string [ timeout seconds ]

- name name

- exit

- telephony-service

- auto assign dn-tag to dn-tag

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

To change
                                                         				  an ephone-dn from dual-line to single-line mode or the reverse, first delete
                                                         				  the ephone-dn and then recreate it.

Step 4

number number [ secondary number ] [ no-reg [ both | primary ]]

#### Example:

```
Router(config-ephone-dn)# number 9000
```

Configures a
                                             				valid extension number for this ephone-dn instance.

Step 5

trunk digit-string [ timeout seconds ]

#### Example:

```
Router(config-ephone-dn)# trunk 5999
```

(Optional)
                                             				Configures extension number to be automatically dialed for accessing the
                                             				extension assigner application.

- digit-string - Must
                                                				  match the number that you configured in the Specifying the Extension for Accessing Extension
                                                   					 Assigner Application section.

Step 6

name name

#### Example:

```
Router(config-ephone-dn)# name hardware
```

(Optional)
                                             				Associates a name with this ephone-dn instance. This name is used for caller-ID
                                             				displays and in the local directory listings.

- Must follow the name order
                                                				  that is specified with the directory command.

Step 7

exit

#### Example:

```
Router(config-ephone-dn)# exit
```

Exits
                                             				ephone-dn configuration mode

Step 8

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 9

auto assign dn-tag to dn-tag

#### Example:

```
Router(config-telephony)# auto assign 90 to 99
```

- Must match the tags that
                                                   				  you configured in earlier step.

Step 10

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

### Configure
                           	 Extension Numbers That Installation Technicians Can Assign to SIP
                           	 Phones

To create voice register dns for an extension numbers that the
                                 		  installation technicians can assign to phones, perform the following steps for
                                 		  each directory number to be created.

Tip

The readme file provided with this feature contains sample entries
                                             			 that you can edit to fit your needs.

### SUMMARY STEPS

- enable

- configure terminal

- voice register dn tag

- number number

- name name

- end

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

voice register dn tag

#### Example:

```
Router(config)# voice register dn 20
```

Enters voice register dn configuration mode, and creates a voice
                                             				register dn.

Step 4

number number

#### Example:

```
Router(config-register-dn)# number 20
```

Configures a valid extension number for this voice register dn
                                             				instance.

Step 5

name name

#### Example:

```
Router(config-register-dn)# name hardware
```

(Optional) Associates a name with this voice register dn instance.
                                             				This name is used for caller-ID displays and in the local directory listings.

- Must follow the name
                                                				  order that is specified with the directory command.

Step 6

end

#### Example:

```
Router(config-register-dn)# end
```

Returns to privileged EXEC mode.

### Configure Ephones with Temporary MAC Addresses

Restriction

To create an ephone configuration with temporary MAC address for a
                                             			 Cisco Unified CME phone to which you want the installation technician to assign
                                             			 extension numbers, perform the following steps for each phone.

Max-ephone setting determines how many phones you can plug in at
                                                   				  one time. For example, if your max-ephone setting is ten more than the number
                                                   				  of phones to which you want to assign extension numbers, the you can plug in
                                                   				  ten phones at a time. If you plug in eleven phones, one phone will not register
                                                   				  or get a temporary extension number until you assign an extension to one of the
                                                   				  first ten phones and reset the eleventh phone.

For Cisco VG224 analog voice gateways with extension assigner, a
                                                   				  minimum of 24 temporary ephones is required.

Tip

The readme file provided with this feature contains some sample
                                             			 entries for this procedure that you can edit to fit your needs.

#### Before you begin

The max-ephone command must be configured for a
                                 		  value equal to at least one greater than the number of phones to which you want
                                 		  to assign extension numbers to allow the autoregister feature to automatically
                                 		  create at least one ephone for your temporary extension numbers.

You are permitted to set the max-ephone value higher than the number
                                             			 of users supported by your Cisco Unified CME licenses for the purpose of
                                             			 enrolling licensed phones using Extension Assigner.

### SUMMARY STEPS

- enable

- configure terminal

- enable phone-tag

- provision-tag number

- mac-address 02EA.EAEA. number

- type phone-type [ addon 1 module-type [ 2 module-type ]]

- button button-number{separator}dn-tag

- end

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

enable phone-tag

#### Example:

```
Router(config)# ephone 20
```

phone-tag-Maximum number is version and platform- specific.
                                                   					 Type ? to display range.

Number that the installation technician enters when assigning
                                                   					 an extension to a phone if Extension Assigner uses ephone-tags (default).

Step 4

provision-tag number

#### Example:

```
Router(config-ephone)# provision-tag 20
```

(Optional) Creates a unique sequence number to be used by
                                             				Extension Assigner to identify extension numbers to be assigned.

required only if you configured the provision-tag keyword with the extension-assigner tag-type command.

Step 5

mac-address 02EA.EAEA. number

#### Example:

```
Router(config-ephone)# mac-address 02EA. EAEA. 0020
```

Specifies a temporary MAC address number for this ephone.

For Extension Assigner, MAC address must begin with 02EA.EAEA.

- number - we
                                                				  strongly recommend that you make this number the same as the ephone number.

Step 6

type phone-type [ addon 1 module-type [ 2 module-type ]]

#### Example:

```
Router(config-ephone)# type 7960 addon 1 7914
```

Specifies the type of phone.

Step 7

button button-number{separator}dn-tag

#### Example:

```
Router(config-ephone)# button 1:1
```

Associates a button number and line characteristics with an
                                             				extension (ephone-dn).

Maximum number of buttons is determined by phone type.

The Cisco Unified IP Phone 7910 has only one line button, but
                                                         				  can be given two ephone-dn tags.

Step 8

end

#### Example:

```
Router(config-ephone)# end
```

Returns to privileged EXEC mode

### Configure Voice
                           	 Register Pools with Temporary MAC Addresses

Restriction

Max-pool
                                                   				  setting determines how many phones you can plug in at one time. For example, if
                                                   				  your max-pool setting is ten more than the number of phones to which you want
                                                   				  to assign extension numbers, the you can plug in ten phones at a time. If you
                                                   				  plug in eleven phones, one phone will not register or get a temporary extension
                                                   				  number until you assign an extension to one of the first ten phones and reset
                                                   				  the eleventh phone.

Tip

The readme file
                                             			 provided with this feature contains some sample entries for this procedure that
                                             			 you can edit to fit your needs.

#### Before you begin

The max-pool command must be configured for a value equal to at least one greater than the
                                 		  number of phones to which you want to assign extension numbers to allow the
                                 		  autoregister feature to automatically create at least one ephone for your
                                 		  temporary extension numbers.

You are
                                                   				  permitted to set the max-pool value higher than the number of users supported
                                                   				  by your Cisco Unified CME licenses for the purpose of enrolling licensed phones
                                                   				  using Extension Assigner.

For a
                                                   				  phone that needs to invoke Extension Assigner application for assign or
                                                   				  unassign operations, g711ulaw codec and dtmf-relay as rtp-nte needs to be
                                                   				  configured in voice register pool.

### SUMMARY STEPS

- enable

- configure terminal

- voice
                                       				  register pool pool-tag

- provision-tag number

- mac-address
                                       				  02EA.EAEA. number

- type phone-type [ addon
                                       				  1 module-type [ 2 module-type ]]

- number number dn dn-tag

- dtmf-relay rtp-nte

- codec g711ulaw

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

voice
                                                				  register pool pool-tag

#### Example:

```
Router(config)# voice register pool 20
```

phone-tag-Maximum number is version and platform- specific.
                                                   					 Type ? to display range.

Number
                                                   					 that the installation technician enters when assigning an extension to a phone.

Step 4

provision-tag number

#### Example:

```
Router(config-register-pool)# provision-tag 20
```

Creates a
                                             				unique sequence number to be used by Extension Assigner to identify extension
                                             				numbers to be assigned.

required
                                                   					 only if you configured the provision-tag keyword with the extension-assigner
                                                         						  tag-type command.

Step 5

mac-address
                                                				  02EA.EAEA. number

#### Example:

```
Router(config-register-pool)# mac-address 02EA. EAEA. 0020
```

Specifies a
                                             				temporary MAC address number for this phone.

For
                                                   					 Extension Assigner, MAC address must begin with 02EA.EAEA.

- number - we strongly recommend that you make this
                                                				  number same as the voice register pool number.

Step 6

type phone-type [ addon
                                                				  1 module-type [ 2 module-type ]]

#### Example:

```
Router(config-register-pool)# type 8860 addon 1 CKEM 2
```

Specifies
                                             				the type of phone.

Step 7

number number dn dn-tag

#### Example:

```
Router(config-register-pool)# number 1 dn 1
```

Associates
                                             				number and line characteristics with an extension (voice register dn).

Step 8

dtmf-relay rtp-nte

#### Example:

```
Router(config-register-pool)# dtmf-relay rtp-nte
```

(Optional) Specifies the method for relaying dual tone
                                             				multifrequency (DTMF) tones between two devices as per RFC2833.

This configuration is required only to perform assign or unassign
                                             				operation using Extension Assigner application.

Step 9

codec g711ulaw

#### Example:

```
Router(config-register-pool)# codec g711ulaw
```

(Optional) Specifies the voice coder rate of speech for a dial
                                             				peer. This configuration is required only to perform assign or unassign
                                             				operation using Extension Assigner application.

- g711ulaw -Option
                                                				  that represents the correct voice decoder rate. g711ulaw is the only codec
                                                				  supported with Extension Assigner application.

Step 10

end

#### Example:

```
Router(config-register-pool)# end
```

Returns to
                                             				privileged EXEC mode.

### Configure the
                           	 Router to Automatically Save Your Configuration

To automatically
                                 		  save your router configuration when the router is restarted, perform the
                                 		  following steps.

### SUMMARY STEPS

- enable

- configure
                                       				  terminal

- kron policy-list list-name

- cli write

- exit

- kron
                                       				  occurrence occurrence-name [ user username ] [[ in numdays: ] numhours: ] nummin { oneshot | recurring }

- policy-list list-name

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

configure
                                                				  terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

kron policy-list list-name

#### Example:

```
Router(config)# kron policy-list save-config
```

If the
                                                   					 value of the list-name argument is new, a new policy list structure is created.

If the
                                                   					 value of the list-name argument exists, the existing policy list structure is accessed. No editor
                                                   					 function is available, and the policy list is run in the order in which it was
                                                   					 configured.

You can also use the CLI command background save interval configured
                                                         				  under telephony-service to automatically save configurations on Unified CME.
                                                         				  This is as an alternative for the kron command.

Step 4

cli write

#### Example:

```
Router(config-kron-policy)# cli write
```

Specifies the
                                             				fully-qualified EXEC command and associated syntax to be added as an entry in
                                             				the Command Scheduler policy list.

Step 5

exit

#### Example:

```
Router(config-kron-policy)# exit
```

Returns to
                                             				global configuration mode.

Step 6

kron
                                                				  occurrence occurrence-name [ user username ] [[ in numdays: ] numhours: ] nummin { oneshot | recurring }

#### Example:

```
Router(config)# kron occurrence backup in 30 recurring
```

Specifies
                                             				schedule parameters for a Command Scheduler occurrence and enters
                                             				kron-occurrence configuration mode.

We
                                                   					 recommend that you configure your router to save your configuration every 30
                                                   					 minutes.

occurrence-name -Specifies the name of the
                                                   					 occurrence. Length of occurrence-name is from 1 to 31 characters. If the
                                                   					 occurrence-name is new, an occurrence structure is created. If the
                                                   					 occurrence-name is not new, the existing occurrence is edited.

user -(Optional) Used to identify a particular
                                                   					 user.

username -Name
                                                   					 of user.

in -Identifies
                                                   					 that the occurrence is to run after a specified time interval. The timer starts
                                                   					 when the occurrence is configured.

numdays :-
                                                   					 (Optional) Number of days. If used, add a colon after the number.

numhours :-
                                                   					 (Optional) Number of hours. If used, add a colon after the number.

nummin :-
                                                   					 (Optional) Number of minutes.

oneshot -Identifies that the occurrence is to run
                                                   					 only one time. After the occurrence has run, the configuration is removed.

recurring -Identifies that the occurrence is to run on a recurring
                                                   					 basis.

Step 7

policy-list list-name

#### Example:

```
Router(config-kron-occurrence)# policy-list save-config
```

Specifies a
                                             				Command Scheduler policy list.

Step 8

end

#### Example:

```
Router(config-kron-occurrence)# end
```

Returns to
                                             				privileged EXEC mode.

### Provide the
                           	 Installation Technician with the Required Information

Before the
                              		installation technician can assign extension numbers to the new phones, you
                              		must provide the following information:

- How many phones the
                                 		  installation technician can plug in at one time. This is determined by the
                                 		  number of temporary MAC addresses that you configured.

- Which extension number to dial to
                                 		  access the extension assigner application.

- Whether the number is dialed
                                 		  automatically when a phone goes off hook (applicable only to SCCP phones).

- What password to
                                 		  enter to access the application.

- Which tag numbers
                                 		  to enter to assign an extension to each phone.

## Configure Extension Assigner Synchronization

### Configure the XML
                           	 Interface for the Secondary Backup Router

To configure the
                                 		  secondary backup router to activate the XML interface required to receive
                                 		  configuration change information from the primary router, perform the following
                                 		  steps.

If there are
                                             			 HTTP connection issues between the primary router and the secondary backup
                                             			 router during automatic synchronization, the extension assigner synchronization
                                             			 changes are lost.

Restriction

Automatic
                                                   				  synchronization for new or replacement routers is not supported.

Extension
                                                   				  assigner preconfiguration must be manually performed on the secondary backup
                                                   				  router.

#### Before you begin

The XML
                                       				interface, provided through the Cisco IOS XML Infrastructure (IXI), must be
                                       				configured. See Configuring
                                          				  the XML API .

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service | voice register
                                       				  global

- xml user user-name password password
                                       				  privilege-level

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

telephony-service | voice register
                                                				  global

#### Example:

```
Router(config)# telephony-service
Router(config)# voice register global
```

Step 4

xml user user-name password password
                                                				  privilege-level

#### Example:

```
Router(config-telephony)# xml user user23 password 3Rs92uzQ 15
Router(config-register-global)# xml user user23 password 3Rs92uzQ 15
```

Defines an
                                             				authorized user.

user-name —Username of the authorized user.

password —Password to use for access.

privilege-level —Level of access to Cisco IOS
                                                   					 commands to be granted to this user. Only the commands with the same or a lower
                                                   					 level can be executed via XML. Range is 0 to 15.

Step 5

end

#### Example:

```
Router(config-telephony)# end
Router(config-register-global)# end
```

Returns to
                                             				privileged EXEC mode.

### Configure
                           	 Extension Assigner Synchronization on the Primary Router

To configure the
                                 		  primary router to enable automatic synchronization to the secondary backup
                                 		  router, perform the following steps.

#### Before you begin

XML interface
                                       				for secondary backup router is configured. See Configuring
                                          				  the XML Interface for the Secondary Backup Router .

The secondary
                                       				backup router’s IP address must already be configured using the ip
                                             					 source-address command in telephony-service configuration mode.

Phone
                                                   				  configurations such as MAC address, pool-tag, and phone type are saved as part
                                                   				  of synchronization for Extension Assigner feature.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service | voice register
                                       				  global

- standby
                                       				  username username password password

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

telephony-service | voice register
                                                				  global

#### Example:

```
Router(config)# telephony-service
Router(config)# voice register global
```

Step 4

standby
                                                				  username username password password

#### Example:

```
Router(config-telephony)# standby username user23 password 3Rs92uzQ
Router(config-register-global)# standby username user23 password 3Rs92uzQ
```

Defines an
                                             				authorized user.

Same
                                                   					 username and password that was previously defined for the XML interface on the
                                                   					 secondary backup router.

Step 5

end

#### Example:

```
Router(config-telephony)# end
Router(config-register-global)# end
```

Returns to
                                             				privileged EXEC mode.

## Assign Extension
                        	 Numbers Onsite by Using Extension Assigner

The following tasks
                           		are performed by the installation technician at the customer’s site:

### Assign New
                           	 Extension Numbers

Initially, when
                                 		  you install a phone, it is assigned a temporary, random extension number. To
                                 		  access Extension Assigner and assign the appropriate extension number to this
                                 		  phone, perform the following steps.

Step 1

Get the
                                          			 information you need to use extension assigner from your system administrator.
                                          			 For a list of this information, see Provide
                                             				the Installation Technician with the Required Information .

Step 2

Dial the
                                          			 appropriate extension number to access the extension assigner system.

Step 3

Enter the password for the extension assigner and press # .

Step 4

Enter the ID number that represents this phone’s extension and press # .

Step 5

If the
                                          			 extension is not assigned to another phone, press 1 to
                                          			 confirm that you want to assign the extension to your phone, then hang up.
                                          			 After the phone resets, the assignment is complete.

Step 6

If the
                                          			 extension is assigned to another phone that is idle:

Press 2 to
                                                				  confirm that you want to unassign the extension from the other phone.

Hang up.

Repeat
                                                				  this procedure beginning at Step 2 .

Step 7

If the
                                          			 extension is assigned to another phone that is in use, either:

Return to Step 5 to enter another extension number.

Perform the procedures in the Unassigning an Extension Number section and then repeat this procedure beginning at Step 2 .

### Unassign an
                           	 Extension Number

After the new
                                 		  extension number is assigned, you may find that you assigned the wrong number
                                 		  or that your original dial plan has changed. To unassign the wrong number so
                                 		  that it can be used by another phone, perform the following steps.

You can
                                             			 unassign the extension number of the phone that is used to dial in to the
                                             			 Extension Assigner or the extension number of another phone that has a
                                             			 provision-tag configured.

Step 1

Get the
                                          			 information you need to use extension assigner from your system administrator.
                                          			 For a list of this information, see Provide
                                             				the Installation Technician with the Required Information .

Step 2

Dial the
                                          			 appropriate extension number to access the extension assigner system.

Step 3

Enter the
                                          			 password for the extension assigner and press # .

Step 4

Enter the
                                          			 provision-tag of the phone that needs to be unassigned, and press # .

Step 5

When you enter
                                          			 the provision-tag for the phone extension that needs to be unassigned, you are
                                          			 prompted to press 2 followed by # to
                                          			 confirm that you want to unassign the extension from the phone.

Step 6

Hang up.

### Reassign the
                           	 Current Extension Number

If you must
                                       				replace a broken phone or you want to reassign an extension number, perform the
                                       				following steps.

You can reassign
                                             			 a number to a phone only if that number:

Is not
                                                   				  assigned to another phone

Is assigned
                                                   				  to another phone and that phone is idle

Is assigned
                                                   				  to another phone and you first unassign the extension

Step 1

Get the
                                          			 information you need to use extension assigner from your system administrator.
                                          			 For a list of this information, see Provide
                                             				the Installation Technician with the Required Information .

Step 2

Dial the
                                          			 appropriate extension number to access the extension assigner system.

Step 3

Enter the
                                          			 password for the extension assigner and press # .

Step 4

Enter the ID
                                          			 number that represents this phone’s extension and press # .

Step 5

If the
                                          			 extension is not assigned to another phone, press 1 to
                                          			 confirm that you want to assign the extension to your phone, then hang up.
                                          			 After the phone resets, the reassignment is complete.

Step 6

If the
                                          			 extension is assigned to another phone that is idle:

- Press 2 to
                                                				  confirm that you want to unassign the extension from the other phone.

- Hang up.

- Perform the procedure in
                                                				  the Assign
                                                   					 New Extension Numbers section.

Step 7

If the
                                          			 extension is assigned to another phone that is in use, either:

- Return to Step 5 to enter another extension number.

- Perform the procedures in
                                                				  the Unassign
                                                   					 an Extension Number section and the Assign
                                                   					 New Extension Numbers section.

## Verify Extension
                        	 Assigner Configuration for SCCP Phones

Step 1

Use the debug ephone
                                             				  extension-assigner command to display status messages produced by
                                       			 the extension assigner application.

Step 2

Use the debug voip application
                                             				  script command to display status messages produced by the server
                                       			 as it runs the assigner application Tcl script.

Step 3

Use the debug ephone
                                          				state command as described in the Cisco IOS Debug Command Reference.

## Verify Extension
                        	 Assigner Configuration for SIP Phones

Step 1

Use the debug voice register events and debug voice register error commands to display status messages produced by the
                                       			 extension assigner application.

Step 2

Use the debug voip application
                                             				  script command to display status messages produced by the server
                                       			 as it runs the assigner application Tcl script.

Step 3

Use the debug ccsip messages and debug ccsip error commands to display status messages for
                                       			 unregistration of phones.

## Configuration Examples for Extension Assigner

### Example for
                           	 Extension Assigner on SCCP Phone

This example shows
                                 		  a router configuration with the following characteristics:

- The extension that the
                                    			 installation technician dials to access the extension assigner application is
                                    			 0999.

- The password that the
                                    			 installation technician enters to access the extension assigner application is
                                    			 1234.

- The auto
                                          				  assign command is configured to assign extensions 0001 to 0005.

- The installation technician
                                    			 can use extension assigner to assign extension numbers 6001 to 6005.

- The extension assigner uses
                                    			 the provision-tag to identify which ephone configuration and extension numbers
                                    			 to assign to the phone.

- The auto-reg-ephone command is shown but required,
                                    			 since it is enabled by default.

- The kron command
                                    			 is used to automatically save the router configuration.

- The max-ephone and max-dn
                                    			 settings of 51 are high enough to allow the installation technician to assign
                                    			 extensions to 50 phones, plugging them in one at a time. If the installation
                                    			 technician is assigning extensions to 40 phones, 11 can be plugged in one at a
                                    			 time. The exception is if you use CiscoVG224AnalogVoiceGateways. Extension
                                    			 assigner creates 24 ephones for each CiscoVG224AnalogVoiceGateway, one for
                                    			 each port.

```
Router# show running-config
```

```
version 12.4
```

```
no service password-encryption
```

```
!
```

```
hostname Test-Router
```

```
!
```

```
boot-start-marker
```

```
boot system flash:c2800nm-ipvoice-mz.2006-05-31.GOPED_DEV
```

```
boot-end-marker
```

```
!
```

```
enable password ww
```

```
!
```

```
no aaa new-model
```

```
!
```

```
resource policy
```

```
!
```

```
ip cef
```

```
no ip dhcp use vrf connected
```

```
!
```

```
ip dhcp pool pool21
```

```
network 172.21.0.0 255.255.0.0
```

```
default-router 172.21.200.200
```

```
option 150 ip 172.30.1.60
```

```
!
```

```
no ip domain lookup
```

```
!
```

```
application
```

```
service EA flash:ea/app-cme-ea-2.0.0.0.tcl
```

```
paramspace english index 0
```

```
paramspace english language en
```

```
param ea-password 1234
```

```
paramspace english location flash:ea/
```

```
paramspace english prefix en
```

```
!
```

```
interface GigabitEthernet0/0
```

```
no ip address
```

```
duplex auto
```

```
speed 100
```

```
no keepalive
```

```
!
```

```
interface GigabitEthernet0/0.21
```

```
encapsulation dot1Q 21
```

```
ip address 172.21.200.200 255.255.0.0
```

```
ip http server
```

```
!
```

```
control-plane
```

```
!
```

```
dial-peer voice 999 voip
```

```
service EA out-bound
```

```
destination-pattern 0999
```

```
session target ipv4:172.21.200.200
```

```
dtmf-relay h245-alphanumeric
```

```
codec g711ulaw
```

```
no vad
```

```
!
```

```
telephony-service
```

```
extension-assigner tag-type provision-tag
```

```
max-ephones 51
```

```
max-dn 51
```

```
ip source-address 172.21.200.200 port 2000
```

```
auto-reg-ephone
```

```
auto assign 101 to 105
```

```
system message Test-CME
```

```
create cnf-files version-stamp 7960 Jun 14 2006 05:37:34
```

```
!
```

```
ephone-dn  1  dual-line
```

```
number 6001
```

```
!
```

```
ephone-dn  2  dual-line
```

```
number 6002
```

```
!
```

```
ephone-dn  3  dual-line
```

```
number 6003
```

```
!
```

```
ephone-dn  4  dual-line
```

```
number 6004
```

```
!
```

```
ephone-dn  5  dual-line
```

```
number 6005
```

```
!
```

```
ephone-dn  101
```

```
number 0101
```

```
label Temp-Line-not assigned yet
```

```
!
```

```
ephone-dn  102
```

```
number 0102
```

```
label Temp-Line-not assigned yet
```

```
!
```

```
ephone-dn  103
```

```
number 0103
```

```
label Temp-Line-not assigned yet
```

```
!
```

```
ephone-dn  104
```

```
number 0104
```

```
label Temp-Line-not assigned yet
```

```
!
```

```
ephone-dn  105
```

```
number 0105
```

```
label Temp-Line-not assigned yet
```

```
!
```

```
ephone  1
```

```
provision-tag 101
```

```
mac-address 02EA.EAEA.0001
```

```
button  1:1
```

```
!
```

```
ephone  2
```

```
provision-tag 102
```

```
mac-address 02EA.EAEA.0002
```

```
button  1:2
```

```
!
```

```
ephone  3
```

```
provision-tag 103
```

```
mac-address 02EA.EAEA.0003
```

```
button  1:3
```

```
!
```

```
ephone  4
```

```
provision-tag 104
```

```
mac-address 02EA.EAEA.0004
```

```
button  1:4
```

```
!
```

```
ephone  5
```

```
provision-tag 105
```

```
mac-address 02EA.EAEA.0005
```

```
button  1:5
```

```
!
```

```
kron occurrence backup in 30 recurring
```

```
policy-list writeconfig
```

```
!
```

```
kron policy-list writeconfig
```

```
cli write
```

```
!
```

```
line con 0
```

```
line aux 0
```

```
line vty 0 4
```

```
logging synchronous
```

```
!
```

```
no scheduler max-task-time
```

```
scheduler allocate 20000 1000
```

```
!
```

```
end
```

### Example for
                           	 Extension Assigner on SIP Phone

The following
                                 		  example shows that provision tag 1001 is configured for voice register pool 1
                                 		  and provision tag 1002 is configured for voice register pool 2:

```
voice register global
 auto-register
  password cisco1234
  auto assign 101-102

voice register dn 1001
 number 1001

voice register dn 1002
 number 1002

voice register pool 1
 provision-tag 1001
 mac-address 02EA.EAEA.0001
 number 1 dn 1001

voice register pool 2
 provision-tag 1002
 mac-address 02EA.EAEA.0002
 number 2 dn 1002
```

### Example for
                           	 Extension Assigner Synchronization

Primary Router:
                                    			 Example

The extension
                                 		  assigner is authorized to send configuration change information from the
                                 		  primary router to the secondary backup router.

```
telephony-service
standby username user555 password purplehat
```

Secondary Backup Router:
                                    			 Example

System components
                                 		  are enabled and the XML interface is readied to receive configuration change
                                 		  information.

```
ip http server
```

```
ixi transport http
```

```
no shutdown
```

```
ixi application cme
```

```
no shutdown
```

```
telephony-service
```

```
xml user user555 password purplehat 15
```

### Feature
                           	 Information for Extension Assigner

The following table
                              		provides release information about the feature or features described in this
                              		module. This table lists only the software release that introduced support for
                              		a given feature in a given software release train. Unless noted otherwise,
                              		subsequent releases of that software release train also support that feature.

Use Cisco Feature
                              		Navigator to find information about platform support and Cisco software image
                              		support. To access Cisco Feature Navigator, go to www.cisco.com/go/cfn .
                              		An account on Cisco.com is not required.

Feature Name

Cisco
                                          				  Unfiied CME Version

Feature
                                          				  Information

Extension
                                          				  Assigner for SIP Phones

11.6

Enables the
                                          				  installation technicians to assign extension numbers to SIP Phones configured
                                          				  on Cisco Unified CME.

Extension
                                          				  Assigner Synchronization

4.2(1)

Enables the
                                          				  secondary backup router to automatically receive any changes made to ephone
                                          				  mac-addresess in the primary router.

Extension
                                          				  Assigner

4.0(3)

Enables
                                          				  installation technicians to assign extension numbers to Cisco Unified CME SCCP
                                          				  phones without accessing the server.

| Note | All
                                                         					 phone configurations such as dn and pool that are generated as part of the auto
                                                         					 registration process are persistent configurations(If the command background save
                                                               						  interval is configured under telephony-service). These phone
                                                         					 configurations are available on Unified CME even after an event of router
                                                         					 reload. |
|---|---|

| Note | For manually
                                             		  registered phones, ephone (or voice register pool) and ephone-dn (or voice
                                             		  register dn) are manually created. |
|---|---|

| Note | For SIP Phones,
                                             		  you need not create temporary dn if auto registration is used. |
|---|---|

| Note | Because this
                                          		feature is implemented using a Tcl script and audio files, you must place the
                                          		script and associated audio prompt files in the correct directory. Do not edit
                                          		this script; just configure Cisco Unified CME to load the appropriate script. |
|---|---|

| Note | You cannot
                                                		  unassign the extension number of a phone if it is in use. The phone has to be
                                                		  in idle or unregistered state. |
|---|---|

| Step 1 | Plug in a
                                             			 specified number of new phones. |
|---|---|
| Step 2 | Wait for the
                                             			 phones to be assigned temporary, random extension numbers. |
| Step 3 | Dial a
                                             			 specified number to access the extension assigner application. |
| Step 4 | Enter a
                                             			 specified password. |
| Step 5 | Enter a tag
                                             			 that identifies an extension number and enables the installation technician to
                                             			 perform one of the following tasks: Assign a
                                                      					 new extension number to a phone. Unassign
                                                      					 the current extension number. Reassign
                                                      					 an extension number. |

| Note | Do not edit the
                                          		  Tcl script |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Go to the
                                          			 Cisco Unified CME software download website at http://software.cisco.com/download/type.html?mdfid=277641082&catid=null . | Gives you
                                             				access to Cisco Unified CME software downloads. |
| Step 2 | Download the
                                          			 Cisco Unified CME extension assigner tar archive to a TFTP server that is
                                          			 accessible to the Cisco Unified CME router. | This tar archive contains the extension assigner Tcl script and the default audio files that you need for the extension assigner
                                                service. |
| Step 3 | enable Example: Router> enable | Enters
                                          			 global configuration mode. |
| Step 4 | archive tar /xtract source-url
                                                				  destination-url Example: Router# archive tar /xtract tftp://192.168.1.1/app-cme-ea-2.0.0.0.tar flash: | Uncompresses
                                             				the files in the archive file and copies them to a location that is accessible
                                             				by the Cisco Unified CME router. source-url —URL of the source of the extension
                                                   				  assigner TAR file. Valid URLs can refer to TFTP or HTTP servers or to flash
                                                   				  memory. location —URL of the destination of the extension
                                                   				  assigner TAR file, including its Tcl script and audio files. Valid URLs can
                                                   				  refer to TFTP or HTTP servers or to flash memory. |

| Note | To change the
                                          		  password, you must remove the existing extension assigner service and create a
                                          		  new service that defines a new password. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | application Example: Router(config)# application | Enters
                                          			 application configuration mode to configure packages and services. |
| Step 4 | service service-name
                                                				  location Example: Router(config-app)# service EA flash:/EA/ | Enters
                                             				service parameter configuration mode to configure parameters for the call-queue
                                             				service. service-name —Name of the extension assigner
                                                   					 service. This arbitrary name is used to identify the service during
                                                   					 configuration tasks. location —URL of the Tcl script for the extension
                                                   					 assigner service. Valid URLs can refer to TFTP or HTTP servers or to flash
                                                   					 memory. |
| Step 5 | param ea-password password Example: Router(config-app-param)# param ea-password 1234 | Sets the
                                             				password that installation technicians enter to access the extension assigner
                                             				application. password —Numerical password that installation
                                                   					 technicians enter to access the extension assigner application. Length: 2 to 10
                                                   					 digits. |
| Step 6 | paramspace english
                                                				  index number Example: Router(config-app-param)# paramspace english index 0 | Defines the
                                             				language of audio files that are used for dynamic prompts by an IVR
                                             				application. For the
                                                   					 Extension Assigner, language must be English and prefix is en. |
| Step 7 | paramspace english
                                                				  language en Example: Router(config-app-param)# paramspace english language en | Defines the
                                             				language of audio files that are used for dynamic prompts by an IVR
                                             				application. For the
                                                   					 Extension Assigner, language must be English and prefix is en. |
| Step 8 | paramspace english location location Example: Router(config-app-param)# paramspace english location flash:/EA/ | Defines the
                                             				location of audio files that are used for dynamic prompts by an IVR
                                             				application. For the
                                                   					 Extension Assigner, language must be English. location —URL of the Tcl script for the extension
                                                   					 assigner service. Valid URLs can refer to TFTP or HTTP servers or to flash
                                                   					 memory. |
| Step 9 | paramspace english prefix
                                                				  en Example: Router(config-app-param)# paramspace english prefix en | Defines the
                                             				prefix of audio files that are used for dynamic prompts by an IVR application. For the
                                                   					 Extension Assigner, language must be English and prefix is en. |
| Step 10 | end Example: Router(config-app-param)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | dial-peer
                                                				  voice tag voip Example: Router(config)# dial-peer voice 5999 voip | Enters
                                          			 dial-peer configuration mode. tag —Number used during configuration tasks to
                                                				  identify this dial peer. |
| Step 4 | service service-name out-bound Example: Router(config-dial-peer)# service extensionassigner out-bound | Loads and
                                             				configures the extension assigner application on a dial peer. service-name —Name must match the name that you
                                                   					 used to load the extension assigner Tcl script in the Configuring the Tcl Script section. outbound —Required for Extension Assigner. |
| Step 5 | destination-pattern string Example: Router(config-dial-peer)# destination pattern 1010 | Specifies
                                             				either the prefix or the full E.164 telephone number (depending on the dial
                                             				plan) for a dial peer. string —Number that the installation technician
                                                				  calls when assigning an extension number to a phone. |
| Step 6 | session protocol sipv2 Example: Router(config-dial-peer)# session protocol sipv2 | Designates a SIP loopback trunk for Extension Assigner
                                             				application. |
| Step 7 | session
                                                				  target ipv4: destination-address Example: Router(config-dial-peer)# session target ipv4:172.16.200.200 | Designates a
                                             				network-specific address to receive calls from a VoIP dial peer. destination -IP address for the Cisco Unified CME
                                                   					 interface on this router. |
| Step 8 | dtmf-relay
                                                				  rtp-nte Example: Router(config-dial-peer)# dtmf-relay rtp-nte | Specifies the
                                             				method for relaying dual tone multifrequency (DTMF) tones between two devices
                                             				as per RFC2833. |
| Step 9 | codec g711ulaw Example: Router(config-dial-peer)# codec g711ulaw | Specifies the
                                             				voice coder rate of speech for a dial peer. g711ulaw -Option that represents the correct voice
                                                				  decoder rate. g711ulaw is the only codec supported with Extension Assigner
                                                				  application. |
| Step 10 | no vad Example: Router(config-dial-peer)# no vad | Disables
                                             				voice activity detection (VAD) for the calls using a particular dial peer. Required for Extension
                                                				  Assigner. |
| Step 11 | end Example: Router(config-dial-peer)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters telephony-service configuration mode. |
| Step 4 | extension-assigner tag-type { ephone-tag \| provision-tag } Example: Router(config-telephony)# extension-assigner tag-type provision-tag | Specifies tag type to use to identify extension numbers for
                                             				Extension Assigner. ephone-tag -Specifies that extension
                                                   					 assigner use the ephone tag to identify the extension number that is assigned
                                                   					 to a phone. The installation technician enters this number to assign an
                                                   					 extension number to a phone. provision-tag -Specifies that
                                                   					 extension assigner use the provision-tag to identify the extension number that
                                                   					 is assigned to a phone. The installation technician enters this number to
                                                   					 assign an extension number to a phone. |
| Step 5 | end Example: Router(config-telephony)# end | Returns to privileged EXEC mode. |

| Tip | The
                                          		  readme file that is included with the script contains some sample entries for
                                          		  this procedure that you can edit to fit your needs. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn dn-tag [ dual-line ] Example: Router(config)# ephone-dn 90 | Enters
                                             				ephone-dn configuration mode, creates an ephone-dn, and optionally assigns it
                                             				dual-line status. Note We recommend
                                                         				  that you use single-line mode for your temporary extension numbers. | Note | We recommend
                                                         				  that you use single-line mode for your temporary extension numbers. |
| Note | We recommend
                                                         				  that you use single-line mode for your temporary extension numbers. |
| Step 4 | number number [ secondary number ] [ no-reg [ both \| primary ]] Example: Router(config-ephone-dn)# number 9000 | Configures a
                                             				valid extension number for this ephone-dn instance. |
| Step 5 | trunk digit-string [ timeout seconds ] Example: Router(config-ephone-dn)# trunk 5999 | (Optional)
                                             				Configures extension number to be automatically dialed for accessing the
                                             				extension assigner application. digit-string - Must match the number that you
                                                   					 configured in the Specifying the Extension for Accessing Extension
                                                      						Assigner Application section. |
| Step 6 | name name Example: RRouter(config-ephone-dn)# name hardware | (Optional)
                                             				Associates a name with this ephone-dn instance. This name is used for caller-ID
                                             				displays and in the local directory listings. Must
                                                   					 follow the name order that is specified with the directory command. |
| Step 7 | exit Example: Router(config-ephone-dn)# exit | Exits
                                             				ephone-dn configuration mode. |
| Step 8 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 9 | auto assign dn-tag to dn-tag Example: Router(config-telephony)# auto assign 90 to 99 | Automatically assigns ephone-dn tags to Cisco Unified IP phones as they
                                             				register for service with a Cisco Unified CME router. Must
                                                   					 match the tags that you configured in earlier step. |
| Step 10 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

| Note | We recommend
                                                         				  that you use single-line mode for your temporary extension numbers. |
|---|---|

| Tip | The
                                          		  readme file that is included with the script contains some sample entries for
                                          		  this procedure that you can edit to fit your needs. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register global Example: Router(config)# voice register global | Enters voice
                                             				register global configuration mode. |
| Step 4 | auto-register Example: Router(config-register-global)# auto-register | Enters
                                             				auto-register configuration mode. |
| Step 5 | password string Example: Router(config-voice-auto-register)# password xxxx | Specifies
                                             				default password for auto registered phones. |
| Step 6 | auto-assign first dn to last dn Example: Router(config-voice-auto-register)# auto-assign 90 to 99 | Automatically
                                             				assigns voice register dn with these extensions to Cisco Unified IP phones as
                                             				they register for service with a Cisco Unified CME router. |
| Step 7 | end Example: Router(config-voice-auto-register)# end | Returns to
                                             				privileged EXEC mode. |

| Tip | The readme file
                                             			 provided with this feature contains sample entries that you can edit to fit
                                             			 your needs. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn dn-tag [ dual-line ] Example: Router(config)# ephone-dn 20 | Enters
                                             				ephone-dn configuration mode, creates an ephone-dn, and optionally assigns it
                                             				dual-line status. Note To change
                                                         				  an ephone-dn from dual-line to single-line mode or the reverse, first delete
                                                         				  the ephone-dn and then recreate it. | Note | To change
                                                         				  an ephone-dn from dual-line to single-line mode or the reverse, first delete
                                                         				  the ephone-dn and then recreate it. |
| Note | To change
                                                         				  an ephone-dn from dual-line to single-line mode or the reverse, first delete
                                                         				  the ephone-dn and then recreate it. |
| Step 4 | number number [ secondary number ] [ no-reg [ both \| primary ]] Example: Router(config-ephone-dn)# number 9000 | Configures a
                                             				valid extension number for this ephone-dn instance. |
| Step 5 | trunk digit-string [ timeout seconds ] Example: Router(config-ephone-dn)# trunk 5999 | (Optional)
                                             				Configures extension number to be automatically dialed for accessing the
                                             				extension assigner application. digit-string - Must
                                                				  match the number that you configured in the Specifying the Extension for Accessing Extension
                                                   					 Assigner Application section. |
| Step 6 | name name Example: Router(config-ephone-dn)# name hardware | (Optional)
                                             				Associates a name with this ephone-dn instance. This name is used for caller-ID
                                             				displays and in the local directory listings. Must follow the name order
                                                				  that is specified with the directory command. |
| Step 7 | exit Example: Router(config-ephone-dn)# exit | Exits
                                             				ephone-dn configuration mode |
| Step 8 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 9 | auto assign dn-tag to dn-tag Example: Router(config-telephony)# auto assign 90 to 99 | Automatically assigns ephone-dn tags to Cisco Unified IP phones as they
                                             				register for service with a Cisco Unified CME router. Must match the tags that
                                                   				  you configured in earlier step. |
| Step 10 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

| Note | To change
                                                         				  an ephone-dn from dual-line to single-line mode or the reverse, first delete
                                                         				  the ephone-dn and then recreate it. |
|---|---|

| Tip | The readme file provided with this feature contains sample entries
                                             			 that you can edit to fit your needs. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice register dn tag Example: Router(config)# voice register dn 20 | Enters voice register dn configuration mode, and creates a voice
                                             				register dn. |
| Step 4 | number number Example: Router(config-register-dn)# number 20 | Configures a valid extension number for this voice register dn
                                             				instance. |
| Step 5 | name name Example: Router(config-register-dn)# name hardware | (Optional) Associates a name with this voice register dn instance.
                                             				This name is used for caller-ID displays and in the local directory listings. Must follow the name
                                                				  order that is specified with the directory command. |
| Step 6 | end Example: Router(config-register-dn)# end | Returns to privileged EXEC mode. |

| Restriction | To create an ephone configuration with temporary MAC address for a
                                             			 Cisco Unified CME phone to which you want the installation technician to assign
                                             			 extension numbers, perform the following steps for each phone. Max-ephone setting determines how many phones you can plug in at
                                                   				  one time. For example, if your max-ephone setting is ten more than the number
                                                   				  of phones to which you want to assign extension numbers, the you can plug in
                                                   				  ten phones at a time. If you plug in eleven phones, one phone will not register
                                                   				  or get a temporary extension number until you assign an extension to one of the
                                                   				  first ten phones and reset the eleventh phone. For Cisco VG224 analog voice gateways with extension assigner, a
                                                   				  minimum of 24 temporary ephones is required. |
|---|---|

| Tip | The readme file provided with this feature contains some sample
                                             			 entries for this procedure that you can edit to fit your needs. |
|---|---|

| Note | You are permitted to set the max-ephone value higher than the number
                                             			 of users supported by your Cisco Unified CME licenses for the purpose of
                                             			 enrolling licensed phones using Extension Assigner. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | enable phone-tag Example: Router(config)# ephone 20 | Enters ephone configuration mode. phone-tag-Maximum number is version and platform- specific.
                                                   					 Type ? to display range. Number that the installation technician enters when assigning
                                                   					 an extension to a phone if Extension Assigner uses ephone-tags (default). |
| Step 4 | provision-tag number Example: Router(config-ephone)# provision-tag 20 | (Optional) Creates a unique sequence number to be used by
                                             				Extension Assigner to identify extension numbers to be assigned. required only if you configured the provision-tag keyword with the extension-assigner tag-type command. |
| Step 5 | mac-address 02EA.EAEA. number Example: Router(config-ephone)# mac-address 02EA. EAEA. 0020 | Specifies a temporary MAC address number for this ephone. For Extension Assigner, MAC address must begin with 02EA.EAEA. number - we
                                                				  strongly recommend that you make this number the same as the ephone number. |
| Step 6 | type phone-type [ addon 1 module-type [ 2 module-type ]] Example: Router(config-ephone)# type 7960 addon 1 7914 | Specifies the type of phone. |
| Step 7 | button button-number{separator}dn-tag Example: Router(config-ephone)# button 1:1 | Associates a button number and line characteristics with an
                                             				extension (ephone-dn). Maximum number of buttons is determined by phone type. Note The Cisco Unified IP Phone 7910 has only one line button, but
                                                         				  can be given two ephone-dn tags. | Note | The Cisco Unified IP Phone 7910 has only one line button, but
                                                         				  can be given two ephone-dn tags. |
| Note | The Cisco Unified IP Phone 7910 has only one line button, but
                                                         				  can be given two ephone-dn tags. |
| Step 8 | end Example: Router(config-ephone)# end | Returns to privileged EXEC mode |

| Note | The Cisco Unified IP Phone 7910 has only one line button, but
                                                         				  can be given two ephone-dn tags. |
|---|---|

| Restriction | Max-pool
                                                   				  setting determines how many phones you can plug in at one time. For example, if
                                                   				  your max-pool setting is ten more than the number of phones to which you want
                                                   				  to assign extension numbers, the you can plug in ten phones at a time. If you
                                                   				  plug in eleven phones, one phone will not register or get a temporary extension
                                                   				  number until you assign an extension to one of the first ten phones and reset
                                                   				  the eleventh phone. |
|---|---|

| Tip | The readme file
                                             			 provided with this feature contains some sample entries for this procedure that
                                             			 you can edit to fit your needs. |
|---|---|

| Note | You are
                                                   				  permitted to set the max-pool value higher than the number of users supported
                                                   				  by your Cisco Unified CME licenses for the purpose of enrolling licensed phones
                                                   				  using Extension Assigner. For a
                                                   				  phone that needs to invoke Extension Assigner application for assign or
                                                   				  unassign operations, g711ulaw codec and dtmf-relay as rtp-nte needs to be
                                                   				  configured in voice register pool. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice
                                                				  register pool pool-tag Example: Router(config)# voice register pool 20 | Enters voice
                                          			 register pool configuration mode. phone-tag-Maximum number is version and platform- specific.
                                                   					 Type ? to display range. Number
                                                   					 that the installation technician enters when assigning an extension to a phone. |
| Step 4 | provision-tag number Example: Router(config-register-pool)# provision-tag 20 | Creates a
                                             				unique sequence number to be used by Extension Assigner to identify extension
                                             				numbers to be assigned. required
                                                   					 only if you configured the provision-tag keyword with the extension-assigner
                                                         						  tag-type command. |
| Step 5 | mac-address
                                                				  02EA.EAEA. number Example: Router(config-register-pool)# mac-address 02EA. EAEA. 0020 | Specifies a
                                             				temporary MAC address number for this phone. For
                                                   					 Extension Assigner, MAC address must begin with 02EA.EAEA. number - we strongly recommend that you make this
                                                				  number same as the voice register pool number. |
| Step 6 | type phone-type [ addon
                                                				  1 module-type [ 2 module-type ]] Example: Router(config-register-pool)# type 8860 addon 1 CKEM 2 | Specifies
                                             				the type of phone. |
| Step 7 | number number dn dn-tag Example: Router(config-register-pool)# number 1 dn 1 | Associates
                                             				number and line characteristics with an extension (voice register dn). |
| Step 8 | dtmf-relay rtp-nte Example: Router(config-register-pool)# dtmf-relay rtp-nte | (Optional) Specifies the method for relaying dual tone
                                             				multifrequency (DTMF) tones between two devices as per RFC2833. This configuration is required only to perform assign or unassign
                                             				operation using Extension Assigner application. |
| Step 9 | codec g711ulaw Example: Router(config-register-pool)# codec g711ulaw | (Optional) Specifies the voice coder rate of speech for a dial
                                             				peer. This configuration is required only to perform assign or unassign
                                             				operation using Extension Assigner application. g711ulaw -Option
                                                				  that represents the correct voice decoder rate. g711ulaw is the only codec
                                                				  supported with Extension Assigner application. |
| Step 10 | end Example: Router(config-register-pool)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure
                                                				  terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | kron policy-list list-name Example: Router(config)# kron policy-list save-config | Specifies a
                                          			 name for a new or existing Command Scheduler policy list and enters kron-policy
                                          			 configuration mode. If the
                                                   					 value of the list-name argument is new, a new policy list structure is created. If the
                                                   					 value of the list-name argument exists, the existing policy list structure is accessed. No editor
                                                   					 function is available, and the policy list is run in the order in which it was
                                                   					 configured. Note You can also use the CLI command background save interval configured
                                                         				  under telephony-service to automatically save configurations on Unified CME.
                                                         				  This is as an alternative for the kron command. | Note | You can also use the CLI command background save interval configured
                                                         				  under telephony-service to automatically save configurations on Unified CME.
                                                         				  This is as an alternative for the kron command. |
| Note | You can also use the CLI command background save interval configured
                                                         				  under telephony-service to automatically save configurations on Unified CME.
                                                         				  This is as an alternative for the kron command. |
| Step 4 | cli write Example: Router(config-kron-policy)# cli write | Specifies the
                                             				fully-qualified EXEC command and associated syntax to be added as an entry in
                                             				the Command Scheduler policy list. |
| Step 5 | exit Example: Router(config-kron-policy)# exit | Returns to
                                             				global configuration mode. |
| Step 6 | kron
                                                				  occurrence occurrence-name [ user username ] [[ in numdays: ] numhours: ] nummin { oneshot \| recurring } Example: Router(config)# kron occurrence backup in 30 recurring | Specifies
                                             				schedule parameters for a Command Scheduler occurrence and enters
                                             				kron-occurrence configuration mode. We
                                                   					 recommend that you configure your router to save your configuration every 30
                                                   					 minutes. occurrence-name -Specifies the name of the
                                                   					 occurrence. Length of occurrence-name is from 1 to 31 characters. If the
                                                   					 occurrence-name is new, an occurrence structure is created. If the
                                                   					 occurrence-name is not new, the existing occurrence is edited. user -(Optional) Used to identify a particular
                                                   					 user. username -Name
                                                   					 of user. in -Identifies
                                                   					 that the occurrence is to run after a specified time interval. The timer starts
                                                   					 when the occurrence is configured. numdays :-
                                                   					 (Optional) Number of days. If used, add a colon after the number. numhours :-
                                                   					 (Optional) Number of hours. If used, add a colon after the number. nummin :-
                                                   					 (Optional) Number of minutes. oneshot -Identifies that the occurrence is to run
                                                   					 only one time. After the occurrence has run, the configuration is removed. recurring -Identifies that the occurrence is to run on a recurring
                                                   					 basis. |
| Step 7 | policy-list list-name Example: Router(config-kron-occurrence)# policy-list save-config | Specifies a
                                             				Command Scheduler policy list. |
| Step 8 | end Example: Router(config-kron-occurrence)# end | Returns to
                                             				privileged EXEC mode. |

| Note | You can also use the CLI command background save interval configured
                                                         				  under telephony-service to automatically save configurations on Unified CME.
                                                         				  This is as an alternative for the kron command. |
|---|---|

| Note | If there are
                                             			 HTTP connection issues between the primary router and the secondary backup
                                             			 router during automatic synchronization, the extension assigner synchronization
                                             			 changes are lost. |
|---|---|

| Restriction | Automatic
                                                   				  synchronization for new or replacement routers is not supported. Extension
                                                   				  assigner preconfiguration must be manually performed on the secondary backup
                                                   				  router. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service \| voice register
                                                				  global Example: Router(config)# telephony-service
Router(config)# voice register global | Enters
                                          			 telephony service configuration mode or voice register global mode. |
| Step 4 | xml user user-name password password
                                                				  privilege-level Example: Router(config-telephony)# xml user user23 password 3Rs92uzQ 15
Router(config-register-global)# xml user user23 password 3Rs92uzQ 15 | Defines an
                                             				authorized user. user-name —Username of the authorized user. password —Password to use for access. privilege-level —Level of access to Cisco IOS
                                                   					 commands to be granted to this user. Only the commands with the same or a lower
                                                   					 level can be executed via XML. Range is 0 to 15. |
| Step 5 | end Example: Router(config-telephony)# end
Router(config-register-global)# end | Returns to
                                             				privileged EXEC mode. |

| Note | Phone
                                                   				  configurations such as MAC address, pool-tag, and phone type are saved as part
                                                   				  of synchronization for Extension Assigner feature. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service \| voice register
                                                				  global Example: Router(config)# telephony-service
Router(config)# voice register global | Enters
                                          			 telephony service configuration mode or voice register global mode. |
| Step 4 | standby
                                                				  username username password password Example: Router(config-telephony)# standby username user23 password 3Rs92uzQ
Router(config-register-global)# standby username user23 password 3Rs92uzQ | Defines an
                                             				authorized user. Same
                                                   					 username and password that was previously defined for the XML interface on the
                                                   					 secondary backup router. |
| Step 5 | end Example: Router(config-telephony)# end
Router(config-register-global)# end | Returns to
                                             				privileged EXEC mode. |

| Step 1 | Get the
                                          			 information you need to use extension assigner from your system administrator.
                                          			 For a list of this information, see Provide
                                             				the Installation Technician with the Required Information . |
|---|---|
| Step 2 | Dial the
                                          			 appropriate extension number to access the extension assigner system. |
| Step 3 | Enter the password for the extension assigner and press # . |
| Step 4 | Enter the ID number that represents this phone’s extension and press # . |
| Step 5 | If the
                                          			 extension is not assigned to another phone, press 1 to
                                          			 confirm that you want to assign the extension to your phone, then hang up.
                                          			 After the phone resets, the assignment is complete. |
| Step 6 | If the
                                          			 extension is assigned to another phone that is idle: Press 2 to
                                                				  confirm that you want to unassign the extension from the other phone. Hang up. Repeat
                                                				  this procedure beginning at Step 2 . |
| Step 7 | If the
                                          			 extension is assigned to another phone that is in use, either: Return to Step 5 to enter another extension number. Perform the procedures in the Unassigning an Extension Number section and then repeat this procedure beginning at Step 2 . |

| Note | You can
                                             			 unassign the extension number of the phone that is used to dial in to the
                                             			 Extension Assigner or the extension number of another phone that has a
                                             			 provision-tag configured. |
|---|---|

| Step 1 | Get the
                                          			 information you need to use extension assigner from your system administrator.
                                          			 For a list of this information, see Provide
                                             				the Installation Technician with the Required Information . |
|---|---|
| Step 2 | Dial the
                                          			 appropriate extension number to access the extension assigner system. |
| Step 3 | Enter the
                                          			 password for the extension assigner and press # . |
| Step 4 | Enter the
                                          			 provision-tag of the phone that needs to be unassigned, and press # . |
| Step 5 | When you enter
                                          			 the provision-tag for the phone extension that needs to be unassigned, you are
                                          			 prompted to press 2 followed by # to
                                          			 confirm that you want to unassign the extension from the phone. |
| Step 6 | Hang up. |

| Note | You can reassign
                                             			 a number to a phone only if that number: Is not
                                                   				  assigned to another phone Is assigned
                                                   				  to another phone and that phone is idle Is assigned
                                                   				  to another phone and you first unassign the extension |
|---|---|

| Step 1 | Get the
                                          			 information you need to use extension assigner from your system administrator.
                                          			 For a list of this information, see Provide
                                             				the Installation Technician with the Required Information . |
|---|---|
| Step 2 | Dial the
                                          			 appropriate extension number to access the extension assigner system. |
| Step 3 | Enter the
                                          			 password for the extension assigner and press # . |
| Step 4 | Enter the ID
                                          			 number that represents this phone’s extension and press # . |
| Step 5 | If the
                                          			 extension is not assigned to another phone, press 1 to
                                          			 confirm that you want to assign the extension to your phone, then hang up.
                                          			 After the phone resets, the reassignment is complete. |
| Step 6 | If the
                                          			 extension is assigned to another phone that is idle: Press 2 to
                                                				  confirm that you want to unassign the extension from the other phone. Hang up. Perform the procedure in
                                                				  the Assign
                                                   					 New Extension Numbers section. |
| Step 7 | If the
                                          			 extension is assigned to another phone that is in use, either: Return to Step 5 to enter another extension number. Perform the procedures in
                                                				  the Unassign
                                                   					 an Extension Number section and the Assign
                                                   					 New Extension Numbers section. |

| Step 1 | Use the debug ephone
                                             				  extension-assigner command to display status messages produced by
                                       			 the extension assigner application. |
|---|---|
| Step 2 | Use the debug voip application
                                             				  script command to display status messages produced by the server
                                       			 as it runs the assigner application Tcl script. |
| Step 3 | Use the debug ephone
                                          				state command as described in the Cisco IOS Debug Command Reference. |

| Step 1 | Use the debug voice register events and debug voice register error commands to display status messages produced by the
                                       			 extension assigner application. |
|---|---|
| Step 2 | Use the debug voip application
                                             				  script command to display status messages produced by the server
                                       			 as it runs the assigner application Tcl script. |
| Step 3 | Use the debug ccsip messages and debug ccsip error commands to display status messages for
                                       			 unregistration of phones. |

| Feature Name | Cisco
                                          				  Unfiied CME Version | Feature
                                          				  Information |
|---|---|---|
| Extension
                                          				  Assigner for SIP Phones | 11.6 | Enables the
                                          				  installation technicians to assign extension numbers to SIP Phones configured
                                          				  on Cisco Unified CME. |
| Extension
                                          				  Assigner Synchronization | 4.2(1) | Enables the
                                          				  secondary backup router to automatically receive any changes made to ephone
                                          				  mac-addresess in the primary router. |
| Extension
                                          				  Assigner | 4.0(3) | Enables
                                          				  installation technicians to assign extension numbers to Cisco Unified CME SCCP
                                          				  phones without accessing the server. |