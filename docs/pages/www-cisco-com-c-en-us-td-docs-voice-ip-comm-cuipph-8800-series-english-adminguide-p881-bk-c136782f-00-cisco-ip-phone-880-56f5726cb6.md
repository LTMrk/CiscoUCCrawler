---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8800-series-english-adminguide-p881-bk-c136782f-00-cisco-ip-phone-880-56f5726cb6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8800-series/english/adminguide/P881_BK_C136782F_00_cisco-ip-phone-8800_series/P881_BK_C136782F_00_cisco-ip-phone-8811-8841_chapter_01100.html
retrieved_at: 2026-08-21T09:49:23.092836+00:00
---

Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

# Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

Updated: November 6, 2025

Chapter: Corporate and Personal Directory

## Chapter: Corporate and Personal Directory

# Corporate and Personal Directory

## Corporate
                        	 Directory Setup

The Corporate Directory allows a user to look up phone numbers for
                           		coworkers. To support this feature, you must configure corporate directories.

Cisco Unified
                              				Communications Manager uses a Lightweight Directory Access Protocol (LDAP) directory to store authentication and authorization information about
                           users of Cisco Unified
                              				Communications Manager applications that interface with Cisco Unified
                              				Communications Manager . Authentication establishes user rights to access the system. Authorization identifies the telephony resources that a user
                           is permitted to use, such as a specific phone extension.

Cisco IP Phones use dynamic allocation for SecureApp on both client and servers. This ensures your phone can read certificates
                           larger than 4KB, and reduces the frequency of Host Not Found error messages when a user accesses their directory.

For more information, see the documentation for your particular Cisco Unified
                              				Communications Manager release.

After you
                           		complete the LDAP directory configuration, users can use the Corporate
                           		Directory service on their phone to look up users in the corporate directory.

## Personal Directory
                        	 Setup

The Personal Directory allows a user to store a set of personal numbers.

Personal
                           		Directory consists of the following features:

Personal Address
                                 			 Book (PAB)

Speed Dials

Address Book Synchronization Tool (TABSynch)

Users can
                           		use these methods to access Personal Directory features:

From a web browser—Users can access the PAB and Speed Dials features from the Cisco Unified Communications Self Care Portal.

From the CiscoIP Phone—Choose Contacts to search the corporate directory or the user personal directory.

From a Microsoft Windows application—Users can use the TABSynch tool to synchronize their PABs with Microsoft Windows Address
                                 Book (WAB). Customers who want to use the Microsoft Outlook Address Book (OAB) should begin by importing the data from the
                                 OAB into the WAB. TabSync can then be used to synchronize the WAB with Personal Directory. For instructions about TABSync,
                                 see Download Cisco IP Phone Address Book Synchronizer and Set Up Synchronizer .

Cisco IP Phones use dynamic allocation for SecureApp on both client and servers. This ensures your phone can read certificates
                           larger than 4KB, and reduces the frequency of Host Not Found error messages when a user accesses their directory.

To ensure that Cisco IP Phone Address Book Synchronizer users access only their end-user data, activate the Cisco UXL Web
                           Service in Cisco Unified Serviceability.

To
                           		configure Personal Directory from a web browser, users must access their Self
                           		Care Portal. You must provide users with a URL and sign-in information.

## User Personal
                        	 Directory Entries Setup

Users can
                           		configure personal directory entries on the Cisco IP Phone. To configure a
                           		personal directory, users must have access to the following:

Self Care
                                 			 Portal: Make sure that users know how to access their Self Care Portal. See Set Up User Access to the Self Care Portal for details.

Cisco IP Phone
                                 			 Address Book Synchronizer: Make sure to provide users with the installer. See Download Cisco IP Phone Address Book Synchronizer .

The Cisco IP Phone Address Book Synchronizer is only supported on  unsupported versions of Windows (for example, Windows XP
                                             and earlier). The tool is not supported on newer versions of Windows. In future, it will be removed from the Cisco Unified
                                             Communications Manager plug-ins list.

### Download Cisco IP Phone Address Book Synchronizer

To download a copy of the synchronizer to
                                 		  send to your users, follow these steps:

Step 1

To obtain the installer, choose Application > Plugins from Cisco Unified Communications Manager Administration.

Step 2

Select Download , which is located next to the Cisco
                                          			 IP Phone Address Book Synchronizer plugin name.

Step 3

When the file download dialog box displays, select Save .

Step 4

Send the TabSyncInstall.exe file and the instructions in Cisco IP Phone Address Book Synchronizer Deployment to all users who require this application.

### Cisco IP Phone Address Book Synchronizer Deployment

The Cisco IP Phone Address Book Synchronizer synchronizes data that is stored in your Microsoft Windows address book with
                                 the Cisco Unified Communications Manager directory and the Self Care Portal Personal Address Book.

Tip

To successfully synchronize the Windows address book with the Personal Address Book, all Windows address book users should
                                             be entered in the Windows address book before you perform the following procedures.

#### Install
                              	 Synchronizer

