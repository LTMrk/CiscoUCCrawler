---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-7-cjab-b-deploy-jabber-webex-messenger-127-cjab-b-deploy-jabber-we-f9f91c198f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_7/cjab_b_deploy-jabber-webex-messenger-127/cjab_b_deploy-jabber-webex-messenger-127_chapter_01001.html
retrieved_at: 2026-08-21T21:05:17.608467+00:00
---

Webex Messenger Deployment for Cisco Jabber 12.7

# Webex Messenger Deployment for Cisco Jabber 12.7

Updated: April 1, 2024

Chapter: Configure Extend and Connect

## Chapter: Configure Extend and Connect

# Configure Extend and Connect

## Configure Extend and Connect Workflow

Step 1

Enable User Mobility

Enable users mobility and you can assign users as owners of CTI remote devices.

Step 2

Create CTI Remote Devices

Create CTI remote devices, these virtual devices monitor and have call control over a  user's remote destination.

Step 3

Add a Remote Destination

(Optional) If you plan to provision users with dedicated CTI remote devices, add a remote destination in Cisco Unified Communications
                                          Manager.

## Enable User
                           		Mobility

This task is
                              		  only for desktop
                              		clients.

You must enable
                              		  user mobility to provision CTI remote devices. If you do not enable mobility
                              		  for users, you cannot assign those users as owners of CTI remote devices.

### Before you begin

This task is
                              		  applicable only if:

You plan to
                                    				assign Cisco Jabber for Mac or Cisco Jabber for Windows users to CTI remote
                                    				devices.

You have Cisco
                                    				Unified Communication Manager release 9.x and later.

Step 1

Select User
                                             				  Management > End User .

The Find
                                             				  and List Users window opens.

Step 2

Specify the
                                       			 appropriate filters in the Find
                                          				User where field to and then select Find to retrieve a list of users.

Step 3

Select the
                                       			 user from the list.

The End
                                             				  User Configuration window opens.

Step 4

Locate the Mobility Information section.

Step 5

Select Enable
                                          				Mobility .

Step 6

Select Save .

## Create CTI Remote Devices

CTI remote devices are virtual devices that monitor and have call control over a  user's remote destination.

Step 1

Open the Cisco Unified CM Administration interface.

Step 2

Select Device > Phone .

The Find and List Phones window opens.

Step 3

Select Add New .

Step 4

Select CTI Remote Device from the Phone Type drop-down list and then select Next .

The Phone Configuration window opens.

Step 5

Select the appropriate user ID from the Owner User ID drop-down list.

Only users for whom you enable mobility are available from the Owner User ID drop-down list. For more information, see Enable SAML SSO in the Client .

Cisco Unified
                                             				  Communications Manager populates the Device Name field with the user ID and a CTIRD prefix; for example, CTIRDusername

Step 6

Edit the default value in the Device Name field, if appropriate.

Step 7

Ensure you select an appropriate option from the Rerouting Calling Search Space drop-down list in the Protocol Specific Information section.

The Rerouting Calling Search Space drop-down list defines the calling search space for re-routing and ensures that users can send and receive calls from the
                                          CTI remote device.

Step 8

Specify all other configuration settings on the Phone Configuration window as appropriate.

See the CTI remote device setup topic in the System Configuration Guide for Cisco Unified Communications Manager documentation for more information.

Step 9

Select Save .

The fields to associate directory numbers and add remote destinations become available on the Phone Configuration window.

## Add a Remote Destination

Remote destinations represent the CTI controllable devices that are available to users.

You should add a remote destination through the Cisco Unified CM Administration interface if you plan to provision users with dedicated CTI remote devices. This task ensures that users can automatically
                              control their phones and place calls  when they start the client.

If you plan to provision users with CTI remote devices along with software phone devices and desk phone devices, you should
                              not add a remote destination through the Cisco Unified CM Administration interface. Users can enter remote destinations through the client interface.

You should create only one remote destination per user. Do not add two or more remote destinations for a user.

Cisco Unified Communications Manager does not verify if it can route remote destinations that you add through the Cisco Unified CM Administration interface. For this reason, you must ensure that Cisco Unified Communications Manager can route the remote destinations you
                                                add.

Cisco Unified Communications Manager automatically applies application dial rules to all remote destination numbers for CTI
                                                remote devices.

Step 1

Open the Cisco Unified CM Administration interface.

Step 2

Select Device > Phone .

The Find and List Phones window opens.

Step 3

Specify the appropriate filters in the Find Phone where field to and then select Find to retrieve a list of phones.

Step 4

Select the CTI remote device from the list.

The Phone Configuration window opens.

Step 5

Locate the Associated Remote Destinations section.

Step 6

Select Add a New Remote Destination .

The Remote Destination Information window opens.

Step 7

Specify JabberRD in the Name field.

Restriction

You must specify JabberRD in the Name field. The client uses only the JabberRD remote destination. If you specify a name other than JabberRD, users cannot access
                                                         that remote destination.

The client automatically sets the JabberRD name when users add remote destinations through the client interface.

Step 8

Enter the destination number in the Destination Number field.

Step 9

Specify all other values as appropriate.

Step 10

