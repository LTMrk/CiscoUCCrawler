---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-2-configuration-guide-pcce-b-admi-9a1280ea6a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_2/configuration/guide/pcce_b_admin_configuration_guide_12_6_2/pcce_b_admin_configuration_guide_12_5_2_chapter_0101.html
retrieved_at: 2026-08-21T12:15:09.867185+00:00
---

Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 12.6(2)

# Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 12.6(2)

Updated: December 3, 2025

Chapter: Script Editor and Internet Script Editor

## Chapter: Script Editor and Internet Script Editor

# Script Editor and Internet Script Editor

## Script Editor and
                        	 Internet Script Editor

In a Packaged CCE
                           		deployment, two tools are available for creating routing and administration
                           		scripts—Script Editor and Internet Script Editor. You can use either or both of
                           		these two tools. They provide the same functionality, and that functionality is
                           		documented in this section. This table lists some considerations:

Script
                                       					 Editor

Internet
                                       					 Script Editor

Is automatically deployed as part of the Unified CCE AW-HDS or AW-HDS-DDS installation.

Must be enabled during the installation of the Unified CCE AW-HDS or AW-HDS-DDS Server by selecting it in Web Setup, then downloaded and installed.

Requires a full Administration and Data server. You must run it from the Unified CCE AW-HDS or AW-HDS-DDS Server, based on your deployment.

Can be run on a local machine.

Can be
                                       					 used by global administrators.

Can be
                                       					 used by global administrators and departmental administrators.

Imposes no
                                       					 scripting access restrictions for global administrators.

Imposes
                                       					 scripting access restrictions for departmental administrators.

## Administrator Privileges in Internet Script Editor

In a Packaged CCE deployment, global administrators and departmental administrators have different access permissions in Internet
                           Script Editor.

Global administrators have access as follows:

Full access to scripts and can reference all global and all departments objects when they create scripts.

Full access to dynamic scripting nodes.

Departmental administrators have access as follows:

Full access to scripts that reference global objects and objects in their departments.

Read-only access to scripts that reference Dynamic Scripting Nodes such as formulas.

No access to scripts that reference objects that are associated with departments they do not administer.

## Install Internet Script Editor

You cannot install
                              		  Internet Script Editor directly on a VM.

For Packaged CCE, this means that you cannot install Internet Script Editor on the Unified CCE AW-HDS-DDS or on an external
                              HDS.

Step 1

Point your browser to server-name /install/iscripteditor.htm , where server-name is the name of the computer on which you installed the distributor with the Internet Script Editor client package.

Step 2

Click Download
                                          				Internet Script Editor .

You can also open the iscripteditor.exe file directly from the web page.

Step 3

Navigate to the directory where you want to save iscripteditor.exe .

Step 4

Click Save to
                                       			 begin the download.

Step 5

After the
                                       			 download is complete, close the browser.

Step 6

On your desktop, navigate to iscripteditor.exe and run the file.

Step 7

When the
                                       			 InstallShield Wizard for Internet Script Editor starts, click Next to
                                       			 continue.

Step 8

Select the
                                       			 default Destination Folder by clicking Next ; or
                                       			 click Browse to navigate to the desired Destination Folder, and then click Next .

Step 9

After the
                                       			 InstallShield Wizard indicates that the installation is complete, click Finish .

A shortcut for Internet Script Editor (IScriptEditor) appears on the desktop, and in the Start menu in the Programs/Cisco Systems Inc. program group.

## Start Internet Script Editor

Step 1

Double-click the desktop shortcut for Internet Script Editor
                                       (IScriptEditor).

Step 2

Click Connection .

Step 3

Enter the correct Address , Port , and ICM Instance information.

Step 4

Click OK .

Step 5

Enter your User Name and Password .

Step 6

Enter the Domain of Unified ICM system.

Step 7

Click OK .

Step 8

Upgrade Internet Script Editor as necessary.

## Upgrade Internet Script Editor

After you start Internet Script Editor, if there is a newer
                              version, you receive a message informing you that you can upgrade
                              Internet Script Editor.

Step 1

Accept a software upgrade.

A web page opens from which you can download the new
                                          Internet Script Editor.

Step 2

Click Download Internet Script Editor .

You cannot use Internet Script Editor during the upgrade.

You can also open the iscripteditor.exe file directly from the web page.

Step 3

Navigate to the directory where you want to save iscripteditor.exe .

Step 4

