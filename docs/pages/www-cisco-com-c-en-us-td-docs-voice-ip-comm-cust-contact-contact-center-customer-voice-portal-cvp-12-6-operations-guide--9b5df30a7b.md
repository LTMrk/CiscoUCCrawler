---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-operations-guide--9b5df30a7b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/operations/guide/ccvp_b_1261-operations-guide-for-cisco-unified-customer-voice-portal/ccvp_b_1251-operations-guide-for-cisco-unified-customer-voice-portal_chapter_01.html
retrieved_at: 2026-08-21T17:44:13.808139+00:00
---

Operations Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

# Operations Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

Updated: May 11, 2021

Chapter: Cisco Serviceability Tools

## Chapter: Cisco Serviceability Tools

# Cisco Serviceability Tools

This chapter presents an overview of Cisco serviceability
                        tools, including the tools available with Unified CVP solutions
                        running on Windows environments. It also presents the serviceability
                        tools that use the Web Services Manager (WSM).

## Web Services Manager

Unified CVP supports a new service layer called the
                           Web Services Manager (WSM). WSM interacts with various subsystems and
                           infrastructure handlers, consolidates the responses, and publishes an XML
                           result. The Web Services Manager supports HTTPS requests and sends a predefined
                           XML response. WSM is installed on each Unified CVP device and runs
                           automatically as a Windows service. For a device to be managed by WSM, the
                           device must be deployed from the Operations Console.

### Create a WSM User

When Unified CVP is installed, a new user called
                                 wsmadmin is created with the same password as the Operations
                                 Console user. You can create and manage additional WSM users using the
                                 Operations Console.

When you have devices deployed in the
                                 Operations Console, log on to any server where WSM is installed and
                                 access the System CLI. See Unified System CLI .

Step 1

Log into the Unified CVP
                                          Operations Console and select User Management > Users .

Step 2

Click Add
                                             New .

Step 3

Provide a Username and Password .

Step 4

Click the User Groups tab.

Step 5

In the Available panel, highlight ServiceabilityAdministrationUserGroup , then click the
                                          right arrow to move that group to the Selected panel.

Step 6

Click Save .

## Unified System CLI

Unified CVP supports a new serviceability CLI
                           called Unified System CLI (System CLI). The System CLI lets you collect
                           diagnostic information (health and status) on Unified CVP servers and collect device-specific information from each supported
                           node connected to the
                           Unified CVP server from which you are using System CLI. The System CLI accesses
                           a new web services layer in Unified CVP called the Web Services Manager. You can run System
                           CLI commands on a local server, or  a
                           remote server. You can obtain information from all the
                           devices in your CVP system by switching to system mode.
                           (Devices must first be configured and deployed in the Operations
                           Console.)

For the system CLI to work, the Web Services Manager service needs to be restarted after  Unified CVP is deployed from OAMP.

The System CLI is installed on all CVP servers. You can leverage
                           the WSM and CLI functionality to collect diagnostic details such as  server map,
                           version information, licenses, configuration, components, sessions, logs,
                           traces, performance factors, and platform information for each Unified CVP
                           Device, on a component and sub-component level. You can also set or reset debug
                           levels using CLI on a component and sub-component level.

The System CLI provides a local mode and a system
                           mode:

The local mode accesses data about the devices
                                 associated with the server that you are logged into. Local mode is the default mode
                                 accessed automatically when you log into the Unified CLI.

The system mode, accessed by typing the system
                                 command at the CLI prompt, provides access to all the devices in your Unified
                                 CVP deployment solution. In system mode, the System CLI automatically detects
                                 the Operations Console and extracts solution topology based on the devices
                                 configured in the Operations Console. Based on options you enter for a given
                                 command, System mode can be limited to a certain device group or list of
                                 servers.

The System CLI commands (for example show all and show
                              component ) enable you to view and zip necessary logs or
                           configurations on a specific server, servers, or groups of servers, and store
                           that data on a local disk.

### Access Unified System CLI and Its Help

The Unified
                                 System CLI is installed on all Unified CVP Servers. Using the CLI client on a
                                 Unified CVP device enables you to connect to the local server or a remote server. You can also connect to servers defined
                                 and deployed in the Operations Console when using system mode.

