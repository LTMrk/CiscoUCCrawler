---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-networking-guide-b-15cucnext-b-14cucnetx-chapter-011-html-312cab7ab1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/networking/guide/b_15cucnext/b_14cucnetx_chapter_011.html
retrieved_at: 2026-08-17T03:33:12.661956+00:00
---

Networking Guide for Cisco Unity Connection Release 15

# Networking Guide for Cisco Unity Connection Release 15

Updated: December 18, 2023

Chapter: VPIM Networking

## Chapter: VPIM Networking

# VPIM Networking

## Introduction

Cisco Unity Connection supports the Voice Profile for Internet Mail (VPIM), an industry standard protocol that allows different
                           voice messaging systems to exchange voice and text messages over the Internet or any TCP/IP network. VPIM is based on the
                           Simple Mail Transfer Protocol (SMTP) and the Multi-Purpose Internet Mail Extension (MIME) protocols.

VPIM Networking can be used for messaging between Unity Connection 2.x and later servers, or between Unity Connection 2.x
                           and later servers and other VPIM-compatible voice messaging systems such as Cisco Unity 4.0 and later.

Additional server discovery and directory synchronization functionality is available when you use Digital Networking rather
                                       than VPIM to connect multiple Unity Connection 2.x and later servers.

## Setting Up VPIM
                        	 Networking

This section describes the prerequisites for setting up VPIM
                           		Networking, and provides a task list containing a high-level view of all of the
                           		tasks you need to complete for the setup, and the order in which they should be
                           		completed. If you are unfamiliar with VPIM Networking, you should first read
                           		the “VPIM
                              		  Messages” section on page 4-15 and then review the task list and
                           		procedures before beginning the setup.

### Prerequisites

Before starting the setup, verify that the following
                              		prerequisites have been met:

Cisco Unity Connection is already installed and connected to the
                                    			 network.

The remote voice messaging system that Unity Connection is networked with is listed in the “Requirements for VPIM Networking”
                                    section of the applicable system requirements document: System Requirements for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/requirements/b_15cucsysreqs.html .

### Task List: Setting
                           	 Up Cisco Unity Connection to Use VPIM Networking

Use the task list that follows to set up VPIM Networking in
                              		Cisco Unity Connection. The links take you to detailed procedures for the
                              		setup.

Make decisions about your numbering plan and gather information
                                    			 needed to configure VPIM Networking. See the “Making
                                       				Design Decisions and Gathering Needed Information” section on page 4-2 .

Determine the domain name that is used for messaging between the
                                    			 remote voice messaging system and Unity Connection. See the “Determining
                                       				the Domain Name” section on page 4-3 .

As applicable, configure DNS files. See the “Resolving
                                       				Names with IP Addresses” section on page 4-4 .

Verify network and SMTP connectivity with the remote voice
                                    			 messaging system. See the “Verifying
                                       				Connectivity with the Remote Voice Messaging System” section on
                                       				page 4-4 .

Create the VPIM locations for each remote voice messaging
                                    			 system. See the “Creating
                                       				VPIM Locations” section on page 4-5 .

Create VPIM contacts for each VPIM location. See the “Creating
                                       				VPIM Contacts” section on page 4-6 .

Optionally, customize the contact creation settings for each
                                    			 VPIM location. See the “Customizing
                                       				VPIM Contact Directory Update Settings” section on page 4-10 .

Optionally, add an alternate name for each VPIM location. See
                                    			 the “Adding
                                       				Alternate Names for Each VPIM Location” section on page 4-13 .

Set up the remote voice messaging system for VPIM. Precisely how
                                    			 this is done depends on the voice messaging system. However, you need to
                                    			 provide the remote system with information about Unity Connection. See the “Gathering
                                       				Information to Configure Another Voice Messaging System for VPIM” section on
                                       				page 4-13 .

Test the setup to verify that Unity Connection can exchange
                                    			 messages with the remote voice messaging system.

## Procedures for
                        	 Setting Up Unity Connection to Use VPIM Networking

This section contains all of the procedures necessary to set up
                           		Unity Connection for VPIM Networking.

For detailed explanations of VPIM Networking concepts, see the “VPIM
                              		  Messages” section on page 4-15 .

### Making Design
                           	 Decisions and Gathering Needed Information

Before you begin setting up Unity Connection for VPIM
                              		Networking, be sure to plan for the following, and gather the applicable
                              		information:

Review your numbering plan strategy to determine whether you
                                    			 need to enter prefixes on the VPIM location and to determine which numbers to
                                    			 assign as Dial IDs for the VPIM locations. Following are requirements that must
                                    			 be considered:

Assign unique Dial IDs. Dial IDs should not be the same as other
                                          				  Dial IDs or extensions.

If you use variable-length Dial IDs, the first digits of each ID
                                          				  should be unique with respect to other Dial IDs.

Follow the given policies:

Establish a fixed length for Dial IDs and, if possible, a fixed
                                          				  length for extensions.

Assign Dial IDs that have at least three digits.

Use a different number range for Dial IDs than for extensions.
                                          				  Do not use Dial IDs that conflict with extensions, such as 001 or 002.

Review your partition and search space configuration to determine the partition and search scope you use for each VPIM location.
                                    For more information, see the “ Dial Plan ” section of the “Call Management” chapter of the System Administration Guide for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html .

Decide for each remote voice messaging system whether to allow
                                    			 Unity Connection to automatically create, modify, and delete VPIM contact
                                    			 records for users on that system, based on information received from incoming
                                    			 VPIM messages. Also decide how to map the source information to VPIM contact
                                    			 display names and extensions.

Decide for each remote voice messaging system whether to allow
                                    			 Unity Connection users to blind address messages to recipients at the location.

Make note of the following information about the remote voice
                                    			 messaging system: the mailbox range, the server name, the domain name, and the
                                    			 IP address.

### Determining the Domain Name

VPIM messages are addressed in the format <Mailbox Number>@<Domain Name>. In order for messages to be exchanged between the
                              remote voice messaging system and Unity Connection, you need to decide on the domain name that the remote voice messaging
                              system uses when addressing messages to Unity Connection users. The domain name is configured as follows:

On the remote voice messaging system, the domain name is configured on the location or node profile that corresponds to Unity
                                    Connection. (For additional information, see the documentation for the remote voice messaging system.)

In the SMTP Domain field, on the System Settings > SMTP Configuration > SMTP Server Configuration page in Cisco Unity Connection
                                    Administration.

If the remote voice messaging system location or node profile that corresponds to Unity Connection has already been configured
                              with a domain name, use that domain name in the procedures in this section.

#### Domain Name Requirements

The domain name uniquely identifies the voice messaging system. When choosing domain names used by Unity Connection and the
                                 remote voice messaging system, keep the following in mind:

Unity Connection and the remote voice messaging system cannot use the same domain name. Each system must use a unique domain
                                       name.

The complete domain name used by Unity Connection cannot be a subset of the domain name used by the remote voice messaging
                                       system. For example, if Unity Connection is using the domain name cisco.com, the remote voice messaging system cannot use
                                       names like london.cisco.com, paris-cisco.com, or romecisco.com. However, you could use europe.cisco.com for Unity Connection,
                                       and then use the names london.cisco.com, paris-cisco.com, and romecisco.com for the remote voice messaging systems.

Caution

Choosing a domain name that does not meet these requirements result in message delivery failure.

### Resolving Names with IP Addresses

VPIM messages are sent over the Internet or any TCP/IP network via SMTP. Therefore, a mechanism for name resolution is required
                              for the remote voice messaging server. The supported method for name resolution is through a Domain Name System (DNS).

You need to know the fully qualified domain name (FQDN) and IP address of the remote voice messaging server. The FQDN is displayed
                              on the System Settings > SMTP Configuration > Server page.

Add a host address resource (A) record and a mail exchange (MX) record in DNS for the remote voice messaging server, if they
                              do not already exist.

For more information about adding A and MX records in DNS, see the documentation for the DNS server.

### Verifying
                           	 Connectivity with the Remote Voice Messaging System

Verify that the servers that handle outgoing and incoming SMTP
                                 		  messages have network connectivity and SMTPwith the remote voice messaging
                                 		  server, and vice versa.

For networking with another voice messaging server, you may need
                                 		  to install and configure an SMTP service or gateway on that server. See the
                                 		  documentation of the other voice messaging system for information on installing
                                 		  the SMTP service or gateway. Before proceeding, verify that the SMTP service or
                                 		  gateway has been installed on the other voice messaging server.

Do the following procedure to verify network connectivity with the
                                 		  remote voice messaging server:

Step 1

