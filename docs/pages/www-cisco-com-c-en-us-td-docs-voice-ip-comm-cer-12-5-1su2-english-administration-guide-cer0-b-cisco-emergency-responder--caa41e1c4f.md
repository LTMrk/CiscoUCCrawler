---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-12-5-1su2-english-administration-guide-cer0-b-cisco-emergency-responder--caa41e1c4f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/12_5_1su2/english/administration/guide/cer0_b_cisco-emergency-responder-administration-guide-1251SU2/cer0_b_cisco-emergency-responder-administration-guide-1251su3_chapter_011.html
retrieved_at: 2026-08-21T15:46:12.061920+00:00
---

Cisco Emergency Responder Administration Guide for Release 12.5(1)SU2

# Cisco Emergency Responder Administration Guide for Release 12.5(1)SU2

Updated: November 23, 2021

Chapter: Configure Cisco Unified Communications Manager

## Chapter: Configure Cisco Unified Communications Manager

# Configure Cisco Unified Communications Manager

## Configure Cisco
                        	 Unified Communications Manager Overview

This chapter
                           		describes procedures for configuring Cisco Unified Communications Manager
                           		(Unified CM) for Cisco Emergency Responder (Emergency Responder).

See the Release
                           		Notes for Unified CM versions that are compatible with Cisco Emergency
                           		Responder.

The procedures
                           		describe what you must configure in Unified CM so that Emergency Responder can
                           		work in your telephone network.

They also describe a
                           		sample Unified CM setup. The names that are chosen (for example, partition and
                           		calling search space names) are not required.

Sections with
                           		examples represent an example setup, with sample values included for reference
                           		only. Your particular configuration depends on the needs of your network and
                           		your naming strategy.

PhoneCSS -
                                    			 Includes the Phones partition.

E911CSS -
                                    			 Includes the E911 and Phones partitions.

The examples are
                           		based on a single Unified CM cluster. If you have more than one cluster, you
                           		must repeat the configuration in each cluster, except for the emergency
                           		location identification number (ELIN) translation patterns. The ELIN
                           		translation patterns are only defined in the Unified CM cluster to which the
                           		gateway sends incoming calls from the public safety answering point (PSAP).

## Set Up Phone Route
                        	 Plans

Before
                           		configuring Emergency Responder, you must ensure that the phones that might be
                           		used to make emergency calls (typically all phones) are added and registered
                           		with Unified CM. See the documentation and online help included with Unified CM
                           		if you need assistance.

The following
                           		sections provide an example setup for your network before adding Emergency
                           		Responder.

### Create Phone
                           	 Partition

If you have
                                 		  not already created a partition for the phones, do so now.

Step 1

Select Call Routing > Class of
                                                				  Control > Partition in Cisco Unified Communications Manager .

The Find and
                                             				List Partitions page appears.

Step 2

Click Add a New
                                             				Partition .

The Partition
                                             				Configuration page appears.

Step 3

Enter a
                                          			 descriptive name, such as Phones , in
                                          			 the Partition Name
                                             				and Description field. You can optionally include a description.

Step 4

Click Insert to
                                          			 add the new partition.

### Create Phone Calling
                           	 Search Space

If you do
                                 		  not already have a calling search space defined for the phones, follow this
                                 		  procedure to create one.

Step 1

Select Call Routing > Class of
                                                				  Control > Calling Search Space in Cisco Unified Communications Manager .

The Find and
                                             				List Calling Search Spaces page appears.

Step 2

Click Add a New
                                             				Calling Search Space .

The Calling
                                             				Search Space Configuration page appears.

Step 3

Enter a
                                          			 descriptive name, such as PhoneCSS, in the Calling Search
                                             				Space Name field.

Step 4

Select the Phones partition in the Available Partitions list box, and click the arrow buttons
                                          			 between the two list boxes to add it to the Selected Partitions list box.

Step 5

Click Insert to
                                          			 add the new calling search space.

### Assign Partition and Calling Search Space to Phones

You can use the Bulk Administration Tool to change the
                                 		  partition and calling search space on telephones in much less time than it
                                 		  takes to make the changes to each phone individually. This procedure describes
                                 		  the phone-by-phone procedure.

After you
                                 		  have created the Phones partition ( Create Phone Partition ) and PhonesCSS calling search space
                                 		  ( Create Phone Calling Search Space ), configure the phones to use them.

Step 1

Select Device >
                                             				Phone .

Unified CM
                                             				displays the Find and List Phones page.

Step 2

Select Device name is
                                             				not empty in the search fields and click Find .

Unified CM lists
                                             				all of the phones in the bottom frame.

Step 3

Click the phone
                                          			 with the configuration that you want to change.

Unified CM
                                             				displays the Phone Configuration page.

Step 4

Change the
                                          			 calling search space to PhoneCSS and
                                          			 click Update .

Step 5

Click the line
                                          			 number that you want to configure in the left-hand column.

Unified CM
                                             				displays the Directory Number Configuration page.

Step 6

Change the
                                          			 partition to Phones , and
                                          			 the calling search space to PhoneCSS .

Step 7

Click Insert to
                                          			 save your changes.

## Set Up Cisco Unified
                        	 Communications Manager for Emergency Responder

To handle
                           		emergency calls, you must configure the emergency call numbers (such as 911) so
                           		that Cisco Emergency Responder (Emergency Responder) intercepts them. Emergency
                           		Responder can then route the calls to the correct public safety answering point
                           		(PSAP) and transform the call as required to route the call and to enable the
                           		PSAP operator to call back the emergency caller if the initial call is
                           		disconnected.

The following
                           		topics describe how to define the Cisco Unified Communications Manager (Unified
                           		CM) elements required for Emergency Responder.

### Create Emergency
                           	 Responder Partition

You must
                                 		  create the Emergency Responder partition E911. This partition contains the
                                 		  numbers used by the PSAP to call into the network and to certain other CTI
                                 		  route points.

Step 1

Select Call Routing > Class of
                                                				  Control > Partition in Cisco Unified Communications Manager .

The Find and
                                             				List Partitions page appears.

Step 2

Click Add a New
                                             				Partition .

The Partition
                                             				Configuration page appears.

Step 3

Enter a
                                          			 descriptive name, such as E911 , in the Partition
                                             				Name field.

Step 4

Click Insert to
                                          			 add the new partition.

### Create Emergency
                           	 Responder Calling Search Space

To create
                                 		  the Emergency Responder calling search space, follow these steps:

Step 1

Select Call Routing > Class of
                                                				  Control > Calling Search Space in Cisco Unified Communications Manager . .

The Find and
                                             				List Calling Search Spaces page appears.

Step 2

Click Add a New
                                             				Calling Search Space .

The Calling
                                             				Search Space Configuration page appears.

Step 3

Enter a
                                          			 descriptive name, such as E911CSS, in the Calling Search
                                             				Space Name field.

Step 4

In the Available
                                          			 Partitions list box, select the E911 partition and then select the Phones partition in that order. Click the arrow buttons between the two
                                          			 list boxes to add them to the Selected Partitions list box. Arrange the
                                          			 partitions so that E911 is at the top of the list.

If you are using
                                             				any other partitions, add them to this list after the E911 partition.

You must list
                                                         				  the E911 partition before the Phones partition for the following reason: When
                                                         				  the user configures the translation pattern 911 or 9.911 (see Create Translation Patterns for 9.911 ),
                                                         				  the 911 Route Point is in the E911 partition; phones cannot look into the E911
                                                         				  Partition. The 911 Translation Pattern is in the phones partition and gets the
                                                         				  E911CSS. When the E911 partition is listed first, it matches the 911 Route
                                                         				  Point and the call goes to the Emergency Responder server as intended. If you
                                                         				  make the error of listing the Phones partition first, the Translation Pattern
                                                         				  keeps searching, resulting in a fast busy signal.

Step 5

Click Insert to
                                          			 add the new calling search space.

### Create Emergency
                           	 Call Route Points

You must
                                 		  configure CTI route points in Unified CM for these numbers:

If you use 9
                                                   				  as the access code, see Create Translation Patterns for 9.911 to configure Emergency Responder.

- The number that your
                                    			 standby Emergency Responder server should listen to, such as 912.

- The number that incoming
                                    			 calls from the public safety answering point (PSAP) use.

- Emergency Responder
                                    			 modifies these calls based on your ELIN configuration to route the call to the
                                    			 person who initiated the emergency call, if the PSAP gets disconnected and
                                    			 needs to call the calling party. See ELIN Numbers Emergency Calls and PSAP Callbacks for information about the rest of
                                    			 the ELIN configuration.

#### Before you begin

This
                                 		  procedure assumes you are using 911 as the main emergency call number. If a
                                 		  different number is used in your locale, substitute it for 911 and make similar
                                 		  substitutions for other numbers based on 911 such as 912. For example, if the
                                 		  emergency call number in your locale is 112, use 112, and perhaps 113, 114.

When you
                                 		  install Emergency Responder, you are required to enter the emergency call
                                 		  number. In this procedure, configure the same number you specify during
                                 		  installation.

CTI route points for the 911, 912, and 913 emergency numbers must be unique. You should not have more than one CTI route point
                                             addressed to the emergency numbers used earlier.

The
                                 		  following table describes the emergency call route points.

Route Point Setting

Route Points

Primary Number (911)

Backup Number (912)

ELIN (913)

Device Name

RP911

RP912

RPELIN913

Description

The emergency call number for the area. Emergency Responder
                                             					 handles all calls to this number.

Route point for the Emergency Responder standby server. If the
                                             					 primary server is unable to handle a call, the standby server receives the call
                                             					 through this route point.

The destination of all
                                             					 incoming calls from the PSAP. Emergency Responder transfers these calls to the
                                             					 emergency caller. The Route pattern is a prefix (913) plus a Fully Qualified
                                             					 Number.

