---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-configurati-d99fda220b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/configuration/guide/ucce_b_1251-configuration-guide-unified-cce/ucce_b_1251-configuration-guide-unified-cce_chapter_011.html
retrieved_at: 2026-08-16T14:50:59.473369+00:00
---

Configuration Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

# Configuration Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

Updated: February 5, 2020

Chapter: Unified CCE Administration

## Chapter: Unified CCE Administration

# Unified CCE Administration

## Unified CCE
                        	 Administration Applications

Unified CCE
                           		Administration is a web-based user interface that contains multiple
                           		applications used to manage agents, calls, bulk jobs, and settings.

This section provides a brief description
                           		of each application. For detailed information about each
                           		application, see the online help that accompanies it.

### Infrastructure Settings

Use the Infrastructure Settings to configure the following:

Inventory: Deployment model and the components in the inventory for that model.

Peripheral Gateways: This display-only tool shows details about the peripheral gateways and peripherals in your deployment.

Smart Licensing: Licensing model that delivers visibility into your license ownership and consumption. For more information
                                    on Smart Licensing, see the Smart Licensing section in Administration Guide for Cisco Unified Contact Center Enterprise https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/administration/guide/ucce_b_administration-guide-for-cisco-unified12_5.html

### Call Settings

Use the Call Settings to configure the following:

Route Settings (Media Routing Domain)

Bucket Interval

### User Setup

This provides details of all the Agents configured.

### Organizational Setup

Use the Organizational Setup to view and configure the following:

Skills:  This allows you to configure Precision Queue and Attributes.

Business Hours: This feature allows you to configure Normal day business hours and Special Day business hours, in addition
                                    to holiday configurations.

### Bulk Import

Use the Bulk Import tool to view and import in bulk, Agents and Single Sign-on settings

### Features

Use the Features tool to view and configure features like Single Sign-on.

## Configure Unified
                        	 CCE Administration for Remote Access

To access Unified CCE administration remotely using Internet Explorer 11 , you must add the configuration
                              				sever address to the list of trusted sites.

Administration
                                          			 clients and administration workstations can support remote desktop access. But,
                                          			 only one user can access a client or workstation at a time. Unified CCE does
                                          			 not support simultaneous access by several users on the same client or
                                          			 workstation.

Step 1

Launch Internet Explorer 11 .

Step 2

Go to Tools >
                                       			 Internet Options.

Step 3

Select the Security Tab.

Step 4

Select Trusted
                                          				Sites .

Step 5

Click the Sites button.

Step 6

In Add this
                                       			 website to the zone, type in the configuration server address as : https://<IP
                                          				address or FQDN> .

Step 7

Click the Add button.

Step 8

Click the Close button.

Step 9

Click the OK button.

## Internet Explorer Settings for Microsoft Windows 2012

If you are using Microsoft Windows 2012 and accessing Unified CCE Administration using Microsoft Internet Explorer 11 , you must enable the font download setting in Internet Explorer.

Step 1

Open Internet
                                       			 Explorer.

Step 2

Click the Tools menu, then click Internet
                                          				Options .

Step 3

Click the Security tab.

Step 4

Click Internet to highlight it, and then click Custom
                                          				level .

Step 5

Scroll down to Downloads > Font
                                          				download , click the Enable radio button, and then click OK .

Step 6

Click Yes on the Warning window that appears.

Step 7

On the
                                       			 Internet Options window, click Apply , and then click OK .

| Note | Administration
                                          			 clients and administration workstations can support remote desktop access. But,
                                          			 only one user can access a client or workstation at a time. Unified CCE does
                                          			 not support simultaneous access by several users on the same client or
                                          			 workstation. |
|---|---|

| Step 1 | Launch Internet Explorer 11 . |
|---|---|
| Step 2 | Go to Tools >
                                       			 Internet Options. |
| Step 3 | Select the Security Tab. |
| Step 4 | Select Trusted
                                          				Sites . |
| Step 5 | Click the Sites button. |
| Step 6 | In Add this
                                       			 website to the zone, type in the configuration server address as : https://<IP
                                          				address or FQDN> . |
| Step 7 | Click the Add button. |
| Step 8 | Click the Close button. |
| Step 9 | Click the OK button. |

| Step 1 | Open Internet
                                       			 Explorer. |
|---|---|
| Step 2 | Click the Tools menu, then click Internet
                                          				Options . The
                                       			 Internet Options window appears. |
| Step 3 | Click the Security tab. |
| Step 4 | Click Internet to highlight it, and then click Custom
                                          				level . The
                                       			 Security Settings - Internet Zone window appears. |
| Step 5 | Scroll down to Downloads > Font
                                          				download , click the Enable radio button, and then click OK . |
| Step 6 | Click Yes on the Warning window that appears. |
| Step 7 | On the
                                       			 Internet Options window, click Apply , and then click OK . |