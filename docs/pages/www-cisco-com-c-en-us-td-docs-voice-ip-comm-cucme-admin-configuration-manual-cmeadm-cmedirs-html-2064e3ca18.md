---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmedirs-html-2064e3ca18
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmedirs.html
retrieved_at: 2026-08-21T07:23:10.345773+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Directory
	 Services

## Chapter: Directory
	 Services

# Directory
                     	 Services

## Information About Directory Services

### Local
                           	 Directory

Cisco Unified CME
                              		automatically creates a local phone directory containing the telephone numbers
                              		that are assigned in the directory number configuration of the phone. You can
                              		make additional entries to the local directory in telephony services
                              		configuration mode. Additional entries can be nonlocal numbers such as
                              		telephone numbers on other Cisco Unified CME systems used by your company.

When a phone user
                              		selects the Directories > Local
                                    			 Directory menu, the phone displays a search page from
                              		Unified CME. After a user enters the search information, the phone sends the
                              		information to Cisco Unified CME, which searches for the requested number or
                              		name pattern in the directory number configuration and sends the response back
                              		to the phone, which displays the matched results. The phone can display up to
                              		32 directory entries. If a search results in more than 32 entries, the phone
                              		displays an error message and the user must refine the search criteria to
                              		narrow the results.

The order of the
                              		names in the directory entries is first-name-first or last-name-first.
                              		Character strings for directory names can contain a spaces and a comma (,) and
                              		cannot contain an ampersand (&).

The local directory
                              		that is displayed on an IP phone is an XML page that is accessed through HTTP
                              		without password protection. The directory HTTP service can be disabled to
                              		suppress the availability of the local directory.

For configuration
                              		information, see Configure Local Directory Service .

From CME 12.0
                              		onwards, an optional username and password can be configured for authenticating
                              		the local directory services.

For more information
                              		on the CLI command service local-directory authenticate username password , see Cisco Unified Communications
                                 		  Manager Express Command Reference .

### External Directory

Cisco Unified IP Phones can support URLs in association with the four
                              		programmable feature buttons on IP phones, including the Directories button.
                              		Operation of these services is determined by the Cisco Unified IP phone
                              		capabilities and the content of the referenced URL. Provisioning the directory
                              		URL to select an external directory resource disables the Cisco Unified CME
                              		local directory service.

### Called-Name
                           	 Display

When phone agents
                              		answer calls for different departments or people, it is often helpful for them
                              		to see a display of the name, rather than the number of the called party. The
                              		Dialed Number Identification Service (or Called-Name Display) feature supports
                              		the display of the name associated with a called number for incoming calls to
                              		IP phones configured on a Unified CME. The display name is obtained from the
                              		list of Unified CME directory names using directory lookup.

You need to
                              		configure the CLI command service dnis
                                    			 dir-lookup under telephony-service configuration mode to use this
                              		directory lookup service. For more information on the CLI command service dnis
                                    			 dir-lookup , see Cisco Unified Communications
                                 		  Manager Express Command Reference Guide .

If the display name
                              		for a called number is not available in Unified CME directory names, the
                              		display name can be added using the CLI command directory
                                    			 entry . For more information on the CLI command directory
                                    			 entry , see Cisco Unified Communications
                                 		  Manager Express Command Reference Guide .

When a phone
                                          		  receives two simultaneous calls, there is a slight time difference between the
                                          		  calls being acknowledged by the phone. Called-name Display is only for the
                                          		  first call acknowledged by the phone. Even when the first call is disconnected
                                          		  and the second call is in ringing state, Called-name Display feature does not
                                          		  work for the second call.

For an example of
                              		Called-Name Display , see Example for Called-Name Display for Voice Hunt Group

The called-name
                              		display feature for ephone-dns can display either of the following types of
                              		name:

Name for a
                                    			 directory number in a local directory

Name associated
                                    			 with an overlay directory number. Calls to the first directory number in a set
                                    			 of overlay numbers will display a caller ID. Calls to the remaining directory
                                    			 numbers in the overlay set will display the name associated with the directory
                                    			 number.

This is an example
                              		of Called-Name Display for ephone-dns. If order-entry agents are servicing
                              		three catalogs with individual 800 numbers configured in one overlay ephone-dn
                              		set, they need to know which catalog is being called to give the correct
                              		greeting, such as “Thank you for calling catalog N . May I take
                              		your order?”

From Unified CME
                              		Release 12.0 onwards, the Dialed Number Identification Service feature is
                              		supported for phones configured under voice hunt group on on Cisco 4000 Series
                              		Integrated Services Routers. The Dialed Number Identification Service is
                              		supported on Peer, Sequential, Parallel, and Longest-Idle voice hunt groups.
                              		Support is introduced for SIP Phones on Cisco IP Phones 7800 and 8800 Series as
                              		part of the Unified CME 12.0 Release. For information on configuring
                              		Called-Name Display feature, see Called-Name Display .

