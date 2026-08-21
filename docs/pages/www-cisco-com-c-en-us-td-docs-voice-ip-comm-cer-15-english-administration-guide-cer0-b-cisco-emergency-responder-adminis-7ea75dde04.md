---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-15-english-administration-guide-cer0-b-cisco-emergency-responder-adminis-7ea75dde04
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/15/english/administration/guide/cer0_b_cisco-emergency-responder-administration-guide-15/cer0_b_cisco-emergency-responder-administration-guide-1401_chapter_0101.html
retrieved_at: 2026-08-21T15:01:54.946954+00:00
---

Cisco Emergency Responder Administration Guide, Release 15 and SUs

# Cisco Emergency Responder Administration Guide, Release 15 and SUs

Updated: March 17, 2026

Chapter: Configure Emergency Responder and National E911 Service Provider Enterprise Services

## Chapter: Configure Emergency Responder and National E911 Service Provider Enterprise Services

# Configure Emergency Responder and National E911 Service Provider Enterprise Services

## Emergency Responder and National E911 Service Provider Enterprise Services Overview

Cisco Emergency Responder (Emergency Responder) supports National E911 Service Provider for Enterprise Service in the Cisco Unified Communications environment as an alternative to direct connection with the Local
                           Exchange Carrier (LEC). The National E911 Service Provider for Enterprise Service provides local routing and emergency service response for National E911 Service Provider customers. Emergency Responder works in conjunction with National E911 Service Provider to provide emergency services to phones that are on the corporate network (on-premise) and phones that are located away from
                           the corporate network (off-premise).

For more information about configuring Emergency Responder, managing Emergency Responder users, working with ERLs, and other
                           related topics, see the "Add Scheduled National E911 Service Provider Updates" section.

These topics provide an overview of how Emergency Responder operates with National E911 Service Provider for Enterprise Service and how to configure and use Emergency Responder to support National E911 Service Provider Enterprise users.

## National E911 Service Provider for Enterprise Service

If you are a subscriber to National E911 Service Provider for Enterprise Service, you can use Emergency Responder to simplify emergency call management. Emergency Responder provides
                           an interface that allows you to enter and synchronize location information directly to the National E911 Service Provider database. Emergency Responder provides location information for emergency calls for both on-premise phones and off-premise
                           phones and works with National E911 Service Provider and Unified CM to complete emergency calls.

Emergency Responder tracks IP phones by the IP subnet or when someone manually configures and assigns the MAC address. Emergency
                           Responder maintains the status of the phones (on-premise, off-premise, unlocated), and passes on any ALI or ELIN information
                           to National E911 Service Provider . Users with on-premise phones rely on Cisco Unified Communications to route their emergency calls to National E911 Service Provider and the designated emergency provider.

Users with
                           		off-premise phones cannot make emergency calls until the users enter in their
                           		location and associate this information with their directory number. After the
                           		location information has been verified, emergency calls placed from off-premise
                           		phones can be completed.

Users can only
                                       		  configure one off-premise location for each DID (DN + External Mask). This
                                       		  configuration also applies to shared lines. If two off-premise phones share a
                                       		  DID, the user can only associate one location to the DID.

The following figure shows the interactions between users, Emergency Responder, and National E911 Service Provider .

### Emergency Call
                           	 Flow

When a user
                              		makes an emergency call:

Unified CM routes
                                    			 the call to Emergency Responder.

Emergency Responder routes the call to National E911 Service Provider .

National E911 Service Provider receives the 10-digit ELIN for the calling party and obtains the ALI data for the caller from this calling party number.

National E911 Service Provider completes the call.

## Set Up Support for National E911 Service Provider for Enterprise Service

After you have confirmed your emergency service support with National E911 Service Provider , you must configure Emergency Responder to support National E911 Service Provider for Enterprise Service.

You must complete the tasks described in the following procedure before creating National E911 Service Provider ERLs.

Step 1

Configure the
                                       			 following items in the Validation and Update Interface (VUI):

Upload the certificate provided by National E911 Service Provider .

Validate the
                                             				  certificate.

Configure National E911 Service Provider Account Information.

Step 2

Configure Route Patterns for routing calls to National E911 Service Provider on the Emergency Responder server.

Step 3

Configure Route Patterns and gateway for routing calls to National E911 Service Provider on Unified CM server.

See Understanding Route Plans chapter in Cisco Unified Communications Manager System Guide, and the "Gateway Configuration" chapter in the Cisco Unified Communications Manager Administration Guide .

Step 4

