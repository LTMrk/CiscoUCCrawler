---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cme911-html-1a5bf05b4e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cme911.html
retrieved_at: 2026-08-21T07:23:19.125994+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Enhanced 911 Services

## Chapter: Enhanced 911 Services

# Enhanced 911 Services

## Prerequisites for
                        	 Enhanced 911 Services

SCCP or SIP
                                 			 phones must be registered to Cisco Unified CME.

At least one
                                 			 CAMA or ISDN trunk must be configured from Cisco Unified CME to each of the 911
                                 			 service provider’s public safety answering point (PSAP).

An Enhanced 911
                                 			 network must be designed for each customer’s voice network.

Cisco Unified CME has an FXS, FXO, SIP, or H.323 trunk interface
                                 			 configured.

Cisco Unified CME

Cisco Unified CME  4.2 or a later version.

Cisco Unified CME
                              		  in SRST Fallback Mode

Cisco Unified CME  4.1 or a later version, configured in SRST
                                 			 fallback mode. See SRST Fallback Mode .

## Restrictions for
                        	 Enhanced 911 Services

Enhanced 911
                                 			 Services for Cisco Unified CME does not interface with the
                                 			 Cisco Emergency Responder.

The information
                                 			 about the most recent phone that called 911 is not preserved after a reboot of
                                 			 Cisco Unified CME.

Cisco Emergency Responder does not have access to any updates
                                 			 made to the emergency call history table when remote Cisco Unified IP phones
                                 			 are in SRST fallback mode. Therefore, if the PSAP calls back after the IP
                                 			 phones register back to Cisco Unified Communications Manager,
                                 			 Cisco Emergency Responder has no history of those calls. As a result, those
                                 			 calls are not routed to the original 911 caller. Instead, the calls are routed
                                 			 to the default destination that is configured on Cisco Emergency Responder for
                                 			 the corresponding ELIN.

For Cisco
                                 			 Unified Wireless 7920 and 7921 IP phones, a caller’s location can only be
                                 			 determined by the static information configured by the system administrator.
                                 			 For more information, see Precautions for Mobile Phones .

The extension
                                 			 numbers of 911 callers can be translated to only two emergency location
                                 			 identification numbers (ELINs) for each emergency response location (ERL). For
                                 			 more information, see Overview of Enhanced 911 Services .

Using ELINs for
                                 			 multiple purposes can result in unexpected interactions with existing
                                 			 Cisco Unified CME features. These multiple uses of an ELIN can include
                                 			 configuring an ELIN for use as an actual phone number (ephone-dn, voice
                                 			 register dn, or FXS destination-pattern), a Call Pickup number, or an alias
                                 			 rerouting number. For more information, see Multiple Usages of an ELIN .

Your
                                 			 configuration of Enhanced 911 Services can interact with existing
                                 			 Cisco Unified CME features and cause unexpected behavior. For a complete
                                 			 description of interactions between Enhanced 911 Services and existing
                                 			 Cisco Unified CME features, see Interactions with Existing Cisco Unified CME Features .

## Information About
                        	 Enhanced 911 Services

### Overview of
                           	 Enhanced 911 Services

Enhanced 911
                              		Services enable 911 operators to:

Immediately
                                    			 pinpoint the location of the 911 caller based on the calling number

Callback the 911
                                    			 caller if a disconnect occurs

Before this feature
                              		was introduced, Cisco Unified CME supported only outbound calls to 911. With
                              		basic 911 functionality, calls were simply routed to a public safety answering
                              		point (PSAP). The 911 operator at the PSAP then had to verbally gather the
                              		emergency information and location from the caller, before dispatching a
                              		response team from the ambulance service, fire department, or police
                              		department. Calls could not be routed to different PSAPs, based on the specific
                              		geographic areas that they cover.

With Enhanced 911
                              		Services, 911 calls are selectively routed to the closest PSAP based on the
                              		caller’s location. In addition, the caller’s phone number and address
                              		automatically display on a terminal at the PSAP. Therefore, the PSAP can
                              		quickly dispatch emergency help, even if the caller is unable to communicate
                              		the location. Also, if the caller disconnects prematurely, the PSAP has the
                              		information it needs to contact the 911 caller.

To use Enhanced 911
                              		Services, you must define an emergency response location (ERL) for each of the
                              		geographic areas needed to cover all of the phones supported by
                              		Cisco Unified CME. The geographic specifications for ERLs are determined by
                              		local law. For example, you might have to define an ERL for each floor of a
                              		building because an ERL must be less than 7000 square feet in area. Because the
                              		ERL defines a known, specific location, this information is uploaded to the
                              		PSAP’s database and is used by the 911 dispatcher to help the emergency
                              		response team to quickly locate a caller.

To determine which
                              		ERL is assigned to a 911 caller, the PSAP uses the caller’s unique phone
                              		number, which is also known as the emergency location identification number
                              		(ELIN). Before you can use Enhanced 911 Services you must supply the PSAP with
                              		a list of your ELINs and street addresses for each ERL. This information is
                              		saved in the PSAP’s automatic location identification (ALI) database.
                              		Typically, you give this information to the PSAP when your phone system is
                              		installed.

With the address
                              		information in the ALI database, the PSAP can find the caller’s location and
                              		can also use the ELIN to callback the 911 caller within a specified time limit.
                              		This limit applies to the Last Caller table, which provides the PSAP with the
                              		911 caller’s ELIN. If no time limit is specified for the Last Caller table, the
                              		default expiry time is three hours.

In addition to
                              		saving call formation in the temporary Last Caller table, you can configure
                              		permanent call detail records. You can view the attributes in these records
                              		from RADIUS accounting, the syslog service, or Cisco IOS show commands.

You have the option
                              		of configuring zero, one, or two ELINs for each ERL. If you configure two
                              		ELINs, the system uses a round-robin algorithm to select which ELIN is sent to
                              		the PSAP. If you do not define an ELIN for an ERL, the PSAP sees the original
                              		calling number. You may not want to define an ELIN if Cisco Unified CME is
                              		using direct-inward-dial numbers or the call is from another Cisco voice
                              		gateway that has already translated the extension to an ELIN.

Optionally define a
                              		default ELIN that the PSAP can use if a 911 caller's IP phone's address does
                              		not match the IP subnet of any location in any zone. This default ELIN can be
                              		an existing ELIN that is already defined for one of the ERLs or it can be a
                              		unique ELIN. If no default ELIN is defined and the 911 caller’s IP Address does
                              		not match any of the ERLs’ IP subnets, a syslog message is issued stating that
                              		no default ELIN is defined, and the original ANI remains intact.

You can also define
                              		a designated callback number that is used when the callback information is lost
                              		in the Last Caller table because of an expiry timeout or system restart. You
                              		can use this designated callback number if the PSAP cannot reach the 911 caller
                              		at the caller’s ELIN or the default ELIN for any other reason. You can further
                              		customize your system by specifying the expiry time for data in the Last Caller
                              		table and by enabling syslog messages that announce all emergency calls.

For large
                              		installations, you can optionally specify that calls from specific ERLs are
                              		routed to specific PSAPs. This is done by configuring emergency response zones,
                              		which lists the ERLs within each zone. This list of ERLs also includes a
                              		ranking of the locations which controls the order of ERL searches when there
                              		are multiple PSAPs. You do not need to configure emergency response zones if
                              		all 911 calls on your system are routed to a single PSAP.

One or more ERLs can
                              		be grouped into a zone which could be equivalent to the area serviced by a
                              		PSAP. When an outbound emergency call is placed, configured emergency response
                              		zones allow the searching of a subset of the ERLs in any order. The ERLs can be
                              		ranked in the order of desired usage.

Zones are also used
                              		to selectively route 911 calls to different PSAPs.You can configure selective
                              		routing by creating a zone with a list of unique locations and assigning each
                              		zone to a different outbound dial peer. In this case, zones route the call
                              		based on the caller’s ERL. When an emergency call is made, each dial peer
                              		matching the called number uses the zone’s list of locations to find a matching
                              		IP subnet to the calling phone’s IP address. If an ERL and ELIN are found, the
                              		dial peer’s interface is used to route the call. If no ERL or ELIN is found,
                              		the next matched dial peer checks its zone.

If a caller’s
                                                				IP address does not match any location in its dial-peers zone, the last dial
                                                				peer that matched is used for routing and the default ELIN is used.

If you want
                                                				911 calls from any particular phone to always use the same dial peer when you
                                                				have multiple dial peers going to the same destination-pattern (911) and the
                                                				zones are different, you must configure the preferred dial peer to be the
                                                				highest priority by setting the preference field.

Duplicate location
                              		tags are not allowed in the same zone. However, the same location tag can be
                              		defined in multiple zones. You are allowed to enter duplicate location
                              		priorities in the same zone, however, the existing location’s priority is then
                              		increased to the next number. For example, if you configure “location 36
                              		priority 5” followed by “location 19 priority 5,” location 19 has priority 5
                              		and location 36 becomes priority 6. Also, if two locations are assigned
                              		priority 100, rather than bump the first location to priority 101, the first
                              		location becomes the first nonprioritized location.

Implementation
                                 		  of Enhanced 911 for Cisco Unified CME shows an example configuration for 911 services. In this example, the phone
                              		system handles calls from multiple floors in multiple buildings. Five ERLs are
                              		defined, with one ELIN defined for each ERL. At the PSAP, the ELIN is used to
                              		find the caller’s physical address from the ALI database. Building 2 is closer
                              		to the PSAP in San Francisco and Building 40 is closer to the PSAP in San Jose.
                              		Therefore, in this case, we recommend that you configure two emergency response
                              		zones to ensure that 911 calls are routed to the PSAP closest to the caller. In
                              		this example, you can configure an emergency response zone that includes all of
                              		the ERLS in building 2 and another zone that includes the ERLs in building 40.
                              		If you choose to not configure emergency response zones, 911 calls are routed
                              		based on matching the destination number configured for the outgoing dial
                              		peers.

### Call Processing
                           	 for E911 Services

When a 911 call is
                              		received by Cisco Unified CME, the initial call processing is the same as for
                              		any other call. Cisco Unified CME takes the called-number and searches for dial
                              		peers that can be used to route the call to that called-number.

The Enhanced 911
                              		feature also analyzes the outgoing dial peer to see if it is going to a PSAP.
                              		If the outgoing dial peer is configured with the emergency response
                                    			 zone command, the system is notified that the call needs Enhanced
                              		911 handling. If the outgoing dial peer is not configured with the emergency response
                                    			 zone command, the Enhanced 911 functionality is not activated and
                              		the caller’s number is not translated to an ELIN.

When the
                              		Enhanced 911 functionality is activated, the first step in Enhanced 911
                              		handling is to determine which ERL is assigned to the caller. There are two
                              		ways to determine the caller’s ERL.

Explicit
                                    			 Assignment—If a 911 call arrives on an inbound dial peer that has an ERL
                                    			 assignment, this ERL is automatically used as the caller’s location.

