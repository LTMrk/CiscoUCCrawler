---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1-su2-cucm-b-bulk-administration-guide-1251su2-cucm-b-bulk-adm-7abb1ed34a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1_SU2/cucm_b_bulk-administration-guide-1251su2/cucm_b_bulk-administration-guide-1251su2_chapter_01001011.html
retrieved_at: 2026-08-21T08:50:53.526076+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

Updated: February 3, 2020

Chapter: Manage Tool for
	 Auto-Registered Phones Support (TAPS)

## Chapter: Manage Tool for
	 Auto-Registered Phones Support (TAPS)

# Manage Tool for
                     	 Auto-Registered Phones Support (TAPS)

This chapter
                        		provides information about installing, configuring, and using the Tool for
                        		Auto-Registered Phones Support (TAPS).

## TAPS Overview

Configure TAPS—Allows you to enable TAPS usage for all
                                       				phones that use auto-registration or to limit TAPS to only phones that are
                                       				added through BAT with dummy MAC addresses.

Secure TAPS—Allows you to keep some directory numbers from
                                       				being updated through TAPS.

User Locales for TAPS—Allows you to choose the languages
                                       				for TAPS prompts.

TAPS components get installed on the Cisco Unified Communications Manager first node as part of the Cisco Unified Communications Manager installation. You must enable
                              		  auto-registration in Cisco Unified Communications Manager for TAPS to function. 
                              		In addition, you must enable the CallManager service on the first node, even if the first node is not being used to register
                              phones.

When you use TAPS, it leads to the depletion of auto-registration
                                          			 range on the Cisco Unified Communications Manager . After update through TAPS, the
                                          			 auto-registered directory number (DN) of the phone becomes an unassigned DN.
                                          			 You should delete unassigned DNs using BAT periodically to free up the
                                          			 auto-registration range.

You must install TAPS application on the Cisco Unified
                              		  Contact Center Express (Cisco UCCX) server. TAPS requires the Cisco IP
                              		  Interactive Voice Response (IP IVR) application that runs on the Cisco UCCX
                              		  server for the user interface and prompts.

Administrators need to provide instructions to tell end users
                              		  how to use TAPS to configure their new phones.

Cisco recommends that you stop the TAPS service when you are not
                                          			 using TAPS to add phones to Cisco Unified Communications Manager database.

### TAPS Auto-registration Options

You can set the following options for using TAPS to update
                                 		  auto-registering phones.

Update MAC addresses and download a predefined configuration for
                                       				new phones.

Reload the configuration for replacement phones.

#### TAPS with New Phone Examples

After BAT has added the new phone configurations with dummy MAC addresses in Cisco Unified Communications Manager Administration, you can plug the phones into the network. You or the phone user can dial a TAPS directory number that causes
                                    the phone to download its configuration. At the same time, the phone gets updated in Cisco Unified Communications Manager Administration with the correct MAC address. You must make sure that Auto-registration is enabled in Cisco Unified Communications Manager Administration for TAPS to function.

When you use TAPS, it leads to the depletion of auto-registration range on the Cisco Unified Communications Manager . After update through TAPS, the auto-registered directory number (DN) of the phone becomes an unassigned DN. You should delete
                                                unassigned DNs using BAT periodically to free up the auto-registration range.

##### Example

You have 100 new-hire employees starting on Monday. You must add these users and their new phones to Cisco Unified Communications Manager Administration. You can use BAT to create a phone template for these 100 phones and a CSV data file for phones and users.
                                    By using the dummy MAC address option in the CSV data file, you do not need to add the individual MAC addresses for the new
                                    phones. With auto-registration enabled in Cisco Unified Communications Manager , you can plug the phones directly into the network. You or the new employee can load the configuration by dialing the TAPS
                                    directory number and following the voice-prompt instructions.

#### Reloading
                              	 Configurations Using TAPS

