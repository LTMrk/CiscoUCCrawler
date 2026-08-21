---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-cisco-vvb-vvb-15-0-1-adminconfig-guide-ccvb-b-15-fc2d331673
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/cisco_vvb/vvb_15_0_1/adminconfig/guide/ccvb_b_150_cisco-virtualized-voice-browser-administration-and-configuration-guide/cisco_vvb_configuration.html
retrieved_at: 2026-08-21T16:30:19.628040+00:00
---

Cisco Virtualized Voice Browser Administration and Configuration Guide, Release 15.0(1)

# Cisco Virtualized Voice Browser Administration and Configuration Guide, Release 15.0(1)

Updated: December 12, 2025

Chapter: Cisco VVB
	 Configuration

## Chapter: Cisco VVB
	 Configuration

# Cisco VVB
                     	 Configuration

## Configure Cisco VVB on Unified CVP

For detailed instructions on how to configure Cisco VVB on Unified CVP, see Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html .

After successfully adding Cisco VVB on Unified CVP, ensure to restart Operations Console service and Web Services Manager
                                          service.

Cisco VVB does not support clustering. Therefore, you may ignore any message on the Cisco VVB Admin UI/CLI that refers to cluster , publisher , subscriber , etc.

## Configure Cisco
                        	 VVB Call Flow

Cisco VVB
                              		  provides the standard list of scripts that require you to configure for the
                              		  Unified CVP call flow to work. The primary steps are to create application and
                              		  assign corresponding SIP trigger.

Log in to Cisco
                              		  VVB Administration Console and follow these tasks:

Step 1

Create an
                                       			 application to define the call flow through the scripts.

To configure
                                          				standalone application, see Configure Cisco VVB Settings for Standalone Call Flow Model .

To configure
                                          				comprehensive and ringtone application, see Configure Cisco VVB Settings for Comprehensive Call Flow Model .

To configure
                                          				error application, see Configure Error Application .

Step 2

Create
                                       			 triggers to invoke an application using the incoming directory number.

To configure
                                          				the trigger, see Configure SIP Triggers .

Step 3

Cisco VVB can
                                       			 play recorded audio prompts and detect DTMF tones. To recognize speech and play
                                       			 text, configure Automatic Speech Recognition (ASR) and Text-To-Speech (TTS).

To configure
                                          				ASR and TTS, see Configure Speech Servers .

Step 4

Manage prompt
                                       			 files to add custom ringtone for comprehensive call flow or to use custom
                                       			 prompts.

To configure
                                          				and manage prompts, see Configure Prompt Management .

## Configure Cisco
                        	 VVB Settings for Standalone Call Flow Model

Step 1

From Cisco VVB Administration menu bar, choose Applications > Application Management .

Step 2

Click the Add
                                          				New icon that is displayed in the toolbar in the upper left corner
                                       			 of the window or the Add
                                          				New button that is displayed at the bottom of the window.

Step 3

Type the application name in the Name field.

This number must not exceed the maximum number of ports supported for Cisco VVB profile. For more information, see Virtualization for Cisco Virtualized Voice Browser available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-virtualized-voice-browser.html .

Step 4

Select the SelfService.aef script from the drop-down list for a standalone application.

The following table describes the parameters:

Parameter

Description

Default

Base Type

Application Name

"HelloWorld"

Port

Ports 7000/7443 must be configured for interworking with CVP Release 11.5 and later. For earlier versions of CVP, configure
                                                                  ports 8000/8443.

"7000"

PrimaryVXMLServer

""

BackupVXMLServer

""

Secured

Change the port number in the above field to 7443.

Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Cisco Unified Communications Operating System Administration Guide.

Restart Tomcat server and Engine from command line.

false

Step 5

Use the Tab key to automatically populate the Description field.

Step 6

Enable the
                                       			 application by selecting the radio button. You can choose to disable the
                                       			 application to retain the configurations for later use.

Step 7

Click Add .

The Cisco Script Application page refreshes and the Add New Trigger hyperlink appears in the left navigation bar. The following message is displayed in the status bar on top:

The operation has been
                                             				  executed successfully.

Step 8

Create a
                                       			 trigger using the Add
                                          				New Trigger hyperlink or follow the procedure Configure SIP Triggers .

## Configure Cisco
                        	 VVB Settings for Comprehensive Call Flow Model

This topic provides information about comprehensive and ringtone applications.

Cisco VVB is prepopulated with comprehensive application (also called bootstrap) and the ringtone application.

To create a custom comprehensive (CVP/VRU comprehensive) or ringtone application, follow the steps:

Step 1

From Cisco VVB Administration menu bar, choose Applications > Application Management .

Step 2

Click Add
                                          				New .

Step 3

(Mandatory)
                                       			 Type the application name in the Name field.

Step 4

The Maximum Number of Sessions field is prepopulated based on the OVA profile. You can edit this field.

This number must not exceed the maximum number of ports supported for Cisco VVB profile. For more information, see Virtualization for Cisco Virtualized Voice Browser available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-virtualized-voice-browser.html .

Step 5

Select the
                                       			 script from the drop-down list.

CVPComprehensive.aef (bootstrap)

Ringtone.aef

The
                                          				  following table describes the parameters:

Parameter

Description

Default

Base Type

Secured

Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Cisco Unified Communications Operating System Administration Guide.

Restart Tomcat server and Engine from command line.

If you are using a coresident VXML and Call Server, use CA-signed certificate.

Boolean

Sigdigit

Enable this parameter to use Significant Digits feature. Enter the number of digits that are used as sigdigit. When Cisco
                                                      VVB receives the call, the CVP comprehensive service is configured to strip the digits. When the IVR leg of the call is set
                                                      up, the original label is used on the incoming VoiceXML request.

0

Numeric

Step 6

Use the Tab key to automatically populate the Description field.

Step 7

Enable the
                                       			 application by selecting the radio button. You can choose to disable the
                                       			 application to retain the configurations for later use.

Step 8

Click Add .

The Cisco Script Application page refreshes and the Add New Trigger hyperlink appears in the left navigation bar. The following message is displayed in the status bar on top:

The operation has been
                                             				  executed successfully.

Step 9

Create a
                                       			 trigger using the Add
                                          				New Trigger hyperlink or follow the procedure Configure SIP Triggers .

## Configure Cisco
                        	 VVB Settings for VRU-Only Call Flow Model

This topic
                              		  provides information to create VRU-Only applications.

Use the VRUComprehensive.aef script if your CVP implementation needs
                              		  to support non-reference VRU call flows or VRU-Only call flows. For more
                              		  details on non-reference call flows, see Solution
                                 			 Design Guide for Cisco Unified Contact Center Enterprise.

To support the
                              		  comprehensive call flow in addition to the non-reference VRU call flows, add
                              		  relevant options to this script. The CVPComprehensive script must not be separately configured to
                              		  handle a mixed implementation.

To create a
                              		  VRU-Only application, follow the steps:

Step 1

From Cisco VVB
                                       			 Administration menu bar, choose Applications > Application
                                             				  Management .

Step 2

Click Add
                                          				New .

Step 3

(Mandatory)
                                       			 Type the application name in the Name field.

Step 4

The Maximum Number of Sessions field is prepopulated
                                       			 based on the OVA profile. You can edit this field.

This number must not exceed the maximum number of ports supported for Cisco VVB profile. For more information, see Virtualization for Cisco Virtualized Voice Browser available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-virtualized-voice-browser.html .

Step 5

From the Script drop-down list, select the VRUComprehensive.aef script.

Parameter

Description

Default

Base
                                                      							 Type

PrimaryVXMLServer

VXML server or load balancer IP address

""

Alphanumeric

BackupVXMLServer

VXML backup server or load balancer IP address

""

Alphanumeric

Port

Port on which VXML server or load balancer is running.

Ports 7000/7443 must be configured for interworking with CVP Release 11.5 and later.

"7000"

Numeric

Secured

If
                                                      							 enabled, HTTPS is used while fetching VXML application from Unified CVP. By
                                                      							 default, Secured is not enabled.

Change the port number to 7443.

Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Configuration Guide for Cisco Unified Customer Voice
                                                                           										Portal.

Restart Tomcat server and engine from command line.

If you are using a co-resident VXML and Call Server, use a
                                                                        									 CA-signed certificate.

false

Boolean

Sigdigit

Enable this parameter to use Significant Digits feature. Enter
                                                      							 the number of digits that are used as sigdigit. When Cisco VVB receives a call,
                                                      							 the VRU comprehensive service is configured to strip the digits. When the IVR
                                                      							 leg of the call is set up, the original label is used on the incoming VoiceXML
                                                      							 request.

0

Numeric

Step 6

Use the Tab
                                       			 key to automatically populate the Description field.

Step 7

Enable the
                                       			 application by selecting the radio button. You can choose to disable the
                                       			 application to retain the configurations for later use.

Step 8

Click Add .

Cisco Script
                                          				Application page refreshes. The Add
                                             				  New Trigger hyperlink appears in the left navigation bar. The
                                          				following message is displayed in the status bar on top:

The operation has been
                                             				  executed successfully.

Step 9

Create a
                                       			 trigger using the Add
                                          				New Trigger hyperlink or follow the procedure Configure SIP Triggers .

## Configure Error
                        	 Application

To create a
                              		  comprehensive application, follow the steps:

Step 1

From Cisco VVB Administration menu bar, choose Applications > Application Management .

Step 2

Click Add
                                          				New .

Step 3

Type the application name in the Name field.

This number must not exceed the maximum number of ports supported for Cisco VVB profile. For more information, see Virtualization for Cisco Virtualized Voice Browser available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-virtualized-voice-browser.html .

Step 4

Select the Error.aef script from the drop-down list. This script is used to play error tone.

The following table describes the parameter details:

Parameter

Default

Base Type

CVPErrorPrompt —Select and associate custom wav file from VVB application.

To override system default wav file, upload custom wav file from Prompt Management menu.

You can upload custom wav files only for Error.aef script.

Step 5

Use the Tab key to automatically populate the Description field.

Step 6

Enable the
                                       			 application by selecting the radio button. You can choose to disable the
                                       			 application to retain the configurations for later use.

Step 7

Click Add .

Cisco Script Application page is refreshed and the Add New Trigger hyperlink appears in the left navigation bar. The following message is displayed in the status bar on top:

The operation has been
                                             				  executed successfully.

Step 8

Create a
                                       			 trigger using the Add
                                          				New Trigger hyperlink or follow the procedure Configure SIP Triggers .

## Configure SIP
                        	 Triggers

An SIP trigger responds to calls that arrive on a specific route point and uses telephony and media resources to complete
                           the call and to invoke the application script.

You must add SIP triggers to invoke Cisco applications in response to incoming contacts.

### Add SIP
                           	 Trigger

To add an SIP trigger:

Step 1

From Cisco VVB Administration menu bar, choose Subsystems > SIP Telephony > SIP Triggers .

Step 2

Click Add New and enter the following fields:

Field

Description

Directory Information

Dial Number Pattern

A unique phone number. The value includes digits and optionally includes " * " to mask multiple digits.

Examples of valid Directory Numbers: 9191*

Examples for valid triggers:

10.919191 where 10. is the same as 101, 102

*12* or 12*23 where *12* is the same as "*" and 12*23 is the same as 12*

The trigger cannot contain only a wildcard character (*). If it contains *, it must also contain numbers.

Capital letter "X" can be used as a wildcard, but small letter "x" cannot be used.

Trigger Information

Application Name

From the drop-down list, choose the application to associate with the trigger.

Advanced Trigger Information (available only if you click Show More )

Enabled

Click a radio button to choose the required option:

Yes— Enable the trigger (default)

No— Disable the trigger

Idle Timeout (in ms)

The number of milliseconds (ms) the system waits before rejecting the SIP request for this trigger.

Override Media Termination

Click a radio button to choose the required options:

Yes— Override media termination.

No— Enable media termination (default).

If you select Yes, two panes open:

Selected Dialog Groups — displays the default or selected group.

You must not change the default Selected Dialog Group associated with the application.

- Available Dialog Groups — displays the configured dialog.

Description

Click the Tab key to populate it.

## Configure SIP
                        	 Properties

Cisco VVB does not send 180 Ringing Provisional Response for an incoming SIP INVITE. To enable SIP 180 Ringing Provisional
                              Response:

Step 1

From the Cisco VVB Administration menu bar, choose Subsystems > SIP Telephony > SIP Properties .

Step 2

Select the Enable radio button and click Update .

## Configure SIP
                        	 RAI

The Resource
                              		  Available Indication (RAI) feature supports:

Monitoring of CPU and memory resources

Reporting of
                                    				VVB resource status to an externally configured device

To configure RAI to a server:

Step 1

From the Cisco VVB Administration menu bar, choose Subsystems > SIP Telephony > SIP RAI .

Step 2

On the SIP RAI Configuration page, click Add New .

Step 3

Enter the
                                       			 following fields:

Field

Default Value / Range

Description

Server Name

Hostname or IP address of SIP server.

Port

5060

Range: 1 to 65535

SIP server port number for communication.

Interval

60

Range: 30 to 86400 (in seconds)

Interval time to send RAI reports.

Step 4

Click Add to add a SIP server.

Step 5

(Optional) To update a server port or interval time, click the server name and update the Port and Interval fields.

Step 6

(Optional) To delete a server, click the Delete icon present on the SIP RAI List or from the update server page.

## Configure Speech
                        	 Servers

Only G711 codec is supported for ASR and TTS integrations.

### Prepare to
                           	 Provision ASR/TTS

The
                              		customer must perform the following tasks:

For more information about supported speech servers for Cisco VVB, see the Solutions Compatibility Matrix available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

- Work with the ASR and TTS
                                 		  vendor to size the solutions.

- Provision, install, and
                                 		  configure the ASR and TTS vendor software on a different server (in the same
                                 		  LAN) and not where the Cisco VVB runs.

### Provision ASR
                           	 Servers

Use the Automatic Speech Recognition Server Configuration web page to specify information about the speech server name and
                                 port location.

Step 1

From the Cisco VVB Administration menu bar, choose Subsystems > Speech Servers > ASR Servers .

Column

Description

Server Name

Hostname or IP address of the ASR server.

ASR server deployment over WAN is not supported in Cisco VVB. Place the ASR server in the same LAN as Cisco VVB. You need
                                                                     to specify the ASR server hostname or IP address that is local with Cisco VVB node while installing the ASR server software
                                                                     in this field.

Port

Port number used to connect to a Speech server.

Status

Status or state of the server.

Step 2

Click the Add New button to provision a new ASR Server.

Step 3

Enter the following fields:

Field

Description

Server Name

Hostname or IP address of the ASR server.

Port Number

Port numbers that are used to connect to a Speech server. The default value for MRCPv1 is 4900 and for MRCPv2 is 5060.

Step 4

Click Add to apply the changes.

Step 5

(Optional)
                                          			 Click the Refresh button to refresh the status of the server.

### Provision TTS
                           	 Servers

Use the Text-to-Speech Server Configuration web page to configure the TTS server name and port location.

Step 1

From the Cisco VVB Administration menu bar, choose Subsystems > Speech Servers > TTS Servers .

The TTS Server Configuration web page opens displaying a list of previously configured servers, if applicable, with the following
                                             information:

Column

Description

Server Name

Hostname or IP address of the TTS server.

TTS server deployment over WAN is not supported in Cisco VVB. In other words, the TTS servers must be in the same LAN as Cisco
                                                                     VVB. Therefore, you need to specify the TTS server hostname or IP address that is local with Cisco VVB node while installing
                                                                     the TTS server software in this field.

Port Number

Port number used to connect to a Speech server.

Status

Status or state of the server.

Step 2

Click the Add New button to provision a new TTS Server.

Step 3

Enter the following fields:

Field

Description

Server Name

Hostname or IP address of the TTS server.

Port Number

Port number used to connect to a TTS server. The default value for MRCPv1 is 4900 and for MRCPv2 is 5060.

If the administrator has configured any other the port value for MRCP/TTS servers then use the same port value here, do not
                                                                     use these default values.

Whenever the administrator changes from MRCP protocol, ensure TTS server are deleted and recreated with appropriate port values.

Step 4

Click Add to apply the changes.

Step 5

(Optional) Click the Refresh button to refresh the status of the server.

## Configure Prompt
                        	 Management

Several system-level prompt files are loaded during Cisco VVB installation. However, any file you create must be available
                              to the Cisco VVB Engine before the Cisco VVB application can use it. Files are made available through the Cisco VVB Repository
                              datastore, where the prompt files are created, stored, and updated.

Use Prompt Management to store prompt WAV files locally. It helps you avoid any fetch latency while playing the large prompt.
                                          You can also use it to override the system default prompts.

### Manage Prompt
                           	 Files

Many applications make
                                 		  use of prerecorded prompts. These are stored as .wav or .au files,
                                 		  and are played back to the callers to provide information and elicit caller
                                 		  response.

To access
                                 		  the Prompt Management page:

Step 1

From Cisco
                                          			 VVBAdministration menu bar, choose Applications > Prompt
                                                				  Management .

Step 2

The Prompt Management page opens to display the
                                          			 following fields.

Field

Description

Name

Name
                                                         							 of the folder.

Size

This column is usually blank on the root page because the items
                                                                        								  on this page are usually folders.

The maximum limit for the uploaded prompt file is 20MB.

Date
                                                         							 Modified

The date and time when the document was last uploaded or changed along with the time zone.

Modified By

The user ID of the person who made these modifications.

Delete

To
                                                         							 remove the folder and its contents from the repository.

Rename

To
                                                         							 rename the folder in the repository.

Refresh

To
                                                         							 refresh the folder in the repository.

Create New Folder

To create a new subfolder.

Upload Prompt

To upload a prompt (.wav/.au) file or prompts packaged in a zip.

The maximum limit for the uploaded prompt file is 20MB.

### Local Audio Files
                           	 Stored on VVB

#### Local Audio
                                 		  Files Stored on VVB

Local audio files
                                 		  that are uploaded to default prompt folder of VVB can be accessed by setting
                                 		  the audio source path starting with "flash:" in microapps or VXML application.
                                 		  The audio files must be pre-uploaded to default folder.

Example : "flash:holdmusic.wav"

If you are creating a custom folder in prompt management and uploading an audio file, then mention the folder name in the
                                 URL.

Example : flash:/<folder_name>/<file_name>

### Overriding Default Ringtone using CVP

