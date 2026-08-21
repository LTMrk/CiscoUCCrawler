---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-7-0-english-integration-notes-ibmstint-html-7062d011cc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/7_0/english/integration_notes/ibmstInt.html
retrieved_at: 2026-08-21T13:51:18.601187+00:00
---

Integration Note for Configuring the Cisco Click-to-Conference Plug-In with IBM Lotus Sametime

# Integration Note for Configuring the Cisco Click-to-Conference Plug-In with IBM Lotus Sametime

### Download Options

Updated: March 16, 2010

## Table Of Contents

Configuring the Cisco Click-to-Conference Plug-In with IBM Lotus Sametime

About the Cisco Click-to-Conference Plug-In for IBM Lotus Sametime

Overview of Components

Requirements for this Integration

Installing the Cisco Click-to-Conference Plug-In on the IBM Lotus Sametime Server

How to Configure the Cisco Click-to-Conference Plug-In on the IBM Lotus Sametime Server

Setting Cisco Click-to-Conference Plug-In Properties

Configuring the IBM Lotus Sametime Server for Cisco Click-to-Conference Plug-In Integration

How to Configure Cisco Unified Communications Manager for Cisco Click-to-Conference Plug-In Integration

Enabling Click-to-Conference Functionality on Cisco Unified Communications Manager

Configuring a SIP Trunk Security Profile

Configuring a SIP Trunk for Lotus Sametime Server

(Optional) Configuring Digest Authentication on the SIP Trunk

Creating and Authenticating an Application User

How to Optimize the Cisco Click-to-Conference Plug-In Integration

Cisco Click-to-Conference Plug-in Deployment in a Mixed User Environment

Enabling and Disabling the Cisco Click-to-Conference Plug-In Functionality on a Per-User Basis

How to Troubleshoot the Cisco Click-to-Conference Plug-In Integration

Known Limitations

Enabling Detailed Logging

Getting More Information

Cisco Unified Communications Manager

IBM Lotus Domino Server

IBM Lotus Sametime

Cisco Phone Control and Presence Plug-In

### Integration Guide

## Configuring the Cisco Click-to-Conference Plug-In with IBM Lotus Sametime

Revised: March 15, 2011

## 1 About the Cisco Click-to-Conference Plug-In for IBM Lotus Sametime

• Overview of Components

• Requirements for this Integration

### Overview of Components

The Cisco Click-to-Conference plug-in for IBM Lotus Sametime allows users to start an audio call with another person from a Sametime Connect client, and to invite additional people to join the call if required. The procedures in this document describe how to install the Cisco Click-to-Conference plug-in on an IBM Lotus Sametime server and how to configure Cisco Unified Communications Manager to handle the calls that the plug-in originates.

Figure 1 shows how the Cisco Click-to-Conference plug-in integrates with Sametime servers in the Cisco Unified Communications Manager network.

Figure 1 Cisco Click-to-Conference Plug-In Architecture

### Requirements for this Integration

Consult the table below for compatibility information before you install and configure the listed components required for this integration:

Components for This Integration

Cisco Click-to-Conference Plug-In Version

Cisco Unified Communications Manager Release

IBM Sametime Server Version

IBM Sametime Connect Client Version

[Optional] IBM Lotus Notes Version

6.0.1

6.x 1

7.5.1

7.5.1

Not applicable

6.1.2

6.x 1

7.5.1

7.5.1

Not applicable

7.0.1

6.x 1

7.x

8.x

8.0.x

8.0.x

8.0.1

8.0.1

6.x 1

7.x

8.x

8.5

8.5.1

8.5

8.5.1

8.5

8.5.1

1 Cisco Unified Communications Manager Release 6.x - only supports two-party calls

Troubleshooting Tips

• The optimum platform of the IBM Sametime server is version 8.0 or a higher version.

• Note that integration with IBM Lotus Notes is optional. If you complete this integration, you can access the native capabilities of IBM Lotus Sametime, as well as those exposed through plug-ins, from within IBM Lotus Notes.

## 2 Installing the Cisco Click-to-Conference Plug-In on the IBM Lotus Sametime Server

Before You Begin

• Ensure that you have installed and configured compatible software components for this configuration.

