---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-configadminguide-12-5-1-su4-cup0-b-config-and-admin-guide-1-65a8536828
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/configAdminGuide/12_5_1_su4/cup0_b_config-and-admin-guide-1251su4/cup0_b_config-and-admin-guide-1251su3_chapter_011111.html
retrieved_at: 2026-08-16T16:46:46.744795+00:00
---

Configuration and Administration of the IM and Presence Service, Release 12.5(1)SU4 to 12.5(1)SU7

# Configuration and Administration of the IM and Presence Service, Release 12.5(1)SU4 to 12.5(1)SU7

Updated: November 27, 2024

Chapter: Bulk Administration of Contact Lists

## Chapter: Bulk Administration of Contact Lists

# Bulk Administration of Contact Lists

## Bulk Administration Overview

With the IM and Presence Service Bulk Administration Tool, you can perform bulk transactions on many IM and Presence Service
                           users, including:

Rename User Contact IDs for use in the Microsoft migration process.

Export the contact lists, non-presence contact lists, and location details of users who belong to a particular node or presence
                                 redundancy group, to a CSV data file.

Non-presence contacts are contacts who do not have an IM address and can only be exported using this procedure.

You can import user contacts lists, non-presence contact lists, and user location migration details you had exported to another
                                 node or presence redundancy group in a different cluster. Prepopulate contact lists for new users or add to existing contact
                                 lists.

These features facilitate the migration of users between clusters.

## Bulk Administration Prerequisites

Before  importing your user contact lists:

Provision the users on Cisco Unified Communications Manager.

Ensure that the users are licensed on Cisco Unified Communications Manager for the IM and Presence Service.

The default contact list import rate is based on the virtual machine deployment hardware type. You can change the contact
                                          list import rate by choosing Cisco Unified CM IM and Presence Administration > System > Service Parameters > Cisco Bulk Provisioning Service . However, if you increase the default import rate, this will result in higher CPU and memory usage on IM and Presence Service.

## Bulk Administration Task Flow

Step 1

Bulk Rename User Contact IDs

Upload the CSV file and rename the contact IDs for a list of users.

Step 2

Bulk Export User Contact Lists and Non-Presence Contact Lists

Use this procedure to export your users' contact lists to a CSV file. You can then use Bulk Administration to move user contact
                                          lists to another node or cluster.

Step 3

Carry out these tasks to import your user contact lists into IM and Presence Service:

### Bulk Rename User Contact IDs

Caution

Bulk rename of contact IDs is used in the migration of users from a Microsoft server (for example Lync) to IM and Presence
                                             Service Service. See the Partitioned Intradomain Federation Guide on Cisco.com for detailed instructions on how this tool
                                             should be used as part of the user migration process. Using this tool in any other circumstances is not supported.

Upload the CSV file and rename the contact IDs for a list of users.

Step 1

Upload the CSV file with the list of contact IDs that you want to rename in all contact lists:

Go to the IM and Presence Service database publisher node.

In Cisco Unified CM IM and Presence Administration , choose Bulk Administration > Upload/Download Files. .

Click Add New .

Click Browse to locate and choose the CSV file. For more on the input file, see Bulk Rename User Contact IDs File Details .

Choose Contacts as the Target.

Choose Rename Contacts – Custom File as the Transaction Type.

Click Save to upload the file.

Step 2

In Cisco Unified CM IM and Presence Administration on the publisher node, choose Bulk Administration > Contact List > Rename Contacts .

Step 3

In the File Name field, choose the file that you uploaded.

Step 4

Choose one of the following actions:

- Click Run Immediately to execute the Bulk Administration job immediately.

- Click Run Later to schedule a time to execute the Bulk Administration job. For more information about scheduling jobs in the Bulk Administration
                                             Tool, see the Online Help in Cisco Unified CM IM and Presence Administration.

Step 5

Click Submit .

If you chose to run the job immediately, the job runs after you click Submit.

#### What to do next

Bulk Export User Contact Lists and Non-Presence Contact Lists

#### Bulk Rename User Contact IDs File Details

The file that you upload before you can run this job must be a CSV file with the following format:

<Contact ID>, <New Contact ID>

where <Contact ID> is the existing contact ID and <New Contact ID> is the new format of the contact ID.

<Contact ID> is the user's IM address as it appears on the Presence Topology User Assignment window .

