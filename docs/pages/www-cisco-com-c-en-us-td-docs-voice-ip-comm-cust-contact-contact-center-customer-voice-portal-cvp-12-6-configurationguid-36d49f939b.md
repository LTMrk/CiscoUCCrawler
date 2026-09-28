---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-configurationguid-36d49f939b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/ConfigurationGuideCVP12_6/guide/ccvp_b_1261-configuration-guide-for-cisco-unified-customer-voice-portal/ccvp_m_tomcat-update.html
retrieved_at: 2026-08-21T06:53:53.314427+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

Updated: June 11, 2024

Chapter: Tomcat Update

## Chapter: Tomcat Update

- Tomcat Update

- Tomcat                              	 Update

- Running Tomcat Service without Administrator Privileges

# Tomcat Update

## Tomcat
                        	 Update

Perform the following procedure to update Tomcat version on Call Server, Operations Console, VXML Server, and Web Services
                              Manager (WSM). For example, you can update from Tomcat version 9.0.8 to 9.0.x.

Perform the following procedure to update Tomcat version on Call Server, Operations Console, VXML Server, and Web Services
                              Manager (WSM). For example, you can update from Tomcat version 9.0.43 to 9.0.x.

### Before you begin

For Call Server: C:\Cisco\CVP\CallServer

For VXML Server: C:\Cisco\CVP\VXMLServer

For Operations Console: C:\Cisco\CVP\OPConsoleServer

For WSM: C:\Cisco\CVP\wsm\Server

Save a backup copy of the Tomcat folder on a directory path that is different from the default destination folder (C:\Cisco\CVP).

Rename the Tomcat folders with a different name. For example: Tomcat_backup.

Step 1

Stop the following Tomcat services:

- Cisco CVP Call Server

- Cisco CVP Operations Console Server

- Cisco CVP VXML Server

- Cisco CVP Web Services Manager

Step 2

Remove the Tomcat folder from the following locations:

- For Call Server: C:\Cisco\CVP\CallServer

- For VXML Server: C:\Cisco\CVP\VXMLServer

- For Operations
                                          				Console: C:\Cisco\CVP\OPConsoleServer

- For WSM: C:\Cisco\CVP\wsm\Server

Step 3

Download the Tomcat binary apache-tomcat-9.0.x-windows-x64.zip file from the following location: https://archive.apache.org/dist/tomcat/tomcat-9/ .

Step 4

Right-click the apache-tomcat-9.0.x -windows-x64.zip file and extract the files to a known location on the local drive.

Step 5

Rename the folder apache-tomcat-9.0.x to Tomcat.

Step 6

Copy the Tomcat  folder to the following locations:

- For Call Server: C:\Cisco\CVP\CallServer

- For VXML Server: C:\Cisco\CVP\VXMLServer

- For Operations Console: C:\Cisco\CVP\OPConsoleServer

- For WSM: C:\Cisco\CVP\wsm\Server

Step 7

Copy the webapps file from the Tomcat_backup folder ( …\Tomcat_backup\webapps ) and paste it in the following folder locations:

- For Call Server: C:\Cisco\CVP\CallServer\Tomcat

- For VXML Server: C:\Cisco\CVP\VXMLServer\Tomcat

- For Operations Console: C:\Cisco\CVP\OPConsoleServer\Tomcat

- For WSM: C:\Cisco\CVP\wsm\Server\Tomcat

Step 8

Copy the missing jar files from the Tomcat_backup folder ( ..\Tomcat_backup\lib ) to the following locations:

- For Call Server: C:\Cisco\CVP\CallServer\Tomcat\lib

- For VXML Server: C:\Cisco\CVP\VXMLServer\Tomcat\lib

- For Operations Console: C:\Cisco\CVP\OPConsoleServer\Tomcat\lib

- For WSM: C:\Cisco\CVP\wsm\Server\Tomcat\lib

Copy the contents of the ..\Tomcat_backup\Shared folder to C:\Cisco\CVP\OPSConsoleServer\Tomcat\ .

Step 9

Copy the context.xml file from the Tomcat_backup folder ( ..\Tomcat_backup\conf ) to the following locations:

- For Call Server: C:\Cisco\CVP\CallServer\Tomcat\conf

- For VXML Server: C:\Cisco\CVP\VXMLServer\Tomcat\conf

- For Operations Console: C:\Cisco\CVP\OPConsoleServer\Tomcat\conf

- For WSM: C:\Cisco\CVP\wsm\Server\Tomcat\conf

Step 10

Compare the properties of the new server.xml file located in (..\Tomcat\server.xml) with those of the backed-up server.xml file found in (..\Tomcat_backup\server.xml) . Ensure that you update the properties in the new server.xml file accordingly to reflect any necessary changes.