When you
                                    		  must replace an existing phone that is not functioning, you can use TAPS to
                                    		  download the existing phone configuration to the new phone. After the user
                                    		  receives the new phone and plugs the phone into the network, the user dials the
                                    		  TAPS directory number to download configuration for the previous phone. The
                                    		  user makes no configuration changes during this process.

In Cisco Unified Communications
                                       			 Manager Administration, you must enable auto-registration. You must
                                    		  ensure that you configure TAPS usage for all phones to enable a user to
                                    		  download an existing phone configuration.

When you use TAPS,
                                                			 it leads to the depletion of auto-registration range on the Cisco Unified Communications
                                                   				Manager . After update through TAPS, the auto-registered directory
                                                			 number (DN) of the phone becomes an unassigned DN. You should delete unassigned
                                                			 DNs using BAT periodically to free up the auto-registration range.

For
                                    		  more information, see the Cisco Unified Communications Manager Online Help .

##### Example

John's
                                    		  Cisco Unified IP Phone model 7940 gets short-circuited during a lightning
                                    		  storm. He receives a new Cisco Unified IP Phone model 7940 and plugs it into
                                    		  the network. John can dial the TAPS directory number, and the new phone will
                                    		  download the configuration that was previously used for the damaged phone. TAPS
                                    		  automatically updates device information in Cisco Unified Communications
                                       			 Manager Administration.

### Secured Directory Numbers

Because TAPS can replace a directory number, you can protect
                                 		  certain directory numbers from being overwritten. To protect important
                                 		  directory numbers, you can use the Secure TAPS option.

#### Example

The directory number 5000 provides voice-messaging access for
                                 		  your system. You do not want a new user to mistakenly configure 5000 on the new
                                 		  phone. The Secure TAPS option allows you to specify that TAPS cannot access
                                 		  directory number "5000."

### Language Prompts for TAPS Users

You can configure user prompts for TAPS to play in several
                                 		  languages. Administrators can choose the languages to make available to users.

If you need to use language prompts other than English
                                 		  prompts, before you install, upgrade, or configure TAPS, run the Cisco Unified Communications Manager Locale Installer on each cluster node and restart each node.

Using the locale installer ensures
                                 		  that you have the latest translated text, translated voice prompts,
                                 		  country-specific phone tones, and country-specific gateways tones available for
                                 		  the phones. For more information on the Cisco Unified Communications Manager Locale Installer, refer to the specific locale
                                 		  installer documentation.

You can use the file get tftp <AAR file name> CLI command the get the AAR file the Cisco Unified Communications Manager TFTP directory.

## Install TAPS

This section provides information about installing,
                              		  reinstalling, and uninstalling TAPS. TAPS interfaces with both Cisco Unified Communications Manager server and Cisco Customer Response Solution
                              		  server. This installation procedure involves installing TAPS on the UCCX
                              		  server.

Refer to the Cisco Unified Contact Center Express (Cisco Unified CCX) Software and Hardware Compatibility Guide 
                                          			 to find out the Cisco UCCX version
                                          				compatible to the TAPS version you are installing.

### Before you begin

The following prerequisites apply to TAPS installation for
                              		  BAT:

- Make sure that the Cisco Unified Communications Manager first node is configured and running.

- Have the IP address for
                                 			 the Cisco Unified Communications Manager first node server.

- Ensure the Cisco UCCX 
                                 			 server is configured. The Cisco UCCX application can reside on its own
                                 			 dedicated server.

- Be sure to use the locale
                                 			 installer to create the country-specific TAPS prompts.

Install TAPS on the UCCX application server.

Log on with administrator privileges to the system that is running
                                       			 the Cisco Unified Communications Manager first node database.

Choose Applications > Plugins .

Find the TAPS link and click Download to save the TAPS_AAR.aar plugin to
                                       			 your local machine.

Log in to the UCCX App admin page through Applications > AAR
                                             				  Management as TAPS user and Upload the TAPS_AAR.aar
                                       			 from AAR Management page.