The following is a sample CSV file with one entry:

```
Contact ID, New Contact ID
john.smith@example.com, jsmith@example.com
```

### Bulk Export User Contact Lists and Non-Presence Contact Lists

Use this procedure to export your users' contact lists to a CSV file. You can then use Bulk Administration to move user contact
                                 lists to another node or cluster.

Contact Lists—This list consists of IM and Presence contacts. Contacts whom do not have an IM address will not be exported
                                       (you must export a non-presence contact list).

Non-presence Contact Lists—This list consists of contacts whom do not have an IM address.

Step 1

From Cisco Unified CM IM and Presence Administration, do either of the following:

- To export Contact Lists, choose Bulk Administration > Contact List > Export Contact List

- To export Non-presence Contact Lists, choose Bulk Administration > Non-presence Contact List > Export Non-presence Contact List and skip the next step.

Step 2

Contact Lists only. Select the users for whom you will export contact lists:

Under Export Contact List Options , choose the category of users for whom you will export contact lists. The default is to export contact lists for all users.

Click Find to bring up the list of users and then click Next .

Step 3

In the File Name field, enter a name for the CSV file.

Step 4

Under Job Information , configure when you want to run this job:

- Run Immediately —Check this button to export contact lists right away.

- Run Later —Check this button if you want to schedule a time for the job. With this option, you will need to use the Job Scheduler page
                                             at Bulk Administration > Job Scheduler to schedule a time for this job to run.

Step 5

Click Submit .

Step 6

After the export file is created, download the exported file:

From Cisco Unified CM IM and Presence Administration, choose Bulk Administration > Upload/Download Files .

Click Find and select the export file.

Click Download Selected and download the file to a location you can access.

#### File Details for Export Contact Lists

The following is a sample CSV file entry:

userA,example.com,userB,example.com,buddyB,General,0

BAT allows you to find and choose the users whose contact lists you want to export. The user contact lists are exported to
                                    a CSV file with the following format:

<User ID>,<User Domain>,<Contact ID>,<Contact Domain>,<Nickname>,<Group Name>,<State>

The following table describes the parameters in the export file.

Parameter

Description

User ID

The user ID of the IM and Presence Service user.

This value is the user portion of the user's IM address.

User Domain

The Presence domain of the IM and Presence Service user.

This value is the domain portion of the user's IM address.

Example 1: bjones@example.com—bjones is the user ID and example.com is the user domain.

Example 2: bjones@usa@example.com—bjones@usa is the user ID and example.com is the user domain.

Contact ID

The user ID of the contact list entry.

Contact Domain

The Presence domain of the contact list entry.

Nickname

The nickname of the contact list entry.

If the user has not specified a nickname for a contact, the Nickname parameter will be blank.

Group Name

The name of the group to which the contact list entry is to be added.

If a user’s contacts are not sorted into groups, the default group name will be specified in the Group Name field.

State

The state of the rosters, the roster database stores it in decimal format.

#### File Details for Export Non-Presence Contact Lists

The non-presence user contact lists are exported to a CSV file with the following format:

<User JID>,<Contact JID>,<Group Name>,<Content Type>,<Version>,<Info>

The following table describes the parameters in the export file:

Parameter

Description

User JID

The User JID. This is the IM address of the user.

Contact JID

The User JID of the contact list entry, if available, otherwise it is the UUID.

Group Name

The name of the group to which the contact list entry is to be added.

Content Type

The textmime type and subtype used in the info field.

Version

The content type used in the info field.

Info

The contact information of the contact list entry in vCard format.

The following is a sample CSV file entry:

```
user2@cisco.com,ce463d44-02c3-4975-a37f-d4553e3f17e1,group01,text/directory,3,BEGIN:VCARD
ADR;TYPE=WORK:ADR\;WORK:\;\;123 Dublin rd\,\;Oranmore\;Galway\;\;Ireland
EMAIL;TYPE=X-CUSTOM1;X LABEL=Custom:testuser01@test.com N:test;user;;; NICKNAME:pizzaguy01
ORG:ABC TEL;TYPE=WORK,VOICE:5323534535 TITLE:QA VERSION:3.0 END:VCARD
```

### Bulk Import Of User Contact Lists

#### Verify Maximum Contact List Size

