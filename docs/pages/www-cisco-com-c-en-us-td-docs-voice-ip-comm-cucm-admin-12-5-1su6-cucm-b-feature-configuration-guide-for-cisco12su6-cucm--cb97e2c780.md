---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su6-cucm-b-feature-configuration-guide-for-cisco12su6-cucm--cb97e2c780
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU6/cucm_b_feature-configuration-guide-for-cisco12su6/cucm_b_feature-configuration-guide-for-cisco1251su3_chapter_0100.html
retrieved_at: 2026-08-16T16:35:19.105992+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

Updated: October 8, 2025

Chapter: Extend and Connect

## Chapter: Extend and Connect

# Extend and Connect

## Extend and Connect
                        	 Overview

The Extend and Connect feature allows administrators to deploy Unified Communications Manager (UC) Computer Telephony Integration (CTI) applications that interoperate with any endpoint. With Extend and Connect, users
                           can access UC applications from any location using any device.

The Extend and Connect feature for Unified Communications Manager provides the following UC features:

Receive incoming
                                 			 enterprise calls

Make Call

Disconnect

Hold and
                                 			 Retrieve

Redirect and
                                 			 Forward

Call Forward All

Call Forward Busy

Call Forward No Answer

Do Not Disturb

Play Dual Tone Multi Frequency (DTMF)
                                 			 (out-of-band and in-band)

Consult
                                 			 Transfer, Conference

Add, edit, and
                                 			 delete remote destinations

Set remote
                                 			 destination as Active or Inactive

Persistent
                                 			 Connection

Play Whisper
                                 			 Announcement

## Extend and Connect
                        	 Prerequisites

Cisco Jabber, Release 9.1(1) or later

Cisco Unified Workspace License (CUWL) Standard, CUWL Professional, or Cisco User Connect License (UCL) - Enhanced

## Extend and Connect
                        	 Configuration Task Flow

### Before you begin

Step 1

Configure User Account

Step 2

Add User Permissions

Step 3

Create CTI Remote Devices

Step 4

Add Directory Number to a Device

Step 5

Add Remote Destination

Add a numerical address or directory URI that represents the other phones that the user owns.

Step 6

Verify Remote Destination

Verify if the remote destination is successfully added for a user.

Step 7

Associate User with Device

### Configure User
                           	 Account

Step 1

From Cisco Unified CM Administration, choose User Management > End User .

Step 2

Perform either of the following:

- Click Add New , to configure a new user.

- Apply the filters using the Find User Where field and click Find to retrieve a list of users.

You may add the new end user account through LDAP integration or local configuration.

Step 3

Locate the Mobility Information section.

Step 4

Check the Enable
                                             				Mobility check box.

Step 5

Click Save .

### Add User
                           	 Permissions

After the end user is active in Unified Communications Manager , add access control group permissions.

Step 1

From Cisco Unified CM Administration, choose User Management > End User .

Step 2

Specify the
                                          			 appropriate filters in the Find
                                             				User Where field, and then select Find to retrieve a list of users.

Step 3

Select the
                                          			 user from the list.

Step 4

Locate the Permissions Information section.

Step 5

Click Add to
                                             				Access Control Group .

The Find
                                                				  and List Access Control Groups window appears.

Step 6

Click Find .

The Access
                                             				Control Group list for Standard Users appears.

Step 7

Check the
                                          			 check boxes next to the following permissions:

Standard
                                                   					 CCM End-Users

Standard
                                                   					 CTI Enabled

Step 8

Click Add
                                             				Selected .

Step 9

Click Save .

### Create CTI Remote
                           	 Devices

Use the following procedure to create a CTI remote device is a device type that represents off-cluster phones that users can
                                 use with Cisco UC applications. The device type is configured with one or more lines (directory numbers) and one or more remote
                                 destinations.

Unified Communications Manager provides Extend and Connect capabilities to control calls on devices such as public switched telephone network (PSTN) phones
                                 and private branch exchange (PBX) devices.

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Add
                                             				New .

