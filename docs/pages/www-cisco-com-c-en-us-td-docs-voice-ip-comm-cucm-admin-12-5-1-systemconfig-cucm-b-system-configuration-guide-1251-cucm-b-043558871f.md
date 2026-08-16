---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-043558871f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_011011.html
retrieved_at: 2026-08-16T17:31:15.605916+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure URI Dialing

## Chapter: Configure URI Dialing

# Configure URI Dialing

## URI Dialing Overview

Unified Communications Manager supports dialing using directory URIs for call addressing. A directory URI is a uniform resource identifier, a string of
                           characters that can be used to identify a directory number. Directory URIs look like email addresses and follow the username@host
                           format where the host portion is an IPv4 address or a fully qualified domain name. If that directory number is assigned to
                           a phone, Unified Communications Manager can route calls to that phone using the directory URI. URI dialing is available for SIP and SCCP endpoints that support directory
                           URIs.

### Directory URI
                           	 Format

Directory URIs are alphanumeric strings that consist of a user and a host address separated by the @ symbol.

Cisco Unified Communications Manager supports the following formats for directory URIs:

user@domain (for example, joe@cisco.com)

user@ip_address (for example, joe@10.10.10.1)

The system supports the following formats in the user portion of a directory URI (the portion before the @ symbol):

Accepted characters are a-z, A-Z, 0-9, !, $, %, &, *, _, +, ~, -, =, , ?, , ‘, ,, ., /, ( and ) .

The user portion has a maximum length of 47 characters.

Cisco Unified Communications Manager automatically applies percent encoding to the following characters when the directory
                                       URI is saved in the database:

# % ^ ` { } | \ : ” < > [ ] \ ‘ and spaces.

The user portion of a directory URI is case sensitive by default. You can edit the user portion to be case insensitive by
                                             editing the URI Lookup Policy enterprise parameter.

Cisco Unified
                                 		  Communications Manager supports the following formats in the host portion of a
                                 		  directory URI (the portion after the @ symbol):

Supports IPv4
                                       				addresses or fully qualified domain names.

Accepted
                                       				characters are alphanumeric characters, hyphens (-), and dots (.).

The host
                                       				portion cannot start or end with a hyphen (-).

The host
                                       				portion cannot have two dots in a row.

The host
                                       				portion has a minimum length of two characters.

The host
                                       				portion is not case sensitive.