Check the Maximum Contact List Size and Maximum Watchers settings on IM and Presence Service. The system default value is
                                    200 for Maximum Contact List Size and 200 for Maximum Watchers.

Cisco recommends that you set the Maximum Contact List Size and Maximum Watchers settings to Unlimited while importing user
                                    contact lists. Even though o exceed the maximum contact list size without losing data when importing contact lists using BAT,
                                    this step ensures that each migrated user contact list is fully imported. After all users have migrated, you can reset the
                                    Maximum Contact List Size and Maximum Watchers settings to the preferred values.

You only need to check the maximum contact list size on those clusters that contain users for whom you wish to import contacts.
                                    When you change Presence settings, the changes are applied to all nodes in the cluster; therefore you only need to change
                                    these settings on the IM and Presence database publisher node within the cluster.

##### What to do next

Upload Input File

#### Upload Input File

The following procedure describes how to upload the CSV input file using BAT for contact lists and non-presence contact lists.

##### Before you begin

Verify Maximum Contact List Size

Step 1

In Cisco Unified CM IM and Presence Administration , choose Bulk Administration > Upload/Download Files .

Step 2

Click Add New .

Step 3

Click Browse to locate and choose the CSV file.

Step 4

For the Target setting:

- If you want to upload an input file for contact lists, choose Contact Lists . For more on user contact list input files, see File Details for Import Contact Lists .

- If you want to upload an input file for non-presence contact lists, choose Non-presence Contact Lists . For more on non-presence user contact list input files, see File Details for Import Non-Presence Contact Lists .

Step 5

For the Transaction Type: Choose  as the Transaction Type.

- If you want to upload an input file for contact lists, choose Import Users’ Contacts – Custom File

- If you want to upload an input file for non-presence contact lists, choose Import Users’ Non Presence Contacts

Step 6

Click Save to upload the file.

##### What to do next

Create New Bulk Administration Job

##### File Details for Import Contact Lists

The input file must be a CSV file in the following format:

<User ID>,<User Domain>,<Contact ID>,<Contact Domain>,<Nickname>,<Group Name>,<State>

The following is a sample CSV file entry:

userA,example.com,userB,example.com,buddyB,General,0

The following table describes the parameters in the input file.

Parameter

Description

User ID

This is a mandatory parameter.

The user ID of the IM and Presence Service user. It can have a maximum 132 characters.

This value is the user portion of the user's IM address.

User Domain

This is a mandatory parameter.

The Presence domain of the IM and Presence Service user. It can have a maximum of 128 characters.

This value is the domain portion of the user's IM address.

Example 1 : bjones@example.com—bjones is the user ID and example.com is the user domain.

Example 2 : bjones@usa@example.com—bjones@usa is the user ID and example.com is the user domain.

Contact ID

This is a mandatory parameter.

The user ID of the contact list entry. It can have a maximum of 132 characters.

Contact Domain

This is a mandatory parameter.

The Presence domain of the contact list entry. The following restrictions apply to the format of the domain name:

Length must be less than or equal to 128 characters

Contains only numbers, upper- and lowercase letters, and hyphens (-)

Must not start or end with hyphen (-)

Length of label must be less than or equal to 63 characters

Top-level domain must be characters only and have at least two characters

Nickname

The nickname of the contact list entry. It can have a maximum of 255 characters.

Group Name

Group Name is a mandatory parameter.

The name of the group to which the contact list entry is to be added. It can have a maximum of 255 characters.

State

The state of the rosters, the roster database stores it in decimal format.

##### File Details for Import Non-Presence Contact Lists

The input file must be a CSV file in the following format:

<User JID>,<Contact JID>,<Group Name>,<Content Type>,<Version>,<Info>

The following is a sample CSV file entry:

```
user2@cisco.com,ce463d44-02c3-4975-a37f-d4553e3f17e1,group01,text/directory,3,BEGIN:VCARD
ADR;TYPE=WORK:ADR\;WORK:\;\;123 Dublin rd\,\;Oranmore\;Galway\;\;Ireland
EMAIL;TYPE=X-CUSTOM1;X LABEL=Custom:testuser01@test.com N:test;user;;; NICKNAME:pizzaguy01
ORG:ABC TEL;TYPE=WORK,VOICE:5323534535 TITLE:QA VERSION:3.0 END:VCARD
```

Caution