### Directory Search

Cisco Unified CME 4.3 increases the number of entries supported in a
                              		search results list from 32 to up to 240 when using the directory search
                              		feature. For example, if a user enters smith as the last name, all 240 matches are
                              		displayed on eight different pages, with 30 entries per page. If multiple pages
                              		are required, the phone displays two new softkeys, “Next” and “Prev” that the
                              		phone user can press to move back and forth between the previous and next
                              		pages. Text such as “Page 2 of 3" displays to indicate the current and total
                              		pages on the search results.

## Configure Directory Services

### Configure Local
                           	 Directory Service

To define the
                                 		  format for local directory names or block the local directory display on all
                                 		  phones, perform the following steps.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- directory { first-name-first | last-name-first }

- no service local-directory

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

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 4

directory { first-name-first | last-name-first }

#### Example:

```
Router(config-telephony)# directory last-name-first
```

Defines the
                                             				format for entries in the local directory.

Default is first-name-first .

Step 5

no service local-directory

#### Example:

```
Router(config-telephony)# no service local-directory
```

Disables local
                                             				directory service on IP phones.

Step 6

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

### Define a Name for
                           	 a Directory Number on SCCP Phone

To define a name
                                 		  to be used for caller-ID displays and as a local directory entry, perform the
                                 		  following steps.

Restriction

The name to
                                                   				  be associated with a directory number cannot contain special characters, such
                                                   				  as an ampersand (&). The only special characters allowed in the name are
                                                   				  the comma (,) and the percent sign (%).

#### Before you begin

Cisco CME 3.0
                                       				or a later version.

Directory
                                       				number for which you are defining a directory entry must already have a number
                                       				assigned by using the number (ephone-
                                             					 dn) command. For configuration information, see Create Directory Numbers for SCCP Phones .

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag

- name name

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
Router(config)# ephone-dn 55
```

Enters
                                             				ephone-dn configuration mode.

Step 4

name name

#### Example:

```
Router(config-ephone-dn)# name Smith, John
```

or

```
Router(config-ephone-dn)# name Shipping and Handling
```

Associates a
                                             				name with this directory number.

Must
                                                   					 follow the name order that is specified with the directory command:
                                                   					 first-name-first or last-name-first.

name —Alphanumeric string to be
                                                   					 displayed.

You must separate the two parts, first last or last first,
                                                         						  of the name string with a space.

The second part of the name string can contain spaces,
                                                         						  such as "and Shipping". The first part of the name string cannot contain
                                                         						  spaces.

You can include a comma (,) in the name string for display purposes,
                                                         						  for example, when you use the last-name-first pattern (last, first).

Step 5

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

### Add an Entry to a
                           	 Local Directory on SCCP Phone

To add an entry to
                                 		  the local directory, perform the following steps.

Restriction

If the
                                                   				  directory entry being configured is to be used for called-name display, the
                                                   				  number being configured must contain at least one wildcard character.

Entry for
                                                   				  local directory cannot include opening or closing quotation marks (‘, ‘, “, or
                                                   				  ”).

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- directory entry { directory-tag number name name | clear }

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

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 4

directory entry { directory-tag number name name | clear }

#### Example:

```
Router(config-telephony)# directory entry 1 5550111 name Sales
```

Creates a
                                             				telephone directory entry that is displayed on an IP phone. Entries appear in
                                             				the order in which they are entered.

directory-tag—Unique sequence number that identifies this
                                                   					 directory entry during all configuration tasks. Range is 1 to 250.

If this
                                                   					 name is to be used for called-name display, the number associated with the names must contain at least one wildcard character.

name —1 to 24 alphanumeric characters, including
                                                   					 spaces. Name cannot include opening or closing quotation marks ( , , , or ).

Step 5

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

### Configure External
                           	 Directory Service on SCCP Phone

To enable an
                                 		  external directory resource on supported Cisco Unified IP phones and disable
                                 		  local directory services on those same phones, perform the following steps.

Restriction

Provisioning
                                                   				  of the directory URL to select an external directory resource disables the
                                                   				  Cisco Unified CME local directory service.

Configuring
                                                   				  external directory service only works with non-Java based phones. Any Java
                                                   				  based phone will display duplicate directories for the following:

Missed

Received

Placed

#### Before you begin

To use a Cisco
                                 		  Unified Communications Manager directory as an external directory source for
                                 		  Cisco Unified CME phones, the Cisco Unified Communications Manager must be made
                                 		  aware of the phones. You must list the MAC addresses of the Cisco Unified CME
                                 		  phones in the Cisco Unified Communications Manager and reset the phones from
                                 		  the Cisco Unified Communications Manager. It is not necessary for you to assign
                                 		  ephone-dns to the phones or for the phones to register with Cisco Unified
                                 		  Communications Manager.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- url directories url

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

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 4

url directories url

#### Example:

```
Router(config-telephony)# url directories http://10.0.0.11/localdirectory
```

Associates a
                                             				URL with the programmable Directories feature button on supported Cisco Unified
                                             				IP phones in Cisco Unified CME.

Provisioning the directories URL to select an external directory
                                                   					 resource disables the Cisco Unified CME local directory service.

Operation
                                                   					 of these services is determined by the Cisco Unified IP phone capabilities and
                                                   					 the content of the specified URL.

Step 5

end

#### Example:

```
Router(config-telephony)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