Using a computer on the same local network segment as the Unity
                                          			 Connection server, open a command prompt window.

Step 2

Enter ping <IP address , where <IP address> is the
                                          			 IP address of the remote voice messaging server, then press Enter .

If you receive no reply, troubleshoot the network connectivity
                                             				problem until the problem is resolved. Then continue with Step 3 .

Step 3

Enter ping <Domain name where <Domain name> is
                                          			 the domain name that is used to address messages to the remote voice messaging
                                          			 server. The domain name in this step is the domain name that is entered for the
                                          			 VPIM location in Cisco Unity Connection Administration when setting up VPIM
                                          			 Networking.

Step 4

If you received a reply when pinging the IP address in Step 2 , but no replies
                                          			 when pinging the domain name in Step 3 , see the “Resolving
                                             				Names with IP Addresses” section on page 4-4 . When the problem is
                                          			 resolved, continue with Step 5 .

Step 5

Test network connectivity in the opposite direction. For systems
                                          			 other than Unity Connection, see the documentation for information on how to
                                          			 conduct the test, and continue with Step 6 . Note that the
                                          			 remaining steps in this procedure may not exactly match the steps necessary for
                                          			 your system, so you may need to make adjustments.

Step 6

On the remote server, ping the IP address of the local server
                                          			 that handles incoming SMTP messages.

If you receive no reply, troubleshoot the network connectivity
                                             				problem until the problem is resolved. Then continue with Step 7 .

Step 7

On the remote server, ping the domain name, where the domain
                                          			 name is the one that is discussed in the “Determining
                                             				the Domain Name” section on page 4-3 .

Step 8

If pinging by domain name fails, see the “Resolving
                                             				Names with IP Addresses” section on page 4-4 .

### Verifying SMTP
                           	 Connectivity with the Remote Voice Messaging Server

Step 1

Using a computer on the same local network segment as the Unity
                                          			 Connection server, open a command prompt window

Step 2

Enter telnet <servername> 25, where <servername> is
                                          			 the IP address or the FQDN of the SMTP server using TCP port 25.

Step 3

Press ENTER after each command.

Step 4

If remote messaging server is connected to SMTP, you receive 220
                                          			 response with the FQDN of the server and the version of SMTP.

Step 5

If the telnet test was successful, enter quit to end the telnet
                                          			 session.

### Creating VPIM
                           	 Locations

Create a VPIM location on Unity Connection for each remote voice
                                 		  messaging system to which users send messages. If Unity Connection sends
                                 		  message with a large number of voice messaging systems, you may prefer to
                                 		  configure only a few VPIM locations at this time and proceed with the rest of
                                 		  the setup. After verifying that messaging works correctly between Unity
                                 		  Connection and the voice messaging systems for which VPIM locations have been
                                 		  configured, you can create the rest of the VPIM locations.

Do the following
                                 		  procedure to create VPIM locations:

Step 1

In Cisco Unity
                                          			 Connection Administration, expand Networking and select VPIM .

Step 2

On the Search
                                          			 VPIM Locations page, select Add New .

Step 3

On the New
                                          			 VPIM Location page, enter basic settings, as applicable. (For more information,
                                          			 see Help > This Page )

Step 4

Select Save .

Step 5

On the Edit
                                          			 VPIM Location page, continue entering applicable settings.

Step 6

When you have
                                          			 finished entering settings on the Edit VPIM Location page, select Save .

### Customizing VPIM
                           	 Locations

You can customize a VPIM location using Cisco Unity Connection
                                 		  Administration for each remote voice messaging system to which users send
                                 		  messages.

Do the following procedure to customize VPIM locations:

Step 1

In Cisco Unity Connection Administration, expand Networking and select VPIM .

Step 2

On the Search VPIM Locations page, select the display name for
                                          			 the VPIM location that you want to customize.

Step 3

On the Edit VPIM Location page, change settings, as applicable.
                                          			 (For more information, see Help> This Page ).

Step 4

When you have finished changing settings on the Edit VPIM
                                          			 Location page, select Save .

### Creating VPIM Contacts

Initially, you should create only a few VPIM contacts to verify that Unity Connection and the remote voice messaging system
                              can successfully exchange messages. After you have confirmed that messaging between Unity Connection and the remote voice
                              messaging system is working correctly, you can finish creating the VPIM contacts.

You must first create VPIM locations before creating VPIM contacts, and the VPIM contacts must be created on the same Unity
                                          Connection server on which you created the VPIM locations.

You can create VPIM contacts using the Bulk Administration Tool or using Cisco Unity Connection Administration. Using the
                              Bulk Administration Tool to Create Multiple VPIM Contacts

The Bulk Administration Tool (BAT) allows you to create multiple VPIM contacts at the same time by importing contact data
                              from a comma-separated value (CSV) file. CSV is a common text file format for moving data from one data store to another.

Use the following procedure to prepare your CSV file.

#### Preparing a CSV
                              	 File for Creating VPIM Contacts

Step 1

Save the data that you use to create VPIM Contacts as a CSV
                                             			 file.

As a best practice, do not include more than 7,500 records in a
                                                				single CSV file, as you may encounter unexpected results when the Bulk
                                                				Administration Tool imports the data.

Step 2

Copy the CSV file to the applicable directory.

Step 3

Open the CSV file in a spreadsheet application or another
                                             			 application with which you can edit and reorganize the data. Do the following:

Confirm that the data is separated by commas, and that no tabs,
                                                      					 spaces, or semicolons separate the data in the file.

If any data includes a space, quotation marks, or commas,
                                                      					 contain the characters within quotation marks.

Step 4

Rearrange the data so that the columns are in the same order as
                                             			 the column headers that you add in Step
                                                				5 . The order of the column headers does not matter, though it is good
                                             			 practice to set up your CSV file as indicated here. For example, the columns of
                                             			 data in this sample are sorted so that the alias of the contact is followed by
                                             			 the last name, the first name, the extension, the remote mailbox ID
                                             			 (RemoteMailAddress), and then by VPIM location (DeliveryLocationDisplayName):

aabade,Abade,Alex,2001,3000,Chicago VMS VPIM Location

kbader,Bader,Kelly,2002,3100,Chicago VMS VPIM Location

tcampbell,Campbell,Terry,2003,3200,Chicago VMS VPIM Location

lcho,Cho,Li,2004,3300,Chicago VMS VPIM Location

Step 5

Enter the column headers above the first row of data. Column
                                             			 headers must be separated by commas, and spelled as indicated below:

Alias,LastName,FirstName,Extension,RemoteMailAddress,DeliveryLocationDisplayName

Step 6

If applicable, add optional column headers to the first row, and
                                             			 the corresponding data that you want to import in the subsequent rows below. As
                                             			 you do so, confirm the following:

Column headers and data are separated by commas. Note that every
                                                      					 row does not have to contain data for optional column headers.

Any data that includes a space, quotation marks, or commas is
                                                      					 contained within quotation marks.

Tip

Step 7

If your CSV
                                             			 file contains columns of data that you do not want to import, delete the
                                             			 columns. Alternatively, you can title one column NOTES. The BAT ignores data
                                             			 beneath any NOTES column header, but it does not support more than one NOTES
                                             			 column in a CSV file.

Step 8

Confirm that
                                             			 each row contains the appropriate data corresponding to each column header.

Step 9

Save the file
                                             			 as a CSV file.

Step 10

Continue with
                                             			 the following “Creating
                                                				VPIM Contacts Using the Bulk Administration Tool” procedure.

#### Creating VPIM
                              	 Contacts Using the Bulk Administration Tool

Step 1

In Cisco Unity Connection Administration, expand Tools and select Bulk Administration Tool .

Step 2

On the Bulk Administration Tool page, under Select Operation,
                                             			 select Create .

Step 3

Under Select Object Type, select System Contacts .

Step 4

Under Select File, select Browse .

Step 5

In the Choose File dialog box, browse to the directory where you
                                             			 saved the CSV file that you created in the “Preparing
                                                				a CSV File for Creating VPIM Contacts” procedure on page 4-6 and select Open .

Step 6

In the Failed Objects File Name field, enter the path and the
                                             			 name of the file in which you want errors recorded.

Step 7

Select Submit .

#### Correcting CSV
                              	 Errors

The failed objects file contains data that failed to create a
                                    		  VPIM contact. The Bulk Administration Tool reports the first error it detects
                                    		  in a row in a CSV file. When you have corrected that error, the BAT may detect
                                    		  additional errors in the same row when the data is imported again. Thus, you
                                    		  may need to repeat the correction process—running the BAT and correcting an
                                    		  error—several times to find and correct all errors.

