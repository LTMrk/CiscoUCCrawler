---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su2-maintain-and-operate-guid-ec80b7214d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su2/maintain_and_operate/guide/uccx_b_1251su2_admin-and-operations-guide/uccx_b_12_5_2admin-and-operations-guide_chapter_01110.html
retrieved_at: 2026-08-16T21:36:33.235977+00:00
---

Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1) SU2

# Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1) SU2

Updated: April 11, 2022

Chapter: Cisco Unified Contact Center Express Supervisor and User Options Plug-Ins

## Chapter: Cisco Unified Contact Center Express Supervisor and User Options Plug-Ins

# Cisco Unified Contact Center Express Supervisor and User Options Plug-Ins

## About User
                        	 Management

In earlier
                              		  versions of Unified CCX, many user parameters like user ID, password, and pin
                              		  were configured from the Unified CM Administrator. Some Unified CCX-related user parameters were configured through
                              		  the Unified CCX Administration.

In Unified
                              		  CCX, all Unified CCX user roles (capabilities) are consolidated into one User
                              		  Configuration area.

Any changes made
                                          			 to the user privileges for the Unified CCX user roles after the backup
                                          			 operation is performed are not restored.

The Unified CM user
                              		  details are stored in the Unified CM database.

## About Unified CCX User Capabilities

The capability for each user refers to the Unified CCX access
                              		  level assigned for each user. Unified CCX users can be assigned to one of the
                              		  following four roles (or capabilities):

Administrator

Supervisor

Historical Report User

Agent

Each of these roles are described in this section.

### Administrator Privileges

A Unified CCX Administrator is a user with complete access to
                                 		  the Unified CCX Administration and has the authority to configure the entire
                                 		  system. An Administrator can also be assigned a combination of other roles.

The Administrator can turn on/off the authority of a
                                 		  Supervisor to manage the teams and agents.

### Supervisor
                           	 Privileges

Supervisors
                                 		  can additionally modify and view skills, view the list of all teams for which
                                 		  this user is the supervisor, view the skills, CSQs, and resource groups
                                 		  configured in this system, view and manage resources, and configure the teams
                                 		  that they are to manage.

Unified CCX
                                 		  provides three types of supervisors:

Application Supervisor : A
                                       				basic supervisor role applicable to a Unified CCX Application server without a
                                       				Unified CCX license. An application supervisor can only view reports.

ACD Supervisor : A
                                       				supervisor with an agent role. This role is applicable to a Unified CCX
                                       				Application server with any Unified CCX license. An ACD supervisor can administer teams/agents and also
                                       				view reports. Thus Unified CCX enables dynamic reskilling, the ability by which
                                       				an ACD supervisor can add or remove skills from an agent without an
                                       				administrator privilege.

Depending
                                 		  on the license allowed, Unified CCX Supervisors have the following privileges:

View reports
                                       				through Unified Intelligence Center web client.

View agents and
                                       				CSQ being monitored. This is only for a remote Supervisor.

View the list of
                                       				all teams for which this user is the Supervisor.

Configure the
                                       				teams managed by the Supervisor.

View the skills,
                                       				CSQs, and Resource Groups configured in this system.

The RmCm menu can
                                             			 be viewed by the Supervisor only when any of the following two options are
                                             			 selected as the parameter value for the Supervisor Access field located in System > System
                                                   				  Parameters > Application Parameters :

- Access to all
                                             			 Teams

- Access to
                                             			 Supervisor's Teams only

View and manage
                                       				all the resources.

### Historical Report User Privileges

A user with a historical report role can view various
                                 		  historical reports. The number and types of reports allowed to be viewed
                                 		  depends on the licenses available on a given Unified CCX system.

### Agent Privileges

An agent capability is only available with a Unified CCX license.

Unified CM users in
                                 		  Unified CCX are assigned an agent role when an agent extension is associated to
                                 		  the user in the Unified CM User Configuration page.
                                 		  Consequently, this role can only be assigned or removed for the user using Unified CM Administrator End User
                                 		  Configuration web page. These users can not be assigned or removed in Unified
                                 		  CCX Administration.

## Unified CCX Supervisor Web Interface

Use the Unified CCX Supervisor web page to:

View and monitor permitted agents

View and monitor permitted CSQs

Access real-time reports, tools, and settings

### Access Unified CCX
                           	 Supervisor Web Page

To
                                 		  access the Unified CCX Supervisor web page, perform the following steps:

Step 1

Ensure
                                          			 supervisor capability is assigned to the user designated as supervisor (see Supervisor Privileges and User View Submenu ).