Create National E911 Service Provider ERL and verify the validity and consistency of the ALI data for the National E911 Service Provider ERL against the National E911 Service Provider TN database.

Step 5

Assign National E911 Service Provider ERLs to switch ports, IP subnets, and unlocated phones.

### Set Up National E911 Service Provider VUI Settings

Before you can configure National E911 Service Provider VUI settings, you must have your account information and a certificate from National E911 Service Provider .

To continue
                                             			 emergency service support when there is a failover to the Emergency Responder
                                             			 subscriber, you must upload the certificate file to the Emergency Responder
                                             			 subscriber separately.

After upgrading the Cisco Emergency Responder, upload the certificate again to continue using the National E911 Service Provider Service.

Step 1

From Emergency Responder, choose System > National E911 Service Provider VUI Settings.

The National E911 Service Provider VUI Settings page displays.

Step 2

Click Upload
                                             				Certificate .

Step 3

Use the Browse button to locate the National E911 Service Provider certificate file, highlight the file, and click the Upload button.

Step 4

Enter the Certificate Password and the VUI URL in the adjacent text boxes. Click Test and Validate .

Step 5

Check the Enable HTTP Proxy check box if you want to use a proxy server for requests between Emergency Responder and National E911 Service Provider.

Step 6

Enter the Proxy Host Name/IP Address of the proxy server, along with the port.

Step 7

Check the Authentication needed on HTTP Proxy check box if you want to communicate with the National E911 Service Provider using authentication based proxy server. If
                                          you enable this check box, only then the Proxy User Name and Proxy Password fields are enabled.

Step 8

Enter the configured user name for proxy server in the Proxy User Name field and the Proxy Password associated to the username.

Step 9

Click the Test and Validate Certificate button to test the validity of your certificate.

Step 10

Enter the
                                          			 Account Information.

VUI Schema
                                                   					 URL

National E911 Service Provider Account ID

Max VUI
                                                   					 Connections

Set MyE911 for location Updates: True

Step 11

Click Update .

For more information about the National E911 Service Provider VUI settings, see National E911 Service Provider VUI Settings .

Step 12

Click Test Connectivity to verify whether Emergency Responder can successfully connect to the customer specific account through the National E911 Service Provider VUI.

### Set Up National E911 Service Provider Patterns on Emergency Responder

Before any emergency calls can be completed by National E911 Service Provider for Enterprise Service, you must configure the route patterns for routing the call to National E911 Service Provider .

Step 1

From Emergency
                                          			 Responder, Choose System > Telephony Settings.

The Telephony
                                             				Settings page is displayed.

Step 2

Under National E911 Service Provider Route Pattern Settings, enter the National E911 Service Provider Route/ Translation Pattern and click the Add button.

### Set Up National E911 Service Provider ERLs

#### Before you begin

You must first configure National E911 Service Provider route patterns before you can add any National E911 Service Provider ERLs.

National E911 Service Provider ERLs differ from conventional ERLs in the following ways:

You can only select route patterns from a preconfigured list in the Telephony Settings web page.

You can query and validate ALI data from National E911 Service Provider by using National E911 Service Provider VUI (Validation & Update interface).

You must submit ALI data (TN Update) to National E911 Service Provider by using National E911 Service Provider VUI before an emergency call can be successfully routed.

Step 1

From Emergency Responder, choose ERL > National E911 Service Provider ERL > National E911 Service Provider ERL(Search and List) .

The Find National E911 Service Provider ERL Data page displays.

Step 2

Click the Add New
                                             				ERL button.

Emergency
                                             				Responder opens the Add New ERL window. See Find National E911 Service Provider ERL for a detail explanation of each
                                             				field.

Step 3

Fill in the
                                          			 ERL Information.

Step 4

Click ALI
                                             				Details

Emergency
                                             				Responder opens the ALI Information window.

Step 5

Enter the ALI Information. The "ALI Information section", Cisco Emergency Responder Administration Web Interface Appendix A , contains detailed explanations of each field. To look up an address in the National E911 Service Provider MSAG database, click Query from National E911 Service Provider .

Step 6

After entering the ALI Information, click Pre-validate from National E911 Service Provider .

Step 7

Make the Add
                                          			 New ERL window the active window if it is not, and click Insert .

Emergency
                                             				Responder saves the ERL and its ALI.

#### National E911 Service Provider ERL Imports

If you have
                                 		multiple ERLs, and you want to add them all at once, you can create a file that
                                 		contains more than one ERL definition, and import all the ERLs at the same time
                                 		into your Emergency Responder configuration. For more information about
                                 		importing ERLs, see Import Several ERLs .

