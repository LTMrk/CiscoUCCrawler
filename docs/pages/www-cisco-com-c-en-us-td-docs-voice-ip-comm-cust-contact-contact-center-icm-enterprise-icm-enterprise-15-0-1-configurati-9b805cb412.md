---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-configurati-9b805cb412
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/configuration/guide/ucce_b_security-guide-for-cisco-unified-icm-contact-center-enterprise-release-15-0/windows_security_hardening.html
retrieved_at: 2026-08-16T14:36:27.662134+00:00
---

Security Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1)

# Security Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1)

Updated: April 30, 2025

Chapter: Windows Security Hardening

## Chapter: Windows Security Hardening

# Windows Security Hardening

## Windows Server Hardening

As a best practice, we recommend using the Microsoft security baseline and CIS benchmarks
                           for secure configuration of ICM servers. Use the latest Microsoft security baseline and
                           Level 1 CIS benchmark profile to lower the attack surface without impacting the
                           functionality and performance.

Apply the security policy in the form of Group Policy Object (GPO) into a separate
                           Organizational Unit(OU) that contains ICM servers. Name the OU as Cisco_ICM_Servers (or
                           a similar clearly identifiable name) and ensure to name these servers in accordance with
                           your corporate policy.

After applying the security policy at the OU level, block any differing policies from being inherited at the Unified Contact
                           Center Enterprise Servers OU. You can override a blocking inheritance, a configuration option at the OU object level, by selecting
                           the Enforced/No Override option at a higher hierarchy level. The application of group policies must follow a thought-out design
                           that starts with the most common denominator. These group policies must be restrictive at the appropriate level in the hierarchy.

## Cisco Unified Contact Center Enterprise Security Hardening for Windows Server

This section outlines the security baseline that is needed for hardening Windows Servers
                           running ICM servers. This security baseline is essentially a collection of Microsoft
                           group policy settings based on the Microsoft security baseline and Level 1 CIS benchmark
                           profile.

To apply the security baseline in the domain controller, perform the following steps:

Download the security hardening templates applicable for the respective Windows
                                 version from the  Microsoft and CIS benchmark URL. You can download these
                                 security hardening templates from https://www.microsoft.com/en-us/download/details.aspx?id=55319 and https://workbench.cisecurity.org/files?q=&tags=3 .

Install the latest Administrative Templates (ADMX) for the Windows Server. These
                                 templates can be downloaded from the Microsoft website at https://www.microsoft.com/en-us/download/details.aspx?id=103667 . You can install the .msi
                                    installer on any Windows node as per your IT policy. The windows
                                 server can be ICM or non ICM or Domain Controller.

Navigate to the installed location of administrative templates. Copy the
                                 below-mentioned template files to the domain controller SYSVOL folder.

Copy the *.admx files from the PolicyDefinitions folder to \<Domain>\SYSVOL<Domain>\Policies\PolicyDefinitions

Copy the *.adml files from the PolicyDefinitions<applicable-language>
                                       folder to \<Domain>\SYSVOL<Domain>\Policies\PolicyDefinitions\en-US

Note

The domain controller automatically copies the admx and adml files to
                                                   all the domain-joined machines.

Select the applicable language code (en-US) based on your
                                                   deployment setting.

Create the PolicyDefinitions folder if it does not exist.

Create a Group Policy Object in the domain controller using the Group
                                    Policy Management console and import respective policy using the
                                 Import Setting Wizard in the console as per below details. This can be done
                                 directly on the ICM nodes based on the IT policy.

The downloaded Microsoft baseline (see Step-1) has Group Policy Object
                                       (GPO) for Windows Client, Windows Server, Common GPO for both Client and
                                       Server, Domain Controller, and Internet Explorer. We recommend you to
                                       import the GPO specific to Windows Server, Internet Explorer, and Common
                                       GPO for both Client and Server.

The downloaded CIS baseline (see Step-1) has GPO for Domain Controller,
                                       Microsoft, and User. We recommend importing only the MS-L1 and User-L1
                                       GPO.

