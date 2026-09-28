---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-installatio-c01a71bda6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/installation/guide/ucce_b_cti-os-system-manager-guide12-5/ucce_b_cti-os-system-manager-guide12-5_chapter_011.html
retrieved_at: 2026-08-16T20:07:03.038275+00:00
---

CTI OS System Manager Guide for Cisco Unified ICM, Release 12.5(1)

# CTI OS System Manager Guide for Cisco Unified ICM, Release 12.5(1)

Updated: February 6, 2020

Chapter: CTI Toolkit Desktop Client Installation

## Chapter: CTI Toolkit Desktop Client Installation

# CTI Toolkit Desktop Client Installation

## CTI Toolkit Desktop Client

The CTI Toolkit Desktop Client consists of the following components:

CTI Toolkit Desktop applications:

Agent desktop (including silent monitor)

UCCE Supervisor Desktop (including silent monitor)

Tools

CTI Toolkit SDK (previously the CTI OS Developer's Toolkit, including necessary files, controls, documentation, and samples
                                    needed to write custom applications):

Win32

Java

.NET

Before you begin installation, verify that your system meets the hardware and software requirements for the components that
                                          you plan to install. See the Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

For details on using Unified CCE in a virtualized environment, see the Virtualization for Unified Contact Center Enterprise at http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html .

## Install Cisco CTI
                        	 Toolkit Desktop Client Component

To install
                              		  the CTI Toolkit Desktop Client components, perform the following steps.

From the
                                       			 CTIOSClient directory on the CD, run Setscreenup.exe .

Click the Next button on the Welcome screen. The Software License Agreement screen appears.

Click the Yes button.

A window
                                          				displays the destination directory of the CTI Toolkit Desktop Client.

If you want to
                                                      				  change the destination directory, you must uninstall and reinstall the Cisco
                                                      				  CTI Toolkit Desktop Client Component.

Click OK .

Select the CTI
                                       			 Toolkit Desktop Client features that you want to install.

If you plan
                                                      				  to use the Silent Monitor Service, you must select at least one of the CTI
                                                      				  Toolkit Desktop Software components or the CTI Desktop SDK Win32 component.

Click Next .

Click Next .

If you select
                                          				CTI Toolkit Agent Desktop or CTI Toolkit UCCE Supervisor Desktop, the CTIOS
                                          				Server Information window appears.

Phones that
                                                      				  are configured to use SRTP cannot be silently monitored. Customers who wish to
                                                      				  silently monitor agents must not configure the agent phones to use SRTP.

Enter the Name
                                          				or IP Address and the Port Number for your CTI OS systems.

If you enable
                                                      				  the QoS checkbox during the CTI OS Server Installation, you must select the
                                                      				  checkbox at this stage.

The CVP Video Agent Desktop window appears. To enable the Cisco Voice Portal Video Agent Browser configuration, click the Enable CVP Video checkbox.

Click the Next button.

The Start
                                          				Copying Files window appears.

Click the Next button to begin installation.

After the
                                       			 installation is complete, the following window appears, prompting you to
                                       			 install the Security feature. For more information about CTI OS Security, see CTI OS Security .

For more
                                          				information about what Security Certificate option you must select, see CTI OS Security

Click OK .

The CTI OS Security InstallShield Wizard appears. Click Next .

While Security
                                          				is being configured, several status messages appear.

Lastly, the
                                       			 CTIOS Setup Completed dialog box appears.

Specify whether
                                       			 or not you want to restart your computer. Click the Finish button to exit Setup.

### Localization

Next, import the configLanguages.reg  registry, which is the registry file to configure language libraries for the CTI OS
                              Agent and Supervisor phones. The following example provides steps for setting the CTIOS desktop language to French Canadian.

Log out of the CTIOS desktop.

Open the Registry Editor.

Import the ConfigLanguages.reg from the location C:\Program Files (x86)\Cisco Systems\CTIOS Client\CTIOS Toolkit\Win32 CIL\Internationalization Kit\Languages .

