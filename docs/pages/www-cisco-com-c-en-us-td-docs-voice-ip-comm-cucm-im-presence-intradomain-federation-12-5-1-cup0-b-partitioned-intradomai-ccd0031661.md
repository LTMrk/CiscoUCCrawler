---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-intradomain-federation-12-5-1-cup0-b-partitioned-intradomai-ccd0031661
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/intradomain_federation/12_5_1/cup0_b_partitioned-intradomain-federation-1251/cup0_b_partitioned-intradomain-federation-1251_chapter_010.html
retrieved_at: 2026-08-16T16:16:06.932621+00:00
---

Partitioned Intradomain Federation Guide for the IM and Presence Service

# Partitioned Intradomain Federation Guide for the IM and Presence Service

Updated: January 17, 2019

Chapter: Planning for User Migration

## Chapter: Planning for User Migration

# Planning for User Migration

## Maintenance of User
                        	 Identity During Migration

During
                              		  migration from Skype for Business /Lync/OCS to IM and Presence
                                 			 Service , Microsoft Lync and Microsoft Office
                                 			 Communicator users should maintain the same identity, which is their
                              		  Uniform Resource Identity (URI). Maintaining the same identity during migration
                              		  has the following benefits:

It allows for
                                    				the user’s availability state to be continually monitored by existing followers
                                    				because the user’s identity does not change.

It also allows
                                    				for much simpler migration of a user’s contact lists because the contact lists
                                    				can be directly imported from the Microsoft server to IM and Presence
                                       				  Service .

IM
                                 			 and Presence Service URIs are composed by joining the Cisco Unified Communications
                                 			 Manager user ID with the IM and Presence Service domain as follows:

<userid>@<domain>

If users
                              		  are manually added through the Cisco Unified Communications
                                 			 Manager user interface or through the Cisco Unified Communications
                                 			 Manager Bulk Administration Tool (BAT), you must ensure that the user
                              		  ID that you specified when you created the user matches the user portion of the
                              		  user’s Microsoft server URI. For example, if the Microsoft user's URI is
                              		  bobjones@foo.com, you should create the CUCM user with a user ID of bobjones.

If Cisco Unified Communications
                                 			 Manager is configured to synchronize users from Active Directory, you
                              		  must ensure that the Active Directory field that is used to map to the Cisco Unified Communications
                                 			 Manager user ID matches the user portion of the Microsoft server URI.
                              		  Note the following:

Cisco Unified Communications Manager maps to userID
                                    				from a limited number of Active Directory fields, the most common of which is
                                    				sAMAccountName.

If Cisco Unified Communications
                                       				  Manager maps userID to sAMAccountName, the Microsoft server URI for
                                    				the migrating users must also match the format
                                    				<sAMAccountName>@<domain>.

If the
                                    				sAMAccountName of Bob Jones is bjones, the Microsoft server URI must be
                                    				bjones@cisco.com.

If any Microsoft
                                    				server URIs do not match the format <sAMAccountName>@<domain>, you
                                    				can modify the URIs for each batch of Microsoft server users before you migrate
                                    				that batch to IM and Presence
                                       				  Service .

### Tasks Before
                           	 Migration

If the Skype for Business /Lync/OCS SIP URI does not match the IM and Presence Service URI format of
                                 		  <userid>@<domain>, you can change the Microsoft server URI for
                                 		  migrating users in a phased manner. In previous releases, you had to change the
                                 		  URI for all migrating users before you began the migration process. With this
                                 		  release, you can change the URI for each batch of users just before you migrate
                                 		  that batch.

If you decide to
                                 		  change the Microsoft server SIP URIs just before you migrate each batch, then,
                                 		  before you migrate each batch of Microsoft server users, you must also update
                                 		  the contact lists on IM and Presence Service to ensure that they contain
                                 		  the latest SIP URI (contact IDs) for the Microsoft server users that are about
                                 		  to be migrated. Consider the following example.

#### Migration
                                 		  Example

John Smith and Bob
                                 		  Jones are Lync users and are both listed in each other’s contact list. Their
                                 		  Lync URIs are john.smith@example.com and bob.jones@example.com. John is being
                                 		  migrated to IM and Presence Service during Phase 1 of the
                                 		  migration and Bob is being migrated during Phase 2.

