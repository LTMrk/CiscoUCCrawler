---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-intradomain-federation-12-5-1-cup0-b-partitioned-intradomai-8704dc807f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/intradomain_federation/12_5_1/cup0_b_partitioned-intradomain-federation-1251/cup0_b_partitioned-intradomain-federation-1251_chapter_01000.html
retrieved_at: 2026-08-16T16:16:32.645109+00:00
---

Partitioned Intradomain Federation Guide for the IM and Presence Service

# Partitioned Intradomain Federation Guide for the IM and Presence Service

Updated: January 17, 2019

Chapter: User Migration

## Chapter: User Migration

# User Migration

## Cisco User Migration
                        	 Tools

Cisco
                              		  provides the following tools to aid the user migration process from Skype for Business /Lync/OCS to IM and Presence Service :

Export Contact
                                    				List tool—allows you to export contact lists in bulk from the Microsoft server
                                    				for migrating users

Disable Account
                                    				tool—allows you to disable the Microsoft server account of migrating users

Delete Account
                                    				tool—allows you to delete migrating users from the Microsoft server so that
                                    				presence requests for these users are later routed to IM and Presence
                                       				  Service

These user
                              		  migration tools can be collectively downloaded as a zip file from the IM and Presence Service Download Software page on
                              		  cisco.com at http://software.cisco.com/download/release.html?mdfid=286269517&flowid=50462&softwareid=282074312&release=UTILS&relind=AVAILABLE&rellifecycle=&reltype=latest .

The zip
                              		  file contains the three tools and a text file called version.txt. The text file
                              		  contains the current version number of the tools and must be saved in the same
                              		  folder as the tools. If the tools are stored in different folders, you must
                              		  store a copy of the text file in each location. If the text file is not in the
                              		  same folder when you run a tool, you receive an error and the tool does not
                              		  run.

Tip

While attempting
                                          			 to run any of the user migration tools you may receive the following error:
                                          			 "Application failed to initialize properly". The reason for this error is that
                                          			 you are attempting to run the user migration tools without the .NET 2.0
                                          			 Framework installed. Each of the user migration tools that Cisco provides
                                          			 requires that at least version 2.0 of the .NET Framework is installed on the
                                          			 server where you are running the tool.

The .NET 2.0
                                          			 Framework comes installed as standard on Windows Server 2003 R2 or newer.

## Recommendations
                        	 before Migration

Cisco
                              		  recommends that you perform the following tasks before you begin to migrate
                              		  users from Skype for Business /Lync/OCS to IM and Presence Service :

Set unlimited
                                    				contact lists and watchers

Enable automatic
                                    				authorization of subscription requests

Disable new
                                    				subscriber notification pop-ups on Microsoft Lync

The IM and Presence Service IM addresses can be set to
                              		  match the OCS/Lync SIP URI (msRTCSIP-PrimaryUserAddress) so that the user's
                              		  identity is maintained throughout the migration. If that is not possible, then
                              		  user rename is required.

For more information about
                              		  setting the IM address value for IM and Presence Service nodes in the cluster, see Configuration
                                 			 and Administration of IM and Presence Service on Cisco Unified
                                 			 Communications Manager .

### Set Unlimited
                           	 Contact Lists and Watchers

Before you
                                 		  migrate users from Skype for Business /Lync/OCS to IM and Presence Service , Cisco recommends that you set
                                 		  the Maximum Contact List Size and Maximum Watchers settings on IM and Presence Service to unlimited. This ensures
                                 		  that each migrated user contact list is fully imported to IM and Presence Service .

After all
                                 		  users have been migrated to IM and Presence Service , reset the Maximum Contact
                                 		  List Size and Maximum Watchers settings on IM and Presence Service to the desired values. The
                                 		  system default value is 200 for Maximum Contact List Size and 200 for Maximum
                                 		  Watchers size.

The
                                 		  following procedure describes how to set unlimited values for the Maximum
                                 		  Contact List Size and Maximum Watchers settings.

If you have a
                                             			 multicluster deployment, you must perform this procedure on each cluster. When
                                             			 you change Presence settings, they are applied to all nodes in the cluster;
                                             			 therefore you need to set them only on the IM and Presence Service database publisher node within
                                             			 any given cluster.

Step 1

Log in to the Cisco
                                             				Unified IM and Presence Administration user interface. Choose Presence > Settings .

Step 2

For Maximum
                                             				Contact List Size (per user) , check the No
                                             				Limit check box.

Step 3

For Maximum Watchers
                                             				(per user) , check the No
                                             				Limit check box.

Step 4

Click Save .

Step 5

Restart the
                                          			 Cisco XCP Router on all IM and Presence Service nodes in the cluster. To
                                          			 restart the Cisco XCP Router, log in to the Cisco
                                             				Unified IM and Presence Serviceability user interface and choose Tools > Control Center – Network
                                                				  Services .

### Enable Automatic
                           	 Authorization of Subscription Requests

To improve
                                 		  user experience during migration, Cisco recommends that you allow automatic
                                 		  authorization of subscription requests before you begin the migration process.
                                 		  Otherwise, each IM and Presence Service user is forced to manually
                                 		  authorize subscription requests each time they are imported as a contact into
                                 		  the IM and Presence Service . This setting should only be
                                 		  disabled, if desired, after all migrations are complete.

The
                                 		  following procedure describes how to enable automatic authorization of
                                 		  subscription requests.

This setting is
                                             			 enabled by default on IM and Presence Service .

If you have a
                                             			 multicluster deployment, you must perform this procedure on each cluster. When
                                             			 you change Presence settings, they are applied to all nodes in the cluster;
                                             			 therefore you need to set them only on the IM and Presence database publisher
                                             			 node within any given cluster.

Step 1

Log in to the Cisco
                                             				Unified IM and Presence Administration user interface. Choose Presence > Settings .

Step 2

Check the check
                                          			 box for Allow
                                             				users to view the availability of other users without being prompted for
                                             				approval .

Step 3

Click Save .

Step 4

Restart the
                                          			 Cisco XCP Router on all IM and Presence Service nodes in the cluster. To
                                          			 restart the Cisco XCP Router, log in to the Cisco
                                             				Unified IM and Presence Serviceability user interface. Choose Tools > Control Center – Network
                                                				  Services .

### Subscriber
                           	 Notification Pop-ups

When you migrate
                                 		  users from Microsoft Lync to IM and Presence Service , users that remain on Lync may
                                 		  receive subscription notification pop-ups from some of those migrated users.
                                 		  Such a notification only occurs when:

the migrated
                                       				user has the Microsoft Lync user in their contact list

the Microsoft
                                       				Lync user does not have that same migrated user in their contact list

If the Microsoft
                                 		  Lync user has the migrated contact in their contact list also, then there is no
                                 		  notification pop-up. When an individual notification pop-up has been handled by
                                 		  the Microsoft Lync user, it will not re-appear.

If you do not want
                                 		  Lync users to receive new subscriber notification pop-ups you can disable Lync
                                 		  pop-ups. You have two options when disabling these notification pop-ups:

you can
                                       				disable pop-ups for the entire duration of user migration

you can
                                       				disable pop-ups only during the migration of a batch of users

If you disable
                                 		  pop-ups, then all pop-ups for all Lync users will be disabled until you
                                 		  re-enable them.

Disabling and
                                             			 enabling Microsoft Lync pop-ups requires a restart of the Lync front-end
                                             			 services.

#### Disable Microsoft
                              	 Lync Pop-ups

If you want to
                                    		  disable all pop-ups for all Microsoft Lync users, complete the following
                                    		  procedure before you begin the user migration or the migration of a batch of
                                    		  users.

Step 1

On the Lync
                                             			 front-end server choose Start > All
                                                   				  Programs > Microsoft Lync Server
                                                   				  2010 > Lync Server Management
                                                   				  Shell .

Tip

Enter either
                                                            				  Microsoft Lync Server 2010 or 2013, depending on your Microsoft Lync Server
                                                            				  version.

Step 2

Enter the
                                             			 following powershell command:

Set-CSClientpolicy
                                                      				  -EnableNotificationForNewSubscriber $False

Step 3

Choose Start > Programs > Administrative
                                                   				  Tools > Services .

Step 4

Right-click
                                             			 the service Lync front end server and click Restart .

#### Restore Microsoft
                              	 Lync Pop-up Behavior

To restore the
                                    		  previous client behavior for notification pop-ups for Microsoft
                                       			 Lync users complete the following procedure after user migration is
                                    		  complete or after the migration of a batch of users is complete.

Step 1

Enter the
                                             			 following command to restore client pop-up behavior on Lync:

Set-CSClientpolicy
                                                      					 -EnableNotificationForNewSubscribers $Null

Step 2

Choose Start > Programs > Administrative
                                                   				  Tools > Services .

Step 3

Right-click
                                             			 the service Lync front end server and choose Restart .

## Verify Microsoft
                        	 Server SIP URI Format for Migrating Users

Use this
                              		  procedure to check that the IM address format that is configured on IM and Presence Service aligns with the IM address
                              		  format of the Microsoft servers.

IM
                                 			 and Presence Service supports two IM address schemes. If you use the
                              		  Directory URI IM address scheme, the IM address format between IM and Presence Service and the Microsoft servers
                              		  align. However, if you use the UserID @ Default_Domain IM
                              		  address scheme, misalignment of the IM address schemes is possible.

The UserID @ Default_Domain IM
                              		  address scheme URIs are composed by joining the Cisco Unified Communications Manager user ID with the IM and Presence Service default domain. If any Skype for Business /Lync/OCS URIs do not match the UserID @ Default_Domain IM
                              		  address format, you must modify the URIs of the migrating users. You can modify
                              		  a batch of Microsoft server URIs before you migrate each batch of Microsoft
                              		  server users to IM and Presence Service .

For releases
                                          			 earlier than release 10.0(1), you must modify all Microsoft server URIs before
                                          			 the first batch of users are migrated from a Microsoft server to IM and Presence
                                             				Service .

