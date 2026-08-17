---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-user-guide-pctr-b-15cucugpctr-b-15cucugpctr-chapter-011-html-37f5de3af2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/user/guide/pctr/b_15cucugpctr/b_15cucugpctr_chapter_011.html
retrieved_at: 2026-08-17T03:35:31.904723+00:00
---

User Guide for the Cisco Unity Connection Personal Call Transfer Rules Web Tool (Release 15)

# User Guide for the Cisco Unity Connection Personal Call Transfer Rules Web Tool (Release 15)

Updated: December 18, 2023

Chapter: Managing Rule Sets and Rules

## Chapter: Managing Rule Sets and Rules

# Managing Rule Sets and Rules

## About Rule Sets and Rules

Personal call transfer rules allow you to consolidate how and where you want to receive calls. Using the Personal Call Transfer
                           Rules web tool, you can create rules to transfer and screen calls based on caller identification, time of day, and meeting
                           schedules. You can also set Cisco Unity Connection to transfer selected calls to a destination or destination group.

You can change the characteristics of your rules as frequently as you need. For example, you might create a rule that sends
                           all calls from a co-worker to your mobile phone and later change the rule to send all calls except those from the co-worker
                           to your mobile phone.

Rules can be general, such as “Send all my calls to voicemail.” Or they can be specific, such as “Send calls from Jane Smith
                           to my mobile phone if she calls between 9:00 am and 10:00 am, and screen the call.”

A rule set is a group of one or more rules that you can enable on certain days and for a range of dates, according to your
                           schedule. When the date or day specified for a rule set becomes current, Connection turns on  the rule set and begins processing
                           calls against it. Connection gives precedence to a rule set enabled for a range of dates over one enabled for day(s) of the
                           week.

Connection uses the first rule in the set that matches the condition of an incoming call and applies it. Therefore, the way
                           in which you order your rules within a set is important. In general, order rules from most specific to least specific.

To set up a rule set successfully, see Task List for Setting Up a Rule Set .

## Task List for
                        	 Setting Up a Rule Set

To set up a rule set
                           		successfully, do the following tasks in the order listed.

Set up any
                                 			 personal contacts, caller groups, personal destinations, and destination groups
                                 			 that you plan to use in your rules. See the applicable topics:

Create a rule set.
                                 			 See Creating Rule Sets .

Add rules to the
                                 			 rule set. See Adding Rules to Rule Sets .

Order the rules
                                 			 correctly. See Reordering Rules in Rule Sets .

If you want
                                 			 Connection to ring your extension before applying your transfer rules, check
                                 			 the check box on the Preferences > Rule Settings page in the Personal Call
                                 			 Transfer Rules web tool. See Changing Your Rule-Processing Preferences .

Test the rule set,
                                 			 if applicable. See Testing Rule Sets .

Change rules as
                                 			 necessary. See Changing Rules .

Enable the rule
                                 			 set. See Enabling and Disabling Rule Sets .

Configure the
                                 			 basic transfer rules to apply personal call transfer rules. See Setting Basic Transfer Rules to Apply Personal Call Transfer Rules .

## Creating Rule
                        	 Sets

Step 1

In the Personal
                                       			 Call Transfer Rules web tool, from the Rules menu, select View
                                          				Call Transfer Rule Sets .

Step 2

On the Call
                                       			 Transfer Rule Sets page, select the New Rule
                                          				Set icon below the menu bar.

Step 3

On the Rule Set
                                       			 page, enter a name for the new rule set. Choose a name that applies to the
                                       			 situation and is easy to remember. (For example, a rule set named “Workweek”
                                       			 might be active Monday through Friday, while a rule set called “Africa Trip”
                                       			 might be active during the calendar dates of that trip.)

Step 4

On the Media
                                       			 Player, select Record and record the name of the rule set.

Cisco Unity
                                          				Connection plays this name to identify the rule set when you access rule
                                          				settings by phone.

Step 5

When you finish
                                       			 recording, select Stop .

Step 6

Select Save .

## Adding Rules to Rule Sets

Once you have created a rule set, add one or more rules to it.

Caution

Any contacts, caller groups, personal destinations, or destination groups that you plan to use in your rules must be created
                                          before you add rules. If they do not exist, you will not be able to set up your rules correctly.

Step 1

In the Personal Call Transfer Rules web tool, from the Rules menu, select View Call Transfer Rule Sets .

Step 2

On the Call Transfer Rule Sets page, select the name of the rule set to which you want to add a rule.

Step 3

On the Rule Set page, in the Transfer Rules section, select Add Rule .

Step 4

On the Rule page, in the If the Call Is section, enter the applicable information that you want Connection to use when identifying
                                       calls or callers. At a minimum, you must choose a destination, destination group, or voicemail to which to transfer the incoming
                                       call. Use the following table to determine values for the fields.

Use with the Caller(s), Caller Group, Phone Number, and/or Call Source fields to set conditions for the caller identity in
                                                   the rule.

Check the From check box, and select From or Not From in the list, as applicable.

Use to add callers to a rule.

a. Check the Caller(s) check box, then select Add Callers .