Phase 1 of user
                                 		  migration begins and John’s Lync URI is changed to jsmith@example.com. John is
                                 		  then migrated to IM and Presence Service . Availability and IM between
                                 		  John and Bob is maintained.

Phase 2 of user
                                 		  migration begins and Bob’s Lync URI is changed to bjones@example.com. John’s
                                 		  contact list on IM and Presence Service is updated with the new
                                 		  contact IDs for all of the users that are being migrated in Phase 2. Bob is
                                 		  then migrated to IM and Presence Service . Availability and IM between
                                 		  John and Bob is maintained.

#### Microsoft Server
                              	 SIP URI Change

If any Skype for Business /Lync/OCS URIs do not match the IM and Presence Service Service URI format, you must
                                    		  change those Microsoft server URIs before you begin the migration process. For
                                    		  more information about how to change the Microsoft server URIs see related
                                    		  topics on verifying the Microsoft server SIP URI format for migrating users.

#### Contact Rename for
                              	 IM and Presence Service Users

The IM and Presence Service Bulk Administration Tool
                                    		  allows you to rename the contact IDs in the contact lists of IM and Presence Service users in a phased manner. This
                                    		  means that you can update the IM and Presence Service contact lists each time that Skype for Business /Lync/OCS URIs are changed.

If you need to
                                                			 update the IM and Presence
                                                   				Service contact lists, you must perform the update before the
                                                			 Microsoft server users (with the changed URIs) are enabled for IM and Presence
                                                   				Service on Cisco Unified
                                                   				Communications Manager .

See related topics
                                    		  for renaming contacts IDs for more information.

## Detailed User
                        	 Migration Plan

The
                              		  partitioned intradomain federation integration between the IM and Presence Service and Skype for Business /Lync/OCS is designed to provide basic communication between users during a phased
                              		  migration from a Microsoft server to IM and Presence Service .

However,
                              		  partitioned intradomain federation integration introduces a performance
                              		  overhead. Because of this, IM and Presence Service can support a maximum of
                              		  130,000 SIP intradomain federation contacts per server. To ensure that this
                              		  federated contact threshold is not exceeded on any IM and Presence Service node during migration of users
                              		  from the Microsoft server to IM and Presence Service , a detailed user migration
                              		  plan may be required.

You can
                              		  use the following calculation to get an estimate of the maximum number of IM and Presence Service users that can be supported
                              		  without breaking the above federated contact threshold:

Max Supported Users = 130,000
                                 			 / Average Contact List Size .

Based on
                              		  this calculation, the following table gives an indication of the maximum number
                              		  of IM and Presence Service users that can be supported
                              		  without breaking the 130,000 federated contact threshold.

Average Contact List Size

Maximum Supported Users (without high availability)

Maximum Supported Users (with high availability 1 )

200

650

325

150

866

433

100

1300

650

75

1733

866

50

2600

1300

25

5000

2500

You
                              		  require a detailed user migration plan if the number of users to be provisioned
                              		  on any IM and Presence Service node within your deployment
                              		  exceeds the relevant limit above. Contact your Cisco Support representative to
                              		  begin the process of defining a detailed migration plan.

### Notes

The values for
                                    				the maximum number of supported users in the table above are based on
                                    				worst-case figures; that is, in the case where all contacts are federated.

With proper
                                    				migration planning, the full complement of users can be deployed on an IM and Presence
                                       				  Service node in a phased manner, without breaking the 130,000
                                    				federated contact threshold.

When high
                                    				availability is enabled, each IM and Presence
                                       				  Service node must be able to handle the load associated with all
                                    				users within the IM and Presence
                                       				  Service 2-node subcluster because, in the event of a node failure,
                                    				the second node in the cluster services all users on its own. Therefore, the
                                    				limit per node must be halved.

If you are
                                    				unsure about the average contact list size within your Microsoft server
                                    				deployment, assume it to be worst-case (200 contacts) when you are deciding
                                    				whether a migration plan is required.