• If a Click-to-Call or Click-to-Conference plug-in is already installed on the Sametime server, uninstall the existing plug-in before you install the new plug-in (select Start > Control Panel > Add or Remove Programs) .

• Stop the Lotus Domino Server service on the computer where you want to install the Cisco Click-to-Conference plug-in and verify that this service is no longer running. Because you must stop the Lotus Domino Server service on the server, it may be more appropriate for you to perform this installation procedure after hours.

Step 1 Browse to http://www.cisco.com/cgi-bin/tablebuild.pl/cucplugin .

Step 2 Download the Cisco Click-to-Conference plug-in .exe file to the computer where you want to install the plug-in.

Step 3 Double-click the Cisco Click-to-Conference plug-in .exe file.

Step 4 Select Next when the InstallShield Wizard displays.

Step 5 Select Finish .

What To Do Next

Setting Cisco Click-to-Conference Plug-In Properties

Troubleshooting Tips

For information about starting or stopping a service, see the documentation that accompanied your operating system. For information about stopping the Lotus Domino Server service, see the IBM Lotus Domino documentation.

Related Topics

Requirements for this Integration

## 3 How to Configure the Cisco Click-to-Conference Plug-In on the IBM Lotus Sametime Server

• Setting Cisco Click-to-Conference Plug-In Properties

• Configuring the IBM Lotus Sametime Server for Cisco Click-to-Conference Plug-In Integration

### Setting Cisco Click-to-Conference Plug-In Properties

The settings that you configure here depend on which version of Cisco Unified Communications Manager you are currently deploying.

Before You Begin

Stop the Lotus Domino Server service, and verify that this service is no longer running. Do not restart the Lotus Domino Server until after you have configured at least one Cisco Unified Communications Manager to integrate with the Cisco Click-to-Conference plug-in.

Step 1 Open the following file using a text editor:

ClickToConfCUCM.properties

Step 2 Navigate to the following directory on the computer where you installed the Cisco Click-to-Conference plug-in:

\lotus\domino

Step 3 Specify the following variables for your Cisco Unified Communications Manager server as required:

• CUCMx_HOST [either a hostname or IP address]

• CUCMx_PORT [defaults to port 5060 if left unconfigured]

• CUCM_VERSION

Note The CUCM_VERSION parameter in the ClickToConfCUCM.properties file does not contain a default value. Set this parameter to 7 or greater to enable click-to-conference functionality within the Sametime Connect client. If you choose not to provide a value for this parameter, the plug-in defaults to work with Release 6.x of Cisco Unified Communications Manager. In addition, note that the plug-in behavior may be unpredictable if you configure an incorrect version of Cisco Unified Communications Manager.

Step 4 Specify any other parameters that are required for your installation.

Note To enable authentication, you must populate the appropriate REALMx, REALMx_USERNAME, REALMx_PASSWORD fields in the ClickToConfCUCM.properties file.

Step 5 Select Save .

Step 6 Perform the following actions:

a. Start the Lotus Domino Server service.

b. Verify that the Lotus Domino Server service is running.

What To Do Next

Configuring the IBM Lotus Sametime Server for Cisco Click-to-Conference Plug-In Integration

Troubleshooting Tips

• A README.txt file is delivered with the installer, and contains detailed information.

• See the ClickToConfCUCM.properties file for more information about the variables that you can configure.

• For information about starting or stopping a service, see the documentation sent with your operating system. For information about starting or stopping the Lotus Domino Server service, see the IBM Lotus Domino documentation.

Related Topics

Installing the Cisco Click-to-Conference Plug-In on the IBM Lotus Sametime Server .

### Configuring the IBM Lotus Sametime Server for Cisco Click-to-Conference Plug-In Integration

Before You Begin

Stop the Lotus Domino Server service and verify that this service is no longer running. Do not restart the Lotus Domino Server until after you have configured the Lotus Sametime Server.

Step 1 Enter the following URL to access your Lotus Sametime Server:

http:// server-address /stcenter.nsf

where

server-address is the domain name or IP address of your Lotus Sametime Server.

Step 2 Select Administer the Server .

Step 3 Log in to Lotus Sametime Server.

Step 4 Select Policies after you log in.

Step 5 Check Allow telephony for contact lists, instant messaging, and instant meetings.

Step 6 Perform the following actions:

a. Start the Lotus Domino Server service.

b. Verify that the Lotus Domino Server service is running.

Troubleshooting Tips

For information about starting or stopping a service, see the documentation that accompanied your operating system. For information about starting or stopping the Lotus Domino Server service, see the IBM Lotus Domino documentation.

Related Topics.

Setting Cisco Click-to-Conference Plug-In Properties

## 4 How to Configure Cisco Unified Communications Manager for Cisco Click-to-Conference Plug-In Integration

• Enabling Click-to-Conference Functionality on Cisco Unified Communications Manager

• Configuring a SIP Trunk for Lotus Sametime Server

• (Optional) Configuring Digest Authentication on the SIP Trunk

• Creating and Authenticating an Application User

### Enabling Click-to-Conference Functionality on Cisco Unified Communications Manager

Step 1 Select System > Service Parameters in Cisco Unified Communications Manager Administration.

Step 2 Select the Cisco Unified Communications Manager server with which your Sametime server is integrated.

Step 3 Select the Cisco CallManager service.

Step 4 Complete the following steps:

a. Locate the Enable Click-to-Conference for Third-Party Applications service parameter.

b. Set its value to True.

Step 5 Select Save .

What To Do Next

Configuring a SIP Trunk Security Profile

### Configuring a SIP Trunk Security Profile

You must configure a SIP trunk interface with Cisco Unified Communications Manager for click-to-conference functionality to work in Lotus Sametime.

Step 1 Select System > Security Profile > SIP Trunk Security Profile in Cisco Unified Communications Manager Administration.

Step 2 Select Add New in the Find and List SIP Trunk Security Profiles window.

Step 3 Enter a name and description for this SIP trunk security profile, for example, Click2Call Security Profile.

Step 4 Check Accept Out-of-Dialog REFER .

Step 5 Select Save .

What To Do Next

Configuring a SIP Trunk for Lotus Sametime Server

Related Topics

Enabling Click-to-Conference Functionality on Cisco Unified Communications Manager

### Configuring a SIP Trunk for Lotus Sametime Server

Before You Begin

Configure a SIP trunk security profile.

Step 1 Select Device > Trunk in Cisco Unified Communications Manager Administration.

Step 2 Select Add New in the Find and List Trunks window.

Step 3 Select SIP Trunk from the Trunk Type drop-down menu.

Step 4 For Device Protocol , accept the default value, SIP .

Step 5 Select Next .

Step 6 Enter a device name and description for this trunk, for example, Click2Call.

Step 7 For Device Pool , select Default .

Step 8 For Destination Address , enter the IP address of the Lotus Sametime Server.

Step 9 For SIP Trunk Security Profile , select the SIP trunk security profile that you created.

Step 10 For SIP Profile , select Standard SIP Profile .

Step 11 Select Save .

Step 12 Select Reset for your changes to take effect.

What To Do Next

(Optional) Configuring Digest Authentication on the SIP Trunk

Related Topics

Configuring a SIP Trunk Security Profile

### (Optional) Configuring Digest Authentication on the SIP Trunk

Although this procedure is optional, we recommend that you configure digest credentials to allow only authenticated users to make and receive calls.

If you configure digest authentication for SIP trunks, Cisco Unified Communications Manager challenges the identity of the SIP user agent that connects to the trunk every time that the trunk sends a SIP request to Cisco Unified Communications Manager. The SIP user agent, in turn, can challenge the identity of Cisco Unified Communications Manager.

Before You Begin

Configure a SIP trunk for Lotus Sametime server.

Step 1 Select System > Security Profile > SIP Trunk Security Profile in Cisco Unified Communications Manager Administration.

Step 2 Select Find in the Find and List SIP Trunk Security Profiles window.

Step 3 Select the SIP trunk security profile that you created for Cisco Click-to-Conference.

Step 4 Check Enable Digest Authentication .

Step 5 Select Save .

Step 6 Select Reset for your changes to take effect.

Step 7 Select System > Enterprise Parameters to configure the realm.

Step 8 Enter the appropriate value for the Cluster ID field.

Step 9 Select Save .

What To Do Next

Creating and Authenticating an Application User

Related Topics

Configuring a SIP Trunk for Lotus Sametime Server

### Creating and Authenticating an Application User

