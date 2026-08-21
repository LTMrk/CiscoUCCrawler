---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-ip-manager-assistant-cisco-unified-callmanager-40-200159-confi-8aa66685f1
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/ip-manager-assistant-cisco-unified-callmanager-40/200159-Configure-and-Troubleshoot-Cisco-IP-Mana.html
retrieved_at: 2026-08-21T13:54:35.347073+00:00
---

Configure and Troubleshoot Cisco IP Manager Assistant (IPMA)

# Configure and Troubleshoot Cisco IP Manager Assistant (IPMA)

Updated: January 13, 2021

Document ID: 200159

Contents

## Contents

## Introduction

This document describes the Cisco IPMA feature on a Call Manager. This feature enables to route the calls to manager/assistant effectively as per the requirement. Based on the filter set on the manager's phone, calls can be routed directly to the manager or to the assistant depending on manager's availability. Alternatively, the filters for manager can also be set from the assistant's phone, thereby, making it a scalable feature.

## Prerequisites

### Requirements

Cisco recommends that you have a basic knowledge of these topics:

- Call Routing and Computer Telephony Integration (CTI) Route Points

- Calling Search Space (CSS) and Partitions

- Configuring IP Phones on Cisco Unified Communications Manager (CUCM)

### Components Used

The information in this document is based on these software versions:

- Cisco Unified Communications Manager 9.1(2)

- Cisco IP Manager Assistant Service

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

Cisco IPMA feature is widely used in order to manage the calls to manager/assistant effectively. It provides redundancy by allowing to configure the primary and secondary IPMA servers in the cluster, however, at a time only one can be active.

This feature in two modes is based on the requirement:

- Proxy Line Mode

- Shared Line Mode

Proxy Line: Assistant's line on the phone acts as a proxy line to manager. Apart from Assistant's primary line, you need to configure a new line on assistant's phone for each manager associated with it. This created line for each manager on assistant phone acts as a proxy line. Cisco IPMA uses these proxy lines in order to attend the calls for manager from assistant's phone.

- CTI Route Point should have the same Directory Number (DN) as that of manager or the superset of it.

- CTI Route Point and Assistant DN must be reachable by all phones and to each other as well. However, Manager's DN must only be reachable from CTI Route Point and Assistant DN.

- This CTI Route Point needs to be configured in IPMA service parameters which associates it this service. Once associated, all the calls to Manager's phone hits the CTI Route Point since it is accessible by all phones and based on IPMA parameters the service will route the calls to assistant/manager.

- The CTI Route Point must be configured for the Call Forward No Answer feature to the Manager/Assistant phone so as not to drop in the call in case of IPMA down/CTI down.

Shared Line: In this mode, the line number on the Manager and Assistant phones is same. When a call comes to manager, it rings the assistant's phone at the same time. The manager or assistant can pick the phone as per requirement. If the manager does not want to take anymore calls and want's assistant to attend all the calls, the manager needs to enable Do Not Disturb (DND) option of the IPMA feature.

## Configure

Here are the pre-configuration tasks:

- Register two IP Phones on the Call Manager. (In this case Cisco 7975 & Cisco 7965)

- Create an enduser Assistant and associate this user with the Assistant's phone and vice versa. (In this case it is Cisco 7975: 00083031ED49 )

- Create an enduser Manager and associate this user with the Manager's phone and vice versa. (In this case it is Cisco 7965: F02929E2D831 )

Steps to configure IPMA:

- Create a Service for IPMA.

- Partitions and Calling Search Space.

- Configure Assistant Phone.

- Configure Manager Phone.

- Configure Manager Enduser.

- Configure Assistant Enduser.

- Configure CTI Route Point.

- Configure IPMA Service Parameter.

- Cisco Unified Communication Manager Assistant Console (optional)

### Step 1. Create Service for IPMA

- Log in to the CUCM Administration web GUI.

- Navigate to Device > Device Settings > Phone Services.

- Add a new Service and name it as IPMA.

- In the Service URL provide the URL: (CUCM - Call Manager). http://<CUCM-IP>:8080/ma/servlet/MAService?cmd=doPhoneService&Name=#DEVICENAME#

- Check the Enable parameter and click Save as shown in the image.

Note : If you use FQDN instead of IP address for IPMA server  , ensure it resolves into only one IP address

### Step 2. Partitions and Calling Search Space

- Log in to the CUCM Administration web GUI.

- Navigate to Call Routing > Class of Control > Partition .

- Create three partitions: ptmanager, ptinternal and pteveryone.

- Navigate to Call Routing > Class of Control > Calling Search Space .

- Create two CSS : generated_css_M_E(ptmanager+pteveryone) and generated_css_I_E:(ptinternal+pteveryone).

### Step 3. Configure Assistant Phone

