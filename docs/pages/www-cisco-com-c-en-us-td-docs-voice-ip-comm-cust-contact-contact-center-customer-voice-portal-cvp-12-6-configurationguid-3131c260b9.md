---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-configurationguid-3131c260b9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/ConfigurationGuideCVP12_6/guide/ccvp_b_1261-configuration-guide-for-cisco-unified-customer-voice-portal/ccvp_m_1252-unified-communications-manager-configuration.html
retrieved_at: 2026-08-21T06:52:40.770569+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

Updated: June 11, 2024

Chapter: Unified Communications Manager Configuration

## Chapter: Unified Communications Manager Configuration

# Unified Communications Manager Configuration

## Configure Unified Communications Manager Server

Step 1

From the Operations Console, select Device
                                             				  Management > Unified CM .

Step 2

Click Add New to add a new Unified CM or click Use As Template to use an existing template to configure 
                                       		  the new Unified CM.

Step 3

Click the following tabs and configure the settings based on your call flow model:

General tab. For more information, see General Settings .

Device Pool tab. For more information about adding, deleting, and editing a device pool, see Add or Remove Device From Device Pool .

Enable Cisco AXL Web Service on the Unified CM for
                                                      				  the synchronization to work.

Step 4

To enable Cisco AXL Web Service on the Unified CM, perform the following steps:

Log on to Unified CM.

Open the Cisco Unified Serviceability dashboard and select Tools > Service Activation .

In the drop down menu, select the Unified CM server that is configured in this Operations Console, and click Go .

In the Database and Admin Services section, check the box next to Cisco AXL Web Service.

Step 5

Click Save .

## Unified CM Settings

### General Settings

Field

Description

Default

Value

Restart Required

IP Address

The IP address of the Unified CM Server.

None

Valid IP address

No

Hostname

The name of the Unified CM Server

None

Valid DNS names, includes letters in the
                                          						  alphabet, the numbers 0 through 9, and a dash.

No

Description

The description of the Unified CM Server

None

Any text

No

Device Admin URL

The Administration URL for the Unified CM Server

None

A valid URL.

The 
                                          						  Operations Console validates the URL for syntax errors but does no validation for the existence of the URL.

No

Enable Synchronization

Enable synchronization

Select to enable synchronization for location. If enabled,
                                          						  the Operations Console extracts  or synchronizes the Unified CM location
                                          						  information from the Unified CM server.

Disabled

When you enable this service, the default value of the Port is 8443.

Enabled or Disabled

No

Username

User name to access the Unified CM AXL interface.

None

Valid Unified CM AXL username.

No

Password

Password to access the Unified CM AXL interface.

None

Valid Unified CM AXL password.

No

Confirm Password

Retype the password to verify that you typed the password
                                          						  correctly.

None

Text must match the text entered in the Password field

No

Port

The port to which the Unified CM server connects while
                                          						  establishing initial contact.

8443

1 through 65,535

No

| Step 1 | From the Operations Console, select Device
                                             				  Management > Unified CM . |
|---|---|
| Step 2 | Click Add New to add a new Unified CM or click Use As Template to use an existing template to configure 
                                       		  the new Unified CM. |
| Step 3 | Click the following tabs and configure the settings based on your call flow model: General tab. For more information, see General Settings . Device Pool tab. For more information about adding, deleting, and editing a device pool, see Add or Remove Device From Device Pool . Note Enable Cisco AXL Web Service on the Unified CM for
                                                      				  the synchronization to work. | Note | Enable Cisco AXL Web Service on the Unified CM for
                                                      				  the synchronization to work. |
| Note | Enable Cisco AXL Web Service on the Unified CM for
                                                      				  the synchronization to work. |
| Step 4 | To enable Cisco AXL Web Service on the Unified CM, perform the following steps: Log on to Unified CM. Open the Cisco Unified Serviceability dashboard and select Tools > Service Activation . In the drop down menu, select the Unified CM server that is configured in this Operations Console, and click Go . In the Database and Admin Services section, check the box next to Cisco AXL Web Service. |
| Step 5 | Click Save . |

| Note | Enable Cisco AXL Web Service on the Unified CM for
                                                      				  the synchronization to work. |
|---|---|

| Field | Description | Default | Value | Restart Required |
|---|---|---|---|---|
| IP Address | The IP address of the Unified CM Server. | None | Valid IP address | No |
| Hostname | The name of the Unified CM Server | None | Valid DNS names, includes letters in the
                                          						  alphabet, the numbers 0 through 9, and a dash. | No |
| Description | The description of the Unified CM Server | None | Any text | No |
| Device Admin URL | The Administration URL for the Unified CM Server | None | A valid URL. The 
                                          						  Operations Console validates the URL for syntax errors but does no validation for the existence of the URL. | No |
| Enable Synchronization |  |
| Enable synchronization | Select to enable synchronization for location. If enabled,
                                          						  the Operations Console extracts  or synchronizes the Unified CM location
                                          						  information from the Unified CM server. | Disabled When you enable this service, the default value of the Port is 8443. | Enabled or Disabled | No |
| Username | User name to access the Unified CM AXL interface. | None | Valid Unified CM AXL username. | No |
| Password | Password to access the Unified CM AXL interface. | None | Valid Unified CM AXL password. | No |
| Confirm Password | Retype the password to verify that you typed the password
                                          						  correctly. | None | Text must match the text entered in the Password field | No |
| Port | The port to which the Unified CM server connects while
                                          						  establishing initial contact. | 8443 | 1 through 65,535 | No |