#### National E911 Service Provider ERL Information Export

Use the
                                    		  Export ERL page to create ERL export files for our own use, for example, to
                                    		  back up or move an ERL configuration. For more information about importing
                                    		  ERLs, see Export ERL Information .

### Reconcile ALI
                           	 Discrepancies

You can use Emergency Responder to compare the records from National E911 Service Provider VUI with the records in the database and displays ALI records that have discrepancies. You can examine each record and choose
                                 to update the local record with information from National E911 Service Provider or update National E911 Service Provider 's record.

Step 1

In Emergency Responder Administration, choose ERL > National E911 Service Provider ERL > View ALI Discrepancies .

The View National E911 Service Provider ALI Discrepancies page appears.

Step 2

Enter search criteria to find any specific ELINS and click Find , or click Find without any search criteria to display all National E911 Service Provider ALI discrepancies. The search results appear.

Step 3

Click on the radio button next to the ELIN that you want to view or click View ALI Discrepancies to launch the View National E911 Service Provider ALI discrepancies for a particular ELIN.

The View National E911 Service Provider ALI Discrepancies for a particular ELIN window appears.

Step 4

Choose the correct data from either the local Emergency Responder database or from National E911 Service Provider .

Step 5

Click Save to save changes to the local Emergency Responder database. Click Save National E911 Service Provider ALI Info to save changes to the National E911 Service Provider VUI.

Step 6

Click Close to close this window.

## ERL Data
                        	 Migration

Emergency Responder supports migrating existing conventional ERLs to National E911 Service Provider ERLs and vice versa.

### Migrate Conventional ERL Data to National E911 Service Provider ERL Data

Step 1

In Emergency Responder Administration, choose ERL > ERL Migration Tool .

The ERL Migration Tool page appears.

Step 2

Choose Conventional ERL in the search parameter drop-down list, enter the search criteria, and click Find .

Step 3

Select the ERLs
                                          			 that you want to migrate by checking the check box next to the ERL name.

The Enter Route
                                             				Patterns for ERL Migration window appears.

Step 4

Choose an updated route pattern from the drop-down list.

Step 5

Click Migrate to National E911 Service Provider ERL .

### Migrate National E911 Service Provider ERL Data to Conventional ERL Data

Step 1

In Emergency Responder Administration, choose ERL > ERL Migration Tool .

Step 2

Choose National E911 Service Provider ERL in the search parameter drop-down list, enter the search criteria, and click Find .

Step 3

Select the ERLs that you wish to migrate by checking the check box
                                          			 next to the ERL name.

Step 4

Enter an updated
                                          			 route/pattern translation pattern in the adjacent text box.

Step 5

Click Migrate to Conventional ERL .

## Add Scheduled National E911 Service Provider Updates

You can create ALI and Secondary Status update schedules between Emergency Responder and National E911 Service Provider . A scheduled ALI update sends newly created TN records to National E911 Service Provider . A scheduled Secondary Status update sends queries to National E911 Service Provider requesting information about records with errors that have been corrected.

Step 1

Choose ERL > National E911 Service Provider ERL > National E911 Service Provider Schedule from Emergency Responder.

Step 2

Choose the days
                                       			 of the week and the time of day that you want to schedule an update.

Step 3

Check the Enable Schedule check box if you want to activate this schedule.

Step 4

Choose either ALI Update Schedule or Secondary Status Update Schedule .

Step 5

Click Add to add the schedule to the list of schedules.

## Update Scheduled National E911 Service Provider Update

Step 1

From Emergency Responder, choose ERL National E911 Service Provider ERL National E911 Service Provider Schedule .

Step 2

Click the Edit link adjacent to the schedule that you want to
                                       			 update.

Step 3

Choose the days
                                       			 of the week and the time of day.

Step 4

Check the Enable Schedule check box to activate this schedule.

Step 5

Click Update to change the schedule on the list of
                                       			 schedules.

| Note | Users can only
                                       		  configure one off-premise location for each DID (DN + External Mask). This
                                       		  configuration also applies to shared lines. If two off-premise phones share a
                                       		  DID, the user can only associate one location to the DID. |
|---|---|

| Note | You must configure the IP address of the DNS server to resolve the URLs provided by National E911 Service Provider before completing these tasks. See Cisco Unified Operating System Administration Web Interface For Cisco Emergency Responder . |
|---|---|

| Step 1 | Configure the
                                       			 following items in the Validation and Update Interface (VUI): Upload the certificate provided by National E911 Service Provider . Validate the
                                             				  certificate. Configure National E911 Service Provider Account Information. |