Follow these
                                 		  steps to override default ringtone:

Go to System > Dialed Number
                                             					 Pattern .

From the
                                       				listed patterns, click Pattern for which custom ringtone needs to be added.

From Dialed Number Pattern Types , check the Enable Custom Ringtone check box.

Specify the
                                       				custom ringtone filename in the text box.

Custom
                                                         						ringtone cannot be named to ringback.wav.

The
                                                         						audio file in Cisco VVB and the filename you entered in CVP under DNP is
                                                         						case-sensitive (should be same with .wav extension)

## Configure System
                        	 Parameters

Use the
                              		  System Parameters web page to configure system parameters such as port settings
                              		  and locale settings and to default session timeout.

The
                              		  parameters in the System Parameters Configuration page are grouped logically
                              		  into sections with headings. Each parameter has a corresponding suggested or
                              		  default value on the right side of the page. Where applicable, radio buttons
                              		  are used to toggle between the parameter options.

Choose System > SystemParameters from the Cisco VVB
                              		  Administration menu bar to access the System Parameters Configuration web page.

### Manage System
                           	 Parameters

On System Parameters page, you can configure basic system settings such as Audio Codec, MRCP version,TLS (SIP), and other
                                 parameters.

This release supports only TLS 1.2. For more information, see Contact Center Enterprise Solution Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/tsd-products-support-series-home.html .

Step 1

From Cisco VVB
                                          			 Administration menu bar, choose System > SystemParameters .

Step 2

To update,
                                          			 click the Update icon in the toolbar or the Update button at the bottom of the window.

The
                                             				System Parameters Configuration web page displays the following fields.

Generic System
                                                            							 Parameter

System Time Zone

The
                                                         						  system time zone of Cisco VVB server configured during installation.

Media Parameters

Codec

G711 and G729 audio
                                                         						  codecs with sampling rate 8K are supported.

Default: G711U

MRCP
                                                         						  Version

Select the MRCP version to communicate between Nuance and Cisco VVB.

Default: MRCPv2

The default value for ASR/TTS server port for MRCPv1 is 4900 and for MRCPv2 is 5060. Whenever the administrator changes from
                                                                           MRCP protocol, ensure ASR/TTS server is deleted and re-created with appropriate port values.

ASR-TTS service is not supported using G729 codec; therefore,
                                                                           								  MRCP is not applicable.

User
                                                         						  Prompts override System Prompts

When
                                                         						  enabled, custom recorded prompt files can be uploaded to the appropriate
                                                         						  language directory under Prompt Management . The custom prompts override the
                                                         						  system default prompt files for that language. By default, this feature is
                                                         						  disabled.

For overriding the system default prompt files for ringtone
                                                                     							 application:

Create a new folder named vb . Select Applications > Prompt Management and click Create New Folder .

Upload the custom ringtone. Choose Applications > Prompt Management and click Upload Prompt . Upload custom ringtone wav file(named same as ringback.wav ) under folder vb .

Security Parameters

TLS(SIP)

TLS (SIP) is disabled by default. When enabled, this setting secures SIP signaling on the IVR leg.  TLS (SIP) version supported
                                                         is TLSv1.2, and the default cipher suites are TLS_RSA_WITH_AES_128_CBC_SHA and TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 .

Multiple clients connecting to Cisco VVB cannot combine RSA and ECDHE cipher suites. They must use either RSA or ECDHE cipher
                                                                     suites.

SSL certificates need to be exchanged between VVB and any SIP endpoint (CVP, Ingress Gateway, and so on.) to talk over TLS.
                                                         For more details on this configuration, see the Upgrade Unified CVP > Postupgrade Tasks > Manual Configuration of Unified CVP Properties section in the Installation and Upgrade Guide for Cisco Unified Customer Voice Portal , Release 15.0(1) available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html .

Cisco VVB Engine restart is required after a change to this configuration.

Supported TLS (SIP) Versions

This allows you to select the version of TLS (SIP). TLS (SIP) version supported is TLSv1.2.

When
                                                         						  you select a given TLS (SIP) version, Cisco VVB will support SIP TLS requests
                                                         						  for this version and the higher supported versions.

Supported TLS (SIP) Versions is available only if TLS (SIP) is
                                                                           								  enabled.

Cisco VVB Engine restart is required after a change to this
                                                                           								  configuration.

The supported TLS (SIP) versions as client or server for securing SIP signaling in the IVR leg can alternatively be specified
                                                                           via the CLI command set tls server min-version as documented in the Cisco Unified Contact Center Express Administration and Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-installation-and-configuration-guides-list.html

Cipher Configuration

This field defines the ciphers that are supported by Cisco VVB with key size lesser than or equal to 2048 bits.

The following ciphers are pre-populated.

TLS_RSA_WITH_AES_128_CBC_SHA

TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256

Cipher configuration is available only if TLS (SIP) is enabled.

You must restart the Cisco VVB engine after modifying the cipher configuration.

If you are using CUBE version 16.6 and higher, you must manually change the crypto suite to 128/256 by enabling CLI on the dial-peer towards VVB as shown:

```
voice class srtp-crypto 1
	crypto 1 AES_CM_128_HMAC_SHA1_32

dial-peer voice xxxx voip (Dial-peer to VVB srtp)
    ...
    voice-class sip srtp-crypto 1
```

To avoid any unsupported cipher issues during the upgrade to Cisco Unified CVP Release 15.0, it is recommended to restart
                                                                     the Cisco VVB engine to ensure a smooth and successful cipher negotiation process.

SRTP

SRTP is disabled by default. When SRTP is disabled, the media is not encrypted.

When SRTP is enabled, it secures the IVR leg. SRTP negotiates between AES_CM_128_HMAC_SHA1_32 or AES_CM_128_HMAC_SHA1_80 crypto-suites, ensuring compatibility and successful
                                                                  encryption of media streams.

When SRTP uses a crypto-suite (for example, AES_CM_128_HMAC_SHA1_32), and the incoming request also uses the same crypto-suite,
                                                                     the request is accepted, and the media stream is successfully encrypted using AES_CM_128_HMAC_SHA1_32.

When SRTP uses a crypto-suite (for example, AES_CM_128_HMAC_SHA1_32), but the incoming request uses a different one (for example,
                                                                     AES_CM_128_HMAC_SHA1_80) or vice versa, the request will be denied and considered unsupported because the encryption methods
                                                                     do not match resulting in an error response.

Multiple ciphers may be included in a request; however, the negotiation will only proceed with the cipher configured in the
                                                                                 system, which will either be AES_CM_128_HMAC_SHA1_32 or AES_CM_128_HMAC_SHA1_80.

If neither of these ciphers match the request, it will be considered unsupported.

When Allow RTP (Mixed mode) check box is checked, the system accepts both SRTP and RTP call flows. This check box can be checked only when SRTP is enabled.

SRTP is available only if TLS (SIP) is enabled.

Check the Allow RTP (Mixed mode) check box if device is configured to work in the RTP mode and interacts with MRCP ARS-TTS servers.

For more details on mixed mode call flow scenarios, see the Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html .

Cisco VVB engine restart is required after a change to this configuration.

SRTP is not supported with VVB XU (Export Unrestricted) software image releases.

System Port Parameter

RMI Port

The port number used by Cisco VVB to serve Remote Method Invocation (RMI) requests. This field is mandatory.

Default: 6999

HTTPS Client TLS
                                                				  Configuration

The supported TLS versions as client for securing HTTPS signaling to fetch the VXML applications from VXML server use the
                                             CLI command set tls client min-version in Cisco Unified Contact Center Express Administration and Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html

## View Media Gateway Configurations

The following configurations are available only if the selected mode is Media Gateway (MGW) or Cisco Vitualized Voice Broswer
                                          (VVB) & Media Gateway (MGW).

From the Cisco VVB Adminstartion menu bar, choose Media Gateway > Configurations .

The Media Gateway Configurations web page displays the following fields.

Field

Decription

Dial Number Configuration

Displays the default dial number.

Proxy Parameters

Displays the configured host name of the proxy.

Displays the configured port number of the proxy.

Displays the masked password of the proxy.

Displays the configured host name of the non-proxy.

Cloud Connect Parameters

Publisher Address

Displays the configured FQDN / IP address of the publisher.

Subscriber Address

Displays the configured FQDN / IP address of the subscriber.

Username

Displays the configured name of the user.

Password

Displays the masked password.

## IP Address and
                        	 Hostname Management

This section provides the steps you need to follow whenever there is a
                           		change in IP address or hostname for Cisco VVB deployment.

### IP Address
                           	 Modification

This section describes how to change the IP address.

Caution

Changing the IP address can interrupt call processing and other
                                             			 system functions. Also, changing the IP address can cause the system to
                                             			 generate certain alarms and alerts such as ServerDown. Because of this
                                             			 potential impact to the system, you must perform IP address changes during a
                                             			 planned maintenance window.

As a prerequisite ensure that the DNS is reachable and the DNS
                                             			 record exists for the server if DNS is enabled.

#### Change IP Address
                              	 using CLI Commands

Use this procedure to change the IP address of Cisco VVB.

Step 1

If DNS is enabled, change the DNS record of the server to point to the new IP address.

Step 2

If you want to change the IP address of the server on the same subnet or a different subnet that requires a new default gateway
                                             address, then use either CLI Commands or Cisco Unified Operating System Administration interface.

Step 3

To change the default gateway, enter the following CLI command: set network gateway <IP Address>

The following is a sample output:

```
admin: set network gateway 10.10.10.1
     ***   W A R N I N G   ***
This will cause the system to temporarily lose network connectivity
Continue (y/n)?
```

Caution

Ensure that the server is moved to the new subnet and has access to the default gateway before proceeding to the following
                                                            sub-step.

Skip this step if you want to change only the IP address of the server.

Step 4

To change the IP address of the server, enter the following CLI command: set network ip eth0 <ip_address> <netmask> <default gateway>

The following sample output displays:

```
admin:set network ip eth0 10.10.10.170 255.255.255.0 10.10.10.1
           ***   W A R N I N G   ***
This command will restart system services
=======================================================
 Note: Please verify that the new ip address is unique 
       across the cluster and, if DNS services are 
       utilized, any DNS configuration is completed 
       before proceeding.
=======================================================
Continue (y/n)?
```

Step 5

Enter y and press Enter to continue.

Step 6

Reboot the system using the CLI command utils system restart .

#### Change IP Address using OS Administration interface

Step 1

Log in to the Cisco Unified OS Administration using administrator login.

Step 2

Go to Settings > IP > Ethernet .

Step 3

Change the Port (IP Address and Subnet Mask) and Gateway information and click Save .

Step 4

Reboot the system using the CLI command utils system restart .

### Hostname Modification

This section describes how to change the hostname.

Caution

Changing the hostname can interrupt call processing and other system functions. Changing the hostname can also cause the system
                                             to generate certain alarms and alerts such as ServerDown. Because of this potential impact to the system, you must perform
                                             hostname changes during a planned maintenance window.

If DNS is enabled, as a prerequisite ensure that the DNS is
                                             			 reachable and the DNS record exists for the server.

#### Change Hostname using CLI Commands

Step 1

Change the DNS record of the server to point to the new hostname if the server is configured. Ensure that you correctly update
                                             both the forward (A) and reverse (PTR) records, and there are no duplicate PTR records.

Step 2

At the CLI prompt, enter set network hostname and press Enter key.

The following is a sample output:

```
***   W A R N I N G   ***
Do not close this window without first canceling the command.
This command will automatically restart system services.
The command should not be issued during normal operating hours.
=======================================================
Note: 
Please verify that the new hostname is a unique name across the cluster and, 
if DNS services are utilized, any DNS configuration is completed before proceeding.
=======================================================
Security Warning :
This operation will regenerate all UCCX Certificates including any third party signed Certificates that have been uploaded.    
Enter the hostname::
```

Step 3

Enter the hostname and press Enter.

Step 4

Enter no if you do not want to change the IP address. Otherwise, press yes and enter the new IP address, the subnet mask, and the address of the gateway when prompted.

Step 5

Verify that all your input is correct and enter yes to start the process.

Do not proceed if the new hostname does not resolve to the correct IP address.

Step 6

Reboot the system using the CLI command utils system restart .

Enter y and press Enter to restart the system.

#### Change Hostname using OS Administration Interface

Step 1

Login to the Cisco Unified OS Administration using administrator
                                             			 login.

Step 2

Go to Settings > IP > Ethernet .

Step 3

Change the hostname and click Save .

Step 4

Reboot the system using the CLI command utils system restart .

## Configure
                        	 Reporting and Monitoring Services

### Real-Time
                           	 Monitoring Tool

Cisco VVB system includes software components called plug-in You can download the Real-Time Monitoring Tool (RTMT) plug-in as a compressed file (.zip) by choosing Tools > Plug-in from the Cisco VVB Administration portal.

The
                                 		  Plug-in web page contains the following hyperlink:

Cisco Unified Real-Time Monitoring Tool for Windows —Click this hyperlink to download client-side Cisco Unified Serviceability RTMT for Windows. RTMT uses HTTPS and TCP to monitor
                                       device status and system performance for troubleshooting system problems. This plug-in is available only for users with administrator capability.

For more information, see the https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/15/rtmt/cucm_b_cisco-unified-rtmt-administration-15/cucm_m_getting-started.html .

For the Cisco VVB, the Unified RTMT is not supported on Linux.

To download,
                                                   				  click the Download hyperlink and select Save File .

You can download  Speech Server and Cisco VVB Engine logs from the RTMT.

### Logging

A trace file is a log file that records activity from the Cisco VVB component subsystems and steps. Trace files let you obtain
                                 specific, detailed information about the system that can help you troubleshoot problems.

This information is stored in a trace file. To help you control the size of the trace file, you specify the components for
                                 which you want to collect information and the level of information that you want to collect.

The Cisco VVB server stores the trace files in the Log directory. You can collect and view trace information using the Real-Time
                                 Monitoring Tool (RTMT).

In a Cisco VVB server, audit logging is supported for Voice Operating System (VOS) and Command Line Interface (CLI) activities,
                                             which can be monitored using the Real Time Monitoring Tool (RTMT). However, VVB services activities are not included in the
                                             audit logs.

To activate and turn off logging, follow this procedure:

#### Engine

Step 1

From the Cisco VVB Serviceability menu bar, choose Trace > Configuration .

Step 2

From the Select Service drop-down list box, choose Engine and click Go .

The debug levels for different Cisco VVB services might vary depending on the selected service. The Cisco VVB-related services
                                                are listed in the following table:

Component Code

Description

JASMIN

Java Signaling and Monitoring Interface

SIP_STACK

SIP Stack logging

SS_SIP

SIP Subsystem

SS_VB

Voice Browser Subsystem

SS_MRCP_ASR

MRCP ASR Subsystem

SS_MRCP_TTS

MRCP TTS Subsystem

To enable XDebugging for any of the components, check the appropriate check boxes.

Step 3

To limit the number and size of the trace files, you can specify the trace output setting using the following two fields.
                                             See the following table for description and default values for these two fields:

Field

Description

Maximum No. of Files

The maximum number of trace files to be retained by the system.

This field specifies the total number of trace files for a given service. Cisco VVB Serviceability automatically appends a
                                                            sequence number to the filename to indicate which file it is; for example, Cisco001MADM14.log. When the last file in the sequence
                                                            is full, the trace data begins writing over the first file. The default value varies by service.

Maximum File Size

This field specifies the maximum size of the trace file in kilobytes or megabytes depending on the selected service. The default
                                                            value varies by service.

Step 4

Update the debug level for one or more components for the selected service of Cisco VVB by performing these steps:

To activate traces for a specific component or logging for a server, select the check box for the service for which you need
                                                      to enable logging.

To turn off logging for a server, clear the check box.

Step 5

Click the Save icon that displays in the toolbar in the upper left corner of the window or the Save button that displays at the bottom of the window to save your trace parameter configuration. The settings are updated in
                                             the system and the trace files are generated as per the saved settings. Click the Restore Defaults icon or button to revert to the default settings for the selected service.

Important

Activate logging only for debugging, and remember to turn off logging after the debugging session is complete.

#### Speech Server

Step 1

From the Cisco VVB Serviceability menu bar, choose Trace > Configuration .

Step 2

From the Select Service drop-down list box, choose Speech Server and click Go .

Component Code

Description

SS_SRV

Speech Server

To enable XDebugging for any of the components, check the appropriate check boxes.

Step 3

To limit the size of the Log File directory and the size of trace files, you can specify the trace output setting using the
                                             following two fields. See the following table for description and default values for these two fields:

Field

Description

Maximum No. of Files

Maximum number of trace files that is used to calculate total log directory size.

Maximum File Size

This field specifies the maximum size of the trace file in kilobytes or megabytes depending on the selected service. The default
                                                            value varies by service.

Step 4

Update the debug level for one or more components for the selected service of Cisco VVB by performing these steps:

To activate traces for a specific component or logging for a server, select the check box for the service for which you need
                                                      to enable logging.

To turn off logging for a server, clear the check box.

Step 5

Click the Save icon that displays in the toolbar in the upper left corner of the window or the Save button that displays at the bottom of the window to save your trace parameter configuration. The settings are updated in
                                             the system and the trace files are generated as per the saved settings. Click the Restore Defaults icon or button to revert to the default settings for the selected service.

Important

Activate logging only for debugging, and remember to turn off logging after the debugging session is complete.

You can download both speech server and Cisco VVB Engine logs from the Real-Time Monitoring Tool (RTMT) or the CLI commands.
                                                            For more information on the CLI commands, refer to the Operations Guide for Cisco Virtualized Voice Browser .

### Service Management

Installed automatically, network services include services that the system requires to function; for example, system services.
                                 Because these services are required for basic functionality, you cannot activate them in the Service Activation window. After
                                 the installation of your application, network services start automatically.

To start, stop, or restart Cisco VVB services, follow these steps:

Step 1

From the Navigation drop-down list, select Cisco VVB Serviceability.

Step 2

Select Tools > Control Center - Network Services .

Step 3

Select the Engine radio button  and click your desired operation button.

The page displays the following information for the network services:

Name of the network services, their dependent subsystems, managers, or components

Status of the service (IN SERVICE, PARTIAL SERVICE, or SHUT DOWN; for individual subsystems, the status can be OUT OF SERVICE
                                                   or NOT CONFIGURED)

Start Time of the service

Up Time of the service

