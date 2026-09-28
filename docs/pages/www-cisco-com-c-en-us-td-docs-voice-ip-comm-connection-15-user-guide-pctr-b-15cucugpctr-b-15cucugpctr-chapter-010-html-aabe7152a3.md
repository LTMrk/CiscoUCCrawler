---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-user-guide-pctr-b-15cucugpctr-b-15cucugpctr-chapter-010-html-aabe7152a3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/user/guide/pctr/b_15cucugpctr/b_15cucugpctr_chapter_010.html
retrieved_at: 2026-08-17T03:35:27.503282+00:00
---

User Guide for the Cisco Unity Connection Personal Call Transfer Rules Web Tool (Release 15)

# User Guide for the Cisco Unity Connection Personal Call Transfer Rules Web Tool (Release 15)

Updated: December 18, 2023

Chapter: Managing Destinations and Destination Groups

## Chapter: Managing Destinations and Destination Groups

# Managing Destinations and Destination Groups

## About
                        	 Destinations

Destinations are phone
                           		numbers or email addresses to which Cisco Unity Connection can transfer your
                           		incoming calls or send text messages as a part of personal call transfer rules.
                           		There are three types of destinations:

Phone
                                       				destinations are phone numbers to which Connection can transfer incoming calls.

Phone numbers
                                       				associated with you in the Connection directory can be used as phone
                                       				destinations. These might include your primary extension, voicemail access
                                       				number, and company mobile phone number. Phone numbers in the directory are
                                       				maintained by your Connection administrator.

You can also
                                       				create personal phone destinations, such as your personal mobile phone number,
                                       				your home phone number (if it is not listed in the Connection directory), and
                                       				phone numbers at which you can be reached during a business trip. You manage
                                       				these destinations in the Personal Call Transfer Rules web tool.

SMS destinations
                                       				are phone numbers for SMS devices to which Connection can send a text message.
                                       				The message uses the standard format “You have a call from <number or
                                       				extension> at <time> on <date>.” (For example, “You have a call
                                       				from 3233 at 15:16 on 04 October 2010.”)

Note that for an
                                       				SMS destination to be used in a rule, it must be added to a destination group
                                       				that contains at least one phone destination. (SMS destinations do not appear
                                       				in the Destination list on the Rule page when you are creating a rule.)

SMS devices may
                                       				be added for you by your Connection administrator, and you may be able to
                                       				modify them in the Messaging Assistant web tool. SMS devices do not need to be
                                       				enabled in the Messaging Assistant to be available as a destination in the
                                       				Personal Call Transfer Rules web tool.

SMTP
                                       				destinations are email addresses to which Connection can send a text message.
                                       				The message uses the standard format “You have a call from <number or
                                       				extension> at <time> on <date>.” (For example, “You have a call
                                       				from 3233 at 15:16 on 04 October 2010.”)

Note that for an
                                       				SMTP destination to be used in a rule, it must be added to a destination group
                                       				that contains at least one phone destination. (SMTP destinations do not appear
                                       				in the Destination list on the Rule page when you are creating a rule.)

SMTP devices may
                                       				be created for you by your Connection administrator, and you may be able to
                                       				modify them in the Messaging Assistant web tool. SMTP devices do not need to be
                                       				enabled in the Messaging Assistant to be available as a destination in the
                                       				Personal Call Transfer Rules web tool.

## Creating Personal Destinations

Step 1

In the Personal Call Transfer Rules web tool, from the Destinations menu, select View Destinations .

Step 2

On the Destinations page, select the New Destination icon below the menu bar.

Step 3

On the Create Destination page, in the Name field, enter a name for the destination.

Step 4

In the Phone Number field, enter a phone number for the destination.

Use digits 0 through 9. Do not use spaces or parentheses between digits. For long-distance numbers, also include 1 and the
                                          area code.

You may not be able to enter certain phone numbers, or your phone system may require additional characters (for example, you
                                          may be required to enter an access code to dial outgoing numbers). If you are experiencing difficulties with this setting,
                                          contact your Connection administrator.

Step 5

In the Rings to Wait field, enter the number of rings you want Connection to wait before transferring the call to voicemail
                                       or to the next destination in a destination group, depending on your other call transfer settings. The default value is four
                                       rings.

Step 6

If you have set this destination to forward calls to Connection, check the Loop Detection Enabled check box.

If you create a rule that transfers calls from Connection to a phone destination, you may inadvertently create a call-looping
                                          situation in which Connection forwards calls to your phone, and your phone consequently forwards the call back to Connection,
                                          and callers may never be able to reach you. Selecting this setting when you configure this type of destination to forward
                                          calls to Connection can help eliminate call-looping problems.