Step 3

Select CTI
                                             				Remote Device from the Phone
                                             				Type drop-down list and then click Next .

Step 4

Select the
                                          			 appropriate user ID from the Owner
                                             				User ID drop-down list.

Only users for whom you enable mobility are available from the Owner User ID drop-down list.

Unified Communications Manager populates the Device Name field with the user ID and a CTRID prefix, for example, CTRIDusername .

Step 5

Edit the
                                          			 default value in the Device
                                             				Name field, if appropriate.

Step 6

Enter a
                                          			 meaningful description in the Description field.

Cisco Jabber displays device descriptions to users. If Cisco Jabber users have multiple devices of the same model, the descriptions
                                                         from Unified Communications Manager help users tell the difference between them.

Step 7

Ensure that
                                          			 you select an appropriate option from the Rerouting Calling Search Space drop-down list in the Protocol Specific Information section.

The Rerouting Calling Search Space drop-down list
                                             				defines the calling search space for rerouting and ensures that users can send
                                             				and receive calls from the CTI remote device.

Step 8

Configure the remaining fields in the Phone Configuration window. For more information on the fields and their configuration options, see Online Help.

Step 9

Click Save .

The fields to
                                             				associate directory numbers and add remote destinations are displayed in the Phone
                                                				  Configuration window.

### Add Directory
                           	 Number to a Device

A directory number
                                 		  (DN) is a numerical address that is configured as a line on the CTI remote
                                 		  device. A DN typically represents the primary work number of a user (for
                                 		  example, 2000 or +1 408 200 2000).

The Calling Search Space (CSS) and partition of DN are mandatory on devices.

The CTI Remote Device should not block its own DN. The CSS is important for the CTIRD device to reach its own DN.

Follow these steps
                                 		  to add a directory number to a CTI remote device.

Step 1

Locate the Association Information section in the Phone
                                             				Configuration window.

Step 2

Click Add a
                                             				new DN .

Step 3

Specify a
                                          			 directory number in the Directory Number field.

Step 4

Configure all other required fields. For more information on the fields and their configuration options, see Online Help.

Step 5

Click Save .

### Add Remote
                           	 Destination

Use the following procedure to add a remote destination is a numerical address or directory URI that represents the other
                                 phones that the user owns (for example, a home office line or other PBX phone). A remote destination may be any off-cluster
                                 device. Unified Communications Manager automatically applies application dial rules to all remote destination numbers for CTI remote devices. By default, four remote
                                 destinations are supported per device. You can set the maximum number to 10 remote destinations per device in End User Configuration window.

You can determine which remote destination the Jabber client has set as Active by opening the Phone Configuration window from the Cisco Unified Communications Manager Administration interface.

Unified Communications Manager users can add remote destinations through the Cisco Jabber interface. For more information, see the Cisco Jabber for Windows Installation and Configuration Guide .

Unified Communications Manager automatically verifies whether it can route calls to remote destinations that Cisco Jabber users add through the client interface.

Unified Communications Manager does not verify whether it can route calls to remote destinations that you add through the Cisco Unified Communications Manager Administration interface.

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Specify the appropriate filters in the Find Phone Where field to and then click Find to retrieve a list of phones.

Step 3

Select the CTI
                                          			 remote device from the list.

Step 4

Locate the Associated Remote Destinations section.

Step 5

Click Add a
                                             				New Remote Destination .

Step 6

Enter the
                                          			 destination number in the Destination Number field.

To use the remote destination with Cisco Jabber clients, you must configure the destination name as JabberRD .

Step 7

Configure the remaining fields in the Remote Destination Information window. For more information on the fields and their configuration options, see Online Help.

Step 8

Click Save .

### Verify Remote
                           	 Destination

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Specify the
                                          			 appropriate filters in the Find
                                             				Phone Where field to and then click Find to retrieve a list of phones.