The failed objects file contains all the records that failed to
                                    		  create a VPIM contact. You can save the file as a CSV file, and use it when you
                                    		  run the BAT again. Note that each time you run the BAT, the failed objects file
                                    		  is overwritten.

Do the following procedure to correct CSV errors:

Step 1

If the Bulk Administration Tool operation results in any
                                             			 failures, you can immediately inspect the failed objects report file by
                                             			 selecting Download the Failed Objects File .

Step 2

Open the file and correct all problems with the data, as
                                             			 indicated by the information in the FailureReason column for each record.

Step 3

Remove the FailureReason column or change the heading to JUNK .

Step 4

When you have finished modifying the data, save the file as a
                                             			 CSV file with a new name.

Step 5

Run the BAT again with the CSV file that you saved in Step 4 as the
                                             			 input file.

Note that each time that you run BAT, the failed objects file is
                                                				overwritten (unless you specify a new name for the file each time you run the
                                                				tool).

Step 6

Repeat this procedure until all VPIM contact accounts are
                                             			 created without error, and then proceed to the “After
                                                				Creating VPIM Contacts” section on page 4-10 .

#### Using Cisco Unity
                              	 Connection Administration to Create VPIM Contacts

You can create VPIM contacts one at a time using Cisco Unity
                                    		  Connection Administration.

Do the following procedure to create VPIM contacts:

Step 1

In Cisco Unity Connection Administration, expand Contacts and select Contacts .

Step 2

On the Search Contacts page, in the Contact menu, select New Contact . Alternatively, select Add New on the
                                             			 Search Contacts page to add a new contact.

Step 3

On the New Contact page, enter the following settings and select Save .

Field

Setting

Alias

Enter the alias of the VPIM contact.

First Name

Enter the first name of the VPIM contact.

Last Name

Enter the last name of the VPIM contact.

Display Name

Enter the display name of the VPIM contact.

Contact Template

Select the template on which to base the VPIM contact.

Step 4

On the Edit Contact Basics page, enter the following settings
                                             			 and select Save .

Field

Setting

Voice Name

Select Play/Record to record a
                                                            						  name for the VPIM contact.

List in Directory

Check this check box to list the VPIM contact in the Unity
                                                            						  Connection directory.

Partition

Select the partition to which the VPIM contact belongs.
                                                            						  Partitions are grouped together into search spaces, which are used to define
                                                            						  the scope of objects (for example, users and distribution lists) that a user or
                                                            						  outside caller can reach while interacting with Unity Connection. A VPIM
                                                            						  contact can belong to only one partition. A partition can belong to more than
                                                            						  one search space.

Transfer Enabled

(Optional) Check this check box if you want Unity Connection
                                                            						  to transfer incoming calls to a phone number that is associated with the VPIM
                                                            						  contact instead of sending a message to the remote mailbox for the VPIM
                                                            						  contact.

Transfer Extension or URI

(Optional) Enter the phone number or URI that the phone
                                                            						  system uses to transfer calls to the VPIM contact, including any outdial access
                                                            						  codes, if necessary. This field works together with the Transfer Enabled field.

Delivery Location

Select the VPIM location for the VPIM contact.

VPIM Remote Mailbox Number

Enter the mailbox number for the VPIM contact on the remote
                                                            						  voice messaging system.

Local Extension

(Optional) For VPIM contacts, you can assign a local
                                                            						  extension that fits into the Unity Connection extension numbering scheme. A
                                                            						  local extension allows callers to address messages to the VPIM contact using an
                                                            						  extension, rather than knowing the location ID and the remote mailbox number of
                                                            						  the contact.

In addition, if you set the Transfer Enabled and Transfer
                                                            						  Extension fields, callers are able to identify and be transferred to the VPIM
                                                            						  contact.

Phone Numbers to Call Contact with Voice Commands

(Optional) Use the Dialed Work Phone, Dialed Home Phone, and
                                                            						  Dialed Mobile Phone fields when you want voice recognition users to be able to
                                                            						  call the VPIM contact by specifying a specific phone type for the contact.

For dialed phone numbers, include any additional numbers
                                                            						  necessary to dial outside calls (for example 9) and for long-distance dialing
                                                            						  (for example, 1).

Phone Numbers or URIs to Identify Contact for Personal Call
                                                            						  Transfer Rules

(Optional) Use the Work Phone, Home Phone, Mobile Phone,
                                                            						  Other Number 1, and Other Number 2 fields to enter phone numbers or URIs that
                                                            						  Unity Connection uses when matching the personal call transfer rules of a user
                                                            						  against incoming phone calls from system contacts.

Step 5

Repeat Step 2 through Step 4 for all
                                             			 remaining VPIM contacts that you want to create.

#### After Creating
                              	 VPIM Contacts

After creating VPIM contacts, consider the following:

It takes a few minutes for the newly-created VPIM contact to be
                                       			 available to receive messages.

You can make changes to settings for individual VPIM contacts in
                                       			 Cisco Unity Connection Administration.

When you want to modify unique VPIM contact settings—such as the
                                       			 extension—for multiple contacts at once, you can rerun the Bulk Administration
                                       			 Tool.

When a VPIM contact no longer needs a Unity Connection account,
                                       			 you can delete the VPIM contact. For details, see the “Deleting
                                          				VPIM Contacts” section on page 4-14 .

### Customizing VPIM Contact Directory Update Settings

In addition to manually creating, modifying, and deleting VPIM contacts, you can configure Unity Connection to automatically
                              update records in the VPIM contact directory based on information that is contained in incoming VPIM messages. The settings
                              that control whether the creation, modification, and deletion actions occur automatically, and how the incoming information
                              is used to create or modify a record, can be individually configured for each VPIM location. By default, no automatic directory
                              updates occur for any VPIM locations.

Depending on the Contact Creation settings that you select for each VPIM location, Unity Connection uses information from
                              the header of an incoming VPIM message. If a VPIM message is received from a sender on a VPIM location that is configured
                              to allow automatic VPIM contact creation, and no existing VPIM contact matches the information of the sender, a new VPIM contact
                              record is created, provided that the VPIM message contains:

A phone number

A text name

A domain name

A recorded name (when required, based on the VPIM location configuration)

Additional Contact Creation settings allow you to specify how to map the parsed text name of the VPIM contact to a first name,
                              last name, and display name, and how to map the phone number to an extension.

Changes to the Map VPIM Contact Extensions setting on the Contact Creation page for a VPIM location affect only VPIM contacts
                                          that are created after the setting is saved. VPIM contacts that already existed before the Map VPIM Contact Extensions setting
                                          is changed are not automatically updated. You must manually change the extension for each previously existing VPIM contact
                                          for that VPIM location.

If a VPIM message is received from a sender on a VPIM location that is configured to allow automatic VPIM contact modification,
                              and an existing VPIM contact matches the sender information, the VPIM contact can be updated. You can select whether VPIM
                              contact information is updated each time a message is received from a VPIM contact, or only when a message is received from
                              a VPIM contact whose text name has changed since the directory entry was created. You can also decide whether or not to allow
                              an update to the display name when a modification is made.

If a message from a Unity Connection user to a VPIM contact results in a non-delivery receipt (NDR), indicating that the message
                              was undeliverable because the intended recipient does not exist (SMTP 5.1.1), and if the VPIM location is configured to allow
                              automatic VPIM contact deletion, the VPIM contact is deleted.

You can update the VPIM location contact creation settings using Cisco Unity Connection Administration.

#### Before Configuring VPIM Contact Creation Settings

Before configuring the VPIM location contact creation settings, consider the following:

If you have pre-populated VPIM contacts with specific display names that should not be changed, but want to allow automatic
                                       modification of other fields in the contact record, you can select to keep the Allow VPIM Contact Display Name Updates check
                                       box unchecked. In this case, the first name, last name, and spoken name of a contact may be modified during an automatic update.
                                       This may result in a mismatch if the spoken name is updated and the display name is not.

When the Allow VPIM Contacts Without Recorded Voice Names check box is not checked, new VPIM contacts are not created for
                                       incoming messages that do not contain an Originator-Spoken-Name attachment. In addition, if automatic modification of VPIM
                                       contacts is enabled, and if the sender of an incoming message matches an existing VPIM contact, the VPIM contact is deleted
                                       if the attachment is not present in the message.

When the Allow VPIM Contacts Without Recorded Voice Names check box is checked, and automatic modification of VPIM contacts
                                       is enabled, if the sender of an incoming message that does not include an Originator-Spoken-Name attachment matches an existing
                                       VPIM contact, the existing recorded name is deleted.