b. On the Find Contacts page, select the applicable tab, depending on whether you want to search the list of users in the
                                                   Connection directory or your contacts list. You may be able to search for both users and administrator-defined  contacts in
                                                   the Connection directory. Administrator-defined contacts are indicated by an asterisk (*) next to the name in the search results
                                                   list.

c. Enter a name or partial name, and select Find .

d. Check the check box next to the caller you want to add to the rule. You can check multiple check boxes to add more than
                                                   one caller at a time.

e. Select Add Users or Add Contacts , as applicable.

f. To remove a caller from the rule, select the name, then select Delete Selected .

Use to add a caller group to a rule.

Check the Caller Group check box, and select a caller group in the list. (Note that before you can use a caller group in a rule, you need to create
                                                   the caller group.)

Use to add a phone number to a rule.

The X character matches any single digit in the range 0 through 9. For example, the pattern 9XXX matches the range of phone
                                                            numbers from 9000 through 9999.

The asterisk (*) character matches any sequence of digits. For example, the pattern 5556304* matches the phone numbers 5556304,
                                                            55563040, 55563041, 5556304100, and so forth.

Use to include or exclude callers based on whether the caller can be identified by Connection as a known number (a Connection
                                                   user, a contact, or a Connection administrator-defined contact) or as an unknown phone number (an external caller), if applicable.

Check the Call Source check box, and select Known Number or Unknown Number in the list, as applicable.

Use to set the time period during which Connection applies the rule to your incoming calls.

Check the Received Between check box, and select Received Between or Not Received Between in the list, as applicable. Choose an hourly range from the hour and minute lists.

Use to have Connection use your Microsoft Outlook calendar to determine whether you are in a meeting when it applies the rule
                                                   to an incoming call. Connection considers you to be in a meeting when your Outlook meeting time is scheduled as Busy. Any
                                                   meetings set as Tentative, Free, or Out of the Office are not considered by Connection.

This feature is not available on all systems. Ask your Connection administrator whether it is available to you.

Step 5

In the Then Transfer the Call To section, enter the applicable information that you want Connection to use when transferring
                                       calls. For a rule to be valid, you must specify either a destination, destination group, or voicemail. Use the following table
                                       to determine values for the fields.

Use to have Connection transfer calls to the destination you specify.

SMS and SMTP destinations do not appear in the Destination list. To be used in a rule, the devices must be in a destination
                                                                  group with at least one phone number.

Use to have Connection transfer calls to the destination group you specify.

Select Destination Group , then select the destination group name in the list.

Use to have Connection transfer calls directly to voicemail.

Select Voicemail .

Use to have Connection screen the incoming calls to which it applies the rule.

Check the Screen the Call check box.

This option is available only if your Connection administrator has enabled screening options for you and there are screening
                                                               options set on the Call Holding and Screening Options page in the Messaging Assistant web tool.

If an incoming call does not match any of your defined rules, the call will be transferred to your primary extension using
                                                   any call-screening options that are enabled. If you do not want these calls to be screened, create a rule by using wildcard
                                                   characters that will match all calls, order it as the last rule in the rule set, and uncheck the Screen the Call check box.

Step 6

In the Preview section, select Update Preview to display a text version of the rule so you can confirm that it is correct before you add it to the rule set.

Step 7

Select Save to add the rule to the rule set.

Step 8

Repeat Step 1 through Step 7 for any additional rules you are adding to the set.

## Changing Rules

Step 1

In the Personal Call Transfer Rules web tool, from the Rules menu, select View Call Transfer Rule Sets .

Step 2

On the Call Transfer Rule Sets page, select the name of the rule set that contains the rule you want to change.

Step 3

On the Rule Set page, in the Transfer Rules list, select the rule name.

Step 4

On the Rule page, make your changes.

Use the tables in Adding Rules to Rule Sets to determine values for the fields.

Step 5

In the Preview section, select Update Preview to display a text version of the rule so you can confirm that your changed version is correct.

Step 6

Select Save .

## Reordering Rules in Rule Sets

The order of rules in a rule set is important because Cisco Unity Connection processes the rules from the top of the list
                              to the bottom, then applies only the first rule whose conditions are met by the incoming call.

If a rule set has more than one rule, arrange the rules from most specific to least specific to ensure that Connection applies
                              the most specific rule to a call, rather than applying a more general rule to it.

Tip

To change the priority of only one rule in a set, make your change to that rule in the Transfer Rules list on the Rule Set
                                          page, and click Update Priority. All other rules in the rule set will be reprioritized accordingly.

Step 1

In the Personal Call Transfer Rules web tool, from the Rules menu, select View Call Transfer Rule Sets .

Step 2

On the Call Transfer Rule Sets page, select the name of the rule set.

Step 3

On the Rule Set page, enter a number in the Priority column to specify the order in which you want Connection to process the
                                       rules in the set. (For example, to process the “Send all my calls to voicemail” rule first, enter 1; to process the “Send
                                       calls from Jane Smith to my mobile phone” rule  second, enter 2.)

Step 4

Select Update Priority . The rules are reorganized according to their priority and saved.

## Testing Rule Sets

Use the Call Transfer Rule Tester tool to see how Cisco Unity Connection would transfer an incoming call based on the rule(s)
                              in a set. You might choose to test a rule set after building it to see if the rule applies to a specific caller or to an incoming
                              call that reaches you at a specific time of day.

