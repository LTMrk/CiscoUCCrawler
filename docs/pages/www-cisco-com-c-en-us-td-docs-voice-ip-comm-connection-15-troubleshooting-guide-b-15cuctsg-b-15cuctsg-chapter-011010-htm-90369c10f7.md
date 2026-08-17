---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-troubleshooting-guide-b-15cuctsg-b-15cuctsg-chapter-011010-htm-90369c10f7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/troubleshooting/guide/b_15cuctsg/b_15cuctsg_chapter_011010.html
retrieved_at: 2026-08-17T02:40:10.105059+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 15

# Troubleshooting Guide for Cisco Unity Connection Release 15

Updated: August 22, 2025

Chapter: Troubleshooting Personal Call Transfer Rules

## Chapter: Troubleshooting Personal Call Transfer Rules

# Troubleshooting Personal Call Transfer Rules

Troubleshooting Personal Call Transfer Rules

## Personal Call
                        	 Transfer Rules Settings Unavailable

If a user does not
                           		hear the Personal Call Transfer Rules Settings menu in the phone interface or
                           		if a user cannot see the Cisco Unity Connection Personal Call Transfer Rules
                           		web tool link in the Cisco Personal Communications Assistant, confirm that the
                           		user is assigned to a class of service that is enabled for access to the
                           		Personal Call Transfer Rules web tool.

In addition, do the following procedure to confirm that the value of the Region Unrestricted Feature licensing option is set
                           to Yes. If the value is set to No, you cannot use personal call transfer rules, and you cannot use English-United States language.
                           To resolve the problem, install a license in which the feature is enabled, and restart Cisco Unity Connection. (An additional
                           fee might be required to enable the feature. Contact your Cisco account team to obtain the updated license file.) For details,
                           see the “ Managing Licenses ” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

### Determining the
                           	 Value of the Region Unrestricted Feature Licensing Option

Step 1

In Cisco Unity Connection Administration, expand System Settings , then select Licenses .

Step 2

Below the License Count table, confirm that the value of US
                                          			 English Usage and Personal Call Routing Rules Allowed (LicRegionIsUnrestricted)
                                          			 is set to Yes.

## Personal Call Transfer Rules and Destinations

Personal call transfer rules can forward calls to a phone destination, a destination group, or to voicemail. The destination
                           group must contain at least one phone destination, and can also contain SMS and SMTP devices. The destinations in a destination
                           group are tried serially in the priority order in which they are listed until a destination phone is answered or the caller
                           hangs up.

When a user has entered phone numbers for notification devices in the Messaging Assistant web tool, the numbers are displayed
                           on the View Destinations page and can be used as destinations for rules. The notification devices do not need to be enabled.
                           These prepopulated destinations cannot be edited or deleted in the Personal Call Transfer Rules web tool. They can be edited
                           only on the Notification Devices page in the Messaging Assistant.

Note that pager destinations are not supported destinations for rules, and thus are not displayed on the View Destinations
                           page.

## Call Screening and Call Holding Options

If call screening and call holding options are not available in the Personal Call Transfer Rules web tool, use the following
                           information to troubleshoot the possible causes:

Confirm that the user belongs to a class of service that allows access to the call screening and/or call holding options.

Call holding applies only to calls to primary extensions.

In the Personal Call Transfer Rules web tool, the Screen the Call check box may be grayed out even when the user belongs to
                                 a class of service that allows access to call screening options. If the option is grayed out, do the following procedure to
                                 correct the problem.

### Enabling the
                           	 Screen the Call Option in the Personal Call Transfer Rules Web Tool

Step 1

In the Personal Call Transfer Rules web tool, on the Preferences
                                          			 menu, select Call Holding and Screening .

Step 2

On the Call Holding and Call Screening Options page, confirm
                                          			 that at least one option under the Screen Calls section is enabled.

## Problems with the Application of Rules

When rules are not applied as expected, consider the following possible issues:

An active rule set has been created but it fails when the user receives a call —See the “Rules Not Applied When a User with Active Rules Receives a Call” section on page 27-3 .

A rule applies to all incoming calls when the user expected it to be applied only to calls from a specific caller —Personal call transfer rules can be created without a “From” condition (set up either as “from” or “not from”). When set
                                 up this way, the rules are applied to all incoming calls.

Rules associated with meetings or calendar entries are not working as expected —See the “Rules Based on a Meeting Condition Not Applied Correctly” section on page 27-4 .

Rules based on a caller or caller group are not applied correctly —Phone numbers that have been set for the primary extension, home phone, work phone, or mobile device of a user, or for administrator-defined
                                 or user-defined contacts must match the incoming caller ID or ANI. Confirm that the phone number of the caller that is specified
                                 in Unity Connection matches the incoming caller ID or ANI.

Rules based on a time condition are not applied correctly —Confirm that the correct time zone has been selected for the user. In Cisco Unity Connection Administration, on the Edit
                                 User Basics page for the user, change the selected time zone if necessary.

### Rules Not Applied When a User with Active Rules Receives a Call

There are several reasons that a rule set can fail:

Personal call transfer rules are used only when the active basic rule—the standard, alternate or closed transfer rule—is set
                                    to apply personal call transfer rules instead of the basic settings.

If the rule set is specified for a day of the week, but another rule set is enabled for a date range that includes the current
                                    date, the date range rule set takes precedence.

Transfers to a destination without a complete dialable phone number may fail. If there is no other destination to try, the
                                    caller is transferred to voicemail.

Use the following troubleshooting steps to resolve the problem:

Confirm that the active basic transfer rule is configured to use personal call transfer rules. See the “Configuring Basic Transfer Rules to Use Personal Call Transfer Rules” section on page 27-3 .

Use the Call Transfer Rule Tester to check the validity of the rule. The test tells you which rule is currently being invoked.
                                    Based on the results, you may want to reprioritize the rules within the rule set.

The rule set that contains the rule that you are testing must be enabled or active in order for the Call Transfer Rule Tester
                                                to work.

Confirm that the destinations for the rule set contain dialable phone numbers, including any outdial access codes required
                                    by the phone system.

On the Rules Settings page, confirm that the Disable All Processing of Personal Call Transfer Rules check box is not checked.
                                    When the check box is checked, all rule processing is disabled.

#### Configuring Basic Transfer Rules to Use Personal Call Transfer Rules

Personal call transfer rules are used only when the active basic rule—the standard, alternate or closed transfer rule—is set
                                 to apply personal call transfer rules instead of the basic settings.

To turn on personal call transfer rules for a user, do the following procedure.

Users can also use the Messaging Assistant to configure their basic transfer rules to apply personal call transfer rules.

### Turning On
                           	 Personal Call Transfer Rules for an Individual User

Step 1

In Cisco Unity Connection Administration, expand Users , then select Users . On the Search Users page, select the alias of
                                          			 the user for whom you want to turn on personal call transfer rules.

Step 2

On the Edit menu, select Transfer Rules .

Step 3

In the Transfer Rules table, select the transfer rule that you
                                          			 want to use with personal call transfer rules.

Step 4

On the Edit Transfer Rule page, in the When This Basic Rule Is
                                          			 Active field, select Apply Personal Call Transfer Rules and select Save.

Step 5

Repeat Step 2 through Step 4 for each
                                          			 additional transfer rule that you want to use.

### Rules Based on a
                           	 Meeting Condition Not Applied Correctly

When a
                              		personal call transfer rule has a condition that is based on a Microsoft
                              		Exchange calendar appointment, the rule might not be applied as expected.
                              		Calendar information is cached every 30 minutes, so a newly created appointment
                              		may not yet be cached.

Try the following troubleshooting steps:

Confirm that the Exchange external service is configured
                                    			 properly. In Cisco Unity Connection Administration, expand Unified
                                    			 Messaging > Unified Messaging Services, confirm that all settings are
                                    			 correct.