| Note | After successfully adding Cisco VVB on Unified CVP, ensure to restart Operations Console service and Web Services Manager
                                          service. |
|---|---|

| Note | Cisco VVB does not support clustering. Therefore, you may ignore any message on the Cisco VVB Admin UI/CLI that refers to cluster , publisher , subscriber , etc. |
|---|---|

| Step 1 | Create an
                                       			 application to define the call flow through the scripts. To configure
                                          				standalone application, see Configure Cisco VVB Settings for Standalone Call Flow Model . To configure
                                          				comprehensive and ringtone application, see Configure Cisco VVB Settings for Comprehensive Call Flow Model . To configure
                                          				error application, see Configure Error Application . |
|---|---|
| Step 2 | Create
                                       			 triggers to invoke an application using the incoming directory number. To configure
                                          				the trigger, see Configure SIP Triggers . |
| Step 3 | Cisco VVB can
                                       			 play recorded audio prompts and detect DTMF tones. To recognize speech and play
                                       			 text, configure Automatic Speech Recognition (ASR) and Text-To-Speech (TTS). To configure
                                          				ASR and TTS, see Configure Speech Servers . |
| Step 4 | Manage prompt
                                       			 files to add custom ringtone for comprehensive call flow or to use custom
                                       			 prompts. To configure
                                          				and manage prompts, see Configure Prompt Management . |

| Step 1 | From Cisco VVB Administration menu bar, choose Applications > Application Management . |
|---|---|
| Step 2 | Click the Add
                                          				New icon that is displayed in the toolbar in the upper left corner
                                       			 of the window or the Add
                                          				New button that is displayed at the bottom of the window. |
| Step 3 | Type the application name in the Name field. The Maximum Number of Sessions field is prepopulated based on the OVA profile. You can edit this field. Note This number must not exceed the maximum number of ports supported for Cisco VVB profile. For more information, see Virtualization for Cisco Virtualized Voice Browser available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-virtualized-voice-browser.html . | Note | This number must not exceed the maximum number of ports supported for Cisco VVB profile. For more information, see Virtualization for Cisco Virtualized Voice Browser available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-virtualized-voice-browser.html . |
| Note | This number must not exceed the maximum number of ports supported for Cisco VVB profile. For more information, see Virtualization for Cisco Virtualized Voice Browser available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-virtualized-voice-browser.html . |
| Step 4 | Select the SelfService.aef script from the drop-down list for a standalone application. The following table describes the parameters: Parameter Description Default Base Type Application Name Application name that is present on the VXML server. Mandatory field to enter. "HelloWorld" Alphanumeric Port Port on which the VXML server or load balancer is running. Note Ports 7000/7443 must be configured for interworking with CVP Release 11.5 and later. For earlier versions of CVP, configure
                                                                  ports 8000/8443. "7000" Numeric PrimaryVXMLServer VXML server or load balancer IP address. "" Alphanumeric BackupVXMLServer VXML server backup server IP address. "" Alphanumeric Secured If enabled, HTTPS is used while fetching VXML application from Unified CVP. By default it is not enabled. Note If you have enabled secure communication, then ensure to: Change the port number in the above field to 7443. Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Cisco Unified Communications Operating System Administration Guide. Restart Tomcat server and Engine from command line. false Boolean | Parameter | Description | Default | Base Type | Application Name | Application name that is present on the VXML server. Mandatory field to enter. | "HelloWorld" | Alphanumeric | Port | Port on which the VXML server or load balancer is running. Note Ports 7000/7443 must be configured for interworking with CVP Release 11.5 and later. For earlier versions of CVP, configure
                                                                  ports 8000/8443. | Note | Ports 7000/7443 must be configured for interworking with CVP Release 11.5 and later. For earlier versions of CVP, configure
                                                                  ports 8000/8443. | "7000" | Numeric | PrimaryVXMLServer | VXML server or load balancer IP address. | "" | Alphanumeric | BackupVXMLServer | VXML server backup server IP address. | "" | Alphanumeric | Secured | If enabled, HTTPS is used while fetching VXML application from Unified CVP. By default it is not enabled. Note If you have enabled secure communication, then ensure to: Change the port number in the above field to 7443. Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Cisco Unified Communications Operating System Administration Guide. Restart Tomcat server and Engine from command line. | Note | If you have enabled secure communication, then ensure to: Change the port number in the above field to 7443. Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Cisco Unified Communications Operating System Administration Guide. Restart Tomcat server and Engine from command line. | false | Boolean |
| Parameter | Description | Default | Base Type |
| Application Name | Application name that is present on the VXML server. Mandatory field to enter. | "HelloWorld" | Alphanumeric |
| Port | Port on which the VXML server or load balancer is running. Note Ports 7000/7443 must be configured for interworking with CVP Release 11.5 and later. For earlier versions of CVP, configure
                                                                  ports 8000/8443. | Note | Ports 7000/7443 must be configured for interworking with CVP Release 11.5 and later. For earlier versions of CVP, configure
                                                                  ports 8000/8443. | "7000" | Numeric |
| Note | Ports 7000/7443 must be configured for interworking with CVP Release 11.5 and later. For earlier versions of CVP, configure
                                                                  ports 8000/8443. |
| PrimaryVXMLServer | VXML server or load balancer IP address. | "" | Alphanumeric |
| BackupVXMLServer | VXML server backup server IP address. | "" | Alphanumeric |
| Secured | If enabled, HTTPS is used while fetching VXML application from Unified CVP. By default it is not enabled. Note If you have enabled secure communication, then ensure to: Change the port number in the above field to 7443. Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Cisco Unified Communications Operating System Administration Guide. Restart Tomcat server and Engine from command line. | Note | If you have enabled secure communication, then ensure to: Change the port number in the above field to 7443. Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Cisco Unified Communications Operating System Administration Guide. Restart Tomcat server and Engine from command line. | false | Boolean |
| Note | If you have enabled secure communication, then ensure to: Change the port number in the above field to 7443. Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Cisco Unified Communications Operating System Administration Guide. Restart Tomcat server and Engine from command line. |
| Step 5 | Use the Tab key to automatically populate the Description field. |
| Step 6 | Enable the
                                       			 application by selecting the radio button. You can choose to disable the
                                       			 application to retain the configurations for later use. |
| Step 7 | Click Add . The Cisco Script Application page refreshes and the Add New Trigger hyperlink appears in the left navigation bar. The following message is displayed in the status bar on top: The operation has been
                                             				  executed successfully. |
| Step 8 | Create a
                                       			 trigger using the Add
                                          				New Trigger hyperlink or follow the procedure Configure SIP Triggers . |

| Note | This number must not exceed the maximum number of ports supported for Cisco VVB profile. For more information, see Virtualization for Cisco Virtualized Voice Browser available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-virtualized-voice-browser.html . |
|---|---|

| Parameter | Description | Default | Base Type |
|---|---|---|---|
| Application Name | Application name that is present on the VXML server. Mandatory field to enter. | "HelloWorld" | Alphanumeric |
| Port | Port on which the VXML server or load balancer is running. Note Ports 7000/7443 must be configured for interworking with CVP Release 11.5 and later. For earlier versions of CVP, configure
                                                                  ports 8000/8443. | Note | Ports 7000/7443 must be configured for interworking with CVP Release 11.5 and later. For earlier versions of CVP, configure
                                                                  ports 8000/8443. | "7000" | Numeric |
| Note | Ports 7000/7443 must be configured for interworking with CVP Release 11.5 and later. For earlier versions of CVP, configure
                                                                  ports 8000/8443. |
| PrimaryVXMLServer | VXML server or load balancer IP address. | "" | Alphanumeric |
| BackupVXMLServer | VXML server backup server IP address. | "" | Alphanumeric |
| Secured | If enabled, HTTPS is used while fetching VXML application from Unified CVP. By default it is not enabled. Note If you have enabled secure communication, then ensure to: Change the port number in the above field to 7443. Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Cisco Unified Communications Operating System Administration Guide. Restart Tomcat server and Engine from command line. | Note | If you have enabled secure communication, then ensure to: Change the port number in the above field to 7443. Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Cisco Unified Communications Operating System Administration Guide. Restart Tomcat server and Engine from command line. | false | Boolean |
| Note | If you have enabled secure communication, then ensure to: Change the port number in the above field to 7443. Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Cisco Unified Communications Operating System Administration Guide. Restart Tomcat server and Engine from command line. |

| Note | Ports 7000/7443 must be configured for interworking with CVP Release 11.5 and later. For earlier versions of CVP, configure
                                                                  ports 8000/8443. |
|---|---|

| Note | If you have enabled secure communication, then ensure to: Change the port number in the above field to 7443. Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Cisco Unified Communications Operating System Administration Guide. Restart Tomcat server and Engine from command line. |
|---|---|

| Note | Cisco VVB is prepopulated with comprehensive application (also called bootstrap) and the ringtone application. |
|---|---|

| Step 1 | From Cisco VVB Administration menu bar, choose Applications > Application Management . |
|---|---|
| Step 2 | Click Add
                                          				New . |
| Step 3 | (Mandatory)
                                       			 Type the application name in the Name field. |
| Step 4 | The Maximum Number of Sessions field is prepopulated based on the OVA profile. You can edit this field. Note This number must not exceed the maximum number of ports supported for Cisco VVB profile. For more information, see Virtualization for Cisco Virtualized Voice Browser available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-virtualized-voice-browser.html . | Note | This number must not exceed the maximum number of ports supported for Cisco VVB profile. For more information, see Virtualization for Cisco Virtualized Voice Browser available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-virtualized-voice-browser.html . |
| Note | This number must not exceed the maximum number of ports supported for Cisco VVB profile. For more information, see Virtualization for Cisco Virtualized Voice Browser available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-virtualized-voice-browser.html . |
| Step 5 | Select the
                                       			 script from the drop-down list. The following scripts are provided for comprehensive call flow: CVPComprehensive.aef (bootstrap) Ringtone.aef The
                                          				  following table describes the parameters: Parameter Description Default Base Type Secured If enabled, HTTPS is used while fetching VXML application from Unified CVP. By default, it is not enabled. Note If you have enabled secure communication, then ensure to: Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Cisco Unified Communications Operating System Administration Guide. Restart Tomcat server and Engine from command line. If you are using a coresident VXML and Call Server, use CA-signed certificate. false Boolean Sigdigit Enable this parameter to use Significant Digits feature. Enter the number of digits that are used as sigdigit. When Cisco
                                                      VVB receives the call, the CVP comprehensive service is configured to strip the digits. When the IVR leg of the call is set
                                                      up, the original label is used on the incoming VoiceXML request. 0 Numeric | Parameter | Description | Default | Base Type | Secured | If enabled, HTTPS is used while fetching VXML application from Unified CVP. By default, it is not enabled. Note If you have enabled secure communication, then ensure to: Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Cisco Unified Communications Operating System Administration Guide. Restart Tomcat server and Engine from command line. If you are using a coresident VXML and Call Server, use CA-signed certificate. | Note | If you have enabled secure communication, then ensure to: Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Cisco Unified Communications Operating System Administration Guide. Restart Tomcat server and Engine from command line. If you are using a coresident VXML and Call Server, use CA-signed certificate. | false | Boolean | Sigdigit | Enable this parameter to use Significant Digits feature. Enter the number of digits that are used as sigdigit. When Cisco
                                                      VVB receives the call, the CVP comprehensive service is configured to strip the digits. When the IVR leg of the call is set
                                                      up, the original label is used on the incoming VoiceXML request. | 0 | Numeric |
| Parameter | Description | Default | Base Type |
| Secured | If enabled, HTTPS is used while fetching VXML application from Unified CVP. By default, it is not enabled. Note If you have enabled secure communication, then ensure to: Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Cisco Unified Communications Operating System Administration Guide. Restart Tomcat server and Engine from command line. If you are using a coresident VXML and Call Server, use CA-signed certificate. | Note | If you have enabled secure communication, then ensure to: Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Cisco Unified Communications Operating System Administration Guide. Restart Tomcat server and Engine from command line. If you are using a coresident VXML and Call Server, use CA-signed certificate. | false | Boolean |
| Note | If you have enabled secure communication, then ensure to: Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Cisco Unified Communications Operating System Administration Guide. Restart Tomcat server and Engine from command line. If you are using a coresident VXML and Call Server, use CA-signed certificate. |
| Sigdigit | Enable this parameter to use Significant Digits feature. Enter the number of digits that are used as sigdigit. When Cisco
                                                      VVB receives the call, the CVP comprehensive service is configured to strip the digits. When the IVR leg of the call is set
                                                      up, the original label is used on the incoming VoiceXML request. | 0 | Numeric |
| Step 6 | Use the Tab key to automatically populate the Description field. |
| Step 7 | Enable the
                                       			 application by selecting the radio button. You can choose to disable the
                                       			 application to retain the configurations for later use. |
| Step 8 | Click Add . The Cisco Script Application page refreshes and the Add New Trigger hyperlink appears in the left navigation bar. The following message is displayed in the status bar on top: The operation has been
                                             				  executed successfully. |
| Step 9 | Create a
                                       			 trigger using the Add
                                          				New Trigger hyperlink or follow the procedure Configure SIP Triggers . |

| Note | This number must not exceed the maximum number of ports supported for Cisco VVB profile. For more information, see Virtualization for Cisco Virtualized Voice Browser available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-virtualized-voice-browser.html . |
|---|---|

| Parameter | Description | Default | Base Type |
|---|---|---|---|
| Secured | If enabled, HTTPS is used while fetching VXML application from Unified CVP. By default, it is not enabled. Note If you have enabled secure communication, then ensure to: Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Cisco Unified Communications Operating System Administration Guide. Restart Tomcat server and Engine from command line. If you are using a coresident VXML and Call Server, use CA-signed certificate. | Note | If you have enabled secure communication, then ensure to: Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Cisco Unified Communications Operating System Administration Guide. Restart Tomcat server and Engine from command line. If you are using a coresident VXML and Call Server, use CA-signed certificate. | false | Boolean |
| Note | If you have enabled secure communication, then ensure to: Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Cisco Unified Communications Operating System Administration Guide. Restart Tomcat server and Engine from command line. If you are using a coresident VXML and Call Server, use CA-signed certificate. |
| Sigdigit | Enable this parameter to use Significant Digits feature. Enter the number of digits that are used as sigdigit. When Cisco
                                                      VVB receives the call, the CVP comprehensive service is configured to strip the digits. When the IVR leg of the call is set
                                                      up, the original label is used on the incoming VoiceXML request. | 0 | Numeric |

| Note | If you have enabled secure communication, then ensure to: Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Cisco Unified Communications Operating System Administration Guide. Restart Tomcat server and Engine from command line. If you are using a coresident VXML and Call Server, use CA-signed certificate. |
|---|---|

| Step 1 | From Cisco VVB
                                       			 Administration menu bar, choose Applications > Application
                                             				  Management . |
|---|---|
| Step 2 | Click Add
                                          				New . |
| Step 3 | (Mandatory)
                                       			 Type the application name in the Name field. |
| Step 4 | The Maximum Number of Sessions field is prepopulated
                                       			 based on the OVA profile. You can edit this field. Note This number must not exceed the maximum number of ports supported for Cisco VVB profile. For more information, see Virtualization for Cisco Virtualized Voice Browser available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-virtualized-voice-browser.html . | Note | This number must not exceed the maximum number of ports supported for Cisco VVB profile. For more information, see Virtualization for Cisco Virtualized Voice Browser available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-virtualized-voice-browser.html . |
| Note | This number must not exceed the maximum number of ports supported for Cisco VVB profile. For more information, see Virtualization for Cisco Virtualized Voice Browser available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-virtualized-voice-browser.html . |
| Step 5 | From the Script drop-down list, select the VRUComprehensive.aef script. Parameter Description Default Base
                                                      							 Type PrimaryVXMLServer VXML server or load balancer IP address "" Alphanumeric BackupVXMLServer VXML backup server or load balancer IP address "" Alphanumeric Port Port on which VXML server or load balancer is running. Note Ports 7000/7443 must be configured for interworking with CVP Release 11.5 and later. "7000" Numeric Secured If
                                                      							 enabled, HTTPS is used while fetching VXML application from Unified CVP. By
                                                      							 default, Secured is not enabled. Note If you have enabled secure communication, then ensure to: Change the port number to 7443. Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Configuration Guide for Cisco Unified Customer Voice
                                                                           										Portal. Restart Tomcat server and engine from command line. If you are using a co-resident VXML and Call Server, use a
                                                                        									 CA-signed certificate. false Boolean Sigdigit Enable this parameter to use Significant Digits feature. Enter
                                                      							 the number of digits that are used as sigdigit. When Cisco VVB receives a call,
                                                      							 the VRU comprehensive service is configured to strip the digits. When the IVR
                                                      							 leg of the call is set up, the original label is used on the incoming VoiceXML
                                                      							 request. 0 Numeric | Parameter | Description | Default | Base
                                                      							 Type | PrimaryVXMLServer | VXML server or load balancer IP address | "" | Alphanumeric | BackupVXMLServer | VXML backup server or load balancer IP address | "" | Alphanumeric | Port | Port on which VXML server or load balancer is running. Note Ports 7000/7443 must be configured for interworking with CVP Release 11.5 and later. | Note | Ports 7000/7443 must be configured for interworking with CVP Release 11.5 and later. | "7000" | Numeric | Secured | If
                                                      							 enabled, HTTPS is used while fetching VXML application from Unified CVP. By
                                                      							 default, Secured is not enabled. Note If you have enabled secure communication, then ensure to: Change the port number to 7443. Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Configuration Guide for Cisco Unified Customer Voice
                                                                           										Portal. Restart Tomcat server and engine from command line. If you are using a co-resident VXML and Call Server, use a
                                                                        									 CA-signed certificate. | Note | If you have enabled secure communication, then ensure to: Change the port number to 7443. Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Configuration Guide for Cisco Unified Customer Voice
                                                                           										Portal. Restart Tomcat server and engine from command line. If you are using a co-resident VXML and Call Server, use a
                                                                        									 CA-signed certificate. | false | Boolean | Sigdigit | Enable this parameter to use Significant Digits feature. Enter
                                                      							 the number of digits that are used as sigdigit. When Cisco VVB receives a call,
                                                      							 the VRU comprehensive service is configured to strip the digits. When the IVR
                                                      							 leg of the call is set up, the original label is used on the incoming VoiceXML
                                                      							 request. | 0 | Numeric |