Step 11

For wsm Tomcat upgrade, ensure the jaas.conf from the backed up Tomcat folder is copied to the new Tomcat/conf folder.

Step 12

Back up connector.property that was created before starting the process from:.

For Operations Console: C:\Cisco\CVP\OPConsoleServer\Tomcat_backup\bin\connector.property

For VXML Server: C:\Cisco\CVP\VXMLServer\Tomcat_backup\bin\connector.property

Step 13

Restore these to:

For Operations Console: C:\Cisco\CVP\OPConsoleServer\Tomcat\bin\connector.property

For VXML Server: C:\Cisco\CVP\VXMLServer\Tomcat\bin\connector.property

Step 14

Restart the following Tomcat services:

- Cisco CVP
                                          				CallServer

- Cisco CVP
                                          				OPSConsoleServer

- Cisco CVP
                                          				VXMLServer

- Cisco CVP
                                          				WebServicesManager

Step 15

Ensure that the CVP Diag portal is up and running.

Step 16

Check Tomcat and CVP logs for any exceptions.

## Running Tomcat Service without Administrator Privileges

Step 1

Create a Windows user, for example, cvp_guest .

Step 2

In C:\Cisco folder, grant read, write, modify permission to cvp_guest.

Step 3

Grant permission to cvp_guest to access the machine remotely (to allow remote connection capability in future) by right clicking This Computer from File Explorer > Properties > Remote Settings > Allow remote connections to this computer > Select Users > Add, type the name
                                          of the new user (eg. cvp_guest) > Check Names > OK .

Step 4

Log out as the current user, and log on as cvp_guest.

Step 5

Get the SID of the cvp_guest user to grant cvp_guest the required permissions to start and stop the Windows services.

Go to Start > regedit > HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\ .

Browse to the folder that has the ProfileImagePath value as C:\Users\cvp_guest .

Right-click that folder and select Copy Key Name to copy the key name to Notepad. By default, the key name appears with the full path. Copy only the last part (for example,
                                             S-1-5-21-1386459338-4158420048-3623644462-1067).

Step 6

Log out as cvp_guest and log in as Administrator to assign permission to cvp_guest for starting and stopping the Tomcat service(s)
                                       that are to be run on that node.

Go to command prompt and run: sc.exe sdshow <service_name> . For example, on a Call Server node, type sc.exe sdshow callserver in the command prompt. Refer to the following table for all possible values of <service_name>.

Sample Output:

```
D:(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA) (A;;CCLCSWLOCRRC;;;IU)
(A;;CCLCSWLOCRRC;;;SU)S:(AU;FA;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;WD)
```

This output lists the permissions for each user and group on this system.

Copy this output for reference and use in the following steps.

Suffix the key to A;;RPWPCR;;; (for example: A;;RPWPCR;;;<KEY_NAME>) and insert it in the output from Step 6a just before ‘S:’ as shown:

Example:

```
D:(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCLCSWLOCRRC;;;IU)(A;;CCLCSWLOCRRC;;;SU) (A;;RPWPCR;;;S-1-5-21-1386459338-4158420048-3623644462-1067) S:(AU;FA;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;WD)
```

Step 7

Go to command prompt and run sc.exe sdset <service_name> <Output from Step 6b>

Example:

```
sc.exe sdset callserver "D:(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA) 
(A;;CCLCSWLOCRRC;;;IU)(A;;CCLCSWLOCRRC;;;SU)(A;;RPWPCR;;;S-1-5-21-1386459338-4158420048-3623644462-1067)S:(AU;FA;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;WD"
```

Depending on which CVP services are to be run on a node, grant permissions to the cvp_guest as follows. For example: on a
                                          Call Server node, run Steps 6 and 7 for ‘callserver’ and ‘vxmlserver’ Tomcat services.

Use the following table to refer to the possible values of <service_name> in the above commands to be run on each node:

Node

Service

<service_name>

Call Server/VXML Server

Call Server

callserver

VXML Server

vxmlserver

Web Services Manager

WebServicesManager

SNMP Management

"Cisco CVP SNMP Management"

OAMP

OPS Console Server

OPSConsoleServer

Web Services Manager

WebServicesManager

SNMP Management

"Cisco CVP SNMP Management"

Reporting Server

Call Server

callserver

Web Services Manager

WebServicesManager

SNMP Management

"Cisco CVP SNMP Management"

Informix IDS

cvp

| Note | Save a backup copy of the Tomcat folder on a directory path that is different from the default destination folder (C:\Cisco\CVP). |
|---|---|

