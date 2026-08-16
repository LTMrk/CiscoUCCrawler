---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su3-maintain-and-operate-guid-93dd829d9f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su3/maintain_and_operate/guide/uccx_b_1251su3_admin-and-operations-guide/uccx_b_12_5_2admin-and-operations-guide_chapter_01000.html
retrieved_at: 2026-08-16T21:33:29.873293+00:00
---

Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1) SU3

# Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1) SU3

Updated: May 8, 2023

Chapter: Provision of Unified CCX

## Chapter: Provision of Unified CCX

# Provision of Unified CCX

To provision
                        		the Unified CCX subsystem, you must provision your telephony and media
                        		resources (see the Provision Telephony and Media Resources ).

Attention

Do not edit
                                       			 users, teams and permissions in Unified Intelligence Center. The Unified CCX to
                                       			 Unified Intelligence Center sync runs as part of daily purge and synchronizes
                                       			 these settings on Unified Intelligence Center according to Unified CCX
                                       			 settings.

The following topics
                        		introduce the Unified CCX subsystem and explain how to provision it in the
                        		Unified CCX system:

## RmCm Provider
                        	 Configuration

The Unified CCX Resource Manager (RM) uses a Unified CM Telephony user (called the RmCm Provider) to monitor agent phones, control agent states, and route and queue calls. For information
                           on adding Unified CM users, see section "Access Control Group Overview" section in the Cisco Unified
                                    				  Communications Manager Administration Guide available here:

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

The RmCm user
                                       		  specified through Unified CCX Administration is updated automatically in Unified CM .

### RmCm Provider
                           	 Modification

This section only
                                             			 applies to Unified CCX deployments with Unified CM.

Caution

While Unified CM supports Unicode characters in first and last
                                             			 names, those characters become corrupted in Unified CCX Administration web
                                             			 pages for RmCm configuration and real-time reporting 
                                             			 .

The RmCm
                                 		  Provider web page is a read-only page that displays the latest configured
                                 		  information. To access this configuration area, choose Subsystems > RmCm > RmCm
                                       				Provider from the Unified CCX Administration menu
                                 		  bar. The RmCm Provider web page opens, displaying the following read-only
                                 		  fields.

Field

Description

Primary
                                             						RmCm Provider

The hostname or IP address of the server, running CTI Manager ( Unified CM that runs CTI Manager).

The RmCm
                                             						subsystem registers with the CTI Manager so that it can observe an agent's
                                             						device when the agent logs in. When the CTI Manager fails, the RmCm subsystem
                                             						registers with the second CTI Manager, if there is one configured.

Secondary
                                             						RmCm Provider

The hostname or IP address of the secondary RmCm Provider.

User ID

The RmCm
                                             						user ID.

To modify
                                 		  the RmCm Provider, click Modify
                                    			 RmCm Provider Information icon in the tool bar in the upper, left
                                 		  corner of the window. The Cisco Unified CM Configuration web page opens.

### Associating Agent Extensions with the RmCm Provider

This section only applies to Unified CCX Deployments with Unified
                                             			 CM.

For every agent/resource created in Unified CM , make sure that the agent phone is also associated with the RmCm Provider. You do this from the Unified CM User Page for the RmCm Provider. In other words, even though you create the RmCm User in Unified CCX Administration, you still need to use the Unified CM interface to associate the RmCm user with an agent phone. These phones are the same as those associated with each agent.

If you use Extension Mobility (EM), ensure that the IPCC extension is associated with the Extension Mobility (EM) User Device
                                             Profile (UDP) and not to the physical phone. The Extension Mobility (EM) profile needs to be associated with the RmCm user
                                             and the physical phones that the agents may be expected to use should not be associated to the RmCm user.

## Resource Groups

Resource groups are collections of agents that your CSQ uses to
                           		handle incoming calls. To use resource group-based CSQs, you must specify a
                           		resource group.

### Create Resource Group

To create a resource group, complete the following steps.

Step 1

From the Unified CCXAdministration menu bar, choose Subsystems > RmCm > Resource
                                                				  Groups .

The Resource Group web page opens with a list of configured
                                             				resource groups (if any).

Step 2

Click Add New icon in the tool bar in the upper,
                                          			 left corner of the window or Add New button at the bottom of the window.

The Resource Group Configuration area opens.

Step 3

In the Resource Group Name field, enter a resource group name.

Enter a name that identifies the resource group to which you want
                                             				to assign agents (for example, "Languages" ).

Step 4

Click Add .

The Resource Groups page opens displaying the resource group name
                                             				in the Resource Group Name column.

### Modify Resource Group Name

To modify a resource group name, complete the following
                                 		  steps.

Step 1

From the Unified CCXAdministration menu bar, choose Subsystems > RmCm > Resource
                                                				  Groups .

The Resource Group web page opens.

Step 2

In the Resource Group Name column, click the resource group that
                                          			 you want to modify.

The Resource Group Configuration area opens.

Step 3

Type the name of the resource group in the Resource Group Name
                                          			 text field.

Step 4

Click Update to apply the modifications.

The Resource Groups area opens, displaying the modified resource
                                             				group name in the Resource Group Name column.

### Delete Resource Group

When you delete a resource group, the resource group is
                                 		  removed automatically if it is not associated with any agents and CSQs. If the
                                 		  resource group is associated with any agents or CSQs and if you click Delete , you will be directed to another web
                                 		  page, where you can see a list of the associated CSQs and agents, and you are
                                 		  prompted to confirm whether you want to delete the same.

Tip

To delete resource groups, you can use the following procedure or
                                             			 open a Resource Group and click 
                                             			 the Delete icon or button in the Resource Group
                                             			 Configuration web page.

To delete a resource group, complete the following steps.

Step 1

From the Unified CCXAdministration menu bar, choose Subsystems > RmCm > Resource
                                                				  Groups .

The Resource Group web page opens.

Step 2

Click Delete icon next to the name of the Resource
                                          			 Group that you want to delete.

A dialog box opens, warning that the resource group is about to be
                                             				permanently deleted.

Step 3

Click Continue .

The resource group is deleted.

## Skills Configuration

Skills are customer-definable labels assigned to agents. All
                           		the Unified CCX license packages can route incoming calls to agents who have
                           		the necessary skill or sets of skill to handle the call.

### Create a Skill

To create a skill, complete the following steps.

Step 1

From the Unified CCXAdministration menu bar, choose Subsystems > RmCm > Skills .

The Skills web page opens to display the Skill Name
                                             				(customer-definable label assigned to an agent), if configured.

Step 2

Click Add New icon in the tool bar in the upper,
                                          			 left corner of the window or Add New button at the bottom of the window.

When the system reaches the maximum number of skills that can be
                                                         				  created, the Add New icon or button no longer appears.

The Skill Configuration web page opens.

Step 3

In the Skill Name field, enter a description of a relevant skill
                                          			 (for example, French).

Unified CCX does not support the following special characters for Skill name.

Symbol

Description

Symbol

Description