Go to Applications > Application Management .

Click on the TAPS application.

Select the Cisco_Unified_CM_IP_Address check box and
                                       			 specify the Cisco Unified Communications Manager IP address, enclosed in double quotes.

By default the IP address will be " " , you must enter the IP address between the quotes.

Restart Tomcat and Cisco Unified CCX Cluster View Daemon using the
                                       			 following commands

- utils service "Cisco Tomcat" stop/start

- utils service "Cisco Unified CCX Cluster View Daemon" stop/start

Refer to the Cisco Unified Contact Center Express Administration
                                                      				  Guide for more information on managing the TAPS_AAR.aar.

## TAPS Application Configuration in UCCX Applications Server

You can review the Cisco UCCX application server
                              		  documentation by browsing to Cisco Voice Applications and Tools at www.cisco.com .
                              		  See the Cisco Unified Contact Center Express Administration Guide for
                              		  instructions on how to configure an application.

The TAPS application does not work with a Cisco UCCX Standard license. You must use either an Enhanced or Premium license.

## Activate TAPS Service

You can activate and deactivate TAPS service using Cisco Unified Communications Manager Serviceability after you access it using the
                              		  appropriate URL.

Access Cisco Unified Communications Manager Serviceability.

Choose Tools > Service Activation .

Choose the appropriate server from the drop-down list box. Click Next .

Choose TAPS Service from Database and Admin Services of the Unified CMServices list and click Save .

If the service is already activated, the Activation Status will
                                                      				  display as Activated.

## Start Stop and Restart TAPS

The TAPS service starts automatically after it is activated
                              		  by using Cisco Unified Communications Manager Serviceability. This section describes the
                              		  procedures to stop or restart the TAPS service.

In Cisco Unified Communications Manager Serviceability, choose Tools > Control Center -
                                             				  Feature Services .

The Control Center–Feature Services window displays.

Choose the Cisco Unified Communications Manager server from the Servers drop-down list box.

TAPS Service displays in list under Database and Admin Services
                                          				column, in the Unified CMServices.

If TAPS is already activated, the Status displays as Activated.

Check the check box that corresponds to TAPS Service.

If you want to restart the TAPS service, click Restart .

The service restarts, and the message, Service Successfully
                                          				Restarted, displays.

If you want to stop the TAPS service, click Stop .

The service stops, and the message, Service Successfully Stopped,
                                          				displays.

If you want to start a stopped TAPS service, click Start .

The service starts, and the message, Service Successfully Started,
                                          				displays.

## TAPS Option Settings

Administrators can choose how to use TAPS in their Cisco Unified Communications Manager system. These TAPS feature options provide
                              		  more flexibility when allowing users to update phones or download phone
                              		  profiles. TAPS options include auto-registration, TAPS secure directory number,
                              		  and user locales for auto-registered phone support.

## Configure TAPS Auto-Registration

The Configure TAPS option provides two ways to use TAPS to
                              		  update phones that auto-register with the Cisco Unified Communications Manager database.

- For phones that are added
                                 			 by using BAT and have a dummy MAC address.

- For existing phones in Cisco Unified Communications Manager Administration

The default setting limits use of TAPS to phones that have a
                              		  dummy MAC address with a device name that starts with the prefix "BAT."

You can set the Configure TAPS option to allow any phone to
                              		  auto-register in the Cisco Unified Communications Manager system, including phones that have a standard
                              		  MAC address.

When you use TAPS, it leads to the depletion of auto-registration
                                          			 range on the Cisco Unified Communications Manager . After update through TAPS, the
                                          			 auto-registered directory number (DN) of the phone becomes an unassigned DN.
                                          			 You should delete unassigned DNs using BAT periodically to free up the
                                          			 auto-registration range.

In the Cisco Unified Communications Manager Administration window, choose System > Service
                                             				  Parameters .

From the Server drop-down list, choose the appropriate server.

