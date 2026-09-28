---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su1-cucm-b-feature-configuration-guide-for-cisco1251su1-cuc-3bce1b1c6b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU1/cucm_b_feature-configuration-guide-for-cisco1251SU1/cucm_b_feature-configuration-guide-for-cisco1251SU2_chapter_011011.html
retrieved_at: 2026-08-16T17:18:41.495577+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

Updated: July 31, 2025

Chapter: Call Forwarding

## Chapter: Call Forwarding

# Call Forwarding

## Call Forwarding Overview

As a user, you can configure a Cisco Unified IP Phone to forward calls to another phone. 
                              		  The following call forwarding
                              		  types are supported:

Call Forward No
                                       				  Bandwidth —Forwards calls when a call to a directory number fails due
                                    				to insufficient bandwidth, and provides forwarding functionality to an
                                    				Automated Alternate Routing (AAR) destination using public
                                    				switched telephone network (PSTN) as the alternate route
                                    				or to a voicemail system.

Call Forward with
                                       				  Alternate Destination —Forwards calls when a call to a directory number
                                    				and the forwarded destination are not answered. The call gets diverted to
                                    				an alternate destination as a last resort. This Call Forwarding type is also
                                    				referred to as "MLPP
                                       				  Alternate Party destination."

Call Forward All
                                       				  (CFA) —Forwards all calls to a directory number.

Call Forward Busy
                                       				  (CFB) —Forwards calls only when the line is in use and the configured Call Forward Busy
                                    				trigger value is reached.

Call Forward No Answer
                                       				  (CFNA) —Forwards calls when the phone is not answered after the configured
                                    				No Answer Ring Duration timer is exceeded or the destination is
                                    				unregistered.

Call Forward No Coverage
                                       				  (CFNC) —Forwards calls when the hunt list is exhausted or timed out, and
                                    				the associated hunt-pilot for coverage specifies "Use Personal
                                       				  Preferences" for its final forwarding.

Call Forward Unregistered
                                       				  (CFU) —Forwards calls when the phone is unregistered due to a remote WAN
                                    				link failure, and provides automated rerouting through the Public Switched Telephone Network (PSTN). Calls can also be
                                    forwarded based on the type of
                                    				caller: internal or external.

CFA Destination
                                       				  Override —Forwards calls when the user to whom calls are being forwarded
                                    				(the target) calls the user whose calls are being forwarded (the initiator). The phone of the initiator rings instead
                                    of call forwarding back to the target.

### Call Forward All, Including CFA Loop Prevention and CFA Loop Breakout

Call
                                 		  Forward All (CFA) allows a phone user to forward all calls to a directory
                                 		  number.

You can configure CFA for internal and external calls and can forward calls to a voicemail system or a dialed destination
                                 number by configuring the calling search space (CSS). Unified Communications Manager includes a secondary Calling Search Space configuration field for CFA. The secondary CSS for CFA combines with the existing
                                 CSS for CFA to allow support of the alternate CSS system configuration. When you activate CFA, only the primary and secondary
                                 CSS for CFA are used to validate the CFA destination and redirect the call to the CFA destination. If these fields are empty,
                                 the null CSS is used. Only the CSS fields that are configured in the primary CSS for CFA and secondary CSS for CFA fields
                                 are used. If CFA is activated from the phone, the CFA destination is validated by using the CSS for CFA and the secondary
                                 CSS for CFA, and the CFA destination gets written to the database. When a CFA is activated, the CFA destination always gets
                                 validated against the CSS for CFA and the secondary CSS for CFA.

Unified Communications Manager prevents CFA activation on the phone when a CFA loop is identified. For example, Unified Communications Manager identifies a call forward loop when the user presses the CFwdALL softkey on the phone with directory number 1000 and enters
                                 1001 as the CFA destination, and 1001 has forwarded all calls to directory number 1002, which has forwarded all calls to directory
                                 number 1003, which has forwarded all calls to 1000. In this case, Unified Communications Manager identifies that a loop has occurred and prevents CFA activation on the phone with directory number 1000.

Tip

If the same directory number exists in different partitions, for example, directory number 1000 exists in partitions 1 and
                                             2, Unified Communications Manager allows the CFA activation on the phone.

CFA loops do not affect call processing because Unified Communications Manager supports CFA loop breakout, which ensures that if a CFA loop is identified, the call goes through the entire forwarding chain,
                                 breaks out of the Call Forward All loop, and the loop is completed as expected, even if CFNA, CFB, or other forwarding options
                                 are configured along with CFA for one of the directory numbers in the forwarding chain.

For example, the user for the phone with directory number 1000 forwards all calls to directory number 1001, which has forwarded
                                 all calls to directory number 1002, which has forwarded all calls to directory number 1000, which creates a CFA loop. In addition,
                                 directory number 1002 has configured CFNA to directory number 1004. The user at the phone with directory number 1003 calls
                                 directory number 1000, which forwards to 1001, which forwards to 1002. Unified Communications Manager identifies a CFA loop, and the call, which breaks out of the loop, tries to connect to directory number 1002. If the No Answer
                                 Ring Duration timer expires before the user for the phone with directory number 1002 answers the call, Unified Communications Manager forwards the call to directory number 1004.

For a single call, Unified Communications Manager may identify multiple CFA loops and attempt to connect the call after each loop is identified.

## Call Forwarding
                        	 Configuration Task Flow

Step 1

Configure Partitions for Call Forwarding

Administrators can configure partitions to restrict Call Forwarding to certain
                                          				numbers based on the design criteria and requirements.

Step 2

Configure Calling Search Space for Call Forwarding

Administrators
                                          				can configure calling search spaces to restrict Call Forwarding to certain
                                          				numbers based on the design criteria and requirements.

Step 3

Configure Call Forwarding when Hunt List is Exhausted or Hunt Timer Expires

You can
                                          				forward a call when hunting fails (that is, when hunting is terminated without
                                          				any hunt party answering, either because no hunt number from the list picked up
                                          				or because the hunt timer timed out).

Step 4

Configure Call Forward No Bandwidth

You can
                                          				forward a call to an Automated Alternate Routing (AAR) destination using public
                                          				switched telephone network (PSTN) as the alternate route or to a voicemail
                                          				system when a call to a called directory number fails due to insufficient
                                          				bandwidth.

Step 5

Configure Call Forward Alternate Destination

You can
                                          				forward calls that go unanswered to the directory number and the forwarded
                                          				destination. Calls will get diverted to an alternate destination as a last
                                          				resort.

Step 6

Configure Other Call Forwarding Types

You can
                                          				configure additional forwarding types such as CFA, CFB, CFNA, CFNC, and CFU.
                                          				You can configure all these forwarding types from the Directory Number Configuration window.

Step 7

Enable Destination Override for Call Forwarding

Administrators
                                          				can override the CFA when the target of the CFA calls the initiator of the CFA.
                                          				This allows the CFA target can reach the initiator for important calls.

### Configure
                           	 Partitions for Call Forwarding

Configure
                                 		  partitions to create a logical grouping of directory numbers (DNs) and route
                                 		  patterns with similar reachability characteristics. Partitions facilitate call
                                 		  routing by dividing the route plan into logical subsets that are based on
                                 		  organization, location, and call type. You can configure multiple partitions.

Configure
                                 		  partitions to restrict call forwarding to certain numbers based on your design
                                 		  criteria and requirements.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Class of Control > Partition .

Step 2

Click Add
                                             				New to create a new partition.

Step 3

In
                                          			 the Partition
                                             				Name, Description field, enter a name for the partition that is
                                          			 unique to the route plan.

Step 4

Enter a
                                          			 comma (,) after the partition name and enter a description of the partition on
                                          			 the same line.

Step 5

To create
                                          			 multiple partitions, use one line for each partition entry.

Step 6

From the Time
                                             				Schedule drop-down list, choose a time schedule to associate with
                                          			 this partition.

Step 7

Select one
                                          			 of the following radio buttons to configure the Time
                                             				Zone :

- Originating
                                                				  Device —When you select this radio button, the system compares the
                                             				time zone of the calling device to the Time Schedule to determine whether the partition is
                                             				available is available to receive an incoming call.

- Specific Time
                                                				  Zone —After you select this radio button, choose a time zone from
                                             				the drop-down list. The system compares the chosen time zone to the Time Schedule to determine whether the partition is
                                             				available is available to receive an incoming call.

Step 8

Click Save .

#### Partition Name Guidelines for Call Forwarding

The list of partitions in a calling search space is limited to a maximum of 1024 characters. This means that the maximum number
                                    of partitions in a CSS varies depending on the length of the partition names. Use the following table to determine the maximum
                                    number of partitions that you can add to a calling search space if partition names are of fixed length.

Partition
                                                					 Name Length

Maximum
                                                					 Number of Partitions

2 characters

340

3 characters

256

4 characters

204

5 characters

172

...

...

10
                                                					 characters

92

15
                                                					 characters

64

### Configure Calling
                           	 Search Space for Call Forwarding

A calling
                                 		  search space is an ordered list of route partitions that are typically
                                 		  assigned to devices. Calling search spaces determine the partitions that
                                 		  calling devices can search when they are attempting to complete a call.

Configure calling
                                 		  search spaces to restrict Call Forwarding to certain numbers based on your
                                 		  design criteria and requirements.

#### Before you begin

Configure Partitions for Call Forwarding

Step 1

From Cisco Unified CM Administration, choose Call Routing > Class of Control > Calling Search Space .

Step 2

Click Add New .

Step 3

In the Name field, enter a name.

Ensure that
                                             				each calling search space name is unique to the system. The name can include up
                                             				to 50 alphanumeric characters and can contain any combination of spaces,
                                             				periods (.), hyphens (-), and underscore characters (_).

Step 4

In the Description field, enter a description.