`

apostrophe

~

tilde

!

exclamation mark

@

at sign

$

dollar

%

percent

^

circumflex

&

ampersand

*

asterix

()

parentheses

=

equals sign

[]

square brackets

braces

;

semicolon

\

backslash

?

question mark

"

double quotes

<>

angle brackets

'

single quote

+

add

|

pipe

:

colon

.

period

/

forward slash

,

comma

#

hash

Step 4

Click Add .

The Skills web page opens, showing the skill in the Skill Name
                                             				column and the total number of skills that exist in the system. You can add a
                                             				maximum of 150 skills.

### Modify a Skill Name

To modify a skill name, complete the following steps.

Step 1

From the Unified CCXAdministration menu bar, choose Subsystems > RmCm > Skills .

The Skills web page opens.

Step 2

In the Skill Name column, click the skill that you want to modify.

The Skill Configuration web page opens.

Step 3

Modify the name of the skill in the Skill Name text field.

Unified CCX does not support special characters for the skill name. To see the list of unsupported characters, see Table 1 .

If you have upgraded to Unified CCX Release 12.5(1) and above and are facing errors when making changes to the Skill name,
                                                         remove the special characters and modify the skill name.

Step 4

Click Update to apply the modifications.

The Skills Configuration summary opens, displaying the modified
                                             				skill name in the Skill Name column.

### Delete a Skill

When you delete a skill, the skill is removed automatically
                                 		  if it is not associated with any agents and CSQs. If the skill is associated
                                 		  with any agents or CSQs and if you click Delete , you are directed to another web
                                 		  page, where you can see a list of the associated CSQs and agents, and you are
                                 		  prompted to confirm whether you want to delete the same.

Tip

To delete a  skill, you can use the following procedure or open a
                                             			 skill and click Delete icon or button in the Skills
                                             			 Configuration web page.

To delete a skill, complete the following steps.

Step 1

From the Unified CCXAdministration menu bar, choose Subsystems > RmCm > Skills .

The Skills web page opens.

Step 2

Click  
                                          			 the Delete icon next to the name of the skill that
                                          			 you want to delete.

A dialog box opens, warning that the skill is about to be
                                             				permanently deleted.

Step 3

Click Continue .

The skill is deleted.

## Agent
                        	 Configuration

You can add skills to agents once the skills have been created. You can also select the competence level of agents in assigned
                           skills. Competence level indicates agent level of expertise in that skill.

You can
                           		assign resource groups and skills to agents either individually or in bulk. The
                           		bulk option enables you to assign skills and resource groups to multiple agents
                           		at the same time.

Once you
                           		assign agents to resource groups and skills, you can create a CSQ.

Warning

After an agent is added, wait for 10 minutes for Unified CCX to automatically synchronize or force synchronization before
                                       the agent can sign in to Cisco Finesse.

The maximum allowed length of an agent's IPCC Extension is 15.

### Special
                              		  Characters

Unified CM supports the use of special characters—square brackets ([ ]), dollar ($), ampersand (&), single quotes (' '),
                                    colon (:), angle brackets( < >), forward slash (/), question mark ( ?), backward slash ( \), parentheses ({ }), double quotes("
                                    "), hash(#), percent (%), semicolon ( ;), comma ( ,), pipe ( |), tilde( ~) and space in a user ID when you configure end users.
                                    However, Unified CCX restricts the use of these characters when you configure end users as agents or supervisors.

Unified CCX does not support the use of special characters—square brackets ([ ]), dollar ($), ampersand (&), single quotes
                                    (' '), colon (:), angle brackets( < >), forward slash (/), question mark ( ?), backward slash ( \), parentheses ({ }), double
                                    quotes(" "), hash(#), percent (%), semicolon ( ;), comma ( ,), pipe ( |), tilde( ~), period (.).

With Cisco Finesse for Unified CCX, agent IDs (or usernames) are case-sensitive and can contain letters, numbers, hyphens
                                    (-), underscores (_), at (@), and periods (.) They cannot begin or end with a period or contain two periods in a row. Finesse agent usernames are restricted
                                    to 7-bit printable ASCII characters (any of the 94 characters with the numeric values from 33 to 126). They do not support
                                    double quotes (" "), forward slash (/), backward slash (\), square brackets ([ ]), colon (:), semicolon (;), pipe (|), equal
                                    to (=), comma (,), add (+), star (*), question mark (?), angle brackets (< >), hash (#), percent (%), SPACE and the characters
                                    restricted by Unified Communications Manager and Unified CCX.

Finesse agent passwords are restricted to 7-bit printable ASCII characters (any of the 94 characters with the numeric values
                                    from 32 to 126). They do not support control characters (for example, Tab) or international characters.

Agent Alias name now supports the use of SPACE in the name.

### Implications of
                           	 Deleting Agents in Unified CM

If you modify an agent's
                              		record in Unified CM (for example, changing the Unified CCX
                              		extension or deleting the agent), ensure to refresh the user page on Unified
                              		CCX Administration interface so that the agent information in the Unified CCX
                              		RmCm subsystem is updated. Choose Subsystems > RmCm > Resources option to update the Unified
                              		CCX information in the Unified CCXAdministration any time. If you change the
                              		Unified CCX extension of an agent who is currently logged in, the agent will
                              		continue to use the old extension until the agent logs off. The agent must log
                              		off and then log back in to the Cisco Finesse desktop to get the new extension.
                              		When Unified CCX performs an agent sync and detects that the agent no longer
                              		exists in Unified CM , the contact is
                              		marked as inactive in the Resource table of the Unified CCX Historical Reporting Database
                              		(db_cra). The resource is not deleted as the resource information is referenced
                              		for the HR reports.

Caution

Deleting Inactive
                                          		  Agents removes the agent details and records from the Historical Reporting
                                          		  Database, and HR reports will not display historical information of these
                                          		  agents.

If Unified CM connection errors have occurred, all agents will not be visible to Unified CCX.
                                          		  In this case, Unified CCX interprets these agents as deleted agents. As a
                                          		  result, the Inactive Agents list will not be accurate. When the errors are
                                          		  resolved, click Inactive
                                             			 Agents again to see an accurate list.

### Assign Resource
                           	 Groups and Skills to One Agent

To assign
                                 		  a resource group and skills to an individual agent, complete the following
                                 		  steps.

Step 1

From the Unified
                                          			 CCXAdministration menu bar, choose Subsystems > RmCm > Resources .

The Resources
                                             				web page opens.

Only agents or
                                                         				  supervisors who have assigned Unified CCX extensions are displayed in the list
                                                         				  of resources in the Resources area.

Step 2

Click the name
                                          			 of the agent in the Resource Name column.

The Resource
                                             				Configuration web page opens.

Step 3

Specify the
                                          			 following fields.

Field

Description

Resource Name

Name
                                                         							 of the agent (display only).

Resource ID

Unique
                                                         							 identifying number of the agent (display only). This is the alpha-numeric user
                                                         							 id assigned in the Unified CM End User
                                                         							 Configuration page.

Unified CCX Extension

Unified CCX Extension assigned to the resource group (display
                                                         							 only). This is the IP Phone extension assigned to the user from the Unified CM End User
                                                         							 Configuration page as IPCC Extension.

Resource Group

A
                                                         							 resource group with which to associate the agent (optional).

Automatic Available

Accept
                                                         							 the default ( Enabled )
                                                         							 to automatically put the agent into the Available or Ready state after the
                                                         							 agent finishes a call and disconnects.

When
                                                                     								a logged on agent in Ready, Not Ready, or Work state answers a call, the agent
                                                                     								state is subject to the Automatic Available setting.

Assigned/Unassigned Skills

Select
                                                         							 one or more skills from the Unassigned Skills list and click < to add the
                                                         							 skills to the Assigned Skills List.

Select
                                                         							 one or more skills from the Assigned Skills List and click > to remove
                                                         							 skills from the Unassigned Skills list.

You
                                                         							 can assign up to 50 skills to the agent.

Competence Level

Select
                                                         							 a skill from the Assigned Skills list and choose a number from the Competence
                                                         							 Level drop-down menu

Changes the competence level of an assigned skill (1 = Beginner,
                                                         							 10 = Expert).

You
                                                                     								can change the competency level one skill at a time, only. You cannot change
                                                                     								skill competency level as a bulk procedure.

Team

A
                                                         							 group of agents who assign the team to which the resource belongs.

Agent Alias

Agent alias is the name used instead of the agent ID
                                                         							 when an agent chats with a customer. This option is available only when Finesse
                                                         							 is used by the chat agent.

Step 4

Click Update to apply the changes.

The Resources
                                             				area of the RmCm Configuration summary web page opens, and the agent is now
                                             				assigned to the resource group and skills (if skills were assigned).

### Assign Resource Groups and Skills to Multiple Agents

To assign resource groups and skills to agents in bulk,
                                 		  complete the following steps.

Step 1

From the Unified CCXAdministration menu bar, select Subsystems > RmCm > Assign
                                                				  Skills .

The Assign Skills summary web page opens.

Tip

Only agents or supervisors who have assigned Unified CCX
                                                         				  extensions are displayed in the list of resources in the Resources area.

Step 2

In the Resource Name column, check the check box beside each agent
                                          			 to whom you want to assign set of same resource group and skills. In the
                                          			 Resource Name column, check the check box next to each agent you want to assign
                                          			 set of same resource group and skills.

You can check the Select All check box to select all agents.

The Skill summary web page shows the total number of skills
                                             				created.

Step 3

Click Add Skill icon that displays in the tool bar
                                          			 in the upper, left corner of the window or the Add Skill button that displays at the bottom
                                          			 of the window.

The Add Skill web page opens.

Step 4

Specify the following fields.

Field

Description

Resource Group

To assign a resource group to all the selected agents,
                                                         							 choose a resource group from the Resource Group drop-down menu.

Skills to Add

Select one or more skills from the Skills list and click
                                                         							 < to add the skills to the Skills to Add List.

The Skills to Add list contains all skills, not just
                                                                     								the skills that agents already have.

Skills

List of the available skills.

Competence Level

Select a skill from the Assigned Skills list and
                                                         							 choosing a number from the Competence Level drop-down menu

Step 5

Click Update to apply the changes.

The Assign Skills area of the RmCm Configuration web page opens,
                                             				and the agents are now assigned to the resource group and their skills (if skills
                                             				were assigned).

### Remove Skills from Agents

If a resource is not assigned a skill that you attempt to remove, the
                                             			 resource is not updated. However, the system will still generate a related
                                             			 message.

To remove skills from agents, complete the following steps.

Step 1

From the Unified CCXAdministration menu bar, choose Subsystems > RmCm > Assign
                                                				  Skills .

The Assign Skill summary web page opens.

Step 2

In the Resource Name column, click the check box next to the agent
                                          			 you want to remove skills from.

You can click Select All check box to select all agents.

Step 3

Click Remove Skill icon that displays in the tool
                                          			 bar in the upper, left corner of the window or the Remove Skill button that displays at the
                                          			 bottom of the window.

The Remove Skill Configuration web page opens.

Step 4

Remove skills by choosing one or more skills from the Skills list
                                          			 and clicking > to move the skills to the Skills to Remove list.

Step 5

Click Update to apply the changes.

The Assign Skills area of the RmCm Configuration web page opens,
                                             				and the agents are no longer assigned to the skills.

## Contact Service Queue Configuration

The Contact Service Queue (CSQ) controls incoming calls by
                           		determining where an incoming call should be placed in the queue and to which
                           		agent the call is sent.

After you assign an agent to a resource group and assign skills, you
                           		need to configure the CSQs.

You assign agents to a CSQ by associating a resource group or
                           		by associating all skills of a particular CSQ. Agents in the selected resource
                           		group or who have all the selected skills are assigned to the CSQ.

Skills within the CSQ can be ordered . This means, when resources are selected, a comparison is
                           		done based on the competency level (highest for "most skilled" and lowest for "least skilled" ) of the first skill in the list. If there is a "tie" the next skill within the order is used, and so on.

Skills within the CSQ can also be weighted . The weight value is an integer from 1 to 1000. Each
                           		competency level is multiplied by the skill's associated weight, and a final
                           		comparison is done on the sum of all the weighted skill competencies (highest
                           		value for "most skilled" and lowest for "least skilled" ).
                           	 The maximum number of CSQs in the system depends on the type
                           		of server on which the engine is running.

For more information, see the Unified CCX Data Sheets at https://www.cisco.com/c/en/us/products/contact-center/unified-contact-center-express/datasheet-listing.html

Each agent can belong to up to 25 CSQs. To ensure that agents
                           		are not assigned to more than 25 CSQs, click Resources submenu option in the RmCm Configuration
                           		web page, and click Open Resources Summary Report icon. The report
                           		opens, listing each agent and the number of CSQs to which the agent belongs. If
                           		the agent belongs to more than 25 CSQs, modify the skills and resource groups
                           		to which the agent is assigned so that the agent does not belong to more than
                           		25 CSQs.

### Create a Contact
                           	 Service Queue

To create
                                 		  a new CSQ and assign agents, complete the following steps.

Step 1

From the Unified
                                          			 CCXAdministration menu bar, choose Subsystems > RmCm > Contact Service
                                                				  Queues .

The Contact
                                             				Service Queues web page opens.

Field

Description

Name

Name
                                                            							 of the resource or skill group.

Contact Queuing Criteria

Algorithm used to order the queued calls (contacts).

Resource Pool Selection Model

The
                                                            							 resource selection criteria chosen for this CSQ.

Resource Pool

The
                                                            							 skills or resource group used for this CSQ.

CSQ
                                                            							 Type

The
                                                            							 type of the CSQ.

Delete

Deletes the selected CSQ.

Step 2

Click Add
                                             				New icon that displays in the tool bar in the upper, left corner of
                                          			 the window or the Add
                                             				New button that displays at the bottom of the window.

The Contact
                                             				Service Queue Configuration web page opens.

If this link
                                                         				  does not appear on the page, it means that the system has reached the maximum
                                                         				  number of CSQs that can be created. The CSQ Summary page displays the total
                                                         				  number of created CSQs.

Step 3

Use the Contact
                                          			 Service Queue Configuration web page to specify the various fields. For more
                                          			 information on the fields, see Contact Service Queue Configuration Web Page .

Step 4

Click Next .

The second
                                             				Contact Service Queue Configuration area opens with the newly-assigned CSQ
                                             				Name.

Step 5

Select an option
                                          			 from the Resource Selection Criteria drop-down menu.

The Resource
                                                         				  Pool Selection Model settings determine the options available in this drop-down
                                                         				  menu.

Longest
                                                      						Available —Selects the agent who has been in the Available state for
                                                   					 the longest amount of time.

Most Handled
                                                      						Contacts —Selects the agent who has handled the most calls.

Shortest Average Handle
                                                      						Time —Selects the agent who generally spends the least amount of
                                                   					 time talking to customers.

Most Skilled —Used
                                                   					 for expert agent call distribution. Selects the agent with the highest total
                                                   					 competency level. The total competency level is determined by adding the
                                                   					 agent's competency levels for each of their assigned skills that are also
                                                   					 assigned to the CSQ.

Example
                                                         						  1: If Agent1 is assigned Skill1(5), Skill2(6), and Skill3(7) and CSQ1 specifies
                                                         						  Skill1(min=1) and Skill3(min=1), the total competency level for Agent1 for CSQ1
                                                         						  is 12.

Example
                                                         						  2: If Agent1 is assigned Skill1(5) and Skill2(6) and Skill3(7) and CSQ1
                                                         						  specifies Skill1(min=1), only, the total competency level for Agent1 for CSQ1
                                                         						  is 5.

Least
                                                      						Skilled —Used for expert agent call distribution. Selects the agent
                                                   					 with the lowest total competency level. The total competency level is
                                                   					 determined by adding the agent’s competency level in each assigned skill.

Most Skilled by
                                                      						Weight — Used for expert agent call distribution. Selects the agent
                                                   					 with the highest total competency level multiplied by the skill’s associated
                                                   					 weight.

Least Skilled by
                                                      						Weight —Used for expert agent call distribution. Selects the agent
                                                   					 with the lowest total competency level multiplied by the skill’s associated
                                                   					 weight.

Most Skilled by
                                                      						Order — Used for expert agent call distribution. Selects the agent
                                                   					 with the highest total competency level in the ordered list.

Least Skilled by
                                                      						Order — Used for expert agent call distribution. Selects the agent
                                                   					 with the lowest total competency level in the ordered list.

Step 6

Specify the
                                          			 following settings, as necessary:

The Resource
                                                         				  Pool Selection Model setting determines the availability of these options.

Use the
                                                				  Select Skills list to highlight the skills you want; click the Add button next to the list.

Specify a
                                                				  Minimum Competence Level for the skills assigned to the CSQ. Depending on the
                                                				  Resource pool criteria you chose, specify a Weight value between 1 and 1000.

If the
                                                				  Resource Selection Criteria is Most Skilled by Order or Least Skilled by Order,
                                                				  use the arrow icons to order the skills by moving them up or down in the list.

Use the Delete icon next to a skill to delete that skill
                                                               						from the Skills Required list.

Step 7

If you
                                          			 selected one of the Least/Most Skilled options as shown in the list below for
                                          			 the Resource Selection Criteria, you can view the agent order using Show
                                             				Resources icon or button.

The order of
                                                         				  the agents determines the priority, with the agent at the top of the list
                                                         				  having the highest priority.

To change the
                                             				order of the agents belonging to the CSQ, you should modify the skill set of
                                             				the agents. The Least/Most Skilled Resource Selection Criteria option comprises
                                             				the following:

Most
                                                				  Skilled

Least
                                                				  Skilled

Most
                                                				  Skilled by Order

Least
                                                				  Skilled by Order

Most
                                                				  Skilled by Weight

Least
                                                				  Skilled by Weight

Step 8

If you
                                          			 selected Resource
                                             				Groups as the Resource Pool Selection Model on the previous page, follow
                                          			 these steps:

Select an
                                                				  option from the Resource Selection Criteria drop-down menu.

Longest Available —Selects the agent who has been in
                                                            						  the Available state for the longest amount of time.

Linear —Selects the next available agent with the
                                                            						  highest priority, as determined by the agent order in the Resources list.

Circular —Selects the next available agent with the
                                                            						  highest priority, based on the last agent selected and the agent order in the
                                                            						  Resources list.

Most Handled Contacts —Selects the agent who has
                                                            						  handled the most calls.

Shortest Average Handle Time —Selects the agent who
                                                            						  generally spends the least amount of time talking to customers.

Choose the
                                                				  resource group for this CSQ from the Resource Group drop-down menu.

Click Show Resources icon to show all agents who meet the
                                                				  specified criteria.

If you
                                                				  selected Linear or Circular as the Resource Selection Criteria, if necessary,
                                                				  rearrange the order of agents in the Resources list by highlighting an agent
                                                				  and using the up and down arrows to move the agent in the list.

Click Add to apply changes and update the system.

The new
                                                   					 CSQ is now displayed, and all agents who belong to the resource group or all
                                                   					 selected skill groups are now a part of this CSQ.

#### Contact Service
                              	 Queue Configuration Web Page

Contact Service
                                    		  Queue Configuration web page:

Field

Description

Contact
                                                						Service Queue Name

Enter a
                                                						meaningful name that is concise, yet easy to recognize (for example, Language
                                                						Experts). This is a mandatory field.

Unified CCX does not support special characters for the Call Service Queue name. To see the list of unsupported characters,
                                                            see Table 1 .

Contact
                                                						Service Queue Type

Display only. Voice—Agents
                                                						in this CSQ can handle inbound and outbound voice calls.

Contact
                                                						Queuing Criteria

Display
                                                						only. Displays the criteria used for queuing the contacts. For example, First
                                                						In, First Out (FIFO).

Determines whether agents handling calls that are routed through this CSQ automatically enter the Wrapup state when a call ends. This field is mandatory. Options are:

Enabled—Agents associated to a CSQ that has the Automatic Wrapup option enabled, enter the Wrapup state automatically when on a call. CSQ ends. If agents are associated to a CSQ that has the Automatic Wrapup option disabled handle transferred calls that were originally delivered by a CSQ that has Automatic Wrapup enabled, they also enter the Wrapup state automatically when a call ends.

Disabled (default)—Agents enter Ready or Not Ready state when a
                                                      							 call ends, depending on the Automatic Available setting.

Wrapup
                                                						Time

Determines the length of the Wrapup state for this CSQ when a call ends. Options are:

Enabled button with Seconds field—The Seconds field specifies the length of the Wrapup state phase.

Disabled—No limit on how long the agent can stay in the Wrapup state.

Resource
                                                						Pool Selection Model

Select
                                                						one of the following options from the drop-down menu:

Resource Skills—To create a skills-based CSQ.

Resource Group—To create a resource group-based CSQ.

This is
                                                						a mandatory field.

Service
                                                						Level

The
                                                						target maximum number of seconds a call is queued before it is connected to an
                                                						agent. This is a mandatory field.

Service
                                                						Level Percentage

The
                                                						target goal for percentage of contacts that meet the service level. This is a
                                                						mandatory field.

For
                                                						example, a call center that has a service level of 20 and a service level
                                                						percentage of 80 percent has a goal of answering 80 percent of its calls within
                                                						20 seconds.

Prompt

.wav
                                                						prompt file to associate with the CSQ. You can retrieve the prompt file that
                                                						you select from this Prompt drop-down list using the Create CSQ Prompt Step in
                                                						the Unified CCX Editor.

In the Unified CCX Editor, Create CSQ Prompt Step is one of the steps used to create scripts for the Unified CCX engine. In
                                                this step, you need to give the CSQ ID that is displayed as the last number in the AppAdmin address bar of the web page that
                                                is displayed when you click on an existing CSQ. For example, the CSQ ID will be 3 if the address bar of an existing CSQ Configuration
                                                web page ends with "&csdid=3" . When you run the script, it will return the prompt associated with the specific CSQ ID. Use the Play Prompt Step within
                                                the script to play this prompt.

See the Cisco Unified CCX Editor Step Reference Guide for
                                                						detailed information on scripting.

The
                                                            						  Prompt field is available only if you have licensed the Cisco Unified CCX
                                                            						  Enhanced or Premium product package.

### Modify a Contact
                           	 Service Queue

Changes take
                                             			 effect when all agents affected by the changes have left the Ready state. Emails Contact
                                                				Service Queues cannot be modified. It is for display only.

To modify
                                 		  an existing CSQ, complete the following steps.

Step 1

From the Unified
                                          			 CCXAdministration menu bar, choose Subsystems > RmCm > Contact Service
                                                				  Queues .

The Contact
                                             				Service Queues web page opens.

Step 2

In the Name
                                          			 list, click the CSQ that you want to modify.

The Contact
                                             				Service Queue Configuration page opens.

Step 3

Modify the
                                          			 Contact Service Queue Configuration information as necessary.

If you change
                                                         				  an existing CSQ name, the old name still exists in the HR reports and the CSQ
                                                         				  is not removed even if all the data is purged.

Step 4

Click Next icon that displays in the tool bar in the upper, left corner of the window or the Next button that displays at the bottom of the window to view and update the remaining fields.

Step 5

Click Update icon in the top of the window or the Update button that displays at the bottom of the
                                          			 window to apply the modifications.

Ensure that the Resource Selection Criteria is changed only when there are no agents signed in. If there are active agents, these changes take effect only when all the
                                                         active agents sign out and sign in again.

### Delete a Contact
                           	 Service Queue

When you
                                 		  delete a CSQ, any skills or resource groups assigned to that CSQ are
                                 		  automatically removed from the CSQ, and any application using that CSQ can no
                                 		  longer access it. Before deleting the CSQ, change the applications to use a
                                 		  different CSQ. If the application is using a CSQ when the CSQ is deleted, new
                                 		  incoming calls will get an error and existing queued calls will not be routed
                                 		  to agents.

Existing Email Contact Service Queues can be deleted.

To delete
                                 		  a CSQ, complete the following steps.

Step 1

From the Unified
                                          			 CCXAdministration menu bar, choose Subsystems > RmCm > Contact Service
                                                				  Queues .

The Contact
                                             				Service Queues web page opens.

Step 2

Click the Delete icon next to the name of the CSQ that you
                                          			 want to delete.

You can also
                                                         				  delete a CSQ from its Contact Service Queue Configuration page using the Delete
                                                         				  icon or button.

### Resource Pool Selection Criteria: Skills and Groups

The resource selection criteria available for CSQs with
                                 		  Resource Skills is different from that of CSQs with Resource Groups .

Example—In a banking application with two skills (Banking
                                 		  and CreditCard) and one Resource Group (General Queries), assume that the
                                 		  following agents, skills, and resource groups are defined:

Agent ID

Assigned Skills

Resource Group

Agent1

Banking (Competence Level 10)

CreditCard (Competence Level 6)

GeneralQueries

Agent2

Banking (Competence Level 5)

CreditCard (Competence Level 10)

GeneralQueries

Agent3

None

GeneralQueries

In addition, suppose you had the following Contact Service
                                 		  Queue information defined:

CSQ Name

Resource Pool Selection Model

Resource Selection Criteria

Skill/Competence

Available Agents

CSQ1

Resource Skills

Most Skilled

BankingMinimum competency: 5

Agent1

Agent2

CSQ2

Resource Skills

Most Skilled

CreditCardMinimum competency: 5

Agent1

Agent2

CSQ3

Resource Group

Longest Available

GeneralQueries

Agent1

Agent2

Agent3

In this scenario, if a caller calls with a question about
                                 		  CreditCard information and there are no CSQs currently available with
                                 		  CreditCard skills (that is, Agent1 and Agent2), there is a possibility for
                                 		  Agent3—who has no CreditCard skill—to get selected as the Longest Available
                                 		  Agent.

To avoid such a situation, you could design the script to
                                 		  always look into CSQ2 for available agents since it has the highest competency
                                 		  of 10 for CreditCard, and agent selection here is based on most skilled.

If two or more agents have equal competency level, the
                                             			 selection automatically defaults to Longest Available selection criteria.

### Resource Skill Selection Criteria within a Contact Service Queue

Resource selection within a CSQ is based on the resource competency levels of the
                                 		  skills associated to the CSQ. You can choose between the most and least
                                 		  skilled.

The Unified CCX system defines a Level 10 competency to be
                                 		  the highest skill level, while a Level 1 denotes the lowest skill level. When
                                 		  more than one skill is involved, each skill is given the same weight, meaning
                                 		  no preference is given to any skill. A comparison is performed on the sum of
                                 		  all the competency levels for the associated skills. (Skills assigned to
                                 		  resources but not associated to the CSQ are ignored.) In the case of a tie when
                                 		  skill competencies are equal, the resource that has been ready for the longest
                                 		  amount of time will be chosen.

The following table provides examples of how Unified CCX
                                 		  selects resources within a CSQ.

Example

CSQ Skills

Agent Competency Levels

Sequence Agents Become Ready

Selection Order

Most skilled resource selection model

Technical Support

Agent A = 10

Agent B = 10

Agent C = 5

A, B C

A, B, C

C, A, B

A, B, C

A, C, B

A, B, C

C, B, A

B, A, C

Least skilled resource selection model

Technical Support

Agent A = 10

Agent B = 10

Agent C = 5

A, B, C

C, A, B

C, A, B

C, A, B

A, C, B

C, A, B

C, B, A

C, B, A

The ordering in the two examples above are not opposite
                                                         						because the selection criteria has changed from most to least skilled—when
                                                         						competency levels are equal, both selection models choose the resources that
                                                         						have been available for the longest time.

Most skilled resource selection model

SalesSupport

Agent A = Sales (10) Support (5)

Agent B = Sales (5), Support (10)

Agent C = Sales (5) Support (1)

A, B, C

A, B, C

C, A, B

A, B, C

A, C, B

A, B, C

C, B, A

B, A, C

Least skilled resource selection model

SalesSupport

Agent A = Sales (10) Support (5)

Agent B = Sales (5), Support (10)

Agent C = Sales (5) Support (1)

A, B, C

C, A, B

C, A, B

C, A, B

A, C, B

C, A, B

C, B, A

C, B, A

## Configure
                        	 Agent-Based Routing

Agent-based routing provides the ability to send a call to a specific agent, rather than any agent available in a CSQ.

Use the
                              		  Agent Based Routing Settings web page to configure system-wide parameters to be
                              		  used in an agent-based routing application.

Step 1

From the Unified
                                       			 CCXAdministration menu bar, choose Subsystems > RmCm > Agent Based Routing
                                             				  Settings . The Agent Based Routing Settings area
                                       			 opens.

The Agent
                                                      				  Based Routing Settings are available only if you are using Unified CCX Enhanced
                                                      				  or Premium license packages.

Step 2

Specify the
                                       			 following fields:

Field

Description

Determines whether agents handling calls that are routed through this CSQ automatically enter the Automatic Wrapup state when a call ends.

Enabled—Agents associated to a CSQ that has the Automatic Wrapup option enabled enter the Wrapup state automatically when on a call. If agents are associated to a CSQ that has the Automatic Wrapup option disabled handle transferred calls that were originally delivered by a CSQ that has Automatic Wrapup enabled, they also enter the Wrapup state automatically when a call ends.

Disabled (default)—Agents enter Ready or Not Ready state when a
                                                            								  call ends, depending on the Automatic Available setting.

Wrapup
                                                      							 Time

Determines if agents automatically enter Wrapup when a call
                                                      							 ends.

Enabled button with seconds field—Controls how long the agent can stay in the Wrapup state if Automatic Wrapup is enabled. The seconds field specifies the Wrapup time length.

Disabled (default)—No limit of how long the agent can stay in the Wrapup state if Automatic Wrapup is enabled.

Step 3

Click Save icon
                                       			 that displays in the tool bar in the upper, left corner of the window or the Save button
                                       			 that displays at the bottom of the window to apply changes.

### Wrap-Up Data
                           	 Usage

Contact
                              		centers use wrap-up data to track the frequency of activities or to identify
                              		the account to which a call is charged, and other similar situations. Like
                              		reason codes, wrap-up data descriptions are set up by your system administrator
                              		to reflect the needs of your contact center. By default this feature is
                              		disabled.

## Teams Configuration

A team is a group of agents who report to the same Supervisor. A team can have one primary Supervisor and optional secondary Supervisors.
                              A Supervisor can also monitor CSQs that are assigned to the team being supervised.

Barge-in is when a Supervisor joins an existing call between an agent and a customer.

Intercept is when the Supervisor joins a call and drops the agent from the call.

A default team is automatically created by the system and cannot be deleted. If agents are not assigned to any team, they belong to the
                              default team. When an agent is assigned to a team, the team Supervisor can barge-in and intercept any call being handled by
                              the agent.

Before creating a team, you must set up Supervisors using the User Management page.

The Advanced Supervisor Capability of Queue Management is removed when:

Supervisor is not associated to any team.

Supervisor is not the primary or secondary Supervisor of any team.

There are no CSQs assigned to the teams associated to the Supervisor.

A team that accesses Live Data reports is limited to 50 agents.

### Assign Supervisor Privilege to a User

Step 1

From the Unified CCX Administration menu, choose Tools > User Management > User View .

The User Configuration page displays the list of all users.

Step 2

Click the user to whom you want to assign supervisor capability.

The User Configuration page displays information about that user. In the Capabilities section, the left pane displays the
                                             list of assigned capabilities and the right pane displays the list of capabilities.

Step 3

Using the left arrow, assign Supervisor capability.

Step 4

Click Update to save your changes.

Agents, who have logged in must logout and login again to use supervisor specific features.

For agents with chat or email skill, who have logged in, it may take maximum of 30 mins to reflect the change.

### Create Teams

Use the Teams area of the RmCm Configuration web page to create or associate teams with various agents, CSQs, and supervisors.

Step 1

From the Unified CCXAdministration menu bar, choose Subsystems > RmCm > Teams .

Step 2

Click Add New icon that displays in the tool bar in the upper left corner of the window or the Add New button at the bottom of the window.

The Team Configuration page appears.

Step 3

Enter the Team Name .

Step 4

Select the Primary Supervisor from the drop-down list.

Step 5

(Optional) Select the secondary supervisor name from the Available Supervisors list and use the arrow icon to move it into the Secondary Supervisors list.

Step 6

(Optional) To add an agent to this team, select an agent name in the Available Resources list and use the arrow icon to move it into the Assigned Resources list.

Step 7

(Optional) Select the CSQ name in the Available CSQs list and use the arrow icon to move it into the Assigned CSQs list to add the CSQ to this team.

Step 8

In the Team Settings section, specify the following information:

Parameter Name

Parameter Value

Global Settings

Change Agent State to Not Ready when Agent Busy on Non ACD Line

Radio button that enables the agent state to change from the Ready state to the Not Ready state when the monitored Non ACD
                                                         lines are used for Incoming or Outgoing calls. The options are:

Enable—Enables the state change of the agent in the team.

Disable (default)—Disables any state change of the agent in the team.

Allow team settings to override global settings—A check box to override the global settings. The global settings is available
                                                               at System > System Parameters > Agent Settings .

When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                     Click OK to proceed or Cancel to discard the changes.

When you click OK, the team level settings override the global settings.

Displays the global settings.

Auto Answer

Enables the incoming calls to be auto answered. The options are:

Enable with Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                               the agent is in the Ready state in the Cisco Finesse desktop. A zip tone plays to alert the agent.

Enable without Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                               the agent is in the Ready state in the Cisco Finesse desktop. The zip tone does not play to alert the agent.

Disable (Default)—Auto answer is not enabled.

To configure Change Agent State to Not Ready when Agent Busy on Non ACD Line at a team level, you must install UCCX 12.5(1) SU1 ES01.

This functionality is applicable only for the agents and not for the supervisors of the team.

Step 9

Click Save to apply changes or Cancel to exit.

### Modify Teams

Use the Teams area to modify the supervisors, agents, CSQs, or auto answer configuration on an existing Team.

Step 1

From the Unified CCXAdministration menu bar, choose Subsystems > RmCm > Teams .

Step 2

Click a name in the Team Name column.

The Team Configuration page appears.

Step 3

Select the Primary Supervisor from the drop-down list.

Step 4

(Optional) Select the secondary supervisor name from the Available Supervisors list and use the arrow icon to move it into the Secondary Supervisors list.

To remove the secondary supervisor name from this team, select the supervisor name in the Secondary Supervisors list and use the arrow icon to move it into the Available Supervisors list. This supervisor now belongs to the default team.

Step 5

(Optional) Select an agent name in the Available Resources list and use the arrow icon to move it into the Assigned Resources list to add an agent to this team.

To remove an agent from this team, select an agent name in the Assigned Resources list and use the arrow icon to move it into the Available Resources list. This agent now belongs to the default team.

Step 6

(Optional) Select the CSQ name in the Available CSQs list and use the arrow icon to move it into the Assigned CSQs list to add the CSQ to this team.

To remove a CSQ from this team, select a CSQ name in the Assigned CSQs list and use the arrow icon to move it into the Available CSQs list. This CSQ now belongs to the default team.

Step 7

In the Team Settings section, specify the following information:

Parameter Name

Parameter Value

Global Settings

Change Agent State to Not Ready when Agent Busy on Non ACD Line

Radio button that enables the agent state to change from the Ready state to the Not Ready state when the monitored Non ACD
                                                         lines are used for Incoming or Outgoing calls. The options are:

Enable—Enables the state change of the agent in the team.

Disable (default)—Disables any state change of the agent in the team.

Allow team settings to override global settings—A check box to override the global settings. The global settings are available
                                                               at System > System Parameters > Agent Settings .

When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                     Click OK to proceed or Cancel to discard the changes.

When you click OK, the team level settings override the global settings.

Displays the global settings.

Auto Answer

Enables the incoming calls to be automatically answered. The options are:

Enable with Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                               the agent is in the Ready state in the Cisco Finesse desktop. A zip tone plays to alert the agent.

Enable without Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                               the agent is in the Ready state in the Cisco Finesse desktop. The zip tone does not play to alert the agent.

Disable (Default)—Auto answer is not enabled.

To configure Change Agent State to Not Ready when Agent Busy on Non ACD Line at a team level, you must install UCCX 12.5(1) SU1 ES01.

Step 8

Click Save or Update to apply changes, Cancel to exit or Delete to delete this team.

### Delete a Team

Use the Teams area of the RmCm Configuration web page to
                                 		  delete an existing Team.

Step 1

From the Unified CCXAdministration menu bar, choose Subsystems > RmCm > Teams .

The Teams web page opens.

Step 2

Click 
                                          			 the Delete icon beside the Team Name icon you want to
                                          			 delete.

The system prompts you to confirm the delete.

Step 3

Click OK .

Unified
                     			 Communications users in a Unified CM deployment refers to a Unified CM user.

| Attention | Do not edit
                                       			 users, teams and permissions in Unified Intelligence Center. The Unified CCX to
                                       			 Unified Intelligence Center sync runs as part of daily purge and synchronizes
                                       			 these settings on Unified Intelligence Center according to Unified CCX
                                       			 settings. |
|---|---|

| Note | The RmCm user
                                       		  specified through Unified CCX Administration is updated automatically in Unified CM . |
|---|---|

| Note | This section only
                                             			 applies to Unified CCX deployments with Unified CM. |
|---|---|

| Caution | While Unified CM supports Unicode characters in first and last
                                             			 names, those characters become corrupted in Unified CCX Administration web
                                             			 pages for RmCm configuration and real-time reporting 
                                             			 . |
|---|---|

| Field | Description |
|---|---|
| Primary
                                             						RmCm Provider | The hostname or IP address of the server, running CTI Manager ( Unified CM that runs CTI Manager). The RmCm
                                             						subsystem registers with the CTI Manager so that it can observe an agent's
                                             						device when the agent logs in. When the CTI Manager fails, the RmCm subsystem
                                             						registers with the second CTI Manager, if there is one configured. |
| Secondary
                                             						RmCm Provider | The hostname or IP address of the secondary RmCm Provider. |
| User ID | The RmCm
                                             						user ID. |

| Note | This section only applies to Unified CCX Deployments with Unified
                                             			 CM. |
|---|---|

| Note | If you use Extension Mobility (EM), ensure that the IPCC extension is associated with the Extension Mobility (EM) User Device
                                             Profile (UDP) and not to the physical phone. The Extension Mobility (EM) profile needs to be associated with the RmCm user
                                             and the physical phones that the agents may be expected to use should not be associated to the RmCm user. |
|---|---|

| Step 1 | From the Unified CCXAdministration menu bar, choose Subsystems > RmCm > Resource
                                                				  Groups . The Resource Group web page opens with a list of configured
                                             				resource groups (if any). |
|---|---|
| Step 2 | Click Add New icon in the tool bar in the upper,
                                          			 left corner of the window or Add New button at the bottom of the window. The Resource Group Configuration area opens. |
| Step 3 | In the Resource Group Name field, enter a resource group name. Enter a name that identifies the resource group to which you want
                                             				to assign agents (for example, "Languages" ). |
| Step 4 | Click Add . The Resource Groups page opens displaying the resource group name
                                             				in the Resource Group Name column. |

| Step 1 | From the Unified CCXAdministration menu bar, choose Subsystems > RmCm > Resource
                                                				  Groups . The Resource Group web page opens. |
|---|---|
| Step 2 | In the Resource Group Name column, click the resource group that
                                          			 you want to modify. The Resource Group Configuration area opens. |
| Step 3 | Type the name of the resource group in the Resource Group Name
                                          			 text field. |
| Step 4 | Click Update to apply the modifications. The Resource Groups area opens, displaying the modified resource
                                             				group name in the Resource Group Name column. |

| Tip | To delete resource groups, you can use the following procedure or
                                             			 open a Resource Group and click 
                                             			 the Delete icon or button in the Resource Group
                                             			 Configuration web page. |
|---|---|

| Step 1 | From the Unified CCXAdministration menu bar, choose Subsystems > RmCm > Resource
                                                				  Groups . The Resource Group web page opens. |
|---|---|
| Step 2 | Click Delete icon next to the name of the Resource
                                          			 Group that you want to delete. A dialog box opens, warning that the resource group is about to be
                                             				permanently deleted. |
| Step 3 | Click Continue . The resource group is deleted. |

| Step 1 | From the Unified CCXAdministration menu bar, choose Subsystems > RmCm > Skills . The Skills web page opens to display the Skill Name
                                             				(customer-definable label assigned to an agent), if configured. |
|---|---|
| Step 2 | Click Add New icon in the tool bar in the upper,
                                          			 left corner of the window or Add New button at the bottom of the window. Note When the system reaches the maximum number of skills that can be
                                                         				  created, the Add New icon or button no longer appears. The Skill Configuration web page opens. | Note | When the system reaches the maximum number of skills that can be
                                                         				  created, the Add New icon or button no longer appears. |
| Note | When the system reaches the maximum number of skills that can be
                                                         				  created, the Add New icon or button no longer appears. |
| Step 3 | In the Skill Name field, enter a description of a relevant skill
                                          			 (for example, French). Note Unified CCX does not support the following special characters for Skill name. Table 1. Unsupported Characters in Skill and CSQ Name Symbol Description Symbol Description ` apostrophe ~ tilde ! exclamation mark @ at sign $ dollar % percent ^ circumflex & ampersand * asterix () parentheses = equals sign [] square brackets {} braces ; semicolon \ backslash ? question mark " double quotes <> angle brackets ' single quote + add \| pipe : colon . period / forward slash , comma # hash | Note | Unified CCX does not support the following special characters for Skill name. | Symbol | Description | Symbol | Description | ` | apostrophe | ~ | tilde | ! | exclamation mark | @ | at sign | $ | dollar | % | percent | ^ | circumflex | & | ampersand | * | asterix | () | parentheses | = | equals sign | [] | square brackets | {} | braces | ; | semicolon | \ | backslash | ? | question mark | " | double quotes | <> | angle brackets | ' | single quote | + | add | \| | pipe | : | colon | . | period | / | forward slash | , | comma | # | hash |
