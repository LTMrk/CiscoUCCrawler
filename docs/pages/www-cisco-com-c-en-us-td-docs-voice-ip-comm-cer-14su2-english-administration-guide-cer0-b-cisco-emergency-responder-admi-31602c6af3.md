---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-14su2-english-administration-guide-cer0-b-cisco-emergency-responder-admi-31602c6af3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/14su2/english/administration/guide/cer0_b_cisco-emergency-responder-administration-guide-14su2/cer0_b_cisco-emergency-responder-administration-guide-1401_chapter_010111.html
retrieved_at: 2026-08-20T23:52:34.896886+00:00
---

Cisco Emergency Responder Administration Guide for Release 14 and SUs

# Cisco Emergency Responder Administration Guide for Release 14 and SUs

Updated: January 9, 2025

Chapter: Configure Cisco Emergency Responder Onsite Alerts

## Chapter: Configure Cisco Emergency Responder Onsite Alerts

# Configure Cisco Emergency Responder Onsite Alerts

## Cisco Emergency Responder Onsite Alerts

In this feature, Emergency Responder provides information about the emergency call as Onsite Alerts or notifications.

When someone makes an emergency call (that is routed through Cisco Emergency Responder), Cisco Emergency Responder offers
                           the ability route the emergency call to the public safety answering point (PSAP), and provides notification to onsite alert
                           (security) personnel. Notifications to onsite alert personnel are made via IP Phone message, a web-based alert on the Emergency
                           Responder end-user interface, and an email message or page if using email-based paging.

Depending on how your administrator sets up your system, you may receive an email alert that provides you with the caller's
                           extension, the time and date of the emergency call, the extension of the caller, the caller's alerting name, the ERL name,
                           and the phone location. You can choose to either view a specific emergency call alert (Web Alert) assigned to a particular
                           personnel or all the alerts in that location using the Cisco Emergency Responder User interface.

### Onsite Alerts Configuration Task Flow

Use the following task flow to guide you to configure the Cisco Emergency Responder Onsite Alert notifications.

Step 1

Configure Users

You can add users to the system and then assign them to user groups.

Step 2

Configure Users Groups

You can add user groups to the system and assign users and roles to each new user group.

Step 3

Configure Onsite Security Personnel

Identify your security or onsite alert personnel whom you can assign to your emergency response locations (ERLs).

Step 4

Configure Default ERL

Create emergency response locations (ERLs) to receive onsite alert email notifications for your area.

#### Configure Users

You can add users to the system and then assign them to user groups. The security levels for new users are determined by which
                                    user groups you assign them to.

In Emergency Responder, you can add a user either as a local user or a remote user. Remote users must use their Unified CM
                                    credentials or Active Directory credentials for authentication.

You can add users to either the primary and standby servers within a single Emergency Responder group. As access is allowed
                                    based on the combination of the user groups defined on the two servers, a user that is defined only on the primary server
                                    can log into the backup server.

##### Before you begin

Develop a list of users for each security level. You must know the user names of all onsite alert personnel, and you should
                                    determine who should have access to each of the administration security levels.

You can use this procedure to add or remove users. However, you cannot remove the administrative user created at the time
                                                of Emergency Responder installation.

Step 1

From the Cisco ER Administration web interface, select User Management > User .

Step 2

Click Add New User .

Step 3

Enter the required information in the User Name, Authentication Mode, Password, Confirm Password, and Unified CM Cluster fields.

Step 4

Click Insert .

Step 5

Repeat these steps to add additional users. For example, user1, user2.

Step 6

To assign security levels to the new users, you must add them to one or more user groups.

Step 7

Repeat this procedure on the other Emergency Responder server in the Emergency Responder server group.

To remove a user from a group, you must remove the user from both the groups in the primary and standby servers.

#### Configure Users Groups

You can add user groups to the system and assign users and roles to each new user group.

##### Before you begin

You should decide what additional user groups that you want to create and determine if any existing default user groups meet
                                    your needs.

Step 1

From the Cisco ER Administration web interface, select User Management > User Group .

Step 2

Click Add New User Group .

Step 3

Enter the User Group Name (required) and Description (optional) in the text boxes.

Step 4

Click Add Users .

Step 5

Enter search criteria to find a specific user and click Find , or click Find without any search criteria to display all configured users. The search results appear.

