---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-emergency-responder-200473-configure-and-troubleshoot-cer-onsi-1f2bba55d5
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/emergency-responder/200473-Configure-and-Troubleshoot-CER-Onsite-Al.html
retrieved_at: 2026-08-17T00:11:07.168953+00:00
---

Configure and Troubleshoot CER Onsite Alert Email

# Configure and Troubleshoot CER Onsite Alert Email

### Download Options

Updated: May 5, 2016

Document ID: 200473

Contents

## Contents

## Introduction

This document describes the the steps to configure and troubleshoot Cisco Emergency Responder (CER) Onsite Alert Email notifications. When someone makes an emergency call (that is routed through CER), CER offers the ability route the emergency call to the public safety answering point (PSAP), and provides notification to onsite alert (security) personnel. Notifications to onsite alert personnel are made via IP Phone message, a web-based alert on the Emergency Responder end-user interface, and an email message or page if using email-based paging.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

The information in this document is based on CER version 10.5.2.13900-12

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Configure

Step 1. Navigate to the CER Admin page > System > CER Group Settings and configure the Simple Mail Transfer Protocol (SMTP) Mail Server ( You can use the IP or FQDN of the mail server), and the Source Mail ID.

The Source Mail ID is the name of an account on the mail server that is used to send mail to Onsite Alert personnel. You may want to create an account on your mail server specifically for email notifications from CER to users.  You do not need to configure System Administrator Mail ID for onsite alert to function, this is for system related messages.

Step 2. Navigate to the CER Admin page > ERL >  Onsite Alert Settings and configure the Onsite Alert Email Address field for any onsite alert personnel that you would like to receive email notifications. This is the email address of that user, if your user is John Smith and their internal email address is jsmith@<yourcompany>.com, you would enter jsmith@<yourcompany>.com.

Step 3. Navigate to the CER Admin page > ERL > Conventional ERL and verify that onsite alert personnel are assigned to Emergency Response Locations (ERLs).

Note that this is not a requirement, and this should only be done if you would like specific onsite alert personnel to receive notifications when emergency calls are made from phones associated with their respective ERLs.

If there are not onsite alert personnel assigned to ERLs you can assign them by navigating to the CER Admin page > ERL > Conventional ERL > Select the desired ERL to open the ERL configuration page . On the configuration page, in order to move onsite alert users from the Available Onsite Alert IDs section to the Onsite Alert IDs for the ERL section, click on the onsite alert user to select that user and then click the Add button. To save the configuration changes click on the Update button.

## Troubleshoot

Common Problems

- The settings for onsite alert are not configured correctly. This is the most common cause of issues with onsite alert email notifications. The best way to troubleshoot is to review the configuration and take a look at the traces.

- CER is not able to reach the Simple Mail Transfer Protocol (SMTP) server. First verify the configuration in CER. Next try to ping the IP address or Fully Qualified Domain Name (FQDN) (depending on configuration) from the Command Line Interface (CLI) of CER with utils network ping command. Note that just because you can ping the SMTP server, does not mean that something on the network does not block SMTP traffic from CER to the SMTP server. At this time the best way to troubleshoot this is a packet capture from CER, and from the SMTP server to verify that the information is sent from CER and received on the SMTP server.

Configure Traces

In order to  configure the appropriate trace levels for troubleshooting, navigate to the CER Admin Page > System > Server Settings and Select All for both Debug and Trace Package List and then click Update Settings to save the changes.

Trace Reading

The relevant traces for troubleshooting are the CERServer trace and in order to find it out, navigate to CER Serviceability > System Logs > CER Logs > CER Server page and find the CERServerXX.log file/files that cover the time of the emergency call.

In order to find the section of the CERServer trace that relates to the onsite alert email, search for sending onsite email notification you should find the line:

```
2616565: May 13 10:38:31.070 EDT %CER-CER_ONSITEALERT-7-DEBUG:Sending onsite email notification
```

More information relating to onsite alert email can be found out:

```
2616725: May 13 10:38:31.227 EDT %CER-CER_ONSITEALERT-6-INFO:SMTPServerName : 10.10.10.10
2616726: May 13 10:38:31.227 EDT %CER-CER_ONSITEALERT-6-INFO:FromAddress : CERSourceMailID
2616727: May 13 10:38:31.227 EDT %CER-CER_ONSITEALERT-7-DEBUG:Sending onsite email notification
2616729: May 13 10:38:31.239 EDT %CER-CER_ONSITEALERT-4-WARNING:Emergency call DetailsCaller Extension:7975Zone/ERL :TestERLLOCATION :Call Time :May 13, 2015 10:38:31 AM EDT
```

If the email was sent successfully, you must see this line:

```
2616991: May 13 10:38:40.559 EDT %CER-CER_ONSITEALERT-7-DEBUG:Onsite email notification sent successfully
```

Other Troubleshoot Techniques

The administration of the CER server and the SMTP server are often the responsibility of different individuals or groups within an organization. To quickly verify that CER sends messages before involving the administrator/administrators of the SMTP server you can test with an SMTP server application that runs on your desktop. You must be able to find an SMTP server to test with a quick search using your favorite search engine for a fake or dummy SMTP server.

Once you have the SMTP server downloaded and running, you will need to navigate to CER Admin page > System > CER Group Settings and modify the SMTP Mail Server settings in order to reflect the IP address of the PC/Laptop running the SMTP server. Remember to change the IP address back to the IP address of your corporate SMTP server after the testing.

Onsite Alert Email Example

EMERGENCY CALL DETAILS (Generated by CiscoER) Caller Extension : 7975 Display Name : Test Phone Zone/ERL : TestERL Location : Port Description : Call Time : May 13, 2015 10:38:31 AM EDT For detailed call information please refer to --  http://TestCERServer/ceruser

Emergency call Details Caller Extension:7975 Display Name :Test Phone Zone/ERL : TestERL LOCATION : Port Description : Call Time : May 13, 2015 10:38:31 AM EDT

Onsite Alert Email Field Details

Caller Extension: This is the directory number of the phone where 911 was dialed

Display Name

- CER 8.7 and later pulls the ASCII Display (Caller ID) from the line/extension configuration page of the calling number in Cisco Unified Communications Manager (CUCM), if this is set.

Zone/ERL

- This is the ERL that was used for the call and depends upon CER > ERL Membership > Switch Port or CER > ERL Membership > IP Subnets

Location

- For Switch Port based tracking Location is pulled from ELM Membership > Switch Port > Location , if configured. This can be configured manually, or pulled automatically from the switch (if a description is defined for the port on the switch). In order to do this, navigate to Phone Tracking > LAN Switch Details, check the Use port description as port location box and Click Save . This pulls the information from the switch (if it is defined for each port) when phone tracking runs.

- For Subnet based tracking the location can be set (for each subnet) when you configure the Subnet. In order to find, navigate to ERL Membership > IP Subnets .

Port Description

- This is pulled from the port description of the physical switch (show run), if it is configured (per port). If you use Subnet based tracking, there will be no set switch to pull the port description from, and CER uses whatever is configured for location.

Note: The URL used in the email can change depending on the version.

Note: CER 8.7 and later must display ASCII Display (Caller ID) from the line/extension config page of the calling number in CUCM, if this is set.

### Revision History

1.0

05-May-2016

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 05-May-2016 | Initial Release |