Create the custom GPO in the Domain Controller to override the policies outlined
                                 in the Security Baseline
                                       Policy Exception for ICM , and import the custom exception GPO
                                 using import setting wizard in the console. You can manually override the
                                 policies directly on the ICM nodes based on the IT policy.

Ensure that the exception policy imported (see Step-5) has higher priority such
                                 that the exception policy is applied after the Microsoft and CIS policies are
                                 applied.

Note

Step 6 is applicable only on domain controllers.

Create the OU Cisco_ICM_Servers (or a similar identifiable
                                 name) under the domain. Map all the ICM machines to this OU. You can perform
                                 this step at any point, even before performing Step-1.

Link the created GPO (see Step-4 and Step-5) to the OU created (see Step-7).

Restart the ICM servers in the organizational unit or run the gpupdate command on the respective target ICM nodes to
                                 apply the security baseline.

Note

You can set the Turn on Virtualization Based Security policy to Disabled when Secure Boot is not enabled on Unified ICM machines.

### Security Baseline Policy Exception for ICM

The following CIS baseline policies impact the ICM functionality.

The recommended values (outlined in the table below) are to be used for the exception
                              policies to override the recommended values of CIS.

You can enable this only after configuring the
                                       appropriate rules under the setting Configure Attack Surface
                                          Reduction rules: Set the state for each ASR rule . These
                                       include adding trusted/known applications with path in the exception
                                       list. The list of impacted application differs, so the
                                       recommendation is to set the value to Disabled .

The following policies are optional. You can enable these policies as per the IT
                              policy after considering the remarks column carefully.

Note

This policy is removed in CIS benchmark for Windows Server 2022.

Ensure 'MSS: (AutoAdminLogon) Enable Automatic Logon (not recommended)' is set to 'Disabled'

CIS

Enabled

Unified ICM and Unified CVP 15.0(1) upgrade via Orchestration requires Automatic Logon to be enabled to control the upgrade
                                       remotely from Cloud Connect. Set this to Enabled only if Orchestration is used for Unified ICM or Unified CVP 15.0(1) upgrade. Post the upgrade, you can set this configuration
                                       to Disabled .

Ensure 'User Account Control: Behavior of the elevation prompt for administrators in Admin Approval Mode' is set to 'Prompt
                                       for consent on the secure desktop'

CIS

Elevate without prompting

Unified ICM and Unified CVP 15.0(1) upgrade via Orchestration requires Elevate without prompting to be set to control the upgrade remotely from Cloud Connect. Set this to Elevate without prompting only if Orchestration is used for Unified ICM or Unified CVP 15.0(1) upgrade. Post the upgrade, you can set this configuration
                                       to Prompt for consent on the secure desktop .

Enable the following policies after you install the ICM server. Refer to the Remarks
                              column for the deviations observed.

Note

The CIS benchmark versions 3.0.0 for Windows Server 2022, version 1.2.1 for Windows Server 2019, Microsoft baseline Windows Server 2019 version 1809,
                                             and latest Microsoft baseline Windows Server 2022 are validated. Before applying the higher version of CIS and Microsoft benchmark, analyze the additional policies introduced in the new
                                       version for the impact on ICM functionality and performance. We recommend the GPOs must be tailored according to your organization’s
                                       need. We recommend rolling out the GPOs to a small group of systems, preferably in a lab environment before rolling out into
                                       production.

In addition to the GPO settings, disable the following settings in Windows Server:

NetBIOS

SMBv1

Note

CCE software requires Windows PowerShell to be available and not blocked by Group Policy during installation, uninstallation,
                                       and upgrade processes of main releases, maintenance releases, and Engineering Specials (ES). Additionally, certain CCE tools
                                       depend on PowerShell and may invoke it dynamically at any time after the CCE software installation. Therefore, access to PowerShell
                                       must not be blocked post-installation.

Ensure that Windows PowerShell execution is permitted and not restricted by Group Policy settings to avoid operational issues.

## Windows Platform Services Hardening

ICM 15.0 disables below platform services which are currently not used by ICM. We recommend you to check your organisational
                              security policies and practices before enabling this services.

Service Name

Service Description

Default Service Startup Type

Disabled by ICM

CDPSvc

