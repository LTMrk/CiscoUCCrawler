---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-installatio-700589aa75
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/installation/guide/ucce_b_stagingguide_release_15_0_1/ucce_m_1261_domain-manager.html
retrieved_at: 2026-08-16T19:58:56.808594+00:00
---

Staging Guide for Cisco Unified ICM/Contact Center Enterprise, Release 15.0(1)

# Staging Guide for Cisco Unified ICM/Contact Center Enterprise, Release 15.0(1)

Updated: March 24, 2025

Chapter: Domain Manager

## Chapter: Domain Manager

# Domain Manager

## Domain Manager Tool
                        	 Functionality

The Domain Manager
                              		  Tool performs the following functions:

Creates a Cisco
                                    				Root OU named Cisco_ICM in the domain. After Domain Manager creates this root
                                    				OU, it also creates two domain local security groups:

Cisco_ICM_Config

Cisco_ICM_Setup

Creates a
                                    				facility OU under the Cisco Root OU, and creates two domain local security
                                    				groups:

< Facility
                                             						name >_Config

< Facility
                                             						name >_Setup

The Domain
                                    				Manager adds the < Facility name >_Setup group to the < Facility
                                       				  name >_Config group. The Domain Manager also adds security groups
                                    				as follows:

Adds
                                          					 Cisco_ICM_Config group to < Facility name >_Config

Adds
                                          					 Cisco_ICM_Setup group to < Facility name >_Setup

Creates an
                                    				instance OU under each facility OU, and creates three domain local security
                                    				groups:

< Facility
                                             						name >_< Instance name >_Config

< Facility
                                             						name >_< Instance name >_Setup

< Facility
                                             						name >_< Instance name >_Service

The Domain
                                    				Manager also performs the following operations:

Adds
                                          					 < Facility
                                             						name >_< Instance name >_Setup to < Facility
                                             						name >_< Instance name >_Config, because the setup group
                                          					 needs the permissions for the config group.

< Facility
                                             						name >_Config group to < Facility
                                             						name >_< Instance name >_Config

< Facility
                                             						name >_Setup group to < Facility
                                             						name >_< Instance name >_Setup

The config
                                    				security group has domain read write permission, so that the user in that group
                                    				can create a users group as well as OUs in the domain.

For more information, see the chapter Organizational Units.

## Open the Domain
                        	 Manager

To run the Domain
                              		  Manager, you must be a Domain admin or a domain user who has domain read write
                              		  permission, so you can create OUs and groups.

You can open the
                                       			 Domain Manager in the following ways:

- Open the Domain Manager
                                          				application from the Cisco Unified Tools folder.

- Access through Start > Programs > Cisco Unified CCE
                                                					 Tools > Domain Manager .

## Domain Manager
                        	 Window

The Domain Manager
                              		  dialog box displays the current domain and the Cisco Unified ICM related OUs
                              		  contained in the domain.

### Domain Manager
                              		  Tree

The Domain Manager
                              		  tree display provides a quick view of the Unified ICM created AD OUs and groups
                              		  in the selected domains. You can display Multiple domains in the tree. The
                              		  default domain displayed is the current machine domain. When you first expand a
                              		  domain node, it is validated. The OU Validation Errors dialog box appears only
                              		  if the error is due to missing or incorrect OU hierarchy information.

A context menu
                              		  displays when you right-click any object in the Domain Manager tree. These
                              		  menus provide additional functionality specific to the following level:

Domains

Add Cisco
                                          					 Root

Refresh

Cisco Root

Remove Cisco
                                          					 Root

Add Facility

Security
                                          					 Information

Properties

Facility

Remove
                                          					 Facility

Add Instance

Security
                                          					 Information

Instance

Service Log
                                          					 On Properties

Security
                                          					 Information

Remove
                                          					 Instance

Security group

Security
                                          					 Group Members

Properties

Property

Description

Domains

To add or
                                          					 remove a domain from the Domain Manager tree, click Select . The Select Domains dialog box appears. For more
                                          					 information, see View Domains .

Cisco Root

To add the
                                          					 Cisco Root when you select a domain that does not already have the Cisco Root,
                                          					 click Add . The Select OU dialog box appears (for more information,
                                          					 see Create or Add Cisco Root ). To remove the selected Cisco Root
                                          					 and all of its facilities and instances, click Remove .