| Note | Unified CCX does not support the following special characters for Skill name. |
| Symbol | Description | Symbol | Description |
| ` | apostrophe | ~ | tilde |
| ! | exclamation mark | @ | at sign |
| $ | dollar | % | percent |
| ^ | circumflex | & | ampersand |
| * | asterix | () | parentheses |
| = | equals sign | [] | square brackets |
| {} | braces | ; | semicolon |
| \ | backslash | ? | question mark |
| " | double quotes | <> | angle brackets |
| ' | single quote | + | add |
| \| | pipe | : | colon |
| . | period | / | forward slash |
| , | comma | # | hash |
| Step 4 | Click Add . The Skills web page opens, showing the skill in the Skill Name
                                             				column and the total number of skills that exist in the system. You can add a
                                             				maximum of 150 skills. |

| Note | When the system reaches the maximum number of skills that can be
                                                         				  created, the Add New icon or button no longer appears. |
|---|---|

| Note | Unified CCX does not support the following special characters for Skill name. |
|---|---|

| Symbol | Description | Symbol | Description |
|---|---|---|---|
| ` | apostrophe | ~ | tilde |
| ! | exclamation mark | @ | at sign |
| $ | dollar | % | percent |
| ^ | circumflex | & | ampersand |
| * | asterix | () | parentheses |
| = | equals sign | [] | square brackets |
| {} | braces | ; | semicolon |
| \ | backslash | ? | question mark |
| " | double quotes | <> | angle brackets |
| ' | single quote | + | add |
| \| | pipe | : | colon |
| . | period | / | forward slash |
| , | comma | # | hash |