Implicit
                                    			 Assignment—If a 911 call arrives from an IP phone, its IP address is determined
                                    			 and Enhanced 911 searches for the IP address of the caller’s phone in one of
                                    			 the IP subnets configured in the ERLs. The ERLs are stored as an ordered list
                                    			 according to their tag numbers, and each subnet is compared to the caller’s IP
                                    			 address in the order listed.

After the caller’s
                              		ERL is determined, the caller’s number is translated to that ERL’s ELIN. If no
                              		ERLs are implicitly or explicitly assigned to a call, you can define a default
                              		ERL for IP phones. This default ERL does not apply to nonIP-phone endpoints,
                              		such as phones on VoIP trunks or FXS/FXO trunks.

After an ELIN is
                              		determined for the call, the following information is saved to the Last Caller
                              		table:

Caller’s ELIN

Caller’s
                                    			 original extension

Time the call
                                    			 originated

The Last Caller
                              		table contains this information for the most recent emergency callers from each
                              		ERL. A caller’s information is purged from the table when the specified expiry
                              		time has passed after the call was originated. If no time limit is specified,
                              		the default expiry time is three hours.

After the 911 call
                              		information is saved to the Last Caller table, the system determines whether an
                              		emergency response zone is configured that contains the caller’s ERL. If no
                              		emergency response zone is configured with the ERL, all ERLs are searched
                              		sequentially to match the caller’s IP address and then route the 911 call to
                              		the appropriate PSAP. If an ERL is included in a zone, the 911 call is routed
                              		to the PSAP associated with that zone.

After the 911 call
                              		is routed to appropriate PSAP, Enhanced 911 processing is complete. Call
                              		processing then proceeds as it does for basic calls, except that the ELIN
                              		replaces the original calling number for the outbound setup request.

Processing a
                                 		  911 Call summarizes the procedure for processing a 911 call.

The 911 operator is
                              		unable to find information about a call in the Last Caller table if the router
                              		was rebooted or specified expiry time (three hours by default) has passed after
                              		the call was originated. If this is the case, the 911 operator hears the
                              		reorder tone. To prevent the 911 operator from getting this tone, you can
                              		configure the default callback as described in Customize E911 Settings .
                              		Alternately, you can configure a call forward number on the dial peer that goes
                              		to an operator or primary contact at the business.

Because the 911
                              		callback feature tracks the last caller by its extension number, if you change
                              		the configuration of your ephone-dns in-between a 911 call and a 911 callback
                              		and within the expiry time, the PSAP might not be able to successfully contact
                              		the last 911 caller.

If two 911 calls are
                              		made from different phones in the same ERL within a short period of time, the
                              		first caller’s information is overwritten in the Last Caller table with the
                              		information for the second caller. Because the table can contain information
                              		about only one caller from each ERL, the 911 operator does not have the
                              		information needed to contact the first caller.

In most cases, if
                              		Cisco Emergency Responder is configured, you should configure
                              		Enhanced 911 Services with the same data for the ELIN and ERL as used by Cisco
                              		Emergency Responder.

### Precautions for Mobile Phones

Emergency calls placed from phones that have been removed from their
                              		primary site might not be answered by local safety authorities. IP phones
                              		should not be used to place emergency calls if removed from the site where it
                              		was initially configured. Therefore, we recommend that you require your mobile
                              		phone users to agree to a policy similar to the one stated below.

Telecommuters, remote office, and traveling personnel must place
                              		emergency calls on a locally configured hotel, office, or home phone (in other
                              		words, their landline). If they must use a remote IP phone for emergency calls
                              		while away from their configured site, they must be prepared to provide
                              		specific information regarding their location (their country, city, state,
                              		street address, and so on) to the answering safety authority or security
                              		operations center personnel.

By accepting this policy your mobile phone users are confirming that
                              		they:

Understand this advisory

Agree to take reasonable precautions to prevent use of any remote IP
                                    			 phone device for emergency calls when it is removed from its configured site

By not responding to or declining to accept this policy, your mobile
                              		phone users are confirming that they understand that all remote IP phone
                              		devices associated with them will be disconnected, and no future requests for
                              		these services will be fulfilled.

### Plan Your
                           	 Implementation of Enhanced 911 Services

Before you
                                 		  configure Enhanced 911 Services for Cisco Unified CME:

Step 1

Make a list
                                          			 of your sites that are serviced by Cisco Unified CME, and the PSAPs serving
                                          			 each site.

Be aware that
                                             				you must use a CAMA/PRI interface to connect to each PSAP. Table 1 shows an example of the information that you need to gather.

Building Name and Address

Responsible PSAP

Interface to which Calls Are Routed

Building 2, 201 Maple Street, San Francisco

San
                                                         						  Francisco, CA

Port
                                                         						  1/0:D

Building 40, 801 Main Street, San Jose

San
                                                         						  Jose, CA

Port
                                                         						  1/1:D

Step 2

Use local laws
                                          			 to determine the number of ERLs you need to configure.

According to
                                             				the National Emergency Number Association (NENA) model legislation, make the
                                             				location specific enough to provide a reasonable opportunity for the emergency
                                             				response team to quickly locate a caller anywhere within it. Table 2 shows an example.

Building

Size
                                                            						  in Square Feet

Number
                                                            						  of Floors

Number
                                                            						  of ERLs Required

Building 2

200,000

3

3

Building 40

7000

2

1

Step 3

(Optional)
                                          			 Assign one or two ELINs to each ERL.

You must
                                             				contact your phone service provider to request phone numbers that are
                                             				designated as ELINs.

Step 4

(Optional)
                                          			 Assign each of your ERLs to an emergency response zone to enable 911 calls to
                                          			 be routed to the PSAP that is closest to the caller. Use the voice emergency response
                                                				  zone command.

Step 5

Configure one
                                          			 or more dial peers for your 911 callers with the emergency response
                                                				  zone command.

You might need
                                             				to configure multiple dial peers for different destination-patterns.

Step 6

Configure one
                                          			 or more dial peers for the PSAP’s 911 callbacks with the emergency response
                                                				  callback command.

Step 7

Decide what
                                          			 method to use to assign ERLs to phones.

You have the
                                             				following choices:

For a
                                                   					 group of phones that are on the same subnet, you can create an IP subnet in the
                                                   					 ERL that includes each phone’s IP address. Each ERL can have one or two unique
                                                   					 IP subnets. This is the easiest option to configure. Table 3 shows an example.

ERL
                                                            						  Number

Description

IP
                                                            						  Address Assignment

ELIN

1

Building 2, 1st floor

10.5.124.xxx

408
                                                            						  555-0142

2

Building 2, 2nd floor

10.7.xxx.xxx

408
                                                            						  555-0143

3
                                                            						  & 4

Building 2, 3rd floor

10.8.xxx.xxx and 10.9.xxx.xxx

408
                                                            						  555-0144 and 408 555-0145

You can
                                                   					 assign an ERL explicitly to a group of phones by using the ephone-template or
                                                   					 voice register template configurations. Instead of assigning an ERL to phones
                                                   					 individually, you can use these templates to save time if you want to apply the
                                                   					 same set of features to several SCCP phones or SIP phones.

You can
                                                   					 assign an ERL to a phone individually. Depending on which type of phone you
                                                   					 have, you can use one of three methods. You can assign an ERL to a phone’s:

Dial-peer configuration

Ephone configuration (SCCP phones)

Voice register pool configuration (SIP phones)

Table 4 shows examples of each of these options.

Phone Configuration

ERL

Dial-peer voice 213 pots

3

Dial-peer voice 214 voip

4

Ephone 100

3

Voice register pool 1

2

Step 8

(Optional)
                                          			 Define a default ELIN to be sent to the PSAP for use if a 911 caller's IP
                                          			 phone's address does not match the IP subnet of any location in any zone.

Step 9

(Optional)
                                          			 Define a designated callback number that is used if the callback information is
                                          			 removed from the Last Caller table because of an expiry timeout or system
                                          			 restart.

Step 10

(Optional)
                                          			 Change the expiry time for data in the Last Caller table from the default time
                                          			 of three hours.

Step 11

(Optional)
                                          			 Enable RADIUS accounting or the syslog service to permanently record call
                                          			 detail records.

### Interactions with Existing Cisco Unified CME Features

Enhanced 911 Services interacts with several Cisco Unified CME features.
                              		The interactions with each of the following features are described in separate
                              		sections below:

Your version of Cisco Unified CME may not support all of these
                                          		  features.

#### Multiple Usages of an ELIN

We recommend that you do not use ELINs for any other purpose because
                                             		  of possible unexpected interactions with existing Cisco Unified CME features.

Examples of using ELINs for other purposes include configuring an ELIN
                                 		for use as an actual phone number (ephone-dn, voice register dn, FXS
                                 		destination-pattern), a Call Pickup number, or an alias rerouting number.

Using ELINs as an actual phone number causes problems when calls are
                                 		made to that number. If a 911 call occurs and the last caller information has
                                 		not expired from the Last Caller table, any outside callers will reach the last
                                 		911 caller instead of the actual phone. We recommend that you do not share the
                                 		phone numbers used for ELINs with real phones.

There is no impact on outbound 911 calls if you use the same number for
                                 		an ELIN and a real phone number.

#### Number Translation

The Enhanced 911 feature translates the calling number to an ELIN during
                                 		an outbound 911 call, and translates the called-number to the last caller’s
                                 		extension during a 911 callback (when the PSAP makes a callback to the 911
                                 		caller). Alternative methods of number translation can conflict with the
                                 		translation done by the Enhanced 911 software, such as:

Dialplan-pattern—Prefixes a pattern to an extension configured under
                                       			 telephony-service

Num-expansion—Expands extensions to full E.164 numbers

Voice-port translation of called and calling numbers

Outgoing number translation for dial peers

Translate-profile for dial peers

Voice translation profiles done for the dial peer, voice-port, POTS
                                       			 voice service, trunk group, trunk group member, voice source-group,
                                       			 call-manager-fallback, and ephone-dn

Ephone-dn translation

Voice register dn’s outgoing translation

Configuring these translation features impacts the Enhanced 911 feature
                                 		if they translate patterns that are part of your ELINs’ patterns. For an
                                 		outgoing 911 call, these features might translate an Enhanced 911 ELIN to a
                                 		different number, giving the PSAP a number they cannot look-up in their ALI
                                 		databases. If the 911 callback number (ELIN) is translated before Enhanced 911
                                 		callback processing, the Enhanced 911 feature is unable to find the last
                                 		caller’s history.

#### Call Transfer

If a phone in a Cisco Unified CME environment performs a semi attended
                                 		or consultative transfer to the PSAP that involves another phone that is in a
                                 		different ERL, the PSAP will use the wrong ELIN. The PSAP will see the ELIN of
                                 		the transferor party, not the transferred party.

There is no impact on 911 callbacks (calls made by the PSAP back to a
                                 		911 caller) or transfers that are made by the PSAP.

A 911 caller can transfer the PSAP to another party if there is a valid
                                 		reason to do so. Otherwise, we recommend that the 911 caller remain connected
                                 		to the PSAP at all times.

