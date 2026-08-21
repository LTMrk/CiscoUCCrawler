---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-user-guide--598a926028
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/User/guide/ucce_b_scripting-and-media-routing-guide_12_6/ucce_b_scripting-and-media-routing-guide_chapter_011.html
retrieved_at: 2026-08-21T11:54:25.226312+00:00
---

Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(1)

# Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(1)

Updated: June 11, 2020

Chapter: Contact Categorization

## Chapter: Contact Categorization

# Contact Categorization

## Categorization and Call Type

Categorization is the process of classifying a contact based on certain
                              data associated with the contact. Through categorization, a script can
                              determine the best way to process a contact.

When you create a routing script, you typically use the nodes available in
                              Script Editor to define how the script is to categorize contacts. By
                              categorizing contacts, a script can provide  unique solutions for different
                              customer's needs.

### Categorization Through Scheduling Scripts by Call Type

Call types provide the first level of categorization for routing scripts. You schedule scripts by call type; therefore, the call type
                                 of a contact determines which script is run, enabling you to create different scripts for different types of contacts.

### Change Call Type to Static

You can change the call type of a contact to static by using the Call Type node in a script. The Call Type node is in the
                                 Routing tab of the Palette.

The following figure is the Call Type Properties dialog box of the Static Call Type node:

To define a static call type node, complete the following steps.

Step 1

In the Call Type tab, click the Statically radio button.

Step 2

From the Call Type list, click the call type to assign to the contact.

#### What to do next

Warning

The Call Type node changes the call type and continues running the current script. The Requalify Call node stops running the
                                             current script and runs a new script associated with that call type.

### Change Call Type to
                           	 Dynamic

You can change the
                                 		  call type of a contact to dynamic by using the Call Type node in a script. The Call Type is on the
                                 		  Routing tab of the Palette.

Dynamic call type selection is not available when an External Authorization server is used with Internet Script Editor and
                                             will be grayed out in the interface.

The following figure
                                 		  is the Call Type Properties dialog box of a dynamic call type node:

To define a dynamic
                                 		  call type node, complete the following steps.

Step 1

On the call type
                                          			 tab, select the Dynamically radio button.

Step 2

To dynamically
                                          			 change the call type of a contact by call type name, In the Find By section,
                                          			 select the Call
                                             				Type Name radio button.

Step 3

To dynamically
                                          			 change the call type of a contact by call type ID, In the Find By section,
                                          			 select the Call
                                             				Type ID radio button.

Step 4

To determine
                                          			 which call type name or ID to use to change the call type of a contact, click
                                          			 the Formula Editor button to create a formula.

#### What to do next

Warning

The Call Type node changes the call type and continues the current script execution. The Requalify Call node terminates the
                                             current script execution and runs a new script associated with that call type.

### Change Call Type and Run a New Script

You can change the call type of a contact from within a script and run a new script associated with the call type by using
                                 the Requalify Call node ( in the Routing tab of the Palette).

Following is the Requalify Properties dialog box of the Requalify Call node:

Define Requalify node properties as follows:

Step 1

In the Requalify Call Tab, select the Call type to assign to
                                          the contact.

Step 2

Optionally, add comments.

#### What to do next

Warning

The Call Type node changes the call type and continues running the current script. The Requalify Call node stops running the
                                             current script and runs a new script associated with that call type.

## Categorization by
                        	 Call Type Qualifiers

As described in the topic Call Types, Contact Data, and Scripting, a contact's call type is determined by three call type
                              qualifiers:

Dialed number

Calling line ID (CLID)

Caller-entered digits (CED)

When the system determines a contact's call type based on these qualifiers, it runs the associated script.

However, after the script is run, you can further categorize the contact based on the values of the call type qualifiers.

For example, a call type may be defined as having a calling line ID that includes calls from all area codes in New England
                              states. When the script associated with that call type is run, it examines the specific area code in the calling line ID and
                              branch differently depending on the value and therefore, treating calls from different area codes in New England differently.

You can categorize a contact based on its call type qualifiers by using one or more of the following nodes:

Dialed Number (DN) Node

Calling Line ID (CLID) Node

Caller Entered Digits (CED) Node

### Categorize Contact by Dialed Number

Following is the DN Properties dialog box of the Dialed Number
                                 node:

Step 1