Confirm that the applicable service is configured as an Unified
                                    			 Messaging Account for the user. In Cisco Unity Connection Administration,
                                    			 select Users and search for the user. On the Edit User Basics page, on the Edit
                                    			 menu, select Unified Messaging Accounts and verify settings.

See the “ Calendar and Contact Integration ” section of the “Introduction to Unified Messaging” chapter of the Unified Messaging Guide for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/unified_messaging/guide/b_15cucumgx.html for detailed information on setting up external service accounts.

Confirm that the Exchange-server and Unity Connection-server
                                    			 clocks are synchronized to the same time source.

If you believe that the problem is due to newly created calendar
                                    			 appointments, you can get around the 30-minute lag for caching appointments by
                                    			 forcing an immediate caching. See the “Forcinging
                                       				an Immediate Caching of Calendar Appointments” section on page 27-4 .

To permanently change the interval at which Unity Connection
                                    			 caches calendar information, see the “Changing
                                       				the Interval at Which Unity Connection Caches Calendar Information” section on
                                       				page 27-4 .

#### Forcinging an
                              	 Immediate Caching of Calendar Appointments

Do the following procedure to force Cisco Unity Connection to
                                    		  immediately cache calendar information.

Step 1

In Cisco Unity Connection Serviceability, on the Tools menu,
                                             			 select Service Management.

Step 2

Under Optional Services, for the Connection Groupware Caching
                                             			 Service, select Stop.

Step 3

After the screen refreshes, for the Connection Groupware Caching
                                             			 Service, select Start.

#### Changing the
                              	 Interval at Which Unity Connection Caches Calendar Information

This setting applies to users who have the Use Short Calendar
                                    		  Caching Poll Interval check box checked on the Edit User Basics page and select
                                    		  Save.

Step 1

In Cisco Unity Connection Administration, expand System Settings > Advanced , then select Unified Messaging Services.

Step 2

On the Unified Messaging Services Configuration page, in the
                                             			 Calendars: Normal Calendar Caching Poll Interval (In Minutes) field, enter the
                                             			 length of time that Unity Connection waits between polling cycles when it
                                             			 caches upcoming Outlook calendar data for users who are configured for a
                                             			 calendar integration.

A larger number reduces the impact on the Unity Connection
                                                				server while reducing the ability of the server to handle last-minute changes
                                                				to the Outlook calendar data for users in a timely manner. A smaller number
                                                				increases the impact on the Unity Connection server while increasing the
                                                				ability of the server to handle last-minute changes to the Outlook calendar
                                                				data for users in a timely manner.

Step 3

In the Calendars: Short Calendar Caching Poll Interval (In
                                             			 Minutes) field, enter the length of time that Unity Connection waits between
                                             			 polling cycles when it caches upcoming Outlook calendar data for calendar users
                                             			 who must have their calendar caches updated more frequently.

#### Changing the
                              	 Interval at Which Unity Connection Caches Calendar Information

This setting applies to users who have the Use Short Calendar
                                    		  Caching Poll Interval check box checked on the Edit User Basics page and select
                                    		  Save.

Step 1

In Cisco Unity Connection Administration, expand System Settings > Advanced , then select External Services.

Step 2

On the External Services Configuration page, in the Normal
                                             			 Calendar Caching Poll Interval field, enter the length of time in minutes that
                                             			 Unity Connection waits between polling cycles when it caches upcoming Outlook
                                             			 calendar data for users who are configured for a calendar integration.

A larger number reduces the impact on the Unity Connection
                                                				server while reducing the ability of the server to handle last-minute changes
                                                				to the Outlook calendar data for users in a timely manner. A smaller number
                                                				increases the impact on the Unity Connection server while increasing the
                                                				ability of the server to handle last-minute changes to the Outlook calendar
                                                				data for users in a timely manner.

Step 3

