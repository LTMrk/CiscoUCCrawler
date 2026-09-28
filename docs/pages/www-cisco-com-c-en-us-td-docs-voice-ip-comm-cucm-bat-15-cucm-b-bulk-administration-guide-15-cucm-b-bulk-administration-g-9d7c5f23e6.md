---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-15-cucm-b-bulk-administration-guide-15-cucm-b-bulk-administration-g-9d7c5f23e6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/15/cucm_b_bulk-administration-guide-15/cucm_b_bulk-administration-guide-1251su2_chapter_011101.html
retrieved_at: 2026-08-21T09:18:07.760034+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: October 1, 2024

Chapter: Cisco Unified Communications Manager Assistant

## Chapter: Cisco Unified Communications Manager Assistant

# Cisco Unified Communications Manager Assistant

This chapter provides information about setting up manager and assistant phones with either shared lines or proxy lines for
                        the Unified Communications Manager Assistant. Information is also provided for adding and updating manager-assistant associations using a BAT spreadsheet, and
                        for creating default and custom CSV data files for manager-assistants.

You can use the Cisco Unified Communications Manager Bulk Administration (BAT) to manage the Cisco Unified Communications Manager Assistant feature in Unified Communications Manager . You can add, update, and delete managers or assistants with their associations in bulk transactions.

For detailed tasks and information about Cisco Unified Communications Manager Assistant, see the Feature Configuration Guide for Cisco Unified Communications Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html .

## Phones and Lines for Cisco Unified Communications Manager Assistant

The CiscoUnifiedCM Assistant feature works with several
                           		CiscoUnifiedIPPhone models and device profiles. CiscoUnifiedCM Assistant
                           		provides two modes for configuring managers and assistants lines for use with
                           		CiscoUnifiedCM Assistant features.

Proxy mode—The primary manager line associates with a proxy line
                                 			 that has a different directory number on the assistant phone.

Shared line mode—The manager and assistant have a shared line on
                                 			 their phones that uses the same directory number and partition.

You can associate users to devices/phones only if they support
                                       		  UnifiedCM Assistant.

You can use BAT to set up the manager and assistant phones with
                           		either proxy lines or shared lines.

### Set Up Phones in
                           	 Proxy Line Mode for Cisco Unified Communications Manager Assistant

To prepare
                                 		  for configuring manager and assistant phones with UnifiedCM Assistant proxy
                                 		  line support, you must complete the following tasks:

Step 1

Set up and
                                          			 configure UnifiedCM Assistant requirements for your system. Cisco recommends
                                          			 that you use the CiscoUnifiedCM Assistant Configuration Wizard. The wizard
                                          			 automatically creates the phone templates for UnifiedCM Assistant manager and
                                          			 assistant, route points, partitions, translation patterns, and calling search
                                          			 space for the CiscoUnifiedCM Assistant service. To run the CiscoUnifiedCM
                                          			 Assistant Configuration Wizard, ensure BAT and the wizard are on the same
                                          			 server.

See the Feature Configuration Guide for Cisco Unified Communications
                                                				  Manager Guide for information about running the CiscoUnifiedCM
                                             				Assistant Configuration Wizard.

You can use
                                                         				  the CiscoUnifiedCM Assistant Configuration Wizard only one time to set up the
                                                         				  UnifiedCM Assistant configuration requirements for your system. After running
                                                         				  the configuration wizard, you can only view, but not change, your configuration
                                                         				  with the wizard.

Step 2

To add new
                                          			 phones and users for managers and assistants, use the UnifiedCM Assistant
                                          			 manager and UnifiedCM Assistant assistant phone templates that the
                                          			 CiscoUnifiedCM Assistant Configuration Wizard produced on the BAT server. Use
                                          			 the BAT templates to configure phones for proxy mode only.

Step 3

For existing
                                          			 manager and assistant phones, you can change the manager and assistant phones
                                          			 to correspond to the UnifiedCM Assistant phone templates by using either of
                                          			 these methods:

You can use
                                                   					 the Add Lines feature in BAT to modify existing phones to resemble the
                                                   					 UnifiedCM Assistant phone templates.

You can
                                                   					 delete the original phones and add new phones by using the UnifiedCM Assistant
                                                   					 phone templates for managers and assistants.

Step 4

After you
                                          			 configure the phones and lines for managers and assistants, you associate the
                                          			 manager and assistant lines for UnifiedCM Assistant control.

#### Cisco Unified Communications Manager Assistant Manager Phone Template Default Settings

The following table lists the default settings for the
                                    		  UnifiedCM Assistant manager phone template.