When the Directory URI IM
                              		  address scheme is used, Microsoft server users do not have to be renamed if
                              		  they are from domains that differ from the domains which are configured on the Cisco Unified Communications Manager and IM and Presence Service clusters. Individual users can
                              		  be assigned a different email domain. You must configure IM and Presence Service for interdomain federation
                              		  with the Microsoft servers and set up the email for federation feature if the
                              		  Microsoft server users are on a different domain.

For more
                              		  information about the SIP URI format, see topics related to maintaining user
                              		  identity during migration.

For more
                              		  information about the IM and Presence Service IM address schemes, see Configuration and Administration of IM and Presence
                                    				Service on Cisco Unified Communications Manager .

For more
                              		  information about setting up interdomain federation between IM and Presence Service and Microsoft servers, see the Interdomain
                                 			 Federation for IM and Presence
                                    				Service on Cisco Unified Communications Manager guide.

Step 1

Verify that
                                       			 the IM address scheme is set to Directory URI and that the directory URI maps
                                       			 to msRTCSIP-PrimaryUserAddress on Cisco Unified Communications Manager .

Step 2

Check that the
                                       			 format of the current IM address scheme for IM and Presence
                                          				Service matches the format that the Microsoft server uses. If the IM
                                       			 address formats do not align, then you must rename the users on the Microsoft
                                       			 server before migration. See the following procedures for more information
                                       			 about modifying the Microsoft server SIP URI.

### What to do next

Rename Contact IDs in IM and Presence Service Contact Lists

### Modify Lync SIP URI

Complete the following procedure to change the format of a Lync user's SIP URI.

Step 1

From the Lync Control Panel, choose the Users  tab.

Step 2

Search for the user that you want to change and double-click the user.

Step 3

Change the SIP address field.

Step 4

Click Commit .

Tip

To modify SIP URIs in bulk, use the Set-CsUser cmdlet. For more information, see http://technet.microsoft.com/en-us/library/gg398510.aspx .

#### What to do next

Rename contact ids in the IM and Presence Service contact lists.

### Modify OCS SIP
                           	 URI

Complete the following procedure on the Active Directory server to
                                 		  change the format of the SIP URI for an OCS user.

Step 1

On the Active Directory
                                          			 server, choose Start > Control
                                                				  Panel > Administrative Tools > Active
                                                				  Directory Users and Computers .

Step 2

Search for the user that you want to change and double-click the
                                          			 user.

Step 3

From the Properties window, choose the 
                                          			 Live Communications tab.

Step 4

Change the 
                                          			 SIP URI field.

Step 5

Click OK .

To modify SIP URIs in bulk, use the System.DirectoryServices
                                                         				  that are provided by Microsoft to update the msRTCSIP-PrimaryUserAddress
                                                         				  property for each affected user. For more information, see http://msdn.microsoft.com/en-us/library/ms180835(v=vs.80).aspx .

#### What to do next

Rename contact ids in the IM and Presence Service contact lists.

## Rename Contact IDs
                        	 in IM and Presence Service Contact Lists

This
                                                				  procedure is necessary only if you modified any Skype for Business /Lync/OCS SIP URIs . For more information about URI formats, see topics related to
                                                				  maintaining user identity during migration.

You must
                                                				  complete this procedure before the modified Microsoft server users are enabled
                                                				  for IM and Presence
                                                   					 Service .

Cisco
                                                				  recommends that you run this tool during a scheduled maintenance window.

Before you can
                              		  rename the contact IDs for a set of users, you must upload a file containing a
                              		  list of contact IDs and the corresponding new format of each of those contact
                              		  IDs. The file must be a CSV file with the following format:

Contact ID, New Contact
                                 			 ID

where Contact
                                 			 ID is the user's IM address as it appears on the Presence
                                 			 Topology User Assignment window.

The following is a
                              		  sample CSV file with one entry:

```
Contact ID, New Contact ID
john.smith@example.com, jsmith@example.com
```

It is your
                                                				  responsibility to compile the CSV file with the appropriate contact IDs.

You must
                                                				  ensure that the header Contact ID, New Contact ID is present in all CSV files.

When you run the
                              		  job, the IM and Presence Service Bulk Administration Tool (BAT)
                              		  updates the contact lists of any user that referenced the old contact IDs.

Complete the
                              		  following procedure to upload the CSV file and rename the contact IDs for a
                              		  list of users.

You must
                                          			 complete this procedure on each IM and Presence
                                             				Service cluster.

Step 1

Upload the CSV
                                       			 file with the list of contact IDs that you want to rename in all contact lists.
                                       			 Do the following:

On the IM and Presence
                                                					 Service database publisher node, log in to the Cisco Unified CM IM and Presence Administration user
                                             				  interface. Choose Bulk
                                                   						Administration > Upload/Download Files .

Click Add New .

Click Browse to locate and choose the CSV file.

Choose Contact as the Target.

Choose Rename Contacts – Custom File as the Transaction
                                             				  Type.

Click Save to upload the file.

Step 2

On the
                                       			 publisher node, log in to the Cisco
                                          				Unified CM IM and Presence Administration user interface. Choose Bulk
                                             				  Administration > Contact List > Rename
                                             				  Contacts .

Step 3

In the File
                                          				Name field, choose the file that you uploaded.

Step 4

Choose one of
                                       			 the following actions:

- Click Run
                                             				  Immediately to execute the Bulk Administration job immediately.

- Click Run
                                             				  Later to schedule a time to execute the Bulk Administration job.
                                          				For more information about scheduling jobs in the BAT, see the Online Help in Cisco Unified CM IM and Presence Administration .

Step 5

Click Submit . If you chose to run the job immediately, the
                                       			 job runs after you click Submit.

Provision of Microsoft Server Users on Cisco Unified Communications Manager

### Results of the
                           	 Rename Contact IDs Job

You can check the
                                 		  results of the Rename Contact IDs job from the Job
                                    			 Scheduler window ( Bulk
                                       				Administration > Job Scheduler ). Depending on the
                                 		  number of entries in the CSV file, the Bulk Administration Tool processes
                                 		  the contents of the file in a few minutes. However, it may take several hours
                                 		  for all of the contact lists to be updated. The Job Status shows as Processing
                                 		  during this time and the current progress of the job is shown in the Job
                                 		  Results section.

The Job Results
                                             			 area on the Job Scheduler window is shown only when the CSV file has been
                                             			 processed. The Number of Records Processed and the Number of Records Failed
                                             			 values do not represent the number of entries that were processed on the CSV
                                             			 file; these values represent the number of contact lists that have been updated
                                             			 and the number of failed contact list updates.

After the contact
                                 		  ids are renamed, you can proceed to provision Skype for Business /Lync/OCS users on Cisco Unified Communications Manager .

## Provision of
                        	 Microsoft Server Users on Cisco Unified Communications Manager

The
                              		  first step in migrating users from Microsoft Lync or Microsoft Office Communications Server (OCS) to IM and Presence Service is to provision the Microsoft
                              		  server users on Cisco Unified Communications
                                 			 Manager and license them for IM and Presence Service and an IM and Presence Service supported client.

After users are
                                          			 provisioned on Cisco Unified Communications Manager and IM and Presence Service , Cisco recommends that you
                                          			 complete the full user migration process during the same maintenance window.
                                          			 Leaving users provisioned on both IM and Presence Service and on the Microsoft servers
                                          			 for any time period disrupts message routing for those users.

See Configuration
                                 			 and Administration of IM and Presence Service on Cisco Unified
                                 			 Communications Manager for information about configuring new users in Cisco Unified Communications
                                 			 Manager and the license requirements for IM and Presence Service and supported clients.

### What To Do
                              		  Next

Backups
                                 			 of user Lync/OCS/LCS contact list information

## Backups of User
                        	 Microsoft Server Contact List Information

The Skype for Business /Lync/OCS provides a tool called dbimpexp.exe. Cisco recommends that you use this tool to
                              		  back up the Microsoft server user contact list information so that you can
                              		  restore this information on the Microsoft server at a later date, if needed.

For the
                              		  purpose of migrating Microsoft server users to an IM and Presence Service supported client, you can use
                              		  this tool to back up the contact list for an individual Microsoft server user
                              		  or all users.

### Related
                              		  Topic

Usage of
                              		  the dbimpexp.exe tool: http://www.ocspedia.com/Misc/Explore_Dbimpexp.aspx?ArticleID=41

What To Do Next

Export of Contact Lists for Migrating Users

## Export of Contact
                        	 Lists for Migrating Users

Cisco
                              		  provides an Export Contact List tool (ExportContacts.exe) to allow an
                              		  administrator to export contact lists in bulk from Skype for Business /Lync/OCS for migrating users. The tool uses the Microsoft server application programming
                              		  interfaces (APIs) to export contact lists and output to a comma-separated
                              		  values (CSV) file. This file can then be used by the IM and Presence Service Bulk Administration Tool (BAT)
                              		  to import these same contact lists into IM and Presence Service at a later point in the
                              		  migration.

- You can run this tool against
                                             				all the supported Microsoft server platforms.

You can run
                                                				  the tool on any Standard Edition server or Enterprise Edition front-end server.

To export
                                                				  contact lists for Lync users, the Export Contact List tool requires read access
                                                				  to the Lync RTC database and also read access to LDAP. You must also ensure
                                                				  that dbo execution account privileges are granted to the RTC database.

Running this
                                                				  tool has no affect on the capabilities of other Microsoft server users who are
                                                				  signed into Microsoft Lync or Microsoft Office Communicator. However, Cisco
                                                				  recommends that you run this tool during a scheduled maintenance window to
                                                				  reduce the load on the Microsoft server and Active Directory system.

After you
                              		  run the tool, a file that contains the exported contact lists is created in the
                              		  same directory as the tool. The filename is
                              		  ExportedContacts<Timestamp>.csv. A time stamp is appended to the filename
                              		  when the file is created; therefore, each time you run the Export Contact List
                              		  tool, it creates a unique output file.