Step 3

Select the CTI
                                          			 remote device from the list.

Step 4

Locate the Associated Remote Destinations section and verify
                                          			 that the remote destination is available.

Step 5

Click Apply
                                             				Config .

The Device
                                                         				  Information section on the Phone Configuration window indicates when a remote
                                                         				  destination is active or controlled by Cisco Jabber.

### Associate User with Device

Step 1

From Cisco Unified CM Administration, choose User Management > End User .

Step 2

Specify the appropriate filters in the Find User Where field to and then click Find to retrieve a list of users.

Step 3

Select the user from the list.

Step 4

Locate the Device Information section.

Step 5

Click Device
                                             				Association .

Step 6

Find and
                                          			 select the CTI remote device.

Step 7

To complete the association, click Save Selected/Changes .

Step 8

From Related Links drop-down list, choose Back to User , and then click Go .

## CTI Remote Device (CTIRD) Call Flows

Unified Communications Manager supports the separate calling party number and billing number feature when users are added as CTI Remote Device. Each CTI
                           Remote Device is configured with the user directory number (DN) (for example, 2000) and a remote destination that represents
                           any off-cluster device (for example, a PBX phone with the number +1 408 111 1111).

When a call is initiated from the PSTN network to a CTIRD line, Unified Communications Manager looks for FROM and PAID header information. The FROM header contains the external presentation name and number and PAID contains
                           the identity of the user (that is a user’s DN or DDI).

If FROM and PAID headers have different numbers and Enable External Presentation Name and Number check box is checked in its SIP profile and Display External Presentation Name and Number service parameter value set to True , then Unified Communications Manager displays the FROM header information on the called device. In the same way, if any one option is disabled, Unified Communications Manager displays PAID header information on the called device.

Similarly, in the outgoing call scenario a user calls from Remote Destination (CTIRD line) configured with External Presentation Name and External Presentation Number on Directory Number configuration page to a PSTN network through a SIP trunk with Enable External Presentation Name and Number configured in its SIP profile. Then, Unified Communications Manager send the External Presentation Information configured on the Directory Number Configuration page in the FROM header of the
                           outgoing SIP message to display on the called device.

If Enable External Presentation Name and Number check box is unchecked, then Unified Communications Manager sends the directory number information in the FROM and PAID to display on the called device and configured External Presentation
                           Information in the X-Cisco-Presentation header.

If you check the Anonymous External Presentation check box, the configured External Presentation Name and Number are removed from the respective fields and external presentation
                           displayed as anonymous on the called device.

For more details on Configuring External Presentation Information, see the Configure Directory Number chapter in the System Configuration Guide for Cisco Unified Communications Manager .

## Extend and Connect
                        	 Interactions

Feature

Interaction

Directory
                                          					 URI Dialing

Configure
                                          					 a Directory URI as the DN, remote destination, or both for the CTI remote
                                          					 device.

Unified
                                          					 Mobility

Extend and Support does not support moving active calls between a Cisco Unified IP Phone and a remote destination.

If you
                                          					 want the capabilities of both Unified Mobility and Extend and Connect, you can
                                          					 configure the same remote destination on the Remote Device Profile and CTI
                                          					 Remote Device types when the Owner ID of both device types is the same. This
                                          					 configuration allows Cisco Mobility features to be used concurrently with
                                          					 Extend and Connect. The ability to configure the same remote destination on
                                          					 both device types is supported using Cisco Unified Communications Manager
                                          					 Release 10.0(1) or later.

Do not
                                          					 configure remote destinations that are used with the Cisco Extend and Connect
                                          					 feature on Cisco Dual-mode for iPhone, Cisco Dual-mode for Android, and
                                          					 Carrier-integrated Mobile device types. Do not use prefixes to differentiate
                                          					 the same remote destination address. For example, 91-4085555555 and
                                          					 +1-4085555555 are treated as the same number.

Hunt List

