---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-networking-guide-b-15cucnext-b-14cucnetx-chapter-0101-html-7cdf573578
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/networking/guide/b_15cucnext/b_14cucnetx_chapter_0101.html
retrieved_at: 2026-08-17T03:33:21.231977+00:00
---

Networking Guide for Cisco Unity Connection Release 15

# Networking Guide for Cisco Unity Connection Release 15

Updated: December 18, 2023

Chapter: Cross-Server Sign-In, Transfers, and Live Reply

## Chapter: Cross-Server Sign-In, Transfers, and Live Reply

# Cross-Server Sign-In, Transfers, and Live Reply

## Introduction

This chapter describes the cross-server sign-in, transfer, and live reply features available between Cisco Unity Connection
                           locations in a site, between Unity Connection locations in different sites linked by an intersite link, and between Cisco Unity
                           and Unity Connection locations in sites linked by an intersite link. The chapter also covers the procedure to configure the
                           cross-server feature.

## Overview of
                        	 Cross-Server Sign-In, Transfer, and Live Reply

In order to limit replication traffic and keep the directory
                           		size manageable, only a subset of user information is replicated from the home
                           		location of the user to other networked locations. For this reason, only the
                           		home location of the user has information about call transfer settings,
                           		greetings, and other specific details for the user. In order for the location
                           		to properly handle calls destined for a user on a different location, it must
                           		hand off the call to the home location of the user. The purpose of the
                           		cross-server feature is to make the user experience in a networked environment
                           		almost the same as in a single server environment, as shown in Table 1 .

Feature

Description

Cross-server sign-in

Cross-server sign-in allows administrators to provide users who
                                       				  are homed on different locations with one phone number that they can call to
                                       				  sign in. When calling from outside the organization, users call the same
                                       				  number, regardless of which is the home server, and are transferred to the
                                       				  applicable home server to sign in.

Cross-server transfer

Cross-server transfer enables calls from the automated attendant
                                       				  or from a directory handler of one location to be transferred to a user on
                                       				  another location, according to the call transfer and screening settings of the
                                       				  called user.

Cross-server live reply

Cross-server live reply allows users who listen to their
                                       				  messages by phone to reply to a message from a user on another location by
                                       				  transferring to the user (according to the call transfer and screening settings
                                       				  of the called user).

Although the cross-server features are distinct features, they
                           		all use the same underlying functionality—an enhanced supervised call transfer:

The location on which a sign-in, transfer, or live reply
                                 			 originates puts the caller on hold and calls the receiving location by dialing
                                 			 a phone number designated as the cross-server dial string for the receiving
                                 			 location.

When the receiving location answers, the originating location
                                 			 sends a sequence of DTMF tones that identify the call as a handoff request.

The receiving location responds with a sequence of DTMF tones,
                                 			 and the originating location hands off the call to the receiving location for
                                 			 processing.

At this point the functionality is the same as if the call had
                           		originated on the receiving location.

In this chapter, an originating location is defined as a server
                           		(or cluster) that calls other locations. A receiving location is defined as a
                           		server (or cluster) that answers a cross-server call.

Cross-server dial strings are not synchronized between
                           		locations. Each originating location can be configured with a dial string for
                           		each receiving location. Note that if an originating location is configured for
                           		multiple phone system integrations, you must select a dial string that all
                           		phone system integrations can use to reach the receiving location.

### Search Space Considerations for Cross-Server Sign-In, Transfers, and Live Reply

When a user dials the pilot number of a Unity Connection location that is not his or her home server, the answering location
                              processes the call according to its call management plan. A search space is assigned to the call by the first call routing
                              rule that the call matches. At each subsequent processing step, the search scope of the call may change. Unity Connection
                              uses the search space that is assigned to the call at the point that the call reaches the Attempt Sign-In conversation to
                              identify which user is trying to sign in. If a user calls from an extension that is in a partition that is not a member of
                              this search space, the call is not identified as coming from the user. If the extension of the user overlaps with an extension
                              in another partition that also appears in this search space, the call is identified as coming from the first object that Unity
                              Connection finds when searching the partitions in the order in which they appear in the search space. Check the direct routing
                              rules on each Unity Connection location that handles incoming sign-in calls from remote users to determine the search space
                              that is set by the rule or other call management object that sends calls to the Attempt Sign-In conversation. If the partitions
                              that contain remote users are not a part of this search space, cross-server sign-in does not work, even if it is enabled.

Also note that for cross-server calls from one Unity Connection location to another Unity Connection location (either in the
                              same site or in a remote site), a mismatch between the search space that is applied to the call on the originating location
                              and the search space that is applied on the receiving location can cause problems for cross-server sign-ins and cross-server
                              transfers. A match could be made on the search scope on the originating location that cannot be made on a different search
                              scope on the receiving location. For this reason, you should verify that the same search scope is configured on both originating
                              and receiving locations. For example, call routing rules can be used to direct cross-server calls on the receiving location
                              to the appropriate search space based on the cross-server dial string that is used to reach that location.

For cross-server live reply, as with any live reply attempt, a Unity Connection user can only call the sender if the sender
                              is in a partition that is a member of the search space configured for the user.

## Cross-Server Sign-In

The cross-server sign-in feature enables users who are calling from outside the organization to call the same number regardless
                           of which server they are homed on, and they are transferred to the applicable home server to sign in. If you do not enable
                           cross-server sign-in, users need to call the phone number of their home server to sign in.

The process for a cross-server sign-in call is as follows:

A user calls the server configured for cross-server sign-in. The user is identified by the calling number or is asked to enter
                                 his or her ID.

The server looks up the caller ID in the database to determine whether the account is homed on the local server or on a networked
                                 server.

If the user account is homed on the local server, the sign-in proceeds as usual.

If the user account is homed on another server, the conversation plays a “One moment please” prompt (if configured to do so),
                                       puts the user on hold, and calls the user home server using the same port that the user called in on. Note that if the user
                                       is calling from his or her primary or alternate extension, the “One moment please” prompt is typically the first prompt that
                                       the user hears.

When the receiving server answers, the originating server sends a sequence of DTMF tones that identifies the call as a cross-server
                                       sign-in.

The receiving location responds with a sequence of DTMF tones.

The originating location hands off the call to the receiving server for processing. The conversation on the receiving server
                                 prompts for the user password. At this point, the behavior is as though the user had called the receiving server directly.

The intended use of this feature is limited to users calling in from outside your organization. Although cross-server sign-in
                           transfers internal calls to the home server, doing so for a large number of users increase the load on the servers. Therefore,
                           user phones should always be configured so that the “Messages” or voicemail speed-dial button calls the home server of the
                           user directly. When moving a user account from one server to another, update the phone system configuration for the user accordingly.

In case of a video call, when two Unity Connection locations are linked by an intersite, intrasite link, or HTTPS network,
                           then if a user from one Unity Connection location attempts to sign-in to another Unity Connection location, the call is downgraded
                           to audio.

### Prerequisites for Enabling Cross-Server Sign-In

If your Cisco Voicemail Organization includes Cisco Unity servers, all of the networked Cisco Unity servers that you configure
                              as originating locations for cross-server sign-in must be configured to be in the same dialing domain as the Cisco Unity site
                              gateway. The dialing domain is configured on the Network > Primary Location > Profile page in the Cisco Unity Administrator.

### Task List for
                           	 Enabling Cross-Server Sign-In

Whether you are configuring a single Unity Connection site, an
                              		organization that contains two Unity Connection sites, or an organization that
                              		contains a Unity Connection site and a Cisco Unity site, the same basic set of
                              		tasks applies. Use the following task list to enable cross-server sign-in. The
                              		cross references take you to detailed procedures.

Determine which locations are originating locations and which
                                    			 are the receiving locations for cross-server sign-in. Often a single location
                                    			 is designated as the originating location that all users call into from outside
                                    			 the organization, and all other location are designated as receiving locations;
                                    			 however, this does not have to be the case. A single location also may be both
                                    			 an originating location and a receiving location.

For each originating location, make a list of the phone numbers
                                    			 that the location must dial to reach the receiving location servers.

Configure each receiving location so that it can handle incoming
                                    			 cross-server handoff requests.

If the receiving location is a Cisco Unity Connection server,
                                          				  see the “Configuring
                                             					 a Unity Connection Receiving Location to Accept Cross-Server Handoff Requests”
                                             					 section on page 6-4 .

If the receiving location is a Cisco Unity server, see the “Verifying
                                             					 a Receiving Cisco Unity Location Routes Calls to the Opening Greeting” section
                                             					 on page 6-5 .

If Cisco Unity Connection locations receive cross-server handoff
                                    			 requests from Cisco Unity servers, configure the Unity Connection locations to
                                    			 allow cross-server DTMF sequences that begin with #. See the “Configuring
                                       				a Unity Connection Receiving Location to Allow Cross-Server DTMF Sequences from
                                       				Cisco Unity Locations” section on page 6-5 .

For each originating location, enable the cross-server sign-in
                                    			 feature and enter the pilot numbers of the receiving locations from the list
                                    			 that you created in Task 2 .

If the location is a Cisco Unity Connection server, see the “Configuring
                                             					 a Unity Connection Originating Location to Perform Cross-Server Sign-In
                                             					 Requests” section on page 6-7 .

If the location is a Cisco Unity server, see the “Configuring
                                             					 a Cisco Unity Originating Location to Perform Cross-Server Sign-In Requests”
                                             					 section on page 6-7 .

Test the cross-server sign-in functionality. See the “Testing
                                       				Cross-Server Sign-In” section on page 6-8 .

#### Configuring a
                              	 Unity Connection Receiving Location to Accept Cross-Server Handoff
                              	 Requests

By default, each Unity Connection server is configured to ignore
                                 		cross-server handoff requests. To enable cross-server features, you must
                                 		configure the receiving location to accept requests and also verify that the
                                 		location routes incoming cross-server calls to a call handler. Do the following
                                 		two procedures toconfigure each receiving Unity Connection location to accept
                                 		handoffs. (Doing so allows the location toreceive handoffs of all
                                 		types-sign-in, transfer, and live reply.)

#### Configuring a
                              	 Unity Connection Receiving Location to Accept Cross-Server Handoff
                              	 Requests

Step 1

In Cisco Unity Connection Administration, on a location that
                                             			 accepts cross-server handoffs for users who are homed on that location (the
                                             			 receiving location), expand System Settings > Advanced and select Conversations .

Step 2

Check the Respond to Cross-Server Handoff Requests check box.

Step 3

Repeat the procedure on all remaining Unity Connection receiving
                                             			 locations.

#### Verifying Call
                              	 Routing Rules are Set to Route Calls to a Call Handler Greeting

Step 1

In Cisco Unity Connection Administration, on a location that
                                             			 accepts cross-server handoffs, expand Call
                                                   				  Management > Call
                                                   				  Routing and select Direct Routing Rules .

Step 2

Select the display name of the routing rule that applies to
                                             			 incoming cross-server calls from originating locations.

Step 3

Verify that calls that match the rule are routed to a call
                                             			 handler.

Step 4

Repeat the procedure on all remaining Unity Connection receiving
                                             			 locations.

#### Verifying a
                              	 Receiving Cisco Unity Location Routes Calls to the Opening Greeting

In order to accept cross-server handoff requests, each
                                    		  Cisco Unity server must be configured to route calls to the Opening Greeting
                                    		  call handler. (This is the default when Cisco Unity is initially installed.)

Do the following procedure to verify that call routing rules are set
                                    		  to route calls to the Opening Greeting

Step 1

In the Cisco Unity Administrator, on a location that accepts
                                             			 cross-server sign-in handoffs, expand Call
                                                   				  Routing > and
                                                   				  select > Direct
                                                   				  Calls .

Step 2

Verify that incoming cross-server calls from originating
                                             			 locations are routed to the Opening Greeting.

The Default Call Handler routing rule (which cannot be deleted
                                                				or modified) sends calls to the Opening Greeting. Therefore, if you have not
                                                				added any routing rules, the server is already set to correctly process
                                                				cross-server calls.

Step 3

Repeat the procedure on all remaining Cisco Unity receiving
                                             			 locations.

#### Configuring a
                              	 Unity Connection Receiving Location to Allow Cross-Server DTMF Sequences from
                              	 Cisco Unity Locations