Field

Default Value

Softkey Template

Softkey Template Standard Manager

Phone Button Template

Standard CiscoUnifiedIPPhone 7960 (2 lines)

Line1

Primary line

- CSS =
                                                   						Generated_CSS_I_E

- Partition =
                                                   						Generated_Managers

Line 2

Incoming Intercom line

- CSS =
                                                   						Generated_CSS_I_E

- Partition =
                                                   						Generated_Everyone

- Also configure
                                                   						auto answer with headset option.

Services

Assistant Primary Service

The following table lists the default settings for the
                                    		  UnifiedCM Assistant assistant phone template.

Field

Default Value

Softkey Template

Softkey Assistant

Phone Button Template

Standard CiscoUnifiedIPPhone 7960 Assistant

Expansion Module 1

14-button expansion module

One line on base phone and five lines on expansion module

For proxy lines, one line on base phone and five lines on
                                                					 expansion module have the following default configuration:

- CSS =
                                                   						Generated_CSS_M_E

- Partition =
                                                   						Generated_Everyone

Line 7

(On Expansion Module)

Intercom line

- CSS =
                                                   						Generated_CSS_I_E

- Partition =
                                                   						Generated_Everyone

- Also configure
                                                   						auto answer with headset option.

#### Manager and Assistant Proxy Line Configurations

BAT assigns UnifiedCM Assistant line configurations by
                                    		  mapping the primary manager lines on the phone to proxy lines on the assistant
                                    		  phone. When you use the UnifiedCM Assistant manager and assistant default
                                    		  templates that the UnifiedCM Assistant wizard created, you can associate from
                                    		  one to five manager lines on one assistant phone. For phones that are
                                    		  configured with the UnifiedCM Assistant templates, this example shows the line
                                    		  configurations when you associate two manager phones to an assistant phone.

##### Manager 1 Phone

Line 1— Primary line

Line 2— Intercom line

##### Manager 2 Phone

Line 1— Primary line

Line 2— Intercom line

##### Assistant Phone

Line 1—Primary line

Line 2—Proxy line for Manager 1

Line 3—Proxy line for Manager 2

Lines 4 through 6 are unassigned

Line 7—Intercom line

##### Assistant Phone

Lines 4 through 6 remain available for other manager
                                    		  associations.

When you associate multiple managers to an assistant phone,
                                    		  BAT creates proxy lines based on the order in the CSV data file. BAT creates
                                    		  the first manager-assistant line by assigning all the primary manager lines as
                                    		  proxy lines to the unassigned lines on the assistant phone. BAT continues
                                    		  creating individual manager-assistant proxy lines based on the order of the CSV
                                    		  record until all lines on the assistant phone are assigned or all managers in
                                    		  the CSV record are associated.

When you associate multiple assistants to a manager primary
                                    		  line, BAT assigns assistants to the manager based on the order in the CSV data
                                    		  file. BAT assigns the primary manager lines based on the first assistant number
                                    		  of available lines. For example, a manager phone has two primary lines. The
                                    		  first assistant, who is listed in the CSV data file, has only one available
                                    		  line. Consequently, BAT associates only one primary line for the manager and
                                    		  one proxy line on all the assistant phones that are listed in the CSV record.

##### Cisco Unified Communications Manager Assistant Manager Phone Line Configurations

The following table lists all possible line configurations
                                       		  for a manager phone that BAT can set up when you are using manager-assistant
                                       		  associations.

Number of Available Lines

Configuration

One line

Line 1—Primary line (UnifiedCM Assistant controlled)

Intercom line (none)

Two lines

(Default UnifiedCM Assistant manager phone template)

Line 1—Primary line (UnifiedCM Assistant controlled)

Line 2—Intercom line (optional)

More than two lines

Last line gets configured as the intercom line.

The number of available lines on the assistant phone
                                                   					 determines the number of manager lines that get associated with proxy lines.

##### Unified CM Assistant Phone Line Configurations

The following table lists the default line configurations
                                       		  for the assistant phones that BAT sets up during manager-assistant
                                       		  associations.

Number of Available Lines

Configuration

One line

Line 1—Proxy line

Intercom line (none)

Two lines

Line 1—Primary line

Line 2—Proxy line

Intercom line (none)

Three lines

Line 1—Primary line

Line 2—Proxy line

Line 3—Intercom line

More than three lines

Line 1—Primary line

Line 2—Proxy line

Last line gets configured as the intercom line

All other lines get configured as proxy lines

Seven lines

(Default UnifiedCM Assistant assistant phone template)

Line 1—Primary line