Fully Qualified Number
                                             					 could be North American Numbering Plan or E.164 with Country Code. In case the
                                             					 ELIN is received as E.164 number with a leading plus sign ( +), use a
                                             					 Translation Pattern to remove the leading plus sign.

Directory Number

911

912

913XXXXXXXXXX

Partition

Phones

E911

E911

Calling Search Space

E911CSS

E911CSS

E911CSS

Forward Busy

Destination: 912

CSS: E911CSS

Destination:

- Route pattern for default
                                                						ERL.

or

- Onsite security
                                                						number.

CSS: E911CSS

Destination: Onsite security number.

CSS: E911CSS

Forward No Answer

Destination: 912

CSS: E911CSS

Destination:

- Route pattern for default
                                                						ERL.

or

- Onsite security
                                                						number.

CSS: E911CSS

Destination: Onsite security number.

CSS: E911CSS

Forward On Failure

Destination: 912

CSS: E911CSS

Destination:

- Route pattern for default
                                                						ERL.

or

- Onsite security
                                                						number.

CSS: E911CSS

Destination: Onsite security number.

CSS: E911CSS

Voice Mail
                                             					 Mask

Do not
                                             					 configure a Voice Mail Mask for this route point.

Do not
                                             					 configure a Voice Mail Mask for this route point.

Do not
                                             					 configure a Voice Mail Mask for this route point.

Configuring
                                                				call-forwarding numbers for the standby server ensures that calls are either
                                                				routed to the PSAP servicing the default ERL, or onsite security, if the
                                                				standby server cannot handle the call. If you do not install a standby server,
                                                				use these settings for the primary server. Configuring call-forwarding numbers
                                                				for the ELIN route point ensures that PSAP callbacks go to onsite security if
                                                				Emergency Responder cannot handle the call.

Step 1

In Unified CM,
                                          			 select Device >
                                             				CTI Route Point .

The Find and
                                             				List CTI Route Points page appears.

Step 2

Click Add a new CTI
                                             				Route Point .

The CTI Route
                                             				Point Configuration page appears.

Step 3

Fill in the
                                          			 CTI route point properties:

- Enter a unique name, such
                                             				as RP911 , in the Device
                                                				  Name field to identify this as the emergency call number. The Emergency
                                             				call route points table above shows suggested names, but you can use any name
                                             				you choose.

- Select the appropriate
                                             				device pool from the Device
                                                				  Pool menu.

- Select the calling search
                                             				space for the route point, as listed in the Emergency call route points table
                                             				above.

Step 4

Click Insert to
                                          			 add the new CTI route point.

Unified CM
                                             				adds the route point and asks if you want to configure line 1. Click OK to
                                             				configure line 1.

Unified CM
                                             				opens the Directory Number configuration page.

Step 5

Enter the
                                          			 configuration for the line you are creating using the information in the
                                          			 Emergency call route points table above.

Step 6

Click Insert .

Unified CM
                                             				adds the line to the device. Repeat this procedure until all devices described
                                             				in the Emergency call route points table above are configured.

For additional
                                             				assistance, see documentation and online help included with Unified CM.

### Create Required CTI
                           	 Ports

Emergency
                                 		  Responder uses CTI ports to call onsite alert (security) personnel when someone
                                 		  makes an emergency call. You should have enough CTI ports so that each person
                                 		  assigned to an ERL can receive a call. The number of ports that you configure
                                 		  is the number of simultaneous calls Emergency Responder can make to these
                                 		  personnel. It does not relate to the number of emergency calls Emergency
                                 		  Responder can handle or forward to the PSAP. There is no configurable
                                 		  limitation to the number of simultaneous emergency calls that Emergency
                                 		  Responder can handle.

#### Before you begin

Emergency
                                 		  Responder requires that the CTI port extension numbers be in succession, so you
                                 		  must find a block of unused extensions. For example, if you want to create four
                                 		  CTI ports starting at 3001, then 3001, 3002, 3003, and 3004 must all be
                                 		  available.

Step 1

Select Device >
                                             				Phone .

Cisco
                                                				  Unified Communications Manager opens the Find and List Phones page.

Step 2

Click Add a New
                                             				Phone .

Cisco
                                                				  Unified Communications Manager opens the Add a New Phone page.

Step 3

Select CTI Port for Phone Type and click Next .

Cisco
                                                				  Unified Communications Manager opens the Phone Configuration page.

Step 4

Configure the
                                          			 CTI Port, entering this information:

- Device Name - Enter
                                             				something meaningful to you, for example, CTI3001.

- Device Pool - Select an
                                             				appropriate device pool. This device pool must use the G.711 region.

- Calling Search Space -
                                             				Select PhoneCSS .

Step 5

Click Insert .

Cisco Unified Communications Manager creates the CTI
                                             				port and asks if you want to configure line 1. Click OK . Cisco
                                                				  Unified Communications Manager opens the Directory Number
                                             				Configuration page.

Step 6

Configure line 1
                                          			 for the CTI port, entering this information:

- Partition - Select Phones .

- Calling Search Space -
                                             				Select PhoneCSS .

Configure only
                                                         				  one line for each CTI port. Onsite security alert prompts may not get from one
                                                         				  or more of these lines when the online alert notification is initiated through
                                                         				  these ports.

Step 7

Click Insert .

Cisco Unified Communications Manager adds the line to
                                             				the device. Repeat the procedure to create each CTI route port that you
                                             				require.

All subsequent
                                                         				  CTI ports you create must be consecutive from the first CTI port DN.

CTI port DN in Cisco
                                                         				  Emergency Responder does not support E.164 dial pattern.

### Create a Cisco
                           	 Unified Communications Manager Group for Cisco Emergency Responder

A Cisco Unified
                                 		  Communications Manager (Unified CM) Group is a list of up to three Unified CMs
                                 		  that are assigned to a device pool to assist with call processing. The first
                                 		  Unified CM in the list acts as the primary Unified CM for the Group and the
                                 		  other members act as secondary and tertiary or backup Unified CMs. By creating
                                 		  a Unified CM Group, you can balance the call process load across multiple
                                 		  Unified CMs and ensure a level of redundancy for your network.

Because each device
                                 		  pool has one Unified CM Group assigned to it, a Unified CM Group improves your
                                 		  load distribution across a device pool. When a device registers, it attempts to
                                 		  connect to the primary Unified CM in the Unified CM Group. If the primary
                                 		  Unified CM is not available, the device tries to connect with the secondary
                                 		  Unified CM. If the secondary Unified CM is not available, the device tries to
                                 		  connect to the tertiary Unified CM.

You must create a
                                 		  Unified CM Group for Emergency Responder.

Step 1

Select System
                                             				> Unified CM Group .

The Find and
                                             				List Unified CM Groups page opens.

Step 2

Click Add
                                             				New .

The Unified CM
                                             				Group Configuration page opens.

Step 3

Enter the
                                          			 following information in the appropriate field:

Name – Enter a CM
                                                      					 Group name that is meaningful to you; for example, Cisco Emergency Responder CM
                                                      					 Group.

Auto-registration Cisco
                                                         						Unified Communications Manager Group - Do not check this box for
                                                      					 the Unified CM Group for Emergency Responder.

Cisco Unified Communications
                                                         						Managers – Add the primary and secondary CTI Manager for Emergency
                                                      					 Responder to the list of Selected Cisco Unified Communications Managers by
                                                      					 selecting each from the Available Cisco Unified Communications Managers and
                                                      					 clicking the Down Arrow .

Step 4

Click Save .

### Error and System
                           	 Messages

Unified CM generates
                                 		  several alarms to assist you in troubleshooting Emergency Responder problems.
                                 		  You should set up notification of Emergency Responder events so that an email
                                 		  notification alerts you to such important events.

The
                                 		  following table shows the relevant alarms.

Relevant Alarms

Alarm Level

Explanation

Recommended
                                             					 Action

CtiProviderOpened

Informational

Application opened the provider successfully.

This alarm
                                             					 is for informational purposes only; no action is required.

CtiProviderClosed

Informational

Application closed the provider.

Verify that
                                             					 Cisco Emergency Responder is up and running, verify network connectivity
                                             					 between application server and Unified CM, and verify the CPU utilization is in
                                             					 the safe range for the application server and Unified CM.

ApplicationConnectionDropped

Warning

TCP or TLS connection between CTIManager and Application is
                                             					 disconnected.

Verify that
                                             					 Cisco Emergency Responder is up and running, verify network connectivity
                                             					 between the application server and Unified CM, and verify the CPU utilization
                                             					 is in the safe range for the application server and Unified CM.

CtiIncompatibleProtocolVersion

Warning

The Cisco Emergency Responder version or its Unified Communications Manager
                                             					 setting is not compatible with this version of CTIManager.

Verify that
                                             					 the correct version of the Cisco Emergency Responder is being used and its
                                             					 Unified CM version setting is correct. See Change Cisco Unified Communications Manager Version to view and update the
                                             					 Unified CM version.

By default, only
                                 		  Error events are posted to the event log. You should modify the event level to
                                 		  post warnings and set up a customer alert if the Emergency Responder user
                                 		  closes its applications or ports.

To do this, navigate
                                 		  to the Serviceability Web Page by selecting Alarm
                                    			 >Configuration>Server>Service Group (CM Services)>Service (Cisco
                                    			 CTI Manager) . Change the Alarm Event Level to Error to have all of the last
                                 		  three alarms in the above table posted to SysLog.

These alarms are
                                 		  systemwide alarms and not specific to Emergency Responder. So any CTI
                                 		  application that triggers a warning message will post to the event log and not
                                 		  only Emergency Responder. You should set up notification of Unified CM events
                                 		  relevant to Emergency Responder so that if the provider goes out of service, an
                                 		  email or other notification event will alert you.