To launch Unified System CLI on
                                 any CVP server, log into a Unified CVP server through windows.  You can use tools such as VNC or Remote Desktop console.

Complete the following example session to quickly learn how to
                                 use Unified System CLI.

Step 1

Launch Unified System CLI.

Select Start > Programs > Cisco Unified Customer Voice Portal > Unified System CLI .

A CMD window displays with an
                                             Enter Username prompt.

Step 2

Log into the Unified System CLI by entering the default username, wsmadmin , or a
                                          username and password that you created. See Creating a System CLI User .

After logging, in you see the
                                             following message and prompt:

```
Welcome to the Platform Command Line Interface
  admin:
```

Step 3

You can now receive Web Services Manager data from the local
                                          machine using the system CLI commands. The following CLI Usage example shows a user
                                          issuing the show tech-support command.

```
Enter username[wsmadmin]: wsmadmin

 Enter password:

 Welcome to the Platform Command Line Interface

 admin: show tech-support
 Warning: Because running this command can affect system performance,
 Cisco recommends that you run the command during off-peak hours.
 Do you want to continue? [y/n]: y

 Retrieving [version] data from device [localhost] ProductType [cvp] ...
 Retrieving [component] data from device [localhost] ProductType [cvp] ...
 Retrieving [log] data from device [localhost] ProductType [cvp] ...
 Default time range is last 24 hours.
 ...
 Output is saved to "C:\Cisco\CVP\wsm\CLI\download\clioutput0.zip"
```

Step 4

Each System CLI command has a set
                                          of command options . Each option consists of a keyword and set
                                          of values. The following is an example of how to use a command with options.

In this example, the keyword component has a value cvp:CallServer and the keyword subcomponent has a value cvp:ICM . The following command tells the System CLI to get
                                             the configuration data for component CallServer and
                                             subcomponent ICM in the Unified CVP deployment.

```
admin: show config component cvp:CallServer subcomponent cvp:ICM
  Downloading Configuration file: [ICM: icm.properties] ...
  ICM.icmGarbageCollectorInterval : 120
  ICM.locationDelimeter : --
  ICM.icmHeartbeatInterval : 5000
  ...
  ICM.preRoutedCallServiceID : 2
  ICM.icmVxmlIdleTimeout : 30
```

Step 5

Almost all commands have a redirect option. This option tells the System CLI to redirect the command output to a
                                          directory (or a file). If the output is saved in a directory, it is saved in a
                                          zip file in that specific directory. The following example saves the zip file
                                          to c:\temp\clioutput.zip :

```
admin: show version redirect dir c:\temp
```

The output
                                             zip file provides a consistent directory structure when you save to a directory. When unzipped, the
                                             directory structure enables you to find the required diagnostic data quickly.

If you redirect the output to a file, the information is
                                             stored in the form a of "flat" file similar to what you see for the
                                             window output. An example of redirecting to a file is:

```
admin: show version redirect file <filename>
```

Step 6

To obtain information from the Web Services Managers that are part
                                          of your Unified CVP environment, you can change to system mode to issue system-wide commands.

To enable
                                             system mode, type system at the prompt.

### Unified System CLI: System Mode

Enter the CLI system mode by typing system at the command prompt and then run the commands exactly like the local version of the CLI for interactive mode.

In system mode, the Unified System CLI automatically detects the Operations Console, which acts as a seed device, and extracts
                              the solution topology automatically based on devices configured in the Operations Console. System mode enables the System
                              CLI to iteratively go to each supported box in the background and run the command that was run by you in system mode.

Optionally, you can limit the system command to run only on a certain device group or list of servers.

Device group
                              is automatically populated based on:

Device type (Unified CVP,
                                    Unified ICM, IOS Firewall , Unified CM as an example)

Device IP/hostname
                                    wildcard (LOC-1*, 10.86.129.* as an example for branch office
                                    deployments)

Device pool (defined within the Operations
                                    Console)

When the System CLI runs the system command, the System CLI queries each device in the list and caches the responses locally during its first time initialization
                              process, or when system init is processed. The cache enables the system command to be run quickly for subsequent sessions.

If an error is reported due to an unreachable destination or incorrect credentials for a specific device during the processing
                              of a system command , then the device is marked OFFLINE in the System CLI cache. Use system init to retry this device.

The most common command to receive all information from all the
                              components in a Unified CVP solution deployment is:

```
system show tech-support dtcomponent "ucm:Cisco CallManager|cusp:Cisco Unified SIP Proxy"
```

This command collects everything from all device types
                              except the devices ucm and cusp . For
                              ucm, it applies the device type filter Cisco CallManager and for the device cusp it applies the device type filter Cisco Unified SIP Proxy .

### System CLI Automated Processing

To automatically run Unified System CLI commands, create a plain text file with the .bat extension as shown in the example
                              below and replace the <password> as highlighted with the Operations Console password.

```
REM TECH-SUPPORT-COLLECTION
 echo show tech-support > clicmds.txt
 echo exit >> clicmds.txt
 type clicmds.txt | systemcli.bat inplace nointeractive novalidation user:wsmadmin passwd:<password>
```

In a batch file, the system command can also be run by prefixing system on any regular command. For example, system show tech-support , the entire example is:

```
REM SYSTEM-TECH-SUPPORT-COLLECTION
   echo system show tech-support > clicmds.txt
   echo exit >> clicmds.txt
   type clicmds.txt | systemcli.bat inplace nointeractive novalidation user:wsmadmin passwd:<password>
```

The most commonly used command in a Unified CVP solution
                              deployment, to get data from all solution components, is given below:

```
REM SYSTEM-TECH-SUPPORT-COLLECTION
   echo system show tech-support dtcomponent "ucm:Cisco CallManager\|cusp:Cisco Unified SIP Proxy"> clicmds.txt
   echo exit >> clicmds.txt
   type clicmds.txt \| systemcli.bat inplace nointeractive novalidation user:wsmadmin passwd:<password>
```

This command collects everything from all device types
                              except for the device ucm and the device cusp . For the ucm device, it applies the device type filter Cisco CallManager and for the device cusp, it applies the
                              device type filter Cisco Unified SIP Proxy .

### System CLI Remote Processing

To launch System CLI
                              remotely from your laptop, (or any Windows system), to connect to any Unified CVP
                              server or other solution component box (for example, Unified CM, ICM, IOS, CUSP
                              Server, etc.), complete the following procedure:

Install Unified CVP Remote Operations, if no other CVP software is
                                    installed.

For information about only installing the Remote
                                    Operations feature of Unified CVP, see Installation and Upgrade Guide for Cisco Unified Customer Voice Portal .

In the Operations Console, complete the following steps:

Select System > Web Services > Remote
                                                Operations Deployment (tab) .

Enter
                                          the IP address, hostname, and description information for the remote
                                          device.

Click Add to add
                                          the device and click Save & Deploy to make this device
                                          available for remote operations.

Start the System CLI on the remote system.

### Help for the System CLI

The following types of help are available:

For an overview of the CLI system help, type help at the admin
                                    prompt and press enter.

admin: help<enter>

For a
                                    list of main commands, enter "?" at the admin prompt.

admin: ?<enter>

To obtain the
                                    syntax of the command, type a "?" at the end of the
                                    current syntax. For example:

admin: capture start
                                       ?

The preceding entry then informs you that there are two
                                    options in the syntax: duration and <cr>

To obtain
                                    detailed help, enter a portion of the command preceded by the
                                    word help. For example:

admin: help show
                                       version

That command provides information about
                                    additional options both local and system modes.

The following entries show an example of "drilling down" to obtain more
                              detailed help. At the option level, placing help in front
                              of the command, provides detailed information, as in the example. Because this
                              command can be used in "local" mode and in "system" mode, the detailed help
                              also gives information about how to limit the command when using system
                              mode.

```
admin: show version ?
                            Options: redirect
                            <cr>

                            show version redirect ?
                            Options: dir
                            file
```

The help system displays the actual components
                              for your Cisco Unified product as shown in the following example for Unified
                              CVP using system mode of the System CLI.

```
admin(system):show log component ?
                            Options:cvp:CallServer
                            cvp:OAMP
                            cvp:ORM
                            cvp:Reporting
                            cvp:VXMLServer
```

### System CLI Troubleshooting

The System CLI shows two
                              types of errors:

Errors from servers (displayed
                                    unchanged)

Errors from the System CLI for which
                                    you need to check the log files in the System CLI directory