The Export
                              		  Contact List tool also creates a second file that contains the Microsoft server
                              		  SIP URI of each user that you specify for the contact list export. The filename
                              		  is UserList<Timestamp>.txt and it is also created in the same directory
                              		  as the tool.

You can use the
                                          			 UserList<Timestamp>.txt file as input to the Disable Account tool and the
                                          			 Delete Account tool.

### Log File

The Export Contact List tool also creates a unique time-stamped log file in the same directory as the output file each time
                                 you run the tool. The filename for the log file is ExportContactsLog<Timestamp>.txt.

It is good practice to check the log file each time you run the Export Contact List tool. You can then scan through the log
                                 file to fix any issues. At the bottom of each log file, the following information is summarized:

Number of users that were successfully processed

Number of users that were not found

Number of users that were not processed due to errors

Largest contact list size

Total number of contacts that were found

Average contact list size

### Run Modes

The Export
                                 		  Contact List tool has two run modes; NORMAL and STATSONLY. NORMAL is the
                                 		  standard way to run the tool. In this mode, three files are created: the CSV
                                 		  file that contains the exported contacts, the log file and the users’ Skype for Business /Lync/OCS SIP URI file. In STATSONLY mode, the Export Contact List tool creates only the
                                 		  log file. This allows you to run the tool to discover any errors that you can
                                 		  fix before you create the exported contacts CSV file and the Microsoft server
                                 		  SIP URI file.

### Input File
                           	 Formats

The Export
                                 		  Contact List tool ( ExportContacts.exe ) allows you to specify an input
                                 		  file containing the list of migrating users. The tool then retrieves the
                                 		  contact lists for the users that are specified in that input file.
                                 		  Alternatively, you can specify a command line parameter to export contact lists
                                 		  for all users in the local Skype for Business /Lync/OCS database.

If you use
                                             			 choose to export all users with the Export Contact List tool, the resulting UserList<Timestamp>.txt file contains the
                                             			 contact lists of all Microsoft server-enabled users in the domain, regardless
                                             			 of whether they are migrating to IM and Presence
                                                				Service . If you later use the UserList<Timestamp>.txt file as input to the
                                             			 Disable Account tool and the Delete Account tool, be aware that all user
                                             			 accounts in the domain are affected by the Disable Account and Delete Account
                                             			 tools.

If you are
                                 		  using an input file, the following input file formats are supported:

Input File Format 1:
                                    			 Microsoft server SIP URIs

Note the
                                 		  following:

- Each line in the input file
                                    			 represents a contact list owner.

- The contact list owner is
                                    			 represented by the owner’s Microsoft server SIP URI, for example,
                                    			 sip:bobjones@foo.com.

```
sip:ann@foo.com
sip:bob@foo.com
sip:joe@foo.com
sip:chuck@foo.com
```

Input File Format 2: Users
                                    			 by Organizational Unit in Active Directory

In this
                                 		  input file format, you can specify the Organizational Unit (OU) in Active
                                 		  Directory that contains the users that you want to migrate. The input file must
                                 		  have the following format:

```
DN:OU=OrgUnit1,OU=OrgUnit2,DC=DomainComp1,DC=DomainComp2
```

where
                                 		  OrgUnit1 is an OU in the OrgUnit2 OU and DomainComp1 and DomainComp2 are the
                                 		  domain components. Domains usually have two domain components in AD, for
                                 		  example cisco and com for the cisco.com domain.

You can
                                 		  also specify multiple distinguished names (DNs) in a single input file to
                                 		  export contact lists for users from different OUs. The format of an input file
                                 		  with multiple DNs is as follows:

```
DN:OU=firstOU,DC=DomainComp1,DC=DomainComp2
DN:OU=secondOU,DC=DomainComp1,DC=DomainComp2
DN:OU=thirdOU,DC=DomainComp1,DC=DomainComp2
```

The
                                 		  following procedure describes how to export contact lists in bulk from the
                                 		  Microsoft server for migrating users.

Step 1

Copy and extract
                                          			 the zip file containing the Cisco user migration tools to the Standard Edition
                                          			 server or Enterprise Edition front-end server.

After
                                                         				  extraction, if you move any of the Cisco user migration tools to a different
                                                         				  location on the Microsoft server, you must also copy the version.txt file to the new location to ensure that
                                                         				  the tool prints out its current version.

Step 2

Open a command
                                          			 prompt and change directory to the location of the Export Contact List tool.

Step 3

At the command
                                          			 prompt, run the tool as follows:

If you want to...

Enter this command

Export the contact list for a list of users as specified in a
                                                         							 Microsoft server SIP URI input file

or

Export the contact list for a list of users in an Organizational
                                                         							 Unit in AD, as specified in a Users by Organizational Unit in AD input file

ExportContacts.exe -s/ LDAPServer -f/ input_file -l/ logLevel -r/ run_mode -i/ database_instance

where:

- LDAPServer —The IP or FQDN of the AD server where
                                                            								Microsoft server users are stored

- input_file —A text file that contains a list of
                                                            								Microsoft server SIP URIs, or, a text file that contains a list of
                                                            								distinguished names for AD Organizational Units that contain the users that you
                                                            								want to migrate

error

info

debug (recommended)

run_mode —The
                                                               								  run mode, which must be one of the following:

NORMAL

STATSONLY

database_instance —The Lync datastore instance name.
                                                               								  This parameter is required only when you are exporting contacts for Lync users.

Sample entries are as follows:

Lync 2010 Standard Edition server: localhost\rtc

Lync 2010 Enterprise Edition server: LyncDatastoreFqdn\rtc

Lync 2013 Standard Edition server: localhost\rtclocal

Lync 2013 Enterprise Edition server: AnyLyncFrontendServer\rtclocal

Export the contact list for all Microsoft server-enabled users
                                                         							 in the domain

ExportContacts.exe -s/ LDAPServer -f/ALL -l/ logLevel -r/ run_mode -i/ database_instance

where:

- LDAPServer —The IP or FQDN of the AD server where
                                                            								Microsoft server users are stored

error

info

debug (recommended)

NORMAL

STATSONLY

database_instance —The Lync datastore instance name.
                                                               								  This parameter is required only when you are exporting contacts for Lync users.

This command exports the contact lists for all Microsoft server
                                                                     								enabled users in the specified domain, regardless of whether they are migrating
                                                                     								to IM and Presence
                                                                        								  Service . If you use the UserList<Timestamp>.txt file, which is created
                                                                     								from this command, as input to the Disable Account tool and the Delete Account
                                                                     								tool, be aware that all user accounts in the domain are affected by the Disable
                                                                     								Account and Delete Account tools.

To ensure
                                                         				  correct contact list migration, the owners of the exported contact lists must
                                                         				  be completely disabled on the Microsoft server before you import the contacts
                                                         				  lists into IM and Presence
                                                            					 Service .

#### What to do next

Disable
                                    			 users on Lync/OCS/LCS

## Disable Users on
                        	 Microsoft Servers

This section
                           		describes procedures on how to disable a Skype for Business /Lync/OCS account for migrating users and how to verify that Active Directory updates are
                           		synchronized to the Microsoft server.

### Disable Microsoft
                           	 Server Account for Migrating Users

Cisco
                                 		  provides a tool to disable the Skype for Business /Lync/OCS account of migrating users. This tool (DisableAccount.exe) connects to Active
                                 		  Directory (AD) and updates the users’ Microsoft server attributes to disable
                                 		  their account. Running the Disable Account tool is the first step in a two-step
                                 		  process that must take place to disable a migrating user on the Microsoft
                                 		  server:

- Disable the Microsoft server
                                    			 user account for migrating user.

- Delete the Microsoft server
                                    			 user data for migrating user.

After you disable the account for migrating user, wait
                                 		  until the Microsoft server's LDAP changes are synchronized before proceeding
                                 		  with the Delete utility. The LDAP synchronization can take up to 30 minutes.

- You can run this tool on all
                                                				supported Microsoft server platforms.

You can run
                                                   				  this tool on any Standard Edition server or Enterprise Edition front-end
                                                   				  server.

Running this
                                                   				  tool has no affect on the capabilities of other Microsoft server users who are
                                                   				  signed into Microsoft Lync or Microsoft Office
                                                      					 Communicator . However, Cisco recommends that you run this tool during
                                                   				  a scheduled maintenance window to reduce the load on the Microsoft server and
                                                   				  Active Directory system.

The Disable Account
                                 		  tool accepts three inputs:

The IP or FQDN
                                       				of the AD server on which the Microsoft server users exist

An input file
                                       				containing the list of Microsoft server user accounts to disable

The logging
                                       				level, which should be one of error, info, or debug (debug is the recommended
                                       				setting)

The Disable Account
                                 		  tool reads the list of users to disable from an input file. Each line in the
                                 		  input file represents a contact list owner. The contact list owner is
                                 		  represented by the owner’s Microsoft server SIP URI, for example,
                                 		  sip:bobjones@cisco.com. The following is a sample input file:

```
sip:ann@cisco.com
sip:bob@cisco.com
sip:joe@cisco.com
sip@chuck@cisco.com
```

You can create your
                                 		  own input file based on the above format. however, Cisco recommends that you
                                 		  use the UserList<Timestamp>.txt file as the input file for the Disable
                                 		  Account tool. The UserList<Timestamp>.txt file does not contain any
                                 		  duplicate, disabled, or nonexistent users.

After you run the
                                 		  Disable Account tool, the tool generates a unique, time-stamped log file called
                                 		  DisableAccountLog<Timestamp>.txt in the same directory as the tool. The
                                 		  log file contains details about any failures or errors that occurred.

#### Before you begin

You must
                                 		  have read/write permission to AD to run this tool.

Step 1