Refresh the Registry Editor and navigate to HKEY_CURRENT_USER\Software\Cisco Systems, Inc.\CTI Desktop\Shared\Languages\<LAN> where <LAN> is the abbreviation for the language code. In this example it will be FRC , as this customer is setting a French Canadian Localization.

Set the value of the DLL Key using the following path: C:\Program Files (x86)\Cisco Systems\CTIOS Client\CTIOS Toolkit\Win32 CIL\Internationalization Kit\Languages\ctioslanguage.FRC.dll .

Set the value of the Language Code key to c0c  (Hexadecimal) .

Navigate to the HKEY_CURRENT_USER\Software\Cisco Systems, Inc.\CTI Desktop\Shared\Languages\Last Language and set the value of Language Code to c0c  (Hexadecimal) .

If the value Last Language key is not set, the CTIOS uses the default locale of the Windows operating system.

Re-launch the CTIOS client desktop.

### Installed
                           	 Files

When you
                                 		  install the CTI Toolkit Agent Desktop or the CTI Toolkit UCCE Supervisor
                                 		  Desktop, the CTI Toolkit installation process installs a number of dynamic link
                                 		  libraries (DLLs). The installation process registers many of these DLLs
                                 		  automatically, but you must manually register some of these DLLs to work
                                 		  correctly.

The
                                 		  following table lists the Windows DLLs that are installed with the CTI Toolkit
                                 		  Agent Desktop or the CTI Toolkit UCCE Supervisor Desktop, along with the
                                 		  command line entry for manually registering the DLL (if needed).

The
                                 		  following Softphone Controls DLLs are installed with the CTI Toolkit Agent
                                 		  Desktop or the CTI Toolkit UCCE Supervisor Desktop:

- AgentGreetingCtl.dll

- AgentSelectCtl.dll

- AgentStateCtl.dll

- AlternateCtl.dll

- AnswerCtl.dll

- Arguments.dll

- BadLineCtl.dll

- ButtonControl.dll

- ChatCtl.dll

- conferenceCtl.dll

- CtiCommonDlgs.dll

- CTIOSAgentStatistics.dll

- ChatCtl.dll

- CTIOSCallAppearance.dll

- CTIOSClient.dll

- CTIOSSessionResolver.dll

- CTIOSSkillGroupStatistics.dll

- CTIOSStatusBar.dll

- EmergencyAssistCtl.dll

- GridControl.dll

- HoldCtl.dll

- IntlResourceLoader.dll

- MakeCallCtl.dll

- ReconnectCtl.dll

- RecordCtl.dll

- SilentMonitorCtl.dll

- SubclassForm.dll

- SupervisorOnlyCtl.dll

- TransferCtl.dll

If the CTI
                                 		  Toolkit Agent Desktop or the CTI Toolkit UCCE Supervisor Desktop indicate that
                                 		  a given DLL is not registered, you can manually register the DLL by using the
                                 		  following command:

regsvr32 <DLL
                                    			 filename>

For
                                 		  example, you can register CtiosStatusbar.dll by using the following command:

regsvr32
                                    			 CtiosStatusbar.dll

With
                                 		  interoperability, the Win32 COM controls work under the .NET framework. The
                                 		  installation lays down the following files and installs them into the Global
                                 		  Access Cache (GAC):

AxInterop.AgentSelectCtl.dll

Cisco.CTICOMMONDLGSLib.dll

Interop.AgentSelectCtl.dll

AxInterop.AgentStateCtl.dll

Cisco.CTIOSARGUMENTSLib.dll

Interop.AgentStateCtl.dll

AxInterop.AlternateCtl.dll

Cisco.CTIOSCLIENTLib.dll

Interop.AlternateCtl.dll

AxInterop.AnswerCtl.dll

Cisco.CTIOSSESSIONRESOLVERLib.dll

Interop.AnswerCtl.dll

AxInterop.BadLineCtl.dll

Cisco.INTLRESOURCELOADERLib.dll

