---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-73739a666a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_0100010.html
retrieved_at: 2026-08-16T17:31:44.565549+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure User Profiles

## Chapter: Configure User Profiles

# Configure User Profiles

## User Profile Overview

User profiles contain common directory number and device settings. You can configure different user profiles that contain
                              the most common directory number settings and device settings that your users require and then assign each user profile to
                              the users that require those settings. You can configure different user profiles for different groups of users in your company,
                              according to the phone line and phone setting requirements for each set of users.

For those end users who are enabled for self-provisioning, the phone and phone line settings from the user profile get applied
                              to any new phones that the user provisions. If the user is not enabled for self-provisioning, the user profile settings can
                              be applied to any new phones that the administrator provisions on behalf of the end user.

User profiles use settings from the following phone and phone line templates to build a profile for the end user:

Universal Line Template—a collection of common phone line settings that are typically assigned to a directory number. Universal
                                    line templates allow you to quickly configure phone lines for new directory numbers that get assigned to an end user.

Universal Device Template—a collection of common device settings that are typically assigned to a phone or other device. Universal
                                    device templates allow you to quickly configure new phones that get  assigned to an end user.

## User Profile Prerequisites

Before configuring your user profiles, make sure to plan how you are going to provision phones for your deployment. Decide
                           whether you are going to use self-provisioning to allow end users to provision their own phones.

## User Profile Configuration Task Flow

Step 1

Configure a Universal Line Template

Configure universal line templates with common settings that are typically applied to a directory number.

Step 2

Configure a Universal Device Template

Configure universal device templates with common settings that are typically applied to phones and other devices.

Step 3

Configure a User Profile

Assign the universal line and universal device templates to a user profile.

### Configure a
                           	 Universal Line Template

Universal Line Templates make it easy to apply common settings to newly assigned directory numbers. Configure different templates
                                 to meet the needs of different groups of users.

Step 1

In Cisco Unified CM Administration, choose User Management > User/Phone Add > Universal Line Template .

Step 2

Click Add
                                             				New .

Step 3

Configure the
                                          			 fields in the Universal Line Template Configuration window. See the
                                          			 online help for more information about the fields and their configuration
                                          			 options.

Step 4

If you are deploying Global Dial Plan Replication with alternate numbers expand the Enterprise Alternate Number and +E.164 Alternate Number sections and do the following:

Click the Add Enterprise Alternate Number button and/or Add +E.164 Alternate Number button.

Add the Number Mask that you want to use to assign to your alternate numbers. For example, a 4-digit extension might use 5XXXX as an enterprise
                                                number mask and 1972555XXXX as an +E.164 alternate number mask.

Assign the partition where you want to assign alternate numbers.

If you want to advertise this number via ILS, check the Advertise Globally via ILS check box. Note that if you are using advertised patterns to summarize a range of alternate numbers, you may not need to
                                                advertise individual alternate numbers.

Expand the PSTN Failover section and choose the Enterprise Number or +E.164 Alternate Number as the PSTN failover to use if normal call routing fails.

Step 5

Click Save .

### Configure a
                           	 Universal Device Template

Universal device templates make it easy to apply configuration settings to newly provisioned devices. The provisioned device
                                 uses the settings of the universal device template. You can configure different device templates to meet the needs of different
                                 groups of users. You can also assign the profiles that you’ve configured to this template.

Step 1

In Cisco Unified CM
                                          			 Administration, choose User
                                                				  Management > User/Phone Add > Universal Device
                                                				  Template .

Step 2

Click Add New .

Step 3

Enter the following mandatory fields:

Enter a Device Description for the template.

Select a Device Pool type from the drop-down list.

Select a Device Security Profile from the drop-down list.

Select a SIP Profile from the drop-down list.

Select a Phone Button Template from the drop-down list.

Step 4

Complete the remaining fields in the Universal Device Template Configuration window. For field descriptions, see the online help.

Step 5

Under Phone Settings , complete the following optional fields:

If you configured a Common Phone Profile , assign the profile.

If you configured a Common Device Configuration , assign the configuration.

If you configured a Feature Control Policy , assign the policy.

Step 6

Click Save .

### Configure a User
                           	 Profile

Assign universal line and universal device template to users through the User Profile. Configure multiple user profiles for
                                 different groups of users. You can also enable self-provisioning for users who use this service profile.

Step 1

From Cisco Unified CM Administration, choose User Management > User Settings > User Profile .

Step 2

Click Add
                                             				New .

Step 3

Enter a Name and Description for the user profile.

Step 4