| Step 1 | Stop the following Tomcat services: Cisco CVP Call Server Cisco CVP Operations Console Server Cisco CVP VXML Server Cisco CVP Web Services Manager |
|---|---|
| Step 2 | Remove the Tomcat folder from the following locations: For Call Server: C:\Cisco\CVP\CallServer For VXML Server: C:\Cisco\CVP\VXMLServer For Operations
                                          				Console: C:\Cisco\CVP\OPConsoleServer For WSM: C:\Cisco\CVP\wsm\Server |
| Step 3 | Download the Tomcat binary apache-tomcat-9.0.x-windows-x64.zip file from the following location: https://archive.apache.org/dist/tomcat/tomcat-9/ . |
| Step 4 | Right-click the apache-tomcat-9.0.x -windows-x64.zip file and extract the files to a known location on the local drive. |
| Step 5 | Rename the folder apache-tomcat-9.0.x to Tomcat. |
| Step 6 | Copy the Tomcat  folder to the following locations: For Call Server: C:\Cisco\CVP\CallServer For VXML Server: C:\Cisco\CVP\VXMLServer For Operations Console: C:\Cisco\CVP\OPConsoleServer For WSM: C:\Cisco\CVP\wsm\Server |
| Step 7 | Copy the webapps file from the Tomcat_backup folder ( …\Tomcat_backup\webapps ) and paste it in the following folder locations: For Call Server: C:\Cisco\CVP\CallServer\Tomcat For VXML Server: C:\Cisco\CVP\VXMLServer\Tomcat For Operations Console: C:\Cisco\CVP\OPConsoleServer\Tomcat For WSM: C:\Cisco\CVP\wsm\Server\Tomcat |
| Step 8 | Copy the missing jar files from the Tomcat_backup folder ( ..\Tomcat_backup\lib ) to the following locations: For Call Server: C:\Cisco\CVP\CallServer\Tomcat\lib For VXML Server: C:\Cisco\CVP\VXMLServer\Tomcat\lib For Operations Console: C:\Cisco\CVP\OPConsoleServer\Tomcat\lib For WSM: C:\Cisco\CVP\wsm\Server\Tomcat\lib Note Copy the contents of the ..\Tomcat_backup\Shared folder to C:\Cisco\CVP\OPSConsoleServer\Tomcat\ . | Note | Copy the contents of the ..\Tomcat_backup\Shared folder to C:\Cisco\CVP\OPSConsoleServer\Tomcat\ . |
| Note | Copy the contents of the ..\Tomcat_backup\Shared folder to C:\Cisco\CVP\OPSConsoleServer\Tomcat\ . |
| Step 9 | Copy the context.xml file from the Tomcat_backup folder ( ..\Tomcat_backup\conf ) to the following locations: For Call Server: C:\Cisco\CVP\CallServer\Tomcat\conf For VXML Server: C:\Cisco\CVP\VXMLServer\Tomcat\conf For Operations Console: C:\Cisco\CVP\OPConsoleServer\Tomcat\conf For WSM: C:\Cisco\CVP\wsm\Server\Tomcat\conf |
| Step 10 | Compare the properties of the new server.xml file located in (..\Tomcat\server.xml) with those of the backed-up server.xml file found in (..\Tomcat_backup\server.xml) . Ensure that you update the properties in the new server.xml file accordingly to reflect any necessary changes. |
| Step 11 | For wsm Tomcat upgrade, ensure the jaas.conf from the backed up Tomcat folder is copied to the new Tomcat/conf folder. |
| Step 12 | Back up connector.property that was created before starting the process from:. For Operations Console: C:\Cisco\CVP\OPConsoleServer\Tomcat_backup\bin\connector.property For VXML Server: C:\Cisco\CVP\VXMLServer\Tomcat_backup\bin\connector.property |
| Step 13 | Restore these to: For Operations Console: C:\Cisco\CVP\OPConsoleServer\Tomcat\bin\connector.property For VXML Server: C:\Cisco\CVP\VXMLServer\Tomcat\bin\connector.property |
| Step 14 | Restart the following Tomcat services: Cisco CVP
                                          				CallServer Cisco CVP
                                          				OPSConsoleServer Cisco CVP
                                          				VXMLServer Cisco CVP
                                          				WebServicesManager |
| Step 15 | Ensure that the CVP Diag portal is up and running. |
| Step 16 | Check Tomcat and CVP logs for any exceptions. |

| Note | Copy the contents of the ..\Tomcat_backup\Shared folder to C:\Cisco\CVP\OPSConsoleServer\Tomcat\ . |
|---|---|

| Step 1 | Create a Windows user, for example, cvp_guest . |
|---|---|
| Step 2 | In C:\Cisco folder, grant read, write, modify permission to cvp_guest. |
| Step 3 | Grant permission to cvp_guest to access the machine remotely (to allow remote connection capability in future) by right clicking This Computer from File Explorer > Properties > Remote Settings > Allow remote connections to this computer > Select Users > Add, type the name
                                          of the new user (eg. cvp_guest) > Check Names > OK . |