The Extend
                                          					 and Connect feature allows users to receive hunt calls on remote destination
                                          					 phones under the following conditions:

The user has a Cisco Unified IP Phone .

The Cisco Unified IP Phone is available to answer hunt calls (logged-in/HLog).

Cisco Jabber is running in Extend and Connect mode.

CallerID
                                          					 Information

The
                                                						  incoming caller ID information (name and number) is displayed on the Jabber
                                                						  client.

This
                                                						  information may also be displayed on the device, depending on your carrier and
                                                						  trunk configuration.

Outbound Dial Via Office calls to the remote destination display Voice Connect as the name and the trunk DID as the
                                                						  number.

Configure the trunk DID in the Unified CM Trunk
                                                						  Pattern, Route Pattern, or Cisco Gateway. This configuration may also be
                                                						  assigned by the carrier. The number field may display as blank if the trunk DID
                                                						  is not configured.

Outbound calls to the desired party display the CTI Remote Device Display Name and Directory Number (DN) as configured in Unified Communications Manager .

Remote destination numbers are never displayed to the called party.

## Extend and Connect
                        	 Restrictions

Restriction

Description

Maximum
                                          					 number of remote destinations

You can configure up to ten remote destinations for each CTI remote device.

By default, four remote destinations are supported per device. You can set the maximum number to 10 remote destinations per
                                                      device.

Off-cluster devices

Remote destination numbers must represent off-cluster devices.

Remote destinations can be off-cluster URIs.

Directory
                                          					 numbers

You cannot
                                          					 configure directory numbers as remote destination numbers.

Cisco
                                          					 Jabber

Before you
                                          					 save the remote destinations that are configured using Cisco Jabber, verify if
                                          					 the remote destinations can be routed by the configured dial plan.

Application dial rules

Application Dial Rules are applied to all remote destinations that are configured on the CTI remote device through the Cisco Unified Communications Manager Administration interface and Cisco Jabber.

Advise end users which number formats the Application Dial Rules are configured to support (for example, nn-nnn-nnnn, E.164,
                                                      both).

Remote destination number

Each
                                          					 remote destination number must be unique within the cluster.

Two or more users cannot use the same remote destination numbers.

Remote destination validation

Remote destination numbers are validated using the CTI remote device reroute calling search space.

Remote destinations that are configured using the Cisco Unified Communications Manager Administration interface and AXL interface are not validated.

Consult transfer limitation

When a consult transfer is initiated from a CTI Remote Device to an internal IP phone or another extend and connect enabled
                                          device, no ringback is heard on the remote destination associated to the CTI Remote device which is initiating the transfer.

Call Forward Unregistered

Extend and Connect does not support Call Forward Unregistered Internal or Call Forward Unregistered External.

Route Next Hop By Calling Party Number

Extend and Connect does not support Translation Patterns when the "Route Next Hop By Calling Party Number" option is enabled.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure User Account | Enable
                                       			 mobility for users so that they can use CTI remote devices. CTI devices are
                                       			 off-cluster phones that work with Cisco UC applications. |
| Step 2 | Add User Permissions | Add access
                                       			 control group permissions. |
| Step 3 | Create CTI Remote Devices | Configure
                                       			 off-cluster phones that users can use with Cisco UC applications. |
| Step 4 | Add Directory Number to a Device | Associate a
                                       			 directory number with the CTI remote device. |
| Step 5 | Add Remote Destination | Add a numerical address or directory URI that represents the other phones that the user owns. |
| Step 6 | Verify Remote Destination | Verify if the remote destination is successfully added for a user. |
| Step 7 | Associate User with Device | Associate an
                                       			 end user account to the CTI remote device. |

