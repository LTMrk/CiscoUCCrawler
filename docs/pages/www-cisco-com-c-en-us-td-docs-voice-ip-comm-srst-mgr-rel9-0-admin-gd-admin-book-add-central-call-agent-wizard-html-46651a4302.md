---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-add-central-call-agent-wizard-html-46651a4302
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/add_central_call_agent_wizard.html
retrieved_at: 2026-08-21T23:38:17.894892+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 5, 2014

Chapter: Using the Central Call Agent Wizard to Add Cisco Unified Communications Manager Information

## Chapter: Using the Central Call Agent Wizard to Add Cisco Unified Communications Manager Information

- Supported AXL Versions

- Supported Phones and Platforms

## Using the Central Call Agent Wizard to Add Cisco Unified Communications Manager Information

The Add Central Call Agent Wizard adds Cisco Unified Communications Manager information that identifies Cisco Unified Communications Manager to Cisco Unified Survivable Remote Site Telephony (SRST) Manager. No changes are made to the Cisco Unified Communications Manager configuration.

Note When deploying Cisco Unified Enhanced-Survivable Remote Site Telephony, Cisco Unified SRST Manager can be configured for only one central call agent. Do not configure more than one installation of Cisco Unified SRST Manager to access the same Cisco Unified Communications Manager, which is the only central call agent that Cisco Unified SRST Manager supports for E-SRST.

Before You Begin

Collect the following information before you add a Cisco Unified Communications Manager:

Table 6 Central Call Agent Parameters

CUCM Hostname

Hostname or IP Address

Identifies the Cisco Unified Communications Manager to Cisco Unified SRST Manager.

Configuring DNS server is optional. You can enter either a hostname or IP address. If you enter an IP address, the system performs a DNS reverse look-up to store the Cisco Unified Communications Manager by hostname.

Note The DNS server forward and reverse tables should be set up with the IP address and hostname of Cisco Unified Communications Manager.

CUCM AXL Interface

AXL Username

The user name that Cisco Unified SRST Manager uses to access the Cisco Unified Communications Manager AXL interface.

This user name must exist on the Cisco Unified Communications Manager as an “application user” and be assigned the role of “standard AXL API access” or “standard CUCM super users.”

AXL Password

The password that corresponds to the Cisco Unified Communications Manager AXL interface user.

This password must correspond to the password configured on Cisco Unified Communications Manager for this user name.

Note If the password changes on Cisco Unified Communications Manager, you must also change the password in Cisco Unified SRST Manager. There is no automatic password synchronization for AXL credentials.

CUCM Cluster

Cluster Name

A descriptive name that uniquely identifies this Cisco Unified Communications Manager cluster. By default, the system uses the hostname that you entered at the beginning of this wizard as the cluster name.

Secondary Node

A second member of the Cisco Unified Communications Manager cluster to be used by Cisco Unified SRST Manager provisioning when the Cisco Unified SRST Manager cannot contact the primary Cisco Unified Communications Manager.

CUCM Schedule

Defines how often you want Cisco Unified SRST Manager to contact Cisco Unified Communications Manager to synchronize configuration data.

Schedule

Enable or disable scheduled provisioning.

Note By default, schedule provisioning is enabled and set to at 12 a.m. EST everyday. If schedule provisioning is disabled, the default schedule is not effective and other schedule parameters fields are grayed out.

Daily

Frequency in days.

Enter the number of days between provisioning cycles.

Weekly

Frequency in weeks.

Enter the number of weeks between provisioning cycles and the day of the week.

Monthly

Frequency in months.

Enter the day of the month.

Note If the day of the month is beyond the number of days the month contains, the provisioning occurs on the last day of that month. (For example if you configure provisioning for the 31st day of every month, provisioning for February occurs on the last day of the month.)

Enter the number of months between provisioning cycles.

Start Time

Start time for the provisioning cycle. This indicates the time of day at which Cisco Unified SRST Manager initiates contact to Cisco Unified Communications Manager.

End Time

(Optional) Indicates whether Cisco Unified SRST Manager should suspend provisioning at a certain time.

If you do not enter an end time, the system continues provisioning until all sites have been processed.

If you enter an end time, and the end time is reached during a provisioning cycle, the system suspends provisioning and waits until the next provisioning cycle to continue, at which time any sites not yet provisioned from the previous cycle will be processed first.

Call Agent Time Zone

Indicates the time zone in which the Cisco Unified Communications Manager is physically located. This enables the start and end times to be specified relative to the Cisco Unified Communications Manager time so that peak call load hours can be avoided.

Step 1 Select Setup Wizards > Add Central Call Agent .

The system displays the Introduction page of the Add Central Call Agent Wizard.

Step 2 Click Next .

The system displays the Unified Communications Manager Hostname page of the Add Central Call Agent Wizard.

Step 3 Enter the Cisco Unified Communications Manager hostname or IP address.

Step 4 Click Next .

The system displays the Unified Communications Manager AXL Interface page of the Add Central Call Agent Wizard.

Step 5 Enter the following information:

Step 6 Click Next .

The system displays a message stating that it will contact the Cisco Unified Communications Manager and downloads all the configured cluster nodes. This can take a few minutes.

Step 7 Click OK at the warning message.

The system displays the Unified Communications Manager Cluster page of the Add Central Call Agent Wizard.

Step 8 Enter the Cisco Unified Communications Manager cluster name and select a secondary node.

Step 9 Click Next .

The system displays the Unified Communications Manager Schedule page of the Add Central Call Agent Wizard.

Step 10 Enter information about how often Cisco Unified SRST Manager should contact Cisco Unified Communications Manager to retrieve configuration information. See CUCM Schedule .