The sequence of DTMF tones that an originating Cisco Unity
                                    		  location sends to the receiving location begins with # (pound). By default, the
                                    		  Unity Connection opening greeting and other call handlers are configured to
                                    		  ignore any additional caller input following a # key. In such a configuration,
                                    		  all cross-server handoffs fail.

You have a couple of options for changing the behavior on a
                                    		  Unity Connection receiving location so that cross-server handoffs are performed
                                    		  successfully:

Change the opening greeting (or other existing call handler that
                                          				receives the cross-server handoff calls based on your routing rule
                                          				configuration) to allow additional input following a # key.

Create a new call handler and direct-call routing rule
                                          				specifically to handle cross-server calls. The new call handler must allow
                                          				additional input after the # key. The direct call routing rule should route
                                          				calls to the new call handler based on criteria that apply to cross-server
                                          				calls—the calling number of any originating Cisco Unity location, for example,
                                          				or the cross-server dial string that the originating locations dial to reach
                                          				the receiving location. (If you do not want other calls to match the routing
                                          				rule, select criteria that are unique to cross-server calls.)

Do the following procedure on each Unity Connection receiving
                                    		  location to configure the opening greeting or other call handler to allow
                                    		  additional input after the # key, and, optionally, to create a new direct-call
                                    		  routing rule.

Step 1

Sign in to Cisco Unity Connection Administration for a location
                                             			 that accept across-server sign-in handoffs. Expand Call Management and select System Call Handlers .

Step 2

On the Search Call Handlers page, you can do either of the
                                             			 following:

Select the display name of the opening greeting or other call
                                                      					 handler that you want to modify. Skip to Step 6 .

Select Add New to create a new call handler specifically for
                                                      					 cross-server calls. See the Step 3 .

Step 3

On the New
                                             			 Call Handler page, enter basic settings, as applicable. (For more information
                                             			 on each field, see Help> This Page ).

Step 4

To configure
                                             			 the call handler to accept the cross-server DTMF sequence:

In the Edit menu, select Caller Input .

On the Caller Input page, select # and uncheck the Ignore Additional Input check box.

Select Save .

Step 5

Create a new
                                             			 Direct Call Routing Rule to send calls from the Cisco Unity servers to the call
                                             			 handler:

Expand Call Management > Call Routing and select Direct Routing Rules .

On the Direct Routing Rules page, select Add New .

On the New Direct Rule page, enter the name of the new rule in
                                                      					 the Display Name field and select Save .

On the Edit Direct Rule page, for the Send Call To field, select Call Handler and the name of the call handler you added in Step 2 .

Select Save .

Under Routing Rule Conditions, select Add New .

Configure the routing rule condition to match cross-server calls
                                                      					 from Cisco Unity servers. For example, use the Calling Number field to match
                                                      					 the phone numbers of the Cisco Unity ports that answer user calls.

Select Save .

On the Edit menu, select Edit Direct Routing Rule .

Repeat f . through i . for each additional
                                                      					 number or number pattern that you need to match cross-server calls.

Step 6

Repeat the
                                             			 procedure on all remaining Unity Connection receiving locations.

#### Configuring a
                              	 Unity Connection Originating Location to Perform Cross-Server Sign-In
                              	 Requests

By default, a Unity Connection location does not attempt to
                                    		  perform a cross-server sign-in for users homed on any other locations.

Step 1

In Cisco Unity Connection Administration, on a location that
                                             			 handles sign-in calls from remote users (the originating location), expand Networking and select Locations .

Step 2

On the Search Locations page, select the Display Name of a
                                             			 remote location that accepts cross-server sign-in requests for users homed on
                                             			 this location (or the receiving location).

Step 3

On the Edit Location page for the receiving location, initiate
                                             			 cross-server features to the receiving location:

To enable cross-server sign-in to the remote location, check the Allow Cross-Server Sign-In to this Remote Location check
                                                   				  box.

Enter the dial string that this location uses to call the
                                                   				  receiving location when performing the handoff (for example, the pilot number
                                                   				  of the home server).

Step 4

Repeat Step 2 and Step 3 to
                                             			 configure each receiving location that accepts cross-server sign-in handoffs
                                             			 from this location.

Tip

Step 5

Repeat the procedure on all remaining Unity Connection originating
                                             			 locations.

#### Configuring a
                              	 Cisco Unity Originating Location to Perform Cross-Server Sign-In
                              	 Requests

By default, a Cisco Unity originating location do not attempt to
                                    		  perform a cross-server sign-in for users homed on any other locations. Do the
                                    		  following procedure to enable cross-server sign-in on any Cisco Unity
                                    		  originating locations.

Step 1

In the Cisco Unity Administrator, expand Network > and select > Dialing Domain
                                                   				  Options .

If the Dialing Domain Options link is unavailable on the system,
                                                            				  you must first configure the dialing domain on the Primary Location Settings
                                                            				  page in the Cisco Unity Administrator.

Step 2

In the Cross Server Logon section, select the Subscribers Dial the Same Number to Log On to
                                                				Cisco Unity check box.

Step 3

In the Pilot Numbers for Cross-Server Logon, Transfer, and Live
                                             			 Reply section, enter the pilot number in the Dial String field for each server
                                             			 that is displayed in the table. (Note that the pilot numbers that you enter are
                                             			 stored in the SQL Server database UnityDb on the Cisco Unity server. Therefore,
                                             			 if the system is using failover, the pilot numbers are replicated to the
                                             			 secondary server.)

Step 4

Check the Play Prompt During Cross-Server Logon, Transfer, and Live Reply
                                                				so That Callers Know Something Is Happening check box. Although
                                             			 playing the “One moment please” prompt is optional, you must check the check
                                             			 box because the cross-server process can take several seconds before the
                                             			 receiving server prompts users to enter their passwords.

Step 5

Select Save .

Step 6

Repeat the procedure on all remaining Cisco Unity originating
                                             			 locations.

#### Testing
                              	 Cross-Server Sign-In

You must test cross-server sign-in before allowing users to use
                                    		  the feature. For failover systems, first test that the primary destination
                                    		  servers answer cross-server calls. Then manually fail over the destination
                                    		  servers to verify that the secondary server answers cross-server calls. If the
                                    		  destination servers are properly configured for failover, the secondary server
                                    		  should answer cross-server calls when the primary server is unavailable.

Do the following procedure to test cross-server sign-in:

Step 1

Create a new user account (or use an existing account) on each
                                             			 of the destination servers for testing purposes. Be sure to verify that the
                                             			 user account information has replicated to all of the servers that you are
                                             			 testing. The time that it takes for the user data to replicate depends on your
                                             			 network configuration and replication schedule.

Step 2

For each user account, call the pilot number for the server
                                             			 configured for cross-server sign-in, and attempt to sign in. Verify that:

The “One moment please” prompt is played (if configured to do
                                                      					 so).

You successfully sign in.

## Cross-Server Transfers

A cross-server transfer is a special kind of supervised transfer that passes control of a call from the automated attendant
                           or a directory handler to the home server of the called user.

A caller calls a Cisco Unity or Unity Connection server on which an audio text application has been configured.

The caller does either of the following:

In a call handler (such as the opening greeting), enters the extension of a user on another server.

In a directory handler, spells the name of a user on another server.

The server that is handling the call puts the caller on hold, and calls the home server of the user.

When the receiving server answers, the originating server sends a sequence of DTMF tones that identify the call as a cross-server
                                 transfer.

The receiving server responds with a sequence of DTMF tones.

The originating server hands off the call to the receiving server for processing. At this point, the behavior is as though
                                 the caller had directly called the automated attendant or directory handler on the receiving server.

In case of a video call, when two Unity Connection locations are linked by an intersite, intrasite link, or HTTPS network,
                                 then if a user from one Unity Connection location attempts to cross-server transfer, the call is downgraded to audio with
                                 respect to supervise transfer.

In case of a video call, when two Unity Connection locations are linked by an intersite, intrasite link, or HTTPS network,
                                 then if a user from one Unity Connection location attempts to cross-server transfer, the call gets established video only
                                 with respect to release to switch.

When cross-server transfers have been configured, user call transfer, call screening, call holding, and announce features
                           are available.

### Prerequisites for
                           	 Enabling Cross-Server Transfers

If your Cisco voicemail organization includes networked
                              		Cisco Unity servers:

All of the Cisco Unity servers that you configure as originating
                                    			 locations for cross-server transfers must be configured to be in the same
                                    			 dialing domain as the Cisco Unity site gateway. The dialing domain is
                                    			 configured on the Network > Primary Location > Profile page in the
                                    			 Cisco Unity Administrator.

The addressing, directory handler, and automated attendant
                                    			 search scopes for each Cisco Unity server must be set to the dialing domain or
                                    			 global directory. For details, see the “Setting the Addressing, Directory
                                    			 Handler, and Automated Attendant Search Scopes” section in the “Digital
                                    			 Networking” chapter of the applicable Networking Guide for Cisco Unity , available at http://www.cisco.com/en/US/products/sw/voicesw/ps2237/products_feature_guides_list.html .

### Task List for
                           	 Enabling Cross-Server Transfers

Whether you are configuring a single Unity Connection site, an
                              		organization that contains two Unity Connection sites, or an organization that
                              		contains a Unity Connection site and a Cisco Unity site, the same basic set of
                              		tasks applies. Use the following task list to enable cross-server transfers.
                              		The cross references take you to detailed procedures.

Determine whether each location is an originating location, a
                                    			 receiving location, or both.

For each originating location, make a list of the phone numbers
                                    			 the location must dial to reach the receiving location servers.

Configure each receiving location so that it can handle incoming
                                    			 cross-server handoff requests.

If the receiving location is a Unity Connection server, see the
                                          				  “Configuring a Unity Connection Receiving Location to Accept Cross-Server
                                          				  Handoff Requests” section on page 6-11.

If the receiving location is a Cisco Unity server, see the “Verifying
                                             					 a Receiving Cisco Unity Location Routes Calls to the Opening Greeting” section
                                             					 on page 6-11 .

If Unity Connection locations receives cross-server handoff
                                    			 requests from Cisco Unity servers, configure the Unity Connection locations to
                                    			 allow cross-server DTMF sequences that begin with #. See the “Configuring
                                       				a Unity Connection Receiving Location to Accept Cross-Server Handoff Requests”
                                       				section on page 6-4 .

For each originating location, enable the cross-server transfer
                                    			 feature and enter the pilot numbers of the receiving locations from the list
                                    			 that you created in Task 2 .

If the location is a Unity Connection server, see the “Configuring
                                             					 Unity Connection Originating Location to Perform Cross-Server Transfer
                                             					 Requests” section on page 6-13 .

If the location is a Cisco Unity server, see the “Configuring
                                             					 a Cisco Unity Originating Location to Perform Cross-Server Transfer Requests”
                                             					 section on page 6-13 .

Test the cross-server transfer functionality. See the “Testing
                                       				Cross-Server Transfer” section on page 6-14 .

#### Configuring Cross-Server Transfers during Call Forward to Cisco Unity Connection

Do the following procedure to configure cross-server transfers during call forward to Cisco Unity Connection:

Step 1

To view the configuration of cross-server transfers during call forward, execute the following command:

```
run cuc dbquery unitydirdb select fullname,name,parentid,valuebool,value from vw_Configuration where name like 'HandoffForwardRemoteForward'
```

If the command results a configured table entry, it means the feature is configured on Cisco Unity Connection. Otherwise,
                                                go to Step 2 to create a configuration entry.

In configured table entry, check the value of  "valuebool" parameter. If valuebool is one, it means the feature is enabled
                                                for Cisco Unity Connection. Otherwise, go to Step 3 to enable the feature.

Step 2

Create the configuration entry using the following command:

```
run cuc dbquery unitydirdb execute procedure csp_ConfigurationCreate(pName='HandoffForwardRemoteForward'::lvarchar, pParentFullName='System.Conversations.CrossBox'::lvarchar, pType=11, pValueBool=0, pRequiresRestart=1)
```

Step 3

Enable the cross-server transfers during call forward using the following command:

```
run cuc dbquery unitydirdb execute procedure csp_ConfigurationModify(pName='HandoffForwardRemoteForward'::lvarchar, pParentFullName='System.Conversations.CrossBox'::lvarchar, pValueBool=1)
```

Step 4

Disable the cross-server transfers during call forward using the following command:

```
run cuc dbquery unitydirdb execute procedure csp_ConfigurationModify(pName='HandoffForwardRemoteForward'::lvarchar, pParentFullName='System.Conversations.CrossBox'::lvarchar, pValueBool=0)
```

In case of a cluster, execute the commands only on publisher server and make sure that database replication is working fine
                                                                  for the cluster.

Service restart is not required after executing the above commands.

#### Configuring a
                              	 Unity Connection Receiving Location to Accept Cross-Server Handoff
                              	 Requests

By default, each Unity Connection server is configured to ignore
                                    		  cross-server handoff requests. To enable cross-server features, you must
                                    		  configure the receiving location to accept requests and also verify that the
                                    		  location routes incoming calls to a call handler.

Do the following procedure configure a Unity Connection receiving
                                    		  location

Step 1

Sign in to Cisco Unity Connection Administration for a location
                                             			 that accepts cross-server handoffs for users homed on that location (the
                                             			 receiving location). Expand System Settings > Advanced and select Conversations .

Step 2

Check the Respond to Cross-Server Handoff Requests check box.

Step 3

Repeat the procedure on all remaining Unity Connection receiving
                                             			 locations.

#### Verifying Call
                              	 Routing Rules are Set to Route Calls to a Call Handler Greeting

Step 1

Sign in to Cisco Unity Connection Administration for a location
                                             			 that accepts cross-server handoffs. Expand Call
                                                   				  Management > Call
                                                   				  Routing and select Direct Routing Rules .

Step 2

Select the display name of the routing rule that applies to
                                             			 incoming cross-server calls from originating locations.

Step 3

Verify that calls that match the rule are routed to a call
                                             			 handler.

Step 4

Repeat the procedure on all remaining Unity Connection receiving
                                             			 locations.

#### Verifying a
                              	 Receiving Cisco Unity Location Routes Calls to the Opening Greeting

In order to accept cross-server handoff requests, each
                                    		  Cisco Unity server must be configured to route calls to the opening greeting
                                    		  call handler. (This is the default when Cisco Unity is initially installed.) Do
                                    		  the following procedure on each of the receiving Cisco Unity servers to verify
                                    		  that the call routing rules are set properly to accept handoffs.

For failover systems, do the procedure on both the primary and
                                                			 secondary servers.

Step 1

Sign in to Cisco Unity Administrator for a location that accepts
                                             			 cross-server transfer handoffs. Expand Call
                                                   				  Routing > Direct
                                                   				  Calls .

Step 2

Verify that incoming cross-server calls from originating
                                             			 locations are routed to the Opening Greeting.

The Default Call Handler routing rule (which cannot be deleted
                                                				or modified) sends calls to the Opening Greeting. Therefore, if you have not
                                                				added any routing rules, the server is already set to correctly process
                                                				cross-server calls.

Step 3

Repeat the procedure on all remaining Cisco Unity receiving
                                             			 locations.

#### Configuring a
                              	 Unity Connection Receiving Location to Allow Cross-Server DTMF Sequences from
                              	 Cisco Unity Locations

The sequence of DTMF tones that an originating Cisco Unity
                                    		  location sends to the receiving location begins with # (pound). By default, the
                                    		  Unity Connection opening greeting and other call handlers are configured to
                                    		  ignore any additional caller input following a # key. In such a configuration,
                                    		  all cross-server handoffs fail.

You have a couple of options for changing the behavior on a
                                    		  Unity Connection receiving location so that cross-server handoffs are performed
                                    		  successfully:

Change the opening greeting (or other existing call handler that
                                          				receives the cross-server handoff calls based on your routing rule
                                          				configuration) to allow additional input.

Create a new call handler and direct-call routing rule
                                          				specifically to handle cross-server calls. The direct call routing rule should
                                          				route calls to the new call handler based on criteria that apply to
                                          				cross-server calls—the calling number of any originating Cisco Unity location,
                                          				for example, or the cross-server dial string that the originating locations
                                          				dial to reach the receiving location. (If you do not want other calls to match
                                          				the routing rule, select criteria that are unique to cross-server calls.)

Do the following procedure on each Unity Connection receiving
                                    		  location to configure the opening greeting or other call handler to allow
                                    		  additional input after the # key, and, optionally, to create a new direct-call
                                    		  routing rule.

Step 1

Sign in to Cisco Unity Connection Administration for a location
                                             			 that accepts cross-server transfer handoffs. Expand Call Management and select System Call Handlers .

Step 2

On the Search Call Handlers page, select the display name of the
                                             			 opening greeting or other call handler that you want to modify, or select Add New to create a new call handler specifically
                                             			 for cross-server calls.

Step 3

If you did not create a new call handler in Step 2 ,
                                             			 skip to Step 6 . If you
                                             			 created a new call handler in Step 2 , on the
                                             			 New Call Handler page, enter basic settings, as applicable. (For field
                                             			 information, on the Help menu, select This Page .)

Step 4

To configure the call handler to accept the cross-server DTMF
                                             			 sequence, do the following substeps:

On the Edit menu, select Caller Input .

On the Caller Input page, select # .

Uncheck the Ignore Additional Input check box.

Select Save .

Step 5

If you created a new call handler in Step 2 , create
                                             			 a new direct-call routing rule to send calls from the Cisco Unity servers to
                                             			 the call handler for processing:

Expand Call Management > Call Routing , then select Direct Routing Rules .

On the Direct Routing Rules page, select Add New .

On the New Direct Rule page, enter the name of the new rule in
                                                   				  the Display Name field.

Select Save .

On the Edit Direct Rule page, for Send Call To, select Call Handler , then select the name of the call handler you
                                                   				  added in Step 2 .

Select Save .

Under Routing Rule Conditions, select Add New .

Configure the routing rule condition to match cross-server calls
                                                   				  from Cisco Unity servers. For example, use the Calling Number field to match
                                                   				  the phone numbers of the Cisco Unity ports that answer user calls.

Select Save .

On the Edit menu, select Edit Direct Routing Rule .

Repeat g . through j . for
                                                   				  each additional number or number pattern that you need to match cross-server
                                                   				  calls.

Step 6

Repeat the procedure on all remaining Unity Connection receiving
                                             			 locations.

#### Configuring Unity
                              	 Connection Originating Location to Perform Cross-Server Transfer
                              	 Requests

By default, a Unity Connection location do not attempt to
                                    		  perform a cross-server transfer. Note that when you enable cross-server
                                    		  transfers on Unity Connection, cross-server live reply is automatically
                                    		  enabled. Do the following procedure to enable cross-server transfer and live
                                    		  reply on any Unity Connection originating locations.

Do the following procedure to configure a Unity Connection originating
                                    		  location to perform cross-server transfer and live reply handoff requests:

Step 1

In Cisco Unity Connection Administration, on a location that
                                             			 transfers calls to remote users (the originating location), expand Networking and select Locations .

Step 2

On the Search Locations page, select the Display Name of a
                                             			 remote location that accepts cross-server transfer handoffs for users who are
                                             			 homed on this location (the receiving location).

Step 3

On the Edit Location page for the receiving location, do the
                                             			 following to initiate cross-server features to this receiving location:

To enable cross-server transfer and live reply to the remote
                                                   				  location, check the Allow Cross-Server Transfer to this Remote Location check
                                                   				  box.

Enter the dial string that this location uses to call the
                                                   				  receiving location when performing the handoff (for example, the pilot number
                                                   				  of the receiving location).

Step 4

Repeat Step 2 and Step 3 for each
                                             			 receiving location that accepts cross-server transfer handoffs from this
                                             			 location.

Tip

Step 5

Repeat the
                                             			 procedure on all remaining Unity Connection originating locations.

#### Configuring a
                              	 Cisco Unity Originating Location to Perform Cross-Server Transfer
                              	 Requests

By default, a Cisco Unity originating location do not attempt to
                                    		  perform cross-server transfers to any other locations. Do the following
                                    		  procedure to enable cross-server transfers on any Cisco Unity originating
                                    		  locations.

Step 1

In the Cisco Unity Administrator, go to the Network > Dialing Domain
                                                   				  Options page.

If the Dialing Domain Options link is unavailable on the system,
                                                            				  you must configure the dialing domain on the Primary Location Settings page in
                                                            				  the Cisco Unity Administrator.

Step 2

Select the Cross-server Transfer: Pass Control to the Called Subscriber’s
                                                				Cisco Unity Server check box. (Selecting Release Calls to the Phone System
                                             			 disables cross-server transfers originating from this server. Instead of
                                             			 handing off calls to the home server of the user, Cisco Unity attempts a
                                             			 release transfer to the Cross-Server Transfer Extension configured for the
                                             			 user. This fails if a Unity Connection user does not have a Cross-Server
                                             			 Transfer Extension configured.)

Step 3

In the Pilot Numbers for Cross-Server Logon, Transfer, and Live
                                             			 Reply section, enter the pilot number in the Dial String field for each server
                                             			 displayed in the table. (Note that the pilot numbers that you enter are stored
                                             			 in the SQL Server database UnityDb on the Cisco Unity server. Therefore, if the
                                             			 system is using failover, the pilot numbers are replicated to the secondary
                                             			 server.)

Step 4

Select the Play Prompt During Cross-Server Logon, Transfer, and Live Reply
                                                				so That Callers Know Something Is Happening check box. Although
                                             			 playing the “One moment please” prompt is optional, you should check the check
                                             			 box because the cross-server process can take several seconds before the caller
                                             			 is transferred.

Step 5

Select Save .

Step 6

Repeat the procedure on all remaining Cisco Unity originating
                                             			 locations.

#### Testing
                              	 Cross-Server Transfer

You should test the cross-server transfers before allowing
                                    		  callers to use the feature. For failover systems, first test that the primary
                                    		  destination servers answer cross-server calls. Then manually fail over the
                                    		  destination servers to verify that the secondary server answers cross-server
                                    		  calls. If the destination servers are properly configured for failover, the
                                    		  secondary server should answer cross-server calls when the primary server is
                                    		  unavailable.

Do the following procedure to test cross-server transfer:

Step 1

Create a new user account (or use an existing account) on each
                                             			 of the destination servers for testing purposes. Be sure to verify that the
                                             			 user account information has replicated to all of the servers that you are
                                             			 testing. The time that it takes for the user data to replicate depends on your
                                             			 network configuration and replication schedule.

Step 2

For each user account, call the pilot number for the server
                                             			 configured for cross-server transfer, and enter the user extension at the
                                             			 opening greeting. Verify that:

The “One moment please” prompt is played (if configured to do
                                                      					 so).

The call is transferred to the user phone or the greeting,
                                                      					 according to the call transfer settings of the called user.

## Cross-Server Live Reply

Live reply, when enabled, allows a user who is listening to messages by phone to reply to a message from another user by transferring
                           to the user. Note that whether users have access to live reply is controlled by the class of service.

When cross-server live reply is enabled:

After listening to a message from a user on another networked location, the message recipient selects to call the user who
                                 left the message.

Note that if identified subscriber messaging (ISM) is disabled on the location that recorded the message, the cross-server
                                 live reply option is only available for messages that are sent by users who sign in and address and send the message from
                                 their mailboxes.

The originating location puts the user on hold and looks up the extension in the database to determine whether the user who
                                 is being replied to is on the same server or is on another networked location. If the user is on the same server, processing
                                 proceeds as usual.

However, if the user who is being replied to is on another location, the originating location calls the applicable receiving
                                 location.

When the receiving location answers, the originating location sends a sequence of DTMF tones that identify the call as a cross-server
                                 live reply.

The receiving location responds with a sequence of DTMF tones.

The originating location hands off the call to the receiving location for processing.

### Prerequisites:
                           	 Enabling Cross-Server Live Reply

Users must belong to a class of service for which live reply
                                    			 between users is enabled. For Cisco Unity Connection users, live reply between
                                    			 users is enabled on the Class of Service > Edit Class of Service page in
                                    			 Cisco Unity Connection Administration, by selecting the Users Can Reply to Messages from Other Users by Calling Them check box.

### Task List for
                           	 Enabling Cross-Server Live Reply

Use the following task list to enable cross-server live reply
                              		between Cisco Unity and Unity Connection sites, or to enable cross-server
                              		transfers and live reply between Unity Connection locations (either in a single
                              		site or between two Unity Connection sites). The cross references take you to
                              		detailed procedures.