| Step 4 | Log out as the current user, and log on as cvp_guest. |
| Step 5 | Get the SID of the cvp_guest user to grant cvp_guest the required permissions to start and stop the Windows services. Go to Start > regedit > HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\ . Browse to the folder that has the ProfileImagePath value as C:\Users\cvp_guest . Right-click that folder and select Copy Key Name to copy the key name to Notepad. By default, the key name appears with the full path. Copy only the last part (for example,
                                             S-1-5-21-1386459338-4158420048-3623644462-1067). |
| Step 6 | Log out as cvp_guest and log in as Administrator to assign permission to cvp_guest for starting and stopping the Tomcat service(s)
                                       that are to be run on that node. Go to command prompt and run: sc.exe sdshow <service_name> . For example, on a Call Server node, type sc.exe sdshow callserver in the command prompt. Refer to the following table for all possible values of <service_name>. Sample Output: D:(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA) (A;;CCLCSWLOCRRC;;;IU)
(A;;CCLCSWLOCRRC;;;SU)S:(AU;FA;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;WD) This output lists the permissions for each user and group on this system. Copy this output for reference and use in the following steps. Suffix the key to A;;RPWPCR;;; (for example: A;;RPWPCR;;;<KEY_NAME>) and insert it in the output from Step 6a just before ‘S:’ as shown: Example: D:(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCLCSWLOCRRC;;;IU)(A;;CCLCSWLOCRRC;;;SU) (A;;RPWPCR;;;S-1-5-21-1386459338-4158420048-3623644462-1067) S:(AU;FA;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;WD) |
| Step 7 | Go to command prompt and run sc.exe sdset <service_name> <Output from Step 6b> Example: sc.exe sdset callserver "D:(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA) 
(A;;CCLCSWLOCRRC;;;IU)(A;;CCLCSWLOCRRC;;;SU)(A;;RPWPCR;;;S-1-5-21-1386459338-4158420048-3623644462-1067)S:(AU;FA;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;WD" Depending on which CVP services are to be run on a node, grant permissions to the cvp_guest as follows. For example: on a
                                          Call Server node, run Steps 6 and 7 for ‘callserver’ and ‘vxmlserver’ Tomcat services. Use the following table to refer to the possible values of <service_name> in the above commands to be run on each node: Node Service <service_name> Call Server/VXML Server Call Server callserver VXML Server vxmlserver Web Services Manager WebServicesManager SNMP Management "Cisco CVP SNMP Management" OAMP OPS Console Server OPSConsoleServer Web Services Manager WebServicesManager SNMP Management "Cisco CVP SNMP Management" Reporting Server Call Server callserver Web Services Manager WebServicesManager SNMP Management "Cisco CVP SNMP Management" Informix IDS cvp | Node | Service | <service_name> | Call Server/VXML Server | Call Server | callserver | VXML Server | vxmlserver | Web Services Manager | WebServicesManager | SNMP Management | "Cisco CVP SNMP Management" | OAMP | OPS Console Server | OPSConsoleServer | Web Services Manager | WebServicesManager | SNMP Management | "Cisco CVP SNMP Management" | Reporting Server | Call Server | callserver | Web Services Manager | WebServicesManager | SNMP Management | "Cisco CVP SNMP Management" | Informix IDS | cvp |
| Node | Service | <service_name> |
| Call Server/VXML Server | Call Server | callserver |
| VXML Server | vxmlserver |
| Web Services Manager | WebServicesManager |
| SNMP Management | "Cisco CVP SNMP Management" |
| OAMP | OPS Console Server | OPSConsoleServer |
| Web Services Manager | WebServicesManager |
| SNMP Management | "Cisco CVP SNMP Management" |
| Reporting Server | Call Server | callserver |
| Web Services Manager | WebServicesManager |
| SNMP Management | "Cisco CVP SNMP Management" |
| Informix IDS | cvp |

| Node | Service | <service_name> |
|---|---|---|
| Call Server/VXML Server | Call Server | callserver |
| VXML Server | vxmlserver |
| Web Services Manager | WebServicesManager |
| SNMP Management | "Cisco CVP SNMP Management" |
| OAMP | OPS Console Server | OPSConsoleServer |
| Web Services Manager | WebServicesManager |
| SNMP Management | "Cisco CVP SNMP Management" |
| Reporting Server | Call Server | callserver |
| Web Services Manager | WebServicesManager |
| SNMP Management | "Cisco CVP SNMP Management" |
| Informix IDS | cvp |