Sometimes it is necessary to change the System CLI debug
                              level to "debug" to collect more data about a System CLI error.

Open CLI\conf\cli_log4j.xml and change the word
                                    "info" to "debug".

Restart the System CLI to reproduce
                                    the error.

See the Doc Wiki troubleshooting page for more CLI
                              troubleshooting information: System CLI troubleshooting tips .

### System CLI Commands and Parameters

The Unified System CLI is designed to work
                              across multiple Cisco Unified products. The meanings of some
                              of the parameters for commands such as show vary from
                              product to product. An example is the components parameter
                              which vary because the components of systems such as Unified CVP
                              and Unified ICM are different.

The CLI online help provides
                              product-specific information for each command's parameters. Type the
                              command and its parameter, followed by the "?" symbol. An example of this
                              mechanism is given in Accessing Help for the System CLI .

The following table provides information about the Unified System CLI commands.

Command or Parameter

Description

capture

Sets up, starts, and stops, a network packet capture.

Capturing network packets with the System CLI can be performed in either
                                          local mode (to run on a single machine), or system mode (to run across several
                                          machines simultaneously). The capture start command has an
                                          optional duration parameter, while the capture stop command
                                          has no parameters. The duration parameter indicates when
                                          the capture should stop. If no duration is provided, the capture process stops
                                          after one day.

The capture command starts the packet capture on a
                                          single Unified CVP device or multiple devices. The capture operation defaults
                                          to the interface card that is receiving packets and is used for the Unified CVP
                                          server socket and IP address binding. The default setting of the capture
                                          command will capture the network packets and save the capture information in
                                          the Unified CVP logs folder which can be retrieved using the regular CLI
                                          trace command.

help

Accesses the online help system overview. Use the "?" character to access
                                          command-specific and parameter-specific help. See Accessing Help for the System CLI .

exit

Exits the
                                          CLI.

show

Accesses, displays and saves
                                          (to a file) data about system configuration and operation. See  the next
                                          table for descriptions of the sub-level show
                                          commands.

system

Enter system mode, which provides access to all the devices in your Unified CVP
                                          deployment solution. Use the exit command to return to
                                          local mode.

The following
                              table describes the variations of the show command.

Show Commands

Descriptions

show all

Shows all available information in all sub-categories listed
                                          in this table. However, you can still enter qualifying parameters to restrict
                                          the information retrieved.

show component

Shows
                                          component-specific information. Available components are based on the Cisco
                                          Unified product type and can be listed by entering the command: 
                                          show
                                          component ?

show config

Displays the
                                          application configuration.

show debug

Shows the current
                                          debug level.

show
                                          devices

Shows a list of the devices
                                          in your deployment (system mode only).

show license

Shows license information.

show log

Shows
                                          log contents. You can narstrow this command to specific
                                          logs.

show
                                          perf

Shows system performance
                                          statistics.

show
                                          platform

Shows platform
                                          information.

show
                                          sessions

Shows the current active
                                          sessions or calls.

show
                                          tech-support

Shows information to
                                          help tech support in solving issues. This command is equivalent to
                                          show all.

show
                                          trace

Shows trace file information.

show
                                          version

Shows Unified CVP component
                                          version
                                          information.

### Details for Specific Options

This section provides detailed information of
                              certain options that require additional explanations.

Results of the match Option
                                 when Information is Sent to a Directory Instead of a File

You can use the match option with the show trace and the show log commands to send selected output to a directory. This option enables you to specify text that the CLI should match when examining
                              data in text files. The output is then limited to log information that matches the specified criteria. However, because the
                              system cannot perform a text match to include or exclude information in binary files such as .zip files, these files are included in your show command processing, since they may contain pertinent information.

If you
                              send the output of the match selection process to a file
                              instead of a directory, the output only includes the actual text the CLI
                              command would return to the screen.

Comparison of
                                 the component Option with the dtcomponent Option

The component limits the output of a command
                              to the results from specific system components.

Using
                              the command show trace component ucm:CallManager and the
                              system components shown in the following list, you receive the following information:

Unified CVP Call Server:
                                    No Information Returned

Unified Call
                                    Manager: Information Returned

Unified CM
                                    Tomcat Server: No Information Returned

The command show trace component ucm:CallManager only returns information from the Call Manager.

