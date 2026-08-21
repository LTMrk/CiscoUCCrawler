---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-calling-222804-collect-the-connector-logs-webex-calli-ht-3b6296efad
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-calling/222804-collect-the-connector-logs-webex-calli.html
retrieved_at: 2026-08-21T07:16:15.046397+00:00
---

Collect the Connector Logs - Webex Calling

# Collect the Connector Logs - Webex Calling

### Download Options

Updated: March 7, 2025

Document ID: 222804

Contents

## Contents

## Introduction

This document describes the process to collect Cisco IOS managed gateway connector logs in debug mode.

## Prerequisites

### Requirements

Access to Control Hub with Full Admin permissions.

Access to the CLI (Command Line Interface) of the Local Gateway.

Access to the Connector GuestShell.

### Components used

The information in this document is based on these software and hardware versions:

- Connector Application (GuestShell)

- Cisco IOS XE Software Version: 17.15.01a

- Script Version: 3.1.1

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

Gateway connectors are small applications installed and running on the Cisco IOS XE GuestShell container and help to maintain a secure connection to the Control Hub, coordinate events, and collect status information.

Note : For more information about gateway connectors, consult the document: Enroll Cisco IOS managed gateways to Webex Cloud

When you have an issue with the connector, connector logs in debugging level are required to troubleshoot.

## Steps to collect gateway connector logs in debugging level

Step 1. Sign in to the gateway using a console or an SSH connection, copy and paste the next command to the router exec command prompt:

tclsh https://binaries.webex.com/ManagedGatewayScriptProdStable/gateway_onboarding.tcl

Note : You can launch (or relaunch) the TCL script directly using tclsh bootflash:gateway_connector/gateway_onboarding.tcl or tclsh https://binaries.webex.com/ManagedGatewayScriptProdStable/gateway_onboarding.tcl at any given point.

Step 2. The connector main menu shows up:

```
===============================================================
                        Webex Managed Gateway Connector
        ===============================================================
             Options
               s :  Display Status Page
               v :  View and Modify Cloud Connector Settings
               e :  Enable Guestshell
               d :  Disable Guestshell
               l :  Collect Logs
               r :  Clear Logs
               u :  Uninstall Connector
               p :  Apply Patch
               q :  Quit

        ===============================================================
                        Select an option from the menu:
```

Press v to select the option View and Modify Cloud Connector Settings .

Step 3. From the next menu, press l to Modify log level for Cloud Connector .

```
===============================================================
                        Webex Managed Gateway Connector
        ===============================================================
                Script Version         : 3.1.1
                Hostname/IP Addr       : X.X.X.X
                DNS Server(s)          : X.X.X.X 8.8.8.8
                                         X.X.X.X
                Gateway Username       : doctorx
                External Interface     : GigabitEthernet2
        ===============================================================
             Options
               c :  Update Gateway Credentials
               e :  Update External Interface
               p :  Update Proxy Details
               n :  Update DNS Server
               k :  Update Connector Package Verification Key
               l :  Modify log level for Cloud Connector
               h :  Go to home menu
               q :  Quit

        ===============================================================
                        Select an option from the menu:
```

Step 4. From the next menu, choose the log level for the cloud connector.

```
===============================================
                  Number      Log Level
         ===============================================
                    1           DEBUG
                    2           INFO
                    3           WARNING
                    4           ERROR
                    5           CRITICAL
         ===============================================
```

Step 5. Press 1 to set the log level to DEBUG .

```
===============================================================
                        Webex Managed Gateway Connector
        ===============================================================

                    Cloud Connector log level is set to : 1

                ===============================================
                            Number        Log Level
                ===============================================
                                1           DEBUG
                ===============================================
        ===============================================================
                  Select option h for home menu or q to quit:
```

Step 6. Press h to go to the home menu.

```
===============================================================
                        Webex Managed Gateway Connector
        ===============================================================
             Options
               s :  Display Status Page
               v :  View and Modify Cloud Connector Settings
               e :  Enable Guestshell
               d :  Disable Guestshell
               l :  Collect Logs
               r :  Clear Logs
               u :  Uninstall Connector
               p :  Apply Patch
               q :  Quit

        ===============================================================
                        Select an option from the menu:
```

Step 7. Replicate the issue and then select l to get the connector logs. Once complete, the command line displays:

```
===============================================================
                        Webex Managed Gateway Connector
        ===============================================================

                Log files are collected and stored at location

            bootflash:/guest-share/gateway_webex_cloud_logs_2025025014034.tar.gz
        ===============================================================
                  Select option h for home menu or q to quit:
```

Step 8. Copy the bootlfash URL and press q to exit the GuestShell.

Note : You can relaunch the TCL script directly from the bootflash memory using tclsh bootflash:gateway_connector/gateway_onboarding.tcl preventing the gateway from downloading the script whenever the command is run.

## Export the Connector Logs

The connector logs are saved in the bootflash directory. You can use FTP, SCP, TFTP, SFTP and other file transfer network protocol, this depends on your preference.

This example assumes a TFTP server is used to transfer the connector log, modify it as needed.

Step 1. Add the next command in the gateway CLI.

```
Router#copy bootflash:/guest-share/gateway_webex_cloud_logs_2025025014034.tar.gz tftp://<TFTP_Server_IP>/<file_name>.tar.gz
```

Step 2. Enter the TFTP server address.

```
Address or name of remote host []? <TFTP_IP>
```

Step 3. Confirm the file name, then hit Enter .

```
Destination filename [gateway_webex_cloud_logs_2025025014034.tar.gz]?
!!
32137 bytes copied in 4.714 secs (6817 bytes/sec)
Router#
```

Step 4. Upload the .tar file to the Cisco TAC case.

### Revision History

1.0

07-Mar-2025

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 07-Mar-2025 | Initial Release |