| Parameter | Description | Default | Base
                                                      							 Type |
| PrimaryVXMLServer | VXML server or load balancer IP address | "" | Alphanumeric |
| BackupVXMLServer | VXML backup server or load balancer IP address | "" | Alphanumeric |
| Port | Port on which VXML server or load balancer is running. Note Ports 7000/7443 must be configured for interworking with CVP Release 11.5 and later. | Note | Ports 7000/7443 must be configured for interworking with CVP Release 11.5 and later. | "7000" | Numeric |
| Note | Ports 7000/7443 must be configured for interworking with CVP Release 11.5 and later. |
| Secured | If
                                                      							 enabled, HTTPS is used while fetching VXML application from Unified CVP. By
                                                      							 default, Secured is not enabled. Note If you have enabled secure communication, then ensure to: Change the port number to 7443. Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Configuration Guide for Cisco Unified Customer Voice
                                                                           										Portal. Restart Tomcat server and engine from command line. If you are using a co-resident VXML and Call Server, use a
                                                                        									 CA-signed certificate. | Note | If you have enabled secure communication, then ensure to: Change the port number to 7443. Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Configuration Guide for Cisco Unified Customer Voice
                                                                           										Portal. Restart Tomcat server and engine from command line. If you are using a co-resident VXML and Call Server, use a
                                                                        									 CA-signed certificate. | false | Boolean |
| Note | If you have enabled secure communication, then ensure to: Change the port number to 7443. Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Configuration Guide for Cisco Unified Customer Voice
                                                                           										Portal. Restart Tomcat server and engine from command line. If you are using a co-resident VXML and Call Server, use a
                                                                        									 CA-signed certificate. |
| Sigdigit | Enable this parameter to use Significant Digits feature. Enter
                                                      							 the number of digits that are used as sigdigit. When Cisco VVB receives a call,
                                                      							 the VRU comprehensive service is configured to strip the digits. When the IVR
                                                      							 leg of the call is set up, the original label is used on the incoming VoiceXML
                                                      							 request. | 0 | Numeric |
| Step 6 | Use the Tab
                                       			 key to automatically populate the Description field. |
| Step 7 | Enable the
                                       			 application by selecting the radio button. You can choose to disable the
                                       			 application to retain the configurations for later use. |
| Step 8 | Click Add . Cisco Script
                                          				Application page refreshes. The Add
                                             				  New Trigger hyperlink appears in the left navigation bar. The
                                          				following message is displayed in the status bar on top: The operation has been
                                             				  executed successfully. |
| Step 9 | Create a
                                       			 trigger using the Add
                                          				New Trigger hyperlink or follow the procedure Configure SIP Triggers . |

| Note | This number must not exceed the maximum number of ports supported for Cisco VVB profile. For more information, see Virtualization for Cisco Virtualized Voice Browser available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-virtualized-voice-browser.html . |
|---|---|

| Parameter | Description | Default | Base
                                                      							 Type |
|---|---|---|---|
| PrimaryVXMLServer | VXML server or load balancer IP address | "" | Alphanumeric |
| BackupVXMLServer | VXML backup server or load balancer IP address | "" | Alphanumeric |
| Port | Port on which VXML server or load balancer is running. Note Ports 7000/7443 must be configured for interworking with CVP Release 11.5 and later. | Note | Ports 7000/7443 must be configured for interworking with CVP Release 11.5 and later. | "7000" | Numeric |
| Note | Ports 7000/7443 must be configured for interworking with CVP Release 11.5 and later. |
| Secured | If
                                                      							 enabled, HTTPS is used while fetching VXML application from Unified CVP. By
                                                      							 default, Secured is not enabled. Note If you have enabled secure communication, then ensure to: Change the port number to 7443. Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Configuration Guide for Cisco Unified Customer Voice
                                                                           										Portal. Restart Tomcat server and engine from command line. If you are using a co-resident VXML and Call Server, use a
                                                                        									 CA-signed certificate. | Note | If you have enabled secure communication, then ensure to: Change the port number to 7443. Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Configuration Guide for Cisco Unified Customer Voice
                                                                           										Portal. Restart Tomcat server and engine from command line. If you are using a co-resident VXML and Call Server, use a
                                                                        									 CA-signed certificate. | false | Boolean |
| Note | If you have enabled secure communication, then ensure to: Change the port number to 7443. Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Configuration Guide for Cisco Unified Customer Voice
                                                                           										Portal. Restart Tomcat server and engine from command line. If you are using a co-resident VXML and Call Server, use a
                                                                        									 CA-signed certificate. |
| Sigdigit | Enable this parameter to use Significant Digits feature. Enter
                                                      							 the number of digits that are used as sigdigit. When Cisco VVB receives a call,
                                                      							 the VRU comprehensive service is configured to strip the digits. When the IVR
                                                      							 leg of the call is set up, the original label is used on the incoming VoiceXML
                                                      							 request. | 0 | Numeric |

| Note | Ports 7000/7443 must be configured for interworking with CVP Release 11.5 and later. |
|---|---|

| Note | If you have enabled secure communication, then ensure to: Change the port number to 7443. Upload the relevant certificate. To upload certificate, see Upload certificate or certificate trust list topic in Configuration Guide for Cisco Unified Customer Voice
                                                                           										Portal. Restart Tomcat server and engine from command line. If you are using a co-resident VXML and Call Server, use a
                                                                        									 CA-signed certificate. |
|---|---|

| Step 1 | From Cisco VVB Administration menu bar, choose Applications > Application Management . |
|---|---|
| Step 2 | Click Add
                                          				New . |
| Step 3 | Type the application name in the Name field. The Maximum Number of Sessions field is prepopulated based on the OVA profile. You can edit this field. Note This number must not exceed the maximum number of ports supported for Cisco VVB profile. For more information, see Virtualization for Cisco Virtualized Voice Browser available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-virtualized-voice-browser.html . | Note | This number must not exceed the maximum number of ports supported for Cisco VVB profile. For more information, see Virtualization for Cisco Virtualized Voice Browser available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-virtualized-voice-browser.html . |
| Note | This number must not exceed the maximum number of ports supported for Cisco VVB profile. For more information, see Virtualization for Cisco Virtualized Voice Browser available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-virtualized-voice-browser.html . |
| Step 4 | Select the Error.aef script from the drop-down list. This script is used to play error tone. The following table describes the parameter details: Parameter Default Base Type CVPErrorPrompt —Select and associate custom wav file from VVB application. To override system default wav file, upload custom wav file from Prompt Management menu. Note You can upload custom wav files only for Error.aef script. 92929292 Numeric | Parameter | Default | Base Type | CVPErrorPrompt —Select and associate custom wav file from VVB application. To override system default wav file, upload custom wav file from Prompt Management menu. Note You can upload custom wav files only for Error.aef script. | Note | You can upload custom wav files only for Error.aef script. | 92929292 | Numeric |
| Parameter | Default | Base Type |
| CVPErrorPrompt —Select and associate custom wav file from VVB application. To override system default wav file, upload custom wav file from Prompt Management menu. Note You can upload custom wav files only for Error.aef script. | Note | You can upload custom wav files only for Error.aef script. | 92929292 | Numeric |
| Note | You can upload custom wav files only for Error.aef script. |
| Step 5 | Use the Tab key to automatically populate the Description field. |
| Step 6 | Enable the
                                       			 application by selecting the radio button. You can choose to disable the
                                       			 application to retain the configurations for later use. |
| Step 7 | Click Add . Cisco Script Application page is refreshed and the Add New Trigger hyperlink appears in the left navigation bar. The following message is displayed in the status bar on top: The operation has been
                                             				  executed successfully. |
| Step 8 | Create a
                                       			 trigger using the Add
                                          				New Trigger hyperlink or follow the procedure Configure SIP Triggers . |

| Note | This number must not exceed the maximum number of ports supported for Cisco VVB profile. For more information, see Virtualization for Cisco Virtualized Voice Browser available at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-virtualized-voice-browser.html . |
|---|---|

| Parameter | Default | Base Type |
|---|---|---|
| CVPErrorPrompt —Select and associate custom wav file from VVB application. To override system default wav file, upload custom wav file from Prompt Management menu. Note You can upload custom wav files only for Error.aef script. | Note | You can upload custom wav files only for Error.aef script. | 92929292 | Numeric |
| Note | You can upload custom wav files only for Error.aef script. |

| Note | You can upload custom wav files only for Error.aef script. |
|---|---|

| Step 1 | From Cisco VVB Administration menu bar, choose Subsystems > SIP Telephony > SIP Triggers . |
|---|---|
| Step 2 | Click Add New and enter the following fields: Field Description Directory Information Dial Number Pattern A unique phone number. The value includes digits and optionally includes " * " to mask multiple digits. Examples of valid Directory Numbers: 9191* Examples for valid triggers: 10.919191 where 10. is the same as 101, 102 *12* or 12*23 where *12* is the same as "*" and 12*23 is the same as 12* Note The trigger cannot contain only a wildcard character (*). If it contains *, it must also contain numbers. Capital letter "X" can be used as a wildcard, but small letter "x" cannot be used. Trigger Information Application Name From the drop-down list, choose the application to associate with the trigger. Advanced Trigger Information (available only if you click Show More ) Enabled Click a radio button to choose the required option: Yes— Enable the trigger (default) No— Disable the trigger Idle Timeout (in ms) The number of milliseconds (ms) the system waits before rejecting the SIP request for this trigger. Override Media Termination Click a radio button to choose the required options: Yes— Override media termination. No— Enable media termination (default). If you select Yes, two panes open: Selected Dialog Groups — displays the default or selected group. Note You must not change the default Selected Dialog Group associated with the application. Available Dialog Groups — displays the configured dialog. Description Click the Tab key to populate it. The new trigger is created and listed on the SIP Trigger page. | Field | Description | Directory Information | Dial Number Pattern | A unique phone number. The value includes digits and optionally includes " * " to mask multiple digits. Examples of valid Directory Numbers: 9191* Examples for valid triggers: 10.919191 where 10. is the same as 101, 102 *12* or 12*23 where *12* is the same as "*" and 12*23 is the same as 12* Note The trigger cannot contain only a wildcard character (*). If it contains *, it must also contain numbers. Capital letter "X" can be used as a wildcard, but small letter "x" cannot be used. | Note | The trigger cannot contain only a wildcard character (*). If it contains *, it must also contain numbers. Capital letter "X" can be used as a wildcard, but small letter "x" cannot be used. | Trigger Information | Application Name | From the drop-down list, choose the application to associate with the trigger. | Advanced Trigger Information (available only if you click Show More ) | Enabled | Click a radio button to choose the required option: Yes— Enable the trigger (default) No— Disable the trigger | Idle Timeout (in ms) | The number of milliseconds (ms) the system waits before rejecting the SIP request for this trigger. | Override Media Termination | Click a radio button to choose the required options: Yes— Override media termination. No— Enable media termination (default). If you select Yes, two panes open: Selected Dialog Groups — displays the default or selected group. Note You must not change the default Selected Dialog Group associated with the application. Available Dialog Groups — displays the configured dialog. | Note | You must not change the default Selected Dialog Group associated with the application. | Description | Click the Tab key to populate it. |
| Field | Description |
| Directory Information |
| Dial Number Pattern | A unique phone number. The value includes digits and optionally includes " * " to mask multiple digits. Examples of valid Directory Numbers: 9191* Examples for valid triggers: 10.919191 where 10. is the same as 101, 102 *12* or 12*23 where *12* is the same as "*" and 12*23 is the same as 12* Note The trigger cannot contain only a wildcard character (*). If it contains *, it must also contain numbers. Capital letter "X" can be used as a wildcard, but small letter "x" cannot be used. | Note | The trigger cannot contain only a wildcard character (*). If it contains *, it must also contain numbers. Capital letter "X" can be used as a wildcard, but small letter "x" cannot be used. |
| Note | The trigger cannot contain only a wildcard character (*). If it contains *, it must also contain numbers. Capital letter "X" can be used as a wildcard, but small letter "x" cannot be used. |
| Trigger Information |
| Application Name | From the drop-down list, choose the application to associate with the trigger. |
| Advanced Trigger Information (available only if you click Show More ) |
| Enabled | Click a radio button to choose the required option: Yes— Enable the trigger (default) No— Disable the trigger |
| Idle Timeout (in ms) | The number of milliseconds (ms) the system waits before rejecting the SIP request for this trigger. |
| Override Media Termination | Click a radio button to choose the required options: Yes— Override media termination. No— Enable media termination (default). If you select Yes, two panes open: Selected Dialog Groups — displays the default or selected group. Note You must not change the default Selected Dialog Group associated with the application. Available Dialog Groups — displays the configured dialog. | Note | You must not change the default Selected Dialog Group associated with the application. |
| Note | You must not change the default Selected Dialog Group associated with the application. |
| Description | Click the Tab key to populate it. |

| Field | Description |
|---|---|
| Directory Information |
| Dial Number Pattern | A unique phone number. The value includes digits and optionally includes " * " to mask multiple digits. Examples of valid Directory Numbers: 9191* Examples for valid triggers: 10.919191 where 10. is the same as 101, 102 *12* or 12*23 where *12* is the same as "*" and 12*23 is the same as 12* Note The trigger cannot contain only a wildcard character (*). If it contains *, it must also contain numbers. Capital letter "X" can be used as a wildcard, but small letter "x" cannot be used. | Note | The trigger cannot contain only a wildcard character (*). If it contains *, it must also contain numbers. Capital letter "X" can be used as a wildcard, but small letter "x" cannot be used. |
| Note | The trigger cannot contain only a wildcard character (*). If it contains *, it must also contain numbers. Capital letter "X" can be used as a wildcard, but small letter "x" cannot be used. |
| Trigger Information |
| Application Name | From the drop-down list, choose the application to associate with the trigger. |
| Advanced Trigger Information (available only if you click Show More ) |
| Enabled | Click a radio button to choose the required option: Yes— Enable the trigger (default) No— Disable the trigger |
| Idle Timeout (in ms) | The number of milliseconds (ms) the system waits before rejecting the SIP request for this trigger. |
| Override Media Termination | Click a radio button to choose the required options: Yes— Override media termination. No— Enable media termination (default). If you select Yes, two panes open: Selected Dialog Groups — displays the default or selected group. Note You must not change the default Selected Dialog Group associated with the application. Available Dialog Groups — displays the configured dialog. | Note | You must not change the default Selected Dialog Group associated with the application. |
| Note | You must not change the default Selected Dialog Group associated with the application. |
| Description | Click the Tab key to populate it. |

| Note | The trigger cannot contain only a wildcard character (*). If it contains *, it must also contain numbers. Capital letter "X" can be used as a wildcard, but small letter "x" cannot be used. |
|---|---|

| Note | You must not change the default Selected Dialog Group associated with the application. |
|---|---|

| Step 1 | From the Cisco VVB Administration menu bar, choose Subsystems > SIP Telephony > SIP Properties . |
|---|---|
| Step 2 | Select the Enable radio button and click Update . |

| Step 1 | From the Cisco VVB Administration menu bar, choose Subsystems > SIP Telephony > SIP RAI . |
|---|---|
| Step 2 | On the SIP RAI Configuration page, click Add New . |
| Step 3 | Enter the
                                       			 following fields: Field Default Value / Range Description Server Name Hostname or IP address of SIP server. Port 5060 Range: 1 to 65535 SIP server port number for communication. Interval 60 Range: 30 to 86400 (in seconds) Interval time to send RAI reports. | Field | Default Value / Range | Description | Server Name |  | Hostname or IP address of SIP server. | Port | 5060 Range: 1 to 65535 | SIP server port number for communication. | Interval | 60 Range: 30 to 86400 (in seconds) | Interval time to send RAI reports. |
| Field | Default Value / Range | Description |
| Server Name |  | Hostname or IP address of SIP server. |
| Port | 5060 Range: 1 to 65535 | SIP server port number for communication. |
| Interval | 60 Range: 30 to 86400 (in seconds) | Interval time to send RAI reports. |
| Step 4 | Click Add to add a SIP server. |
| Step 5 | (Optional) To update a server port or interval time, click the server name and update the Port and Interval fields. |
| Step 6 | (Optional) To delete a server, click the Delete icon present on the SIP RAI List or from the update server page. |

| Field | Default Value / Range | Description |
|---|---|---|
| Server Name |  | Hostname or IP address of SIP server. |
| Port | 5060 Range: 1 to 65535 | SIP server port number for communication. |
| Interval | 60 Range: 30 to 86400 (in seconds) | Interval time to send RAI reports. |

| Note | Only G711 codec is supported for ASR and TTS integrations. |
|---|---|

| Note | For more information about supported speech servers for Cisco VVB, see the Solutions Compatibility Matrix available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html . |
|---|---|

| Step 1 | From the Cisco VVB Administration menu bar, choose Subsystems > Speech Servers > ASR Servers . Column Description Server Name Hostname or IP address of the ASR server. Note ASR server deployment over WAN is not supported in Cisco VVB. Place the ASR server in the same LAN as Cisco VVB. You need
                                                                     to specify the ASR server hostname or IP address that is local with Cisco VVB node while installing the ASR server software
                                                                     in this field. Port Port number used to connect to a Speech server. Status Status or state of the server. | Column | Description | Server Name | Hostname or IP address of the ASR server. Note ASR server deployment over WAN is not supported in Cisco VVB. Place the ASR server in the same LAN as Cisco VVB. You need
                                                                     to specify the ASR server hostname or IP address that is local with Cisco VVB node while installing the ASR server software
                                                                     in this field. | Note | ASR server deployment over WAN is not supported in Cisco VVB. Place the ASR server in the same LAN as Cisco VVB. You need
                                                                     to specify the ASR server hostname or IP address that is local with Cisco VVB node while installing the ASR server software
                                                                     in this field. | Port | Port number used to connect to a Speech server. | Status | Status or state of the server. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Column | Description |
| Server Name | Hostname or IP address of the ASR server. Note ASR server deployment over WAN is not supported in Cisco VVB. Place the ASR server in the same LAN as Cisco VVB. You need
                                                                     to specify the ASR server hostname or IP address that is local with Cisco VVB node while installing the ASR server software
                                                                     in this field. | Note | ASR server deployment over WAN is not supported in Cisco VVB. Place the ASR server in the same LAN as Cisco VVB. You need
                                                                     to specify the ASR server hostname or IP address that is local with Cisco VVB node while installing the ASR server software
                                                                     in this field. |