Click Save to begin the download.

Step 5

After the download is complete, close the browser.

Step 6

On your desktop, navigate to iscripteditor.exe and run the file.

Step 7

When the InstallShield Wizard for Internet Script Editor starts, click Next to continue.

Step 8

Select the default Destination Folder by clicking Next ; or click Browse to navigate to the desired Destination Folder, and then click Next .

Step 9

After the InstallShield Wizard indicates that the installation is complete, click Finish .

| Script
                                       					 Editor | Internet
                                       					 Script Editor |
|---|---|
| Is automatically deployed as part of the Unified CCE AW-HDS or AW-HDS-DDS installation. | Must be enabled during the installation of the Unified CCE AW-HDS or AW-HDS-DDS Server by selecting it in Web Setup, then downloaded and installed. |
| Requires a full Administration and Data server. You must run it from the Unified CCE AW-HDS or AW-HDS-DDS Server, based on your deployment. | Can be run on a local machine. |
| Can be
                                       					 used by global administrators. | Can be
                                       					 used by global administrators and departmental administrators. |
| Imposes no
                                       					 scripting access restrictions for global administrators. | Imposes
                                       					 scripting access restrictions for departmental administrators. |

| Step 1 | Point your browser to server-name /install/iscripteditor.htm , where server-name is the name of the computer on which you installed the distributor with the Internet Script Editor client package. |
|---|---|
| Step 2 | Click Download
                                          				Internet Script Editor . Note You can also open the iscripteditor.exe file directly from the web page. | Note | You can also open the iscripteditor.exe file directly from the web page. |
| Note | You can also open the iscripteditor.exe file directly from the web page. |
| Step 3 | Navigate to the directory where you want to save iscripteditor.exe . |
| Step 4 | Click Save to
                                       			 begin the download. |
| Step 5 | After the
                                       			 download is complete, close the browser. |
| Step 6 | On your desktop, navigate to iscripteditor.exe and run the file. |
| Step 7 | When the
                                       			 InstallShield Wizard for Internet Script Editor starts, click Next to
                                       			 continue. |
| Step 8 | Select the
                                       			 default Destination Folder by clicking Next ; or
                                       			 click Browse to navigate to the desired Destination Folder, and then click Next . |
| Step 9 | After the
                                       			 InstallShield Wizard indicates that the installation is complete, click Finish . |

| Note | You can also open the iscripteditor.exe file directly from the web page. |
|---|---|

| Step 1 | Double-click the desktop shortcut for Internet Script Editor
                                       (IScriptEditor). |
|---|---|
| Step 2 | Click Connection . |
| Step 3 | Enter the correct Address , Port , and ICM Instance information. |
| Step 4 | Click OK . |
| Step 5 | Enter your User Name and Password . |
| Step 6 | Enter the Domain of Unified ICM system. |
| Step 7 | Click OK . |
| Step 8 | Upgrade Internet Script Editor as necessary. |

| Note | Some upgrades are optional; these upgrades typically contain GUI
                                       enhancements. Other upgrades, typically involving protocol or
                                       database changes, are mandatory. You cannot use Internet Script
                                       Editor until you accept mandatory upgrades. |
|---|---|

| Step 1 | Accept a software upgrade. A web page opens from which you can download the new
                                          Internet Script Editor. |
|---|---|
| Step 2 | Click Download Internet Script Editor . Note You cannot use Internet Script Editor during the upgrade. You can also open the iscripteditor.exe file directly from the web page. | Note | You cannot use Internet Script Editor during the upgrade. You can also open the iscripteditor.exe file directly from the web page. |
| Note | You cannot use Internet Script Editor during the upgrade. You can also open the iscripteditor.exe file directly from the web page. |
| Step 3 | Navigate to the directory where you want to save iscripteditor.exe . |
| Step 4 | Click Save to begin the download. |
| Step 5 | After the download is complete, close the browser. |
| Step 6 | On your desktop, navigate to iscripteditor.exe and run the file. |
| Step 7 | When the InstallShield Wizard for Internet Script Editor starts, click Next to continue. |
| Step 8 | Select the default Destination Folder by clicking Next ; or click Browse to navigate to the desired Destination Folder, and then click Next . |
| Step 9 | After the InstallShield Wizard indicates that the installation is complete, click Finish . |

| Note | You cannot use Internet Script Editor during the upgrade. You can also open the iscripteditor.exe file directly from the web page. |
|---|---|