Copy and extract
                                          			 the zip file containing the Cisco user migration tools to the Standard Edition
                                          			 server or Enterprise Edition front-end server.

After
                                                         				  extraction, if you move any of the Cisco user migration tools to a different
                                                         				  location on the Microsoft servers, you must also copy the version.txt file to
                                                         				  the new location to ensure that the tool prints out its current version.

Step 2

Open a command
                                          			 prompt and change directory to the location of the Disable Account tool.

Step 3

At the command
                                          			 prompt, enter the following command:

DisableAccount.exe -s/LDAPServer -f/ input_file -l/logLevel

where:

LDAPServer —The IP or
                                                   					 FQDN of the AD server on which the users exist

input_file —The file
                                                   					 containing the list of Microsoft server user accounts to disable,
                                                   					 UserList<Timestamp>.txt

logLevel —The logging
                                                   					 level, which must be one of error, info or debug (debug is the recommended
                                                   					 setting)

Step 4

Check the
                                          			 DisableAccountLog<Timestamp>.txt log file after each execution of the
                                          			 Disable Account tool to ensure that all users were successfully disabled.

#### What to do next

Verify That Active Directory Updates Synchronized to Microsoft Servers

### Verify That Active
                           	 Directory Updates Synchronized to Microsoft Servers

After the
                                 		  Active Directory updates are made to disable the Skype for Business /Lync/OCS accounts, the next step is to verify
                                 		  that those updates have synchronized to the Microsoft server. Verification
                                 		  takes place on the Standard Edition server or Enterprise Edition pool where the
                                 		  disabled Microsoft server account was provisioned. You must wait until the
                                 		  Microsoft server LDAP changes are synched before proceeding with the Delete
                                 		  utility.

Depending on your
                                             			 Microsoft server deployment, it may take up to 30 minutes for these changes to
                                             			 synchronize to the Microsoft server.

Step 1

Depending on
                                          			 your deployment, do one of the following:

If you are
                                                   					 using Lync Server 2010, choose Start > All
                                                         						  Programs > Microsoft Lync Server 2010 > Lync Server Control
                                                         						  Panel .

Tip

Choose Microsoft Lync Server 2013 if you are using
                                                                  						  Microsoft Lync Server 2013.

If you are
                                                   					 using OCS 2007 R2, choose Start > Programs > Administrative
                                                         						  Tools > Office Communications Server 2007 R2 Start > Programs >
                                                      						Administrative Tools > Office Communications Server 2007 R2 .

Step 2

Depending on
                                          			 your deployment, check the following:

For Lync,
                                                   					 choose Users and ensure that the disabled user no longer
                                                   					 appears in the list of users.

For OCS,
                                                   					 choose Users and ensure that the disabled user no longer
                                                   					 appears in the list of enabled OCS users.

#### What to do next

Delete User Data from Database for Migrating Users

## Delete User Data
                        	 from Database for Migrating Users

To delete user
                                          			 data from the Skype for Business /Lync/OCS database for migrating users, you must have read/write access to the Microsoft
                                          			 server database.

The
                              		  Microsoft server provides an administrative way to delete a user from the
                              		  Microsoft server database. However, if you delete a user from the database in
                              		  this way, the user is removed from other users’ contact lists. To prevent the
                              		  user being removed from the contact lists of other Microsoft Lync or Microsoft Office
                                 			 Communicator users, Cisco provides an alternative means of deleting
                              		  the user from the Microsoft server database.

This
                              		  alternative tool ( DeleteAccount.exe ) allows you to delete migrating
                              		  users so that availability requests for these users are later routed to IM and Presence Service . This tool also ensures that
                              		  the deleted users are not removed from the contact list of any users that
                              		  remain on the Microsoft server. Running the Delete Account tool is the second
                              		  step in a two-step process to disable a migrating user on the Microsoft server.
                              		  The two-step process is as follows:

Disable the
                                    				Microsoft server account for migrating user.

Delete the
                                    				Microsoft server user data for migrating user.

After you disable the account for migrating user, wait
                              		  until the Microsoft server's LDAP changes are synchronized before proceeding
                              		  with the Delete utility. The LDAP synchronization can take up to 30 minutes.

- You can run this tool on all
                                             				supported Microsoft server platforms.

You can run
                                                				  this tool on any Standard Edition server or Enterprise Edition pool.

Running this
                                                				  tool has no affect on the capabilities of other Microsoft server users who are
                                                				  signed into Microsoft Lync or Microsoft Office
                                                   					 Communicator . However, Cisco recommends that you run this tool during
                                                				  a scheduled maintenance window to reduce the load on the Microsoft server and
                                                				  Active Directory system.

The Delete Account
                              		  tool reads the list of users to delete from an input file. Each line in the
                              		  input file represents a contact list owner. The contact list owner is
                              		  represented by the owner’s Microsoft server SIP URI, for example,
                              		  sip:bobjones@cisco.com. The following is a sample input file:

```
sip:ann@cisco.com
sip:bob@cisco.com
sip:joe@cisco.com
sip@chuck@cisco.com
```

You can create your
                              		  own input file based on the above format. however, Cisco recommends that you
                              		  use the UserList<Timestamp>.txt file as the input file for the Delete
                              		  Account tool. The UserList<Timestamp>.txt file does not contain
                              		  any duplicate, disabled, or nonexistent users.

Running the Delete Account
                                 			 Tool on Standard Edition Deployments

When deleting data
                              		  for a list of users, you must run this tool once on each Standard Edition
                              		  server. The database is coresident on the Standard Edition server.

Running the Delete Account
                                 			 Tool on Enterprise Edition Deployments

When
                              		  deleting data for a list of users, you must run this tool once on each
                              		  Enterprise Edition pool. The Lync/OCS database instance name to which the
                              		  Microsoft server's front-end connects must be specified when running the tool.

Caution

For Lync
                                          			 Enterprise Edition, you must run this tool first on the back-end database
                                          			 server and then on each front-end server. The Lync database instance name to
                                          			 which the Lync front-end connects must be specified in both options. The name
                                          			 of the database for the front-end servers is rtclocal. The default name of the
                                          			 database for the back-end server is rtc, but that can be changed during system
                                          			 installation.

For
                                          			 OCS Enterprise Edition, the tool must be run on only the back-end database
                                          			 server.

Step 1

Ensure that you
                                       			 have read/write access to the Microsoft server database before you run this
                                       			 tool.

Step 2

Copy and extract
                                       			 the zip file containing the Cisco user migration tools to the Standard Edition
                                       			 server or one of the Enterprise Edition pool servers (front-end or back-end).

After
                                                      				  extraction, if you move any of the Cisco user migration tools to a different
                                                      				  location on the Microsoft server, you must also copy the version.txt file to the new location to ensure that
                                                      				  the tool prints out its current version.

Step 3

Open a command
                                       			 prompt and change directory to the location of the Delete Account tool.

Step 4

At the command
                                       			 prompt, enter the command as follows:

DeleteAccount.exe -s/ database_instance -f/ input_file -l/ logLevel

where:

database_instance —The database instance name of the
                                                					 Lync/OCS pool

input_file —The file containing the list of
                                                					 Microsoft server user accounts to delete, UserList<Timestamp>.txt

logLevel —The logging level, which must be one of
                                                					 error, info, or debug (debug is the recommended setting)

After the
                                                      				  command executes, the Delete Account tool generates a unique, time-stamped log
                                                      				  file called DeleteAccountLog<Timestamp>.txt in the same
                                                      				  directory as the tool. The log file contains details about any failures or
                                                      				  errors that have occurred.

Step 5

For each
                                       			 Standard Edition server or Enterprise Edition pool, repeat Steps 1 to 3.

For
                                          				troubleshooting tips, see Delete Account Tool

Step 6

If you are
                                       			 deleting user data from a Lync database you must also repeat Steps 2 to 4 on
                                       			 each front-end server. To access the front-end server database, the command in
                                       			 Step 4 must be run locally on the front-end server. In addition, you must use front-end_server_hostname \rtclocal as
                                       			 the value for the database instance parameter.

### What to do next

Import Contact Lists for Migrating Users into IM and Presence

## Import Contact Lists
                        	 for Migrating Users into IM and Presence

You can
                              		  use the IM and Presence Service Bulk Administration Tool (BAT)
                              		  to import Skype for Business /Lync/OCS user contact lists into IM and Presence Service .

Complete
                              		  the following steps to import the Microsoft server user contact lists into the IM and Presence Service :

- Upload the CSV File Using
                                 			 BAT.

- Create a New Bulk
                                 			 Administration Job.

- Check Results of Bulk
                                 			 Administration Job.

The default
                                          			 contact list import rate is based on the server hardware type. You can change
                                          			 the contact list import rate by logging in to the Cisco
                                             				Unified IM and Presence Administration user interface and choosing System > Service Parameters > Cisco Bulk Provisioning Service , then
                                          			 change the variable under Import Users Contact Rate. However, if you increase
                                          			 the default import rate, this results in a higher CPU and Memory usage on IM and Presence Service .

### Before you begin

The
                              		  procedure to import the Microsoft server user contact lists is one of the final
                              		  steps in the user migration process. Before you import the Microsoft server
                              		  user contact lists, you must complete the following procedures:

Provision the
                                    				Microsoft server users on Cisco Unified Communications Manager .

Ensure that the
                                    				Microsoft server users are licensed and assigned to IM and Presence
                                       				  Service .

Ensure that the IM and Presence
                                       				  Service Maximum Contact List Size and Maximum Watchers settings are
                                    				set to unlimited to ensure all contact lists are fully imported. See Set Unlimited Contact Lists and Watchers .

Run the Export
                                    				Contact List tool to produce the ExportedContacts<Timestamp>.csv file. See Export of Contact Lists for Migrating Users .

Ensure that the
                                    				Microsoft server users have been fully disabled on the Microsoft server. See Disable Users on Microsoft Servers .

### CSV File Upload
                           	 Using BAT