| Note | ASR server deployment over WAN is not supported in Cisco VVB. Place the ASR server in the same LAN as Cisco VVB. You need
                                                                     to specify the ASR server hostname or IP address that is local with Cisco VVB node while installing the ASR server software
                                                                     in this field. |
| Port | Port number used to connect to a Speech server. |
| Status | Status or state of the server. |
| Step 2 | Click the Add New button to provision a new ASR Server. |
| Step 3 | Enter the following fields: Field Description Server Name Hostname or IP address of the ASR server. Port Number Port numbers that are used to connect to a Speech server. The default value for MRCPv1 is 4900 and for MRCPv2 is 5060. Note If the administrator has configured any other the port value for MRCP/ASR servers, then use the same port value here. Do not
                                                                     use these default values. Whenever the administrator changes from MRCP protocol, ensure ASR server is deleted and re-created
                                                                     with the appropriate port values. | Field | Description | Server Name | Hostname or IP address of the ASR server. | Port Number | Port numbers that are used to connect to a Speech server. The default value for MRCPv1 is 4900 and for MRCPv2 is 5060. Note If the administrator has configured any other the port value for MRCP/ASR servers, then use the same port value here. Do not
                                                                     use these default values. Whenever the administrator changes from MRCP protocol, ensure ASR server is deleted and re-created
                                                                     with the appropriate port values. | Note | If the administrator has configured any other the port value for MRCP/ASR servers, then use the same port value here. Do not
                                                                     use these default values. Whenever the administrator changes from MRCP protocol, ensure ASR server is deleted and re-created
                                                                     with the appropriate port values. |
| Field | Description |
| Server Name | Hostname or IP address of the ASR server. |
| Port Number | Port numbers that are used to connect to a Speech server. The default value for MRCPv1 is 4900 and for MRCPv2 is 5060. Note If the administrator has configured any other the port value for MRCP/ASR servers, then use the same port value here. Do not
                                                                     use these default values. Whenever the administrator changes from MRCP protocol, ensure ASR server is deleted and re-created
                                                                     with the appropriate port values. | Note | If the administrator has configured any other the port value for MRCP/ASR servers, then use the same port value here. Do not
                                                                     use these default values. Whenever the administrator changes from MRCP protocol, ensure ASR server is deleted and re-created
                                                                     with the appropriate port values. |
| Note | If the administrator has configured any other the port value for MRCP/ASR servers, then use the same port value here. Do not
                                                                     use these default values. Whenever the administrator changes from MRCP protocol, ensure ASR server is deleted and re-created
                                                                     with the appropriate port values. |
| Step 4 | Click Add to apply the changes. |
| Step 5 | (Optional)
                                          			 Click the Refresh button to refresh the status of the server. |

| Column | Description |
|---|---|
| Server Name | Hostname or IP address of the ASR server. Note ASR server deployment over WAN is not supported in Cisco VVB. Place the ASR server in the same LAN as Cisco VVB. You need
                                                                     to specify the ASR server hostname or IP address that is local with Cisco VVB node while installing the ASR server software
                                                                     in this field. | Note | ASR server deployment over WAN is not supported in Cisco VVB. Place the ASR server in the same LAN as Cisco VVB. You need
                                                                     to specify the ASR server hostname or IP address that is local with Cisco VVB node while installing the ASR server software
                                                                     in this field. |
| Note | ASR server deployment over WAN is not supported in Cisco VVB. Place the ASR server in the same LAN as Cisco VVB. You need
                                                                     to specify the ASR server hostname or IP address that is local with Cisco VVB node while installing the ASR server software
                                                                     in this field. |
| Port | Port number used to connect to a Speech server. |
| Status | Status or state of the server. |

| Note | ASR server deployment over WAN is not supported in Cisco VVB. Place the ASR server in the same LAN as Cisco VVB. You need
                                                                     to specify the ASR server hostname or IP address that is local with Cisco VVB node while installing the ASR server software
                                                                     in this field. |
|---|---|

| Field | Description |
|---|---|
| Server Name | Hostname or IP address of the ASR server. |
| Port Number | Port numbers that are used to connect to a Speech server. The default value for MRCPv1 is 4900 and for MRCPv2 is 5060. Note If the administrator has configured any other the port value for MRCP/ASR servers, then use the same port value here. Do not
                                                                     use these default values. Whenever the administrator changes from MRCP protocol, ensure ASR server is deleted and re-created
                                                                     with the appropriate port values. | Note | If the administrator has configured any other the port value for MRCP/ASR servers, then use the same port value here. Do not
                                                                     use these default values. Whenever the administrator changes from MRCP protocol, ensure ASR server is deleted and re-created
                                                                     with the appropriate port values. |
| Note | If the administrator has configured any other the port value for MRCP/ASR servers, then use the same port value here. Do not
                                                                     use these default values. Whenever the administrator changes from MRCP protocol, ensure ASR server is deleted and re-created
                                                                     with the appropriate port values. |

| Note | If the administrator has configured any other the port value for MRCP/ASR servers, then use the same port value here. Do not
                                                                     use these default values. Whenever the administrator changes from MRCP protocol, ensure ASR server is deleted and re-created
                                                                     with the appropriate port values. |
|---|---|

| Step 1 | From the Cisco VVB Administration menu bar, choose Subsystems > Speech Servers > TTS Servers . The TTS Server Configuration web page opens displaying a list of previously configured servers, if applicable, with the following
                                             information: Column Description Server Name Hostname or IP address of the TTS server. Note TTS server deployment over WAN is not supported in Cisco VVB. In other words, the TTS servers must be in the same LAN as Cisco
                                                                     VVB. Therefore, you need to specify the TTS server hostname or IP address that is local with Cisco VVB node while installing
                                                                     the TTS server software in this field. Port Number Port number used to connect to a Speech server. Status Status or state of the server. | Column | Description | Server Name | Hostname or IP address of the TTS server. Note TTS server deployment over WAN is not supported in Cisco VVB. In other words, the TTS servers must be in the same LAN as Cisco
                                                                     VVB. Therefore, you need to specify the TTS server hostname or IP address that is local with Cisco VVB node while installing
                                                                     the TTS server software in this field. | Note | TTS server deployment over WAN is not supported in Cisco VVB. In other words, the TTS servers must be in the same LAN as Cisco
                                                                     VVB. Therefore, you need to specify the TTS server hostname or IP address that is local with Cisco VVB node while installing
                                                                     the TTS server software in this field. | Port Number | Port number used to connect to a Speech server. | Status | Status or state of the server. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Column | Description |
| Server Name | Hostname or IP address of the TTS server. Note TTS server deployment over WAN is not supported in Cisco VVB. In other words, the TTS servers must be in the same LAN as Cisco
                                                                     VVB. Therefore, you need to specify the TTS server hostname or IP address that is local with Cisco VVB node while installing
                                                                     the TTS server software in this field. | Note | TTS server deployment over WAN is not supported in Cisco VVB. In other words, the TTS servers must be in the same LAN as Cisco
                                                                     VVB. Therefore, you need to specify the TTS server hostname or IP address that is local with Cisco VVB node while installing
                                                                     the TTS server software in this field. |
| Note | TTS server deployment over WAN is not supported in Cisco VVB. In other words, the TTS servers must be in the same LAN as Cisco
                                                                     VVB. Therefore, you need to specify the TTS server hostname or IP address that is local with Cisco VVB node while installing
                                                                     the TTS server software in this field. |
| Port Number | Port number used to connect to a Speech server. |
| Status | Status or state of the server. |
| Step 2 | Click the Add New button to provision a new TTS Server. |
| Step 3 | Enter the following fields: Field Description Server Name Hostname or IP address of the TTS server. Port Number Port number used to connect to a TTS server. The default value for MRCPv1 is 4900 and for MRCPv2 is 5060. Note If the administrator has configured any other the port value for MRCP/TTS servers then use the same port value here, do not
                                                                     use these default values. Whenever the administrator changes from MRCP protocol, ensure TTS server are deleted and recreated with appropriate port values. | Field | Description | Server Name | Hostname or IP address of the TTS server. | Port Number | Port number used to connect to a TTS server. The default value for MRCPv1 is 4900 and for MRCPv2 is 5060. Note If the administrator has configured any other the port value for MRCP/TTS servers then use the same port value here, do not
                                                                     use these default values. Whenever the administrator changes from MRCP protocol, ensure TTS server are deleted and recreated with appropriate port values. | Note | If the administrator has configured any other the port value for MRCP/TTS servers then use the same port value here, do not
                                                                     use these default values. Whenever the administrator changes from MRCP protocol, ensure TTS server are deleted and recreated with appropriate port values. |
| Field | Description |
| Server Name | Hostname or IP address of the TTS server. |
| Port Number | Port number used to connect to a TTS server. The default value for MRCPv1 is 4900 and for MRCPv2 is 5060. Note If the administrator has configured any other the port value for MRCP/TTS servers then use the same port value here, do not
                                                                     use these default values. Whenever the administrator changes from MRCP protocol, ensure TTS server are deleted and recreated with appropriate port values. | Note | If the administrator has configured any other the port value for MRCP/TTS servers then use the same port value here, do not
                                                                     use these default values. Whenever the administrator changes from MRCP protocol, ensure TTS server are deleted and recreated with appropriate port values. |
| Note | If the administrator has configured any other the port value for MRCP/TTS servers then use the same port value here, do not
                                                                     use these default values. Whenever the administrator changes from MRCP protocol, ensure TTS server are deleted and recreated with appropriate port values. |
| Step 4 | Click Add to apply the changes. |
| Step 5 | (Optional) Click the Refresh button to refresh the status of the server. |

| Column | Description |
|---|---|
| Server Name | Hostname or IP address of the TTS server. Note TTS server deployment over WAN is not supported in Cisco VVB. In other words, the TTS servers must be in the same LAN as Cisco
                                                                     VVB. Therefore, you need to specify the TTS server hostname or IP address that is local with Cisco VVB node while installing
                                                                     the TTS server software in this field. | Note | TTS server deployment over WAN is not supported in Cisco VVB. In other words, the TTS servers must be in the same LAN as Cisco
                                                                     VVB. Therefore, you need to specify the TTS server hostname or IP address that is local with Cisco VVB node while installing
                                                                     the TTS server software in this field. |
| Note | TTS server deployment over WAN is not supported in Cisco VVB. In other words, the TTS servers must be in the same LAN as Cisco
                                                                     VVB. Therefore, you need to specify the TTS server hostname or IP address that is local with Cisco VVB node while installing
                                                                     the TTS server software in this field. |
| Port Number | Port number used to connect to a Speech server. |
| Status | Status or state of the server. |

| Note | TTS server deployment over WAN is not supported in Cisco VVB. In other words, the TTS servers must be in the same LAN as Cisco
                                                                     VVB. Therefore, you need to specify the TTS server hostname or IP address that is local with Cisco VVB node while installing
                                                                     the TTS server software in this field. |
|---|---|

| Field | Description |
|---|---|
| Server Name | Hostname or IP address of the TTS server. |
| Port Number | Port number used to connect to a TTS server. The default value for MRCPv1 is 4900 and for MRCPv2 is 5060. Note If the administrator has configured any other the port value for MRCP/TTS servers then use the same port value here, do not
                                                                     use these default values. Whenever the administrator changes from MRCP protocol, ensure TTS server are deleted and recreated with appropriate port values. | Note | If the administrator has configured any other the port value for MRCP/TTS servers then use the same port value here, do not
                                                                     use these default values. Whenever the administrator changes from MRCP protocol, ensure TTS server are deleted and recreated with appropriate port values. |
| Note | If the administrator has configured any other the port value for MRCP/TTS servers then use the same port value here, do not
                                                                     use these default values. Whenever the administrator changes from MRCP protocol, ensure TTS server are deleted and recreated with appropriate port values. |

| Note | If the administrator has configured any other the port value for MRCP/TTS servers then use the same port value here, do not
                                                                     use these default values. Whenever the administrator changes from MRCP protocol, ensure TTS server are deleted and recreated with appropriate port values. |
|---|---|

| Note | Use Prompt Management to store prompt WAV files locally. It helps you avoid any fetch latency while playing the large prompt.
                                          You can also use it to override the system default prompts. |
|---|---|

| Step 1 | From Cisco
                                          			 VVBAdministration menu bar, choose Applications > Prompt
                                                				  Management . |
|---|---|
| Step 2 | The Prompt Management page opens to display the
                                          			 following fields. Field Description Name Name
                                                         							 of the folder. Size The
                                                         							 size of the prompt file in kilobytes (KB). Note This column is usually blank on the root page because the items
                                                                        								  on this page are usually folders. The maximum limit for the uploaded prompt file is 20MB. Date
                                                         							 Modified The date and time when the document was last uploaded or changed along with the time zone. Modified By The user ID of the person who made these modifications. Delete To
                                                         							 remove the folder and its contents from the repository. Rename To
                                                         							 rename the folder in the repository. Refresh To
                                                         							 refresh the folder in the repository. Create New Folder To create a new subfolder. Upload Prompt To upload a prompt (.wav/.au) file or prompts packaged in a zip. Note The maximum limit for the uploaded prompt file is 20MB. | Field | Description | Name | Name
                                                         							 of the folder. | Size | The
                                                         							 size of the prompt file in kilobytes (KB). Note This column is usually blank on the root page because the items
                                                                        								  on this page are usually folders. The maximum limit for the uploaded prompt file is 20MB. | Note | This column is usually blank on the root page because the items
                                                                        								  on this page are usually folders. The maximum limit for the uploaded prompt file is 20MB. | Date
                                                         							 Modified | The date and time when the document was last uploaded or changed along with the time zone. | Modified By | The user ID of the person who made these modifications. | Delete | To
                                                         							 remove the folder and its contents from the repository. | Rename | To
                                                         							 rename the folder in the repository. | Refresh | To
                                                         							 refresh the folder in the repository. | Create New Folder | To create a new subfolder. | Upload Prompt | To upload a prompt (.wav/.au) file or prompts packaged in a zip. Note The maximum limit for the uploaded prompt file is 20MB. | Note | The maximum limit for the uploaded prompt file is 20MB. |
| Field | Description |
| Name | Name
                                                         							 of the folder. |
| Size | The
                                                         							 size of the prompt file in kilobytes (KB). Note This column is usually blank on the root page because the items
                                                                        								  on this page are usually folders. The maximum limit for the uploaded prompt file is 20MB. | Note | This column is usually blank on the root page because the items
                                                                        								  on this page are usually folders. The maximum limit for the uploaded prompt file is 20MB. |
| Note | This column is usually blank on the root page because the items
                                                                        								  on this page are usually folders. The maximum limit for the uploaded prompt file is 20MB. |
| Date
                                                         							 Modified | The date and time when the document was last uploaded or changed along with the time zone. |
| Modified By | The user ID of the person who made these modifications. |
| Delete | To
                                                         							 remove the folder and its contents from the repository. |
| Rename | To
                                                         							 rename the folder in the repository. |
| Refresh | To
                                                         							 refresh the folder in the repository. |
| Create New Folder | To create a new subfolder. |
| Upload Prompt | To upload a prompt (.wav/.au) file or prompts packaged in a zip. Note The maximum limit for the uploaded prompt file is 20MB. | Note | The maximum limit for the uploaded prompt file is 20MB. |
| Note | The maximum limit for the uploaded prompt file is 20MB. |

| Field | Description |
|---|---|
| Name | Name
                                                         							 of the folder. |
| Size | The
                                                         							 size of the prompt file in kilobytes (KB). Note This column is usually blank on the root page because the items
                                                                        								  on this page are usually folders. The maximum limit for the uploaded prompt file is 20MB. | Note | This column is usually blank on the root page because the items
                                                                        								  on this page are usually folders. The maximum limit for the uploaded prompt file is 20MB. |
| Note | This column is usually blank on the root page because the items
                                                                        								  on this page are usually folders. The maximum limit for the uploaded prompt file is 20MB. |
| Date
                                                         							 Modified | The date and time when the document was last uploaded or changed along with the time zone. |
| Modified By | The user ID of the person who made these modifications. |
| Delete | To
                                                         							 remove the folder and its contents from the repository. |
| Rename | To
                                                         							 rename the folder in the repository. |
| Refresh | To
                                                         							 refresh the folder in the repository. |
| Create New Folder | To create a new subfolder. |
| Upload Prompt | To upload a prompt (.wav/.au) file or prompts packaged in a zip. Note The maximum limit for the uploaded prompt file is 20MB. | Note | The maximum limit for the uploaded prompt file is 20MB. |
| Note | The maximum limit for the uploaded prompt file is 20MB. |

| Note | This column is usually blank on the root page because the items
                                                                        								  on this page are usually folders. The maximum limit for the uploaded prompt file is 20MB. |
|---|---|

| Note | The maximum limit for the uploaded prompt file is 20MB. |
|---|---|

| Note | Custom
                                                         						ringtone cannot be named to ringback.wav. The
                                                         						audio file in Cisco VVB and the filename you entered in CVP under DNP is
                                                         						case-sensitive (should be same with .wav extension) |
|---|---|

| Note | This release supports only TLS 1.2. For more information, see Contact Center Enterprise Solution Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/tsd-products-support-series-home.html . |
|---|---|

| Step 1 | From Cisco VVB
                                          			 Administration menu bar, choose System > SystemParameters . |
