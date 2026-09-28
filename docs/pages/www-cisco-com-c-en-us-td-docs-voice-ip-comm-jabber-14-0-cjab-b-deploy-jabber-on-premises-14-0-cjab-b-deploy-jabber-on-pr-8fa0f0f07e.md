---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-14-0-cjab-b-deploy-jabber-on-premises-14-0-cjab-b-deploy-jabber-on-pr-8fa0f0f07e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/14_0/cjab_b_deploy-jabber-on-premises-14_0/cjab_b_deploy-jabber-on-premises-129_chapter_0101.html
retrieved_at: 2026-08-21T07:06:52.696406+00:00
---

On-Premises Deployment for Cisco Jabber 14.0

# On-Premises Deployment for Cisco Jabber 14.0

Updated: April 1, 2024

Chapter: Configure Instant Messaging and Presence Service

## Chapter: Configure Instant Messaging and Presence Service

# Configure Instant Messaging and Presence Service

## IM and Presence
                        	 Service Workflow with Cisco Unified Communications
                        	 Manager Release 10.5 and Later

Step 1

Configure IM Address Scheme

Configure an IM address for users.

Step 2

Enable Message Settings

In the Cisco Unified Communications  IM and Presence service, set the options to enable instant message and logging.

## IM and Presence
                        	 Service Workflow  with Cisco Unified Communications
                        	 Manager Release 9.x and Later

Step 1

Enable Message Settings

In the Cisco Unified Communications  IM and Presence service, set the options to enable instant message and logging.

Step 2

Add an IM and Presence Service

Create an IM and Presence UC Service.

Step 3

Apply an IM and Presence Service

Add the IM and Presence UC Service to the Service Profile.

## Add an IM and
                        	 Presence Service

Provide users with
                              		  IM and Presence Service capabilities.

Step 1

Open the Cisco
                                          				Unified CM Administration interface.

Step 2

Select User
                                             				  Management > User Settings > UC
                                             				  Service .

The Find
                                             				  and List UC Services window opens.

Step 3

Select Add
                                          				New .

The UC
                                             				  Service Configuration window opens.

Step 4

In the Add a UC
                                          				Service section, select IM and
                                          				Presence from the UC
                                          				Service Type drop-down list.

Step 5

Select Next .

Step 6

Provide details
                                       			 for the IM and Presence Service as follows:

Select Unified CM (IM and Presence) from the Product Type drop-down list.

Specify a
                                             				  name for the service in the Name field.

The name you
                                                					 specify displays when you add the service to a profile. Ensure the name you
                                                					 specify is unique, meaningful, and easy to identify.

Specify an
                                             				  optional description in the Description field.

Specify the
                                             				  instant messaging and presence service address in the Host
                                                					 Name/IP Address field.

Important

The
                                                            						service address must be a fully qualified domain name or IP address.

Step 7

Select Save .

### Apply an IM and
                           	 Presence Service

After you add an
                                 		  IM and Presence Service on 
                                 		  Cisco Unified Communications Manager,
                                 		  you must apply it to a service profile so that the client can retrieve the
                                 		  settings.

#### Before you begin

Add an IM and Presence Service

Step 1

Open the Cisco Unified CM Administration interface.

Step 2

Select User Management > User Settings > Service Profile .

The Find and List Service Profiles window opens.

Step 3

Find and select your service profile.

The Service Profile Configuration window opens.

Step 4

In the IM and Presence Profile section, select up to three services from the following drop-down lists:

Primary

Secondary

Tertiary

Step 5

Click Save .

## Configure IM
                        	 Address Scheme

This feature is supported on Cisco Unified Communications Manager IM
                              		  and Presence Service release 10.x or later. For versions of Cisco Unified
                              		  Communications Manager IM and Presence Service release 9.x and earlier the
                              		  default IM address scheme used is UserID@[Default Domain] .

Step 1

Choose the IM Address Scheme .

Open Cisco Unified CM IM and Presence Administration .

Select Presence > Settings > Advanced Configuration

Select IM Address Scheme and from the list choose one of the following:

If you use the UserID, ensure that you configure a default
                                                      				  domain. For example, services must be named cups.com and not cups .

Directory URI

Step 2

Select the required mapping.

Open Cisco Unified CM Administration .

Select System > LDAP > LDAP Directory .

Find and select the directory from the list.

In the Standard User Fields To Be Synchronized section choose the mapping:

User ID mapped
                                                      				to an LDAP field, the default is sAMAccountName .

Directory URI
                                                      				mapped to either mail or msRTCSIP-primaryuseraddress .

## Enable Message
                        	 Settings

Enable and configure instant messaging capabilities.

Step 1

Open the Cisco
                                          				Unified CM IM and Presence Administration interface.

Step 2

Select Messaging > Settings .

Step 3

Select the
                                       			 following options:

Enable instant
                                                      						messaging

Allow clients to log
                                                      						instant message history

Allow cut & paste in instant messages

Step 4

Select other
                                       			 messaging settings as appropriate.

Step 5

Select Save .

Important

Cisco Jabber does not support the following settings on the Presence Settings window on Cisco Unified Communications Manager IM and Presence Service release 9.0.x:

Use DND status when user is on the phone

Use DND status when user is in a meeting

### What to do next

