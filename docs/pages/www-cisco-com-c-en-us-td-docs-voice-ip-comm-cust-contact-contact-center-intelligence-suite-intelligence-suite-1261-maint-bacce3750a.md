---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-1261-maint-bacce3750a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_1261/maintain_and_operate/guide/cuic_b_1261-admin-console-user-guide/cuic_m_configured-devices-that-contain-1261.html
retrieved_at: 2026-08-21T04:39:09.523752+00:00
---

Administration Console User Guide for Cisco Unified Intelligence Center, Release 12.6(1)

# Administration Console User Guide for Cisco Unified Intelligence Center, Release 12.6(1)

Updated: May 14, 2021

Chapter: Device Configuration

## Chapter: Device Configuration

- Device Configuration

- Create or Edit                              	 Device Information

# Device Configuration

Devices are the
                        physical machines servers on which the Cisco Unified Intelligence Center
                        Administration Console and the Cisco Unified Intelligence Center reporting
                        applications are installed.

## Device Configuration

This page lists all the currently configured devices (nodes) in the cluster that contain the Unified Intelligence Center reporting
                              process.

A cluster can contain a maximum of eight such devices:

One Controller (which runs both Administration and Unified Intelligence Center reporting)

Seven Members (which run Unified Intelligence Center)

This list always contains at least one row for the Controller, added during the installation. You cannot delete the Controller
                              from this page. To delete the Controller, you must uninstall it.

Field

Description

Name

The name of the device.

The software assigns default alias names - for the Controller, CUIC1 ; for the members, Member1 , Member2 , and so forth.

Click the member row to edit the default aliases of members to names that are more meaningful for you.

Host Address

The IP address or Host name or FQDN for the device.

Description

The description of the device.

Type

The type of the device: Controller or Member.

There is only one Controller. It runs both the Administration console and Unified Intelligence Center Reporting.

There can be a maximum of seven Members. Members run the
                                                						  Unified Intelligence Center Reporting.

To

Do This

Create New Device Configuration

Click New . For more information, see Create or Edit Device Information .

Delete a device

Click the Ellipsis button (...) and click Delete against the device member to be deleted.

You cannot delete the Controller.

The interface allows you to delete Members, but you must reinstall a Member device to add it back to the cluster.

Edit an existing device

Click the Ellipsis button (...) and click Edit against the device to be edited. Create or Edit Device Information .

### Create or Edit
                           	 Device Information

Use this page to define information about a new device or to edit information about an existing device.

Field

Description

Type

Displays the type of the server you are adding or editing.

Name*

The name of the device.

Host Address*

The IP address or hostname of the device.

You cannot
                                             					 edit the IP address of the Controller on this page.

You can edit the IP address of a Member on this page, but changing it here does not effect a change in the cluster. The cluster
                                             continues to recognize the original IP address for replication, and the replication will fail. For more information on the
                                             procedure to change the IP address of Unified Intelligence Center nodes in a cluster, see Changing the IP Address and hostname in Unified Intelligence Center .

Description

The
                                             					 description of the device.

Actions on this page are Save (changes) and Cancel (changes).

| Field | Description |
|---|---|
| Name | The name of the device. The software assigns default alias names - for the Controller, CUIC1 ; for the members, Member1 , Member2 , and so forth. Click the member row to edit the default aliases of members to names that are more meaningful for you. |
| Host Address | The IP address or Host name or FQDN for the device. |
| Description | The description of the device. |
| Type | The type of the device: Controller or Member. There is only one Controller. It runs both the Administration console and Unified Intelligence Center Reporting. There can be a maximum of seven Members. Members run the
                                                						  Unified Intelligence Center Reporting. |

| To | Do This |
|---|---|
| Create New Device Configuration | Click New . For more information, see Create or Edit Device Information . |
| Delete a device | Click the Ellipsis button (...) and click Delete against the device member to be deleted. You cannot delete the Controller. The interface allows you to delete Members, but you must reinstall a Member device to add it back to the cluster. |
| Edit an existing device | Click the Ellipsis button (...) and click Edit against the device to be edited. Create or Edit Device Information . |

| Field | Description |
|---|---|
| Type | Displays the type of the server you are adding or editing. |
| Name* | The name of the device. |
| Host Address* | The IP address or hostname of the device. You cannot
                                             					 edit the IP address of the Controller on this page. You can edit the IP address of a Member on this page, but changing it here does not effect a change in the cluster. The cluster
                                             continues to recognize the original IP address for replication, and the replication will fail. For more information on the
                                             procedure to change the IP address of Unified Intelligence Center nodes in a cluster, see Changing the IP Address and hostname in Unified Intelligence Center . |
| Description | The
                                             					 description of the device. |