Assign a Universal Device Template to apply to users' Desk
                                             				Phones , Mobile
                                             				and Desktop Devices , and Remote
                                             				Destination/Device Profiles .

Step 5

Assign a Universal Line Template to apply to the phone lines
                                          			 for users in this user profile.

Step 6

If you want
                                          			 the users in this user profile to be able to use the self-provisioning feature
                                          			 to provision their own phones, do the following:

Check the Allow End User to Provision their own phones check box.

In the Limit Provisioning once End User has this many phones field, enter a maximum number of phones the user is allowed to provision. The maximum is 20.

Step 7

If you want Cisco Jabber users who are associated with this user profile, to be able to use the Mobile and Remote Access feature,
                                          check the Enable Mobile and Remote Access check box.

By default, this check box is selected. When you uncheck this check box, the Client Policies section is disabled, and No Service client policy option is selected by default.

This setting is mandatory only for Cisco Jabber users whom are using OAuth Refresh Logins. Non-Jabber users do not need this
                                                               setting to be able to use Mobile and Remote Access. Mobile and Remote Access feature is applicable only for the Jabber Mobile
                                                               and Remote Access users and not to any other endpoints or clients.

Step 8

Assign the Jabber policies for this user profile. From the Desktop Client Policy , and Mobile Client Policy drop-down list, choose one of the following options:

- No Service—This policy disables access to all Cisco Jabber services.

- IM & Presence only—This policy enables only instant messaging and presence capabilities.

- IM & Presence, Voice and Video calls—This policy enables instant messaging, presence, voicemail, and conferencing capabilities
                                             for all users with audio or video devices. This is the default option.

Jabber desktop client includes Cisco Jabber for Windows users and Cisco Jabber for Mac users. Jabber mobile client includes
                                                         Cisco Jabber for iPad and iPhone users and Cisco Jabber for Android users.

Step 9

If you want the users in this user profile to set the maximum login time for Extension Mobility or Extension Mobility Cross
                                          Cluster through Cisco Unified Communications Self Care Portal, check the Allow End User to set their Extension Mobility maximum login time check box.

By default Allow End User to set their Extension Mobility maximum login time check box is unchecked.

Step 10

Click Save .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure a Universal Line Template | Configure universal line templates with common settings that are typically applied to a directory number. |
| Step 2 | Configure a Universal Device Template | Configure universal device templates with common settings that are typically applied to phones and other devices. |
| Step 3 | Configure a User Profile | Assign the universal line and universal device templates to a user profile. |

| Step 1 | In Cisco Unified CM Administration, choose User Management > User/Phone Add > Universal Line Template . |
|---|---|
| Step 2 | Click Add
                                             				New . |
| Step 3 | Configure the
                                          			 fields in the Universal Line Template Configuration window. See the
                                          			 online help for more information about the fields and their configuration
                                          			 options. |
| Step 4 | If you are deploying Global Dial Plan Replication with alternate numbers expand the Enterprise Alternate Number and +E.164 Alternate Number sections and do the following: Click the Add Enterprise Alternate Number button and/or Add +E.164 Alternate Number button. Add the Number Mask that you want to use to assign to your alternate numbers. For example, a 4-digit extension might use 5XXXX as an enterprise
                                                number mask and 1972555XXXX as an +E.164 alternate number mask. Assign the partition where you want to assign alternate numbers. If you want to advertise this number via ILS, check the Advertise Globally via ILS check box. Note that if you are using advertised patterns to summarize a range of alternate numbers, you may not need to
                                                advertise individual alternate numbers. Expand the PSTN Failover section and choose the Enterprise Number or +E.164 Alternate Number as the PSTN failover to use if normal call routing fails. |
| Step 5 | Click Save . |

| Step 1 | In Cisco Unified CM
                                          			 Administration, choose User
                                                				  Management > User/Phone Add > Universal Device
                                                				  Template . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Enter the following mandatory fields: Enter a Device Description for the template. Select a Device Pool type from the drop-down list. Select a Device Security Profile from the drop-down list. Select a SIP Profile from the drop-down list. Select a Phone Button Template from the drop-down list. |
| Step 4 | Complete the remaining fields in the Universal Device Template Configuration window. For field descriptions, see the online help. |
| Step 5 | Under Phone Settings , complete the following optional fields: If you configured a Common Phone Profile , assign the profile. If you configured a Common Device Configuration , assign the configuration. If you configured a Feature Control Policy , assign the policy. |
| Step 6 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose User Management > User Settings > User Profile . |
|---|---|
| Step 2 | Click Add
                                             				New . |
