---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-tapi-dev-12-5-1-cucm-b-tapi-dev-guide-1251-cucm-b-tapi-dev-guide-1251-c-483e71076d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/tapi_dev/12_5_1/cucm_b_tapi-dev-guide-1251/cucm_b_tapi-dev-guide-1251_chapter_011.html
retrieved_at: 2026-08-16T18:14:02.461973+00:00
---

Cisco Unified TAPI Developers Guide for Cisco Unified Communications Manager Release 12.5(1)

# Cisco Unified TAPI Developers Guide for Cisco Unified Communications Manager Release 12.5(1)

Updated: May 29, 2025

Chapter: Cisco Unified TAPI Installation

## Chapter: Cisco Unified TAPI Installation

# Cisco Unified TAPI Installation

This chapter describes how to install and configure the Cisco Unified Telephony Application Programming Interface (TAPI) client
                        software for Unified Communications Manager .

The upgraded TAPI client software does not work with previous releases of Unified Communications Manager .

## Required Software

Cisco TSP requires the following software:

Unified Communications Manager

Supported Windows Platforms

## Supported Windows Platforms

All Windows operating systems support CiscoTAPI. Depending on the type and version of your operating system, you may need
                           to install a service pack.

For a detailed breakdown of supported Windows platforms for Cisco Unified TAPI, see https://developer.cisco.com/site/tapi/documents/supported-windows-os/ .

Caution

You can install Cisco TSP on a system only where Windows is installed on
                                       C:\. If Windows is installed on a drive other than
                                       C:\, an attempt to install Cisco TSP will fail.

Windows(64-bit) Operating Systems require native 64-bit Cisco TSP client. For more information on availability, see https://community.cisco.com/t5/collaboration-blogs/bg-p/j-blogs-dev-collab .

Cisco TSP legacy wave driver is not supported under VMWare.

## Installing the Cisco Unified CM TSP Client

Download the Cisco TSP client software from the Cisco Unified CM Administration Plug-Ins page. For information on installing
                           plug-ins, refer to the Unified Communications Manager Administration Guide. The Cisco TSP client installation wizard varies
                           depending on whether previous versions have been installed.

If you are installing multiple TSPs, multiple copies of CiscoTSPXXX.tsp and CiscoTUISPXXX.dll files will exist in the same
                                       Windows system directory.

To begin installation of the Cisco TSP client from the Cisco Unified CM Administration, perform the following steps:

Download the Cisco Telephony Service Provider plugin from Cisco Unified Communication Manager Administration > Application > plugins .

Save it on the desired Desktop.

Double-click Cisco TSP.exe.

Follow the online instructions.

### Cisco TSP Client Interaction with Windows Services

The Cisco TSP client is tightly coupled with the Microsoft Telephony and QWAVE Services. These services should not be stopped
                                 as it will lead to unexpected and undesirable behaviour of CiscoTSP . By default the Microsoft Telephony Service is dependent
                                 on the Microsoft Remote Connection Manager Service which cannot be restarted manually. To ensure proper installation of the
                                 Cisco TSP client, reboot the computer following Cisco TSP installation. Cisco also recommends rebooting the computer anytime
                                 the Cisco TSP configuration settings are changed to ensure the Microsoft Telephony Service is updated properly. If the Microsoft
                                 Remote Connection Service is disabled, computer reboot is not required; simply restart the Microsoft Telephony Service using
                                 the Windows Services Applet for the new settings to take effect.

### Installation Setup Screen

Click on Cisco TSP.exe to begin the installation process. Specify the destination folder where the Cisco TSP files must reside
                              from the Choose Destination Location screen (shown below) and configure the number of TSP instances desired.

### Configure TSP Instance for Unified CM Releases Until 15SU1

For each desired TSP Instance, configure the User ID, Password, and CTIManager settings in the Configure TSP Instance screen
                              shown below. If the required information is not known during the installation, it can be configured later using the Open Cisco TAPI Configuration icon found in the Programs Menu (available after the installation).

### Configure Secure TSP Instance

To configure a secure CTI connection, click the Configure Security button on the desired Configure TSP Instance. Populate the specified information from the Configure Secure TSP Instance screen
                              as shown below. Refer to the Unified Communications Manager Security Guide for the desired release for additional information
                              regarding Securing CTI.

### Cisco Media Driver Selection

Cisco introduced a new media driver in Unified Communications Manager 8.0(1). The TSP client may be configured to install
                                 the Cisco Media Driver or the Cisco Wave Driver. Cisco Media and Wave Drivers are used with TSP applications that play or
                                 record media. Refer to the Installation Guide provided by your vendor to determine which driver may be required.

Cisco Media Driver settings apply to all configured TSP instances.
                                             			 Cisco Wave Driver settings are instance specific.

Cisco Media Driver

To install the Cisco Media Driver, select Cisco Media Driver
                                 		  from the installation screen. Set the desired start and end ports used by Cisco
                                 		  Media Driver. The port settings are used by all TSP instances. Each media
                                 		  channel requires 4 ports (1 Channel = 4 ports). Refer to the Installation Guide
                                 		  provided by your application vendor to determine the appropriate port settings.
                                 		  The Media Driver is ready for use after the installation completes and the
                                 		  computer is rebooted.

Cisco Wave Driver

Select Cisco Wave Driver from the installation screen.
                                 		  Complete the TSP installation and reboot the PC. After the PC has rebooted,
                                 		  complete the installation of the Cisco Wave Driver by performing the following
                                 		  steps.

#### Cisco Wave Driver for Windows XP, Vista, 2003, 2008

Procedure for Windows XP / Windows Vista / Windows 2003 /
                                    		  Windows 2008

Step 1

Open the Control Panel.

Step 2

Open Add Hardware . The Add Hardware Wizard window appears.

Step 3

Click Next .

Step 4

Select Yes, I have already connected the hardware .

Step 5

Select Add a New Hardware Device .

Step 6

Click Next .

Step 7

Select Install the Hardware that I manually select from a list .

Step 8

Click Next .

Step 9

For the hardware type, choose Sound, video and game controller .

Step 10

Click Next .

Step 11

Click Have Disk .

Step 12

Click Browse and navigate to the Wave Drivers folder in the folder
                                             			 where the Cisco Unified Communication Manager TSP is installed.

Step 13

Choose OEMSETUP.INF and click Open .

Step 14

In the Install From Disk window, click OK .

Step 15

In the Select a Device Driver window, select the Cisco Unified Communication Manager TAPI Wave Driver and click Next .

Step 16

In the Start Hardware Installation window, click Next .

Step 17

If Prompted for Digital signature Not Found, click Continue Anyway .

Step 18

The installation may issue the following prompt:

The avaudio32.dll file on Windows NT Setup Disk #1 is needed,

Type the path where the file is located and then click OK .