The Call Transfer Rule Tester tool is also a good way to diagnose a call-forwarding problem. For example, if a call was not
                              forwarded in a way that you expected, enter the name of the actual caller and the time of day and date when the call was placed,
                              and the Rule Tester can help you figure out the part of the rule set that Connection would apply to the incoming call.

To get results with the Call Transfer Rule Tester, the rule set that contains the rule you are testing must be enabled or
                              active.

Contact your Connection administrator if you are unable to diagnose call-forwarding problems with the Call Transfer Rule Tester
                                          tool.

Step 1

In the Personal Call Transfer Rules web tool, from the Tools menu, select Call Transfer Rule Tester .

Step 2

On the Call Transfer Rule Tester page, enter or choose the incoming-call conditions that you want to use for the test:

Name or phone number of the caller. If you are testing for a known user (a user in the Connection directory or a contact),
                                                select Select Caller to add the user to the Rule Tester.

Time of day.

Calendar date.

Year.

Whether or not you are in a meeting.

To get accurate results with the Rule Tester tool, specify a date. If you do not specify a date, the rule is evaluated with
                                          the current date, which is the default.

You can combine the conditions in any way to test your rules. For example, you can specify the caller, time, date, and year.
                                          Or you can specify only the time of day and date.

Step 3

Select Test .

If an enabled or active rule applies to the call conditions that you specified, Connection displays the rule.

If no enabled or active rule applies to the call conditions that you specified, Connection displays a message explaining that
                                          no matching rules were found.

Tip

When using the Call Transfer Rule Tester to diagnose why a call was not forwarded in a particular way, start by defining broad
                                                      call conditions. For example, provide a name and date. If the rule applies to the broad conditions, begin to narrow the conditions
                                                      to single out the reason why your rule did not apply to the incoming phone call.

## Deleting Rule Sets

Step 1

In the Personal Call Transfer Rules web tool, from the Rules menu, select View Call Transfer Rule Sets .

Step 2

On the Call Transfer Rule Sets page, check the check box next to the rule set you want to delete.

Step 3

Select the Delete Selected Rows icon below the menu bar.

If the rule set is active, you will receive an error message that the rule set cannot be deleted.

Step 4

Select OK to delete the rule set.

## Enabling and Disabling Rule Sets

Enabling a rule set means to set the days or date range that it will be active. Cisco Unity Connection uses the schedule to
                              apply rules to your incoming phone calls. You can schedule the active period in advance in the Personal Call Transfer Rules
                              web tool.

Disabling a rule set means making it ineligible to be active.

Connection allows more than one rule set to be enabled within the same time period. When more than one rule set is enabled,
                              a set enabled within a range of dates takes precedence over a set enabled by days of the week. When the range of dates is
                              no longer applicable, the set enabled by days of the week is restored. Multiple rule sets cannot be enabled on overlapping
                              dates.

Step 1

In the Personal Call Transfer Rules web tool, from the Rules menu, select Enable Rule Sets .

Step 2

To enable a rule set for a range of dates:

On the Enable Rule Sets page, in the Date Range section, select the rule set in the Rule Set column list that you want to
                                             enable. The check box in the Enabled column is checked automatically.

Set the applicable dates in the Start Date and End Date column lists.

To add another row, select Add Date Range , then repeat Step a and Step b to specify the date range for any additional rule sets.

You can schedule several date ranges in advance. For example:

Vacation rule set, enabled March 1 to March 8

Work Travel rule set, enabled March 9 to March 11

Workweek rule set, enabled March 12 to March 31

Only the rule set enabled during the date range that includes the current date is active.

Select Save .

Step 3

To enable a rule set for days of the week:

On the Enable Rule Sets page, in the Days of Week section, select the rule set in the Rule Set column list that you want to
                                             enable for the applicable days of the week. The check box in the Enabled column is checked automatically.

You can specify a rule set for one or more days of the week (for example, every Tuesday, every weekday, or every weekend),
                                                or you can choose Daily to apply the rule set to every day of the week.

Select Save .

Step 4

To disable a rule set:

On the Enable Rule Sets page, uncheck the check box in the Enabled column.

Alternatively, you can select None in the Rule Set column list.

Select Save .

## Setting Basic Transfer Rules to Apply Personal Call Transfer Rules

Personal call transfer rules are used only if the active basic rule—the standard, alternate or closed transfer rule—is set
                              to apply personal call transfer rules instead of the basic settings. Once you have created and enabled personal call transfer
                              rule sets, you must set the basic transfer rules to apply personal call transfer rules.

You use the Messaging Assistant web tool to do the following procedure (not the Personal Call Transfer Rules web tool).

Step 1

In the Messaging Assistant web tool, from the Preferences menu, select Transfer and Screening .

Step 2

In the Transfer Rule table, choose the basic transfer rule that you want to set to use personal call transfer rules.

Step 3

In the When This Basic Rule Is Active field, select Apply Personal Call Transfer Rules .

Step 4

Select Save .

Step 5

Repeat Step 1 through Step 4 for each additional basic transfer rule that you want to set to use personal call transfer rules.