If you enable digest authentication on the SIP trunk, and allow Cisco Unified Communications Manager to challenge the identity of the SIP user agent, you must create an application user and provide the credentials for SIP authentication.

Before You Begin

• Configure digest authentication on the SIP trunk.

• To enable authentication, populate the appropriate REALMx, REALMx_USERNAME, REALMx_PASSWORD fields in ClickToConfCUCM.properties file, and then restart the Domino server for the changes to take effect.

Step 1 Select User Management > Application User .

Step 2 Select Add New in t he Find and List Application Users window.

Step 3 Enter and confirm the User ID and password of the application user.

Step 4 Enter and confirm the digest credentials for the application user.

Step 5 Check Accept Out-of-dialog REFER .

Step 6 Select Save .

Step 7 Select System > Security Profile > SIP Trunk Security Profile.

Step 8 Select Find in t he Find and List SIP Trunk Security Profiles window.

Step 9 To add the new application user to the profile, click the SIP trunk security profile that you created for the Cisco Click-to-Conference plug-in.

Step 10 Select Reset for your changes to take effect.

Related Topics

(Optional) Configuring Digest Authentication on the SIP Trunk

## 5 How to Optimize the Cisco Click-to-Conference Plug-In Integration

• Cisco Click-to-Conference Plug-in Deployment in a Mixed User Environment

• Enabling and Disabling the Cisco Click-to-Conference Plug-In Functionality on a Per-User Basis

### Cisco Click-to-Conference Plug-in Deployment in a Mixed User Environment

Note that a client plug-in, called Cisco Phone Control and Presence, is also available to enable phone control of Cisco IP Communicator from the Sametime Connect client. If your organization needs to deploy the Cisco Click-to-Conference plug-in (that works with IBM Lotus Sametime versions 7.5.1 and 8.0) for some IBM Sametime users and the Cisco Phone Control and Presence plug-in for other users, Cisco will support the simultaneous deployment of both plug-in types on a single Sametime server. However, we recommend that you do not allow users simultaneous access to both plug-ins.

In a mixed user environment, you should disable the Click-to-Conference plug-in for any users who are using another call or conferencing plug-in. Create multiple policies and do the following:

• assign users of the Click-to-Conference server plug-in to a policy that has telephony enabled

• assign users of any other client plug-in to a policy that has telephony disabled

What To Do Next

• Enabling and Disabling the Cisco Click-to-Conference Plug-In Functionality on a Per-User Basis

### Enabling and Disabling the Cisco Click-to-Conference Plug-In Functionality on a Per-User Basis

You can configure a new policy on the Lotus Sametime Server, assign users to it, and enable or disable the functionality provided by the Cisco Click-to-Conference plug-in.

Before You Begin

Review the recommended best practice for deploying a mixed plug-in environment.

Step 1 Enter the following URL to access the IBM Lotus Sametime Server:

http:// server-address /stcenter.nsf

where

server-address is the domain name or IP address of your Lotus Sametime Server.

Step 2 Select Administer the Server .

Step 3 Sign in to Lotus Sametime Server.

Step 4 Select Policies after you sign in.

Step 5 Select New .

Step 6 Enter a name and description for the new policy.

Step 7 Select the policy attributes to enable or disable telephony, and select OK.

Step 8 Select Assign Users.

Step 9 Complete the following actions in the Assign Users window:

• Select the directory from which to add users or groups to the policy.

• Search for or enter the names of the users or groups to add to the policy

• Add the selected users to the policy.

• Select OK.

Step 10 Complete the following actions to ensure your policy changes take effect:

• Restart the Lotus Domino Server service.

• Verify that the Lotus Domino Server service is running.

Related Topics

• Cisco Click-to-Conference Plug-in Deployment in a Mixed User Environment

• For more information about configuring the IBM Lotus Sametime server, see http://www-128.ibm.com/developerworks/lotus/documentation/sametime/

## 6 How to Troubleshoot the Cisco Click-to-Conference Plug-In Integration

• Known Limitations

• Enabling Detailed Logging

### Known Limitations

There are known IBM Lotus Sametime Issues (for which hotfixes are available) and known Cisco limitations with this integration. For more information, see the Release Notes for the Cisco Click-to-Conference Plug-In with IBM Lotus Sametime at this URL: http://www.cisco.com/en/US/products/ps9830/prod_release_notes_list.html