Line 2 through line 6 can get configured as proxy lines to
                                                   					 support up to five managers.

Line 7—Intercom line

##### Proxy Line Example for Cisco Unified Communications Manager Assistant Manager and Assistant Phones

You associate two managers, each with three existing lines,
                                       		  to an assistant phone with six unassigned lines. BAT sets the following line
                                       		  configurations on the manager and assistant phones.

###### Manager 1 Phone

Line 1—Manager primary line (DN is 2355)

Line 2—Manager primary line (DN is 2366)

Line 3—Manager intercom line

###### Manager 2 Phone

Line 1—Manager primary line (DN is 2656)

Line 2—Manager primary line (DN is 2666)

Line 3—Manager intercom line

###### Assistant Phone

Line 1—Assistant primary line (DN is 3333)

Line 2—Proxy line 1 for Manager 1 (DN is 3455)

Line 3—Proxy line 1 for Manager 2 (DN is 3656))

Line 4—Proxy line 2 for Manager 1 (DN is 3366)

Line 5—Proxy line 2 for Manager 2 (DN is 3666)

Line 6—Available

Line 7—Assistant intercom line

###### Assistant Phone

When you associate a manager phone that has preexisting
                                       		  primary lines, you must ensure that the number of unassigned lines on the
                                       		  assistant phone equals or is greater than the number of primary lines on the
                                       		  manager phone. For instance, BAT does not allow you to create an association
                                       		  between a manager that has a phone with four configured primary lines and an
                                       		  assistant with only three available lines.

#### Set Up Proxy Lines on New Manager and Assistant Phones for Cisco Unified Communications Manager Assistant

You can set up new UnifiedCM Assistant manager and
                                    		  assistant phones to use proxy lines.

##### Before you begin

- Run the UnifiedCM
                                       			 Assistant Configuration Wizard to create the UnifiedCM Assistant templates,
                                       			 partition, and calling search space.

- If you want to associate
                                       			 more than five managers to an assistant, you must access the UnifiedCM
                                       			 Assistant Template and make a copy with a new name. Add more lines to the
                                       			 template to accommodate the additional managers.

Step 1

Choose BAT
                                                   				  Administration > Phones > Phones
                                                   				  Template .

The Phone Template Configuration window displays.

Because BAT UnifiedCM Assistant templates are write protected,
                                                            				  if you want to make changes to these templates, you must make a copy of the
                                                            				  template and then edit the template with your changes. See Table 1 for default manager phone template field descriptions. See Table 2 for default assistant phone template field descriptions.

Step 2

Create the CSV data file for manager phones and another file for
                                             			 assistant phones using these options:

Use the BAT spreadsheet and choose the Phones tab.

Use a text editor and refer to the manager or assistant
                                                   				  template fields as a guide.

##### What to do next

Follow the procedures in Add Phones to Database to insert new phones.

#### Set Up Proxy Lines on Existing Manager and Assistant Phones for Cisco Unified Communications Manager Assistant

You can set up existing UnifiedCM Assistant manager and assistant phones to use proxy lines.

Step 1

Choose BAT Administration > Phones > Add Lines .

Step 2

You may need to copy and modify the UnifiedCM Assistant templates for BAT.

See Table 1 for default manager phone template field descriptions, and see Table 2 for default assistant phone template field descriptions.

If you changed any configuration information (for example, partition names) when you ran the CiscoUnifiedCM Assistant Configuration
                                                            Wizard, you must use the same configuration information for the fields when you edit the template.

Step 3

Create the CSV data file for manager phones and another file for assistant phones using one of these options:

Use the BAT spreadsheet and choose the Add Lines tab.

Use a text editor and use the manager or assistant template fields as a guide.

##### What to do next

You can set up manager and assistant lines on existing phones.

### Set Up Phones in Shared Line Mode for Cisco Unified Communications Manager Assistant

You can set up manager and assistant phones to use shared
                                 		  lines when you create a BAT template to add new phones in the CiscoUnified Communications Manager database. Use
                                 		  the procedures for setting up new phones using BAT.

#### Before you begin

You must set up the UnifiedCM Assistant service parameters for shared
                                 		  line support in CiscoUnified Communications Manager .

If you have a CiscoUnifiedIPPhone model 7960, you need a phone
                                             			 button template with five or more lines.

Create a BAT template to add new or update existing manager and
                                          			 assistant phones using the following guidelines:

For manager phones, see Manager Phone Settings for Shared Line Mode .

For assistant phones, see Assistant Phone Settings for Shared Line Mode .

#### What to do next