You must
                                 		  upload the ExportedContacts<Timestamp>.csv file to IM and Presence Service using the BAT. See Configuration
                                    			 and Administration of IM and Presence Service on Cisco Unified
                                    			 Communications Manager for instructions on how to upload the CSV file.

#### Related
                                 		  Topic

Configuration and
                                    			 Administration of IM and Presence Service on Cisco Unified Communications
                                    			 Manager

#### What To Do
                                 		  Next

Creation of a New Bulk Administration Job

### Creation of a New
                           	 Bulk Administration Job

After you
                                 		  upload the CSV file, you must create a new bulk administration job in the Cisco
                                    		  Unified CM IM and Presence Administration user interface to update the user contact lists. See Configuration and Administration of IM and Presence Service on
                                    				  Cisco Unified Communications Manager for instructions on how to create a new bulk administration
                                 		  job.

#### Related
                                 		  Topic

Configuration and Administration of  IM and
                                    			 Presence Service on Cisco Unified Communications Manager

#### What To Do
                                 		  Next

Results of Bulk Administration Job

### Results of Bulk
                           	 Administration Job

When the
                                 		  bulk administration job is complete, the IM and Presence Service Bulk Administration Tool writes the
                                 		  results of the contact list import job to a log file. See Configuration and Administration of IM and Presence Service on
                                    				  Cisco Unified Communications Manager for instructions on how to check the results of the
                                 		  bulk administration job.

#### What To Do
                                 		  Next

Deploy an IM and Presence Service Supported Client on Users Desktop

## Deploy an IM and
                        	 Presence Service Supported Client on Users Desktop

After you
                              		  provision the Skype for Business /Lync/OCS users on Cisco Unified Communications
                                 			 Manager and license them for IM and Presence Service and an IM and Presence Service supported client, you can
                              		  install the client software on the users’ desktops. See Configuration
                                 			 and Administration of IM and Presence Service on Cisco Unified
                                 			 Communications Manager for information about deploying IM and Presence Service supported clients.

## Reset Maximum
                        	 Contact List Size and Maximum Watcher Size

Before
                              		  migrating users from Skype for Business /Lync/OCS to IM and Presence Service , Cisco recommends that you set
                              		  the Maximum Contact List Size and Maximum Watchers settings on IM and Presence Service to unlimited. This ensures
                              		  that each migrated user contact list is fully imported to IM and Presence Service .

After all
                              		  users have been migrated to IM and Presence Service , reset the Maximum Contact
                              		  List Size and Maximum Watchers settings on IM and Presence Service to the desired values. The
                              		  system default value is 200 for Maximum Contact List Size and 200 for Maximum
                              		  Watchers size.

If you are
                                          			 performing a phased migration of users from the Microsoft server to IM and Presence Service , do not reset the Maximum
                                          			 Contact List Size and Maximum Watchers values until all users have been
                                          			 migrated.

The
                              		  following procedure describes how to set values for the Maximum Contact List
                              		  Size and Maximum Watchers settings.

If you have a
                                          			 multicluster deployment, you must perform this procedure on each cluster. When
                                          			 you change Presence settings, they are applied to all nodes in the cluster;
                                          			 therefore you need to set them only on the IM and Presence Service publisher node within any
                                          			 given cluster.

Step 1

Log in to the Cisco
                                          				Unified IM and Presence Administration user interface. Choose Presence > Settings .

Step 2

For Maximum Contact
                                          				List Size (per user) , uncheck the check box for No
                                          				Limit and enter the desired limit.

Step 3

For Maximum Watchers
                                          				(per user) , uncheck the check box for No
                                          				Limit and enter the desired limit.

Step 4

Click Save .

Step 5

Restart the
                                       			 Cisco XCP Router on all IM and Presence Service nodes in the cluster. To
                                       			 restart the Cisco XCP Router, log in to the Cisco
                                          				Unified IM and Presence Serviceability user interface and choose Tools > Control Center – Network
                                             				  Services .

| Tip | While attempting
                                          			 to run any of the user migration tools you may receive the following error:
                                          			 "Application failed to initialize properly". The reason for this error is that
                                          			 you are attempting to run the user migration tools without the .NET 2.0
                                          			 Framework installed. Each of the user migration tools that Cisco provides
                                          			 requires that at least version 2.0 of the .NET Framework is installed on the
                                          			 server where you are running the tool. The .NET 2.0
                                          			 Framework comes installed as standard on Windows Server 2003 R2 or newer. |
|---|---|

| Note | If you have a
                                             			 multicluster deployment, you must perform this procedure on each cluster. When
                                             			 you change Presence settings, they are applied to all nodes in the cluster;
                                             			 therefore you need to set them only on the IM and Presence Service database publisher node within
                                             			 any given cluster. |
|---|---|

| Step 1 | Log in to the Cisco
                                             				Unified IM and Presence Administration user interface. Choose Presence > Settings . |
|---|---|
| Step 2 | For Maximum
                                             				Contact List Size (per user) , check the No
                                             				Limit check box. |
| Step 3 | For Maximum Watchers
                                             				(per user) , check the No
                                             				Limit check box. |
| Step 4 | Click Save . |
| Step 5 | Restart the
                                          			 Cisco XCP Router on all IM and Presence Service nodes in the cluster. To
                                          			 restart the Cisco XCP Router, log in to the Cisco
                                             				Unified IM and Presence Serviceability user interface and choose Tools > Control Center – Network
                                                				  Services . |

| Note | This setting is
                                             			 enabled by default on IM and Presence Service . |
|---|---|

| Note | If you have a
                                             			 multicluster deployment, you must perform this procedure on each cluster. When
                                             			 you change Presence settings, they are applied to all nodes in the cluster;
                                             			 therefore you need to set them only on the IM and Presence database publisher
                                             			 node within any given cluster. |
|---|---|

| Step 1 | Log in to the Cisco
                                             				Unified IM and Presence Administration user interface. Choose Presence > Settings . |
|---|---|
| Step 2 | Check the check
                                          			 box for Allow
                                             				users to view the availability of other users without being prompted for
                                             				approval . |
| Step 3 | Click Save . |
| Step 4 | Restart the
                                          			 Cisco XCP Router on all IM and Presence Service nodes in the cluster. To
                                          			 restart the Cisco XCP Router, log in to the Cisco
                                             				Unified IM and Presence Serviceability user interface. Choose Tools > Control Center – Network
                                                				  Services . |

| Note | Disabling and
                                             			 enabling Microsoft Lync pop-ups requires a restart of the Lync front-end
                                             			 services. |
|---|---|

| Step 1 | On the Lync
                                             			 front-end server choose Start > All
                                                   				  Programs > Microsoft Lync Server
                                                   				  2010 > Lync Server Management
                                                   				  Shell . Tip Enter either
                                                            				  Microsoft Lync Server 2010 or 2013, depending on your Microsoft Lync Server
                                                            				  version. | Tip | Enter either
                                                            				  Microsoft Lync Server 2010 or 2013, depending on your Microsoft Lync Server
                                                            				  version. |
|---|---|---|---|
| Tip | Enter either
                                                            				  Microsoft Lync Server 2010 or 2013, depending on your Microsoft Lync Server
                                                            				  version. |
| Step 2 | Enter the
                                             			 following powershell command: Set-CSClientpolicy
                                                      				  -EnableNotificationForNewSubscriber $False |
| Step 3 | Choose Start > Programs > Administrative
                                                   				  Tools > Services . |
| Step 4 | Right-click
                                             			 the service Lync front end server and click Restart . |

| Tip | Enter either
                                                            				  Microsoft Lync Server 2010 or 2013, depending on your Microsoft Lync Server
                                                            				  version. |
|---|---|

| Step 1 | Enter the
                                             			 following command to restore client pop-up behavior on Lync: Set-CSClientpolicy
                                                      					 -EnableNotificationForNewSubscribers $Null |
|---|---|
| Step 2 | Choose Start > Programs > Administrative
                                                   				  Tools > Services . |
| Step 3 | Right-click
                                             			 the service Lync front end server and choose Restart . |

| Note | For releases
                                          			 earlier than release 10.0(1), you must modify all Microsoft server URIs before
                                          			 the first batch of users are migrated from a Microsoft server to IM and Presence
                                             				Service . |
|---|---|

| Step 1 | Verify that
                                       			 the IM address scheme is set to Directory URI and that the directory URI maps
                                       			 to msRTCSIP-PrimaryUserAddress on Cisco Unified Communications Manager . If the
                                       			 Directory URI IM address scheme is configured and is properly mapped, then
                                       			 alignment is guaranteed. If it is not possible to configure IM and Presence
                                          				Service to use the Directory URI address scheme, proceed to the next
                                       			 step. |
|---|---|
| Step 2 | Check that the
                                       			 format of the current IM address scheme for IM and Presence
                                          				Service matches the format that the Microsoft server uses. If the IM
                                       			 address formats do not align, then you must rename the users on the Microsoft
                                       			 server before migration. See the following procedures for more information
                                       			 about modifying the Microsoft server SIP URI. |

| Step 1 | From the Lync Control Panel, choose the Users  tab. |
|---|---|
| Step 2 | Search for the user that you want to change and double-click the user. |
| Step 3 | Change the SIP address field. |
| Step 4 | Click Commit . Tip To modify SIP URIs in bulk, use the Set-CsUser cmdlet. For more information, see http://technet.microsoft.com/en-us/library/gg398510.aspx . | Tip | To modify SIP URIs in bulk, use the Set-CsUser cmdlet. For more information, see http://technet.microsoft.com/en-us/library/gg398510.aspx . |
| Tip | To modify SIP URIs in bulk, use the Set-CsUser cmdlet. For more information, see http://technet.microsoft.com/en-us/library/gg398510.aspx . |

| Tip | To modify SIP URIs in bulk, use the Set-CsUser cmdlet. For more information, see http://technet.microsoft.com/en-us/library/gg398510.aspx . |
|---|---|