| Step 1 | From the Unified CCXAdministration menu bar, choose Subsystems > RmCm > Skills . The Skills web page opens. |
|---|---|
| Step 2 | In the Skill Name column, click the skill that you want to modify. The Skill Configuration web page opens. |
| Step 3 | Modify the name of the skill in the Skill Name text field. Note Unified CCX does not support special characters for the skill name. To see the list of unsupported characters, see Table 1 . If you have upgraded to Unified CCX Release 12.5(1) and above and are facing errors when making changes to the Skill name,
                                                         remove the special characters and modify the skill name. | Note | Unified CCX does not support special characters for the skill name. To see the list of unsupported characters, see Table 1 . If you have upgraded to Unified CCX Release 12.5(1) and above and are facing errors when making changes to the Skill name,
                                                         remove the special characters and modify the skill name. |
| Note | Unified CCX does not support special characters for the skill name. To see the list of unsupported characters, see Table 1 . If you have upgraded to Unified CCX Release 12.5(1) and above and are facing errors when making changes to the Skill name,
                                                         remove the special characters and modify the skill name. |
| Step 4 | Click Update to apply the modifications. The Skills Configuration summary opens, displaying the modified
                                             				skill name in the Skill Name column. |

| Note | Unified CCX does not support special characters for the skill name. To see the list of unsupported characters, see Table 1 . If you have upgraded to Unified CCX Release 12.5(1) and above and are facing errors when making changes to the Skill name,
                                                         remove the special characters and modify the skill name. |
|---|---|

| Tip | To delete a  skill, you can use the following procedure or open a
                                             			 skill and click Delete icon or button in the Skills
                                             			 Configuration web page. |
|---|---|

| Step 1 | From the Unified CCXAdministration menu bar, choose Subsystems > RmCm > Skills . The Skills web page opens. |
|---|---|
| Step 2 | Click  
                                          			 the Delete icon next to the name of the skill that
                                          			 you want to delete. A dialog box opens, warning that the skill is about to be
                                             				permanently deleted. |
| Step 3 | Click Continue . The skill is deleted. |

| Warning | After an agent is added, wait for 10 minutes for Unified CCX to automatically synchronize or force synchronization before
                                       the agent can sign in to Cisco Finesse. The maximum allowed length of an agent's IPCC Extension is 15. |
|---|---|