From the Service drop-down list, choose TAPS Service .

Choose one of these two options from the Parameter Value drop-down
                                       			 list box, and click Save .

Allow Auto-Registered phones to reset with a
                                                					 profile with a dummy MAC address .

Allow Auto-Registered phones to reset with any
                                                					 profile.

### What to do next

To return to the TAPS Options window, click Back .

## TAPS Secure Directory Number Option

The Secure TAPS options let you specify directory numbers
                              		  that TAPS cannot access. Use this capability when you want to protect directory
                              		  numbers from being accidentally assigned to another phone.

When you use TAPS, it leads to the depletion of auto-registration
                                          			 range on the Cisco Unified Communications Manager . After update through TAPS, the
                                          			 auto-registered directory number (DN) of the phone becomes an unassigned DN.
                                          			 You should delete unassigned DNs using BAT periodically to free up the
                                          			 auto-registration range.

Use the following sections to find restricted directory
                              		  numbers or to add restrict more directory numbers:

### Find Secure Directory Numbers

You can find and list the directory numbers that have been
                                 		  restricted.

Choose Bulk
                                                				  Administration > TAPS > Secure
                                                				  TAPS .

Enter the appropriate search criteria and click Search .

#### What to do next

You can proceed to restrict directory numbers or lift the
                                 		  restriction for a directory number.

### Restrict Directory Numbers

You can block TAPS from using directory numbers that you
                                 		  specify. TAPS cannot use any directory number that you include in the list of
                                 		  secured directory numbers.

Choose Bulk
                                                				  Administration > TAPS > Secure
                                                				  TAPS .

Click Add New .

In the Directory Number field, enter the number(s)
                                          			 that you want to protect from TAPS, and click Save.

To enter multiple Directory Numbers, use one line for each
                                                         				  Directory Number entry.

To return to Find and List Directory Numbers window, choose Back to Find/List from the Related links drop-down list box on the right,
                                          			 top corner of the window and click Go .

TAPS cannot use the directory numbers that are shown in this list.
                                             				If a user tries to update a device profile by entering one of the directory
                                             				numbers in this list, TAPS will refuse the request.

### Remove Directory Number Restriction

You can remove a directory number from the list of directory
                                 		  numbers that TAPS cannot access.

Choose Bulk
                                                				  Administration > TAPS > Secure
                                                				  TAPS .

Find the directory numbers you want to delete.

Choose the directory numbers that you want to remove from the
                                          			 secure directory number list and click Delete .

## View TAPS Log Files

Use BAT to view TAPS log files. Each row of the log file
                              		  represents each TAPS transaction.

Choose Bulk
                                             				  Administration > TAPS > View Taps Log
                                             				  File .

## Related Topics

| Note | When you use TAPS, it leads to the depletion of auto-registration
                                          			 range on the Cisco Unified Communications Manager . After update through TAPS, the
                                          			 auto-registered directory number (DN) of the phone becomes an unassigned DN.
                                          			 You should delete unassigned DNs using BAT periodically to free up the
                                          			 auto-registration range. |
|---|---|

| Note | Cisco recommends that you stop the TAPS service when you are not
                                          			 using TAPS to add phones to Cisco Unified Communications Manager database. |
|---|---|

| Note | When you use TAPS, it leads to the depletion of auto-registration range on the Cisco Unified Communications Manager . After update through TAPS, the auto-registered directory number (DN) of the phone becomes an unassigned DN. You should delete
                                                unassigned DNs using BAT periodically to free up the auto-registration range. |
|---|---|

| Note | When you use TAPS,
                                                			 it leads to the depletion of auto-registration range on the Cisco Unified Communications
                                                   				Manager . After update through TAPS, the auto-registered directory
                                                			 number (DN) of the phone becomes an unassigned DN. You should delete unassigned
                                                			 DNs using BAT periodically to free up the auto-registration range. |
|---|---|