If the phone number in an incoming message cannot be successfully mapped to an extension using the option selected for the
                                       Map VPIM Contact Extensions To field, a VPIM contact is not created for the sender.

#### Using Cisco Unity Connection Administration to Configure VPIM Contact Creation Settings

After you create a VPIM location, you can configure the settings that control automatic directory updates for that specific
                                 VPIM location using Cisco Unity Connection Administration.

##### Configuring VPIM
                                 	 Contact Creation Settings Using Cisco Unity Connection Administration

Step 1

In Cisco Unity Connection Administration, expand Networking and select VPIM Locations .

Step 2

On the Search VPIM Locations page, select the name of the VPIM
                                                			 location for which you want to configure contact creation settings.

Step 3

On the Edit VPIM Location page, in the Edit menu, select Contact Creation .

Step 4

On the Contact Creation page, check the Automatically Create VPIM Contacts check box to
                                                			 enable automatic creation of a VPIM contact record for this location when a
                                                			 VPIM message arrives and the sender does not already have a corresponding VPIM
                                                			 contact record.

Step 5

If you checked the Automatically Create VPIM Contacts check box
                                                			 in Step 4 , in the Contact
                                                			 Template list, select the template on which to base the automatically created
                                                			 contacts.

Step 6

In the Automatically Modify VPIM Contact field, select one of
                                                			 the following to apply to VPIM contacts for this location:

No Automatic Update of Contacts —The VPIM contact record is
                                                         					 not updated with the sender information in a VPIM message when an incoming
                                                         					 message has changed sender information.

Only When the Text Name Changes —The VPIM contact record is
                                                         					 updated only when the text name received in the VPIM message does not match the
                                                         					 name of the VPIM contact.

With Each VPIM Message —Every incoming VPIM message from a
                                                         					 VPIM contact at this location results in an update to the corresponding VPIM
                                                         					 contact record.

Step 7

Check the Automatically Delete VPIM Contact check box to
                                                			 enable automatic deletion of a VPIM contact for this location when a VPIM
                                                			 message is returned as undeliverable.

Step 8

Check the Allow VPIM Contact Display Name Updates check box to
                                                			 enable automatic updates to the VPIM contact display name when an incoming
                                                			 message from this location has a changed display name for the sender.

Step 9

Check the Allow VPIM Contacts Without Recorded Voice Names check box to enable automatic updates for this location to records for VPIM
                                                			 contacts that do not have a recorded name.

Step 10

In the Mapping Text Names field, select one of the following
                                                			 options to indicate how text names in incoming messages from this location are
                                                			 mapped to the display names for automatically created VPIM contact records:

Directly to VPIM Contact Display Names —The display names for
                                                         					 VPIM contacts match the corresponding text names.

Custom —Enter the rule that defines how text names are mapped
                                                         					 to display names for VPIM contacts. You can enter the tokens <FN>,
                                                         					 <LN>, or <TN> (respectively first name, last name, or text name) in
                                                         					 any combination, along with any additional text. Always precede <FN>,
                                                         					 <LN>, or <TN> with a space, comma, or semicolon unless it appears
                                                         					 at the beginning of the rule. In addition, always follow one of these tokens
                                                         					 with a space, comma or semicolon unless it appears at the end of the rule. No
                                                         					 additional characters are required at the beginning or end of a rule.

Step 11

In the Map VPIM Contact Extensions To field, select one of the
                                                			 following settings to indicate how the phone number on incoming messages from
                                                			 this location is mapped to the extension for automatically created VPIM contact
                                                			 records:

Phone Number —Extensions are the same as the phone numbers
                                                         					 that are parsed from incoming VPIM messages.

Phone Number - Remote Phone Prefix —Extensions are formed by
                                                         					 removing the remote phone prefix from the beginning of the phone numbers.

Location Dial ID + Phone Number —Extensions are formed by
                                                         					 adding the location Dial ID in front of the phone numbers.

Location Dial ID + Phone Number - Remote Phone
                                                            						Prefix —Extensions are formed by removing the remote phone prefix from the
                                                         					 beginning of the phone number, and adding the location Dial ID in front of the
                                                         					 resulting number.

Step 12

Select Save.

Step 13

On the VPIM Location menu, select Search VPIM Locations .

Step 14

Repeat Step 2 through Step 13 for
                                                			 all remaining VPIM locations.

### Adding Alternate
                           	 Names for Each VPIM Location

When the Unity Connection system uses the voice-recognition
                                 		  option, you can also specify alternate names for the display name that you give
                                 		  a VPIM location. Users say the display name when they use voice commands to
                                 		  blind address to a mailbox number at a VPIM location (for example, to address
                                 		  to extension 55 at a VPIM location named Seattle, a user would say “five five
                                 		  at Seattle”) or to address a message to a VPIM contact name at a VPIM location
                                 		  (for example, “Robin Smith in Chicago”). Consider specifying alternate names if
                                 		  the VPIM location display name contains administrative information that users
                                 		  are not likely to know, or if it is not pronounced the way it would be read, as
                                 		  may be the case with acronyms and abbreviations. Also consider adding alternate
                                 		  names if users tend to refer to a location in multiple ways. For example, if
                                 		  users at one site refer to a location as “Seattle branch” and users at another
                                 		  site refer to the same location as “Seattle office,” you could add both
                                 		  “Seattle branch” and “Seattle office” as alternate names.

Do the following procedure to add an alternate name:

Step 1

In Cisco Unity Connection Administration, expand Networking and select VPIM Locations .

Step 2

On the Search VPIM Locations page, select the name of the VPIM
                                          			 location for which you want to add an alternate name.

Step 3

On the Edit VPIM Location page, in the Edit menu, select Alternate Names .

Step 4

On the Edit Alternate Names page, in the Display Name field,
                                          			 enter the alternate name you want for the VPIM location, then select Add New .

Step 5

On the VPIM Location menu, select Search VPIM Locations .

Step 6

Repeat Step 2 through Step 5 for all
                                          			 remaining VPIM locations for which you want to add alternate names.

### Gathering Information to Configure Another Voice Messaging System for VPIM

Configuring another voice messaging system to exchange VPIM messages with Unity Connection may require the following information:

The server name and domain name of the SMTP server that handles incoming SMTP messages.

The Unity Connection phone prefix (if any) and Remote phone prefix (if any) entered on the corresponding VPIM location page.

The mailbox number range for Unity Connection users.

Incoming VPIM messages must be routed to the SMTP server. When defining a location for Unity Connection on the remote voice
                              messaging system, use the domain name that you entered for the SMTP server.

Unity Connection expects incoming VPIM messages to be formatted as follows:

<ConnectionPhonePrefix+ConnectionUserExtension@PrimaryLocationSMTPDomainName>

These specific properties are configured in Unity Connection, but similar information needs to be configured in the other
                              voice messaging system.

## Deleting VPIM
                        	 Contacts

Step 1

In Cisco Unity Connection Administration, expand Contacts and select Contacts .

Step 2

On the Search Contacts page, check the check boxes next to the
                                       			 VPIM contacts that you want to delete.

Step 3

Select Delete Selected .

Step 4

When prompted to confirm the deletion, select OK .

## Removing a VPIM
                        	 Location

When you remove a VPIM location, you must remove (or reassign)
                           		any contacts and contact templates that use the location before deleting the
                           		VPIM location object. Use the following task list to remove a VPIM location.

Use the Bulk
                                 			 Administration Tool to export a list of all administrator-defined contacts. See
                                 			 the “Bulk Administration Tool”

Download the
                                 			 export file, and use a text editor to modify it to contain only the rows in
                                 			 which the DeliveryLocationDisplayName matches the display name of the VPIM
                                 			 location that you are removing. (If you plan to reassign the contacts to a
                                 			 different VPIM location, update the value in the DeliveryLocationDisplayName
                                 			 column.)

Use the Bulk
                                 			 Administration Tool to delete the list of contacts you generated in Task 2 . Alternatively, to
                                 			 reassign the contacts to a different VPIM location, use the Update option.

In Cisco Unity
                                 			 Connection Administration, expand Templates and select Contact Templates. If a
                                 			 contact template is configured to use the VPIM location as the delivery
                                 			 location, change the delivery location, or delete the template. (You may need
                                 			 to select the display name of each template on the Search Contact Templates
                                 			 page to verify or change the delivery location.)

To delete the
                                 			 location, in Unity Connection Administration, expand Networking and select VPIM
                                 			 Locations. On the Search VPIM Locations page, check the check box next to the
                                 			 display name of the location that you want to delete, then select Delete
                                 			 Selected.