#### Call Forward

There is no impact if an IP phone user calls another phone that is
                                 		configured to forward calls to the PSAP.

If the PSAP makes a callback to a 911 caller that is using a phone that
                                 		has Call Forward enabled, the PSAP is redirected to a party that is not the
                                 		original 911 caller.

#### Call Blocking Features

Outbound 911 calls can be blocked by features such as After-Hours Call
                                 		Blocking if the system administrator does not create an exception to 911 calls.

911 callbacks will not reach the 911 caller if the phone is configured
                                 		with a blocking feature (for example, Do Not Disturb).

#### Call Waiting

After a 911 call is established with a PSAP, call waiting can interrupt
                                 		the call. The 911 caller has the choice of putting the operator on hold.
                                 		Although holding is not prohibited, we recommend that the 911 caller remain
                                 		connected to the PSAP until the call is over.

#### Three-Way Conference

Although the 911 caller is allowed to activate three-way conferencing
                                 		when talking to the PSAP, we recommend that the 911 caller remain connected
                                 		privately to the PSAP until the call is over.

#### Dial-Peer Rotary

If a 911 caller uses a rotary phone, you must configure each dial peer
                                 		with the emergency response zone command for the call to be processed as an Enhanced 911
                                 		call. Otherwise, calls received on dial peers that are not configured for
                                 		Enhanced 911 functionality are treated as regular calls and there is no ELIN
                                 		translation.

Do not configure two dial peers with the same destination-pattern to
                                 		route to different PSAPs. The caller’s number will not be translated to two
                                 		different ELINs and the two dial peers will not route to different PSAPs.
                                 		However, you can route calls to different PSAPs if you configure the dial peers
                                 		with different destination-patterns (for example, 9911 and 95105558911). You
                                 		might need to use the number translation feature or add prefix/forward-digits
                                 		to change the 95105558911 to 9911 for the second dial peer if a specific
                                 		called-number is required by the service provider.

Caution

We recommend that you do not configure the same dial peer using both
                                             		  the emergency response zone and emergency response callback commands.

#### Dial Plan Patterns

Dial plan patterns expand the caller’s original extension number into a
                                 		fully qualified E.164 number. If an ERL is found for a 911 caller, the expanded
                                 		number is translated to an ELIN.

For 911 callbacks, the called-number is translated to the 911 caller’s
                                 		expanded number.

#### Caller ID Blocking

When you set Caller ID Blocking for an ephone or voice-port
                                 		configuration, the far-end gateway device blocks the display of the calling
                                 		party information. This feature is overridden when an Enhanced 911 call is
                                 		placed because the PSAP must receive the ELIN (the calling party information).

The Caller ID Blocking feature does not impact callbacks.

#### Shared Line

The Shared Line feature allows multiple phones to share a common
                                 		directory number. When a shared line receives an incoming call, each phone
                                 		rings. Only the first user that answers the call is connected to the caller.

The Shared Line feature does not affect outbound 911 calls.

For 911 callbacks, all phones sharing the directory number will ring.
                                 		Therefore, someone who did not originate the 911 call might answer the phone
                                 		and get connected to the PSAP. This could cause confusion if the PSAP needs to
                                 		talk only with the 911 caller.

## Configure Enhanced 911 Services

### Configure the
                           	 Emergency Response Location

Perform this
                                 		  procedure to create the ERL. The ERL defines an area that allows emergency
                                 		  teams to quickly locate a caller.

The ERL can define
                                 		  zero, one, or two ELINs. If one ELIN is defined, this ELIN is always used for
                                 		  phones calling from this ERL. If you define two ELINs, the system alternates
                                 		  using each ELIN for phones calling from this ERL. If you define no ELINs and
                                 		  phones use this ERL, the outbound calls do not have their calling numbers
                                 		  translated. The PSAP sees the original calling numbers for these 911 calls.

If multiple ERLs
                                 		  are created, the Enhanced 911 software uses the ERL tag number to determine
                                 		  which ELIN to use. The Enhanced 911 software searches the ERLs sequentially
                                 		  from tag 1 to 2147483647. The first ERL that has a subnet mask encompassing the
                                 		  caller's IP address is used for ELIN translation.

#### Before you begin

Cisco Unified
                                       				CME 4.1 or a later version.

The address and name commands
                                       				are supported in Cisco Unified CME 4.2 and later versions.

Plan your 911
                                       				configuration as described in Plan Your Implementation of Enhanced 911 Services

### SUMMARY STEPS

- enable

- configure terminal

- voice emergency response location tag

- elin [ 1 | 2 ] E.164-number

- address address

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

voice emergency response location tag

#### Example:

```
Router(config)# voice emergency response location 4
```

Enters
                                             				emergency response location configuration mode to define parameters for an ERL.

Step 4

elin [ 1 | 2 ] E.164-number

#### Example:

```
Router(cfg-emrgncy-resp-location)# elin 14085550100
```

This number is displayed on the PSAP’s terminal and is used by
                                                      					 the PSAP to query the ALI database to locate the caller. It is also used by the
                                                      					 PSAP for callbacks. You can define a second ELIN using the optional elin 2
                                                      					 command. If an ELIN is not defined for the ERL, the PSAP sees the original
                                                      					 calling number.

Step 5

address address

#### Example:

```
Router(cfg-emrgncy-resp-location)# address I,604,5550100, ,184 ,Main St,Kansas City,KS,1,
```

(Optional) Defines a comma-separated string used for the automatic
                                             				location identification (ALI) database upload of the caller’s address.

String must conform to the record format that is required by
                                                   					 the service provider. The string maximum is 247 characters.

Address is saved as part of the E911 ERL configuration. When
                                                   					 used with the show voice emergency addresses command, the address
                                                   					 information can be saved to a text file.

This command is supported in Cisco Unified CME 4.2 and later
                                                   					 versions.

Step 6

name name

#### Example:

```
Router(cfg-emrgncy-resp-location)# name Bldg C, Floor 2
```

(Optional) Defines a 30-character string used internally to
                                             				identify or describe the emergency response location.

This command is supported in Cisco Unified CME 4.2 and later
                                                   					 versions.

Step 7

end

#### Example:

```
Router(cfg-emrgncy-resp-location)# end
```

Returns to
                                             				privileged EXEC mode.

### Configure
                           	 Locations under Emergency Response Zones

In the
                                 		  configuration of emergency response zones, a list of locations within a zone is
                                 		  created using location tags. The zone configuration allows a ranking of the
                                 		  locations which controls the order of ERL searches when there are multiple
                                 		  PSAPs. The zone command is not used if all 911 calls on the system are
                                 		  routed to a single PSAP.

#### Before you begin

Cisco Unified
                                       				CME 4.2 or a later version

Define your
                                       				ERLs as described in Configure the Emergency Response Location .

### SUMMARY STEPS

- enable

- configure terminal

- voice emergency response zone tag

- location location-tag [ priority number ]

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

voice emergency response zone tag

#### Example:

```
Router(config)# voice emergency response zone 10
```

Enters voice
                                             				emergency response zone configuration mode to define parameters for an
                                             				emergency response zone.

tag —Range is 1-100.

Step 4

location location-tag [ priority number ]

#### Example:

```
Router(cfg-emrgncy-resp-zone)# location 8 priority 2
```

Each location
                                             				tag must correspond to a location tag created using the voice emergency response
                                                   					 location command.

number —(optional) Ranks the location in the zone
                                                   					 list. Range is 1-100, with 1 being the highest priority.

Repeat
                                                   					 this command for each location included in the zone.

Step 5

end

#### Example:

```
Router(cfg-emrgncy-resp-zone)# end
```

Returns to
                                             				privileged EXEC mode.

### Configure Outgoing
                           	 Dial Peers for Enhanced 911 Services

Depending on whether
                              		you decided to configure emergency response zones while you planned your 911
                              		configuration as described in Plan Your Implementation of Enhanced 911 Services ,
                              		use one of the following procedures:

If you decided
                                    			 to not use zones, see Configure Dial Peers for Emergency Calls .

If you decided
                                    			 to use zones, see Configure Dial Peers for Emergency Response Zones .

#### Configure Dial
                              	 Peers for Emergency Calls

Perform this
                                    		  procedure to create a dial peer for emergency calls to the PSAP. The
                                    		  destination-pattern of this dial peer is usually some variation of 911, such as
                                    		  9911. This dial peer uses the port number of the CAMA or PRI network interface
                                    		  card. The new command emergency response
                                          				zone specifies that this dial peer translates the calling number
                                    		  of any outgoing call’s to an ELIN.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice number pots

- destination-pattern n 911

- prefix number

- emergency response zone

- end

### DETAILED STEPS

Step 1

enable

##### Example:

```
Router> enable
```

Enables
                                                				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global
                                                				configuration mode.

Step 3

dial-peer voice number pots

##### Example:

```
Router(config)# dial-peer voice 911 pots
```

Enters
                                                				dial-peer configuration mode to define parameters for an individual dial peer.

Step 4

destination-pattern n 911

##### Example:

```
Router(config-dial-peer)# destination-pattern 9911
```

Matches dialed
                                                				digits to a telephony device. The digits included in this command specify the
                                                				E.164 or private dialing plan telephone number. For Enhanced 911 Services, the
                                                				digits are usually some variation of 911.

Step 5

prefix number

##### Example:

```
Router(config-dial-peer)# prefix 911
```

(Optional)
                                                				Includes a prefix that the system adds automatically to the front of the dial
                                                				string before passing it to the telephony interface. For Enhanced 911 Services,
                                                				the dial string is some variation of 911.

Step 6

emergency response zone

##### Example:

```
Router(config-dial-peer)# emergency response zone
```

Defines this
                                                				dial peer as the one to use to route all ERLs defined in the system to the
                                                				PSAP.

Step 7

end

##### Example:

```
Router(config-dial-peer)# end
```

Returns to
                                                				privileged EXEC mode.

#### Configure Dial
                              	 Peers for Emergency Response Zones

You can
                                    		  selectively route a 911 call based on the ERL by assigning different zones to
                                    		  dial peers. The emergency response
                                          				zone command identifies the dial peer that routes the 911 call
                                    		  and the voice interface to use. Only ERLs that are defined in the zone can be
                                    		  routed on the dial peer. Callers dialing the same emergency number are routed
                                    		  to different voice interfaces based on the zone of the ERL.

##### Before you begin

Cisco Unified
                                          				CME 4.2 or a later version

Define your
                                          				ERLs and emergency response zones as described in:

Configure the Emergency Response Location

Configure Locations under Emergency Response Zones

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice number pots

- destination-pattern n 911

- prefix number

- emergency response zone tag

- end

### DETAILED STEPS

Step 1

enable

##### Example:

```
Router> enable
```

Enables
                                                				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global
                                                				configuration mode.

Step 3

dial-peer voice number pots

##### Example:

```
Router(config)# dial-peer voice 911 pots
```

Enters
                                                				dial-peer configuration mode to define parameters for an individual dial peer.

Step 4

destination-pattern n 911

##### Example:

```
Router(config-dial-peer)# destination-pattern 9911
```

Matches dialed
                                                				digits to a telephony device. The digits included in this command specify the
                                                				E.164 or private dialing plan telephone number. For E911 services, the digits
                                                				are usually some variation of 911.

Step 5

prefix number

##### Example:

```
Router(config-dial-peer)# prefix 911
```

(Optional)
                                                				Includes a prefix that the system adds automatically to the front of the dial
                                                				string before passing it to the telephony interface. For E911 services, the
                                                				dial string is some variation of 911.

Step 6

emergency response zone tag

##### Example:

```
Router(config-dial-peer)# emergency response zone 10
```

Defines this
                                                				dial peer as the one that is used to route ERLs defined for that zone.

tag —Points to an existing configured zone. Range
                                                      					 is 1-100.

Step 7

end

##### Example:

```
Router(config-dial-peer)# end
```

Returns to
                                                				privileged EXEC mode.

### Configure a Dial
                           	 Peer for Callbacks from the PSAP

Perform this
                                 		  procedure to create a dial peer for 911 callbacks from the PSAP. This dial peer
                                 		  enables the PSAP to use the ELIN to make callbacks. When a call arrives that
                                 		  matches this dial peer, the emergency response callback command instructs the system to find the last caller
                                 		  that used the ELIN and translate the destination number of the incoming call to
                                 		  the extension of the last caller.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice number pots

- incoming called-number number

- direct-inward-dial

- emergency response callback

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

dial-peer voice number pots

#### Example:

```
Router(config)# dial-peer voice 100 pots
```

Enters
                                             				dial-peer configuration mode to define parameters for an individual dial peer.

Step 4

incoming called-number number

#### Example:

```
Router(config-dial-peer)# incoming called-number 4085550100
```

(Optional)
                                             				Selects the inbound dial peer based on the called number to identify the last
                                             				caller. This number is the ELIN.

Step 5

direct-inward-dial

#### Example:

```
Router(config-dial-peer)# direct-inward-dial
```

(Optional) Enables the Direct Inward Dialing (DID) call
                                             				treatment for the incoming called number. For more information, see the chapter Configuring Voice Ports in the Cisco Voice, Video, and Fax
                                                				  Configuration Guide .

Step 6

emergency response callback

#### Example:

```
Router(config-dial-peer)# emergency response callback
```

Identifies a
                                             				dial peer as an ELIN dial peer.

Step 7

end

#### Example:

```
Router(config-dial-peer)# end
```

Returns to
                                             				privileged EXEC mode.

### Assign ERLs to
                           	 Phones

You must specify an
                              		ERL for each phone. The type of phones that you have determines which of the
                              		following tasks you use to associate an ERL with your phones, as explained in Step 7 in Plan Your Implementation of Enhanced 911 Services .

To create an IP
                                    			 subnet in the ERL that includes each phone’s IP address, you must also
                                    			 configure each ERL to specify which phones are part of the ERL. See Assign an ERL to a Phone’s IP Subnet .
                                    			 You can optionally specify up to two different subnets.

To assign an ERL
                                    			 to a SIP phone, you must specify the ERL in the voice register pool
                                    			 configuration. See Assign an ERL to a SIP Phone .

To assign an ERL
                                    			 to a SCCP phone, you must specify the ERL in the ephone configuration. See Assign an ERL to a SCCP Phone .

To assign an ERL
                                    			 to a phone’s dial peer, you must specify the ERL in the dial-peer
                                    			 configuration. See Assign an ERL to a Dial Peer .

#### Prerequisites for
                              	 Assigning ERLs to Phones

Define your ERLs and emergency response zones as described in the Configure the Emergency Response Location .

#### Assign an ERL to a
                              	 Phone’s IP Subnet

Use this procedure
                                    		  when you have a group of phones that are on the same subnet. You can configure
                                    		  an ERL to be associated with one or two unique IP subnets. This indicates that
                                    		  all IP phones in a specific subnet use the ELIN defined in this ERL.

### SUMMARY STEPS

- enable

- configure terminal

- voice emergency response location tag

- subnet [ 1 | 2 ] IPaddress-mask

- end

### DETAILED STEPS

Step 1

enable

##### Example:

```
Router> enable
```

Enables
                                                				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global
                                                				configuration mode.

Step 3

voice emergency response location tag

##### Example:

```
Router(config)# voice emergency response location 4
```

Enters
                                                				emergency response location configuration mode to define parameters for an ERL.

Step 4

subnet [ 1 | 2 ] IPaddress-mask

##### Example:

```
Router(cfg-emrgncy-resp-location)# subnet 1 192.168.0.0 255.255.0.0
```

Defines the
                                                				groups of IP phones that are part of this location. You can create up to 2
                                                				different subnets.

To include
                                                      					 all IP phones on a single ERL, use the command subnet 1 0.0.0.0 0.0.0.0 to configure a default subnet.
                                                      					 This subnet does not apply to nonIP-phone endpoints, such as phones on VoIP
                                                      					 trunks or FXS/FXO trunks.

Step 5

end

##### Example:

```
Router(cfg-emrgncy-resp-location)# end
```

Returns to
                                                				privileged EXEC mode.

#### Assign an ERL to a
                              	 SIP Phone

Perform this
                                    		  procedure if you chose to assign a specific ERL to a SIP phone instead of using
                                    		  the phone’s IP address to match a subnet defined for an ERL. For more
                                    		  information about this decision, see Step 7 in Plan Your Implementation of Enhanced 911 Services .

### SUMMARY STEPS

- enable

- configure terminal

- voice register pool tag

- emergency response location tag

- end

### DETAILED STEPS

Step 1

enable

##### Example:

```
Router> enable
```

Enables
                                                				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global
                                                				configuration mode.

Step 3

voice register pool tag

##### Example:

```
Router(config)# voice register pool 8
```

Enters voice
                                                				register pool mode to define parameters for an individual voice register pool.

Step 4

emergency response location tag

##### Example:

```
Router(config-register-pool)# emergency response location 12
```

Assigns an ERL
                                                				to a phone s voice register pool using an ERL s tag.

tag —Range is 1 to 2147483647.

If the
                                                      					 ERL's tag is not a configured tag, the phone is not associated to an ERL and
                                                      					 the phone defaults to its IP address to find the inclusive ERL subnet.

This
                                                      					 command can also be configured in voice register template configuration mode
                                                      					 and applied to one or more phones. The voice register pool configuration has
                                                      					 priority over the voice register template configuration.

Step 5

end

##### Example:

```
Router(config-register-pool)# end
```

Returns to
                                                				privileged EXEC mode.

#### Assign an ERL to a
                              	 SCCP Phone

Perform this
                                    		  procedure if you chose to assign an ERL to a SCCP phone instead of configuring
                                    		  an ERL to be associated with IP subnets. For more information about this
                                    		  decision, see Step 7 in Plan Your Implementation of Enhanced 911 Services .

### SUMMARY STEPS

- enable

- configure terminal

- ephone tag

- emergency response location tag

- end

### DETAILED STEPS

Step 1

enable

##### Example:

```
Router> enable
```

Enables
                                                				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global
                                                				configuration mode.

Step 3

ephone tag

##### Example:

```
Router(config)# ephone 224
```

Enters ephone
                                                				configuration mode to define parameters for an individual ephone.

Step 4

emergency response location tag

##### Example:

```
Router(config-ephone)# emergency response location 12
```

Assigns an ERL
                                                				to a phone s ephone configuration using an ERL s tag.

tag —Range is 1 to 2147483647.

If the
                                                      					 ERL's tag is not a configured tag, the phone is not associated to an ERL and
                                                      					 the phone defaults to its IP address to find the inclusive ERL subnet.

This
                                                      					 command can also be configured in ephone-template configuration mode and
                                                      					 applied to one or more phones. The ephone configuration has priority over the
                                                      					 ephone-template configuration.

Step 5

end

##### Example:

```
Router(config-ephone)# end
```

Returns to
                                                				privileged EXEC mode.

#### Assign an ERL to a
                              	 Dial Peer

Perform this
                                    		  procedure to assign an ERL to a FXS/FXO or VoIP dial peer. Because these
                                    		  interfaces do not have IP addresses associated with them, you must use this
                                    		  procedure instead of configuring an ERL to be associated with IP subnets. For
                                    		  more information about this decision, see Step 7 in Plan Your Implementation of Enhanced 911 Services .

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice tag
                                          				  type

- emergency response location tag

- end

### DETAILED STEPS

Step 1

enable

##### Example:

```
Router> enable
```

Enables
                                                				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global
                                                				configuration mode.

Step 3

dial-peer voice tag
                                                   				  type

##### Example:

```
Router(config)# dial-peer voice 100 pots
```

Enters dial
                                                				peer configuration mode to define parameters for an individual dial peer.

Step 4

emergency response location tag

##### Example:

```
Router(config-dial-peer)# emergency response location 12
```

Assigns an ERL
                                                				to a phone s dial peer configuration using an ERL's tag. The tag is an integer
                                                				from 1 to 2147483647. If the ERL's tag is not a configured tag, no translation
                                                				occurs and no Enhanced 911 information is saved to the last emergency caller
                                                				table.

Step 5

end

##### Example:

```
Router(config-dial-peer)# end
```

Returns to
                                                				privileged EXEC mode.

### Customize E911
                           	 Settings

The E911 settings
                                 		  you can customize are:

Elin : The
                                       				default ELIN. If a 911 caller’s IP phone address does not match the subnet of
                                       				any location in any zone, the default ELIN is used to replace the original
                                       				automatic number identification (ANI). The default ELIN can be already defined
                                       				in one of the ERLs or can be unique. If a default ELIN is not defined and there
                                       				is no match for the 911 caller’s IP address, the PSAP sees the ANI for callback
                                       				purposes. A syslog message is sent requesting the default ELIN, and no caller
                                       				location information is available to the PSAP.

Expiry : The
                                       				number of minutes a 911 call is associated to an ELIN in case of a callback
                                       				from the 911 operator. The callback expiry can be changed from a default of 3
                                       				hours to any time between 2 minutes and 48 hours. The timer is started the
                                       				moment the 911 call goes to the PSAP. The PSAP can call back the ELIN and reach
                                       				the last caller within this expiry time.

Callback : The
                                       				default phone number to contact if a 911 callback cannot find the last 911
                                       				caller from the Last Caller table. This can happen if the callback occurs after
                                       				a router has rebooted or if the expiration has elapsed.

Logging : A
                                       				syslog informational message is printed to the console every time an emergency
                                       				call is made. Such a message is required for third party applications to send
                                       				an e-mail or page to an in-house emergency administrator. This is a default
                                       				feature that can be disabled using the no logging command. The following is an example of a syslog notification message:

```
%E911-5-EMERGENCY_CALL_PLACED: calling #[4085550100] called
#[911] ELIN [4085550199]
```

#### Before you begin

Cisco Unified
                                       				CME 4.2 or a later version

### SUMMARY STEPS

- enable

- configure terminal