|---|---|
| Step 2 | To update,
                                          			 click the Update icon in the toolbar or the Update button at the bottom of the window. The
                                             				System Parameters Configuration web page displays the following fields. Table 1. System
                                                   				Parameters Configuration Field Description Generic System
                                                            							 Parameter System Time Zone The
                                                         						  system time zone of Cisco VVB server configured during installation. Media Parameters Codec G711 and G729 audio
                                                         						  codecs with sampling rate 8K are supported. Default: G711U MRCP
                                                         						  Version Select the MRCP version to communicate between Nuance and Cisco VVB. Default: MRCPv2 Note The default value for ASR/TTS server port for MRCPv1 is 4900 and for MRCPv2 is 5060. Whenever the administrator changes from
                                                                           MRCP protocol, ensure ASR/TTS server is deleted and re-created with appropriate port values. ASR-TTS service is not supported using G729 codec; therefore,
                                                                           								  MRCP is not applicable. User
                                                         						  Prompts override System Prompts When
                                                         						  enabled, custom recorded prompt files can be uploaded to the appropriate
                                                         						  language directory under Prompt Management . The custom prompts override the
                                                         						  system default prompt files for that language. By default, this feature is
                                                         						  disabled. Note For overriding the system default prompt files for ringtone
                                                                     							 application: Create a new folder named vb . Select Applications > Prompt Management and click Create New Folder . Upload the custom ringtone. Choose Applications > Prompt Management and click Upload Prompt . Upload custom ringtone wav file(named same as ringback.wav ) under folder vb . Security Parameters TLS(SIP) TLS (SIP) is disabled by default. When enabled, this setting secures SIP signaling on the IVR leg.  TLS (SIP) version supported
                                                         is TLSv1.2, and the default cipher suites are TLS_RSA_WITH_AES_128_CBC_SHA and TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 . Note Multiple clients connecting to Cisco VVB cannot combine RSA and ECDHE cipher suites. They must use either RSA or ECDHE cipher
                                                                     suites. SSL certificates need to be exchanged between VVB and any SIP endpoint (CVP, Ingress Gateway, and so on.) to talk over TLS.
                                                         For more details on this configuration, see the Upgrade Unified CVP > Postupgrade Tasks > Manual Configuration of Unified CVP Properties section in the Installation and Upgrade Guide for Cisco Unified Customer Voice Portal , Release 15.0(1) available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html . Note Cisco VVB Engine restart is required after a change to this configuration. Supported TLS (SIP) Versions This allows you to select the version of TLS (SIP). TLS (SIP) version supported is TLSv1.2. When
                                                         						  you select a given TLS (SIP) version, Cisco VVB will support SIP TLS requests
                                                         						  for this version and the higher supported versions. Note Supported TLS (SIP) Versions is available only if TLS (SIP) is
                                                                           								  enabled. Cisco VVB Engine restart is required after a change to this
                                                                           								  configuration. The supported TLS (SIP) versions as client or server for securing SIP signaling in the IVR leg can alternatively be specified
                                                                           via the CLI command set tls server min-version as documented in the Cisco Unified Contact Center Express Administration and Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-installation-and-configuration-guides-list.html Cipher Configuration This field defines the ciphers that are supported by Cisco VVB with key size lesser than or equal to 2048 bits. The following ciphers are pre-populated. TLS_RSA_WITH_AES_128_CBC_SHA TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 Note Cipher configuration is available only if TLS (SIP) is enabled. You must restart the Cisco VVB engine after modifying the cipher configuration. If you are using CUBE version 16.6 and higher, you must manually change the crypto suite to 128/256 by enabling CLI on the dial-peer towards VVB as shown: voice class srtp-crypto 1
	crypto 1 AES_CM_128_HMAC_SHA1_32

dial-peer voice xxxx voip (Dial-peer to VVB srtp)
    ...
    voice-class sip srtp-crypto 1 Note To avoid any unsupported cipher issues during the upgrade to Cisco Unified CVP Release 15.0, it is recommended to restart
                                                                     the Cisco VVB engine to ensure a smooth and successful cipher negotiation process. SRTP SRTP is disabled by default. When SRTP is disabled, the media is not encrypted. When SRTP is enabled, it secures the IVR leg. SRTP negotiates between AES_CM_128_HMAC_SHA1_32 or AES_CM_128_HMAC_SHA1_80 crypto-suites, ensuring compatibility and successful
                                                                  encryption of media streams. When SRTP uses a crypto-suite (for example, AES_CM_128_HMAC_SHA1_32), and the incoming request also uses the same crypto-suite,
                                                                     the request is accepted, and the media stream is successfully encrypted using AES_CM_128_HMAC_SHA1_32. When SRTP uses a crypto-suite (for example, AES_CM_128_HMAC_SHA1_32), but the incoming request uses a different one (for example,
                                                                     AES_CM_128_HMAC_SHA1_80) or vice versa, the request will be denied and considered unsupported because the encryption methods
                                                                     do not match resulting in an error response. Note Multiple ciphers may be included in a request; however, the negotiation will only proceed with the cipher configured in the
                                                                                 system, which will either be AES_CM_128_HMAC_SHA1_32 or AES_CM_128_HMAC_SHA1_80. If neither of these ciphers match the request, it will be considered unsupported. When Allow RTP (Mixed mode) check box is checked, the system accepts both SRTP and RTP call flows. This check box can be checked only when SRTP is enabled. Note SRTP is available only if TLS (SIP) is enabled. Check the Allow RTP (Mixed mode) check box if device is configured to work in the RTP mode and interacts with MRCP ARS-TTS servers. For more details on mixed mode call flow scenarios, see the Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html . Cisco VVB engine restart is required after a change to this configuration. SRTP is not supported with VVB XU (Export Unrestricted) software image releases. System Port Parameter RMI Port The port number used by Cisco VVB to serve Remote Method Invocation (RMI) requests. This field is mandatory. Default: 6999 HTTPS Client TLS
                                                				  Configuration The supported TLS versions as client for securing HTTPS signaling to fetch the VXML applications from VXML server use the
                                             CLI command set tls client min-version in Cisco Unified Contact Center Express Administration and Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html | Field | Description | Generic System
                                                            							 Parameter | System Time Zone | The
                                                         						  system time zone of Cisco VVB server configured during installation. | Media Parameters | Codec | G711 and G729 audio
                                                         						  codecs with sampling rate 8K are supported. Default: G711U | MRCP
                                                         						  Version | Select the MRCP version to communicate between Nuance and Cisco VVB. Default: MRCPv2 Note The default value for ASR/TTS server port for MRCPv1 is 4900 and for MRCPv2 is 5060. Whenever the administrator changes from
                                                                           MRCP protocol, ensure ASR/TTS server is deleted and re-created with appropriate port values. ASR-TTS service is not supported using G729 codec; therefore,
                                                                           								  MRCP is not applicable. | Note | The default value for ASR/TTS server port for MRCPv1 is 4900 and for MRCPv2 is 5060. Whenever the administrator changes from
                                                                           MRCP protocol, ensure ASR/TTS server is deleted and re-created with appropriate port values. ASR-TTS service is not supported using G729 codec; therefore,
                                                                           								  MRCP is not applicable. | User
                                                         						  Prompts override System Prompts | When
                                                         						  enabled, custom recorded prompt files can be uploaded to the appropriate
                                                         						  language directory under Prompt Management . The custom prompts override the
                                                         						  system default prompt files for that language. By default, this feature is
                                                         						  disabled. Note For overriding the system default prompt files for ringtone
                                                                     							 application: Create a new folder named vb . Select Applications > Prompt Management and click Create New Folder . Upload the custom ringtone. Choose Applications > Prompt Management and click Upload Prompt . Upload custom ringtone wav file(named same as ringback.wav ) under folder vb . | Note | For overriding the system default prompt files for ringtone
                                                                     							 application: Create a new folder named vb . Select Applications > Prompt Management and click Create New Folder . Upload the custom ringtone. Choose Applications > Prompt Management and click Upload Prompt . Upload custom ringtone wav file(named same as ringback.wav ) under folder vb . | Security Parameters | TLS(SIP) | TLS (SIP) is disabled by default. When enabled, this setting secures SIP signaling on the IVR leg.  TLS (SIP) version supported
                                                         is TLSv1.2, and the default cipher suites are TLS_RSA_WITH_AES_128_CBC_SHA and TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 . Note Multiple clients connecting to Cisco VVB cannot combine RSA and ECDHE cipher suites. They must use either RSA or ECDHE cipher
                                                                     suites. SSL certificates need to be exchanged between VVB and any SIP endpoint (CVP, Ingress Gateway, and so on.) to talk over TLS.
                                                         For more details on this configuration, see the Upgrade Unified CVP > Postupgrade Tasks > Manual Configuration of Unified CVP Properties section in the Installation and Upgrade Guide for Cisco Unified Customer Voice Portal , Release 15.0(1) available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html . Note Cisco VVB Engine restart is required after a change to this configuration. | Note | Multiple clients connecting to Cisco VVB cannot combine RSA and ECDHE cipher suites. They must use either RSA or ECDHE cipher
                                                                     suites. | Note | Cisco VVB Engine restart is required after a change to this configuration. | Supported TLS (SIP) Versions | This allows you to select the version of TLS (SIP). TLS (SIP) version supported is TLSv1.2. When
                                                         						  you select a given TLS (SIP) version, Cisco VVB will support SIP TLS requests
                                                         						  for this version and the higher supported versions. Note Supported TLS (SIP) Versions is available only if TLS (SIP) is
                                                                           								  enabled. Cisco VVB Engine restart is required after a change to this
                                                                           								  configuration. The supported TLS (SIP) versions as client or server for securing SIP signaling in the IVR leg can alternatively be specified
                                                                           via the CLI command set tls server min-version as documented in the Cisco Unified Contact Center Express Administration and Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-installation-and-configuration-guides-list.html | Note | Supported TLS (SIP) Versions is available only if TLS (SIP) is
                                                                           								  enabled. Cisco VVB Engine restart is required after a change to this
                                                                           								  configuration. The supported TLS (SIP) versions as client or server for securing SIP signaling in the IVR leg can alternatively be specified
                                                                           via the CLI command set tls server min-version as documented in the Cisco Unified Contact Center Express Administration and Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-installation-and-configuration-guides-list.html | Cipher Configuration | This field defines the ciphers that are supported by Cisco VVB with key size lesser than or equal to 2048 bits. The following ciphers are pre-populated. TLS_RSA_WITH_AES_128_CBC_SHA TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 Note Cipher configuration is available only if TLS (SIP) is enabled. You must restart the Cisco VVB engine after modifying the cipher configuration. If you are using CUBE version 16.6 and higher, you must manually change the crypto suite to 128/256 by enabling CLI on the dial-peer towards VVB as shown: voice class srtp-crypto 1
	crypto 1 AES_CM_128_HMAC_SHA1_32

dial-peer voice xxxx voip (Dial-peer to VVB srtp)
    ...
    voice-class sip srtp-crypto 1 Note To avoid any unsupported cipher issues during the upgrade to Cisco Unified CVP Release 15.0, it is recommended to restart
                                                                     the Cisco VVB engine to ensure a smooth and successful cipher negotiation process. | Note | Cipher configuration is available only if TLS (SIP) is enabled. You must restart the Cisco VVB engine after modifying the cipher configuration. If you are using CUBE version 16.6 and higher, you must manually change the crypto suite to 128/256 by enabling CLI on the dial-peer towards VVB as shown: voice class srtp-crypto 1
	crypto 1 AES_CM_128_HMAC_SHA1_32

dial-peer voice xxxx voip (Dial-peer to VVB srtp)
    ...
    voice-class sip srtp-crypto 1 | Note | To avoid any unsupported cipher issues during the upgrade to Cisco Unified CVP Release 15.0, it is recommended to restart
                                                                     the Cisco VVB engine to ensure a smooth and successful cipher negotiation process. | SRTP | SRTP is disabled by default. When SRTP is disabled, the media is not encrypted. When SRTP is enabled, it secures the IVR leg. SRTP negotiates between AES_CM_128_HMAC_SHA1_32 or AES_CM_128_HMAC_SHA1_80 crypto-suites, ensuring compatibility and successful
                                                                  encryption of media streams. When SRTP uses a crypto-suite (for example, AES_CM_128_HMAC_SHA1_32), and the incoming request also uses the same crypto-suite,
                                                                     the request is accepted, and the media stream is successfully encrypted using AES_CM_128_HMAC_SHA1_32. When SRTP uses a crypto-suite (for example, AES_CM_128_HMAC_SHA1_32), but the incoming request uses a different one (for example,
                                                                     AES_CM_128_HMAC_SHA1_80) or vice versa, the request will be denied and considered unsupported because the encryption methods
                                                                     do not match resulting in an error response. Note Multiple ciphers may be included in a request; however, the negotiation will only proceed with the cipher configured in the
                                                                                 system, which will either be AES_CM_128_HMAC_SHA1_32 or AES_CM_128_HMAC_SHA1_80. If neither of these ciphers match the request, it will be considered unsupported. When Allow RTP (Mixed mode) check box is checked, the system accepts both SRTP and RTP call flows. This check box can be checked only when SRTP is enabled. Note SRTP is available only if TLS (SIP) is enabled. Check the Allow RTP (Mixed mode) check box if device is configured to work in the RTP mode and interacts with MRCP ARS-TTS servers. For more details on mixed mode call flow scenarios, see the Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html . Cisco VVB engine restart is required after a change to this configuration. SRTP is not supported with VVB XU (Export Unrestricted) software image releases. | Note | Multiple ciphers may be included in a request; however, the negotiation will only proceed with the cipher configured in the
                                                                                 system, which will either be AES_CM_128_HMAC_SHA1_32 or AES_CM_128_HMAC_SHA1_80. If neither of these ciphers match the request, it will be considered unsupported. | Note | SRTP is available only if TLS (SIP) is enabled. Check the Allow RTP (Mixed mode) check box if device is configured to work in the RTP mode and interacts with MRCP ARS-TTS servers. For more details on mixed mode call flow scenarios, see the Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html . Cisco VVB engine restart is required after a change to this configuration. SRTP is not supported with VVB XU (Export Unrestricted) software image releases. | System Port Parameter | RMI Port | The port number used by Cisco VVB to serve Remote Method Invocation (RMI) requests. This field is mandatory. Default: 6999 |
| Field | Description |
| Generic System
                                                            							 Parameter |
| System Time Zone | The
                                                         						  system time zone of Cisco VVB server configured during installation. |
| Media Parameters |
| Codec | G711 and G729 audio
                                                         						  codecs with sampling rate 8K are supported. Default: G711U |
| MRCP
                                                         						  Version | Select the MRCP version to communicate between Nuance and Cisco VVB. Default: MRCPv2 Note The default value for ASR/TTS server port for MRCPv1 is 4900 and for MRCPv2 is 5060. Whenever the administrator changes from
                                                                           MRCP protocol, ensure ASR/TTS server is deleted and re-created with appropriate port values. ASR-TTS service is not supported using G729 codec; therefore,
                                                                           								  MRCP is not applicable. | Note | The default value for ASR/TTS server port for MRCPv1 is 4900 and for MRCPv2 is 5060. Whenever the administrator changes from
                                                                           MRCP protocol, ensure ASR/TTS server is deleted and re-created with appropriate port values. ASR-TTS service is not supported using G729 codec; therefore,
                                                                           								  MRCP is not applicable. |
| Note | The default value for ASR/TTS server port for MRCPv1 is 4900 and for MRCPv2 is 5060. Whenever the administrator changes from
                                                                           MRCP protocol, ensure ASR/TTS server is deleted and re-created with appropriate port values. ASR-TTS service is not supported using G729 codec; therefore,
                                                                           								  MRCP is not applicable. |
| User
                                                         						  Prompts override System Prompts | When
                                                         						  enabled, custom recorded prompt files can be uploaded to the appropriate
                                                         						  language directory under Prompt Management . The custom prompts override the
                                                         						  system default prompt files for that language. By default, this feature is
                                                         						  disabled. Note For overriding the system default prompt files for ringtone
                                                                     							 application: Create a new folder named vb . Select Applications > Prompt Management and click Create New Folder . Upload the custom ringtone. Choose Applications > Prompt Management and click Upload Prompt . Upload custom ringtone wav file(named same as ringback.wav ) under folder vb . | Note | For overriding the system default prompt files for ringtone
                                                                     							 application: Create a new folder named vb . Select Applications > Prompt Management and click Create New Folder . Upload the custom ringtone. Choose Applications > Prompt Management and click Upload Prompt . Upload custom ringtone wav file(named same as ringback.wav ) under folder vb . |
| Note | For overriding the system default prompt files for ringtone
                                                                     							 application: Create a new folder named vb . Select Applications > Prompt Management and click Create New Folder . Upload the custom ringtone. Choose Applications > Prompt Management and click Upload Prompt . Upload custom ringtone wav file(named same as ringback.wav ) under folder vb . |
| Security Parameters |
| TLS(SIP) | TLS (SIP) is disabled by default. When enabled, this setting secures SIP signaling on the IVR leg.  TLS (SIP) version supported
                                                         is TLSv1.2, and the default cipher suites are TLS_RSA_WITH_AES_128_CBC_SHA and TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 . Note Multiple clients connecting to Cisco VVB cannot combine RSA and ECDHE cipher suites. They must use either RSA or ECDHE cipher
                                                                     suites. SSL certificates need to be exchanged between VVB and any SIP endpoint (CVP, Ingress Gateway, and so on.) to talk over TLS.
                                                         For more details on this configuration, see the Upgrade Unified CVP > Postupgrade Tasks > Manual Configuration of Unified CVP Properties section in the Installation and Upgrade Guide for Cisco Unified Customer Voice Portal , Release 15.0(1) available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html . Note Cisco VVB Engine restart is required after a change to this configuration. | Note | Multiple clients connecting to Cisco VVB cannot combine RSA and ECDHE cipher suites. They must use either RSA or ECDHE cipher
                                                                     suites. | Note | Cisco VVB Engine restart is required after a change to this configuration. |
| Note | Multiple clients connecting to Cisco VVB cannot combine RSA and ECDHE cipher suites. They must use either RSA or ECDHE cipher
                                                                     suites. |
| Note | Cisco VVB Engine restart is required after a change to this configuration. |
| Supported TLS (SIP) Versions | This allows you to select the version of TLS (SIP). TLS (SIP) version supported is TLSv1.2. When
                                                         						  you select a given TLS (SIP) version, Cisco VVB will support SIP TLS requests
                                                         						  for this version and the higher supported versions. Note Supported TLS (SIP) Versions is available only if TLS (SIP) is
                                                                           								  enabled. Cisco VVB Engine restart is required after a change to this
                                                                           								  configuration. The supported TLS (SIP) versions as client or server for securing SIP signaling in the IVR leg can alternatively be specified
                                                                           via the CLI command set tls server min-version as documented in the Cisco Unified Contact Center Express Administration and Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-installation-and-configuration-guides-list.html | Note | Supported TLS (SIP) Versions is available only if TLS (SIP) is
                                                                           								  enabled. Cisco VVB Engine restart is required after a change to this
                                                                           								  configuration. The supported TLS (SIP) versions as client or server for securing SIP signaling in the IVR leg can alternatively be specified
                                                                           via the CLI command set tls server min-version as documented in the Cisco Unified Contact Center Express Administration and Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-installation-and-configuration-guides-list.html |