|---|---|
| Step 2 | Configure Route Patterns for routing calls to National E911 Service Provider on the Emergency Responder server. |
| Step 3 | Configure Route Patterns and gateway for routing calls to National E911 Service Provider on Unified CM server. See Understanding Route Plans chapter in Cisco Unified Communications Manager System Guide, and the "Gateway Configuration" chapter in the Cisco Unified Communications Manager Administration Guide . |
| Step 4 | Create National E911 Service Provider ERL and verify the validity and consistency of the ALI data for the National E911 Service Provider ERL against the National E911 Service Provider TN database. |
| Step 5 | Assign National E911 Service Provider ERLs to switch ports, IP subnets, and unlocated phones. |

| Note | To continue
                                             			 emergency service support when there is a failover to the Emergency Responder
                                             			 subscriber, you must upload the certificate file to the Emergency Responder
                                             			 subscriber separately. |
|---|---|

| Note | After upgrading the Cisco Emergency Responder, upload the certificate again to continue using the National E911 Service Provider Service. |
|---|---|

| Step 1 | From Emergency Responder, choose System > National E911 Service Provider VUI Settings. The National E911 Service Provider VUI Settings page displays. |
|---|---|
| Step 2 | Click Upload
                                             				Certificate . An Upload
                                          			 Certificate window opens. |
| Step 3 | Use the Browse button to locate the National E911 Service Provider certificate file, highlight the file, and click the Upload button. |
| Step 4 | Enter the Certificate Password and the VUI URL in the adjacent text boxes. Click Test and Validate . |
| Step 5 | Check the Enable HTTP Proxy check box if you want to use a proxy server for requests between Emergency Responder and National E911 Service Provider. |
| Step 6 | Enter the Proxy Host Name/IP Address of the proxy server, along with the port. |
| Step 7 | Check the Authentication needed on HTTP Proxy check box if you want to communicate with the National E911 Service Provider using authentication based proxy server. If
                                          you enable this check box, only then the Proxy User Name and Proxy Password fields are enabled. |
| Step 8 | Enter the configured user name for proxy server in the Proxy User Name field and the Proxy Password associated to the username. |
| Step 9 | Click the Test and Validate Certificate button to test the validity of your certificate. |
| Step 10 | Enter the
                                          			 Account Information. VUI Schema
                                                   					 URL National E911 Service Provider Account ID Max VUI
                                                   					 Connections Set MyE911 for location Updates: True Note In case the remote users are not updating their locations using MyE911 or Remote Location Manager when Off-premises, set the MyE911 for Location Updates flag to False . | Note | In case the remote users are not updating their locations using MyE911 or Remote Location Manager when Off-premises, set the MyE911 for Location Updates flag to False . |
| Note | In case the remote users are not updating their locations using MyE911 or Remote Location Manager when Off-premises, set the MyE911 for Location Updates flag to False . |
| Step 11 | Click Update . Note To replace the National E911 Service Provider VUI certificate, you must delete the existing National E911 Service Provider account and then proceed from Step 1. Else, the Upload Certificate option will be grayed out. For more information about the National E911 Service Provider VUI settings, see National E911 Service Provider VUI Settings . | Note | To replace the National E911 Service Provider VUI certificate, you must delete the existing National E911 Service Provider account and then proceed from Step 1. Else, the Upload Certificate option will be grayed out. |
| Note | To replace the National E911 Service Provider VUI certificate, you must delete the existing National E911 Service Provider account and then proceed from Step 1. Else, the Upload Certificate option will be grayed out. |
| Step 12 | Click Test Connectivity to verify whether Emergency Responder can successfully connect to the customer specific account through the National E911 Service Provider VUI. |

| Note | In case the remote users are not updating their locations using MyE911 or Remote Location Manager when Off-premises, set the MyE911 for Location Updates flag to False . |
|---|---|

| Note | To replace the National E911 Service Provider VUI certificate, you must delete the existing National E911 Service Provider account and then proceed from Step 1. Else, the Upload Certificate option will be grayed out. |
|---|---|

| Step 1 | From Emergency
                                          			 Responder, Choose System > Telephony Settings. The Telephony
                                             				Settings page is displayed. |
|---|---|
| Step 2 | Under National E911 Service Provider Route Pattern Settings, enter the National E911 Service Provider Route/ Translation Pattern and click the Add button. |