Facility

To add a
                                          					 new facility, select the Cisco Root OU then click Add . The Enter Facility Name dialog box appears (for more
                                          					 information, see Create or Add Facility OU ). To remove the selected facility
                                          					 and all of its instances, click Remove .

Instance

To add an
                                          					 instance, select a facility in the Domain tree display, then click Add . The Add Instance dialog box appears (for more
                                          					 information, see Create Instance OU ). To remove the selected instance,
                                          					 click Remove .

Security
                                          					 group

Click Members to display the Security Group Members dialog box (for more
                                          					 information, see Add Users to Security Group ) where you assign users to
                                          					 security groups.

### View Domains

Step 1

Open the Domain
                                          			 Manager.

Step 2

In the right top
                                          			 pane of the Domain Manager, click Select .

You can now add or
                                 		  remove domains for use with the system software.

Property

Description

Enter domain
                                             					 name:

Allows you
                                             					 to enter fully qualified domain name. After you enter the qualified domain
                                             					 name, click Add . The domain appears in the Choose domains list.

Filter
                                             					 domain choices

Forest – Filters the Choose domains list to display
                                                   						  only domains in the same forest.

Trusted – Filters the Choose domains list to display
                                                   						  only trusted domains.

Both – Filters the Choose domains list to display
                                                   						  both forest and trusted domains.

Choose
                                             					 domains:

Choose a
                                             					 domain from the displayed list:

Add > — Adds domains
                                                   						  selected in the Choose domains list to the Selected domains list.

< Remove — Removes
                                                   						  selected domains from the Selected domains list.

Add All >> — Adds
                                                   						  all the domains in the Choose domains list to the Selected domains list.

<< Remove All —
                                                   						  Moves all the domains from the Selected domains list to the Choose domains
                                                   						  list.

Selected
                                             					 domains:

Displays a
                                             					 list of all the selected domains.

For more information, see the chapter Domain Manager.

### Add Domain to a View

You can add domains by using the controls in the Select Domains dialog
                                 		  box. Follow these steps to add a domain:

Step 1

In the left pane under Choose domains, select one or more domains.

Step 2

Click Add > to add the selected domains, or click Add All >> to add all the domains.

You can also manually type in a domain to add to a view instead of
                                             				clicking.

Step 3

In the field under Enter domain name, enter the fully qualified
                                          			 domain name to add.

Step 4

Click Add .

Step 5

Click OK .

The added domains now appear in the Domain Manager dialog box. You can
                                 		  then add the Cisco Root OU.

### Remove Domain from a View

You can remove domains by using the controls in the Select Domains
                                 		  dialog box. Follow these steps to remove a domain:

Step 1

In the Select Domains dialog box, in right pane under Selected domains: , select one or more domains.

Step 2

Click <Remove to remove the selected domains, or
                                          			 click <<Remove All to remove all the domains.

Step 3

Click OK .

The removed domains no longer appear in the Domain Manager dialog box.

### Create or Add Cisco
                           	 Root

You can create the
                                 		  Cisco Root OU either in the domain root, or beneath another OU in the domain.

Step 1

Select the
                                          			 domain you want to add.

If the current
                                             				domain, which the Domain Manager loads by default, is not the domain to which
                                             				you want to add a root, then add a domain to the view.

Step 2

Click the Cisco
                                             				Root Add button. This displays the Select OU dialog box.

Step 3

Click Add to add the Root.

The Select
                                             				Organizational Unit dialog box appears.

Step 4

Select the OU
                                          			 under which you want to create the Cisco Root OU, then click OK .

When you return to
                                 		  the Unified ICM Domain Manager dialog box, the Cisco Root OU appears either at
                                 		  the domain root, or under the OU you selected in step 3. You can now add
                                 		  facilities and configure security groups.

To access the Cisco
                                 		  Root Properties, right-click the Root node in the main dialog box and select Properties . Add is disabled if the Root already exists.

### Remove Cisco
                           	 Root

Only users with administrative control at the level above the Cisco Root OU can delete the Cisco Root OU.

Step 1

Open the Domain
                                          			 Manager.

Step 2

Select the root
                                          			 in the tree.