Select one or more dialed numbers or Script Selectors from the
                                          Dialed numbers list and click Add> to move
                                          them to the Target dialed numbers list. If the current contact
                                          matches one of the selections in the Target dialed numbers list,
                                          processing continues on the node's success branch; otherwise,
                                          processing continues on the failure branch.

Step 2

Optionally, add comments and connection labels.

### Categorize Contact by Calling Line ID

- A specific (CLID) that you
                                    			 provide (for example, a specific region, area code, or an area code plus a
                                    			 local exchange).

- A variable expression.

By default, Unified ICM compares the list of values against the
                                 		  calling line ID of the contact. However, you can specify another value or
                                 		  expression to be used instead of the CLID.

Before defining CLID node properties, insert one or more
                                 		  targets and connections from the CLID node.

Step 1

In the Calling Line ID tab:

For each branch to a different target, select the Case (the
                                                				  number displayed on each success connection branch); for example, 1, 2, and 3.

For each Case, select the Type of match. Click Region , Prefix , or Exact Match .

For each Case, enter the Calling line ID to match. If you
                                                				  selected Region, choose a region from the drop-down list; for example,
                                                				  California. If you selected Prefix, enter the Prefix number. If you selected
                                                				  Exact Match, enter the Calling line ID to match.

To sort the list by case, click Sort .

To delete a row, select the row and click Delete .

Step 2

In the Variable tab:

By default, Use Calling Line ID is selected to have Unified ICM
                                                				  compare the list of values you define in the Calling Line ID tab against the
                                                				  calling line ID of the contact.

To have Unified ICM use the value of an expression instead of
                                                				  the Calling Line ID, select Use Expression and enter the expression directly or click Formula Editor to use a formula to define the expression.

Step 3

Optionally, add comments and connection labels.

#### What to do next

### Categorize Contact by Caller-Entered Digits (CED)

- SkillGroupA if the
                                    			 Caller-Entered Digits match a specific string

- SkillGroupB if there are
                                    			 no Caller-Entered Digits

Following is the CED Properties dialog box of the CED node:

You must insert targets and connections from the Caller-Entered-Digits
                                 		  node before you can define the node's properties.

Step 1

