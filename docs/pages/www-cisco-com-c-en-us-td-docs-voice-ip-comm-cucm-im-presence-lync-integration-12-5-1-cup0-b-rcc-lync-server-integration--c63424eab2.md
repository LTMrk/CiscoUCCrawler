---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-lync-integration-12-5-1-cup0-b-rcc-lync-server-integration--c63424eab2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/lync_integration/12_5_1/cup0_b_rcc-lync-server-integration-1251/cup0_b_rcc-lync-server-integration-1251_chapter_010.html
retrieved_at: 2026-08-16T17:28:43.272980+00:00
---

Remote Call Control with Microsoft Lync Server for IM and Presence Service, Release 12.5(1)

# Remote Call Control with Microsoft Lync Server for IM and Presence Service, Release 12.5(1)

Updated: January 23, 2019

Chapter: Cisco Unified Communications Manager Server Setup

## Chapter: Cisco Unified Communications Manager Server Setup

# Cisco Unified Communications Manager Server Setup

Note that because menu options and parameters may vary for different Cisco Unified Communications Manager releases, see the Cisco Unified Communications Manager documentation appropriate to your release.

## Cisco Unified Communications Manager User and Device Setup

Before you configure Cisco Unified Communications Manager for integration with Microsoft Lync , you need to complete the user and device configuration on Cisco Unified Communications Manager . You need to configure the phone devices, configure the users, and then associate a device with each user.

You also need to associate a line to a device, or for users of the Extension Mobility feature, to a device profile. This association
                              forms a line appearance. When a user is associated to the device or to a device profile, the line appearance is associated
                              to the user.

Task

Menu path

Configure the phone devices, and associate a primary extension with each device

Cisco Unified Communications Manager Administration > Device > Phone Phone

Configure the users, and associate a device with each user

Cisco Unified Communications Manager Administration > User Management > End User

Associate a user with a line appearance

Cisco Unified Communications Manager Administration > Device > Phone

### What To Do Next

Add Users to a Standard CCM Access Control Group

## Add Users to a Standard CCM Access Control Group

### Before you begin

Make sure you have completed the prerequisite user and device configuration on Cisco Unified Communications Manager .

Select Cisco Unified Communications Manager Administration > User Management > User Settings > Access Control Group .

Select Find .

Select Standard CCM End Users .

Select Add End Users to Group .

Select the end user to add to the Standard CCM access control group.

Select Add Selected .

Select Save .

### What to do next

Set Up CTI Gateway Application User

## Set Up CTI Gateway Application User

Complete the following procedure to configure an application user for the CTI Gateway.

Select Cisco Unified Communications Manager Administration > User Management > Application User .

Select Add New .

Enter an application user name in the User ID field.

### Example:

Enter a password for this application user, and confirm the password.

Select Save .

### What to do next

Add Application User to CTI-Enabled Access Control Group

## Add Application User to CTI-Enabled Access Control Group

Complete the following procedure to add the application user to a CTI-enabled access control group.

### Before you begin

Configure an application user for the CTI Gateway.

Select Cisco Unified Communications Manager Administration > User
                                             				  Management > User Settings > Access Control Group .

Select Find .

Select Standard CTI Enabled .

Select Add App Users to Group .

Select the application user that you created for the CTI Gateway.

Select Add Selected .

Select Save .

### What to do next

Assign CTI Device Control to Application User

## Assign CTI Device Control to Application User

### Before you begin

Configure an application user for the CTI gateway.

Select Cisco Unified Communications Manager Administration > User
                                             				  Management > User Settings > Access Control Group .

Select Find .

Select Standard CTI Allow Control of All Devices . 
                                       		  If you are deploying an RT model of Cisco Unified IP phones,
                                       			 select Standard CTI Allow Control of Phones supporting Connected
                                          				Xfer and conf .

Select Add App Users to Group .

Select the application user that you created for the CTI Gateway.

Select Add Selected .

## Set Up Dial Rules

A dial rule must be set up to strip the + prefix coming from the Lync server. If this is not done, the Cisco Unified Communications Manager will not find the Line URI and the result is a failed call attempt.