| Note | Supported TLS (SIP) Versions is available only if TLS (SIP) is
                                                                           								  enabled. Cisco VVB Engine restart is required after a change to this
                                                                           								  configuration. The supported TLS (SIP) versions as client or server for securing SIP signaling in the IVR leg can alternatively be specified
                                                                           via the CLI command set tls server min-version as documented in the Cisco Unified Contact Center Express Administration and Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-installation-and-configuration-guides-list.html |
| Cipher Configuration | This field defines the ciphers that are supported by Cisco VVB with key size lesser than or equal to 2048 bits. The following ciphers are pre-populated. TLS_RSA_WITH_AES_128_CBC_SHA TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 Note Cipher configuration is available only if TLS (SIP) is enabled. You must restart the Cisco VVB engine after modifying the cipher configuration. If you are using CUBE version 16.6 and higher, you must manually change the crypto suite to 128/256 by enabling CLI on the dial-peer towards VVB as shown: voice class srtp-crypto 1
	crypto 1 AES_CM_128_HMAC_SHA1_32

dial-peer voice xxxx voip (Dial-peer to VVB srtp)
    ...
    voice-class sip srtp-crypto 1 Note To avoid any unsupported cipher issues during the upgrade to Cisco Unified CVP Release 15.0, it is recommended to restart
                                                                     the Cisco VVB engine to ensure a smooth and successful cipher negotiation process. | Note | Cipher configuration is available only if TLS (SIP) is enabled. You must restart the Cisco VVB engine after modifying the cipher configuration. If you are using CUBE version 16.6 and higher, you must manually change the crypto suite to 128/256 by enabling CLI on the dial-peer towards VVB as shown: voice class srtp-crypto 1
	crypto 1 AES_CM_128_HMAC_SHA1_32

dial-peer voice xxxx voip (Dial-peer to VVB srtp)
    ...
    voice-class sip srtp-crypto 1 | Note | To avoid any unsupported cipher issues during the upgrade to Cisco Unified CVP Release 15.0, it is recommended to restart
                                                                     the Cisco VVB engine to ensure a smooth and successful cipher negotiation process. |
| Note | Cipher configuration is available only if TLS (SIP) is enabled. You must restart the Cisco VVB engine after modifying the cipher configuration. If you are using CUBE version 16.6 and higher, you must manually change the crypto suite to 128/256 by enabling CLI on the dial-peer towards VVB as shown: voice class srtp-crypto 1
	crypto 1 AES_CM_128_HMAC_SHA1_32

dial-peer voice xxxx voip (Dial-peer to VVB srtp)
    ...
    voice-class sip srtp-crypto 1 |
| Note | To avoid any unsupported cipher issues during the upgrade to Cisco Unified CVP Release 15.0, it is recommended to restart
                                                                     the Cisco VVB engine to ensure a smooth and successful cipher negotiation process. |
| SRTP | SRTP is disabled by default. When SRTP is disabled, the media is not encrypted. When SRTP is enabled, it secures the IVR leg. SRTP negotiates between AES_CM_128_HMAC_SHA1_32 or AES_CM_128_HMAC_SHA1_80 crypto-suites, ensuring compatibility and successful
                                                                  encryption of media streams. When SRTP uses a crypto-suite (for example, AES_CM_128_HMAC_SHA1_32), and the incoming request also uses the same crypto-suite,
                                                                     the request is accepted, and the media stream is successfully encrypted using AES_CM_128_HMAC_SHA1_32. When SRTP uses a crypto-suite (for example, AES_CM_128_HMAC_SHA1_32), but the incoming request uses a different one (for example,
                                                                     AES_CM_128_HMAC_SHA1_80) or vice versa, the request will be denied and considered unsupported because the encryption methods
                                                                     do not match resulting in an error response. Note Multiple ciphers may be included in a request; however, the negotiation will only proceed with the cipher configured in the
                                                                                 system, which will either be AES_CM_128_HMAC_SHA1_32 or AES_CM_128_HMAC_SHA1_80. If neither of these ciphers match the request, it will be considered unsupported. When Allow RTP (Mixed mode) check box is checked, the system accepts both SRTP and RTP call flows. This check box can be checked only when SRTP is enabled. Note SRTP is available only if TLS (SIP) is enabled. Check the Allow RTP (Mixed mode) check box if device is configured to work in the RTP mode and interacts with MRCP ARS-TTS servers. For more details on mixed mode call flow scenarios, see the Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html . Cisco VVB engine restart is required after a change to this configuration. SRTP is not supported with VVB XU (Export Unrestricted) software image releases. | Note | Multiple ciphers may be included in a request; however, the negotiation will only proceed with the cipher configured in the
                                                                                 system, which will either be AES_CM_128_HMAC_SHA1_32 or AES_CM_128_HMAC_SHA1_80. If neither of these ciphers match the request, it will be considered unsupported. | Note | SRTP is available only if TLS (SIP) is enabled. Check the Allow RTP (Mixed mode) check box if device is configured to work in the RTP mode and interacts with MRCP ARS-TTS servers. For more details on mixed mode call flow scenarios, see the Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html . Cisco VVB engine restart is required after a change to this configuration. SRTP is not supported with VVB XU (Export Unrestricted) software image releases. |
| Note | Multiple ciphers may be included in a request; however, the negotiation will only proceed with the cipher configured in the
                                                                                 system, which will either be AES_CM_128_HMAC_SHA1_32 or AES_CM_128_HMAC_SHA1_80. If neither of these ciphers match the request, it will be considered unsupported. |
| Note | SRTP is available only if TLS (SIP) is enabled. Check the Allow RTP (Mixed mode) check box if device is configured to work in the RTP mode and interacts with MRCP ARS-TTS servers. For more details on mixed mode call flow scenarios, see the Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html . Cisco VVB engine restart is required after a change to this configuration. SRTP is not supported with VVB XU (Export Unrestricted) software image releases. |
| System Port Parameter |
| RMI Port | The port number used by Cisco VVB to serve Remote Method Invocation (RMI) requests. This field is mandatory. Default: 6999 |

| Field | Description |
|---|---|
| Generic System
                                                            							 Parameter |
| System Time Zone | The
                                                         						  system time zone of Cisco VVB server configured during installation. |
| Media Parameters |
| Codec | G711 and G729 audio
                                                         						  codecs with sampling rate 8K are supported. Default: G711U |
| MRCP
                                                         						  Version | Select the MRCP version to communicate between Nuance and Cisco VVB. Default: MRCPv2 Note The default value for ASR/TTS server port for MRCPv1 is 4900 and for MRCPv2 is 5060. Whenever the administrator changes from
                                                                           MRCP protocol, ensure ASR/TTS server is deleted and re-created with appropriate port values. ASR-TTS service is not supported using G729 codec; therefore,
                                                                           								  MRCP is not applicable. | Note | The default value for ASR/TTS server port for MRCPv1 is 4900 and for MRCPv2 is 5060. Whenever the administrator changes from
                                                                           MRCP protocol, ensure ASR/TTS server is deleted and re-created with appropriate port values. ASR-TTS service is not supported using G729 codec; therefore,
                                                                           								  MRCP is not applicable. |
| Note | The default value for ASR/TTS server port for MRCPv1 is 4900 and for MRCPv2 is 5060. Whenever the administrator changes from
                                                                           MRCP protocol, ensure ASR/TTS server is deleted and re-created with appropriate port values. ASR-TTS service is not supported using G729 codec; therefore,
                                                                           								  MRCP is not applicable. |
| User
                                                         						  Prompts override System Prompts | When
                                                         						  enabled, custom recorded prompt files can be uploaded to the appropriate
                                                         						  language directory under Prompt Management . The custom prompts override the
                                                         						  system default prompt files for that language. By default, this feature is
                                                         						  disabled. Note For overriding the system default prompt files for ringtone
                                                                     							 application: Create a new folder named vb . Select Applications > Prompt Management and click Create New Folder . Upload the custom ringtone. Choose Applications > Prompt Management and click Upload Prompt . Upload custom ringtone wav file(named same as ringback.wav ) under folder vb . | Note | For overriding the system default prompt files for ringtone
                                                                     							 application: Create a new folder named vb . Select Applications > Prompt Management and click Create New Folder . Upload the custom ringtone. Choose Applications > Prompt Management and click Upload Prompt . Upload custom ringtone wav file(named same as ringback.wav ) under folder vb . |
| Note | For overriding the system default prompt files for ringtone
                                                                     							 application: Create a new folder named vb . Select Applications > Prompt Management and click Create New Folder . Upload the custom ringtone. Choose Applications > Prompt Management and click Upload Prompt . Upload custom ringtone wav file(named same as ringback.wav ) under folder vb . |
| Security Parameters |
| TLS(SIP) | TLS (SIP) is disabled by default. When enabled, this setting secures SIP signaling on the IVR leg.  TLS (SIP) version supported
                                                         is TLSv1.2, and the default cipher suites are TLS_RSA_WITH_AES_128_CBC_SHA and TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 . Note Multiple clients connecting to Cisco VVB cannot combine RSA and ECDHE cipher suites. They must use either RSA or ECDHE cipher
                                                                     suites. SSL certificates need to be exchanged between VVB and any SIP endpoint (CVP, Ingress Gateway, and so on.) to talk over TLS.
                                                         For more details on this configuration, see the Upgrade Unified CVP > Postupgrade Tasks > Manual Configuration of Unified CVP Properties section in the Installation and Upgrade Guide for Cisco Unified Customer Voice Portal , Release 15.0(1) available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html . Note Cisco VVB Engine restart is required after a change to this configuration. | Note | Multiple clients connecting to Cisco VVB cannot combine RSA and ECDHE cipher suites. They must use either RSA or ECDHE cipher
                                                                     suites. | Note | Cisco VVB Engine restart is required after a change to this configuration. |
| Note | Multiple clients connecting to Cisco VVB cannot combine RSA and ECDHE cipher suites. They must use either RSA or ECDHE cipher
                                                                     suites. |
| Note | Cisco VVB Engine restart is required after a change to this configuration. |
| Supported TLS (SIP) Versions | This allows you to select the version of TLS (SIP). TLS (SIP) version supported is TLSv1.2. When
                                                         						  you select a given TLS (SIP) version, Cisco VVB will support SIP TLS requests
                                                         						  for this version and the higher supported versions. Note Supported TLS (SIP) Versions is available only if TLS (SIP) is
                                                                           								  enabled. Cisco VVB Engine restart is required after a change to this
                                                                           								  configuration. The supported TLS (SIP) versions as client or server for securing SIP signaling in the IVR leg can alternatively be specified
                                                                           via the CLI command set tls server min-version as documented in the Cisco Unified Contact Center Express Administration and Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-installation-and-configuration-guides-list.html | Note | Supported TLS (SIP) Versions is available only if TLS (SIP) is
                                                                           								  enabled. Cisco VVB Engine restart is required after a change to this
                                                                           								  configuration. The supported TLS (SIP) versions as client or server for securing SIP signaling in the IVR leg can alternatively be specified
                                                                           via the CLI command set tls server min-version as documented in the Cisco Unified Contact Center Express Administration and Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-installation-and-configuration-guides-list.html |
| Note | Supported TLS (SIP) Versions is available only if TLS (SIP) is
                                                                           								  enabled. Cisco VVB Engine restart is required after a change to this
                                                                           								  configuration. The supported TLS (SIP) versions as client or server for securing SIP signaling in the IVR leg can alternatively be specified
                                                                           via the CLI command set tls server min-version as documented in the Cisco Unified Contact Center Express Administration and Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-installation-and-configuration-guides-list.html |
| Cipher Configuration | This field defines the ciphers that are supported by Cisco VVB with key size lesser than or equal to 2048 bits. The following ciphers are pre-populated. TLS_RSA_WITH_AES_128_CBC_SHA TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 Note Cipher configuration is available only if TLS (SIP) is enabled. You must restart the Cisco VVB engine after modifying the cipher configuration. If you are using CUBE version 16.6 and higher, you must manually change the crypto suite to 128/256 by enabling CLI on the dial-peer towards VVB as shown: voice class srtp-crypto 1
	crypto 1 AES_CM_128_HMAC_SHA1_32

dial-peer voice xxxx voip (Dial-peer to VVB srtp)
    ...
    voice-class sip srtp-crypto 1 Note To avoid any unsupported cipher issues during the upgrade to Cisco Unified CVP Release 15.0, it is recommended to restart
                                                                     the Cisco VVB engine to ensure a smooth and successful cipher negotiation process. | Note | Cipher configuration is available only if TLS (SIP) is enabled. You must restart the Cisco VVB engine after modifying the cipher configuration. If you are using CUBE version 16.6 and higher, you must manually change the crypto suite to 128/256 by enabling CLI on the dial-peer towards VVB as shown: voice class srtp-crypto 1
	crypto 1 AES_CM_128_HMAC_SHA1_32

dial-peer voice xxxx voip (Dial-peer to VVB srtp)
    ...
    voice-class sip srtp-crypto 1 | Note | To avoid any unsupported cipher issues during the upgrade to Cisco Unified CVP Release 15.0, it is recommended to restart
                                                                     the Cisco VVB engine to ensure a smooth and successful cipher negotiation process. |
| Note | Cipher configuration is available only if TLS (SIP) is enabled. You must restart the Cisco VVB engine after modifying the cipher configuration. If you are using CUBE version 16.6 and higher, you must manually change the crypto suite to 128/256 by enabling CLI on the dial-peer towards VVB as shown: voice class srtp-crypto 1
	crypto 1 AES_CM_128_HMAC_SHA1_32

dial-peer voice xxxx voip (Dial-peer to VVB srtp)
    ...
    voice-class sip srtp-crypto 1 |
| Note | To avoid any unsupported cipher issues during the upgrade to Cisco Unified CVP Release 15.0, it is recommended to restart
                                                                     the Cisco VVB engine to ensure a smooth and successful cipher negotiation process. |
| SRTP | SRTP is disabled by default. When SRTP is disabled, the media is not encrypted. When SRTP is enabled, it secures the IVR leg. SRTP negotiates between AES_CM_128_HMAC_SHA1_32 or AES_CM_128_HMAC_SHA1_80 crypto-suites, ensuring compatibility and successful
                                                                  encryption of media streams. When SRTP uses a crypto-suite (for example, AES_CM_128_HMAC_SHA1_32), and the incoming request also uses the same crypto-suite,
                                                                     the request is accepted, and the media stream is successfully encrypted using AES_CM_128_HMAC_SHA1_32. When SRTP uses a crypto-suite (for example, AES_CM_128_HMAC_SHA1_32), but the incoming request uses a different one (for example,
                                                                     AES_CM_128_HMAC_SHA1_80) or vice versa, the request will be denied and considered unsupported because the encryption methods
                                                                     do not match resulting in an error response. Note Multiple ciphers may be included in a request; however, the negotiation will only proceed with the cipher configured in the
                                                                                 system, which will either be AES_CM_128_HMAC_SHA1_32 or AES_CM_128_HMAC_SHA1_80. If neither of these ciphers match the request, it will be considered unsupported. When Allow RTP (Mixed mode) check box is checked, the system accepts both SRTP and RTP call flows. This check box can be checked only when SRTP is enabled. Note SRTP is available only if TLS (SIP) is enabled. Check the Allow RTP (Mixed mode) check box if device is configured to work in the RTP mode and interacts with MRCP ARS-TTS servers. For more details on mixed mode call flow scenarios, see the Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html . Cisco VVB engine restart is required after a change to this configuration. SRTP is not supported with VVB XU (Export Unrestricted) software image releases. | Note | Multiple ciphers may be included in a request; however, the negotiation will only proceed with the cipher configured in the
                                                                                 system, which will either be AES_CM_128_HMAC_SHA1_32 or AES_CM_128_HMAC_SHA1_80. If neither of these ciphers match the request, it will be considered unsupported. | Note | SRTP is available only if TLS (SIP) is enabled. Check the Allow RTP (Mixed mode) check box if device is configured to work in the RTP mode and interacts with MRCP ARS-TTS servers. For more details on mixed mode call flow scenarios, see the Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html . Cisco VVB engine restart is required after a change to this configuration. SRTP is not supported with VVB XU (Export Unrestricted) software image releases. |
| Note | Multiple ciphers may be included in a request; however, the negotiation will only proceed with the cipher configured in the
                                                                                 system, which will either be AES_CM_128_HMAC_SHA1_32 or AES_CM_128_HMAC_SHA1_80. If neither of these ciphers match the request, it will be considered unsupported. |
| Note | SRTP is available only if TLS (SIP) is enabled. Check the Allow RTP (Mixed mode) check box if device is configured to work in the RTP mode and interacts with MRCP ARS-TTS servers. For more details on mixed mode call flow scenarios, see the Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html . Cisco VVB engine restart is required after a change to this configuration. SRTP is not supported with VVB XU (Export Unrestricted) software image releases. |
| System Port Parameter |
| RMI Port | The port number used by Cisco VVB to serve Remote Method Invocation (RMI) requests. This field is mandatory. Default: 6999 |

| Note | The default value for ASR/TTS server port for MRCPv1 is 4900 and for MRCPv2 is 5060. Whenever the administrator changes from
                                                                           MRCP protocol, ensure ASR/TTS server is deleted and re-created with appropriate port values. ASR-TTS service is not supported using G729 codec; therefore,
                                                                           								  MRCP is not applicable. |
|---|---|

| Note | For overriding the system default prompt files for ringtone
                                                                     							 application: Create a new folder named vb . Select Applications > Prompt Management and click Create New Folder . Upload the custom ringtone. Choose Applications > Prompt Management and click Upload Prompt . Upload custom ringtone wav file(named same as ringback.wav ) under folder vb . |
|---|---|

| Note | Multiple clients connecting to Cisco VVB cannot combine RSA and ECDHE cipher suites. They must use either RSA or ECDHE cipher
                                                                     suites. |
|---|---|

| Note | Cisco VVB Engine restart is required after a change to this configuration. |
|---|---|

| Note | Supported TLS (SIP) Versions is available only if TLS (SIP) is
                                                                           								  enabled. Cisco VVB Engine restart is required after a change to this
                                                                           								  configuration. The supported TLS (SIP) versions as client or server for securing SIP signaling in the IVR leg can alternatively be specified
                                                                           via the CLI command set tls server min-version as documented in the Cisco Unified Contact Center Express Administration and Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-installation-and-configuration-guides-list.html |