Click Add Digits to add a new CED value for a branch. In the new
                                          			 row, add a CED value and select the branch number. You can associate one or
                                          			 more CED values with each connection. Valid characters are: digits 0 through 9,
                                          			 asterisk (*), and number sign (#).

Step 2

Click Add None to add the value of None to a connection, specifying
                                          			 that it matches only those cases where no digits are entered or where no digits
                                          			 are required. When you specify None , you can select the following options:

None, to include both None Entered and None Required
                                                				  situations.

None Entered, to apply when the caller was prompted for digits
                                                				  but did not enter any.

None Required, to apply when the caller was not prompted for
                                                				  digits.

#### What to do next

## Categorization by Time and Date

You schedule a script by associating it with a call type. When a contact
                              of a certain call type is received, the associated script runs for that
                              contact.

However, after the script is run, you can further categorize the contact based on the time and day of week. This categorization
                              refines the schedule.

For example, a call type named "CHAT_CT" may be defined to include all chat web requests. A script named "CHAT_SCRIPT" runs
                              every time a contact with the call type "CHAT_CT" is received. Typically, this script instructs Enterprise Chat and
                                    						Email to assign the request to the longest available agent in the "Chat" skill group. However, the contact center is staffed differently
                              over the weekend and the supervisor wants to report to improved weekend activity. Therefore, for chat web requests received
                              on Saturday or Sunday, the script branches differently and instructs Enterprise Chat and
                                    						Email to assign the request to the longest available agent in the "WKEND_SUPPORT" skill group.

As another example, for a contact center where no phone support is available during night hours or weekends, you may choose
                              to design a script that routes a phone call to an announcement instead to an agent, during the off hours.

### Categorize Contact by Date and Time

Following is the Properties dialog box of the Time node:

You must insert targets and connections from the Time node before you can define the node's properties.

Step 1

For each branch listed in the Connections list, define a Time
                                          Range. You can define multiple time ranges for a single branch.
                                          Click Add Time to add a new time range to the
                                          branch, or select a time range listed and click Modify
                                             Time to modify it. A dialog box opens in which you
                                          can define the time range (the Add Time dialog box is shown
                                          below; the Modify Time dialog box looks and functions
                                          similarly):

Step 2

To delete a time associated with the branch, select the time
                                          and click Delete Time .

Step 3

You can define a branch as Otherwise by selecting the branch
                                          and clicking Make Otherwise . Execution follows
                                          this branch if none of the specified time ranges apply. You can
                                          specify only one Otherwise branch for the node. If you do not
                                          want to define the branch as Otherwise , select
                                          the branch and click Delete Otherwise .

Step 4

Optionally, add comments and connection labels.

#### What to do next

If you delete a connection, the time-range information you specified in the Properties dialog box is also deleted.

### Categorize Contact by the Day of Week

Following is the Properties dialog box of the Day of Week node:

You can define multiple output connections from the Day of Week node
                                 and associate each with one or more days of the week.

You must insert targets and connections from the Day of Week node
                                 before you can define the node's properties.

Step 1

For each branch listed in the Connection list, check the days
                                          of the week in which processing should continue on that branch.
                                          To check the day for that connection, left-click in a spot in
                                          the grid corresponding to that connection and day. A check mark
                                          appears in the grid. You can associate each day of week with one connection.
                                          However, you can associate each connection with one or more days
                                          of the week.

Step 2

Optionally, add comments and connection labels.

#### What to do next

## Categorization by Branching

Within a script, you can create multiple branches to direct script
                              processing based on certain conditions. Branching allows you to use a single
                              script that processes contacts differently, depending on data associated
                              with the contact, or on conditions at the contact center.

### Run a Different Script

For example, you might have several scripts that check for exception conditions and, if none are found, run a standard subroutine.
                                 Instead of including that subroutine as a branch from the failure output terminal of each of the exception conditions, you
                                 could use a Go To Script node pointing to a separate script containing the subroutine.

Following is the Properties dialog box of the Go To Script node:

Step 1

Select the Business entity that owns the script that the node should run. By default, Unified ICM consists of one business
                                          entity. Multiple business entities are allowed only if you enable partitioning. For more information about partitioning, see
                                          the Security Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

Step 2

Select a script from the Scripts list.  From within an administrative script, you can only go to another administrative script.
                                          Within a routing script, you can
                                          only go to another routing script.

Step 3

Optionally, add comments and connection labels.

### Direct Script Execution to a Specific Branch

Following is the Properties dialog box of the Switch node:

You must insert targets and connections from the Switch node before
                                 you can define the node's properties.

Step 1

By default, Connections are labeled "A", "B", etc. To re-label
                                          a Connection, click Modify Name and make
                                          changes to the name.

Step 2

To make a connection active, select a connection and click Make Active .

Step 3

Optionally, add comments and connection labels.

### Direct Script Execution to Different Branches by Percentage

You can direct specific percentages of contacts to different branches in a script by using the Percent Allocation node (in
                                 the General tab of the Palette).

Each branch may lead directly to a target, or may include additional processing. Because contacts are distributed by percentage
                                 and without tests of the targets' data, distributing by percentage never fails.

For example, in a geographically diverse environment, you can create a script that sends 10% of contacts to Boston, 5% to
                                 Chicago, and distributes the remaining 85% to another set of targets.

Warning

Unlike selecting targets by rules or distributing contacts to targets, distributing contacts does not consider real-time contact
                                             center conditions and therefore may lead to load imbalances.

Following is the Properties dialog box of the Percent Allocation node:

Define Percent Allocation node properties as follows:

Step 1

In the Percent column for each connection, enter a percent
                                          number for the percentage of contacts to process on that branch.

Step 2

Optionally, modify the Connection name. Changes appear in the
                                          connector labels when you save the properties and view the
                                          script.

Step 3

Optionally, add comments and connection labels.

### Categorize Contact Based on a Condition

When the system runs an If node, it first evaluates the condition specified in the node Properties dialog box Define condition
                                 field. If the system determines that the condition is true, control flows through the success output terminal; if it determines
                                 the condition is false, control flows through the failure output terminal.

Following is the Properties dialog box of the If node:

Step 1

In the Define condition field, enter a condition or use the
                                          Formula Editor to create a formula.

Step 2

Optionally, add comments and connection labels.

### Categorize a Contact Based on Its Media Routing Domain

## Categorization by External Data

Scripts can categorize a contact based on data stored in a database that
                              is not part of Unified ICM, such as a Customer Relationship Management (CRM)
                              system.

For example, a script that processes incoming phone calls can query a CRM
                              using the CLID to determine if the customer should receive Premium or
                              Standard phone support. The records for the customer with the phone number
                              matching the CLID are retrieved, and the value of the Support column is
                              returned to the script. If the value indicates that the customer has paid
                              for Premium support, script processing continues down one branch that
                              assigns the phone call to a skill group dedicated to responding to Premium
                              customers; otherwise, script processing continues down another branch that
                              assigns the phone call to a more general skill group, where the wait time is
                              expected to be longer.

You can categorize a contact by retrieving external data with the DB
                              Lookup node, then referencing the retrieved external data on the DB Lookup
                              node success branch.

### Modify CallRouter Registry to Provide for Database Lookup Authentication

By default, when attempting to access a remote database, the CallRouter
                                 authenticates itself as:

To access the remote database, the call router
                                 authenticates using external database lookup value in SQLLogin registry key located
                                 at HKEY_LOCAL_MACHINE\SOFTWARE\Cisco.System,INC.\ICM\<instancename>\
                                 RouterA\Router\CurrentVersion\Configuration\Database.

Update the External
                                 DBLookUp registry value using the CCEDataProtect Tool. For more information, see Configure External DBLookUp Registry Value using CCEDataProtect Tool procedure in the Administration Guide for Cisco Unified Contact Center
                                    Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html .

You must specify the following registry value in the
                                 CCEDataProtect Tool on the CallRouter for SQLLogin registry
                                 key.

Use
                                 a comma as the delimiter to separate data for separate databases.

The
                                 following example shows login credentials for two external databases:

Important

The SQLLogin key does not support passwords that contains the following
                                             characters:

'/', '\', '=', '(', ')', or ','

You must configure the database paths to Side A and Side B in the DB Lookup
                                 Explorer and the CallRouter Registry for the Database Lookup Authentication.

The database paths in the DB Lookup tool and the CallRouter Registry must be the
                                             same. Use either hostname or IP addresses in the DB Lookup Explorer and the
                                             CallRouter Registry. If you use hostname in the DB Lookup Explorer tool, use
                                             hostname in CallRouter Registry as well. If you use IP Address in the DB Lookup
                                             Explorer tool, use IP Address in CallRouter Registry as well.

If the external remote database is on SQL Server 2017 version, you have to
                                             install the ODBC Driver 17 manually on the server hosting the external database.
                                             Download the ODBC Driver 17 from Microsoft.

### Categorize Contact
                           	 by External Data

Following is the
                                 		  Properties dialog box of the DB Lookup node:

Step 1

Select the
                                          			 database table you want to query. (The drop-down list contains the enterprise
                                          			 names of all lookup tables defined in Unified ICM.)

Step 2

In the Lookup
                                          			 value field, define constant or expression to match the primary key value in
                                          			 the row you want to retrieve. The lookup value must be of the appropriate data
                                          			 type to match the primary key field in the table. You can use formulas to
                                          			 define the expression. For example, if phone_number is the primary key field in
                                          			 the database table, you might use Call.CallingLineID as the Lookup Value.

Step 3

Optionally, add
                                          			 comments and connection labels.

### Reference Retrieved External Data

Database.table-name.column-name

table-name is the enterprise name
                                    of the table as defined through the Configuration Manager.

column-name is the name of the
                                    column from the table, which is also defined through the Unified ICM Configuration Manager.

#### What to do next

For example, if the table Customers contains a column named Priority,
                                 you would reference that column in an If expression as follows:

Database.Customers.Priority = 1

For more information, see  the chapter Use of Formulas.

## Categorize by External Applications

For example, a script that processes incoming phone calls can send the
                              caller's account number to an external application, which returns to the
                              script the caller's account balance. The script can then branch on the value
                              of the account balance, providing premium service to callers with higher
                              account balances.

Step 1

In the Send tab:

Choose the gateway from the Application Gateway drop-down
                                             list.

In the Subtype field, enter the string that is to be sent
                                             to the external application, or use the Formula Editor to
                                             write an expression that evaluates to a string.

In the Call variables list, check the call variables to
                                             send to the external application.

To send expanded call variables to the external
                                             application, check Expanded call context
                                                variables .

Step 2

In the Receive tab:

Select No Reply if the external
                                             application is not to return data to the script.

In the Call variables list, check variables that the
                                             external application may modify.

Select Expanded call context variables if the external
                                             application modifies and returns values for the expanded
                                             call variables.

Step 3

Optionally, add comments and connection labels.

| Step 1 | In the Call Type tab, click the Statically radio button. |
|---|---|
| Step 2 | From the Call Type list, click the call type to assign to the contact. |

| Warning | The Call Type node changes the call type and continues running the current script. The Requalify Call node stops running the
                                             current script and runs a new script associated with that call type. |
|---|---|

| Note | Dynamic call type selection is not available when an External Authorization server is used with Internet Script Editor and
                                             will be grayed out in the interface. |
|---|---|

| Step 1 | On the call type
                                          			 tab, select the Dynamically radio button. |
|---|---|
| Step 2 | To dynamically
                                          			 change the call type of a contact by call type name, In the Find By section,
                                          			 select the Call
                                             				Type Name radio button. |
| Step 3 | To dynamically
                                          			 change the call type of a contact by call type ID, In the Find By section,
                                          			 select the Call
                                             				Type ID radio button. |
| Step 4 | To determine
                                          			 which call type name or ID to use to change the call type of a contact, click
                                          			 the Formula Editor button to create a formula. |

| Warning | The Call Type node changes the call type and continues the current script execution. The Requalify Call node terminates the
                                             current script execution and runs a new script associated with that call type. |
|---|---|

| Step 1 | In the Requalify Call Tab, select the Call type to assign to
                                          the contact. |
|---|---|
| Step 2 | Optionally, add comments. |

| Warning | The Call Type node changes the call type and continues running the current script. The Requalify Call node stops running the
                                             current script and runs a new script associated with that call type. |
|---|---|

| Step 1 | Select one or more dialed numbers or Script Selectors from the
                                          Dialed numbers list and click Add> to move
                                          them to the Target dialed numbers list. If the current contact
                                          matches one of the selections in the Target dialed numbers list,
                                          processing continues on the node's success branch; otherwise,
                                          processing continues on the failure branch. |
|---|---|
| Step 2 | Optionally, add comments and connection labels. |

| Note | For Web Collaboration requests, the CLID maps to the
                                          		  applicationstring1 variable. |
|---|---|

| Step 1 | In the Calling Line ID tab: Figure 10. CLID Properties - Calling Line ID For each branch to a different target, select the Case (the
                                                				  number displayed on each success connection branch); for example, 1, 2, and 3. For each Case, select the Type of match. Click Region , Prefix , or Exact Match . For each Case, enter the Calling line ID to match. If you
                                                				  selected Region, choose a region from the drop-down list; for example,
                                                				  California. If you selected Prefix, enter the Prefix number. If you selected
                                                				  Exact Match, enter the Calling line ID to match. To sort the list by case, click Sort . To delete a row, select the row and click Delete . |
|---|---|
| Step 2 | In the Variable tab: Figure 11. CLID Properties - Variable Tab By default, Use Calling Line ID is selected to have Unified ICM
                                                				  compare the list of values you define in the Calling Line ID tab against the
                                                				  calling line ID of the contact. To have Unified ICM use the value of an expression instead of
                                                				  the Calling Line ID, select Use Expression and enter the expression directly or click Formula Editor to use a formula to define the expression. |
| Step 3 | Optionally, add comments and connection labels. |

| Note | If you delete a connection associated with a Case, the Case
                                          		  information you specified in the Properties dialog box is also deleted. |
|---|---|

| Note | For Enterprise Chat and
                                                						Email requests,
                                          		  the CED maps to the applicationstring2 variable. |
|---|---|

| Step 1 | Click Add Digits to add a new CED value for a branch. In the new
                                          			 row, add a CED value and select the branch number. You can associate one or
                                          			 more CED values with each connection. Valid characters are: digits 0 through 9,
                                          			 asterisk (*), and number sign (#). |
|---|---|
| Step 2 | Click Add None to add the value of None to a connection, specifying
                                          			 that it matches only those cases where no digits are entered or where no digits
                                          			 are required. When you specify None , you can select the following options: None, to include both None Entered and None Required
                                                				  situations. None Entered, to apply when the caller was prompted for digits
                                                				  but did not enter any. None Required, to apply when the caller was not prompted for
                                                				  digits. |

| Note | If you delete a connection associated with a Case, the Case
                                          		  information you specified in the Properties dialog box is also deleted. |
|---|---|

| Note | The time and day of the week are determined by the settings on the Central Controller VM. |
|---|---|

| Step 1 | For each branch listed in the Connections list, define a Time
                                          Range. You can define multiple time ranges for a single branch.
                                          Click Add Time to add a new time range to the
                                          branch, or select a time range listed and click Modify
                                             Time to modify it. A dialog box opens in which you
                                          can define the time range (the Add Time dialog box is shown
                                          below; the Modify Time dialog box looks and functions
                                          similarly): Figure 16. Add Time Dialog |
|---|---|
| Step 2 | To delete a time associated with the branch, select the time
                                          and click Delete Time . |
| Step 3 | You can define a branch as Otherwise by selecting the branch
                                          and clicking Make Otherwise . Execution follows
                                          this branch if none of the specified time ranges apply. You can
                                          specify only one Otherwise branch for the node. If you do not
                                          want to define the branch as Otherwise , select
                                          the branch and click Delete Otherwise . |
| Step 4 | Optionally, add comments and connection labels. |

| Note | If you delete a connection, the time-range information you specified in the Properties dialog box is also deleted. |
|---|---|

| Step 1 | For each branch listed in the Connection list, check the days
                                          of the week in which processing should continue on that branch.
                                          To check the day for that connection, left-click in a spot in
                                          the grid corresponding to that connection and day. A check mark
                                          appears in the grid. You can associate each day of week with one connection.
                                          However, you can associate each connection with one or more days
                                          of the week. |
|---|---|
| Step 2 | Optionally, add comments and connection labels. |

| Note | If you delete a connection, the day of the week information you specified in the Properties dialog box is also deleted. |
|---|---|

| Step 1 | Select the Business entity that owns the script that the node should run. By default, Unified ICM consists of one business
                                          entity. Multiple business entities are allowed only if you enable partitioning. For more information about partitioning, see
                                          the Security Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html . |
|---|---|
| Step 2 | Select a script from the Scripts list.  From within an administrative script, you can only go to another administrative script.
                                          Within a routing script, you can
                                          only go to another routing script. |
| Step 3 | Optionally, add comments and connection labels. |

| Step 1 | By default, Connections are labeled "A", "B", etc. To re-label
                                          a Connection, click Modify Name and make
                                          changes to the name. |
|---|---|
| Step 2 | To make a connection active, select a connection and click Make Active . Note Only one connection can be active at any time. To change the
                                                      active branch, you must re-edit the script and create a new
                                                      script version. | Note | Only one connection can be active at any time. To change the
                                                      active branch, you must re-edit the script and create a new
                                                      script version. |
| Note | Only one connection can be active at any time. To change the
                                                      active branch, you must re-edit the script and create a new
                                                      script version. |
| Step 3 | Optionally, add comments and connection labels. |

| Note | Only one connection can be active at any time. To change the
                                                      active branch, you must re-edit the script and create a new
                                                      script version. |
|---|---|

| Warning | Unlike selecting targets by rules or distributing contacts to targets, distributing contacts does not consider real-time contact
                                             center conditions and therefore may lead to load imbalances. |
|---|---|

| Step 1 | In the Percent column for each connection, enter a percent
                                          number for the percentage of contacts to process on that branch. Note The percent total for all rows must equal 100. | Note | The percent total for all rows must equal 100. |
|---|---|---|---|
| Note | The percent total for all rows must equal 100. |
| Step 2 | Optionally, modify the Connection name. Changes appear in the
                                          connector labels when you save the properties and view the
                                          script. |
| Step 3 | Optionally, add comments and connection labels. |

| Note | The percent total for all rows must equal 100. |
|---|---|

| Step 1 | In the Define condition field, enter a condition or use the
                                          Formula Editor to create a formula. |
|---|---|
| Step 2 | Optionally, add comments and connection labels. |

| Note | You must use Unified ICM Configuration Manager to define the external database table and the columns that are to be referenced
                                       in scripts. For more information, see the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html . |
|---|---|

| Important | The SQLLogin key does not support passwords that contains the following
                                             characters: '/', '\', '=', '(', ')', or ',' |
|---|---|

| Note | The database paths in the DB Lookup tool and the CallRouter Registry must be the
                                             same. Use either hostname or IP addresses in the DB Lookup Explorer and the
                                             CallRouter Registry. If you use hostname in the DB Lookup Explorer tool, use
                                             hostname in CallRouter Registry as well. If you use IP Address in the DB Lookup
                                             Explorer tool, use IP Address in CallRouter Registry as well. |
|---|---|

| Note | If the external remote database is on SQL Server 2017 version, you have to
                                             install the ODBC Driver 17 manually on the server hosting the external database.
                                             Download the ODBC Driver 17 from Microsoft. |
|---|---|

| Step 1 | Select the
                                          			 database table you want to query. (The drop-down list contains the enterprise
                                          			 names of all lookup tables defined in Unified ICM.) Note Define all
                                                      				integer fields in tables accessed by a DBLookup node as NOT NULL. Only the
                                                      				following data types are supported for SQL databases: SQLINT1 (tinyint),
                                                      				SQLINT2 (smallint), SQLINT4 (int), SQLCHAR (char), SQLVARCHAR (varchar),
                                                      				SQLFLT4DBFLT4 (real), SQLFLT8DBFLT8 (float), and SQLDATETIME (datetime). You
                                                      				must define all fields except SQLDATETIME, SQLVARCHAR, and SQLCHAR as NOT NULL
                                                      				fields. You can define these three fields as NULL. | Note | Define all
                                                      				integer fields in tables accessed by a DBLookup node as NOT NULL. Only the
                                                      				following data types are supported for SQL databases: SQLINT1 (tinyint),
                                                      				SQLINT2 (smallint), SQLINT4 (int), SQLCHAR (char), SQLVARCHAR (varchar),
                                                      				SQLFLT4DBFLT4 (real), SQLFLT8DBFLT8 (float), and SQLDATETIME (datetime). You
                                                      				must define all fields except SQLDATETIME, SQLVARCHAR, and SQLCHAR as NOT NULL
                                                      				fields. You can define these three fields as NULL. |
|---|---|---|---|
| Note | Define all
                                                      				integer fields in tables accessed by a DBLookup node as NOT NULL. Only the
                                                      				following data types are supported for SQL databases: SQLINT1 (tinyint),
                                                      				SQLINT2 (smallint), SQLINT4 (int), SQLCHAR (char), SQLVARCHAR (varchar),
                                                      				SQLFLT4DBFLT4 (real), SQLFLT8DBFLT8 (float), and SQLDATETIME (datetime). You
                                                      				must define all fields except SQLDATETIME, SQLVARCHAR, and SQLCHAR as NOT NULL
                                                      				fields. You can define these three fields as NULL. |
| Step 2 | In the Lookup
                                          			 value field, define constant or expression to match the primary key value in
                                          			 the row you want to retrieve. The lookup value must be of the appropriate data
                                          			 type to match the primary key field in the table. You can use formulas to
                                          			 define the expression. For example, if phone_number is the primary key field in
                                          			 the database table, you might use Call.CallingLineID as the Lookup Value. |
| Step 3 | Optionally, add
                                          			 comments and connection labels. |

| Note | Define all
                                                      				integer fields in tables accessed by a DBLookup node as NOT NULL. Only the
                                                      				following data types are supported for SQL databases: SQLINT1 (tinyint),
                                                      				SQLINT2 (smallint), SQLINT4 (int), SQLCHAR (char), SQLVARCHAR (varchar),
                                                      				SQLFLT4DBFLT4 (real), SQLFLT8DBFLT8 (float), and SQLDATETIME (datetime). You
                                                      				must define all fields except SQLDATETIME, SQLVARCHAR, and SQLCHAR as NOT NULL
                                                      				fields. You can define these three fields as NULL. |
|---|---|

| Note | You must use Unified ICM Configuration Manager to define the external
                                       application. For more information, see the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise . |
|---|---|

| Step 1 | In the Send tab: Figure 30. App Gateway Properties - Send Choose the gateway from the Application Gateway drop-down
                                             list. In the Subtype field, enter the string that is to be sent
                                             to the external application, or use the Formula Editor to
                                             write an expression that evaluates to a string. In the Call variables list, check the call variables to
                                             send to the external application. To send expanded call variables to the external
                                             application, check Expanded call context
                                                variables . |
|---|---|
| Step 2 | In the Receive tab: Figure 31. App Gateway Properties - Receive Select No Reply if the external
                                             application is not to return data to the script. Note If you select this option, Unified ICM cannot retrieve any data from the external application. In the Call variables list, check variables that the
                                             external application may modify. Select Expanded call context variables if the external
                                             application modifies and returns values for the expanded
                                             call variables. | Note | If you select this option, Unified ICM cannot retrieve any data from the external application. |
| Note | If you select this option, Unified ICM cannot retrieve any data from the external application. |
| Step 3 | Optionally, add comments and connection labels. |

| Note | If you select this option, Unified ICM cannot retrieve any data from the external application. |
|---|---|