For more information on Bulk Administration Tool, appendix of System Administration Guide for Cisco Unity Connection, Release 15, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html .

## VPIM
                        	 Messages

VPIM messages are made up of one or more MIME-encoded parts. The
                           		VPIM specification allows for optional MIME parts for spoken name and for
                           		forwarded and text messages. Unity Connection does not, however, support
                           		sending or receiving a vCard (an electronic business card that includes phone
                           		number, text name, and email address). If a vCard is attached to an outgoing or
                           		incoming message, Unity Connection removes the vCard data. In addition, any
                           		attachments to messages other than the voice message and embedded messages are
                           		removed from outgoing and incoming messages.

Unity Connection allows you to specify whether the recorded name
                           		of the sender is sent with outgoing messages. If incoming messages include a
                           		recorded name, it is played as part of the message. Unity Connection can also
                           		be configured to update the directory with information from the header from
                           		incoming messages.

Outgoing messages to a VPIM location do not include any
                           		recipients other than those at the VPIM location. Therefore, when a VPIM
                           		recipient replies to all addressees on a message, the reply go only to the
                           		sender and to any other recipients at the same VPIM location.

Figure 1 shows a sample
                           		VPIM message. Only a portion of the MIME encoding of the spoken name and voice
                           		message parts are shown because they are very long.

### VPIM Addresses

A VPIM address is in the same format as a typical SMTP email address: localpart@hostpart. The right-hand side of the address
                              is the domain name of the system on the TCP/IP network that handles messages. The left-hand side of the address is a unique
                              identifier for the user. Typically, the left-hand side is the user mailbox number or the mailbox number with a prefix.

For example, an outgoing VPIM message to Terry Campbell with the remote mailbox ID 2233 could be addressed:

To: 2233@remotevoicemailsystem.com

If it is necessary to accommodate the numbering plan for your organization, the address can also contain a prefix:

To: 8882233@remotevoicemailsystem.com

VPIM addresses are created by Unity Connection when sending VPIM messages; they are not entered by users when addressing messages.

### Message Addressing Options

Unity Connection provides the following ways to address messages to individuals on a remote voice messaging system:

Unity Connection directory—When the List in Directory check box is checked for VPIM contacts, the Unity Connection directory
                                    has the names and extensions for the VPIM contacts. Users can address messages to VPIM contacts the same way that they address
                                    messages to regular Unity Connection users—by extension or by spelling the name of the recipient. Note that spoken name confirmation
                                    is available when a recorded name exists for the VPIM contact; if the contact does not have a recorded name, Unity Connection
                                    uses Text to Speech to play the display name of the contact.

Blind addressing—Blind addressing allows users to send messages to recipients at the VPIM location even if the recipients
                                    are not defined as contacts in the Unity Connection directory. If the Allow Blind Addressing check box is checked on the VPIM
                                    Location page, users can address messages to recipients at this location by entering a number that is made up of the VPIM
                                    location Dial ID and the mailbox number of the recipient, or by saying the digits of the mailbox number and the display name
                                    of the VPIM location (for example, “five five at Seattle office”).

Distribution lists—Users can address messages to a private or system distribution list that includes VPIM contacts so that
                                    the VPIM contact receives the message.

### Messaging Similarities and Limitations

For the most part, messaging between Unity Connection users and individuals on a remote voice messaging system is the same
                              as messaging among Unity Connection users. For example:

Messages marked urgent when they are sent are marked urgent when they are retrieved by the recipient.

Messages marked private when they are sent are marked private when they are retrieved by the recipient.

Users can send messages to Unity Connection distribution lists that include VPIM contacts.

Note the following exceptions:

Requests for read receipts and delivery receipts are both returned as delivery receipts.

In order for users on the remote voice messaging system to send messages to Unity Connection distribution lists, the Accept
                                    Messages From Foreign System check box must be checked on the Edit Distribution List Basics page in Unity Connection Administration.
                                    This check box is not checked by default.

### Audio Format Considerations

The Audio Format Conversion settings for the VPIM location (on the Networking > Edit VPIM Location page in Cisco Unity Connection
                              Administration) allow you to control the audio format of outgoing and incoming VPIM messages, as follows:

Incoming Messages—You can set whether incoming VPIM messages are stored in the format in which they were sent, or converted
                                    to the audio format that Unity Connection uses for recording messages.

Outbound Messages—You can set whether outbound VPIM messages are sent in the format in which they were recorded, or converted
                                    to the G.726 codec.

To make decisions about these settings, consider the following:

The audio format that the local Unity Connection server uses for recording and playing voice messages.

The audio format in which the remote voice messaging system can send and receive VPIM messages. Some voice messaging systems
                                    support only the G.726 format for VPIM messages, but you must consult the documentation of the remote voice messaging server
                                    to be sure.

The network bandwidth.

The incoming VPIM messages be stored in the same audio format that the local Unity Connection server uses for recording and
                              playing messages.

## Multiple VPIM Bridgeheads

In an HTTPS network, you can designate multiple Unity Connection locations in the network as VPIM bridgeheads. The following
                           are the ways to add multiple bridgeheads in an HTTPS network:

You can add different VPIM servers on different VPIM bridgehead in an HTTPS network with unique dial id.

You can add the same VPIM server on multiple VPIM bridgeheads with unique and not null remote phone prefix along with a unique
                                 dial id.

You can add the same VPIM server to the same VPIM bridgehead multiple times with unique remote phone prefix. However, if a
                                 VPIM server is already added as VPIM bridgehead on Cisco Unity Connection with no remote phone prefix and you want to add
                                 the same VPIM server to same Unity Connection location or another Unity Connection location as VPIM bridgehead with some remote
                                 phone prefix (Non Null value) then you need to perform the following steps:

Manually delete all the existing VPIM contacts that are created with no remote phone prefix.

Change the remote phone prefix of already connected VPIM location.

Add the same VPIM location as VPIM bridgehead with different remote phone prefix to another or the same Unity Connection location.

Push the contacts from the VPIM server to the Unity Connection location.

| Note | Additional server discovery and directory synchronization functionality is available when you use Digital Networking rather
                                       than VPIM to connect multiple Unity Connection 2.x and later servers. |
|---|---|

| Caution | Choosing a domain name that does not meet these requirements result in message delivery failure. |
|---|---|

| Step 1 | Using a computer on the same local network segment as the Unity
                                          			 Connection server, open a command prompt window. |
|---|---|
| Step 2 | Enter ping <IP address , where <IP address> is the
                                          			 IP address of the remote voice messaging server, then press Enter . If you receive no reply, troubleshoot the network connectivity
                                             				problem until the problem is resolved. Then continue with Step 3 . |
| Step 3 | Enter ping <Domain name where <Domain name> is
                                          			 the domain name that is used to address messages to the remote voice messaging
                                          			 server. The domain name in this step is the domain name that is entered for the
                                          			 VPIM location in Cisco Unity Connection Administration when setting up VPIM
                                          			 Networking. |
| Step 4 | If you received a reply when pinging the IP address in Step 2 , but no replies
                                          			 when pinging the domain name in Step 3 , see the “Resolving
                                             				Names with IP Addresses” section on page 4-4 . When the problem is
                                          			 resolved, continue with Step 5 . |
| Step 5 | Test network connectivity in the opposite direction. For systems
                                          			 other than Unity Connection, see the documentation for information on how to
                                          			 conduct the test, and continue with Step 6 . Note that the
                                          			 remaining steps in this procedure may not exactly match the steps necessary for
                                          			 your system, so you may need to make adjustments. |
| Step 6 | On the remote server, ping the IP address of the local server
                                          			 that handles incoming SMTP messages. If you receive no reply, troubleshoot the network connectivity
                                             				problem until the problem is resolved. Then continue with Step 7 . |
| Step 7 | On the remote server, ping the domain name, where the domain
                                          			 name is the one that is discussed in the “Determining
                                             				the Domain Name” section on page 4-3 . |
| Step 8 | If pinging by domain name fails, see the “Resolving
                                             				Names with IP Addresses” section on page 4-4 . Note Optionally,
                                                         				  you can verify network connectivity using the “utils network ping” CLI command. | Note | Optionally,
                                                         				  you can verify network connectivity using the “utils network ping” CLI command. |
| Note | Optionally,
                                                         				  you can verify network connectivity using the “utils network ping” CLI command. |

| Note | Optionally,
                                                         				  you can verify network connectivity using the “utils network ping” CLI command. |
|---|---|

| Step 1 | Using a computer on the same local network segment as the Unity
                                          			 Connection server, open a command prompt window |