|---|---|

| Note | Cipher configuration is available only if TLS (SIP) is enabled. You must restart the Cisco VVB engine after modifying the cipher configuration. If you are using CUBE version 16.6 and higher, you must manually change the crypto suite to 128/256 by enabling CLI on the dial-peer towards VVB as shown: voice class srtp-crypto 1
	crypto 1 AES_CM_128_HMAC_SHA1_32

dial-peer voice xxxx voip (Dial-peer to VVB srtp)
    ...
    voice-class sip srtp-crypto 1 |
|---|---|

| Note | To avoid any unsupported cipher issues during the upgrade to Cisco Unified CVP Release 15.0, it is recommended to restart
                                                                     the Cisco VVB engine to ensure a smooth and successful cipher negotiation process. |
|---|---|

| Note | Multiple ciphers may be included in a request; however, the negotiation will only proceed with the cipher configured in the
                                                                                 system, which will either be AES_CM_128_HMAC_SHA1_32 or AES_CM_128_HMAC_SHA1_80. If neither of these ciphers match the request, it will be considered unsupported. |
|---|---|

| Note | SRTP is available only if TLS (SIP) is enabled. Check the Allow RTP (Mixed mode) check box if device is configured to work in the RTP mode and interacts with MRCP ARS-TTS servers. For more details on mixed mode call flow scenarios, see the Solution Design Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-implementation-design-guides-list.html . Cisco VVB engine restart is required after a change to this configuration. SRTP is not supported with VVB XU (Export Unrestricted) software image releases. |
|---|---|

| Note | The following configurations are available only if the selected mode is Media Gateway (MGW) or Cisco Vitualized Voice Broswer
                                          (VVB) & Media Gateway (MGW). |
|---|---|

| From the Cisco VVB Adminstartion menu bar, choose Media Gateway > Configurations . The Media Gateway Configurations web page displays the following fields. Table 2. Media Gateway Configurations Field Decription Dial Number Configuration Dial Number Displays the default dial number. Proxy Parameters Host Displays the configured host name of the proxy. Port Displays the configured port number of the proxy. Password Displays the masked password of the proxy. Non-Proxy Hosts Displays the configured host name of the non-proxy. Cloud Connect Parameters Publisher Address Displays the configured FQDN / IP address of the publisher. Subscriber Address Displays the configured FQDN / IP address of the subscriber. Username Displays the configured name of the user. Password Displays the masked password. | Field | Decription | Dial Number Configuration | Dial Number | Displays the default dial number. | Proxy Parameters | Host | Displays the configured host name of the proxy. | Port | Displays the configured port number of the proxy. | Password | Displays the masked password of the proxy. | Non-Proxy Hosts | Displays the configured host name of the non-proxy. | Cloud Connect Parameters | Publisher Address | Displays the configured FQDN / IP address of the publisher. | Subscriber Address | Displays the configured FQDN / IP address of the subscriber. | Username | Displays the configured name of the user. | Password | Displays the masked password. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Field | Decription |
| Dial Number Configuration |
| Dial Number | Displays the default dial number. |
| Proxy Parameters |
| Host | Displays the configured host name of the proxy. |
| Port | Displays the configured port number of the proxy. |
| Password | Displays the masked password of the proxy. |
| Non-Proxy Hosts | Displays the configured host name of the non-proxy. |
| Cloud Connect Parameters |
| Publisher Address | Displays the configured FQDN / IP address of the publisher. |
| Subscriber Address | Displays the configured FQDN / IP address of the subscriber. |
| Username | Displays the configured name of the user. |
| Password | Displays the masked password. |

| Field | Decription |
|---|---|
| Dial Number Configuration |
| Dial Number | Displays the default dial number. |
| Proxy Parameters |
| Host | Displays the configured host name of the proxy. |
| Port | Displays the configured port number of the proxy. |
| Password | Displays the masked password of the proxy. |
| Non-Proxy Hosts | Displays the configured host name of the non-proxy. |
| Cloud Connect Parameters |
| Publisher Address | Displays the configured FQDN / IP address of the publisher. |
| Subscriber Address | Displays the configured FQDN / IP address of the subscriber. |
| Username | Displays the configured name of the user. |
| Password | Displays the masked password. |

| Caution | Changing the IP address can interrupt call processing and other
                                             			 system functions. Also, changing the IP address can cause the system to
                                             			 generate certain alarms and alerts such as ServerDown. Because of this
                                             			 potential impact to the system, you must perform IP address changes during a
                                             			 planned maintenance window. |
|---|---|

| Note | As a prerequisite ensure that the DNS is reachable and the DNS
                                             			 record exists for the server if DNS is enabled. |
|---|---|

| Step 1 | If DNS is enabled, change the DNS record of the server to point to the new IP address. |
|---|---|
| Step 2 | If you want to change the IP address of the server on the same subnet or a different subnet that requires a new default gateway
                                             address, then use either CLI Commands or Cisco Unified Operating System Administration interface. |
| Step 3 | To change the default gateway, enter the following CLI command: set network gateway <IP Address> The following is a sample output: admin: set network gateway 10.10.10.1
     ***   W A R N I N G   ***
This will cause the system to temporarily lose network connectivity
Continue (y/n)? Caution Ensure that the server is moved to the new subnet and has access to the default gateway before proceeding to the following
                                                            sub-step. Note Skip this step if you want to change only the IP address of the server. | Caution | Ensure that the server is moved to the new subnet and has access to the default gateway before proceeding to the following
                                                            sub-step. | Note | Skip this step if you want to change only the IP address of the server. |
| Caution | Ensure that the server is moved to the new subnet and has access to the default gateway before proceeding to the following
                                                            sub-step. |
| Note | Skip this step if you want to change only the IP address of the server. |
| Step 4 | To change the IP address of the server, enter the following CLI command: set network ip eth0 <ip_address> <netmask> <default gateway> The following sample output displays: admin:set network ip eth0 10.10.10.170 255.255.255.0 10.10.10.1
           ***   W A R N I N G   ***
This command will restart system services
=======================================================
 Note: Please verify that the new ip address is unique 
       across the cluster and, if DNS services are 
       utilized, any DNS configuration is completed 
       before proceeding.
=======================================================
Continue (y/n)? |
| Step 5 | Enter y and press Enter to continue. |
| Step 6 | Reboot the system using the CLI command utils system restart . |

| Caution | Ensure that the server is moved to the new subnet and has access to the default gateway before proceeding to the following
                                                            sub-step. |
|---|---|

| Note | Skip this step if you want to change only the IP address of the server. |
|---|---|

| Step 1 | Log in to the Cisco Unified OS Administration using administrator login. |
|---|---|
| Step 2 | Go to Settings > IP > Ethernet . |
| Step 3 | Change the Port (IP Address and Subnet Mask) and Gateway information and click Save . |
| Step 4 | Reboot the system using the CLI command utils system restart . |

| Caution | Changing the hostname can interrupt call processing and other system functions. Changing the hostname can also cause the system
                                             to generate certain alarms and alerts such as ServerDown. Because of this potential impact to the system, you must perform
                                             hostname changes during a planned maintenance window. |
|---|---|

| Note | If DNS is enabled, as a prerequisite ensure that the DNS is
                                             			 reachable and the DNS record exists for the server. |
|---|---|

| Step 1 | Change the DNS record of the server to point to the new hostname if the server is configured. Ensure that you correctly update
                                             both the forward (A) and reverse (PTR) records, and there are no duplicate PTR records. |
|---|---|
| Step 2 | At the CLI prompt, enter set network hostname and press Enter key. The following is a sample output: ***   W A R N I N G   ***
Do not close this window without first canceling the command.
This command will automatically restart system services.
The command should not be issued during normal operating hours.
=======================================================
Note: 
Please verify that the new hostname is a unique name across the cluster and, 
if DNS services are utilized, any DNS configuration is completed before proceeding.
=======================================================
Security Warning :
This operation will regenerate all UCCX Certificates including any third party signed Certificates that have been uploaded.    
Enter the hostname:: |
| Step 3 | Enter the hostname and press Enter. |
| Step 4 | Enter no if you do not want to change the IP address. Otherwise, press yes and enter the new IP address, the subnet mask, and the address of the gateway when prompted. |
| Step 5 | Verify that all your input is correct and enter yes to start the process. Do not proceed if the new hostname does not resolve to the correct IP address. |
| Step 6 | Reboot the system using the CLI command utils system restart . Enter y and press Enter to restart the system. |

| Step 1 | Login to the Cisco Unified OS Administration using administrator
                                             			 login. |
|---|---|
| Step 2 | Go to Settings > IP > Ethernet . |
| Step 3 | Change the hostname and click Save . |
| Step 4 | Reboot the system using the CLI command utils system restart . |

| Note | For the Cisco VVB, the Unified RTMT is not supported on Linux. |
|---|---|

| Note | To download,
                                                   				  click the Download hyperlink and select Save File . |
|---|---|

| Note | You can download  Speech Server and Cisco VVB Engine logs from the RTMT. |
|---|---|

| Note | In a Cisco VVB server, audit logging is supported for Voice Operating System (VOS) and Command Line Interface (CLI) activities,
                                             which can be monitored using the Real Time Monitoring Tool (RTMT). However, VVB services activities are not included in the
                                             audit logs. |
|---|---|

| Step 1 | From the Cisco VVB Serviceability menu bar, choose Trace > Configuration . |
|---|---|
| Step 2 | From the Select Service drop-down list box, choose Engine and click Go . The debug levels for different Cisco VVB services might vary depending on the selected service. The Cisco VVB-related services
                                                are listed in the following table: Component Code Description JASMIN Java Signaling and Monitoring Interface SIP_STACK SIP Stack logging SS_SIP SIP Subsystem SS_VB Voice Browser Subsystem SS_MRCP_ASR MRCP ASR Subsystem SS_MRCP_TTS MRCP TTS Subsystem Note To enable XDebugging for any of the components, check the appropriate check boxes. | Component Code | Description | JASMIN | Java Signaling and Monitoring Interface | SIP_STACK | SIP Stack logging | SS_SIP | SIP Subsystem | SS_VB | Voice Browser Subsystem | SS_MRCP_ASR | MRCP ASR Subsystem | SS_MRCP_TTS | MRCP TTS Subsystem | Note | To enable XDebugging for any of the components, check the appropriate check boxes. |
| Component Code | Description |
| JASMIN | Java Signaling and Monitoring Interface |
| SIP_STACK | SIP Stack logging |
| SS_SIP | SIP Subsystem |
| SS_VB | Voice Browser Subsystem |
| SS_MRCP_ASR | MRCP ASR Subsystem |
| SS_MRCP_TTS | MRCP TTS Subsystem |
| Note | To enable XDebugging for any of the components, check the appropriate check boxes. |
| Step 3 | To limit the number and size of the trace files, you can specify the trace output setting using the following two fields.
                                             See the following table for description and default values for these two fields: Field Description Maximum No. of Files The maximum number of trace files to be retained by the system. This field specifies the total number of trace files for a given service. Cisco VVB Serviceability automatically appends a
                                                            sequence number to the filename to indicate which file it is; for example, Cisco001MADM14.log. When the last file in the sequence
                                                            is full, the trace data begins writing over the first file. The default value varies by service. Maximum File Size This field specifies the maximum size of the trace file in kilobytes or megabytes depending on the selected service. The default
                                                            value varies by service. | Field | Description | Maximum No. of Files | The maximum number of trace files to be retained by the system. This field specifies the total number of trace files for a given service. Cisco VVB Serviceability automatically appends a
                                                            sequence number to the filename to indicate which file it is; for example, Cisco001MADM14.log. When the last file in the sequence
                                                            is full, the trace data begins writing over the first file. The default value varies by service. | Maximum File Size | This field specifies the maximum size of the trace file in kilobytes or megabytes depending on the selected service. The default
                                                            value varies by service. |
| Field | Description |
| Maximum No. of Files | The maximum number of trace files to be retained by the system. This field specifies the total number of trace files for a given service. Cisco VVB Serviceability automatically appends a
                                                            sequence number to the filename to indicate which file it is; for example, Cisco001MADM14.log. When the last file in the sequence
                                                            is full, the trace data begins writing over the first file. The default value varies by service. |
| Maximum File Size | This field specifies the maximum size of the trace file in kilobytes or megabytes depending on the selected service. The default
                                                            value varies by service. |
| Step 4 | Update the debug level for one or more components for the selected service of Cisco VVB by performing these steps: To activate traces for a specific component or logging for a server, select the check box for the service for which you need
                                                      to enable logging. To turn off logging for a server, clear the check box. |
| Step 5 | Click the Save icon that displays in the toolbar in the upper left corner of the window or the Save button that displays at the bottom of the window to save your trace parameter configuration. The settings are updated in
                                             the system and the trace files are generated as per the saved settings. Click the Restore Defaults icon or button to revert to the default settings for the selected service. Important Activate logging only for debugging, and remember to turn off logging after the debugging session is complete. | Important | Activate logging only for debugging, and remember to turn off logging after the debugging session is complete. |
| Important | Activate logging only for debugging, and remember to turn off logging after the debugging session is complete. |

| Component Code | Description |
|---|---|
| JASMIN | Java Signaling and Monitoring Interface |
| SIP_STACK | SIP Stack logging |
| SS_SIP | SIP Subsystem |
| SS_VB | Voice Browser Subsystem |
| SS_MRCP_ASR | MRCP ASR Subsystem |
| SS_MRCP_TTS | MRCP TTS Subsystem |

| Note | To enable XDebugging for any of the components, check the appropriate check boxes. |
|---|---|

| Field | Description |
|---|---|
| Maximum No. of Files | The maximum number of trace files to be retained by the system. This field specifies the total number of trace files for a given service. Cisco VVB Serviceability automatically appends a
                                                            sequence number to the filename to indicate which file it is; for example, Cisco001MADM14.log. When the last file in the sequence
                                                            is full, the trace data begins writing over the first file. The default value varies by service. |
| Maximum File Size | This field specifies the maximum size of the trace file in kilobytes or megabytes depending on the selected service. The default
                                                            value varies by service. |

| Important | Activate logging only for debugging, and remember to turn off logging after the debugging session is complete. |
|---|---|

| Step 1 | From the Cisco VVB Serviceability menu bar, choose Trace > Configuration . |
|---|---|
| Step 2 | From the Select Service drop-down list box, choose Speech Server and click Go . Component Code Description SS_SRV Speech Server Note To enable XDebugging for any of the components, check the appropriate check boxes. | Component Code | Description | SS_SRV | Speech Server | Note | To enable XDebugging for any of the components, check the appropriate check boxes. |
| Component Code | Description |
| SS_SRV | Speech Server |
| Note | To enable XDebugging for any of the components, check the appropriate check boxes. |
| Step 3 | To limit the size of the Log File directory and the size of trace files, you can specify the trace output setting using the
                                             following two fields. See the following table for description and default values for these two fields: Field Description Maximum No. of Files Maximum number of trace files that is used to calculate total log directory size. Maximum File Size This field specifies the maximum size of the trace file in kilobytes or megabytes depending on the selected service. The default
                                                            value varies by service. | Field | Description | Maximum No. of Files | Maximum number of trace files that is used to calculate total log directory size. | Maximum File Size | This field specifies the maximum size of the trace file in kilobytes or megabytes depending on the selected service. The default
                                                            value varies by service. |
| Field | Description |
| Maximum No. of Files | Maximum number of trace files that is used to calculate total log directory size. |
| Maximum File Size | This field specifies the maximum size of the trace file in kilobytes or megabytes depending on the selected service. The default
                                                            value varies by service. |
| Step 4 | Update the debug level for one or more components for the selected service of Cisco VVB by performing these steps: To activate traces for a specific component or logging for a server, select the check box for the service for which you need
                                                      to enable logging. To turn off logging for a server, clear the check box. |
| Step 5 | Click the Save icon that displays in the toolbar in the upper left corner of the window or the Save button that displays at the bottom of the window to save your trace parameter configuration. The settings are updated in
                                             the system and the trace files are generated as per the saved settings. Click the Restore Defaults icon or button to revert to the default settings for the selected service. Important Activate logging only for debugging, and remember to turn off logging after the debugging session is complete. Note You can download both speech server and Cisco VVB Engine logs from the Real-Time Monitoring Tool (RTMT) or the CLI commands.
                                                            For more information on the CLI commands, refer to the Operations Guide for Cisco Virtualized Voice Browser . | Important | Activate logging only for debugging, and remember to turn off logging after the debugging session is complete. | Note | You can download both speech server and Cisco VVB Engine logs from the Real-Time Monitoring Tool (RTMT) or the CLI commands.
                                                            For more information on the CLI commands, refer to the Operations Guide for Cisco Virtualized Voice Browser . |
| Important | Activate logging only for debugging, and remember to turn off logging after the debugging session is complete. |
| Note | You can download both speech server and Cisco VVB Engine logs from the Real-Time Monitoring Tool (RTMT) or the CLI commands.
                                                            For more information on the CLI commands, refer to the Operations Guide for Cisco Virtualized Voice Browser . |

| Component Code | Description |
|---|---|
| SS_SRV | Speech Server |

| Note | To enable XDebugging for any of the components, check the appropriate check boxes. |
|---|---|

| Field | Description |
|---|---|
| Maximum No. of Files | Maximum number of trace files that is used to calculate total log directory size. |
| Maximum File Size | This field specifies the maximum size of the trace file in kilobytes or megabytes depending on the selected service. The default
                                                            value varies by service. |

| Important | Activate logging only for debugging, and remember to turn off logging after the debugging session is complete. |
|---|---|

| Note | You can download both speech server and Cisco VVB Engine logs from the Real-Time Monitoring Tool (RTMT) or the CLI commands.
                                                            For more information on the CLI commands, refer to the Operations Guide for Cisco Virtualized Voice Browser . |
|---|---|

| Step 1 | From the Navigation drop-down list, select Cisco VVB Serviceability. |
|---|---|
| Step 2 | Select Tools > Control Center - Network Services . |
| Step 3 | Select the Engine radio button  and click your desired operation button. The page displays the following information for the network services: Name of the network services, their dependent subsystems, managers, or components Status of the service (IN SERVICE, PARTIAL SERVICE, or SHUT DOWN; for individual subsystems, the status can be OUT OF SERVICE
                                                   or NOT CONFIGURED) Start Time of the service Up Time of the service |