| Step 1 | From Cisco Unified CM Administration, choose User Management > End User . |
|---|---|
| Step 2 | Perform either of the following: Click Add New , to configure a new user. Apply the filters using the Find User Where field and click Find to retrieve a list of users. Note You may add the new end user account through LDAP integration or local configuration. | Note | You may add the new end user account through LDAP integration or local configuration. |
| Note | You may add the new end user account through LDAP integration or local configuration. |
| Step 3 | Locate the Mobility Information section. |
| Step 4 | Check the Enable
                                             				Mobility check box. |
| Step 5 | Click Save . |

| Note | You may add the new end user account through LDAP integration or local configuration. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose User Management > End User . |
|---|---|
| Step 2 | Specify the
                                          			 appropriate filters in the Find
                                             				User Where field, and then select Find to retrieve a list of users. |
| Step 3 | Select the
                                          			 user from the list. |
| Step 4 | Locate the Permissions Information section. |
| Step 5 | Click Add to
                                             				Access Control Group . The Find
                                                				  and List Access Control Groups window appears. |
| Step 6 | Click Find . The Access
                                             				Control Group list for Standard Users appears. |
| Step 7 | Check the
                                          			 check boxes next to the following permissions: Standard
                                                   					 CCM End-Users Standard
                                                   					 CTI Enabled |
| Step 8 | Click Add
                                             				Selected . |
| Step 9 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Add
                                             				New . |
| Step 3 | Select CTI
                                             				Remote Device from the Phone
                                             				Type drop-down list and then click Next . |
| Step 4 | Select the
                                          			 appropriate user ID from the Owner
                                             				User ID drop-down list. Note Only users for whom you enable mobility are available from the Owner User ID drop-down list. Unified Communications Manager populates the Device Name field with the user ID and a CTRID prefix, for example, CTRIDusername . | Note | Only users for whom you enable mobility are available from the Owner User ID drop-down list. |
| Note | Only users for whom you enable mobility are available from the Owner User ID drop-down list. |
| Step 5 | Edit the
                                          			 default value in the Device
                                             				Name field, if appropriate. |
| Step 6 | Enter a
                                          			 meaningful description in the Description field. Note Cisco Jabber displays device descriptions to users. If Cisco Jabber users have multiple devices of the same model, the descriptions
                                                         from Unified Communications Manager help users tell the difference between them. | Note | Cisco Jabber displays device descriptions to users. If Cisco Jabber users have multiple devices of the same model, the descriptions
                                                         from Unified Communications Manager help users tell the difference between them. |
| Note | Cisco Jabber displays device descriptions to users. If Cisco Jabber users have multiple devices of the same model, the descriptions
                                                         from Unified Communications Manager help users tell the difference between them. |
| Step 7 | Ensure that
                                          			 you select an appropriate option from the Rerouting Calling Search Space drop-down list in the Protocol Specific Information section. The Rerouting Calling Search Space drop-down list
                                             				defines the calling search space for rerouting and ensures that users can send
                                             				and receive calls from the CTI remote device. |
| Step 8 | Configure the remaining fields in the Phone Configuration window. For more information on the fields and their configuration options, see Online Help. |
| Step 9 | Click Save . The fields to
                                             				associate directory numbers and add remote destinations are displayed in the Phone
                                                				  Configuration window. |

| Note | Only users for whom you enable mobility are available from the Owner User ID drop-down list. |
|---|---|

| Note | Cisco Jabber displays device descriptions to users. If Cisco Jabber users have multiple devices of the same model, the descriptions
                                                         from Unified Communications Manager help users tell the difference between them. |
|---|---|

| Note | The Calling Search Space (CSS) and partition of DN are mandatory on devices. The CTI Remote Device should not block its own DN. The CSS is important for the CTIRD device to reach its own DN. |
|---|---|

| Step 1 | Locate the Association Information section in the Phone
                                             				Configuration window. |
|---|---|
| Step 2 | Click Add a
                                             				new DN . |
| Step 3 | Specify a
                                          			 directory number in the Directory Number field. |
| Step 4 | Configure all other required fields. For more information on the fields and their configuration options, see Online Help. |
| Step 5 | Click Save . |