Determine whether each location is an originating location, a
                                    			 receiving location, or both.

For each originating location, make a list of the phone numbers
                                    			 the location must dial to reach the receiving location servers.

Configure each receiving location so that it can handle incoming
                                    			 cross-server handoff requests.

If the receiving location is a Cisco Unity Connection server,
                                          				  see the “Configuring
                                             					 a Unity Connection Receiving Location to Allow Cross-Server DTMF Sequences from
                                             					 Cisco Unity Locations” section on page 6-5 .

If the receiving location is a Cisco Unity server, see the “Verifying
                                             					 That a Receiving Cisco Unity Location Routes Calls to the Opening Greeting”
                                             					 section on page 6-17 .

If Unity Connection locations receive cross-server handoff
                                    			 requests from Cisco Unity servers, configure the Unity Connection locations to
                                    			 allow cross-server DTMF sequences that begin with #. See the “Configuring
                                       				a Unity Connection Originating Location to Perform Cross-Server Sign-In
                                       				Requests” section on page 6-7 .

For each originating location, enable the applicable
                                    			 cross-server features and enter the pilot numbers of the receiving locations
                                    			 from the list that you created in Task 2 .

If the location is a Cisco Unity Connection server, see the “Configuring
                                             					 a Cisco Unity Originating Location to Perform Cross-Server Sign-In Requests”
                                             					 section on page 6-7 .

If the location is a Cisco Unity server, see the “Configuring
                                             					 a Cisco Unity Originating Location to Perform Cross-Server Live Reply Requests”
                                             					 section on page 6-19 .

Test the cross-server live reply functionality. See the “Testing
                                       				Cross-Server Sign-In” section on page 6-8 .

### Procedures: Enabling Cross-Server Live Reply

#### Configuring a
                              	 Unity Connection Receiving Location to Accept Cross-Server Handoff
                              	 Requests

By default, each Unity Connection server is configured to ignore
                                    		  cross-server handoff requests. To enable cross-server features, you must
                                    		  configure the receiving location to accept requests and also verify that the
                                    		  location routes incoming calls to a call handler.

Step 1

In Cisco Unity Connection Administration, on a location that
                                             			 accepts cross-server handoffs for users who are homed on that location (the
                                             			 receiving location), expand System Settings > Advanced and select Conversations .

Step 2

Check the Respond to Cross-Server Handoff Requests check box.

Step 3

Repeat the procedure on all remaining Unity Connection receiving
                                             			 locations.

#### Verifying Call
                              	 Routing Rules are Set to Route Calls to a Call Handler Greeting

Step 1

In Cisco Unity Connection Administration, on a location that
                                             			 accepts cross-server handoffs, expand Call
                                                   				  Management > Call
                                                   				  Routing and select Direct Routing Rules .

Step 2

Select the display name of the routing rule that applies to
                                             			 incoming cross-server calls from originating locations.

Step 3

Verify that calls that match the rule are routed to a call
                                             			 handler.

Step 4

Repeat the procedure on all remaining Unity Connection receiving
                                             			 locations.

#### Verifying That a
                              	 Receiving Cisco Unity Location Routes Calls to the Opening Greeting

In order to accept cross-server handoff requests, each
                                    		  Cisco Unity server must be configured to route calls to the Opening Greeting
                                    		  call handler. (This is the default when Cisco Unity is initially installed.) Do
                                    		  the following procedure on each of the receiving Cisco Unity servers to verify
                                    		  that the call routing rules are set properly to accept handoffs.

Step 1

In the Cisco Unity Administrator, on a location that accepts
                                             			 cross-server live reply handoffs, go to the Call
                                                   				  Routing > Direct
                                                   				  Calls page.

Step 2

Verify that incoming cross-server calls from originating
                                             			 locations are routed to the Opening Greeting.

The Default Call Handler routing rule (which cannot be deleted
                                                				or modified) sends calls to the Opening Greeting. Therefore, if you have not
                                                				added any routing rules, the server is already set to correctly process
                                                				cross-server calls.

Step 3

Repeat the procedure on all remaining Cisco Unity receiving
                                             			 locations.

#### Configuring a
                              	 Unity Connection Receiving Location to Allow Cross-Server DTMF Sequences from
                              	 Cisco Unity Locations

The sequence of DTMF tones that an originating Cisco Unity
                                    		  location sends to the receiving location begins with # (pound) and includes a
                                    		  second tone that distinguishes the type of handoff (sign-in, transfer, or live
                                    		  reply). By default, the Unity Connection opening greeting and other call
                                    		  handlers are configured to ignore any additional caller input following a #
                                    		  key. In such a configuration, all cross-server handoffs fail.

You have a couple of options for changing the behavior on a
                                    		  Unity Connection receiving location so that cross-server handoffs are performed
                                    		  successfully:

Change the opening greeting (or other existing call handler that
                                          				receive the cross-server handoff calls based on your routing rule
                                          				configuration) to allow additional input.

Create a new call handler and direct-call routing rule
                                          				specifically to handle cross-server calls. The direct call routing rule should
                                          				route calls to the new call handler based on criteria that apply to
                                          				cross-server calls—the calling number of any originating Cisco Unity location,
                                          				for example, or the cross-server dial string that the originating locations
                                          				dial to reach the receiving location. (If you do not want other calls to match
                                          				the routing rule, select criteria that are unique to cross-server calls.)

Do the following procedure on each Unity Connection receiving
                                    		  location to configure the opening greeting or other call handler to allow
                                    		  additional input after the # key, and, optionally, to create a new direct-call
                                    		  routing rule.

Step 1

In Cisco Unity Connection Administration, on a location that
                                             			 accepts cross-server sign-in handoffs, expand Call Management and select System Call Handlers .

Step 2

On the Search Call Handlers page, select the display name of the
                                             			 opening greeting or other call handler that you want to modify, or select Add New to create a new call handler specifically
                                             			 for cross-server calls.

Step 3

If you did not create a new call handler in Step 2 ,
                                             			 skip to Step 6 . If you
                                             			 created a new call handler in Step 2 ,
                                             			 on the New Call Handler page, enter basic settings, as applicable. (For field
                                             			 information, on the Help menu, select This Page .)

Step 4

To configure the call handler to accept the cross-server DTMF
                                             			 sequence, do the following substeps:

In the Edit menu, select Caller Input .

On the Caller Input page, select # .

Uncheck the Ignore Additional Input check box and select Save .

Step 5

If you created a new call handler in Step 2 ,
                                             			 create a new direct-call routing rule to send calls from the Cisco Unity
                                             			 servers to the call handler for processing:

Expand Call Management > Call Routing and select Direct Routing Rules .

On the Direct Routing Rules page, select Add New .

On the New Direct Rule page, enter the name of the new rule in
                                                   				  the Display Name field.

Select Save .

On the Edit Direct Rule page, for Send Call To, select Call Handler , then select the name of the call handler you
                                                   				  added in Step 2 .

Select Save .

Under Routing Rule Conditions, select Add New .

Configure the routing rule condition to match cross-server calls
                                                   				  from Cisco Unity servers. For example, use the Calling Number field to match
                                                   				  the phone numbers of the Cisco Unity ports that answer user calls and select Save .

On the Edit menu, select Edit Direct Routing Rule .

Repeat g . through i . for
                                                   				  each additional number or number pattern that you need to match cross-server
                                                   				  calls.

Step 6

Repeat the procedure on all remaining Unity Connection receiving
                                             			 locations.

#### Configuring a
                              	 Unity Connection Originating Location to Perform Cross-Server Live Reply and
                              	 Transfer Requests

By default, a Unity Connection location do not attempt to
                                    		  perform a cross-server live reply. Note that when you enable cross-server live
                                    		  reply on Unity Connection, cross-server transfer is automatically enabled. Do
                                    		  the following procedure to enable cross-server transfer and live reply in on
                                    		  any Unity Connection originating locations.

Step 1

In Cisco Unity Connection Administration, on a location that
                                             			 transfers calls to remote users (the originating location), expand Networking and select Locations .

Step 2

On the Search Locations page, select the Display Name of a
                                             			 remote location that accepts cross-server live reply and transfer handoffs for
                                             			 users who are homed on this location (the receiving location).

Step 3

On the Edit Location page for the receiving location, do the
                                             			 following to initiate cross-server features to this receiving location:

To enable cross-server transfer and live reply to the remote
                                                   				  location, check the Allow Cross-Server Transfer to this Remote Location check
                                                   				  box.

Enter the dial string that this location uses to call the
                                                   				  receiving location when performing the handoff (for example, the pilot number
                                                   				  of the receiving location).

Step 4

Repeat Step 2 and Step 3 for
                                             			 each receiving location that accepts cross-server transfer handoffs from this
                                             			 location.

Tip

Step 5

Repeat the procedure on all remaining Unity Connection originating
                                             			 locations.

#### Configuring a
                              	 Cisco Unity Originating Location to Perform Cross-Server Live Reply
                              	 Requests

By default, a Cisco Unity originating location do not attempt to
                                    		  perform a cross-server live reply to any other locations. Do the following
                                    		  procedure to enable cross-server live reply on any Cisco Unity originating
                                    		  locations.

Step 1

In the Cisco Unity Administrator, expand Network > and select > Dialing Domain
                                                   				  Options page.

Step 2

In the Live Reply section, select the Subscribers with Class of Service Rights Can Reply to Messages
                                                				from Subscribers Homed on Other Cisco Unity Servers by Calling Them check box, then select Cross-Server Live Reply: Pass Control to the Called Subscriber’s
                                                				Cisco Unity Server . (Selecting Release Calls to the Phone System
                                             			 disables cross-server transfers originating from this server. Instead of
                                             			 handing off calls to the home server of the user, Cisco Unity attempts a
                                             			 release transfer to the Cross-Server Transfer Extension configured for the
                                             			 user. This fails if a Unity Connection user does not have a Cross-Server
                                             			 Transfer Extension configured.)

Step 3

In the Pilot Numbers for Cross-Server Logon, Transfer, and Live
                                             			 Reply section, enter the pilot number in the Dial String field for each server
                                             			 displayed in the table. (Note that the pilot numbers that you enter are stored
                                             			 in the SQL Server database UnityDb on the Cisco Unity server. Therefore, if the
                                             			 system is using failover, the pilot numbers are replicated to the secondary
                                             			 server.)

Step 4

Select the Play Prompt During Cross-Server Logon, Transfer, and Live Reply
                                                				so That Callers Know Something Is Happening check box. Although
                                             			 playing the “One moment please” prompt is optional, you should check the check
                                             			 box because the cross-server process can take several seconds before the caller
                                             			 is transferred.

Step 5

Select Save .

Step 6

Repeat the procedure on all remaining Unity Connection
                                             			 originating locations.

#### Testing
                              	 Cross-Server Live Reply

You should test the cross-server live reply before allowing
                                    		  callers to use the feature.

For failover systems, first test that the primary destination
                                    		  servers answer cross-server calls. Then manually fail over the destination
                                    		  servers to verify that the secondary server answers cross-server calls. If the
                                    		  destination servers are properly configured for failover, the secondary server
                                    		  should answer cross-server calls when the primary server is unavailable.

Do the following procedure to test cross-server live reply:

Step 1

Create a new user account (or use an existing account) on each
                                             			 location for testing purposes. Verify that users belong to a class of service
                                             			 in which live reply is enabled. Also verify that the user account information
                                             			 has replicated to all of the servers that you are testing. The time that it
                                             			 takes for the user data to replicate depends on your network configuration and
                                             			 replication schedule.

Step 2

Sign in as a user on an originating location and send a message
                                             			 to the test users on other locations.

Step 3

For each user that receives the test message, sign in, listen to
                                             			 the message, and select to call the sender. Verify that:

The “One moment please” prompt is played (if configured to do
                                                      					 so).

The call is transferred to the user phone or the greeting,
                                                      					 according to the call transfer settings of the called user.

## Notable Behavior for Cross-Server Sign-In, Transfers, and Live Reply

This section provides information about notable expected behavior associated with cross server sign-in, transfers and live
                           reply.

### Cross-Server Sign-In Not Providing User Workstation Client Sign-In Access

Users must access their home server (or cluster) when using client applications such as the Cisco Personal Communications
                              Assistant (Cisco PCA) and IMAP clients. The phone interface is the only client that provides cross-server sign-in capability.