Interop.BadLineCtl.dll

AxInterop.ButtonControl.dll

Interop.ButtonControl.dll

AxInterop.ChatCtl.dll

Interop.ChatCtl.dll

AxInterop.ConferenceCtl.dll

Interop.ConferenceCtl.dll

AxInterop.CTIOSAgentStatistics.dll

Interop.CTIOSAgentStatistics.dll

AxInterop.CTIOSCallAppearance.dll

Interop.CTIOSCallAppearance.dll

AxInterop.CTIOSSkill GroupStatistics.dll

Interop.CTIOSSkill GroupStatistics.dll

AxInterop.CTIOSStatusBar.dll

Interop.CTIOSStatusBar.dll

AxInterop.EmergencyAssistCtl.dll

Interop.EmergencyAssistCtl.dll

AxInterop.GridControl.dll

Interop.GridControl.dll

AxInterop.HoldCtl.dll

Interop.HoldCtl.dll

AxInterop.MakeCallCtl.dll

Interop.MakeCallCtl.dll

AxInterop.ReconnectCtl.dll

Interop.ReconnectCtl.dll

AxInterop.RecordCtl.dll

Interop.RecordCtl.dll

AxInterop.SilentMonitorCtl.dll

Interop.SilentMonitorCtl.dll

AxInterop.SubclassForm.dll

Interop.SubclassForm.dll

AxInterop.SupervisorOnlyCtl.dll

Interop.SupervisorOnlyCtl.dll

AxInterop.TransferCtl.dll

Interop.TransferCtl.dll

AxInterop.AgentGreetingCtl.dll

Interop.SHDocVw.dll

## Uninstall CTI Toolkit

To uninstall the CTI Toolkit, run Add/Remove programs from the Windows Control
                              		  Panel and select Cisco CTI Toolkit Uninstall .

## Determine Version
                        	 Number of Installed CTI Toolkit Files

If the CTI
                              		  Toolkit Agent Desktop or the CTI Toolkit Supervisor Desktop for UCCE are
                              		  currently running, the title bars of the desktop windows display the CTI
                              		  Toolkit version number.

If these
                              		  desktops are not currently
                              		  running, you can determine the version number of an installed CTI Toolkit file
                              		  by performing the following steps.

Go to the
                                       			 directory:

Highlight, and
                                       			 then right-click the ctiosclient.dll file.

Select Properties from the drop-down menu.

The Properties
                                          				dialog box appears.

Select the Version tab.

This tab
                                          				contains version information (release number and build number) for the file.

## Unified CM Intercept Configuration Requirement

You must set the Cisco Unified CM service parameter named Drop Ad Hoc Conference to "never" (the default value), otherwise during the Intercept function, all the parties in the call get dropped.

## Configure Supervisory Assistance Features

The CTI Toolkit Agent Desktop includes buttons that enable
                              		  an agent to make an emergency call to a supervisor or to place a call to
                              		  request assistance from a supervisor. To enable the functionality for these
                              		  buttons, a Unified ICM system administrator must perform the following
                              		  steps.

Perform the following tasks from the Unified ICM Configuration Manager
                                       			 (for more information, see Configuration Guide for Cisco Unified ICM/Contact Center Enterprise ).

On the Dialed Number List screen, create a Dialed Number for the supervisor.

On the Agent Team List screen, enter the Dialed Number in the Supervisor script dialed number field.

Perform the following task from the Script Editor (for more information, see Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise ).

On the Call Type Manager screen, associate the Dialed Number with your script.

| Note | Before you begin installation, verify that your system meets the hardware and software requirements for the components that
                                          you plan to install. See the Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html . For details on using Unified CCE in a virtualized environment, see the Virtualization for Unified Contact Center Enterprise at http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html . |
|---|---|

| Step 1 | From the
                                       			 CTIOSClient directory on the CD, run Setscreenup.exe . |
