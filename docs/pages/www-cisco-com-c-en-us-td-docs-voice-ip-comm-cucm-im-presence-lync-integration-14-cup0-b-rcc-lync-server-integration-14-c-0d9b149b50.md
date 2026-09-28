---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-lync-integration-14-cup0-b-rcc-lync-server-integration-14-c-0d9b149b50
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/lync_integration/14/cup0_b_rcc-lync-server-integration-14/cup0_b_rcc-lync-server-integration-1251_chapter_01000.html
retrieved_at: 2026-08-16T16:34:48.758950+00:00
---

Remote Call Control with Microsoft Lync Server for IM and Presence Service, Release 14 and SUs

# Remote Call Control with Microsoft Lync Server for IM and Presence Service, Release 14 and SUs

Updated: November 27, 2025

Chapter: Lync Remote Call Control Installation

## Chapter: Lync Remote Call Control Installation

# Lync Remote Call Control Installation

## Install IM and Presence Service Lync Remote Call Control
                        	 Plugin on Client Computer

The Cisco
                              		Unified CM IM and Presence Service Lync Remote Call
                              		Control Plugin adds a IM and
                                 		  Presence Service menu item to the Microsoft Lync client interface that enables the user to select a phone device to control. You
                              		must install this plug-in if the user has multiple devices (lines). When the
                              		user selects the IM and Presence Service menu item, IM and Presence Service opens a web page in
                              		the user's default web browser. The user can select which phone device to
                              		control from this web page.

### Before you begin

- Your username and password for Cisco Unified Communications Manager IM and Presence Service User Options.

- The administrator must assign the user to the "Standard CCM End User" Group. Confirm that you have been added to this group.

- For this
                                 		  procedure you require the Cisco Unified Communications Manager IM and Presence Lync Remote Call Control Plugin batch file called
                                 		  addrccmenu.bat, which you can download from the Cisco Unified CM 
                                    		  IM and
                                    			 Presence Administration user interface. Select Application > Plugins and download the Cisco Unified
                                 		  Communications Manager IM and
                                    			 Presence Lync Remote Call Control Plugin. The batch file is
                                 		  downloaded as a zip file. You must save this zip file to a location on the Microsoft Lync client computer and extract its contents.

Step 1

Open a Windows
                                       			 command prompt on the Microsoft Lync client computer.

Step 2

Navigate to the
                                       			 location of the extracted addrccmenu.bat file.

Step 3

At the command
                                       			 line, enter the following command, where impserveraddress is the IP
                                       			 address, hostname or FQDN of the IM and Presence Service node:

Step 4

If you receive a
                                       			 regedit security warning, allow the operation to continue.

Step 5

When the
                                       			 operation is complete, log out and exit the Microsoft Lync client.

Step 6

Log in to the Microsoft Lync client again and choose the Tools menu option. You can now see the new Cisco
                                       			 menu item.

If you need to
                                                      				  direct the IM and Presence Service menu
                                                      				  item to a different IM and Presence Service node,
                                                      				  you can execute this procedure again using the IP address, hostname or FQDN for
                                                      				  a different IM and Presence Service node.

### What to do next

If the IM and Presence Service web page does not
                              		  open in the user's default web browser when the Microsoft Lync client user accesses the IM and Presence Service menu item, see IM and Presence Service Web Page Does Not Open from the Microsoft Lync Client Default Web Browser.

## Uninstall IM and Presence Service Lync Remote Call Control
                        	 Plugin

To
                              		  uninstall the Cisco Unified Communications Manager IM and Presence Service Lync Remote Call
                              		  Control Plugin, you must rerun the batch file without specifying the IP
                              		  address, hostname or FQDN of the IM and
                                 			 Presence Service node.

Step 1

Download the zip
                                       			 file to the Microsoft Lync computer and extract the contents of the zip file.

Step 2

Open a Windows
                                       			 command prompt.

Step 3

Navigate to the
                                       			 location of the extracted addrccmenu.bat file.

Step 4

At the command
                                       			 line, enter the following command:

Step 5

If you receive a
                                       			 regedit security warning, allow the operation to continue.

Step 6

When the
                                       			 operation is complete, log out and exit the Microsoft Lync client.

Step 7