The option dtcomponent (device type component option) only restricts
                              the information from the given device type, while allowing data to be returned
                              from other device types.

Using the above system and the command show trace dtcomponent ucm:CallManager would restrict its ucm component output to just the Call Manager, but returns information for other device types. In this example, it returns the
                              following 
                              information for the Unified CVP Call Server and the Call Manager, but not the
                              Unified CM Tomcat Server:

Unified CVP Call Server: Information Returned

Unified Call
                                    Manager: Information Returned

Unified
                                    CM Tomcat Server: No Information Returned

## Configure Analysis Manager with Unified CVP

Step 1

From the Unified Analysis Manager menu, choose Inventory > Node .

The Node window appears.

Step 2

Click Add to add a node or select a node from the list. Click Edit to edit an existing configuration.

The Add or Edit Node window appears.

Fields on this window that are marked with an asterisk (*) are required fields.

Step 3

From the Product Type drop-down list box,  select CVP .

Step 4

In the IP/Host Name field, enter the host name or the IP address of the Unified CVP OAMP box.

Step 5

In the Transport Protocol field, select the protocol you want to use. Use the default value populated (HTTPS).

Step 6

In the Port Number field, enter the port number of the node you are using.

Use the default value populated (8111).

Step 7

Enter the user name as wsmadmin and enter the OAMP password. Re-enter the password in the Confirm Password field.

Step 8

In the Description field, you can optionally provide a brief description of the node you are adding.

Step 9

In the Associated Call Record Server and Associated Trace File Server fields, use the drop-down list to select the respective
                                       servers you want to use for the node.

Step 10

To add a node to an existing group, check the Associated Group check box.

Step 11

If you have a NAT or Terminal Server configuration, use the Advanced button to display the Add Node-Advanced screen. Enter
                                       the appropriate information in the Alternate IP/Hostname and Alternate Port fields.

Step 12

Click Save to save the node to the list. Click Cancel to end the operation without adding the node.

## System CLI Commands Map to IOS CLI Commands

The
                           following table maps the System CLI commands to their corresponding IOS CLI
                           commands:

System CLI
                                          Commands

IOS CLI
                                          Commands

show
                                       config

show
                                       running-config

show
                                       version

show version

show
                                       clock

show
                                       license

show
                                       license

show
                                       perf

show call resource voice
                                       stat

show memory statistics

show processes cpu
                                       history

show processes memory sorted

show voice dsp
                                       group all

show voice dsp voice

show debug

show debug

show
                                       log

N/A

show sessions

show call active voice compact

show voice call status | inc
                                       calls

show voip rtp connections | inc connect

sh sip-ua
                                       calls | inc calls

show
                                       tech-support

show tech-support

<Everything else given above>

show trace

show logging

show
                                       platform

show diag

sh
                                       inventory

sh int | inc media type|Ethernet|address

sh
                                       controllers T1 | inc T1

sh controllers E1 | inc E1

debug

0 no debug all

1 -

deb
                                       ccsip err

deb cch323 err

deb voip app vxml err

deb http client err

deb mrcp err

deb
                                       rtsp err

deb h225 asn1 err

deb h245 asn1 err

2 -

debug isdn q931

debug h225 events

debug h245 events

debug voip ccapi inout

debug
                                       vtsp events

3 -

debug ccsip messages

debug h225 q931

debug h225 asn1

debug h245 asn1

| Note | System CLI
                                    uses WSM to collect and present the data available to WSM from the various
                                    Unified CVP components. |
|---|---|

| Step 1 | Log into the Unified CVP
                                          Operations Console and select User Management > Users . |
|---|---|
| Step 2 | Click Add
                                             New . |
| Step 3 | Provide a Username and Password . |
| Step 4 | Click the User Groups tab. |
| Step 5 | In the Available panel, highlight ServiceabilityAdministrationUserGroup , then click the
                                          right arrow to move that group to the Selected panel. |
| Step 6 | Click Save . |

| Note | For the system CLI to work, the Web Services Manager service needs to be restarted after  Unified CVP is deployed from OAMP. |
|---|---|

| Note | To quickly access and use the System CLI, see Quick Start Exercise: Accessing and Using the Unified System CLI and its Help |
|---|---|