Step 6

Check the check box to the left of the user names to be added and click Add .

The User Name page closes and the added names appears in the Add Users to Group text box in the Add User Group page.

To delete users from this list, select the user name and click Remove Users .

Step 7

Click Add Roles .

Step 8

Enter search criteria to find a specific role and click Find , or click Find without any search criteria to display all configured roles. The search results appear.

Step 9

Check the check box to the left of the roles to be added and click Add .

The Role Names page closes and the added roles appear in the Add Roles to Group text box in the Add User Group page.

To delete roles from this list, select the user name and click Delete Roles .

Step 10

Click Insert to add the new user group to the system.

#### Configure Onsite Security Personnel

You must identify your security, or onsite alert personnel so that you can assign them to your Emergency Response locations
                                    (ERLs). If an emergency call is made from an ERL, the associated onsite alert personnel receive the following:

A web-based alert on the Cisco Emergency Responder end-user interface specific to emergency calls originating from the assigned
                                          ERL. They also can view all alerts in the system.

An email message. If you use an email-based paging address, the message results in a page.

A telephone call indicating that an emergency call was made.

In case an Onsite Security personnel is managing multiple sites (Emergency Response Locations); the Onsite Security personnel
                                    can configure Emergency Responder to get alerts from all the ERLs or only from specific ERL.

##### Before you begin

You must log into Emergency Responder with system administrator or ERL administrator authority.

Collect information about all of your onsite alert personnel, including names, telephone numbers, and email addresses. Also,
                                          develop a unique identification name for each, if you do not already have one readily available (such as badge number).

Step 1

From the Cisco ER Administration web interface, select ERL > Onsite Alert Settings .

Step 2

Enter the unique ID, name, telephone number, email address, and pager address, and available User Group of a security or onsite
                                             alert person.

Unique ID might be a badge number, email name, or other site-specific unique name. You use this ID to assign the person to
                                                an ERL, so ensure that you use a naming strategy useful to you.

You can use an email-based paging address for the email address, so that onsite alert personnel receive a page rather than
                                                an email.

Step 3

Click Insert .

Emergency Responder adds the person to the list of onsite personnel. Repeat until you define all security or onsite personnel.

Tip

To delete a person, first remove the person from all ERL definitions. Then, in the Available Onsite Alerts list on the Onsite
                                                                  Alerts Settings page, click the Delete icon corresponding to that person's record.

To modify onsite alert settings, click on the person's Onsite Alert ID, Onsite Alert Name, Onsite Alert Number, Onsite Alert
                                                                  Email Address, or Onsite Alert Pager Address in the Available Onsite Alerts list. The information for that person displays
                                                                  in the 'Modify Onsite Alert Contact' section of the page. Modify the information as needed and then click Update . You cannot change a person's Onsite Alert ID: to change the Onsite Alert ID, delete the person's entry and create a new
                                                                  one.

#### Configure Default ERL

In addition to supporting switch port-based ERLs, Emergency Responder supports IP subnet-based (Layer 3) ERLs. You can configure
                                    IP subnets and assign ERLs to the configured IP subnets; Cisco Emergency Responder then routes the emergency calls based on
                                    the configured IP subnet and ERL associations.

This feature is useful in environments where strict IP addressing rules are followed and cubicle-level location is not required,
                                    such as configurations with wireless phones.

##### Before you begin

You must have a system administrator or ERL administrator authority to access this page.

Step 1

From Cisco ER Administration web interface, select ERL Membership > IP Subnets .

Step 2

In the Find and List IP Subnets page, click Add New IP Subnet .

Step 3

At the Subnet ID field, enter the IP address of the IPv4 or IPv6 subnet that you want to define. For example,the subnet ID
                                             for IPv4 is 10.76.35.0.

IPv6 subnet is not supported.

Step 4

For IPv4 subnet, enter the mask of the subnet that you want to define, for example, 255.255.255.224 at the Subnet Mask field.

Step 5

In the ERL Name, enter a name for the specific ERL site.

Step 6

To select the ERL you want to assign to the subnet, click the Search ERL button next to the ERL Name field. The Find ERL page appears.

Step 7

Enter the ERL Search Parameters and click Find . The search results appear.

Step 8

Click the radio button next to the ERL that you want to assign to the subnet and click Select ERL . The Find ERL page closes.