| Caution | Deleting Inactive
                                          		  Agents removes the agent details and records from the Historical Reporting
                                          		  Database, and HR reports will not display historical information of these
                                          		  agents. If Unified CM connection errors have occurred, all agents will not be visible to Unified CCX.
                                          		  In this case, Unified CCX interprets these agents as deleted agents. As a
                                          		  result, the Inactive Agents list will not be accurate. When the errors are
                                          		  resolved, click Inactive
                                             			 Agents again to see an accurate list. |
|---|---|

| Step 1 | From the Unified
                                          			 CCXAdministration menu bar, choose Subsystems > RmCm > Resources . The Resources
                                             				web page opens. Note Only agents or
                                                         				  supervisors who have assigned Unified CCX extensions are displayed in the list
                                                         				  of resources in the Resources area. | Note | Only agents or
                                                         				  supervisors who have assigned Unified CCX extensions are displayed in the list
                                                         				  of resources in the Resources area. |
|---|---|---|---|
| Note | Only agents or
                                                         				  supervisors who have assigned Unified CCX extensions are displayed in the list
                                                         				  of resources in the Resources area. |
| Step 2 | Click the name
                                          			 of the agent in the Resource Name column. The Resource
                                             				Configuration web page opens. |
| Step 3 | Specify the
                                          			 following fields. Field Description Resource Name Name
                                                         							 of the agent (display only). Resource ID Unique
                                                         							 identifying number of the agent (display only). This is the alpha-numeric user
                                                         							 id assigned in the Unified CM End User
                                                         							 Configuration page. Unified CCX Extension Unified CCX Extension assigned to the resource group (display
                                                         							 only). This is the IP Phone extension assigned to the user from the Unified CM End User
                                                         							 Configuration page as IPCC Extension. Resource Group A
                                                         							 resource group with which to associate the agent (optional). Automatic Available Accept
                                                         							 the default ( Enabled )
                                                         							 to automatically put the agent into the Available or Ready state after the
                                                         							 agent finishes a call and disconnects. Note When
                                                                     								a logged on agent in Ready, Not Ready, or Work state answers a call, the agent
                                                                     								state is subject to the Automatic Available setting. Assigned/Unassigned Skills Select
                                                         							 one or more skills from the Unassigned Skills list and click < to add the
                                                         							 skills to the Assigned Skills List. Select
                                                         							 one or more skills from the Assigned Skills List and click > to remove
                                                         							 skills from the Unassigned Skills list. You
                                                         							 can assign up to 50 skills to the agent. Competence Level Select
                                                         							 a skill from the Assigned Skills list and choose a number from the Competence
                                                         							 Level drop-down menu Changes the competence level of an assigned skill (1 = Beginner,
                                                         							 10 = Expert). Note You
                                                                     								can change the competency level one skill at a time, only. You cannot change
                                                                     								skill competency level as a bulk procedure. Team A
                                                         							 group of agents who assign the team to which the resource belongs. Agent Alias Agent alias is the name used instead of the agent ID
                                                         							 when an agent chats with a customer. This option is available only when Finesse
                                                         							 is used by the chat agent. | Field | Description | Resource Name | Name
                                                         							 of the agent (display only). | Resource ID | Unique
                                                         							 identifying number of the agent (display only). This is the alpha-numeric user
                                                         							 id assigned in the Unified CM End User
                                                         							 Configuration page. | Unified CCX Extension | Unified CCX Extension assigned to the resource group (display
                                                         							 only). This is the IP Phone extension assigned to the user from the Unified CM End User
                                                         							 Configuration page as IPCC Extension. | Resource Group | A
                                                         							 resource group with which to associate the agent (optional). | Automatic Available | Accept
                                                         							 the default ( Enabled )
                                                         							 to automatically put the agent into the Available or Ready state after the
                                                         							 agent finishes a call and disconnects. Note When
                                                                     								a logged on agent in Ready, Not Ready, or Work state answers a call, the agent
                                                                     								state is subject to the Automatic Available setting. | Note | When
                                                                     								a logged on agent in Ready, Not Ready, or Work state answers a call, the agent
                                                                     								state is subject to the Automatic Available setting. | Assigned/Unassigned Skills | Select
                                                         							 one or more skills from the Unassigned Skills list and click < to add the
                                                         							 skills to the Assigned Skills List. Select
                                                         							 one or more skills from the Assigned Skills List and click > to remove
                                                         							 skills from the Unassigned Skills list. You
                                                         							 can assign up to 50 skills to the agent. | Competence Level | Select
                                                         							 a skill from the Assigned Skills list and choose a number from the Competence
                                                         							 Level drop-down menu Changes the competence level of an assigned skill (1 = Beginner,
                                                         							 10 = Expert). Note You
                                                                     								can change the competency level one skill at a time, only. You cannot change
                                                                     								skill competency level as a bulk procedure. | Note | You
                                                                     								can change the competency level one skill at a time, only. You cannot change
                                                                     								skill competency level as a bulk procedure. | Team | A
                                                         							 group of agents who assign the team to which the resource belongs. | Agent Alias | Agent alias is the name used instead of the agent ID
                                                         							 when an agent chats with a customer. This option is available only when Finesse
                                                         							 is used by the chat agent. |
| Field | Description |
| Resource Name | Name
                                                         							 of the agent (display only). |
| Resource ID | Unique
                                                         							 identifying number of the agent (display only). This is the alpha-numeric user
                                                         							 id assigned in the Unified CM End User
                                                         							 Configuration page. |
| Unified CCX Extension | Unified CCX Extension assigned to the resource group (display
                                                         							 only). This is the IP Phone extension assigned to the user from the Unified CM End User
                                                         							 Configuration page as IPCC Extension. |
| Resource Group | A
                                                         							 resource group with which to associate the agent (optional). |
| Automatic Available | Accept
                                                         							 the default ( Enabled )
                                                         							 to automatically put the agent into the Available or Ready state after the
                                                         							 agent finishes a call and disconnects. Note When
                                                                     								a logged on agent in Ready, Not Ready, or Work state answers a call, the agent
                                                                     								state is subject to the Automatic Available setting. | Note | When
                                                                     								a logged on agent in Ready, Not Ready, or Work state answers a call, the agent
                                                                     								state is subject to the Automatic Available setting. |
| Note | When
                                                                     								a logged on agent in Ready, Not Ready, or Work state answers a call, the agent
                                                                     								state is subject to the Automatic Available setting. |
| Assigned/Unassigned Skills | Select
                                                         							 one or more skills from the Unassigned Skills list and click < to add the
                                                         							 skills to the Assigned Skills List. Select
                                                         							 one or more skills from the Assigned Skills List and click > to remove
                                                         							 skills from the Unassigned Skills list. You
                                                         							 can assign up to 50 skills to the agent. |
| Competence Level | Select
                                                         							 a skill from the Assigned Skills list and choose a number from the Competence
                                                         							 Level drop-down menu Changes the competence level of an assigned skill (1 = Beginner,
                                                         							 10 = Expert). Note You
                                                                     								can change the competency level one skill at a time, only. You cannot change
                                                                     								skill competency level as a bulk procedure. | Note | You
                                                                     								can change the competency level one skill at a time, only. You cannot change
                                                                     								skill competency level as a bulk procedure. |
| Note | You
                                                                     								can change the competency level one skill at a time, only. You cannot change
                                                                     								skill competency level as a bulk procedure. |
| Team | A
                                                         							 group of agents who assign the team to which the resource belongs. |
| Agent Alias | Agent alias is the name used instead of the agent ID
                                                         							 when an agent chats with a customer. This option is available only when Finesse
                                                         							 is used by the chat agent. |
| Step 4 | Click Update to apply the changes. The Resources
                                             				area of the RmCm Configuration summary web page opens, and the agent is now
                                             				assigned to the resource group and skills (if skills were assigned). |

| Note | Only agents or
                                                         				  supervisors who have assigned Unified CCX extensions are displayed in the list
                                                         				  of resources in the Resources area. |
|---|---|

| Field | Description |
|---|---|
| Resource Name | Name
                                                         							 of the agent (display only). |
| Resource ID | Unique
                                                         							 identifying number of the agent (display only). This is the alpha-numeric user
                                                         							 id assigned in the Unified CM End User
                                                         							 Configuration page. |
| Unified CCX Extension | Unified CCX Extension assigned to the resource group (display
                                                         							 only). This is the IP Phone extension assigned to the user from the Unified CM End User
                                                         							 Configuration page as IPCC Extension. |
| Resource Group | A
                                                         							 resource group with which to associate the agent (optional). |
| Automatic Available | Accept
                                                         							 the default ( Enabled )
                                                         							 to automatically put the agent into the Available or Ready state after the
                                                         							 agent finishes a call and disconnects. Note When
                                                                     								a logged on agent in Ready, Not Ready, or Work state answers a call, the agent
                                                                     								state is subject to the Automatic Available setting. | Note | When
                                                                     								a logged on agent in Ready, Not Ready, or Work state answers a call, the agent
                                                                     								state is subject to the Automatic Available setting. |
| Note | When
                                                                     								a logged on agent in Ready, Not Ready, or Work state answers a call, the agent
                                                                     								state is subject to the Automatic Available setting. |
| Assigned/Unassigned Skills | Select
                                                         							 one or more skills from the Unassigned Skills list and click < to add the
                                                         							 skills to the Assigned Skills List. Select
                                                         							 one or more skills from the Assigned Skills List and click > to remove
                                                         							 skills from the Unassigned Skills list. You
                                                         							 can assign up to 50 skills to the agent. |
| Competence Level | Select
                                                         							 a skill from the Assigned Skills list and choose a number from the Competence
                                                         							 Level drop-down menu Changes the competence level of an assigned skill (1 = Beginner,
                                                         							 10 = Expert). Note You
                                                                     								can change the competency level one skill at a time, only. You cannot change
                                                                     								skill competency level as a bulk procedure. | Note | You
                                                                     								can change the competency level one skill at a time, only. You cannot change
                                                                     								skill competency level as a bulk procedure. |
| Note | You
                                                                     								can change the competency level one skill at a time, only. You cannot change
                                                                     								skill competency level as a bulk procedure. |
| Team | A
                                                         							 group of agents who assign the team to which the resource belongs. |
| Agent Alias | Agent alias is the name used instead of the agent ID
                                                         							 when an agent chats with a customer. This option is available only when Finesse
                                                         							 is used by the chat agent. |

| Note | When
                                                                     								a logged on agent in Ready, Not Ready, or Work state answers a call, the agent
                                                                     								state is subject to the Automatic Available setting. |
|---|---|

| Note | You
                                                                     								can change the competency level one skill at a time, only. You cannot change
                                                                     								skill competency level as a bulk procedure. |
|---|---|

| Step 1 | From the Unified CCXAdministration menu bar, select Subsystems > RmCm > Assign
                                                				  Skills . The Assign Skills summary web page opens. Tip Only agents or supervisors who have assigned Unified CCX
                                                         				  extensions are displayed in the list of resources in the Resources area. | Tip | Only agents or supervisors who have assigned Unified CCX
                                                         				  extensions are displayed in the list of resources in the Resources area. |
|---|---|---|---|
| Tip | Only agents or supervisors who have assigned Unified CCX
                                                         				  extensions are displayed in the list of resources in the Resources area. |
| Step 2 | In the Resource Name column, check the check box beside each agent
                                          			 to whom you want to assign set of same resource group and skills. In the
                                          			 Resource Name column, check the check box next to each agent you want to assign
                                          			 set of same resource group and skills. Note You can check the Select All check box to select all agents. The Skill summary web page shows the total number of skills
                                             				created. | Note | You can check the Select All check box to select all agents. |
| Note | You can check the Select All check box to select all agents. |
| Step 3 | Click Add Skill icon that displays in the tool bar
                                          			 in the upper, left corner of the window or the Add Skill button that displays at the bottom
                                          			 of the window. The Add Skill web page opens. |
| Step 4 | Specify the following fields. Field Description Resource Group To assign a resource group to all the selected agents,
                                                         							 choose a resource group from the Resource Group drop-down menu. Skills to Add Select one or more skills from the Skills list and click
                                                         							 < to add the skills to the Skills to Add List. Note The Skills to Add list contains all skills, not just
                                                                     								the skills that agents already have. Skills List of the available skills. Competence Level Select a skill from the Assigned Skills list and
                                                         							 choosing a number from the Competence Level drop-down menu | Field | Description | Resource Group | To assign a resource group to all the selected agents,
                                                         							 choose a resource group from the Resource Group drop-down menu. | Skills to Add | Select one or more skills from the Skills list and click
                                                         							 < to add the skills to the Skills to Add List. Note The Skills to Add list contains all skills, not just
                                                                     								the skills that agents already have. | Note | The Skills to Add list contains all skills, not just
                                                                     								the skills that agents already have. | Skills | List of the available skills. | Competence Level | Select a skill from the Assigned Skills list and
                                                         							 choosing a number from the Competence Level drop-down menu |
| Field | Description |
| Resource Group | To assign a resource group to all the selected agents,
                                                         							 choose a resource group from the Resource Group drop-down menu. |
| Skills to Add | Select one or more skills from the Skills list and click
                                                         							 < to add the skills to the Skills to Add List. Note The Skills to Add list contains all skills, not just
                                                                     								the skills that agents already have. | Note | The Skills to Add list contains all skills, not just
                                                                     								the skills that agents already have. |
| Note | The Skills to Add list contains all skills, not just
                                                                     								the skills that agents already have. |