The service is used during connecting with Bluetooth devices and Printers, scanners, music players, mobile phones, cameras,
                                          etc.

Automatic

Yes

CDPUserSvc

Manages connections with devices like Bluetooth and Wi-Fi Direct. This service is used for Connected Devices and Universal
                                          Glass scenarios.

Automatic

Yes

DiagTrack

Customer Experience Improvement Program (CEIP) that collects and sends anonymized data to Microsoft.

Automatic

Yes

Spooler

This service spools print jobs and handles interaction with the printer. If you turn off this service, you can't print or
                                          see your printers.

Automatic

Yes

AJRouter

AllJoyn Router Service used for IOT.

Manual

Yes

bthserv

The Bluetooth service supports discovery and association of remote Bluetooth devices.

Manual

Yes

CaptureService

Enables optional screen capture functionality for applications that use Windows screen capture APIs.

Manual

Yes

CertPropSvc

Copies user certificates and root certificates from smart cards into the current user's certificate store, detects when a
                                          smart card is inserted into a smart card reader, and, if needed, installs the smart card Plug and Play minidriver.

Manual

Yes

DevicesFlowUserSvc

Allows the Connect user interface and Settings app to connect and pair with WiFi displays and Bluetooth devices.

Manual

Yes

DevQueryBroker

The DevQueryBroker service works by running a background task that periodically scans for devices. When it finds a new device,
                                          it sends a notification to all apps that have registered for device discovery events.

Manual

Yes

FrameServer

Enables multiple clients to access video frames from camera devices.

Manual

Yes

FrameServerMonitor

Monitors the status and health of Windows Camera Frame Server.

Manual

Yes

McpManagementService

Universal Print Management Service used to support remote printing.

Manual

Yes

PrintNotify

This service opens custom printer dialog boxes and handles notifications from a remote print server or a printer.

Manual

Yes

PrintWorkflowUserSvc

The PrintWorkflowUserSvc service in Windows supports applications that customize the printing workflow. This includes apps
                                          that alter the print content or print ticket, such as by adding watermarks, cropping margins, or applying filters.

Manual

Yes

RpcLocator

This is not used by latest Windows version, kept it for backward compatiblity of apps developed pre-Win2003. Remote Procedure
                                          Call (RPC) Locator service manages the RPC name service database.

Manual

Yes

SCardSvr

Manages access to smart cards read by this computer. If you stop this service, this computer becomes unable to read smart
                                          cards.

Manual

Yes

SCPolicySvc

Allows the system to be configured to lock the user desktop upon smart card removal.

Manual

Yes

SensorService

Manages the functionality of different sensors, including Simple Device Orientation (SDO) and History. Loads the SDO sensor
                                          that reports device orientation changes.

Manual

Yes

StiSvc

Provides image acquisition services for scanners and cameras.

Manual

Yes

TabletInputService

Service that optimizes Windows for tablet PCs with touch screens.

Manual

Yes

WbioSrvc

The Windows biometric service gives client applications the ability to capture, compare, manipulate, and store biometric data
                                          without gaining direct access to any biometric hardware or samples.

Manual

Yes

WMPNetworkSvc

The Windows Media Player Network Sharing Service (WMPNetworkSvc) shares Windows Media Player libraries to other media devices
                                          and networked players using Universal Plug and Play.

Manual

Yes

UnistoreSvc

Handles storage of structured user data, including contact info, calendars, messages, and other content.

Manual

Yes

WiaRpc

Launches applications associated with still image acquisition events. The WIA platform enables imaging/graphics applications
                                          to interact with imaging hardware and standardizes the interaction between different applications and scanners. This allows
                                          those different applications to talk to and interact with those different scanners without requiring the application writers
                                          and scanner manufactures to customize their application or drivers for each application-device combination.

Manual

Yes

### Contact Cisco

- Open a Support Case

- (Requires a Cisco Service Contract )

| Note | The domain controller automatically copies the admx and adml files to
                                                   all the domain-joined machines. Select the applicable language code (en-US) based on your
                                                   deployment setting. Create the PolicyDefinitions folder if it does not exist. |
|---|---|