### Called-Name
                           	 Display

To enable
                                 		  called-name display, perform the following steps.

Restriction

The service dnis
                                                         						overlay command can only be used to configure overlaid
                                                   				  ephone-dns.

#### Before you begin

For directory
                                       				numbers other than overlaid directory numbers—To display a name in the
                                       				called-name display, the name to be displayed must be defined in the local
                                       				directory. See Add an Entry to a Local Directory on SCCP Phone .

For overlaid
                                       				directory numbers—To display a name in the called-name display for a directory
                                       				number that is in a set of overlaid directory numbers, the name to be displayed
                                       				must be defined. See Define a Name for a Directory Number on SCCP Phone .

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- service dnis dir-lookup

- service dnis overlay

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

telephony-service

#### Example:

```
Router(config)#
```

Enters
                                             				telephony-service configuration mode.

Step 4

service dnis dir-lookup

#### Example:

```
Router(config-telephony)# service dnis dir-lookup
```

Specifies that
                                             				incoming calls to a called number should display the name that was defined for
                                             				this directory number with the directory
                                                   					 entry command.

If the service dnis dir-lookup and service dnis
                                                         						  overlay commands are both used in one configuration, the service dnis
                                                         						  dir-lookup command takes precedence.

Step 5

service dnis overlay

#### Example:

```
Router(config-telephony)# service dnis overlay
```

(For overlaid
                                             				directory numbers only.) Specifies that incoming calls to a called number
                                             				should display the name that was defined for this directory number with the name command.

If the service dnis dir-lookup and service dnis
                                                               						overlay commands are both used in one configuration, the service dnis
                                                               						dir-lookup command takes precedence.

Step 6

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

### Verify Called-Name Display

Step 1

Use the show running-config command to verify your
                                          			 configuration. Called-name display is shown in the telephony-service part of
                                          			 the output.

#### Example:

```
Router# show running-config telephony-service
 service dnis overlay
```

Step 2

Use the show telephony-service directory-entry command to display current directory entries.

#### Example:

```
Router# show telephony-service directory-entry directory entry 1 5550341 name doctor1
 directory entry 2 5550772 name doctor1
 directory entry 3 5550263 name doctor3
```

Step 3

Use the show telephony-service ephone-dn command to
                                          			 verify that you have used at least one wildcard (period or .) in the ephone-dn
                                          			 primary or secondary number or to verify that you have entered a name for the
                                          			 number.

#### Example:

```
Router# show telephony-service ephone-dn ephone-dn 2
 number 5002 secondary 200.
 name catalogN
 huntstop
 call-forward noan 5001 timeout 8
```

Step 4

Use the show ephone overlay command to verify the
                                          			 contents of overlaid ephone-dn sets.

#### Example:

```
Router# show ephone overlay ephone-1 Mac:0007.0EA6.353A TCP socket:[1] activeLine:0 REGISTERED
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
 
IP:10.2.225.205 52486 Telecaster 7960  keepalive 2771 max_line 6
button 1: dn 11 number 60011 CH1 IDLE      overlay 
button 2: dn 17 number 60017 CH1 IDLE      overlay 
button 3: dn 24 number 60024 CH1 IDLE      overlay 
button 4: dn 30 number 60030 CH1 IDLE      overlay 
button 5: dn 36 number 60036 CH1 IDLE      CH2 IDLE      overlay 
button 6: dn 39 number 60039 CH1 IDLE      CH2 IDLE      overlay 
overlay 1: 11(60011) 12(60012) 13(60013) 14(60014) 15(60015) 16(60016) 
overlay 2: 17(60017) 18(60018) 19(60019) 20(60020) 21(60021) 22(60022) 
overlay 3: 23(60023) 24(60024) 25(60025) 26(60026) 27(60027) 28(60028) 
overlay 4: 29(60029) 30(60030) 31(60031) 32(60032) 33(60033) 34(60034) 
overlay 5: 35(60035) 36(60036) 37(60037) 
overlay 6: 38(60038) 39(60039) 40(60040
```

### Define a Name for
                           	 a Directory Number on SIP Phone

To define name for
                                 		  a directory number on a SIP phone, perform the following steps.

#### Before you begin