If the
                                                         				  supervisor is assigned administrator capability as well, the Unified CCX
                                                         				  Administration window is opened instead of the Supervisor web page.

Step 2

From a web
                                          			 browser on any computer on your network, enter the following case-sensitive
                                          			 URL:

```
https://<servername>/appadmin
```

In this
                                             				example, replace <servername> with the hostname or IP address of
                                             				the required Unified CCX server.

Tip

If you have already accessed the Unified CCX Administration application or Supervisor web page in the browser, be sure to
                                                         logout from the current session using Logout link displayed in the top right corner of any Cisco Unified CCX Administration web page or System > Logout and login with respective user credentials.

User IDs are case-sensitive when logging into the Unified CCX Administration web interface. To make them case-insensitive,
                                                         you must install 12.5(1) SU1 ES02.

The Unified
                                             				CCX Supervisor web page appears.

## Unified CCX User Options Web Interface

Use the Unified CCX User Options web page to perform:

Unified CCX downloads

Alternate pronunciations for call by name

Access the Unified CM User web page

### Access Unified CCX
                           	 User Options Web Page

To access the Unified CCX User Options web page, perform the following steps:

Step 1

From the Unified CCXAdministration, enter https ://<Cisco Unified CCX IP address>/ appuser/appusermain .

Step 2

If prompted to
                                          			 do so, enter your User ID and Password.

The Unified
                                             				CCX User Options web page appears.

Only Unified CM users are allowed to log in.

Step 3

When finished,
                                          			 click Logout .

### Add Alternative Pronunciations

Alternative Pronunciations for Call by Name is an
                                 		  independent feature located on the Unified CCX User Options Welcome web page.
                                 		  This feature lets you add one or more alternate pronunciations for your first
                                 		  or last name and is useful if callers might refer to you by more than one name.
                                 		  For example, if your first name is Bob, you might add the alternate
                                 		  pronunciations "Bob" and "Bobby" . Similarly, if your last name is Xhu, you might add the
                                 		  alternate pronunciation "Xhu" .

To access the Alternative Pronunciations for Call by Name
                                 		  web page, perform the following steps:

Step 1

In the Cisco Unified CCX User Options Welcome web page, choose User
                                                				  Options > Alternative Pronunciations for Call by
                                                				  Name .

The Alternate Pronunciations web page appears.

Step 2

In the First Name field, you can enter an alternate pronunciation
                                          			 of your first name. For example, if your name is "Mary," you might enter "Maria."

Step 3

Click Add>> .

The name moves to a list of alternate first name pronunciations.

Step 4

Repeat Steps 2 and 3 as needed to add other alternate
                                          			 pronunciations.

To remove an alternate pronunciation for your first name, click
                                             				the alternate pronunciation and then click Remove .

Step 5

In the Last Name field, you can enter an alternate pronunciation
                                          			 of your last name. For example, if your last name is "Smith," you might enter "Smitty."

Step 6

Click Add>> .

The name moves to a list of alternate last name pronunciations.

Step 7

Repeat Steps 5 and 6 as needed to add other alternate
                                          			 pronunciations.

To remove an alternate pronunciation of your last name, click the
                                             				alternate pronunciation and then click Remove .

Step 8

Click Save to apply the changes.

### Access Unified CM User Options Page

To access the Unified CM User Options web page,
                                 		  perform the following steps:

Step 1

In the Unified CCX User Options Welcome web page, choose User Options > Cisco Unified CM User
                                                				  Page .

The Unified CM User Options Log On
                                             				dialog box appears.

Step 2

Enter your Unified CM user ID and password,
                                          			 and then click Log On .

The Unified CM User Options web
                                             				page appears.

Step 3

Click the option you want.

Step 4

When finished, click Logout .

| Note | Any changes made
                                          			 to the user privileges for the Unified CCX user roles after the backup
                                          			 operation is performed are not restored. |
|---|---|

| Note | The RmCm menu can
                                             			 be viewed by the Supervisor only when any of the following two options are
                                             			 selected as the parameter value for the Supervisor Access field located in System > System
                                                   				  Parameters > Application Parameters : - Access to all
                                             			 Teams - Access to
                                             			 Supervisor's Teams only |
|---|---|

| Note | An agent capability is only available with a Unified CCX license. |
|---|---|

| Step 1 | Ensure
                                          			 supervisor capability is assigned to the user designated as supervisor (see Supervisor Privileges and User View Submenu ). Note If the
                                                         				  supervisor is assigned administrator capability as well, the Unified CCX
                                                         				  Administration window is opened instead of the Supervisor web page. | Note | If the
                                                         				  supervisor is assigned administrator capability as well, the Unified CCX
                                                         				  Administration window is opened instead of the Supervisor web page. |