The
                                             				description can include up to 50 characters in any language, but it cannot
                                             				include double-quotes ("), percentage sign (%), ampersand (&), back-slash
                                             				(\), or angle brackets (<>).

Step 5

From the Available Partitions drop-down list, perform one of
                                          			 the following steps:

- For a single partition,
                                             				select that partition.

- For multiple partitions,
                                             				hold down the Control (CTRL) key, then select the appropriate
                                             				partitions.

Step 6

Select the
                                          			 down arrow between the boxes to move the partitions to the Selected Partitions field.

Step 7

(Optional) Change the priority of selected partitions by using the arrow keys to the right
                                          			 of the Selected Partitions box.

Step 8

Click Save .

### Configure Call
                           	 Forwarding when Hunt List is Exhausted or Hunt Timer Expires

The concept of hunting differs from that of call forwarding. Hunting allows Unified Communications Manager to extend a call to one or more lists of numbers, where each list specifies a hunting order that is chosen from a fixed set
                                 of algorithms. When a call extends to a hunt party from these lists and the party fails to answer or is busy, hunting resumes
                                 with the next hunt party. (The next hunt party varies depending on the current hunt algorithm.) Hunting then ignores the Call
                                 Forward No Answer (CFNA), Call Forward Busy (CFB), or Call Forward All (CFA) configured values for the attempted party.

Call Forwarding
                                 		  allows detailed control as to how to extend (divert or redirect) a call when a
                                 		  called party fails to answer, or is busy and hunting is not taking place. For
                                 		  example, if the CFNA value for a line is set to a hunt-pilot number, a call to
                                 		  that line that is not answered diverts to the hunt-pilot number and begins
                                 		  hunting.

#### Before you begin

Configure Calling Search Space for Call Forwarding

Step 1

From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Hunt Pilot .

Step 2

Click Find .

Step 3

Choose the
                                          			 pattern for which you want to configure call treatment when hunting fails.

Step 4

Configure the fields in the Hunt Pilot Configuration for the Hunt Call Treatment Settings area. For more information on the fields and their configuration options, see Online Help.

Step 5

Click Save .

#### Hunt Call
                              	 Treatment Fields for Call Forwarding

Field

Description

Hunt Call Treatment
                                                   						  Settings

Forward Hunt No Answer or Forward Hunt Busy fields are designed to move calls
                                                            						  through the route list. Queuing is used to hold callers in
                                                            						  a route list. Therefore, if queuing is enabled, both Forward Hunt No Answer and Forward Hunt Busy are automatically disabled.
                                                            						  Conversely, if Forward Hunt No Answer or Forward Hunt Busy are enabled, queuing is
                                                            						  automatically disabled.

Forward
                                                						Hunt No Answer

When the
                                                						call that is distributed through the hunt list is not answered in a specific
                                                						period of time, this field specifies the destination to which the call gets
                                                						forwarded. Choose one of the following options:

Do Not Forward Unanswered
                                                         								Calls

Forward Unanswered Calls
                                                         								to

Destination —Enter a directory number to which calls
                                                            								  must be forwarded to.

Calling Search Space —Choose a calling search space
                                                            								  from the drop-down list which applies to all devices that use this directory
                                                            								  number.

Maximum Hunt Timer —Enter a value (in seconds) that
                                                      							 specifies the maximum time for hunting without queuing.

Valid values are 1 to 3600. The default value is 1800 seconds
                                                      							 (30 minutes).

Caution

Do not specify the same value for the Maximum Hunt Timer and the RNA Reversion Timeout on the associated line group.

The forward no answer timer should be greater than the RNA timer of the line group.

The forward no answer timer should not be multiples of RNA timer of line group.

This
                                                      							 timer is canceled if either a hunt member answers the call or the hunt list
                                                      							 gets exhausted before the timer expires. If you do not specify a value for this
                                                      							 timer, hunting continues until a hunt member answers or the hunt list is
                                                      							 exhausted. If neither event takes place, hunting continues for 30 minutes,
                                                      							 after which the call is received  for final treatment.

If
                                                            						  hunting exceeds the number of hops that the Forward Maximum Hop Count service parameter
                                                            						  specifies, hunting expires before the 30 minute maximum hunt timer value, and
                                                            						  the caller receives a reorder tone.

Forward
                                                						Hunt Busy

When the
                                                						call that is distributed through the hunt list is not answered in a specific
                                                						period of time, this field specifies the destination to which the call gets
                                                						forwarded. Choose one of the following options:

Do Not Forward Unanswered
                                                         								Calls

Use Forward Settings of
                                                         								Line Group Member

Forward Unanswered Calls
                                                         								to

Destination —Enter a directory number to which calls
                                                            								  must be forwarded to.

Calling Search Space —Choose a calling search space
                                                            								  from the drop-down list which applies to all devices that use this directory
                                                            								  number.

### Configure Call
                           	 Forward No Bandwidth

#### Before you begin

Configure Call Forwarding when Hunt List is Exhausted or Hunt Timer Expires

Step 1

From Cisco Unified CM Administration, choose Call Routing > Directory Number Configuration .

Step 2

Click Find .

Step 3

Choose the
                                          			 directory number for which you want to configure call forward when there is
                                          			 insufficient bandwidth.

Step 4

Configure the fields In the AAR Settings area. See Directory Number Configuration Fields for Call Forwarding for more information about the fields and their configuration options.

Step 5

Click Save .

#### Directory Number Configuration Fields for Call Forwarding

Field

Description

Voice
                                                   						Mail

Check this check box to forward the call to the voicemail.

When you check this check box, Unified Communications Manager ignores the values in the Destination and Calling Search Space fields.

AAR Destination
                                                   						Mask

Enter a destination mask to determine the AAR destination to
                                                					 dial instead of using the external phone number mask.

AAR
                                                   						Group

Choose an AAR group from the drop-down list. It provides the
                                                					 prefix digits that are used to route calls that are otherwise blocked due to
                                                					 insufficient bandwidth. If you choose None , the server does not attempt to reroute the
                                                					 blocked calls.

You can
                                                					 also configure this value in the Precedence Alternate Party Timeout service parameter
                                                					 from System > Service
                                                      						  Parameters .

Retain this destination in
                                                   						the call forwarding history

By default, the directory number
                                                					 configuration retains the AAR leg of the call in the call history, which
                                                					 ensures that the AAR forward to voicemail system will prompt the user to leave
                                                					 a voice message.

If you
                                                					 check the check box, the AAR leg of the call will be present in the call
                                                					 forwarding history.

### Configure Call
                           	 Forward Alternate Destination

#### Before you begin

Configure Call Forward No Bandwidth

Step 1

From Cisco Unified CM Administration, choose Call Routing > Directory Number Configuration .

Step 2

Click Find .

Step 3

Choose the
                                          			 directory number for which you want to configure an alternate destination.

Step 4

Configure the fields in the MLPP Alternate Party And Confidential Access Level Settings area. See MLPP Alternate Party And Confidential Access Level Settings Fields for Call Forwarding for more information about the fields and their configuration options.

Step 5

Click Save .

#### MLPP Alternate Party And Confidential Access Level Settings Fields for Call Forwarding

Field

Description

Target
                                                   						(Destination)

Enter the number to which MLPP precedence calls
                                                					 should be diverted if this directory number receives a precedence call and
                                                					 neither this number nor its Call Forward destination answers the precedence
                                                					 call.

Values can
                                                					 include numeric characters, octothorpe (#), and asterisk (*).

MLPP Calling Search
                                                   						Space

From the drop-down list, choose a calling search space to
                                                					 associate with the MLPP alternate party target (destination) number.

MLPP No Answer Ring
                                                   						Duration (seconds)

Enter the number of seconds (between 4 and 60)
                                                					 after which an MLPP precedence call will be directed to this directory number
                                                					 alternate party, if this directory number and its Call Forward destination have
                                                					 not answered the precedence call.

You can
                                                					 also configure this value in the Precedence Alternate Party Timeout service parameter
                                                					 from System > Service
                                                      						  Parameters from Cisco Unified CM Administration.

### Configure Other
                           	 Call Forwarding Types

You can configure
                                 		  Call Forward All (CFA), Call Forward Busy (CFB), Call Forward No Answer (CFNA),
                                 		  Call Forward No Coverage (CFNC), and Call Forward Unregistered (CFU) from the Directory
                                    			 Number Configuration window.

#### Before you begin

For Call
                                       				Forwarding functionality to work as intended, Cisco recommends that for the
                                       				configured phones and the directory numbers in various partitions, the Call
                                       				Forward Calling Search Spaces also be configured or else the forwarding may
                                       				fail. When a call is forwarded or redirected to the Call Forward destination,
                                       				the configured Call Forward Calling Search Space is used to forward the call.

Configure Call Forward Alternate Destination

Step 1

From Cisco Unified CM Administration, choose Call Routing > Directory Number Configuration .

The Find and List Directory Numbers window is displayed.

Step 2

Configure the Call Forwarding and Call Pickup Settings fields in the Directory Number Configuration window to configure CFA, CFB, CFNA, CFNC, and CFU. See Call Forwarding Fields for information about the fields and their configuration options.

Step 3

Click Save .

#### Call Forwarding
                              	 Fields

Field

Description

Call Forward and Call Pickup Settings

Calling Search Space Activation Policy

Three possible values exist for this option:

Use System Default —The CFA CSS Activation Policy service parameter determines which Forward All Calling Search Space to use for Call Forwarding. If the CFA CSS Activation Policy service parameter is set to With Configured CSS , then Forward All Calling Search Space and secondary Calling Search Space for Forward All will be used for Call Forwarding.
                                                      This is the default setting.

With Configured CSS —The Forward All Calling Search Space that is explicitly configured in the Directory Number Configuration window controls the Forward All activation and Call Forwarding.

If the Forward All Calling Search Space is set to None , no CSS is configured for Forward All. A Forward All activation attempt to any directory number with a partition will fail.
                                                      No change in the Forward All Calling Search Space and secondary Calling Search Space for Forward All occurs during the Forward
                                                      All activation.

With Activating Device/Line CSS —A combination of the Directory Number Calling Search Space and Device Calling Search Space controls the Forward All activation
                                                      and Call Forwarding without explicitly configuring a Forward All Calling Search Space.

When Forward All is activated from the phone, the Forward All Calling Search Space and secondary Calling Search Space for
                                                      Forward All automatically gets populated with the Directory Number Calling Search Space and Device Calling Search Space for
                                                      the activating device.

If the Forward All Calling Search Space is set to None , and when Forward All is activated through the phone, the combination of Directory Number Calling Search Space and activating
                                                      Device Calling Search Space controls the Forward All attempt.

CFA CSS Activation Policy —Ensure that you configure this service parameter correctly for Forward All to work as intended in the Service Parameter Configuration window. The service parameter includes two possible values:

With Configured CSS —The primary and secondary CFA Calling Search Space controls the Call Forwarding attempt.

With Activating Device/Line CSS —The primary and secondary CFA Calling Search Space is updated with primary Line Calling Search Space and activating Device
                                                      Calling Search Space.

Roaming —When a device is roaming in the same device mobility group, Cisco Unified Communications Manager uses the Device Mobility CSS to reach the local gateway. If a user sets Call Forward All at the phone, the CFA CSS is set
                                                to None , and the CFA CSS Activation Policy is set to With Activating Device/Line CSS , then:

The Device CSS and Line CSS is used as the CFA CSS when the device is in its home location.

If the device is roaming within the same device mobility group, the Device Mobility CSS from the Roaming Device Pool and the
                                                      Line CSS is used as the CFA CSS.

If the device is roaming within a different device mobility group, the Device CSS and Line CSS is used as the CFA CSS.

Forward All

The fields in this row of fields specify the Call Forwarding treatment for calls to this directory number if the directory
                                                number is set to forward all calls. The value in the Calling Search Space field is used to validate the Forward All destination that is entered when the user activates Call Forward All from the phone.
                                                This field is also used to redirect the call to the Call Forward All destination.

Configure the following values:

Voice Mail —Check this check box to use the value that is set in the Voice Mail Profile Configuration window.

When this check box is checked, Unified Communications Manager ignores the values in the Destination and Calling Search Space fields.

Destination —This field indicates the directory number to which all calls are forwarded. Use any dialable phone number, including an outside
                                                      destination.

Calling Search Space —This value applies to all devices that use this directory number.

Forward Maximum Hop Count —Configure this parameter from the Cisco Unified CM Administrator, choose System > Service Parameters .

This service parameter specifies the maximum number of times that a single call can be forwarded or diverted, and has special
                                                      considerations for QSIG calls. For an incoming QSIG call, the maximum value is 15 (per ISO specifications); if you specify
                                                      a greater value in this field, the specified value will apply to non-QSIG calls and for an incoming QSIG call, the call will
                                                      only divert a maximum of 15 times. When QSIG trunks are configured, Cisco recommends setting this parameter to 15.

For example, if the value of this parameter is seven, and a Call Forward All chain occurs consecutively from directory numbers
                                                      1000 to 007, which comprises seven hops, Cisco Unified Communications Manager prevents a phone user with directory number 2000 from activating CFA to directory number 1000, because no more than seven
                                                      forwarding hops are supported for a single call.

Secondary Calling Search Space for Forward All

Because Call Forwarding is a line-based feature, in cases where the Device Calling Search Space is unknown, the system uses
                                                only the Line Calling Search Space to forward the call. If the Line Calling Search Space is restrictive and not routable,
                                                the forward attempt fails.

Addition of a secondary calling search space for Call Forward All provides a solution to enable forwarding. The primary calling
                                                search space for Call Forward All and secondary calling search space for Call Forward All get concatenated (primary CFA CSS
                                                + secondary CFA CSS). Unified Communications Manager uses this combination to validate the CFA destination and to forward the call.

Forward Busy Internal

The fields in this row of fields specify the forwarding treatment for internal calls to this directory number if the directory
                                                number is busy. The values in the Destination and the Calling Search Space fields are used to redirect the call to the forward destination. Configure the following values:

Voice Mail —Check this check box to use the configured values in the Voice Mail Profile Configuration window for internal calls.

When this check box is checked, the calling search space of the voicemail pilot is used. Unified Communications Manager ignores the values in the Destination and the Calling Search Space fields.

When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to be forwarded to the voicemail system, you must uncheck
                                                                  the Voice Mail check box for external calls.

Destination —This field indicates the Call Forward Busy destination for internal calls. Use any dialable phone number, including an outside
                                                      destination.

When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls.

Calling Search Space —The Forward Busy Internal Calling Search Space is used to forward the call to the Forward Busy Internal destination. It applies
                                                      to all devices that use this directory number.

If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured Call Forward Calling
                                                                  Search Space is used to forward the call. If the Calling Search Space field is set to None , the forward operation fails if the system uses partitions and calling search spaces. For example, if you configure the Forward
                                                                  Busy destination, you should also configure the Forward Busy Calling Search Space. If you do not configure the Forward Busy
                                                                  Calling Search Space and the Forward Busy destination is in a partition, the forward operation fails.

When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, you must
                                                                  choose a different value in the Calling Search Space field for external calls.

The Call Forward Busy trigger is configured for each line appearance and cannot exceed the maximum number of calls that are
                                                configured for a line appearance. The Call Forward Busy trigger determines how many active calls exist on a line before the
                                                Call Forward Busy setting is activated (for example, ten calls).

Tip

Keep the busy trigger slightly lower than the maximum number of calls so that users can make outgoing calls and perform transfers.

Tip

If a call gets forwarded to a directory number that is busy, the call is not completed.

Forward Busy External

The fields in this row of fields specify the forwarding treatment for external calls to this directory number if the directory
                                                number is busy. The Destination and Calling Search Space fields is used to redirect the call to the forward destination.

Configure the following values:

Voice Mail —Check this check box to use the configured values in the Voice Mail Profile Configuration window for external calls.

When this check box is checked, the calling search space of the voicemail pilot is used. Unified Communications Manager ignores the values in the Destination and the Calling Search Space fields.

When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to be forwarded to the voicemail system, you must uncheck
                                                                  the Voice Mail check box for external calls.

Destination —This field indicates the Call Forward Busy destination for external calls. Use any dialable phone number, including an outside
                                                      destination.

When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls.

Calling Search Space —The Forward Busy External Calling Search Space forwards the call to the Forward Busy External destination. It applies to
                                                      all devices that use this directory number.

If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured Call Forward Calling
                                                                  Search Space is used to forward the call. If the Calling Search Space field is set to None , the forward operation fails if the system uses partitions and calling search spaces. For example, if you configure the Forward
                                                                  Busy destination, you should also configure the Forward Busy Calling Search Space. If you do not configure the Forward Busy
                                                                  Calling Search Space and the Forward Busy destination is in a partition, the forward operation fails.

When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, you must
                                                                  choose a different value in the Calling Search Space field for external calls.

Forward No Answer Internal

The fields in this row of fields specify the forwarding treatment for internal calls to this directory number if the directory
                                                number does not answer. The Destination and Calling Search Space fields are used to redirect the call to the forward destination.

Configure the following values:

Voice Mail —Check this check box to use the configured values in the Voice Mail Profile Configuration window.

When this check box is checked, the calling search space of the voicemail pilot is used. Unified Communications Manager ignores the values in the Destination and the Calling Search Space fields.

When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to be forwarded to the voicemail system, you must uncheck
                                                                  the Voice Mail check box for external calls.

Destination —This field indicates the directory number to which an internal call is forwarded when the call is not answered. Use any dialable
                                                      phone number, including an outside destination.

When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls.

Calling Search Space —The Forward No Answer Internal Calling Search Space is used to forward the call to the Forward No Answer Internal destination.
                                                      It applies to all devices that use this directory number.

If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured Call Forward Calling
                                                                  Search Space is used to forward the call. If the Calling Search Space field is set to None , the forward operation fails if the system uses partitions and calling search spaces. For example, if you configure the Forward
                                                                  No Answer destination, you should also configure the Forward No Answer Calling Search Space. If you do not configure the Forward
                                                                  No Answer Calling Search Space and the Forward No Answer destination is in a partition, the forward operation fails.

When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, you must
                                                                  choose a different value in the Calling Search Space field for external calls.

Forward No Answer External

The fields in this row of fields specify the forwarding treatment for external calls to this directory number if the directory
                                                number does not answer. The Destination and Calling Search Space fields are used to redirect the call to the forward destination.

Configure the following values:

Voice Mail —Check this check box to use the configured values in the Voice Mail Profile Configuration window.

When this check box is checked, the calling search space of the voicemail pilot is used. Unified Communications Manager ignores the values in the Destination and the Calling Search Space fields.

When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to be forwarded to the voicemail system, you must uncheck
                                                                  the Voice Mail check box for external calls.

Destination —This field indicates the directory number to which an external call is forwarded when the call is not answered. Use any dialable
                                                      phone number, including an outside destination.

When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls.

Calling Search Space —The Forward No Answer External Calling Search Space is used to forward the call to the Forward No Answer External destination.
                                                      It applies to all devices that use this directory number.

If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured Call Forward Calling
                                                                  Search Space is used to forward the call. If the Calling Search Space field is set to None , the forward operation fails if the system uses partitions and calling search spaces. For example, if you configure the Forward
                                                                  Busy destination, you should also configure the Forward No Answer Calling Search Space. If you do not configure the Forward
                                                                  No Answer Calling Search Space and the Forward No Answer destination is in a partition, the forward operation fails.

When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, you must
                                                                  choose a different value in the Calling Search Space field for external calls.

Forward No Coverage Internal

The Destination and Calling Search Space fields are used to redirect the call to the forward destination.

Configure the following values:

Voice Mail —Check this check box to use the configured values in the Voice Mail Profile Configuration window.

When this check box is checked, Unified Communications Manager ignores the values in the Destination and Calling Search Space fields. When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to forward to the voicemail system, you must uncheck the Voice Mail check box for external calls.

Destination —This field specifies the directory number to which an internal nonconnected call is forwarded when an application that controls
                                                      that directory number fails. Use any dialable phone number, including an outside destination.

When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls.

Calling Search Space —The Forward No Coverage Internal Calling Search Space is used to forward the call to the Forward No Coverage Internal destination.
                                                      This value applies to all devices that use this directory number.

If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured Call Forward Calling
                                                                  Search Space is used to forward the call. If the Calling Search Space field is set to None, the forward operation fails if the system uses partitions and calling search spaces. For example, if
                                                                  you configure the Forward Busy destination, you should also configure the Forward No Coverage Calling Search Space. If you
                                                                  do not configure the Forward No Coverage Calling Search Space and the Forward Busy destination is in a partition, the forward
                                                                  operation fails.

When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, you must
                                                                  choose a different value in the Calling Search Space field for external calls.

Forward No Coverage External

The Destination and Calling Search Space fields are et used to redirect the call to the forward destination.

Specify the following values:

Voice Mail —Check this check box to use the configured values in the Voice Mail Profile Configuration window.

When this check box is checked, Unified Communications Manager ignores the values in the Destination and the Calling Search Space fields. When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to forward to the voicemail system, you must uncheck the Voice Mail check box for external calls.

Destination —This field specifies the directory number to which an internal nonconnected call is forwarded when an application that controls
                                                      that directory number fails. Use any dialable phone number, including an outside destination.

When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls.

Calling Search Space —The Forward No Coverage External Calling Search Space is used to forward the call to the Forward No Coverage External destination.
                                                      This value applies to all devices that use this directory number.

If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured call forward calling
                                                                  search space is used to forward the call. If the Calling Search Space is None , the forward operation may fail if the system is using partitions and calling search spaces. For example, if you configure
                                                                  the Forward No Coverage destination, you should also configure the Forward No Coverage Calling Search Space. If you do not
                                                                  configure the Forward No Coverage Calling Search Space, and the Forward No Coverage destination is in a partition, the forward
                                                                  operation may fail.

When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, choose a
                                                                  different value in the Calling Search Space field for external calls.

Forward on CTI Failure

This field applies only to CTI route points and CTI ports. The fields in this row specify the forwarding treatment for external
                                                calls to this CTI route point or CTI port if the CTI route point or CTI port fails.

Configure the following values:

Voice Mail —Check this check box to use the configured values in the Voice Mail Profile Configuration window.

Destination —This field specifies the directory number to which an internal nonconnected call is forwarded when an application that controls
                                                      that directory number fails. Use any dialable phone number, including an outside destination.

Calling Search Space —This value applies to all devices that use this directory number.

Forward Unregistered Internal

This field applies to unregistered internal DN calls. The calls are rerouted to a specified destination or voicemail.

You must also specify the maximum number of forwards in the Service Parameters Configuration window for a directory number in the Max Forward UnRegistered Hops to DN service parameter.

This parameter specifies the maximum number of forward unregistered hops that are allowed for a directory number at the same
                                                            time. This parameter limits the number of times the call can be forwarded due to unregistered DN when a forwarding loop occurs.
                                                            Use this count to stop forward loops for external calls that have been Call Forward Unregistered. Unified Communications Manager terminates the call when the value that is specified in this service parameter is exceeded.

Forward Unregistered External

This field applies to unregistered external DN calls. The calls are rerouted to a specified destination or voicemail.

You must also specify the maximum number of forwards in the Service Parameters Configuration window for a directory number in the Max Forward UnRegistered Hops to DN service parameter.

This parameter specifies the maximum number of forward unregistered hops that are allowed for a directory number at the same
                                                            time. This parameter limits the number of times the call can be forwarded due to unregistered DN when a forwarding loop occurs.
                                                            Use this count to stop forward loops for external calls that have been Call Forward Unregistered. Unified Communications Manager terminates the call when the value that is specified in this service parameter is exceeded.

No Answer Ring Duration (seconds)

This field specifies the seconds to wait before forwarding the unanswered call to the Call Forward No Answer destination,
                                                if specified. Make sure the value that is specified in this parameter is less than the value that is specified in the T301 Timer service parameter. If the value in the Forward No Answer Timer service parameter is greater than the value that is specified in the T301 Timer service parameter, the call is not forwarded and the caller receives a busy signal.

Leave this field empty if you want to set the value in the Cisco Unified Communications Manager Forward No Answer Timer service parameter.

### Enable Destination
                           	 Override for Call Forwarding

Enable the destination override for call forwarding, Unified Communications Manager ignores the CFA destination when it matches the calling party number. The override applies to both internal and external
                                 calls.

In cases where the
                                 		  calling party number has been transformed, the calling party number does not
                                 		  match the CFA destination, no override occurs.

#### Before you begin

Configure Other Call Forwarding Types

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

In the Clusterwide Parameters (Feature - Hold Reversion) area, set the CFA
                                             				Destination Override service parameter value to True .

## Call Forwarding Interactions

Feature

Interaction

Call
                                          						Back

Calls
                                          						that are made from the CallBack notification screen will override all the Call
                                          						Forward configured values  on the target DN. The calls should be made before the CallBack
                                          						recall timer expires, otherwise the calls will not override the Call Forward
                                          						configured values.

Call
                                          						Display Restrictions

The Connected Number Display restriction applies to all calls that originate in the system. When this value is set to True , this field interacts transparently with existing Unified Communications Manager applications, features, and call processing. The value applies to all calls that terminate inside or outside the system.
                                          The Connected Number Display is updated to show the modified number or redirected number when a call is routed to a Call Forward
                                          All or Call Forward Busy destination, or gets redirected through a call transfer or CTI application.

Do Not
                                          						Disturb

On Cisco
                                          						Unified IP Phones, the message that indicates that the Do Not Disturb (DND)
                                          						feature is active takes priority over the message that indicates that the user
                                          						has new voice messages. However, the message that indicates that the Call
                                          						Forward All feature is active has a higher priority than DND.

External
                                          						Call Control

External Call Control intercepts calls at the translation pattern level, while Call Forward intercepts calls at the directory
                                          number level. External Call Control has higher priority; for calls where call forward is invoked, Unified Communications Manager sends a routing query to the adjunct route server if the translation pattern has an External Call Control profile assigned
                                          to it. Call Forwarding is triggered only when the adjunct route server sends a Permit decision with a Continue obligation
                                          to the Unified Communications Manager .

Extension Mobility Cross Cluster

Cisco
                                          						Extension Mobility Cross Cluster supports Call Forwarding.

Extend
                                          						and Connect

Extend
                                          						and Connect supports Call Forward All.

Immediate Divert

When the
                                          						Forward No Answer field  in the Directory Number Configuration window is not
                                          						configured, Call Forward uses the clusterwide CFNA timer service parameter, Forward No Answer Timer .

If a
                                          						user presses the iDivert softkey at the same time as the call is being
                                          						forwarded, the call gets diverted to an assigned call forward directory number
                                          						(because the amount of time set on the timer was too short), not the voicemail. To resolve this situation, set the CFNA
                                          timer service parameter to
                                          						enough time (for example, 60 seconds).

Logical
                                          						Partitioning

Unified Communications Manager performs logical partitioning policy check using the geolocation identifier information that associates with the incoming
                                          and forwarded devices. This handling applies to all types of call forwarding.

Multilevel Precedence and Preemption (MLPP)

Call Forward Busy

You can optionally configure a preconfigured Precedence Alternate Party target for any MLPP-enabled station.

Cisco Unified Communications Manager applies the Call Forward Busy feature to forward a precedence call in the usual manner before it applies to any Precedence
                                                Alternate Party Diversion procedures to the call.

The system preserves precedence of calls across multiple forwarded calls.

If the incoming precedence call is of higher precedence than the existing call, preemption occurs. Both the preempted parties
                                                in the active call receive a continuous preemption tone until the station to which the precedence call is directed hangs up.
                                                After hanging up, the station to which the precedence call is directed receives precedence ringing. The destination station
                                                connects to the preempting call when the station goes off hook.

Call Forward No Answer

For calls of Priority precedence level and above, call processing preserves the precedence level of calls during the forwarding
                                                process and may preempt the forwarded-to user.

If an Alternate Party is configured for the destination of a precedence call, call processing diverts the precedence call
                                                to the Alternate Party after the Precedence Call Alternate Party timeout expires. If no Alternate Party value is configured
                                                for the destination of a precedence call, call processing diverts the precedence call to the Call Forward No Answer value.

Normally, precedence calls are routed to users and not to the voicemail system. The administrator sets the Use Standard VM Handling For Precedence Calls enterprise parameter to avoid routing precedence calls to voicemail systems.

If the
                                          						incoming precedence call is of equal or lower precedence than the existing
                                          						call, call processing invokes normal call-forwarding behavior. If the
                                          						destination station for a precedence call is nonpreemptable (that is, not
                                          						MLPP-configured), call processing invokes call-forwarding behavior.

Alternate Party Diversion (APD) comprises a special type of call
                                          						forwarding. If users are configured for APD, APD takes place when a precedence
                                          						call is directed to a directory number (DN) that is busy or does not answer.
                                          						MLPP APD applies only to precedence calls. An MLPP APD call disables the DN
                                          						Call Forward No Answer value  for precedence calls.

Originally called party name in Placed Call History

When
                                          						privacy is configured only in the SIP profile of the called party device and
                                          						Call Forward All (CFA), or Call Forward Busy (CFB), or Call Forward
                                          						Unregistered (CFUR) is enabled, the configured alerting name is displayed
                                          						instead of "private" . To ensure that "private" is displayed for call forwarding, Cisco recommends
                                          						that you configure the name presentation restriction in the translation pattern
                                          						or the route pattern rather than in the SIP profile.

Rollover Lines

By using call forwarding settings, you can create rollover lines for a shared line. This could be a useful for some call center
                                          situations.

With rollover lines, when someone dials a number (e.g. 1-800-HOTLINE), the call always is routed to a specific phone line.
                                          This may be a shared line that is shared by multiple phones. If line 1 is busy, the call rolls over to line 2, if line 2 is
                                          busy it rolls over to line 3, and so on. Line 2 or 3 become available only if line 1 is busy.

This type of call functionality is possible via call forwarding busy settings and the Busy Trigger as follows:

On line 1, set the Busy Trigger to 1 and configure Call Forward Busy to the second line in the chain.

On line 2, set the Busy Trigger to 1 and configure Call Forward Busy to the third line in the chain

Continue this for as many lines as meets your needs.

Secure
                                          						Tone

Call
                                          						Forward All is supported on protected phones.

Session
                                          						Handoff

When
                                          						the user hands off a call, a new call gets presented on the desk phone. While
                                          						the desk phone is flashing, Call Forward All is not triggered on the desk phone
                                          						for the call that was handed off.

Shared Lines

When you use a shared line with Call Forward All (CFA) setting and choose the 'Calling Number' as 'Redirected Party's External
                                          Phone Number' presentation in the outgoing trunk, then the redirected number that is displayed may not be consistent when
                                          shared lines have different E164 numbers configured. So we recommend using the same E164 number across Shared lines.

## Call Forwarding Restrictions

Feature

Restriction

Call Forwarding

If Call Forward All activation occurs in Unified Communications Manager or the Cisco Unified Communications Self Care Portal, Unified Communications Manager does not prevent the CFA loop.

Unified Communications Manager prevents Call Forward All loops if CFA is activated from the phone, if the number of hops for a Call Forward All call exceeds
                                             the value that is specified for the Forward Maximum Hop Count service parameter, and if all phones in the forwarding chain
                                             have CFA activated (not CFB, CFNA, or any other call forwarding options).

For example, if the user with directory number 1000 forwards all calls to directory number 1001, which has CFB and CFNA configured
                                             to directory number 1002, which has CFA configured to directory number 1000, Unified Communications Manager allows the call to occur because directory number 1002 acts as the CFB and CFNA (not CFA) destination for directory number
                                             1001.

You cannot activate Call Back if you forward all calls to
                                             						  voicemail system.

An uncommon condition in connection with the Forward No Answer
                                             						  Timeout exists when you press the iDivert softkey. For example, if a manager
                                             						  presses the iDivert softkey immediately after the Forward No Answer timeout,
                                             						  Call Forward forwards the call to a preconfigured directory number. However, if
                                             						  the manager presses the iDivert softkey before the Forward No Answer timeout,
                                             						  Immediate Divert diverts the call to the voicemail of the manager.

Immediate Divert

When Call Forward All (CFA) and Call Forward Busy (CFB) are
                                       					 activated, the system does not support Immediate Divert (CFA and CFB have
                                       					 precedence over Immediate Divert).

Intercom

You cannot forward Intercom calls.

Log Out of Hunt Group

When a phone that is running SIP (7906, 7911, 7941, 7961) is logged in to hunt groups and Call Forward All is activated, the
                                       call gets presented to the phone that is running SIP.

When 7940
                                       					 and 7960 IP phones that are running SIP are logged in to hunt groups and Call
                                       					 Forward All is activated, the phone gets skipped and the next phone in the line
                                       					 group is rung.

Logical Partitioning

Logical partitioning handling does not take place in the following circumstances:

When both the caller and forwarded devices are Voice over IP (VoIP) phones.

When geolocation or a geolocation filter is not associated with any device.

Multilevel Precedence and Preemption (MLPP)

Multilevel Precedence and Preemption (MLPP) support for
                                       					 supplementary services specifies the following restrictions for Call
                                       					 Forwarding:

Call
                                             						  Forward All (CFA) support for inbound MLPP calls always forwards the call to
                                             						  the MLPP Alternate Party (MAP) target of the called party, if the MAP target is
                                             						  configured. In the event of an incorrect configuration (that is, if no MAP
                                             						  target is specified), the call gets rejected, and the calling party receives
                                             						  reorder tone.

Call
                                             						  Forward No Answer (CFNA) support for inbound MLPP calls forwards the call once
                                             						  to a CFNA target. After the first hop, if the call remains unanswered, the call
                                             						  is sent to the MAP target of the original called party, if the MAP target is
                                             						  configured. In the event of an incorrect configuration (that is, if no MAP
                                             						  target is specified), the call gets rejected, and the calling party receives
                                             						  reorder tone.

Call
                                             						  Forward Busy (CFB) support for inbound MLPP calls forwards the call up to the
                                             						  maximum number that is configured for forwarding hops. If the maximum hop count
                                             						  is reached, the call is sent to the MAP target of the original called party, if
                                             						  the MAP target is configured. In the event of an incorrect configuration (that
                                             						  is, no MAP target is specified), the call gets rejected, and the calling party
                                             						  receives reorder tone.

When a call is transferred, the call classification takes on the classification of the transferred leg, rather than the original
                                       leg. For example:

Incoming call from PSTN is received by a receptionist. This is an external call.

The receptionist transfers the call to extension 3100. The transferred call is now an internal call.

The user at extension 3100 is busy, but has Call Forward External configured to send external calls back to the receptionist.
                                             However, because the call takes on the classification of the second leg (internal), the call goes to voicemail.

| Tip | If the same directory number exists in different partitions, for example, directory number 1000 exists in partitions 1 and
                                             2, Unified Communications Manager allows the CFA activation on the phone. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Partitions for Call Forwarding | Administrators can configure partitions to restrict Call Forwarding to certain
                                          				numbers based on the design criteria and requirements. |
| Step 2 | Configure Calling Search Space for Call Forwarding | Administrators
                                          				can configure calling search spaces to restrict Call Forwarding to certain
                                          				numbers based on the design criteria and requirements. |
| Step 3 | Configure Call Forwarding when Hunt List is Exhausted or Hunt Timer Expires | You can
                                          				forward a call when hunting fails (that is, when hunting is terminated without
                                          				any hunt party answering, either because no hunt number from the list picked up
                                          				or because the hunt timer timed out). |
| Step 4 | Configure Call Forward No Bandwidth | You can
                                          				forward a call to an Automated Alternate Routing (AAR) destination using public
                                          				switched telephone network (PSTN) as the alternate route or to a voicemail
                                          				system when a call to a called directory number fails due to insufficient
                                          				bandwidth. |
| Step 5 | Configure Call Forward Alternate Destination | You can
                                          				forward calls that go unanswered to the directory number and the forwarded
                                          				destination. Calls will get diverted to an alternate destination as a last
                                          				resort. |
| Step 6 | Configure Other Call Forwarding Types | You can
                                          				configure additional forwarding types such as CFA, CFB, CFNA, CFNC, and CFU.
                                          				You can configure all these forwarding types from the Directory Number Configuration window. |
| Step 7 | Enable Destination Override for Call Forwarding | Administrators
                                          				can override the CFA when the target of the CFA calls the initiator of the CFA.
                                          				This allows the CFA target can reach the initiator for important calls. |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Class of Control > Partition . |
|---|---|
| Step 2 | Click Add
                                             				New to create a new partition. |
| Step 3 | In
                                          			 the Partition
                                             				Name, Description field, enter a name for the partition that is
                                          			 unique to the route plan. Partition
                                          			 names can contain alphanumeric characters, as well as spaces, hyphens (-), and
                                          			 underscore characters (_). See the online help for guidelines about partition
                                          			 names. |
| Step 4 | Enter a
                                          			 comma (,) after the partition name and enter a description of the partition on
                                          			 the same line. The
                                          			 description can contain up to 50 characters in any language, but it cannot
                                          			 include double quotes ("), percentage sign (%), ampersand (&), backslash
                                          			 (\), angle brackets (<>), or square brackets ([ ]). If you do
                                          			 not enter a description, Cisco Unified Communications Manager automatically
                                          			 enters the partition name in this field. |
| Step 5 | To create
                                          			 multiple partitions, use one line for each partition entry. |
| Step 6 | From the Time
                                             				Schedule drop-down list, choose a time schedule to associate with
                                          			 this partition. The time
                                          			 schedule specifies when the partition is available to receive incoming calls.
                                          			 If you choose None , the partition remains active at all times. |
| Step 7 | Select one
                                          			 of the following radio buttons to configure the Time
                                             				Zone : Originating
                                                				  Device —When you select this radio button, the system compares the
                                             				time zone of the calling device to the Time Schedule to determine whether the partition is
                                             				available is available to receive an incoming call. Specific Time
                                                				  Zone —After you select this radio button, choose a time zone from
                                             				the drop-down list. The system compares the chosen time zone to the Time Schedule to determine whether the partition is
                                             				available is available to receive an incoming call. |
| Step 8 | Click Save . |

| Partition
                                                					 Name Length | Maximum
                                                					 Number of Partitions |
|---|---|
| 2 characters | 340 |
| 3 characters | 256 |
| 4 characters | 204 |
| 5 characters | 172 |
| ... | ... |
| 10
                                                					 characters | 92 |
| 15
                                                					 characters | 64 |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Class of Control > Calling Search Space . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | In the Name field, enter a name. Ensure that
                                             				each calling search space name is unique to the system. The name can include up
                                             				to 50 alphanumeric characters and can contain any combination of spaces,
                                             				periods (.), hyphens (-), and underscore characters (_). |
| Step 4 | In the Description field, enter a description. The
                                             				description can include up to 50 characters in any language, but it cannot
                                             				include double-quotes ("), percentage sign (%), ampersand (&), back-slash
                                             				(\), or angle brackets (<>). |
| Step 5 | From the Available Partitions drop-down list, perform one of
                                          			 the following steps: For a single partition,
                                             				select that partition. For multiple partitions,
                                             				hold down the Control (CTRL) key, then select the appropriate
                                             				partitions. |
| Step 6 | Select the
                                          			 down arrow between the boxes to move the partitions to the Selected Partitions field. |
| Step 7 | (Optional) Change the priority of selected partitions by using the arrow keys to the right
                                          			 of the Selected Partitions box. |
| Step 8 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Hunt Pilot . The Find and List Hunt Pilots window is displayed. |
|---|---|
| Step 2 | Click Find . A list
                                          			 of configured Hunt Pilots is displayed. |
| Step 3 | Choose the
                                          			 pattern for which you want to configure call treatment when hunting fails. The Hunt
                                             				Pilot Configuration window is displayed. |
| Step 4 | Configure the fields in the Hunt Pilot Configuration for the Hunt Call Treatment Settings area. For more information on the fields and their configuration options, see Online Help. |
| Step 5 | Click Save . |

| Field | Description |
|---|---|
| Hunt Call Treatment
                                                   						  Settings Note Forward Hunt No Answer or Forward Hunt Busy fields are designed to move calls
                                                            						  through the route list. Queuing is used to hold callers in
                                                            						  a route list. Therefore, if queuing is enabled, both Forward Hunt No Answer and Forward Hunt Busy are automatically disabled.
                                                            						  Conversely, if Forward Hunt No Answer or Forward Hunt Busy are enabled, queuing is
                                                            						  automatically disabled. | Note | Forward Hunt No Answer or Forward Hunt Busy fields are designed to move calls
                                                            						  through the route list. Queuing is used to hold callers in
                                                            						  a route list. Therefore, if queuing is enabled, both Forward Hunt No Answer and Forward Hunt Busy are automatically disabled.
                                                            						  Conversely, if Forward Hunt No Answer or Forward Hunt Busy are enabled, queuing is
                                                            						  automatically disabled. |
| Note | Forward Hunt No Answer or Forward Hunt Busy fields are designed to move calls
                                                            						  through the route list. Queuing is used to hold callers in
                                                            						  a route list. Therefore, if queuing is enabled, both Forward Hunt No Answer and Forward Hunt Busy are automatically disabled.
                                                            						  Conversely, if Forward Hunt No Answer or Forward Hunt Busy are enabled, queuing is
                                                            						  automatically disabled. |
| Forward
                                                						Hunt No Answer | When the
                                                						call that is distributed through the hunt list is not answered in a specific
                                                						period of time, this field specifies the destination to which the call gets
                                                						forwarded. Choose one of the following options: Do Not Forward Unanswered
                                                         								Calls Forward Unanswered Calls
                                                         								to Destination —Enter a directory number to which calls
                                                            								  must be forwarded to. Calling Search Space —Choose a calling search space
                                                            								  from the drop-down list which applies to all devices that use this directory
                                                            								  number. Maximum Hunt Timer —Enter a value (in seconds) that
                                                      							 specifies the maximum time for hunting without queuing. Valid values are 1 to 3600. The default value is 1800 seconds
                                                      							 (30 minutes). Caution Do not specify the same value for the Maximum Hunt Timer and the RNA Reversion Timeout on the associated line group. The forward no answer timer should be greater than the RNA timer of the line group. The forward no answer timer should not be multiples of RNA timer of line group. This
                                                      							 timer is canceled if either a hunt member answers the call or the hunt list
                                                      							 gets exhausted before the timer expires. If you do not specify a value for this
                                                      							 timer, hunting continues until a hunt member answers or the hunt list is
                                                      							 exhausted. If neither event takes place, hunting continues for 30 minutes,
                                                      							 after which the call is received  for final treatment. Note If
                                                            						  hunting exceeds the number of hops that the Forward Maximum Hop Count service parameter
                                                            						  specifies, hunting expires before the 30 minute maximum hunt timer value, and
                                                            						  the caller receives a reorder tone. | Caution | Do not specify the same value for the Maximum Hunt Timer and the RNA Reversion Timeout on the associated line group. The forward no answer timer should be greater than the RNA timer of the line group. The forward no answer timer should not be multiples of RNA timer of line group. | Note | If
                                                            						  hunting exceeds the number of hops that the Forward Maximum Hop Count service parameter
                                                            						  specifies, hunting expires before the 30 minute maximum hunt timer value, and
                                                            						  the caller receives a reorder tone. |
| Caution | Do not specify the same value for the Maximum Hunt Timer and the RNA Reversion Timeout on the associated line group. The forward no answer timer should be greater than the RNA timer of the line group. The forward no answer timer should not be multiples of RNA timer of line group. |
| Note | If
                                                            						  hunting exceeds the number of hops that the Forward Maximum Hop Count service parameter
                                                            						  specifies, hunting expires before the 30 minute maximum hunt timer value, and
                                                            						  the caller receives a reorder tone. |
| Forward
                                                						Hunt Busy | When the
                                                						call that is distributed through the hunt list is not answered in a specific
                                                						period of time, this field specifies the destination to which the call gets
                                                						forwarded. Choose one of the following options: Do Not Forward Unanswered
                                                         								Calls Use Forward Settings of
                                                         								Line Group Member Forward Unanswered Calls
                                                         								to Destination —Enter a directory number to which calls
                                                            								  must be forwarded to. Calling Search Space —Choose a calling search space
                                                            								  from the drop-down list which applies to all devices that use this directory
                                                            								  number. |

| Note | Forward Hunt No Answer or Forward Hunt Busy fields are designed to move calls
                                                            						  through the route list. Queuing is used to hold callers in
                                                            						  a route list. Therefore, if queuing is enabled, both Forward Hunt No Answer and Forward Hunt Busy are automatically disabled.
                                                            						  Conversely, if Forward Hunt No Answer or Forward Hunt Busy are enabled, queuing is
                                                            						  automatically disabled. |
|---|---|

| Caution | Do not specify the same value for the Maximum Hunt Timer and the RNA Reversion Timeout on the associated line group. The forward no answer timer should be greater than the RNA timer of the line group. The forward no answer timer should not be multiples of RNA timer of line group. |
|---|---|

| Note | If
                                                            						  hunting exceeds the number of hops that the Forward Maximum Hop Count service parameter
                                                            						  specifies, hunting expires before the 30 minute maximum hunt timer value, and
                                                            						  the caller receives a reorder tone. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Directory Number Configuration . The Find and List Directory Numbers window is displayed. |
|---|---|
| Step 2 | Click Find . A list
                                          			 of configured directory numbers is displayed. |
| Step 3 | Choose the
                                          			 directory number for which you want to configure call forward when there is
                                          			 insufficient bandwidth. The Directory Number Configuration window is displayed. |
| Step 4 | Configure the fields In the AAR Settings area. See Directory Number Configuration Fields for Call Forwarding for more information about the fields and their configuration options. |
| Step 5 | Click Save . |

| Field | Description |
|---|---|
| Voice
                                                   						Mail | Check this check box to forward the call to the voicemail. Note When you check this check box, Unified Communications Manager ignores the values in the Destination and Calling Search Space fields. | Note | When you check this check box, Unified Communications Manager ignores the values in the Destination and Calling Search Space fields. |
| Note | When you check this check box, Unified Communications Manager ignores the values in the Destination and Calling Search Space fields. |
| AAR Destination
                                                   						Mask | Enter a destination mask to determine the AAR destination to
                                                					 dial instead of using the external phone number mask. |
| AAR
                                                   						Group | Choose an AAR group from the drop-down list. It provides the
                                                					 prefix digits that are used to route calls that are otherwise blocked due to
                                                					 insufficient bandwidth. If you choose None , the server does not attempt to reroute the
                                                					 blocked calls. You can
                                                					 also configure this value in the Precedence Alternate Party Timeout service parameter
                                                					 from System > Service
                                                      						  Parameters . |
| Retain this destination in
                                                   						the call forwarding history | By default, the directory number
                                                					 configuration retains the AAR leg of the call in the call history, which
                                                					 ensures that the AAR forward to voicemail system will prompt the user to leave
                                                					 a voice message. If you
                                                					 check the check box, the AAR leg of the call will be present in the call
                                                					 forwarding history. |

| Note | When you check this check box, Unified Communications Manager ignores the values in the Destination and Calling Search Space fields. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Directory Number Configuration . The Find and List Directory Numbers window is displayed. |
|---|---|
| Step 2 | Click Find . A list
                                          			 of configured directory numbers is displayed. |
| Step 3 | Choose the
                                          			 directory number for which you want to configure an alternate destination. The Directory Number Configuration window is displayed. |
| Step 4 | Configure the fields in the MLPP Alternate Party And Confidential Access Level Settings area. See MLPP Alternate Party And Confidential Access Level Settings Fields for Call Forwarding for more information about the fields and their configuration options. |
| Step 5 | Click Save . |

| Field | Description |
|---|---|
| Target
                                                   						(Destination) | Enter the number to which MLPP precedence calls
                                                					 should be diverted if this directory number receives a precedence call and
                                                					 neither this number nor its Call Forward destination answers the precedence
                                                					 call. Values can
                                                					 include numeric characters, octothorpe (#), and asterisk (*). |
| MLPP Calling Search
                                                   						Space | From the drop-down list, choose a calling search space to
                                                					 associate with the MLPP alternate party target (destination) number. |
| MLPP No Answer Ring
                                                   						Duration (seconds) | Enter the number of seconds (between 4 and 60)
                                                					 after which an MLPP precedence call will be directed to this directory number
                                                					 alternate party, if this directory number and its Call Forward destination have
                                                					 not answered the precedence call. You can
                                                					 also configure this value in the Precedence Alternate Party Timeout service parameter
                                                					 from System > Service
                                                      						  Parameters from Cisco Unified CM Administration. |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Directory Number Configuration . The Find and List Directory Numbers window is displayed. |
|---|---|
| Step 2 | Configure the Call Forwarding and Call Pickup Settings fields in the Directory Number Configuration window to configure CFA, CFB, CFNA, CFNC, and CFU. See Call Forwarding Fields for information about the fields and their configuration options. |
| Step 3 | Click Save . |

| Field | Description |
|---|---|
| Call Forward and Call Pickup Settings |
| Calling Search Space Activation Policy | Three possible values exist for this option: Use System Default —The CFA CSS Activation Policy service parameter determines which Forward All Calling Search Space to use for Call Forwarding. If the CFA CSS Activation Policy service parameter is set to With Configured CSS , then Forward All Calling Search Space and secondary Calling Search Space for Forward All will be used for Call Forwarding.
                                                      This is the default setting. With Configured CSS —The Forward All Calling Search Space that is explicitly configured in the Directory Number Configuration window controls the Forward All activation and Call Forwarding. If the Forward All Calling Search Space is set to None , no CSS is configured for Forward All. A Forward All activation attempt to any directory number with a partition will fail.
                                                      No change in the Forward All Calling Search Space and secondary Calling Search Space for Forward All occurs during the Forward
                                                      All activation. With Activating Device/Line CSS —A combination of the Directory Number Calling Search Space and Device Calling Search Space controls the Forward All activation
                                                      and Call Forwarding without explicitly configuring a Forward All Calling Search Space. When Forward All is activated from the phone, the Forward All Calling Search Space and secondary Calling Search Space for
                                                      Forward All automatically gets populated with the Directory Number Calling Search Space and Device Calling Search Space for
                                                      the activating device. If the Forward All Calling Search Space is set to None , and when Forward All is activated through the phone, the combination of Directory Number Calling Search Space and activating
                                                      Device Calling Search Space controls the Forward All attempt. CFA CSS Activation Policy —Ensure that you configure this service parameter correctly for Forward All to work as intended in the Service Parameter Configuration window. The service parameter includes two possible values: With Configured CSS —The primary and secondary CFA Calling Search Space controls the Call Forwarding attempt. With Activating Device/Line CSS —The primary and secondary CFA Calling Search Space is updated with primary Line Calling Search Space and activating Device
                                                      Calling Search Space. Roaming —When a device is roaming in the same device mobility group, Cisco Unified Communications Manager uses the Device Mobility CSS to reach the local gateway. If a user sets Call Forward All at the phone, the CFA CSS is set
                                                to None , and the CFA CSS Activation Policy is set to With Activating Device/Line CSS , then: The Device CSS and Line CSS is used as the CFA CSS when the device is in its home location. If the device is roaming within the same device mobility group, the Device Mobility CSS from the Roaming Device Pool and the
                                                      Line CSS is used as the CFA CSS. If the device is roaming within a different device mobility group, the Device CSS and Line CSS is used as the CFA CSS. |
| Forward All | The fields in this row of fields specify the Call Forwarding treatment for calls to this directory number if the directory
                                                number is set to forward all calls. The value in the Calling Search Space field is used to validate the Forward All destination that is entered when the user activates Call Forward All from the phone.
                                                This field is also used to redirect the call to the Call Forward All destination. Configure the following values: Voice Mail —Check this check box to use the value that is set in the Voice Mail Profile Configuration window. Note When this check box is checked, Unified Communications Manager ignores the values in the Destination and Calling Search Space fields. Destination —This field indicates the directory number to which all calls are forwarded. Use any dialable phone number, including an outside
                                                      destination. Calling Search Space —This value applies to all devices that use this directory number. Forward Maximum Hop Count —Configure this parameter from the Cisco Unified CM Administrator, choose System > Service Parameters . This service parameter specifies the maximum number of times that a single call can be forwarded or diverted, and has special
                                                      considerations for QSIG calls. For an incoming QSIG call, the maximum value is 15 (per ISO specifications); if you specify
                                                      a greater value in this field, the specified value will apply to non-QSIG calls and for an incoming QSIG call, the call will
                                                      only divert a maximum of 15 times. When QSIG trunks are configured, Cisco recommends setting this parameter to 15. For example, if the value of this parameter is seven, and a Call Forward All chain occurs consecutively from directory numbers
                                                      1000 to 007, which comprises seven hops, Cisco Unified Communications Manager prevents a phone user with directory number 2000 from activating CFA to directory number 1000, because no more than seven
                                                      forwarding hops are supported for a single call. | Note | When this check box is checked, Unified Communications Manager ignores the values in the Destination and Calling Search Space fields. |
| Note | When this check box is checked, Unified Communications Manager ignores the values in the Destination and Calling Search Space fields. |
| Secondary Calling Search Space for Forward All | Because Call Forwarding is a line-based feature, in cases where the Device Calling Search Space is unknown, the system uses
                                                only the Line Calling Search Space to forward the call. If the Line Calling Search Space is restrictive and not routable,
                                                the forward attempt fails. Addition of a secondary calling search space for Call Forward All provides a solution to enable forwarding. The primary calling
                                                search space for Call Forward All and secondary calling search space for Call Forward All get concatenated (primary CFA CSS
                                                + secondary CFA CSS). Unified Communications Manager uses this combination to validate the CFA destination and to forward the call. |
| Forward Busy Internal | The fields in this row of fields specify the forwarding treatment for internal calls to this directory number if the directory
                                                number is busy. The values in the Destination and the Calling Search Space fields are used to redirect the call to the forward destination. Configure the following values: Voice Mail —Check this check box to use the configured values in the Voice Mail Profile Configuration window for internal calls. Note When this check box is checked, the calling search space of the voicemail pilot is used. Unified Communications Manager ignores the values in the Destination and the Calling Search Space fields. Note When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to be forwarded to the voicemail system, you must uncheck
                                                                  the Voice Mail check box for external calls. Destination —This field indicates the Call Forward Busy destination for internal calls. Use any dialable phone number, including an outside
                                                      destination. Note When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls. Calling Search Space —The Forward Busy Internal Calling Search Space is used to forward the call to the Forward Busy Internal destination. It applies
                                                      to all devices that use this directory number. Note If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured Call Forward Calling
                                                                  Search Space is used to forward the call. If the Calling Search Space field is set to None , the forward operation fails if the system uses partitions and calling search spaces. For example, if you configure the Forward
                                                                  Busy destination, you should also configure the Forward Busy Calling Search Space. If you do not configure the Forward Busy
                                                                  Calling Search Space and the Forward Busy destination is in a partition, the forward operation fails. Note When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, you must
                                                                  choose a different value in the Calling Search Space field for external calls. The Call Forward Busy trigger is configured for each line appearance and cannot exceed the maximum number of calls that are
                                                configured for a line appearance. The Call Forward Busy trigger determines how many active calls exist on a line before the
                                                Call Forward Busy setting is activated (for example, ten calls). Tip Keep the busy trigger slightly lower than the maximum number of calls so that users can make outgoing calls and perform transfers. Tip If a call gets forwarded to a directory number that is busy, the call is not completed. | Note | When this check box is checked, the calling search space of the voicemail pilot is used. Unified Communications Manager ignores the values in the Destination and the Calling Search Space fields. | Note | When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to be forwarded to the voicemail system, you must uncheck
                                                                  the Voice Mail check box for external calls. | Note | When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls. | Note | If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured Call Forward Calling
                                                                  Search Space is used to forward the call. If the Calling Search Space field is set to None , the forward operation fails if the system uses partitions and calling search spaces. For example, if you configure the Forward
                                                                  Busy destination, you should also configure the Forward Busy Calling Search Space. If you do not configure the Forward Busy
                                                                  Calling Search Space and the Forward Busy destination is in a partition, the forward operation fails. | Note | When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, you must
                                                                  choose a different value in the Calling Search Space field for external calls. | Tip | Keep the busy trigger slightly lower than the maximum number of calls so that users can make outgoing calls and perform transfers. | Tip | If a call gets forwarded to a directory number that is busy, the call is not completed. |
| Note | When this check box is checked, the calling search space of the voicemail pilot is used. Unified Communications Manager ignores the values in the Destination and the Calling Search Space fields. |
| Note | When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to be forwarded to the voicemail system, you must uncheck
                                                                  the Voice Mail check box for external calls. |
| Note | When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls. |
| Note | If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured Call Forward Calling
                                                                  Search Space is used to forward the call. If the Calling Search Space field is set to None , the forward operation fails if the system uses partitions and calling search spaces. For example, if you configure the Forward
                                                                  Busy destination, you should also configure the Forward Busy Calling Search Space. If you do not configure the Forward Busy
                                                                  Calling Search Space and the Forward Busy destination is in a partition, the forward operation fails. |
| Note | When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, you must
                                                                  choose a different value in the Calling Search Space field for external calls. |
| Tip | Keep the busy trigger slightly lower than the maximum number of calls so that users can make outgoing calls and perform transfers. |
| Tip | If a call gets forwarded to a directory number that is busy, the call is not completed. |
| Forward Busy External | The fields in this row of fields specify the forwarding treatment for external calls to this directory number if the directory
                                                number is busy. The Destination and Calling Search Space fields is used to redirect the call to the forward destination. Configure the following values: Voice Mail —Check this check box to use the configured values in the Voice Mail Profile Configuration window for external calls. Note When this check box is checked, the calling search space of the voicemail pilot is used. Unified Communications Manager ignores the values in the Destination and the Calling Search Space fields. Note When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to be forwarded to the voicemail system, you must uncheck
                                                                  the Voice Mail check box for external calls. Destination —This field indicates the Call Forward Busy destination for external calls. Use any dialable phone number, including an outside
                                                      destination. Note When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls. Calling Search Space —The Forward Busy External Calling Search Space forwards the call to the Forward Busy External destination. It applies to
                                                      all devices that use this directory number. Note If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured Call Forward Calling
                                                                  Search Space is used to forward the call. If the Calling Search Space field is set to None , the forward operation fails if the system uses partitions and calling search spaces. For example, if you configure the Forward
                                                                  Busy destination, you should also configure the Forward Busy Calling Search Space. If you do not configure the Forward Busy
                                                                  Calling Search Space and the Forward Busy destination is in a partition, the forward operation fails. Note When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, you must
                                                                  choose a different value in the Calling Search Space field for external calls. | Note | When this check box is checked, the calling search space of the voicemail pilot is used. Unified Communications Manager ignores the values in the Destination and the Calling Search Space fields. | Note | When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to be forwarded to the voicemail system, you must uncheck
                                                                  the Voice Mail check box for external calls. | Note | When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls. | Note | If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured Call Forward Calling
                                                                  Search Space is used to forward the call. If the Calling Search Space field is set to None , the forward operation fails if the system uses partitions and calling search spaces. For example, if you configure the Forward
                                                                  Busy destination, you should also configure the Forward Busy Calling Search Space. If you do not configure the Forward Busy
                                                                  Calling Search Space and the Forward Busy destination is in a partition, the forward operation fails. | Note | When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, you must
                                                                  choose a different value in the Calling Search Space field for external calls. |
| Note | When this check box is checked, the calling search space of the voicemail pilot is used. Unified Communications Manager ignores the values in the Destination and the Calling Search Space fields. |
| Note | When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to be forwarded to the voicemail system, you must uncheck
                                                                  the Voice Mail check box for external calls. |
| Note | When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls. |
| Note | If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured Call Forward Calling
                                                                  Search Space is used to forward the call. If the Calling Search Space field is set to None , the forward operation fails if the system uses partitions and calling search spaces. For example, if you configure the Forward
                                                                  Busy destination, you should also configure the Forward Busy Calling Search Space. If you do not configure the Forward Busy
                                                                  Calling Search Space and the Forward Busy destination is in a partition, the forward operation fails. |
| Note | When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, you must
                                                                  choose a different value in the Calling Search Space field for external calls. |
| Forward No Answer Internal | The fields in this row of fields specify the forwarding treatment for internal calls to this directory number if the directory
                                                number does not answer. The Destination and Calling Search Space fields are used to redirect the call to the forward destination. Configure the following values: Voice Mail —Check this check box to use the configured values in the Voice Mail Profile Configuration window. Note When this check box is checked, the calling search space of the voicemail pilot is used. Unified Communications Manager ignores the values in the Destination and the Calling Search Space fields. Note When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to be forwarded to the voicemail system, you must uncheck
                                                                  the Voice Mail check box for external calls. Destination —This field indicates the directory number to which an internal call is forwarded when the call is not answered. Use any dialable
                                                      phone number, including an outside destination. Note When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls. Calling Search Space —The Forward No Answer Internal Calling Search Space is used to forward the call to the Forward No Answer Internal destination.
                                                      It applies to all devices that use this directory number. Note If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured Call Forward Calling
                                                                  Search Space is used to forward the call. If the Calling Search Space field is set to None , the forward operation fails if the system uses partitions and calling search spaces. For example, if you configure the Forward
                                                                  No Answer destination, you should also configure the Forward No Answer Calling Search Space. If you do not configure the Forward
                                                                  No Answer Calling Search Space and the Forward No Answer destination is in a partition, the forward operation fails. Note When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, you must
                                                                  choose a different value in the Calling Search Space field for external calls. | Note | When this check box is checked, the calling search space of the voicemail pilot is used. Unified Communications Manager ignores the values in the Destination and the Calling Search Space fields. | Note | When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to be forwarded to the voicemail system, you must uncheck
                                                                  the Voice Mail check box for external calls. | Note | When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls. | Note | If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured Call Forward Calling
                                                                  Search Space is used to forward the call. If the Calling Search Space field is set to None , the forward operation fails if the system uses partitions and calling search spaces. For example, if you configure the Forward
                                                                  No Answer destination, you should also configure the Forward No Answer Calling Search Space. If you do not configure the Forward
                                                                  No Answer Calling Search Space and the Forward No Answer destination is in a partition, the forward operation fails. | Note | When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, you must
                                                                  choose a different value in the Calling Search Space field for external calls. |
| Note | When this check box is checked, the calling search space of the voicemail pilot is used. Unified Communications Manager ignores the values in the Destination and the Calling Search Space fields. |
| Note | When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to be forwarded to the voicemail system, you must uncheck
                                                                  the Voice Mail check box for external calls. |
| Note | When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls. |
| Note | If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured Call Forward Calling
                                                                  Search Space is used to forward the call. If the Calling Search Space field is set to None , the forward operation fails if the system uses partitions and calling search spaces. For example, if you configure the Forward
                                                                  No Answer destination, you should also configure the Forward No Answer Calling Search Space. If you do not configure the Forward
                                                                  No Answer Calling Search Space and the Forward No Answer destination is in a partition, the forward operation fails. |
| Note | When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, you must
                                                                  choose a different value in the Calling Search Space field for external calls. |
| Forward No Answer External | The fields in this row of fields specify the forwarding treatment for external calls to this directory number if the directory
                                                number does not answer. The Destination and Calling Search Space fields are used to redirect the call to the forward destination. Configure the following values: Voice Mail —Check this check box to use the configured values in the Voice Mail Profile Configuration window. Note When this check box is checked, the calling search space of the voicemail pilot is used. Unified Communications Manager ignores the values in the Destination and the Calling Search Space fields. Note When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to be forwarded to the voicemail system, you must uncheck
                                                                  the Voice Mail check box for external calls. Destination —This field indicates the directory number to which an external call is forwarded when the call is not answered. Use any dialable
                                                      phone number, including an outside destination. Note When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls. Calling Search Space —The Forward No Answer External Calling Search Space is used to forward the call to the Forward No Answer External destination.
                                                      It applies to all devices that use this directory number. Note If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured Call Forward Calling
                                                                  Search Space is used to forward the call. If the Calling Search Space field is set to None , the forward operation fails if the system uses partitions and calling search spaces. For example, if you configure the Forward
                                                                  Busy destination, you should also configure the Forward No Answer Calling Search Space. If you do not configure the Forward
                                                                  No Answer Calling Search Space and the Forward No Answer destination is in a partition, the forward operation fails. Note When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, you must
                                                                  choose a different value in the Calling Search Space field for external calls. | Note | When this check box is checked, the calling search space of the voicemail pilot is used. Unified Communications Manager ignores the values in the Destination and the Calling Search Space fields. | Note | When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to be forwarded to the voicemail system, you must uncheck
                                                                  the Voice Mail check box for external calls. | Note | When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls. | Note | If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured Call Forward Calling
                                                                  Search Space is used to forward the call. If the Calling Search Space field is set to None , the forward operation fails if the system uses partitions and calling search spaces. For example, if you configure the Forward
                                                                  Busy destination, you should also configure the Forward No Answer Calling Search Space. If you do not configure the Forward
                                                                  No Answer Calling Search Space and the Forward No Answer destination is in a partition, the forward operation fails. | Note | When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, you must
                                                                  choose a different value in the Calling Search Space field for external calls. |
| Note | When this check box is checked, the calling search space of the voicemail pilot is used. Unified Communications Manager ignores the values in the Destination and the Calling Search Space fields. |
| Note | When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to be forwarded to the voicemail system, you must uncheck
                                                                  the Voice Mail check box for external calls. |
| Note | When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls. |
| Note | If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured Call Forward Calling
                                                                  Search Space is used to forward the call. If the Calling Search Space field is set to None , the forward operation fails if the system uses partitions and calling search spaces. For example, if you configure the Forward
                                                                  Busy destination, you should also configure the Forward No Answer Calling Search Space. If you do not configure the Forward
                                                                  No Answer Calling Search Space and the Forward No Answer destination is in a partition, the forward operation fails. |
| Note | When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, you must
                                                                  choose a different value in the Calling Search Space field for external calls. |
| Forward No Coverage Internal | The Destination and Calling Search Space fields are used to redirect the call to the forward destination. Configure the following values: Voice Mail —Check this check box to use the configured values in the Voice Mail Profile Configuration window. Note When this check box is checked, Unified Communications Manager ignores the values in the Destination and Calling Search Space fields. When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to forward to the voicemail system, you must uncheck the Voice Mail check box for external calls. Destination —This field specifies the directory number to which an internal nonconnected call is forwarded when an application that controls
                                                      that directory number fails. Use any dialable phone number, including an outside destination. Note When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls. Calling Search Space —The Forward No Coverage Internal Calling Search Space is used to forward the call to the Forward No Coverage Internal destination.
                                                      This value applies to all devices that use this directory number. Note If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured Call Forward Calling
                                                                  Search Space is used to forward the call. If the Calling Search Space field is set to None, the forward operation fails if the system uses partitions and calling search spaces. For example, if
                                                                  you configure the Forward Busy destination, you should also configure the Forward No Coverage Calling Search Space. If you
                                                                  do not configure the Forward No Coverage Calling Search Space and the Forward Busy destination is in a partition, the forward
                                                                  operation fails. Note When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, you must
                                                                  choose a different value in the Calling Search Space field for external calls. | Note | When this check box is checked, Unified Communications Manager ignores the values in the Destination and Calling Search Space fields. When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to forward to the voicemail system, you must uncheck the Voice Mail check box for external calls. | Note | When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls. | Note | If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured Call Forward Calling
                                                                  Search Space is used to forward the call. If the Calling Search Space field is set to None, the forward operation fails if the system uses partitions and calling search spaces. For example, if
                                                                  you configure the Forward Busy destination, you should also configure the Forward No Coverage Calling Search Space. If you
                                                                  do not configure the Forward No Coverage Calling Search Space and the Forward Busy destination is in a partition, the forward
                                                                  operation fails. | Note | When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, you must
                                                                  choose a different value in the Calling Search Space field for external calls. |
| Note | When this check box is checked, Unified Communications Manager ignores the values in the Destination and Calling Search Space fields. When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to forward to the voicemail system, you must uncheck the Voice Mail check box for external calls. |
| Note | When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls. |
| Note | If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured Call Forward Calling
                                                                  Search Space is used to forward the call. If the Calling Search Space field is set to None, the forward operation fails if the system uses partitions and calling search spaces. For example, if
                                                                  you configure the Forward Busy destination, you should also configure the Forward No Coverage Calling Search Space. If you
                                                                  do not configure the Forward No Coverage Calling Search Space and the Forward Busy destination is in a partition, the forward
                                                                  operation fails. |
| Note | When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, you must
                                                                  choose a different value in the Calling Search Space field for external calls. |
| Forward No Coverage External | The Destination and Calling Search Space fields are et used to redirect the call to the forward destination. Specify the following values: Voice Mail —Check this check box to use the configured values in the Voice Mail Profile Configuration window. Note When this check box is checked, Unified Communications Manager ignores the values in the Destination and the Calling Search Space fields. When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to forward to the voicemail system, you must uncheck the Voice Mail check box for external calls. Destination —This field specifies the directory number to which an internal nonconnected call is forwarded when an application that controls
                                                      that directory number fails. Use any dialable phone number, including an outside destination. Note When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls. Calling Search Space —The Forward No Coverage External Calling Search Space is used to forward the call to the Forward No Coverage External destination.
                                                      This value applies to all devices that use this directory number. Note If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured call forward calling
                                                                  search space is used to forward the call. If the Calling Search Space is None , the forward operation may fail if the system is using partitions and calling search spaces. For example, if you configure
                                                                  the Forward No Coverage destination, you should also configure the Forward No Coverage Calling Search Space. If you do not
                                                                  configure the Forward No Coverage Calling Search Space, and the Forward No Coverage destination is in a partition, the forward
                                                                  operation may fail. Note When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, choose a
                                                                  different value in the Calling Search Space field for external calls. | Note | When this check box is checked, Unified Communications Manager ignores the values in the Destination and the Calling Search Space fields. When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to forward to the voicemail system, you must uncheck the Voice Mail check box for external calls. | Note | When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls. | Note | If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured call forward calling
                                                                  search space is used to forward the call. If the Calling Search Space is None , the forward operation may fail if the system is using partitions and calling search spaces. For example, if you configure
                                                                  the Forward No Coverage destination, you should also configure the Forward No Coverage Calling Search Space. If you do not
                                                                  configure the Forward No Coverage Calling Search Space, and the Forward No Coverage destination is in a partition, the forward
                                                                  operation may fail. | Note | When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, choose a
                                                                  different value in the Calling Search Space field for external calls. |
| Note | When this check box is checked, Unified Communications Manager ignores the values in the Destination and the Calling Search Space fields. When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to forward to the voicemail system, you must uncheck the Voice Mail check box for external calls. |
| Note | When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls. |
| Note | If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured call forward calling
                                                                  search space is used to forward the call. If the Calling Search Space is None , the forward operation may fail if the system is using partitions and calling search spaces. For example, if you configure
                                                                  the Forward No Coverage destination, you should also configure the Forward No Coverage Calling Search Space. If you do not
                                                                  configure the Forward No Coverage Calling Search Space, and the Forward No Coverage destination is in a partition, the forward
                                                                  operation may fail. |
| Note | When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, choose a
                                                                  different value in the Calling Search Space field for external calls. |
| Forward on CTI Failure | This field applies only to CTI route points and CTI ports. The fields in this row specify the forwarding treatment for external
                                                calls to this CTI route point or CTI port if the CTI route point or CTI port fails. Configure the following values: Voice Mail —Check this check box to use the configured values in the Voice Mail Profile Configuration window. Note When this check box is checked, Unified Communications Manager ignores the values in the Destination and Calling Search Space fields. Destination —This field specifies the directory number to which an internal nonconnected call is forwarded when an application that controls
                                                      that directory number fails. Use any dialable phone number, including an outside destination. Calling Search Space —This value applies to all devices that use this directory number. | Note | When this check box is checked, Unified Communications Manager ignores the values in the Destination and Calling Search Space fields. |
| Note | When this check box is checked, Unified Communications Manager ignores the values in the Destination and Calling Search Space fields. |
| Forward Unregistered Internal | This field applies to unregistered internal DN calls. The calls are rerouted to a specified destination or voicemail. Note You must also specify the maximum number of forwards in the Service Parameters Configuration window for a directory number in the Max Forward UnRegistered Hops to DN service parameter. This parameter specifies the maximum number of forward unregistered hops that are allowed for a directory number at the same
                                                            time. This parameter limits the number of times the call can be forwarded due to unregistered DN when a forwarding loop occurs.
                                                            Use this count to stop forward loops for external calls that have been Call Forward Unregistered. Unified Communications Manager terminates the call when the value that is specified in this service parameter is exceeded. | Note | You must also specify the maximum number of forwards in the Service Parameters Configuration window for a directory number in the Max Forward UnRegistered Hops to DN service parameter. This parameter specifies the maximum number of forward unregistered hops that are allowed for a directory number at the same
                                                            time. This parameter limits the number of times the call can be forwarded due to unregistered DN when a forwarding loop occurs.
                                                            Use this count to stop forward loops for external calls that have been Call Forward Unregistered. Unified Communications Manager terminates the call when the value that is specified in this service parameter is exceeded. |
| Note | You must also specify the maximum number of forwards in the Service Parameters Configuration window for a directory number in the Max Forward UnRegistered Hops to DN service parameter. This parameter specifies the maximum number of forward unregistered hops that are allowed for a directory number at the same
                                                            time. This parameter limits the number of times the call can be forwarded due to unregistered DN when a forwarding loop occurs.
                                                            Use this count to stop forward loops for external calls that have been Call Forward Unregistered. Unified Communications Manager terminates the call when the value that is specified in this service parameter is exceeded. |
| Forward Unregistered External | This field applies to unregistered external DN calls. The calls are rerouted to a specified destination or voicemail. Note You must also specify the maximum number of forwards in the Service Parameters Configuration window for a directory number in the Max Forward UnRegistered Hops to DN service parameter. This parameter specifies the maximum number of forward unregistered hops that are allowed for a directory number at the same
                                                            time. This parameter limits the number of times the call can be forwarded due to unregistered DN when a forwarding loop occurs.
                                                            Use this count to stop forward loops for external calls that have been Call Forward Unregistered. Unified Communications Manager terminates the call when the value that is specified in this service parameter is exceeded. | Note | You must also specify the maximum number of forwards in the Service Parameters Configuration window for a directory number in the Max Forward UnRegistered Hops to DN service parameter. This parameter specifies the maximum number of forward unregistered hops that are allowed for a directory number at the same
                                                            time. This parameter limits the number of times the call can be forwarded due to unregistered DN when a forwarding loop occurs.
                                                            Use this count to stop forward loops for external calls that have been Call Forward Unregistered. Unified Communications Manager terminates the call when the value that is specified in this service parameter is exceeded. |
| Note | You must also specify the maximum number of forwards in the Service Parameters Configuration window for a directory number in the Max Forward UnRegistered Hops to DN service parameter. This parameter specifies the maximum number of forward unregistered hops that are allowed for a directory number at the same
                                                            time. This parameter limits the number of times the call can be forwarded due to unregistered DN when a forwarding loop occurs.
                                                            Use this count to stop forward loops for external calls that have been Call Forward Unregistered. Unified Communications Manager terminates the call when the value that is specified in this service parameter is exceeded. |
| No Answer Ring Duration (seconds) | This field specifies the seconds to wait before forwarding the unanswered call to the Call Forward No Answer destination,
                                                if specified. Make sure the value that is specified in this parameter is less than the value that is specified in the T301 Timer service parameter. If the value in the Forward No Answer Timer service parameter is greater than the value that is specified in the T301 Timer service parameter, the call is not forwarded and the caller receives a busy signal. Leave this field empty if you want to set the value in the Cisco Unified Communications Manager Forward No Answer Timer service parameter. |

| Note | When this check box is checked, Unified Communications Manager ignores the values in the Destination and Calling Search Space fields. |
|---|---|

| Note | When this check box is checked, the calling search space of the voicemail pilot is used. Unified Communications Manager ignores the values in the Destination and the Calling Search Space fields. |
|---|---|

| Note | When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to be forwarded to the voicemail system, you must uncheck
                                                                  the Voice Mail check box for external calls. |
|---|---|

| Note | When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls. |
|---|---|

| Note | If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured Call Forward Calling
                                                                  Search Space is used to forward the call. If the Calling Search Space field is set to None , the forward operation fails if the system uses partitions and calling search spaces. For example, if you configure the Forward
                                                                  Busy destination, you should also configure the Forward Busy Calling Search Space. If you do not configure the Forward Busy
                                                                  Calling Search Space and the Forward Busy destination is in a partition, the forward operation fails. |
|---|---|

| Note | When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, you must
                                                                  choose a different value in the Calling Search Space field for external calls. |
|---|---|

| Tip | Keep the busy trigger slightly lower than the maximum number of calls so that users can make outgoing calls and perform transfers. |
|---|---|

| Tip | If a call gets forwarded to a directory number that is busy, the call is not completed. |
|---|---|

| Note | When this check box is checked, the calling search space of the voicemail pilot is used. Unified Communications Manager ignores the values in the Destination and the Calling Search Space fields. |
|---|---|

| Note | When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to be forwarded to the voicemail system, you must uncheck
                                                                  the Voice Mail check box for external calls. |
|---|---|

| Note | When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls. |
|---|---|

| Note | If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured Call Forward Calling
                                                                  Search Space is used to forward the call. If the Calling Search Space field is set to None , the forward operation fails if the system uses partitions and calling search spaces. For example, if you configure the Forward
                                                                  Busy destination, you should also configure the Forward Busy Calling Search Space. If you do not configure the Forward Busy
                                                                  Calling Search Space and the Forward Busy destination is in a partition, the forward operation fails. |
|---|---|

| Note | When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, you must
                                                                  choose a different value in the Calling Search Space field for external calls. |
|---|---|

| Note | When this check box is checked, the calling search space of the voicemail pilot is used. Unified Communications Manager ignores the values in the Destination and the Calling Search Space fields. |
|---|---|

| Note | When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to be forwarded to the voicemail system, you must uncheck
                                                                  the Voice Mail check box for external calls. |
|---|---|

| Note | When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls. |
|---|---|

| Note | If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured Call Forward Calling
                                                                  Search Space is used to forward the call. If the Calling Search Space field is set to None , the forward operation fails if the system uses partitions and calling search spaces. For example, if you configure the Forward
                                                                  No Answer destination, you should also configure the Forward No Answer Calling Search Space. If you do not configure the Forward
                                                                  No Answer Calling Search Space and the Forward No Answer destination is in a partition, the forward operation fails. |
|---|---|

| Note | When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, you must
                                                                  choose a different value in the Calling Search Space field for external calls. |
|---|---|

| Note | When this check box is checked, the calling search space of the voicemail pilot is used. Unified Communications Manager ignores the values in the Destination and the Calling Search Space fields. |
|---|---|

| Note | When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to be forwarded to the voicemail system, you must uncheck
                                                                  the Voice Mail check box for external calls. |
|---|---|

| Note | When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls. |
|---|---|

| Note | If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured Call Forward Calling
                                                                  Search Space is used to forward the call. If the Calling Search Space field is set to None , the forward operation fails if the system uses partitions and calling search spaces. For example, if you configure the Forward
                                                                  Busy destination, you should also configure the Forward No Answer Calling Search Space. If you do not configure the Forward
                                                                  No Answer Calling Search Space and the Forward No Answer destination is in a partition, the forward operation fails. |
|---|---|

| Note | When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, you must
                                                                  choose a different value in the Calling Search Space field for external calls. |
|---|---|

| Note | When this check box is checked, Unified Communications Manager ignores the values in the Destination and Calling Search Space fields. When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to forward to the voicemail system, you must uncheck the Voice Mail check box for external calls. |
|---|---|

| Note | When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls. |
|---|---|

| Note | If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured Call Forward Calling
                                                                  Search Space is used to forward the call. If the Calling Search Space field is set to None, the forward operation fails if the system uses partitions and calling search spaces. For example, if
                                                                  you configure the Forward Busy destination, you should also configure the Forward No Coverage Calling Search Space. If you
                                                                  do not configure the Forward No Coverage Calling Search Space and the Forward Busy destination is in a partition, the forward
                                                                  operation fails. |
|---|---|

| Note | When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, you must
                                                                  choose a different value in the Calling Search Space field for external calls. |
|---|---|

| Note | When this check box is checked, Unified Communications Manager ignores the values in the Destination and the Calling Search Space fields. When this check box is checked for internal calls, the system automatically checks the Voice Mail check box for external calls. If you do not want external calls to forward to the voicemail system, you must uncheck the Voice Mail check box for external calls. |
|---|---|

| Note | When you enter a destination value for internal calls, the system automatically copies this value to the Destination field for external calls. If you want external calls to be forwarded to a different destination, you must enter a different
                                                                  value in the Destination field for external calls. |
|---|---|

| Note | If the system is using partitions and calling search spaces, Cisco recommends that you configure the Call Forward Calling
                                                                  Search Spaces. When a call is forwarded or redirected to the Call Forward destination, the configured call forward calling
                                                                  search space is used to forward the call. If the Calling Search Space is None , the forward operation may fail if the system is using partitions and calling search spaces. For example, if you configure
                                                                  the Forward No Coverage destination, you should also configure the Forward No Coverage Calling Search Space. If you do not
                                                                  configure the Forward No Coverage Calling Search Space, and the Forward No Coverage destination is in a partition, the forward
                                                                  operation may fail. |
|---|---|

| Note | When you choose a calling search space for internal calls, the system automatically copies this value to the calling search
                                                                  space setting for external calls. If you want external calls to be forwarded to a different calling search space, choose a
                                                                  different value in the Calling Search Space field for external calls. |
|---|---|

| Note | When this check box is checked, Unified Communications Manager ignores the values in the Destination and Calling Search Space fields. |
|---|---|

| Note | You must also specify the maximum number of forwards in the Service Parameters Configuration window for a directory number in the Max Forward UnRegistered Hops to DN service parameter. This parameter specifies the maximum number of forward unregistered hops that are allowed for a directory number at the same
                                                            time. This parameter limits the number of times the call can be forwarded due to unregistered DN when a forwarding loop occurs.
                                                            Use this count to stop forward loops for external calls that have been Call Forward Unregistered. Unified Communications Manager terminates the call when the value that is specified in this service parameter is exceeded. |
|---|---|

| Note | You must also specify the maximum number of forwards in the Service Parameters Configuration window for a directory number in the Max Forward UnRegistered Hops to DN service parameter. This parameter specifies the maximum number of forward unregistered hops that are allowed for a directory number at the same
                                                            time. This parameter limits the number of times the call can be forwarded due to unregistered DN when a forwarding loop occurs.
                                                            Use this count to stop forward loops for external calls that have been Call Forward Unregistered. Unified Communications Manager terminates the call when the value that is specified in this service parameter is exceeded. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . The Service Parameter Configuration window is displayed. |
|---|---|
| Step 2 | In the Clusterwide Parameters (Feature - Hold Reversion) area, set the CFA
                                             				Destination Override service parameter value to True . |

| Feature | Interaction |
|---|---|
| Call
                                          						Back | Calls
                                          						that are made from the CallBack notification screen will override all the Call
                                          						Forward configured values  on the target DN. The calls should be made before the CallBack
                                          						recall timer expires, otherwise the calls will not override the Call Forward
                                          						configured values. |
| Call
                                          						Display Restrictions | The Connected Number Display restriction applies to all calls that originate in the system. When this value is set to True , this field interacts transparently with existing Unified Communications Manager applications, features, and call processing. The value applies to all calls that terminate inside or outside the system.
                                          The Connected Number Display is updated to show the modified number or redirected number when a call is routed to a Call Forward
                                          All or Call Forward Busy destination, or gets redirected through a call transfer or CTI application. |
| Do Not
                                          						Disturb | On Cisco
                                          						Unified IP Phones, the message that indicates that the Do Not Disturb (DND)
                                          						feature is active takes priority over the message that indicates that the user
                                          						has new voice messages. However, the message that indicates that the Call
                                          						Forward All feature is active has a higher priority than DND. |
| External
                                          						Call Control | External Call Control intercepts calls at the translation pattern level, while Call Forward intercepts calls at the directory
                                          number level. External Call Control has higher priority; for calls where call forward is invoked, Unified Communications Manager sends a routing query to the adjunct route server if the translation pattern has an External Call Control profile assigned
                                          to it. Call Forwarding is triggered only when the adjunct route server sends a Permit decision with a Continue obligation
                                          to the Unified Communications Manager . Note The Call Diversion Hop Count service parameter that supports External Call Control,
                                                   						and the Call Forward Call Hop Count service parameter that supports Call
                                                   						Forwarding are independent of each other; they work separately. | Note | The Call Diversion Hop Count service parameter that supports External Call Control,
                                                   						and the Call Forward Call Hop Count service parameter that supports Call
                                                   						Forwarding are independent of each other; they work separately. |
| Note | The Call Diversion Hop Count service parameter that supports External Call Control,
                                                   						and the Call Forward Call Hop Count service parameter that supports Call
                                                   						Forwarding are independent of each other; they work separately. |
| Extension Mobility Cross Cluster | Cisco
                                          						Extension Mobility Cross Cluster supports Call Forwarding. |
| Extend
                                          						and Connect | Extend
                                          						and Connect supports Call Forward All. |
| Immediate Divert | When the
                                          						Forward No Answer field  in the Directory Number Configuration window is not
                                          						configured, Call Forward uses the clusterwide CFNA timer service parameter, Forward No Answer Timer . If a
                                          						user presses the iDivert softkey at the same time as the call is being
                                          						forwarded, the call gets diverted to an assigned call forward directory number
                                          						(because the amount of time set on the timer was too short), not the voicemail. To resolve this situation, set the CFNA
                                          timer service parameter to
                                          						enough time (for example, 60 seconds). |
| Logical
                                          						Partitioning | Unified Communications Manager performs logical partitioning policy check using the geolocation identifier information that associates with the incoming
                                          and forwarded devices. This handling applies to all types of call forwarding. |
| Multilevel Precedence and Preemption (MLPP) | Call Forward Busy You can optionally configure a preconfigured Precedence Alternate Party target for any MLPP-enabled station. Cisco Unified Communications Manager applies the Call Forward Busy feature to forward a precedence call in the usual manner before it applies to any Precedence
                                                Alternate Party Diversion procedures to the call. The system preserves precedence of calls across multiple forwarded calls. If the incoming precedence call is of higher precedence than the existing call, preemption occurs. Both the preempted parties
                                                in the active call receive a continuous preemption tone until the station to which the precedence call is directed hangs up.
                                                After hanging up, the station to which the precedence call is directed receives precedence ringing. The destination station
                                                connects to the preempting call when the station goes off hook. Call Forward No Answer For calls of Priority precedence level and above, call processing preserves the precedence level of calls during the forwarding
                                                process and may preempt the forwarded-to user. If an Alternate Party is configured for the destination of a precedence call, call processing diverts the precedence call
                                                to the Alternate Party after the Precedence Call Alternate Party timeout expires. If no Alternate Party value is configured
                                                for the destination of a precedence call, call processing diverts the precedence call to the Call Forward No Answer value. Normally, precedence calls are routed to users and not to the voicemail system. The administrator sets the Use Standard VM Handling For Precedence Calls enterprise parameter to avoid routing precedence calls to voicemail systems. If the
                                          						incoming precedence call is of equal or lower precedence than the existing
                                          						call, call processing invokes normal call-forwarding behavior. If the
                                          						destination station for a precedence call is nonpreemptable (that is, not
                                          						MLPP-configured), call processing invokes call-forwarding behavior. Alternate Party Diversion (APD) comprises a special type of call
                                          						forwarding. If users are configured for APD, APD takes place when a precedence
                                          						call is directed to a directory number (DN) that is busy or does not answer.
                                          						MLPP APD applies only to precedence calls. An MLPP APD call disables the DN
                                          						Call Forward No Answer value  for precedence calls. |
| Originally called party name in Placed Call History | When
                                          						privacy is configured only in the SIP profile of the called party device and
                                          						Call Forward All (CFA), or Call Forward Busy (CFB), or Call Forward
                                          						Unregistered (CFUR) is enabled, the configured alerting name is displayed
                                          						instead of "private" . To ensure that "private" is displayed for call forwarding, Cisco recommends
                                          						that you configure the name presentation restriction in the translation pattern
                                          						or the route pattern rather than in the SIP profile. |
| Rollover Lines | By using call forwarding settings, you can create rollover lines for a shared line. This could be a useful for some call center
                                          situations. With rollover lines, when someone dials a number (e.g. 1-800-HOTLINE), the call always is routed to a specific phone line.
                                          This may be a shared line that is shared by multiple phones. If line 1 is busy, the call rolls over to line 2, if line 2 is
                                          busy it rolls over to line 3, and so on. Line 2 or 3 become available only if line 1 is busy. This type of call functionality is possible via call forwarding busy settings and the Busy Trigger as follows: On line 1, set the Busy Trigger to 1 and configure Call Forward Busy to the second line in the chain. On line 2, set the Busy Trigger to 1 and configure Call Forward Busy to the third line in the chain Continue this for as many lines as meets your needs. |
| Secure
                                          						Tone | Call
                                          						Forward All is supported on protected phones. |
| Session
                                          						Handoff | When
                                          						the user hands off a call, a new call gets presented on the desk phone. While
                                          						the desk phone is flashing, Call Forward All is not triggered on the desk phone
                                          						for the call that was handed off. |
| Shared Lines | When you use a shared line with Call Forward All (CFA) setting and choose the 'Calling Number' as 'Redirected Party's External
                                          Phone Number' presentation in the outgoing trunk, then the redirected number that is displayed may not be consistent when
                                          shared lines have different E164 numbers configured. So we recommend using the same E164 number across Shared lines. |

| Note | The Call Diversion Hop Count service parameter that supports External Call Control,
                                                   						and the Call Forward Call Hop Count service parameter that supports Call
                                                   						Forwarding are independent of each other; they work separately. |
|---|---|

| Feature | Restriction |
|---|---|
| Call Forwarding | If Call Forward All activation occurs in Unified Communications Manager or the Cisco Unified Communications Self Care Portal, Unified Communications Manager does not prevent the CFA loop. Unified Communications Manager prevents Call Forward All loops if CFA is activated from the phone, if the number of hops for a Call Forward All call exceeds
                                             the value that is specified for the Forward Maximum Hop Count service parameter, and if all phones in the forwarding chain
                                             have CFA activated (not CFB, CFNA, or any other call forwarding options). For example, if the user with directory number 1000 forwards all calls to directory number 1001, which has CFB and CFNA configured
                                             to directory number 1002, which has CFA configured to directory number 1000, Unified Communications Manager allows the call to occur because directory number 1002 acts as the CFB and CFNA (not CFA) destination for directory number
                                             1001. You cannot activate Call Back if you forward all calls to
                                             						  voicemail system. An uncommon condition in connection with the Forward No Answer
                                             						  Timeout exists when you press the iDivert softkey. For example, if a manager
                                             						  presses the iDivert softkey immediately after the Forward No Answer timeout,
                                             						  Call Forward forwards the call to a preconfigured directory number. However, if
                                             						  the manager presses the iDivert softkey before the Forward No Answer timeout,
                                             						  Immediate Divert diverts the call to the voicemail of the manager. |
| Immediate Divert | When Call Forward All (CFA) and Call Forward Busy (CFB) are
                                       					 activated, the system does not support Immediate Divert (CFA and CFB have
                                       					 precedence over Immediate Divert). |
| Intercom | You cannot forward Intercom calls. |
| Log Out of Hunt Group | When a phone that is running SIP (7906, 7911, 7941, 7961) is logged in to hunt groups and Call Forward All is activated, the
                                       call gets presented to the phone that is running SIP. When 7940
                                       					 and 7960 IP phones that are running SIP are logged in to hunt groups and Call
                                       					 Forward All is activated, the phone gets skipped and the next phone in the line
                                       					 group is rung. |
| Logical Partitioning | Logical partitioning handling does not take place in the following circumstances: When both the caller and forwarded devices are Voice over IP (VoIP) phones. When geolocation or a geolocation filter is not associated with any device. |
| Multilevel Precedence and Preemption (MLPP) | Multilevel Precedence and Preemption (MLPP) support for
                                       					 supplementary services specifies the following restrictions for Call
                                       					 Forwarding: Call
                                             						  Forward All (CFA) support for inbound MLPP calls always forwards the call to
                                             						  the MLPP Alternate Party (MAP) target of the called party, if the MAP target is
                                             						  configured. In the event of an incorrect configuration (that is, if no MAP
                                             						  target is specified), the call gets rejected, and the calling party receives
                                             						  reorder tone. Call
                                             						  Forward No Answer (CFNA) support for inbound MLPP calls forwards the call once
                                             						  to a CFNA target. After the first hop, if the call remains unanswered, the call
                                             						  is sent to the MAP target of the original called party, if the MAP target is
                                             						  configured. In the event of an incorrect configuration (that is, if no MAP
                                             						  target is specified), the call gets rejected, and the calling party receives
                                             						  reorder tone. Call
                                             						  Forward Busy (CFB) support for inbound MLPP calls forwards the call up to the
                                             						  maximum number that is configured for forwarding hops. If the maximum hop count
                                             						  is reached, the call is sent to the MAP target of the original called party, if
                                             						  the MAP target is configured. In the event of an incorrect configuration (that
                                             						  is, no MAP target is specified), the call gets rejected, and the calling party
                                             						  receives reorder tone. |
| Call Forward Classification with Call Transfer | When a call is transferred, the call classification takes on the classification of the transferred leg, rather than the original
                                       leg. For example: Incoming call from PSTN is received by a receptionist. This is an external call. The receptionist transfers the call to extension 3100. The transferred call is now an internal call. The user at extension 3100 is busy, but has Call Forward External configured to send external calls back to the receptionist.
                                             However, because the call takes on the classification of the second leg (internal), the call goes to voicemail. |