Step 7

Select Save .

## Changing Personal Destinations

Step 1

In the Personal Call Transfer Rules web tool, from the Destinations menu, select View Destinations .

Step 2

On the Destinations page, select the name of the personal destination.

Step 3

On the Change Destination page, make the applicable changes and select Save .

## Deleting Personal Destinations

You cannot delete a personal destination while it is being used in a destination group or in a rule. Delete the destination
                              from the destination group or rule first, then delete the destination.

Step 1

In the Personal Call Transfer Rules web tool, from the Destinations menu, select View Destinations .

Step 2

On the Destinations page, check the check box for the personal destination you want to delete. You can check multiple check
                                       boxes to delete more than one personal destination at a time.

Step 3

Select the Delete Selected Rows icon below the menu bar.

## Changing the Rings-to-Wait Setting for Phone Destinations

For phone destinations, you can change the Rings-to-Wait setting on the Destinations page.

Step 1

In the Personal Call Transfer Rules web tool, from the Destinations menu, select View Destinations .

Step 2

On the Destinations page, in the Rings to Wait column, enter the new value for the number of rings you want Connection to
                                       wait before transferring the call to voicemail or to the next destination in a destination group.

Step 3

Select Update .

## Changing the Loop-Detection Setting for Destinations

For phone destinations other than your primary extension, you can use the Loop Detection Enabled setting to indicate when
                              you have configured a phone to forward calls to Cisco Unity Connection. For example, you may configure your mobile phone to
                              forward all calls to Connection to store all your voice messages in Connection. If you then create a rule that transfers calls
                              from Connection to your mobile phone, you may inadvertently create a call-looping situation in which Connection forwards calls
                              to your mobile phone, and your mobile phone consequently forwards calls back to Connection, and callers may never be able
                              to reach you.

Selecting this setting can help to eliminate the call-looping problem. If calls seem to be transferring from the phone destination
                              to Connection and then back to the phone, Connection will either transfer the call to the next assigned device (if you have
                              created a destination group) or transfer the call to voicemail if there are no additional destinations defined.

When this setting is enabled, you can expect to hear a slight delay as Connection transfers the call to the next destination
                                          in the destination group, or to voicemail.

Step 1

In the Personal Call Transfer Rules web tool, from the Destinations menu, select View Destinations .

Step 2

If you have set this destination to forward calls to Cisco Unity Connection, check the Loop Detection Enabled check box.

Step 3

Select Update .

## About Destination Groups

Destination groups contain multiple destinations arranged in a sequence and stored under a single group name.

For example, to ensure that you receive calls from a specific contact, you might create a destination group with your primary
                           extension, mobile, and home phone numbers, then create a rule that tells Cisco Unity Connection to transfer calls from the
                           contact to the destination group. To be used in a rule, a destination group must contain at least one phone destination.

When a call is transferred to a destination group, Connection tries the destinations in the order listed until a phone is
                           answered, until the caller leaves a voice message or hangs up, or until the last destination in the group is reached. If the
                           group contains an SMS or SMTP destination, Connection sends the device a text message about the call.

If a destination is not answered, Connection prompts the caller to press 1 to continue waiting while it tries the next destination
                           or to press 2 to leave a voice message. Connection waits for a phone to be answered based on the specified number of rings,
                           which is set in the Rings to Wait field when you create a destination. If you do not specify a number of rings, Connection
                           uses the default value of four rings. You can change the Rings to Wait setting anytime after you create a destination.

When Connection runs out of destinations, the call is forwarded to your default phone number or to the primary extension in
                           the destination group, which is typically your primary extension.

## Creating Destination Groups

You can add any of your destinations to a destination group. You can also add a destination to more than one destination group.
                              A destination group must contain at least one phone number.

The order of destinations within a group is important because Cisco Unity Connection dials the destinations from top to bottom
                              as they appear in the list. After you add destinations to a group, you may need to reorder them to suit your needs.

Step 1

In the Personal Call Transfer Rules web tool, from the Destinations menu, select View Destination Groups .

Step 2

On the Destinations Groups page, select the New Destination Group icon below the menu bar.

Step 3

On the Destination Group page, enter the name of the group.

Step 4

Select Save .

Step 5

On the Destination Group page, select Add Destinations .

Step 6

On the Add Destinations page, check the check box next to the destination that you want to add to the group. You can check
                                       multiple check boxes to add more than one destination at a time.

Step 7

Select Add Destinations .

