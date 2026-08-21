---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-configurationguid-5cdc518488
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/ConfigurationGuideCVP12_6/guide/ccvp_b_1261-configuration-guide-for-cisco-unified-customer-voice-portal/ccvp_m_1252-speech-server-configuration.html
retrieved_at: 2026-08-21T06:52:55.102762+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

Updated: June 11, 2024

Chapter: Speech Server Configuration

## Chapter: Speech Server Configuration

# Speech Server Configuration

## Configure Speech Server

### Before you begin

Install the Remote Operations in the Speech Server before you add the Speech Server to the Operations console.

Step 1

From the  Operations Console, select Device Management > Speech Server .

Step 2

Click Add New to add a new Speech Server or click Use As Template to use an existing template to configure the new Speech Server.

Step 3

Click the following tabs and configure the settings based on your call flow model:

General tab. For more information, see General Settings .

Device Pool tab. Add the Speech Server to a device pool by moving the device pool from Available pane to the Selected pane. For more information about adding, deleting, and editing device pool, see Add or Remove Device From Device Pool .

Step 4

Click Save to save the settings in the Operations Server database. Click Save and Deploy to deploy the changes to the  Speech Server page later.

## Speech Server Settings

### General Settings

Field

Description

Default

Value

Reboot/Restart Required

IP Address

The IP address of the Speech Server.

None

Valid IP address

Yes - Reboot Speech Server

Hostname

The host name of the Speech Server.

None

Valid DNS name, includes letters, the numbers 0 through 9, and a dash

Yes - Reboot Speech Server

Description

The description of the Speech Server.

None

Up to 1024 characters

No

Enable secure communication with the Ops console

Select On to enable secure communications between the Operations Server and this component. Access the device using SSH and files are
                                             transferred using HTTPS.

None

On or Off

No

## Generate G729
                        	 Prompts for Unified CVP

To generate the
                           		G.729 prompts for Unified CVP, perform the following procedure:

Convert the
                                 			 audio files from G.711 to G.729 format using the Music on Hold (MOH) audio
                                 			 translator.

Change the G.729
                                 			 compression identifier in the file header.

### Convert the Audio
                           	 Files from G.711 to G.729 Format

Step 1

Log in to the Cisco Unified CM Administration portal
                                          			 and select Media
                                                				  Resources > MOH Audio File Management .

Step 2

Click Upload
                                             				File and select the G.711 audio files individually.

Step 3

Click Media
                                                				  Resources > MOH Audio File Management and check
                                          			 whether the audio files have been converted to G.729 format. If the conversion
                                          			 was successful, the recording length of audio files has a nonzero value.

Step 4

Copy the
                                          			 converted audio files to your Windows server using the Secure File Transfer
                                          			 Protocol (SFTP) Server.

Do not add
                                                         				  spaces when you rename the audio files.

Step 5

Use putty to
                                          			 sign in to the Unified Communications Manager Server as an administrator.

Step 6