If so, navigate to the same location where you chose
                                                				OEMSETUP.INF, select avaudio32.dll, and click OK .

Step 19

Click Yes .

Step 20

Click Finish .

Step 21

Click Yes to restart the computer.

#### Cisco Wave Driver for Windows 7

Procedure for Windows 7

Step 1

Right click My computer and select Manage . The Computer Management window appears.

Step 2

From System Tools , select Device Manager .

Step 3

Right click on the <Computer-Name> and select Install Legacy Wave Driver . This action pops up an Add
                                             			 Hardware window.

Step 4

Select Install the Hardware that I manually select from a list .

Step 5

Click Next .

Step 6

For the hardware type, choose Sound, video and game controller .

Step 7

Click Next .

Step 8

Click Have Disk .

Step 9

Click Browse and navigate to the Wave Drivers folder in the folder
                                             			 where the Cisco Unified Communication Manager TSP is installed.

Step 10

Choose OEMSETUP.INF and click Open .

Step 11

In the Install From Disk window, click OK .

Step 12

In the Select a Device Driver window, select the Cisco Unified Communication Manager TAPI Wave Driver and click Next .

Step 13

In the Start Hardware Installation window, click Next .

Step 14

If Prompted for Digital signature Not Found, click Continue Anyway .

Step 15

The installation may issue the following prompt:

The avaudio32.dll file on Windows NT Setup Disk #1 is needed,

Type the path where the file is located and then click OK .

If so, navigate to the same location where you chose
                                                				OEMSETUP.INF, select avaudio32.dll, and click OK .

Step 16

Click Yes .

Step 17

Click Finish .

Step 18

Click Yes to restart the computer.

### Verifying the Cisco Wave Driver

Use these steps to verify the Cisco Wave Driver when performing install and uninstall operations.

Step 1

Click Start > Run .

Step 2

In the text box, enter regedit.

Step 3

Click OK .

Step 4