Within Cisco Unified Communications Manager Administration , when you use Bulk Administration to import a CSV file that contains directory URIs with embedded double quotes and commas,
                                             you must enclose the entire directory URI in double quotes (").

### Call Forward to URI

Call-forwarding to URIs won't be possible from physical phones.

Call-forward to a URI can only be configured through applications if that URI is already in the Unified Communications Manager database. If the URI is not in the database, then the application will error out "Call Forward Setting Failed /n Failed to
                                    forward calls to: New Number" while trying to configure call-forward.

Call-forward can be configured for any URI, whether the URI exists in the database or not through the Unified Communications
                                    Manager Administration page.

You can configure call-forwards on the Cisco Unified Communications Self Care Portal > End User Page to any URI, regardless of whether it exists in the database. The 'Percent Encoding' must be used when entering these
                                    characters # % ^ ` { } | \ : ? < > [ ] \ ‘ . For example, %3A is used for mentioning : and %20 is used for mentioning space.

You must provide " mobile%3A%2012345@cisco.com " under the Call-Forward section of the Cisco Unified Communications Self Care Portal > End User page, if you need to forward calls to the URI " mobile: 12345@cisco.com ".

## URI Dialing
                        	 Prerequisites

Before you
                              		  configure the URI dialing, you must set up an ILS network and enable Global
                              		  Dial Plan Replication in the ILS network. Refer the following sections to
                              		  complete this task:

Global Dial Plan Replication Task Flow

ILS Configuration Task Flow

## URI Dialing
                        	 Configuration Task Flow

Step 1

Assign
                                       			 directory URIs to the local cluster in the network:

- Assign Directory URI to Users

- Associate Directory URI with Directory Numbers

Provision end
                                          				users into your system and assign directory URI to those end users. Also,
                                          				configure a directory number and associate a directory URI with that directory
                                          				number.

Step 2

Assign Default Directory URI Partition

Assign the
                                          				default directory URI partition to an existing partition that is located in a
                                          				calling search space.

Step 3

Configure SIP Profiles for URI Dialing

Configure the
                                          				SIP profiles to configure intercluster URI dialing in your network.

Step 4

Configure SIP Trunks for URI Dialing

Configure
                                          				whether Cisco
                                             				  Unified Communications Manager inserts a directory number, a
                                          				directory URI, or a blended address for outgoing SIP messages.

Step 5

Configure SIP Route Patterns

Configure SIP
                                          				route patterns to route intercluster directory URI calls.

Step 6

Repeat step 1
                                       			 to step 5 for all the clusters in your ILS network.

Perform this step if you have multiple clusters in your ILS
                                          				network.

Step 7

Import Directory URI Catalogs

(Optional) If
                                          				you want to place directory URI calls to a Cisco TelePresence Video
                                          				Communications Server, or a third-party call control system, import directory
                                          				URI catalogs from a CSV file for the other system into any hub cluster in the
                                          				ILS network.

### Assign Directory
                           	 URI to Users

Perform the
                                 		  following steps to assign a directory URI to an end user.

Step 1

In Cisco
                                          			 Unified CM Administration, choose User
                                                				  Management > End User .

Step 2

In the Find
                                             				and List Users window, specify the search criteria and click Find .

Step 3

Choose a user
                                          			 from the resulting list. The End
                                             				User Configuration window appears.

Step 4

In the Directory URI field, enter a directory URI that you
                                          			 want to associate to this end user. A directory URI looks like an email address
                                          			 and follows the user@host format.

If you
                                                         				  enter a directory URI and also enter a directory number in the Primary Extension field, this directory URI
                                                         				  automatically becomes the primary directory URI that is associated to that
                                                         				  directory number.

Step 5

Click Save .

### Associate
                           	 Directory URI with Directory Numbers

#### Before you begin

Assign Directory URI to Users

Step 1

In Cisco
                                          			 Unified CM Administration, choose Device > Phone . The Find
                                             				and List Phones window appears.

Step 2

Specify the
                                          			 filter criteria and click Find .

Step 3

Click on the
                                          			 device for which you want to associate the directory number. The Phone
                                             				Configuration window appears.

Step 4

In the Association pane:

- Click on an existing
                                             				directory number.

- Click on Add
                                                				  a new DN if no directory numbers are configured.

Step 5

In the Directory Number Configuration window, enter the
                                          			 directory URI address in the URI text box.

Step 6

From the Partition drop-down list, choose the partition to
                                          			 which the directory URI belongs.

Ensure that
                                             				the directory URI that you enter is unique within the partition that you
                                             				choose. If you do not want to restrict access to the URI, choose None for the partition.

Step 7

Click Save .

#### What to do next

Assign Default Directory URI Partition

### Assign Default
                           	 Directory URI Partition

Perform the
                                 		  following procedure to assign a default directory URI partition.

#### Before you begin

Associate Directory URI with Directory Numbers

Step 1

In Cisco
                                          			 Unified CM Administration, choose System > Enterprise
                                                				  Parameters . The Enterprise Parameters Configuration window appears.

Step 2

For the Directory URI Alias Partition in the End
                                             				User Parameters area, choose an existing partition that is in an
                                          			 existing calling search space.

Step 3

Click Save .

#### What to do next

Configure SIP Profiles for URI Dialing

### Configure SIP
                           	 Profiles for URI Dialing

#### Before you begin

Assign Default Directory URI Partition

Step 1

In Cisco
                                          			 Unified CM Administration, choose Device > Device
                                                				  Settings > SIP Profile . The Find
                                             				and List SIP Profiles window appears.

Step 2

Enter the
                                          			 appropriate search criteria and click Find . A list of existing SIP profiles appear.

Step 3

Select the SIP
                                          			 profile that you want to view. The SIP
                                             				Profile Configuration window appears.

Step 4

From the Dial
                                             				String Interpretation drop-down list, choose one of the following
                                          			 options:

- Always treat all dial
                                                				  strings as URI addresses —Select this option to treat the address of
                                             				incoming calls as URI addresses.

- Phone number consists of
                                                				  characters 0–9, A–D, *, and + (others treated as URI
                                                				  addresses) —Select this option to treat the incoming call as a
                                             				directory number if all the characters in the user portion of the SIP identity
                                             				header fall within this range. If the user portion of the address uses any
                                             				characters that do not fall within this range, the address is treated as a URI.

- Phone number consists of
                                                				  characters 0-9, *, and + (others treated as URI addresses —Select
                                             				this option to treat the incoming call as a directory number if all the
                                             				characters in the user portion of the SIP identity header fall within this
                                             				range. If the user portion of the address uses any characters that do not fall
                                             				within this range, the address is treated as a URI.

Step 5

Check the Use
                                             				Fully Qualified Domain Name in SIP Requests check box for all the
                                          			 SIP profiles in your network.

Step 6

Click Apply
                                             				Config .

#### What to do next

Configure SIP Trunks for URI Dialing

### Configure SIP
                           	 Trunks for URI Dialing

If you are deploying URI dialing, configure the contact header addressing policy for the SIP trunks in your network. Cisco Unified Communications Manager can insert a directory number, directory URI, or a blended address that includes both the directory number and directory
                                 URI in the SIP identity headers for outgoing SIP messages.

Step 1

From Cisco Unified CM Administration, choose Device > Trunk .

Step 2

Click Find and select an existing SIP trunk.

Step 3

In the Outbound Calls area, select one of the following from the Calling and Connected Party Info Format drop-down list:

- Deliver DN only in connected party —In outgoing SIP messages, Unified Communications Manager inserts the calling party’s directory number in the SIP contact
                                             header information. This is the default setting.

- Deliver URI only in connected party, if available —In outgoing SIP messages, Unified Communications Manager inserts the sending party’s directory URI in the SIP contact header.
                                             If a directory URI is not available, Unified Communications Manager inserts the directory number instead.

- Deliver URI and DN in connected party, if available —In outgoing SIP messages, Unified Communications Manager inserts a blended address that includes the calling party's directory
                                             URI and directory number in the SIP contact headers. If a directory URI is not available, Unified Communications Manager includes
                                             the directory number only.

Step 4

Click Save .

### Configure SIP
                           	 Route Patterns

You must configure
                                 		  SIP route patterns to route intercluster directory URI calls.

Follow these steps
                                 		  to configure SIP route patterns.

#### Before you begin

Configure SIP Trunks for URI Dialing

Step 1

In Cisco
                                          			 Unified CM Administration, choose Call
                                                				  Routing > SIP Route Pattern .

Step 2

Choose one of
                                          			 the following options:

- To add a new SIP route
                                             				pattern, click the Add
                                                				  New button.

- To modify the settings for
                                             				an existing SIP route pattern, enter the search criteria, click Find , and choose a SIP route pattern from the
                                             				resulting list.

Step 3

Configure the
                                          			 fields in the SIP
                                             				Route Pattern Configuration window. See the online help for more
                                          			 information about the fields and their configuration options.

Step 4

Click Save .

#### What to do next

(Optional) Import Directory URI Catalogs

### Import Directory
                           	 URI Catalogs

Cisco Unified
                                 		  Communications Manager allows you to import global dial plan data from a CSV
                                 		  file into any hub cluster in an ILS network and ILS replicates the imported
                                 		  global dial plan data throughout the ILS network allowing you to interoperate
                                 		  Cisco Unified Communications Manager with a Cisco TelePresence Video
                                 		  Communications Server or a third-party call control system.

(Optional) To
                                 		  import directory URI catalogs, follow this procedure:

Step 1

From Cisco
                                          			 Unified CM Administration, choose Call
                                                				  Routing > Global Dial Plan RepIication > Imported Global Dial Plan
                                                				  Catalog .

Step 2

From the Find
                                             				and List Imported Global Dial Plan Catalogs window, perform one of
                                          			 the following tasks:

- Click Find and select an existing catalog from the resulting list.

- Click Add New to add a new catalog.

Step 3

From the Imported Global Dial Plan Catalog Settings window, in
                                          			 the Name field, enter a unique name to identify the
                                          			 catalog that you want to import.

Step 4

(Optional) In the Description field, enter a description of the catalog.

Step 5

In the Route
                                             				String field, create a route string for the system from which you
                                          			 are importing the catalog.

Step 6

Click Save .

Step 7

From Cisco Unified CM Administration, choose Bulk Administration > Upload/Download Files .

- Click Add New .

- Click Browse and select the CSV file for the catalog that you want to import.

Step 8

In the Select
                                             				the Target drop-down list, select Imported Directory URIs and Patterns .

Step 9

In the Select
                                             				Transaction Type drop-down list, select Insert
                                             				Imported Directory URIs and Patterns .

Step 10

Click Save .

Step 11

From Cisco Unified CM Administration, choose Bulk Administration > Directory URIs and Patterns > Insert Imported Directory URIs and Patterns .

Step 12

In the File
                                             				Name drop-down list, choose the CSV file that contains the catalog
                                          			 that you want to import.

Step 13

In the Imported Directory URI Catalog drop-down list,
                                          			 choose the catalog that you named in the Imported Global Dial Plan Catalog window.

Step 14

In the Job
                                             				Description text box, enter a name for the job that you are about
                                          			 to run.

Step 15

Perform one of
                                          			 the following steps:

- If you want to run the job
                                             				now, select the Run
                                                				  Immediately option, and click Submit .

- If you want to schedule the
                                             				job to run at a specified time, select the Run
                                                				  Later radio button and click Submit .

| Note | The user portion of a directory URI is case sensitive by default. You can edit the user portion to be case insensitive by
                                             editing the URI Lookup Policy enterprise parameter. When you apply percent encoding, the digit length of the directory URI increases. For example, if you input joe smith#@cisco.com
                                          (20 characters) as a directory URI, Unified Communications Manager stores the directory URI in the database as joe%20smith%23@cisco.com (24 characters). Due to database restrictions, the Directory URI field has a maximum length of 254 characters. |
|---|---|

| Note | Within Cisco Unified Communications Manager Administration , when you use Bulk Administration to import a CSV file that contains directory URIs with embedded double quotes and commas,
                                             you must enclose the entire directory URI in double quotes ("). |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Assign
                                       			 directory URIs to the local cluster in the network: Assign Directory URI to Users Associate Directory URI with Directory Numbers | Provision end
                                          				users into your system and assign directory URI to those end users. Also,
                                          				configure a directory number and associate a directory URI with that directory
                                          				number. Note For both
                                                   				end user configuration and directory number configuration, you can also use
                                                   				Bulk Administration to import end users, directory URIs, directory numbers, and
                                                   				phones into Cisco
                                                      				  Unified Communications Manager . For more information, see the Bulk
                                                      				  Administration Guide for Cisco Unified Communications Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . | Note | For both
                                                   				end user configuration and directory number configuration, you can also use
                                                   				Bulk Administration to import end users, directory URIs, directory numbers, and
                                                   				phones into Cisco
                                                      				  Unified Communications Manager . For more information, see the Bulk
                                                      				  Administration Guide for Cisco Unified Communications Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
| Note | For both
                                                   				end user configuration and directory number configuration, you can also use
                                                   				Bulk Administration to import end users, directory URIs, directory numbers, and
                                                   				phones into Cisco
                                                      				  Unified Communications Manager . For more information, see the Bulk
                                                      				  Administration Guide for Cisco Unified Communications Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
| Step 2 | Assign Default Directory URI Partition | Assign the
                                          				default directory URI partition to an existing partition that is located in a
                                          				calling search space. |
| Step 3 | Configure SIP Profiles for URI Dialing | Configure the
                                          				SIP profiles to configure intercluster URI dialing in your network. |
| Step 4 | Configure SIP Trunks for URI Dialing | Configure
                                          				whether Cisco
                                             				  Unified Communications Manager inserts a directory number, a
                                          				directory URI, or a blended address for outgoing SIP messages. |
| Step 5 | Configure SIP Route Patterns | Configure SIP
                                          				route patterns to route intercluster directory URI calls. |
| Step 6 | Repeat step 1
                                       			 to step 5 for all the clusters in your ILS network. | Perform this step if you have multiple clusters in your ILS
                                          				network. |
| Step 7 | Import Directory URI Catalogs | (Optional) If
                                          				you want to place directory URI calls to a Cisco TelePresence Video
                                          				Communications Server, or a third-party call control system, import directory
                                          				URI catalogs from a CSV file for the other system into any hub cluster in the
                                          				ILS network. |

| Note | For both
                                                   				end user configuration and directory number configuration, you can also use
                                                   				Bulk Administration to import end users, directory URIs, directory numbers, and
                                                   				phones into Cisco
                                                      				  Unified Communications Manager . For more information, see the Bulk
                                                      				  Administration Guide for Cisco Unified Communications Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html . |
|---|---|

| Step 1 | In Cisco
                                          			 Unified CM Administration, choose User
                                                				  Management > End User . |
|---|---|
| Step 2 | In the Find
                                             				and List Users window, specify the search criteria and click Find . |
| Step 3 | Choose a user
                                          			 from the resulting list. The End
                                             				User Configuration window appears. |
| Step 4 | In the Directory URI field, enter a directory URI that you
                                          			 want to associate to this end user. A directory URI looks like an email address
                                          			 and follows the user@host format. Note If you
                                                         				  enter a directory URI and also enter a directory number in the Primary Extension field, this directory URI
                                                         				  automatically becomes the primary directory URI that is associated to that
                                                         				  directory number. | Note | If you
                                                         				  enter a directory URI and also enter a directory number in the Primary Extension field, this directory URI
                                                         				  automatically becomes the primary directory URI that is associated to that
                                                         				  directory number. |
| Note | If you
                                                         				  enter a directory URI and also enter a directory number in the Primary Extension field, this directory URI
                                                         				  automatically becomes the primary directory URI that is associated to that
                                                         				  directory number. |
| Step 5 | Click Save . |

| Note | If you
                                                         				  enter a directory URI and also enter a directory number in the Primary Extension field, this directory URI
                                                         				  automatically becomes the primary directory URI that is associated to that
                                                         				  directory number. |
|---|---|

| Step 1 | In Cisco
                                          			 Unified CM Administration, choose Device > Phone . The Find
                                             				and List Phones window appears. |
|---|---|
| Step 2 | Specify the
                                          			 filter criteria and click Find . |
| Step 3 | Click on the
                                          			 device for which you want to associate the directory number. The Phone
                                             				Configuration window appears. |
| Step 4 | In the Association pane: Click on an existing
                                             				directory number. Click on Add
                                                				  a new DN if no directory numbers are configured. |
| Step 5 | In the Directory Number Configuration window, enter the
                                          			 directory URI address in the URI text box. |
| Step 6 | From the Partition drop-down list, choose the partition to
                                          			 which the directory URI belongs. Ensure that
                                             				the directory URI that you enter is unique within the partition that you
                                             				choose. If you do not want to restrict access to the URI, choose None for the partition. |
| Step 7 | Click Save . |

| Step 1 | In Cisco
                                          			 Unified CM Administration, choose System > Enterprise
                                                				  Parameters . The Enterprise Parameters Configuration window appears. |
|---|---|
| Step 2 | For the Directory URI Alias Partition in the End
                                             				User Parameters area, choose an existing partition that is in an
                                          			 existing calling search space. |
| Step 3 | Click Save . |

| Step 1 | In Cisco
                                          			 Unified CM Administration, choose Device > Device
                                                				  Settings > SIP Profile . The Find
                                             				and List SIP Profiles window appears. |
|---|---|
| Step 2 | Enter the
                                          			 appropriate search criteria and click Find . A list of existing SIP profiles appear. |
| Step 3 | Select the SIP
                                          			 profile that you want to view. The SIP
                                             				Profile Configuration window appears. |
| Step 4 | From the Dial
                                             				String Interpretation drop-down list, choose one of the following
                                          			 options: Always treat all dial
                                                				  strings as URI addresses —Select this option to treat the address of
                                             				incoming calls as URI addresses. Phone number consists of
                                                				  characters 0–9, A–D, *, and + (others treated as URI
                                                				  addresses) —Select this option to treat the incoming call as a
                                             				directory number if all the characters in the user portion of the SIP identity
                                             				header fall within this range. If the user portion of the address uses any
                                             				characters that do not fall within this range, the address is treated as a URI. Phone number consists of
                                                				  characters 0-9, *, and + (others treated as URI addresses —Select
                                             				this option to treat the incoming call as a directory number if all the
                                             				characters in the user portion of the SIP identity header fall within this
                                             				range. If the user portion of the address uses any characters that do not fall
                                             				within this range, the address is treated as a URI. |
| Step 5 | Check the Use
                                             				Fully Qualified Domain Name in SIP Requests check box for all the
                                          			 SIP profiles in your network. |
| Step 6 | Click Apply
                                             				Config . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Trunk . |
|---|---|
| Step 2 | Click Find and select an existing SIP trunk. |
| Step 3 | In the Outbound Calls area, select one of the following from the Calling and Connected Party Info Format drop-down list: Deliver DN only in connected party —In outgoing SIP messages, Unified Communications Manager inserts the calling party’s directory number in the SIP contact
                                             header information. This is the default setting. Deliver URI only in connected party, if available —In outgoing SIP messages, Unified Communications Manager inserts the sending party’s directory URI in the SIP contact header.
                                             If a directory URI is not available, Unified Communications Manager inserts the directory number instead. Deliver URI and DN in connected party, if available —In outgoing SIP messages, Unified Communications Manager inserts a blended address that includes the calling party's directory
                                             URI and directory number in the SIP contact headers. If a directory URI is not available, Unified Communications Manager includes
                                             the directory number only. |
| Step 4 | Click Save . |

| Step 1 | In Cisco
                                          			 Unified CM Administration, choose Call
                                                				  Routing > SIP Route Pattern . |
|---|---|
| Step 2 | Choose one of
                                          			 the following options: To add a new SIP route
                                             				pattern, click the Add
                                                				  New button. To modify the settings for
                                             				an existing SIP route pattern, enter the search criteria, click Find , and choose a SIP route pattern from the
                                             				resulting list. |
| Step 3 | Configure the
                                          			 fields in the SIP
                                             				Route Pattern Configuration window. See the online help for more
                                          			 information about the fields and their configuration options. |
| Step 4 | Click Save . |

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose Call
                                                				  Routing > Global Dial Plan RepIication > Imported Global Dial Plan
                                                				  Catalog . |
|---|---|
| Step 2 | From the Find
                                             				and List Imported Global Dial Plan Catalogs window, perform one of
                                          			 the following tasks: Click Find and select an existing catalog from the resulting list. Click Add New to add a new catalog. |
| Step 3 | From the Imported Global Dial Plan Catalog Settings window, in
                                          			 the Name field, enter a unique name to identify the
                                          			 catalog that you want to import. |
| Step 4 | (Optional) In the Description field, enter a description of the catalog. |
| Step 5 | In the Route
                                             				String field, create a route string for the system from which you
                                          			 are importing the catalog. Note Route strings can be up to 250 alphanumeric characters long and can include dots and dashes. | Note | Route strings can be up to 250 alphanumeric characters long and can include dots and dashes. |
| Note | Route strings can be up to 250 alphanumeric characters long and can include dots and dashes. |
| Step 6 | Click Save . |
| Step 7 | From Cisco Unified CM Administration, choose Bulk Administration > Upload/Download Files . Click Add New . Click Browse and select the CSV file for the catalog that you want to import. Note Ensure that the CSV file that you use for the import is compatible with the version of Cisco Unified Communications Manager . For example, a CSV file that is compatible to import into Version 9.0(1) is not compatible with Version 10.0(1). | Note | Ensure that the CSV file that you use for the import is compatible with the version of Cisco Unified Communications Manager . For example, a CSV file that is compatible to import into Version 9.0(1) is not compatible with Version 10.0(1). |
| Note | Ensure that the CSV file that you use for the import is compatible with the version of Cisco Unified Communications Manager . For example, a CSV file that is compatible to import into Version 9.0(1) is not compatible with Version 10.0(1). |
| Step 8 | In the Select
                                             				the Target drop-down list, select Imported Directory URIs and Patterns . |
| Step 9 | In the Select
                                             				Transaction Type drop-down list, select Insert
                                             				Imported Directory URIs and Patterns . |
| Step 10 | Click Save . |
| Step 11 | From Cisco Unified CM Administration, choose Bulk Administration > Directory URIs and Patterns > Insert Imported Directory URIs and Patterns . |
| Step 12 | In the File
                                             				Name drop-down list, choose the CSV file that contains the catalog
                                          			 that you want to import. |
| Step 13 | In the Imported Directory URI Catalog drop-down list,
                                          			 choose the catalog that you named in the Imported Global Dial Plan Catalog window. |
| Step 14 | In the Job
                                             				Description text box, enter a name for the job that you are about
                                          			 to run. |
| Step 15 | Perform one of
                                          			 the following steps: If you want to run the job
                                             				now, select the Run
                                                				  Immediately option, and click Submit . If you want to schedule the
                                             				job to run at a specified time, select the Run
                                                				  Later radio button and click Submit . Note If you choose the Run Later option, you must use the Bulk Administration Job Scheduler to schedule when the job runs. Cisco Unified Communications Manager saves all imported +E.164 patterns to the Global Learned +E.164 Patterns partition. | Note | If you choose the Run Later option, you must use the Bulk Administration Job Scheduler to schedule when the job runs. |
| Note | If you choose the Run Later option, you must use the Bulk Administration Job Scheduler to schedule when the job runs. |

| Note | Route strings can be up to 250 alphanumeric characters long and can include dots and dashes. |
|---|---|

| Note | Ensure that the CSV file that you use for the import is compatible with the version of Cisco Unified Communications Manager . For example, a CSV file that is compatible to import into Version 9.0(1) is not compatible with Version 10.0(1). |
|---|---|

| Note | If you choose the Run Later option, you must use the Bulk Administration Job Scheduler to schedule when the job runs. |
|---|---|