| Step 1 | In the Personal
                                       			 Call Transfer Rules web tool, from the Rules menu, select View
                                          				Call Transfer Rule Sets . |
|---|---|
| Step 2 | On the Call
                                       			 Transfer Rule Sets page, select the New Rule
                                          				Set icon below the menu bar. |
| Step 3 | On the Rule Set
                                       			 page, enter a name for the new rule set. Choose a name that applies to the
                                       			 situation and is easy to remember. (For example, a rule set named “Workweek”
                                       			 might be active Monday through Friday, while a rule set called “Africa Trip”
                                       			 might be active during the calendar dates of that trip.) |
| Step 4 | On the Media
                                       			 Player, select Record and record the name of the rule set. Cisco Unity
                                          				Connection plays this name to identify the rule set when you access rule
                                          				settings by phone. |
| Step 5 | When you finish
                                       			 recording, select Stop . |
| Step 6 | Select Save . |

| Caution | Any contacts, caller groups, personal destinations, or destination groups that you plan to use in your rules must be created
                                          before you add rules. If they do not exist, you will not be able to set up your rules correctly. |
|---|---|

| Step 1 | In the Personal Call Transfer Rules web tool, from the Rules menu, select View Call Transfer Rule Sets . |
|---|---|
| Step 2 | On the Call Transfer Rule Sets page, select the name of the rule set to which you want to add a rule. |
| Step 3 | On the Rule Set page, in the Transfer Rules section, select Add Rule . |
| Step 4 | On the Rule page, in the If the Call Is section, enter the applicable information that you want Connection to use when identifying
                                       calls or callers. At a minimum, you must choose a destination, destination group, or voicemail to which to transfer the incoming
                                       call. Use the following table to determine values for the fields. Field Considerations From Use with the Caller(s), Caller Group, Phone Number, and/or Call Source fields to set conditions for the caller identity in
                                                   the rule. Check the From check box, and select From or Not From in the list, as applicable. Caller(s) Use to add callers to a rule. a. Check the Caller(s) check box, then select Add Callers . b. On the Find Contacts page, select the applicable tab, depending on whether you want to search the list of users in the
                                                   Connection directory or your contacts list. You may be able to search for both users and administrator-defined  contacts in
                                                   the Connection directory. Administrator-defined contacts are indicated by an asterisk (*) next to the name in the search results
                                                   list. c. Enter a name or partial name, and select Find . d. Check the check box next to the caller you want to add to the rule. You can check multiple check boxes to add more than
                                                   one caller at a time. e. Select Add Users or Add Contacts , as applicable. f. To remove a caller from the rule, select the name, then select Delete Selected . Caller Group Use to add a caller group to a rule. Check the Caller Group check box, and select a caller group in the list. (Note that before you can use a caller group in a rule, you need to create
                                                   the caller group.) Phone Number Use to add a phone number to a rule. Check the Phone Number check box, and enter the number that Connection will associate with the incoming call. Connection processes the rule only
                                                   if the phone number of an incoming call matches exactly what you enter in the field. You can use the wildcard characters X
                                                   and * to match more than one phone number: The X character matches any single digit in the range 0 through 9. For example, the pattern 9XXX matches the range of phone
                                                            numbers from 9000 through 9999. The asterisk (*) character matches any sequence of digits. For example, the pattern 5556304* matches the phone numbers 5556304,
                                                            55563040, 55563041, 5556304100, and so forth. Call Source Use to include or exclude callers based on whether the caller can be identified by Connection as a known number (a Connection
                                                   user, a contact, or a Connection administrator-defined contact) or as an unknown phone number (an external caller), if applicable. Check the Call Source check box, and select Known Number or Unknown Number in the list, as applicable. Received Between Use to set the time period during which Connection applies the rule to your incoming calls. Check the Received Between check box, and select Received Between or Not Received Between in the list, as applicable. Choose an hourly range from the hour and minute lists. I Am in a Meeting Use to have Connection use your Microsoft Outlook calendar to determine whether you are in a meeting when it applies the rule
                                                   to an incoming call. Connection considers you to be in a meeting when your Outlook meeting time is scheduled as Busy. Any
                                                   meetings set as Tentative, Free, or Out of the Office are not considered by Connection. Check the I Am in a Meeting check box, and select I Am In a Meeting or I Am Not in a Meeting in the list, as applicable. Note This feature is not available on all systems. Ask your Connection administrator whether it is available to you. | Field | Considerations | From | Use with the Caller(s), Caller Group, Phone Number, and/or Call Source fields to set conditions for the caller identity in
                                                   the rule. Check the From check box, and select From or Not From in the list, as applicable. | Caller(s) | Use to add callers to a rule. a. Check the Caller(s) check box, then select Add Callers . b. On the Find Contacts page, select the applicable tab, depending on whether you want to search the list of users in the
                                                   Connection directory or your contacts list. You may be able to search for both users and administrator-defined  contacts in
                                                   the Connection directory. Administrator-defined contacts are indicated by an asterisk (*) next to the name in the search results
                                                   list. c. Enter a name or partial name, and select Find . d. Check the check box next to the caller you want to add to the rule. You can check multiple check boxes to add more than
                                                   one caller at a time. e. Select Add Users or Add Contacts , as applicable. f. To remove a caller from the rule, select the name, then select Delete Selected . | Caller Group | Use to add a caller group to a rule. Check the Caller Group check box, and select a caller group in the list. (Note that before you can use a caller group in a rule, you need to create
                                                   the caller group.) | Phone Number | Use to add a phone number to a rule. Check the Phone Number check box, and enter the number that Connection will associate with the incoming call. Connection processes the rule only
                                                   if the phone number of an incoming call matches exactly what you enter in the field. You can use the wildcard characters X
                                                   and * to match more than one phone number: The X character matches any single digit in the range 0 through 9. For example, the pattern 9XXX matches the range of phone
                                                            numbers from 9000 through 9999. The asterisk (*) character matches any sequence of digits. For example, the pattern 5556304* matches the phone numbers 5556304,
                                                            55563040, 55563041, 5556304100, and so forth. | Call Source | Use to include or exclude callers based on whether the caller can be identified by Connection as a known number (a Connection
                                                   user, a contact, or a Connection administrator-defined contact) or as an unknown phone number (an external caller), if applicable. Check the Call Source check box, and select Known Number or Unknown Number in the list, as applicable. | Received Between | Use to set the time period during which Connection applies the rule to your incoming calls. Check the Received Between check box, and select Received Between or Not Received Between in the list, as applicable. Choose an hourly range from the hour and minute lists. | I Am in a Meeting | Use to have Connection use your Microsoft Outlook calendar to determine whether you are in a meeting when it applies the rule
                                                   to an incoming call. Connection considers you to be in a meeting when your Outlook meeting time is scheduled as Busy. Any
                                                   meetings set as Tentative, Free, or Out of the Office are not considered by Connection. Check the I Am in a Meeting check box, and select I Am In a Meeting or I Am Not in a Meeting in the list, as applicable. Note This feature is not available on all systems. Ask your Connection administrator whether it is available to you. | Note | This feature is not available on all systems. Ask your Connection administrator whether it is available to you. |