| Note | You can use the file get tftp <AAR file name> CLI command the get the AAR file the Cisco Unified Communications Manager TFTP directory. |
|---|---|

| Note | Refer to the Cisco Unified Contact Center Express (Cisco Unified CCX) Software and Hardware Compatibility Guide 
                                          			 to find out the Cisco UCCX version
                                          				compatible to the TAPS version you are installing. |
|---|---|

| Step 1 | Log on with administrator privileges to the system that is running
                                       			 the Cisco Unified Communications Manager first node database. |
|---|---|
| Step 2 | Choose Applications > Plugins . The Find and List Plugins window displays. |
| Step 3 | Find the TAPS link and click Download to save the TAPS_AAR.aar plugin to
                                       			 your local machine. |
| Step 4 | Log in to the UCCX App admin page through Applications > AAR
                                             				  Management as TAPS user and Upload the TAPS_AAR.aar
                                       			 from AAR Management page. |
| Step 5 | Go to Applications > Application Management . The Application Management page displays. |
| Step 6 | Click on the TAPS application. |
| Step 7 | Select the Cisco_Unified_CM_IP_Address check box and
                                       			 specify the Cisco Unified Communications Manager IP address, enclosed in double quotes. Note By default the IP address will be " " , you must enter the IP address between the quotes. | Note | By default the IP address will be " " , you must enter the IP address between the quotes. |
| Note | By default the IP address will be " " , you must enter the IP address between the quotes. |
| Step 8 | Restart Tomcat and Cisco Unified CCX Cluster View Daemon using the
                                       			 following commands utils service "Cisco Tomcat" stop/start utils service "Cisco Unified CCX Cluster View Daemon" stop/start Note Refer to the Cisco Unified Contact Center Express Administration
                                                      				  Guide for more information on managing the TAPS_AAR.aar. | Note | Refer to the Cisco Unified Contact Center Express Administration
                                                      				  Guide for more information on managing the TAPS_AAR.aar. |
| Note | Refer to the Cisco Unified Contact Center Express Administration
                                                      				  Guide for more information on managing the TAPS_AAR.aar. |

| Note | By default the IP address will be " " , you must enter the IP address between the quotes. |
|---|---|

| Note | Refer to the Cisco Unified Contact Center Express Administration
                                                      				  Guide for more information on managing the TAPS_AAR.aar. |
|---|---|

| Note | The TAPS application does not work with a Cisco UCCX Standard license. You must use either an Enhanced or Premium license. |
|---|---|

| Step 1 | Access Cisco Unified Communications Manager Serviceability. |
|---|---|
| Step 2 | Choose Tools > Service Activation . The Service Activation window displays. |
| Step 3 | Choose the appropriate server from the drop-down list box. Click Next . |
| Step 4 | Choose TAPS Service from Database and Admin Services of the Unified CMServices list and click Save . Note If the service is already activated, the Activation Status will
                                                      				  display as Activated. The service gets activated, and the Activation Status
                                       			 column displays the status as Activated. | Note | If the service is already activated, the Activation Status will
                                                      				  display as Activated. |
| Note | If the service is already activated, the Activation Status will
                                                      				  display as Activated. |

| Note | If the service is already activated, the Activation Status will
                                                      				  display as Activated. |
|---|---|

| Step 1 | In Cisco Unified Communications Manager Serviceability, choose Tools > Control Center -
                                             				  Feature Services . The Control Center–Feature Services window displays. |
|---|---|
| Step 2 | Choose the Cisco Unified Communications Manager server from the Servers drop-down list box. TAPS Service displays in list under Database and Admin Services
                                          				column, in the Unified CMServices. Note If TAPS is already activated, the Status displays as Activated. | Note | If TAPS is already activated, the Status displays as Activated. |
| Note | If TAPS is already activated, the Status displays as Activated. |
| Step 3 | Check the check box that corresponds to TAPS Service. |
| Step 4 | If you want to restart the TAPS service, click Restart . The service restarts, and the message, Service Successfully
                                          				Restarted, displays. |