- Log in to the CUCM Administration web GUI.

- Navigate to Device > Phone > Phone configuration page (Assistant Phone).

- Select the softkey template to Standard Assistant .

- Create a new line as a primary DN of Assistant in partition pteveryone and CSS as generated_css_I_E.

- Create a new line that acts as a proxy line for manager in partition pteveryone and CSS as generated_css_M_E as shown in the image.

- Navigate to Related Links > Subscriber/Unsubscriber Services and subscribe IPMA service for this phone as shown in the images.

### Step 4. Configure Manager Phone

- Log in to the CUCM Administration web GUI.

- Navigate to Device > Phone > Phone configuration page (Manager Phone).

- Select the softkey template to Standard Manager .

- Create a new line as a primary DN of Manager in partition ptmanager and CSS as generated_css_I_E.

- Navigate to Related Links > Subscriber/Unsubscriber Services and subscribe IPMA service for this phone.

### Step 5. Configure Manager Enduser

- Log in to the CUCM Administration web GUI.

- Navigate to User Management > End User.

- Create a new user Manager with appropriate credentials and details.

- Associate the Manager phone to this user from Device Association tab as shown in the image.

- Check the Allow Control of Device from CTI check box and Assisgn/Select the primary extention of the Manager as shown in this image.

- Navigate to the bottom of the page and select Add to Access Control Group and assign all CTI roles here as per the requirement.

- Navigate to the Related Links section > Manager Configuration > Go .

- Uncheck the Automatic Configuration check box and select the Phone device name for manager.

- Choose the assistant you want to associate with this manager. (You can associate more than one assistant if needed)

- Choose the lines that you need to be controlled by IPMA service over CTI and click Save as shown in the image.

- Navigate to the Manager phone device page and associate the Manager user here.

### Step 6. Configure Assistant Enduser

- Log in to the CUCM Administration web GUI.

- Navigate to User Management > End User.

- Create a new user Assistant with appropriate credentials and details.

- Associate the Assistant phone to this user from Device Association tab.

- Check the Allow Control of Device from CTI check box and Assign/Select the primary extension of the Assistant..

- Navigate to the page bottom and select Add to Access Control Group and assign all CTI roles here as per requirement.

- Navigate to the Related Links section > Assistant Configuration > Go .

- Uncheck the box for Automatic Configuration and select the Phone device name for Assistant.

- In the Associate Manager's box, all the Managers with whom this Assistant was associated, are listed out.

- In Manager Association to Assistant Line, choose any Available Line from assistant that you want to associate with any particular manager. Choose the Manager name for this line you want to associate. Choose the Manager line number which you want to associate with the available line of Assistant. Click Save .

### Step 7. Configure CTI Route Point

- Log in to the CUCM Administration web GUI.

- Navigate to Device > CTI Route Point > Add New.

- Provide any name and details as required.

- Add a new DN to this CTI Route Point which must match the Manager's DN. In case of more than one manager, the DN must be such that it matches the DNs of all managers (such as 50XX which uses wildcard characters).

- Assign the partition as ptinternal to it and CSS as generated_css_M_E as it must be reachable to all Manager DN's as shown in the image.

### Step 8. Configure IPMA Service Parameter

- Log in to the CUCM Administration web GUI.

- Navigate to System > Service Parameters.

- Select the Call Manager server > Cisco IP Manager Assistant.

- Set the primary CTI Manager and primary IPMA server IP address.

- Set the Route Point name being used for IPMA

- Rest all the parameters you can keep default and as per the configuration done in the cluster as shown in the images. Note : If you use FQDN instead of IP address for IPMA server  , ensure it resolves into only one IP address

Note : If you have configured more than one IPMA servers in the cluster, specify the IPMA server service that you want to use as primary on in Cisco IPMA Primary Phone Service and other as Secondary. For IPMA, local server can be configured as the CTI Server (recommended).

### Step 9. Cisco Unified Communication Manager Assistant Console

This is an application designed as an additional feature to the Assistant's that enables them to use all the Assistant phone features through the application (Assistant Console). The complete assistant phone is controlled via CUCM Assistant Console. The assistant can install the assistant console, a client-server java application, on a PC that runs Windows 2000, Windows XP, Windows Vista or Windows 7. The assistant console connects to the CUCM (IPMA) Service for login and directory services. Multiple assistant consoles can connect to a single CUCM IPMA Service.

In order to download this application:

- Log into the CUCM Administration web GUI.

- Navigate to Application > Plugins > Cisco Unified CM Assistant Console (download).

Once installed, the interface after configurations looks as shown in this image.