- voice emergency response settings

- expiry time

- callback number

- logging

- elin number

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

voice emergency response settings

#### Example:

```
Router(config)# voice emergency response settings
```

Enters voice
                                             				emergency response settings mode to define settings you can customize for E911
                                             				calls.

Step 4

expiry time

#### Example:

```
Router(cfg-emrgncy-resp-settings)# expiry 300
```

(Optional)
                                             				Defines the time period (in minutes) that the emergency caller history
                                             				information for each ELIN is stored in the Last Caller table. The time can be
                                             				an integer in the range of 2 minutes to 2880 minutes. The default value is 180
                                             				minutes.

Step 5

callback number

#### Example:

```
Router(cfg-emrgncy-resp-settings)# callback 7500
```

(Optional)
                                             				Defines the E.164 callback number (for example, a company operator or main help
                                             				desk) if a 911 callback cannot find the last caller associated to the ELIN.

Step 6

logging

#### Example:

```
Router(cfg-emrgncy-resp-settings)# no logging
```

(Optional)
                                             				Enables syslog messages that announce every emergency call. The syslog messages
                                             				can be tracked to send pager or e-mail notifications to an in-house support
                                             				number. By default, logging is enabled. Use the no form of
                                             				this command to disable logging.

Step 7

elin number

#### Example:

```
Router(cfg-emrgncy-resp-settings)# elin 4085550100
```

Specifies the
                                             				E.164 number to be used as the default ELIN if no ERL has a subnet mask that
                                             				matches the current 911 caller s IP phone address.

Step 8

end

#### Example:

```
Router (cfg-emrgncy-resp-settings)# end
```

Returns to
                                             				privileged EXEC mode.

### Using the Address
                           	 Command for Two ELINS

For ERLs that have
                                 		  two ELINs defined, you cannot use just one address field
                                 		  to have two address entries for each ELIN in the ALI database. Instead of
                                 		  entering the specific phone number, a key phrase is entered to represent each
                                 		  ELIN. The show voice emergency
                                       				address command produces output that replaces the key phrase with
                                 		  the ELIN information and generates two lines of addresses.

To define the
                                 		  expression, use the keyword elin (context-insensitive), followed by a period, the starting position of the ELIN
                                 		  to use, followed by another period, and finally the ending position of the
                                 		  ELIN. For example:

```
address I,ELIN.1.3,ELIN.4.7,678 ,Alder Drive ,Milpitas ,CA,95035
```

In the example,
                                 		  the second parameter of address following I are digits 1-3 of each ELIN. The third parameter are digits 4-7 of
                                 		  each ELIN. When you enter the show voice emergency
                                       				address command, the output will replace the key phrase as seen
                                 		  in the following:

```
I,408,5550101,678,Alder Drive ,Milpitas ,CA,95035 
I,408,5550190,678,Alder Drive ,Milpitas ,CA,95035
```

### Enable Call Detail
                           	 Records

To conform to
                              		internal policy or external regulations, you may be required to save 911 call
                              		history data including the following information:

Original
                                    			 caller’s extension

ELIN information

ERL information
                                    			 (the integer tag and the text name)

Original
                                    			 caller’s phone IP address

These attributes are
                              		visible from the RADIUS accounting server and syslog server output, or by using
                              		the show call history
                                    			 voice command.

You must enable
                                          		  the RADIUS server or the syslog server to display these details. See your
                                          		  RADIUS or syslog server documentation.

#### Output from a RADIUS Accounting Server

For RADIUS accounting, the emergency call information is under a
                                    		  feature-vsa record. The fields are:

EMR: Emergency call

CGN: Original calling number

ELIN: Emergency line identification number; the translated number

CDN: Called number

ERL: Emergency response location tag number

ERLN: Emergency response location name; the name entered for the
                                          				ERL, if one exists

CIP: Caller’s IP address; nonzero for implicit ERL assignments

ETAG: ERL tag; nonzero for explicit ERL assignments

The following shows an output example from a RADIUS server:

```
*Jul 18 15:37:43.691: RADIUS: Cisco AVpair [1] 202 "feature-vsa=fn:EMR
,ft:07/18/2007 15:37:32.227,frs:0,fid:6,fcid:A2444CAF347B11DC8822F63A1B4078DE,
legID:57EC,cgn:6045550101,elin:6045550199,cdn:911,erl:2,erln:Fisco,cip:1.5.6.200,etag:0"
```

#### Output from a Syslog Server

If gateway accounting is directed to the syslog server, a
                                    		  VOIP_FEAT_HISTORY system message appears. The feature-vsa parameters are the
                                    		  same ones described for RADIUS accounting.

The following shows an output example from a syslog server:

```
*Jul 18 15:37:43.675: %VOIPAAA-5-VOIP_FEAT_HISTORY: FEAT_VSA=fn:EMR,ft:07/18/2007
15:37:32.227,frs:0,fid:6,fcid:A2444CAF347B11DC8822F63A1B4078DE,legID:57EC,cgn:6045550199,
elin:6045550100,cdn:911,erl:2,erln:ABCDEFGHIJKLMNOPQRSTUVWXYZ123,cip:1.5.6.200,etag:0,
bguid:A23F6AD7347B11DC881DF63A1B4078DE
```

#### Output from the show call history voice Command

View emergency call information on the gateway using show call active voice and show call history voice . Some emergency call
                                    		  information is already in existing fields. The original caller’s number is
                                    		  under OriginalCallingNumber . The ELIN is at TranslatedCallingNumber . The four new fields
                                    		  are the ERL, ERL name, the calling phone’s IP address, and any explicit ERL
                                    		  assignments. These fields only appear if an ELIN translation occurs. For
                                    		  example, any 911 calls from an ERL with no ELIN defined do not print the four
                                    		  emergency fields in the show call commands. If no ERLs match the
                                    		  calling phone and the default ELIN is used, the ERL field displays No Match .

The following shows an output example using the show call history voice command:

```
EmergencyResponseLocation=3 (Cisco Systems 3)
ERLAssignment=3
DeviceIPAddress=1.5.6.202
```

### Verify E911 Configuration

New show commands are introduced to display E911
                                 		  configuration or usage.

Use the show voice emergency callers command to
                                       				see the translations made by outbound 911 calls. This command lists the
                                       				originating number, the ELIN used, and the time for each 911 call. This history
                                       				is active for only three hours after the call is placed. Expired calls are not
                                       				shown in this output.

```
router# show voice emergency callers EMERGENCY CALLS CALL BACK table
ELIN                      | CALLER                     | TIME                
6045550100                | 6045550150                 | Oct 12 2006 03:59:43
6045550110                | 8155550124                 | Oct 12 2006 04:05:21
```

Use the show voice emergency command to display
                                       				IP addresses, subnet masks, and ELINs for each ERL.

```
Router# show voice emergency EMERGENCY RESPONSE LOCATIONS
ERL               | ELIN 1     | ELIN2      | SUBNET 1 | SUBNET 2       
1                 | 6045550101 |            | 10.0.0.0        | 255.0.0.0 
2                 | 6045550102 | 6045550106 | 192.168.0.0     | 255.255.0.0 
3                 |            | 6045550107 | 172.16.0.0      | 255.255.0.0 
4                 | 6045550103 |            | 192.168.0.0     | 255.255.0.0 
5                 | 6045550105 |            | 209.165.200.224 | 255.0.0.0 
6 6045550198      |            | 6045550109 | 209.165.201.0   | 255.255.255.224
```

Use the show voice emergency addresses command to display address information for each ERL.

```
Router# show voice emergency addresses 3850 Zanker Rd, San Jose,604,5550101
225 W Tasman Dr, San Jose,604,5550102
275 W Tasman Dr, San Jose,604,5550103
518 Bellew Dr,Milpitas,604,5550104
400 Tasman Dr,San Jose,604,5550105
3675 Cisco Way,San Jose,604,5550106
```

Use the show voice emergency all command to
                                       				display all ERL information.

```
Router# show voice emergency all VOICE EMERGENCY RESPONSE SETTINGS
   Callback Number: 6045550103
   Emergency Line ID Number: 6045550155
   Expiry: 2 minutes
   Logging Enabled

EMERGENCY RESPONSE LOCATION 1
   Name: Cisco Systems 1
   Address: 3850 Zanker Rd, San Jose,elin.1.3,elin.4.10 
   IP Address 1: 209.165.200.226 IP mask 1: 255.255.255.254
   IP Address 2: 209.165.202.129 IP mask 2: 255.255.0.0
   Emergency Line ID 1: 6045550180
   Emergency Line ID 2: 
   Last Caller:  6045550188 [Jan 30 2007 16:05.52 PM]
   Next ELIN For Emergency Call: 6045550166

EMERGENCY RESPONSE LOCATION 3
   Name: Cisco Systems 3
   Address: 225 W Tasman Dr, San Jose,elin.1.3,elin.4.10 
   IP Address 1: 209.165.202.133 IP mask 1: 255.255.0.0
   IP Address 2: 209.165.202.130 IP mask 2: 255.0.0.0
   Emergency Line ID 1: 
   Emergency Line ID 2: 6045550150
   Last Caller:  
   Next ELIN For Emergency Call: 6045550151
```

Use the show voice emergency zone command to display each zone’s list of locations in order of priority.

```
Router# show voice emergency zone EMERGENCY RESPONSE ZONES
 zone 90
    location 4
    location 5
    location 6
    location 7
    location 2147483647
 zone 100
    location 1 priority 1
    location 2 priority 2
    location 3 priority 3
```

### Troubleshooting Enhanced 911 Services

Use the debug voice application error and
                                          			 the debug voice application callsetup command. These
                                          			 are existing commands for calls made using the default session or TCL
                                          			 applications.

This example shows the debug output when a call to 911 is made:

```
Router# debug voice application error Router# debug voice application callsetup Nov 10 23:49:05.855: //emrgncy_resp_xlate_callingNum: InDialPeer[20001], OutDialPeer[911] callingNum[6046692003] 
			 Nov 10 23:49:05.855: //ER_HistTbl_Find_CallHistory: 6046699100 
			 Nov 10 23:49:05.855: //59//Dest:/DestProcessEmergencyCall: Emergency Call detected: Using ELIN 6046699100
```

This example shows the debug output when a PSAP calls back an
                                             				emergency caller:

```
Router# debug voice application error Router# debug voice application callsetup Nov 10 23:49:37.279: //emrgncy_resp_xlate_calledNum: calledNum[6046699100], dpeerTag[6046699] 
			 Nov 10 23:49:37.279: //ER_HistTbl_Find_CallHistory: 6046699100 
			 Nov 10 23:49:37.279: //HasERHistoryExpired: elapsedTime[10 minutes] 
			 Nov 10 23:49:37.279: //67//Dest:/DestProcessEmergencyCallback: Emergency Response Callback: Forward to 6046692003.
			 Nov 10 23:49:37.279: //67//Dest:/DestCaptureCallForward: forwarded to 6046692003 reason 1
```

### Error Messages