| Step 5 | If you want to stop the TAPS service, click Stop . The service stops, and the message, Service Successfully Stopped,
                                          				displays. |
| Step 6 | If you want to start a stopped TAPS service, click Start . The service starts, and the message, Service Successfully Started,
                                          				displays. |

| Note | If TAPS is already activated, the Status displays as Activated. |
|---|---|

| Note | When you use TAPS, it leads to the depletion of auto-registration
                                          			 range on the Cisco Unified Communications Manager . After update through TAPS, the
                                          			 auto-registered directory number (DN) of the phone becomes an unassigned DN.
                                          			 You should delete unassigned DNs using BAT periodically to free up the
                                          			 auto-registration range. |
|---|---|

| Step 1 | In the Cisco Unified Communications Manager Administration window, choose System > Service
                                             				  Parameters . The Service Parameter Configuration window displays. |
|---|---|
| Step 2 | From the Server drop-down list, choose the appropriate server. |
| Step 3 | From the Service drop-down list, choose TAPS Service . |
| Step 4 | Choose one of these two options from the Parameter Value drop-down
                                       			 list box, and click Save . Allow Auto-Registered phones to reset with a
                                                					 profile with a dummy MAC address . TAPS updates auto-registered phones with a profile that have
                                             				  the dummy MAC address only. Allow Auto-Registered phones to reset with any
                                                					 profile. TAPS updates auto-registered phones with any profile. A status message indicates that the update is successful. |

| Note | When you use TAPS, it leads to the depletion of auto-registration
                                          			 range on the Cisco Unified Communications Manager . After update through TAPS, the
                                          			 auto-registered directory number (DN) of the phone becomes an unassigned DN.
                                          			 You should delete unassigned DNs using BAT periodically to free up the
                                          			 auto-registration range. |
|---|---|

| Step 1 | Choose Bulk
                                                				  Administration > TAPS > Secure
                                                				  TAPS . The Find and List Directory Numbers to Secure window
                                          			 displays. |
|---|---|
| Step 2 | Enter the appropriate search criteria and click Search . If there are secured numbers available, then the list displays
                                          			 those numbers. |

| Step 1 | Choose Bulk
                                                				  Administration > TAPS > Secure
                                                				  TAPS . The Find and List Directory Numbers To Secure window
                                          			 displays. |
|---|---|
| Step 2 | Click Add New . The Secure Directory Numbers Configuration window
                                          			 displays. |
| Step 3 | In the Directory Number field, enter the number(s)
                                          			 that you want to protect from TAPS, and click Save. Tip To enter multiple Directory Numbers, use one line for each
                                                         				  Directory Number entry. | Tip | To enter multiple Directory Numbers, use one line for each
                                                         				  Directory Number entry. |
| Tip | To enter multiple Directory Numbers, use one line for each
                                                         				  Directory Number entry. |
| Step 4 | To return to Find and List Directory Numbers window, choose Back to Find/List from the Related links drop-down list box on the right,
                                          			 top corner of the window and click Go . TAPS cannot use the directory numbers that are shown in this list.
                                             				If a user tries to update a device profile by entering one of the directory
                                             				numbers in this list, TAPS will refuse the request. |

| Tip | To enter multiple Directory Numbers, use one line for each
                                                         				  Directory Number entry. |
|---|---|

| Step 1 | Choose Bulk
                                                				  Administration > TAPS > Secure
                                                				  TAPS . The Find and List Secure Directory Numbers window
                                          			 displays. |
|---|---|
| Step 2 | Find the directory numbers you want to delete. |
| Step 3 | Choose the directory numbers that you want to remove from the
                                          			 secure directory number list and click Delete . |

| Choose Bulk
                                             				  Administration > TAPS > View Taps Log
                                             				  File . The View TAPS Log File window displays. |
|---|