|---|---|
| Step 2 | Enter telnet <servername> 25, where <servername> is
                                          			 the IP address or the FQDN of the SMTP server using TCP port 25. |
| Step 3 | Press ENTER after each command. |
| Step 4 | If remote messaging server is connected to SMTP, you receive 220
                                          			 response with the FQDN of the server and the version of SMTP. |
| Step 5 | If the telnet test was successful, enter quit to end the telnet
                                          			 session. |

| Step 1 | In Cisco Unity
                                          			 Connection Administration, expand Networking and select VPIM . |
|---|---|
| Step 2 | On the Search
                                          			 VPIM Locations page, select Add New . |
| Step 3 | On the New
                                          			 VPIM Location page, enter basic settings, as applicable. (For more information,
                                          			 see Help > This Page ) Note Fields
                                                      				marked with * (an asterisk) are required. | Note | Fields
                                                      				marked with * (an asterisk) are required. |
| Note | Fields
                                                      				marked with * (an asterisk) are required. |
| Step 4 | Select Save . |
| Step 5 | On the Edit
                                          			 VPIM Location page, continue entering applicable settings. |
| Step 6 | When you have
                                          			 finished entering settings on the Edit VPIM Location page, select Save . |

| Note | Fields
                                                      				marked with * (an asterisk) are required. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Networking and select VPIM . |
|---|---|
| Step 2 | On the Search VPIM Locations page, select the display name for
                                          			 the VPIM location that you want to customize. |
| Step 3 | On the Edit VPIM Location page, change settings, as applicable.
                                          			 (For more information, see Help> This Page ). |
| Step 4 | When you have finished changing settings on the Edit VPIM
                                          			 Location page, select Save . |

| Note | You must first create VPIM locations before creating VPIM contacts, and the VPIM contacts must be created on the same Unity
                                          Connection server on which you created the VPIM locations. |
|---|---|

| Step 1 | Save the data that you use to create VPIM Contacts as a CSV
                                             			 file. As a best practice, do not include more than 7,500 records in a
                                                				single CSV file, as you may encounter unexpected results when the Bulk
                                                				Administration Tool imports the data. |
|---|---|
| Step 2 | Copy the CSV file to the applicable directory. |
| Step 3 | Open the CSV file in a spreadsheet application or another
                                             			 application with which you can edit and reorganize the data. Do the following: Confirm that the data is separated by commas, and that no tabs,
                                                      					 spaces, or semicolons separate the data in the file. If any data includes a space, quotation marks, or commas,
                                                      					 contain the characters within quotation marks. |
| Step 4 | Rearrange the data so that the columns are in the same order as
                                             			 the column headers that you add in Step
                                                				5 . The order of the column headers does not matter, though it is good
                                             			 practice to set up your CSV file as indicated here. For example, the columns of
                                             			 data in this sample are sorted so that the alias of the contact is followed by
                                             			 the last name, the first name, the extension, the remote mailbox ID
                                             			 (RemoteMailAddress), and then by VPIM location (DeliveryLocationDisplayName): aabade,Abade,Alex,2001,3000,Chicago VMS VPIM Location kbader,Bader,Kelly,2002,3100,Chicago VMS VPIM Location tcampbell,Campbell,Terry,2003,3200,Chicago VMS VPIM Location lcho,Cho,Li,2004,3300,Chicago VMS VPIM Location Note The only required column headers for creating contacts are Alias
                                                         				and Extension. However, in order to create VPIM contacts you must also include
                                                         				columns for the remote mailbox ID and the VPIM location. | Note | The only required column headers for creating contacts are Alias
                                                         				and Extension. However, in order to create VPIM contacts you must also include
                                                         				columns for the remote mailbox ID and the VPIM location. |
| Note | The only required column headers for creating contacts are Alias
                                                         				and Extension. However, in order to create VPIM contacts you must also include
                                                         				columns for the remote mailbox ID and the VPIM location. |
| Step 5 | Enter the column headers above the first row of data. Column
                                             			 headers must be separated by commas, and spelled as indicated below: Alias,LastName,FirstName,Extension,RemoteMailAddress,DeliveryLocationDisplayName |
| Step 6 | If applicable, add optional column headers to the first row, and
                                             			 the corresponding data that you want to import in the subsequent rows below. As
                                             			 you do so, confirm the following: Column headers and data are separated by commas. Note that every
                                                      					 row does not have to contain data for optional column headers. Any data that includes a space, quotation marks, or commas is
                                                      					 contained within quotation marks. Tip Include a column with the ListInDirectory header and a value of 1 for each contact if you would like users to be able to address
                                                         messages to VPIM contacts the same way that they address messages to regular Unity Connection users—by extension or by spelling
                                                         the name of the recipient. For a list of optional column headers, see the “ Required and Optional CSV Fields in BAT ” section of the “Bulk Administration Tool” appendix of the System Administration Guide for Cisco Unity Connection, Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html . | Tip | Include a column with the ListInDirectory header and a value of 1 for each contact if you would like users to be able to address
                                                         messages to VPIM contacts the same way that they address messages to regular Unity Connection users—by extension or by spelling
                                                         the name of the recipient. For a list of optional column headers, see the “ Required and Optional CSV Fields in BAT ” section of the “Bulk Administration Tool” appendix of the System Administration Guide for Cisco Unity Connection, Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html . |
| Tip | Include a column with the ListInDirectory header and a value of 1 for each contact if you would like users to be able to address
                                                         messages to VPIM contacts the same way that they address messages to regular Unity Connection users—by extension or by spelling
                                                         the name of the recipient. For a list of optional column headers, see the “ Required and Optional CSV Fields in BAT ” section of the “Bulk Administration Tool” appendix of the System Administration Guide for Cisco Unity Connection, Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html . |
| Step 7 | If your CSV
                                             			 file contains columns of data that you do not want to import, delete the
                                             			 columns. Alternatively, you can title one column NOTES. The BAT ignores data
                                             			 beneath any NOTES column header, but it does not support more than one NOTES
                                             			 column in a CSV file. |
| Step 8 | Confirm that
                                             			 each row contains the appropriate data corresponding to each column header. |
| Step 9 | Save the file
                                             			 as a CSV file. |
| Step 10 | Continue with
                                             			 the following “Creating
                                                				VPIM Contacts Using the Bulk Administration Tool” procedure. |

| Note | The only required column headers for creating contacts are Alias
                                                         				and Extension. However, in order to create VPIM contacts you must also include
                                                         				columns for the remote mailbox ID and the VPIM location. |
|---|---|

| Tip | Include a column with the ListInDirectory header and a value of 1 for each contact if you would like users to be able to address
                                                         messages to VPIM contacts the same way that they address messages to regular Unity Connection users—by extension or by spelling
                                                         the name of the recipient. For a list of optional column headers, see the “ Required and Optional CSV Fields in BAT ” section of the “Bulk Administration Tool” appendix of the System Administration Guide for Cisco Unity Connection, Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html . |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Tools and select Bulk Administration Tool . |
|---|---|
| Step 2 | On the Bulk Administration Tool page, under Select Operation,
                                             			 select Create . |
| Step 3 | Under Select Object Type, select System Contacts . |
| Step 4 | Under Select File, select Browse . |
| Step 5 | In the Choose File dialog box, browse to the directory where you
                                             			 saved the CSV file that you created in the “Preparing
                                                				a CSV File for Creating VPIM Contacts” procedure on page 4-6 and select Open . |
| Step 6 | In the Failed Objects File Name field, enter the path and the
                                             			 name of the file in which you want errors recorded. |
| Step 7 | Select Submit . |

| Step 1 | If the Bulk Administration Tool operation results in any
                                             			 failures, you can immediately inspect the failed objects report file by
                                             			 selecting Download the Failed Objects File . |
|---|---|
| Step 2 | Open the file and correct all problems with the data, as
                                             			 indicated by the information in the FailureReason column for each record. |
| Step 3 | Remove the FailureReason column or change the heading to JUNK . |
| Step 4 | When you have finished modifying the data, save the file as a
                                             			 CSV file with a new name. |
| Step 5 | Run the BAT again with the CSV file that you saved in Step 4 as the
                                             			 input file. Note that each time that you run BAT, the failed objects file is
                                                				overwritten (unless you specify a new name for the file each time you run the
                                                				tool). |
| Step 6 | Repeat this procedure until all VPIM contact accounts are
                                             			 created without error, and then proceed to the “After
                                                				Creating VPIM Contacts” section on page 4-10 . |

| Step 1 | In Cisco Unity Connection Administration, expand Contacts and select Contacts . |
|---|---|
| Step 2 | On the Search Contacts page, in the Contact menu, select New Contact . Alternatively, select Add New on the
                                             			 Search Contacts page to add a new contact. |