### Users Prompted for a Password During Cross-Server Sign-In Between Unity Connection and Cisco Unity

When a Unity Connection user calls a Cisco Unity location from a known extension and is transferred to the home location using
                              cross-server sign-in, the receiving Unity Connection location can identify the user but does not recognize that the user is
                              calling from a known extension. For this reason, the user is always prompted for a password, regardless of whether the Skip
                              Password When Calling From a Known Extension setting is selected on the System Settings > Advanced > Conversation page in
                              Cisco Unity Connection Administration.

Likewise, when a Cisco Unity user calls a Unity Connection location from a known extension and is transferred to the home
                              location using cross-server sign-in, the user is always prompted for a password, regardless of whether Prompt for Phone Password
                              is set to Only When User Calls from an Unknown Extension (on the Phone Password page for the user).

### Factors Causing Delays During Cross-Server Handoff

The following factors can contribute significantly to delays in cross-server call handoff:

Longer user extensions. A four-digit extension does not take as long to dial during the handoff as a ten-digit extension.

Longer dialing strings to reach the receiving location. A four-digit dialing string does not take as long to dial as a ten-digit
                                    dialing string.

Multiple elements (such as PIMG/TIMG units, voice gateways, TDM trunks, and PSTN interfaces) in the call path between the
                                    originating location and the receiving location. More elements in the call path require more processing time for handing off
                                    cross-server calls.

In your environment, these factors can create delays that may cause the cross-server features to be unusable or unfeasible
                              for callers. You must test your cross-server configuration on a representative call path in your environment to determine
                              whether the delays that callers experience are acceptable.

### Increased Port Usage with Cross-Server Features

The cross-server features require the use of ports on both the originating and receiving locations. Depending on how busy
                              your servers are, you may need to add more ports or an additional server before enabling these features. You may also need
                              to adjust how ports are configured. For example, you may need to enable more ports to accept incoming calls.

After enabling the cross-server features, you should monitor activity on the servers closely until you are confident that
                              the servers can handle the increased load. For Cisco Unity Connection servers, you can use the Port Activity report in Cisco Unity
                              Connection Serviceability to monitor port usage. For Cisco Unity servers, you can use the Port Usage Analyzer for this task.
                              The Port Usage Analyzer is available in the Report Tools section of Tools Depot. See Port Usage Analyzer Help for detailed
                              instructions. Be sure to also monitor the Windows Event Viewer on any originating and receiving Cisco Unity servers for event
                              log messages related to problems with ports.

### Transfer Overrides
                           	 on Cross-Server Transfers

When a caller enters an extension in the automated attendant
                                 		  followed by the digits “#2,” the caller is routed directly to the greeting for
                                 		  the extension entered without a transfer being attempted. This is known as the
                                 		  transfer override digit sequence.

Unity Connection automatically supports the transfer override
                                 		  sequence between networked locations. For Cisco Unity servers, by default the
                                 		  transfer override digit sequence is ignored when the user who is associated
                                 		  with the extension preceding the “#2” is homed on another server in the dialing
                                 		  domain. If you want to enable the transfer override digit sequence for users
                                 		  who are homed on other locations in the dialing domain, including Unity
                                 		  Connection locations, do the following procedure on each Cisco Unity server
                                 		  that originates the cross-server transfer requests.

Procedure to enable transfer override on cross-server transfers from a
                                 		  Cisco Unity location

Step 1

On the Cisco Unity server desktop, double-click the Cisco Unity Tools Depot icon.

Step 2

In the left pane, under Administrative Tools, double-click Advanced Settings Tool .

Step 3

In the Unity Settings pane, select Networking—Allow Transfer Override on Cross-Server Transfer
                                             				Handoff .

Step 4

In the New Value list, select 1 , and then select Set .

Step 5

When prompted, select OK .

You do not need to restart the Cisco Unity software or server
                                             				when you make a change.

### Using Cross-Server Features with Display Original Calling Number on Transfer Parameter

When Cisco Unity Connection (and/or Cisco Unity) is integrated with Cisco Unified Communications Manager, the Display Original
                              Calling Number on Transfer from Cisco Unity service parameter in Cisco Unified CM can interfere with the cross-server handoff,
                              because the receiving location does not recognize that the incoming cross-server handoff call is from another location.

Do the following tasks so that cross-server handoffs complete properly between locations when this service parameter is set
                              in Cisco Unified CM. In the task list, you create a special directory number for each receiving location that is used only
                              during cross-server handoffs, so that the receiving location recognizes the call as a handoff.

#### Task List for
                              	 Configuring a Cross-Server Directory Number for Cross-Server Features

In Cisco Unified Communications Manager Administration, create a
                                       			 new directory number (for example, on a CTI route point) for each location that
                                       			 receives cross-server sign-in, transfer, or live reply calls. Configure the new
                                       			 directory number to always forward calls to the pilot number for the location.
                                       			 See the “Directory Number Configuration” chapter of the applicable Cisco Unified Communications Manager Administration Guide for your release of Cisco Unified CM, at http://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_maintenance_guides_list.html .

Configure each receiving location with a forwarded call routing
                                       			 rule that sends calls in which the forwarding station equals the location’s new
                                       			 cross-server directory number to the Opening Greeting call handler. See the “Adding
                                          				Forwarded Call Routing Rules to Destination Locations for Cross-Server Calls”
                                          				section on page 6-23 .

Update each originating location to dial the cross-server
                                       			 directory number of the receiving location during cross-server calls, rather
                                       			 than the pilot number. See the “Configuring
                                          				the Cross-Server Directory Number as the Dial String on Originating Locations”
                                          				section on page 6-25 .

#### Adding Forwarded
                              	 Call Routing Rules to Destination Locations for Cross-Server Calls

This section contains two procedures. Do either or both of the
                                    		  procedures, depending on whether you have Cisco Unity Connection and/or
                                    		  Cisco Unity receiving locations:

Step 1

In Cisco Unity Connection Administration on any one of the Unity
                                             			 Connection receiving locations, create the new forwarded routing rule:

Expand Call Management > Call Routing and select Forwarded Routing Rules .

On the Forwarded Routing Rules page, select Add New .

On the New Forwarded Rule page, enter the name of the new rule
                                                   				  in the Display Name field and select Save .

On the Edit Forwarded Routing Rule page, for Send Call To,
                                                   				  select Call Handler . From the call handler drop-down list, select Opening Greeting and select Save .

On the Edit Forwarded Routing Rule page, under Routing Rule
                                                   				  Conditions, select Add New .

On the New Forwarded Routing Rule Condition page, select Forwarding Station . From the forwarding station drop-down
                                                   				  list, select Equals . In the text box, enter the new cross-server
                                                   				  directory number for this location.

Select Save .

Step 2

Return to the Forwarded Routing Rules page by selecting Forwarded Routing Rules > Forwarded Routing Rules , or by navigating to Call
                                                   				  Management > Call
                                                   				  Routing > Forwarded Routing
                                                   				  Rules .

Step 3

Check the order of forwarded routing rules on the page. If the
                                             			 new routing rule that you created in Step 1 is not at the
                                             			 top of the table (in order of descending precedence) do the following substeps
                                             			 to move the new routing rule to the top of the forwarded routing rules table:

On the Forwarded Routing Rules page, select Change Order .

On the Edit Forwarded Routing Rule Order page, select the
                                                   				  Display Name of the new routing rule that you created in Step 1 .

Select the up arrow icon below the table to move the rule to the
                                                   				  top position. (You may need to select the icon multiple times.)

Select Save .

Step 4

Repeat the procedure for each remaining Unity Connection
                                             			 receiving location.

#### Adding Forwarded
                              	 Call Routing Rule to Cisco Unity Receiving Locations

Step 1

In the Cisco Unity Administrator on any one of the Cisco Unity
                                             			 receiving locations, create the new forwarded routing rule:

Navigate to Call Management > Call Routing .

Select Forwarded Calls .

Select the Add icon.

In the Add a Call Routing Rule dialog box, enter the name of the
                                                   				  new rule in the Name field.

Select Add .

In the Forwarding Station field, enter the new cross-server
                                                   				  directory number for this location.

In the Send Call To field, select Call Handler . Then, select Select Call Handler .

In the Call Handler Selection box, select the Opening Greeting
                                                   				  call handler.

Select Save .

Step 2

Check the order of forwarded routing rules on the page. If the
                                             			 new routing rule that you created in Step 1 is not
                                             			 at the top of the table (in order of descending precedence) do the following
                                             			 substeps to move the new routing rule to the top of the forwarded routing rules
                                             			 table:

Select Change Rule Order .

On the Forwarded Calls Rules Reorganization page, select the
                                                   				  Display Name of the new routing rule that you created in Step 1 .

Select Up to move the rule to the top position and select Close .

Step 3

Select the Save icon.

Step 4

Repeat the procedure for each remaining Cisco Unity receiving
                                             			 location.

#### Configuring the
                              	 Cross-Server Directory Number as the Dial String on Originating
                              	 Locations

Follow either of the given procedures depending whether you have
                                    		  Unity Connection and/or Cisco Unity originating locations:

Step 1

In Cisco Unity Connection Administration, on any one of the
                                             			 Unity Connection locations that originate cross-server calls, expand Networking > and select Locations .

Step 2

On the Search Locations page, select the Display Name of a
                                             			 receiving location.

Step 3

On the Edit Location page for the receiving location, change the
                                             			 dial string that this location uses to call the receiving location to the new
                                             			 cross-server directory number of the receiving location. Select Save.

Step 4

Repeat Step 2 and Step 3 to configure each receiving location that accepts cross-server handoffs from
                                             			 this location.

Tip

Step 5

Repeat the procedure on all remaining Unity Connection originating
                                             			 locations.

#### Configuring the
                              	 Cross-Server Directory Number as the Dial String on Cisco Unity Originating
                              	 Locations

Step 1

In the Cisco Unity Administrator, expand Network > and select > Dialing Domain
                                                   				  Options .

Step 2

In the Pilot Numbers for Cross-Server Logon, Transfer, and Live
                                             			 Reply section, enter the new cross-server directory number in the Dial String
                                             			 field for each server that is displayed in the table.

Step 3

Select Save and repeat the
                                             			 procedure on all remaining Cisco Unity originating locations.

| Feature | Description |
|---|---|
| Cross-server sign-in | Cross-server sign-in allows administrators to provide users who
                                       				  are homed on different locations with one phone number that they can call to
                                       				  sign in. When calling from outside the organization, users call the same
                                       				  number, regardless of which is the home server, and are transferred to the
                                       				  applicable home server to sign in. |
| Cross-server transfer | Cross-server transfer enables calls from the automated attendant
                                       				  or from a directory handler of one location to be transferred to a user on
                                       				  another location, according to the call transfer and screening settings of the
                                       				  called user. |
| Cross-server live reply | Cross-server live reply allows users who listen to their
                                       				  messages by phone to reply to a message from a user on another location by
                                       				  transferring to the user (according to the call transfer and screening settings
                                       				  of the called user). |

| Note | You can enter only one dial string for each receiving location.
                                             			 If the originating location is configured for multiple phone system
                                             			 integrations, you need a dial string that all phone system integrations can use
                                             			 to reach the receiving location. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, on a location that
                                             			 accepts cross-server handoffs for users who are homed on that location (the
                                             			 receiving location), expand System Settings > Advanced and select Conversations . |
|---|---|
| Step 2 | Check the Respond to Cross-Server Handoff Requests check box. |
| Step 3 | Repeat the procedure on all remaining Unity Connection receiving
                                             			 locations. |

| Step 1 | In Cisco Unity Connection Administration, on a location that
                                             			 accepts cross-server handoffs, expand Call
                                                   				  Management > Call
                                                   				  Routing and select Direct Routing Rules . |
|---|---|
| Step 2 | Select the display name of the routing rule that applies to
                                             			 incoming cross-server calls from originating locations. |
| Step 3 | Verify that calls that match the rule are routed to a call
                                             			 handler. |
| Step 4 | Repeat the procedure on all remaining Unity Connection receiving
                                             			 locations. |

| Note | For failover
                                             		  systems, do the procedure on both the primary and secondary servers. |
|---|---|