|---|---|---|---|
| Note | If the
                                                         				  supervisor is assigned administrator capability as well, the Unified CCX
                                                         				  Administration window is opened instead of the Supervisor web page. |
| Step 2 | From a web
                                          			 browser on any computer on your network, enter the following case-sensitive
                                          			 URL: https://<servername>/appadmin In this
                                             				example, replace <servername> with the hostname or IP address of
                                             				the required Unified CCX server. Tip If you have already accessed the Unified CCX Administration application or Supervisor web page in the browser, be sure to
                                                         logout from the current session using Logout link displayed in the top right corner of any Cisco Unified CCX Administration web page or System > Logout and login with respective user credentials. User IDs are case-sensitive when logging into the Unified CCX Administration web interface. To make them case-insensitive,
                                                         you must install 12.5(1) SU1 ES02. The Unified
                                             				CCX Supervisor web page appears. | Tip | If you have already accessed the Unified CCX Administration application or Supervisor web page in the browser, be sure to
                                                         logout from the current session using Logout link displayed in the top right corner of any Cisco Unified CCX Administration web page or System > Logout and login with respective user credentials. User IDs are case-sensitive when logging into the Unified CCX Administration web interface. To make them case-insensitive,
                                                         you must install 12.5(1) SU1 ES02. |
| Tip | If you have already accessed the Unified CCX Administration application or Supervisor web page in the browser, be sure to
                                                         logout from the current session using Logout link displayed in the top right corner of any Cisco Unified CCX Administration web page or System > Logout and login with respective user credentials. User IDs are case-sensitive when logging into the Unified CCX Administration web interface. To make them case-insensitive,
                                                         you must install 12.5(1) SU1 ES02. |

| Note | If the
                                                         				  supervisor is assigned administrator capability as well, the Unified CCX
                                                         				  Administration window is opened instead of the Supervisor web page. |
|---|---|

| Tip | If you have already accessed the Unified CCX Administration application or Supervisor web page in the browser, be sure to
                                                         logout from the current session using Logout link displayed in the top right corner of any Cisco Unified CCX Administration web page or System > Logout and login with respective user credentials. User IDs are case-sensitive when logging into the Unified CCX Administration web interface. To make them case-insensitive,
                                                         you must install 12.5(1) SU1 ES02. |
|---|---|

| Step 1 | From the Unified CCXAdministration, enter https ://<Cisco Unified CCX IP address>/ appuser/appusermain . |
|---|---|
| Step 2 | If prompted to
                                          			 do so, enter your User ID and Password. The Unified
                                             				CCX User Options web page appears. Note Only Unified CM users are allowed to log in. | Note | Only Unified CM users are allowed to log in. |
| Note | Only Unified CM users are allowed to log in. |
| Step 3 | When finished,
                                          			 click Logout . |

| Note | Only Unified CM users are allowed to log in. |
|---|---|

| Step 1 | In the Cisco Unified CCX User Options Welcome web page, choose User
                                                				  Options > Alternative Pronunciations for Call by
                                                				  Name . The Alternate Pronunciations web page appears. |
|---|---|
| Step 2 | In the First Name field, you can enter an alternate pronunciation
                                          			 of your first name. For example, if your name is "Mary," you might enter "Maria." |
| Step 3 | Click Add>> . The name moves to a list of alternate first name pronunciations. |
| Step 4 | Repeat Steps 2 and 3 as needed to add other alternate
                                          			 pronunciations. To remove an alternate pronunciation for your first name, click
                                             				the alternate pronunciation and then click Remove . |
| Step 5 | In the Last Name field, you can enter an alternate pronunciation
                                          			 of your last name. For example, if your last name is "Smith," you might enter "Smitty." |
| Step 6 | Click Add>> . The name moves to a list of alternate last name pronunciations. |
| Step 7 | Repeat Steps 5 and 6 as needed to add other alternate
                                          			 pronunciations. To remove an alternate pronunciation of your last name, click the
                                             				alternate pronunciation and then click Remove . |
| Step 8 | Click Save to apply the changes. |

| Step 1 | In the Unified CCX User Options Welcome web page, choose User Options > Cisco Unified CM User
                                                				  Page . The Unified CM User Options Log On
                                             				dialog box appears. |
|---|---|
| Step 2 | Enter your Unified CM user ID and password,
                                          			 and then click Log On . The Unified CM User Options web
                                             				page appears. |
| Step 3 | Click the option you want. |
| Step 4 | When finished, click Logout . |