### ELIN Numbers
                           	 Emergency Calls and PSAP Callbacks

Emergency
                              		calls are routed based on the calling party number, not the called party
                              		number. If an emergency call is disconnected for some reason (for example, the
                              		caller hangs up), the PSAP needs to be able to call back the emergency caller
                              		using the calling party number. The PSAP might also want to call back to obtain
                              		updated information after ending an emergency call normally.

Emergency
                              		Responder converts a caller extension to an emergency location identification
                              		number (ELIN), and this number is used to route the call and to enable PSAP
                              		callbacks. Emergency Responder reuses the same set of numbers, and keeps track
                              		of the internal extension of the phone from which the call was made for up to
                              		three hours. When there is no active association of an ELIN to an internal
                              		phone extension, Emergency Responder routes calls to that ELIN to on-site
                              		security.

To set up
                              		the ELIN numbers, you must first obtain direct inward dial (DID) numbers from
                              		your service provider. Because you must pay for each number, you might want to
                              		limit the number of DIDs you obtain to two or three per ERL. The DIDs must be
                              		unique for each ERL.

Emergency
                              		Responder reuses the ELIN numbers assigned to an ERL if necessary. For example,
                              		if you configure two numbers for an ERL, and three emergency calls are made
                              		within a three-hour period, the first emergency caller's ELIN mapping is
                              		replaced by the third caller's extension. If the PSAP tries to call the first
                              		caller, the PSAP reaches the third caller. This information will help as you
                              		determine the number of DIDs you need for each ERL.

See ERL Creation for information about how to
                              		configure the ERLs with these numbers.

#### Create Route
                              	 Patterns for ERLs

Emergency
                                    		  Responder uses route patterns to route emergency calls to the local public
                                    		  safety answering point (PSAP). In the route pattern, you are associating a
                                    		  pattern with a gateway that connects to the PSAP. The gateway you choose
                                    		  depends on the emergency response location (ERL) to which you assign the route
                                    		  pattern.

You must
                                    		  create one route pattern for every ERL in your network. These are the direct
                                    		  inward dial (DID) numbers you obtain from your service provider for the purpose
                                    		  of allowing the PSAP to call into your network.

##### Before you begin

Each ERL
                                    		  requires unique route patterns for the ELINs. Work with the ERL administrator
                                    		  to get an idea of how many route patterns are needed, and the locale of the
                                    		  ERLs so that you can select an appropriate gateway. The ERL administrator must
                                    		  enter the route patterns you create into the ERL definition. See ERL Creation for information about ERLs.

Step 1

Select Call
                                                   				  Routing > Route/Hunt > Route
                                                   				  Pattern in Cisco Unified Communications Manager .

Unified CM opens
                                                				the Find and List Route Patterns page.

Step 2

Click Add a New Route
                                                				Pattern .

Unified CM opens
                                                				the Route Pattern Configuration page.

Step 3

Enter the
                                             			 information for the route pattern:

- Route Pattern - A pattern
                                                				that you can transform to the emergency call number, typically a number, a dot,
                                                				and the emergency call number. For example, 10.911, 11.911, and so forth. The
                                                				pattern can only contain numbers and dots.

- Partition - Select E911 .

- Numbering Plan - Select
                                                				the numbering plan for your area.

- Gateway/Route List -
                                                				Select the gateway to use for connecting to the local PSAP.

- Route Option - Select Route this
                                                   				  pattern .

- Use Calling Party's External
                                                   				  Phone Number Mask - Select this option.

- Discard Digits - Select PreDot if
                                                				you use the suggested pattern, such as 10.911. If using a different technique,
                                                				select the appropriate setting and enter a Called Party
                                                   				  Transform Mask if necessary (to dial the emergency number).

Step 4

Click Insert .

Unified CM saves
                                                				the route pattern. To add additional route patterns, return to Step 2 .

Tip

Consider
                                                            				  developing a detailed naming strategy for the route patterns because you might
                                                            				  end up with a large number of them. For example, you could use a pattern such
                                                            				  as xyzzaaab.911, where x is a Emergency Responder cluster identifier; y is a
                                                            				  Emergency Responder group identifier; zz is the PSAP identifier; aaa is the ERL
                                                            				  identifier; and b is the ELIN identifier (within the ERL).

#### Create Translation
                              	 Patterns for ELINs

Create
                                    		  translation patterns that cover the direct inward dial (DID) numbers you are
                                    		  using for ELIN numbers. The PSAP uses these ELINs to call into your network.
                                    		  Emergency Responder needs to intercept these calls so it can route the call to
                                    		  the correct emergency caller. The translation pattern is required so that a
                                    		  number prefixed to the ELIN becomes the route point you configured for PSAP
                                    		  callbacks, as explained in the Create Emergency Call Route Points .

##### Before you begin

Ensure
                                    		  that you have a list of all the DIDs you are using for ELINs.

Step 1

Select Call
                                                   				  Routing > Translation Pattern in Cisco Unified Communications Manager .

Unified CM opens
                                                				the Find and List Translation Patterns page.

Step 2

Click Add a New
                                                				Translation Pattern .

Unified CM opens
                                                				the Translation Pattern Configuration page.

Step 3

Create the
                                             			 translation pattern:

- Translation Pattern - The
                                                				DID you are using as an ELIN. If you can, use X variables to create a pattern
                                                				that covers more than one DID (for example, 5555551XXX). If you cannot create a
                                                				pattern, define translation patterns for each DID separately.

- Partition - Select E911 .

- Numbering Plan - Select
                                                				the numbering plan for your area.

- Calling Search Space -
                                                				Select E911CSS .

- Route Option - Select Route this
                                                   				  pattern .

- Called Party Transformations,
                                                   				  Prefix Digits (Outgoing Calls) —Enter the digits to prefix to the number.
                                                				Enter the digits you used when creating the PSAP callback route point.

Step 4

Click Insert .

Unified CM saves
                                                				the translation pattern. To add additional translation patterns, return to Step 2 .

#### Create Translation
                              	 Patterns for 9.911

In systems
                                    		  where the external access code is 9, a CTI Route Point of 911 or 9.911 may
                                    		  interfere with the timing of secondary dialtone for users when they are
                                    		  attempting to dial external destinations. The creation of a translation pattern
                                    		  for 911 and 9.911 eliminates the secondary dialtone timing.

Create
                                    		  translation patterns so that when users dial the local system external access
                                    		  code of 9 plus 911, the calls are directed to the single 911 pattern previously
                                    		  created in the Create Emergency Call Route Points .

##### Before you begin

This
                                    		  procedure applies to systems where the external access code is 9. If the
                                    		  external access code is something other than 9, this procedure may not apply.

To
                                    		  complete this procedure, you must have already added the partitions and the
                                    		  calling search space for the CiscoEmergencyResponder installation.

The
                                    		  following table provides translation patterns for external access code of 9.

Translation Pattern

911

9.911

Partition

Phones

Phones

Calling Search Space

E911CSS

E911CSS

Route Option

Route this pattern

Route this pattern

Provide outside dial tone

Check this box

Check this box

Called Party Transformations, Discard Digits (Outgoing Calls)

None

PreDot

Step 1

Select Call
                                                   				  Routing > Translation Pattern in Cisco Unified Communications Manager .

Unified CM opens
                                                				the Find and List Translation Patterns page.

Step 2

Click Add a New
                                                				Translation Pattern .

Unified CM opens
                                                				the Translation Pattern Configuration page.

Step 3

Create the
                                             			 translation pattern:

- Translation Pattern -
                                                				911.

- Partition - Phones.

- Numbering Plan - Select
                                                				the numbering plan for your area.

- Calling Search Space -
                                                				Select E911CSS .

- Route Option - Select Route this
                                                   				  pattern .

- Provide Outside Dial Tone - Make sure that this box is checked.

- Called Party Transformations,
                                                   				  Discard Digits - Select <none>.

Step 4

Click Insert .

Unified CM saves
                                                				the translation pattern.

Step 5

Repeat Step 2 to Step 4 with the following changes:

- Translation Pattern —9.911

- Called Party
                                                   				  Transformations, Discard Digits (Outgoing Calls) —PreDot

After you have configured the 9.911 translation patterns, you
                                                				must create the route points. Table 1 provides emergency call route points for 9.911.

These route
                                                            				  points are similar to the route points that you created in the Create Emergency Call Route Points .
                                                            				  In this case, you enter E911 for the partition instead of Phones.

Route Point Setting

Route Points

Primary Number (911)

Backup Number (912)

ELIN (913)

Device Name

RP911

RP912

RPELIN913

Description

The emergency call number for the area. Emergency Responder
                                                            						  handles all calls to this number.

Route point for the Emergency Responder standby server. If the
                                                            						  primary server is unable to handle a call, the standby server receives the call
                                                            						  through this route point.

The destination of all incoming calls from the PSAP. Emergency
                                                            						  Responder transfers these calls to the emergency caller. Route pattern is
                                                            						  prefix (913) plus 10 Xs. Number of Xs should be the same as the standard phone
                                                            						  number used in your locale based on your numbering plan.

The number can only consist of numbers and Xs.

Directory Number

911

912

913XXXXXXXXXX

Partition

E911

E911

E911

Calling Search Space

E911CSS

E911CSS

E911CSS

Forward Busy

Destination: 912

CSS: E911CSS

Destination:

or

- Onsite security number.

CSS: E911CSS

Destination: Onsite security number.

CSS: E911CSS

Forward No Answer

Destination: 912

CSS: E911CSS

Destination:

or

- Onsite security number.

CSS: E911CSS

Destination: Onsite security number.

CSS: E911CSS