Cisco CME 3.4
                                       				or a later version.

Directory
                                       				number for which you are defining a name must already have a number assigned by
                                       				using the number (voice register
                                             					 dn) command. For configuration information, see Create Directory Numbers for SIP Phones .

### SUMMARY STEPS

- enable

- configure terminal

- voice register dn dn-tag

- name name

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

voice register dn dn-tag

#### Example:

```
Router(config-register-global)# voice register dn 17
```

Enters voice
                                             				register dn configuration mode to define a directory number for a SIP phone,
                                             				intercom line, voice port, or a message-waiting indicator (MWI).

Step 4

name name

#### Example:

```
Router(config-register-dn)# name Smith, John
```

or

```
Router(config-register-dn)# name John Smith
```

Associates a
                                             				name with a directory number in Cisco Unified CME and provides caller ID for
                                             				calls originating from a SIP phone.

Name must
                                                   					 follow the order specified by using the directory
                                                         						  (telephony-service) command.

Step 5

end

#### Example:

```
Router(config-register-dn)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

### Configure External
                           	 Directory Service on SIP Service

To enable an
                                 		  external directory resource on supported Cisco Unified IP phones and disable
                                 		  local directory services on those same phones, perform the following steps.

Restriction

Provisioning
                                                   				  of the directory URL to select an external directory resource disables the
                                                   				  Cisco Unified CME local directory service.

Supported
                                                   				  only on Cisco Unified IP Phone 7960s and 7960Gs and Cisco Unified IP Phone
                                                   				  7940s and 7940Gs.

#### Before you begin

Cisco CME 3.4 or a
                                 		  later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- url directory url

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
                                             				phones in Cisco Unified CME.

Step 4

url directory url

#### Example:

```
Router(config-register-global)# url directory http://10.0.0.11/localdirectory
```

Associates a
                                             				URL with the programmable Directories feature button on supported Cisco Unified
                                             				IP phones in Cisco Unified CME.

Provisioning the directory URL to select an external directory
                                                   					 resource disables the Cisco Unified CME local directory service.

Operation
                                                   					 of these services is determined by the Cisco Unified IP phone capabilities and
                                                   					 the content of the specified URL.

Step 5

end

#### Example:

```
Router(config-register-global)# end
```

Exits to
                                             				privileged EXEC mode.

### Verify Directory Services

To verify the configuration for local directory services, perform the
                                 		  following steps.

Step 1

show running-config

This command displays the running configuration. Directory
                                             				configuration commands are listed in the telephony-service portion of the
                                             				output.

#### Example:

```
Router# show running-config .
.
.
timeout busy 10
timeout ringing 100
caller-id name-only: enable
system message XYZ Company
web admin system name admin1 password admin1
web admin customer name Customer 
edit DN through Web:  enabled.
edit TIME through web:  enabled.
Log (table parameters):
     max-size: 150
     retain-timer: 15
create cnf-files version-stamp Jan 01 2002 00:00:00
transfer-system full-consult 
multicast moh 239.12.20.123 port 2000
fxo hook-flash
local directory service: enabled.
```

Step 2

show telephony-service

This command displays only the telephony-service configuration
                                             				information.

Step 3

Use the show telephony-service directory-entry command to display the entries made using the directory entry command.

## Configuration Examples for Directory Services

### Example for Configuring Local Directory

The following example defines the naming order for the local directory
                                 		  on IP phones served by the Cisco Unified CME router:

```
telephony-service
directory last-name-first
```

The following example creates a directory of three telephone listings:

```
telephony-service
directory entry 1 14045550111 name Sales
directory entry 2 13125550122 name Marketing
directory entry 3 12135550144 name Support Center
```

The following example disables the local directory on IP phones served
                                 		  by the Cisco Unified CME router:

```
telephony-service
no service local-directory
```

### Example for
                           	 Configuring Called-Name Display

This section
                              		contains the following examples:

#### Example for
                              	 Called-Name Display for Voice Hunt Group

The following is an example of a voice hunt group configuration,
                                    		  where the CLI command service dnis dir-lookup allows the directory
                                    		  entry names to be displayed on the IP phones when a call is placed to a number
                                    		  declared using the CLI command directory entry . In this example, the pilot
                                    		  umber is configured as 11… This means that the user can dial the numbers 1100
                                    		  to 1199. When the user dials 1111, the directory name dept1 is displayed for
                                    		  the directory numbers 2001, 2002, and 2003. If user dials 1155, then the
                                    		  directory name dept2 is displayed and if user dials 5500, then the directory
                                    		  name dept3 is displayed for the directory numbers 2001, 2002, and 2003.

```
telephony-service 
 service dnis dir-lookup
 directory entry 1 1111 name dept1
 directory entry 2 1155 name dept2
 directory entry 3 5500 name dept3