| Step 3 | Enter a Name and Description for the user profile. |
| Step 4 | Assign a Universal Device Template to apply to users' Desk
                                             				Phones , Mobile
                                             				and Desktop Devices , and Remote
                                             				Destination/Device Profiles . |
| Step 5 | Assign a Universal Line Template to apply to the phone lines
                                          			 for users in this user profile. |
| Step 6 | If you want
                                          			 the users in this user profile to be able to use the self-provisioning feature
                                          			 to provision their own phones, do the following: Check the Allow End User to Provision their own phones check box. In the Limit Provisioning once End User has this many phones field, enter a maximum number of phones the user is allowed to provision. The maximum is 20. |
| Step 7 | If you want Cisco Jabber users who are associated with this user profile, to be able to use the Mobile and Remote Access feature,
                                          check the Enable Mobile and Remote Access check box. Note By default, this check box is selected. When you uncheck this check box, the Client Policies section is disabled, and No Service client policy option is selected by default. This setting is mandatory only for Cisco Jabber users whom are using OAuth Refresh Logins. Non-Jabber users do not need this
                                                               setting to be able to use Mobile and Remote Access. Mobile and Remote Access feature is applicable only for the Jabber Mobile
                                                               and Remote Access users and not to any other endpoints or clients. | Note | By default, this check box is selected. When you uncheck this check box, the Client Policies section is disabled, and No Service client policy option is selected by default. This setting is mandatory only for Cisco Jabber users whom are using OAuth Refresh Logins. Non-Jabber users do not need this
                                                               setting to be able to use Mobile and Remote Access. Mobile and Remote Access feature is applicable only for the Jabber Mobile
                                                               and Remote Access users and not to any other endpoints or clients. |
| Note | By default, this check box is selected. When you uncheck this check box, the Client Policies section is disabled, and No Service client policy option is selected by default. This setting is mandatory only for Cisco Jabber users whom are using OAuth Refresh Logins. Non-Jabber users do not need this
                                                               setting to be able to use Mobile and Remote Access. Mobile and Remote Access feature is applicable only for the Jabber Mobile
                                                               and Remote Access users and not to any other endpoints or clients. |
| Step 8 | Assign the Jabber policies for this user profile. From the Desktop Client Policy , and Mobile Client Policy drop-down list, choose one of the following options: No Service—This policy disables access to all Cisco Jabber services. IM & Presence only—This policy enables only instant messaging and presence capabilities. IM & Presence, Voice and Video calls—This policy enables instant messaging, presence, voicemail, and conferencing capabilities
                                             for all users with audio or video devices. This is the default option. Note Jabber desktop client includes Cisco Jabber for Windows users and Cisco Jabber for Mac users. Jabber mobile client includes
                                                         Cisco Jabber for iPad and iPhone users and Cisco Jabber for Android users. | Note | Jabber desktop client includes Cisco Jabber for Windows users and Cisco Jabber for Mac users. Jabber mobile client includes
                                                         Cisco Jabber for iPad and iPhone users and Cisco Jabber for Android users. |
| Note | Jabber desktop client includes Cisco Jabber for Windows users and Cisco Jabber for Mac users. Jabber mobile client includes
                                                         Cisco Jabber for iPad and iPhone users and Cisco Jabber for Android users. |
| Step 9 | If you want the users in this user profile to set the maximum login time for Extension Mobility or Extension Mobility Cross
                                          Cluster through Cisco Unified Communications Self Care Portal, check the Allow End User to set their Extension Mobility maximum login time check box. Note By default Allow End User to set their Extension Mobility maximum login time check box is unchecked. | Note | By default Allow End User to set their Extension Mobility maximum login time check box is unchecked. |
| Note | By default Allow End User to set their Extension Mobility maximum login time check box is unchecked. |
| Step 10 | Click Save . |

| Note | By default, this check box is selected. When you uncheck this check box, the Client Policies section is disabled, and No Service client policy option is selected by default. This setting is mandatory only for Cisco Jabber users whom are using OAuth Refresh Logins. Non-Jabber users do not need this
                                                               setting to be able to use Mobile and Remote Access. Mobile and Remote Access feature is applicable only for the Jabber Mobile
                                                               and Remote Access users and not to any other endpoints or clients. |
|---|---|

| Note | Jabber desktop client includes Cisco Jabber for Windows users and Cisco Jabber for Mac users. Jabber mobile client includes
                                                         Cisco Jabber for iPad and iPhone users and Cisco Jabber for Android users. |
|---|---|

| Note | By default Allow End User to set their Extension Mobility maximum login time check box is unchecked. |
|---|---|