| Note | You can determine which remote destination the Jabber client has set as Active by opening the Phone Configuration window from the Cisco Unified Communications Manager Administration interface. |
|---|---|

| Note | Unified Communications Manager users can add remote destinations through the Cisco Jabber interface. For more information, see the Cisco Jabber for Windows Installation and Configuration Guide . Unified Communications Manager automatically verifies whether it can route calls to remote destinations that Cisco Jabber users add through the client interface. Unified Communications Manager does not verify whether it can route calls to remote destinations that you add through the Cisco Unified Communications Manager Administration interface. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Specify the appropriate filters in the Find Phone Where field to and then click Find to retrieve a list of phones. |
| Step 3 | Select the CTI
                                          			 remote device from the list. |
| Step 4 | Locate the Associated Remote Destinations section. |
| Step 5 | Click Add a
                                             				New Remote Destination . |
| Step 6 | Enter the
                                          			 destination number in the Destination Number field. To use the remote destination with Cisco Jabber clients, you must configure the destination name as JabberRD . |
| Step 7 | Configure the remaining fields in the Remote Destination Information window. For more information on the fields and their configuration options, see Online Help. |
| Step 8 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Specify the
                                          			 appropriate filters in the Find
                                             				Phone Where field to and then click Find to retrieve a list of phones. |
| Step 3 | Select the CTI
                                          			 remote device from the list. |
| Step 4 | Locate the Associated Remote Destinations section and verify
                                          			 that the remote destination is available. |
| Step 5 | Click Apply
                                             				Config . Note The Device
                                                         				  Information section on the Phone Configuration window indicates when a remote
                                                         				  destination is active or controlled by Cisco Jabber. | Note | The Device
                                                         				  Information section on the Phone Configuration window indicates when a remote
                                                         				  destination is active or controlled by Cisco Jabber. |
| Note | The Device
                                                         				  Information section on the Phone Configuration window indicates when a remote
                                                         				  destination is active or controlled by Cisco Jabber. |

| Note | The Device
                                                         				  Information section on the Phone Configuration window indicates when a remote
                                                         				  destination is active or controlled by Cisco Jabber. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose User Management > End User . |
|---|---|
| Step 2 | Specify the appropriate filters in the Find User Where field to and then click Find to retrieve a list of users. |
| Step 3 | Select the user from the list. |
| Step 4 | Locate the Device Information section. |
| Step 5 | Click Device
                                             				Association . |
| Step 6 | Find and
                                          			 select the CTI remote device. |
| Step 7 | To complete the association, click Save Selected/Changes . |
| Step 8 | From Related Links drop-down list, choose Back to User , and then click Go . The End User Configuration window appears, and the associated device that you chose appears in the Controlled Devices pane. |

| Feature | Interaction |
|---|---|
| Directory
                                          					 URI Dialing | Configure
                                          					 a Directory URI as the DN, remote destination, or both for the CTI remote
                                          					 device. |
| Unified
                                          					 Mobility | Extend and Support does not support moving active calls between a Cisco Unified IP Phone and a remote destination. If you
                                          					 want the capabilities of both Unified Mobility and Extend and Connect, you can
                                          					 configure the same remote destination on the Remote Device Profile and CTI
                                          					 Remote Device types when the Owner ID of both device types is the same. This
                                          					 configuration allows Cisco Mobility features to be used concurrently with
                                          					 Extend and Connect. The ability to configure the same remote destination on
                                          					 both device types is supported using Cisco Unified Communications Manager
                                          					 Release 10.0(1) or later. Do not
                                          					 configure remote destinations that are used with the Cisco Extend and Connect
                                          					 feature on Cisco Dual-mode for iPhone, Cisco Dual-mode for Android, and
                                          					 Carrier-integrated Mobile device types. Do not use prefixes to differentiate
                                          					 the same remote destination address. For example, 91-4085555555 and
                                          					 +1-4085555555 are treated as the same number. |