You must associate the manager and assistant lines for UnifiedCM Assistant
                                 		  control. Follow the procedures in the CSV Data File for Manager-Assistant Associations .

#### Manager Phone Settings for Shared Line Mode

When you create the BAT template to add new or update
                                    		  existing manager phones with shared lines, use the following phone settings:

Assign the Softkey template: Standard Shared Mode Manager.

Add primary lines to share with assistants, if needed.

Set up the voice-messaging profile on the primary line.

Add an incoming intercom line (optional).

Add speed-dial buttons for outgoing intercom targets (optional).

Set the user locale.

#### Assistant Phone Settings for Shared Line Mode

When you create the BAT template to add new or update
                                    		  existing assistant phones with shared lines, use the following phone settings:

Assign the Softkey template: Standard Assistant

If you are using a Cisco 14-button expansion module (7914) for
                                          				additional lines, specify the expansion module type in the BAT template.

CiscoUnifiedIPPhone 7960 phone button templates include
                                                      				  expansion module lines.

Add a personal primary line.

Add shared lines for each associated manager. Use the same
                                          				directory number and partition as the primary line on the manager phone.

Add an incoming intercom line (optional)

Add speed dials to the managers intercom lines (optional)

Set the user locale

#### Manager and Assistant Shared Line Configurations

BAT associates CiscoUnifiedCM Assistant line
                                    		  configurations to shared lines that are assigned to the manager and the
                                    		  assistant phones. You set the shared line mode in the manager’s configuration
                                    		  when associating managers with assistants.

In shared line mode, the manager line corresponds to a
                                    		  shared line on the assistant phone. For example, to associate two managers with
                                    		  an assistant, you add two lines to the assistant phone that have the same
                                    		  directory numbers and partitions as the primary lines on the manager phones.

##### Manager 1 Phone

Line 1— Primary line (DN is 2355)

Line 2— Intercom line (optional)

##### Manager 2 Phone

Line 1— Primary line (DN is 2875)

Line 2— Intercom line (optional)

##### Assistant Phone

Line 1—Assistant primary line (DN is 3356)

Line 2—Shared line with Manager 1 (DN is 2355)

Line 3—Shared line with Manager 2 (DN is 2875)

Lines 4 through 6 are available

Line 7—Intercom line (optional)

You can add lines 4 through 6 as shared lines for other
                                    		  managers.

When you add multiple manager lines to an assistant phone,
                                    		  all lines on the assistant phone must use shared line mode. You cannot mix
                                    		  proxy and shared lines on the assistant phone. Likewise, when a manager has
                                    		  multiple assistants, all associations must use shared line mode.

When you associate multiple assistants to a manager who has
                                    		  shared line mode, BAT assigns UnifiedCM Assistant associations only to those
                                    		  assistants that are also using shared line mode.

## CSV Data File for Manager-Assistant Associations

When you use BAT to insert manager-assistant associations to the Unified Communications Manager database, you can add new associations or update existing associations.

You have two options for creating a CSV data file to add or update manager-assistant associations:
                              		 using the BAT spreadsheet or using a text editor to create a text file in CSV format.

When you create an association for a new manager, you need
                              		  to enter a device name. When you update a manager with an existing UnifiedCM
                              		  Assistant record, consider these fields optional. BAT does not allow you to assign the intercom line of a
                              		  manager to a proxy line for an assistant if the number of manager lines is
                              		  greater than or equal to three.

### Add or Update Manager-Assistant Associations Using BAT Spreadsheet

Use the BAT spreadsheet to add new or update existing
                                 		  UnifiedCM Assistant associations. The BAT spreadsheet includes data file
                                 		  templates with macros to make it easy to add, update, or delete
                                 		  manager-assistant associations.

Add new UnifiedCM Assistant associations using the BAT
                                          			 spreadsheet.

To create manager-assistant associations with the default line
                                                				  configuration, see Create Default Manager-Assistant CSV Data Files .

To assign proxy lines that do not follow the default line
                                                				  configuration, see Create Custom Manager-Assistant CSV Data Files .

### Manager-assistant Association Additions and Updates Using BAT Spreadsheet

The BAT spreadsheet includes data file templates with macros to make it easy to add, update, or delete manager-assistant associations.

When you use the BAT spreadsheet to add  new Unified CM Assistant associations, you can set up the manager-assistant configurations
                                 in two ways:

Create manager-assistant associations with the default line configuration. For the default line configurations for the manager
                                       and assistant phones, see Table 1 and Table 1 .

Assign proxy lines that do not follow the default line configuration using a custom CSV data file.

### Create Default Manager-Assistant CSV Data Files