| Step 1 | On the Active Directory
                                          			 server, choose Start > Control
                                                				  Panel > Administrative Tools > Active
                                                				  Directory Users and Computers . |
|---|---|
| Step 2 | Search for the user that you want to change and double-click the
                                          			 user. |
| Step 3 | From the Properties window, choose the 
                                          			 Live Communications tab. |
| Step 4 | Change the 
                                          			 SIP URI field. |
| Step 5 | Click OK . Note To modify SIP URIs in bulk, use the System.DirectoryServices
                                                         				  that are provided by Microsoft to update the msRTCSIP-PrimaryUserAddress
                                                         				  property for each affected user. For more information, see http://msdn.microsoft.com/en-us/library/ms180835(v=vs.80).aspx . | Note | To modify SIP URIs in bulk, use the System.DirectoryServices
                                                         				  that are provided by Microsoft to update the msRTCSIP-PrimaryUserAddress
                                                         				  property for each affected user. For more information, see http://msdn.microsoft.com/en-us/library/ms180835(v=vs.80).aspx . |
| Note | To modify SIP URIs in bulk, use the System.DirectoryServices
                                                         				  that are provided by Microsoft to update the msRTCSIP-PrimaryUserAddress
                                                         				  property for each affected user. For more information, see http://msdn.microsoft.com/en-us/library/ms180835(v=vs.80).aspx . |

| Note | To modify SIP URIs in bulk, use the System.DirectoryServices
                                                         				  that are provided by Microsoft to update the msRTCSIP-PrimaryUserAddress
                                                         				  property for each affected user. For more information, see http://msdn.microsoft.com/en-us/library/ms180835(v=vs.80).aspx . |
|---|---|

| Note | This
                                                				  procedure is necessary only if you modified any Skype for Business /Lync/OCS SIP URIs . For more information about URI formats, see topics related to
                                                				  maintaining user identity during migration. You must
                                                				  complete this procedure before the modified Microsoft server users are enabled
                                                				  for IM and Presence
                                                   					 Service . Cisco
                                                				  recommends that you run this tool during a scheduled maintenance window. |
|---|---|

| Note | It is your
                                                				  responsibility to compile the CSV file with the appropriate contact IDs. You must
                                                				  ensure that the header Contact ID, New Contact ID is present in all CSV files. |
|---|---|

| Note | You must
                                          			 complete this procedure on each IM and Presence
                                             				Service cluster. |
|---|---|

| Step 1 | Upload the CSV
                                       			 file with the list of contact IDs that you want to rename in all contact lists.
                                       			 Do the following: On the IM and Presence
                                                					 Service database publisher node, log in to the Cisco Unified CM IM and Presence Administration user
                                             				  interface. Choose Bulk
                                                   						Administration > Upload/Download Files . Click Add New . Click Browse to locate and choose the CSV file. Choose Contact as the Target. Choose Rename Contacts – Custom File as the Transaction
                                             				  Type. Click Save to upload the file. |
|---|---|
| Step 2 | On the
                                       			 publisher node, log in to the Cisco
                                          				Unified CM IM and Presence Administration user interface. Choose Bulk
                                             				  Administration > Contact List > Rename
                                             				  Contacts . |
| Step 3 | In the File
                                          				Name field, choose the file that you uploaded. |
| Step 4 | Choose one of
                                       			 the following actions: Click Run
                                             				  Immediately to execute the Bulk Administration job immediately. Click Run
                                             				  Later to schedule a time to execute the Bulk Administration job.
                                          				For more information about scheduling jobs in the BAT, see the Online Help in Cisco Unified CM IM and Presence Administration . |
| Step 5 | Click Submit . If you chose to run the job immediately, the
                                       			 job runs after you click Submit. |

| Note | The Job Results
                                             			 area on the Job Scheduler window is shown only when the CSV file has been
                                             			 processed. The Number of Records Processed and the Number of Records Failed
                                             			 values do not represent the number of entries that were processed on the CSV
                                             			 file; these values represent the number of contact lists that have been updated
                                             			 and the number of failed contact list updates. |
|---|---|

| Note | After users are
                                          			 provisioned on Cisco Unified Communications Manager and IM and Presence Service , Cisco recommends that you
                                          			 complete the full user migration process during the same maintenance window.
                                          			 Leaving users provisioned on both IM and Presence Service and on the Microsoft servers
                                          			 for any time period disrupts message routing for those users. |
|---|---|

| Note | You can run this tool against
                                             				all the supported Microsoft server platforms. You can run
                                                				  the tool on any Standard Edition server or Enterprise Edition front-end server. To export
                                                				  contact lists for Lync users, the Export Contact List tool requires read access
                                                				  to the Lync RTC database and also read access to LDAP. You must also ensure
                                                				  that dbo execution account privileges are granted to the RTC database. Running this
                                                				  tool has no affect on the capabilities of other Microsoft server users who are
                                                				  signed into Microsoft Lync or Microsoft Office Communicator. However, Cisco
                                                				  recommends that you run this tool during a scheduled maintenance window to
                                                				  reduce the load on the Microsoft server and Active Directory system. |
|---|---|

| Note | You can use the
                                          			 UserList<Timestamp>.txt file as input to the Disable Account tool and the
                                          			 Delete Account tool. |
|---|---|

| Note | If you use
                                             			 choose to export all users with the Export Contact List tool, the resulting UserList<Timestamp>.txt file contains the
                                             			 contact lists of all Microsoft server-enabled users in the domain, regardless
                                             			 of whether they are migrating to IM and Presence
                                                				Service . If you later use the UserList<Timestamp>.txt file as input to the
                                             			 Disable Account tool and the Delete Account tool, be aware that all user
                                             			 accounts in the domain are affected by the Disable Account and Delete Account
                                             			 tools. |
|---|---|

| Step 1 | Copy and extract
                                          			 the zip file containing the Cisco user migration tools to the Standard Edition
                                          			 server or Enterprise Edition front-end server. Note After
                                                         				  extraction, if you move any of the Cisco user migration tools to a different
                                                         				  location on the Microsoft server, you must also copy the version.txt file to the new location to ensure that
                                                         				  the tool prints out its current version. | Note | After
                                                         				  extraction, if you move any of the Cisco user migration tools to a different
                                                         				  location on the Microsoft server, you must also copy the version.txt file to the new location to ensure that
                                                         				  the tool prints out its current version. |
|---|---|---|---|
| Note | After
                                                         				  extraction, if you move any of the Cisco user migration tools to a different
                                                         				  location on the Microsoft server, you must also copy the version.txt file to the new location to ensure that
                                                         				  the tool prints out its current version. |
| Step 2 | Open a command
                                          			 prompt and change directory to the location of the Export Contact List tool. |
| Step 3 | At the command
                                          			 prompt, run the tool as follows: If you want to... Enter this command Export the contact list for a list of users as specified in a
                                                         							 Microsoft server SIP URI input file or Export the contact list for a list of users in an Organizational
                                                         							 Unit in AD, as specified in a Users by Organizational Unit in AD input file ExportContacts.exe -s/ LDAPServer -f/ input_file -l/ logLevel -r/ run_mode -i/ database_instance where: LDAPServer —The IP or FQDN of the AD server where
                                                            								Microsoft server users are stored input_file —A text file that contains a list of
                                                            								Microsoft server SIP URIs, or, a text file that contains a list of
                                                            								distinguished names for AD Organizational Units that contain the users that you
                                                            								want to migrate logLevel —The logging level, which must be one of
                                                            								the following: error info debug (recommended) run_mode —The
                                                               								  run mode, which must be one of the following: NORMAL STATSONLY database_instance —The Lync datastore instance name.
                                                               								  This parameter is required only when you are exporting contacts for Lync users. Sample entries are as follows: Lync 2010 Standard Edition server: localhost\rtc Lync 2010 Enterprise Edition server: LyncDatastoreFqdn\rtc Lync 2013 Standard Edition server: localhost\rtclocal Lync 2013 Enterprise Edition server: AnyLyncFrontendServer\rtclocal Export the contact list for all Microsoft server-enabled users
                                                         							 in the domain ExportContacts.exe -s/ LDAPServer -f/ALL -l/ logLevel -r/ run_mode -i/ database_instance where: LDAPServer —The IP or FQDN of the AD server where
                                                            								Microsoft server users are stored logLevel —The logging level, which must be one of
                                                            								the following: error info debug (recommended) run_mode —The
                                                               								  run mode, which must be one of the following: NORMAL STATSONLY database_instance —The Lync datastore instance name.
                                                               								  This parameter is required only when you are exporting contacts for Lync users. Note This command exports the contact lists for all Microsoft server
                                                                     								enabled users in the specified domain, regardless of whether they are migrating
                                                                     								to IM and Presence
                                                                        								  Service . If you use the UserList<Timestamp>.txt file, which is created
                                                                     								from this command, as input to the Disable Account tool and the Delete Account
                                                                     								tool, be aware that all user accounts in the domain are affected by the Disable
                                                                     								Account and Delete Account tools. Note To ensure
                                                         				  correct contact list migration, the owners of the exported contact lists must
                                                         				  be completely disabled on the Microsoft server before you import the contacts
                                                         				  lists into IM and Presence
                                                            					 Service . | If you want to... | Enter this command | Export the contact list for a list of users as specified in a
                                                         							 Microsoft server SIP URI input file or Export the contact list for a list of users in an Organizational
                                                         							 Unit in AD, as specified in a Users by Organizational Unit in AD input file | ExportContacts.exe -s/ LDAPServer -f/ input_file -l/ logLevel -r/ run_mode -i/ database_instance where: LDAPServer —The IP or FQDN of the AD server where
                                                            								Microsoft server users are stored input_file —A text file that contains a list of
                                                            								Microsoft server SIP URIs, or, a text file that contains a list of
                                                            								distinguished names for AD Organizational Units that contain the users that you
                                                            								want to migrate logLevel —The logging level, which must be one of
                                                            								the following: error info debug (recommended) run_mode —The
                                                               								  run mode, which must be one of the following: NORMAL STATSONLY database_instance —The Lync datastore instance name.
                                                               								  This parameter is required only when you are exporting contacts for Lync users. Sample entries are as follows: Lync 2010 Standard Edition server: localhost\rtc Lync 2010 Enterprise Edition server: LyncDatastoreFqdn\rtc Lync 2013 Standard Edition server: localhost\rtclocal Lync 2013 Enterprise Edition server: AnyLyncFrontendServer\rtclocal | Export the contact list for all Microsoft server-enabled users
                                                         							 in the domain | ExportContacts.exe -s/ LDAPServer -f/ALL -l/ logLevel -r/ run_mode -i/ database_instance where: LDAPServer —The IP or FQDN of the AD server where
                                                            								Microsoft server users are stored logLevel —The logging level, which must be one of
                                                            								the following: error info debug (recommended) run_mode —The
                                                               								  run mode, which must be one of the following: NORMAL STATSONLY database_instance —The Lync datastore instance name.
                                                               								  This parameter is required only when you are exporting contacts for Lync users. Note This command exports the contact lists for all Microsoft server
                                                                     								enabled users in the specified domain, regardless of whether they are migrating
                                                                     								to IM and Presence
                                                                        								  Service . If you use the UserList<Timestamp>.txt file, which is created
                                                                     								from this command, as input to the Disable Account tool and the Delete Account
                                                                     								tool, be aware that all user accounts in the domain are affected by the Disable
                                                                     								Account and Delete Account tools. | Note | This command exports the contact lists for all Microsoft server
                                                                     								enabled users in the specified domain, regardless of whether they are migrating
                                                                     								to IM and Presence
                                                                        								  Service . If you use the UserList<Timestamp>.txt file, which is created
                                                                     								from this command, as input to the Disable Account tool and the Delete Account
                                                                     								tool, be aware that all user accounts in the domain are affected by the Disable
                                                                     								Account and Delete Account tools. | Note | To ensure
                                                         				  correct contact list migration, the owners of the exported contact lists must
                                                         				  be completely disabled on the Microsoft server before you import the contacts
                                                         				  lists into IM and Presence
                                                            					 Service . |