| Field | Considerations |
| From | Use with the Caller(s), Caller Group, Phone Number, and/or Call Source fields to set conditions for the caller identity in
                                                   the rule. Check the From check box, and select From or Not From in the list, as applicable. |
| Caller(s) | Use to add callers to a rule. a. Check the Caller(s) check box, then select Add Callers . b. On the Find Contacts page, select the applicable tab, depending on whether you want to search the list of users in the
                                                   Connection directory or your contacts list. You may be able to search for both users and administrator-defined  contacts in
                                                   the Connection directory. Administrator-defined contacts are indicated by an asterisk (*) next to the name in the search results
                                                   list. c. Enter a name or partial name, and select Find . d. Check the check box next to the caller you want to add to the rule. You can check multiple check boxes to add more than
                                                   one caller at a time. e. Select Add Users or Add Contacts , as applicable. f. To remove a caller from the rule, select the name, then select Delete Selected . |
| Caller Group | Use to add a caller group to a rule. Check the Caller Group check box, and select a caller group in the list. (Note that before you can use a caller group in a rule, you need to create
                                                   the caller group.) |
| Phone Number | Use to add a phone number to a rule. Check the Phone Number check box, and enter the number that Connection will associate with the incoming call. Connection processes the rule only
                                                   if the phone number of an incoming call matches exactly what you enter in the field. You can use the wildcard characters X
                                                   and * to match more than one phone number: The X character matches any single digit in the range 0 through 9. For example, the pattern 9XXX matches the range of phone
                                                            numbers from 9000 through 9999. The asterisk (*) character matches any sequence of digits. For example, the pattern 5556304* matches the phone numbers 5556304,
                                                            55563040, 55563041, 5556304100, and so forth. |
| Call Source | Use to include or exclude callers based on whether the caller can be identified by Connection as a known number (a Connection
                                                   user, a contact, or a Connection administrator-defined contact) or as an unknown phone number (an external caller), if applicable. Check the Call Source check box, and select Known Number or Unknown Number in the list, as applicable. |
| Received Between | Use to set the time period during which Connection applies the rule to your incoming calls. Check the Received Between check box, and select Received Between or Not Received Between in the list, as applicable. Choose an hourly range from the hour and minute lists. |
| I Am in a Meeting | Use to have Connection use your Microsoft Outlook calendar to determine whether you are in a meeting when it applies the rule
                                                   to an incoming call. Connection considers you to be in a meeting when your Outlook meeting time is scheduled as Busy. Any
                                                   meetings set as Tentative, Free, or Out of the Office are not considered by Connection. Check the I Am in a Meeting check box, and select I Am In a Meeting or I Am Not in a Meeting in the list, as applicable. Note This feature is not available on all systems. Ask your Connection administrator whether it is available to you. | Note | This feature is not available on all systems. Ask your Connection administrator whether it is available to you. |