Forward On Failure

Destination: 912

CSS: E911CSS

Destination:

or

- Onsite security number.

CSS: E911CSS

Destination: Onsite security number.

CSS: E911CSS

Configuring call-forwarding numbers for the standby server
                                                               					 ensures that calls are either routed to the PSAP servicing the default ERL or
                                                               					 to onsite security, if the standby server cannot handle the call. If you do not
                                                               					 install a standby server, use these settings for the primary server.
                                                               					 Configuring call-forwarding numbers for the ELIN route point ensures that PSAP
                                                               					 callbacks go to onsite security if Emergency Responder cannot handle the call.

#### Create Route Points
                              	 for 9.911

Step 1

In Unified CM,
                                             			 select Device > CTI
                                                				Route Point .

The Find and
                                                				List CTI Route Points page appears.

Step 2

Click Add a new CTI
                                                				Route Point .

The CTI Route
                                                				Point Configuration page appears.

Step 3

Fill in the CTI
                                             			 route point properties:

- Enter a unique name, such
                                                				as RP911 , in the Device
                                                   				  Name field to identify this as the emergency call number. Table 1 shows suggested names, but you can
                                                				use any name you choose.

- Select the appropriate device
                                                				pool from the Device
                                                   				  Pool menu.

- Select the calling search
                                                				space for the route point, as listed in Table 1 .

Step 4

Click Insert to
                                             			 add the new CTI route point.

- Unified CM adds the
                                                   				  route point and asks if you want to configure line 1. Click OK to configure line 1.

- Unified CM opens the
                                                   				  Directory Number configuration page.

Step 5

Enter the
                                             			 configuration for the line that you are creating using the information in Table 1 .

Step 6

Click Insert .

Unified CM adds
                                                				the line to the device. Repeat this procedure until all devices described in Table 1 are configured.

For additional
                                                				assistance, see the documentation and online help included with Unified CM.

### Create Alternate
                           	 Emergency Call Numbers

If your
                                 		  users are used to dialing 9 (or another number) to get an outside line, they
                                 		  might try to dial the emergency number by first dialing the outside line access
                                 		  number. For example, if the emergency number is 911, they might try to dial
                                 		  9911. If you want to accommodate these possibilities, configure translation
                                 		  patterns for the numbers you think are likely to be used. This procedure shows
                                 		  how to set up 9911 as an alternate emergency call number.

Step 1

Select Call
                                                				  Routing > Translation Pattern .

Unified CM opens
                                             				the Find and List Translation Patterns page.

Step 2

Click Add a New
                                             				Translation Pattern .

Unified CM opens
                                             				the Translation Pattern Configuration page.

Step 3

Create the
                                          			 translation pattern:

- Translation Pattern - The
                                             				number you want to support as an emergency number. In this example, 9.911.

- Partition - Select Phones .

- Numbering Plan - Select
                                             				the numbering plan for your area.

- Calling Search Space -
                                             				Select E911CSS .

- Route Option - Select Route this
                                                				  pattern .

- Provide Outside Dial Tone - Select this.

- Called Party Transformations,
                                                				  Discard Digits (Outgoing Calls) - Select PreDot .

Step 4

Click Insert .

Unified CM saves
                                             				the translation pattern. To add additional translation patterns, return to Step 2 .

### Set Up Calling
                           	 Search Space for Gateway and PSAP Connection

You must
                                 		  set up a gateway to use a CAMA or PRI connection to the emergency network or
                                 		  PSTN so that emergency calls can be routed to the local PSAP. See the
                                 		  documentation for your gateway for information about setting up the gateway,
                                 		  and the Unified CM documentation for configuring the gateway. After you set up
                                 		  the gateway, you can follow this procedure to set up the calling search space
                                 		  for the gateway.

Step 1

Select Device >
                                             				Gateway .

Unified CM opens
                                             				the Find and List Gateways page.

Step 2

Click Find without
                                          			 entering search criteria to list all of the gateways, or enter the search
                                          			 criteria required to list the gateway you want to configure and click Find .

Unified CM lists
                                             				the gateways that match your criteria.

Step 3

Click the
                                          			 gateway you want to configure.

Unified CM opens
                                             				the Gateway Configuration page.

Step 4

Select E911CSS for Calling Search
                                             				Space .

Step 5

Click Update .

Unified CM saves
                                             				your changes.

### Create Route
                           	 Patterns for Inter-Cisco Emergency Responder Group Communications

If you
                                 		  have more than one Emergency Responder group in an Emergency Responder cluster,
                                 		  you must configure route patterns to enable each Emergency Responder group to
                                 		  route emergency calls to another Emergency Responder group if a caller's phone
                                 		  homes to a Unified CM cluster outside the current location of the phone. See Cisco Emergency Responder Clusters for a detailed explanation of how
                                 		  Emergency Responder groups communicate within a Emergency Responder cluster.

This
                                 		  procedure explains how to create the route pattern for one Emergency Responder
                                 		  group. The Inter-Cisco ER Group Route Pattern defined on a Emergency Responder
                                 		  Group is a route pattern for incoming Emergency Calls. Consider the network
                                 		  setup in the following figure.

For
                                 		  inter-group communications to work:

You must
                                       				define inter-cluster trunks in each Unified CM cluster to enable communications
                                       				between the Unified CM clusters. See the Unified CM documentation for
                                       				information about creating these types of gateways.

Define the
                                       				route pattern on the Unified CM

- Define route pattern
                                          				  2000.911 and 3000.911 in CUCM cluster A.

- Define Route Pattern
                                          				  1000.911 and 3000.911 in CUCM cluster B.

- Define Route Pattern
                                          				  1000.911 and 2000.911 in CUCM cluster C.

Define
                                       				Inter-Emergency Responder Group Route Pattern

In
                                             					 Emergency Responder Group A, define 1000.911 as the Inter-Emergency Responder
                                             					 Group Route Pattern.

In
                                             					 Emergency Responder Group B, define 2000.911 as the Inter-Emergency Responder
                                             					 Group Route Pattern.

In
                                             					 Emergency Responder Group C, define 3000.911 as the Inter Emergency Responder
                                             					 Group Route Pattern.

These definitions
                                 		  allow a call in an ERL managed by Emergency Responder Group B to be routed to
                                 		  Emergency Responder Group B even though the phone homes to Unified CM cluster
                                 		  A, which is serviced by Emergency Responder Group A.

#### Create Route
                              	 Patterns on Unified CM

##### Before you begin

The dial
                                    		  plans must be unique between all Unified CM clusters supported by a Emergency
                                    		  Responder cluster. For example, in the network shown in Create Route Patterns for Inter-Cisco Emergency Responder Group Communications ,
                                    		  the extension 3003 can only be defined in Unified CM cluster CUCM-A.

Step 1

Go to Cisco
                                             			 Unified CM Administration. Select Call Routing
                                                				> Route/Hunt > Route Pattern .

Step 2

Click Add New .

Step 3

Enter the
                                             			 information for the route pattern:

- Route Pattern — A
                                                				pattern that you can transform to the emergency call number, typically a
                                                				number, a decimal point, and the emergency call number. For example, 1000.911
                                                				or 2000.911. The pattern can only consist of numbers and decimal points.

- Partition — Select E911 .

- Numbering Plan — Select
                                                				the numbering plan for your area.

- Gateway/Route List —
                                                				Select the inter-cluster trunk gateway to use for connecting to the Unified CM
                                                				cluster supported by the Emergency Responder group whose inter-Emergency
                                                				Responder group route pattern you are defining.

- Route Option — Select Route this
                                                   				  pattern .

- Called Party
                                                   				  Transformations: Discard Digits — Select PreDot if you use the suggested pattern, such as 1000.911. If using a different
                                                				technique, select the appropriate setting and enter a Called Party
                                                   				  Transform Mask , if necessary to dial the emergency number.

Step 4

Click Save .

Ensure that you
                                                			 define the route pattern in all other Unified CM clusters serviced by Emergency
                                                			 Responder groups other than the Emergency Responder group whose Inter-Emergency
                                                			 Responder group route pattern you are defining.

For emergency calls to work across Emergency Responder Server Groups in a Emergency Responder cluster, the Calling Party Selection option should be set to Originator in the Device > Trunk Configuration page in Unified CM Administration user interface.

#### Create an Inter-Emergency Responder Group Route Pattern

Ensure you
                                                			 define the Inter-Emergency Responder Route pattern in all other Cisco Emergency
                                                			 Responder groups.

Step 1

Go to Cisco
                                             			 Emergency Responder Administration. Select System >
                                                				Telephony Settings .

Step 2

Add the
                                             			 Inter-Emergency Responder Route pattern.

Step 3

Update
                                             			 Settings.

## Create Emergency
                        	 Responder Cisco Unified Communications Manager User

You must
                              		  add Emergency Responder as a Unified CM user. The settings you enter here are
                              		  used when you configure the Unified CM settings for Emergency Responder.

Step 1

In Unified CM,
                                       			 select User
                                          				Management > Application
                                          				User . Click the Add New button.

Unified CM
                                          				displays the Application User Configuration page.

Step 2

Complete the
                                       			 following required fields:

- UserID —Use a descriptive
                                          				name such as "Emergency_Responder_User."

- Password —Enter a password
                                          				for this user.

- Confirm Password —Reenter
                                          				the password for this user.

Step 3

In the Device
                                          				Information section, select the desired route points and CTI ports and then
                                       			 click the down arrow to add the selected devices to the user control list. The
                                       			 list of devices appears in the Controlled Devices area.

Step 4

Select the
                                       			 following devices:

You may need
                                                      				  to use Find Phones or Find Route Points to select the desired devices.

- All CTI ports created
                                             				  for Cisco Emergency Responder use. For more information, see "Creating the Required CTI Ports" section.