We recommend that you do not manually modify the CSV file, due to the size of the file itself and the risk of corrupting the
                                                   vCard information.

The following table describes the parameters in the input file for non-presence contacts:

Parameter

Description

User JID

The User JID. This is the IM address of the user.

Contact JID

The User JID of the contact list entry, if available, otherwise it is the UUID.

Group Name

The name of the group to which the contact list entry is to be added.

Content Type

The textmime type and subtype used in the info field.

Version

The content type used in the info field.

Info

The contact information of the contact list entry in vCard format.

#### Create New Bulk Administration Job

Create a new bulk administration job for contact lists and non-presence contact lists.

##### Before you begin

Upload Input File

Step 1

In Cisco Unified CM IM and Presence Administration :

- If you want to create a new bulk administration job for contact lists, choose Bulk Administration > Contact List > Update

- If you want to create a new bulk administration job for contact lists, choose Bulk Administration > Contact Non-presence List > Import Non-presence Contact List .

- If you want to create a new bulk administration job for user location migration, choose Bulk Administration > User Location Migration > Import User Location Details .

Step 2

From the File Name drop-down list, choose the file to import.

Step 3

In the Job Description field, enter a description for this Bulk Administration job.

Step 4

Choose one of the following:

- Click Run Immediately to execute the Bulk Administration job immediately.

- Click Run Later to schedule a time to execute the Bulk Administration job. For more information about scheduling jobs in BAT, see the Online
                                                Help in Cisco Unified CM IM and Presence Administration.

Step 5

Click Submit . If you chose to run the job immediately, the job runs after you click Submit.

##### What to do next

Check Results of Bulk Administration Job

#### Check Results of Bulk Administration Job

When the Bulk Administration job is complete, the IM and Presence Service BAT tool writes the results of the contact list
                                    import job to a log file. The log file contains the following information:

The number of contacts that were successfully imported.

The number of internal server errors that were encountered while trying to import the contacts.

The number of contacts that were not imported (ignored). The log file lists a reason for each ignored contact at the end of
                                          the log file. The following are the reasons for not importing a contact:

Invalid format - invalid row format, for example, a required field is missing or empty

Invalid contact domain - the contact domain is in an invalid format. See topics related to bulk import of user contact lists
                                                for the valid format of the contact domain

Cannot add self as a contact - you cannot import a contact for a user if the contact is the user

User’s contact list is over limit - the user has reached the maximum contact list size and no more contacts can be imported
                                                for that user

User is not assigned to local node - the user is not assigned to the local node

The number of contacts in the CSV file that were unprocessed due to an error that caused the BAT job to finish early. This
                                          error rarely occurs.

Complete the following procedure to access this log file.

##### Before you begin

Create New Bulk Administration Job

Step 1

In Cisco Unified CM IM and Presence Administration , choose Bulk Administration > Job Scheduler .

Step 2

Click Find and choose the job ID of the contact list import job.

Step 3

Click the Log File Name link to open the log.

| Note | Non-presence contacts are contacts who do not have an IM address and can only be exported using this procedure. |
|---|---|

| Note | The default contact list import rate is based on the virtual machine deployment hardware type. You can change the contact
                                          list import rate by choosing Cisco Unified CM IM and Presence Administration > System > Service Parameters > Cisco Bulk Provisioning Service . However, if you increase the default import rate, this will result in higher CPU and memory usage on IM and Presence Service. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Bulk Rename User Contact IDs | Upload the CSV file and rename the contact IDs for a list of users. |
| Step 2 | Bulk Export User Contact Lists and Non-Presence Contact Lists | Use this procedure to export your users' contact lists to a CSV file. You can then use Bulk Administration to move user contact
                                          lists to another node or cluster. |
| Step 3 | Carry out these tasks to import your user contact lists into IM and Presence Service: |  |

| Caution | Bulk rename of contact IDs is used in the migration of users from a Microsoft server (for example Lync) to IM and Presence
                                             Service Service. See the Partitioned Intradomain Federation Guide on Cisco.com for detailed instructions on how this tool
                                             should be used as part of the user migration process. Using this tool in any other circumstances is not supported. |
|---|---|