| Step 1 | In the Cisco Unity Administrator, on a location that accepts
                                             			 cross-server sign-in handoffs, expand Call
                                                   				  Routing > and
                                                   				  select > Direct
                                                   				  Calls . |
|---|---|
| Step 2 | Verify that incoming cross-server calls from originating
                                             			 locations are routed to the Opening Greeting. The Default Call Handler routing rule (which cannot be deleted
                                                				or modified) sends calls to the Opening Greeting. Therefore, if you have not
                                                				added any routing rules, the server is already set to correctly process
                                                				cross-server calls. |
| Step 3 | Repeat the procedure on all remaining Cisco Unity receiving
                                             			 locations. |

| Step 1 | Sign in to Cisco Unity Connection Administration for a location
                                             			 that accept across-server sign-in handoffs. Expand Call Management and select System Call Handlers . |
|---|---|
| Step 2 | On the Search Call Handlers page, you can do either of the
                                             			 following: Select the display name of the opening greeting or other call
                                                      					 handler that you want to modify. Skip to Step 6 . Select Add New to create a new call handler specifically for
                                                      					 cross-server calls. See the Step 3 . |
| Step 3 | On the New
                                             			 Call Handler page, enter basic settings, as applicable. (For more information
                                             			 on each field, see Help> This Page ). |
| Step 4 | To configure
                                             			 the call handler to accept the cross-server DTMF sequence: In the Edit menu, select Caller Input . On the Caller Input page, select # and uncheck the Ignore Additional Input check box. Select Save . |
| Step 5 | Create a new
                                             			 Direct Call Routing Rule to send calls from the Cisco Unity servers to the call
                                             			 handler: Expand Call Management > Call Routing and select Direct Routing Rules . On the Direct Routing Rules page, select Add New . On the New Direct Rule page, enter the name of the new rule in
                                                      					 the Display Name field and select Save . On the Edit Direct Rule page, for the Send Call To field, select Call Handler and the name of the call handler you added in Step 2 . Select Save . Under Routing Rule Conditions, select Add New . Configure the routing rule condition to match cross-server calls
                                                      					 from Cisco Unity servers. For example, use the Calling Number field to match
                                                      					 the phone numbers of the Cisco Unity ports that answer user calls. Select Save . On the Edit menu, select Edit Direct Routing Rule . Repeat f . through i . for each additional
                                                      					 number or number pattern that you need to match cross-server calls. |
| Step 6 | Repeat the
                                             			 procedure on all remaining Unity Connection receiving locations. |

| Step 1 | In Cisco Unity Connection Administration, on a location that
                                             			 handles sign-in calls from remote users (the originating location), expand Networking and select Locations . |
|---|---|
| Step 2 | On the Search Locations page, select the Display Name of a
                                             			 remote location that accepts cross-server sign-in requests for users homed on
                                             			 this location (or the receiving location). |
| Step 3 | On the Edit Location page for the receiving location, initiate
                                             			 cross-server features to the receiving location: To enable cross-server sign-in to the remote location, check the Allow Cross-Server Sign-In to this Remote Location check
                                                   				  box. Enter the dial string that this location uses to call the
                                                   				  receiving location when performing the handoff (for example, the pilot number
                                                   				  of the home server). Note You can
                                                               					 enter only one dial string for each receiving location. If the originating
                                                               					 location is configured for multiple phone system integrations, enter a dial
                                                               					 string that all phone system integrations can use to reach the receiving
                                                               					 location. | Note | You can
                                                               					 enter only one dial string for each receiving location. If the originating
                                                               					 location is configured for multiple phone system integrations, enter a dial
                                                               					 string that all phone system integrations can use to reach the receiving
                                                               					 location. |
| Note | You can
                                                               					 enter only one dial string for each receiving location. If the originating
                                                               					 location is configured for multiple phone system integrations, enter a dial
                                                               					 string that all phone system integrations can use to reach the receiving
                                                               					 location. |
| Step 4 | Repeat Step 2 and Step 3 to
                                             			 configure each receiving location that accepts cross-server sign-in handoffs
                                             			 from this location. Tip After you have
                                                         				saved the changes on a page, use the Next and Previous buttons to quickly navigate through each location
                                                         				in the organization. | Tip | After you have
                                                         				saved the changes on a page, use the Next and Previous buttons to quickly navigate through each location
                                                         				in the organization. |
| Tip | After you have
                                                         				saved the changes on a page, use the Next and Previous buttons to quickly navigate through each location
                                                         				in the organization. |
| Step 5 | Repeat the procedure on all remaining Unity Connection originating
                                             			 locations. |

| Note | You can
                                                               					 enter only one dial string for each receiving location. If the originating
                                                               					 location is configured for multiple phone system integrations, enter a dial
                                                               					 string that all phone system integrations can use to reach the receiving
                                                               					 location. |
|---|---|

| Tip | After you have
                                                         				saved the changes on a page, use the Next and Previous buttons to quickly navigate through each location
                                                         				in the organization. |
|---|---|

| Note | If the system is
                                             		  using failover, do the procedure on both the primary and secondary server,
                                             		  because most of the settings on the Network > Dialing Domain Options page
                                             		  are stored in the registry. (Registry settings are not replicated to the
                                             		  secondary server.) |
|---|---|

| Step 1 | In the Cisco Unity Administrator, expand Network > and select > Dialing Domain
                                                   				  Options . Note If the Dialing Domain Options link is unavailable on the system,
                                                            				  you must first configure the dialing domain on the Primary Location Settings
                                                            				  page in the Cisco Unity Administrator. | Note | If the Dialing Domain Options link is unavailable on the system,
                                                            				  you must first configure the dialing domain on the Primary Location Settings
                                                            				  page in the Cisco Unity Administrator. |
|---|---|---|---|
| Note | If the Dialing Domain Options link is unavailable on the system,
                                                            				  you must first configure the dialing domain on the Primary Location Settings
                                                            				  page in the Cisco Unity Administrator. |
| Step 2 | In the Cross Server Logon section, select the Subscribers Dial the Same Number to Log On to
                                                				Cisco Unity check box. |
| Step 3 | In the Pilot Numbers for Cross-Server Logon, Transfer, and Live
                                             			 Reply section, enter the pilot number in the Dial String field for each server
                                             			 that is displayed in the table. (Note that the pilot numbers that you enter are
                                             			 stored in the SQL Server database UnityDb on the Cisco Unity server. Therefore,
                                             			 if the system is using failover, the pilot numbers are replicated to the
                                             			 secondary server.) |
| Step 4 | Check the Play Prompt During Cross-Server Logon, Transfer, and Live Reply
                                                				so That Callers Know Something Is Happening check box. Although
                                             			 playing the “One moment please” prompt is optional, you must check the check
                                             			 box because the cross-server process can take several seconds before the
                                             			 receiving server prompts users to enter their passwords. |
| Step 5 | Select Save . |
| Step 6 | Repeat the procedure on all remaining Cisco Unity originating
                                             			 locations. |

| Note | If the Dialing Domain Options link is unavailable on the system,
                                                            				  you must first configure the dialing domain on the Primary Location Settings
                                                            				  page in the Cisco Unity Administrator. |
|---|---|

| Step 1 | Create a new user account (or use an existing account) on each
                                             			 of the destination servers for testing purposes. Be sure to verify that the
                                             			 user account information has replicated to all of the servers that you are
                                             			 testing. The time that it takes for the user data to replicate depends on your
                                             			 network configuration and replication schedule. |
|---|---|
| Step 2 | For each user account, call the pilot number for the server
                                             			 configured for cross-server sign-in, and attempt to sign in. Verify that: The “One moment please” prompt is played (if configured to do
                                                      					 so). You successfully sign in. |

| Note | You can enter
                                             			 only one dial string for each receiving location. If the originating location
                                             			 is configured for multiple phone system integrations, you need a dial string
                                             			 that all phone system integrations can use to reach the receiving location. |
|---|---|

| Step 1 | To view the configuration of cross-server transfers during call forward, execute the following command: run cuc dbquery unitydirdb select fullname,name,parentid,valuebool,value from vw_Configuration where name like 'HandoffForwardRemoteForward' If the command results a configured table entry, it means the feature is configured on Cisco Unity Connection. Otherwise,
                                                go to Step 2 to create a configuration entry. In configured table entry, check the value of  "valuebool" parameter. If valuebool is one, it means the feature is enabled
                                                for Cisco Unity Connection. Otherwise, go to Step 3 to enable the feature. |
|---|---|
| Step 2 | Create the configuration entry using the following command: run cuc dbquery unitydirdb execute procedure csp_ConfigurationCreate(pName='HandoffForwardRemoteForward'::lvarchar, pParentFullName='System.Conversations.CrossBox'::lvarchar, pType=11, pValueBool=0, pRequiresRestart=1) |
| Step 3 | Enable the cross-server transfers during call forward using the following command: run cuc dbquery unitydirdb execute procedure csp_ConfigurationModify(pName='HandoffForwardRemoteForward'::lvarchar, pParentFullName='System.Conversations.CrossBox'::lvarchar, pValueBool=1) |
| Step 4 | Disable the cross-server transfers during call forward using the following command: run cuc dbquery unitydirdb execute procedure csp_ConfigurationModify(pName='HandoffForwardRemoteForward'::lvarchar, pParentFullName='System.Conversations.CrossBox'::lvarchar, pValueBool=0) Note In case of a cluster, execute the commands only on publisher server and make sure that database replication is working fine
                                                                  for the cluster. Service restart is not required after executing the above commands. Note You can also enable the cross-server transfers during call forward through Cisco Unity Connection Administration. To enable
                                                         the feature, navigate System Setting > Advanced > Conversations and check the Cisco Unity Cross-Server Handoff During Call Forward check box on Conversation Configuration page of Cisco Unity Connection Administration. | Note | In case of a cluster, execute the commands only on publisher server and make sure that database replication is working fine
                                                                  for the cluster. Service restart is not required after executing the above commands. | Note | You can also enable the cross-server transfers during call forward through Cisco Unity Connection Administration. To enable
                                                         the feature, navigate System Setting > Advanced > Conversations and check the Cisco Unity Cross-Server Handoff During Call Forward check box on Conversation Configuration page of Cisco Unity Connection Administration. |
| Note | In case of a cluster, execute the commands only on publisher server and make sure that database replication is working fine
                                                                  for the cluster. Service restart is not required after executing the above commands. |
| Note | You can also enable the cross-server transfers during call forward through Cisco Unity Connection Administration. To enable
                                                         the feature, navigate System Setting > Advanced > Conversations and check the Cisco Unity Cross-Server Handoff During Call Forward check box on Conversation Configuration page of Cisco Unity Connection Administration. |

| Note | In case of a cluster, execute the commands only on publisher server and make sure that database replication is working fine
                                                                  for the cluster. Service restart is not required after executing the above commands. |
|---|---|

| Note | You can also enable the cross-server transfers during call forward through Cisco Unity Connection Administration. To enable
                                                         the feature, navigate System Setting > Advanced > Conversations and check the Cisco Unity Cross-Server Handoff During Call Forward check box on Conversation Configuration page of Cisco Unity Connection Administration. |
|---|---|

| Step 1 | Sign in to Cisco Unity Connection Administration for a location
                                             			 that accepts cross-server handoffs for users homed on that location (the
                                             			 receiving location). Expand System Settings > Advanced and select Conversations . |
|---|---|
| Step 2 | Check the Respond to Cross-Server Handoff Requests check box. |
| Step 3 | Repeat the procedure on all remaining Unity Connection receiving
                                             			 locations. |

| Step 1 | Sign in to Cisco Unity Connection Administration for a location
                                             			 that accepts cross-server handoffs. Expand Call
                                                   				  Management > Call
                                                   				  Routing and select Direct Routing Rules . |
|---|---|
| Step 2 | Select the display name of the routing rule that applies to
                                             			 incoming cross-server calls from originating locations. |
| Step 3 | Verify that calls that match the rule are routed to a call
                                             			 handler. |
| Step 4 | Repeat the procedure on all remaining Unity Connection receiving
                                             			 locations. |

| Note | For failover systems, do the procedure on both the primary and
                                                			 secondary servers. |
|---|---|

| Step 1 | Sign in to Cisco Unity Administrator for a location that accepts
                                             			 cross-server transfer handoffs. Expand Call
                                                   				  Routing > Direct
                                                   				  Calls . |