Step 9

Click Insert to add the subnet.

A pop-up message requests that you perform a switch port update. You can do this after all the IP subnets have been added.

Step 10

To revert back to the last saved settings, click Cancel Changes .

### Onsite Alerts Email Example

```
EMERGENCY CALL DETAILS (Generated by CiscoER)
Caller Extension : 7975
Display Name : Test Phone
Zone/ERL : TestERL
Location :
Port Description :
Call Time : May 13, 2019 10:38:31 AM EDT
For detailed call information please refer to --  http://TestCERServer/ceruser
Emergency call Details Caller Extension:7975 Display Name :Test Phone Zone/ERL :TestERL LOCATION : Port Description : Call Time : May 13, 2019 10:38:31 AM EDT
```

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Users | You can add users to the system and then assign them to user groups. |
| Step 2 | Configure Users Groups | You can add user groups to the system and assign users and roles to each new user group. |
| Step 3 | Configure Onsite Security Personnel | Identify your security or onsite alert personnel whom you can assign to your emergency response locations (ERLs). |
| Step 4 | Configure Default ERL | Create emergency response locations (ERLs) to receive onsite alert email notifications for your area. |

| Note | You can use this procedure to add or remove users. However, you cannot remove the administrative user created at the time
                                                of Emergency Responder installation. |
|---|---|

| Step 1 | From the Cisco ER Administration web interface, select User Management > User . |
|---|---|
| Step 2 | Click Add New User . |
| Step 3 | Enter the required information in the User Name, Authentication Mode, Password, Confirm Password, and Unified CM Cluster fields. |
| Step 4 | Click Insert . |
| Step 5 | Repeat these steps to add additional users. For example, user1, user2. |
| Step 6 | To assign security levels to the new users, you must add them to one or more user groups. |
| Step 7 | Repeat this procedure on the other Emergency Responder server in the Emergency Responder server group. Note To remove a user from a group, you must remove the user from both the groups in the primary and standby servers. | Note | To remove a user from a group, you must remove the user from both the groups in the primary and standby servers. |
| Note | To remove a user from a group, you must remove the user from both the groups in the primary and standby servers. |

| Note | To remove a user from a group, you must remove the user from both the groups in the primary and standby servers. |
|---|---|

| Step 1 | From the Cisco ER Administration web interface, select User Management > User Group . |
|---|---|
| Step 2 | Click Add New User Group . |
| Step 3 | Enter the User Group Name (required) and Description (optional) in the text boxes. |
| Step 4 | Click Add Users . |
| Step 5 | Enter search criteria to find a specific user and click Find , or click Find without any search criteria to display all configured users. The search results appear. |
| Step 6 | Check the check box to the left of the user names to be added and click Add . The User Name page closes and the added names appears in the Add Users to Group text box in the Add User Group page. Note To delete users from this list, select the user name and click Remove Users . | Note | To delete users from this list, select the user name and click Remove Users . |
| Note | To delete users from this list, select the user name and click Remove Users . |
| Step 7 | Click Add Roles . |
| Step 8 | Enter search criteria to find a specific role and click Find , or click Find without any search criteria to display all configured roles. The search results appear. |
| Step 9 | Check the check box to the left of the roles to be added and click Add . The Role Names page closes and the added roles appear in the Add Roles to Group text box in the Add User Group page. Note To delete roles from this list, select the user name and click Delete Roles . | Note | To delete roles from this list, select the user name and click Delete Roles . |
| Note | To delete roles from this list, select the user name and click Delete Roles . |
| Step 10 | Click Insert to add the new user group to the system. |

| Note | To delete users from this list, select the user name and click Remove Users . |
|---|---|

| Note | To delete roles from this list, select the user name and click Delete Roles . |
|---|---|

| Step 1 | From the Cisco ER Administration web interface, select ERL > Onsite Alert Settings . |
|---|---|
| Step 2 | Enter the unique ID, name, telephone number, email address, and pager address, and available User Group of a security or onsite
                                             alert person. Unique ID might be a badge number, email name, or other site-specific unique name. You use this ID to assign the person to
                                                an ERL, so ensure that you use a naming strategy useful to you. You can use an email-based paging address for the email address, so that onsite alert personnel receive a page rather than
                                                an email. |