| Note | This feature is not available on all systems. Ask your Connection administrator whether it is available to you. |
| Step 5 | In the Then Transfer the Call To section, enter the applicable information that you want Connection to use when transferring
                                       calls. For a rule to be valid, you must specify either a destination, destination group, or voicemail. Use the following table
                                       to determine values for the fields. Field Considerations Destination Use to have Connection transfer calls to the destination you specify. Select Destination , then select the destination name in the list. Note SMS and SMTP destinations do not appear in the Destination list. To be used in a rule, the devices must be in a destination
                                                                  group with at least one phone number. Destination Group Use to have Connection transfer calls to the destination group you specify. Select Destination Group , then select the destination group name in the list. Voicemail Use to have Connection transfer calls directly to voicemail. Select Voicemail . Screen the Call Use to have Connection screen the incoming calls to which it applies the rule. Check the Screen the Call check box. Note This option is available only if your Connection administrator has enabled screening options for you and there are screening
                                                               options set on the Call Holding and Screening Options page in the Messaging Assistant web tool. If an incoming call does not match any of your defined rules, the call will be transferred to your primary extension using
                                                   any call-screening options that are enabled. If you do not want these calls to be screened, create a rule by using wildcard
                                                   characters that will match all calls, order it as the last rule in the rule set, and uncheck the Screen the Call check box. | Field | Considerations | Destination | Use to have Connection transfer calls to the destination you specify. Select Destination , then select the destination name in the list. Note SMS and SMTP destinations do not appear in the Destination list. To be used in a rule, the devices must be in a destination
                                                                  group with at least one phone number. | Note | SMS and SMTP destinations do not appear in the Destination list. To be used in a rule, the devices must be in a destination
                                                                  group with at least one phone number. | Destination Group | Use to have Connection transfer calls to the destination group you specify. Select Destination Group , then select the destination group name in the list. | Voicemail | Use to have Connection transfer calls directly to voicemail. Select Voicemail . | Screen the Call | Use to have Connection screen the incoming calls to which it applies the rule. Check the Screen the Call check box. Note This option is available only if your Connection administrator has enabled screening options for you and there are screening
                                                               options set on the Call Holding and Screening Options page in the Messaging Assistant web tool. If an incoming call does not match any of your defined rules, the call will be transferred to your primary extension using
                                                   any call-screening options that are enabled. If you do not want these calls to be screened, create a rule by using wildcard
                                                   characters that will match all calls, order it as the last rule in the rule set, and uncheck the Screen the Call check box. | Note | This option is available only if your Connection administrator has enabled screening options for you and there are screening
                                                               options set on the Call Holding and Screening Options page in the Messaging Assistant web tool. |
| Field | Considerations |
| Destination | Use to have Connection transfer calls to the destination you specify. Select Destination , then select the destination name in the list. Note SMS and SMTP destinations do not appear in the Destination list. To be used in a rule, the devices must be in a destination
                                                                  group with at least one phone number. | Note | SMS and SMTP destinations do not appear in the Destination list. To be used in a rule, the devices must be in a destination
                                                                  group with at least one phone number. |
| Note | SMS and SMTP destinations do not appear in the Destination list. To be used in a rule, the devices must be in a destination
                                                                  group with at least one phone number. |
| Destination Group | Use to have Connection transfer calls to the destination group you specify. Select Destination Group , then select the destination group name in the list. |
| Voicemail | Use to have Connection transfer calls directly to voicemail. Select Voicemail . |
| Screen the Call | Use to have Connection screen the incoming calls to which it applies the rule. Check the Screen the Call check box. Note This option is available only if your Connection administrator has enabled screening options for you and there are screening
                                                               options set on the Call Holding and Screening Options page in the Messaging Assistant web tool. If an incoming call does not match any of your defined rules, the call will be transferred to your primary extension using
                                                   any call-screening options that are enabled. If you do not want these calls to be screened, create a rule by using wildcard
                                                   characters that will match all calls, order it as the last rule in the rule set, and uncheck the Screen the Call check box. | Note | This option is available only if your Connection administrator has enabled screening options for you and there are screening
                                                               options set on the Call Holding and Screening Options page in the Messaging Assistant web tool. |
| Note | This option is available only if your Connection administrator has enabled screening options for you and there are screening
                                                               options set on the Call Holding and Screening Options page in the Messaging Assistant web tool. |
| Step 6 | In the Preview section, select Update Preview to display a text version of the rule so you can confirm that it is correct before you add it to the rule set. |
| Step 7 | Select Save to add the rule to the rule set. |
| Step 8 | Repeat Step 1 through Step 7 for any additional rules you are adding to the set. |

| Field | Considerations |
|---|---|
| From | Use with the Caller(s), Caller Group, Phone Number, and/or Call Source fields to set conditions for the caller identity in
                                                   the rule. Check the From check box, and select From or Not From in the list, as applicable. |
| Caller(s) | Use to add callers to a rule. a. Check the Caller(s) check box, then select Add Callers . b. On the Find Contacts page, select the applicable tab, depending on whether you want to search the list of users in the
                                                   Connection directory or your contacts list. You may be able to search for both users and administrator-defined  contacts in
                                                   the Connection directory. Administrator-defined contacts are indicated by an asterisk (*) next to the name in the search results
                                                   list. c. Enter a name or partial name, and select Find . d. Check the check box next to the caller you want to add to the rule. You can check multiple check boxes to add more than
                                                   one caller at a time. e. Select Add Users or Add Contacts , as applicable. f. To remove a caller from the rule, select the name, then select Delete Selected . |