- The primary emergency
                                             				  call number, for example, 911.

- The backup emergency
                                             				  call number, for example, 912.

- The route point used
                                             				  for ELINs, for example, 913XXXXXXXXXX.

Step 5

Click Save .

Step 6

In the Unified
                                       			 CM menu at the top, click User
                                          				Management > User Group .

The user group
                                          				search page appears.

Step 7

At search
                                       			 criterion, enter standard and click Find .

The list of user
                                          				groups starting with the name standard appears.

Step 8

Click the Standard CTI
                                          				Allow Calling Number Modification user group link to display the User Group
                                       			 configuration page.

Step 9

Click Add Application
                                          				Users to Group .

The Find and
                                          				List Application Users popup window appears.

Step 10

Enter the User
                                       			 ID and click Find .

The list of
                                          				Applications users appears.

Step 11

Check the check
                                       			 box next to the user ID and click Add
                                          				Selected .

Unified CM adds
                                          				the selected user to the Standard CTI Allow Calling Number Modification user
                                          				group.

Step 12

Choose User Management
                                          				> User Group .

The user group
                                          				search page appears.

Step 13

Enter standard as
                                       			 the search criterion and click Find .

The list of user
                                          				groups starting with the name Standard appears.

Step 14

Click the Standard CTI
                                          				Enabled group.

Repeat steps 9
                                          				through 11 to add the user to the Standard CTI Enabled group.

| Step 1 | Select Call Routing > Class of
                                                				  Control > Partition in Cisco Unified Communications Manager . The Find and
                                             				List Partitions page appears. |
|---|---|
| Step 2 | Click Add a New
                                             				Partition . The Partition
                                             				Configuration page appears. |
| Step 3 | Enter a
                                          			 descriptive name, such as Phones , in
                                          			 the Partition Name
                                             				and Description field. You can optionally include a description. |
| Step 4 | Click Insert to
                                          			 add the new partition. |

| Step 1 | Select Call Routing > Class of
                                                				  Control > Calling Search Space in Cisco Unified Communications Manager . The Find and
                                             				List Calling Search Spaces page appears. |
|---|---|
| Step 2 | Click Add a New
                                             				Calling Search Space . The Calling
                                             				Search Space Configuration page appears. |
| Step 3 | Enter a
                                          			 descriptive name, such as PhoneCSS, in the Calling Search
                                             				Space Name field. |
| Step 4 | Select the Phones partition in the Available Partitions list box, and click the arrow buttons
                                          			 between the two list boxes to add it to the Selected Partitions list box. |
| Step 5 | Click Insert to
                                          			 add the new calling search space. |

| Step 1 | Select Device >
                                             				Phone . Unified CM
                                             				displays the Find and List Phones page. |
|---|---|
| Step 2 | Select Device name is
                                             				not empty in the search fields and click Find . Unified CM lists
                                             				all of the phones in the bottom frame. |
| Step 3 | Click the phone
                                          			 with the configuration that you want to change. Unified CM
                                             				displays the Phone Configuration page. |
| Step 4 | Change the
                                          			 calling search space to PhoneCSS and
                                          			 click Update . |
| Step 5 | Click the line
                                          			 number that you want to configure in the left-hand column. Unified CM
                                             				displays the Directory Number Configuration page. |
| Step 6 | Change the
                                          			 partition to Phones , and
                                          			 the calling search space to PhoneCSS . |
| Step 7 | Click Insert to
                                          			 save your changes. |

| Step 1 | Select Call Routing > Class of
                                                				  Control > Partition in Cisco Unified Communications Manager . The Find and
                                             				List Partitions page appears. |
|---|---|
| Step 2 | Click Add a New
                                             				Partition . The Partition
                                             				Configuration page appears. |
| Step 3 | Enter a
                                          			 descriptive name, such as E911 , in the Partition
                                             				Name field. |
| Step 4 | Click Insert to
                                          			 add the new partition. |

| Step 1 | Select Call Routing > Class of
                                                				  Control > Calling Search Space in Cisco Unified Communications Manager . . The Find and
                                             				List Calling Search Spaces page appears. |
|---|---|
| Step 2 | Click Add a New
                                             				Calling Search Space . The Calling
                                             				Search Space Configuration page appears. |
| Step 3 | Enter a
                                          			 descriptive name, such as E911CSS, in the Calling Search
                                             				Space Name field. |
| Step 4 | In the Available
                                          			 Partitions list box, select the E911 partition and then select the Phones partition in that order. Click the arrow buttons between the two
                                          			 list boxes to add them to the Selected Partitions list box. Arrange the
                                          			 partitions so that E911 is at the top of the list. If you are using
                                             				any other partitions, add them to this list after the E911 partition. Note You must list
                                                         				  the E911 partition before the Phones partition for the following reason: When
                                                         				  the user configures the translation pattern 911 or 9.911 (see Create Translation Patterns for 9.911 ),
                                                         				  the 911 Route Point is in the E911 partition; phones cannot look into the E911
                                                         				  Partition. The 911 Translation Pattern is in the phones partition and gets the
                                                         				  E911CSS. When the E911 partition is listed first, it matches the 911 Route
                                                         				  Point and the call goes to the Emergency Responder server as intended. If you
                                                         				  make the error of listing the Phones partition first, the Translation Pattern
                                                         				  keeps searching, resulting in a fast busy signal. | Note | You must list
                                                         				  the E911 partition before the Phones partition for the following reason: When
                                                         				  the user configures the translation pattern 911 or 9.911 (see Create Translation Patterns for 9.911 ),
                                                         				  the 911 Route Point is in the E911 partition; phones cannot look into the E911
                                                         				  Partition. The 911 Translation Pattern is in the phones partition and gets the
                                                         				  E911CSS. When the E911 partition is listed first, it matches the 911 Route
                                                         				  Point and the call goes to the Emergency Responder server as intended. If you
                                                         				  make the error of listing the Phones partition first, the Translation Pattern
                                                         				  keeps searching, resulting in a fast busy signal. |
| Note | You must list
                                                         				  the E911 partition before the Phones partition for the following reason: When
                                                         				  the user configures the translation pattern 911 or 9.911 (see Create Translation Patterns for 9.911 ),
                                                         				  the 911 Route Point is in the E911 partition; phones cannot look into the E911
                                                         				  Partition. The 911 Translation Pattern is in the phones partition and gets the
                                                         				  E911CSS. When the E911 partition is listed first, it matches the 911 Route
                                                         				  Point and the call goes to the Emergency Responder server as intended. If you
                                                         				  make the error of listing the Phones partition first, the Translation Pattern
                                                         				  keeps searching, resulting in a fast busy signal. |
| Step 5 | Click Insert to
                                          			 add the new calling search space. |

| Note | You must list
                                                         				  the E911 partition before the Phones partition for the following reason: When
                                                         				  the user configures the translation pattern 911 or 9.911 (see Create Translation Patterns for 9.911 ),
                                                         				  the 911 Route Point is in the E911 partition; phones cannot look into the E911
                                                         				  Partition. The 911 Translation Pattern is in the phones partition and gets the
                                                         				  E911CSS. When the E911 partition is listed first, it matches the 911 Route
                                                         				  Point and the call goes to the Emergency Responder server as intended. If you
                                                         				  make the error of listing the Phones partition first, the Translation Pattern
                                                         				  keeps searching, resulting in a fast busy signal. |
|---|---|

| Note | If you use 9
                                                   				  as the access code, see Create Translation Patterns for 9.911 to configure Emergency Responder. |
|---|---|

| Note | CTI route points for the 911, 912, and 913 emergency numbers must be unique. You should not have more than one CTI route point
                                             addressed to the emergency numbers used earlier. |
|---|---|

| Route Point Setting | Route Points |
|---|---|
| Primary Number (911) | Backup Number (912) | ELIN (913) |
| Device Name | RP911 | RP912 | RPELIN913 |
| Description | The emergency call number for the area. Emergency Responder
                                             					 handles all calls to this number. | Route point for the Emergency Responder standby server. If the
                                             					 primary server is unable to handle a call, the standby server receives the call
                                             					 through this route point. | The destination of all
                                             					 incoming calls from the PSAP. Emergency Responder transfers these calls to the
                                             					 emergency caller. The Route pattern is a prefix (913) plus a Fully Qualified
                                             					 Number. Fully Qualified Number
                                             					 could be North American Numbering Plan or E.164 with Country Code. In case the
                                             					 ELIN is received as E.164 number with a leading plus sign ( +), use a
                                             					 Translation Pattern to remove the leading plus sign. Note In case the ELIN is
                                                      					 received as E.164 number with a leading plus sign ( +), use a Translation
                                                      					 Pattern to remove the leading plus sign. | Note | In case the ELIN is
                                                      					 received as E.164 number with a leading plus sign ( +), use a Translation
                                                      					 Pattern to remove the leading plus sign. |
| Note | In case the ELIN is
                                                      					 received as E.164 number with a leading plus sign ( +), use a Translation
                                                      					 Pattern to remove the leading plus sign. |
| Directory Number | 911 | 912 | 913XXXXXXXXXX |
| Partition | Phones | E911 | E911 |
| Calling Search Space | E911CSS | E911CSS | E911CSS |
| Forward Busy | Destination: 912 CSS: E911CSS | Destination: Route pattern for default
                                                						ERL. or Onsite security
                                                						number. CSS: E911CSS | Destination: Onsite security number. CSS: E911CSS |
| Forward No Answer | Destination: 912 CSS: E911CSS | Destination: Route pattern for default
                                                						ERL. or Onsite security
                                                						number. CSS: E911CSS | Destination: Onsite security number. CSS: E911CSS |