Step 11 Enter a start time. You can optionally enter an end time.

Step 12 Enter a time zone.

Step 13 Click Next .

The system displays the CUCM Enable page of the Add Central Call Agent Wizard. You can set Enable Provisioning to either On or Off. If Off is selected, scheduled provisioning is not activated.

Step 14 Set Enable Provisioning to On to enable Cisco Unified SRST Manager to access Cisco Unified Communications Manager.

Step 15 Click Finish to complete the Central Call Agent Wizard and save this information.

Related Topics

## Supported AXL Versions

The following AXL versions are supported for Cisco Unified SRST Manager:

Table 7 Supported AXL Versions

9.0.4

9.1, 9.0, and 8.5

7.0.1

9.0.6

10.5, 10.0, 9.1, 9.0 and 8.5

8.5

11.0

11.0,10.5, 10.0, 9.1, and 9.0

9.0

## Supported Phones and Platforms

Refer to Cisco Unified SRST Manager Compatibility Matrix for more information on the following:

- Supported Phones

This section lists all the phone models supported by Cisco Unified SRST Manager.

- Supported Administrative XML (AXL) versions

This section provides the list of AXL versions supported by Cisco Unified SRST Manager.

- ESRST Scalability

This section provides the information on increase in scalability for E-SRST.

- New Platforms Supported

This section provides the list of platforms that are newly supported from Cisco Unified SRST Manager 11.0.0 Release.

- Fast track support

Fast track is supported only for SIP phones available from Cisco IOS Release 15.3(3)M, or Cisco Unified Communications Manager Express 10.0 or Cisco Unified SRST 10.0. Some phones are natively supported in Cisco Unified Communications Manager Express, Cisco Unified SRST or Cisco Unified E-SRST, which is known as inbuilt support.

For information on fast track use cases for Cisco Unified SRST Manager phone configuration, see Cisco Unified SRST Manager Compatibility Matrix .

| Parameter | Description |
|---|---|
| CUCM Hostname |
| Hostname or IP Address | Identifies the Cisco Unified Communications Manager to Cisco Unified SRST Manager. Configuring DNS server is optional. You can enter either a hostname or IP address. If you enter an IP address, the system performs a DNS reverse look-up to store the Cisco Unified Communications Manager by hostname. Note The DNS server forward and reverse tables should be set up with the IP address and hostname of Cisco Unified Communications Manager. |
| CUCM AXL Interface |
| AXL Username | The user name that Cisco Unified SRST Manager uses to access the Cisco Unified Communications Manager AXL interface. This user name must exist on the Cisco Unified Communications Manager as an “application user” and be assigned the role of “standard AXL API access” or “standard CUCM super users.” |
| AXL Password | The password that corresponds to the Cisco Unified Communications Manager AXL interface user. This password must correspond to the password configured on Cisco Unified Communications Manager for this user name. Note If the password changes on Cisco Unified Communications Manager, you must also change the password in Cisco Unified SRST Manager. There is no automatic password synchronization for AXL credentials. |
| CUCM Cluster |
| Cluster Name | A descriptive name that uniquely identifies this Cisco Unified Communications Manager cluster. By default, the system uses the hostname that you entered at the beginning of this wizard as the cluster name. |
| Secondary Node | A second member of the Cisco Unified Communications Manager cluster to be used by Cisco Unified SRST Manager provisioning when the Cisco Unified SRST Manager cannot contact the primary Cisco Unified Communications Manager. |
| CUCM Schedule |
| Defines how often you want Cisco Unified SRST Manager to contact Cisco Unified Communications Manager to synchronize configuration data. Tip We recommend that you schedule Cisco Unified SRST Manager to contact the Cisco Unified Communications Manager during off-peak hours. |
| Schedule | Enable or disable scheduled provisioning. Note By default, schedule provisioning is enabled and set to at 12 a.m. EST everyday. If schedule provisioning is disabled, the default schedule is not effective and other schedule parameters fields are grayed out. |
| Daily | Frequency in days. Enter the number of days between provisioning cycles. |
| Weekly | Frequency in weeks. Enter the number of weeks between provisioning cycles and the day of the week. |
| Monthly | Frequency in months. Enter the day of the month. Note If the day of the month is beyond the number of days the month contains, the provisioning occurs on the last day of that month. (For example if you configure provisioning for the 31st day of every month, provisioning for February occurs on the last day of the month.) Enter the number of months between provisioning cycles. |
| Start Time | Start time for the provisioning cycle. This indicates the time of day at which Cisco Unified SRST Manager initiates contact to Cisco Unified Communications Manager. |
| End Time | (Optional) Indicates whether Cisco Unified SRST Manager should suspend provisioning at a certain time. If you do not enter an end time, the system continues provisioning until all sites have been processed. If you enter an end time, and the end time is reached during a provisioning cycle, the system suspends provisioning and waits until the next provisioning cycle to continue, at which time any sites not yet provisioned from the previous cycle will be processed first. |
| Call Agent Time Zone | Indicates the time zone in which the Cisco Unified Communications Manager is physically located. This enables the start and end times to be specified relative to the Cisco Unified Communications Manager time so that peak call load hours can be avoided. |

| Cisco Unified SRST Manager Version | Supported Cisco Unified CM Versions | Supported AXL Versions |
|---|---|---|
| 9.0.4 | 9.1, 9.0, and 8.5 | 7.0.1 |
| 9.0.6 | 10.5, 10.0, 9.1, 9.0 and 8.5 | 8.5 |
| 11.0 | 11.0,10.5, 10.0, 9.1, and 9.0 | 9.0 |