You perform the following configuration only if users are provisioned with E.164 numbers. If both users and IP phones are
                                          provisioned with E.164 numbers, then there is no need to set up an application dial rule to strip the + prefix.

Select Cisco Unified Communications Manager Administration > Call Routing > Dial Rules > Application Dial Rules > Add New .

Enter a name and a description for the dial rule.

In the Number Begins With field, enter + .

In the Number of Digits field, enter 12 to support the following number format: xxx-xxx-xxxx.

In the Total Digits to be Removed field, enter 1 .

This will ensure that the + prefix will be stripped because digits are always stripped from left to right.

Select Save .

### What to do next

IM and Presence Service Node Setup

| Note | Note that because menu options and parameters may vary for different Cisco Unified Communications Manager releases, see the Cisco Unified Communications Manager documentation appropriate to your release. |
|---|---|

| Task | Menu path |
|---|---|
| Configure the phone devices, and associate a primary extension with each device | Cisco Unified Communications Manager Administration > Device > Phone Phone |
| Configure the users, and associate a device with each user | Cisco Unified Communications Manager Administration > User Management > End User |
| Associate a user with a line appearance | Cisco Unified Communications Manager Administration > Device > Phone |

| Step 1 | Select Cisco Unified Communications Manager Administration > User Management > User Settings > Access Control Group . |
|---|---|
| Step 2 | Select Find . |
| Step 3 | Select Standard CCM End Users . |
| Step 4 | Select Add End Users to Group . |
| Step 5 | Select the end user to add to the Standard CCM access control group. |
| Step 6 | Select Add Selected . |
| Step 7 | Select Save . |

| Step 1 | Select Cisco Unified Communications Manager Administration > User Management > Application User . |
|---|---|
| Step 2 | Select Add New . |
| Step 3 | Enter an application user name in the User ID field. Example: CtiGW |
| Step 4 | Enter a password for this application user, and confirm the password. |
| Step 5 | Select Save . |

| Step 1 | Select Cisco Unified Communications Manager Administration > User
                                             				  Management > User Settings > Access Control Group . |
|---|---|
| Step 2 | Select Find . |
| Step 3 | Select Standard CTI Enabled . |
| Step 4 | Select Add App Users to Group . |
| Step 5 | Select the application user that you created for the CTI Gateway. |
| Step 6 | Select Add Selected . |
| Step 7 | Select Save . |

| Caution | Do not add devices as controlled devices to the application user because the role "Standard CTI Allow Control of All Devices"
                                          gives the application user sufficient privileges to control any Cisco Unified Communications Manager device. Adding devices
                                          as controlled devices to the application user can negatively impact Cisco Unified Communications Manager performance because
                                          Cisco Unified Communications Manager does not support a single user controlling a large number of devices in this manner. |
|---|---|

| Step 1 | Select Cisco Unified Communications Manager Administration > User
                                             				  Management > User Settings > Access Control Group . |
|---|---|
| Step 2 | Select Find . |
| Step 3 | Select Standard CTI Allow Control of All Devices . 
                                       		  If you are deploying an RT model of Cisco Unified IP phones,
                                       			 select Standard CTI Allow Control of Phones supporting Connected
                                          				Xfer and conf . |
| Step 4 | Select Add App Users to Group . |
| Step 5 | Select the application user that you created for the CTI Gateway. |
| Step 6 | Select Add Selected . |

| Note | You perform the following configuration only if users are provisioned with E.164 numbers. If both users and IP phones are
                                          provisioned with E.164 numbers, then there is no need to set up an application dial rule to strip the + prefix. |
|---|---|

| Step 1 | Select Cisco Unified Communications Manager Administration > Call Routing > Dial Rules > Application Dial Rules > Add New . |
|---|---|
| Step 2 | Enter a name and a description for the dial rule. |
| Step 3 | In the Number Begins With field, enter + . |
| Step 4 | In the Number of Digits field, enter 12 to support the following number format: xxx-xxx-xxxx. |
| Step 5 | In the Total Digits to be Removed field, enter 1 . This will ensure that the + prefix will be stripped because digits are always stripped from left to right. |
| Step 6 | Select Save . |