### Enabling Detailed Logging

If you experience problems with your Cisco Click-to-Conference plug-in integration, navigate to the Trace folder under the Domino directory, and look for warning or error messages in the log files located on the Sametime Server.

Table 1 identifies the files that control logs and debugs, and your troubleshooting next steps.

Table 1 Cisco Plug-in Log Files

Filename

File Function

Problem Resolution

telephony_x.log

By default, this file stores the Click-to-Call plug-in service logs.

Increase the amount of information recorded in this log.

For instructions about how to configure increased log verbosity, see SametimeDiagnostics_Telephony.properties. This file controls the type of information that gets logged and the amount of information that gets recorded for the Click-to-Conference plug-in service and sessions.

c2c_sip_combined.log

By default, this file stores the SIP library debugs.

Increase the amount of information recorded in thislog.

For instructions about how to configure increased log verbosity, see log4j.properties. This file controls the type of information that gets logged and the amount of information that gets recorded for the SIP library debugs.

c2c_sip_wire.log

By default, this file stores the SIP wire debugs.

Increase the amount of information recorded in thislog.

For instructions about how to how to configure increased log verbosity, see log4j.properties. This file controls the type of information that gets logged and the amount of information that gets recorded for the SIP wire (signalling) debugs.

## 7 Getting More Information

### Cisco Unified Communications Manager

For Cisco Unified Communications Manager documentation, see the following URL:

http://www.cisco.com/en/US/products/sw/voicesw/ps556/tsd_products_support_series_home.html

### IBM Lotus Domino Server

For information about installing or upgrading IBM Lotus Domino Server, see the following URL:

http://www-128.ibm.com/developerworks/lotus/documentation/domino/

### IBM Lotus Sametime

• Forinformation about installing and configuring Lotus Sametime, see the following URL:

http://www-128.ibm.com/developerworks/lotus/documentation/sametime/

• For more user support information on Lotus Sametime, see the following URL:

http://www-1.ibm.com/support/docview.wss?rs=477&uid=swg21195515

### Cisco Phone Control and Presence Plug-In

For information about installing and using the Cisco Phone Control and Presence plug-in for IBM Lotus Sametime, see the following URL:

http://www.cisco.com/en/US/products/ps9830/prod_installation_guides_list.html

### This Document Applies to These Products

- Unified Communications Manager (CallManager)

|  | Components for This Integration |
|---|---|
| Cisco Click-to-Conference Plug-In Version | Cisco Unified Communications Manager Release | IBM Sametime Server Version | IBM Sametime Connect Client Version | [Optional] IBM Lotus Notes Version |
| 6.0.1 | 6.x 1 | 7.5.1 | 7.5.1 | Not applicable |
| 6.1.2 | 6.x 1 | 7.5.1 | 7.5.1 | Not applicable |
| 7.0.1 | 6.x 1 7.x 8.x | 8.0.x | 8.0.x | 8.0.1 |
| 8.0.1 | 6.x 1 7.x 8.x | 8.5 8.5.1 | 8.5 8.5.1 | 8.5 8.5.1 |

| 1 Cisco Unified Communications Manager Release 6.x - only supports two-party calls |
|---|

| Filename | File Function | Problem Resolution |
|---|---|---|
| telephony_x.log | By default, this file stores the Click-to-Call plug-in service logs. | Increase the amount of information recorded in this log. For instructions about how to configure increased log verbosity, see SametimeDiagnostics_Telephony.properties. This file controls the type of information that gets logged and the amount of information that gets recorded for the Click-to-Conference plug-in service and sessions. |
| c2c_sip_combined.log | By default, this file stores the SIP library debugs. | Increase the amount of information recorded in thislog. For instructions about how to configure increased log verbosity, see log4j.properties. This file controls the type of information that gets logged and the amount of information that gets recorded for the SIP library debugs. |
| c2c_sip_wire.log | By default, this file stores the SIP wire debugs. | Increase the amount of information recorded in thislog. For instructions about how to how to configure increased log verbosity, see log4j.properties. This file controls the type of information that gets logged and the amount of information that gets recorded for the SIP wire (signalling) debugs. |