In the Short Calendar Caching Poll Interval field, enter the
                                             			 length of time (in minutes) that Unity Connection waits between polling cycles
                                             			 when it caches upcoming Outlook calendar data for calendar users who must have
                                             			 their calendar caches updated more frequently.

## Problems with Transfer All Rule

The following issues can occur when using the Transfer All rule:

You are unable to create a Transfer All rule —You cannot create a Transfer All rule in the Personal Call Transfer Rules web tool. The Transfer All rule can be created
                                 only by phone. After the rule has been added by phone, it can be edited in the Personal Call Transfer Rules web tools. Both
                                 the destination and duration can be changed in the web tool.

The Transfer All rule is not applied as expected —If the Transfer All rule is not being applied as expected, confirm that the destination number includes any outdial access
                                 codes required by the phone system.

## Phone Menu Behavior Using Personal Call Transfer Rules

When phone menus do not behave as expected when using personal call transfer rules, consider the following possible issues:

Users cannot change personal call transfer rules using voice commands— The voice-recognition feature does not yet support the Personal Call Transfer Rules phone menu options. If users want to use
                                 personal call transfer rules, they must temporarily switch to using the phone keypad. They can temporarily switch to using
                                 the phone keypad by saying “Touchtone conversation,” or by pressing 9 at the Main menu.

Phone menu options for personal call transfer rules vary —Users may notice variations in the phone menus for personal call transfer rules that they hear. Personal Call Transfer Rules
                                 phone menu options are built dynamically, and they depend on the existing rule sets and which sets are enabled and active.

The phone menu for setting or cancelling call forwarding is unavailable —See the “Phone Menu Option to Set or Cancel Forwarding All Calls to Unity Connection Unavailable” section on page 27-6 .

Users notice inconsistencies in how calls are placed through Cisco Unity Connection or dialed directly —See the “Inconsistent Behavior in Calls Placed through Unity Connection and Calls Placed Directly to a User Phone” section on page 27-6 .

Calls loop during rule processing —See the “Call Looping During Rule Processing” section on page 27-7 .

### Phone Menu Option
                           	 to Set or Cancel Forwarding All Calls to Unity Connection Unavailable

The information in this section is not applicable to Cisco
                                          		  Business Edition.

If the phone menu option that sets or cancels forwarding all
                              		calls to Cisco Unity Connection is unavailable, try the following
                              		troubleshooting steps:

Confirm that the AXL server settings for the phone system are
                                    			 correct. In Cisco Unity Connection Administration, expand Telephony
                                    			 Integrations > Phone System. On the Phone System Basics page, on the Edit
                                    			 menu, select Cisco Unified CM AXL Servers, and verify settings.

See the “ Phone System ” section of the “Telephony Integrations” chapter of the System Administration Guide for Cisco Unity Connection Release 15 for detailed information about AXL server settings. The guide is available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html .

Check to see if the publisher Cisco Unified CM server is shut
                                    			 down or if there are network connectivity issues between Unity Connection and
                                    			 the publisher Cisco Unified CM servers. Use the Test button on the Edit AXL
                                    			 Server page to test the connection. If the Cisco Unified CM publisher database
                                    			 is down, Unity Connection cannot change the Call Forward All (CFA) setting for
                                    			 the phone.

The option to forward all calls to Unity Connection is available
                              		only in integrations with Cisco Unified CM versions 4.0 and later. The option
                              		is not available with earlier versions of Cisco Unified CM or with Cisco
                              		Unified CM Express.

### Inconsistent Behavior in Calls Placed through Unity Connection and Calls Placed Directly to a User Phone

Callers may notice inconsistent behavior when calling a user through the Unity Connection automated attendant and when dialing
                              the user phone directly. Rules are typically applied immediately to calls placed through the automated attendant, while direct
                              calls must wait until the Call Forward No Answer timer for the phone expires before the call is forwarded to Unity Connection.
                              Rules are then applied.