| Step 3 | On the New Contact page, enter the following settings and select Save . Table 1. Settings for the New Contact Page Field Setting Alias Enter the alias of the VPIM contact. First Name Enter the first name of the VPIM contact. Last Name Enter the last name of the VPIM contact. Display Name Enter the display name of the VPIM contact. Contact Template Select the template on which to base the VPIM contact. | Field | Setting | Alias | Enter the alias of the VPIM contact. | First Name | Enter the first name of the VPIM contact. | Last Name | Enter the last name of the VPIM contact. | Display Name | Enter the display name of the VPIM contact. | Contact Template | Select the template on which to base the VPIM contact. |
| Field | Setting |
| Alias | Enter the alias of the VPIM contact. |
| First Name | Enter the first name of the VPIM contact. |
| Last Name | Enter the last name of the VPIM contact. |
| Display Name | Enter the display name of the VPIM contact. |
| Contact Template | Select the template on which to base the VPIM contact. |
| Step 4 | On the Edit Contact Basics page, enter the following settings
                                             			 and select Save . Table 2. Settings for the Edit Contact Basics Page Field Setting Voice Name Select Play/Record to record a
                                                            						  name for the VPIM contact. List in Directory Check this check box to list the VPIM contact in the Unity
                                                            						  Connection directory. Partition Select the partition to which the VPIM contact belongs.
                                                            						  Partitions are grouped together into search spaces, which are used to define
                                                            						  the scope of objects (for example, users and distribution lists) that a user or
                                                            						  outside caller can reach while interacting with Unity Connection. A VPIM
                                                            						  contact can belong to only one partition. A partition can belong to more than
                                                            						  one search space. Transfer Enabled (Optional) Check this check box if you want Unity Connection
                                                            						  to transfer incoming calls to a phone number that is associated with the VPIM
                                                            						  contact instead of sending a message to the remote mailbox for the VPIM
                                                            						  contact. Transfer Extension or URI (Optional) Enter the phone number or URI that the phone
                                                            						  system uses to transfer calls to the VPIM contact, including any outdial access
                                                            						  codes, if necessary. This field works together with the Transfer Enabled field. Delivery Location Select the VPIM location for the VPIM contact. VPIM Remote Mailbox Number Enter the mailbox number for the VPIM contact on the remote
                                                            						  voice messaging system. Local Extension (Optional) For VPIM contacts, you can assign a local
                                                            						  extension that fits into the Unity Connection extension numbering scheme. A
                                                            						  local extension allows callers to address messages to the VPIM contact using an
                                                            						  extension, rather than knowing the location ID and the remote mailbox number of
                                                            						  the contact. In addition, if you set the Transfer Enabled and Transfer
                                                            						  Extension fields, callers are able to identify and be transferred to the VPIM
                                                            						  contact. Phone Numbers to Call Contact with Voice Commands (Optional) Use the Dialed Work Phone, Dialed Home Phone, and
                                                            						  Dialed Mobile Phone fields when you want voice recognition users to be able to
                                                            						  call the VPIM contact by specifying a specific phone type for the contact. For dialed phone numbers, include any additional numbers
                                                            						  necessary to dial outside calls (for example 9) and for long-distance dialing
                                                            						  (for example, 1). Phone Numbers or URIs to Identify Contact for Personal Call
                                                            						  Transfer Rules (Optional) Use the Work Phone, Home Phone, Mobile Phone,
                                                            						  Other Number 1, and Other Number 2 fields to enter phone numbers or URIs that
                                                            						  Unity Connection uses when matching the personal call transfer rules of a user
                                                            						  against incoming phone calls from system contacts. | Field | Setting | Voice Name | Select Play/Record to record a
                                                            						  name for the VPIM contact. | List in Directory | Check this check box to list the VPIM contact in the Unity
                                                            						  Connection directory. | Partition | Select the partition to which the VPIM contact belongs.
                                                            						  Partitions are grouped together into search spaces, which are used to define
                                                            						  the scope of objects (for example, users and distribution lists) that a user or
                                                            						  outside caller can reach while interacting with Unity Connection. A VPIM
                                                            						  contact can belong to only one partition. A partition can belong to more than
                                                            						  one search space. | Transfer Enabled | (Optional) Check this check box if you want Unity Connection
                                                            						  to transfer incoming calls to a phone number that is associated with the VPIM
                                                            						  contact instead of sending a message to the remote mailbox for the VPIM
                                                            						  contact. | Transfer Extension or URI | (Optional) Enter the phone number or URI that the phone
                                                            						  system uses to transfer calls to the VPIM contact, including any outdial access
                                                            						  codes, if necessary. This field works together with the Transfer Enabled field. | Delivery Location | Select the VPIM location for the VPIM contact. | VPIM Remote Mailbox Number | Enter the mailbox number for the VPIM contact on the remote
                                                            						  voice messaging system. | Local Extension | (Optional) For VPIM contacts, you can assign a local
                                                            						  extension that fits into the Unity Connection extension numbering scheme. A
                                                            						  local extension allows callers to address messages to the VPIM contact using an
                                                            						  extension, rather than knowing the location ID and the remote mailbox number of
                                                            						  the contact. In addition, if you set the Transfer Enabled and Transfer
                                                            						  Extension fields, callers are able to identify and be transferred to the VPIM
                                                            						  contact. | Phone Numbers to Call Contact with Voice Commands | (Optional) Use the Dialed Work Phone, Dialed Home Phone, and
                                                            						  Dialed Mobile Phone fields when you want voice recognition users to be able to
                                                            						  call the VPIM contact by specifying a specific phone type for the contact. For dialed phone numbers, include any additional numbers
                                                            						  necessary to dial outside calls (for example 9) and for long-distance dialing
                                                            						  (for example, 1). | Phone Numbers or URIs to Identify Contact for Personal Call
                                                            						  Transfer Rules | (Optional) Use the Work Phone, Home Phone, Mobile Phone,
                                                            						  Other Number 1, and Other Number 2 fields to enter phone numbers or URIs that
                                                            						  Unity Connection uses when matching the personal call transfer rules of a user
                                                            						  against incoming phone calls from system contacts. |
| Field | Setting |
| Voice Name | Select Play/Record to record a
                                                            						  name for the VPIM contact. |
| List in Directory | Check this check box to list the VPIM contact in the Unity
                                                            						  Connection directory. |
| Partition | Select the partition to which the VPIM contact belongs.
                                                            						  Partitions are grouped together into search spaces, which are used to define
                                                            						  the scope of objects (for example, users and distribution lists) that a user or
                                                            						  outside caller can reach while interacting with Unity Connection. A VPIM
                                                            						  contact can belong to only one partition. A partition can belong to more than
                                                            						  one search space. |
| Transfer Enabled | (Optional) Check this check box if you want Unity Connection
                                                            						  to transfer incoming calls to a phone number that is associated with the VPIM
                                                            						  contact instead of sending a message to the remote mailbox for the VPIM
                                                            						  contact. |
| Transfer Extension or URI | (Optional) Enter the phone number or URI that the phone
                                                            						  system uses to transfer calls to the VPIM contact, including any outdial access
                                                            						  codes, if necessary. This field works together with the Transfer Enabled field. |
| Delivery Location | Select the VPIM location for the VPIM contact. |
| VPIM Remote Mailbox Number | Enter the mailbox number for the VPIM contact on the remote
                                                            						  voice messaging system. |
| Local Extension | (Optional) For VPIM contacts, you can assign a local
                                                            						  extension that fits into the Unity Connection extension numbering scheme. A
                                                            						  local extension allows callers to address messages to the VPIM contact using an
                                                            						  extension, rather than knowing the location ID and the remote mailbox number of
                                                            						  the contact. In addition, if you set the Transfer Enabled and Transfer
                                                            						  Extension fields, callers are able to identify and be transferred to the VPIM
                                                            						  contact. |
| Phone Numbers to Call Contact with Voice Commands | (Optional) Use the Dialed Work Phone, Dialed Home Phone, and
                                                            						  Dialed Mobile Phone fields when you want voice recognition users to be able to
                                                            						  call the VPIM contact by specifying a specific phone type for the contact. For dialed phone numbers, include any additional numbers
                                                            						  necessary to dial outside calls (for example 9) and for long-distance dialing
                                                            						  (for example, 1). |
| Phone Numbers or URIs to Identify Contact for Personal Call
                                                            						  Transfer Rules | (Optional) Use the Work Phone, Home Phone, Mobile Phone,
                                                            						  Other Number 1, and Other Number 2 fields to enter phone numbers or URIs that
                                                            						  Unity Connection uses when matching the personal call transfer rules of a user
                                                            						  against incoming phone calls from system contacts. |