| Skills | List of the available skills. |
| Competence Level | Select a skill from the Assigned Skills list and
                                                         							 choosing a number from the Competence Level drop-down menu |
| Step 5 | Click Update to apply the changes. The Assign Skills area of the RmCm Configuration web page opens,
                                             				and the agents are now assigned to the resource group and their skills (if skills
                                             				were assigned). |

| Tip | Only agents or supervisors who have assigned Unified CCX
                                                         				  extensions are displayed in the list of resources in the Resources area. |
|---|---|

| Note | You can check the Select All check box to select all agents. |
|---|---|

| Field | Description |
|---|---|
| Resource Group | To assign a resource group to all the selected agents,
                                                         							 choose a resource group from the Resource Group drop-down menu. |
| Skills to Add | Select one or more skills from the Skills list and click
                                                         							 < to add the skills to the Skills to Add List. Note The Skills to Add list contains all skills, not just
                                                                     								the skills that agents already have. | Note | The Skills to Add list contains all skills, not just
                                                                     								the skills that agents already have. |
| Note | The Skills to Add list contains all skills, not just
                                                                     								the skills that agents already have. |
| Skills | List of the available skills. |
| Competence Level | Select a skill from the Assigned Skills list and
                                                         							 choosing a number from the Competence Level drop-down menu |

| Note | The Skills to Add list contains all skills, not just
                                                                     								the skills that agents already have. |
|---|---|

| Note | If a resource is not assigned a skill that you attempt to remove, the
                                             			 resource is not updated. However, the system will still generate a related
                                             			 message. |
|---|---|

| Step 1 | From the Unified CCXAdministration menu bar, choose Subsystems > RmCm > Assign
                                                				  Skills . The Assign Skill summary web page opens. |
|---|---|
| Step 2 | In the Resource Name column, click the check box next to the agent
                                          			 you want to remove skills from. Note You can click Select All check box to select all agents. | Note | You can click Select All check box to select all agents. |
| Note | You can click Select All check box to select all agents. |
| Step 3 | Click Remove Skill icon that displays in the tool
                                          			 bar in the upper, left corner of the window or the Remove Skill button that displays at the
                                          			 bottom of the window. The Remove Skill Configuration web page opens. |
| Step 4 | Remove skills by choosing one or more skills from the Skills list
                                          			 and clicking > to move the skills to the Skills to Remove list. |
| Step 5 | Click Update to apply the changes. The Assign Skills area of the RmCm Configuration web page opens,
                                             				and the agents are no longer assigned to the skills. |

| Note | You can click Select All check box to select all agents. |
|---|---|

| Step 1 | From the Unified
                                          			 CCXAdministration menu bar, choose Subsystems > RmCm > Contact Service
                                                				  Queues . The Contact
                                             				Service Queues web page opens. Use this web
                                             				page to view the following fields: Field Description Name Name
                                                            							 of the resource or skill group. Contact Queuing Criteria Algorithm used to order the queued calls (contacts). Resource Pool Selection Model The
                                                            							 resource selection criteria chosen for this CSQ. Resource Pool The
                                                            							 skills or resource group used for this CSQ. CSQ
                                                            							 Type The
                                                            							 type of the CSQ. Delete Deletes the selected CSQ. | Field | Description | Name | Name
                                                            							 of the resource or skill group. | Contact Queuing Criteria | Algorithm used to order the queued calls (contacts). | Resource Pool Selection Model | The
                                                            							 resource selection criteria chosen for this CSQ. | Resource Pool | The
                                                            							 skills or resource group used for this CSQ. | CSQ
                                                            							 Type | The
                                                            							 type of the CSQ. | Delete | Deletes the selected CSQ. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Field | Description |
| Name | Name
                                                            							 of the resource or skill group. |
| Contact Queuing Criteria | Algorithm used to order the queued calls (contacts). |
| Resource Pool Selection Model | The
                                                            							 resource selection criteria chosen for this CSQ. |
| Resource Pool | The
                                                            							 skills or resource group used for this CSQ. |
| CSQ
                                                            							 Type | The
                                                            							 type of the CSQ. |
| Delete | Deletes the selected CSQ. |
| Step 2 | Click Add
                                             				New icon that displays in the tool bar in the upper, left corner of
                                          			 the window or the Add
                                             				New button that displays at the bottom of the window. The Contact
                                             				Service Queue Configuration web page opens. Note If this link
                                                         				  does not appear on the page, it means that the system has reached the maximum
                                                         				  number of CSQs that can be created. The CSQ Summary page displays the total
                                                         				  number of created CSQs. | Note | If this link
                                                         				  does not appear on the page, it means that the system has reached the maximum
                                                         				  number of CSQs that can be created. The CSQ Summary page displays the total
                                                         				  number of created CSQs. |
| Note | If this link
                                                         				  does not appear on the page, it means that the system has reached the maximum
                                                         				  number of CSQs that can be created. The CSQ Summary page displays the total
                                                         				  number of created CSQs. |
| Step 3 | Use the Contact
                                          			 Service Queue Configuration web page to specify the various fields. For more
                                          			 information on the fields, see Contact Service Queue Configuration Web Page . |
| Step 4 | Click Next . The second
                                             				Contact Service Queue Configuration area opens with the newly-assigned CSQ
                                             				Name. |
| Step 5 | Select an option
                                          			 from the Resource Selection Criteria drop-down menu. Note The Resource
                                                         				  Pool Selection Model settings determine the options available in this drop-down
                                                         				  menu. Longest
                                                      						Available —Selects the agent who has been in the Available state for
                                                   					 the longest amount of time. Most Handled
                                                      						Contacts —Selects the agent who has handled the most calls. Shortest Average Handle
                                                      						Time —Selects the agent who generally spends the least amount of
                                                   					 time talking to customers. Most Skilled —Used
                                                   					 for expert agent call distribution. Selects the agent with the highest total
                                                   					 competency level. The total competency level is determined by adding the
                                                   					 agent's competency levels for each of their assigned skills that are also
                                                   					 assigned to the CSQ. Example
                                                         						  1: If Agent1 is assigned Skill1(5), Skill2(6), and Skill3(7) and CSQ1 specifies
                                                         						  Skill1(min=1) and Skill3(min=1), the total competency level for Agent1 for CSQ1
                                                         						  is 12. Example
                                                         						  2: If Agent1 is assigned Skill1(5) and Skill2(6) and Skill3(7) and CSQ1
                                                         						  specifies Skill1(min=1), only, the total competency level for Agent1 for CSQ1
                                                         						  is 5. Least
                                                      						Skilled —Used for expert agent call distribution. Selects the agent
                                                   					 with the lowest total competency level. The total competency level is
                                                   					 determined by adding the agent’s competency level in each assigned skill. Most Skilled by
                                                      						Weight — Used for expert agent call distribution. Selects the agent
                                                   					 with the highest total competency level multiplied by the skill’s associated
                                                   					 weight. Least Skilled by
                                                      						Weight —Used for expert agent call distribution. Selects the agent
                                                   					 with the lowest total competency level multiplied by the skill’s associated
                                                   					 weight. Most Skilled by
                                                      						Order — Used for expert agent call distribution. Selects the agent
                                                   					 with the highest total competency level in the ordered list. Least Skilled by
                                                      						Order — Used for expert agent call distribution. Selects the agent
                                                   					 with the lowest total competency level in the ordered list. Note If two or
                                                         				  more agents have equal competency level, the selection automatically defaults
                                                         				  to Longest Available selection criteria. | Note | The Resource
                                                         				  Pool Selection Model settings determine the options available in this drop-down
                                                         				  menu. | Note | If two or
                                                         				  more agents have equal competency level, the selection automatically defaults
                                                         				  to Longest Available selection criteria. |
| Note | The Resource
                                                         				  Pool Selection Model settings determine the options available in this drop-down
                                                         				  menu. |
| Note | If two or
                                                         				  more agents have equal competency level, the selection automatically defaults
                                                         				  to Longest Available selection criteria. |
| Step 6 | Specify the
                                          			 following settings, as necessary: Note The Resource
                                                         				  Pool Selection Model setting determines the availability of these options. Use the
                                                				  Select Skills list to highlight the skills you want; click the Add button next to the list. Specify a
                                                				  Minimum Competence Level for the skills assigned to the CSQ. Depending on the
                                                				  Resource pool criteria you chose, specify a Weight value between 1 and 1000. If the
                                                				  Resource Selection Criteria is Most Skilled by Order or Least Skilled by Order,
                                                				  use the arrow icons to order the skills by moving them up or down in the list. Note Use the Delete icon next to a skill to delete that skill
                                                               						from the Skills Required list. | Note | The Resource
                                                         				  Pool Selection Model setting determines the availability of these options. | Note | Use the Delete icon next to a skill to delete that skill
                                                               						from the Skills Required list. |
| Note | The Resource
                                                         				  Pool Selection Model setting determines the availability of these options. |
| Note | Use the Delete icon next to a skill to delete that skill
                                                               						from the Skills Required list. |
| Step 7 | If you
                                          			 selected one of the Least/Most Skilled options as shown in the list below for
                                          			 the Resource Selection Criteria, you can view the agent order using Show
                                             				Resources icon or button. Note The order of
                                                         				  the agents determines the priority, with the agent at the top of the list
                                                         				  having the highest priority. To change the
                                             				order of the agents belonging to the CSQ, you should modify the skill set of
                                             				the agents. The Least/Most Skilled Resource Selection Criteria option comprises
                                             				the following: Most
                                                				  Skilled Least
                                                				  Skilled Most
                                                				  Skilled by Order Least
                                                				  Skilled by Order Most
                                                				  Skilled by Weight Least
                                                				  Skilled by Weight | Note | The order of
                                                         				  the agents determines the priority, with the agent at the top of the list
                                                         				  having the highest priority. |
| Note | The order of
                                                         				  the agents determines the priority, with the agent at the top of the list
                                                         				  having the highest priority. |
| Step 8 | If you
                                          			 selected Resource
                                             				Groups as the Resource Pool Selection Model on the previous page, follow
                                          			 these steps: Select an
                                                				  option from the Resource Selection Criteria drop-down menu. Longest Available —Selects the agent who has been in
                                                            						  the Available state for the longest amount of time. Linear —Selects the next available agent with the
                                                            						  highest priority, as determined by the agent order in the Resources list. Circular —Selects the next available agent with the
                                                            						  highest priority, based on the last agent selected and the agent order in the
                                                            						  Resources list. Most Handled Contacts —Selects the agent who has
                                                            						  handled the most calls. Shortest Average Handle Time —Selects the agent who
                                                            						  generally spends the least amount of time talking to customers. Choose the
                                                				  resource group for this CSQ from the Resource Group drop-down menu. Click Show Resources icon to show all agents who meet the
                                                				  specified criteria. If you
                                                				  selected Linear or Circular as the Resource Selection Criteria, if necessary,
                                                				  rearrange the order of agents in the Resources list by highlighting an agent
                                                				  and using the up and down arrows to move the agent in the list. Click Add to apply changes and update the system. The new
                                                   					 CSQ is now displayed, and all agents who belong to the resource group or all
                                                   					 selected skill groups are now a part of this CSQ. |

| Field | Description |
|---|---|
| Name | Name
                                                            							 of the resource or skill group. |
| Contact Queuing Criteria | Algorithm used to order the queued calls (contacts). |
| Resource Pool Selection Model | The
                                                            							 resource selection criteria chosen for this CSQ. |
| Resource Pool | The
                                                            							 skills or resource group used for this CSQ. |
| CSQ
                                                            							 Type | The
                                                            							 type of the CSQ. |
| Delete | Deletes the selected CSQ. |

| Note | If this link
                                                         				  does not appear on the page, it means that the system has reached the maximum
                                                         				  number of CSQs that can be created. The CSQ Summary page displays the total
                                                         				  number of created CSQs. |
|---|---|

| Note | The Resource
                                                         				  Pool Selection Model settings determine the options available in this drop-down
                                                         				  menu. |
|---|---|

| Note | If two or
                                                         				  more agents have equal competency level, the selection automatically defaults
                                                         				  to Longest Available selection criteria. |
|---|---|

| Note | The Resource
                                                         				  Pool Selection Model setting determines the availability of these options. |
|---|---|

| Note | Use the Delete icon next to a skill to delete that skill
                                                               						from the Skills Required list. |
|---|---|

| Note | The order of
                                                         				  the agents determines the priority, with the agent at the top of the list
                                                         				  having the highest priority. |
|---|---|

| Field | Description |
|---|---|
| Contact
                                                						Service Queue Name | Enter a
                                                						meaningful name that is concise, yet easy to recognize (for example, Language
                                                						Experts). This is a mandatory field. Note Unified CCX does not support special characters for the Call Service Queue name. To see the list of unsupported characters,
                                                            see Table 1 . | Note | Unified CCX does not support special characters for the Call Service Queue name. To see the list of unsupported characters,
                                                            see Table 1 . |
| Note | Unified CCX does not support special characters for the Call Service Queue name. To see the list of unsupported characters,
                                                            see Table 1 . |
| Contact
                                                						Service Queue Type | Display only. Voice—Agents
                                                						in this CSQ can handle inbound and outbound voice calls. |
| Contact
                                                						Queuing Criteria | Display
                                                						only. Displays the criteria used for queuing the contacts. For example, First
                                                						In, First Out (FIFO). |