The Enhanced 911 feature introduces a new system error message. The
                                 		  following error message displays if a 911 callback cannot route to the last 911
                                 		  caller because the saved history was lost because of a reboot, an expiration of
                                 		  an entry, or a software error:

```
%E911_NO_CALLER:  Unable to contact last 911 caller.
```

## Configuration Examples for Enhanced 911 Services

### Example for Configuring Enhanced E911 Services with Cisco Unified CME
                           	 4.2

Emergency response settings are:

default elin if no elin match is found: 604 555-0120

expiry time for information in the Last Caller table: 180 minutes

callback number if the PSAP operator must call back the 911 caller
                                       				and the call back history has expired: 604 555-0199

Zone 1 has four locations, 1, 2, 3, and 4, and a name, address, and
                                 		  elin are defined for each location. Each of the four locations is assigned a
                                 		  priority. In this example, because location 4 has been assigned the highest
                                 		  priority, it is the first that is searched for IP subnet matches to identify
                                 		  the ELIN assigned to the 911 caller’s phone. A dial peer is configured to route
                                 		  911 calls to the PSAP (voice port 1/0/0). Callback dial peers are also
                                 		  configured.

```
!
voice emergency response settings
elin 6045550120
expiry 180
callback 6045550199
!
voice emergency response location 1
name Bldg C, Floor 1
address I,604,5550135, ,184 ,Main St,Kansas City,KS,1,
elin 1 6045550125
subnet 1 172.16.0.0 255.255.0.0
!
voice emergency response location 2
name Bldg C, Floor 2
address I,elin.1.3,elin.4.7, ,184 ,Main St,Kansas City,KS,2,
elin 1 6045550126
elin 2 6045550127
subnet 1 192.168.0.0 255.255.0.0
!
voice emergency response location 3
name Bldg C, Floor 3
address I,604,5550138, ,184 ,Main St,Kansas City,KS,3,
elin 2 6045550128
subnet 1 209.165.200.225 255.255.0.0
subnet 2 209.165.200.240 255.255.0.0
!
voice emergency response location 4
name Bldg D
address I,604,5550139, ,192 ,Main St,Kansas City,KS,
elin 1 6045550129
subnet 1 209.165.200.231 255.255.0.0
!
voice emergency response zone 1
location 4 priority 1
location 3 priority 2
location 2 priority 3
location 1 priority 4
!
dial-peer voice 911 pots
description Public Safety Answering Point
emergency response zone 1
destination-pattern 911
port 1/0/0
!
dial-peer voice 6045550 voip
emergency response callback
destination-pattern 6045550...
session target loopback:rtp
codec g711ulaw
!
dial-peer voice 1222 pots
emergency response location 4
destination-pattern 6045550130
port 1/0/1
!
dial-peer voice 5550144 voip
emergency response callback
session target ipv4:1.5.6.10
incoming called-number 604555....
codec g711ulaw
!
```

### Example for Configuring Enhanced E911 Services with Cisco Unified CME
                           	 4.1 in SRST Fallback Mode

In this example, Enhanced 911 Services is configured to assign an ERL
                                 		  to the following:

The 10.20.20.0 IP subnet

Two dial peers

An ephone

A SI P phone

```
Router# show running-config Building configuration...

Current configuration : 7557 bytes
!
version 12.4
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname rm-uut3-2821
!
boot-start-marker
boot-end-marker
!
no logging console
!
no aaa new-model
network-clock-participate wic 1
network-clock-participate wic 2
no network-clock-participate wic 3
!
!
!
ip cef
no ip dhcp use vrf connected
!
ip dhcp pool sccp-7912-phone1
host 10.20.20.122 255.255.0.0
client-identifier 0100.1200.3482.cd
default-router 10.20.20.3
option 150 ip 10.21.20.218
!
ip dhcp pool sccp-7960-phone2
host 10.20.20.123 255.255.0.0
client-identifier 0100.131a.a67d.cf
default-router 10.20.20.3
option 150 ip 10.21.20.218
dns-server 10.20.20.3
!
ip dhcp pool sip-phone1
host 10.20.20.121 255.255.0.0
 client-identifier 0100.15f9.b38b.a6
default-router 10.20.20.3
option 150 ip 10.21.20.218
!
ip dhcp pool sccp-7960-phone1
host 10.20.20.124 255.255.0.0
client-identifier 0100.14f2.37e0.00
default-router 10.20.20.3
option 150 ip 10.21.20.218
dns-server 10.20.20.3
!
!
no ip domain lookup
ip host rm-uut3-c2821 10.20.20.3
ip host RescuMe01 10.21.20.218
multilink bundle-name authenticated
!
isdn switch-type basic-net3
!
!
voice service voip
allow-connections h323 to h323
allow-connections h323 to sip
allow-connections sip to h323
allow-connections sip to sip
supplementary-service h450.12
sip
registrar server
!
!
voice register global
system message RM-SIP-SRST
max-dn 192
max-pool 48
!
voice register dn  1
number 32101
!
voice register dn  185
number 38301
!
voice register dn  190
number 38201
!
voice register dn  191
number 38202
!
voice register dn  192
number 38204
!
voice register pool  1
id mac DCC0.2222.0001
number 1 dn 1 emergency response location 2100 !
voice register pool  45
id mac 0015.F9B3.8BA6
number 1 dn 185
! voice emergency response location 1
elin 1 22222
subnet 1 10.20.20.0 255.255.255.0
!
voice emergency response location 2
elin 1 21111
elin 2 21112 !
!
voice-card 0
no dspfarm
!
!
archive
log config
hidekeys
!
!
controller T1 0/1/0
framing esf
linecode b8zs
pri-group timeslots 8,24
!
controller T1 0/1/1
framing esf
linecode b8zs
pri-group timeslots 2,24
!
controller T1 0/2/0
framing esf
clock source internal
linecode b8zs
ds0-group 1 timeslots 2 type e&m-immediate-start
!
controller T1 0/2/1
framing esf
linecode b8zs
pri-group timeslots 2,24
!
!
translation-rule 5
Rule 0 ^37103 1
!
!
translation-rule 6
Rule 6 ^2 911
!
!
interface GigabitEthernet0/0
ip address 31.20.0.3 255.255.0.0
duplex auto
speed auto
!
interface GigabitEthernet0/1
ip address 10.20.20.3 255.255.0.0
duplex auto
speed auto
!
interface Serial0/1/0:23
no ip address
encapsulation hdlc
isdn switch-type primary-5ess
isdn incoming-voice voice
no cdp enable
!
interface Serial0/1/1:23
no ip address
encapsulation hdlc
isdn switch-type primary-net5
isdn incoming-voice voice
no cdp enable
!
interface Serial0/2/1:23
no ip address
encapsulation hdlc
isdn switch-type primary-net5
isdn incoming-voice voice
no cdp enable
!
interface BRI0/3/0
no ip address
isdn switch-type basic-5ess
isdn twait-disable
isdn point-to-point-setup
isdn autodetect
isdn incoming-voice voice
no keepalive
!
interface BRI0/3/1
no ip address
isdn switch-type basic-5ess
isdn point-to-point-setup
!
!
ip http server
!
!
voice-port 0/0/0
!
voice-port 0/0/1
!
voice-port 0/1/0:23
!
voice-port 0/2/0:1
!
voice-port 0/1/1:23
!
voice-port 0/2/1:23
!
voice-port 0/3/0
!
voice-port 0/3/1
!
!
dial-peer voice 2002 pots
shutdown
destination-pattern 2....
port 0/2/0:1
forward-digits all
!
dial-peer voice 2005 pots
description for-cme2-408-pri emergency response location 2000 shutdown
incoming called-number 911
direct-inward-dial
port 0/2/1:23
forward-digits all
!
dial-peer voice 2004 voip
description for-cme2-408-thru-ip emergency response location 2000 shutdown
session target loopback:rtp
incoming called-number 911
!
dial-peer voice 1052 pots
description 911callbackto-cme2-3
shutdown
incoming called-number .....
direct-inward-dial
port 0/1/1:23
forward-digits all
!
dial-peer voice 1013 pots
description for-analog
destination-pattern 39101
port 0/0/0
forward-digits all
!
dial-peer voice 1014 pots
description for-analog-2
destination-pattern 39201
port 0/0/1
forward-digits all
!
dial-peer voice 3111 pots emergency response Zone destination-pattern 9....
port 0/1/0:23
forward-digits all
!
dial-peer voice 3121 pots emergency response callback incoming called-number 2....
direct-inward-dial
port 0/1/0:23
forward-digits all
!
!
telephony-service
srst mode auto-provision none
load 7960-7940 P00307020200
load 7970 TERM70.7-0-1-0s
load 7912 CP7912060101SCCP050429B.sbin
max-ephones 50
max-dn 190
ip source-address 10.20.20.3 port 2000
system message RM-SCCP-CME-SRST
max-conferences 8 gain -6
moh flash:music-on-hold.au
multicast moh 236.1.1.1 port 3000
transfer-system full-consult
transfer-pattern .....
transfer-pattern 911
!
!
ephone-dn  1  dual-line
number 31101
!
!
ephone-dn  2  dual-line
number 31201
!
!
ephone-dn  3  dual-line
number 31301
!
!
ephone-dn  100  dual-line
number 37101 secondary 37111
name 7960-sccp-1
!
!
ephone-dn  101  dual-line
number 37102
!
!
ephone-dn  102  dual-line
number 37103
!
!
ephone-dn  105
number 37201
!
!
ephone-dn  106  dual-line
number 37101
!
!
ephone-dn  107  dual-line
number 37302
!
!
ephone-dn  108  dual-line
number 37303
!
!
ephone-dn  110  dual-line
number 37401
!
!
ephone-dn  111  dual-line
number 37402
!
!
ephone  1
mac-address DCC0.1111.0001
type 7960
button  1:1
!
!
ephone  2
mac-address DCC0.1111.0002
type 7960
button  1:2
!
!
ephone  3
mac-address DCC0.1111.0003
type 7970
button  1:3
!
!
ephone  40
mac-address 0013.1AA6.7DCF
type 7960
button  1:100 2:101 3:102
!
!
ephone  41
mac-address 0012.0034.82CD
type 7912
button  1:105
!
!
ephone  42
mac-address 0014.F237.E000 emergency response location 2 type 7940
button  1:107 2:108
!
!
ephone  43
mac-address 000F.90B0.BE0B
type 7960
button  1:110 2:111
!
!
line con 0
exec-timeout 0 0
line aux 0
line vty 0 4
login
!
scheduler allocate 20000 1000
!
end
```

## Feature
                        	 Information for Enhanced 911 Services

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature
                                             					 Name

Cisco Unified CME Version

Feature
                                             					 Information

Enhanced
                                             					 911 Services for Cisco Unified CME

4.2

Assigns ERLs to zones to enable routing to the PSAP that is
                                                   						  closest to the caller

Customizes E911 by defining a default ELIN, identifying a
                                                   						  designated number if the 911 caller cannot be reached on callback, specifying
                                                   						  the expiry time for data in the Last Caller table, and enabling syslog messages
                                                   						  that announce all emergency calls