voice hunt-group 1 sequential
pilot 11.. 
list 2001, 2002, 2003
final 8888
timeout 10
```

#### Example for
                              	 Configuring First Ephone-dn in the Overlay Set

The following
                                    		  example shows a configuration for three phones that use the same set of
                                    		  overlaid ephone-dns for each phone’s button 1.

```
telephony-service
 service dnis overlay

ephone-dn 1
 number 18005550100

ephone-dn 2
 name department1
 number 18005550101

ephone-dn 3
 name department2
 number 18005550102

ephone 1
 button 1o1,2,3

ephone 2
 button 1o1,2,3

ephone 3
 button 1o1,2,3
```

The default
                                    		  display for all three phones is the number of the first ephone-dn listed in the
                                    		  overlay set (18005550100). A call is made to the first ephone-dn (18005550100),
                                    		  and the caller ID (for example, 4085550123) is displayed on all three phones.
                                    		  The user for phone 1 answers the call. The caller ID (4085550123) remains
                                    		  displayed on phone 1, and the displays on phone 2 and phone 3 return to the
                                    		  default display (18005550100). A call to the next ephone-dn is made. The
                                    		  default display on phone 2 and phone 3 is replaced with the called ephone-dn’s
                                    		  name (18005550101).

#### Example for
                              	 Configuring Directory Name for an Overlaid Ephone-dn Set

The following is
                                    		  an example of a configuration of overlaid ephone-dns that uses wildcards in the
                                    		  secondary numbers for the ephone-dns. The wildcards allow you to control the
                                    		  display according to the number that was dialed. The example is for a medical
                                    		  answering service with three IP phones that accept calls for nine doctors on
                                    		  one button. When a call to 5550001 rings on button 1 on ephone 1 through ephone
                                    		  3, “doctor1” is displayed on all three ephones.

```
telephony-service
 service dnis dir-lookup

 directory entry 1 5550001 name doctor1
 directory entry 2 5550002 name doctor2 directory entry 3 5550003 name doctor3 directory entry 4 5550010 name doctor4
 directory entry 5 5550011 name doctor5
 directory entry 6 5550012 name doctor6

 directory entry 7 5550020 name doctor7
 directory entry 8 5550021 name doctor8
 directory entry 9 5550022 name doctor9

ephone-dn 1
 number 5500 secondary 555000.

ephone-dn 2
 number 5501 secondary 555001.

ephone-dn 3
 number 5502 secondary 555002.

ephone 1
 button 1o1,2,3
 mac-address 1111.1111.1111

ephone 2
 button 1o1,2,3
 mac-address 2222.2222.2222

ephone 3
 button 1o1,2,3
 mac-address 3333.3333.3333
```

For more
                                    		  information about making directory entries, see Local Directory . For more information about overlaid ephone-dns, see Call Coverage Features .

#### Example for
                              	 Configuring Directory Name for a Hunt Group with Overlaid Ephone-dns

The following
                                    		  example shows a hunt-group configuration for a medical answering service with
                                    		  two phones and four doctors. Each phone has two buttons, and each button is
                                    		  assigned two doctors’ numbers. When a patient calls 5550341, Cisco Unified CME
                                    		  matches the hunt-group pilot secondary number (555....), rings button 1 on one
                                    		  of the two phones, and displays “doctor1.”

```
telephony-service
 service dnis dir-lookup
 max-redirect 20
 directory entry 1 5550341 name doctor1
 directory entry 2 5550772 name doctor1
 directory entry 3 5550263 name doctor3
 directory entry 4 5550150 name doctor4

ephone-dn 1
 number 1001

ephone-dn 2
 number 1002

ephone-dn 3
 number 1003

ephone-dn 4
 number 104

ephone 1
 button 1o1,2
 button 2o3,4
 mac-address 1111.1111.1111

ephone 2
 button 1o1,2
 button 2o3,4
 mac-address 2222.2222.2222

ephone-hunt 1 peer
 pilot 5100 secondary 555....
 list 1001, 1002, 1003, 1004
 final number 5556000
 hops 5
 preference 1
 timeout 20
 no-reg
```

For more
                                    		  information about hunt-group behavior, see Call Coverage Features .
                                    		  Note that wildcards are used only in secondary numbers and cannot be used with
                                    		  primary numbers. For more information about making directory entries, see Call Coverage Features .
                                    		  For more information about overlaid ephone-dns, see Call Coverage Features .

#### Example for
                              	 Configuring Directory Name for Non-Overlaid Ephone-dns

The following is a
                                    		  configuration for three IP phones, each with two buttons. Button 1 receives
                                    		  calls from doctor1, doctor2, and doctor3, and button 2 receives calls from
                                    		  doctor4, doctor5, and doctor6.

```
telephony-service
 service dnis dir-lookup
 directory entry 1 5550001 name doctor1
 directory entry 2 5550002 name doctor2
 directory entry 3 5550003 name doctor3
 directory entry 4 5550010 name doctor4
 directory entry 5 5550011 name doctor5 directory entry 6 5550012 name doctor6

