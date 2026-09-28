---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-fbac1e487a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_0100100.html
retrieved_at: 2026-08-16T17:31:52.900931+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure Feature Group Template

## Chapter: Configure Feature Group Template

# Configure Feature Group Template

## Feature Group Template Overview

Feature group templates help you deploy your end users with configured phones and phone lines. Feature group templates allow
                              you to assign common phone, phone line, and service settings to all users who are assigned that feature group template. If
                              you have also enabled self-provisioning for your end users, the feature group template allows your users to quickly provision
                              and set up their phones with the desired phone, phone line and services settings.

The feature group template configuration includes the following profiles that you can assign to the feature group template:

User Profile—contains a set of common phone and phone line settings. You must configure the user profile with a universal
                                    line template, which assigns the common phone line settings, and a universal device template, which assigns the common phone
                                    settings. These templates assist users who are set up for self-provisioning to configure their own phones.

Service Profile—contains a group of common settings for Unified Communications services such as conferencing and directory
                                    services.

When you configure a feature group template to include a user profile and service profile and then assign that feature group
                              template to an end user, the  user profile and service profile settings propagate through to any new phones that the end user
                              provisions.

If you are deploying the IM and Presence Service, you can use the feature group template to enable LDAP-synchronized users
                              with instant messaging and presence capability.

## Feature Group Template Prerequisites

Before you configure a feature group template, configure a user profile and service profile for your end users.

User Profile Configuration Task Flow

Service Profile Configuration Task Flow

## Configure a
                        	 Feature Group Template

Feature group templates aid in your system deployment by helping you to quickly configure phones, lines, and features for
                              your provisioned users. If you are syncing users from a company LDAP directory, configure a feature group template with the
                              User Profile and Service Profile that you want users synced from the directory to use. You can also enable the IM and Presence
                              Service for synced users through this template.

Step 1

In Cisco
                                       			 Unified CM Administration, choose User
                                             				  Management > User/Phone Add > Feature Group
                                             				  Template .

Step 2

Click Add
                                          				New .

Step 3

Enter a Name and Description for the Feature Group Template.

Step 4

Check the Home Cluster check box if you want to use the local cluster as the home cluster for all users whom use this template.

Step 5

Check the Enable User for Unified CM IM and Presence check box to allow users whom use this template to exchange instant messaging and presence information.

Step 6

From the drop-down list, select a Services Profile and User Profile .

Step 7

Complete the
                                       			 remaining fields in the Feature
                                          				Group Template Configuration window. Refer to the online help for
                                       			 field descriptions.

Step 8

Click Save .

### What to do next

Associate the feature group template with an LDAP directory sync to apply the settings from the template to synchronized end
                              users.

| Step 1 | In Cisco
                                       			 Unified CM Administration, choose User
                                             				  Management > User/Phone Add > Feature Group
                                             				  Template . |
|---|---|
| Step 2 | Click Add
                                          				New . |
| Step 3 | Enter a Name and Description for the Feature Group Template. |
| Step 4 | Check the Home Cluster check box if you want to use the local cluster as the home cluster for all users whom use this template. |
| Step 5 | Check the Enable User for Unified CM IM and Presence check box to allow users whom use this template to exchange instant messaging and presence information. |
| Step 6 | From the drop-down list, select a Services Profile and User Profile . |
| Step 7 | Complete the
                                       			 remaining fields in the Feature
                                          				Group Template Configuration window. Refer to the online help for
                                       			 field descriptions. |
| Step 8 | Click Save . |