Step 3

In the right
                                          			 pane under Cisco Root, click Remove .

You are prompted
                                             				to confirm the removal of the Cisco_ICM OU.

Warning

All Unified ICM instances in this domain will no longer work properly if the OU is removed. All users, groups, and other objects
                                                         in this OU will also be deleted.

Step 4

Click OK to confirm the removal.

### Create or Add
                           	 Facility OU

You create a
                                 		  Facility OU to group one or more Instance OUs.

You must create the
                                 		  Cisco Root OU for the domain before you can create a Facility OU.

Step 1

Open the Domain
                                          			 Manager.

Step 2

In the tree view
                                          			 in the left pane, select the Cisco Root OU under which you want to create the
                                          			 Facility OU.

Step 3

In the right
                                          			 pane, under Facility, click Add .

The Enter
                                                				  Facility Name dialog box opens.

Step 4

Enter the name
                                          			 for the facility.

Step 5

Click OK .

The Facility OU is
                                 		  created in the OU tree and shown in the left pane, beneath the Cisco Root OU.

### Remove Facility
                           	 OU

Only users with administrative control at the level above the Facility OU might delete the Facility OU.

Step 1

Open the Domain
                                          			 Manager.

Step 2

In the tree view
                                          			 in the left pane, navigate down the tree to find and select the Facility OU you
                                          			 want to delete.

Step 3

In the right
                                          			 pane, under Facility, click Remove .

You are prompted
                                             				to confirm the removal.

Warning

All Unified ICM instances in this facility will no longer work properly if the OU is removed. All users, groups, and other
                                                         objects in this OU will also be deleted.

Step 4

Click OK to confirm the removal.

The Facility OU is
                                 		  removed from the tree.

### Create Instance
                           	 OU

You can create an
                                 		  Instance OU while creating a Unified ICM instance, or before you create the
                                 		  Unified ICM instance.

Step 1

Open the Domain
                                          			 Manager.

Step 2

In the tree view
                                          			 in the left pane, navigate to and select the Facility OU under which you want
                                          			 to create the Instance OU.

Step 3

In the right
                                          			 pane, under Instance, click Add .

The Add Instance
                                             				dialog box opens.

Step 4

At this point,
                                          			 you have two options:

If you are
                                                				  installing Unified ICM on the current computer for the first time, under the Enter instance name radio button, enter the instance
                                                				  name.

The
                                                               						Instance OU name must be five alpha-numeric characters or less, cannot begin
                                                               						with a numeric character, and cannot be a reserved name such as local or sddsn.

If you are
                                                				  upgrading an existing Unified ICM instance, the instance is listed under the Select existing instances radio button. In this
                                                				  situation, select Select existing instance , then select the Unified
                                                				  ICM instance from the list.

Step 5

Click OK .

The Instance OU is
                                 		  added below the selected Facility OU.

### Remove Instance
                           	 OU

Step 1

Open the Domain
                                          			 Manager.

Step 2

In the tree view
                                          			 in the left pane, navigate down the tree to find and select the Instance OU you
                                          			 want to delete.

Step 3

In the right
                                          			 pane, under Instance, click Remove .

You are prompted
                                             				to confirm the removal.

Warning

This Unified ICM instance will no longer work properly if the OU is removed. All users, groups, and other objects in this
                                                         OU will also be deleted.

Step 4

Click OK to confirm the removal.

The Instance OU is
                                 		  removed from the tree.

## Security
                        	 Groups

A security group is
                              		  a collection of domain users to whom you grant a set of permissions to perform
                              		  tasks with the system software.

For each security
                              		  group, you add a set of domain users who are granted privileges to the
                              		  functions controlled by that security group. The Security Group Members dialog
                              		  box displays the list of groups that are members of the security group selected
                              		  in the Domain Manager main dialog box. You can add and remove users from the
                              		  selected group using this dialog box.

Property

Description

Groups

Displays
                                          					 groups that are members of the security group selected in the Domain Manager
                                          					 main dialog box

Users

Displays the
                                          					 name and user login name of the user.

Add

Use this
                                          					 option to add members to the Security Group.

Remove

Use this
                                          					 option to remove members from the Security Group.

OK

Use this
                                          					 option to save changes and return to Domain Manager.