| Step 1 | Upload the CSV file with the list of contact IDs that you want to rename in all contact lists: Go to the IM and Presence Service database publisher node. In Cisco Unified CM IM and Presence Administration , choose Bulk Administration > Upload/Download Files. . Click Add New . Click Browse to locate and choose the CSV file. For more on the input file, see Bulk Rename User Contact IDs File Details . Choose Contacts as the Target. Choose Rename Contacts – Custom File as the Transaction Type. Click Save to upload the file. |
|---|---|
| Step 2 | In Cisco Unified CM IM and Presence Administration on the publisher node, choose Bulk Administration > Contact List > Rename Contacts . |
| Step 3 | In the File Name field, choose the file that you uploaded. |
| Step 4 | Choose one of the following actions: Click Run Immediately to execute the Bulk Administration job immediately. Click Run Later to schedule a time to execute the Bulk Administration job. For more information about scheduling jobs in the Bulk Administration
                                             Tool, see the Online Help in Cisco Unified CM IM and Presence Administration. |
| Step 5 | Click Submit . If you chose to run the job immediately, the job runs after you click Submit. |

| Step 1 | From Cisco Unified CM IM and Presence Administration, do either of the following: To export Contact Lists, choose Bulk Administration > Contact List > Export Contact List To export Non-presence Contact Lists, choose Bulk Administration > Non-presence Contact List > Export Non-presence Contact List and skip the next step. |
|---|---|
| Step 2 | Contact Lists only. Select the users for whom you will export contact lists: Under Export Contact List Options , choose the category of users for whom you will export contact lists. The default is to export contact lists for all users. Click Find to bring up the list of users and then click Next . |
| Step 3 | In the File Name field, enter a name for the CSV file. |
| Step 4 | Under Job Information , configure when you want to run this job: Run Immediately —Check this button to export contact lists right away. Run Later —Check this button if you want to schedule a time for the job. With this option, you will need to use the Job Scheduler page
                                             at Bulk Administration > Job Scheduler to schedule a time for this job to run. |
| Step 5 | Click Submit . If you choose Run Immediately , the export job runs right away. |
| Step 6 | After the export file is created, download the exported file: From Cisco Unified CM IM and Presence Administration, choose Bulk Administration > Upload/Download Files . Click Find and select the export file. Click Download Selected and download the file to a location you can access. |

| Parameter | Description |
|---|---|
| User ID | The user ID of the IM and Presence Service user. Note This value is the user portion of the user's IM address. | Note | This value is the user portion of the user's IM address. |
| Note | This value is the user portion of the user's IM address. |
| User Domain | The Presence domain of the IM and Presence Service user. Note This value is the domain portion of the user's IM address. Example 1: bjones@example.com—bjones is the user ID and example.com is the user domain. Example 2: bjones@usa@example.com—bjones@usa is the user ID and example.com is the user domain. | Note | This value is the domain portion of the user's IM address. |
| Note | This value is the domain portion of the user's IM address. |
| Contact ID | The user ID of the contact list entry. |
| Contact Domain | The Presence domain of the contact list entry. |
| Nickname | The nickname of the contact list entry. If the user has not specified a nickname for a contact, the Nickname parameter will be blank. |
| Group Name | The name of the group to which the contact list entry is to be added. If a user’s contacts are not sorted into groups, the default group name will be specified in the Group Name field. |
| State | The state of the rosters, the roster database stores it in decimal format. |

| Note | This value is the user portion of the user's IM address. |
|---|---|

| Note | This value is the domain portion of the user's IM address. |
|---|---|

| Parameter | Description |
|---|---|
| User JID | The User JID. This is the IM address of the user. |
| Contact JID | The User JID of the contact list entry, if available, otherwise it is the UUID. |
| Group Name | The name of the group to which the contact list entry is to be added. |
| Content Type | The textmime type and subtype used in the info field. |
| Version | The content type used in the info field. |
| Info | The contact information of the contact list entry in vCard format. |

| Step 1 | In Cisco Unified CM IM and Presence Administration , choose Bulk Administration > Upload/Download Files . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Click Browse to locate and choose the CSV file. |
| Step 4 | For the Target setting: If you want to upload an input file for contact lists, choose Contact Lists . For more on user contact list input files, see File Details for Import Contact Lists . If you want to upload an input file for non-presence contact lists, choose Non-presence Contact Lists . For more on non-presence user contact list input files, see File Details for Import Non-Presence Contact Lists . |
| Step 5 | For the Transaction Type: Choose  as the Transaction Type. If you want to upload an input file for contact lists, choose Import Users’ Contacts – Custom File If you want to upload an input file for non-presence contact lists, choose Import Users’ Non Presence Contacts |
| Step 6 | Click Save to upload the file. |