ephone-dn 1
 number 1001 secondary 555000.

ephone-dn 2
 number 1002 secondary 555001.

ephone 1
 button 1:1
 button 2:2
 mac-address 1111.1111.1111

ephone 2
 button 1:1
 button 2:2
 mac-address 2222.2222.2222

ephone 3
 button 1:1
 button 2:2
 mac-address 3333.3333.3333
```

For more
                                    		  information about making directory entries, see Local Directory .

#### Example for
                              	 Configuring Ephone-dn Name for Overlaid Ephone-dns

The following
                                    		  example shows three phones that have button 1 assigned to pick up three 800
                                    		  numbers for three different catalogs.

The default
                                    		  display for all four phones is the number of the first ephone-dn listed in the
                                    		  overlay set (18005550000). A call is made to the first ephone-dn (18005550000),
                                    		  and the caller ID (for example, 4085550123) is displayed on all phones. The
                                    		  user for phone 1 answers the call. The caller ID (4085550123) remains displayed
                                    		  on phone 1, and the displays on phone 2 and phone 3 return to the default
                                    		  display (18005550000). A call to the second ephone-dn (18005550001) is made.
                                    		  The default display on phone 2 and phone 3 is replaced with the called
                                    		  ephone-dn's name (catalog1) and number (18005550001).

```
telephony-service
 service dnis overlay

ephone-dn 1
 number 18005550000

ephone-dn 2
 name catalog1
 number 18005550001

ephone-dn 3
 name catalog2
 number 18005550002

ephone-dn 4
 name catalog3
 number 18005550003

ephone 1
 button 1o1,2,3,4

ephone 2
 button 1o1,2,3,4

ephone 3
 button 1o1,2,3,4