From the
                                          			 command prompt, run file get
                                             				activelog mohprep/*g729.wav and provide the SFTP prompts.

### Change the G.729
                           	 Compression Identifier in the File Header

The G.729 files that the Unified Communications Manager generates have a non-standard compression codec tag in the file header.
                                 The VXML Gateway cannot play these audio files, as it does not recognize the codec type. Change the compression codec type value to convert
                                 the audio files into the standard G729r8 format.

Use the following
                                 		  procedure to change the compression codec type number in the file header from
                                 		  0x0133 to the standard 0x14db, G729r8 format.

Step 1

Create a
                                          			 folder in the Unified CVP directory. Copy the G.729 audio files that have a
                                          			 nonstandard compression codec tag in the file header into the new folder
                                          			 location.

Step 2

From the
                                          			 command prompt, navigate to the C:\Cisco\CVP\bin folder.

Step 3

Perform one of
                                          			 these steps:

To convert
                                                   					 audio files individually, from the command prompt, run <UCMHeaderFixer.exe Audio file Name>\*.* .

To perform
                                                   					 bulk conversion of audio files, from the command prompt, run UCMHeaderFixer.exe Folder Path .

The script
                                             				runs and the audio file is converted from name.g729.wav file into name.wav
                                             				format.

Step 4

Use the
                                          			 Operations Console to upload the converted audio files to the IOS Gateway.

## Configuration

No additional configuration is required for SIP service to use IVR service. By default, the SIP service uses the IVR service
                           that resides on the VXML server. It is also no longer necessary to configure the VoiceXML Gateway with the IP address of the VXML Server’s IVR service. When SIP is used, the SIP service inserts the URL of the VXML Server's
                           IVR service into a header in the SIP INVITE message when the call is sent to the VoiceXML Gateway . The VoiceXML Gateway extracts this information from the SIP INVITE and use this information to determine which Call Server to use. The VoiceXML Gateway examines the source IP address of the incoming call from the Call Server. This IP address is used as the address for the
                           VXML Server's IVR service.

The following example illustrates the IOS VoiceXML Gateway bootstrap service that is invoked when a call is received:

```
service bootstrap flash:bootstrap.tcl
     paramspace english index 0
     paramspace english language en
     paramspace english location flash
     paramspace english prefix en
```

For configuring
                                       		  the same feature in Cisco VVB, see section "Cisco VVB
                                          			 configuration for Comprehensive Call Flows" .

With
                           		Unified CVP4.0 and later releases, you have to configure the IP address of the
                           		Call Server. The bootstrap.tcl learns the IP address of the source Call Server
                           		and uses it as its Call Server. There is no need for backup Call Server
                           		configuration, because receiving a call from the Call Server means that the
                           		server is operational.

The
                           		following files in flash memory on the IOS Voice Gateway are also involved with
                           		high availability: handoff.tcl, survivability.tcl, recovery.vxml, and several
                           		.wav files. Use Trivial File Transfer Protocol (TFTP) to load the proper files
                           		into flash. Configuration information for each file can be found within the
                           		file itself. For information, see the latest version of the Configuration Guide for
                                    				  Cisco Unified Customer Voice Portal ,
                           		available at:

https://www.cisco.com/en/US/products/sw/custcosw/ps1006/products_installation_and_configuration_guides_list.html

| Step 1 | From the  Operations Console, select Device Management > Speech Server . |
|---|---|
| Step 2 | Click Add New to add a new Speech Server or click Use As Template to use an existing template to configure the new Speech Server. |
| Step 3 | Click the following tabs and configure the settings based on your call flow model: General tab. For more information, see General Settings . Device Pool tab. Add the Speech Server to a device pool by moving the device pool from Available pane to the Selected pane. For more information about adding, deleting, and editing device pool, see Add or Remove Device From Device Pool . |
| Step 4 | Click Save to save the settings in the Operations Server database. Click Save and Deploy to deploy the changes to the  Speech Server page later. |

| Field | Description | Default | Value | Reboot/Restart Required |
|---|---|---|---|---|
| IP Address | The IP address of the Speech Server. | None | Valid IP address | Yes - Reboot Speech Server |
| Hostname | The host name of the Speech Server. | None | Valid DNS name, includes letters, the numbers 0 through 9, and a dash | Yes - Reboot Speech Server |
| Description | The description of the Speech Server. | None | Up to 1024 characters | No |
| Enable secure communication with the Ops console | Select On to enable secure communications between the Operations Server and this component. Access the device using SSH and files are
                                             transferred using HTTPS. | None | On or Off | No |

| Step 1 | Log in to the Cisco Unified CM Administration portal
                                          			 and select Media
                                                				  Resources > MOH Audio File Management . |
|---|---|
| Step 2 | Click Upload
                                             				File and select the G.711 audio files individually. |
| Step 3 | Click Media
                                                				  Resources > MOH Audio File Management and check
                                          			 whether the audio files have been converted to G.729 format. If the conversion
                                          			 was successful, the recording length of audio files has a nonzero value. |
| Step 4 | Copy the
                                          			 converted audio files to your Windows server using the Secure File Transfer
                                          			 Protocol (SFTP) Server. Note Do not add
                                                         				  spaces when you rename the audio files. | Note | Do not add
                                                         				  spaces when you rename the audio files. |
| Note | Do not add
                                                         				  spaces when you rename the audio files. |
| Step 5 | Use putty to
                                          			 sign in to the Unified Communications Manager Server as an administrator. |
| Step 6 | From the
                                          			 command prompt, run file get
                                             				activelog mohprep/*g729.wav and provide the SFTP prompts. |

| Note | Do not add
                                                         				  spaces when you rename the audio files. |
|---|---|

| Step 1 | Create a
                                          			 folder in the Unified CVP directory. Copy the G.729 audio files that have a
                                          			 nonstandard compression codec tag in the file header into the new folder
                                          			 location. |
|---|---|
| Step 2 | From the
                                          			 command prompt, navigate to the C:\Cisco\CVP\bin folder. |
| Step 3 | Perform one of
                                          			 these steps: To convert
                                                   					 audio files individually, from the command prompt, run <UCMHeaderFixer.exe Audio file Name>\*.* . To perform
                                                   					 bulk conversion of audio files, from the command prompt, run UCMHeaderFixer.exe Folder Path . The script
                                             				runs and the audio file is converted from name.g729.wav file into name.wav
                                             				format. |
| Step 4 | Use the
                                          			 Operations Console to upload the converted audio files to the IOS Gateway. |

| Note | For configuring
                                       		  the same feature in Cisco VVB, see section "Cisco VVB
                                          			 configuration for Comprehensive Call Flows" . |
|---|---|