| Note | Step 6 is applicable only on domain controllers. |
|---|---|

| Note | You can set the Turn on Virtualization Based Security policy to Disabled when Secure Boot is not enabled on Unified ICM machines. |
|---|---|

| Policy | CIS/Microsoft Baseline | Recommended Setting | Remarks |
|---|---|---|---|
| Ensure 'Perform volume maintenance tasks' is set to
                                    'Administrators' | CIS | Administrators, NT Service/MSSQLServer | The ICM database engine runs as service MSSQLSERVER . The NT
                                       SERVICE/MSSQLSERVER login is used by the service to
                                    connect to the database engine. This policy impacts on this
                                    connectivity. Hence, include the NT
                                       SERVICE/MSSQLSERVER setting in addition to the Administrators setting. |
| Ensure 'Windows Firewall: Public: Settings: Apply local firewall
                                    rules' is set to 'No' | CIS | Yes | This setting has an impact on operations of duplex CCE systems. For
                                    example, it impacts the private interface between the duplex router
                                    process. |
| Ensure 'Configure Attack Surface Reduction rules' is set to
                                    'Enabled' | CIS | Disabled | This policy impacts the CCE functionality. For example, patch install
                                    is impacted. Applications such as snmp, msgagent etc., are
                                    blocked. You can enable this only after configuring the
                                       appropriate rules under the setting Configure Attack Surface
                                          Reduction rules: Set the state for each ASR rule . These
                                       include adding trusted/known applications with path in the exception
                                       list. The list of impacted application differs, so the
                                       recommendation is to set the value to Disabled . |
| Ensure 'Select when Preview Builds and Feature Updates are received'
                                    is set to 'Enabled: Semi-Annual Channel, 180 or more days' | CIS | Disabled | Automatic updates interrupt the functionality during automatic
                                    restarts. |
| Ensure 'Select when Quality Updates are received' is set to 'Enabled:
                                    0 days' | CIS | Disabled | Automatic updates interrupt the functionality during automatic
                                    restarts. |
| Ensure 'Configure Automatic Updates' is set to 'Enabled' | CIS | Disabled | Automatic updates interrupts the functionality during automatic
                                    restarts. |
| Ensure 'No auto restart with logged-in users for scheduled automatic
                                    updates installations' is set to 'Disabled' | CIS | Enabled | Automatic updates interrupt the functionality during automatic
                                    restarts. |

| Policy | CIS/Microsoft Baseline | Recommended Setting | Remarks |
|---|---|---|---|
| Ensure 'Allow log on locally' is set to 'Administrators' | CIS | BUILTIN\Users, BUILTIN\Administrators | After you apply the policy, the Domain only accounts cannot log in to
                                    the machine and perform operations. We recommend you to add BUILTIN\Users and BUILTIN\Administrators . You can enable this
                                    policy based on the IT policy and operational requirements. |
| Ensure 'Deny access to this computer from the network' to include
                                    'Guests, Local account and member of Administrators group' (MS
                                    only) | CIS | Guests | This policy may have operational impacts specifically for day 0/1
                                    activities. We recommend setting the value to Guests . You can
                                    override this policy based on the IT policy and operational
                                    requirements. |
| Ensure 'Deny log on through Remote Desktop Services is set to
                                    'Guests, Local account' (MS only) | CIS | Guests | This policy may have operational impacts specifically for day 0/1
                                    activities. We recommend you setting the value to Guests . You can
                                    override this policy based on the IT policy and operational
                                    requirements. |
| 'Prevent ignoring certificate errors' to be set as 'Enabled' | Microsoft | Disabled | CCE web applications such as Websetup cannot be accessed using
                                    Internet Explorer. Accessing these web applications with other supported
                                    browsers like Mozilla Firefox and Google Chrome will not be impacted due
                                    to this policy. We recommend setting the value to Disabled . |
| 'Turn on Enhanced Protected Mode' to be set as 'Enabled' | Microsoft | Disabled | CCE web applications such as Websetup cannot be accessed using
                                    Internet Explorer. Accessing these web applications with other supported
                                    browsers like Mozilla Firefox and Google Chrome will not be impacted due
                                    to this policy. We recommend setting the value to Disabled . |