## Add Users to
                        	 Security Group

Step 1

In the Domain
                                       			 Manager, select the Security Group you want to add a user to.

Step 2

Click Member in the Security Group pane of the ICM Domain
                                       			 Manager.

The Security
                                          				Group dialog box appears.

Step 3

In the Users
                                       			 pane, select Add .

The Add Members
                                          				to Security Group dialog box appears.

Step 4

Select the
                                       			 filters that are used to create a list of users to select from.

Domain – Select
                                                					 the domain you want to add as a member to the Security Group.

Optional filter

Select the
                                                					 optional filter you want to use:

<None> – No additional filter selections
                                                      						  applied, Condition and Value inaccessible.

Name – Continue and search the appropriate Condition
                                                      						  and Value. This filter is based on the username of the user.

User Login Name – Continue and search the
                                                      						  appropriate Condition and Value. This filter is based on the username of the
                                                      						  user.

Condition

Select the
                                                					 condition to facilitate your search for the member you want to list:

Contains – find and list members containing the
                                                      						  entered Value.

Starts with – find and list members whose name or
                                                      						  user login name starts with the entered Value.

Ends with – find and list members whose name or user
                                                      						  logon name ends with the entered Value.

Value

Enter the
                                                					 appropriate value to search on, for example, enter the first name of the user
                                                					 you want to add. This value provides a list of members with that name for you
                                                					 to choose from.

Step 5

Select the
                                       			 member you want to add to the Security Group from the displayed list.

Step 6

Click OK to add the selected member to the Security Group.

## Remove Members from
                        	 Security Group

Step 1

In the Domain
                                       			 Manager, select the Security Group from which you want to remove members.

Step 2

In the Security
                                       			 Group pane of the Domain Manager dialog box, select Members .

The Security
                                          				Group dialog box appears.

Step 3

In the Users
                                       			 pane, select the member you want to remove from the Security Group.

Step 4

Click Remove .

Step 5

Click OK to remove the selected member from the Security
                                       			 Group.

## Organizational Unit
                        	 Validation Errors Dialog Box

This dialog box
                              		  appears if errors are found during OU validation.

Property

Description

Validation
                                          					 error for organizational unit:

Displays the
                                          					 OU containing the error found during OU validation.

Error

Displays
                                          					 description of errors found during OU validation.

Location

Displays the
                                          					 location of each error found during OU validation.

Do you want
                                          					 to fix the errors?

Four
                                          					 possible responses:

Yes – Fixes the displayed
                                                						  error then attempts to sequentially validate the next OU. If more errors are
                                                						  found, you return to this dialog box.

Yes to All – Recursively
                                                						  fixes the displayed error and any errors found during sequential validation
                                                						  attempts for other ICM OUs without returning to this dialog box.

No – Does not fix the
                                                						  displayed error but attempts to sequentially validate the next OU. If more
                                                						  errors are found, you return to this dialog box.

No to All – Does not fix
                                                						  the displayed error but recursively validates the OUs and logs any additional
                                                						  errors without returning you to this dialog box.

| You can open the
                                       			 Domain Manager in the following ways: Open the Domain Manager
                                          				application from the Cisco Unified Tools folder. Access through Start > Programs > Cisco Unified CCE
                                                					 Tools > Domain Manager . |
|---|

| Note | When the Domain
                                       		  Manager dialog box opens, multiple domains might display in the domain tree in
                                       		  the left pane of the dialog box. The default domain displayed is the domain the
                                       		  current user is logged into. |
|---|---|

| Property | Description |
|---|---|
| Domains | To add or
                                          					 remove a domain from the Domain Manager tree, click Select . The Select Domains dialog box appears. For more
                                          					 information, see View Domains . |
| Cisco Root | To add the
                                          					 Cisco Root when you select a domain that does not already have the Cisco Root,
                                          					 click Add . The Select OU dialog box appears (for more information,
                                          					 see Create or Add Cisco Root ). To remove the selected Cisco Root
                                          					 and all of its facilities and instances, click Remove . |
| Facility | To add a
                                          					 new facility, select the Cisco Root OU then click Add . The Enter Facility Name dialog box appears (for more
                                          					 information, see Create or Add Facility OU ). To remove the selected facility
                                          					 and all of its instances, click Remove . |
