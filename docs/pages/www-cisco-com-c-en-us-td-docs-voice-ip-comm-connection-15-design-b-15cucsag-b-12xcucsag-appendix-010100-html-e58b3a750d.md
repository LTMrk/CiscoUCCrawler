---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-design-b-15cucsag-b-12xcucsag-appendix-010100-html-e58b3a750d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/design/b_15cucsag/b_12xcucsag_appendix_010100.html
retrieved_at: 2026-08-17T03:46:51.134188+00:00
---

System Administration Guide

# System Administration Guide

Updated: June 27, 2023

Chapter: Bulk
	 Administration Tool

## Chapter: Bulk
	 Administration Tool

# Bulk
                     	 Administration Tool

## Required and
                        	 Optional CSV Fields in BAT

The BAT tool allows
                           		you to create, update, and delete multiple user accounts, contacts,
                           		distribution lists, distribution list members, or unified messaging accounts by
                           		importing information contained in a comma separated value (CSV) file. For more
                           		information on BAT, see the Bulk Administration Tool section.

The tables in this
                           		section list the required and optional fields to include input CSV files. The
                           		fields are listed in alphabetical order, except for the required fields that
                           		are listed first.

Use the applicable
                           		table, depending on the type of object:

- Users With or Without Voice
                              		  Mailboxes

- Contacts

- Distribution Lists

- Distribution List Members

- Unified Messaging Accounts

## Required and
                        	 Optional CSV Fields for User

Alias

The unique
                                       				  text name for the user account.

Any
                                       				  combination of ASCII or unicode alphanumeric characters, periods, commas,
                                       				  spaces, and the special characters `, ~, !, @, #, $, %, ^, &, -, _, ', up
                                       				  to a maximum of 64 characters.

You should
                                       				  use only printable ASCII characters in the Alias field, because some messaging
                                       				  features do not support non-printing ASCII characters or Unicode. (The
                                       				  non-printing ASCII control characters are those below code 0x20.) For example,
                                       				  IMAP only supports user names that contain printable ASCII characters, so users
                                       				  with aliases that contain non-printing characters or unicode are unable to
                                       				  access their Connection messages via IMAP clients. In addition, the Cisco
                                       				  Object Backup and Restore Application Suite (COBRAS) is unable to back up
                                       				  messages for such users, because COBRAS uses IMAP to perform the backup.

Extension

(Users With
                                       				  Mailbox Only)

The number
                                       				  that callers dial to reach the user.

The value
                                       				  must be unique among users in the partition.

Any
                                       				  combination of ASCII alphanumeric characters, from 3 to 40 characters long.

TemplateAlias

The unique
                                       				  text name for the user template to apply to the account during creation.

Caution

Password

The unique
                                       				  characters that the user enters to access Unity Connection web applications.

Any
                                       				  combination of alphanumeric characters, and the following special characters:
                                       				  ~!@#$%^&*()-_+={}|[]:"';<>?/\.

To help
                                       				  protect Unity Connection from unauthorized access and toll fraud, enter a long,
                                       				  eight or more characters and non-trivial password.

PIN

(Users With
                                       				  Mailbox Only)

The unique
                                       				  digits that the user enters to access voice messages by phone.

Any
                                       				  combination of digits 0 through 9.

To help
                                       				  protect Unity Connection from unauthorized access and toll fraud, enter a
                                       				  long-six or more digits-and non-trivial PIN.

For more
                                       				  information on PIN Synchronization, see the " PIN Synchronization between
                                          					 Unity Connection and Cisco Unified CM " section of the "User Settings"
                                       				  chapter.

Address

The physical
                                       				  address, such as a house number and street name where the user is located, or
                                       				  with which the user is associated.

Any
                                       				  combination of ASCII or unicode characters up to a maximum of 128 characters.

AltFirstNames

(Users With
                                       				  Mailbox Only)

An alternate
                                       				  version of the first name. Unity Connection considers alternate names when
                                       				  users and callers use voice recognition to place a call or address voice
                                       				  messages.

To
                                       				  create/update more than one alternate first name per user, separate them by
                                       				  semicolons (;). If an alternate name needs to contain a semicolon, precede the
                                       				  semicolon with another semicolon to indicate to Unity Connection that the name
                                       				  contains a semicolon.

Use this
                                       				  field in conjunction with the AltLastNames field to add nicknames or maiden
                                       				  names for users. You can also use alternate names to add phonetic spellings of
                                       				  hard-to-pronounce names.

Alternate
                                       				  first names and alternate last names are stored as a pair in the database. When
                                       				  submitting multiple alternate names, make sure that you have the same number of
                                       				  alternate first names and alternate last names.

For example,
                                       				  if you have a user named Elizabeth Brown, who is sometimes known as "Liz" and
                                       				  sometimes known by her maiden name of "Smith," you would enter the following
                                       				  AltFirstNames and AltLastNames to ensure that all four combinations are
                                       				  submitted to the database:

- Elizabeth; Liz; Elizabeth;
                                          					 Liz

- Brown; Brown; Smith; Smith

AltLastNames

(Users With
                                       				  Mailbox Only)

An alternate
                                       				  version of the last name. Unity Connection considers alternate names when users
                                       				  and callers use voice recognition to place a call or address voice messages.

To
                                       				  create/update more than one alternate last name per user, separate them by
                                       				  semicolons (;). If an alternate name needs to contain a semicolon, precede the
                                       				  semicolon with another semicolon to indicate to Unity Connection that the name
                                       				  contains a semicolon.

Use this
                                       				  field in conjunction with the AltFirstNames field to add nicknames or maiden
                                       				  names for users. You can also use alternate names to add phonetic spellings of
                                       				  hard-to-pronounce names.

Alternate
                                       				  first names and alternate last names are stored as a pair in the database. When
                                       				  submitting multiple alternate names, make sure that you have the same number of
                                       				  alternate first names and alternate last names.

For example,
                                       				  if you have a user named Elizabeth Brown, who is sometimes known as "Liz" and
                                       				  sometimes known by her maiden name of "Smith," you would enter the following
                                       				  AltFirstNames and AltLastNames to ensure that all four combinations are
                                       				  submitted to the database:

- Elizabeth; Liz;
                                          					 Elizabeth; Liz

- Brown; Brown; Smith;
                                          					 Smith

AltFirstName

(Users
                                       				  With Mailbox Only)

An
                                       				  alternate spelling of the user first name in an internationally recognizable
                                       				  format (i.e., ASCII only characters). The value is used by the phone interface
                                       				  to search for users and to address messages.

Any
                                       				  combination of ASCII alphanumeric characters up to maximum of 64 characters.

AltLastName

(Users
                                       				  With Mailbox Only)

An
                                       				  alternate spelling of the user first name in an internationally recognizable
                                       				  format (i.e., ASCII only characters). The value is used by the phone interface
                                       				  to search for users and to address messages.

Any
                                       				  combination of ASCII alphanumeric characters up to maximum of 64 characters.

BillingId

Organization-specific information about the user, such as
                                       				  accounting information, department names, or project codes. The information can
                                       				  be included in user reports.

Any
                                       				  combination of digits from 0 through 9 up to a maximum of 32 digits.

Building

The name
                                       				  of the building where the user is based.

Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters.

City

The name
                                       				  of a locality, such as a city or other geographic region where the user is
                                       				  located, or with which the user is associated.

Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters.

Country

The two
                                       				  letter ISO 3166-1 country code where the user is located, or with which the
                                       				  user is associated.

Two ASCII
                                       				  lower or upper case alpha characters.

Department

The name
                                       				  or number for the department or sub division of an organization to which the
                                       				  user belongs.

Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters.

DisplayName

The user
                                       				  name that appears on the administration and user interfaces.

If
                                       				  Displayname is empty and both Firstname, Lastname are present, then Displayname
                                       				  would be combination of "Firstname Lastname", else Displayname would be Alias.

Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters.

DisplayName

(Users
                                       				  With Mailbox Only)

The user
                                       				  name that appears on the administration and user interfaces.

If
                                       				  Displayname is empty and both Firstname, Lastname are present, then Displayname
                                       				  would be combination of "Firstname Lastname", else Displayname would be Alias.

Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters.

EmailAddress

The email
                                       				  address of the user. This corresponds to the Corporate Email Address field in
                                       				  Cisco Unity Connection Administration.

Any
                                       				  combination of ASCII alphanumeric characters, and the special characters
                                       				  hyphen, underscore, period and at sign ("@"), up to a maximum of 320
                                       				  characters.

MailName

(Users
                                       				  With Mailbox Only)

Name used
                                       				  to construct part of SMTP address before the @ sign.

A name is
                                       				  needed for unicode aliases that cannot be converted into a valid SMTP
                                       				  addresses.

EmployeeId

The
                                       				  numeric or alphanumeric identifier assigned to a user, typically based on order
                                       				  of hire or association with an organization.

Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters.

EnhancedSecurityAlias

The unique
                                       				  text name used to identify and authenticate the user with an RSA SecurID
                                       				  security system.

Any
                                       				  combination of ASCII or unicode characters up to a maximum of 50 characters.

FirstName

The user
                                       				  first name.

Any
                                       				  combination of ANSI or Unicode alphanumeric characters, periods, commas,
                                       				  spaces, and the special characters `, ~, !, @, #, $, %, ^, &, -, _, ', up
                                       				  to a maximum of 64 characters.

Initials

The
                                       				  initials of part or all of the user name.

Any
                                       				  combination of ANSI or unicode alphanumeric characters, periods, commas,
                                       				  spaces, and the special characters `, ~, !, @, #, $, %, ^, &, -, _, ', up
                                       				  to a maximum of 6 characters.

Language

The preferred language of the user.

Use the Windows language code, such as 1033 for U.S. English. For a list of supported languages and the corresponding language
                                       codes, see the "Numeric and Alphabetic Codes for Supported Languages" section in the System Requirements for Cisco Unity Connection
                                       15 at

LastName

The user
                                       				  last name.

Any
                                       				  combination of ANSI or unicode alphanumeric characters, periods, commas,
                                       				  spaces, and the special characters `, ~, !, @, #, $, %, ^, &, -, _, ', up
                                       				  to a maximum of 64 characters.

Manager

The name
                                       				  of the manager or supervisor of the user.

Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters.

PostalCode

For users
                                       				  located in the United States, the zip code where the user is located, or with
                                       				  which the user is associated. For users located in Canada, Mexico, and other
                                       				  countries, the postal code where the user is located, or with which the user is
                                       				  associated.

Any
                                       				  combination of ASCII or unicode characters up to a maximum of 40 characters.

State

The full
                                       				  name of the state or province where the user is located, or with which the user
                                       				  is associated.

Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters.

TimeZone

The time
                                       				  zone with which the user account is associated.

Title

The
                                       				  position or function of the user within the organization, for example "Vice
                                       				  President."

Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters.

COSDisplayName

(Users
                                       				  With Mailbox Only)

The unique
                                       				  text name that is displayed on the user interfaces for the class of service
                                       				  (COS) with which the user account is associated.

Any
                                       				  combination of ASCII or Unicode characters, up to a maximum of 64 characters.

ClientMatterCode

(Users
                                       				  With Mailbox Only)

The
                                       				  required Client Matter Code (CMC) to transmit to Cisco Unified Communications
                                       				  Manager (CM), if applicable, when the user makes an outbound call.

CMCs are
                                       				  typically used to enable the system to track calls for account or billing
                                       				  purposes.

The value
                                       				  is used only if the system is using Cisco Unified CM and if the version of
                                       				  Cisco Unified CM is 4.1 and later.

Whether
                                       				  the CMC is transmitted depends on the setting for outbound calls. The user CMC
                                       				  is used only if the outbound call does not have its own CMC.

The code
                                       				  length can be from 1 through 40 characters.

TransferType

(Users
                                       				  With Mailbox Only)

(Applicable only to the Alternate transfer rule.) Determines the
                                       				  way in which Unity Connection transfers calls from the automated attendant or a
                                       				  directory handler to the user phone for the Alternate transfer rule:

- 0-supervised

- 1-unsupervised (also
                                             					 called a "Release to Switch" transfer)

TransferRings

(Users
                                       				  With Mailbox Only)

(Applicable only to the Alternate transfer rule.) Determines the
                                       				  number of times the user extension rings before Unity Connection considers the
                                       				  call unanswered ("ring-no-answer") and plays the applicable greeting. This
                                       				  setting is applicable only when the TransferType is configured for a supervised
                                       				  transfer.

An
                                       				  integer value from 2 through 100.

TransferExtension

(Users
                                       				  With Mailbox Only)

TransferAction

(Users
                                       				  With Mailbox Only)

(Applicable only to the Alternate transfer rule.) Determines
                                       				  whether Unity Connection transfers the incoming calls for the user to the user
                                       				  greeting or to the extension specified in TransferExtension:

- 0-Transfer to the
                                             					 greeting.

- 1-Transfer to
                                             					 TransferExtension.

RnaAction

(Users
                                       				  With Mailbox Only)

(Applicable only to the Alternate transfer rule.) This setting
                                       				  is applicable only when the TransferType is configured for a supervised
                                       				  transfer. Determines whether Unity Connection transfers the call to the
                                       				  applicable greeting or releases the call to the phone system when a call is
                                       				  unanswered ("ring-no-answer"):

- 0-Release the call to
                                             					 the phone system.

- 1-After the number of
                                             					 rings specified in the TransferRings field, transfer the call to the
                                             					 appropriate greeting.

StandardTransferType

(Users
                                       				  With Mailbox Only)

(Applicable only to the Standard transfer rule.) Determines the
                                       				  way in which Unity Connection transfers calls from the automated attendant or a
                                       				  directory handler to the user phone for the standard (default) transfer rule:

- 0-supervised

- 1-unsupervised (also
                                             					 called a "Release to Switch" transfer)

StandardTransferRings

(Users
                                       				  With Mailbox Only)

(Applicable only to the Standard transfer rule.) Determines the
                                       				  number of times the user extension rings before Unity Connection considers the
                                       				  call unanswered ("ring-no-answer") and plays the applicable greeting. This
                                       				  setting is applicable only when the StandardTransferType is configured for a
                                       				  supervised transfer.

An
                                       				  integer value from 2 through 100.

StandardTransferExtension

(Users
                                       				  With Mailbox Only)

StandardTransferAction

(Applicable only to the Standard transfer rule.) Determines
                                       				  whether Unity Connection transfers the incoming calls for the user to the user
                                       				  greeting or to the extension specified in StandardTransferExtension:

- 0-Transfer to the
                                             					 greeting.

- 1-Transfer to
                                             					 StandardTransferExtension.

StandardRnaAction

(Users
                                       				  With Mailbox Only)

(Applicable only to the Standard transfer rule.) This setting is
                                       				  applicable only when the StandardTransferType is configured for a supervised
                                       				  transfer. Determines whether Unity Connection transfers the call to the
                                       				  applicable greeting or releases the call to the phone system when a call is
                                       				  unanswered ("ring-no-answer"):

- 0-Release the call to
                                             					 the phone system.

- 1-After the number of
                                             					 rings specified in the StandardTransferRings field, transfer the call to the
                                             					 appropriate greeting.

ClosedTransferType

(Users
                                       				  With Mailbox Only)

(Applicable only to the Closed transfer rule.) Determines the
                                       				  way in which Unity Connection transfers calls from the automated attendant or a
                                       				  directory handler to the user phone for the Closed transfer rule:

- 0-supervised

- 1-unsupervised (also
                                             					 called a "Release to Switch" transfer)

ClosedTransferRings

(Users
                                       				  With Mailbox Only)

(Applicable only to the Closed transfer rule.) Determines the
                                       				  number of times the user extension rings before Unity Connection considers the
                                       				  call unanswered ("ring-no-answer") and plays the applicable greeting. This
                                       				  setting is applicable only when the ClosedTransferType is configured for a
                                       				  supervised transfer.

An
                                       				  integer value from 2 through 100.

ClosedTransferExtension

(Users
                                       				  With Mailbox Only)

ClosedTransferAction

(Users
                                       				  With Mailbox Only)

(Applicable only to the Closed transfer rule.) Determines
                                       				  whether Cisco Unity Connection transfers the incoming calls for the user to the
                                       				  user greeting or to the extension specified in ClosedTransferExtension:

- 0-Transfer to the
                                             					 greeting.

- 1-Transfer to
                                             					 ClosedTransferExtension.

ClosedRnaAction

(Users
                                       				  With Mailbox Only)

(Applicable only to the Closed transfer rule.) This setting is
                                       				  applicable only when the StandardTransferType is configured for a supervised
                                       				  transfer. Determines whether Unity Connection transfers the call to the
                                       				  applicable greeting or releases the call to the phone system when a call is
                                       				  unanswered ("ring-no-answer"):

- 0-Release the call to
                                             					 the phone system.

- 1-After the number of
                                             					 rings specified in the ClosedTransferRings field, transfer the call to the
                                             					 appropriate greeting.

MWIExtension

(Users
                                       				  With Mailbox Only)

The phone
                                       				  number (extension) of the default message waiting indicator (MWI) to light when
                                       				  callers leave messages for the user.

If no
                                       				  value is provided, Unity Connection uses the number of the primary extension.

MWIMediaSwitchDisplay Name

(Users
                                       				  With Mailbox Only)

The text
                                       				  name displayed on the system administration interface of the phone system used
                                       				  to turn message waiting indicators on and off for the phone number specified in
                                       				  the MWIExtension column.

If no
                                       				  value is provided, Unity Connection uses the phone system specified in the
                                       				  MediaSwitchDisplayName column.

MaxMsgLen

(Users
                                       				  With Mailbox Only)

The
                                       				  maximum duration (in seconds) for recording a message from an outside
                                       				  (unidentified) caller.

The
                                       				  length specified can be from 1 through 1,200 seconds.

Play After
                                       				  Message Recording

(Users
                                       				  With Mailbox Only)

Indicates
                                       				  whether Unity Connection plays a recording to the callers after a message has
                                       				  been sent:

- 0-Do Not Play Recording.
                                             					 Select this setting to disable the feature. After a message is sent, users do
                                             					 not hear any recording.

- 1-System Default
                                             					 Recording. After a message is sent, users hear the default system recording.

- 2-Play Recording. After
                                             					 a message is sent, users hear the cutomized recording.

PlayPostGreetingRecording

(Users
                                       				  With Mailbox Only)

Indicates
                                       				  whether Unity Connection plays a recording to callers before allowing them to
                                       				  leave a message for the user. You can also indicate whether all callers hear
                                       				  the recording or only unidentified callers:

- 0-Do Not Play Recording.
                                             					 Select this setting to disable the feature. Before they leave a message,
                                             					 callers hear only the user greeting.

- 1-Play Recording to All
                                             					 Callers. Before they leave a message, users and outside callers hear the user
                                             					 or call handler greeting and then the recording.

- 2-Play Recording Only to
                                             					 Unidentified Callers. Before they leave a message, outside callers hear the
                                             					 user greeting and then the post-greeting recording. Likewise, users who call
                                             					 from a phone that is not associated with their account and do not sign in to
                                             					 Unity Connection hear the post-greeting recording.

PostGreetingRecordingDisplayName

(Users
                                       				  With Mailbox Only)

The
                                       				  display name of the post-greeting recording that plays after the greeting for
                                       				  this user.

ForcedAuthoizationCode

(Users
                                       				  With Mailbox Only)

The
                                       				  required forced-authorization code (FACs) to transmit to Cisco Unified
                                       				  Communications Manager, if applicable, when the user makes an outbound call.

Your
                                       				  organization may use FACs to prevent toll fraud. For example, users may have to
                                       				  provide FACs to place long-distance calls.

The value
                                       				  is used only if the system is using Cisco Unified CM and its version is 4.1 and
                                       				  later.

The code
                                       				  length can be from 1 to 40 characters.

ListInDirectory

(Users
                                       				  With Mailbox Only)

Determines
                                       				  whether the user is included in the phone directory for outside callers:

- 0-Not included in the
                                             					 directory

- 1-Included in the
                                             					 directory

CreateSmtpProxyFromCorp

(Users
                                       				  With Mailbox Only)

Determines
                                       				  whether Unity Connection uses the value in the EmailAddress column (Corporate
                                       				  Email Address field in Cisco Unity Connection Administration) to automatically
                                       				  create a new SMTP proxy address, so that IMAP messages to or from this email
                                       				  address can be properly identified by Unity Connection as belonging to this
                                       				  user. If you uncheck it, no such SMTP proxy address is automatically created.

- 0-SMTP proxy address is
                                             					 not automatically created.

- 1-SMTP proxy address is
                                             					 automatically created using the Corporate Email Address field.

MediaSwitchDisplayName

(Users
                                       				  With Mailbox Only)

The text
                                       				  name displayed on the system administration interface of the phone system used
                                       				  for Telephone Record and Playback (TRAP) sessions and to turn message waiting
                                       				  indicators on and off.

Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters.

PhoneNumber_HomePhone

(Users
                                       				  With Mailbox Only)

The user
                                       				  home phone number.

