---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-useroptions-14-cucm-b-self-care-guide-for-14-cucm-b-cisco-unified-commu-c438fe51f1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/useroptions/14/cucm_b_self-care-guide-for-14/cucm_b_cisco-unified-communications-self-care_125SU1_chapter_011.html
retrieved_at: 2026-08-17T00:22:07.108227+00:00
---

Cisco Unified Communications Self Care Portal User Guide, Release 14

# Cisco Unified Communications Self Care Portal User Guide, Release 14

Updated: April 6, 2021

Chapter: Phone Feature Configuration

## Chapter: Phone Feature Configuration

# Phone Feature Configuration

## Create Speed-Dial Numbers

From Unified Communications Self Care Portal , choose Phones > Phone Settings > Speed Dial Numbers .

Choose your phone and click Add New Speed Dial .

Enter the required field details such as Number/URI, Label (description) and Speed Dial, and then click Ok .

### Set Speed Dial Numbers with Pauses

You can set pauses in a speed dial. This allows you to make calls to destinations that require Forced Authorization Code (FAC),
                              Client Matter Code (CMC), dialing pause, or additional digits (such as a user extension, meeting access number, or voice mail
                              password without manual intervention. When you press the speed dial the phone establishes a call and sends other digits to
                              the destination along with the dialing pauses.

To include pauses in a speed dial, you have to specify a comma (,) in the speed dial string. Each comma indicates a pause
                              of two seconds.

For example— you want to set up a speed dial that includes codes such as Forced Authorization Code (FAC) and Client Matter
                              Code (CMC), followed by IVR prompts where:

The called number is 91886543.

The FAC code is 8787.

The CMC code is 5656.

The IVR response is 987989#. You need to enter this response four seconds after the call connects.

In this case, you can set 91886543,8787,5656,987989# as the speed dial.

## Set Up Your Voicemail Notifications

From Unified Communications Self Care Portal , choose Phones > Phone Settings > Voicemail Notification Settings .

Choose your phone number and check any of the notification options check boxes to enable them.

Turn on message waiting light—A red light blinks near the message icon button on your phone screen when you receive a voicemail
                                                message.

Display screen prompt—A voicemail icon appears on your phone screen when you receive a voicemail message.

Play stutter tone when on a call—You hear a dial tone when you pick up your phone or when you are on a call. The dial tone
                                                indicates that there is a voicemail message.

Click Save .

### Set Voicemail Preferences

You can set preferences for your voicemail such as the device on which you want to set the voicemail or your preferred language
                                 and so on.

From Unified Communications Self Care Portal , choose Voicemail.

Click Dial Voicemail Preferences IVR .

## Set up Login Time Limit for Extension Mobility

From Unified Communications Self Care Portal , choose General Settings > Extension Mobility .

- Click the Use system default Maximum Login Time radio button, if you want to retain the default maximum login time limit.

- Click the No Maximum Login Time radio button, if you do not want to set the maximum login time limit.

- Click the Automatically log me out radio button, enter the hours and minutes in the respective fields, if you want to customize the login time limit.

Click Save .

## Save Your Recent Calls

By default, all your missed calls are saved in the call history. If you don't want to save your recent missed calls, uncheck
                                          the Log Missed Calls check box.

From Unified Communications Self Care Portal , choose Phones > Phone Settings > Call History .

Choose your phone number and check the Log Missed Calls check box.

Click Save .

## Add People to Your Phone Contacts

The contact list is unique to each phone. You can't share the contact list with your other phones.

From Unified Communications Self Care Portal , choose Phones > Phone Setting > Phone Contacts .

Click Create New Contact .

Enter the required field details for Contact Information and Contact Methods , and then click Save .

You can click the edit icon to modify the contact name or click the delete icon to remove the contact name from your phone list.

## Forward Your Phone Calls

Call Forward All (CFA) allows a phone user to forward all calls to a directory number. You can configure CFA for internal
                              and external calls and can forward calls to a voicemail system or a dialed destination number by configuring the calling search
                              space (CSS). includes a secondary Calling Search Space configuration field for CFA. The secondary CSS for CFA combines with the existing
                              CSS for CFA to allow support of the alternate CSS system configuration. When you activate CFA, only the primary and secondary
                              CSS for CFA are used to validate the CFA destination and redirect the call to the CFA destination. If these fields are empty,
                              the null CSS is used. Only the CSS fields that are configured in the primary CSS for CFA and secondary CSS for CFA fields
                              are used. If CFA is activated from the phone, the CFA destination is validated by using the CSS for CFA and the secondary
                              CSS for CFA, and the CFA destination gets written to the database. When a CFA is activated, the CFA destination always gets
                              validated against the CSS for CFA and the secondary CSS for CFA.

prevents CFA activation on the phone when a CFA loop is identified. For example, identifies a call forward loop when the user presses the CFwdALL softkey on the phone with directory number 1000 and enters
                              1001 as the CFA destination, and 1001 has forwarded all calls to directory number 1002, which has forwarded all calls to directory
                              number 1003, which has forwarded all calls to 1000. In this case, identifies that a loop has occurred and prevents CFA activation on the phone with directory number 1000.

If the same directory number exists in different partitions, for example, directory number 1000 exists in partitions 1 and
                                          2, allows the CFA activation on the phone.

CFA loops do not affect call processing because supports CFA loop breakout, which ensures that if a CFA loop is identified, the call goes through the entire forwarding chain,
                              breaks out of the Call Forward All loop, and the loop is completed as expected, even if CFNA, CFB, or other forwarding options
                              are configured along with CFA for one of the directory numbers in the forwarding chain.

For example, the user for the phone with directory number 1000 forwards all calls to directory number 1001, which has forwarded
                              all calls to directory number 1002, which has forwarded all calls to directory number 1000, which creates a CFA loop. In addition,
                              directory number 1002 has configured CFNA to directory number 1004. The user at the phone with directory number 1003 calls
                              directory number 1000, which forwards to 1001, which forwards to 1002. identifies a CFA loop, and the call, which breaks out of the loop, tries to connect to directory number 1002. If the No Answer
                              Ring Duration timer expires before the user for the phone with directory number 1002 answers the call, forwards the call to directory number 1004.

For a single call, may identify multiple CFA loops and attempt to connect the call after each loop is identified.

The forward does not work from self care portal unless css is already configured correctly to reach this number from line web page , and the "forwarded to ###" always comes up.

From Unified Communications Self Care Portal , choose Phones > Call Forwarding .

Choose your phone number and do the following:

To forward calls to a voicemail account, check the Forward all calls to: check box, and choose Voicemail from the drop-down list.

To forward calls to another phone number, check the Forward all calls to: check box, and choose Add a new number from the drop-down list, and enter the phone number in the text box.

To forward your internal or external calls, click Advanced calling rules and choose either Voicemail or Add a new number from the drop-down list, and then click Save .

To delete or remove a Call Forwarding setting, do the following:

To delete the Call Forward All settting, uncheck the Forward all calls to: check box and click Save .

To delete an advanced call forwarding setting, expand the Advanced calling rules area, uncheck the check box for the setting that you want to delete, and click Save .

## Handle Work Calls From Any Phone

You can also set the time interval when you want someone to reach out to you on your phones.

From Unified Communications Self Care Portal , choose Phones > My Phones .

Click the Add New icon.

Enter the phone number and description in the respective fields.

Check the Enable Single Number Reach check box and the Enable Move to Mobile check box.

Click Advanced call timing and choose any of the options if you want to set up a time interval for the call transfer.

Wait ( ) seconds before ringing this phone when my business line is dialed —Allows you to set the time interval for your desk phone to ring before trying to contact you at the new number.

Using a time delay of ( )seconds to detect when calls go straight to voicemail —Allows you to set up a time interval before allowing the call to reach your phone's voicemail

Requiring you to respond to a prompt to be connected —Your call is on hold and prompts you to enter a digit on your phone to answer the call rather than send it to your phone's
                                                         voicemail.

Stop ringing this phone after ( ) seconds to avoid connecting to this phones voicemail —Allows you to set up a ring time interval for your phone to stop ringing, so that the calls are not moved to your phone's
                                                voicemail.

Click Save .

## Transfer Your Work Calls to Your Personal Phone

From Unified Communications Self Care Portal , choose Phones > My Phones .

Hover over your additional phone, click the Settings icon, and choose Edit .

In the Edit Additional Phone dialog box, check the Enable Move To Mobile check box, and then click Save .

| Step 1 | From Unified Communications Self Care Portal , choose Phones > Phone Settings > Speed Dial Numbers . |
|---|---|
| Step 2 | Choose your phone and click Add New Speed Dial . |
| Step 3 | Enter the required field details such as Number/URI, Label (description) and Speed Dial, and then click Ok . |

| Step 1 | From Unified Communications Self Care Portal , choose Phones > Phone Settings > Voicemail Notification Settings . |
|---|---|
| Step 2 | Choose your phone number and check any of the notification options check boxes to enable them. Turn on message waiting light—A red light blinks near the message icon button on your phone screen when you receive a voicemail
                                                message. Display screen prompt—A voicemail icon appears on your phone screen when you receive a voicemail message. Play stutter tone when on a call—You hear a dial tone when you pick up your phone or when you are on a call. The dial tone
                                                indicates that there is a voicemail message. |
| Step 3 | Click Save . |

| Step 1 | From Unified Communications Self Care Portal , choose Voicemail. |
|---|---|
| Step 2 | Click Dial Voicemail Preferences IVR . Cisco Web Dialer dials the Voicemail Preferences IVR, where you can set up voicemail preferences for your phones. |

| Step 1 | From Unified Communications Self Care Portal , choose General Settings > Extension Mobility . Click the Use system default Maximum Login Time radio button, if you want to retain the default maximum login time limit. Click the No Maximum Login Time radio button, if you do not want to set the maximum login time limit. Click the Automatically log me out radio button, enter the hours and minutes in the respective fields, if you want to customize the login time limit. |
|---|---|
| Step 2 | Click Save . |

| Note | By default, all your missed calls are saved in the call history. If you don't want to save your recent missed calls, uncheck
                                          the Log Missed Calls check box. |
|---|---|

| Step 1 | From Unified Communications Self Care Portal , choose Phones > Phone Settings > Call History . |
|---|---|
| Step 2 | Choose your phone number and check the Log Missed Calls check box. |
| Step 3 | Click Save . |

| Note | The contact list is unique to each phone. You can't share the contact list with your other phones. |
|---|---|

| Step 1 | From Unified Communications Self Care Portal , choose Phones > Phone Setting > Phone Contacts . |
|---|---|
| Step 2 | Click Create New Contact . |
| Step 3 | Enter the required field details for Contact Information and Contact Methods , and then click Save . Note You can click the edit icon to modify the contact name or click the delete icon to remove the contact name from your phone list. | Note | You can click the edit icon to modify the contact name or click the delete icon to remove the contact name from your phone list. |
| Note | You can click the edit icon to modify the contact name or click the delete icon to remove the contact name from your phone list. |

| Note | You can click the edit icon to modify the contact name or click the delete icon to remove the contact name from your phone list. |
|---|---|

| Tip | If the same directory number exists in different partitions, for example, directory number 1000 exists in partitions 1 and
                                          2, allows the CFA activation on the phone. |
|---|---|

| Note | The forward does not work from self care portal unless css is already configured correctly to reach this number from line web page , and the "forwarded to ###" always comes up. |
|---|---|

| Step 1 | From Unified Communications Self Care Portal , choose Phones > Call Forwarding . |
|---|---|
| Step 2 | Choose your phone number and do the following: To forward calls to a voicemail account, check the Forward all calls to: check box, and choose Voicemail from the drop-down list. To forward calls to another phone number, check the Forward all calls to: check box, and choose Add a new number from the drop-down list, and enter the phone number in the text box. |
| Step 3 | To forward your internal or external calls, click Advanced calling rules and choose either Voicemail or Add a new number from the drop-down list, and then click Save . Note To delete or remove a Call Forwarding setting, do the following: To delete the Call Forward All settting, uncheck the Forward all calls to: check box and click Save . To delete an advanced call forwarding setting, expand the Advanced calling rules area, uncheck the check box for the setting that you want to delete, and click Save . | Note | To delete or remove a Call Forwarding setting, do the following: To delete the Call Forward All settting, uncheck the Forward all calls to: check box and click Save . To delete an advanced call forwarding setting, expand the Advanced calling rules area, uncheck the check box for the setting that you want to delete, and click Save . |
| Note | To delete or remove a Call Forwarding setting, do the following: To delete the Call Forward All settting, uncheck the Forward all calls to: check box and click Save . To delete an advanced call forwarding setting, expand the Advanced calling rules area, uncheck the check box for the setting that you want to delete, and click Save . |

| Note | To delete or remove a Call Forwarding setting, do the following: To delete the Call Forward All settting, uncheck the Forward all calls to: check box and click Save . To delete an advanced call forwarding setting, expand the Advanced calling rules area, uncheck the check box for the setting that you want to delete, and click Save . |
|---|---|

| Step 1 | From Unified Communications Self Care Portal , choose Phones > My Phones . |
|---|---|
| Step 2 | Click the Add New icon. |
| Step 3 | Enter the phone number and description in the respective fields. |
| Step 4 | Check the Enable Single Number Reach check box and the Enable Move to Mobile check box. |
| Step 5 | Click Advanced call timing and choose any of the options if you want to set up a time interval for the call transfer. Wait ( ) seconds before ringing this phone when my business line is dialed —Allows you to set the time interval for your desk phone to ring before trying to contact you at the new number. Prevent this call from going straight to this phones voice mail by Using a time delay of ( )seconds to detect when calls go straight to voicemail —Allows you to set up a time interval before allowing the call to reach your phone's voicemail Requiring you to respond to a prompt to be connected —Your call is on hold and prompts you to enter a digit on your phone to answer the call rather than send it to your phone's
                                                         voicemail. Stop ringing this phone after ( ) seconds to avoid connecting to this phones voicemail —Allows you to set up a ring time interval for your phone to stop ringing, so that the calls are not moved to your phone's
                                                voicemail. |
| Step 6 | Click Save . |

| Step 1 | From Unified Communications Self Care Portal , choose Phones > My Phones . |
|---|---|
| Step 2 | Hover over your additional phone, click the Settings icon, and choose Edit . |
| Step 3 | In the Edit Additional Phone dialog box, check the Enable Move To Mobile check box, and then click Save . |