| Note | In
                                    addition to the System CLI, which is automatically installed with the Unified
                                    CVP installation, you can also obtain a GUI-based client, . This client is called the Analysis Manager, and it is part of
                                    Unified CM. For more information on
                                    the Analysis Manager, refer to Cisco Unified Communications Analysis Manager User Guide . For instructions specific to configuring Analysis Manager with Unified CVP, see Configure Analysis Manager with Unified CVP |
|---|---|

| Note | Before you can use the system CLI to obtain
                                    information about a device, that device must be listed in and deployed by the
                                    Operations Console. |
|---|---|

| Note | To be able to log in to the
                                          System CLI on Unified CVP, the WSM service must be up and running. By default
                                          WSM service is always running. |
|---|---|

| Note | The System CLI only provides
                                          information on devices that have been configured, saved, and deployed in the
                                          Operations Console. If you change the configuration of a device, you must
                                          save and deploy the revised configuration before it is available to the System
                                          CLI. |
|---|---|

| Step 1 | Launch Unified System CLI. Select Start > Programs > Cisco Unified Customer Voice Portal > Unified System CLI . A CMD window displays with an
                                             Enter Username prompt. |
|---|---|
| Step 2 | Log into the Unified System CLI by entering the default username, wsmadmin , or a
                                          username and password that you created. See Creating a System CLI User . After logging, in you see the
                                             following message and prompt: Welcome to the Platform Command Line Interface
  admin: |
| Step 3 | You can now receive Web Services Manager data from the local
                                          machine using the system CLI commands. The following CLI Usage example shows a user
                                          issuing the show tech-support command. Enter username[wsmadmin]: wsmadmin

 Enter password:

 Welcome to the Platform Command Line Interface

 admin: show tech-support
 Warning: Because running this command can affect system performance,
 Cisco recommends that you run the command during off-peak hours.
 Do you want to continue? [y/n]: y

 Retrieving [version] data from device [localhost] ProductType [cvp] ...
 Retrieving [component] data from device [localhost] ProductType [cvp] ...
 Retrieving [log] data from device [localhost] ProductType [cvp] ...
 Default time range is last 24 hours.
 ...
 Output is saved to "C:\Cisco\CVP\wsm\CLI\download\clioutput0.zip" Note The show tech-support command creates a
                                                      single zip file in the directory %CVP_HOME%\wsm\CLI\download . Note By default, this
                                                      command collects the traces for the last 24 hours. Use the reltime parameter to change the time  period. For example, if you
                                                      want to pull traces for the last three  days, use the following command: show tech-support reltime 3 days . | Note | The show tech-support command creates a
                                                      single zip file in the directory %CVP_HOME%\wsm\CLI\download . | Note | By default, this
                                                      command collects the traces for the last 24 hours. Use the reltime parameter to change the time  period. For example, if you
                                                      want to pull traces for the last three  days, use the following command: show tech-support reltime 3 days . |
| Note | The show tech-support command creates a
                                                      single zip file in the directory %CVP_HOME%\wsm\CLI\download . |
| Note | By default, this
                                                      command collects the traces for the last 24 hours. Use the reltime parameter to change the time  period. For example, if you
                                                      want to pull traces for the last three  days, use the following command: show tech-support reltime 3 days . |
| Step 4 | Each System CLI command has a set
                                          of command options . Each option consists of a keyword and set
                                          of values. The following is an example of how to use a command with options. In this example, the keyword component has a value cvp:CallServer and the keyword subcomponent has a value cvp:ICM . The following command tells the System CLI to get
                                             the configuration data for component CallServer and
                                             subcomponent ICM in the Unified CVP deployment. admin: show config component cvp:CallServer subcomponent cvp:ICM
  Downloading Configuration file: [ICM: icm.properties] ...
  ICM.icmGarbageCollectorInterval : 120
  ICM.locationDelimeter : --
  ICM.icmHeartbeatInterval : 5000
  ...
  ICM.preRoutedCallServiceID : 2
  ICM.icmVxmlIdleTimeout : 30 |
| Step 5 | Almost all commands have a redirect option. This option tells the System CLI to redirect the command output to a
                                          directory (or a file). If the output is saved in a directory, it is saved in a
                                          zip file in that specific directory. The following example saves the zip file
                                          to c:\temp\clioutput.zip : admin: show version redirect dir c:\temp The output
                                             zip file provides a consistent directory structure when you save to a directory. When unzipped, the
                                             directory structure enables you to find the required diagnostic data quickly. If you redirect the output to a file, the information is
                                             stored in the form a of "flat" file similar to what you see for the
                                             window output. An example of redirecting to a file is: admin: show version redirect file <filename> |