| Forward On Failure | Destination: 912 CSS: E911CSS | Destination: Route pattern for default
                                                						ERL. or Onsite security
                                                						number. CSS: E911CSS | Destination: Onsite security number. CSS: E911CSS |
| Voice Mail
                                             					 Mask | Do not
                                             					 configure a Voice Mail Mask for this route point. | Do not
                                             					 configure a Voice Mail Mask for this route point. | Do not
                                             					 configure a Voice Mail Mask for this route point. |

| Note | In case the ELIN is
                                                      					 received as E.164 number with a leading plus sign ( +), use a Translation
                                                      					 Pattern to remove the leading plus sign. |
|---|---|

| Note | Configuring
                                                				call-forwarding numbers for the standby server ensures that calls are either
                                                				routed to the PSAP servicing the default ERL, or onsite security, if the
                                                				standby server cannot handle the call. If you do not install a standby server,
                                                				use these settings for the primary server. Configuring call-forwarding numbers
                                                				for the ELIN route point ensures that PSAP callbacks go to onsite security if
                                                				Emergency Responder cannot handle the call. |
|---|---|

| Step 1 | In Unified CM,
                                          			 select Device >
                                             				CTI Route Point . The Find and
                                             				List CTI Route Points page appears. |
|---|---|
| Step 2 | Click Add a new CTI
                                             				Route Point . The CTI Route
                                             				Point Configuration page appears. |
| Step 3 | Fill in the
                                          			 CTI route point properties: Enter a unique name, such
                                             				as RP911 , in the Device
                                                				  Name field to identify this as the emergency call number. The Emergency
                                             				call route points table above shows suggested names, but you can use any name
                                             				you choose. Select the appropriate
                                             				device pool from the Device
                                                				  Pool menu. Select the calling search
                                             				space for the route point, as listed in the Emergency call route points table
                                             				above. |
| Step 4 | Click Insert to
                                          			 add the new CTI route point. Unified CM
                                             				adds the route point and asks if you want to configure line 1. Click OK to
                                             				configure line 1. Unified CM
                                             				opens the Directory Number configuration page. |
| Step 5 | Enter the
                                          			 configuration for the line you are creating using the information in the
                                          			 Emergency call route points table above. |
| Step 6 | Click Insert . Unified CM
                                             				adds the line to the device. Repeat this procedure until all devices described
                                             				in the Emergency call route points table above are configured. For additional
                                             				assistance, see documentation and online help included with Unified CM. |

| Step 1 | Select Device >
                                             				Phone . Cisco
                                                				  Unified Communications Manager opens the Find and List Phones page. |
|---|---|
| Step 2 | Click Add a New
                                             				Phone . Cisco
                                                				  Unified Communications Manager opens the Add a New Phone page. |
| Step 3 | Select CTI Port for Phone Type and click Next . Cisco
                                                				  Unified Communications Manager opens the Phone Configuration page. |
| Step 4 | Configure the
                                          			 CTI Port, entering this information: Device Name - Enter
                                             				something meaningful to you, for example, CTI3001. Device Pool - Select an
                                             				appropriate device pool. This device pool must use the G.711 region. Calling Search Space -
                                             				Select PhoneCSS . |
| Step 5 | Click Insert . Cisco Unified Communications Manager creates the CTI
                                             				port and asks if you want to configure line 1. Click OK . Cisco
                                                				  Unified Communications Manager opens the Directory Number
                                             				Configuration page. |
| Step 6 | Configure line 1
                                          			 for the CTI port, entering this information: Partition - Select Phones . Calling Search Space -
                                             				Select PhoneCSS . Note Configure only
                                                         				  one line for each CTI port. Onsite security alert prompts may not get from one
                                                         				  or more of these lines when the online alert notification is initiated through
                                                         				  these ports. | Note | Configure only
                                                         				  one line for each CTI port. Onsite security alert prompts may not get from one
                                                         				  or more of these lines when the online alert notification is initiated through
                                                         				  these ports. |
| Note | Configure only
                                                         				  one line for each CTI port. Onsite security alert prompts may not get from one
                                                         				  or more of these lines when the online alert notification is initiated through
                                                         				  these ports. |
| Step 7 | Click Insert . Cisco Unified Communications Manager adds the line to
                                             				the device. Repeat the procedure to create each CTI route port that you
                                             				require. Note All subsequent
                                                         				  CTI ports you create must be consecutive from the first CTI port DN. CTI port DN in Cisco
                                                         				  Emergency Responder does not support E.164 dial pattern. | Note | All subsequent
                                                         				  CTI ports you create must be consecutive from the first CTI port DN. CTI port DN in Cisco
                                                         				  Emergency Responder does not support E.164 dial pattern. |
| Note | All subsequent
                                                         				  CTI ports you create must be consecutive from the first CTI port DN. CTI port DN in Cisco
                                                         				  Emergency Responder does not support E.164 dial pattern. |

| Note | Configure only
                                                         				  one line for each CTI port. Onsite security alert prompts may not get from one
                                                         				  or more of these lines when the online alert notification is initiated through
                                                         				  these ports. |
|---|---|

| Note | All subsequent
                                                         				  CTI ports you create must be consecutive from the first CTI port DN. CTI port DN in Cisco
                                                         				  Emergency Responder does not support E.164 dial pattern. |
|---|---|

| Note | The primary
                                             			 Cisco Unified CM in the Group assigned to the device pool for Cisco ER must
                                             			 also be the primary CTI Manager for Cisco Emergency Responder. The Group must
                                             			 also contain the secondary CTI manager for Cisco ER. |
|---|---|

| Step 1 | Select System
                                             				> Unified CM Group . The Find and
                                             				List Unified CM Groups page opens. |
|---|---|
| Step 2 | Click Add
                                             				New . The Unified CM
                                             				Group Configuration page opens. |
| Step 3 | Enter the
                                          			 following information in the appropriate field: Name – Enter a CM
                                                      					 Group name that is meaningful to you; for example, Cisco Emergency Responder CM
                                                      					 Group. Auto-registration Cisco
                                                         						Unified Communications Manager Group - Do not check this box for
                                                      					 the Unified CM Group for Emergency Responder. Cisco Unified Communications
                                                         						Managers – Add the primary and secondary CTI Manager for Emergency
                                                      					 Responder to the list of Selected Cisco Unified Communications Managers by
                                                      					 selecting each from the Available Cisco Unified Communications Managers and
                                                      					 clicking the Down Arrow . |
| Step 4 | Click Save . |

| Relevant Alarms | Alarm Level | Explanation | Recommended
                                             					 Action |
|---|---|---|---|
| CtiProviderOpened | Informational | Application opened the provider successfully. | This alarm
                                             					 is for informational purposes only; no action is required. |
| CtiProviderClosed | Informational | Application closed the provider. | Verify that
                                             					 Cisco Emergency Responder is up and running, verify network connectivity
                                             					 between application server and Unified CM, and verify the CPU utilization is in
                                             					 the safe range for the application server and Unified CM. |
| ApplicationConnectionDropped | Warning | TCP or TLS connection between CTIManager and Application is
                                             					 disconnected. | Verify that
                                             					 Cisco Emergency Responder is up and running, verify network connectivity
                                             					 between the application server and Unified CM, and verify the CPU utilization
                                             					 is in the safe range for the application server and Unified CM. |
| CtiIncompatibleProtocolVersion | Warning | The Cisco Emergency Responder version or its Unified Communications Manager
                                             					 setting is not compatible with this version of CTIManager. | Verify that
                                             					 the correct version of the Cisco Emergency Responder is being used and its
                                             					 Unified CM version setting is correct. See Change Cisco Unified Communications Manager Version to view and update the
                                             					 Unified CM version. |

| Step 1 | Select Call
                                                   				  Routing > Route/Hunt > Route
                                                   				  Pattern in Cisco Unified Communications Manager . Unified CM opens
                                                				the Find and List Route Patterns page. |
|---|---|
| Step 2 | Click Add a New Route
                                                				Pattern . Unified CM opens
                                                				the Route Pattern Configuration page. |
| Step 3 | Enter the
                                             			 information for the route pattern: Route Pattern - A pattern
                                                				that you can transform to the emergency call number, typically a number, a dot,
                                                				and the emergency call number. For example, 10.911, 11.911, and so forth. The
                                                				pattern can only contain numbers and dots. Partition - Select E911 . Numbering Plan - Select
                                                				the numbering plan for your area. Gateway/Route List -
                                                				Select the gateway to use for connecting to the local PSAP. Route Option - Select Route this
                                                   				  pattern . Use Calling Party's External
                                                   				  Phone Number Mask - Select this option. Discard Digits - Select PreDot if
                                                				you use the suggested pattern, such as 10.911. If using a different technique,
                                                				select the appropriate setting and enter a Called Party
                                                   				  Transform Mask if necessary (to dial the emergency number). |
| Step 4 | Click Insert . Unified CM saves
                                                				the route pattern. To add additional route patterns, return to Step 2 . Tip Consider
                                                            				  developing a detailed naming strategy for the route patterns because you might
                                                            				  end up with a large number of them. For example, you could use a pattern such
                                                            				  as xyzzaaab.911, where x is a Emergency Responder cluster identifier; y is a
                                                            				  Emergency Responder group identifier; zz is the PSAP identifier; aaa is the ERL
                                                            				  identifier; and b is the ELIN identifier (within the ERL). | Tip | Consider
                                                            				  developing a detailed naming strategy for the route patterns because you might
                                                            				  end up with a large number of them. For example, you could use a pattern such
                                                            				  as xyzzaaab.911, where x is a Emergency Responder cluster identifier; y is a
                                                            				  Emergency Responder group identifier; zz is the PSAP identifier; aaa is the ERL
                                                            				  identifier; and b is the ELIN identifier (within the ERL). |