| Caller Group | Use to add a caller group to a rule. Check the Caller Group check box, and select a caller group in the list. (Note that before you can use a caller group in a rule, you need to create
                                                   the caller group.) |
| Phone Number | Use to add a phone number to a rule. Check the Phone Number check box, and enter the number that Connection will associate with the incoming call. Connection processes the rule only
                                                   if the phone number of an incoming call matches exactly what you enter in the field. You can use the wildcard characters X
                                                   and * to match more than one phone number: The X character matches any single digit in the range 0 through 9. For example, the pattern 9XXX matches the range of phone
                                                            numbers from 9000 through 9999. The asterisk (*) character matches any sequence of digits. For example, the pattern 5556304* matches the phone numbers 5556304,
                                                            55563040, 55563041, 5556304100, and so forth. |
| Call Source | Use to include or exclude callers based on whether the caller can be identified by Connection as a known number (a Connection
                                                   user, a contact, or a Connection administrator-defined contact) or as an unknown phone number (an external caller), if applicable. Check the Call Source check box, and select Known Number or Unknown Number in the list, as applicable. |
| Received Between | Use to set the time period during which Connection applies the rule to your incoming calls. Check the Received Between check box, and select Received Between or Not Received Between in the list, as applicable. Choose an hourly range from the hour and minute lists. |
| I Am in a Meeting | Use to have Connection use your Microsoft Outlook calendar to determine whether you are in a meeting when it applies the rule
                                                   to an incoming call. Connection considers you to be in a meeting when your Outlook meeting time is scheduled as Busy. Any
                                                   meetings set as Tentative, Free, or Out of the Office are not considered by Connection. Check the I Am in a Meeting check box, and select I Am In a Meeting or I Am Not in a Meeting in the list, as applicable. Note This feature is not available on all systems. Ask your Connection administrator whether it is available to you. | Note | This feature is not available on all systems. Ask your Connection administrator whether it is available to you. |
| Note | This feature is not available on all systems. Ask your Connection administrator whether it is available to you. |

| Note | This feature is not available on all systems. Ask your Connection administrator whether it is available to you. |
|---|---|

| Field | Considerations |
|---|---|
| Destination | Use to have Connection transfer calls to the destination you specify. Select Destination , then select the destination name in the list. Note SMS and SMTP destinations do not appear in the Destination list. To be used in a rule, the devices must be in a destination
                                                                  group with at least one phone number. | Note | SMS and SMTP destinations do not appear in the Destination list. To be used in a rule, the devices must be in a destination
                                                                  group with at least one phone number. |
| Note | SMS and SMTP destinations do not appear in the Destination list. To be used in a rule, the devices must be in a destination
                                                                  group with at least one phone number. |
| Destination Group | Use to have Connection transfer calls to the destination group you specify. Select Destination Group , then select the destination group name in the list. |
| Voicemail | Use to have Connection transfer calls directly to voicemail. Select Voicemail . |
| Screen the Call | Use to have Connection screen the incoming calls to which it applies the rule. Check the Screen the Call check box. Note This option is available only if your Connection administrator has enabled screening options for you and there are screening
                                                               options set on the Call Holding and Screening Options page in the Messaging Assistant web tool. If an incoming call does not match any of your defined rules, the call will be transferred to your primary extension using
                                                   any call-screening options that are enabled. If you do not want these calls to be screened, create a rule by using wildcard
                                                   characters that will match all calls, order it as the last rule in the rule set, and uncheck the Screen the Call check box. | Note | This option is available only if your Connection administrator has enabled screening options for you and there are screening
                                                               options set on the Call Holding and Screening Options page in the Messaging Assistant web tool. |
| Note | This option is available only if your Connection administrator has enabled screening options for you and there are screening
                                                               options set on the Call Holding and Screening Options page in the Messaging Assistant web tool. |

| Note | SMS and SMTP destinations do not appear in the Destination list. To be used in a rule, the devices must be in a destination
                                                                  group with at least one phone number. |
|---|---|

| Note | This option is available only if your Connection administrator has enabled screening options for you and there are screening
                                                               options set on the Call Holding and Screening Options page in the Messaging Assistant web tool. |
|---|---|

| Step 1 | In the Personal Call Transfer Rules web tool, from the Rules menu, select View Call Transfer Rule Sets . |
|---|---|
| Step 2 | On the Call Transfer Rule Sets page, select the name of the rule set that contains the rule you want to change. |
| Step 3 | On the Rule Set page, in the Transfer Rules list, select the rule name. |
| Step 4 | On the Rule page, make your changes. Use the tables in Adding Rules to Rule Sets to determine values for the fields. |
| Step 5 | In the Preview section, select Update Preview to display a text version of the rule so you can confirm that your changed version is correct. |
| Step 6 | Select Save . |

| Tip | To change the priority of only one rule in a set, make your change to that rule in the Transfer Rules list on the Rule Set
                                          page, and click Update Priority. All other rules in the rule set will be reprioritized accordingly. |
|---|---|