| Step 6 | To obtain information from the Web Services Managers that are part
                                          of your Unified CVP environment, you can change to system mode to issue system-wide commands. To enable
                                             system mode, type system at the prompt. Note See Accessing Help for the System CLI . | Note | See Accessing Help for the System CLI . |
| Note | See Accessing Help for the System CLI . |

| Note | The show tech-support command creates a
                                                      single zip file in the directory %CVP_HOME%\wsm\CLI\download . |
|---|---|

| Note | By default, this
                                                      command collects the traces for the last 24 hours. Use the reltime parameter to change the time  period. For example, if you
                                                      want to pull traces for the last three  days, use the following command: show tech-support reltime 3 days . |
|---|---|

| Note | See Accessing Help for the System CLI . |
|---|---|

| Note | For system mode system CLI to work properly, the system CLI in OAMP and all deployed CVP servers must be in working condition. |
|---|---|

| Note | System CLI initialization for the first system mode command processing, or for the system init command, may take a few minutes to complete, especially when there are a lot of devices in a Unified CVP solution, or if
                                       devices are unreachable, or network timeouts are involved. |
|---|---|

| Note | You
                                       can run a Windows scheduled job and collect traces periodically from one or
                                       multiple servers using a schedule. See How to Schedule Tasks in Windows XP for information about scheduling a Windows job. |
|---|---|

| Note | You can
                                       also run a Windows scheduled job and collect traces periodically from one or
                                       multiple servers, using a schedule from a remote
                                       system. |
|---|---|

| Command or Parameter | Description |
|---|---|
| capture | Sets up, starts, and stops, a network packet capture. Capturing network packets with the System CLI can be performed in either
                                          local mode (to run on a single machine), or system mode (to run across several
                                          machines simultaneously). The capture start command has an
                                          optional duration parameter, while the capture stop command
                                          has no parameters. The duration parameter indicates when
                                          the capture should stop. If no duration is provided, the capture process stops
                                          after one day. The capture command starts the packet capture on a
                                          single Unified CVP device or multiple devices. The capture operation defaults
                                          to the interface card that is receiving packets and is used for the Unified CVP
                                          server socket and IP address binding. The default setting of the capture
                                          command will capture the network packets and save the capture information in
                                          the Unified CVP logs folder which can be retrieved using the regular CLI
                                          trace command. |
| help | Accesses the online help system overview. Use the "?" character to access
                                          command-specific and parameter-specific help. See Accessing Help for the System CLI . |
| exit | Exits the
                                          CLI. |
| show | Accesses, displays and saves
                                          (to a file) data about system configuration and operation. See  the next
                                          table for descriptions of the sub-level show
                                          commands. |
| system | Enter system mode, which provides access to all the devices in your Unified CVP
                                          deployment solution. Use the exit command to return to
                                          local mode. |

| Show Commands | Descriptions |
|---|---|
| show all | Shows all available information in all sub-categories listed
                                          in this table. However, you can still enter qualifying parameters to restrict
                                          the information retrieved. |
| show component | Shows
                                          component-specific information. Available components are based on the Cisco
                                          Unified product type and can be listed by entering the command: 
                                          show
                                          component ? |
| show config | Displays the
                                          application configuration. |
| show debug | Shows the current
                                          debug level. |
| show
                                          devices | Shows a list of the devices
                                          in your deployment (system mode only). |
| show license | Shows license information. |
| show log | Shows
                                          log contents. You can narstrow this command to specific
                                          logs. |
| show
                                          perf | Shows system performance
                                          statistics. |
| show
                                          platform | Shows platform
                                          information. |
| show
                                          sessions | Shows the current active
                                          sessions or calls. |