| Ensure 'Accounts: Administrator account status' is set to 'Disabled'
                                    (MS only) | CIS | Enabled | This policy has operational impacts. For example, if a member server goes out of domain for any reason, with this policy in
                                    place ,we need to use unrecommended safe mode login to add back the member server to the domain. Other operations will have
                                    similar impact too. Note This policy is removed in CIS benchmark for Windows Server 2022. | Note | This policy is removed in CIS benchmark for Windows Server 2022. |
| Note | This policy is removed in CIS benchmark for Windows Server 2022. |
| Ensure 'MSS: (AutoAdminLogon) Enable Automatic Logon (not recommended)' is set to 'Disabled' | CIS | Enabled | Unified ICM and Unified CVP 15.0(1) upgrade via Orchestration requires Automatic Logon to be enabled to control the upgrade
                                       remotely from Cloud Connect. Set this to Enabled only if Orchestration is used for Unified ICM or Unified CVP 15.0(1) upgrade. Post the upgrade, you can set this configuration
                                       to Disabled . |
| Ensure 'User Account Control: Behavior of the elevation prompt for administrators in Admin Approval Mode' is set to 'Prompt
                                       for consent on the secure desktop' | CIS | Elevate without prompting | Unified ICM and Unified CVP 15.0(1) upgrade via Orchestration requires Elevate without prompting to be set to control the upgrade remotely from Cloud Connect. Set this to Elevate without prompting only if Orchestration is used for Unified ICM or Unified CVP 15.0(1) upgrade. Post the upgrade, you can set this configuration
                                       to Prompt for consent on the secure desktop . |

| Note | This policy is removed in CIS benchmark for Windows Server 2022. |
|---|---|

| Policy | CIS/Microsoft Baseline | Recommended Setting | Remarks |
|---|---|---|---|
| Ensure 'Adjust memory quotas for a process' is set to
                                    'Administrators, LOCAL SERVICE, NETWORK SERVICE' | CIS | Administrators, Local Service, Network Service | IIS default user IIS Apppool\DefaultAppPool is
                                    added automatically to this policy after starting the IIS services.
                                    However, the CIS benchmark scans mark this policy as not compliant
                                    because of the presence of IIS default user. |
| Ensure 'Generate security audits' is set to 'LOCAL SERVICE, NETWORK
                                    SERVICE' | CIS | Local Service, Network Service | IIS default user IIS Apppool\DefaultAppPool is
                                    added automatically to this policy after starting the IIS services.
                                    However, the CIS benchmark scans mark this policy as not compliant
                                    because of the presence of IIS default user. |
| Ensure 'Replace a process level token' is set to 'LOCAL SERVICE,
                                    NETWORK SERVICE' | CIS | Local Service, Network Service | IIS default user IIS Apppool\DefaultAppPool is
                                    added automatically to this policy after starting the IIS services.
                                    However, the CIS benchmark scans mark this policy as not compliant
                                    because of the presence of IIS default user. |

| Note | The CIS benchmark versions 3.0.0 for Windows Server 2022, version 1.2.1 for Windows Server 2019, Microsoft baseline Windows Server 2019 version 1809,
                                             and latest Microsoft baseline Windows Server 2022 are validated. Before applying the higher version of CIS and Microsoft benchmark, analyze the additional policies introduced in the new
                                       version for the impact on ICM functionality and performance. We recommend the GPOs must be tailored according to your organization’s
                                       need. We recommend rolling out the GPOs to a small group of systems, preferably in a lab environment before rolling out into
                                       production. In addition to the GPO settings, disable the following settings in Windows Server: NetBIOS SMBv1 |
|---|---|

| Note | CCE software requires Windows PowerShell to be available and not blocked by Group Policy during installation, uninstallation,
                                       and upgrade processes of main releases, maintenance releases, and Engineering Specials (ES). Additionally, certain CCE tools
                                       depend on PowerShell and may invoke it dynamically at any time after the CCE software installation. Therefore, access to PowerShell
                                       must not be blocked post-installation. Ensure that Windows PowerShell execution is permitted and not restricted by Group Policy settings to avoid operational issues. |