Step 8

On the Destination Group page, enter numbers in the Priority column to specify the order in which you want Connection to try
                                       the destinations in the group. (For example, to call your mobile phone first and your home phone second, enter 1 for your
                                       mobile phone and 2 for your home phone.)

Step 9

Select Save .

## Changing Destination Groups

You can change the group name, add or delete destinations from the group, and change the priority order of the destinations
                              in the group.

Step 1

In the Personal Call Transfer Rules web tool, from the Destinations menu, select View Destination Groups .

Step 2

On the Destination Groups page, select the name of the group.

Step 3

On the Destination Group page, change the group name or change the priority order of the destinations in the group.

Step 4

Select Add Destinations to add another destination to the group. To remove a destination from the group, check the check box next to the destination
                                       name and select Delete Selected .

Step 5

Select Save .

## Deleting Destinations from Destination Groups

The last phone destination cannot be deleted from a destination group if that will result in the group having only SMS or
                              SMTP destinations.

Step 1

In the Personal Call Transfer Rules web tool, from the Destinations menu, select View Destination Groups .

Step 2

On the Destination Groups page, select the name of the group.

Step 3

On the Destination Group page, check the check box for the destination you want to delete from the group. You can check multiple
                                       check boxes to delete more than one destination at a time.

Step 4

Select Delete Selected .

## Deleting Destination Groups

You cannot delete a destination group while it is used in a rule. Remove the destination group from the rule first, and then
                              delete the destination group.

Step 1

In the Personal Call Transfer Rules web tool, from the Destinations menu, select View Destination Groups .

Step 2

On the Destination Groups page, check the check box for the group you want to delete. You can check multiple check boxes to
                                       delete more than one destination group at a time.

Step 3

Select the Delete Selected Rows icon below the menu bar.

| Phone | Phone
                                       				destinations are phone numbers to which Connection can transfer incoming calls. Phone numbers
                                       				associated with you in the Connection directory can be used as phone
                                       				destinations. These might include your primary extension, voicemail access
                                       				number, and company mobile phone number. Phone numbers in the directory are
                                       				maintained by your Connection administrator. You can also
                                       				create personal phone destinations, such as your personal mobile phone number,
                                       				your home phone number (if it is not listed in the Connection directory), and
                                       				phone numbers at which you can be reached during a business trip. You manage
                                       				these destinations in the Personal Call Transfer Rules web tool. |
|---|---|
| SMS | SMS destinations
                                       				are phone numbers for SMS devices to which Connection can send a text message.
                                       				The message uses the standard format “You have a call from <number or
                                       				extension> at <time> on <date>.” (For example, “You have a call
                                       				from 3233 at 15:16 on 04 October 2010.”) Note that for an
                                       				SMS destination to be used in a rule, it must be added to a destination group
                                       				that contains at least one phone destination. (SMS destinations do not appear
                                       				in the Destination list on the Rule page when you are creating a rule.) SMS devices may
                                       				be added for you by your Connection administrator, and you may be able to
                                       				modify them in the Messaging Assistant web tool. SMS devices do not need to be
                                       				enabled in the Messaging Assistant to be available as a destination in the
                                       				Personal Call Transfer Rules web tool. |
| SMTP | SMTP
                                       				destinations are email addresses to which Connection can send a text message.
                                       				The message uses the standard format “You have a call from <number or
                                       				extension> at <time> on <date>.” (For example, “You have a call
                                       				from 3233 at 15:16 on 04 October 2010.”) Note that for an
                                       				SMTP destination to be used in a rule, it must be added to a destination group
                                       				that contains at least one phone destination. (SMTP destinations do not appear
                                       				in the Destination list on the Rule page when you are creating a rule.) SMTP devices may
                                       				be created for you by your Connection administrator, and you may be able to
                                       				modify them in the Messaging Assistant web tool. SMTP devices do not need to be
                                       				enabled in the Messaging Assistant to be available as a destination in the
                                       				Personal Call Transfer Rules web tool. |
| HTML | HTML destinations are email addresses to which
                                    			 Connection can send email. The email uses the standard format “You have a call
                                    			 from <number > <extension>.” (For example, “You have a call from
                                    			 Jana [1014] ”). |