If you have
                                       				Cisco Unified Communications Manager IM and Presence Service release 9.x and
                                       				later, Add an IM and Presence Service .

## Disable Instant Message Settings

Step 1

From Cisco Unified CM IM and Presence Administration go to Messaging > Settings .

Step 2

Uncheck Enable instant messaging and click Save .

### What to do next

## Manage Presence Settings

Step 1

From Cisco Unified CM IM and Presence Administration , go to Presence > Settings > Standard Configuration .

Step 2

Uncheck Enable availability sharing and click Save .

### What to do next

Restart the Cisco XCP Router service.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure IM Address Scheme | Configure an IM address for users. |
| Step 2 | Enable Message Settings | In the Cisco Unified Communications  IM and Presence service, set the options to enable instant message and logging. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Enable Message Settings | In the Cisco Unified Communications  IM and Presence service, set the options to enable instant message and logging. |
| Step 2 | Add an IM and Presence Service | Create an IM and Presence UC Service. |
| Step 3 | Apply an IM and Presence Service | Add the IM and Presence UC Service to the Service Profile. |

| Step 1 | Open the Cisco
                                          				Unified CM Administration interface. |
|---|---|
| Step 2 | Select User
                                             				  Management > User Settings > UC
                                             				  Service . The Find
                                             				  and List UC Services window opens. |
| Step 3 | Select Add
                                          				New . The UC
                                             				  Service Configuration window opens. |
| Step 4 | In the Add a UC
                                          				Service section, select IM and
                                          				Presence from the UC
                                          				Service Type drop-down list. |
| Step 5 | Select Next . |
| Step 6 | Provide details
                                       			 for the IM and Presence Service as follows: Select Unified CM (IM and Presence) from the Product Type drop-down list. Specify a
                                             				  name for the service in the Name field. The name you
                                                					 specify displays when you add the service to a profile. Ensure the name you
                                                					 specify is unique, meaningful, and easy to identify. Specify an
                                             				  optional description in the Description field. Specify the
                                             				  instant messaging and presence service address in the Host
                                                					 Name/IP Address field. Important The
                                                            						service address must be a fully qualified domain name or IP address. | Important | The
                                                            						service address must be a fully qualified domain name or IP address. |
| Important | The
                                                            						service address must be a fully qualified domain name or IP address. |
| Step 7 | Select Save . |

| Important | The
                                                            						service address must be a fully qualified domain name or IP address. |
|---|---|

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select User Management > User Settings > Service Profile . The Find and List Service Profiles window opens. |
| Step 3 | Find and select your service profile. The Service Profile Configuration window opens. |
| Step 4 | In the IM and Presence Profile section, select up to three services from the following drop-down lists: Primary Secondary Tertiary |
| Step 5 | Click Save . |

| Step 1 | Choose the IM Address Scheme . Open Cisco Unified CM IM and Presence Administration . Select Presence > Settings > Advanced Configuration The Advanced Presence Settings window opens. Select IM Address Scheme and from the list choose one of the following: UserID@[Default
                                                   				Domain] If you use the UserID, ensure that you configure a default
                                                      				  domain. For example, services must be named cups.com and not cups . Directory URI |
|---|---|
| Step 2 | Select the required mapping. Open Cisco Unified CM Administration . Select System > LDAP > LDAP Directory . The Find and List LDAP Directories window opens. Find and select the directory from the list. The LDAP Directory window opens. In the Standard User Fields To Be Synchronized section choose the mapping: User ID mapped
                                                      				to an LDAP field, the default is sAMAccountName . Directory URI
                                                      				mapped to either mail or msRTCSIP-primaryuseraddress . |

| Step 1 | Open the Cisco
                                          				Unified CM IM and Presence Administration interface. |
|---|---|
| Step 2 | Select Messaging > Settings . |
| Step 3 | Select the
                                       			 following options: Enable instant
                                                      						messaging Allow clients to log
                                                      						instant message history Allow cut & paste in instant messages |
| Step 4 | Select other
                                       			 messaging settings as appropriate. |
| Step 5 | Select Save . Important Cisco Jabber does not support the following settings on the Presence Settings window on Cisco Unified Communications Manager IM and Presence Service release 9.0.x: Use DND status when user is on the phone Use DND status when user is in a meeting | Important | Cisco Jabber does not support the following settings on the Presence Settings window on Cisco Unified Communications Manager IM and Presence Service release 9.0.x: Use DND status when user is on the phone Use DND status when user is in a meeting |
| Important | Cisco Jabber does not support the following settings on the Presence Settings window on Cisco Unified Communications Manager IM and Presence Service release 9.0.x: Use DND status when user is on the phone Use DND status when user is in a meeting |

| Important | Cisco Jabber does not support the following settings on the Presence Settings window on Cisco Unified Communications Manager IM and Presence Service release 9.0.x: Use DND status when user is on the phone Use DND status when user is in a meeting |
|---|---|

| Step 1 | From Cisco Unified CM IM and Presence Administration go to Messaging > Settings . |
|---|---|
| Step 2 | Uncheck Enable instant messaging and click Save . |

| Step 1 | From Cisco Unified CM IM and Presence Administration , go to Presence > Settings > Standard Configuration . |
|---|---|
| Step 2 | Uncheck Enable availability sharing and click Save . |