Use the BAT spreadsheet to create a CSV data file for
                                 		  inserting, updating, or deleting default manager-assistant associations for
                                 		  both proxy and shared mode.

After you have finished editing all the fields in the BAT spreadsheet,
                                 		  you can export the content to a CSV formatted data file. The file is saved to C:\XLSDataFiles or to your choice of another
                                 		  existing folder on your local workstation and is assigned a default filename:

<type of operation>ManagerAssistants-timestamp.txt

where <type of operation> can be either insert or
                                 		  delete, and " timestamp " represents the precise date and time
                                 		  that the file was created.

Step 1

Download and open the BAT.xlt file to open the BAT spreadsheet.

Step 2

When prompted, click Enable Macros to use the spreadsheet
                                          			 capabilities.

Step 3

To display the manager-assistant association options, click the Default Managers-Assistants tab at the bottom
                                          			 of the spreadsheet.

Step 4

Scroll to the right side of the template until you see the radio
                                          			 buttons and choose the type of associations for this transaction:

- One manager,
                                             				multiple assistants

- One assistant,
                                             				multiple managers

Step 5

Complete all mandatory fields and any relevant, optional fields.

If you choose the One manager, multiple assistants radio
                                                				  button, enter the following information in each row:

Manager ID—Enter the user ID, up to 30 characters, of the manager.

Assistant ID # —Enter the user IDs, up to 30 characters, for the assistants to whom the manager will be associated, where the # symbol represents the number of assistants assigned to a manager.

Tip

To add more assistants, click Add more Assistants .

If you choose the One assistant, multiple managers radio
                                                				  button, enter the following information in each row:

Assistant ID—Enter the user ID, up to 30 characters, of the assistant.

Manager ID # —Enter the user IDs, up to 30 characters, for the managers to whom the assistant will be associated. where the # symbol represents the number of managers assigned to an assistant.

To add more managers, click Add more Managers .

Step 6

Choose the operation that you want to perform:

To create new manager-assistant associations, click Insert .

To delete a manager or an assistant from a manager-assistant
                                                				  association, click Delete .

Step 7

To transfer the data from the BAT spreadsheet into a CSV data
                                          			 file, click Export to BAT Format .

Tip

For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 Managers/Assistants window in BAT.

#### What to do next

You must upload the CSV data file to the Cisco Unified Communications Manager first node database server so BAT can access the CSV data file.

### Create Custom Manager-Assistant CSV Data Files

When you have existing phones that you want to set up with
                                 		  manager-assistant associations, you can use the Custom Managers-Assistants tab in the BAT
                                 		  spreadsheet. Use the BAT spreadsheet to create a custom CSV data file for
                                 		  inserting or updating manager-assistant associations for proxy lines on the
                                 		  assistant phones.

After you have finished editing all the fields in the BAT spreadsheet,
                                 		  you can export the content to a CSV formatted data file. The system saves the
                                 		  file using the default filename Custom Manager-Assistants-timestamp.txt to C:\XLSDataFiles or to your choice of another
                                 		  existing folder on your local workstation.

Step 1

Download the BAT.xlt file from Cisco Unified Communications Manager server.

Step 2

Open the BAT.xlt file. When prompted, click Enable Macros to use the spreadsheet
                                          			 capabilities.

Step 3

To display the manager-assistant association options, click the Custom Managers-Assistants tab at the bottom
                                          			 of the spreadsheet.

Step 4

Scroll to the right side of the template until you see Number of Proxy Lines box. In that box, enter
                                          			 the number of proxy lines that you are assigning to an assistant. The
                                          			 spreadsheet adds Proxy Line DN and Manager Line DN Columns based on the number
                                          			 that you enter.

Complete all mandatory fields and any relevant, optional fields.

Manager ID—Enter the user ID of the manager.

Device Name—Enter the device name that are assigned to the manager phone.

Intercom DN—Enter the directory number for the manager intercom line. (Optional)

Assistant ID—Enter the user IDs for the assistants to whom the manager will be associated.

Device Name—Enter the device name that are assigned to the assistant's phone.

Intercom DN—Enter the directory number for the assistant intercom line. (Optional)

Proxy Line DN # —Enter the directory number for the assistant proxy line.

Manager Line DN # —Enter the directory number for the manager primary line.

The # symbol represents the number of proxy lines that
                                             				are associated to a manager.

Step 5

To transfer the data from the BAT spreadsheet into a CSV data
                                          			 file, click Export to BAT Format button.

Tip

For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 Managers/Assistants window in BAT.