| Parameter | Description |
|---|---|
| User ID | This is a mandatory parameter. The user ID of the IM and Presence Service user. It can have a maximum 132 characters. Note This value is the user portion of the user's IM address. | Note | This value is the user portion of the user's IM address. |
| Note | This value is the user portion of the user's IM address. |
| User Domain | This is a mandatory parameter. The Presence domain of the IM and Presence Service user. It can have a maximum of 128 characters. Note This value is the domain portion of the user's IM address. Example 1 : bjones@example.com—bjones is the user ID and example.com is the user domain. Example 2 : bjones@usa@example.com—bjones@usa is the user ID and example.com is the user domain. | Note | This value is the domain portion of the user's IM address. Example 1 : bjones@example.com—bjones is the user ID and example.com is the user domain. Example 2 : bjones@usa@example.com—bjones@usa is the user ID and example.com is the user domain. |
| Note | This value is the domain portion of the user's IM address. Example 1 : bjones@example.com—bjones is the user ID and example.com is the user domain. Example 2 : bjones@usa@example.com—bjones@usa is the user ID and example.com is the user domain. |
| Contact ID | This is a mandatory parameter. The user ID of the contact list entry. It can have a maximum of 132 characters. |
| Contact Domain | This is a mandatory parameter. The Presence domain of the contact list entry. The following restrictions apply to the format of the domain name: Length must be less than or equal to 128 characters Contains only numbers, upper- and lowercase letters, and hyphens (-) Must not start or end with hyphen (-) Length of label must be less than or equal to 63 characters Top-level domain must be characters only and have at least two characters |
| Nickname | The nickname of the contact list entry. It can have a maximum of 255 characters. |
| Group Name | Group Name is a mandatory parameter. The name of the group to which the contact list entry is to be added. It can have a maximum of 255 characters. |
| State | The state of the rosters, the roster database stores it in decimal format. |

| Note | This value is the user portion of the user's IM address. |
|---|---|

| Note | This value is the domain portion of the user's IM address. Example 1 : bjones@example.com—bjones is the user ID and example.com is the user domain. Example 2 : bjones@usa@example.com—bjones@usa is the user ID and example.com is the user domain. |
|---|---|

| Caution | We recommend that you do not manually modify the CSV file, due to the size of the file itself and the risk of corrupting the
                                                   vCard information. The following table describes the parameters in the input file for non-presence contacts: |
|---|---|

| Parameter | Description |
|---|---|
| User JID | The User JID. This is the IM address of the user. |
| Contact JID | The User JID of the contact list entry, if available, otherwise it is the UUID. |
| Group Name | The name of the group to which the contact list entry is to be added. |
| Content Type | The textmime type and subtype used in the info field. |
| Version | The content type used in the info field. |
| Info | The contact information of the contact list entry in vCard format. |

| Step 1 | In Cisco Unified CM IM and Presence Administration : If you want to create a new bulk administration job for contact lists, choose Bulk Administration > Contact List > Update If you want to create a new bulk administration job for contact lists, choose Bulk Administration > Contact Non-presence List > Import Non-presence Contact List . If you want to create a new bulk administration job for user location migration, choose Bulk Administration > User Location Migration > Import User Location Details . |
|---|---|
| Step 2 | From the File Name drop-down list, choose the file to import. |
| Step 3 | In the Job Description field, enter a description for this Bulk Administration job. |
| Step 4 | Choose one of the following: Click Run Immediately to execute the Bulk Administration job immediately. Click Run Later to schedule a time to execute the Bulk Administration job. For more information about scheduling jobs in BAT, see the Online
                                                Help in Cisco Unified CM IM and Presence Administration. |
| Step 5 | Click Submit . If you chose to run the job immediately, the job runs after you click Submit. |

| Step 1 | In Cisco Unified CM IM and Presence Administration , choose Bulk Administration > Job Scheduler . |
|---|---|
| Step 2 | Click Find and choose the job ID of the contact list import job. |
| Step 3 | Click the Log File Name link to open the log. |