| Hunt List | The Extend
                                          					 and Connect feature allows users to receive hunt calls on remote destination
                                          					 phones under the following conditions: The user has a Cisco Unified IP Phone . The Cisco Unified IP Phone is available to answer hunt calls (logged-in/HLog). Cisco Jabber is running in Extend and Connect mode. |
| CallerID
                                          					 Information | The
                                                						  incoming caller ID information (name and number) is displayed on the Jabber
                                                						  client. This
                                                						  information may also be displayed on the device, depending on your carrier and
                                                						  trunk configuration. Outbound Dial Via Office calls to the remote destination display Voice Connect as the name and the trunk DID as the
                                                						  number. Configure the trunk DID in the Unified CM Trunk
                                                						  Pattern, Route Pattern, or Cisco Gateway. This configuration may also be
                                                						  assigned by the carrier. The number field may display as blank if the trunk DID
                                                						  is not configured. Outbound calls to the desired party display the CTI Remote Device Display Name and Directory Number (DN) as configured in Unified Communications Manager . Remote destination numbers are never displayed to the called party. |

| Restriction | Description |
|---|---|
| Maximum
                                          					 number of remote destinations | You can configure up to ten remote destinations for each CTI remote device. Note By default, four remote destinations are supported per device. You can set the maximum number to 10 remote destinations per
                                                      device. | Note | By default, four remote destinations are supported per device. You can set the maximum number to 10 remote destinations per
                                                      device. |
| Note | By default, four remote destinations are supported per device. You can set the maximum number to 10 remote destinations per
                                                      device. |
| Off-cluster devices | Remote destination numbers must represent off-cluster devices. Remote destinations can be off-cluster URIs. |
| Directory
                                          					 numbers | You cannot
                                          					 configure directory numbers as remote destination numbers. |
| Cisco
                                          					 Jabber | Before you
                                          					 save the remote destinations that are configured using Cisco Jabber, verify if
                                          					 the remote destinations can be routed by the configured dial plan. |
| Application dial rules | Application Dial Rules are applied to all remote destinations that are configured on the CTI remote device through the Cisco Unified Communications Manager Administration interface and Cisco Jabber. Note Advise end users which number formats the Application Dial Rules are configured to support (for example, nn-nnn-nnnn, E.164,
                                                      both). | Note | Advise end users which number formats the Application Dial Rules are configured to support (for example, nn-nnn-nnnn, E.164,
                                                      both). |
| Note | Advise end users which number formats the Application Dial Rules are configured to support (for example, nn-nnn-nnnn, E.164,
                                                      both). |
| Remote destination number | Each
                                          					 remote destination number must be unique within the cluster. Note Two or more users cannot use the same remote destination numbers. | Note | Two or more users cannot use the same remote destination numbers. |
| Note | Two or more users cannot use the same remote destination numbers. |
| Remote destination validation | Remote destination numbers are validated using the CTI remote device reroute calling search space. Remote destinations that are configured using the Cisco Unified Communications Manager Administration interface and AXL interface are not validated. |
| Consult transfer limitation | When a consult transfer is initiated from a CTI Remote Device to an internal IP phone or another extend and connect enabled
                                          device, no ringback is heard on the remote destination associated to the CTI Remote device which is initiating the transfer. |
| Call Forward Unregistered | Extend and Connect does not support Call Forward Unregistered Internal or Call Forward Unregistered External. |
| Route Next Hop By Calling Party Number | Extend and Connect does not support Translation Patterns when the "Route Next Hop By Calling Party Number" option is enabled. |

| Note | By default, four remote destinations are supported per device. You can set the maximum number to 10 remote destinations per
                                                      device. |
|---|---|

| Note | Advise end users which number formats the Application Dial Rules are configured to support (for example, nn-nnn-nnnn, E.164,
                                                      both). |
|---|---|

| Note | Two or more users cannot use the same remote destination numbers. |
|---|---|