The system saves the file using the default filename Custom Manager-Assistants-timestamp.txt to C:\XLSDataFiles or to your choice of another
                                             				existing folder on your local workstation.

#### What to do next

You must upload the CSV data file to the Unified Communications Manager first node database server so BAT can access the CSV data file.

## Topics Related to CVS Data Files for Manager-Assistant

| Note | You can associate users to devices/phones only if they support
                                       		  UnifiedCM Assistant. |
|---|---|

| Step 1 | Set up and
                                          			 configure UnifiedCM Assistant requirements for your system. Cisco recommends
                                          			 that you use the CiscoUnifiedCM Assistant Configuration Wizard. The wizard
                                          			 automatically creates the phone templates for UnifiedCM Assistant manager and
                                          			 assistant, route points, partitions, translation patterns, and calling search
                                          			 space for the CiscoUnifiedCM Assistant service. To run the CiscoUnifiedCM
                                          			 Assistant Configuration Wizard, ensure BAT and the wizard are on the same
                                          			 server. See the Feature Configuration Guide for Cisco Unified Communications
                                                				  Manager Guide for information about running the CiscoUnifiedCM
                                             				Assistant Configuration Wizard. Note You can use
                                                         				  the CiscoUnifiedCM Assistant Configuration Wizard only one time to set up the
                                                         				  UnifiedCM Assistant configuration requirements for your system. After running
                                                         				  the configuration wizard, you can only view, but not change, your configuration
                                                         				  with the wizard. | Note | You can use
                                                         				  the CiscoUnifiedCM Assistant Configuration Wizard only one time to set up the
                                                         				  UnifiedCM Assistant configuration requirements for your system. After running
                                                         				  the configuration wizard, you can only view, but not change, your configuration
                                                         				  with the wizard. |
|---|---|---|---|
| Note | You can use
                                                         				  the CiscoUnifiedCM Assistant Configuration Wizard only one time to set up the
                                                         				  UnifiedCM Assistant configuration requirements for your system. After running
                                                         				  the configuration wizard, you can only view, but not change, your configuration
                                                         				  with the wizard. |
| Step 2 | To add new
                                          			 phones and users for managers and assistants, use the UnifiedCM Assistant
                                          			 manager and UnifiedCM Assistant assistant phone templates that the
                                          			 CiscoUnifiedCM Assistant Configuration Wizard produced on the BAT server. Use
                                          			 the BAT templates to configure phones for proxy mode only. |
| Step 3 | For existing
                                          			 manager and assistant phones, you can change the manager and assistant phones
                                          			 to correspond to the UnifiedCM Assistant phone templates by using either of
                                          			 these methods: You can use
                                                   					 the Add Lines feature in BAT to modify existing phones to resemble the
                                                   					 UnifiedCM Assistant phone templates. You can
                                                   					 delete the original phones and add new phones by using the UnifiedCM Assistant
                                                   					 phone templates for managers and assistants. |
| Step 4 | After you
                                          			 configure the phones and lines for managers and assistants, you associate the
                                          			 manager and assistant lines for UnifiedCM Assistant control. |

| Note | You can use
                                                         				  the CiscoUnifiedCM Assistant Configuration Wizard only one time to set up the
                                                         				  UnifiedCM Assistant configuration requirements for your system. After running
                                                         				  the configuration wizard, you can only view, but not change, your configuration
                                                         				  with the wizard. |
|---|---|

| Field | Default Value |
|---|---|
| Softkey Template | Softkey Template Standard Manager |
| Phone Button Template | Standard CiscoUnifiedIPPhone 7960 (2 lines) |
| Line1 | Primary line CSS =
                                                   						Generated_CSS_I_E Partition =
                                                   						Generated_Managers |
| Line 2 | Incoming Intercom line CSS =
                                                   						Generated_CSS_I_E Partition =
                                                   						Generated_Everyone Also configure
                                                   						auto answer with headset option. |
| Services | Assistant Primary Service |

| Field | Default Value |
|---|---|
| Softkey Template | Softkey Assistant |
| Phone Button Template | Standard CiscoUnifiedIPPhone 7960 Assistant |
| Expansion Module 1 | 14-button expansion module |
| One line on base phone and five lines on expansion module | For proxy lines, one line on base phone and five lines on
                                                					 expansion module have the following default configuration: CSS =
                                                   						Generated_CSS_M_E Partition =
                                                   						Generated_Everyone |
| Line 7 (On Expansion Module) | Intercom line CSS =
                                                   						Generated_CSS_I_E Partition =
                                                   						Generated_Everyone Also configure
                                                   						auto answer with headset option. |