| If you want to... | Enter this command |
| Export the contact list for a list of users as specified in a
                                                         							 Microsoft server SIP URI input file or Export the contact list for a list of users in an Organizational
                                                         							 Unit in AD, as specified in a Users by Organizational Unit in AD input file | ExportContacts.exe -s/ LDAPServer -f/ input_file -l/ logLevel -r/ run_mode -i/ database_instance where: LDAPServer —The IP or FQDN of the AD server where
                                                            								Microsoft server users are stored input_file —A text file that contains a list of
                                                            								Microsoft server SIP URIs, or, a text file that contains a list of
                                                            								distinguished names for AD Organizational Units that contain the users that you
                                                            								want to migrate logLevel —The logging level, which must be one of
                                                            								the following: error info debug (recommended) run_mode —The
                                                               								  run mode, which must be one of the following: NORMAL STATSONLY database_instance —The Lync datastore instance name.
                                                               								  This parameter is required only when you are exporting contacts for Lync users. Sample entries are as follows: Lync 2010 Standard Edition server: localhost\rtc Lync 2010 Enterprise Edition server: LyncDatastoreFqdn\rtc Lync 2013 Standard Edition server: localhost\rtclocal Lync 2013 Enterprise Edition server: AnyLyncFrontendServer\rtclocal |
| Export the contact list for all Microsoft server-enabled users
                                                         							 in the domain | ExportContacts.exe -s/ LDAPServer -f/ALL -l/ logLevel -r/ run_mode -i/ database_instance where: LDAPServer —The IP or FQDN of the AD server where
                                                            								Microsoft server users are stored logLevel —The logging level, which must be one of
                                                            								the following: error info debug (recommended) run_mode —The
                                                               								  run mode, which must be one of the following: NORMAL STATSONLY database_instance —The Lync datastore instance name.
                                                               								  This parameter is required only when you are exporting contacts for Lync users. Note This command exports the contact lists for all Microsoft server
                                                                     								enabled users in the specified domain, regardless of whether they are migrating
                                                                     								to IM and Presence
                                                                        								  Service . If you use the UserList<Timestamp>.txt file, which is created
                                                                     								from this command, as input to the Disable Account tool and the Delete Account
                                                                     								tool, be aware that all user accounts in the domain are affected by the Disable
                                                                     								Account and Delete Account tools. | Note | This command exports the contact lists for all Microsoft server
                                                                     								enabled users in the specified domain, regardless of whether they are migrating
                                                                     								to IM and Presence
                                                                        								  Service . If you use the UserList<Timestamp>.txt file, which is created
                                                                     								from this command, as input to the Disable Account tool and the Delete Account
                                                                     								tool, be aware that all user accounts in the domain are affected by the Disable
                                                                     								Account and Delete Account tools. |
| Note | This command exports the contact lists for all Microsoft server
                                                                     								enabled users in the specified domain, regardless of whether they are migrating
                                                                     								to IM and Presence
                                                                        								  Service . If you use the UserList<Timestamp>.txt file, which is created
                                                                     								from this command, as input to the Disable Account tool and the Delete Account
                                                                     								tool, be aware that all user accounts in the domain are affected by the Disable
                                                                     								Account and Delete Account tools. |
| Note | To ensure
                                                         				  correct contact list migration, the owners of the exported contact lists must
                                                         				  be completely disabled on the Microsoft server before you import the contacts
                                                         				  lists into IM and Presence
                                                            					 Service . |

| Note | After
                                                         				  extraction, if you move any of the Cisco user migration tools to a different
                                                         				  location on the Microsoft server, you must also copy the version.txt file to the new location to ensure that
                                                         				  the tool prints out its current version. |
|---|---|

| If you want to... | Enter this command |
|---|---|
| Export the contact list for a list of users as specified in a
                                                         							 Microsoft server SIP URI input file or Export the contact list for a list of users in an Organizational
                                                         							 Unit in AD, as specified in a Users by Organizational Unit in AD input file | ExportContacts.exe -s/ LDAPServer -f/ input_file -l/ logLevel -r/ run_mode -i/ database_instance where: LDAPServer —The IP or FQDN of the AD server where
                                                            								Microsoft server users are stored input_file —A text file that contains a list of
                                                            								Microsoft server SIP URIs, or, a text file that contains a list of
                                                            								distinguished names for AD Organizational Units that contain the users that you
                                                            								want to migrate logLevel —The logging level, which must be one of
                                                            								the following: error info debug (recommended) run_mode —The
                                                               								  run mode, which must be one of the following: NORMAL STATSONLY database_instance —The Lync datastore instance name.
                                                               								  This parameter is required only when you are exporting contacts for Lync users. Sample entries are as follows: Lync 2010 Standard Edition server: localhost\rtc Lync 2010 Enterprise Edition server: LyncDatastoreFqdn\rtc Lync 2013 Standard Edition server: localhost\rtclocal Lync 2013 Enterprise Edition server: AnyLyncFrontendServer\rtclocal |
| Export the contact list for all Microsoft server-enabled users
                                                         							 in the domain | ExportContacts.exe -s/ LDAPServer -f/ALL -l/ logLevel -r/ run_mode -i/ database_instance where: LDAPServer —The IP or FQDN of the AD server where
                                                            								Microsoft server users are stored logLevel —The logging level, which must be one of
                                                            								the following: error info debug (recommended) run_mode —The
                                                               								  run mode, which must be one of the following: NORMAL STATSONLY database_instance —The Lync datastore instance name.
                                                               								  This parameter is required only when you are exporting contacts for Lync users. Note This command exports the contact lists for all Microsoft server
                                                                     								enabled users in the specified domain, regardless of whether they are migrating
                                                                     								to IM and Presence
                                                                        								  Service . If you use the UserList<Timestamp>.txt file, which is created
                                                                     								from this command, as input to the Disable Account tool and the Delete Account
                                                                     								tool, be aware that all user accounts in the domain are affected by the Disable
                                                                     								Account and Delete Account tools. | Note | This command exports the contact lists for all Microsoft server
                                                                     								enabled users in the specified domain, regardless of whether they are migrating
                                                                     								to IM and Presence
                                                                        								  Service . If you use the UserList<Timestamp>.txt file, which is created
                                                                     								from this command, as input to the Disable Account tool and the Delete Account
                                                                     								tool, be aware that all user accounts in the domain are affected by the Disable
                                                                     								Account and Delete Account tools. |
| Note | This command exports the contact lists for all Microsoft server
                                                                     								enabled users in the specified domain, regardless of whether they are migrating
                                                                     								to IM and Presence
                                                                        								  Service . If you use the UserList<Timestamp>.txt file, which is created
                                                                     								from this command, as input to the Disable Account tool and the Delete Account
                                                                     								tool, be aware that all user accounts in the domain are affected by the Disable
                                                                     								Account and Delete Account tools. |

| Note | This command exports the contact lists for all Microsoft server
                                                                     								enabled users in the specified domain, regardless of whether they are migrating
                                                                     								to IM and Presence
                                                                        								  Service . If you use the UserList<Timestamp>.txt file, which is created
                                                                     								from this command, as input to the Disable Account tool and the Delete Account
                                                                     								tool, be aware that all user accounts in the domain are affected by the Disable
                                                                     								Account and Delete Account tools. |
|---|---|

| Note | To ensure
                                                         				  correct contact list migration, the owners of the exported contact lists must
                                                         				  be completely disabled on the Microsoft server before you import the contacts
                                                         				  lists into IM and Presence
                                                            					 Service . |
|---|---|