|---|---|

| Service Name | Service Description | Default Service Startup Type | Disabled by ICM |
|---|---|---|---|
| CDPSvc | The service is used during connecting with Bluetooth devices and Printers, scanners, music players, mobile phones, cameras,
                                          etc. | Automatic | Yes |
| CDPUserSvc | Manages connections with devices like Bluetooth and Wi-Fi Direct. This service is used for Connected Devices and Universal
                                          Glass scenarios. | Automatic | Yes |
| DiagTrack | Customer Experience Improvement Program (CEIP) that collects and sends anonymized data to Microsoft. | Automatic | Yes |
| Spooler | This service spools print jobs and handles interaction with the printer. If you turn off this service, you can't print or
                                          see your printers. | Automatic | Yes |
| AJRouter | AllJoyn Router Service used for IOT. | Manual | Yes |
| bthserv | The Bluetooth service supports discovery and association of remote Bluetooth devices. | Manual | Yes |
| CaptureService | Enables optional screen capture functionality for applications that use Windows screen capture APIs. | Manual | Yes |
| CertPropSvc | Copies user certificates and root certificates from smart cards into the current user's certificate store, detects when a
                                          smart card is inserted into a smart card reader, and, if needed, installs the smart card Plug and Play minidriver. | Manual | Yes |
| DevicesFlowUserSvc | Allows the Connect user interface and Settings app to connect and pair with WiFi displays and Bluetooth devices. | Manual | Yes |
| DevQueryBroker | The DevQueryBroker service works by running a background task that periodically scans for devices. When it finds a new device,
                                          it sends a notification to all apps that have registered for device discovery events. | Manual | Yes |
| FrameServer | Enables multiple clients to access video frames from camera devices. | Manual | Yes |
| FrameServerMonitor | Monitors the status and health of Windows Camera Frame Server. | Manual | Yes |
| McpManagementService | Universal Print Management Service used to support remote printing. | Manual | Yes |
| PrintNotify | This service opens custom printer dialog boxes and handles notifications from a remote print server or a printer. | Manual | Yes |
| PrintWorkflowUserSvc | The PrintWorkflowUserSvc service in Windows supports applications that customize the printing workflow. This includes apps
                                          that alter the print content or print ticket, such as by adding watermarks, cropping margins, or applying filters. | Manual | Yes |
| RpcLocator | This is not used by latest Windows version, kept it for backward compatiblity of apps developed pre-Win2003. Remote Procedure
                                          Call (RPC) Locator service manages the RPC name service database. | Manual | Yes |
| SCardSvr | Manages access to smart cards read by this computer. If you stop this service, this computer becomes unable to read smart
                                          cards. | Manual | Yes |
| SCPolicySvc | Allows the system to be configured to lock the user desktop upon smart card removal. | Manual | Yes |
| SensorService | Manages the functionality of different sensors, including Simple Device Orientation (SDO) and History. Loads the SDO sensor
                                          that reports device orientation changes. | Manual | Yes |
| StiSvc | Provides image acquisition services for scanners and cameras. | Manual | Yes |
| TabletInputService | Service that optimizes Windows for tablet PCs with touch screens. | Manual | Yes |
| WbioSrvc | The Windows biometric service gives client applications the ability to capture, compare, manipulate, and store biometric data
                                          without gaining direct access to any biometric hardware or samples. | Manual | Yes |
| WMPNetworkSvc | The Windows Media Player Network Sharing Service (WMPNetworkSvc) shares Windows Media Player libraries to other media devices
                                          and networked players using Universal Plug and Play. | Manual | Yes |
| UnistoreSvc | Handles storage of structured user data, including contact info, calendars, messages, and other content. | Manual | Yes |
| WiaRpc | Launches applications associated with still image acquisition events. The WIA platform enables imaging/graphics applications
                                          to interact with imaging hardware and standardizes the interaction between different applications and scanners. This allows
                                          those different applications to talk to and interact with those different scanners without requiring the application writers
                                          and scanner manufactures to customize their application or drivers for each application-device combination. | Manual | Yes |