|---|---|
| Step 2 | Click the Next button on the Welcome screen. The Software License Agreement screen appears. |
| Step 3 | Click the Yes button. A window
                                          				displays the destination directory of the CTI Toolkit Desktop Client. Note If you want to
                                                      				  change the destination directory, you must uninstall and reinstall the Cisco
                                                      				  CTI Toolkit Desktop Client Component. | Note | If you want to
                                                      				  change the destination directory, you must uninstall and reinstall the Cisco
                                                      				  CTI Toolkit Desktop Client Component. |
| Note | If you want to
                                                      				  change the destination directory, you must uninstall and reinstall the Cisco
                                                      				  CTI Toolkit Desktop Client Component. |
| Step 4 | Click OK . The Select
                                          				Features window appears. |
| Step 5 | Select the CTI
                                       			 Toolkit Desktop Client features that you want to install. Note If you plan
                                                      				  to use the Silent Monitor Service, you must select at least one of the CTI
                                                      				  Toolkit Desktop Software components or the CTI Desktop SDK Win32 component. | Note | If you plan
                                                      				  to use the Silent Monitor Service, you must select at least one of the CTI
                                                      				  Toolkit Desktop Software components or the CTI Desktop SDK Win32 component. |
| Note | If you plan
                                                      				  to use the Silent Monitor Service, you must select at least one of the CTI
                                                      				  Toolkit Desktop Software components or the CTI Desktop SDK Win32 component. |
| Step 6 | Click Next . The
                                       			 IMPORTANT NOTE window appears. |
| Step 7 | Click Next . If you select
                                          				CTI Toolkit Agent Desktop or CTI Toolkit UCCE Supervisor Desktop, the CTIOS
                                          				Server Information window appears. Note Phones that
                                                      				  are configured to use SRTP cannot be silently monitored. Customers who wish to
                                                      				  silently monitor agents must not configure the agent phones to use SRTP. Enter the Name
                                          				or IP Address and the Port Number for your CTI OS systems. Note If you enable
                                                      				  the QoS checkbox during the CTI OS Server Installation, you must select the
                                                      				  checkbox at this stage. | Note | Phones that
                                                      				  are configured to use SRTP cannot be silently monitored. Customers who wish to
                                                      				  silently monitor agents must not configure the agent phones to use SRTP. | Note | If you enable
                                                      				  the QoS checkbox during the CTI OS Server Installation, you must select the
                                                      				  checkbox at this stage. |
| Note | Phones that
                                                      				  are configured to use SRTP cannot be silently monitored. Customers who wish to
                                                      				  silently monitor agents must not configure the agent phones to use SRTP. |
| Note | If you enable
                                                      				  the QoS checkbox during the CTI OS Server Installation, you must select the
                                                      				  checkbox at this stage. |
| Step 8 | The CVP Video Agent Desktop window appears. To enable the Cisco Voice Portal Video Agent Browser configuration, click the Enable CVP Video checkbox. |
| Step 9 | Click the Next button. The Start
                                          				Copying Files window appears. |
| Step 10 | Click the Next button to begin installation. |
| Step 11 | After the
                                       			 installation is complete, the following window appears, prompting you to
                                       			 install the Security feature. For more information about CTI OS Security, see CTI OS Security . For more
                                          				information about what Security Certificate option you must select, see CTI OS Security |
| Step 12 | Click OK . The CTI OS Security InstallShield Wizard appears. Click Next . While Security
                                          				is being configured, several status messages appear. |
| Step 13 | Lastly, the
                                       			 CTIOS Setup Completed dialog box appears. |
| Step 14 | Specify whether
                                       			 or not you want to restart your computer. Click the Finish button to exit Setup. |

| Note | If you want to
                                                      				  change the destination directory, you must uninstall and reinstall the Cisco
                                                      				  CTI Toolkit Desktop Client Component. |
|---|---|

| Note | If you plan
                                                      				  to use the Silent Monitor Service, you must select at least one of the CTI
                                                      				  Toolkit Desktop Software components or the CTI Desktop SDK Win32 component. |
|---|---|