Expands the E911 location information to include name and
                                                   						  address

Uses
                                                   						  templates to assign ERLs to a group of phones

Adds
                                                   						  new permanent call detail records

Enhanced
                                             					 911 Services

4.1

Enhanced
                                             					 911 Services was introduced for Cisco Unified CME in SRST Fallback Mode.

| Note | For information
                                    		about configuring ephones, ephone-dns, voice register pools, and voice register
                                    		dns, see Configure Phones to Make Basic Call . |
|---|---|

| Note | If a caller’s
                                                				IP address does not match any location in its dial-peers zone, the last dial
                                                				peer that matched is used for routing and the default ELIN is used. If you want
                                                				911 calls from any particular phone to always use the same dial peer when you
                                                				have multiple dial peers going to the same destination-pattern (911) and the
                                                				zones are different, you must configure the preferred dial peer to be the
                                                				highest priority by setting the preference field. |
|---|---|

| Step 1 | Make a list
                                          			 of your sites that are serviced by Cisco Unified CME, and the PSAPs serving
                                          			 each site. Be aware that
                                             				you must use a CAMA/PRI interface to connect to each PSAP. Table 1 shows an example of the information that you need to gather. Table 1. List of
                                                   				Sites and PSAPs Building Name and Address Responsible PSAP Interface to which Calls Are Routed Building 2, 201 Maple Street, San Francisco San
                                                         						  Francisco, CA Port
                                                         						  1/0:D Building 40, 801 Main Street, San Jose San
                                                         						  Jose, CA Port
                                                         						  1/1:D | Building Name and Address | Responsible PSAP | Interface to which Calls Are Routed | Building 2, 201 Maple Street, San Francisco | San
                                                         						  Francisco, CA | Port
                                                         						  1/0:D | Building 40, 801 Main Street, San Jose | San
                                                         						  Jose, CA | Port
                                                         						  1/1:D |
|---|---|---|---|---|---|---|---|---|---|---|
| Building Name and Address | Responsible PSAP | Interface to which Calls Are Routed |
| Building 2, 201 Maple Street, San Francisco | San
                                                         						  Francisco, CA | Port
                                                         						  1/0:D |
| Building 40, 801 Main Street, San Jose | San
                                                         						  Jose, CA | Port
                                                         						  1/1:D |
| Step 2 | Use local laws
                                          			 to determine the number of ERLs you need to configure. According to
                                             				the National Emergency Number Association (NENA) model legislation, make the
                                             				location specific enough to provide a reasonable opportunity for the emergency
                                             				response team to quickly locate a caller anywhere within it. Table 2 shows an example. Table 2. ERL
                                                      				Calculation Building Size
                                                            						  in Square Feet Number
                                                            						  of Floors Number
                                                            						  of ERLs Required Building 2 200,000 3 3 Building 40 7000 2 1 | Building | Size
                                                            						  in Square Feet | Number
                                                            						  of Floors | Number
                                                            						  of ERLs Required | Building 2 | 200,000 | 3 | 3 | Building 40 | 7000 | 2 | 1 |
| Building | Size
                                                            						  in Square Feet | Number
                                                            						  of Floors | Number
                                                            						  of ERLs Required |
| Building 2 | 200,000 | 3 | 3 |
| Building 40 | 7000 | 2 | 1 |
| Step 3 | (Optional)
                                          			 Assign one or two ELINs to each ERL. You must
                                             				contact your phone service provider to request phone numbers that are
                                             				designated as ELINs. |
| Step 4 | (Optional)
                                          			 Assign each of your ERLs to an emergency response zone to enable 911 calls to
                                          			 be routed to the PSAP that is closest to the caller. Use the voice emergency response
                                                				  zone command. |
| Step 5 | Configure one
                                          			 or more dial peers for your 911 callers with the emergency response
                                                				  zone command. You might need
                                             				to configure multiple dial peers for different destination-patterns. |
| Step 6 | Configure one
                                          			 or more dial peers for the PSAP’s 911 callbacks with the emergency response
                                                				  callback command. |
| Step 7 | Decide what
                                          			 method to use to assign ERLs to phones. You have the
                                             				following choices: For a
                                                   					 group of phones that are on the same subnet, you can create an IP subnet in the
                                                   					 ERL that includes each phone’s IP address. Each ERL can have one or two unique
                                                   					 IP subnets. This is the easiest option to configure. Table 3 shows an example. Table 3. Definitions of ERL, Description, IP Subnets, and ELIN ERL
                                                            						  Number Description IP
                                                            						  Address Assignment ELIN 1 Building 2, 1st floor 10.5.124.xxx 408
                                                            						  555-0142 2 Building 2, 2nd floor 10.7.xxx.xxx 408
                                                            						  555-0143 3
                                                            						  & 4 Building 2, 3rd floor 10.8.xxx.xxx and 10.9.xxx.xxx 408
                                                            						  555-0144 and 408 555-0145 You can
                                                   					 assign an ERL explicitly to a group of phones by using the ephone-template or
                                                   					 voice register template configurations. Instead of assigning an ERL to phones
                                                   					 individually, you can use these templates to save time if you want to apply the
                                                   					 same set of features to several SCCP phones or SIP phones. You can
                                                   					 assign an ERL to a phone individually. Depending on which type of phone you
                                                   					 have, you can use one of three methods. You can assign an ERL to a phone’s: Dial-peer configuration Ephone configuration (SCCP phones) Voice register pool configuration (SIP phones) Table 4 shows examples of each of these options. Table 4. Explicit
                                                   				ERL Assignment Per Phone Phone Configuration ERL Dial-peer voice 213 pots 3 Dial-peer voice 214 voip 4 Ephone 100 3 Voice register pool 1 2 | ERL
                                                            						  Number | Description | IP
                                                            						  Address Assignment | ELIN | 1 | Building 2, 1st floor | 10.5.124.xxx | 408
                                                            						  555-0142 | 2 | Building 2, 2nd floor | 10.7.xxx.xxx | 408
                                                            						  555-0143 | 3
                                                            						  & 4 | Building 2, 3rd floor | 10.8.xxx.xxx and 10.9.xxx.xxx | 408
                                                            						  555-0144 and 408 555-0145 | Phone Configuration | ERL | Dial-peer voice 213 pots | 3 | Dial-peer voice 214 voip | 4 | Ephone 100 | 3 | Voice register pool 1 | 2 |
| ERL
                                                            						  Number | Description | IP
                                                            						  Address Assignment | ELIN |
| 1 | Building 2, 1st floor | 10.5.124.xxx | 408
                                                            						  555-0142 |
| 2 | Building 2, 2nd floor | 10.7.xxx.xxx | 408
                                                            						  555-0143 |
| 3
                                                            						  & 4 | Building 2, 3rd floor | 10.8.xxx.xxx and 10.9.xxx.xxx | 408
                                                            						  555-0144 and 408 555-0145 |
| Phone Configuration | ERL |
| Dial-peer voice 213 pots | 3 |
| Dial-peer voice 214 voip | 4 |
| Ephone 100 | 3 |
| Voice register pool 1 | 2 |
| Step 8 | (Optional)
                                          			 Define a default ELIN to be sent to the PSAP for use if a 911 caller's IP
                                          			 phone's address does not match the IP subnet of any location in any zone. |
| Step 9 | (Optional)
                                          			 Define a designated callback number that is used if the callback information is
                                          			 removed from the Last Caller table because of an expiry timeout or system
                                          			 restart. |
| Step 10 | (Optional)
                                          			 Change the expiry time for data in the Last Caller table from the default time
                                          			 of three hours. |
| Step 11 | (Optional)
                                          			 Enable RADIUS accounting or the syslog service to permanently record call
                                          			 detail records. |

| Building Name and Address | Responsible PSAP | Interface to which Calls Are Routed |
|---|---|---|
| Building 2, 201 Maple Street, San Francisco | San
                                                         						  Francisco, CA | Port
                                                         						  1/0:D |
| Building 40, 801 Main Street, San Jose | San
                                                         						  Jose, CA | Port
                                                         						  1/1:D |

| Building | Size
                                                            						  in Square Feet | Number
                                                            						  of Floors | Number
                                                            						  of ERLs Required |
|---|---|---|---|
| Building 2 | 200,000 | 3 | 3 |
| Building 40 | 7000 | 2 | 1 |

| ERL
                                                            						  Number | Description | IP
                                                            						  Address Assignment | ELIN |
|---|---|---|---|
| 1 | Building 2, 1st floor | 10.5.124.xxx | 408
                                                            						  555-0142 |
| 2 | Building 2, 2nd floor | 10.7.xxx.xxx | 408
                                                            						  555-0143 |
| 3
                                                            						  & 4 | Building 2, 3rd floor | 10.8.xxx.xxx and 10.9.xxx.xxx | 408
                                                            						  555-0144 and 408 555-0145 |

| Phone Configuration | ERL |
|---|---|
| Dial-peer voice 213 pots | 3 |
| Dial-peer voice 214 voip | 4 |
| Ephone 100 | 3 |
| Voice register pool 1 | 2 |

| Note | Your version of Cisco Unified CME may not support all of these
                                          		  features. |
|---|---|

| Note | We recommend that you do not use ELINs for any other purpose because
                                             		  of possible unexpected interactions with existing Cisco Unified CME features. |
|---|---|

| Caution | We recommend that you do not configure the same dial peer using both
                                             		  the emergency response zone and emergency response callback commands. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice emergency response location tag Example: Router(config)# voice emergency response location 4 | Enters
                                             				emergency response location configuration mode to define parameters for an ERL. |
| Step 4 | elin [ 1 \| 2 ] E.164-number Example: Router(cfg-emrgncy-resp-location)# elin 14085550100 | (Optional) Specifies the ELIN, an E.164 PSTN number that replaces
                                             				the caller's extension. This number is displayed on the PSAP’s terminal and is used by
                                                      					 the PSAP to query the ALI database to locate the caller. It is also used by the
                                                      					 PSAP for callbacks. You can define a second ELIN using the optional elin 2
                                                      					 command. If an ELIN is not defined for the ERL, the PSAP sees the original
                                                      					 calling number. |
| Step 5 | address address Example: Router(cfg-emrgncy-resp-location)# address I,604,5550100, ,184 ,Main St,Kansas City,KS,1, | (Optional) Defines a comma-separated string used for the automatic
                                             				location identification (ALI) database upload of the caller’s address. String must conform to the record format that is required by
                                                   					 the service provider. The string maximum is 247 characters. Address is saved as part of the E911 ERL configuration. When
                                                   					 used with the show voice emergency addresses command, the address
                                                   					 information can be saved to a text file. This command is supported in Cisco Unified CME 4.2 and later
                                                   					 versions. |
| Step 6 | name name Example: Router(cfg-emrgncy-resp-location)# name Bldg C, Floor 2 | (Optional) Defines a 30-character string used internally to
                                             				identify or describe the emergency response location. This command is supported in Cisco Unified CME 4.2 and later
                                                   					 versions. |