| Automatic Wrapup | Determines whether agents handling calls that are routed through this CSQ automatically enter the Wrapup state when a call ends. This field is mandatory. Options are: Enabled—Agents associated to a CSQ that has the Automatic Wrapup option enabled, enter the Wrapup state automatically when on a call. CSQ ends. If agents are associated to a CSQ that has the Automatic Wrapup option disabled handle transferred calls that were originally delivered by a CSQ that has Automatic Wrapup enabled, they also enter the Wrapup state automatically when a call ends. Disabled (default)—Agents enter Ready or Not Ready state when a
                                                      							 call ends, depending on the Automatic Available setting. |
| Wrapup
                                                						Time | Determines the length of the Wrapup state for this CSQ when a call ends. Options are: Enabled button with Seconds field—The Seconds field specifies the length of the Wrapup state phase. Disabled—No limit on how long the agent can stay in the Wrapup state. |
| Resource
                                                						Pool Selection Model | Select
                                                						one of the following options from the drop-down menu: Resource Skills—To create a skills-based CSQ. Resource Group—To create a resource group-based CSQ. This is
                                                						a mandatory field. |
| Service
                                                						Level | The
                                                						target maximum number of seconds a call is queued before it is connected to an
                                                						agent. This is a mandatory field. |
| Service
                                                						Level Percentage | The
                                                						target goal for percentage of contacts that meet the service level. This is a
                                                						mandatory field. For
                                                						example, a call center that has a service level of 20 and a service level
                                                						percentage of 80 percent has a goal of answering 80 percent of its calls within
                                                						20 seconds. |
| Prompt | .wav
                                                						prompt file to associate with the CSQ. You can retrieve the prompt file that
                                                						you select from this Prompt drop-down list using the Create CSQ Prompt Step in
                                                						the Unified CCX Editor. In the Unified CCX Editor, Create CSQ Prompt Step is one of the steps used to create scripts for the Unified CCX engine. In
                                                this step, you need to give the CSQ ID that is displayed as the last number in the AppAdmin address bar of the web page that
                                                is displayed when you click on an existing CSQ. For example, the CSQ ID will be 3 if the address bar of an existing CSQ Configuration
                                                web page ends with "&csdid=3" . When you run the script, it will return the prompt associated with the specific CSQ ID. Use the Play Prompt Step within
                                                the script to play this prompt. See the Cisco Unified CCX Editor Step Reference Guide for
                                                						detailed information on scripting. Note The
                                                            						  Prompt field is available only if you have licensed the Cisco Unified CCX
                                                            						  Enhanced or Premium product package. | Note | The
                                                            						  Prompt field is available only if you have licensed the Cisco Unified CCX
                                                            						  Enhanced or Premium product package. |
| Note | The
                                                            						  Prompt field is available only if you have licensed the Cisco Unified CCX
                                                            						  Enhanced or Premium product package. |

| Note | Unified CCX does not support special characters for the Call Service Queue name. To see the list of unsupported characters,
                                                            see Table 1 . |
|---|---|

| Note | The
                                                            						  Prompt field is available only if you have licensed the Cisco Unified CCX
                                                            						  Enhanced or Premium product package. |
|---|---|

| Note | Changes take
                                             			 effect when all agents affected by the changes have left the Ready state. Emails Contact
                                                				Service Queues cannot be modified. It is for display only. |
|---|---|

| Step 1 | From the Unified
                                          			 CCXAdministration menu bar, choose Subsystems > RmCm > Contact Service
                                                				  Queues . The Contact
                                             				Service Queues web page opens. |
|---|---|
| Step 2 | In the Name
                                          			 list, click the CSQ that you want to modify. The Contact
                                             				Service Queue Configuration page opens. |
| Step 3 | Modify the
                                          			 Contact Service Queue Configuration information as necessary. Note If you change
                                                         				  an existing CSQ name, the old name still exists in the HR reports and the CSQ
                                                         				  is not removed even if all the data is purged. | Note | If you change
                                                         				  an existing CSQ name, the old name still exists in the HR reports and the CSQ
                                                         				  is not removed even if all the data is purged. |
| Note | If you change
                                                         				  an existing CSQ name, the old name still exists in the HR reports and the CSQ
                                                         				  is not removed even if all the data is purged. |
| Step 4 | Click Next icon that displays in the tool bar in the upper, left corner of the window or the Next button that displays at the bottom of the window to view and update the remaining fields. |
| Step 5 | Click Update icon in the top of the window or the Update button that displays at the bottom of the
                                          			 window to apply the modifications. Note Ensure that the Resource Selection Criteria is changed only when there are no agents signed in. If there are active agents, these changes take effect only when all the
                                                         active agents sign out and sign in again. | Note | Ensure that the Resource Selection Criteria is changed only when there are no agents signed in. If there are active agents, these changes take effect only when all the
                                                         active agents sign out and sign in again. |
| Note | Ensure that the Resource Selection Criteria is changed only when there are no agents signed in. If there are active agents, these changes take effect only when all the
                                                         active agents sign out and sign in again. |

| Note | If you change
                                                         				  an existing CSQ name, the old name still exists in the HR reports and the CSQ
                                                         				  is not removed even if all the data is purged. |
|---|---|

| Note | Ensure that the Resource Selection Criteria is changed only when there are no agents signed in. If there are active agents, these changes take effect only when all the
                                                         active agents sign out and sign in again. |
|---|---|

| Note | Existing Email Contact Service Queues can be deleted. |
|---|---|

| Step 1 | From the Unified
                                          			 CCXAdministration menu bar, choose Subsystems > RmCm > Contact Service
                                                				  Queues . The Contact
                                             				Service Queues web page opens. |
|---|---|
| Step 2 | Click the Delete icon next to the name of the CSQ that you
                                          			 want to delete. Note You can also
                                                         				  delete a CSQ from its Contact Service Queue Configuration page using the Delete
                                                         				  icon or button. | Note | You can also
                                                         				  delete a CSQ from its Contact Service Queue Configuration page using the Delete
                                                         				  icon or button. |
| Note | You can also
                                                         				  delete a CSQ from its Contact Service Queue Configuration page using the Delete
                                                         				  icon or button. |

| Note | You can also
                                                         				  delete a CSQ from its Contact Service Queue Configuration page using the Delete
                                                         				  icon or button. |
|---|---|

| Agent ID | Assigned Skills | Resource Group |
|---|---|---|
| Agent1 | Banking (Competence Level 10) CreditCard (Competence Level 6) | GeneralQueries |
| Agent2 | Banking (Competence Level 5) CreditCard (Competence Level 10) | GeneralQueries |
| Agent3 | None | GeneralQueries |

| CSQ Name | Resource Pool Selection Model | Resource Selection Criteria | Skill/Competence | Available Agents |
|---|---|---|---|---|
| CSQ1 | Resource Skills | Most Skilled | BankingMinimum competency: 5 | Agent1 Agent2 |
| CSQ2 | Resource Skills | Most Skilled | CreditCardMinimum competency: 5 | Agent1 Agent2 |
| CSQ3 | Resource Group | Longest Available | GeneralQueries | Agent1 Agent2 Agent3 |

| Note | If two or more agents have equal competency level, the
                                             			 selection automatically defaults to Longest Available selection criteria. |
|---|---|

| Example | CSQ Skills | Agent Competency Levels | Sequence Agents Become Ready | Selection Order |
|---|---|---|---|---|
| Most skilled resource selection model | Technical Support | Agent A = 10 Agent B = 10 Agent C = 5 | A, B C | A, B, C |
| C, A, B | A, B, C |
| A, C, B | A, B, C |
| C, B, A | B, A, C |
| Least skilled resource selection model | Technical Support | Agent A = 10 Agent B = 10 Agent C = 5 | A, B, C | C, A, B |
| C, A, B | C, A, B |
| A, C, B | C, A, B |
| C, B, A | C, B, A |
| Note The ordering in the two examples above are not opposite
                                                         						because the selection criteria has changed from most to least skilled—when
                                                         						competency levels are equal, both selection models choose the resources that
                                                         						have been available for the longest time. | Note | The ordering in the two examples above are not opposite
                                                         						because the selection criteria has changed from most to least skilled—when
                                                         						competency levels are equal, both selection models choose the resources that
                                                         						have been available for the longest time. |
| Note | The ordering in the two examples above are not opposite
                                                         						because the selection criteria has changed from most to least skilled—when
                                                         						competency levels are equal, both selection models choose the resources that
                                                         						have been available for the longest time. |
| Most skilled resource selection model | SalesSupport | Agent A = Sales (10) Support (5) Agent B = Sales (5), Support (10) Agent C = Sales (5) Support (1) | A, B, C | A, B, C |
| C, A, B | A, B, C |
| A, C, B | A, B, C |
| C, B, A | B, A, C |
| Least skilled resource selection model | SalesSupport | Agent A = Sales (10) Support (5) Agent B = Sales (5), Support (10) Agent C = Sales (5) Support (1) | A, B, C | C, A, B |
| C, A, B | C, A, B |
| A, C, B | C, A, B |
| C, B, A | C, B, A |

| Note | The ordering in the two examples above are not opposite
                                                         						because the selection criteria has changed from most to least skilled—when
                                                         						competency levels are equal, both selection models choose the resources that
                                                         						have been available for the longest time. |
|---|---|

| Step 1 | From the Unified
                                       			 CCXAdministration menu bar, choose Subsystems > RmCm > Agent Based Routing
                                             				  Settings . The Agent Based Routing Settings area
                                       			 opens. Note The Agent
                                                      				  Based Routing Settings are available only if you are using Unified CCX Enhanced
                                                      				  or Premium license packages. | Note | The Agent
                                                      				  Based Routing Settings are available only if you are using Unified CCX Enhanced
                                                      				  or Premium license packages. |
|---|---|---|---|
| Note | The Agent
                                                      				  Based Routing Settings are available only if you are using Unified CCX Enhanced
                                                      				  or Premium license packages. |
| Step 2 | Specify the
                                       			 following fields: Field Description Automatic Wrapup Determines whether agents handling calls that are routed through this CSQ automatically enter the Automatic Wrapup state when a call ends. Enabled—Agents associated to a CSQ that has the Automatic Wrapup option enabled enter the Wrapup state automatically when on a call. If agents are associated to a CSQ that has the Automatic Wrapup option disabled handle transferred calls that were originally delivered by a CSQ that has Automatic Wrapup enabled, they also enter the Wrapup state automatically when a call ends. Disabled (default)—Agents enter Ready or Not Ready state when a
                                                            								  call ends, depending on the Automatic Available setting. Wrapup
                                                      							 Time Determines if agents automatically enter Wrapup when a call
                                                      							 ends. Enabled button with seconds field—Controls how long the agent can stay in the Wrapup state if Automatic Wrapup is enabled. The seconds field specifies the Wrapup time length. Disabled (default)—No limit of how long the agent can stay in the Wrapup state if Automatic Wrapup is enabled. | Field | Description | Automatic Wrapup | Determines whether agents handling calls that are routed through this CSQ automatically enter the Automatic Wrapup state when a call ends. Enabled—Agents associated to a CSQ that has the Automatic Wrapup option enabled enter the Wrapup state automatically when on a call. If agents are associated to a CSQ that has the Automatic Wrapup option disabled handle transferred calls that were originally delivered by a CSQ that has Automatic Wrapup enabled, they also enter the Wrapup state automatically when a call ends. Disabled (default)—Agents enter Ready or Not Ready state when a
                                                            								  call ends, depending on the Automatic Available setting. | Wrapup
                                                      							 Time | Determines if agents automatically enter Wrapup when a call
                                                      							 ends. Enabled button with seconds field—Controls how long the agent can stay in the Wrapup state if Automatic Wrapup is enabled. The seconds field specifies the Wrapup time length. Disabled (default)—No limit of how long the agent can stay in the Wrapup state if Automatic Wrapup is enabled. |
| Field | Description |
| Automatic Wrapup | Determines whether agents handling calls that are routed through this CSQ automatically enter the Automatic Wrapup state when a call ends. Enabled—Agents associated to a CSQ that has the Automatic Wrapup option enabled enter the Wrapup state automatically when on a call. If agents are associated to a CSQ that has the Automatic Wrapup option disabled handle transferred calls that were originally delivered by a CSQ that has Automatic Wrapup enabled, they also enter the Wrapup state automatically when a call ends. Disabled (default)—Agents enter Ready or Not Ready state when a
                                                            								  call ends, depending on the Automatic Available setting. |
| Wrapup
                                                      							 Time | Determines if agents automatically enter Wrapup when a call
                                                      							 ends. Enabled button with seconds field—Controls how long the agent can stay in the Wrapup state if Automatic Wrapup is enabled. The seconds field specifies the Wrapup time length. Disabled (default)—No limit of how long the agent can stay in the Wrapup state if Automatic Wrapup is enabled. |
| Step 3 | Click Save icon
                                       			 that displays in the tool bar in the upper, left corner of the window or the Save button
                                       			 that displays at the bottom of the window to apply changes. |

| Note | The Agent
                                                      				  Based Routing Settings are available only if you are using Unified CCX Enhanced
                                                      				  or Premium license packages. |
|---|---|