| Instance | To add an
                                          					 instance, select a facility in the Domain tree display, then click Add . The Add Instance dialog box appears (for more
                                          					 information, see Create Instance OU ). To remove the selected instance,
                                          					 click Remove . |
| Security
                                          					 group | Click Members to display the Security Group Members dialog box (for more
                                          					 information, see Add Users to Security Group ) where you assign users to
                                          					 security groups. |

| Step 1 | Open the Domain
                                          			 Manager. |
|---|---|
| Step 2 | In the right top
                                          			 pane of the Domain Manager, click Select . |

| Property | Description |
|---|---|
| Enter domain
                                             					 name: | Allows you
                                             					 to enter fully qualified domain name. After you enter the qualified domain
                                             					 name, click Add . The domain appears in the Choose domains list. |
| Filter
                                             					 domain choices | Forest – Filters the Choose domains list to display
                                                   						  only domains in the same forest. Trusted – Filters the Choose domains list to display
                                                   						  only trusted domains. Both – Filters the Choose domains list to display
                                                   						  both forest and trusted domains. |
| Choose
                                             					 domains: | Choose a
                                             					 domain from the displayed list: Add > — Adds domains
                                                   						  selected in the Choose domains list to the Selected domains list. < Remove — Removes
                                                   						  selected domains from the Selected domains list. Add All >> — Adds
                                                   						  all the domains in the Choose domains list to the Selected domains list. << Remove All —
                                                   						  Moves all the domains from the Selected domains list to the Choose domains
                                                   						  list. |
| Selected
                                             					 domains: | Displays a
                                             					 list of all the selected domains. |

| Step 1 | In the left pane under Choose domains, select one or more domains. |
|---|---|
| Step 2 | Click Add > to add the selected domains, or click Add All >> to add all the domains. You can also manually type in a domain to add to a view instead of
                                             				clicking. |
| Step 3 | In the field under Enter domain name, enter the fully qualified
                                          			 domain name to add. |
| Step 4 | Click Add . |
| Step 5 | Click OK . |

| Step 1 | In the Select Domains dialog box, in right pane under Selected domains: , select one or more domains. |
|---|---|
| Step 2 | Click <Remove to remove the selected domains, or
                                          			 click <<Remove All to remove all the domains. |
| Step 3 | Click OK . |

| Note | The user who
                                          		  creates the Cisco Root OU automatically becomes a member of the Setup Security
                                          		  Group for the Cisco Root OU. In effect, this user is granted privileges to all
                                          		  Unified ICM tasks in the domain. |
|---|---|

| Step 1 | Select the
                                          			 domain you want to add. If the current
                                             				domain, which the Domain Manager loads by default, is not the domain to which
                                             				you want to add a root, then add a domain to the view. |
|---|---|
| Step 2 | Click the Cisco
                                             				Root Add button. This displays the Select OU dialog box. |
| Step 3 | Click Add to add the Root. The Select
                                             				Organizational Unit dialog box appears. Figure 3. Select OU
                                                				  Dialog Box |
| Step 4 | Select the OU
                                          			 under which you want to create the Cisco Root OU, then click OK . |

| Note | The Domain
                                          		  Administrator is made a member of the Setup group as well. |
|---|---|

| Note | Only users with administrative control at the level above the Cisco Root OU can delete the Cisco Root OU. |
|---|---|

| Step 1 | Open the Domain
                                          			 Manager. |
|---|---|
| Step 2 | Select the root
                                          			 in the tree. |
| Step 3 | In the right
                                          			 pane under Cisco Root, click Remove . You are prompted
                                             				to confirm the removal of the Cisco_ICM OU. Warning All Unified ICM instances in this domain will no longer work properly if the OU is removed. All users, groups, and other objects
                                                         in this OU will also be deleted. | Warning | All Unified ICM instances in this domain will no longer work properly if the OU is removed. All users, groups, and other objects
                                                         in this OU will also be deleted. |
| Warning | All Unified ICM instances in this domain will no longer work properly if the OU is removed. All users, groups, and other objects
                                                         in this OU will also be deleted. |
| Step 4 | Click OK to confirm the removal. |