| Step 1 | In the Personal Call Transfer Rules web tool, from the Rules menu, select View Call Transfer Rule Sets . |
|---|---|
| Step 2 | On the Call Transfer Rule Sets page, select the name of the rule set. |
| Step 3 | On the Rule Set page, enter a number in the Priority column to specify the order in which you want Connection to process the
                                       rules in the set. (For example, to process the “Send all my calls to voicemail” rule first, enter 1; to process the “Send
                                       calls from Jane Smith to my mobile phone” rule  second, enter 2.) |
| Step 4 | Select Update Priority . The rules are reorganized according to their priority and saved. |

| Note | Contact your Connection administrator if you are unable to diagnose call-forwarding problems with the Call Transfer Rule Tester
                                          tool. |
|---|---|

| Step 1 | In the Personal Call Transfer Rules web tool, from the Tools menu, select Call Transfer Rule Tester . |
|---|---|
| Step 2 | On the Call Transfer Rule Tester page, enter or choose the incoming-call conditions that you want to use for the test: Name or phone number of the caller. If you are testing for a known user (a user in the Connection directory or a contact),
                                                select Select Caller to add the user to the Rule Tester. Time of day. Calendar date. Year. Whether or not you are in a meeting. To get accurate results with the Rule Tester tool, specify a date. If you do not specify a date, the rule is evaluated with
                                          the current date, which is the default. You can combine the conditions in any way to test your rules. For example, you can specify the caller, time, date, and year.
                                          Or you can specify only the time of day and date. |
| Step 3 | Select Test . If an enabled or active rule applies to the call conditions that you specified, Connection displays the rule. If no enabled or active rule applies to the call conditions that you specified, Connection displays a message explaining that
                                          no matching rules were found. Tip When using the Call Transfer Rule Tester to diagnose why a call was not forwarded in a particular way, start by defining broad
                                                      call conditions. For example, provide a name and date. If the rule applies to the broad conditions, begin to narrow the conditions
                                                      to single out the reason why your rule did not apply to the incoming phone call. | Tip | When using the Call Transfer Rule Tester to diagnose why a call was not forwarded in a particular way, start by defining broad
                                                      call conditions. For example, provide a name and date. If the rule applies to the broad conditions, begin to narrow the conditions
                                                      to single out the reason why your rule did not apply to the incoming phone call. |
| Tip | When using the Call Transfer Rule Tester to diagnose why a call was not forwarded in a particular way, start by defining broad
                                                      call conditions. For example, provide a name and date. If the rule applies to the broad conditions, begin to narrow the conditions
                                                      to single out the reason why your rule did not apply to the incoming phone call. |

| Tip | When using the Call Transfer Rule Tester to diagnose why a call was not forwarded in a particular way, start by defining broad
                                                      call conditions. For example, provide a name and date. If the rule applies to the broad conditions, begin to narrow the conditions
                                                      to single out the reason why your rule did not apply to the incoming phone call. |
|---|---|

| Step 1 | In the Personal Call Transfer Rules web tool, from the Rules menu, select View Call Transfer Rule Sets . |
|---|---|
| Step 2 | On the Call Transfer Rule Sets page, check the check box next to the rule set you want to delete. |
| Step 3 | Select the Delete Selected Rows icon below the menu bar. If the rule set is active, you will receive an error message that the rule set cannot be deleted. |
| Step 4 | Select OK to delete the rule set. |

| Step 1 | In the Personal Call Transfer Rules web tool, from the Rules menu, select Enable Rule Sets . |
|---|---|
| Step 2 | To enable a rule set for a range of dates: On the Enable Rule Sets page, in the Date Range section, select the rule set in the Rule Set column list that you want to
                                             enable. The check box in the Enabled column is checked automatically. Set the applicable dates in the Start Date and End Date column lists. To add another row, select Add Date Range , then repeat Step a and Step b to specify the date range for any additional rule sets. You can schedule several date ranges in advance. For example: Vacation rule set, enabled March 1 to March 8 Work Travel rule set, enabled March 9 to March 11 Workweek rule set, enabled March 12 to March 31 Only the rule set enabled during the date range that includes the current date is active. Select Save . |
| Step 3 | To enable a rule set for days of the week: On the Enable Rule Sets page, in the Days of Week section, select the rule set in the Rule Set column list that you want to
                                             enable for the applicable days of the week. The check box in the Enabled column is checked automatically. You can specify a rule set for one or more days of the week (for example, every Tuesday, every weekday, or every weekend),
                                                or you can choose Daily to apply the rule set to every day of the week. Select Save . |
| Step 4 | To disable a rule set: On the Enable Rule Sets page, uncheck the check box in the Enabled column. Alternatively, you can select None in the Rule Set column list. Select Save . |

| Note | You use the Messaging Assistant web tool to do the following procedure (not the Personal Call Transfer Rules web tool). |
|---|---|

| Step 1 | In the Messaging Assistant web tool, from the Preferences menu, select Transfer and Screening . |
|---|---|
| Step 2 | In the Transfer Rule table, choose the basic transfer rule that you want to set to use personal call transfer rules. |
| Step 3 | In the When This Basic Rule Is Active field, select Apply Personal Call Transfer Rules . |
| Step 4 | Select Save . |
| Step 5 | Repeat Step 1 through Step 4 for each additional basic transfer rule that you want to set to use personal call transfer rules. |