Log in to the Microsoft Lync client again and select the Tools menu option. The Cisco menu item should no
                                       			 longer be visible.

## Access Phone Selection Through a Web Browser

You use the Cisco Unified Communications Manager IM and Presence Service User Options Web interface to customize settings, create personal response messages, and organize contacts.

### Before you begin

- The hostname or IP address for Cisco Unified Communications Manager IM and Presence Service User Options.

- Your username and password for Cisco Unified Communications Manager IM and Presence Service User Options.

- To be able to log in to the Cisco Unified Communications Manager IM and Presence Service User Options Web interface, the administrator must assign the user to the "Standard CCM End User" Group.

Step 1

Open a supported Web browser on your computer.

Step 2

Enter the URL addresses for Cisco Unified Communications Manager IM and Presence Service User Options:

Step 3

Enter your username for Cisco Unified Communications Manager IM and Presence Service User Options.

Step 4

Enter your password Cisco Unified Communications Manager IM and Presence Service User Options provided by your system 				administrator.

Step 5

Click Login .

| Step 1 | Open a Windows
                                       			 command prompt on the Microsoft Lync client computer. |
|---|---|
| Step 2 | Navigate to the
                                       			 location of the extracted addrccmenu.bat file. |
| Step 3 | At the command
                                       			 line, enter the following command, where impserveraddress is the IP
                                       			 address, hostname or FQDN of the IM and Presence Service node: addrccmenu.bat impserveraddress |
| Step 4 | If you receive a
                                       			 regedit security warning, allow the operation to continue. |
| Step 5 | When the
                                       			 operation is complete, log out and exit the Microsoft Lync client. |
| Step 6 | Log in to the Microsoft Lync client again and choose the Tools menu option. You can now see the new Cisco
                                       			 menu item. Note If you need to
                                                      				  direct the IM and Presence Service menu
                                                      				  item to a different IM and Presence Service node,
                                                      				  you can execute this procedure again using the IP address, hostname or FQDN for
                                                      				  a different IM and Presence Service node. | Note | If you need to
                                                      				  direct the IM and Presence Service menu
                                                      				  item to a different IM and Presence Service node,
                                                      				  you can execute this procedure again using the IP address, hostname or FQDN for
                                                      				  a different IM and Presence Service node. |
| Note | If you need to
                                                      				  direct the IM and Presence Service menu
                                                      				  item to a different IM and Presence Service node,
                                                      				  you can execute this procedure again using the IP address, hostname or FQDN for
                                                      				  a different IM and Presence Service node. |

| Note | If you need to
                                                      				  direct the IM and Presence Service menu
                                                      				  item to a different IM and Presence Service node,
                                                      				  you can execute this procedure again using the IP address, hostname or FQDN for
                                                      				  a different IM and Presence Service node. |
|---|---|

| Step 1 | Download the zip
                                       			 file to the Microsoft Lync computer and extract the contents of the zip file. |
|---|---|
| Step 2 | Open a Windows
                                       			 command prompt. |
| Step 3 | Navigate to the
                                       			 location of the extracted addrccmenu.bat file. |
| Step 4 | At the command
                                       			 line, enter the following command: addrccmenu.bat |
| Step 5 | If you receive a
                                       			 regedit security warning, allow the operation to continue. |
| Step 6 | When the
                                       			 operation is complete, log out and exit the Microsoft Lync client. |
| Step 7 | Log in to the Microsoft Lync client again and select the Tools menu option. The Cisco menu item should no
                                       			 longer be visible. |

| Step 1 | Open a supported Web browser on your computer. |
|---|---|
| Step 2 | Enter the URL addresses for Cisco Unified Communications Manager IM and Presence Service User Options: https:// imp_server_address :8443/cupuser/showHomeMini.do?mini=true Where imp_server_address is the hostname, FQDN, or IP address of  the IM and Presence Service node. |
| Step 3 | Enter your username for Cisco Unified Communications Manager IM and Presence Service User Options. |
| Step 4 | Enter your password Cisco Unified Communications Manager IM and Presence Service User Options provided by your system 				administrator. |
| Step 5 | Click Login . To log out of the User Options Web interface, click Logout in the upper right corner of the User Options page. For security purposes, you will be automatically logged out of User Options
                                       after thirty minutes of inactivity |