| Warning | All Unified ICM instances in this domain will no longer work properly if the OU is removed. All users, groups, and other objects
                                                         in this OU will also be deleted. |
|---|---|

| Note | You must create
                                          		  at least one Facility OU before you can create a Unified ICM instance. |
|---|---|

| Step 1 | Open the Domain
                                          			 Manager. |
|---|---|
| Step 2 | In the tree view
                                          			 in the left pane, select the Cisco Root OU under which you want to create the
                                          			 Facility OU. |
| Step 3 | In the right
                                          			 pane, under Facility, click Add . The Enter
                                                				  Facility Name dialog box opens. Figure 4. Enter
                                                				  Facility Name Dialog Box |
| Step 4 | Enter the name
                                          			 for the facility. Note Facility OU
                                                      				names must be 32 characters or less, and cannot contain the characters # , + "
                                                      				< > ; / \ [] : ? * | Note | Facility OU
                                                      				names must be 32 characters or less, and cannot contain the characters # , + "
                                                      				< > ; / \ [] : ? * |
| Note | Facility OU
                                                      				names must be 32 characters or less, and cannot contain the characters # , + "
                                                      				< > ; / \ [] : ? * |
| Step 5 | Click OK . |

| Note | Facility OU
                                                      				names must be 32 characters or less, and cannot contain the characters # , + "
                                                      				< > ; / \ [] : ? * |
|---|---|

| Note | Only users with administrative control at the level above the Facility OU might delete the Facility OU. |
|---|---|

| Step 1 | Open the Domain
                                          			 Manager. |
|---|---|
| Step 2 | In the tree view
                                          			 in the left pane, navigate down the tree to find and select the Facility OU you
                                          			 want to delete. |
| Step 3 | In the right
                                          			 pane, under Facility, click Remove . You are prompted
                                             				to confirm the removal. Warning All Unified ICM instances in this facility will no longer work properly if the OU is removed. All users, groups, and other
                                                         objects in this OU will also be deleted. | Warning | All Unified ICM instances in this facility will no longer work properly if the OU is removed. All users, groups, and other
                                                         objects in this OU will also be deleted. |
| Warning | All Unified ICM instances in this facility will no longer work properly if the OU is removed. All users, groups, and other
                                                         objects in this OU will also be deleted. |
| Step 4 | Click OK to confirm the removal. |

| Warning | All Unified ICM instances in this facility will no longer work properly if the OU is removed. All users, groups, and other
                                                         objects in this OU will also be deleted. |
|---|---|

| Step 1 | Open the Domain
                                          			 Manager. |
|---|---|
| Step 2 | In the tree view
                                          			 in the left pane, navigate to and select the Facility OU under which you want
                                          			 to create the Instance OU. |
| Step 3 | In the right
                                          			 pane, under Instance, click Add . The Add Instance
                                             				dialog box opens. Figure 5. Add
                                                				  Instance (Organizational Unit) Dialog Box |
| Step 4 | At this point,
                                          			 you have two options: If you are
                                                				  installing Unified ICM on the current computer for the first time, under the Enter instance name radio button, enter the instance
                                                				  name. Note The
                                                               						Instance OU name must be five alpha-numeric characters or less, cannot begin
                                                               						with a numeric character, and cannot be a reserved name such as local or sddsn. If you are
                                                				  upgrading an existing Unified ICM instance, the instance is listed under the Select existing instances radio button. In this
                                                				  situation, select Select existing instance , then select the Unified
                                                				  ICM instance from the list. | Note | The
                                                               						Instance OU name must be five alpha-numeric characters or less, cannot begin
                                                               						with a numeric character, and cannot be a reserved name such as local or sddsn. |
| Note | The
                                                               						Instance OU name must be five alpha-numeric characters or less, cannot begin
                                                               						with a numeric character, and cannot be a reserved name such as local or sddsn. |
| Step 5 | Click OK . |

| Note | The
                                                               						Instance OU name must be five alpha-numeric characters or less, cannot begin
                                                               						with a numeric character, and cannot be a reserved name such as local or sddsn. |
|---|---|

| Step 1 | Open the Domain
                                          			 Manager. |
|---|---|
| Step 2 | In the tree view
                                          			 in the left pane, navigate down the tree to find and select the Instance OU you
                                          			 want to delete. |