To
                                    		  install the Cisco IP Phone Address Book Synchronizer, follow these steps:

Step 1

Get the Cisco
                                             			 IP Phone Address Book Synchronizer installer file from your system
                                             			 administrator.

Step 2

Double-click
                                             			 the TabSyncInstall.exe file that your administrator provided.

Step 3

Select Run .

Step 4

Select Next .

Step 5

Read the
                                             			 license agreement information, and select the I
                                                				Accept . Select Next .

Step 6

Choose the
                                             			 directory in which you want to install the application and select Next .

Step 7

Select Install .

Step 8

Select Finish .

Step 9

To complete
                                             			 the process, follow the steps in Set Up Synchronizer .

#### Set Up Synchronizer

To configure the Cisco IP Phone
                                    		  Address Book Synchronizer, perform these steps:

Step 1

Open the Cisco IP Phone Address Book Synchronizer.

If you accepted the default installation directory, you can open
                                                				the application by choosing Start > All
                                                      					 Programs > Cisco
                                                      					 Systems > TabSync .

Step 2

To configure user information, select User .

Step 3

Enter the Cisco IP Phone user name and password and select OK .

Step 4

To configure Cisco Unified Communications Manager server
                                             			 information, select Server .

Step 5

Enter the IP address or host name and the port number of the Cisco
                                             			 Unified Communications Manager server and select OK .

If you do not have this information, contact your system
                                                				administrator.

Step 6

To start the directory synchronization process, select Synchronize .

The Synchronization Status window provides the status of the
                                                				address book synchronization. If you chose the user intervention for duplicate
                                                				entries rule and you have duplicate address book entries, the Duplicate
                                                				Selection window displays.

Step 7

Choose the entry that you want to include in your Personal Address
                                             			 Book and select OK .

Step 8

When synchronization is complete, select Exit to close the Cisco Unified CallManager
                                             			 Address Book Synchronizer.

Step 9

To verify whether the synchronization worked, sign in to your Self Care Portal and choose Personal Address Book . The
                                             			 users from your Windows address book should be listed.

| Note | The Cisco IP Phone Address Book Synchronizer is only supported on  unsupported versions of Windows (for example, Windows XP
                                             and earlier). The tool is not supported on newer versions of Windows. In future, it will be removed from the Cisco Unified
                                             Communications Manager plug-ins list. |
|---|---|

| Step 1 | To obtain the installer, choose Application > Plugins from Cisco Unified Communications Manager Administration. |
|---|---|
| Step 2 | Select Download , which is located next to the Cisco
                                          			 IP Phone Address Book Synchronizer plugin name. |
| Step 3 | When the file download dialog box displays, select Save . |
| Step 4 | Send the TabSyncInstall.exe file and the instructions in Cisco IP Phone Address Book Synchronizer Deployment to all users who require this application. |

| Tip | To successfully synchronize the Windows address book with the Personal Address Book, all Windows address book users should
                                             be entered in the Windows address book before you perform the following procedures. |
|---|---|

| Step 1 | Get the Cisco
                                             			 IP Phone Address Book Synchronizer installer file from your system
                                             			 administrator. |
|---|---|
| Step 2 | Double-click
                                             			 the TabSyncInstall.exe file that your administrator provided. |
| Step 3 | Select Run . |
| Step 4 | Select Next . |
| Step 5 | Read the
                                             			 license agreement information, and select the I
                                                				Accept . Select Next . |
| Step 6 | Choose the
                                             			 directory in which you want to install the application and select Next . |
| Step 7 | Select Install . |
| Step 8 | Select Finish . |
| Step 9 | To complete
                                             			 the process, follow the steps in Set Up Synchronizer . |

| Step 1 | Open the Cisco IP Phone Address Book Synchronizer. If you accepted the default installation directory, you can open
                                                				the application by choosing Start > All
                                                      					 Programs > Cisco
                                                      					 Systems > TabSync . |
|---|---|
| Step 2 | To configure user information, select User . |
| Step 3 | Enter the Cisco IP Phone user name and password and select OK . |
| Step 4 | To configure Cisco Unified Communications Manager server
                                             			 information, select Server . |
| Step 5 | Enter the IP address or host name and the port number of the Cisco
                                             			 Unified Communications Manager server and select OK . If you do not have this information, contact your system
                                                				administrator. |
| Step 6 | To start the directory synchronization process, select Synchronize . The Synchronization Status window provides the status of the
                                                				address book synchronization. If you chose the user intervention for duplicate
                                                				entries rule and you have duplicate address book entries, the Duplicate
                                                				Selection window displays. |
| Step 7 | Choose the entry that you want to include in your Personal Address
                                             			 Book and select OK . |
| Step 8 | When synchronization is complete, select Exit to close the Cisco Unified CallManager
                                             			 Address Book Synchronizer. |
| Step 9 | To verify whether the synchronization worked, sign in to your Self Care Portal and choose Personal Address Book . The
                                             			 users from your Windows address book should be listed. |