Use the following steps to provide a consistent caller experience regardless of how a call is placed:

To set a user phone to always ring first before rules are applied, turn off the Forward All Calls to Cisco Unity Connection
                                    feature by phone. Then, in the Personal Call Transfer Rules web tool, on the Preferences menu, select Rules Settings. On the
                                    Rules Settings page, check the Always Ring Primary Extension Before Applying Call Transfer Rules check box.

To set user rules for immediate processing, turn on the Forward All Calls to Cisco Unity Connection feature by phone. Then,
                                    in the Personal Call Transfer Rules web tool, on the Preferences menu, select Rules Settings. On the Rules Settings page,
                                    uncheck the Always Ring Primary Extension Before Applying Call Transfer Rules check box.

### Call Looping During Rule Processing

Call looping can occur when calls that are forwarded by Unity Connection are forwarded back to Unity Connection and rules
                              are applied again. Callers may experience inconsistent behavior, such as repeated instances of the opening greeting or continuous
                              attempts to reach the same destination.

The following settings can be used to prevent call looping conditions:

In Cisco Unity Connection Administration, expand Telephony Integrations > Phone System and select the applicable phone system.
                                    On the Phone System Basics page, check the Enable for Supervised Transfers check box. The Enable for Supervised Transfers
                                    setting causes Unity Connection to detect and terminate call looping conditions so that calls proceed correctly.

In the Personal Call Transfer Rules web tool, on the Destinations > View Destinations page, check the Loop Detection Enabled
                                    check box for any phone-type destinations to help eliminate call-looping problems with Unity Connection forwarding calls to
                                    the mobile phone of the user, and the mobile phone forwarding the calls back to Unity Connection. When the Loop Detection
                                    setting is enabled, Unity Connection either transfers the call to the next assigned device (if the user has created a destination
                                    group) or transfers the call to voicemail if there are no additional destinations defined.

Allow Unity Connection to maintain control of calls by setting the value in the Rings to Wait field for rule destinations
                                    to be less than the value in the Cisco Unified Communications Manager Forward No Answer Timer field. The Cisco Unified CM
                                    Forward No Answer Timer value defaults to 12 seconds. A ring occurs approximately every 3 seconds. Therefore, setting the
                                    Rings to Wait value for Unity Connection destinations to 3 rings allows Unity Connection to maintain control of the call.
                                    The supervised transfer initiated by Unity Connection pulls the call back before the loop begins, and attempts to transfer
                                    the call to the next destination or to voicemail, as applicable.

## Using Diagnostic
                        	 Traces for Personal Call Transfer Rules

You can use traces to troubleshoot problems with personal call
                           		transfer rules. For detailed instructions on enabling and collecting diagnostic
                           		traces, see the Using Diagnostic Traces for Troubleshooting chapter.

Enable the following micro traces to troubleshoot personal call
                           		transfer rules:

CCL (levels 10, 11, 12, 13)—Used when accessing calendar
                                 			 information.

CDE (all levels)—Used in rules-related conversations.

ConvSub (all levels)—Used when configuring personal call
                                 			 transfer rules settings by phone.

ConvRoutingRules (all levels)—Used when a rules-enabled user
                                 			 receives a call and while transferring calls between destinations.

CsWebDav (levels 10, 11, 12, 13)—Used when accessing calendar
                                 			 information.

RulesEngine (all levels)—Used in rule processing during calls to
                                 			 a rules-enabled user to determine the applicable rule. Also used in determining
                                 			 the applicable rule when using the Rules Tester.

If necessary, enable the following micro traces for the
                           		supporting components:

CDL—Used in rules-related conversations.

CuGAL—Used in rule processing with a meeting condition and for
                                 			 importing contacts from Exchange.

MiuCall MiuGeneral—Used in rule processing during calls to a
                                 			 rules-enabled user.

PhraseServer—Used in rules-related conversations to play
                                 			 prompts.

Notifier—Used in rule processing when sending SMTP and SMS
                                 			 messages.