The values for
                                    				the maximum number of supported users in the table above assume the Cisco
                                    				supported virtual platform based on the IM and Presence
                                       				  Service OVA template for 5000 users. The equivalent numbers for the
                                    				1000 user OVA are detailed below.

### 1000 User
                           	 OVA

Average Contact List Size

Maximum Supported Users (without high availability)

Maximum Supported Users (with high availability 2 )

200

90

45

150

120

60

100

180

90

75

240

120

50

360

180

25

720

360

18

1000

500

### 5000 User
                           	 OVA

IM and Presence
                                    			 Service can support up to 90,000 SIP intradomain federation contacts
                                 		  per node with the 5000 user OVA. The following table gives an indication of the
                                 		  maximum number of IM and Presence Service users that can be supported
                                 		  without breaking the 90,000 federated contact threshold.

Average Contact List Size

Maximum Supported Users (without high availability)

Maximum Supported Users (with high availability 3 )

200

450

225

150

600

300

100

900

450

75

1200

600

50

1800

900

25

3600

1800

18

5000

2500

## Duration Guidelines
                        	 for User Migration Tools

Cisco
                              		  provides a number of tools to allow bulk migration of users from Skype for Business /Lync/OCS to IM and Presence Service . To allow you to plan your
                              		  migration, it is important to be aware of the time required for each tool to
                              		  run when you are migrating a large number of users. This section describes the
                              		  expected run time for each of those tools.

If you have a
                                          			 mixed deployment of both Lync and OCS servers, you must run the tools on the
                                          			 Lync users and then run the tools again on the OCS users.

### Export Contact List
                           	 Tool

The Export
                                 		  Contact List tool (ExportContacts.exe) can export contacts from Skype for Business /Lync/OCS at an average rate of 800 contacts per second (or 48,000 contacts per minute).
                                 		  You can use the following equation as a guide to estimate the expected run time
                                 		  for this tool for a set of Microsoft server users.

Time to export
                                 		  contacts (mins) = Number of Microsoft server users x Average Contact List Size
                                 		  / 48000.

The
                                 		  following table shows the expected run time for a number of sample cases.

Number of Microsoft Server Users

Average Contact List Size

Time to Export Contacts

2000

100

5
                                             					 minutes

5000

75

8
                                             					 minutes

15000

60

19
                                             					 minutes

### Disable Account
                           	 Tool

The
                                 		  Disable Account tool (DisableAccount.exe) can disable Skype for Business /Lync/OCS accounts at an average rate of 13 accounts per second (or 800 accounts per
                                 		  minute). You can use the following equation as a guide to estimate the expected
                                 		  run time for this tool for a set of Microsoft server users.

Time to disable
                                 		  accounts (mins) = Number of Microsoft server users / 800

The
                                 		  following table shows the expected run time for a number of sample cases.

Number of Microsoft server users

Time to disable accounts

2000

3
                                             					 minutes

5000

7
                                             					 minutes

15000

20
                                             					 minutes

### Delete Account
                           	 Tool

The Delete
                                 		  Account tool (DeleteAccount.exe) can delete Skype for Business /Lync/OCS accounts at an average rate of 13 accounts per second (or 800 accounts per
                                 		  minute). You can use the following equation as a guide to estimate the expected
                                 		  run time for this tool for a set of Microsoft server users.

Time to delete
                                 		  accounts (mins) = Number of Microsoft server users / 800.

The
                                 		  following table shows the expected run time for a number of sample cases.

Number of Microsoft Server Users

Time to Delete Accounts

2000

3
                                             					 minutes

5000

7
                                             					 minutes

15000

20
                                             					 minutes

### Bulk Administration
                           	 Tool Contact List Import

The IM and Presence Service Bulk Administration Tool (BAT) can import contacts at varying rates, depending on the IM and
                                    			 Presence Service platform. The following table shows the expected import rate
                                 		  for a selection of IM and
                                    			 Presence Service platforms.

OVA Template

Import Rate

2000 user
                                             					 OVA

6/sec

5000 user
                                             					 OVA

12/sec

15000 user
                                             					 OVA

22/sec

The
                                 		  following table shows the expected run time for a number of sample cases

Number of Users

Average Contact List Size