| Number of Available Lines | Configuration |
|---|---|
| One line | Line 1—Primary line (UnifiedCM Assistant controlled) Intercom line (none) |
| Two lines (Default UnifiedCM Assistant manager phone template) | Line 1—Primary line (UnifiedCM Assistant controlled) Line 2—Intercom line (optional) |
| More than two lines | Last line gets configured as the intercom line. The number of available lines on the assistant phone
                                                   					 determines the number of manager lines that get associated with proxy lines. |

| Number of Available Lines | Configuration |
|---|---|
| One line | Line 1—Proxy line Intercom line (none) |
| Two lines | Line 1—Primary line Line 2—Proxy line Intercom line (none) |
| Three lines | Line 1—Primary line Line 2—Proxy line Line 3—Intercom line |
| More than three lines | Line 1—Primary line Line 2—Proxy line Last line gets configured as the intercom line All other lines get configured as proxy lines |
| Seven lines (Default UnifiedCM Assistant assistant phone template) | Line 1—Primary line Line 2 through line 6 can get configured as proxy lines to
                                                   					 support up to five managers. Line 7—Intercom line |

| Step 1 | Choose BAT
                                                   				  Administration > Phones > Phones
                                                   				  Template . The Phone Template Configuration window displays. Note Because BAT UnifiedCM Assistant templates are write protected,
                                                            				  if you want to make changes to these templates, you must make a copy of the
                                                            				  template and then edit the template with your changes. See Table 1 for default manager phone template field descriptions. See Table 2 for default assistant phone template field descriptions. | Note | Because BAT UnifiedCM Assistant templates are write protected,
                                                            				  if you want to make changes to these templates, you must make a copy of the
                                                            				  template and then edit the template with your changes. See Table 1 for default manager phone template field descriptions. See Table 2 for default assistant phone template field descriptions. |
|---|---|---|---|
| Note | Because BAT UnifiedCM Assistant templates are write protected,
                                                            				  if you want to make changes to these templates, you must make a copy of the
                                                            				  template and then edit the template with your changes. See Table 1 for default manager phone template field descriptions. See Table 2 for default assistant phone template field descriptions. |
| Step 2 | Create the CSV data file for manager phones and another file for
                                             			 assistant phones using these options: Use the BAT spreadsheet and choose the Phones tab. Use a text editor and refer to the manager or assistant
                                                   				  template fields as a guide. |

| Note | Because BAT UnifiedCM Assistant templates are write protected,
                                                            				  if you want to make changes to these templates, you must make a copy of the
                                                            				  template and then edit the template with your changes. See Table 1 for default manager phone template field descriptions. See Table 2 for default assistant phone template field descriptions. |
|---|---|

| Step 1 | Choose BAT Administration > Phones > Add Lines . The Phone Add Lines window displays. |
|---|---|
| Step 2 | You may need to copy and modify the UnifiedCM Assistant templates for BAT. See Table 1 for default manager phone template field descriptions, and see Table 2 for default assistant phone template field descriptions. Note If you changed any configuration information (for example, partition names) when you ran the CiscoUnifiedCM Assistant Configuration
                                                            Wizard, you must use the same configuration information for the fields when you edit the template. | Note | If you changed any configuration information (for example, partition names) when you ran the CiscoUnifiedCM Assistant Configuration
                                                            Wizard, you must use the same configuration information for the fields when you edit the template. |
| Note | If you changed any configuration information (for example, partition names) when you ran the CiscoUnifiedCM Assistant Configuration
                                                            Wizard, you must use the same configuration information for the fields when you edit the template. |
| Step 3 | Create the CSV data file for manager phones and another file for assistant phones using one of these options: Use the BAT spreadsheet and choose the Add Lines tab. Use a text editor and use the manager or assistant template fields as a guide. |

| Note | If you changed any configuration information (for example, partition names) when you ran the CiscoUnifiedCM Assistant Configuration
                                                            Wizard, you must use the same configuration information for the fields when you edit the template. |
|---|---|

| Note | If you have a CiscoUnifiedIPPhone model 7960, you need a phone
                                             			 button template with five or more lines. |
|---|---|

| Create a BAT template to add new or update existing manager and
                                          			 assistant phones using the following guidelines: For manager phones, see Manager Phone Settings for Shared Line Mode . For assistant phones, see Assistant Phone Settings for Shared Line Mode . |
|---|

| Note | CiscoUnifiedIPPhone 7960 phone button templates include
                                                      				  expansion module lines. |
|---|---|