| Step 3 | In the right
                                          			 pane, under Instance, click Remove . You are prompted
                                             				to confirm the removal. Warning This Unified ICM instance will no longer work properly if the OU is removed. All users, groups, and other objects in this
                                                         OU will also be deleted. | Warning | This Unified ICM instance will no longer work properly if the OU is removed. All users, groups, and other objects in this
                                                         OU will also be deleted. |
| Warning | This Unified ICM instance will no longer work properly if the OU is removed. All users, groups, and other objects in this
                                                         OU will also be deleted. |
| Step 4 | Click OK to confirm the removal. |

| Warning | This Unified ICM instance will no longer work properly if the OU is removed. All users, groups, and other objects in this
                                                         OU will also be deleted. |
|---|---|

| Property | Description |
|---|---|
| Groups | Displays
                                          					 groups that are members of the security group selected in the Domain Manager
                                          					 main dialog box |
| Users | Displays the
                                          					 name and user login name of the user. |
| Add | Use this
                                          					 option to add members to the Security Group. |
| Remove | Use this
                                          					 option to remove members from the Security Group. |
| OK | Use this
                                          					 option to save changes and return to Domain Manager. |

| Step 1 | In the Domain
                                       			 Manager, select the Security Group you want to add a user to. |
|---|---|
| Step 2 | Click Member in the Security Group pane of the ICM Domain
                                       			 Manager. The Security
                                          				Group dialog box appears. Figure 7. Security
                                             				  Group Members Dialog Box |
| Step 3 | In the Users
                                       			 pane, select Add . The Add Members
                                          				to Security Group dialog box appears. Figure 8. Add
                                             				  Members to Security Group Dialog Box |
| Step 4 | Select the
                                       			 filters that are used to create a list of users to select from. Domain – Select
                                                					 the domain you want to add as a member to the Security Group. Optional filter Select the
                                                					 optional filter you want to use: <None> – No additional filter selections
                                                      						  applied, Condition and Value inaccessible. Name – Continue and search the appropriate Condition
                                                      						  and Value. This filter is based on the username of the user. User Login Name – Continue and search the
                                                      						  appropriate Condition and Value. This filter is based on the username of the
                                                      						  user. Condition Select the
                                                					 condition to facilitate your search for the member you want to list: Contains – find and list members containing the
                                                      						  entered Value. Starts with – find and list members whose name or
                                                      						  user login name starts with the entered Value. Ends with – find and list members whose name or user
                                                      						  logon name ends with the entered Value. Value Enter the
                                                					 appropriate value to search on, for example, enter the first name of the user
                                                					 you want to add. This value provides a list of members with that name for you
                                                					 to choose from. |
| Step 5 | Select the
                                       			 member you want to add to the Security Group from the displayed list. |
| Step 6 | Click OK to add the selected member to the Security Group. |

| Step 1 | In the Domain
                                       			 Manager, select the Security Group from which you want to remove members. |
|---|---|
| Step 2 | In the Security
                                       			 Group pane of the Domain Manager dialog box, select Members . The Security
                                          				Group dialog box appears. |
| Step 3 | In the Users
                                       			 pane, select the member you want to remove from the Security Group. |
| Step 4 | Click Remove . |
| Step 5 | Click OK to remove the selected member from the Security
                                       			 Group. |

| Property | Description |
|---|---|
| Validation
                                          					 error for organizational unit: | Displays the
                                          					 OU containing the error found during OU validation. |
| Error | Displays
                                          					 description of errors found during OU validation. |
| Location | Displays the
                                          					 location of each error found during OU validation. |
| Do you want
                                          					 to fix the errors? | Four
                                          					 possible responses: Yes – Fixes the displayed
                                                						  error then attempts to sequentially validate the next OU. If more errors are
                                                						  found, you return to this dialog box. Yes to All – Recursively
                                                						  fixes the displayed error and any errors found during sequential validation
                                                						  attempts for other ICM OUs without returning to this dialog box. No – Does not fix the
                                                						  displayed error but attempts to sequentially validate the next OU. If more
                                                						  errors are found, you return to this dialog box. No to All – Does not fix
                                                						  the displayed error but recursively validates the OUs and logs any additional
                                                						  errors without returning you to this dialog box. |