TextToSpeech—Used in rule-settings conversation.

## Using Performance
                        	 Counters for Personal Call Transfer Rules

### SUMMARY STEPS

- Launch Real-Time Monitoring Tool (RTMT).

- In RTMT, on the System menu, select Performance > Open
                                    				  Performance Monitoring .

- Expand the Unity Connection server.

- Expand CUC Personal Call Transfer Rules .

- Select the applicable counters:

### DETAILED STEPS

Step 1

Launch Real-Time Monitoring Tool (RTMT).

For details on using RTMT, see the Cisco Unified Real-Time Monitoring Tool Administration Guide, available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

Step 2

In RTMT, on the System menu, select Performance > Open
                                             				  Performance Monitoring .

Step 3

Expand the Unity Connection server.

Step 4

Expand CUC Personal Call Transfer Rules .

Step 5

Select the applicable counters:

Applicable Rule Found—Call resulted in rule processing, and an
                                                					 applicable rule was found.

Destinations Tried—Number of destinations tried while applying
                                                					 personal call transfer rules.

PCTR Calls—Call is subject to personal call transfer rules
                                                					 processing: user is assigned to a class of service that has the Personal Call
                                                					 Transfer Rules feature enabled; user is associated with a Cisco Unified CM
                                                					 phone system; and user has enabled personal call transfer rules.

Rules Evaluated—Number of rules evaluated during rule processing
                                                					 in a call.

Subscriber Reached—Number of times a user was reached while
                                                					 applying personal call transfer rules.

Transfer Failed—Number of times a transfer to a destination
                                                					 failed while applying personal call transfer rules.

Voice Mail Reached—Number of times voicemail was reached while
                                                					 applying personal call transfer rules.

| Step 1 | In Cisco Unity Connection Administration, expand System Settings , then select Licenses . |
|---|---|
| Step 2 | Below the License Count table, confirm that the value of US
                                          			 English Usage and Personal Call Routing Rules Allowed (LicRegionIsUnrestricted)
                                          			 is set to Yes. |

| Note | Call holding applies only to calls to primary extensions. |
|---|---|

| Step 1 | In the Personal Call Transfer Rules web tool, on the Preferences
                                          			 menu, select Call Holding and Screening . |
|---|---|
| Step 2 | On the Call Holding and Call Screening Options page, confirm
                                          			 that at least one option under the Screen Calls section is enabled. |

| Note | The rule set that contains the rule that you are testing must be enabled or active in order for the Call Transfer Rule Tester
                                                to work. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Users , then select Users . On the Search Users page, select the alias of
                                          			 the user for whom you want to turn on personal call transfer rules. |
|---|---|
| Step 2 | On the Edit menu, select Transfer Rules . |
| Step 3 | In the Transfer Rules table, select the transfer rule that you
                                          			 want to use with personal call transfer rules. |
| Step 4 | On the Edit Transfer Rule page, in the When This Basic Rule Is
                                          			 Active field, select Apply Personal Call Transfer Rules and select Save. |
| Step 5 | Repeat Step 2 through Step 4 for each
                                          			 additional transfer rule that you want to use. |

| Note | See the “ Calendar and Contact Integration ” section of the “Introduction to Unified Messaging” chapter of the Unified Messaging Guide for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/unified_messaging/guide/b_15cucumgx.html for detailed information on setting up external service accounts. |
|---|---|

| Step 1 | In Cisco Unity Connection Serviceability, on the Tools menu,
                                             			 select Service Management. |
|---|---|
| Step 2 | Under Optional Services, for the Connection Groupware Caching
                                             			 Service, select Stop. |
| Step 3 | After the screen refreshes, for the Connection Groupware Caching
                                             			 Service, select Start. |