Any
                                       				  combination of the digits 0-9, T, t, commas, hashes (#), and asterisks (*), up
                                       				  to a maximum of 38 characters.

Active_HomePhone

(Users
                                       				  With Mailbox Only)

Whether
                                       				  the user home phone device is enabled:

- 0-disabled

- 1-enabled

DisplayName_HomePhone

(Users
                                       				  With Mailbox Only)

The text
                                       				  name for the user home phone displayed on the Unity Connection interfaces.

Any
                                       				  combination of ASCII or Unicode characters, up to a maximum of 64 characters.

PhoneNumber_WorkPhone

(Users
                                       				  With Mailbox Only)

The user
                                       				  work phone number.

Any
                                       				  combination of the digits 0-9, T, t, commas, hashes (#), and asterisks (*), up
                                       				  to a maximum of 38 characters.

Active_WorkPhone

(Users
                                       				  With Mailbox Only)

Whether
                                       				  the user work phone device is enabled:

- 0-disabled

- 1-enabled

DisplayName_WorkPhone

(Users
                                       				  With Mailbox Only)

The text
                                       				  name for the user work phone displayed on the Unity Connection interfaces.

Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters.

PhoneNumber_MobilePhone

(Users
                                       				  With Mailbox Only)

The user
                                       				  mobile phone number.

Any
                                       				  combination of the digits 0-9, T, t, commas, hashes (#), and asterisks (*), up
                                       				  to a maximum of 38 characters.

Active_MobilePhone

(Users
                                       				  With Mailbox Only)

Whether
                                       				  the user mobile phone device is enabled:

- 0-disabled

- 1-enabled

DisplayName_MobilePhone

(Users
                                       				  With Mailbox Only)

The text
                                       				  name for the user mobile phone displayed on the Unity Connection interfaces.

Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters.

PhoneNumber_Pager

(Users
                                       				  With Mailbox Only)

The user
                                       				  pager number.

Any
                                       				  combination of the digits 0-9, T, t, commas, hashes (#), and asterisks (*), up
                                       				  to a maximum of 38 characters.

AfterDialDigits_Pager

(Users
                                       				  With Mailbox Only)

Digits to
                                       				  send to the pager. This is referred to in Unity Connection Administration as
                                       				  "Extra Digits." For numeric pagers, the field holds numeric text to send to the
                                       				  pager; for text pagers, the field is blank.

The
                                       				  maximum length is 32 digits.

Active_Pager

(Users
                                       				  With Mailbox Only)

Whether
                                       				  the user pager device is enabled:

- 0-disabled

- 1-enabled

DisplayName_Pager

(Users
                                       				  With Mailbox Only)

The text
                                       				  name for the user pager displayed on the Unity Connection interfaces.

Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters.

PhoneNumber_TextPager1

(Users
                                       				  With Mailbox Only)

This phone
                                       				  number is entered in the From field on the default SMTP device for the user.

Any
                                       				  combination of ASCII only alphanumeric characters, hyphens, underscores,
                                       				  periods, at signs ("@"), commas and hashes (#), up to a maximum of 40
                                       				  characters.

SmtpAddress_TextPager1

(Users
                                       				  With Mailbox Only)

Active_TextPager1

(Users
                                       				  With Mailbox Only)

Whether
                                       				  the user text pager device is enabled:

- 0-disabled

- 1-enabled

DisplayName_TextPager1

(Users
                                       				  With Mailbox Only)

The text
                                       				  name for the user text pager displayed on the Unity Connection interfaces.

Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters.

Extension_Alt1

(Users
                                       				  With Mailbox Only)

The first
                                       				  alternate extension for the user.

The value
                                       				  must be unique in the partition.

Any
                                       				  combination of ASCII alphanumeric characters, from 1 to 40 characters long.

Extension_Alt1_Partition

(Users
                                       				  With Mailbox Only)

The text
                                       				  name of the partition to which the first alternate extension belongs.

Extension_Alt2

(Users
                                       				  With Mailbox Only)

The second
                                       				  alternate extension for the user.

The value
                                       				  must be unique in the partition.

Any
                                       				  combination of ASCII alphanumeric characters, from 1 to 40 characters long.

Extension_Alt2_Partition

(Users
                                       				  With Mailbox Only)

The text
                                       				  name of the partition to which the second alternate extension belongs.

Extension_Alt3

(Users
                                       				  With Mailbox Only)

The third
                                       				  alternate extension for the user.

The value
                                       				  must be unique in the partition.

Any
                                       				  combination of ASCII alphanumeric characters, from 1 to 40 characters long.

Extension_Alt3_Partition

(Users
                                       				  With Mailbox Only)

The text
                                       				  name of the partition to which the third alternate extension belongs.

Extension_Alt4

(Users
                                       				  With Mailbox Only)

The fourth
                                       				  alternate extension for the user.

The value
                                       				  must be unique in the partition.

Any
                                       				  combination of ASCII alphanumeric characters, from 1 to 40 characters long.

Extension_Alt4_Partition

(Users
                                       				  With Mailbox Only)

The text
                                       				  name of the partition to which the fourth alternate extension belongs.

Extension_Alt5

(Users
                                       				  With Mailbox Only)

The fifth
                                       				  alternate extension for the user.

The value
                                       				  must be unique in the partition.

Any
                                       				  combination of ASCII alphanumeric characters, from 1 to 40 characters long.

Extension_Alt5_Partition

(Users
                                       				  With Mailbox Only)

The text
                                       				  name of the partition to which the fifth alternate extension belongs.

Extension_Alt6

(Users
                                       				  With Mailbox Only)

The sixth
                                       				  alternate extension for the user.

The value
                                       				  must be unique in the partition.

Any
                                       				  combination of ASCII alphanumeric characters, from 1 to 40 characters long.

Extension_Alt6_Partition

(Users
                                       				  With Mailbox Only)

The text
                                       				  name of the partition to which the sixth alternate extension belongs.

Extension_Alt7

(Users
                                       				  With Mailbox Only)

The
                                       				  seventh alternate extension for the user.

The value
                                       				  must be unique in the partition.

Any
                                       				  combination of ASCII alphanumeric characters, from 1 to 40 characters long.

Extension_Alt7_Partition

The text
                                       				  name of the partition to which the seventh alternate extension belongs.

Extension_Alt8

(Users
                                       				  With Mailbox Only)

The eighth
                                       				  alternate extension for the user.

The value
                                       				  must be unique in the partition.

Any
                                       				  combination of ASCII alphanumeric characters, from 1 to 40 characters long.

Extension_Alt8_Partition

(Users
                                       				  With Mailbox Only)

The text
                                       				  name of the partition to which the eighth alternate extension belongs.

Extension_Alt9

(Users
                                       				  With Mailbox Only)

The ninth
                                       				  alternate extension for the user.

The value
                                       				  must be unique in the partition.

Any
                                       				  combination of ASCII alphanumeric characters, from 1 to 40 characters long.

Extension_Alt9_Partition

(Users
                                       				  With Mailbox Only)

The text
                                       				  name of the partition to which the ninth alternate extension belongs.

CcmId

(Users
                                       				  With Mailbox Only)

The Cisco
                                       				  Unified Communications Manager user ID that is associated with the user.

Any
                                       				  combination of characters except for non-printing ASCII characters, up to a
                                       				  maximum of 128 characters.

Exchange2010Service_Service DisplayName

(Users
                                       				  With Mailbox Only)

The
                                       				  display name of the Exchange 2010 external service that corresponds with the
                                       				  Exchange 2010 server that contains the Exchange 2010 mailbox for this user.

To add an
                                       				  Exchange 2010 external service for a user, include values for both the
                                       				  Exchange2010Service_ServiceDisplayName and Exchange2010Service_EmailAddress
                                       				  fields in the CSV input file.

To remove
                                       				  the Exchange 2010 service for a user, set at least one of either the
                                       				  Exchange2010Service_ServiceDisplayName and Exchange2010Service_EmailAddress
                                       				  fields to %null% in the CSV input file

Exchange2010Service_Email Address

(Users
                                       				  With Mailbox Only)

The
                                       				  primary email address that is associated with the Exchange mailbox that you
                                       				  want this user to be able to access.

To add an
                                       				  Exchange 2010 external service for a user, include values for both the
                                       				  Exchange2010Service_ServiceDisplayName and Exchange2010Service_EmailAddress
                                       				  fields in the CSV input file

Exchange2010Service_UserId

(Users
                                       				  With Mailbox Only)

The
                                       				  Windows domain alias for the user in Exchange 2010 (useful when the setting is
                                       				  different from the user alias).

Exchange2010Service_User Password

(Users
                                       				  With Mailbox Only)

The
                                       				  Windows domain password for the user.

EmailAction

(Users
                                       				  With Mailbox Only)

Action to
                                       				  take for a voice message:

- 0-Reject the message

- 1-Accept the message

- 2-Relay the message

- 3-Accept the message and
                                             					 relay a copy

VoiceMailAction

(Users
                                       				  With Mailbox Only)

Action to
                                       				  take for a voice message:

- 0-Reject the message

- 1-Accept the message

- 2-Relay the message

- 3-Accept the message and
                                             					 relay a copy

FaxAction

(Users
                                       				  With Mailbox Only)

Action to
                                       				  take for a voice message:

- 0-Reject the message

- 1-Accept the message

- 2-Relay the message

- 3-Accept the message and
                                             					 relay a copy

DeliveryReceiptAction

(Users
                                       				  With Mailbox Only)

Action to
                                       				  take for a voice message:

- 0-Reject the message

- 1-Accept the message

- 2-Relay the message

- 3-Accept the message and
                                             					 relay a copy

RelayAddress

(Users
                                       				  With Mailbox Only)

Specifies
                                       				  the address to relay incoming message when one or more of the actions
                                       				  (EmailAction, VoicemailAction, FaxAction, DeliveryReceiptAction) is set to 2
                                       				  (Relay the message).

RelayAddress is in the format of someone@somewhere or someone@somewhere.com.

SmtpProxyAddresses

(Users
                                       				  With Mailbox Only)

The full
                                       				  SMTP proxy addresses for users. To create/update more than one address per
                                       				  user, separate them by commas and surround them all with double quotes. For
                                       				  example:

"someone1@somewhere.com,someone2@somewhere.com"

LdapCcmUserID

The value
                                       				  of the LDAP field that you mapped to the Unity Connection Alias field when you
                                       				  configured Cisco Unity Connection to integrate with an LDAP directory. See the Task List for Configuring LDAP section.

This
                                       				  field is used when you create Unity Connection users by importing LDAP user
                                       				  data and when you integrate existing Unity Connection users with LDAP users.

CorporatePhoneNumber

(Users
                                       				  With Mailbox Only)

The phone
                                       				  number of the user.

Note that
                                       				  the field is only for directory information purposes. Cisco Unity Connection
                                       				  does not use the phone number to route calls.

DisplayName_HTML1

(Users
                                       				  With Mailbox Only)

A
                                       				  descriptive name for the notification device. This field is required if you
                                       				  want to create an HTML notification device.

Active_HTML1

(Users
                                       				  With Mailbox Only)

Enables
                                       				  the HTML notification device.

callback_HTML1

(Users
                                       				  With Mailbox Only)

The phone
                                       				  number that the user use to play and record voice message.

disableMobPCA_HTML1

(Users
                                       				  With Mailbox Only)

Disallow
                                       				  the users to change the mobile number from Cisco PCA and Mini Web inbox for
                                       				  HTML notification.

disableTemplatePCA_HTML1

(Users
                                       				  With Mailbox Only)

Disallow
                                       				  the users to change the notification template from PCA.

SmtpAddress_HTML1

(Users
                                       				  With Mailbox Only)

The email
                                       				  address of the user text-compatible mobile phone, or another email account
                                       				  (such as a home email address) on which the user receives the HTML
                                       				  notification. Up to 128 characters can be entered in this field.

SmtpAddress_HTML1 column is mandatory if Active_HTML1 column is set to 1.

templateName_HTML1

(Users
                                       				  With Mailbox Only)

A default
                                       				  or a customized template name for HTML notification device.

DisplayName_HTML2

(Users
                                       				  With Mailbox Only)

A
                                       				  descriptive name for the notification device. This field is required if you
                                       				  want to create an HTML Missed Call notification device.

Active_HTML2

(Users
                                       				  With Mailbox Only)

Enables
                                       				  the HTML Missed Call notification device.

callback_HTML2

(Users
                                       				  With Mailbox Only)

The phone
                                       				  number that the user use to view the missed calls.

disableMobPCA_HTML2

(Users
                                       				  With Mailbox Only)

Disallow
                                       				  the users to change the mobile number from Cisco PCA and Mini Web inbox for
                                       				  HTML Missed Call notification.

disableTemplatePCA_HTML2

(Users
                                       				  With Mailbox Only)

Disallow
                                       				  the users to change the notification template from PCA. This field is
                                       				  applicable for HTML Missed Call notification template.

SmtpAddress_HTML2

(Users
                                       				  With Mailbox Only)

The email
                                       				  address of the user text-compatible mobile phone, or another email account
                                       				  (such as a home email address) on which the user receives the HTML Missed Call
                                       				  notification. Up to 128 characters can be entered in this field.

SmtpAddress_HTML2 column is mandatory if Active_HTML2 column is set to 1.

templateName_HTML2

(Users
                                       				  With Mailbox Only)

A default
                                       				  or a customized template name for HTML Missed Call notification device.

DisplayName_HTML3

(Users
                                       				  With Mailbox Only)

A
                                       				  descriptive name for the notification device. This field is required if you
                                       				  want to create an HTML Scheduled Summary notification device.

Active_HTML3

(Users
                                       				  With Mailbox Only)

Enables
                                       				  the HTML Scheduled Summary notification device.

callback_HTML3

(Users
                                       				  With Mailbox Only)

The phone
                                       				  number that the user use to play the voice messages received in Summary
                                       				  notification.

disableMobPCA_HTML3

(Users
                                       				  With Mailbox Only)

Disallow
                                       				  the users to change the mobile number from Cisco PCA and Mini Web inbox for
                                       				  HTML Scheduled Summary notification.

disableTemplatePCA_HTML3

(Users
                                       				  With Mailbox Only)

Disallow
                                       				  the users to change the notification template from PCA. This field is
                                       				  applicable for HTML Scheduled Summary notification template.

SmtpAddress_HTML3

(Users
                                       				  With Mailbox Only)

The email
                                       				  address of the user text-compatible mobile phone, or another email account
                                       				  (such as a home email address) on which the user receives the Summary
                                       				  notification of the voice messages. Up to 128 characters can be entered in this
                                       				  field.

SmtpAddress_HTML3 column is mandatory if Active_HTML3 column is set to 1.

templateName_HTML3

(Users
                                       				  With Mailbox Only)

A default
                                       				  or a customized template name for HTML Scheduled Summary notification device.

DisplayName_HTML3

(Users
                                       				  With Mailbox Only)

A
                                       				  descriptive name for the notification device. This field is required if you
                                       				  want to create an HTML Scheduled Summary notification device.

Active_HTML3

(Users
                                       				  With Mailbox Only)

Enables
                                       				  the HTML Scheduled Summary notification device.

## Required and
                        	 Optional CSV Fields for Contacts

Alias

The unique
                                       				  text name for the contact.

Any
                                       				  combination of ASCII or unicode alphanumeric characters, periods, commas,
                                       				  spaces, and the special characters `, ~, !, @, #, $, %, ^, &, -, _, ', up
                                       				  to a maximum of 64 characters.

Extension

The number
                                       				  that callers dial to reach the contact.

The value
                                       				  must be unique among users and contacts in the partition.

Any
                                       				  combination of ASCII alphanumeric characters up to a maximum of 40 characters.

ContactTemplateAlias

The unique
                                       				  text name for the contact template to apply to the contact during creation.

AltFirstNames

An
                                       				  alternate version of the first name. Unity Connection considers alternate names
                                       				  when users and callers use voice recognition to place a call or address voice
                                       				  messages.

To
                                       				  create/update more than one alternate first name per contact, separate them by
                                       				  semicolons (;). If an alternate name needs to contain a semicolon, precede the
                                       				  semicolon with another semicolon to indicate to Unity Connection that the name
                                       				  contains a semicolon.

Use this
                                       				  field in conjunction with the AltLastNames field to add nicknames or maiden
                                       				  names for users. You can also use alternate names to add phonetic spellings of
                                       				  hard-to-pronounce names.

Alternate
                                       				  first names and alternate last names are stored as a pair in the database. When
                                       				  submitting multiple alternate names, make sure that you have the same number of
                                       				  alternate first names and alternate last names.

For
                                       				  example, if you have a contact named Elizabeth Brown, who is sometimes known as
                                       				  "Liz" and sometimes known by her maiden name of "Smith," you would enter the
                                       				  following AltFirstNames and AltLastNames to ensure that all four combinations
                                       				  are submitted to the database:

- Elizabeth; Liz; Elizabeth;
                                             					 Liz

- Brown; Brown; Smith; Smith

AltLastNames

An alternate
                                       				  version of the last name. Unity Connection considers alternate names when users
                                       				  and callers use voice recognition to place a call or address voice messages.

To
                                       				  create/update more than one alternate last name per contact, separate them by
                                       				  semicolons (;). If an alternate name needs to contain a semicolon, precede the
                                       				  semicolon with another semicolon to indicate to Unity Connection that the name
                                       				  contains a semicolon.

Use this
                                       				  field in conjunction with the AltFirstNames field to add nicknames or maiden
                                       				  names for users. You can also use alternate names to add phonetic spellings of
                                       				  hard-to-pronounce names.

Alternate
                                       				  first names and alternate last names are stored as a pair in the database. When
                                       				  submitting multiple alternate names, make sure that you have the same number of
                                       				  alternate first names and alternate last names.

For
                                       				  example, if you have a contact named Elizabeth Brown, who is sometimes known as
                                       				  "Liz" and sometimes known by her maiden name of "Smith," you would enter the
                                       				  following AltFirstNames and AltLastNames to ensure that all four combinations
                                       				  are submitted to the database:

- Elizabeth; Liz; Elizabeth;
                                             					 Liz

- Brown; Brown; Smith; Smith

AltFirstName

An alternate
                                       				  spelling of the contact first name in an internationally recognizable format
                                       				  (ASCII characters). The value is used by the phone interface to search for
                                       				  users and to address messages.

Any
                                       				  combination of ASCII alphanumeric characters up to maximum of 64 characters.

AltLastName

An alternate
                                       				  spelling of the contact last name in an internationally recognizable format
                                       				  (ASCII characters). The value is used by the phone interface to search for
                                       				  users and to address messages.

Any
                                       				  combination of ASCII alphanumeric characters up to maximum of 64 characters.

DisplayName

The contact
                                       				  name that appears on the administration and user interfaces.

If no value
                                       				  is provided, the value is set to the Alias.

Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters.

FirstName

The
                                       				  contact first name.

Any
                                       				  combination of ANSI or unicode alphanumeric characters, periods, commas,
                                       				  spaces, and the special characters `, ~, !, @, #, $, %, ^, &, -, _, ', up
                                       				  to a maximum of 64 characters.

LastName

The
                                       				  contact last name.

Any
                                       				  combination of ANSI or unicode alphanumeric characters, periods, commas,
                                       				  spaces, and the special characters `, ~, !, @, #, $, %, ^, &, -, _, ', up
                                       				  to a maximum of 64 characters.

ListInDirectory

Determines
                                       				  whether the contact is included in the phone directory for outside callers:

- 0-Not included in the
                                             					 directory

- 1-Included in the
                                             					 directory

RemoteMailAddress

For VPIM
                                       				  contacts, enter the mailbox number of the VPIM contact on the remote voice
                                       				  messaging system.

The
                                       				  maximum length is 256 characters.

TransferEnabled

Determines
                                       				  whether Unity Connection transfers calls from the automated attendant or a
                                       				  directory handler to the phone number that is specified in the
                                       				  TransferExtension field.

- 0-Do not transfer calls.
                                             					 Unity Connection takes a message and sends it to the remote mailbox for the
                                             					 VPIM contact instead.

- 1-Transfer incoming
                                             					 calls to TransferExtension.

TransferExtension

The
                                       				  extension or phone number to which Unity Connection transfers calls when
                                       				  TransferEnabled is set to 1.

When
                                       				  entering a phone number, include any additional numbers necessary to dial
                                       				  outside calls (for example, 9) and for long-distance dialing (for example, 1).

Any
                                       				  combination of numeric digits, commas, and the special characters # and *, up
                                       				  to a maximum of 40 characters.

TransferRings

Determines
                                       				  the number of times the extension of the contact rings before Unity Connection
                                       				  considers the call unanswered ("ring-no-answer") and plays the applicable
                                       				  greeting.

An
                                       				  integer value from 2 through 100.

TransferType

Determines
                                       				  the way in which Unity Connection transfers calls from the automated attendant
                                       				  or a directory handler to the contact phone for the standard (default) transfer
                                       				  rule:

- 0-supervised

- 1-unsupervised (also
                                             					 called a "Release to Switch" transfer)

DeliveryLocation DisplayName

For VPIM
                                       				  contacts, the VPIM delivery location on which the contact mailbox resides. Use
                                       				  the display name of the VPIM location as it is listed in Cisco Unity Connection
                                       				  Administration.

Any
                                       				  combination of ASCII or Unicode characters (except nonprinting ASCII
                                       				  characters), up to maximum of 64 characters.

PartitionDisplayName

The
                                       				  display name of the partition to which the contact belongs.

SmtpProxyAddresses

The full
                                       				  SMTP proxy addresses for contacts. To create/update more than one address per
                                       				  user, separate them by commas and surround them all with double quotes. For
                                       				  example:

"someone1@somewhere.com,someone2@somewhere.com"

DialableWorkPhone

A phone
                                       				  number that voice recognition users can use to call the contact. Include any
                                       				  additional numbers necessary to dial outside calls (for example, 9) and for
                                       				  long-distance dialing (for example, 1).

Any
                                       				  combination of numeric digits, commas, and the special characters # and *, from
                                       				  1 to 255 characters long.

DialableHomePhone

A phone
                                       				  number that voice recognition users can use to call the contact. Include any
                                       				  additional numbers necessary to dial outside calls (for example, 9) and for
                                       				  long-distance dialing (for example, 1).

Any
                                       				  combination of numeric digits, commas, and the special characters #, and *,
                                       				  from 1 to 255 characters long.

DialableMobilePhone

A phone
                                       				  number that voice recognition users can use to call the contact. Include any
                                       				  additional numbers necessary to dial outside calls (for example, 9) and for
                                       				  long-distance dialing (for example, 1).

Any
                                       				  combination of numeric digits, commas, and the special characters #, and *,
                                       				  from 1 to 255 characters long.

City

The name
                                       				  of a locality including a city, county or other geographic region where the
                                       				  contact is located, or with which the contact is associated.

Callers
                                       				  who reach a voice-enabled directory handler can narrow down their search for a
                                       				  contact by saying the name and city of the contact if this field is defined for
                                       				  the contact. (ListInDirectory must also be set to 1 for the contact to be
                                       				  reachable via directory handlers.)

Any
                                       				  combination of ASCII or Unicode characters, up to a maximum of 64 characters.

Department

The name
                                       				  or number for the department or subdivision of an organization to which the
                                       				  contact belongs.

Callers
                                       				  who reach a voice-enabled directory handler can narrow down their search for a
                                       				  contact by saying the name and department of the contact if this field is
                                       				  defined for the contact. (ListInDirectory must also be set to 1 for the contact
                                       				  to be reachable via directory handlers.)

Any
                                       				  combination of ASCII or Unicode characters, up to a maximum of 64 characters.

## Required and Optional CSV Fields
                        	 for Distribution Lists

Alias

The unique
                                       				  text name for the distribution list.

Any
                                       				  combination of ASCII or unicode alphanumeric characters, periods, commas,
                                       				  spaces, and the special characters `, ~, !, @, #, $, %, ^, &, -, _, ', up
                                       				  to a maximum of 64 characters.

Display Name

The name of
                                       				  the distribution list.

AltNames

An alternate
                                       				  version of the name. Unity Connection considers alternate names when users or
                                       				  contacts use voice recognition to place a call or address voice messages.

To
                                       				  create/update more than one alternate name distribution list, separate them by
                                       				  semicolons (;). If an alternate name needs to contain a semicolon, precede the
                                       				  semicolon with another semicolon to indicate to Unity Connection that the name
                                       				  contains a semicolon.

Extension

The number
                                       				  that callers dial to reach the distribution list.

Any
                                       				  combination of ASCII alphanumeric characters, up to a maximum of 40 characters.

AllowContacts

Allows
                                       				  contacts to be added as members of the distribution list.

AllowForeignMessage

Allows users
                                       				  on remote voice messaging systems that are configured as VPIM locations to send
                                       				  messages to this distribution list.

PartitionName

The name of
                                       				  the partition to which the distribution list belongs.

## Required and Optional CSV Fields
                        	 for Distribution List Members

DLAlias

The unique
                                       				  text name of the distribution list to which the member belongs.

MemberAlias

The unique
                                       				  text name of the member (a user, contact, user template, or another
                                       				  distribution list).

LocationNames

The display
                                       				  name of the location where the member is homed. By default, this is the display
                                       				  name of the local system.

## Required and
                        	 Optional CSV Fields for Unified Messaging Accounts

subscriberAlias

The alias of
                                       				  the Unity Connection user for which you want to add a unified messaging
                                       				  account. Note the following:

- When creating unified
                                             					 messaging accounts, this column is required.

- When updating and deleting
                                             					 unified messaging accounts, you should use OptionalServiceAccountID to identify
                                             					 the unified messaging accounts that you want to update or delete. You can also
                                             					 use subscriberAlias and serviceDisplayName.

serviceDisplayName

The
                                       				  descriptive name for the unified messaging service that you want to associate
                                       				  with this unified messaging account. Note the following:

- When creating unified
                                             					 messaging accounts, this column is required.

- When updating and deleting
                                             					 unified messaging accounts, you should use OptionalServiceAccountID to identify
                                             					 the unified messaging accounts that you want to update or delete. You can also
                                             					 use subscriberAlias and serviceDisplayName.

OptionalServiceAccountID

A unique
                                       				  identifier that distinguishes multiple unified messaging accounts for the same
                                       				  user. Note the following:

- When creating unified
                                             					 messaging accounts, leave this column blank.

- When updating and deleting
                                             					 unified messaging accounts, you should use OptionalServiceAccountID to identify
                                             					 the unified messaging accounts that you want to update or delete. You can also
                                             					 use subscriberAlias and serviceDisplayName.

UMEmailAddress

Exchange
                                       				  only: If you set the emailAddressUseCorp to:

- 0-Enter the Exchange email
                                             					 address that you want Unity Connection to access for unified messaging features
                                             					 for this user.

- 1-Leave this field blank.
                                             					 If you enter a value, Unity Connection ignores it.

emailAddressUseCorp

Exchange
                                       				  only: Determines which Exchange email address to access for unified messaging
                                       				  features:

- 0-Do not use the
                                             					 EmailAddress column in Table 1 , which corresponds with the Corporate Email
                                             					 Address field on the New and Edit User Basics pages. Instead, use the
                                             					 UMEmailAddress column in this table, which is associated with the Use This
                                             					 Email Address option on the New or Edit Unified Messaging Account pages.

- 1-Use the EmailAddress
                                             					 column in Table 1 , which corresponds with the Corporate Email Address field on
                                             					 the New and Edit User Basics pages.

enableCalendar

Exchange
                                       				  only: Determines whether calendar and contact functionality is enabled for this
                                       				  user:

- 0-Not enabled

- 1-Enabled

enableMeeting

Cisco
                                       				  Unified MeetingPlace only: Determines whether the MeetingPlace Scheduling and
                                       				  Joining feature is enabled for this user.

- 0-Not enabled

- 1-Enabled

If the
                                       				  feature is not enabled in the unified messaging service specified by
                                       				  serviceDisplayName, the value that you specify here, if any, is ignored.

enableMbxSynch

Exchange
                                       				  only: Determines whether the Synchronize Connection and Exchange Mailboxes
                                       				  (single inbox) feature is enabled for this user.

- 0-Not enabled

- 1-Enabled

If the
                                       				  feature is not enabled in the unified messaging service specified by
                                       				  serviceDisplayName, the value that you specify here, if any, is ignored.

isPrimaryMeetingService

Cisco
                                       				  Unified MeetingPlace only: Determines whether MeetingPlace meetings sre set up
                                       				  through the server listed in the unified messaging service specified by
                                       				  serviceDisplayName.

- 0-MeetingPlace meetings
                                             					 are set up through a different server.

- 1-MeetingPlace meetings
                                             					 are set up through the server listed in the service specified by
                                             					 serviceDisplayName.

loginType

Required
                                       				  when creating unified messaging accounts for MeetingPlace.

Required
                                       				  when creating unified messaging accounts for Exchange when all of the following
                                       				  are true:

- You are creating users.

- You want the user to be
                                             					 able to access Exchange email using text to speech.

If you
                                       				  specify a loginType of:

- 0-Unity Connection uses
                                             					 the alias to sign in to MeetingPlace.

- 1-Unity Connection signs
                                             					 in using the MeetingPlace server guest account.

- 2-Unity Connection uses
                                             					 the value specified in the userID column to sign in to MeetingPlace for this
                                             					 user. The value of the userID column corresponds with the User ID field on the
                                             					 New and Edit Unified Messaging Accounts pages.

userId

Required
                                       				  when creating unified messaging accounts for MeetingPlace.

Required
                                       				  when creating unified messaging accounts for Exchange when all of the following
                                       				  are true:

- You are creating users.

- You want the user to be
                                             					 able to access Exchange email using text to speech.

- You specify a loginType
                                             					 of 2.

| Column Heading | Creating | Updating | Deleting | Descriptions |
|---|---|---|---|---|
| Alias | Required | Required | Required | The unique
                                       				  text name for the user account. Any
                                       				  combination of ASCII or unicode alphanumeric characters, periods, commas,
                                       				  spaces, and the special characters `, ~, !, @, #, $, %, ^, &, -, _, ', up
                                       				  to a maximum of 64 characters. You should
                                       				  use only printable ASCII characters in the Alias field, because some messaging
                                       				  features do not support non-printing ASCII characters or Unicode. (The
                                       				  non-printing ASCII control characters are those below code 0x20.) For example,
                                       				  IMAP only supports user names that contain printable ASCII characters, so users
                                       				  with aliases that contain non-printing characters or unicode are unable to
                                       				  access their Connection messages via IMAP clients. In addition, the Cisco
                                       				  Object Backup and Restore Application Suite (COBRAS) is unable to back up
                                       				  messages for such users, because COBRAS uses IMAP to perform the backup. |
| Extension (Users With
                                       				  Mailbox Only) | Required | Optional | N/A | The number
                                       				  that callers dial to reach the user. The value
                                       				  must be unique among users in the partition. Any
                                       				  combination of ASCII alphanumeric characters, from 3 to 40 characters long. |
| TemplateAlias | Required | N/A | N/A | The unique
                                       				  text name for the user template to apply to the account during creation. Caution If you specify an administrator template for TemplateAlias, the
                                                				  users do not have mailboxes. | Caution | If you specify an administrator template for TemplateAlias, the
                                                				  users do not have mailboxes. |
| Caution | If you specify an administrator template for TemplateAlias, the
                                                				  users do not have mailboxes. |
| Password | Optional | Optional | N/A | The unique
                                       				  characters that the user enters to access Unity Connection web applications. Any
                                       				  combination of alphanumeric characters, and the following special characters:
                                       				  ~!@#$%^&*()-_+={}\|[]:"';<>?/\. To help
                                       				  protect Unity Connection from unauthorized access and toll fraud, enter a long,
                                       				  eight or more characters and non-trivial password. |
| PIN (Users With
                                       				  Mailbox Only) | Optional | Optional | N/A | The unique
                                       				  digits that the user enters to access voice messages by phone. Any
                                       				  combination of digits 0 through 9. To help
                                       				  protect Unity Connection from unauthorized access and toll fraud, enter a
                                       				  long-six or more digits-and non-trivial PIN. Note Whenever you update the phone PIN for multiple users through BAT
                                                   					 on Unity Connection, the PIN gets updated on Cisco Unified CM for the users if
                                                   					 the PIN synchronization feature is enabled on the Edit AXL Server page. For more
                                       				  information on PIN Synchronization, see the " PIN Synchronization between
                                          					 Unity Connection and Cisco Unified CM " section of the "User Settings"
                                       				  chapter. | Note | Whenever you update the phone PIN for multiple users through BAT
                                                   					 on Unity Connection, the PIN gets updated on Cisco Unified CM for the users if
                                                   					 the PIN synchronization feature is enabled on the Edit AXL Server page. |
| Note | Whenever you update the phone PIN for multiple users through BAT
                                                   					 on Unity Connection, the PIN gets updated on Cisco Unified CM for the users if
                                                   					 the PIN synchronization feature is enabled on the Edit AXL Server page. |
| Address | Optional | Optional | N/A | The physical
                                       				  address, such as a house number and street name where the user is located, or
                                       				  with which the user is associated. Any
                                       				  combination of ASCII or unicode characters up to a maximum of 128 characters. |
| AltFirstNames (Users With
                                       				  Mailbox Only) | Optional | Optional | N/A | An alternate
                                       				  version of the first name. Unity Connection considers alternate names when
                                       				  users and callers use voice recognition to place a call or address voice
                                       				  messages. To
                                       				  create/update more than one alternate first name per user, separate them by
                                       				  semicolons (;). If an alternate name needs to contain a semicolon, precede the
                                       				  semicolon with another semicolon to indicate to Unity Connection that the name
                                       				  contains a semicolon. Use this
                                       				  field in conjunction with the AltLastNames field to add nicknames or maiden
                                       				  names for users. You can also use alternate names to add phonetic spellings of
                                       				  hard-to-pronounce names. Alternate
                                       				  first names and alternate last names are stored as a pair in the database. When
                                       				  submitting multiple alternate names, make sure that you have the same number of
                                       				  alternate first names and alternate last names. For example,
                                       				  if you have a user named Elizabeth Brown, who is sometimes known as "Liz" and
                                       				  sometimes known by her maiden name of "Smith," you would enter the following
                                       				  AltFirstNames and AltLastNames to ensure that all four combinations are
                                       				  submitted to the database: Elizabeth; Liz; Elizabeth;
                                          					 Liz Brown; Brown; Smith; Smith |
| AltLastNames (Users With
                                       				  Mailbox Only) | Optional | Optional | N/A | An alternate
                                       				  version of the last name. Unity Connection considers alternate names when users
                                       				  and callers use voice recognition to place a call or address voice messages. To
                                       				  create/update more than one alternate last name per user, separate them by
                                       				  semicolons (;). If an alternate name needs to contain a semicolon, precede the
                                       				  semicolon with another semicolon to indicate to Unity Connection that the name
                                       				  contains a semicolon. Use this
                                       				  field in conjunction with the AltFirstNames field to add nicknames or maiden
                                       				  names for users. You can also use alternate names to add phonetic spellings of
                                       				  hard-to-pronounce names. Alternate
                                       				  first names and alternate last names are stored as a pair in the database. When
                                       				  submitting multiple alternate names, make sure that you have the same number of
                                       				  alternate first names and alternate last names. For example,
                                       				  if you have a user named Elizabeth Brown, who is sometimes known as "Liz" and
                                       				  sometimes known by her maiden name of "Smith," you would enter the following
                                       				  AltFirstNames and AltLastNames to ensure that all four combinations are
                                       				  submitted to the database: Elizabeth; Liz;
                                          					 Elizabeth; Liz Brown; Brown; Smith;
                                          					 Smith |
| AltFirstName (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | An
                                       				  alternate spelling of the user first name in an internationally recognizable
                                       				  format (i.e., ASCII only characters). The value is used by the phone interface
                                       				  to search for users and to address messages. Any
                                       				  combination of ASCII alphanumeric characters up to maximum of 64 characters. |
| AltLastName (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | An
                                       				  alternate spelling of the user first name in an internationally recognizable
                                       				  format (i.e., ASCII only characters). The value is used by the phone interface
                                       				  to search for users and to address messages. Any
                                       				  combination of ASCII alphanumeric characters up to maximum of 64 characters. |
| BillingId | Optional | Optional | N/A | Organization-specific information about the user, such as
                                       				  accounting information, department names, or project codes. The information can
                                       				  be included in user reports. Any
                                       				  combination of digits from 0 through 9 up to a maximum of 32 digits. |
| Building | Optional | Optional | N/A | The name
                                       				  of the building where the user is based. Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters. |
| City | Optional | Optional | N/A | The name
                                       				  of a locality, such as a city or other geographic region where the user is
                                       				  located, or with which the user is associated. Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters. |
| Country | Optional | Optional | N/A | The two
                                       				  letter ISO 3166-1 country code where the user is located, or with which the
                                       				  user is associated. Two ASCII
                                       				  lower or upper case alpha characters. |
| Department | Optional | Optional | N/A | The name
                                       				  or number for the department or sub division of an organization to which the
                                       				  user belongs. Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters. |
| DisplayName | Optional | Optional | N/A | The user
                                       				  name that appears on the administration and user interfaces. If
                                       				  Displayname is empty and both Firstname, Lastname are present, then Displayname
                                       				  would be combination of "Firstname Lastname", else Displayname would be Alias. Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters. |
| DisplayName (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The user
                                       				  name that appears on the administration and user interfaces. If
                                       				  Displayname is empty and both Firstname, Lastname are present, then Displayname
                                       				  would be combination of "Firstname Lastname", else Displayname would be Alias. Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters. |
| EmailAddress | Optional | Optional | N/A | The email
                                       				  address of the user. This corresponds to the Corporate Email Address field in
                                       				  Cisco Unity Connection Administration. Note The
                                                				  field is only for directory information purposes. Unity Connection does not use
                                                				  the address to deliver incoming messages. Any
                                       				  combination of ASCII alphanumeric characters, and the special characters
                                       				  hyphen, underscore, period and at sign ("@"), up to a maximum of 320
                                       				  characters. | Note | The
                                                				  field is only for directory information purposes. Unity Connection does not use
                                                				  the address to deliver incoming messages. |
| Note | The
                                                				  field is only for directory information purposes. Unity Connection does not use
                                                				  the address to deliver incoming messages. |
| MailName (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Name used
                                       				  to construct part of SMTP address before the @ sign. A name is
                                       				  needed for unicode aliases that cannot be converted into a valid SMTP
                                       				  addresses. |
| EmployeeId | Optional | Optional | N/A | The
                                       				  numeric or alphanumeric identifier assigned to a user, typically based on order
                                       				  of hire or association with an organization. Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters. |
| EnhancedSecurityAlias | Optional | Optional | N/A | The unique
                                       				  text name used to identify and authenticate the user with an RSA SecurID
                                       				  security system. Any
                                       				  combination of ASCII or unicode characters up to a maximum of 50 characters. |
| FirstName | Optional | Optional | N/A | The user
                                       				  first name. Any
                                       				  combination of ANSI or Unicode alphanumeric characters, periods, commas,
                                       				  spaces, and the special characters `, ~, !, @, #, $, %, ^, &, -, _, ', up
                                       				  to a maximum of 64 characters. |
| Initials | Optional | Optional | N/A | The
                                       				  initials of part or all of the user name. Any
                                       				  combination of ANSI or unicode alphanumeric characters, periods, commas,
                                       				  spaces, and the special characters `, ~, !, @, #, $, %, ^, &, -, _, ', up
                                       				  to a maximum of 6 characters. |
| Language | Optional | Optional | N/A | The preferred language of the user. Use the Windows language code, such as 1033 for U.S. English. For a list of supported languages and the corresponding language
                                       codes, see the "Numeric and Alphabetic Codes for Supported Languages" section in the System Requirements for Cisco Unity Connection
                                       15 at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/requirements/b_15cucsysreqs.html . |
| LastName | Optional | Optional | N/A | The user
                                       				  last name. Any
                                       				  combination of ANSI or unicode alphanumeric characters, periods, commas,
                                       				  spaces, and the special characters `, ~, !, @, #, $, %, ^, &, -, _, ', up
                                       				  to a maximum of 64 characters. |
| Manager | Optional | Optional | N/A | The name
                                       				  of the manager or supervisor of the user. Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters. |
| PostalCode | Optional | Optional | N/A | For users
                                       				  located in the United States, the zip code where the user is located, or with
                                       				  which the user is associated. For users located in Canada, Mexico, and other
                                       				  countries, the postal code where the user is located, or with which the user is
                                       				  associated. Any
                                       				  combination of ASCII or unicode characters up to a maximum of 40 characters. |
| State | Optional | Optional | N/A | The full
                                       				  name of the state or province where the user is located, or with which the user
                                       				  is associated. Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters. |
| TimeZone | Optional | Optional | N/A | The time
                                       				  zone with which the user account is associated. |
| Title | Optional | Optional | N/A | The
                                       				  position or function of the user within the organization, for example "Vice
                                       				  President." Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters. |
| COSDisplayName (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The unique
                                       				  text name that is displayed on the user interfaces for the class of service
                                       				  (COS) with which the user account is associated. Any
                                       				  combination of ASCII or Unicode characters, up to a maximum of 64 characters. |
| ClientMatterCode (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The
                                       				  required Client Matter Code (CMC) to transmit to Cisco Unified Communications
                                       				  Manager (CM), if applicable, when the user makes an outbound call. CMCs are
                                       				  typically used to enable the system to track calls for account or billing
                                       				  purposes. The value
                                       				  is used only if the system is using Cisco Unified CM and if the version of
                                       				  Cisco Unified CM is 4.1 and later. Whether
                                       				  the CMC is transmitted depends on the setting for outbound calls. The user CMC
                                       				  is used only if the outbound call does not have its own CMC. The code
                                       				  length can be from 1 through 40 characters. |
| TransferType (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | (Applicable only to the Alternate transfer rule.) Determines the
                                       				  way in which Unity Connection transfers calls from the automated attendant or a
                                       				  directory handler to the user phone for the Alternate transfer rule: 0-supervised 1-unsupervised (also
                                             					 called a "Release to Switch" transfer) |
| TransferRings (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | (Applicable only to the Alternate transfer rule.) Determines the
                                       				  number of times the user extension rings before Unity Connection considers the
                                       				  call unanswered ("ring-no-answer") and plays the applicable greeting. This
                                       				  setting is applicable only when the TransferType is configured for a supervised
                                       				  transfer. An
                                       				  integer value from 2 through 100. |
| TransferExtension (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | (Applicable only to the Alternate transfer rule.) The phone
                                    				number that Unity Connection transfers calls to if TransferAction is set to 1. |
| TransferAction (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | (Applicable only to the Alternate transfer rule.) Determines
                                       				  whether Unity Connection transfers the incoming calls for the user to the user
                                       				  greeting or to the extension specified in TransferExtension: 0-Transfer to the
                                             					 greeting. 1-Transfer to
                                             					 TransferExtension. |
| RnaAction (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | (Applicable only to the Alternate transfer rule.) This setting
                                       				  is applicable only when the TransferType is configured for a supervised
                                       				  transfer. Determines whether Unity Connection transfers the call to the
                                       				  applicable greeting or releases the call to the phone system when a call is
                                       				  unanswered ("ring-no-answer"): 0-Release the call to
                                             					 the phone system. 1-After the number of
                                             					 rings specified in the TransferRings field, transfer the call to the
                                             					 appropriate greeting. |
| StandardTransferType (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | (Applicable only to the Standard transfer rule.) Determines the
                                       				  way in which Unity Connection transfers calls from the automated attendant or a
                                       				  directory handler to the user phone for the standard (default) transfer rule: 0-supervised 1-unsupervised (also
                                             					 called a "Release to Switch" transfer) |
| StandardTransferRings (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | (Applicable only to the Standard transfer rule.) Determines the
                                       				  number of times the user extension rings before Unity Connection considers the
                                       				  call unanswered ("ring-no-answer") and plays the applicable greeting. This
                                       				  setting is applicable only when the StandardTransferType is configured for a
                                       				  supervised transfer. An
                                       				  integer value from 2 through 100. |
| StandardTransferExtension (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | (Applicable only to the Standard transfer rule.) The phone
                                    				number that Unity Connection transfers calls to if StandardTransferAction is
                                    				set to 1. |
| StandardTransferAction | Optional | Optional | N/A | (Applicable only to the Standard transfer rule.) Determines
                                       				  whether Unity Connection transfers the incoming calls for the user to the user
                                       				  greeting or to the extension specified in StandardTransferExtension: 0-Transfer to the
                                             					 greeting. 1-Transfer to
                                             					 StandardTransferExtension. |
| StandardRnaAction (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | (Applicable only to the Standard transfer rule.) This setting is
                                       				  applicable only when the StandardTransferType is configured for a supervised
                                       				  transfer. Determines whether Unity Connection transfers the call to the
                                       				  applicable greeting or releases the call to the phone system when a call is
                                       				  unanswered ("ring-no-answer"): 0-Release the call to
                                             					 the phone system. 1-After the number of
                                             					 rings specified in the StandardTransferRings field, transfer the call to the
                                             					 appropriate greeting. |
| ClosedTransferType (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | (Applicable only to the Closed transfer rule.) Determines the
                                       				  way in which Unity Connection transfers calls from the automated attendant or a
                                       				  directory handler to the user phone for the Closed transfer rule: 0-supervised 1-unsupervised (also
                                             					 called a "Release to Switch" transfer) |
| ClosedTransferRings (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | (Applicable only to the Closed transfer rule.) Determines the
                                       				  number of times the user extension rings before Unity Connection considers the
                                       				  call unanswered ("ring-no-answer") and plays the applicable greeting. This
                                       				  setting is applicable only when the ClosedTransferType is configured for a
                                       				  supervised transfer. An
                                       				  integer value from 2 through 100. |
| ClosedTransferExtension (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | (Applicable only to the Closed transfer rule.) The phone number
                                    				that Unity Connection transfers calls to if ClosedTransferAction is set to 1. |
| ClosedTransferAction (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | (Applicable only to the Closed transfer rule.) Determines
                                       				  whether Cisco Unity Connection transfers the incoming calls for the user to the
                                       				  user greeting or to the extension specified in ClosedTransferExtension: 0-Transfer to the
                                             					 greeting. 1-Transfer to
                                             					 ClosedTransferExtension. |
| ClosedRnaAction (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | (Applicable only to the Closed transfer rule.) This setting is
                                       				  applicable only when the StandardTransferType is configured for a supervised
                                       				  transfer. Determines whether Unity Connection transfers the call to the
                                       				  applicable greeting or releases the call to the phone system when a call is
                                       				  unanswered ("ring-no-answer"): 0-Release the call to
                                             					 the phone system. 1-After the number of
                                             					 rings specified in the ClosedTransferRings field, transfer the call to the
                                             					 appropriate greeting. |
| MWIExtension (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The phone
                                       				  number (extension) of the default message waiting indicator (MWI) to light when
                                       				  callers leave messages for the user. If no
                                       				  value is provided, Unity Connection uses the number of the primary extension. |
| MWIMediaSwitchDisplay Name (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The text
                                       				  name displayed on the system administration interface of the phone system used
                                       				  to turn message waiting indicators on and off for the phone number specified in
                                       				  the MWIExtension column. If no
                                       				  value is provided, Unity Connection uses the phone system specified in the
                                       				  MediaSwitchDisplayName column. |
| MaxMsgLen (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The
                                       				  maximum duration (in seconds) for recording a message from an outside
                                       				  (unidentified) caller. The
                                       				  length specified can be from 1 through 1,200 seconds. |
| Play After
                                       				  Message Recording (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Indicates
                                       				  whether Unity Connection plays a recording to the callers after a message has
                                       				  been sent: 0-Do Not Play Recording.
                                             					 Select this setting to disable the feature. After a message is sent, users do
                                             					 not hear any recording. 1-System Default
                                             					 Recording. After a message is sent, users hear the default system recording. 2-Play Recording. After
                                             					 a message is sent, users hear the cutomized recording. Note By
                                                				  Default the System Default Recording option is selected. | Note | By
                                                				  Default the System Default Recording option is selected. |
| Note | By
                                                				  Default the System Default Recording option is selected. |
| PlayPostGreetingRecording (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Indicates
                                       				  whether Unity Connection plays a recording to callers before allowing them to
                                       				  leave a message for the user. You can also indicate whether all callers hear
                                       				  the recording or only unidentified callers: 0-Do Not Play Recording.
                                             					 Select this setting to disable the feature. Before they leave a message,
                                             					 callers hear only the user greeting. 1-Play Recording to All
                                             					 Callers. Before they leave a message, users and outside callers hear the user
                                             					 or call handler greeting and then the recording. 2-Play Recording Only to
                                             					 Unidentified Callers. Before they leave a message, outside callers hear the
                                             					 user greeting and then the post-greeting recording. Likewise, users who call
                                             					 from a phone that is not associated with their account and do not sign in to
                                             					 Unity Connection hear the post-greeting recording. |
| PostGreetingRecordingDisplayName (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The
                                       				  display name of the post-greeting recording that plays after the greeting for
                                       				  this user. |
| ForcedAuthoizationCode (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The
                                       				  required forced-authorization code (FACs) to transmit to Cisco Unified
                                       				  Communications Manager, if applicable, when the user makes an outbound call. Your
                                       				  organization may use FACs to prevent toll fraud. For example, users may have to
                                       				  provide FACs to place long-distance calls. The value
                                       				  is used only if the system is using Cisco Unified CM and its version is 4.1 and
                                       				  later. The code
                                       				  length can be from 1 to 40 characters. |
| ListInDirectory (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Determines
                                       				  whether the user is included in the phone directory for outside callers: 0-Not included in the
                                             					 directory 1-Included in the
                                             					 directory |
| CreateSmtpProxyFromCorp (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Determines
                                       				  whether Unity Connection uses the value in the EmailAddress column (Corporate
                                       				  Email Address field in Cisco Unity Connection Administration) to automatically
                                       				  create a new SMTP proxy address, so that IMAP messages to or from this email
                                       				  address can be properly identified by Unity Connection as belonging to this
                                       				  user. If you uncheck it, no such SMTP proxy address is automatically created. 0-SMTP proxy address is
                                             					 not automatically created. 1-SMTP proxy address is
                                             					 automatically created using the Corporate Email Address field. |
| MediaSwitchDisplayName (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The text
                                       				  name displayed on the system administration interface of the phone system used
                                       				  for Telephone Record and Playback (TRAP) sessions and to turn message waiting
                                       				  indicators on and off. Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters. |
| PhoneNumber_HomePhone (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The user
                                       				  home phone number. Any
                                       				  combination of the digits 0-9, T, t, commas, hashes (#), and asterisks (*), up
                                       				  to a maximum of 38 characters. |
| Active_HomePhone (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Whether
                                       				  the user home phone device is enabled: 0-disabled 1-enabled |
| DisplayName_HomePhone (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The text
                                       				  name for the user home phone displayed on the Unity Connection interfaces. Any
                                       				  combination of ASCII or Unicode characters, up to a maximum of 64 characters. |
| PhoneNumber_WorkPhone (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The user
                                       				  work phone number. Any
                                       				  combination of the digits 0-9, T, t, commas, hashes (#), and asterisks (*), up
                                       				  to a maximum of 38 characters. |
| Active_WorkPhone (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Whether
                                       				  the user work phone device is enabled: 0-disabled 1-enabled |
| DisplayName_WorkPhone (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The text
                                       				  name for the user work phone displayed on the Unity Connection interfaces. Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters. |
| PhoneNumber_MobilePhone (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The user
                                       				  mobile phone number. Any
                                       				  combination of the digits 0-9, T, t, commas, hashes (#), and asterisks (*), up
                                       				  to a maximum of 38 characters. |
| Active_MobilePhone (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Whether
                                       				  the user mobile phone device is enabled: 0-disabled 1-enabled |
| DisplayName_MobilePhone (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The text
                                       				  name for the user mobile phone displayed on the Unity Connection interfaces. Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters. |
| PhoneNumber_Pager (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The user
                                       				  pager number. Any
                                       				  combination of the digits 0-9, T, t, commas, hashes (#), and asterisks (*), up
                                       				  to a maximum of 38 characters. |
| AfterDialDigits_Pager (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Digits to
                                       				  send to the pager. This is referred to in Unity Connection Administration as
                                       				  "Extra Digits." For numeric pagers, the field holds numeric text to send to the
                                       				  pager; for text pagers, the field is blank. The
                                       				  maximum length is 32 digits. |
| Active_Pager (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Whether
                                       				  the user pager device is enabled: 0-disabled 1-enabled |
| DisplayName_Pager (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The text
                                       				  name for the user pager displayed on the Unity Connection interfaces. Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters. |
| PhoneNumber_TextPager1 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | This phone
                                       				  number is entered in the From field on the default SMTP device for the user. Any
                                       				  combination of ASCII only alphanumeric characters, hyphens, underscores,
                                       				  periods, at signs ("@"), commas and hashes (#), up to a maximum of 40
                                       				  characters. |
| SmtpAddress_TextPager1 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Message notifications for the user are sent to this SMTP
                                    				address. Note The
                                                				  SMTP address cannot include non-ASCII characters. | Note | The
                                                				  SMTP address cannot include non-ASCII characters. |
| Note | The
                                                				  SMTP address cannot include non-ASCII characters. |
| Active_TextPager1 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Whether
                                       				  the user text pager device is enabled: 0-disabled 1-enabled |
| DisplayName_TextPager1 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The text
                                       				  name for the user text pager displayed on the Unity Connection interfaces. Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters. |
| Extension_Alt1 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The first
                                       				  alternate extension for the user. The value
                                       				  must be unique in the partition. Any
                                       				  combination of ASCII alphanumeric characters, from 1 to 40 characters long. |
| Extension_Alt1_Partition (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The text
                                       				  name of the partition to which the first alternate extension belongs. |
| Extension_Alt2 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The second
                                       				  alternate extension for the user. The value
                                       				  must be unique in the partition. Any
                                       				  combination of ASCII alphanumeric characters, from 1 to 40 characters long. |
| Extension_Alt2_Partition (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The text
                                       				  name of the partition to which the second alternate extension belongs. |
| Extension_Alt3 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The third
                                       				  alternate extension for the user. The value
                                       				  must be unique in the partition. Any
                                       				  combination of ASCII alphanumeric characters, from 1 to 40 characters long. |
| Extension_Alt3_Partition (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The text
                                       				  name of the partition to which the third alternate extension belongs. |
| Extension_Alt4 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The fourth
                                       				  alternate extension for the user. The value
                                       				  must be unique in the partition. Any
                                       				  combination of ASCII alphanumeric characters, from 1 to 40 characters long. |
| Extension_Alt4_Partition (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The text
                                       				  name of the partition to which the fourth alternate extension belongs. |
| Extension_Alt5 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The fifth
                                       				  alternate extension for the user. The value
                                       				  must be unique in the partition. Any
                                       				  combination of ASCII alphanumeric characters, from 1 to 40 characters long. |
| Extension_Alt5_Partition (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The text
                                       				  name of the partition to which the fifth alternate extension belongs. |
| Extension_Alt6 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The sixth
                                       				  alternate extension for the user. The value
                                       				  must be unique in the partition. Any
                                       				  combination of ASCII alphanumeric characters, from 1 to 40 characters long. |
| Extension_Alt6_Partition (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The text
                                       				  name of the partition to which the sixth alternate extension belongs. |
| Extension_Alt7 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The
                                       				  seventh alternate extension for the user. The value
                                       				  must be unique in the partition. Any
                                       				  combination of ASCII alphanumeric characters, from 1 to 40 characters long. |
| Extension_Alt7_Partition | Optional | Optional | N/A | The text
                                       				  name of the partition to which the seventh alternate extension belongs. |
| Extension_Alt8 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The eighth
                                       				  alternate extension for the user. The value
                                       				  must be unique in the partition. Any
                                       				  combination of ASCII alphanumeric characters, from 1 to 40 characters long. |
| Extension_Alt8_Partition (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The text
                                       				  name of the partition to which the eighth alternate extension belongs. |
| Extension_Alt9 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The ninth
                                       				  alternate extension for the user. The value
                                       				  must be unique in the partition. Any
                                       				  combination of ASCII alphanumeric characters, from 1 to 40 characters long. |
| Extension_Alt9_Partition (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The text
                                       				  name of the partition to which the ninth alternate extension belongs. |
| CcmId (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The Cisco
                                       				  Unified Communications Manager user ID that is associated with the user. Any
                                       				  combination of characters except for non-printing ASCII characters, up to a
                                       				  maximum of 128 characters. |
| Exchange2010Service_Service DisplayName (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The
                                       				  display name of the Exchange 2010 external service that corresponds with the
                                       				  Exchange 2010 server that contains the Exchange 2010 mailbox for this user. To add an
                                       				  Exchange 2010 external service for a user, include values for both the
                                       				  Exchange2010Service_ServiceDisplayName and Exchange2010Service_EmailAddress
                                       				  fields in the CSV input file. To remove
                                       				  the Exchange 2010 service for a user, set at least one of either the
                                       				  Exchange2010Service_ServiceDisplayName and Exchange2010Service_EmailAddress
                                       				  fields to %null% in the CSV input file |
| Exchange2010Service_Email Address (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The
                                       				  primary email address that is associated with the Exchange mailbox that you
                                       				  want this user to be able to access. To add an
                                       				  Exchange 2010 external service for a user, include values for both the
                                       				  Exchange2010Service_ServiceDisplayName and Exchange2010Service_EmailAddress
                                       				  fields in the CSV input file |
| Exchange2010Service_UserId (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The
                                       				  Windows domain alias for the user in Exchange 2010 (useful when the setting is
                                       				  different from the user alias). |
| Exchange2010Service_User Password (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The
                                       				  Windows domain password for the user. |
| EmailAction (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Action to
                                       				  take for a voice message: 0-Reject the message 1-Accept the message 2-Relay the message 3-Accept the message and
                                             					 relay a copy |
| VoiceMailAction (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Action to
                                       				  take for a voice message: 0-Reject the message 1-Accept the message 2-Relay the message 3-Accept the message and
                                             					 relay a copy |
| FaxAction (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Action to
                                       				  take for a voice message: 0-Reject the message 1-Accept the message 2-Relay the message 3-Accept the message and
                                             					 relay a copy |
| DeliveryReceiptAction (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Action to
                                       				  take for a voice message: 0-Reject the message 1-Accept the message 2-Relay the message 3-Accept the message and
                                             					 relay a copy |
| RelayAddress (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Specifies
                                       				  the address to relay incoming message when one or more of the actions
                                       				  (EmailAction, VoicemailAction, FaxAction, DeliveryReceiptAction) is set to 2
                                       				  (Relay the message). RelayAddress is in the format of someone@somewhere or someone@somewhere.com. |
| SmtpProxyAddresses (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The full
                                       				  SMTP proxy addresses for users. To create/update more than one address per
                                       				  user, separate them by commas and surround them all with double quotes. For
                                       				  example: "someone1@somewhere.com,someone2@somewhere.com" |
| LdapCcmUserID | Optional | Optional | N/A | The value
                                       				  of the LDAP field that you mapped to the Unity Connection Alias field when you
                                       				  configured Cisco Unity Connection to integrate with an LDAP directory. See the Task List for Configuring LDAP section. This
                                       				  field is used when you create Unity Connection users by importing LDAP user
                                       				  data and when you integrate existing Unity Connection users with LDAP users. |
| CorporatePhoneNumber (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The phone
                                       				  number of the user. Note that
                                       				  the field is only for directory information purposes. Cisco Unity Connection
                                       				  does not use the phone number to route calls. |
| DisplayName_HTML1 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | A
                                       				  descriptive name for the notification device. This field is required if you
                                       				  want to create an HTML notification device. |
| Active_HTML1 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Enables
                                       				  the HTML notification device. |
| callback_HTML1 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The phone
                                       				  number that the user use to play and record voice message. |
| disableMobPCA_HTML1 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Disallow
                                       				  the users to change the mobile number from Cisco PCA and Mini Web inbox for
                                       				  HTML notification. |
| disableTemplatePCA_HTML1 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Disallow
                                       				  the users to change the notification template from PCA. |
| SmtpAddress_HTML1 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The email
                                       				  address of the user text-compatible mobile phone, or another email account
                                       				  (such as a home email address) on which the user receives the HTML
                                       				  notification. Up to 128 characters can be entered in this field. SmtpAddress_HTML1 column is mandatory if Active_HTML1 column is set to 1. |
| templateName_HTML1 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | A default
                                       				  or a customized template name for HTML notification device. |
| DisplayName_HTML2 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | A
                                       				  descriptive name for the notification device. This field is required if you
                                       				  want to create an HTML Missed Call notification device. |
| Active_HTML2 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Enables
                                       				  the HTML Missed Call notification device. |
| callback_HTML2 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The phone
                                       				  number that the user use to view the missed calls. |
| disableMobPCA_HTML2 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Disallow
                                       				  the users to change the mobile number from Cisco PCA and Mini Web inbox for
                                       				  HTML Missed Call notification. |
| disableTemplatePCA_HTML2 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Disallow
                                       				  the users to change the notification template from PCA. This field is
                                       				  applicable for HTML Missed Call notification template. |
| SmtpAddress_HTML2 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The email
                                       				  address of the user text-compatible mobile phone, or another email account
                                       				  (such as a home email address) on which the user receives the HTML Missed Call
                                       				  notification. Up to 128 characters can be entered in this field. SmtpAddress_HTML2 column is mandatory if Active_HTML2 column is set to 1. |
| templateName_HTML2 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | A default
                                       				  or a customized template name for HTML Missed Call notification device. |
| DisplayName_HTML3 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | A
                                       				  descriptive name for the notification device. This field is required if you
                                       				  want to create an HTML Scheduled Summary notification device. |
| Active_HTML3 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Enables
                                       				  the HTML Scheduled Summary notification device. |
| callback_HTML3 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The phone
                                       				  number that the user use to play the voice messages received in Summary
                                       				  notification. |
| disableMobPCA_HTML3 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Disallow
                                       				  the users to change the mobile number from Cisco PCA and Mini Web inbox for
                                       				  HTML Scheduled Summary notification. |
| disableTemplatePCA_HTML3 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Disallow
                                       				  the users to change the notification template from PCA. This field is
                                       				  applicable for HTML Scheduled Summary notification template. |
| SmtpAddress_HTML3 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | The email
                                       				  address of the user text-compatible mobile phone, or another email account
                                       				  (such as a home email address) on which the user receives the Summary
                                       				  notification of the voice messages. Up to 128 characters can be entered in this
                                       				  field. SmtpAddress_HTML3 column is mandatory if Active_HTML3 column is set to 1. |
| templateName_HTML3 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | A default
                                       				  or a customized template name for HTML Scheduled Summary notification device. |
| DisplayName_HTML3 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | A
                                       				  descriptive name for the notification device. This field is required if you
                                       				  want to create an HTML Scheduled Summary notification device. |
| Active_HTML3 (Users
                                       				  With Mailbox Only) | Optional | Optional | N/A | Enables
                                       				  the HTML Scheduled Summary notification device. |

| Caution | If you specify an administrator template for TemplateAlias, the
                                                				  users do not have mailboxes. |
|---|---|

| Note | Whenever you update the phone PIN for multiple users through BAT
                                                   					 on Unity Connection, the PIN gets updated on Cisco Unified CM for the users if
                                                   					 the PIN synchronization feature is enabled on the Edit AXL Server page. |
|---|---|

| Note | The
                                                				  field is only for directory information purposes. Unity Connection does not use
                                                				  the address to deliver incoming messages. |
|---|---|

| Note | By
                                                				  Default the System Default Recording option is selected. |
|---|---|

| Note | The
                                                				  SMTP address cannot include non-ASCII characters. |
|---|---|

| Column Heading | Creating | Updating | Deleting | Descriptions |
|---|---|---|---|---|
| Alias | Required | Required | Required | The unique
                                       				  text name for the contact. Any
                                       				  combination of ASCII or unicode alphanumeric characters, periods, commas,
                                       				  spaces, and the special characters `, ~, !, @, #, $, %, ^, &, -, _, ', up
                                       				  to a maximum of 64 characters. |
| Extension | Required | Optional | N/A | The number
                                       				  that callers dial to reach the contact. The value
                                       				  must be unique among users and contacts in the partition. Any
                                       				  combination of ASCII alphanumeric characters up to a maximum of 40 characters. |
| ContactTemplateAlias | Optional | N/A | N/A | The unique
                                       				  text name for the contact template to apply to the contact during creation. |
| AltFirstNames | Optional | Optional | N/A | An
                                       				  alternate version of the first name. Unity Connection considers alternate names
                                       				  when users and callers use voice recognition to place a call or address voice
                                       				  messages. To
                                       				  create/update more than one alternate first name per contact, separate them by
                                       				  semicolons (;). If an alternate name needs to contain a semicolon, precede the
                                       				  semicolon with another semicolon to indicate to Unity Connection that the name
                                       				  contains a semicolon. Use this
                                       				  field in conjunction with the AltLastNames field to add nicknames or maiden
                                       				  names for users. You can also use alternate names to add phonetic spellings of
                                       				  hard-to-pronounce names. Alternate
                                       				  first names and alternate last names are stored as a pair in the database. When
                                       				  submitting multiple alternate names, make sure that you have the same number of
                                       				  alternate first names and alternate last names. For
                                       				  example, if you have a contact named Elizabeth Brown, who is sometimes known as
                                       				  "Liz" and sometimes known by her maiden name of "Smith," you would enter the
                                       				  following AltFirstNames and AltLastNames to ensure that all four combinations
                                       				  are submitted to the database: Elizabeth; Liz; Elizabeth;
                                             					 Liz Brown; Brown; Smith; Smith |
| AltLastNames | Optional | Optional | N/A | An alternate
                                       				  version of the last name. Unity Connection considers alternate names when users
                                       				  and callers use voice recognition to place a call or address voice messages. To
                                       				  create/update more than one alternate last name per contact, separate them by
                                       				  semicolons (;). If an alternate name needs to contain a semicolon, precede the
                                       				  semicolon with another semicolon to indicate to Unity Connection that the name
                                       				  contains a semicolon. Use this
                                       				  field in conjunction with the AltFirstNames field to add nicknames or maiden
                                       				  names for users. You can also use alternate names to add phonetic spellings of
                                       				  hard-to-pronounce names. Alternate
                                       				  first names and alternate last names are stored as a pair in the database. When
                                       				  submitting multiple alternate names, make sure that you have the same number of
                                       				  alternate first names and alternate last names. For
                                       				  example, if you have a contact named Elizabeth Brown, who is sometimes known as
                                       				  "Liz" and sometimes known by her maiden name of "Smith," you would enter the
                                       				  following AltFirstNames and AltLastNames to ensure that all four combinations
                                       				  are submitted to the database: Elizabeth; Liz; Elizabeth;
                                             					 Liz Brown; Brown; Smith; Smith |
| AltFirstName | Optional | Optional | N/A | An alternate
                                       				  spelling of the contact first name in an internationally recognizable format
                                       				  (ASCII characters). The value is used by the phone interface to search for
                                       				  users and to address messages. Any
                                       				  combination of ASCII alphanumeric characters up to maximum of 64 characters. |
| AltLastName | Optional | Optional | N/A | An alternate
                                       				  spelling of the contact last name in an internationally recognizable format
                                       				  (ASCII characters). The value is used by the phone interface to search for
                                       				  users and to address messages. Any
                                       				  combination of ASCII alphanumeric characters up to maximum of 64 characters. |
| DisplayName | Optional | Optional | N/A | The contact
                                       				  name that appears on the administration and user interfaces. If no value
                                       				  is provided, the value is set to the Alias. Any
                                       				  combination of ASCII or unicode characters up to a maximum of 64 characters. |
| FirstName | Optional | Optional | N/A | The
                                       				  contact first name. Any
                                       				  combination of ANSI or unicode alphanumeric characters, periods, commas,
                                       				  spaces, and the special characters `, ~, !, @, #, $, %, ^, &, -, _, ', up
                                       				  to a maximum of 64 characters. |
| LastName | Optional | Optional | N/A | The
                                       				  contact last name. Any
                                       				  combination of ANSI or unicode alphanumeric characters, periods, commas,
                                       				  spaces, and the special characters `, ~, !, @, #, $, %, ^, &, -, _, ', up
                                       				  to a maximum of 64 characters. |
| ListInDirectory | Optional | Optional | N/A | Determines
                                       				  whether the contact is included in the phone directory for outside callers: 0-Not included in the
                                             					 directory 1-Included in the
                                             					 directory |
| RemoteMailAddress | Optional | Optional | N/A | For VPIM
                                       				  contacts, enter the mailbox number of the VPIM contact on the remote voice
                                       				  messaging system. The
                                       				  maximum length is 256 characters. |
| TransferEnabled | Optional | Optional | N/A | Determines
                                       				  whether Unity Connection transfers calls from the automated attendant or a
                                       				  directory handler to the phone number that is specified in the
                                       				  TransferExtension field. 0-Do not transfer calls.
                                             					 Unity Connection takes a message and sends it to the remote mailbox for the
                                             					 VPIM contact instead. 1-Transfer incoming
                                             					 calls to TransferExtension. |
| TransferExtension | Optional | Optional | N/A | The
                                       				  extension or phone number to which Unity Connection transfers calls when
                                       				  TransferEnabled is set to 1. When
                                       				  entering a phone number, include any additional numbers necessary to dial
                                       				  outside calls (for example, 9) and for long-distance dialing (for example, 1). Any
                                       				  combination of numeric digits, commas, and the special characters # and *, up
                                       				  to a maximum of 40 characters. |
| TransferRings | Optional | Optional | N/A | Determines
                                       				  the number of times the extension of the contact rings before Unity Connection
                                       				  considers the call unanswered ("ring-no-answer") and plays the applicable
                                       				  greeting. An
                                       				  integer value from 2 through 100. |
| TransferType | Optional | Optional | N/A | Determines
                                       				  the way in which Unity Connection transfers calls from the automated attendant
                                       				  or a directory handler to the contact phone for the standard (default) transfer
                                       				  rule: 0-supervised 1-unsupervised (also
                                             					 called a "Release to Switch" transfer) |
| DeliveryLocation DisplayName | Optional | Optional | N/A | For VPIM
                                       				  contacts, the VPIM delivery location on which the contact mailbox resides. Use
                                       				  the display name of the VPIM location as it is listed in Cisco Unity Connection
                                       				  Administration. Any
                                       				  combination of ASCII or Unicode characters (except nonprinting ASCII
                                       				  characters), up to maximum of 64 characters. |
| PartitionDisplayName | Optional | Optional | N/A | The
                                       				  display name of the partition to which the contact belongs. |
| SmtpProxyAddresses | Optional | Optional | N/A | The full
                                       				  SMTP proxy addresses for contacts. To create/update more than one address per
                                       				  user, separate them by commas and surround them all with double quotes. For
                                       				  example: "someone1@somewhere.com,someone2@somewhere.com" |
| DialableWorkPhone | Optional | Optional | N/A | A phone
                                       				  number that voice recognition users can use to call the contact. Include any
                                       				  additional numbers necessary to dial outside calls (for example, 9) and for
                                       				  long-distance dialing (for example, 1). Any
                                       				  combination of numeric digits, commas, and the special characters # and *, from
                                       				  1 to 255 characters long. |
| DialableHomePhone | Optional | Optional | N/A | A phone
                                       				  number that voice recognition users can use to call the contact. Include any
                                       				  additional numbers necessary to dial outside calls (for example, 9) and for
                                       				  long-distance dialing (for example, 1). Any
                                       				  combination of numeric digits, commas, and the special characters #, and *,
                                       				  from 1 to 255 characters long. |
| DialableMobilePhone | Optional | Optional | N/A | A phone
                                       				  number that voice recognition users can use to call the contact. Include any
                                       				  additional numbers necessary to dial outside calls (for example, 9) and for
                                       				  long-distance dialing (for example, 1). Any
                                       				  combination of numeric digits, commas, and the special characters #, and *,
                                       				  from 1 to 255 characters long. |
| City | Optional | Optional | N/A | The name
                                       				  of a locality including a city, county or other geographic region where the
                                       				  contact is located, or with which the contact is associated. Callers
                                       				  who reach a voice-enabled directory handler can narrow down their search for a
                                       				  contact by saying the name and city of the contact if this field is defined for
                                       				  the contact. (ListInDirectory must also be set to 1 for the contact to be
                                       				  reachable via directory handlers.) Any
                                       				  combination of ASCII or Unicode characters, up to a maximum of 64 characters. |
| Department | Optional | Optional | N/A | The name
                                       				  or number for the department or subdivision of an organization to which the
                                       				  contact belongs. Callers
                                       				  who reach a voice-enabled directory handler can narrow down their search for a
                                       				  contact by saying the name and department of the contact if this field is
                                       				  defined for the contact. (ListInDirectory must also be set to 1 for the contact
                                       				  to be reachable via directory handlers.) Any
                                       				  combination of ASCII or Unicode characters, up to a maximum of 64 characters. |

| Column Heading | Creating | Updating | Deleting | Descriptions |
|---|---|---|---|---|
| Alias | Required | Required | Required | The unique
                                       				  text name for the distribution list. Any
                                       				  combination of ASCII or unicode alphanumeric characters, periods, commas,
                                       				  spaces, and the special characters `, ~, !, @, #, $, %, ^, &, -, _, ', up
                                       				  to a maximum of 64 characters. |
| Display Name | Required | Optional | N/A | The name of
                                       				  the distribution list. |
| AltNames | Optional | Optional | N/A | An alternate
                                       				  version of the name. Unity Connection considers alternate names when users or
                                       				  contacts use voice recognition to place a call or address voice messages. To
                                       				  create/update more than one alternate name distribution list, separate them by
                                       				  semicolons (;). If an alternate name needs to contain a semicolon, precede the
                                       				  semicolon with another semicolon to indicate to Unity Connection that the name
                                       				  contains a semicolon. |
| Extension | Optional | Optional | N/A | The number
                                       				  that callers dial to reach the distribution list. Any
                                       				  combination of ASCII alphanumeric characters, up to a maximum of 40 characters. |
| AllowContacts | Optional | Optional | N/A | Allows
                                       				  contacts to be added as members of the distribution list. |
| AllowForeignMessage | Optional | Optional | N/A | Allows users
                                       				  on remote voice messaging systems that are configured as VPIM locations to send
                                       				  messages to this distribution list. |
| PartitionName | Optional | Optional | N/A | The name of
                                       				  the partition to which the distribution list belongs. |

| Column Heading | Creating | Deleting | Descriptions |
|---|---|---|---|
| DLAlias | Required | Required | The unique
                                       				  text name of the distribution list to which the member belongs. |
| MemberAlias | Required | Required | The unique
                                       				  text name of the member (a user, contact, user template, or another
                                       				  distribution list). |
| LocationNames | Optional | Optional | The display
                                       				  name of the location where the member is homed. By default, this is the display
                                       				  name of the local system. |

| Column Heading | Creating | Updating | Deleting | Descriptions |
|---|---|---|---|---|
| subscriberAlias | Required | Optional. See Description | Optional. See Description | The alias of
                                       				  the Unity Connection user for which you want to add a unified messaging
                                       				  account. Note the following: When creating unified
                                             					 messaging accounts, this column is required. When updating and deleting
                                             					 unified messaging accounts, you should use OptionalServiceAccountID to identify
                                             					 the unified messaging accounts that you want to update or delete. You can also
                                             					 use subscriberAlias and serviceDisplayName. |
| serviceDisplayName | Required | Optional. See Description | Optional. See Description | The
                                       				  descriptive name for the unified messaging service that you want to associate
                                       				  with this unified messaging account. Note the following: When creating unified
                                             					 messaging accounts, this column is required. When updating and deleting
                                             					 unified messaging accounts, you should use OptionalServiceAccountID to identify
                                             					 the unified messaging accounts that you want to update or delete. You can also
                                             					 use subscriberAlias and serviceDisplayName. |
| OptionalServiceAccountID | Omit | Recommended. See Description | Recommended. See Description | A unique
                                       				  identifier that distinguishes multiple unified messaging accounts for the same
                                       				  user. Note the following: When creating unified
                                             					 messaging accounts, leave this column blank. When updating and deleting
                                             					 unified messaging accounts, you should use OptionalServiceAccountID to identify
                                             					 the unified messaging accounts that you want to update or delete. You can also
                                             					 use subscriberAlias and serviceDisplayName. |
| UMEmailAddress | Optional | Optional | Optional | Exchange
                                       				  only: If you set the emailAddressUseCorp to: 0-Enter the Exchange email
                                             					 address that you want Unity Connection to access for unified messaging features
                                             					 for this user. 1-Leave this field blank.
                                             					 If you enter a value, Unity Connection ignores it. |
| emailAddressUseCorp | Optional | Optional | Optional | Exchange
                                       				  only: Determines which Exchange email address to access for unified messaging
                                       				  features: 0-Do not use the
                                             					 EmailAddress column in Table 1 , which corresponds with the Corporate Email
                                             					 Address field on the New and Edit User Basics pages. Instead, use the
                                             					 UMEmailAddress column in this table, which is associated with the Use This
                                             					 Email Address option on the New or Edit Unified Messaging Account pages. 1-Use the EmailAddress
                                             					 column in Table 1 , which corresponds with the Corporate Email Address field on
                                             					 the New and Edit User Basics pages. |
| enableCalendar | Optional | Optional | Optional | Exchange
                                       				  only: Determines whether calendar and contact functionality is enabled for this
                                       				  user: 0-Not enabled 1-Enabled |
| enableMeeting | Optional | Optional | Optional | Cisco
                                       				  Unified MeetingPlace only: Determines whether the MeetingPlace Scheduling and
                                       				  Joining feature is enabled for this user. 0-Not enabled 1-Enabled If the
                                       				  feature is not enabled in the unified messaging service specified by
                                       				  serviceDisplayName, the value that you specify here, if any, is ignored. |
| enableMbxSynch | Optional | Optional | Optional | Exchange
                                       				  only: Determines whether the Synchronize Connection and Exchange Mailboxes
                                       				  (single inbox) feature is enabled for this user. 0-Not enabled 1-Enabled If the
                                       				  feature is not enabled in the unified messaging service specified by
                                       				  serviceDisplayName, the value that you specify here, if any, is ignored. |
| isPrimaryMeetingService | Optional | Optional | Optional | Cisco
                                       				  Unified MeetingPlace only: Determines whether MeetingPlace meetings sre set up
                                       				  through the server listed in the unified messaging service specified by
                                       				  serviceDisplayName. 0-MeetingPlace meetings
                                             					 are set up through a different server. 1-MeetingPlace meetings
                                             					 are set up through the server listed in the service specified by
                                             					 serviceDisplayName. |
| loginType | See Description | Optional | Optional | Required
                                       				  when creating unified messaging accounts for MeetingPlace. Required
                                       				  when creating unified messaging accounts for Exchange when all of the following
                                       				  are true: You are creating users. You want the user to be
                                             					 able to access Exchange email using text to speech. If you
                                       				  specify a loginType of: 0-Unity Connection uses
                                             					 the alias to sign in to MeetingPlace. 1-Unity Connection signs
                                             					 in using the MeetingPlace server guest account. 2-Unity Connection uses
                                             					 the value specified in the userID column to sign in to MeetingPlace for this
                                             					 user. The value of the userID column corresponds with the User ID field on the
                                             					 New and Edit Unified Messaging Accounts pages. |
| userId | See Description | Optional | Optional | Required
                                       				  when creating unified messaging accounts for MeetingPlace. Required
                                       				  when creating unified messaging accounts for Exchange when all of the following
                                       				  are true: You are creating users. You want the user to be
                                             					 able to access Exchange email using text to speech. You specify a loginType
                                             					 of 2. |