One additional feature that you can use exclusively through Assistant Console is Inclusive/Exclusive filtering of calls. When the inclusive filtering is enabled and filter mode is set to ON, Manager can still receive the calls from the numbers that match the patterns in this configuration. When exclusive filtering is enabled, filter ON/OFF would not make any difference, however, Manager would not receive the calls from the numbers which match the patterns in this configuration.

In order to configure these filters:

- Log in to the CUCM Assistant Console.

- Navigate to the My Managers > Manager (you want to configure) > Configuration as shown in the image.

- Create the patterns here as per the requirement as shown in this image.

Note : This illustrated configuration is for the basic IPMA functions. Based on the requirement, speed dials, intercom and additional lines can be added to Manager/Assistant phones.

### Network Diagram

This image illustrates the complete basic flowchart for the working of IPMA.

- If the filer mode is set to Exclusive, all the calls are diverted to the divert target irrespective of the filter ON/OFF as shown in the image.

- If the filer mode is set to Inclusive, all the calls are filtered to Manager/Assistant based on ON/OFF irrespective of the Divert ON/OFF as shown in the image.

- If Do Not Disturb option is turned on, based on the filter settings calls can still be diverted to Manager, however, the phone would not ring. Only the visual alerts with call information is visible on the Manager's phone as shown in the image.

- As per the design, if the phone was failover to the secondary server, it would not go back to the primary again even if it becomes active, until the secondary is down.

- If in case IPMA service is down, Call Forward No Answer (CFNA) can be configured for Manager's DN so as to avoid dropping of calls and keep them going.

- CTI Route points are not needed while using IPMA in shared line mode.

## Verify

Use this section in order to confirm that your configuration works properly.

- Check if the IPMA service is accessible from the Manager and Assistant Phones.

- IPMA icons (Assistant Watch Window) and softkeys must appear on the Manager phones.

- Check if the call gets routed to assistant phone when Manager's DN is dialled and filer is set to ON.

- Install Cisco Unified Communication Manager Assistant Console and log in as Assistant here. Try to set the IPMA filter's and call routing to check if it works fine.

- Turn off the IPMA service on primary server to check if the IPMA failover works as expected. (Even if the Cisco Tomcat service is down on the server, IPMA will failover)

## Troubleshoot

This section provides information you can use in order to troubleshoot your configuration.

### IP Phone support for IPMA

In order to start with, it is essential to verify and check on what all protocols the IP Phone supports the IPMA feature.

- Log in to the Cisco Unified Reporting page.

- Navigate to System Reports > Unified CM Phone Feature List

- Click the Unified CM Phone Feature List hyperlink under the Report Name to navigate to query page.

- Select the IP Phone model in the Product list and Feature as IPMA. for example, if the IP Phone supports this feature for SIP protocol then the output would be displayed as shown in this image. Else all the rows will be blank in the table if the phone does not support IPMA on any protocol.

### Common Checkpoints to Troubleshoot

- If you receive any kind of HTTP errors on phone while you access the IPMA service, recheck the Phone URL configured in the Phone Service configuration on CUCM. Here is the generic URL: http://<CUCM-Server-IP>:8080/ma/servlet/MAService?cmd=doPhoneService&Name=#DEVICENAME#

- Verify the exact IP address of the primary and secondary IPMA/CTI servers in the service parameter list of all the servers. (Incorrect config might result in CTI Route point unregistering frequently or IPMA icons being disappeared on the phones)

- Cross-verify if all the Manager/Assistant phones have subscribed to IPMA service.

- For any kind of issues that arises after any kind of change in the IPMA configuration, good practise is to restart these services: - Cisco IPMA - Cisco Tomcat - Cisco CTIManager

- For any related network issues for IPMA, by default port assigned for IPMA server communication is 2912. Verify is this is allowed on all the devices in between CUCM and IP Phone.

- While using the shared line mode, Uses Shared Lines option must be checked in the Manager configuration.

- If the issue still persists, please collect the below traces from Real Time Monitoring Tool (RTMT) and open a TAC case with them attached: Cisco IPMA Cisco CTIManager Cisco CallManager Cisco Tomcat (Ensure that you provide the user, IP Phone and cluster details with them)

### Common Cisco Bug IDs

CSCtg21509 & CSCup52338 : IPMA File not Found error on the IP Phones. (Reconfigure the Manager/Assistant configuration)

CSCuq44874 , CSCud90278 & CSCud11654 : IPMA Failover issues, if primary goes not it does not fallback to secondary.

CSCte60089 : IPMA Host not Found error on the IP Phones.

CSCun74352 : IPMA Vulnerability (that could allow an unauthenticated, remote attacker to access sensitive information on the affected device)

CSCvi54672 : IPMA functionality stopped working JTAPI event thread is still blocked by IPMA

## Related Information

### Contributed by Cisco Engineers

Sagar Wani

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager (CallManager)