|---|---|
| Step 2 | Verify that incoming cross-server calls from originating
                                             			 locations are routed to the Opening Greeting. The Default Call Handler routing rule (which cannot be deleted
                                                				or modified) sends calls to the Opening Greeting. Therefore, if you have not
                                                				added any routing rules, the server is already set to correctly process
                                                				cross-server calls. |
| Step 3 | Repeat the procedure on all remaining Cisco Unity receiving
                                             			 locations. |

| Step 1 | Sign in to Cisco Unity Connection Administration for a location
                                             			 that accepts cross-server transfer handoffs. Expand Call Management and select System Call Handlers . |
|---|---|
| Step 2 | On the Search Call Handlers page, select the display name of the
                                             			 opening greeting or other call handler that you want to modify, or select Add New to create a new call handler specifically
                                             			 for cross-server calls. |
| Step 3 | If you did not create a new call handler in Step 2 ,
                                             			 skip to Step 6 . If you
                                             			 created a new call handler in Step 2 , on the
                                             			 New Call Handler page, enter basic settings, as applicable. (For field
                                             			 information, on the Help menu, select This Page .) |
| Step 4 | To configure the call handler to accept the cross-server DTMF
                                             			 sequence, do the following substeps: On the Edit menu, select Caller Input . On the Caller Input page, select # . Uncheck the Ignore Additional Input check box. Select Save . |
| Step 5 | If you created a new call handler in Step 2 , create
                                             			 a new direct-call routing rule to send calls from the Cisco Unity servers to
                                             			 the call handler for processing: Expand Call Management > Call Routing , then select Direct Routing Rules . On the Direct Routing Rules page, select Add New . On the New Direct Rule page, enter the name of the new rule in
                                                   				  the Display Name field. Select Save . On the Edit Direct Rule page, for Send Call To, select Call Handler , then select the name of the call handler you
                                                   				  added in Step 2 . Select Save . Under Routing Rule Conditions, select Add New . Configure the routing rule condition to match cross-server calls
                                                   				  from Cisco Unity servers. For example, use the Calling Number field to match
                                                   				  the phone numbers of the Cisco Unity ports that answer user calls. Select Save . On the Edit menu, select Edit Direct Routing Rule . Repeat g . through j . for
                                                   				  each additional number or number pattern that you need to match cross-server
                                                   				  calls. |
| Step 6 | Repeat the procedure on all remaining Unity Connection receiving
                                             			 locations. |

| Step 1 | In Cisco Unity Connection Administration, on a location that
                                             			 transfers calls to remote users (the originating location), expand Networking and select Locations . |
|---|---|
| Step 2 | On the Search Locations page, select the Display Name of a
                                             			 remote location that accepts cross-server transfer handoffs for users who are
                                             			 homed on this location (the receiving location). |
| Step 3 | On the Edit Location page for the receiving location, do the
                                             			 following to initiate cross-server features to this receiving location: To enable cross-server transfer and live reply to the remote
                                                   				  location, check the Allow Cross-Server Transfer to this Remote Location check
                                                   				  box. Enter the dial string that this location uses to call the
                                                   				  receiving location when performing the handoff (for example, the pilot number
                                                   				  of the receiving location). Note You can enter only one dial string for each receiving location.
                                                               					 If the originating location is configured for multiple phone system
                                                               					 integrations, enter a dial string that all phone system integrations can use to
                                                               					 reach the receiving location. | Note | You can enter only one dial string for each receiving location.
                                                               					 If the originating location is configured for multiple phone system
                                                               					 integrations, enter a dial string that all phone system integrations can use to
                                                               					 reach the receiving location. |
| Note | You can enter only one dial string for each receiving location.
                                                               					 If the originating location is configured for multiple phone system
                                                               					 integrations, enter a dial string that all phone system integrations can use to
                                                               					 reach the receiving location. |
| Step 4 | Repeat Step 2 and Step 3 for each
                                             			 receiving location that accepts cross-server transfer handoffs from this
                                             			 location. Tip After you have saved the changes on a page, use the Next and Previous buttons to quickly navigate through each location
                                                         				in the organization. | Tip | After you have saved the changes on a page, use the Next and Previous buttons to quickly navigate through each location
                                                         				in the organization. |
| Tip | After you have saved the changes on a page, use the Next and Previous buttons to quickly navigate through each location
                                                         				in the organization. |
| Step 5 | Repeat the
                                             			 procedure on all remaining Unity Connection originating locations. |

| Note | You can enter only one dial string for each receiving location.
                                                               					 If the originating location is configured for multiple phone system
                                                               					 integrations, enter a dial string that all phone system integrations can use to
                                                               					 reach the receiving location. |
|---|---|

| Tip | After you have saved the changes on a page, use the Next and Previous buttons to quickly navigate through each location
                                                         				in the organization. |
|---|---|

| Note | If the system is
                                             		  using failover, do the following procedure on both the primary and secondary
                                             		  server, because most of the settings on the Network > Dialing Domain Options
                                             		  page are stored in the registry. (Registry settings are not replicated to the
                                             		  secondary server.) |
|---|---|

| Step 1 | In the Cisco Unity Administrator, go to the Network > Dialing Domain
                                                   				  Options page. Note If the Dialing Domain Options link is unavailable on the system,
                                                            				  you must configure the dialing domain on the Primary Location Settings page in
                                                            				  the Cisco Unity Administrator. | Note | If the Dialing Domain Options link is unavailable on the system,
                                                            				  you must configure the dialing domain on the Primary Location Settings page in
                                                            				  the Cisco Unity Administrator. |
|---|---|---|---|
| Note | If the Dialing Domain Options link is unavailable on the system,
                                                            				  you must configure the dialing domain on the Primary Location Settings page in
                                                            				  the Cisco Unity Administrator. |
| Step 2 | Select the Cross-server Transfer: Pass Control to the Called Subscriber’s
                                                				Cisco Unity Server check box. (Selecting Release Calls to the Phone System
                                             			 disables cross-server transfers originating from this server. Instead of
                                             			 handing off calls to the home server of the user, Cisco Unity attempts a
                                             			 release transfer to the Cross-Server Transfer Extension configured for the
                                             			 user. This fails if a Unity Connection user does not have a Cross-Server
                                             			 Transfer Extension configured.) |
| Step 3 | In the Pilot Numbers for Cross-Server Logon, Transfer, and Live
                                             			 Reply section, enter the pilot number in the Dial String field for each server
                                             			 displayed in the table. (Note that the pilot numbers that you enter are stored
                                             			 in the SQL Server database UnityDb on the Cisco Unity server. Therefore, if the
                                             			 system is using failover, the pilot numbers are replicated to the secondary
                                             			 server.) |
| Step 4 | Select the Play Prompt During Cross-Server Logon, Transfer, and Live Reply
                                                				so That Callers Know Something Is Happening check box. Although
                                             			 playing the “One moment please” prompt is optional, you should check the check
                                             			 box because the cross-server process can take several seconds before the caller
                                             			 is transferred. |
| Step 5 | Select Save . |
| Step 6 | Repeat the procedure on all remaining Cisco Unity originating
                                             			 locations. |

| Note | If the Dialing Domain Options link is unavailable on the system,
                                                            				  you must configure the dialing domain on the Primary Location Settings page in
                                                            				  the Cisco Unity Administrator. |
|---|---|

| Step 1 | Create a new user account (or use an existing account) on each
                                             			 of the destination servers for testing purposes. Be sure to verify that the
                                             			 user account information has replicated to all of the servers that you are
                                             			 testing. The time that it takes for the user data to replicate depends on your
                                             			 network configuration and replication schedule. |
|---|---|
| Step 2 | For each user account, call the pilot number for the server
                                             			 configured for cross-server transfer, and enter the user extension at the
                                             			 opening greeting. Verify that: The “One moment please” prompt is played (if configured to do
                                                      					 so). The call is transferred to the user phone or the greeting,
                                                      					 according to the call transfer settings of the called user. |

| Note | In Unity Connection,
                                       		cross-server live reply is automatically supported (for users whose class of
                                       		service allows it) when cross-server transfer is enabled. If you have
                                       		previously configured a Unity Connection location as an originating or
                                       		receiving location for cross-server transfers, the location also originates or
                                       		receives cross-server live reply requests. |
|---|---|

| Note | You can enter
                                             			 only one dial string for each receiving location. If the originating location
                                             			 is configured for multiple phone system integrations, you need a dial string
                                             			 that all phone system integrations can use to reach the receiving location. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, on a location that
                                             			 accepts cross-server handoffs for users who are homed on that location (the
                                             			 receiving location), expand System Settings > Advanced and select Conversations . |
|---|---|
| Step 2 | Check the Respond to Cross-Server Handoff Requests check box. |
| Step 3 | Repeat the procedure on all remaining Unity Connection receiving
                                             			 locations. |

| Step 1 | In Cisco Unity Connection Administration, on a location that
                                             			 accepts cross-server handoffs, expand Call
                                                   				  Management > Call
                                                   				  Routing and select Direct Routing Rules . |
|---|---|
| Step 2 | Select the display name of the routing rule that applies to
                                             			 incoming cross-server calls from originating locations. |
| Step 3 | Verify that calls that match the rule are routed to a call
                                             			 handler. |
| Step 4 | Repeat the procedure on all remaining Unity Connection receiving
                                             			 locations. |

| Note | For failover
                                             		  systems, do the procedure on both the primary and secondary servers. |
|---|---|

| Step 1 | In the Cisco Unity Administrator, on a location that accepts
                                             			 cross-server live reply handoffs, go to the Call
                                                   				  Routing > Direct
                                                   				  Calls page. |
|---|---|
| Step 2 | Verify that incoming cross-server calls from originating
                                             			 locations are routed to the Opening Greeting. The Default Call Handler routing rule (which cannot be deleted
                                                				or modified) sends calls to the Opening Greeting. Therefore, if you have not
                                                				added any routing rules, the server is already set to correctly process
                                                				cross-server calls. |
| Step 3 | Repeat the procedure on all remaining Cisco Unity receiving
                                             			 locations. |

| Step 1 | In Cisco Unity Connection Administration, on a location that
                                             			 accepts cross-server sign-in handoffs, expand Call Management and select System Call Handlers . |
|---|---|
| Step 2 | On the Search Call Handlers page, select the display name of the
                                             			 opening greeting or other call handler that you want to modify, or select Add New to create a new call handler specifically
                                             			 for cross-server calls. |
| Step 3 | If you did not create a new call handler in Step 2 ,
                                             			 skip to Step 6 . If you
                                             			 created a new call handler in Step 2 ,
                                             			 on the New Call Handler page, enter basic settings, as applicable. (For field
                                             			 information, on the Help menu, select This Page .) |
| Step 4 | To configure the call handler to accept the cross-server DTMF
                                             			 sequence, do the following substeps: In the Edit menu, select Caller Input . On the Caller Input page, select # . Uncheck the Ignore Additional Input check box and select Save . |
| Step 5 | If you created a new call handler in Step 2 ,
                                             			 create a new direct-call routing rule to send calls from the Cisco Unity
                                             			 servers to the call handler for processing: Expand Call Management > Call Routing and select Direct Routing Rules . On the Direct Routing Rules page, select Add New . On the New Direct Rule page, enter the name of the new rule in
                                                   				  the Display Name field. Select Save . On the Edit Direct Rule page, for Send Call To, select Call Handler , then select the name of the call handler you
                                                   				  added in Step 2 . Select Save . Under Routing Rule Conditions, select Add New . Configure the routing rule condition to match cross-server calls
                                                   				  from Cisco Unity servers. For example, use the Calling Number field to match
                                                   				  the phone numbers of the Cisco Unity ports that answer user calls and select Save . On the Edit menu, select Edit Direct Routing Rule . Repeat g . through i . for
                                                   				  each additional number or number pattern that you need to match cross-server
                                                   				  calls. |
| Step 6 | Repeat the procedure on all remaining Unity Connection receiving
                                             			 locations. |

| Step 1 | In Cisco Unity Connection Administration, on a location that
                                             			 transfers calls to remote users (the originating location), expand Networking and select Locations . |
|---|---|
| Step 2 | On the Search Locations page, select the Display Name of a
                                             			 remote location that accepts cross-server live reply and transfer handoffs for
                                             			 users who are homed on this location (the receiving location). |