| Tip | Consider
                                                            				  developing a detailed naming strategy for the route patterns because you might
                                                            				  end up with a large number of them. For example, you could use a pattern such
                                                            				  as xyzzaaab.911, where x is a Emergency Responder cluster identifier; y is a
                                                            				  Emergency Responder group identifier; zz is the PSAP identifier; aaa is the ERL
                                                            				  identifier; and b is the ELIN identifier (within the ERL). |

| Tip | Consider
                                                            				  developing a detailed naming strategy for the route patterns because you might
                                                            				  end up with a large number of them. For example, you could use a pattern such
                                                            				  as xyzzaaab.911, where x is a Emergency Responder cluster identifier; y is a
                                                            				  Emergency Responder group identifier; zz is the PSAP identifier; aaa is the ERL
                                                            				  identifier; and b is the ELIN identifier (within the ERL). |
|---|---|

| Step 1 | Select Call
                                                   				  Routing > Translation Pattern in Cisco Unified Communications Manager . Unified CM opens
                                                				the Find and List Translation Patterns page. |
|---|---|
| Step 2 | Click Add a New
                                                				Translation Pattern . Unified CM opens
                                                				the Translation Pattern Configuration page. |
| Step 3 | Create the
                                             			 translation pattern: Translation Pattern - The
                                                				DID you are using as an ELIN. If you can, use X variables to create a pattern
                                                				that covers more than one DID (for example, 5555551XXX). If you cannot create a
                                                				pattern, define translation patterns for each DID separately. Partition - Select E911 . Numbering Plan - Select
                                                				the numbering plan for your area. Calling Search Space -
                                                				Select E911CSS . Route Option - Select Route this
                                                   				  pattern . Called Party Transformations,
                                                   				  Prefix Digits (Outgoing Calls) —Enter the digits to prefix to the number.
                                                				Enter the digits you used when creating the PSAP callback route point. |
| Step 4 | Click Insert . Unified CM saves
                                                				the translation pattern. To add additional translation patterns, return to Step 2 . |

| Translation Pattern | 911 | 9.911 |
|---|---|---|
| Partition | Phones | Phones |
| Calling Search Space | E911CSS | E911CSS |
| Route Option | Route this pattern | Route this pattern |
| Provide outside dial tone | Check this box | Check this box |
| Called Party Transformations, Discard Digits (Outgoing Calls) | None | PreDot |

| Step 1 | Select Call
                                                   				  Routing > Translation Pattern in Cisco Unified Communications Manager . Unified CM opens
                                                				the Find and List Translation Patterns page. |
|---|---|
| Step 2 | Click Add a New
                                                				Translation Pattern . Unified CM opens
                                                				the Translation Pattern Configuration page. |
| Step 3 | Create the
                                             			 translation pattern: Translation Pattern -
                                                				911. Partition - Phones. Numbering Plan - Select
                                                				the numbering plan for your area. Calling Search Space -
                                                				Select E911CSS . Route Option - Select Route this
                                                   				  pattern . Provide Outside Dial Tone - Make sure that this box is checked. Called Party Transformations,
                                                   				  Discard Digits - Select <none>. |
| Step 4 | Click Insert . Unified CM saves
                                                				the translation pattern. |
| Step 5 | Repeat Step 2 to Step 4 with the following changes: Translation Pattern —9.911 Called Party
                                                   				  Transformations, Discard Digits (Outgoing Calls) —PreDot After you have configured the 9.911 translation patterns, you
                                                				must create the route points. Table 1 provides emergency call route points for 9.911. Note These route
                                                            				  points are similar to the route points that you created in the Create Emergency Call Route Points .
                                                            				  In this case, you enter E911 for the partition instead of Phones. Table 4. Emergency
                                                      				Call Route Points for 9.911 Route Point Setting Route Points Primary Number (911) Backup Number (912) ELIN (913) Device Name RP911 RP912 RPELIN913 Description The emergency call number for the area. Emergency Responder
                                                            						  handles all calls to this number. Route point for the Emergency Responder standby server. If the
                                                            						  primary server is unable to handle a call, the standby server receives the call
                                                            						  through this route point. The destination of all incoming calls from the PSAP. Emergency
                                                            						  Responder transfers these calls to the emergency caller. Route pattern is
                                                            						  prefix (913) plus 10 Xs. Number of Xs should be the same as the standard phone
                                                            						  number used in your locale based on your numbering plan. The number can only consist of numbers and Xs. Directory Number 911 912 913XXXXXXXXXX Partition E911 E911 E911 Calling Search Space E911CSS E911CSS E911CSS Forward Busy Destination: 912 CSS: E911CSS Destination: Route pattern for default
                                                               							 ERL. or Onsite security number. CSS: E911CSS Destination: Onsite security number. CSS: E911CSS Forward No Answer Destination: 912 CSS: E911CSS Destination: Route pattern for default
                                                               							 ERL. or Onsite security number. CSS: E911CSS Destination: Onsite security number. CSS: E911CSS Forward On Failure Destination: 912 CSS: E911CSS Destination: Route pattern for default
                                                               							 ERL. or Onsite security number. CSS: E911CSS Destination: Onsite security number. CSS: E911CSS Note Configuring call-forwarding numbers for the standby server
                                                               					 ensures that calls are either routed to the PSAP servicing the default ERL or
                                                               					 to onsite security, if the standby server cannot handle the call. If you do not
                                                               					 install a standby server, use these settings for the primary server.
                                                               					 Configuring call-forwarding numbers for the ELIN route point ensures that PSAP
                                                               					 callbacks go to onsite security if Emergency Responder cannot handle the call. | Note | These route
                                                            				  points are similar to the route points that you created in the Create Emergency Call Route Points .
                                                            				  In this case, you enter E911 for the partition instead of Phones. | Route Point Setting | Route Points | Primary Number (911) | Backup Number (912) | ELIN (913) | Device Name | RP911 | RP912 | RPELIN913 | Description | The emergency call number for the area. Emergency Responder
                                                            						  handles all calls to this number. | Route point for the Emergency Responder standby server. If the
                                                            						  primary server is unable to handle a call, the standby server receives the call
                                                            						  through this route point. | The destination of all incoming calls from the PSAP. Emergency
                                                            						  Responder transfers these calls to the emergency caller. Route pattern is
                                                            						  prefix (913) plus 10 Xs. Number of Xs should be the same as the standard phone
                                                            						  number used in your locale based on your numbering plan. The number can only consist of numbers and Xs. | Directory Number | 911 | 912 | 913XXXXXXXXXX | Partition | E911 | E911 | E911 | Calling Search Space | E911CSS | E911CSS | E911CSS | Forward Busy | Destination: 912 CSS: E911CSS | Destination: Route pattern for default
                                                               							 ERL. or Onsite security number. CSS: E911CSS | Destination: Onsite security number. CSS: E911CSS | Forward No Answer | Destination: 912 CSS: E911CSS | Destination: Route pattern for default
                                                               							 ERL. or Onsite security number. CSS: E911CSS | Destination: Onsite security number. CSS: E911CSS | Forward On Failure | Destination: 912 CSS: E911CSS | Destination: Route pattern for default
                                                               							 ERL. or Onsite security number. CSS: E911CSS | Destination: Onsite security number. CSS: E911CSS | Note | Configuring call-forwarding numbers for the standby server
                                                               					 ensures that calls are either routed to the PSAP servicing the default ERL or
                                                               					 to onsite security, if the standby server cannot handle the call. If you do not
                                                               					 install a standby server, use these settings for the primary server.
                                                               					 Configuring call-forwarding numbers for the ELIN route point ensures that PSAP
                                                               					 callbacks go to onsite security if Emergency Responder cannot handle the call. |
| Note | These route
                                                            				  points are similar to the route points that you created in the Create Emergency Call Route Points .
                                                            				  In this case, you enter E911 for the partition instead of Phones. |
| Route Point Setting | Route Points |
| Primary Number (911) | Backup Number (912) | ELIN (913) |
| Device Name | RP911 | RP912 | RPELIN913 |
| Description | The emergency call number for the area. Emergency Responder
                                                            						  handles all calls to this number. | Route point for the Emergency Responder standby server. If the
                                                            						  primary server is unable to handle a call, the standby server receives the call
                                                            						  through this route point. | The destination of all incoming calls from the PSAP. Emergency
                                                            						  Responder transfers these calls to the emergency caller. Route pattern is
                                                            						  prefix (913) plus 10 Xs. Number of Xs should be the same as the standard phone
                                                            						  number used in your locale based on your numbering plan. The number can only consist of numbers and Xs. |
| Directory Number | 911 | 912 | 913XXXXXXXXXX |
| Partition | E911 | E911 | E911 |
| Calling Search Space | E911CSS | E911CSS | E911CSS |
| Forward Busy | Destination: 912 CSS: E911CSS | Destination: Route pattern for default
                                                               							 ERL. or Onsite security number. CSS: E911CSS | Destination: Onsite security number. CSS: E911CSS |
| Forward No Answer | Destination: 912 CSS: E911CSS | Destination: Route pattern for default
                                                               							 ERL. or Onsite security number. CSS: E911CSS | Destination: Onsite security number. CSS: E911CSS |
| Forward On Failure | Destination: 912 CSS: E911CSS | Destination: Route pattern for default
                                                               							 ERL. or Onsite security number. CSS: E911CSS | Destination: Onsite security number. CSS: E911CSS |
| Note | Configuring call-forwarding numbers for the standby server
                                                               					 ensures that calls are either routed to the PSAP servicing the default ERL or
                                                               					 to onsite security, if the standby server cannot handle the call. If you do not
                                                               					 install a standby server, use these settings for the primary server.
                                                               					 Configuring call-forwarding numbers for the ELIN route point ensures that PSAP
                                                               					 callbacks go to onsite security if Emergency Responder cannot handle the call. |