| Step 5 | Repeat Step 2 through Step 4 for all
                                             			 remaining VPIM contacts that you want to create. |

| Field | Setting |
|---|---|
| Alias | Enter the alias of the VPIM contact. |
| First Name | Enter the first name of the VPIM contact. |
| Last Name | Enter the last name of the VPIM contact. |
| Display Name | Enter the display name of the VPIM contact. |
| Contact Template | Select the template on which to base the VPIM contact. |

| Field | Setting |
|---|---|
| Voice Name | Select Play/Record to record a
                                                            						  name for the VPIM contact. |
| List in Directory | Check this check box to list the VPIM contact in the Unity
                                                            						  Connection directory. |
| Partition | Select the partition to which the VPIM contact belongs.
                                                            						  Partitions are grouped together into search spaces, which are used to define
                                                            						  the scope of objects (for example, users and distribution lists) that a user or
                                                            						  outside caller can reach while interacting with Unity Connection. A VPIM
                                                            						  contact can belong to only one partition. A partition can belong to more than
                                                            						  one search space. |
| Transfer Enabled | (Optional) Check this check box if you want Unity Connection
                                                            						  to transfer incoming calls to a phone number that is associated with the VPIM
                                                            						  contact instead of sending a message to the remote mailbox for the VPIM
                                                            						  contact. |
| Transfer Extension or URI | (Optional) Enter the phone number or URI that the phone
                                                            						  system uses to transfer calls to the VPIM contact, including any outdial access
                                                            						  codes, if necessary. This field works together with the Transfer Enabled field. |
| Delivery Location | Select the VPIM location for the VPIM contact. |
| VPIM Remote Mailbox Number | Enter the mailbox number for the VPIM contact on the remote
                                                            						  voice messaging system. |
| Local Extension | (Optional) For VPIM contacts, you can assign a local
                                                            						  extension that fits into the Unity Connection extension numbering scheme. A
                                                            						  local extension allows callers to address messages to the VPIM contact using an
                                                            						  extension, rather than knowing the location ID and the remote mailbox number of
                                                            						  the contact. In addition, if you set the Transfer Enabled and Transfer
                                                            						  Extension fields, callers are able to identify and be transferred to the VPIM
                                                            						  contact. |
| Phone Numbers to Call Contact with Voice Commands | (Optional) Use the Dialed Work Phone, Dialed Home Phone, and
                                                            						  Dialed Mobile Phone fields when you want voice recognition users to be able to
                                                            						  call the VPIM contact by specifying a specific phone type for the contact. For dialed phone numbers, include any additional numbers
                                                            						  necessary to dial outside calls (for example 9) and for long-distance dialing
                                                            						  (for example, 1). |
| Phone Numbers or URIs to Identify Contact for Personal Call
                                                            						  Transfer Rules | (Optional) Use the Work Phone, Home Phone, Mobile Phone,
                                                            						  Other Number 1, and Other Number 2 fields to enter phone numbers or URIs that
                                                            						  Unity Connection uses when matching the personal call transfer rules of a user
                                                            						  against incoming phone calls from system contacts. |

| Note | Changes to the Map VPIM Contact Extensions setting on the Contact Creation page for a VPIM location affect only VPIM contacts
                                          that are created after the setting is saved. VPIM contacts that already existed before the Map VPIM Contact Extensions setting
                                          is changed are not automatically updated. You must manually change the extension for each previously existing VPIM contact
                                          for that VPIM location. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Networking and select VPIM Locations . |
|---|---|
| Step 2 | On the Search VPIM Locations page, select the name of the VPIM
                                                			 location for which you want to configure contact creation settings. |
| Step 3 | On the Edit VPIM Location page, in the Edit menu, select Contact Creation . |
| Step 4 | On the Contact Creation page, check the Automatically Create VPIM Contacts check box to
                                                			 enable automatic creation of a VPIM contact record for this location when a
                                                			 VPIM message arrives and the sender does not already have a corresponding VPIM
                                                			 contact record. |
| Step 5 | If you checked the Automatically Create VPIM Contacts check box
                                                			 in Step 4 , in the Contact
                                                			 Template list, select the template on which to base the automatically created
                                                			 contacts. |
| Step 6 | In the Automatically Modify VPIM Contact field, select one of
                                                			 the following to apply to VPIM contacts for this location: No Automatic Update of Contacts —The VPIM contact record is
                                                         					 not updated with the sender information in a VPIM message when an incoming
                                                         					 message has changed sender information. Only When the Text Name Changes —The VPIM contact record is
                                                         					 updated only when the text name received in the VPIM message does not match the
                                                         					 name of the VPIM contact. With Each VPIM Message —Every incoming VPIM message from a
                                                         					 VPIM contact at this location results in an update to the corresponding VPIM
                                                         					 contact record. |
| Step 7 | Check the Automatically Delete VPIM Contact check box to
                                                			 enable automatic deletion of a VPIM contact for this location when a VPIM
                                                			 message is returned as undeliverable. |
| Step 8 | Check the Allow VPIM Contact Display Name Updates check box to
                                                			 enable automatic updates to the VPIM contact display name when an incoming
                                                			 message from this location has a changed display name for the sender. |
| Step 9 | Check the Allow VPIM Contacts Without Recorded Voice Names check box to enable automatic updates for this location to records for VPIM
                                                			 contacts that do not have a recorded name. |
| Step 10 | In the Mapping Text Names field, select one of the following
                                                			 options to indicate how text names in incoming messages from this location are
                                                			 mapped to the display names for automatically created VPIM contact records: Directly to VPIM Contact Display Names —The display names for
                                                         					 VPIM contacts match the corresponding text names. Custom —Enter the rule that defines how text names are mapped
                                                         					 to display names for VPIM contacts. You can enter the tokens <FN>,
                                                         					 <LN>, or <TN> (respectively first name, last name, or text name) in
                                                         					 any combination, along with any additional text. Always precede <FN>,
                                                         					 <LN>, or <TN> with a space, comma, or semicolon unless it appears
                                                         					 at the beginning of the rule. In addition, always follow one of these tokens
                                                         					 with a space, comma or semicolon unless it appears at the end of the rule. No
                                                         					 additional characters are required at the beginning or end of a rule. |
| Step 11 | In the Map VPIM Contact Extensions To field, select one of the
                                                			 following settings to indicate how the phone number on incoming messages from
                                                			 this location is mapped to the extension for automatically created VPIM contact
                                                			 records: Phone Number —Extensions are the same as the phone numbers
                                                         					 that are parsed from incoming VPIM messages. Phone Number - Remote Phone Prefix —Extensions are formed by
                                                         					 removing the remote phone prefix from the beginning of the phone numbers. Location Dial ID + Phone Number —Extensions are formed by
                                                         					 adding the location Dial ID in front of the phone numbers. Location Dial ID + Phone Number - Remote Phone
                                                            						Prefix —Extensions are formed by removing the remote phone prefix from the
                                                         					 beginning of the phone number, and adding the location Dial ID in front of the
                                                         					 resulting number. |
| Step 12 | Select Save. |
| Step 13 | On the VPIM Location menu, select Search VPIM Locations . |
| Step 14 | Repeat Step 2 through Step 13 for
                                                			 all remaining VPIM locations. |

| Step 1 | In Cisco Unity Connection Administration, expand Networking and select VPIM Locations . |
|---|---|
| Step 2 | On the Search VPIM Locations page, select the name of the VPIM
                                          			 location for which you want to add an alternate name. |
| Step 3 | On the Edit VPIM Location page, in the Edit menu, select Alternate Names . |
| Step 4 | On the Edit Alternate Names page, in the Display Name field,
                                          			 enter the alternate name you want for the VPIM location, then select Add New . |
| Step 5 | On the VPIM Location menu, select Search VPIM Locations . |
| Step 6 | Repeat Step 2 through Step 5 for all
                                          			 remaining VPIM locations for which you want to add alternate names. |

| Step 1 | In Cisco Unity Connection Administration, expand Contacts and select Contacts . |
|---|---|
| Step 2 | On the Search Contacts page, check the check boxes next to the
                                       			 VPIM contacts that you want to delete. |
| Step 3 | Select Delete Selected . |
| Step 4 | When prompted to confirm the deletion, select OK . |

| Note | If the Unity Connection is in HTTPS network, make sure to run
                                             				the Network Remover task to completely remove the location from the network.
                                             				The VPIM contacts get automatically deleted on deleting a VPIM location. |
|---|---|