```

For more
                                    		  information about overlaid ephone-dns, see Call Coverage Features .

## Feature
                        	 Information for Directory Services

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature
                                             					 Name

Unified CME Version

Feature
                                             					 Information

Service
                                             					 Local Directory

12.0

The CLI
                                             					 command for accessing local directory service was enhanced to configure
                                             					 username and password, as service local-directory authenticate username password .

Directory
                                             					 Search

7.0/4.3

Number of
                                             					 entries supported in a search results list was increased from 32 to 240 when
                                             					 using directory search.

Called-Name Display

12.0

Support for Called-Name Display on phones configured under
                                             					 voice hunt group.

3.2

Called-Name Display was introduced.

Local
                                             					 Directory Service External Directory Service

4.0(2)

Added
                                             					 support for transferring a call directly to a selected number listed in the
                                             					 directory. If directory transfer is not supported, the user must press Transfer
                                             					 and then use the keypad to manually enter the number of the monitored line to
                                             					 transfer the incoming call.

3.4

Added
                                             					 support of directory services for SIP phones directly connected in
                                             					 Cisco Unified CME.

3.0

The
                                             					 ability to add local directory entries in addition to those that are
                                             					 automatically added from phone configurations was introduced. Authentication
                                             					 for local directory display was introduced.

2.1

The
                                             					 ability to block the display of the local directory on phones was introduced.

2.0

The
                                             					 specification of name format in the local directory was introduced.

| Note | When a phone
                                          		  receives two simultaneous calls, there is a slight time difference between the
                                          		  calls being acknowledged by the phone. Called-name Display is only for the
                                          		  first call acknowledged by the phone. Even when the first call is disconnected
                                          		  and the second call is in ringing state, Called-name Display feature does not
                                          		  work for the second call. |
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
| Step 4 | directory { first-name-first \| last-name-first } Example: Router(config-telephony)# directory last-name-first | Defines the
                                             				format for entries in the local directory. Default is first-name-first . |
| Step 5 | no service local-directory Example: Router(config-telephony)# no service local-directory | Disables local
                                             				directory service on IP phones. |
| Step 6 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

| Restriction | The name to
                                                   				  be associated with a directory number cannot contain special characters, such
                                                   				  as an ampersand (&). The only special characters allowed in the name are
                                                   				  the comma (,) and the percent sign (%). |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn dn-tag Example: Router(config)# ephone-dn 55 | Enters
                                             				ephone-dn configuration mode. |
| Step 4 | name name Example: Router(config-ephone-dn)# name Smith, John or Router(config-ephone-dn)# name Shipping and Handling | Associates a
                                             				name with this directory number. Must
                                                   					 follow the name order that is specified with the directory command:
                                                   					 first-name-first or last-name-first. name —Alphanumeric string to be
                                                   					 displayed. You must separate the two parts, first last or last first,
                                                         						  of the name string with a space. The second part of the name string can contain spaces,
                                                         						  such as "and Shipping". The first part of the name string cannot contain
                                                         						  spaces. You can include a comma (,) in the name string for display purposes,
                                                         						  for example, when you use the last-name-first pattern (last, first). |
| Step 5 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

| Restriction | If the
                                                   				  directory entry being configured is to be used for called-name display, the
                                                   				  number being configured must contain at least one wildcard character. Entry for
                                                   				  local directory cannot include opening or closing quotation marks (‘, ‘, “, or
                                                   				  ”). |
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
| Step 4 | directory entry { directory-tag number name name \| clear } Example: Router(config-telephony)# directory entry 1 5550111 name Sales | Creates a
                                             				telephone directory entry that is displayed on an IP phone. Entries appear in
                                             				the order in which they are entered. directory-tag—Unique sequence number that identifies this
                                                   					 directory entry during all configuration tasks. Range is 1 to 250. If this
                                                   					 name is to be used for called-name display, the number associated with the names must contain at least one wildcard character. name —1 to 24 alphanumeric characters, including
                                                   					 spaces. Name cannot include opening or closing quotation marks ( , , , or ). |
| Step 5 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

| Restriction | Provisioning
                                                   				  of the directory URL to select an external directory resource disables the
                                                   				  Cisco Unified CME local directory service. Configuring
                                                   				  external directory service only works with non-Java based phones. Any Java
                                                   				  based phone will display duplicate directories for the following: Missed Received Placed |
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
| Step 4 | url directories url Example: Router(config-telephony)# url directories http://10.0.0.11/localdirectory | Associates a
                                             				URL with the programmable Directories feature button on supported Cisco Unified
                                             				IP phones in Cisco Unified CME. Provisioning the directories URL to select an external directory
                                                   					 resource disables the Cisco Unified CME local directory service. Operation
                                                   					 of these services is determined by the Cisco Unified IP phone capabilities and
                                                   					 the content of the specified URL. |
| Step 5 | end Example: Router(config-telephony)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

| Restriction | The service dnis
                                                         						overlay command can only be used to configure overlaid
                                                   				  ephone-dns. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# | Enters
                                             				telephony-service configuration mode. |
| Step 4 | service dnis dir-lookup Example: Router(config-telephony)# service dnis dir-lookup | Specifies that
                                             				incoming calls to a called number should display the name that was defined for
                                             				this directory number with the directory
                                                   					 entry command. If the service dnis dir-lookup and service dnis
                                                         						  overlay commands are both used in one configuration, the service dnis
                                                         						  dir-lookup command takes precedence. |
| Step 5 | service dnis overlay Example: Router(config-telephony)# service dnis overlay | (For overlaid
                                             				directory numbers only.) Specifies that incoming calls to a called number
                                             				should display the name that was defined for this directory number with the name command. Note If the service dnis dir-lookup and service dnis
                                                               						overlay commands are both used in one configuration, the service dnis
                                                               						dir-lookup command takes precedence. | Note | If the service dnis dir-lookup and service dnis
                                                               						overlay commands are both used in one configuration, the service dnis
                                                               						dir-lookup command takes precedence. |
| Note | If the service dnis dir-lookup and service dnis
                                                               						overlay commands are both used in one configuration, the service dnis
                                                               						dir-lookup command takes precedence. |
| Step 6 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

| Note | If the service dnis dir-lookup and service dnis
                                                               						overlay commands are both used in one configuration, the service dnis
                                                               						dir-lookup command takes precedence. |
|---|---|

| Step 1 | Use the show running-config command to verify your
                                          			 configuration. Called-name display is shown in the telephony-service part of
                                          			 the output. Example: Router# show running-config telephony-service
 service dnis overlay |
|---|---|
| Step 2 | Use the show telephony-service directory-entry command to display current directory entries. Example: Router# show telephony-service directory-entry directory entry 1 5550341 name doctor1
 directory entry 2 5550772 name doctor1
 directory entry 3 5550263 name doctor3 |
| Step 3 | Use the show telephony-service ephone-dn command to
                                          			 verify that you have used at least one wildcard (period or .) in the ephone-dn
                                          			 primary or secondary number or to verify that you have entered a name for the
                                          			 number. Example: Router# show telephony-service ephone-dn ephone-dn 2
 number 5002 secondary 200.
 name catalogN
 huntstop
 call-forward noan 5001 timeout 8 |
| Step 4 | Use the show ephone overlay command to verify the
                                          			 contents of overlaid ephone-dn sets. Example: Router# show ephone overlay ephone-1 Mac:0007.0EA6.353A TCP socket:[1] activeLine:0 REGISTERED
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
 
IP:10.2.225.205 52486 Telecaster 7960  keepalive 2771 max_line 6
button 1: dn 11 number 60011 CH1 IDLE      overlay 
button 2: dn 17 number 60017 CH1 IDLE      overlay 
button 3: dn 24 number 60024 CH1 IDLE      overlay 
button 4: dn 30 number 60030 CH1 IDLE      overlay 
button 5: dn 36 number 60036 CH1 IDLE      CH2 IDLE      overlay 
button 6: dn 39 number 60039 CH1 IDLE      CH2 IDLE      overlay 
overlay 1: 11(60011) 12(60012) 13(60013) 14(60014) 15(60015) 16(60016) 
overlay 2: 17(60017) 18(60018) 19(60019) 20(60020) 21(60021) 22(60022) 
overlay 3: 23(60023) 24(60024) 25(60025) 26(60026) 27(60027) 28(60028) 
overlay 4: 29(60029) 30(60030) 31(60031) 32(60032) 33(60033) 34(60034) 
overlay 5: 35(60035) 36(60036) 37(60037) 
overlay 6: 38(60038) 39(60039) 40(60040 |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register dn dn-tag Example: Router(config-register-global)# voice register dn 17 | Enters voice
                                             				register dn configuration mode to define a directory number for a SIP phone,
                                             				intercom line, voice port, or a message-waiting indicator (MWI). |
| Step 4 | name name Example: Router(config-register-dn)# name Smith, John or Router(config-register-dn)# name John Smith | Associates a
                                             				name with a directory number in Cisco Unified CME and provides caller ID for
                                             				calls originating from a SIP phone. Name must
                                                   					 follow the order specified by using the directory
                                                         						  (telephony-service) command. |
| Step 5 | end Example: Router(config-register-dn)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

| Restriction | Provisioning
                                                   				  of the directory URL to select an external directory resource disables the
                                                   				  Cisco Unified CME local directory service. Supported
                                                   				  only on Cisco Unified IP Phone 7960s and 7960Gs and Cisco Unified IP Phone
                                                   				  7940s and 7940Gs. |
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
                                             				phones in Cisco Unified CME. |
| Step 4 | url directory url Example: Router(config-register-global)# url directory http://10.0.0.11/localdirectory | Associates a
                                             				URL with the programmable Directories feature button on supported Cisco Unified
                                             				IP phones in Cisco Unified CME. Provisioning the directory URL to select an external directory
                                                   					 resource disables the Cisco Unified CME local directory service. Operation
                                                   					 of these services is determined by the Cisco Unified IP phone capabilities and
                                                   					 the content of the specified URL. |
| Step 5 | end Example: Router(config-register-global)# end | Exits to
                                             				privileged EXEC mode. |

| Step 1 | show running-config This command displays the running configuration. Directory
                                             				configuration commands are listed in the telephony-service portion of the
                                             				output. Example: Router# show running-config .
.
.
timeout busy 10
timeout ringing 100
caller-id name-only: enable
system message XYZ Company
web admin system name admin1 password admin1
web admin customer name Customer 
edit DN through Web:  enabled.
edit TIME through web:  enabled.
Log (table parameters):
     max-size: 150
     retain-timer: 15
create cnf-files version-stamp Jan 01 2002 00:00:00
transfer-system full-consult 
multicast moh 239.12.20.123 port 2000
fxo hook-flash
local directory service: enabled. |
|---|---|
| Step 2 | show telephony-service This command displays only the telephony-service configuration
                                             				information. |
| Step 3 | Use the show telephony-service directory-entry command to display the entries made using the directory entry command. |

| Feature
                                             					 Name | Unified CME Version | Feature
                                             					 Information |
|---|---|---|
| Service
                                             					 Local Directory | 12.0 | The CLI
                                             					 command for accessing local directory service was enhanced to configure
                                             					 username and password, as service local-directory authenticate username password . |
| Directory
                                             					 Search | 7.0/4.3 | Number of
                                             					 entries supported in a search results list was increased from 32 to 240 when
                                             					 using directory search. |
| Called-Name Display | 12.0 | Support for Called-Name Display on phones configured under
                                             					 voice hunt group. |
| 3.2 | Called-Name Display was introduced. |
| Local
                                             					 Directory Service External Directory Service | 4.0(2) | Added
                                             					 support for transferring a call directly to a selected number listed in the
                                             					 directory. If directory transfer is not supported, the user must press Transfer
                                             					 and then use the keypad to manually enter the number of the monitored line to
                                             					 transfer the incoming call. |
| 3.4 | Added
                                             					 support of directory services for SIP phones directly connected in
                                             					 Cisco Unified CME. |
| 3.0 | The
                                             					 ability to add local directory entries in addition to those that are
                                             					 automatically added from phone configurations was introduced. Authentication
                                             					 for local directory display was introduced. |
| 2.1 | The
                                             					 ability to block the display of the local directory on phones was introduced. |
| 2.0 | The
                                             					 specification of name format in the local directory was introduced. |