| Note | National E911 Service Provider ERLs differ from conventional ERLs in the following ways: You can only select route patterns from a preconfigured list in the Telephony Settings web page. You can query and validate ALI data from National E911 Service Provider by using National E911 Service Provider VUI (Validation & Update interface). You must submit ALI data (TN Update) to National E911 Service Provider by using National E911 Service Provider VUI before an emergency call can be successfully routed. |
|---|---|

| Step 1 | From Emergency Responder, choose ERL > National E911 Service Provider ERL > National E911 Service Provider ERL(Search and List) . The Find National E911 Service Provider ERL Data page displays. |
|---|---|
| Step 2 | Click the Add New
                                             				ERL button. Emergency
                                             				Responder opens the Add New ERL window. See Find National E911 Service Provider ERL for a detail explanation of each
                                             				field. |
| Step 3 | Fill in the
                                          			 ERL Information. |
| Step 4 | Click ALI
                                             				Details Emergency
                                             				Responder opens the ALI Information window. |
| Step 5 | Enter the ALI Information. The "ALI Information section", Cisco Emergency Responder Administration Web Interface Appendix A , contains detailed explanations of each field. To look up an address in the National E911 Service Provider MSAG database, click Query from National E911 Service Provider . |
| Step 6 | After entering the ALI Information, click Pre-validate from National E911 Service Provider . |
| Step 7 | Make the Add
                                          			 New ERL window the active window if it is not, and click Insert . Emergency
                                             				Responder saves the ERL and its ALI. |

| Step 1 | In Emergency Responder Administration, choose ERL > National E911 Service Provider ERL > View ALI Discrepancies . The View National E911 Service Provider ALI Discrepancies page appears. |
|---|---|
| Step 2 | Enter search criteria to find any specific ELINS and click Find , or click Find without any search criteria to display all National E911 Service Provider ALI discrepancies. The search results appear. |
| Step 3 | Click on the radio button next to the ELIN that you want to view or click View ALI Discrepancies to launch the View National E911 Service Provider ALI discrepancies for a particular ELIN. The View National E911 Service Provider ALI Discrepancies for a particular ELIN window appears. |
| Step 4 | Choose the correct data from either the local Emergency Responder database or from National E911 Service Provider . |
| Step 5 | Click Save to save changes to the local Emergency Responder database. Click Save National E911 Service Provider ALI Info to save changes to the National E911 Service Provider VUI. |
| Step 6 | Click Close to close this window. |

| Step 1 | In Emergency Responder Administration, choose ERL > ERL Migration Tool . The ERL Migration Tool page appears. |
|---|---|
| Step 2 | Choose Conventional ERL in the search parameter drop-down list, enter the search criteria, and click Find . |
| Step 3 | Select the ERLs
                                          			 that you want to migrate by checking the check box next to the ERL name. The Enter Route
                                             				Patterns for ERL Migration window appears. |
| Step 4 | Choose an updated route pattern from the drop-down list. |
| Step 5 | Click Migrate to National E911 Service Provider ERL . |

| Step 1 | In Emergency Responder Administration, choose ERL > ERL Migration Tool . The ERL Migration Tool page appears. |
|---|---|
| Step 2 | Choose National E911 Service Provider ERL in the search parameter drop-down list, enter the search criteria, and click Find . |
| Step 3 | Select the ERLs that you wish to migrate by checking the check box
                                          			 next to the ERL name. The Enter Route Patterns for ERL Migration window appears. |
| Step 4 | Enter an updated
                                          			 route/pattern translation pattern in the adjacent text box. |
| Step 5 | Click Migrate to Conventional ERL . |

| Step 1 | Choose ERL > National E911 Service Provider ERL > National E911 Service Provider Schedule from Emergency Responder. The National E911 Service Provider Schedule page appears. |
|---|---|
| Step 2 | Choose the days
                                       			 of the week and the time of day that you want to schedule an update. |
| Step 3 | Check the Enable Schedule check box if you want to activate this schedule. |
| Step 4 | Choose either ALI Update Schedule or Secondary Status Update Schedule . |
| Step 5 | Click Add to add the schedule to the list of schedules. |

| Step 1 | From Emergency Responder, choose ERL National E911 Service Provider ERL National E911 Service Provider Schedule . The National E911 Service Provider Schedule page appears. |
|---|---|
| Step 2 | Click the Edit link adjacent to the schedule that you want to
                                       			 update. |
| Step 3 | Choose the days
                                       			 of the week and the time of day. |
| Step 4 | Check the Enable Schedule check box to activate this schedule. |
| Step 5 | Click Update to change the schedule on the list of
                                       			 schedules. |