| Step 1 | In the Personal Call Transfer Rules web tool, from the Destinations menu, select View Destinations . |
|---|---|
| Step 2 | On the Destinations page, select the New Destination icon below the menu bar. |
| Step 3 | On the Create Destination page, in the Name field, enter a name for the destination. |
| Step 4 | In the Phone Number field, enter a phone number for the destination. Use digits 0 through 9. Do not use spaces or parentheses between digits. For long-distance numbers, also include 1 and the
                                          area code. You may not be able to enter certain phone numbers, or your phone system may require additional characters (for example, you
                                          may be required to enter an access code to dial outgoing numbers). If you are experiencing difficulties with this setting,
                                          contact your Connection administrator. |
| Step 5 | In the Rings to Wait field, enter the number of rings you want Connection to wait before transferring the call to voicemail
                                       or to the next destination in a destination group, depending on your other call transfer settings. The default value is four
                                       rings. |
| Step 6 | If you have set this destination to forward calls to Connection, check the Loop Detection Enabled check box. If you create a rule that transfers calls from Connection to a phone destination, you may inadvertently create a call-looping
                                          situation in which Connection forwards calls to your phone, and your phone consequently forwards the call back to Connection,
                                          and callers may never be able to reach you. Selecting this setting when you configure this type of destination to forward
                                          calls to Connection can help eliminate call-looping problems. |
| Step 7 | Select Save . |

| Step 1 | In the Personal Call Transfer Rules web tool, from the Destinations menu, select View Destinations . |
|---|---|
| Step 2 | On the Destinations page, select the name of the personal destination. |
| Step 3 | On the Change Destination page, make the applicable changes and select Save . |

| Step 1 | In the Personal Call Transfer Rules web tool, from the Destinations menu, select View Destinations . |
|---|---|
| Step 2 | On the Destinations page, check the check box for the personal destination you want to delete. You can check multiple check
                                       boxes to delete more than one personal destination at a time. |
| Step 3 | Select the Delete Selected Rows icon below the menu bar. |

| Step 1 | In the Personal Call Transfer Rules web tool, from the Destinations menu, select View Destinations . |
|---|---|
| Step 2 | On the Destinations page, in the Rings to Wait column, enter the new value for the number of rings you want Connection to
                                       wait before transferring the call to voicemail or to the next destination in a destination group. |
| Step 3 | Select Update . |

| Note | When this setting is enabled, you can expect to hear a slight delay as Connection transfers the call to the next destination
                                          in the destination group, or to voicemail. |
|---|---|

| Step 1 | In the Personal Call Transfer Rules web tool, from the Destinations menu, select View Destinations . |
|---|---|
| Step 2 | If you have set this destination to forward calls to Cisco Unity Connection, check the Loop Detection Enabled check box. |
| Step 3 | Select Update . |

| Step 1 | In the Personal Call Transfer Rules web tool, from the Destinations menu, select View Destination Groups . |
|---|---|
| Step 2 | On the Destinations Groups page, select the New Destination Group icon below the menu bar. |
| Step 3 | On the Destination Group page, enter the name of the group. |
| Step 4 | Select Save . |
| Step 5 | On the Destination Group page, select Add Destinations . |
| Step 6 | On the Add Destinations page, check the check box next to the destination that you want to add to the group. You can check
                                       multiple check boxes to add more than one destination at a time. |
| Step 7 | Select Add Destinations . |
| Step 8 | On the Destination Group page, enter numbers in the Priority column to specify the order in which you want Connection to try
                                       the destinations in the group. (For example, to call your mobile phone first and your home phone second, enter 1 for your
                                       mobile phone and 2 for your home phone.) |
| Step 9 | Select Save . |

| Step 1 | In the Personal Call Transfer Rules web tool, from the Destinations menu, select View Destination Groups . |
|---|---|
| Step 2 | On the Destination Groups page, select the name of the group. |
| Step 3 | On the Destination Group page, change the group name or change the priority order of the destinations in the group. |
| Step 4 | Select Add Destinations to add another destination to the group. To remove a destination from the group, check the check box next to the destination
                                       name and select Delete Selected . |
| Step 5 | Select Save . |

| Step 1 | In the Personal Call Transfer Rules web tool, from the Destinations menu, select View Destination Groups . |
|---|---|
| Step 2 | On the Destination Groups page, select the name of the group. |
| Step 3 | On the Destination Group page, check the check box for the destination you want to delete from the group. You can check multiple
                                       check boxes to delete more than one destination at a time. |
| Step 4 | Select Delete Selected . |

| Step 1 | In the Personal Call Transfer Rules web tool, from the Destinations menu, select View Destination Groups . |
|---|---|
| Step 2 | On the Destination Groups page, check the check box for the group you want to delete. You can check multiple check boxes to
                                       delete more than one destination group at a time. |
| Step 3 | Select the Delete Selected Rows icon below the menu bar. |