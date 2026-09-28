---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-plm-11-5-1-su-1-userguide-cplm-b-user-guide-rel-1151su1-cplm-b-user-gui-f0df3e42d2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/plm/11_5_1_SU_1/userguide/cplm_b_user-guide-rel-1151SU1/cplm_b_user-guide-rel-1151a_chapter_0110.html
retrieved_at: 2026-09-08T04:59:24.751325+00:00
---

Cisco Prime License Manager User Guide, Release 11.5(1)SU1

# Cisco Prime License Manager User Guide, Release 11.5(1)SU1

Updated: November 6, 2016

Chapter: Troubleshooting

## Chapter: Troubleshooting

# Troubleshooting

The following are
		recommended troubleshooting steps to address common issues that may occur when
		using Cisco Prime License
		  Manager :

## Unknown Username
	 and Password

### Description

I do not know the
		  username and password of the system when it was originally installed, so I
		  cannot log into Cisco Prime License Manager .

### Resolution

Log into the
		  platform CLI with the OS administration credentials and use the license management list
			 users command to view the username to use for signing into the Cisco Prime License Manager application. If you are
		  not sure what the password is for this username, you can use the license
			 management reset user password command to change this password.

## Configuration
	 Changes Are Not Appearing

### Description

I made a
		  configuration change in my products, but I am not seeing a change in the
		  requested licenses reflected in Cisco Prime License Manager .

### Resolution

Cisco
			 Prime License Manager synchronizes with products every 24 hours. If
		  you wish to see the latest configuration changes, Update Usage Details from the License Usage Report window and then select Product Instances and
		  click Synchronize
			 Now .

## The Cause of The
	 Error Is Unknown

### Description

I received the
		  following error message "The cause of the
			 error is unknown" .

### Resolution

Check the Cisco Prime License Manager diagnostic log for
		  details. To access diagnostic logs, see Accessing Diagnostic Logs .

If the cause of
		  the error is not easily identifiable from these details, please open a Service
		  Request using the TAC Service Request Tool, https:/​/​tools.cisco.com/​ServiceRequestTool/​scm/​mgmt/​case . Please have your valid Cisco.com user ID and password
		  available. As an alternative, you may also call our main Technical Assistance
		  Center at 800-553-2447.

## Product Instance was not Added

### Description

I tried to add a product instance for Cisco Unified Communications Manager but received a 401 error.

### Resolution

Check the status of the Cisco Unified Communications Manager account by executing the following CLI command: show accountlocking . You can only add a product instance if the account is unlocked. Disable the lock on the account using the following command: set accountlocking disable .

## Product Instance
	 was Deleted, but is Still Showing Up in License Usage Data

### Description

I deleted a
		  product instance, but I do not see it reflected in the license usage data
		  reported on the Dashboard and Licenses > Usage .

### Resolution

When a product
		  instance is deleted from Cisco Prime License Manager , usage data is not
		  available until the Cisco Prime License Manager synchronizes with the
		  product instance. Synchronization happens once every 24 hours, or can be
		  manually requested from Monitoring > License Usage using the Synchronize Now button.

## Product Instance
	 Was Added and Is Not Showing Up in License Usage Data

### Description

I added a product
		  instance, but I do not see it reflected in the license usage data in Monitoring > Dashboard and Dashboard > License Usage .

### Resolution

When a product
		  instance is added to the Cisco Prime License Manager , usage data is not
		  available until the Cisco Prime License Manager synchronizes with the
		  product instance. Synchronization happens once every 24 hours, or can be
		  manually requested from Monitoring > License Usage using the Synchronize Now button.

## License Usage Data
	 in Product Admin GUI Does Not Match Product Instances View

### Description

The license usage
		  data in the administration GUI for that product (for example, when I select Product Instances > Launch Admin GUI) does not match the license usage
		  reported at Cisco Prime License Manager in Product Instances (select Product
		  Instance Name).

### Resolution

Changes in the
		  configuration of a product instance are not seen in the Cisco Prime License Manager until the next
		  synchronization following the configuration change. Synchronization happens
		  once every 24 hours. 
		 If
		  you wish to see the latest configuration changes, Update Usage Details from the License Usage Report window and then select Product Instances and
		  click Synchronize
			 Now .

## Non-Compliance Alerts are not Appearing when License Manager Goes into Non-Compliance

### Description

I am not receiving
		  any alerts when my Cisco Prime License Manager goes into non-compliance.

### Resolution

Non-compliance alerts are
		  generated by the product instances, not by Cisco Prime License Manager . Ensure that the product
		  supports non-compliance alerting. If a product supports non-compliance alerting, it must be
		  configured in the GUI for that product. For example, the administration
		  interface in Cisco Unified Communications Manager allows you to specify which conditions are alerted and
		  in what manner. Therefore, if you are not seeing non-compliance alerts for Cisco Unified Communications Manager,
		  you should verify that non-compliance alerts are configured in Cisco Unified Communications Manager. If not, the
		  alerts will be visible in the administration interface, but you will not
		  receive those alerts via the mechanism you have selected (for example, email,
		  SNMP, syslog).

## License Manager
	 Does Not Indicate a Product Overage

### Description

My product says it
		  is in overage, but my Cisco Prime License Manager does not show overage.

### Resolution

If a product
		  instance is unable to synchronize with its Cisco Prime License Manager , it goes into overage
		  because it is unable to confirm that there are licenses available. Please check
		  the last synchronization date for the product instance under Inventory >
		  Product Instances. If synchronization is not occurring, verify that the
		  credentials in the Cisco Prime License Manager for the product instance
		  are accurate and that there is network connectivity between your Cisco Prime License Manager and the product instance.

## Licenses Are
	 Missing Following Restoration of License Manager on a Different Server

### Description

I have restored my Cisco Prime License Manager on a different server and
		  I do not have any licenses.

### Resolution

When you move your Cisco Prime License Manager to a different virtual
		  server, your licenses need to be rehosted to the new server and reinstalled.
		  Please open a Service Request using the TAC Service Request Tool, https:/​/​tools.cisco.com/​ServiceRequestTool/​scm/​mgmt/​case , or send an email to licensing@cisco.com
		  for next steps. Please have your valid Cisco.com user Id and password
		  available. As an alternative, you may also call our main Technical Assistance
		  Center at 800-553-2447.

## Cannot Bring
	 System into Compliance Using the Upgrade Licenses Wizard

### Description

In the Licenses > Planning > Create an Add Licenses Plan wizard, I am unable to bring the
		  system into compliance.

### Resolution

If, across all the
		  product instances managed by your Cisco Prime License Manager , you are using more
		  licenses than are already installed combined with those available from the
		  product instances you are upgrading, you will not have sufficient licenses to
		  upgrade to bring your Cisco Prime License Manager into compliance. You will
		  need to purchase additional licenses to cover your needs, or reduce the number
		  of licenses required by your product instances by changing their configuration.

| Note | From the License Counts window of the Create an Add Licenses Plan wizard, click Run Compliance
			 Check to determine your license count needs. If your receive a
		  message stating "Compliance Check Passed", you have a sufficient number of
		  licenses and can click Next to move to the next window in the wizard. For more
		  information, see Create a License Plan |
|---|---|