| Step 3 | Click Insert . Emergency Responder adds the person to the list of onsite personnel. Repeat until you define all security or onsite personnel. Tip To delete a person, first remove the person from all ERL definitions. Then, in the Available Onsite Alerts list on the Onsite
                                                                  Alerts Settings page, click the Delete icon corresponding to that person's record. To modify onsite alert settings, click on the person's Onsite Alert ID, Onsite Alert Name, Onsite Alert Number, Onsite Alert
                                                                  Email Address, or Onsite Alert Pager Address in the Available Onsite Alerts list. The information for that person displays
                                                                  in the 'Modify Onsite Alert Contact' section of the page. Modify the information as needed and then click Update . You cannot change a person's Onsite Alert ID: to change the Onsite Alert ID, delete the person's entry and create a new
                                                                  one. | Tip | To delete a person, first remove the person from all ERL definitions. Then, in the Available Onsite Alerts list on the Onsite
                                                                  Alerts Settings page, click the Delete icon corresponding to that person's record. To modify onsite alert settings, click on the person's Onsite Alert ID, Onsite Alert Name, Onsite Alert Number, Onsite Alert
                                                                  Email Address, or Onsite Alert Pager Address in the Available Onsite Alerts list. The information for that person displays
                                                                  in the 'Modify Onsite Alert Contact' section of the page. Modify the information as needed and then click Update . You cannot change a person's Onsite Alert ID: to change the Onsite Alert ID, delete the person's entry and create a new
                                                                  one. |
| Tip | To delete a person, first remove the person from all ERL definitions. Then, in the Available Onsite Alerts list on the Onsite
                                                                  Alerts Settings page, click the Delete icon corresponding to that person's record. To modify onsite alert settings, click on the person's Onsite Alert ID, Onsite Alert Name, Onsite Alert Number, Onsite Alert
                                                                  Email Address, or Onsite Alert Pager Address in the Available Onsite Alerts list. The information for that person displays
                                                                  in the 'Modify Onsite Alert Contact' section of the page. Modify the information as needed and then click Update . You cannot change a person's Onsite Alert ID: to change the Onsite Alert ID, delete the person's entry and create a new
                                                                  one. |

| Tip | To delete a person, first remove the person from all ERL definitions. Then, in the Available Onsite Alerts list on the Onsite
                                                                  Alerts Settings page, click the Delete icon corresponding to that person's record. To modify onsite alert settings, click on the person's Onsite Alert ID, Onsite Alert Name, Onsite Alert Number, Onsite Alert
                                                                  Email Address, or Onsite Alert Pager Address in the Available Onsite Alerts list. The information for that person displays
                                                                  in the 'Modify Onsite Alert Contact' section of the page. Modify the information as needed and then click Update . You cannot change a person's Onsite Alert ID: to change the Onsite Alert ID, delete the person's entry and create a new
                                                                  one. |
|---|---|

| Note | Subnet-based tracking is limited by the IP subnet addressing plan. It cannot distinguish location within a same IP Subnet. |
|---|---|

| Step 1 | From Cisco ER Administration web interface, select ERL Membership > IP Subnets . |
|---|---|
| Step 2 | In the Find and List IP Subnets page, click Add New IP Subnet . |
| Step 3 | At the Subnet ID field, enter the IP address of the IPv4 or IPv6 subnet that you want to define. For example,the subnet ID
                                             for IPv4 is 10.76.35.0. Note IPv6 subnet is not supported. | Note | IPv6 subnet is not supported. |
| Note | IPv6 subnet is not supported. |
| Step 4 | For IPv4 subnet, enter the mask of the subnet that you want to define, for example, 255.255.255.224 at the Subnet Mask field. |
| Step 5 | In the ERL Name, enter a name for the specific ERL site. |
| Step 6 | To select the ERL you want to assign to the subnet, click the Search ERL button next to the ERL Name field. The Find ERL page appears. |
| Step 7 | Enter the ERL Search Parameters and click Find . The search results appear. |
| Step 8 | Click the radio button next to the ERL that you want to assign to the subnet and click Select ERL . The Find ERL page closes. |
| Step 9 | Click Insert to add the subnet. A pop-up message requests that you perform a switch port update. You can do this after all the IP subnets have been added. |
| Step 10 | To revert back to the last saved settings, click Cancel Changes . |

| Note | IPv6 subnet is not supported. |
|---|---|