Import Time (Rate = 22/sec 4 )

2000

100

2hours, 32 minutes

5000

75

4
                                             					 hours, 45 minutes

15000

60

11
                                             					 hours, 22 minutes

#### Notes

The calculations
                                       				for the Export Contact List tool, Disable Account tool, and Delete Account tool
                                       				are based on the Skype for Business /Lync/OCS and Active Directory (AD) running on hardware with at least 2Ghz CPU processing
                                       				power, and 2GB of RAM.

Running these
                                       				user migration tools has no affect on the capabilities of other Microsoft
                                       				server users who are signed into Microsoft Lync or Microsoft Office
                                          				  Communicator .

Cisco recommends
                                       				that you perform user migration during a scheduled maintenance window to reduce
                                       				the load on the Microsoft server and AD system.

### Bulk Administration Tool Contact Rename

The Bulk Administration Tool Contact Rename utility duration rates are influenced by two primary factors:

The number of users in the cluster with renamed contact IDs in their contact list

The average number of renamed contact IDs for each such user

These factors vary for each deployment. For large-scale operations (over 1000 contact IDs renamed), it may take a number of
                                 hours for the job to complete. To estimate the likely job completion rate, view the job progress indicators to see the rate
                                 at which impacted users are being updated.

| Note | If you need to
                                                			 update the IM and Presence
                                                   				Service contact lists, you must perform the update before the
                                                			 Microsoft server users (with the changed URIs) are enabled for IM and Presence
                                                   				Service on Cisco Unified
                                                   				Communications Manager . |
|---|---|

| Average Contact List Size | Maximum Supported Users (without high availability) | Maximum Supported Users (with high availability 1 ) |
|---|---|---|
| 200 | 650 | 325 |
| 150 | 866 | 433 |
| 100 | 1300 | 650 |
| 75 | 1733 | 866 |
| 50 | 2600 | 1300 |
| 25 | 5000 | 2500 |

| Average Contact List Size | Maximum Supported Users (without high availability) | Maximum Supported Users (with high availability 2 ) |
|---|---|---|
| 200 | 90 | 45 |
| 150 | 120 | 60 |
| 100 | 180 | 90 |
| 75 | 240 | 120 |
| 50 | 360 | 180 |
| 25 | 720 | 360 |
| 18 | 1000 | 500 |

| Average Contact List Size | Maximum Supported Users (without high availability) | Maximum Supported Users (with high availability 3 ) |
|---|---|---|
| 200 | 450 | 225 |
| 150 | 600 | 300 |
| 100 | 900 | 450 |
| 75 | 1200 | 600 |
| 50 | 1800 | 900 |
| 25 | 3600 | 1800 |
| 18 | 5000 | 2500 |

| Note | If you have a
                                          			 mixed deployment of both Lync and OCS servers, you must run the tools on the
                                          			 Lync users and then run the tools again on the OCS users. |
|---|---|

| Number of Microsoft Server Users | Average Contact List Size | Time to Export Contacts |
|---|---|---|
| 2000 | 100 | 5
                                             					 minutes |
| 5000 | 75 | 8
                                             					 minutes |
| 15000 | 60 | 19
                                             					 minutes |

| Number of Microsoft server users | Time to disable accounts |
|---|---|
| 2000 | 3
                                             					 minutes |
| 5000 | 7
                                             					 minutes |
| 15000 | 20
                                             					 minutes |

| Number of Microsoft Server Users | Time to Delete Accounts |
|---|---|
| 2000 | 3
                                             					 minutes |
| 5000 | 7
                                             					 minutes |
| 15000 | 20
                                             					 minutes |

| OVA Template | Import Rate |
|---|---|
| 2000 user
                                             					 OVA | 6/sec |
| 5000 user
                                             					 OVA | 12/sec |
| 15000 user
                                             					 OVA | 22/sec |

| Number of Users | Average Contact List Size | Import Time (Rate = 22/sec 4 ) |
|---|---|---|
| 2000 | 100 | 2hours, 32 minutes |
| 5000 | 75 | 4
                                             					 hours, 45 minutes |
| 15000 | 60 | 11
                                             					 hours, 22 minutes |