| Step 3 | On the Edit Location page for the receiving location, do the
                                             			 following to initiate cross-server features to this receiving location: To enable cross-server transfer and live reply to the remote
                                                   				  location, check the Allow Cross-Server Transfer to this Remote Location check
                                                   				  box. Enter the dial string that this location uses to call the
                                                   				  receiving location when performing the handoff (for example, the pilot number
                                                   				  of the receiving location). Note You can
                                                               					 enter only one dial string for each receiving location. If the originating
                                                               					 location is configured for multiple phone system integrations, enter a dial
                                                               					 string that all phone system integrations can use to reach the receiving
                                                               					 location. | Note | You can
                                                               					 enter only one dial string for each receiving location. If the originating
                                                               					 location is configured for multiple phone system integrations, enter a dial
                                                               					 string that all phone system integrations can use to reach the receiving
                                                               					 location. |
| Note | You can
                                                               					 enter only one dial string for each receiving location. If the originating
                                                               					 location is configured for multiple phone system integrations, enter a dial
                                                               					 string that all phone system integrations can use to reach the receiving
                                                               					 location. |
| Step 4 | Repeat Step 2 and Step 3 for
                                             			 each receiving location that accepts cross-server transfer handoffs from this
                                             			 location. Tip After you have
                                                         				saved the changes on a page, use the Next and Previous buttons to quickly navigate through each location
                                                         				in the organization. | Tip | After you have
                                                         				saved the changes on a page, use the Next and Previous buttons to quickly navigate through each location
                                                         				in the organization. |
| Tip | After you have
                                                         				saved the changes on a page, use the Next and Previous buttons to quickly navigate through each location
                                                         				in the organization. |
| Step 5 | Repeat the procedure on all remaining Unity Connection originating
                                             			 locations. |

| Note | You can
                                                               					 enter only one dial string for each receiving location. If the originating
                                                               					 location is configured for multiple phone system integrations, enter a dial
                                                               					 string that all phone system integrations can use to reach the receiving
                                                               					 location. |
|---|---|

| Tip | After you have
                                                         				saved the changes on a page, use the Next and Previous buttons to quickly navigate through each location
                                                         				in the organization. |
|---|---|

| Note | If the system is
                                             		  using failover, do the following procedure on both the primary and secondary
                                             		  server, because most of the settings on the Network > Dialing Domain Options
                                             		  page are stored in the registry. (Registry settings are not replicated to the
                                             		  secondary server.) |
|---|---|

| Step 1 | In the Cisco Unity Administrator, expand Network > and select > Dialing Domain
                                                   				  Options page. Note If the Dialing
                                                         				Domain Options link is unavailable on the system, you must configure the
                                                         				dialing domain on the Primary Location Settings page in the Cisco Unity
                                                         				Administrator. | Note | If the Dialing
                                                         				Domain Options link is unavailable on the system, you must configure the
                                                         				dialing domain on the Primary Location Settings page in the Cisco Unity
                                                         				Administrator. |
|---|---|---|---|
| Note | If the Dialing
                                                         				Domain Options link is unavailable on the system, you must configure the
                                                         				dialing domain on the Primary Location Settings page in the Cisco Unity
                                                         				Administrator. |
| Step 2 | In the Live Reply section, select the Subscribers with Class of Service Rights Can Reply to Messages
                                                				from Subscribers Homed on Other Cisco Unity Servers by Calling Them check box, then select Cross-Server Live Reply: Pass Control to the Called Subscriber’s
                                                				Cisco Unity Server . (Selecting Release Calls to the Phone System
                                             			 disables cross-server transfers originating from this server. Instead of
                                             			 handing off calls to the home server of the user, Cisco Unity attempts a
                                             			 release transfer to the Cross-Server Transfer Extension configured for the
                                             			 user. This fails if a Unity Connection user does not have a Cross-Server
                                             			 Transfer Extension configured.) |
| Step 3 | In the Pilot Numbers for Cross-Server Logon, Transfer, and Live
                                             			 Reply section, enter the pilot number in the Dial String field for each server
                                             			 displayed in the table. (Note that the pilot numbers that you enter are stored
                                             			 in the SQL Server database UnityDb on the Cisco Unity server. Therefore, if the
                                             			 system is using failover, the pilot numbers are replicated to the secondary
                                             			 server.) |
| Step 4 | Select the Play Prompt During Cross-Server Logon, Transfer, and Live Reply
                                                				so That Callers Know Something Is Happening check box. Although
                                             			 playing the “One moment please” prompt is optional, you should check the check
                                             			 box because the cross-server process can take several seconds before the caller
                                             			 is transferred. |
| Step 5 | Select Save . |
| Step 6 | Repeat the procedure on all remaining Unity Connection
                                             			 originating locations. |

| Note | If the Dialing
                                                         				Domain Options link is unavailable on the system, you must configure the
                                                         				dialing domain on the Primary Location Settings page in the Cisco Unity
                                                         				Administrator. |
|---|---|

| Step 1 | Create a new user account (or use an existing account) on each
                                             			 location for testing purposes. Verify that users belong to a class of service
                                             			 in which live reply is enabled. Also verify that the user account information
                                             			 has replicated to all of the servers that you are testing. The time that it
                                             			 takes for the user data to replicate depends on your network configuration and
                                             			 replication schedule. |
|---|---|
| Step 2 | Sign in as a user on an originating location and send a message
                                             			 to the test users on other locations. |
| Step 3 | For each user that receives the test message, sign in, listen to
                                             			 the message, and select to call the sender. Verify that: The “One moment please” prompt is played (if configured to do
                                                      					 so). The call is transferred to the user phone or the greeting,
                                                      					 according to the call transfer settings of the called user. |

| Step 1 | On the Cisco Unity server desktop, double-click the Cisco Unity Tools Depot icon. |
|---|---|
| Step 2 | In the left pane, under Administrative Tools, double-click Advanced Settings Tool . |
| Step 3 | In the Unity Settings pane, select Networking—Allow Transfer Override on Cross-Server Transfer
                                             				Handoff . |
| Step 4 | In the New Value list, select 1 , and then select Set . |
| Step 5 | When prompted, select OK . You do not need to restart the Cisco Unity software or server
                                             				when you make a change. Note For Cisco Unity failover, registry changes on one Cisco Unity
                                                      				server must be made manually on the other Cisco Unity server, because registry
                                                      				changes are not replicated. | Note | For Cisco Unity failover, registry changes on one Cisco Unity
                                                      				server must be made manually on the other Cisco Unity server, because registry
                                                      				changes are not replicated. |
| Note | For Cisco Unity failover, registry changes on one Cisco Unity
                                                      				server must be made manually on the other Cisco Unity server, because registry
                                                      				changes are not replicated. |

| Note | For Cisco Unity failover, registry changes on one Cisco Unity
                                                      				server must be made manually on the other Cisco Unity server, because registry
                                                      				changes are not replicated. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration on any one of the Unity
                                             			 Connection receiving locations, create the new forwarded routing rule: Expand Call Management > Call Routing and select Forwarded Routing Rules . On the Forwarded Routing Rules page, select Add New . On the New Forwarded Rule page, enter the name of the new rule
                                                   				  in the Display Name field and select Save . On the Edit Forwarded Routing Rule page, for Send Call To,
                                                   				  select Call Handler . From the call handler drop-down list, select Opening Greeting and select Save . On the Edit Forwarded Routing Rule page, under Routing Rule
                                                   				  Conditions, select Add New . On the New Forwarded Routing Rule Condition page, select Forwarding Station . From the forwarding station drop-down
                                                   				  list, select Equals . In the text box, enter the new cross-server
                                                   				  directory number for this location. Select Save . |
|---|---|
| Step 2 | Return to the Forwarded Routing Rules page by selecting Forwarded Routing Rules > Forwarded Routing Rules , or by navigating to Call
                                                   				  Management > Call
                                                   				  Routing > Forwarded Routing
                                                   				  Rules . |
| Step 3 | Check the order of forwarded routing rules on the page. If the
                                             			 new routing rule that you created in Step 1 is not at the
                                             			 top of the table (in order of descending precedence) do the following substeps
                                             			 to move the new routing rule to the top of the forwarded routing rules table: On the Forwarded Routing Rules page, select Change Order . On the Edit Forwarded Routing Rule Order page, select the
                                                   				  Display Name of the new routing rule that you created in Step 1 . Select the up arrow icon below the table to move the rule to the
                                                   				  top position. (You may need to select the icon multiple times.) Select Save . |
| Step 4 | Repeat the procedure for each remaining Unity Connection
                                             			 receiving location. |

| Step 1 | In the Cisco Unity Administrator on any one of the Cisco Unity
                                             			 receiving locations, create the new forwarded routing rule: Navigate to Call Management > Call Routing . Select Forwarded Calls . Select the Add icon. In the Add a Call Routing Rule dialog box, enter the name of the
                                                   				  new rule in the Name field. Select Add . In the Forwarding Station field, enter the new cross-server
                                                   				  directory number for this location. In the Send Call To field, select Call Handler . Then, select Select Call Handler . In the Call Handler Selection box, select the Opening Greeting
                                                   				  call handler. Select Save . |
|---|---|
| Step 2 | Check the order of forwarded routing rules on the page. If the
                                             			 new routing rule that you created in Step 1 is not
                                             			 at the top of the table (in order of descending precedence) do the following
                                             			 substeps to move the new routing rule to the top of the forwarded routing rules
                                             			 table: Select Change Rule Order . On the Forwarded Calls Rules Reorganization page, select the
                                                   				  Display Name of the new routing rule that you created in Step 1 . Select Up to move the rule to the top position and select Close . |
| Step 3 | Select the Save icon. |
| Step 4 | Repeat the procedure for each remaining Cisco Unity receiving
                                             			 location. |

| Step 1 | In Cisco Unity Connection Administration, on any one of the
                                             			 Unity Connection locations that originate cross-server calls, expand Networking > and select Locations . |
|---|---|
| Step 2 | On the Search Locations page, select the Display Name of a
                                             			 receiving location. |
| Step 3 | On the Edit Location page for the receiving location, change the
                                             			 dial string that this location uses to call the receiving location to the new
                                             			 cross-server directory number of the receiving location. Select Save. |
| Step 4 | Repeat Step 2 and Step 3 to configure each receiving location that accepts cross-server handoffs from
                                             			 this location. Tip After you have
                                                         				saved the changes on a page, use the Next and Previous buttons to quickly navigate through each location
                                                         				in the organization. | Tip | After you have
                                                         				saved the changes on a page, use the Next and Previous buttons to quickly navigate through each location
                                                         				in the organization. |
| Tip | After you have
                                                         				saved the changes on a page, use the Next and Previous buttons to quickly navigate through each location
                                                         				in the organization. |
| Step 5 | Repeat the procedure on all remaining Unity Connection originating
                                             			 locations. |

| Tip | After you have
                                                         				saved the changes on a page, use the Next and Previous buttons to quickly navigate through each location
                                                         				in the organization. |
|---|---|

| Step 1 | In the Cisco Unity Administrator, expand Network > and select > Dialing Domain
                                                   				  Options . |
|---|---|
| Step 2 | In the Pilot Numbers for Cross-Server Logon, Transfer, and Live
                                             			 Reply section, enter the new cross-server directory number in the Dial String
                                             			 field for each server that is displayed in the table. Note The numbers
                                                         				that you enter are stored in the SQL Server database UnityDb on the Cisco Unity
                                                         				server. Therefore, if the system is using failover, the numbers are replicated
                                                         				to the secondary server.) | Note | The numbers
                                                         				that you enter are stored in the SQL Server database UnityDb on the Cisco Unity
                                                         				server. Therefore, if the system is using failover, the numbers are replicated
                                                         				to the secondary server.) |
| Note | The numbers
                                                         				that you enter are stored in the SQL Server database UnityDb on the Cisco Unity
                                                         				server. Therefore, if the system is using failover, the numbers are replicated
                                                         				to the secondary server.) |
| Step 3 | Select Save and repeat the
                                             			 procedure on all remaining Cisco Unity originating locations. |

| Note | The numbers
                                                         				that you enter are stored in the SQL Server database UnityDb on the Cisco Unity
                                                         				server. Therefore, if the system is using failover, the numbers are replicated
                                                         				to the secondary server.) |
|---|---|