Select Save .

### What to do next

Complete the following steps to verify the remote destination and apply the configuration to the CTI remote device:

Repeat the steps to open the Phone Configuration window for the CTI remote device.

Locate the Associated Remote Destinations section.

Verify the remote destination is available.

Select Apply Config .

The Device Information section on the Phone Configuration window contains a Active Remote Destination field.

When users select a remote destination in the client, it displays as the value of Active Remote Destination .

none displays as the value of Active Remote Destination if:

Users do not select a remote destination in the client.

Users exit or are not signed in to the client.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Enable User Mobility | Enable users mobility and you can assign users as owners of CTI remote devices. |
| Step 2 | Create CTI Remote Devices | Create CTI remote devices, these virtual devices monitor and have call control over a  user's remote destination. |
| Step 3 | Add a Remote Destination | (Optional) If you plan to provision users with dedicated CTI remote devices, add a remote destination in Cisco Unified Communications
                                          Manager. |

| Step 1 | Select User
                                             				  Management > End User . The Find
                                             				  and List Users window opens. |
|---|---|
| Step 2 | Specify the
                                       			 appropriate filters in the Find
                                          				User where field to and then select Find to retrieve a list of users. |
| Step 3 | Select the
                                       			 user from the list. The End
                                             				  User Configuration window opens. |
| Step 4 | Locate the Mobility Information section. |
| Step 5 | Select Enable
                                          				Mobility . |
| Step 6 | Select Save . |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Device > Phone . The Find and List Phones window opens. |
| Step 3 | Select Add New . |
| Step 4 | Select CTI Remote Device from the Phone Type drop-down list and then select Next . The Phone Configuration window opens. |
| Step 5 | Select the appropriate user ID from the Owner User ID drop-down list. Note Only users for whom you enable mobility are available from the Owner User ID drop-down list. For more information, see Enable SAML SSO in the Client . Cisco Unified
                                             				  Communications Manager populates the Device Name field with the user ID and a CTIRD prefix; for example, CTIRDusername | Note | Only users for whom you enable mobility are available from the Owner User ID drop-down list. For more information, see Enable SAML SSO in the Client . |
| Note | Only users for whom you enable mobility are available from the Owner User ID drop-down list. For more information, see Enable SAML SSO in the Client . |
| Step 6 | Edit the default value in the Device Name field, if appropriate. |
| Step 7 | Ensure you select an appropriate option from the Rerouting Calling Search Space drop-down list in the Protocol Specific Information section. The Rerouting Calling Search Space drop-down list defines the calling search space for re-routing and ensures that users can send and receive calls from the
                                          CTI remote device. |
| Step 8 | Specify all other configuration settings on the Phone Configuration window as appropriate. See the CTI remote device setup topic in the System Configuration Guide for Cisco Unified Communications Manager documentation for more information. |
| Step 9 | Select Save . The fields to associate directory numbers and add remote destinations become available on the Phone Configuration window. |

| Note | Only users for whom you enable mobility are available from the Owner User ID drop-down list. For more information, see Enable SAML SSO in the Client . |
|---|---|

| Note | You should create only one remote destination per user. Do not add two or more remote destinations for a user. Cisco Unified Communications Manager does not verify if it can route remote destinations that you add through the Cisco Unified CM Administration interface. For this reason, you must ensure that Cisco Unified Communications Manager can route the remote destinations you
                                                add. Cisco Unified Communications Manager automatically applies application dial rules to all remote destination numbers for CTI
                                                remote devices. |
|---|---|

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Device > Phone . The Find and List Phones window opens. |
| Step 3 | Specify the appropriate filters in the Find Phone where field to and then select Find to retrieve a list of phones. |
| Step 4 | Select the CTI remote device from the list. The Phone Configuration window opens. |
| Step 5 | Locate the Associated Remote Destinations section. |
| Step 6 | Select Add a New Remote Destination . The Remote Destination Information window opens. |
| Step 7 | Specify JabberRD in the Name field. Restriction You must specify JabberRD in the Name field. The client uses only the JabberRD remote destination. If you specify a name other than JabberRD, users cannot access
                                                         that remote destination. The client automatically sets the JabberRD name when users add remote destinations through the client interface. | Restriction | You must specify JabberRD in the Name field. The client uses only the JabberRD remote destination. If you specify a name other than JabberRD, users cannot access
                                                         that remote destination. |
| Restriction | You must specify JabberRD in the Name field. The client uses only the JabberRD remote destination. If you specify a name other than JabberRD, users cannot access
                                                         that remote destination. |
| Step 8 | Enter the destination number in the Destination Number field. |
| Step 9 | Specify all other values as appropriate. |
| Step 10 | Select Save . |

| Restriction | You must specify JabberRD in the Name field. The client uses only the JabberRD remote destination. If you specify a name other than JabberRD, users cannot access
                                                         that remote destination. |
|---|---|

| Note | The Device Information section on the Phone Configuration window contains a Active Remote Destination field. When users select a remote destination in the client, it displays as the value of Active Remote Destination . none displays as the value of Active Remote Destination if: Users do not select a remote destination in the client. Users exit or are not signed in to the client. |
|---|---|