| Note | You can run this tool on all
                                                				supported Microsoft server platforms. You can run
                                                   				  this tool on any Standard Edition server or Enterprise Edition front-end
                                                   				  server. Running this
                                                   				  tool has no affect on the capabilities of other Microsoft server users who are
                                                   				  signed into Microsoft Lync or Microsoft Office
                                                      					 Communicator . However, Cisco recommends that you run this tool during
                                                   				  a scheduled maintenance window to reduce the load on the Microsoft server and
                                                   				  Active Directory system. |
|---|---|

| Step 1 | Copy and extract
                                          			 the zip file containing the Cisco user migration tools to the Standard Edition
                                          			 server or Enterprise Edition front-end server. Note After
                                                         				  extraction, if you move any of the Cisco user migration tools to a different
                                                         				  location on the Microsoft servers, you must also copy the version.txt file to
                                                         				  the new location to ensure that the tool prints out its current version. | Note | After
                                                         				  extraction, if you move any of the Cisco user migration tools to a different
                                                         				  location on the Microsoft servers, you must also copy the version.txt file to
                                                         				  the new location to ensure that the tool prints out its current version. |
|---|---|---|---|
| Note | After
                                                         				  extraction, if you move any of the Cisco user migration tools to a different
                                                         				  location on the Microsoft servers, you must also copy the version.txt file to
                                                         				  the new location to ensure that the tool prints out its current version. |
| Step 2 | Open a command
                                          			 prompt and change directory to the location of the Disable Account tool. |
| Step 3 | At the command
                                          			 prompt, enter the following command: DisableAccount.exe -s/LDAPServer -f/ input_file -l/logLevel where: LDAPServer —The IP or
                                                   					 FQDN of the AD server on which the users exist input_file —The file
                                                   					 containing the list of Microsoft server user accounts to disable,
                                                   					 UserList<Timestamp>.txt logLevel —The logging
                                                   					 level, which must be one of error, info or debug (debug is the recommended
                                                   					 setting) |
| Step 4 | Check the
                                          			 DisableAccountLog<Timestamp>.txt log file after each execution of the
                                          			 Disable Account tool to ensure that all users were successfully disabled. |

| Note | After
                                                         				  extraction, if you move any of the Cisco user migration tools to a different
                                                         				  location on the Microsoft servers, you must also copy the version.txt file to
                                                         				  the new location to ensure that the tool prints out its current version. |
|---|---|

| Note | Depending on your
                                             			 Microsoft server deployment, it may take up to 30 minutes for these changes to
                                             			 synchronize to the Microsoft server. |
|---|---|

| Step 1 | Depending on
                                          			 your deployment, do one of the following: If you are
                                                   					 using Lync Server 2010, choose Start > All
                                                         						  Programs > Microsoft Lync Server 2010 > Lync Server Control
                                                         						  Panel . Tip Choose Microsoft Lync Server 2013 if you are using
                                                                  						  Microsoft Lync Server 2013. If you are
                                                   					 using OCS 2007 R2, choose Start > Programs > Administrative
                                                         						  Tools > Office Communications Server 2007 R2 Start > Programs >
                                                      						Administrative Tools > Office Communications Server 2007 R2 . | Tip | Choose Microsoft Lync Server 2013 if you are using
                                                                  						  Microsoft Lync Server 2013. |
|---|---|---|---|
| Tip | Choose Microsoft Lync Server 2013 if you are using
                                                                  						  Microsoft Lync Server 2013. |
| Step 2 | Depending on
                                          			 your deployment, check the following: For Lync,
                                                   					 choose Users and ensure that the disabled user no longer
                                                   					 appears in the list of users. For OCS,
                                                   					 choose Users and ensure that the disabled user no longer
                                                   					 appears in the list of enabled OCS users. |

| Tip | Choose Microsoft Lync Server 2013 if you are using
                                                                  						  Microsoft Lync Server 2013. |
|---|---|

| Note | To delete user
                                          			 data from the Skype for Business /Lync/OCS database for migrating users, you must have read/write access to the Microsoft
                                          			 server database. |
|---|---|

| Note | You can run this tool on all
                                             				supported Microsoft server platforms. You can run
                                                				  this tool on any Standard Edition server or Enterprise Edition pool. Running this
                                                				  tool has no affect on the capabilities of other Microsoft server users who are
                                                				  signed into Microsoft Lync or Microsoft Office
                                                   					 Communicator . However, Cisco recommends that you run this tool during
                                                				  a scheduled maintenance window to reduce the load on the Microsoft server and
                                                				  Active Directory system. |
|---|---|

| Caution | For Lync
                                          			 Enterprise Edition, you must run this tool first on the back-end database
                                          			 server and then on each front-end server. The Lync database instance name to
                                          			 which the Lync front-end connects must be specified in both options. The name
                                          			 of the database for the front-end servers is rtclocal. The default name of the
                                          			 database for the back-end server is rtc, but that can be changed during system
                                          			 installation. For
                                          			 OCS Enterprise Edition, the tool must be run on only the back-end database
                                          			 server. |
|---|---|

| Step 1 | Ensure that you
                                       			 have read/write access to the Microsoft server database before you run this
                                       			 tool. |
|---|---|
| Step 2 | Copy and extract
                                       			 the zip file containing the Cisco user migration tools to the Standard Edition
                                       			 server or one of the Enterprise Edition pool servers (front-end or back-end). Note After
                                                      				  extraction, if you move any of the Cisco user migration tools to a different
                                                      				  location on the Microsoft server, you must also copy the version.txt file to the new location to ensure that
                                                      				  the tool prints out its current version. | Note | After
                                                      				  extraction, if you move any of the Cisco user migration tools to a different
                                                      				  location on the Microsoft server, you must also copy the version.txt file to the new location to ensure that
                                                      				  the tool prints out its current version. |
| Note | After
                                                      				  extraction, if you move any of the Cisco user migration tools to a different
                                                      				  location on the Microsoft server, you must also copy the version.txt file to the new location to ensure that
                                                      				  the tool prints out its current version. |
| Step 3 | Open a command
                                       			 prompt and change directory to the location of the Delete Account tool. |
| Step 4 | At the command
                                       			 prompt, enter the command as follows: DeleteAccount.exe -s/ database_instance -f/ input_file -l/ logLevel where: database_instance —The database instance name of the
                                                					 Lync/OCS pool input_file —The file containing the list of
                                                					 Microsoft server user accounts to delete, UserList<Timestamp>.txt logLevel —The logging level, which must be one of
                                                					 error, info, or debug (debug is the recommended setting) Note After the
                                                      				  command executes, the Delete Account tool generates a unique, time-stamped log
                                                      				  file called DeleteAccountLog<Timestamp>.txt in the same
                                                      				  directory as the tool. The log file contains details about any failures or
                                                      				  errors that have occurred. | Note | After the
                                                      				  command executes, the Delete Account tool generates a unique, time-stamped log
                                                      				  file called DeleteAccountLog<Timestamp>.txt in the same
                                                      				  directory as the tool. The log file contains details about any failures or
                                                      				  errors that have occurred. |
| Note | After the
                                                      				  command executes, the Delete Account tool generates a unique, time-stamped log
                                                      				  file called DeleteAccountLog<Timestamp>.txt in the same
                                                      				  directory as the tool. The log file contains details about any failures or
                                                      				  errors that have occurred. |
| Step 5 | For each
                                       			 Standard Edition server or Enterprise Edition pool, repeat Steps 1 to 3. For
                                          				troubleshooting tips, see Delete Account Tool |
| Step 6 | If you are
                                       			 deleting user data from a Lync database you must also repeat Steps 2 to 4 on
                                       			 each front-end server. To access the front-end server database, the command in
                                       			 Step 4 must be run locally on the front-end server. In addition, you must use front-end_server_hostname \rtclocal as
                                       			 the value for the database instance parameter. |

| Note | After
                                                      				  extraction, if you move any of the Cisco user migration tools to a different
                                                      				  location on the Microsoft server, you must also copy the version.txt file to the new location to ensure that
                                                      				  the tool prints out its current version. |
|---|---|

| Note | After the
                                                      				  command executes, the Delete Account tool generates a unique, time-stamped log
                                                      				  file called DeleteAccountLog<Timestamp>.txt in the same
                                                      				  directory as the tool. The log file contains details about any failures or
                                                      				  errors that have occurred. |
|---|---|

| Note | The default
                                          			 contact list import rate is based on the server hardware type. You can change
                                          			 the contact list import rate by logging in to the Cisco
                                             				Unified IM and Presence Administration user interface and choosing System > Service Parameters > Cisco Bulk Provisioning Service , then
                                          			 change the variable under Import Users Contact Rate. However, if you increase
                                          			 the default import rate, this results in a higher CPU and Memory usage on IM and Presence Service . |
|---|---|

| Note | If you are
                                          			 performing a phased migration of users from the Microsoft server to IM and Presence Service , do not reset the Maximum
                                          			 Contact List Size and Maximum Watchers values until all users have been
                                          			 migrated. |
|---|---|

| Note | If you have a
                                          			 multicluster deployment, you must perform this procedure on each cluster. When
                                          			 you change Presence settings, they are applied to all nodes in the cluster;
                                          			 therefore you need to set them only on the IM and Presence Service publisher node within any
                                          			 given cluster. |
|---|---|

| Step 1 | Log in to the Cisco
                                          				Unified IM and Presence Administration user interface. Choose Presence > Settings . |
|---|---|
| Step 2 | For Maximum Contact
                                          				List Size (per user) , uncheck the check box for No
                                          				Limit and enter the desired limit. |
| Step 3 | For Maximum Watchers
                                          				(per user) , uncheck the check box for No
                                          				Limit and enter the desired limit. |
| Step 4 | Click Save . |
| Step 5 | Restart the
                                       			 Cisco XCP Router on all IM and Presence Service nodes in the cluster. To
                                       			 restart the Cisco XCP Router, log in to the Cisco
                                          				Unified IM and Presence Serviceability user interface and choose Tools > Control Center – Network
                                             				  Services . |