| Step 7 | end Example: Router(cfg-emrgncy-resp-location)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice emergency response zone tag Example: Router(config)# voice emergency response zone 10 | Enters voice
                                             				emergency response zone configuration mode to define parameters for an
                                             				emergency response zone. tag —Range is 1-100. |
| Step 4 | location location-tag [ priority number ] Example: Router(cfg-emrgncy-resp-zone)# location 8 priority 2 | Each location
                                             				tag must correspond to a location tag created using the voice emergency response
                                                   					 location command. number —(optional) Ranks the location in the zone
                                                   					 list. Range is 1-100, with 1 being the highest priority. Repeat
                                                   					 this command for each location included in the zone. |
| Step 5 | end Example: Router(cfg-emrgncy-resp-zone)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                                				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                                				configuration mode. |
| Step 3 | dial-peer voice number pots Example: Router(config)# dial-peer voice 911 pots | Enters
                                                				dial-peer configuration mode to define parameters for an individual dial peer. |
| Step 4 | destination-pattern n 911 Example: Router(config-dial-peer)# destination-pattern 9911 | Matches dialed
                                                				digits to a telephony device. The digits included in this command specify the
                                                				E.164 or private dialing plan telephone number. For Enhanced 911 Services, the
                                                				digits are usually some variation of 911. |
| Step 5 | prefix number Example: Router(config-dial-peer)# prefix 911 | (Optional)
                                                				Includes a prefix that the system adds automatically to the front of the dial
                                                				string before passing it to the telephony interface. For Enhanced 911 Services,
                                                				the dial string is some variation of 911. |
| Step 6 | emergency response zone Example: Router(config-dial-peer)# emergency response zone | Defines this
                                                				dial peer as the one to use to route all ERLs defined in the system to the
                                                				PSAP. |
| Step 7 | end Example: Router(config-dial-peer)# end | Returns to
                                                				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                                				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                                				configuration mode. |
| Step 3 | dial-peer voice number pots Example: Router(config)# dial-peer voice 911 pots | Enters
                                                				dial-peer configuration mode to define parameters for an individual dial peer. |
| Step 4 | destination-pattern n 911 Example: Router(config-dial-peer)# destination-pattern 9911 | Matches dialed
                                                				digits to a telephony device. The digits included in this command specify the
                                                				E.164 or private dialing plan telephone number. For E911 services, the digits
                                                				are usually some variation of 911. |
| Step 5 | prefix number Example: Router(config-dial-peer)# prefix 911 | (Optional)
                                                				Includes a prefix that the system adds automatically to the front of the dial
                                                				string before passing it to the telephony interface. For E911 services, the
                                                				dial string is some variation of 911. |
| Step 6 | emergency response zone tag Example: Router(config-dial-peer)# emergency response zone 10 | Defines this
                                                				dial peer as the one that is used to route ERLs defined for that zone. tag —Points to an existing configured zone. Range
                                                      					 is 1-100. |
| Step 7 | end Example: Router(config-dial-peer)# end | Returns to
                                                				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | dial-peer voice number pots Example: Router(config)# dial-peer voice 100 pots | Enters
                                             				dial-peer configuration mode to define parameters for an individual dial peer. |
| Step 4 | incoming called-number number Example: Router(config-dial-peer)# incoming called-number 4085550100 | (Optional)
                                             				Selects the inbound dial peer based on the called number to identify the last
                                             				caller. This number is the ELIN. |
| Step 5 | direct-inward-dial Example: Router(config-dial-peer)# direct-inward-dial | (Optional) Enables the Direct Inward Dialing (DID) call
                                             				treatment for the incoming called number. For more information, see the chapter Configuring Voice Ports in the Cisco Voice, Video, and Fax
                                                				  Configuration Guide . |
| Step 6 | emergency response callback Example: Router(config-dial-peer)# emergency response callback | Identifies a
                                             				dial peer as an ELIN dial peer. |
| Step 7 | end Example: Router(config-dial-peer)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                                				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                                				configuration mode. |
| Step 3 | voice emergency response location tag Example: Router(config)# voice emergency response location 4 | Enters
                                                				emergency response location configuration mode to define parameters for an ERL. |
| Step 4 | subnet [ 1 \| 2 ] IPaddress-mask Example: Router(cfg-emrgncy-resp-location)# subnet 1 192.168.0.0 255.255.0.0 | Defines the
                                                				groups of IP phones that are part of this location. You can create up to 2
                                                				different subnets. To include
                                                      					 all IP phones on a single ERL, use the command subnet 1 0.0.0.0 0.0.0.0 to configure a default subnet.
                                                      					 This subnet does not apply to nonIP-phone endpoints, such as phones on VoIP
                                                      					 trunks or FXS/FXO trunks. |
| Step 5 | end Example: Router(cfg-emrgncy-resp-location)# end | Returns to
                                                				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                                				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                                				configuration mode. |
| Step 3 | voice register pool tag Example: Router(config)# voice register pool 8 | Enters voice
                                                				register pool mode to define parameters for an individual voice register pool. |
| Step 4 | emergency response location tag Example: Router(config-register-pool)# emergency response location 12 | Assigns an ERL
                                                				to a phone s voice register pool using an ERL s tag. tag —Range is 1 to 2147483647. If the
                                                      					 ERL's tag is not a configured tag, the phone is not associated to an ERL and
                                                      					 the phone defaults to its IP address to find the inclusive ERL subnet. This
                                                      					 command can also be configured in voice register template configuration mode
                                                      					 and applied to one or more phones. The voice register pool configuration has
                                                      					 priority over the voice register template configuration. |
| Step 5 | end Example: Router(config-register-pool)# end | Returns to
                                                				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                                				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                                				configuration mode. |
| Step 3 | ephone tag Example: Router(config)# ephone 224 | Enters ephone
                                                				configuration mode to define parameters for an individual ephone. |
| Step 4 | emergency response location tag Example: Router(config-ephone)# emergency response location 12 | Assigns an ERL
                                                				to a phone s ephone configuration using an ERL s tag. tag —Range is 1 to 2147483647. If the
                                                      					 ERL's tag is not a configured tag, the phone is not associated to an ERL and
                                                      					 the phone defaults to its IP address to find the inclusive ERL subnet. This
                                                      					 command can also be configured in ephone-template configuration mode and
                                                      					 applied to one or more phones. The ephone configuration has priority over the
                                                      					 ephone-template configuration. |
| Step 5 | end Example: Router(config-ephone)# end | Returns to
                                                				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                                				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                                				configuration mode. |
| Step 3 | dial-peer voice tag
                                                   				  type Example: Router(config)# dial-peer voice 100 pots | Enters dial
                                                				peer configuration mode to define parameters for an individual dial peer. |
| Step 4 | emergency response location tag Example: Router(config-dial-peer)# emergency response location 12 | Assigns an ERL
                                                				to a phone s dial peer configuration using an ERL's tag. The tag is an integer
                                                				from 1 to 2147483647. If the ERL's tag is not a configured tag, no translation
                                                				occurs and no Enhanced 911 information is saved to the last emergency caller
                                                				table. |
| Step 5 | end Example: Router(config-dial-peer)# end | Returns to
                                                				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice emergency response settings Example: Router(config)# voice emergency response settings | Enters voice
                                             				emergency response settings mode to define settings you can customize for E911
                                             				calls. |
| Step 4 | expiry time Example: Router(cfg-emrgncy-resp-settings)# expiry 300 | (Optional)
                                             				Defines the time period (in minutes) that the emergency caller history
                                             				information for each ELIN is stored in the Last Caller table. The time can be
                                             				an integer in the range of 2 minutes to 2880 minutes. The default value is 180
                                             				minutes. |
| Step 5 | callback number Example: Router(cfg-emrgncy-resp-settings)# callback 7500 | (Optional)
                                             				Defines the E.164 callback number (for example, a company operator or main help
                                             				desk) if a 911 callback cannot find the last caller associated to the ELIN. |
| Step 6 | logging Example: Router(cfg-emrgncy-resp-settings)# no logging | (Optional)
                                             				Enables syslog messages that announce every emergency call. The syslog messages
                                             				can be tracked to send pager or e-mail notifications to an in-house support
                                             				number. By default, logging is enabled. Use the no form of
                                             				this command to disable logging. |
| Step 7 | elin number Example: Router(cfg-emrgncy-resp-settings)# elin 4085550100 | Specifies the
                                             				E.164 number to be used as the default ELIN if no ERL has a subnet mask that
                                             				matches the current 911 caller s IP phone address. |
| Step 8 | end Example: Router (cfg-emrgncy-resp-settings)# end | Returns to
                                             				privileged EXEC mode. |

| Note | You must enable
                                          		  the RADIUS server or the syslog server to display these details. See your
                                          		  RADIUS or syslog server documentation. |
|---|---|

| Use the debug voice application error and
                                          			 the debug voice application callsetup command. These
                                          			 are existing commands for calls made using the default session or TCL
                                          			 applications. This example shows the debug output when a call to 911 is made: Router# debug voice application error Router# debug voice application callsetup Nov 10 23:49:05.855: //emrgncy_resp_xlate_callingNum: InDialPeer[20001], OutDialPeer[911] callingNum[6046692003] 
			 Nov 10 23:49:05.855: //ER_HistTbl_Find_CallHistory: 6046699100 
			 Nov 10 23:49:05.855: //59//Dest:/DestProcessEmergencyCall: Emergency Call detected: Using ELIN 6046699100 This example shows the debug output when a PSAP calls back an
                                             				emergency caller: Router# debug voice application error Router# debug voice application callsetup Nov 10 23:49:37.279: //emrgncy_resp_xlate_calledNum: calledNum[6046699100], dpeerTag[6046699] 
			 Nov 10 23:49:37.279: //ER_HistTbl_Find_CallHistory: 6046699100 
			 Nov 10 23:49:37.279: //HasERHistoryExpired: elapsedTime[10 minutes] 
			 Nov 10 23:49:37.279: //67//Dest:/DestProcessEmergencyCallback: Emergency Response Callback: Forward to 6046692003.
			 Nov 10 23:49:37.279: //67//Dest:/DestCaptureCallForward: forwarded to 6046692003 reason 1 |
|---|

| Feature
                                             					 Name | Cisco Unified CME Version | Feature
                                             					 Information |
|---|---|---|
| Enhanced
                                             					 911 Services for Cisco Unified CME | 4.2 | Assigns ERLs to zones to enable routing to the PSAP that is
                                                   						  closest to the caller Customizes E911 by defining a default ELIN, identifying a
                                                   						  designated number if the 911 caller cannot be reached on callback, specifying
                                                   						  the expiry time for data in the Last Caller table, and enabling syslog messages
                                                   						  that announce all emergency calls Expands the E911 location information to include name and
                                                   						  address Uses
                                                   						  templates to assign ERLs to a group of phones Adds
                                                   						  new permanent call detail records |
| Enhanced
                                             					 911 Services | 4.1 | Enhanced
                                             					 911 Services was introduced for Cisco Unified CME in SRST Fallback Mode. |