| Field | Description |
|---|---|
| Automatic Wrapup | Determines whether agents handling calls that are routed through this CSQ automatically enter the Automatic Wrapup state when a call ends. Enabled—Agents associated to a CSQ that has the Automatic Wrapup option enabled enter the Wrapup state automatically when on a call. If agents are associated to a CSQ that has the Automatic Wrapup option disabled handle transferred calls that were originally delivered by a CSQ that has Automatic Wrapup enabled, they also enter the Wrapup state automatically when a call ends. Disabled (default)—Agents enter Ready or Not Ready state when a
                                                            								  call ends, depending on the Automatic Available setting. |
| Wrapup
                                                      							 Time | Determines if agents automatically enter Wrapup when a call
                                                      							 ends. Enabled button with seconds field—Controls how long the agent can stay in the Wrapup state if Automatic Wrapup is enabled. The seconds field specifies the Wrapup time length. Disabled (default)—No limit of how long the agent can stay in the Wrapup state if Automatic Wrapup is enabled. |

| Note | Before creating a team, you must set up Supervisors using the User Management page. |
|---|---|

| Note | The Advanced Supervisor Capability of Queue Management is removed when: Supervisor is not associated to any team. Supervisor is not the primary or secondary Supervisor of any team. There are no CSQs assigned to the teams associated to the Supervisor. |
|---|---|

| Note | A team that accesses Live Data reports is limited to 50 agents. |
|---|---|

| Step 1 | From the Unified CCX Administration menu, choose Tools > User Management > User View . The User Configuration page displays the list of all users. |
|---|---|
| Step 2 | Click the user to whom you want to assign supervisor capability. The User Configuration page displays information about that user. In the Capabilities section, the left pane displays the
                                             list of assigned capabilities and the right pane displays the list of capabilities. |
| Step 3 | Using the left arrow, assign Supervisor capability. |
| Step 4 | Click Update to save your changes. |

| Step 1 | From the Unified CCXAdministration menu bar, choose Subsystems > RmCm > Teams . |
|---|---|
| Step 2 | Click Add New icon that displays in the tool bar in the upper left corner of the window or the Add New button at the bottom of the window. The Team Configuration page appears. |
| Step 3 | Enter the Team Name . |
| Step 4 | Select the Primary Supervisor from the drop-down list. |
| Step 5 | (Optional) Select the secondary supervisor name from the Available Supervisors list and use the arrow icon to move it into the Secondary Supervisors list. |
| Step 6 | (Optional) To add an agent to this team, select an agent name in the Available Resources list and use the arrow icon to move it into the Assigned Resources list. |
| Step 7 | (Optional) Select the CSQ name in the Available CSQs list and use the arrow icon to move it into the Assigned CSQs list to add the CSQ to this team. |
| Step 8 | In the Team Settings section, specify the following information: Parameter Name Parameter Value Global Settings Change Agent State to Not Ready when Agent Busy on Non ACD Line Radio button that enables the agent state to change from the Ready state to the Not Ready state when the monitored Non ACD
                                                         lines are used for Incoming or Outgoing calls. The options are: Enable—Enables the state change of the agent in the team. Disable (default)—Disables any state change of the agent in the team. Allow team settings to override global settings—A check box to override the global settings. The global settings is available
                                                               at System > System Parameters > Agent Settings . Note When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                     Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. Displays the global settings. Auto Answer Enables the incoming calls to be auto answered. The options are: Enable with Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                               the agent is in the Ready state in the Cisco Finesse desktop. A zip tone plays to alert the agent. Enable without Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                               the agent is in the Ready state in the Cisco Finesse desktop. The zip tone does not play to alert the agent. Disable (Default)—Auto answer is not enabled. Note To configure Change Agent State to Not Ready when Agent Busy on Non ACD Line at a team level, you must install UCCX 12.5(1) SU1 ES01. This functionality is applicable only for the agents and not for the supervisors of the team. | Parameter Name | Parameter Value | Global Settings | Change Agent State to Not Ready when Agent Busy on Non ACD Line | Radio button that enables the agent state to change from the Ready state to the Not Ready state when the monitored Non ACD
                                                         lines are used for Incoming or Outgoing calls. The options are: Enable—Enables the state change of the agent in the team. Disable (default)—Disables any state change of the agent in the team. Allow team settings to override global settings—A check box to override the global settings. The global settings is available
                                                               at System > System Parameters > Agent Settings . Note When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                     Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. | Note | When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                     Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. | Displays the global settings. | Auto Answer | Enables the incoming calls to be auto answered. The options are: Enable with Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                               the agent is in the Ready state in the Cisco Finesse desktop. A zip tone plays to alert the agent. Enable without Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                               the agent is in the Ready state in the Cisco Finesse desktop. The zip tone does not play to alert the agent. Disable (Default)—Auto answer is not enabled. |  | Note | To configure Change Agent State to Not Ready when Agent Busy on Non ACD Line at a team level, you must install UCCX 12.5(1) SU1 ES01. This functionality is applicable only for the agents and not for the supervisors of the team. |
| Parameter Name | Parameter Value | Global Settings |
| Change Agent State to Not Ready when Agent Busy on Non ACD Line | Radio button that enables the agent state to change from the Ready state to the Not Ready state when the monitored Non ACD
                                                         lines are used for Incoming or Outgoing calls. The options are: Enable—Enables the state change of the agent in the team. Disable (default)—Disables any state change of the agent in the team. Allow team settings to override global settings—A check box to override the global settings. The global settings is available
                                                               at System > System Parameters > Agent Settings . Note When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                     Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. | Note | When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                     Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. | Displays the global settings. |
| Note | When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                     Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. |
| Auto Answer | Enables the incoming calls to be auto answered. The options are: Enable with Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                               the agent is in the Ready state in the Cisco Finesse desktop. A zip tone plays to alert the agent. Enable without Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                               the agent is in the Ready state in the Cisco Finesse desktop. The zip tone does not play to alert the agent. Disable (Default)—Auto answer is not enabled. |  |
| Note | To configure Change Agent State to Not Ready when Agent Busy on Non ACD Line at a team level, you must install UCCX 12.5(1) SU1 ES01. This functionality is applicable only for the agents and not for the supervisors of the team. |
| Step 9 | Click Save to apply changes or Cancel to exit. |

| Parameter Name | Parameter Value | Global Settings |
|---|---|---|
| Change Agent State to Not Ready when Agent Busy on Non ACD Line | Radio button that enables the agent state to change from the Ready state to the Not Ready state when the monitored Non ACD
                                                         lines are used for Incoming or Outgoing calls. The options are: Enable—Enables the state change of the agent in the team. Disable (default)—Disables any state change of the agent in the team. Allow team settings to override global settings—A check box to override the global settings. The global settings is available
                                                               at System > System Parameters > Agent Settings . Note When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                     Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. | Note | When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                     Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. | Displays the global settings. |
| Note | When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                     Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. |
| Auto Answer | Enables the incoming calls to be auto answered. The options are: Enable with Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                               the agent is in the Ready state in the Cisco Finesse desktop. A zip tone plays to alert the agent. Enable without Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                               the agent is in the Ready state in the Cisco Finesse desktop. The zip tone does not play to alert the agent. Disable (Default)—Auto answer is not enabled. |  |

| Note | When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                     Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. |
|---|---|

| Note | To configure Change Agent State to Not Ready when Agent Busy on Non ACD Line at a team level, you must install UCCX 12.5(1) SU1 ES01. This functionality is applicable only for the agents and not for the supervisors of the team. |
|---|---|

| Step 1 | From the Unified CCXAdministration menu bar, choose Subsystems > RmCm > Teams . |
|---|---|
| Step 2 | Click a name in the Team Name column. The Team Configuration page appears. |
| Step 3 | Select the Primary Supervisor from the drop-down list. |
| Step 4 | (Optional) Select the secondary supervisor name from the Available Supervisors list and use the arrow icon to move it into the Secondary Supervisors list. To remove the secondary supervisor name from this team, select the supervisor name in the Secondary Supervisors list and use the arrow icon to move it into the Available Supervisors list. This supervisor now belongs to the default team. |
| Step 5 | (Optional) Select an agent name in the Available Resources list and use the arrow icon to move it into the Assigned Resources list to add an agent to this team. To remove an agent from this team, select an agent name in the Assigned Resources list and use the arrow icon to move it into the Available Resources list. This agent now belongs to the default team. |
| Step 6 | (Optional) Select the CSQ name in the Available CSQs list and use the arrow icon to move it into the Assigned CSQs list to add the CSQ to this team. To remove a CSQ from this team, select a CSQ name in the Assigned CSQs list and use the arrow icon to move it into the Available CSQs list. This CSQ now belongs to the default team. |
| Step 7 | In the Team Settings section, specify the following information: Parameter Name Parameter Value Global Settings Change Agent State to Not Ready when Agent Busy on Non ACD Line Radio button that enables the agent state to change from the Ready state to the Not Ready state when the monitored Non ACD
                                                         lines are used for Incoming or Outgoing calls. The options are: Enable—Enables the state change of the agent in the team. Disable (default)—Disables any state change of the agent in the team. Allow team settings to override global settings—A check box to override the global settings. The global settings are available
                                                               at System > System Parameters > Agent Settings . Note When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                     Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. Displays the global settings. Auto Answer Enables the incoming calls to be automatically answered. The options are: Enable with Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                               the agent is in the Ready state in the Cisco Finesse desktop. A zip tone plays to alert the agent. Enable without Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                               the agent is in the Ready state in the Cisco Finesse desktop. The zip tone does not play to alert the agent. Disable (Default)—Auto answer is not enabled. Note To configure Change Agent State to Not Ready when Agent Busy on Non ACD Line at a team level, you must install UCCX 12.5(1) SU1 ES01. | Parameter Name | Parameter Value | Global Settings | Change Agent State to Not Ready when Agent Busy on Non ACD Line | Radio button that enables the agent state to change from the Ready state to the Not Ready state when the monitored Non ACD
                                                         lines are used for Incoming or Outgoing calls. The options are: Enable—Enables the state change of the agent in the team. Disable (default)—Disables any state change of the agent in the team. Allow team settings to override global settings—A check box to override the global settings. The global settings are available
                                                               at System > System Parameters > Agent Settings . Note When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                     Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. | Note | When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                     Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. | Displays the global settings. | Auto Answer | Enables the incoming calls to be automatically answered. The options are: Enable with Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                               the agent is in the Ready state in the Cisco Finesse desktop. A zip tone plays to alert the agent. Enable without Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                               the agent is in the Ready state in the Cisco Finesse desktop. The zip tone does not play to alert the agent. Disable (Default)—Auto answer is not enabled. |  | Note | To configure Change Agent State to Not Ready when Agent Busy on Non ACD Line at a team level, you must install UCCX 12.5(1) SU1 ES01. |
| Parameter Name | Parameter Value | Global Settings |
| Change Agent State to Not Ready when Agent Busy on Non ACD Line | Radio button that enables the agent state to change from the Ready state to the Not Ready state when the monitored Non ACD
                                                         lines are used for Incoming or Outgoing calls. The options are: Enable—Enables the state change of the agent in the team. Disable (default)—Disables any state change of the agent in the team. Allow team settings to override global settings—A check box to override the global settings. The global settings are available
                                                               at System > System Parameters > Agent Settings . Note When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                     Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. | Note | When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                     Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. | Displays the global settings. |
| Note | When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                     Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. |
| Auto Answer | Enables the incoming calls to be automatically answered. The options are: Enable with Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                               the agent is in the Ready state in the Cisco Finesse desktop. A zip tone plays to alert the agent. Enable without Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                               the agent is in the Ready state in the Cisco Finesse desktop. The zip tone does not play to alert the agent. Disable (Default)—Auto answer is not enabled. |  |
| Note | To configure Change Agent State to Not Ready when Agent Busy on Non ACD Line at a team level, you must install UCCX 12.5(1) SU1 ES01. |
| Step 8 | Click Save or Update to apply changes, Cancel to exit or Delete to delete this team. |

| Parameter Name | Parameter Value | Global Settings |
|---|---|---|
| Change Agent State to Not Ready when Agent Busy on Non ACD Line | Radio button that enables the agent state to change from the Ready state to the Not Ready state when the monitored Non ACD
                                                         lines are used for Incoming or Outgoing calls. The options are: Enable—Enables the state change of the agent in the team. Disable (default)—Disables any state change of the agent in the team. Allow team settings to override global settings—A check box to override the global settings. The global settings are available
                                                               at System > System Parameters > Agent Settings . Note When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                     Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. | Note | When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                     Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. | Displays the global settings. |
| Note | When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                     Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. |
| Auto Answer | Enables the incoming calls to be automatically answered. The options are: Enable with Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                               the agent is in the Ready state in the Cisco Finesse desktop. A zip tone plays to alert the agent. Enable without Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                               the agent is in the Ready state in the Cisco Finesse desktop. The zip tone does not play to alert the agent. Disable (Default)—Auto answer is not enabled. |  |

| Note | When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                     Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. |
|---|---|

| Note | To configure Change Agent State to Not Ready when Agent Busy on Non ACD Line at a team level, you must install UCCX 12.5(1) SU1 ES01. |
|---|---|

| Step 1 | From the Unified CCXAdministration menu bar, choose Subsystems > RmCm > Teams . The Teams web page opens. |
|---|---|
| Step 2 | Click 
                                          			 the Delete icon beside the Team Name icon you want to
                                          			 delete. The system prompts you to confirm the delete. |
| Step 3 | Click OK . |