| Add new UnifiedCM Assistant associations using the BAT
                                          			 spreadsheet. To create manager-assistant associations with the default line
                                                				  configuration, see Create Default Manager-Assistant CSV Data Files . See Table 1 and Table 1 for the default line configurations for the
                                                				  manager and assistant phones. To assign proxy lines that do not follow the default line
                                                				  configuration, see Create Custom Manager-Assistant CSV Data Files . |
|---|

| Step 1 | Download and open the BAT.xlt file to open the BAT spreadsheet. |
|---|---|
| Step 2 | When prompted, click Enable Macros to use the spreadsheet
                                          			 capabilities. |
| Step 3 | To display the manager-assistant association options, click the Default Managers-Assistants tab at the bottom
                                          			 of the spreadsheet. |
| Step 4 | Scroll to the right side of the template until you see the radio
                                          			 buttons and choose the type of associations for this transaction: One manager,
                                             				multiple assistants One assistant,
                                             				multiple managers |
| Step 5 | Complete all mandatory fields and any relevant, optional fields. If you choose the One manager, multiple assistants radio
                                                				  button, enter the following information in each row: Manager ID—Enter the user ID, up to 30 characters, of the manager. Assistant ID # —Enter the user IDs, up to 30 characters, for the assistants to whom the manager will be associated, where the # symbol represents the number of assistants assigned to a manager. Tip To add more assistants, click Add more Assistants . If you choose the One assistant, multiple managers radio
                                                				  button, enter the following information in each row: Assistant ID—Enter the user ID, up to 30 characters, of the assistant. Manager ID # —Enter the user IDs, up to 30 characters, for the managers to whom the assistant will be associated. where the # symbol represents the number of managers assigned to an assistant. Note To add more managers, click Add more Managers . | Tip | To add more assistants, click Add more Assistants . | Note | To add more managers, click Add more Managers . |
| Tip | To add more assistants, click Add more Assistants . |
| Note | To add more managers, click Add more Managers . |
| Step 6 | Choose the operation that you want to perform: To create new manager-assistant associations, click Insert . To delete a manager or an assistant from a manager-assistant
                                                				  association, click Delete . |
| Step 7 | To transfer the data from the BAT spreadsheet into a CSV data
                                          			 file, click Export to BAT Format . Tip For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 Managers/Assistants window in BAT. The system saves the file using the default filename <type of
                                             				operation>ManagerAssistants-timestamp.txt to C:\XLSDataFiles or to your choice of another
                                          			 existing folder on your local workstation. | Tip | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 Managers/Assistants window in BAT. |
| Tip | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 Managers/Assistants window in BAT. |

| Tip | To add more assistants, click Add more Assistants . |
|---|---|

| Note | To add more managers, click Add more Managers . |
|---|---|

| Tip | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 Managers/Assistants window in BAT. |
|---|---|

| Step 1 | Download the BAT.xlt file from Cisco Unified Communications Manager server. |
|---|---|
| Step 2 | Open the BAT.xlt file. When prompted, click Enable Macros to use the spreadsheet
                                          			 capabilities. |
| Step 3 | To display the manager-assistant association options, click the Custom Managers-Assistants tab at the bottom
                                          			 of the spreadsheet. |
| Step 4 | Scroll to the right side of the template until you see Number of Proxy Lines box. In that box, enter
                                          			 the number of proxy lines that you are assigning to an assistant. The
                                          			 spreadsheet adds Proxy Line DN and Manager Line DN Columns based on the number
                                          			 that you enter. Complete all mandatory fields and any relevant, optional fields. Manager ID—Enter the user ID of the manager. Device Name—Enter the device name that are assigned to the manager phone. Intercom DN—Enter the directory number for the manager intercom line. (Optional) Assistant ID—Enter the user IDs for the assistants to whom the manager will be associated. Device Name—Enter the device name that are assigned to the assistant's phone. Intercom DN—Enter the directory number for the assistant intercom line. (Optional) Proxy Line DN # —Enter the directory number for the assistant proxy line. Manager Line DN # —Enter the directory number for the manager primary line. The # symbol represents the number of proxy lines that
                                             				are associated to a manager. |
| Step 5 | To transfer the data from the BAT spreadsheet into a CSV data
                                          			 file, click Export to BAT Format button. Tip For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 Managers/Assistants window in BAT. The system saves the file using the default filename Custom Manager-Assistants-timestamp.txt to C:\XLSDataFiles or to your choice of another
                                             				existing folder on your local workstation. | Tip | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 Managers/Assistants window in BAT. |
| Tip | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 Managers/Assistants window in BAT. |

| Tip | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 Managers/Assistants window in BAT. |
|---|---|