| Note | Phones that
                                                      				  are configured to use SRTP cannot be silently monitored. Customers who wish to
                                                      				  silently monitor agents must not configure the agent phones to use SRTP. |
|---|---|

| Note | If you enable
                                                      				  the QoS checkbox during the CTI OS Server Installation, you must select the
                                                      				  checkbox at this stage. |
|---|---|

| Note | If the value Last Language key is not set, the CTIOS uses the default locale of the Windows operating system. |
|---|---|

| AxInterop.AgentSelectCtl.dll | Cisco.CTICOMMONDLGSLib.dll | Interop.AgentSelectCtl.dll |
|---|---|---|
| AxInterop.AgentStateCtl.dll | Cisco.CTIOSARGUMENTSLib.dll | Interop.AgentStateCtl.dll |
| AxInterop.AlternateCtl.dll | Cisco.CTIOSCLIENTLib.dll | Interop.AlternateCtl.dll |
| AxInterop.AnswerCtl.dll | Cisco.CTIOSSESSIONRESOLVERLib.dll | Interop.AnswerCtl.dll |
| AxInterop.BadLineCtl.dll | Cisco.INTLRESOURCELOADERLib.dll | Interop.BadLineCtl.dll |
| AxInterop.ButtonControl.dll |  | Interop.ButtonControl.dll |
| AxInterop.ChatCtl.dll |  | Interop.ChatCtl.dll |
| AxInterop.ConferenceCtl.dll |  | Interop.ConferenceCtl.dll |
| AxInterop.CTIOSAgentStatistics.dll |  | Interop.CTIOSAgentStatistics.dll |
| AxInterop.CTIOSCallAppearance.dll |  | Interop.CTIOSCallAppearance.dll |
| AxInterop.CTIOSSkill GroupStatistics.dll |  | Interop.CTIOSSkill GroupStatistics.dll |
| AxInterop.CTIOSStatusBar.dll |  | Interop.CTIOSStatusBar.dll |
| AxInterop.EmergencyAssistCtl.dll |  | Interop.EmergencyAssistCtl.dll |
| AxInterop.GridControl.dll |  | Interop.GridControl.dll |
| AxInterop.HoldCtl.dll |  | Interop.HoldCtl.dll |
| AxInterop.MakeCallCtl.dll |  | Interop.MakeCallCtl.dll |
| AxInterop.ReconnectCtl.dll |  | Interop.ReconnectCtl.dll |
| AxInterop.RecordCtl.dll |  | Interop.RecordCtl.dll |
| AxInterop.SilentMonitorCtl.dll |  | Interop.SilentMonitorCtl.dll |
| AxInterop.SubclassForm.dll |  | Interop.SubclassForm.dll |
| AxInterop.SupervisorOnlyCtl.dll |  | Interop.SupervisorOnlyCtl.dll |
| AxInterop.TransferCtl.dll |  | Interop.TransferCtl.dll |
| AxInterop.AgentGreetingCtl.dll |  | Interop.SHDocVw.dll |

| Step 1 | Go to the
                                       			 directory: Program Files\Cisco
                                          				Systems\CTIOS Client\CTIOS Toolkit\Win32 CIL\COM Servers and Activex
                                          				Controls |
|---|---|
| Step 2 | Highlight, and
                                       			 then right-click the ctiosclient.dll file. |
| Step 3 | Select Properties from the drop-down menu. The Properties
                                          				dialog box appears. |
| Step 4 | Select the Version tab. This tab
                                          				contains version information (release number and build number) for the file. |

| Step 1 | Perform the following tasks from the Unified ICM Configuration Manager
                                       			 (for more information, see Configuration Guide for Cisco Unified ICM/Contact Center Enterprise ). On the Dialed Number List screen, create a Dialed Number for the supervisor. On the Agent Team List screen, enter the Dialed Number in the Supervisor script dialed number field. |
|---|---|
| Step 2 | Perform the following task from the Script Editor (for more information, see Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise ). On the Call Type Manager screen, associate the Dialed Number with your script. |