| show
                                          tech-support | Shows information to
                                          help tech support in solving issues. This command is equivalent to
                                          show all. Note When you issue the show tech-support command, the System CLI issues the other show commands needed to provide all of the
                                                   system information. During the process of running the other show commands, the System CLI passes component and sub-component
                                                   parameters to the show trace command, but does not include component and sub-component parameters when it runs command such
                                                   as show configuration and show log. | Note | When you issue the show tech-support command, the System CLI issues the other show commands needed to provide all of the
                                                   system information. During the process of running the other show commands, the System CLI passes component and sub-component
                                                   parameters to the show trace command, but does not include component and sub-component parameters when it runs command such
                                                   as show configuration and show log. |
| Note | When you issue the show tech-support command, the System CLI issues the other show commands needed to provide all of the
                                                   system information. During the process of running the other show commands, the System CLI passes component and sub-component
                                                   parameters to the show trace command, but does not include component and sub-component parameters when it runs command such
                                                   as show configuration and show log. |
| show
                                          trace | Shows trace file information. |
| show
                                          version | Shows Unified CVP component
                                          version
                                          information. |

| Note | When you issue the show tech-support command, the System CLI issues the other show commands needed to provide all of the
                                                   system information. During the process of running the other show commands, the System CLI passes component and sub-component
                                                   parameters to the show trace command, but does not include component and sub-component parameters when it runs command such
                                                   as show configuration and show log. |
|---|---|

| Step 1 | From the Unified Analysis Manager menu, choose Inventory > Node . The Node window appears. |
|---|---|
| Step 2 | Click Add to add a node or select a node from the list. Click Edit to edit an existing configuration. The Add or Edit Node window appears. Note Fields on this window that are marked with an asterisk (*) are required fields. | Note | Fields on this window that are marked with an asterisk (*) are required fields. |
| Note | Fields on this window that are marked with an asterisk (*) are required fields. |
| Step 3 | From the Product Type drop-down list box,  select CVP . |
| Step 4 | In the IP/Host Name field, enter the host name or the IP address of the Unified CVP OAMP box. |
| Step 5 | In the Transport Protocol field, select the protocol you want to use. Use the default value populated (HTTPS). |
| Step 6 | In the Port Number field, enter the port number of the node you are using. Note Use the default value populated (8111). | Note | Use the default value populated (8111). |
| Note | Use the default value populated (8111). |
| Step 7 | Enter the user name as wsmadmin and enter the OAMP password. Re-enter the password in the Confirm Password field. |
| Step 8 | In the Description field, you can optionally provide a brief description of the node you are adding. |
| Step 9 | In the Associated Call Record Server and Associated Trace File Server fields, use the drop-down list to select the respective
                                       servers you want to use for the node. |
| Step 10 | To add a node to an existing group, check the Associated Group check box. |
| Step 11 | If you have a NAT or Terminal Server configuration, use the Advanced button to display the Add Node-Advanced screen. Enter
                                       the appropriate information in the Alternate IP/Hostname and Alternate Port fields. |
| Step 12 | Click Save to save the node to the list. Click Cancel to end the operation without adding the node. |

| Note | Fields on this window that are marked with an asterisk (*) are required fields. |
|---|---|

| Note | Use the default value populated (8111). |
|---|---|

| System CLI
                                          Commands | IOS CLI
                                          Commands |
|---|---|
| show
                                       config | show
                                       running-config |
| show
                                       version | show version show
                                       clock |
| show
                                       license | show
                                       license |
| show
                                       perf | show call resource voice
                                       stat show memory statistics show processes cpu
                                       history show processes memory sorted show voice dsp
                                       group all show voice dsp voice |
| show debug | show debug |
| show
                                       log | N/A |
| show sessions | show call active voice compact show voice call status \| inc
                                       calls show voip rtp connections \| inc connect sh sip-ua
                                       calls \| inc calls |
| show
                                       tech-support | show tech-support <Everything else given above> |
| show trace | show logging |
| show
                                       platform | show diag sh
                                       inventory sh int \| inc media type\|Ethernet\|address sh
                                       controllers T1 \| inc T1 sh controllers E1 \| inc E1 |
| debug | 0 no debug all 1 - deb
                                       ccsip err deb cch323 err deb voip app vxml err deb http client err deb mrcp err deb
                                       rtsp err deb h225 asn1 err deb h245 asn1 err 2 - debug isdn q931 debug h225 events debug h245 events debug voip ccapi inout debug
                                       vtsp events 3 - debug ccsip messages debug h225 q931 debug h225 asn1 debug h245 asn1 |