| Step 1 | In Cisco Unity Connection Administration, expand System Settings > Advanced , then select Unified Messaging Services. |
|---|---|
| Step 2 | On the Unified Messaging Services Configuration page, in the
                                             			 Calendars: Normal Calendar Caching Poll Interval (In Minutes) field, enter the
                                             			 length of time that Unity Connection waits between polling cycles when it
                                             			 caches upcoming Outlook calendar data for users who are configured for a
                                             			 calendar integration. A larger number reduces the impact on the Unity Connection
                                                				server while reducing the ability of the server to handle last-minute changes
                                                				to the Outlook calendar data for users in a timely manner. A smaller number
                                                				increases the impact on the Unity Connection server while increasing the
                                                				ability of the server to handle last-minute changes to the Outlook calendar
                                                				data for users in a timely manner. |
| Step 3 | In the Calendars: Short Calendar Caching Poll Interval (In
                                             			 Minutes) field, enter the length of time that Unity Connection waits between
                                             			 polling cycles when it caches upcoming Outlook calendar data for calendar users
                                             			 who must have their calendar caches updated more frequently. |

| Step 1 | In Cisco Unity Connection Administration, expand System Settings > Advanced , then select External Services. |
|---|---|
| Step 2 | On the External Services Configuration page, in the Normal
                                             			 Calendar Caching Poll Interval field, enter the length of time in minutes that
                                             			 Unity Connection waits between polling cycles when it caches upcoming Outlook
                                             			 calendar data for users who are configured for a calendar integration. A larger number reduces the impact on the Unity Connection
                                                				server while reducing the ability of the server to handle last-minute changes
                                                				to the Outlook calendar data for users in a timely manner. A smaller number
                                                				increases the impact on the Unity Connection server while increasing the
                                                				ability of the server to handle last-minute changes to the Outlook calendar
                                                				data for users in a timely manner. |
| Step 3 | In the Short Calendar Caching Poll Interval field, enter the
                                             			 length of time (in minutes) that Unity Connection waits between polling cycles
                                             			 when it caches upcoming Outlook calendar data for calendar users who must have
                                             			 their calendar caches updated more frequently. |

| Note | The information in this section is not applicable to Cisco
                                          		  Business Edition. |
|---|---|

| Note | See the “ Phone System ” section of the “Telephony Integrations” chapter of the System Administration Guide for Cisco Unity Connection Release 15 for detailed information about AXL server settings. The guide is available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html . |
|---|---|

| Step 1 | Launch Real-Time Monitoring Tool (RTMT). Note For details on using RTMT, see the Cisco Unified Real-Time Monitoring Tool Administration Guide, available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . | Note | For details on using RTMT, see the Cisco Unified Real-Time Monitoring Tool Administration Guide, available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
|---|---|---|---|
| Note | For details on using RTMT, see the Cisco Unified Real-Time Monitoring Tool Administration Guide, available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
| Step 2 | In RTMT, on the System menu, select Performance > Open
                                             				  Performance Monitoring . |
| Step 3 | Expand the Unity Connection server. |
| Step 4 | Expand CUC Personal Call Transfer Rules . |
| Step 5 | Select the applicable counters: Applicable Rule Found—Call resulted in rule processing, and an
                                                					 applicable rule was found. Destinations Tried—Number of destinations tried while applying
                                                					 personal call transfer rules. PCTR Calls—Call is subject to personal call transfer rules
                                                					 processing: user is assigned to a class of service that has the Personal Call
                                                					 Transfer Rules feature enabled; user is associated with a Cisco Unified CM
                                                					 phone system; and user has enabled personal call transfer rules. Rules Evaluated—Number of rules evaluated during rule processing
                                                					 in a call. Subscriber Reached—Number of times a user was reached while
                                                					 applying personal call transfer rules. Transfer Failed—Number of times a transfer to a destination
                                                					 failed while applying personal call transfer rules. Voice Mail Reached—Number of times voicemail was reached while
                                                					 applying personal call transfer rules. |

| Note | For details on using RTMT, see the Cisco Unified Real-Time Monitoring Tool Administration Guide, available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
|---|---|