| Note | These route
                                                            				  points are similar to the route points that you created in the Create Emergency Call Route Points .
                                                            				  In this case, you enter E911 for the partition instead of Phones. |
|---|---|

| Route Point Setting | Route Points |
|---|---|
| Primary Number (911) | Backup Number (912) | ELIN (913) |
| Device Name | RP911 | RP912 | RPELIN913 |
| Description | The emergency call number for the area. Emergency Responder
                                                            						  handles all calls to this number. | Route point for the Emergency Responder standby server. If the
                                                            						  primary server is unable to handle a call, the standby server receives the call
                                                            						  through this route point. | The destination of all incoming calls from the PSAP. Emergency
                                                            						  Responder transfers these calls to the emergency caller. Route pattern is
                                                            						  prefix (913) plus 10 Xs. Number of Xs should be the same as the standard phone
                                                            						  number used in your locale based on your numbering plan. The number can only consist of numbers and Xs. |
| Directory Number | 911 | 912 | 913XXXXXXXXXX |
| Partition | E911 | E911 | E911 |
| Calling Search Space | E911CSS | E911CSS | E911CSS |
| Forward Busy | Destination: 912 CSS: E911CSS | Destination: Route pattern for default
                                                               							 ERL. or Onsite security number. CSS: E911CSS | Destination: Onsite security number. CSS: E911CSS |
| Forward No Answer | Destination: 912 CSS: E911CSS | Destination: Route pattern for default
                                                               							 ERL. or Onsite security number. CSS: E911CSS | Destination: Onsite security number. CSS: E911CSS |
| Forward On Failure | Destination: 912 CSS: E911CSS | Destination: Route pattern for default
                                                               							 ERL. or Onsite security number. CSS: E911CSS | Destination: Onsite security number. CSS: E911CSS |

| Note | Configuring call-forwarding numbers for the standby server
                                                               					 ensures that calls are either routed to the PSAP servicing the default ERL or
                                                               					 to onsite security, if the standby server cannot handle the call. If you do not
                                                               					 install a standby server, use these settings for the primary server.
                                                               					 Configuring call-forwarding numbers for the ELIN route point ensures that PSAP
                                                               					 callbacks go to onsite security if Emergency Responder cannot handle the call. |
|---|---|

| Step 1 | In Unified CM,
                                             			 select Device > CTI
                                                				Route Point . The Find and
                                                				List CTI Route Points page appears. |
|---|---|
| Step 2 | Click Add a new CTI
                                                				Route Point . The CTI Route
                                                				Point Configuration page appears. |
| Step 3 | Fill in the CTI
                                             			 route point properties: Enter a unique name, such
                                                				as RP911 , in the Device
                                                   				  Name field to identify this as the emergency call number. Table 1 shows suggested names, but you can
                                                				use any name you choose. Select the appropriate device
                                                				pool from the Device
                                                   				  Pool menu. Select the calling search
                                                				space for the route point, as listed in Table 1 . |
| Step 4 | Click Insert to
                                             			 add the new CTI route point. Unified CM adds the
                                                   				  route point and asks if you want to configure line 1. Click OK to configure line 1. Unified CM opens the
                                                   				  Directory Number configuration page. |
| Step 5 | Enter the
                                             			 configuration for the line that you are creating using the information in Table 1 . |
| Step 6 | Click Insert . Unified CM adds
                                                				the line to the device. Repeat this procedure until all devices described in Table 1 are configured. For additional
                                                				assistance, see the documentation and online help included with Unified CM. |

| Step 1 | Select Call
                                                				  Routing > Translation Pattern . Unified CM opens
                                             				the Find and List Translation Patterns page. |
|---|---|
| Step 2 | Click Add a New
                                             				Translation Pattern . Unified CM opens
                                             				the Translation Pattern Configuration page. |
| Step 3 | Create the
                                          			 translation pattern: Translation Pattern - The
                                             				number you want to support as an emergency number. In this example, 9.911. Partition - Select Phones . Numbering Plan - Select
                                             				the numbering plan for your area. Calling Search Space -
                                             				Select E911CSS . Route Option - Select Route this
                                                				  pattern . Provide Outside Dial Tone - Select this. Called Party Transformations,
                                                				  Discard Digits (Outgoing Calls) - Select PreDot . |
| Step 4 | Click Insert . Unified CM saves
                                             				the translation pattern. To add additional translation patterns, return to Step 2 . |

| Step 1 | Select Device >
                                             				Gateway . Unified CM opens
                                             				the Find and List Gateways page. |
|---|---|
| Step 2 | Click Find without
                                          			 entering search criteria to list all of the gateways, or enter the search
                                          			 criteria required to list the gateway you want to configure and click Find . Unified CM lists
                                             				the gateways that match your criteria. |
| Step 3 | Click the
                                          			 gateway you want to configure. Unified CM opens
                                             				the Gateway Configuration page. |
| Step 4 | Select E911CSS for Calling Search
                                             				Space . |
| Step 5 | Click Update . Unified CM saves
                                             				your changes. |

| Step 1 | Go to Cisco
                                             			 Unified CM Administration. Select Call Routing
                                                				> Route/Hunt > Route Pattern . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Enter the
                                             			 information for the route pattern: Route Pattern — A
                                                				pattern that you can transform to the emergency call number, typically a
                                                				number, a decimal point, and the emergency call number. For example, 1000.911
                                                				or 2000.911. The pattern can only consist of numbers and decimal points. Partition — Select E911 . Numbering Plan — Select
                                                				the numbering plan for your area. Gateway/Route List —
                                                				Select the inter-cluster trunk gateway to use for connecting to the Unified CM
                                                				cluster supported by the Emergency Responder group whose inter-Emergency
                                                				Responder group route pattern you are defining. Route Option — Select Route this
                                                   				  pattern . Called Party
                                                   				  Transformations: Discard Digits — Select PreDot if you use the suggested pattern, such as 1000.911. If using a different
                                                				technique, select the appropriate setting and enter a Called Party
                                                   				  Transform Mask , if necessary to dial the emergency number. |
| Step 4 | Click Save . Unified CM
                                             			 saves the route pattern. To add additional route patterns, return to Step 2 . |

| Note | Ensure that you
                                                			 define the route pattern in all other Unified CM clusters serviced by Emergency
                                                			 Responder groups other than the Emergency Responder group whose Inter-Emergency
                                                			 Responder group route pattern you are defining. |
|---|---|

| Note | For emergency calls to work across Emergency Responder Server Groups in a Emergency Responder cluster, the Calling Party Selection option should be set to Originator in the Device > Trunk Configuration page in Unified CM Administration user interface. |
|---|---|

| Note | Ensure you
                                                			 define the Inter-Emergency Responder Route pattern in all other Cisco Emergency
                                                			 Responder groups. |
|---|---|

| Step 1 | Go to Cisco
                                             			 Emergency Responder Administration. Select System >
                                                				Telephony Settings . |
|---|---|
| Step 2 | Add the
                                             			 Inter-Emergency Responder Route pattern. |
| Step 3 | Update
                                             			 Settings. |

| Step 1 | In Unified CM,
                                       			 select User
                                          				Management > Application
                                          				User . Click the Add New button. Unified CM
                                          				displays the Application User Configuration page. |
|---|---|
| Step 2 | Complete the
                                       			 following required fields: UserID —Use a descriptive
                                          				name such as "Emergency_Responder_User." Password —Enter a password
                                          				for this user. Confirm Password —Reenter
                                          				the password for this user. |
| Step 3 | In the Device
                                          				Information section, select the desired route points and CTI ports and then
                                       			 click the down arrow to add the selected devices to the user control list. The
                                       			 list of devices appears in the Controlled Devices area. |
| Step 4 | Select the
                                       			 following devices: Note You may need
                                                      				  to use Find Phones or Find Route Points to select the desired devices. All CTI ports created
                                             				  for Cisco Emergency Responder use. For more information, see "Creating the Required CTI Ports" section. The primary emergency
                                             				  call number, for example, 911. The backup emergency
                                             				  call number, for example, 912. The route point used
                                             				  for ELINs, for example, 913XXXXXXXXXX. | Note | You may need
                                                      				  to use Find Phones or Find Route Points to select the desired devices. |
| Note | You may need
                                                      				  to use Find Phones or Find Route Points to select the desired devices. |
| Step 5 | Click Save . |
| Step 6 | In the Unified
                                       			 CM menu at the top, click User
                                          				Management > User Group . The user group
                                          				search page appears. |
| Step 7 | At search
                                       			 criterion, enter standard and click Find . The list of user
                                          				groups starting with the name standard appears. |
| Step 8 | Click the Standard CTI
                                          				Allow Calling Number Modification user group link to display the User Group
                                       			 configuration page. |
| Step 9 | Click Add Application
                                          				Users to Group . The Find and
                                          				List Application Users popup window appears. |
| Step 10 | Enter the User
                                       			 ID and click Find . The list of
                                          				Applications users appears. |
| Step 11 | Check the check
                                       			 box next to the user ID and click Add
                                          				Selected . Unified CM adds
                                          				the selected user to the Standard CTI Allow Calling Number Modification user
                                          				group. |
| Step 12 | Choose User Management
                                          				> User Group . The user group
                                          				search page appears. |
| Step 13 | Enter standard as
                                       			 the search criterion and click Find . The list of user
                                          				groups starting with the name Standard appears. |
| Step 14 | Click the Standard CTI
                                          				Enabled group. Repeat steps 9
                                          				through 11 to add the user to the Standard CTI Enabled group. |

| Note | You may need
                                                      				  to use Find Phones or Find Route Points to select the desired devices. |
|---|---|