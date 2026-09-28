---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-214233-configure-se-4bb65db3c6
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/214233-configure-self-provisioning-feature-on-c.html
retrieved_at: 2026-08-21T13:58:42.504842+00:00
---

Configure Self-Provisioning Feature on CUCM  (IVR Based)

# Configure Self-Provisioning Feature on CUCM  (IVR Based)

### Download Options

Updated: March 27, 2019

Document ID: 214233

Contents

## Contents

## Introduction

This Document describes how to configure Self-Provisioning Feature on CUCM (IVR Based).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Communication Manager.

- Voice over Internet Protocol (VoIP)

- Phone Registration Process.

### Components Used

The information in this document is based on Cisco Unified Communications Manager 10.5

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

### What is Self-Provisioning?

Self-Provisioning is a feature introduced in the 10.x release of Cisco’s Unified Communications Manager (CUCM). It provides a plug and play type of functionality that simplifies the phone deployment process. Using auto-registration , some template and profile configurations, along with an IVR service, CUCM administrators have the ability to deploy phones with minimal upfront configuration.

Self-Provisioning (IVR Based) similar in function to the old Tool for Auto-Registered Phones (TAPS) method. The key difference with Self-Provisioning is that the IVR service runs on CUCM so you don’t need UCCX as you do with TAPS.

## Configure

1. Create a Universal Device template (UDT).

Step 1. Navigate to User management > User Phone add > Universal Device Template and Add New Template.

Step 2. Apply the Configuration that you expect the phones to take after auto registration to the new UDT.

2. Create Universal Line Template (ULT).

Step 1. Navigate to User Management > User/Phone Add > User Line Template , as shown in the image.

Step 2. Add the Route partition and CSS that is expected on the Phone after Auto Registration.

Note : These Universal Device Template and Universal Line Template should be linked with Auto registration so that the Phones Can take the Configuration when Auto-Registered.

3. Add the Templates to the CUCM node for Auto-registration Configuration and navigate to System > Cisco Unified CM , as shown in the image.

4. Add a New User Profile for Self-Provisioning.

Step 1. Navigate to User Management > User Settings > User Profile , as shown in the image.

Step 2. Add the User Device Template, User Line Template and Check the Allow End User to Provision their Own Phone CheckBox.

Note : These Setting Are Applied When the Users try to Self-Provision the Devices with Their own Extensions.

Note : You Can Also set a Maximum Limit to Users for Number of Devices After Which the Self Provisioning would not work for Users. E.g.: if User has 9 devices assigned already since the Maximum limit in Above screenshot is set to 10, User can self-provision only one Device.

Note : If the “Allow End User to Provision their Own Phone” Check-box is left unchecked. Self-Provisioning would not work for Users.

5. Create Feature Template Group and assign the User Profile. Now navigate to User Management > User/Phone Add > Feature Group Template and click Add New .

6. Create a user from Quick user/phone add page and Add the Feature Group Template .

Step 1. Navigate to User management > User Phone Add > Quick User/Phone Add .

Step 2. Add the Standard CCM End Users under Access Control Group membership.

Step 3. Add an extension in the extension field to the User, click on + Icon under Action to enable the Field.

Step 4. If a New Extension is to be created click on New and Add a New DN, as shown in the image option 1. If the Extension already Exists on CUCM and is to be assigned to User, choose that from Dropdown menu shown in option 2 of the image here.

Note : Once the User is Created, it Takes Primary Line as Self-Service User ID by default.

7. Verify the End User has received the primary Extension , Self-service User ID, User Profile and Standard CCM End User Role . Now navigate to User Management > End User and Access the newly Created User, as shown in the image.

8. In order to create a CTI Route point , navigate to Device > CTI Route Point , and click on Add New , as shown in the image.

Step 1. Add the Name and Device Pool entries and click on Save , as shown in the image.

Step 2. Add a Directory Number to the CTI Route Point,

9. In order to add a New Application User , navigate to User Management > Application User , and click on Add New .

Step 1. Add the Created CTI Route Point , under Controlled Devices

Step 2. Add the Standard CTI Enabled and Standard CTI Allow Control of All Devices under Permission Information Section.

10. Self-Provisioning Service Can be Set up at the System Level to Use Secure mode and a Password can be set. This feature is set to Non-Authentication Required Mode by default, which Does not Require any PIN to Use Self Provisioning.

Step 1. Navigate to User Management > Self-Provisioning.

Step 2. Add the CTI Route Point and Application User to Self-Provisioning .

Note : Every time a Configuration change is made on IVR Settings, a Restart of Self Provisioning IVR Setting is required to trigger the change.

### Services Associated with Self-Provisioning

Cisco Call Manager

This Service is associated with the Phone registration and Must be enabled on the Node to which registration is attempted.

Self Provisioning IVR

This Service can be found under CM services on Feature Services Page In Cisco Unified Serviceability.

Note : You can configure self-provisioning even if the service is deactivated, but the administrator cannot assign IP phones to users using the IVR service. By default, this service is deactivated.

Note : Self-provisioning IVR service runs only on Publisher.

### End-user experience on the Phone

- End User Dials the CTI Route Point and is Prompted to enter the Self-Service ID.

- The user is asked to Confirm the Self-Service ID and enter the PIN.

- Once the PIN is verified the Device goes for a reboot to get the new Extension.

## Troubleshoot

Error: Alert “device Cannot be provisioned” is received.

Cause: Device is Already Provisioned, cannot be re-provisioned.

### Logs to be Collected

In order to further troubleshoot, Collect the “Self-Provisioning IVR service” Log from RTMT.

File names are of format PnP#####.log.  (# represents a number.)

The Traces are Set to Info Level by Default.

The maximum file size is 1 MB by default. The maximum number of stored files defaults to 10.

Note : When you change either the Maximum No. of Files or the Maximum File Size settings in the Trace Configuration window, the system deletes all service log files except for the current file, that is, if the service runs. If the service has not been activated, the system deletes the files immediately after you activate the service.

### Known defects

CSCun16461

## Related Information

- Technical Support & Documentation - Cisco Systems