Choose the Drivers32 key that is located in the following path:

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion
```

Step 5

If you are installing the Wave driver, make sure that the driver avaudio32.dll displays in the data column. If you are uninstalling
                                          the Wave driver, make sure that the driver avaudio32.dll does not display in the data column. This designates the Cisco Wave
                                          Driver.

Step 6

Verify that the previously existing Wave values appear in the data column for Wave1, Wave2, Wave3, and so on. You can compare
                                          this registry list to the contents of the .reg file that you saved in the procedure by opening the .reg file in a text editor
                                          and viewing it and the registry window side by side.

Step 7

If necessary, add the appropriate WaveX string values for any missing Wave values that should be installed on the system.
                                          For each missing Wave value, choose Edit > New > String Value and enter a value name. Then, choose Edit > Modify , enter the value data, and click OK .

Step 8

Close the registry by choosing Registry > Exit .

Configure the Cisco Wave Driver settings using the Wave tab in the Cisco TAPI Configuration tool (available after installation).

### AutoUpgrade

The TSP client can be configured to detect and install new client versions automatically when Cisco Unified CM is upgraded.
                              When set to Always or Ask, the auto-upgrade service requires the login User to have local Administrative rights to install
                              applications. If the logged-in User is not permitted to install applications, set Auto-upgrade to Never.

### Update Credentials

Cisco TSP 8.0 introduces a new feature that enables the Administrator to allow Users to update their credentials (UserID and
                              Password) without requiring the User to have local Administrative rights. When this option is checked, all Standard Users
                              can update their UserID and Password using the Cisco TAPI Configuration tool. Configuring all other Cisco TSP options requires
                              local Administrative rights. If the Administrator does not want to allow Standard Users to update their credentials, leave
                              this unchecked.

### Cisco TSP Notifier

Cisco TSP 8.0 introduces a new feature that helps identify connectivity issues between Cisco Unified CM CTI Manager and the
                              PC where the TSP client has been installed. TSP Notifier is installed automatically and can be configured to run during Windows
                              start-up. The user must disable UAC to have the notifier run during startup. TSP Notifier runs as a background application
                              in the system tray.

The Cisco TAPI Notifier can detect the following errors:

Unified CM TSP Authentication failed -Check UserID and Password

Unified CM TSP Initialization failed -User not configured in Cisco Unified CM for CTI usage

Unified CM TSP Initialization error -Check and update Cisco Unified CM TSP version

Unified CM TSP Version is incompatible with Cisco Unified CM version

Unified CM TSP Initialization failed -User not configured in Cisco Unified CM for secure CTI usage

Unified CM TSP Initialization failed -Cisco Unified CM security configuration does not match with Unified CM TSP

Unified CM TSP Initialization failed -Invalid security certificate

Unified CM TSP Initialization failed -Security certificate compromised

### Multi-Language Settings

Populate the TFTP server where locale files have been installed. The locale files are downloaded after the installation is
                              completed and the PC rebooted. Use the Cisco TAPI Configuration tool to set the desired locale.

### Installation Completed

The following screen displays when the installation is
                              		complete. You must reboot your computer after the installation. You can refer
                              		to the Release Notes for further details.

### Reinstall or Add a New Instance

If a previous version of the Cisco TSP client is detected and the version of the existing client matches the installer, the
                              Setup Type screen, shown below, displays with the following options:

Reinstall—Select this option to reinstall the TSP client. This option will be available only if the same version of the TSP
                                    client is detected.

Uninstall—Select this option to remove the Cisco TSP from the PC.

Add TSP Instance—Select this option to add additional TSP instances. The drop-down menu controls the number of instances to
                                    add. The number of instances is limited to 10, so the number of instances that can be added is limited to the maximum number
                                    minus the number of instances already installed. If additional instances are added, the installer prompts the Configure TSP
                                    Instance for all new instances.

### Upgrading CiscoTSP

If a previous version of the Cisco TSP client is detected and the version of the installer is newer than the one already installed,
                              the Setup Type screen, shown below, displays with the following options:

Upgrade—Select this option to upgrade all existing TSP instances and client.

Uninstall Cisco TSP—Select this option to remove the Cisco TSP from the PC.

Upgrade and Add a New TSP Instance—Select this option to add additional TSP instances and upgrade all instances to the newer
                                    version. The drop-down menu controls the number of instances to add. The number of instances is limited to 10, so the number
                                    of instances that can be added is limited to the maximum number minus the number of instances already installed. If additional
                                    instances are added, the installer will prompt Configure TSP Instance for all new instances.

### Downgrade or Uninstall of Cisco TSP

If a previous version of the Cisco TSP client is detected and the version of the installer is older than the one already installed,
                              the Setup Type screen, shown below, displays with this option:

Uninstall —Select this option to remove the Cisco TSP from your computer.

## Silent Installation of Cisco Unified CM TSP

Cisco TSP 8.0 introduces a new Silent Installation feature that allows the Cisco TSP to be remotely installed using Microsoft
                              Group Policy or other remote installation tools. See the list of silent installation parameters to determine the correct settings
                              based on the needed configuration.

### Example 1

New Cisco TSP installation which does not require Cisco
                              		  Media Driver or Cisco Wave Driver:

USER ID = bob

PASSWORD = cisco123

CTIManager1 = 1.1.1.1

CTI1_TYPE = IPV4

```
Cisco TSP.exe /s /v"/qn PASS = \"cisco123\" USER = \"bob\" CTI1 = \"1.1.1.1\" 
CTI1_TYPE = \"ipv4\""
```

### Example 2

New Cisco TSP installation which requires the Cisco Media
                              		  Driver:

USER ID = bob

PASSWORD = cisco123

CTIManager1 = 1.1.1.1

CTI1_TYPE = IPV4

DRIVER_TYPE = NEW

MDP_START = 30000

MDP_END = 31000

```
Cisco TSP.exe /s /v"/qn PASS = \"cisco123\" USER = \"bob\" CTI1 = \"1.1.1.1\" 
CTI1_TYPE = \"ipv4\" DRIVER_TYPE = \"NEW\" MDP_START = \"30000\" MDP_END = \"31000\""
```

### Syntax Format

No spaces between the parameter and the " = " sign.

"\" is used as an escape character, so \" is needed to indicate a double quote.

If no parameters are used:

For Silent Install -CiscoTSP.exe /s /v/"qn"

Silent Upgrade -CiscoTSP.exe /s /v"/qn [REINSTALL = \"ALL\"
                                          					 REBOOT = \"ReallySuppress\"]"

Silent Reinstall -CiscoTSP.exe /s /v"/qn REINSTALL = \"ALL\"
                                          					 REBOOT = \"ReallySuppress\""

See the following table for the list of parameters that you can pass (default).

Name

Comment

Valid values

USER

User name used to during provider initializing

All

PASS

Password used to during provider initializing

All

CTI1

CTI Manager 1 IP address

All

CTI2

CTI Manager 2 IP address

All

NONAD

Non-admin can modify the userid/password

"NO", "YES"

CTI1_TYPE

Ipv4, Ipv6, or hostname

"NONE", "IPV4", "IPV6", "HOST"

CTI2_TYPE

None, Ipv4, Ipv6, or hostname

"NONE", "IPV4", "IPV6", "HOST"

AUTOUPGRADE_TYPE

Ask, Always, Never

"ASK", "NEVER", "ALWAYS"

DRIVER_TYPE

Cisco Wave Driver, Cisco Media Driver

"WAVE", "MEDIA"

NUM_WDP

Number of Legacy Wave Driver Ports

0 -255

MDP_START

Media Driver Port Start Range

0 -65535

MDP_END

Media Driver Port End Range

0 -65535

### Upgrading Unified CM TSP Client to Release 8.5(1) or Later Using Silent Installation

After the silent fresh installation or silent upgrade from previous versions of TSP to the 8.5(1) client, you must reboot
                              the system for the changes to take effect.

In a case where more than one TSP instance is installed, you must use the client UI-based installation package when upgrading
                                          the TSP to maintain the existing configuration settings.

## Using Cisco TSP

The following section describes program group and program elements.

### Program Group and Program Elements

There is a new program group called Cisco TAPI created during installation and contains the following program elements:

Cisco TAPI Configuration—Displays the configuration tool for all TSP instances. If the logged-in User has local Administrative
                                    rights, then all settings can be changed. If the administrator selects Allow Standard User to Update Credentials , then the Cisco TAPI Configuration tool only allows the UserID/Password to be updated.

Cisco TAPI Media Driver Configuration—Displays the configuration settings for the Cisco Media Driver. The settings apply to
                                    all configured TSP instances.

Launch Cisco TAPI Notifier—Starts the Cisco TSP Notifier tool to help detect communication issues between Cisco Unified CM
                                    and the PC.

Open Cisco TAPI Media Driver Readme—Displays the Cisco Media Driver Readme file.

Open Cisco TAPI Readme—Displays the Cisco TSP Readme file.

Open Cisco TAPI Release Notes—Displays the Cisco TSP Release Notes for the installed version.

Uninstall Cisco TAPI—Removes Cisco TSP and Cisco Media Driver from the PC. The Cisco Wave Driver (if installed) must be removed
                                    using the Telephony Services applet found in the Control Panel.

After installation is completed, the program group appears as shown below.

Invoking the uninstall of Cisco TAPI the removes both the TSP and the next generation Media Driver (the old existing Wave
                              Driver is NOT removed). It removes the Program Group from the Windows Task Bar along with all the program elements.

### Modifying Cisco TSP Configuration

Select Cisco TAPI Configuration from the Cisco TSP Program Group as shown below in the CiscoConfig dialog.

## Cisco Unified CM TSP Configuration Settings

### General

The General Tab displays the Cisco TSP version and auto-update settings, as illustrated below.

The following table lists the General tab fields that must be set and their descriptions.

Field

Description

Ask Before Update

Auto-upgrade service prompts the User to upgrade the TSP client.

Never AutoUpdate

Select this to disable the auto-update service.

Always AutoUpdate

Select this to enable automatic updates when new TSP client versions are detected.

AutoUpdate on Incompatible QBEProtocolVersion

Select this to allow the Cisco TSP to auto update only when the local TSP version is incompatible with the Unified CM version.

### User

The User tab allows you to set the user name and password, as illustrated in below.

The table below describes the fields for the User tab that must be set.

Field

Description

User Name

Enter the user name of the user. The TSP instance will access devices and lines that are associated with this User in Cisco
                                             Unified CM. Make sure that this User is enabled for CTI using the Cisco Unified CM Administration UI

You can designate only one user name and password to be active at any time for any one TSP instance.

Password

Enter the password that is associated with the user. The computer encrypts the password and stores it in the registry.

Verify Password

Reenter the user password.

### CTI Manager Tab for Unified CM Releases Until 15SU1

The CTI Manager tab enables you to configure the primary and backup CTI Manager information, as illustrated in the following screenshot.

The following table describes the CTI Manager tab fields that you must set.

Field

Description

Primary CTI Manager Location

Use this field to specify the CTI Manager to which the TSP attempts to connect to first. Select one of the following options:

Click the IP Address radio button and use the text box to provide the IPv4 address of the Primary CTI Manager.

Click the IPV6 Address radio button and use the text box to provide the IPv6 address, if the application must connect using IPv6 with the Primary
                                                   CTI Manager.

Click the Host Name radio button and enter the host name of the Primary CTI Manager.

Backup CTI Manager Location

Use this field to specify the CTI Manager to which the TSP attempts to connect when the Primary CTI Manager is not reachable.
                                             Select one of the following options:

Click the IP Address radio button and use the text box to provide the IPv4 address of the Backup CTI Manager.

Click the IPV6 Address radio button and use the text box to provide the IPv6 address, if the application must connect using IPv6 with the Backup
                                                   CTI Manager.

Click the Host Name radio button and enter the host name of the Backup CTI Manager.

IP Addressing Preference

Preferred addressing mode with which the application tries to connect with the CTI Manager when IPv4 or IPv6 address is available.
                                             Click the radio button that is applicable.

If the TSP fails to connect, it retries with the other IP addressing modes.

### Security

The Security tab allow you to configure the security settings for the selected TSP instance, as illustrated in below.

The table below describes the Security tab fields that must be set.

Field

Description

Secure Connection to CTIManager

If selected, TSP will secure the connection with CTIManager. Default setting is a non-secure connection, so the setting is
                                             unchecked.

It is important that the security flag for the TSP User must be enabled through the Cisco Unified CM Administration UI. CTIManager
                                             performs a verification to check whether the User connecting via TLS is allowed to have secure access. CTIManager allows only
                                             security-enabled users to connect using TLS.

The User flag to enable security requires the cluster security to also be enabled/set, otherwise the connection has to be
                                             non-secure.

Fetch Certificates

Select this option for the Cisco TSP to download certificate files if they are not already available or installed. This is
                                             performed when the certificate status is Need Update.

This setting is not stored anywhere and is used only to update the Client certificate when checked and is cleared automatically.

Authorization String

Provide the authentication (authorization) string generated under the CAPF profile.

To install or upgrade a locally stored certificate, the User must enter the authentication (authorization) string. This string
                                             supports one-time use only; after you use the string for an instance, you cannot use it again.

This is required for Client authentication with CAPF Server and Private Key storage on client machine.

Instance Identifier

Provide Instance ID for CAPF end User profile:

Each secure connection to CTIManager must have its own certificate for authentication. With the restriction of a distinct
                                             certificate per connection, CAPF Server must verify that the user with appropriate AuthCode and InstanceID is requesting the
                                             certificate. CAPF server uses the AuthCode and InstanceID to verify the User's identity. Once CAPF server provides a certificate
                                             it clears the AuthCode to ensure that only one instance of an application requests a certificate based on a single AuthCode.
                                             Cisco Unified CM Administration UI allows User configuration to provide multiple InstanceID and AuthCode.

IP Address

Provide the CAPF server IP address from which to fetch the client certificate.

Port

Provide the CAPF Server Port to connect for Certificate download (Default :3804).

Number of Retries for Certificate Fetch

Indicates the number of retries TSP will perform to connect to the CAPF Server for certificate download in case of an error.

This value is used when a communication failure occurs while the certificate installation is taking place.

Default value is 0 and range is 0 to 3.

Retry Interval for Certificate Fetch

Indicates the number of seconds the TSP should wait between re-attempting to retrieve the certificate.

Default value is 0 and range is 0 to 15.

TFTP IP Address

Indicates the TFTP server IP address from which to fetch the CTL file. CTL file is required to verify the server certificate,
                                             sent while mutually authenticating the TLS connection.

TAPI connects to default UDP port (69) while downloading the CTL file.

### Configuring Cisco Media Driver and Cisco Wave Driver

#### Cisco Media Driver

The Cisco Media Driver configuration can be changed by
                                 		  selecting Configure Cisco TAPI Media Driver from the Cisco TSP Program Group.
                                 		  The user can choose to use the Cisco Wave Driver or the new Cisco Media Driver,
                                 		  as show below. When the Cisco Media Driver is selected, the Udp Port Range
                                 		  Start and End settings appear. The media driver settings are used by all TSP
                                 		  instances. If the Cisco Wave Driver is desired, select Cisco Wave Driver and
                                 		  refer to Cisco Media Driver Selection .

#### Cisco Wave Driver

The Cisco Wave Media configuration can be changed by
                                 		  selecting Cisco TAPI Configuration from the Cisco TSP Program Group. Select the
                                 		  desired Instance and click Configure. Choose the Wave tab, see the following
                                 		  figure, to configure the Wave driver settings for the specified instance.

The table below describes the Wave tab fields that must be
                                 		  set.

Field

Description

Automated Voice Calls

The number of Cisco Wave devices determines the
                                             					 number of automated voice lines. (The default value is 5.) The application can
                                             					 open as many CTI ports as the number of Cisco Wave devices that are configured.
                                             					 For example, if you enter "5," you need to create five CTI port devices in
                                             					 Cisco Unified Communications Manager. If you change this number, you need to
                                             					 remove and then reinstall any Cisco Wave devices which were installed.

A maximum of 255 Wave devices for all installed TSP
                                             					 instances can be configured. The Wave device limit is specific to Microsoft
                                             					 TAPI which limits the number of Wave devices per Wave driver to 255. The Cisco
                                             					 Media Driver does not have this limitation.

When you configure 256 or more Wave devices
                                             					 (including Cisco or other Wave devices), Windows displays the following message
                                             					 when you access the Sounds and Multimedia control panel: "An Error occurred
                                             					 while Windows was working with the Control Panel file
                                             					 C:\Winnt\System32\MMSYS.CPL."

The current number of possible automated voice lines
                                             					 designates the maximum number of lines that can be simultaneously opened by
                                             					 using both LINEMEDIAMODE_AUTOMATEDVOICE and LINEMEDIAMODE_INTERACTIVEVOICE.

If you are not developing a third-party call control
                                             					 application, check the Enumerate only lines that support automated voice check
                                             					 box, so the Cisco TSP detects only lines that are associated with a CTI port
                                             					 device.

Silence Detection

If you use silence detection, this check box
                                             					 notifies the Wave driver to detect silence on lines that support automated
                                             					 voice calls that are using the Cisco Wave Driver. If the check box is selected
                                             					 (default), the Wave driver searches for the absence of audio-stream RTP
                                             					 packets. As all devices on the network suppress silence and stop sending
                                             					 packets, this method provides a very efficient way for the Wave driver to
                                             					 detect silence.

However, if some phones or gateways do not perform
                                             					 silence suppression, the Wave driver must analyze the content of the media
                                             					 stream and, at some threshold, declare that silence is in effect. This
                                             					 CPU-intensive method handles media streams from any type of device.

If some phones or gateways on your network do not
                                             					 perform silence suppression, you must specify the energy level at which the
                                             					 Wave driver declares that silence is in effect. This value of the 16-bit linear
                                             					 energy level ranges from 0 to 32767, and the default value is 200. If all
                                             					 phones and gateways perform silence suppression, the system ignores this value.

### Trace

The Trace tab allows you to configure various trace settings, as illustrated below. Changes to trace parameters take effect
                                 immediately and do not require a computer reboot, even if the TSP is running.

The table below describes the Trace tab fields that must be set.

Field

Description

On

This setting allows you to enable Global Cisco TSP trace.

Select the check box to enable Cisco TSP trace. When you enable trace, you can modify other trace parameters in the dialog
                                             box. The Cisco TSP trace depends on the values that you enter in these fields.

Clear the check box to disable Cisco TSP trace. When you disable trace, you cannot choose any trace parameters in the dialog
                                             box, and TSP ignores the values that are entered in these fields.

File size

Default file size is 1 MB.

No. of files

Use this field to specify the maximum number of trace files. The default value is 10. File numbering occurs in a rotating
                                             sequence starting at 0. The counter restarts at 0 after it reaches the maximum number of files minus one.

Directory

Use this field to specify the location in which trace files for all CiscoTSPs are stored.

The system creates a subdirectory for each instance of CiscoTSP. For example, the CiscoTSP001Log directory stores Cisco TSP
                                             1 log files. The system creates trace files with filename TSP001Debug000xxx.txt for each TSP in its respective subdirectory.

TSP Trace

This setting activates internal TSP tracing. When you activate TSP tracing, Cisco Unified TSP logs internal debug information
                                             that you can use for debugging purposes. You can choose one of the following levels:

Error—Logs only TSP errors.

Detailed—Logs all TSP details (such as log function calls in the order that they are called).

The system checks the TSP Trace check box and chooses the Error radio button by default.

CTI Trace

This setting traces messages that flow between Cisco TSP and CTIManager. By default, CTI Trace is not selected.

TSPI Trace

This setting traces all messages and function calls between Microsoft TAPI and the Cisco TSP.   By default, TSPI Trace is
                                             not selected.

If TSPI Trace is enabled, Cisco TSP traces all the function calls that Microsoft TAPI makes to the Cisco TSP with parameters
                                             and messages (events) from Cisco TSP to MS TAPI.

### Advanced

The Advanced tab allows you to configure timer settings, as illustrated in below.

Timer settings should only be changed when necessary and recommended by Cisco Technical Assistance Center (TAC).

The table below describes the Advanced tab fields that must be set.

Field

Description

Synchronous Message Timeout (secs)

Use this field to designate the time that the TSP waits to receive a response to a synchronous message. The value displays
                                             in seconds, and the default value is 15. Range goes from 5 to 60 seconds.

Requested Heartbeat Interval (secs)

Use this field to designate the interval at which the heartbeat messages are sent from TSP to detect whether the CTI Manager
                                             connection is still alive. TSP sends heartbeats when no traffic exists between the TSP and CTI Manager for 30 seconds or more.
                                             The default interval is 30 seconds. Range goes from 30 to 300 seconds.

Connect Retry Interval (secs)

Use this field to designate the interval between reconnection attempts after a CTI Manager connection failure. The default
                                             value is 30 seconds. Range goes from 15 to 300 seconds.

Provider Open Completed Timeout (secs)

Use this field to designate the time that Cisco Unified TSP waits for a Provider Open Completed Event, which indicates the
                                             CTI Manager is initialized and ready to serve TSP requests. Be aware that CTI initialization time is directly proportional
                                             to the number of devices that are configured in the system. The default value is 50 seconds. Range goes from 5 to 900 seconds.

### Language

The Language tab displays the installed locales and allows for localization of the client user interface, as illustrated in
                                 below.

The following table desctribes the Language tab fields.

Field

Description

TFTP Server IP Address

Configure the TFTP server IP where the COP files are installed for the desired Locales.

Update Locale Files

Downloads the locale files from the configured TFTP server and extracts those files to the resources directory in the client
                                             machine

Change Language

Choose a language and click this to reload the tabs with the text in that language.

## Managing the Cisco Unified CM TSP

You can perform the following actions on all installed TSPs:

Reinstall the existing Cisco Unified TSP client (same version)

Upgrade to the newer version of the Cisco TSP client

Remove Cisco TSP from the Telephone Service Provider List

Uninstall the Cisco TSP client

Uninstall the Cisco Wave Driver

### Reinstall the Cisco Unified TSP

Use the following procedure to reinstall the Cisco Unified
                                 		  TSP on all supported platforms.

Step 1

Open the Control Panel and double-click Add/Remove Programs .

Step 2

Choose Cisco Unified TSP and click Change .

The Cisco Unified TSP maintenance install dialog box displays.

Step 3

Click the Reinstall TSP radio button and click Next .

Step 4

Follow the online instructions.

Step 5

Restart the computer

### Upgrade the Cisco Unified TSP

Use the following procedure to upgrade the Cisco Unified TSP
                                 		  on all supported platforms.

Step 1

Download and save the new TSP client on the target PC and
                                          			 double-click the installer.

Step 2

Select the Upgrade from TSP radio button and click Next .

Step 3

Follow the online instructions.

Step 4

Restart the computer

### Remove Cisco Unified TSP From the Provider List

This process removes the Cisco TSP from the Microsoft
                                 		  provider list but does not uninstall the TSP client. To make these changes,
                                 		  perform the following steps.

Step 1

Open the Control Panel.

Step 2

Double-click the Phone and Modem icon.

Step 3

Click the Advanced tab.

Step 4

Choose the Cisco Unified TSP that you want to remove.

Step 5

To delete the Cisco Unified TSP from the list, click Remove .

### Uninstall the Cisco TSP Client

To remove the Cisco TSP client, choose Uninstall Cisco TAPI
                                 		  from the Cisco TSP Program Group.

Alternatively, use the following procedure to uninstall the
                                 		  Cisco TSP on all supported platforms.

Step 1

Open the Control Panel and double-click Add/Remove Programs .

Step 2

Choose the Cisco Unified TSP that you want to remove and click Remove .

The Cisco TSP maintenance install dialog box displays.

Step 3

Select the Uninstall: Remove the installed TSP radio button and click Next .

Step 4

Follow the online instructions.

Step 5

Restart the computer

### Uninstall the Cisco Wave Driver

To remove the Cisco Wave Driver, perform one of the
                                 		  following procedures.

### Auto Update for Cisco Unified TSP Upgrades

Cisco TSP supports an auto update feature, so the latest client is downloaded and installed on the client machine automatically.
                              When Cisco Unified Communications Manager is upgraded to a higher version and the Cisco TSP client Auto-Upgrade option is
                              set to Ask or Always, the latest Cisco TSP client will be downloaded to the computer automatically. If Ask is configured,
                              the user will be prompted to upgrade the client. If Always is configured, the client will upgrade automatically. The logged-in
                              user must have local Administrative rights to install applications to use the auto-upgrade feature.

## Verify the Cisco Unified CM TSP Installation

Use the Microsoft Windows Phone Dialer Application to verify
                              		  that the Cisco TSP client has been installed and is configured correctly.
                              		  Locate the dialer application by performing a search for dialer.exe.

Step 1

Open the Dialer application by locating it in Windows Explorer and
                                       			 double-clicking it

Step 2

Choose Edit > Options .

Step 3

Choose Phone as the Preferred Line for Calling .

Step 4

In the Line Used For area, choose one Cisco Line in the Phone Calls drop-down menu.

Step 5

Click OK .

Step 6

Click Dial .

Step 7

Enter a number to dial, choose Phone Call in the Dial as box, and
                                       			 then click Place Call .

### What to do next

If the call is successful, the Cisco TSP client is installed
                              		  correctly.

If you encounter problems during this procedure, or if no lines appear
                              		  in the line drop-down list on the dialer application, check the following
                              		  items:

Verify the Cisco TSP configuration settings by opening the Cisco
                                    				TAPI Configuration tool and verifying the configured parameters.

Reboot the computer to ensure all configuration options and
                                    				installation processes have completed and are updated successfully.

Test the network link between the Cisco TSP client machine and
                                    				Cisco Unified CM by using the ping command to check connectivity.

Ensure that the Cisco Unified CM CTIManager is running.

## Cisco TSP Behavior on Windows Upgrade

On upgrade of windows to a higher version, for example from Windows 8 to Windows 10, Cisco TSP must be reinstalled to retain
                           all the previous instances of data present in CiscoTSP Configuration.

Perform the following procedure to reinstall the Cisco Unified TSP.

Reinstall the Cisco Unified TSP

| Note | The upgraded TAPI client software does not work with previous releases of Unified Communications Manager . |
|---|---|

| Caution | You can install Cisco TSP on a system only where Windows is installed on
                                       C:\. If Windows is installed on a drive other than
                                       C:\, an attempt to install Cisco TSP will fail. |
|---|---|

| Note | Windows(64-bit) Operating Systems require native 64-bit Cisco TSP client. For more information on availability, see https://community.cisco.com/t5/collaboration-blogs/bg-p/j-blogs-dev-collab . |
|---|---|

| Note | Cisco TSP legacy wave driver is not supported under VMWare. . |
|---|---|

| Note | If you are installing multiple TSPs, multiple copies of CiscoTSPXXX.tsp and CiscoTUISPXXX.dll files will exist in the same
                                       Windows system directory. |
|---|---|

| Note | Cisco Media Driver settings apply to all configured TSP instances.
                                             			 Cisco Wave Driver settings are instance specific. |
|---|---|

| Step 1 | Open the Control Panel. |
|---|---|
| Step 2 | Open Add Hardware . The Add Hardware Wizard window appears. |
| Step 3 | Click Next . |
| Step 4 | Select Yes, I have already connected the hardware . |
| Step 5 | Select Add a New Hardware Device . |
| Step 6 | Click Next . |
| Step 7 | Select Install the Hardware that I manually select from a list . |
| Step 8 | Click Next . |
| Step 9 | For the hardware type, choose Sound, video and game controller . |
| Step 10 | Click Next . |
| Step 11 | Click Have Disk . |
| Step 12 | Click Browse and navigate to the Wave Drivers folder in the folder
                                             			 where the Cisco Unified Communication Manager TSP is installed. |
| Step 13 | Choose OEMSETUP.INF and click Open . |
| Step 14 | In the Install From Disk window, click OK . |
| Step 15 | In the Select a Device Driver window, select the Cisco Unified Communication Manager TAPI Wave Driver and click Next . |
| Step 16 | In the Start Hardware Installation window, click Next . |
| Step 17 | If Prompted for Digital signature Not Found, click Continue Anyway . |
| Step 18 | The installation may issue the following prompt: The avaudio32.dll file on Windows NT Setup Disk #1 is needed, Type the path where the file is located and then click OK . If so, navigate to the same location where you chose
                                                				OEMSETUP.INF, select avaudio32.dll, and click OK . |
| Step 19 | Click Yes . |
| Step 20 | Click Finish . |
| Step 21 | Click Yes to restart the computer. |

| Step 1 | Right click My computer and select Manage . The Computer Management window appears. |
|---|---|
| Step 2 | From System Tools , select Device Manager . |
| Step 3 | Right click on the <Computer-Name> and select Install Legacy Wave Driver . This action pops up an Add
                                             			 Hardware window. |
| Step 4 | Select Install the Hardware that I manually select from a list . |
| Step 5 | Click Next . |
| Step 6 | For the hardware type, choose Sound, video and game controller . |
| Step 7 | Click Next . |
| Step 8 | Click Have Disk . |
| Step 9 | Click Browse and navigate to the Wave Drivers folder in the folder
                                             			 where the Cisco Unified Communication Manager TSP is installed. |
| Step 10 | Choose OEMSETUP.INF and click Open . |
| Step 11 | In the Install From Disk window, click OK . |
| Step 12 | In the Select a Device Driver window, select the Cisco Unified Communication Manager TAPI Wave Driver and click Next . |
| Step 13 | In the Start Hardware Installation window, click Next . |
| Step 14 | If Prompted for Digital signature Not Found, click Continue Anyway . |
| Step 15 | The installation may issue the following prompt: The avaudio32.dll file on Windows NT Setup Disk #1 is needed, Type the path where the file is located and then click OK . If so, navigate to the same location where you chose
                                                				OEMSETUP.INF, select avaudio32.dll, and click OK . |
| Step 16 | Click Yes . |
| Step 17 | Click Finish . |
| Step 18 | Click Yes to restart the computer. |

| Step 1 | Click Start > Run . |
|---|---|
| Step 2 | In the text box, enter regedit. |
| Step 3 | Click OK . |
| Step 4 | Choose the Drivers32 key that is located in the following path: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion |
| Step 5 | If you are installing the Wave driver, make sure that the driver avaudio32.dll displays in the data column. If you are uninstalling
                                          the Wave driver, make sure that the driver avaudio32.dll does not display in the data column. This designates the Cisco Wave
                                          Driver. |
| Step 6 | Verify that the previously existing Wave values appear in the data column for Wave1, Wave2, Wave3, and so on. You can compare
                                          this registry list to the contents of the .reg file that you saved in the procedure by opening the .reg file in a text editor
                                          and viewing it and the registry window side by side. |
| Step 7 | If necessary, add the appropriate WaveX string values for any missing Wave values that should be installed on the system.
                                          For each missing Wave value, choose Edit > New > String Value and enter a value name. Then, choose Edit > Modify , enter the value data, and click OK . |
| Step 8 | Close the registry by choosing Registry > Exit . Configure the Cisco Wave Driver settings using the Wave tab in the Cisco TAPI Configuration tool (available after installation). |

| Name | Comment | Valid values |
|---|---|---|
| USER | User name used to during provider initializing | All |
| PASS | Password used to during provider initializing | All |
| CTI1 | CTI Manager 1 IP address | All |
| CTI2 | CTI Manager 2 IP address | All |
| NONAD | Non-admin can modify the userid/password | "NO", "YES" |
| CTI1_TYPE | Ipv4, Ipv6, or hostname | "NONE", "IPV4", "IPV6", "HOST" |
| CTI2_TYPE | None, Ipv4, Ipv6, or hostname | "NONE", "IPV4", "IPV6", "HOST" |
| AUTOUPGRADE_TYPE | Ask, Always, Never | "ASK", "NEVER", "ALWAYS" |
| DRIVER_TYPE | Cisco Wave Driver, Cisco Media Driver | "WAVE", "MEDIA" |
| NUM_WDP | Number of Legacy Wave Driver Ports | 0 -255 |
| MDP_START | Media Driver Port Start Range | 0 -65535 |
| MDP_END | Media Driver Port End Range | 0 -65535 |

| Note | In a case where more than one TSP instance is installed, you must use the client UI-based installation package when upgrading
                                          the TSP to maintain the existing configuration settings. |
|---|---|

| Field | Description |
|---|---|
| Ask Before Update | Auto-upgrade service prompts the User to upgrade the TSP client. |
| Never AutoUpdate | Select this to disable the auto-update service. |
| Always AutoUpdate | Select this to enable automatic updates when new TSP client versions are detected. |
| AutoUpdate on Incompatible QBEProtocolVersion | Select this to allow the Cisco TSP to auto update only when the local TSP version is incompatible with the Unified CM version. |

| Field | Description |
|---|---|
| User Name | Enter the user name of the user. The TSP instance will access devices and lines that are associated with this User in Cisco
                                             Unified CM. Make sure that this User is enabled for CTI using the Cisco Unified CM Administration UI Note You can designate only one user name and password to be active at any time for any one TSP instance. | Note | You can designate only one user name and password to be active at any time for any one TSP instance. |
| Note | You can designate only one user name and password to be active at any time for any one TSP instance. |
| Password | Enter the password that is associated with the user. The computer encrypts the password and stores it in the registry. |
| Verify Password | Reenter the user password. |

| Note | You can designate only one user name and password to be active at any time for any one TSP instance. |
|---|---|

| Field | Description |
|---|---|
| Primary CTI Manager Location | Use this field to specify the CTI Manager to which the TSP attempts to connect to first. Select one of the following options: Click the IP Address radio button and use the text box to provide the IPv4 address of the Primary CTI Manager. Click the IPV6 Address radio button and use the text box to provide the IPv6 address, if the application must connect using IPv6 with the Primary
                                                   CTI Manager. Click the Host Name radio button and enter the host name of the Primary CTI Manager. |
| Backup CTI Manager Location | Use this field to specify the CTI Manager to which the TSP attempts to connect when the Primary CTI Manager is not reachable.
                                             Select one of the following options: Click the IP Address radio button and use the text box to provide the IPv4 address of the Backup CTI Manager. Click the IPV6 Address radio button and use the text box to provide the IPv6 address, if the application must connect using IPv6 with the Backup
                                                   CTI Manager. Click the Host Name radio button and enter the host name of the Backup CTI Manager. |
| IP Addressing Preference | Preferred addressing mode with which the application tries to connect with the CTI Manager when IPv4 or IPv6 address is available.
                                             Click the radio button that is applicable. If the TSP fails to connect, it retries with the other IP addressing modes. |

| Field | Description |
|---|---|
| Secure Connection to CTIManager | If selected, TSP will secure the connection with CTIManager. Default setting is a non-secure connection, so the setting is
                                             unchecked. It is important that the security flag for the TSP User must be enabled through the Cisco Unified CM Administration UI. CTIManager
                                             performs a verification to check whether the User connecting via TLS is allowed to have secure access. CTIManager allows only
                                             security-enabled users to connect using TLS. The User flag to enable security requires the cluster security to also be enabled/set, otherwise the connection has to be
                                             non-secure. |
| Fetch Certificates | Select this option for the Cisco TSP to download certificate files if they are not already available or installed. This is
                                             performed when the certificate status is Need Update. This setting is not stored anywhere and is used only to update the Client certificate when checked and is cleared automatically. |
| Authorization String | Provide the authentication (authorization) string generated under the CAPF profile. To install or upgrade a locally stored certificate, the User must enter the authentication (authorization) string. This string
                                             supports one-time use only; after you use the string for an instance, you cannot use it again. This is required for Client authentication with CAPF Server and Private Key storage on client machine. |
| Instance Identifier | Provide Instance ID for CAPF end User profile: Each secure connection to CTIManager must have its own certificate for authentication. With the restriction of a distinct
                                             certificate per connection, CAPF Server must verify that the user with appropriate AuthCode and InstanceID is requesting the
                                             certificate. CAPF server uses the AuthCode and InstanceID to verify the User's identity. Once CAPF server provides a certificate
                                             it clears the AuthCode to ensure that only one instance of an application requests a certificate based on a single AuthCode.
                                             Cisco Unified CM Administration UI allows User configuration to provide multiple InstanceID and AuthCode. |
| IP Address | Provide the CAPF server IP address from which to fetch the client certificate. |
| Port | Provide the CAPF Server Port to connect for Certificate download (Default :3804). |
| Number of Retries for Certificate Fetch | Indicates the number of retries TSP will perform to connect to the CAPF Server for certificate download in case of an error. This value is used when a communication failure occurs while the certificate installation is taking place. Default value is 0 and range is 0 to 3. |
| Retry Interval for Certificate Fetch | Indicates the number of seconds the TSP should wait between re-attempting to retrieve the certificate. Default value is 0 and range is 0 to 15. |
| TFTP IP Address | Indicates the TFTP server IP address from which to fetch the CTL file. CTL file is required to verify the server certificate,
                                             sent while mutually authenticating the TLS connection. Note TAPI connects to default UDP port (69) while downloading the CTL file. | Note | TAPI connects to default UDP port (69) while downloading the CTL file. |
| Note | TAPI connects to default UDP port (69) while downloading the CTL file. |

| Note | TAPI connects to default UDP port (69) while downloading the CTL file. |
|---|---|

| Field | Description |
|---|---|
| Automated Voice Calls | The number of Cisco Wave devices determines the
                                             					 number of automated voice lines. (The default value is 5.) The application can
                                             					 open as many CTI ports as the number of Cisco Wave devices that are configured.
                                             					 For example, if you enter "5," you need to create five CTI port devices in
                                             					 Cisco Unified Communications Manager. If you change this number, you need to
                                             					 remove and then reinstall any Cisco Wave devices which were installed. A maximum of 255 Wave devices for all installed TSP
                                             					 instances can be configured. The Wave device limit is specific to Microsoft
                                             					 TAPI which limits the number of Wave devices per Wave driver to 255. The Cisco
                                             					 Media Driver does not have this limitation. When you configure 256 or more Wave devices
                                             					 (including Cisco or other Wave devices), Windows displays the following message
                                             					 when you access the Sounds and Multimedia control panel: "An Error occurred
                                             					 while Windows was working with the Control Panel file
                                             					 C:\Winnt\System32\MMSYS.CPL." The current number of possible automated voice lines
                                             					 designates the maximum number of lines that can be simultaneously opened by
                                             					 using both LINEMEDIAMODE_AUTOMATEDVOICE and LINEMEDIAMODE_INTERACTIVEVOICE. If you are not developing a third-party call control
                                             					 application, check the Enumerate only lines that support automated voice check
                                             					 box, so the Cisco TSP detects only lines that are associated with a CTI port
                                             					 device. |
| Silence Detection | If you use silence detection, this check box
                                             					 notifies the Wave driver to detect silence on lines that support automated
                                             					 voice calls that are using the Cisco Wave Driver. If the check box is selected
                                             					 (default), the Wave driver searches for the absence of audio-stream RTP
                                             					 packets. As all devices on the network suppress silence and stop sending
                                             					 packets, this method provides a very efficient way for the Wave driver to
                                             					 detect silence. However, if some phones or gateways do not perform
                                             					 silence suppression, the Wave driver must analyze the content of the media
                                             					 stream and, at some threshold, declare that silence is in effect. This
                                             					 CPU-intensive method handles media streams from any type of device. If some phones or gateways on your network do not
                                             					 perform silence suppression, you must specify the energy level at which the
                                             					 Wave driver declares that silence is in effect. This value of the 16-bit linear
                                             					 energy level ranges from 0 to 32767, and the default value is 200. If all
                                             					 phones and gateways perform silence suppression, the system ignores this value. |

| Field | Description |
|---|---|
| On | This setting allows you to enable Global Cisco TSP trace. Select the check box to enable Cisco TSP trace. When you enable trace, you can modify other trace parameters in the dialog
                                             box. The Cisco TSP trace depends on the values that you enter in these fields. Clear the check box to disable Cisco TSP trace. When you disable trace, you cannot choose any trace parameters in the dialog
                                             box, and TSP ignores the values that are entered in these fields. |
| File size | Default file size is 1 MB. |
| No. of files | Use this field to specify the maximum number of trace files. The default value is 10. File numbering occurs in a rotating
                                             sequence starting at 0. The counter restarts at 0 after it reaches the maximum number of files minus one. |
| Directory | Use this field to specify the location in which trace files for all CiscoTSPs are stored. The system creates a subdirectory for each instance of CiscoTSP. For example, the CiscoTSP001Log directory stores Cisco TSP
                                             1 log files. The system creates trace files with filename TSP001Debug000xxx.txt for each TSP in its respective subdirectory. |
| TSP Trace | This setting activates internal TSP tracing. When you activate TSP tracing, Cisco Unified TSP logs internal debug information
                                             that you can use for debugging purposes. You can choose one of the following levels: Error—Logs only TSP errors. Detailed—Logs all TSP details (such as log function calls in the order that they are called). The system checks the TSP Trace check box and chooses the Error radio button by default. |
| CTI Trace | This setting traces messages that flow between Cisco TSP and CTIManager. By default, CTI Trace is not selected. |
| TSPI Trace | This setting traces all messages and function calls between Microsoft TAPI and the Cisco TSP.   By default, TSPI Trace is
                                             not selected. If TSPI Trace is enabled, Cisco TSP traces all the function calls that Microsoft TAPI makes to the Cisco TSP with parameters
                                             and messages (events) from Cisco TSP to MS TAPI. |

| Note | Timer settings should only be changed when necessary and recommended by Cisco Technical Assistance Center (TAC). |
|---|---|

| Field | Description |
|---|---|
| Synchronous Message Timeout (secs) | Use this field to designate the time that the TSP waits to receive a response to a synchronous message. The value displays
                                             in seconds, and the default value is 15. Range goes from 5 to 60 seconds. |
| Requested Heartbeat Interval (secs) | Use this field to designate the interval at which the heartbeat messages are sent from TSP to detect whether the CTI Manager
                                             connection is still alive. TSP sends heartbeats when no traffic exists between the TSP and CTI Manager for 30 seconds or more.
                                             The default interval is 30 seconds. Range goes from 30 to 300 seconds. |
| Connect Retry Interval (secs) | Use this field to designate the interval between reconnection attempts after a CTI Manager connection failure. The default
                                             value is 30 seconds. Range goes from 15 to 300 seconds. |
| Provider Open Completed Timeout (secs) | Use this field to designate the time that Cisco Unified TSP waits for a Provider Open Completed Event, which indicates the
                                             CTI Manager is initialized and ready to serve TSP requests. Be aware that CTI initialization time is directly proportional
                                             to the number of devices that are configured in the system. The default value is 50 seconds. Range goes from 5 to 900 seconds. |

| Field | Description |
|---|---|
| TFTP Server IP Address | Configure the TFTP server IP where the COP files are installed for the desired Locales. |
| Update Locale Files | Downloads the locale files from the configured TFTP server and extracts those files to the resources directory in the client
                                             machine |
| Change Language | Choose a language and click this to reload the tabs with the text in that language. |

| Step 1 | Open the Control Panel and double-click Add/Remove Programs . |
|---|---|
| Step 2 | Choose Cisco Unified TSP and click Change . The Cisco Unified TSP maintenance install dialog box displays. |
| Step 3 | Click the Reinstall TSP radio button and click Next . |
| Step 4 | Follow the online instructions. |
| Step 5 | Restart the computer |

| Step 1 | Download and save the new TSP client on the target PC and
                                          			 double-click the installer. |
|---|---|
| Step 2 | Select the Upgrade from TSP radio button and click Next . |
| Step 3 | Follow the online instructions. |
| Step 4 | Restart the computer |

| Step 1 | Open the Control Panel. |
|---|---|
| Step 2 | Double-click the Phone and Modem icon. |
| Step 3 | Click the Advanced tab. |
| Step 4 | Choose the Cisco Unified TSP that you want to remove. |
| Step 5 | To delete the Cisco Unified TSP from the list, click Remove . |

| Step 1 | Open the Control Panel and double-click Add/Remove Programs . |
|---|---|
| Step 2 | Choose the Cisco Unified TSP that you want to remove and click Remove . The Cisco TSP maintenance install dialog box displays. |
| Step 3 | Select the Uninstall: Remove the installed TSP radio button and click Next . |
| Step 4 | Follow the online instructions. |
| Step 5 | Restart the computer |

| Step 1 | Open the Dialer application by locating it in Windows Explorer and
                                       			 double-clicking it |
|---|---|
| Step 2 | Choose Edit > Options . |
| Step 3 | Choose Phone as the Preferred Line for Calling . |
| Step 4 | In the Line Used For area, choose one Cisco Line in the Phone Calls drop-down menu. |
| Step 5 | Click OK . |
| Step 6 | Click Dial . |
| Step 7 | Enter a number to dial, choose Phone Call in the Dial as box, and
                                       			 then click Place Call . |