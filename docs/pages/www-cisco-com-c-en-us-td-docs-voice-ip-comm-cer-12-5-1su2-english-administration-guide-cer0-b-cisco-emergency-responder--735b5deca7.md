---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-12-5-1su2-english-administration-guide-cer0-b-cisco-emergency-responder--735b5deca7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/12_5_1su2/english/administration/guide/cer0_b_cisco-emergency-responder-administration-guide-1251SU2/cer0_b_cisco-emergency-responder-administration-guide-1251su3_chapter_0101.html
retrieved_at: 2026-08-21T15:46:22.511947+00:00
---

Cisco Emergency Responder Administration Guide for Release 12.5(1)SU2

# Cisco Emergency Responder Administration Guide for Release 12.5(1)SU2

Updated: November 23, 2021

Chapter: Configure Emergency Responder and Intrado V9-1-1 Enterprise Services

## Chapter: Configure Emergency Responder and Intrado V9-1-1 Enterprise Services

# Configure Emergency Responder and Intrado V9-1-1 Enterprise Services

## Emergency Responder and Intrado V9-1-1 Enterprise Services Overview

Cisco Emergency Responder (Emergency Responder) supports Intrado V9-1-1 for Enterprise Service in the Cisco Unified Communications environment as an alternative to direct connection with the Local
                           Exchange Carrier (LEC). The Intrado V9-1-1 for Enterprise Service provides local routing and emergency service response for Intrado customers. Emergency Responder works in conjunction with Intrado to provide emergency services to phones that are on the corporate network (on-premise) and phones that are located away from
                           the corporate network (off-premise).

For more information about configuring Emergency Responder, managing Emergency Responder users, working with ERLs, and other
                           related topics, see the "Add Scheduled Intrado Updates" section.

These topics provide an overview of how Emergency Responder operates with Intrado V9-1-1 for Enterprise Service and how to configure and use Emergency Responder to support Intrado V9-1-1 Enterprise users.

## Intrado V9-1-1 for Enterprise Service

If you are a subscriber to Intrado V9-1-1 for Enterprise Service, you can use Emergency Responder to simplify emergency call management. Emergency Responder provides
                           an interface that allows you to enter and synchronize location information directly to the Intrado database. Emergency Responder provides location information for emergency calls for both on-premise phones and off-premise
                           phones and works with Intrado and Unified CM to complete emergency calls.

Emergency Responder tracks IP phones by the IP subnet or when someone manually configures and assigns the MAC address. Emergency
                           Responder maintains the status of the phones (on-premise, off-premise, unlocated), and passes on any ALI or ELIN information
                           to Intrado . Users with on-premise phones rely on Cisco Unified Communications to route their emergency calls to Intrado and the designated emergency provider.

Users with
                           		off-premise phones cannot make emergency calls until the users enter in their
                           		location and associate this information with their directory number. After the
                           		location information has been verified, emergency calls placed from off-premise
                           		phones can be completed.

Users can only
                                       		  configure one off-premise location for each DID (DN + External Mask). This
                                       		  configuration also applies to shared lines. If two off-premise phones share a
                                       		  DID, the user can only associate one location to the DID.

The following figure shows the interactions between users, Emergency Responder, and Intrado .

### Emergency Call
                           	 Flow

When a user
                              		makes an emergency call:

Unified CM routes
                                    			 the call to Emergency Responder.

Emergency Responder routes the call to Intrado .

Intrado receives the 10-digit ELIN for the calling party and obtains the ALI data for the caller from this calling party number.

Intrado completes the call.

## Set Up Support for Intrado V9-1-1 for Enterprise Service

After you have confirmed your emergency service support with Intrado , you must configure Emergency Responder to support Intrado V9-1-1 for Enterprise Service.

You must complete the tasks described in the following procedure before creating Intrado ERLs.

Step 1

Configure the
                                       			 following items in the Validation and Update Interface (VUI):

Upload the certificate provided by Intrado .

Validate the
                                             				  certificate.

Configure Intrado Account Information.

Step 2

Configure Route Patterns for routing calls to Intrado on the Emergency Responder server.

Step 3

Configure Route Patterns and gateway for routing calls to Intrado on Unified CM server.

See Understanding Route Plans chapter in Cisco Unified Communications Manager System Guide, and the "Gateway Configuration" chapter in the Cisco Unified Communications Manager Administration Guide .

Step 4

Create Intrado ERL and verify the validity and consistency of the ALI data for the Intrado ERL against the Intrado TN database.

Step 5

Assign Intrado ERLs to switch ports, IP subnets, and unlocated phones.

### Set Up Intrado VUI Settings

Before you can configure Intrado VUI settings, you must have your account information and a certificate from Intrado .

To continue
                                             			 emergency service support when there is a failover to the Emergency Responder
                                             			 subscriber, you must upload the certificate file to the Emergency Responder
                                             			 subscriber separately.

After upgrading the Cisco Emergency Responder, upload the certificate again to continue using the Intrado Service.

Step 1

From Emergency Responder, choose System > Intrado VUI Settings.

The Intrado VUI Settings page displays.

Step 2

Click Upload
                                             				Certificate .

Step 3

Use the Browse button to locate the Intrado certificate file, highlight the file, and click the Upload button.

Step 4

Enter the Certificate Password and the VUI URL in the adjacent text boxes. Click Test and Validate .

Step 5

Enter the
                                          			 Account Information.

VUI Schema
                                                   					 URL

Intrado Account ID

Max VUI
                                                   					 Connections

Step 6

Click Update .

For more information about the Intrado VUI settings, see Intrado VUI Settings .

Step 7

Click Test Connectivity to verify whether Emergency Responder can successfully connect to the customer specific account through the Intrado VUI.

### Set Up Intrado Patterns on Emergency Responder

Before any emergency calls can be completed by Intrado V9-1-1 for Enterprise Service, you must configure the route patterns for routing the call to Intrado .

Step 1

From Emergency
                                          			 Responder, Choose System > Telephony Settings.

The Telephony
                                             				Settings page is displayed.

Step 2

Under Intrado Route Pattern Settings, enter the Intrado Route/ Translation Pattern and click the Add button.

### Set Up Intrado ERLs

#### Before you begin

You must first configure Intrado route patterns before you can add any Intrado ERLs.

Intrado ERLs differ from conventional ERLs in the following ways:

You can only select route patterns from a preconfigured list in the Telephony Settings web page.

You can query and validate ALI data from Intrado by using Intrado VUI (Validation & Update interface).

You must submit ALI data (TN Update) to Intrado by using Intrado VUI before an emergency call can be successfully routed.

Step 1

From Emergency Responder, choose ERL > Intrado ERL > Intrado ERL(Search and List) .

The Find Intrado ERL Data page displays.

Step 2

Click the Add New
                                             				ERL button.

Emergency
                                             				Responder opens the Add New ERL window. See Find Intrado ERL for a detail explanation of each
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

Enter the ALI Information. The "ALI Information section", Cisco Emergency Responder Administration Web Interface Appendix A , contains detailed explanations of each field. To look up an address in the Intrado MSAG database, click Query from Intrado .

Step 6

After entering the ALI Information, click Pre-validate from Intrado .

Step 7

Make the Add
                                          			 New ERL window the active window if it is not, and click Insert .

Emergency
                                             				Responder saves the ERL and its ALI.

#### Intrado ERL Imports

If you have
                                 		multiple ERLs, and you want to add them all at once, you can create a file that
                                 		contains more than one ERL definition, and import all the ERLs at the same time
                                 		into your Emergency Responder configuration. For more information about
                                 		importing ERLs, see Import Several ERLs .

#### Intrado ERL Information Export

Use the
                                    		  Export ERL page to create ERL export files for our own use, for example, to
                                    		  back up or move an ERL configuration. For more information about importing
                                    		  ERLs, see Export ERL Information .

### Reconcile ALI
                           	 Discrepancies

You can use Emergency Responder to compare the records from Intrado VUI with the records in the database and displays ALI records that have discrepancies. You can examine each record and choose
                                 to update the local record with information from Intrado or update Intrado 's record.

Step 1

In Emergency Responder Administration, choose ERL > Intrado ERL > View ALI Discrepancies .

The View Intrado ALI Discrepancies page appears.

Step 2

Enter search criteria to find any specific ELINS and click Find , or click Find without any search criteria to display all Intrado ALI discrepancies. The search results appear.

Step 3

Click on the radio button next to the ELIN that you want to view or click View ALI Discrepancies to launch the View Intrado ALI discrepancies for a particular ELIN.

The View Intrado ALI Discrepancies for a particular ELIN window appears.

Step 4

Choose the correct data from either the local Emergency Responder database or from Intrado .

Step 5

Click Save to save changes to the local Emergency Responder database. Click Save Intrado ALI Info to save changes to the Intrado VUI.

Step 6

Click Close to close this window.

## ERL Data
                        	 Migration

Emergency Responder supports migrating existing conventional ERLs to Intrado ERLs and vice versa.

### Migrate Conventional ERL Data to Intrado ERL Data

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

Click Migrate to Intrado ERL .

### Migrate Intrado ERL Data to Conventional ERL Data

Step 1

In Emergency Responder Administration, choose ERL > ERL Migration Tool .

Step 2

Choose Intrado ERL in the search parameter drop-down list, enter the search criteria, and click Find .

Step 3

Select the ERLs that you wish to migrate by checking the check box
                                          			 next to the ERL name.

Step 4

Enter an updated
                                          			 route/pattern translation pattern in the adjacent text box.

Step 5

Click Migrate to Conventional ERL .

## Add Scheduled Intrado Updates

You can create ALI and Secondary Status update schedules between Emergency Responder and Intrado . A scheduled ALI update sends newly created TN records to Intrado . A scheduled Secondary Status update sends queries to Intrado requesting information about records with errors that have been corrected.

Step 1

Choose ERL > Intrado ERL > Intrado Schedule from Emergency Responder.

Step 2

Choose the days
                                       			 of the week and the time of day that you want to schedule an update.

Step 3

Check the Enable Schedule check box if you want to activate this schedule.

Step 4

Choose either ALI Update Schedule or Secondary Status Update Schedule .

Step 5

Click Add to add the schedule to the list of schedules.

## Update Scheduled Intrado Update

Step 1

From Emergency Responder, choose ERL Intrado ERL Intrado Schedule .

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

| Note | You must configure the IP address of the DNS server to resolve the URLs provided by Intrado before completing these tasks. See Cisco Unified Operating System Administration Web Interface For Cisco Emergency Responder . |
|---|---|

| Step 1 | Configure the
                                       			 following items in the Validation and Update Interface (VUI): Upload the certificate provided by Intrado . Validate the
                                             				  certificate. Configure Intrado Account Information. |
|---|---|
| Step 2 | Configure Route Patterns for routing calls to Intrado on the Emergency Responder server. |
| Step 3 | Configure Route Patterns and gateway for routing calls to Intrado on Unified CM server. See Understanding Route Plans chapter in Cisco Unified Communications Manager System Guide, and the "Gateway Configuration" chapter in the Cisco Unified Communications Manager Administration Guide . |
| Step 4 | Create Intrado ERL and verify the validity and consistency of the ALI data for the Intrado ERL against the Intrado TN database. |
| Step 5 | Assign Intrado ERLs to switch ports, IP subnets, and unlocated phones. |

| Note | To continue
                                             			 emergency service support when there is a failover to the Emergency Responder
                                             			 subscriber, you must upload the certificate file to the Emergency Responder
                                             			 subscriber separately. |
|---|---|

| Note | After upgrading the Cisco Emergency Responder, upload the certificate again to continue using the Intrado Service. |
|---|---|

| Step 1 | From Emergency Responder, choose System > Intrado VUI Settings. The Intrado VUI Settings page displays. |
|---|---|
| Step 2 | Click Upload
                                             				Certificate . An Upload
                                          			 Certificate window opens. |
| Step 3 | Use the Browse button to locate the Intrado certificate file, highlight the file, and click the Upload button. |
| Step 4 | Enter the Certificate Password and the VUI URL in the adjacent text boxes. Click Test and Validate . |
| Step 5 | Enter the
                                          			 Account Information. VUI Schema
                                                   					 URL Intrado Account ID Max VUI
                                                   					 Connections |
| Step 6 | Click Update . Note To replace the Intrado VUI certificate, you must delete the existing Intrado account and then proceed from Step 1. Else, the Upload Certificate option will be grayed out. For more information about the Intrado VUI settings, see Intrado VUI Settings . | Note | To replace the Intrado VUI certificate, you must delete the existing Intrado account and then proceed from Step 1. Else, the Upload Certificate option will be grayed out. |
| Note | To replace the Intrado VUI certificate, you must delete the existing Intrado account and then proceed from Step 1. Else, the Upload Certificate option will be grayed out. |
| Step 7 | Click Test Connectivity to verify whether Emergency Responder can successfully connect to the customer specific account through the Intrado VUI. |

| Note | To replace the Intrado VUI certificate, you must delete the existing Intrado account and then proceed from Step 1. Else, the Upload Certificate option will be grayed out. |
|---|---|

| Step 1 | From Emergency
                                          			 Responder, Choose System > Telephony Settings. The Telephony
                                             				Settings page is displayed. |
|---|---|
| Step 2 | Under Intrado Route Pattern Settings, enter the Intrado Route/ Translation Pattern and click the Add button. |

| Note | Intrado ERLs differ from conventional ERLs in the following ways: You can only select route patterns from a preconfigured list in the Telephony Settings web page. You can query and validate ALI data from Intrado by using Intrado VUI (Validation & Update interface). You must submit ALI data (TN Update) to Intrado by using Intrado VUI before an emergency call can be successfully routed. |
|---|---|

| Step 1 | From Emergency Responder, choose ERL > Intrado ERL > Intrado ERL(Search and List) . The Find Intrado ERL Data page displays. |
|---|---|
| Step 2 | Click the Add New
                                             				ERL button. Emergency
                                             				Responder opens the Add New ERL window. See Find Intrado ERL for a detail explanation of each
                                             				field. |
| Step 3 | Fill in the
                                          			 ERL Information. |
| Step 4 | Click ALI
                                             				Details Emergency
                                             				Responder opens the ALI Information window. |
| Step 5 | Enter the ALI Information. The "ALI Information section", Cisco Emergency Responder Administration Web Interface Appendix A , contains detailed explanations of each field. To look up an address in the Intrado MSAG database, click Query from Intrado . |
| Step 6 | After entering the ALI Information, click Pre-validate from Intrado . |
| Step 7 | Make the Add
                                          			 New ERL window the active window if it is not, and click Insert . Emergency
                                             				Responder saves the ERL and its ALI. |

| Step 1 | In Emergency Responder Administration, choose ERL > Intrado ERL > View ALI Discrepancies . The View Intrado ALI Discrepancies page appears. |
|---|---|
| Step 2 | Enter search criteria to find any specific ELINS and click Find , or click Find without any search criteria to display all Intrado ALI discrepancies. The search results appear. |
| Step 3 | Click on the radio button next to the ELIN that you want to view or click View ALI Discrepancies to launch the View Intrado ALI discrepancies for a particular ELIN. The View Intrado ALI Discrepancies for a particular ELIN window appears. |
| Step 4 | Choose the correct data from either the local Emergency Responder database or from Intrado . |
| Step 5 | Click Save to save changes to the local Emergency Responder database. Click Save Intrado ALI Info to save changes to the Intrado VUI. |
| Step 6 | Click Close to close this window. |

| Step 1 | In Emergency Responder Administration, choose ERL > ERL Migration Tool . The ERL Migration Tool page appears. |
|---|---|
| Step 2 | Choose Conventional ERL in the search parameter drop-down list, enter the search criteria, and click Find . |
| Step 3 | Select the ERLs
                                          			 that you want to migrate by checking the check box next to the ERL name. The Enter Route
                                             				Patterns for ERL Migration window appears. |
| Step 4 | Choose an updated route pattern from the drop-down list. |
| Step 5 | Click Migrate to Intrado ERL . |

| Step 1 | In Emergency Responder Administration, choose ERL > ERL Migration Tool . The ERL Migration Tool page appears. |
|---|---|
| Step 2 | Choose Intrado ERL in the search parameter drop-down list, enter the search criteria, and click Find . |
| Step 3 | Select the ERLs that you wish to migrate by checking the check box
                                          			 next to the ERL name. The Enter Route Patterns for ERL Migration window appears. |
| Step 4 | Enter an updated
                                          			 route/pattern translation pattern in the adjacent text box. |
| Step 5 | Click Migrate to Conventional ERL . |

| Step 1 | Choose ERL > Intrado ERL > Intrado Schedule from Emergency Responder. The Intrado Schedule page appears. |
|---|---|
| Step 2 | Choose the days
                                       			 of the week and the time of day that you want to schedule an update. |
| Step 3 | Check the Enable Schedule check box if you want to activate this schedule. |
| Step 4 | Choose either ALI Update Schedule or Secondary Status Update Schedule . |
| Step 5 | Click Add to add the schedule to the list of schedules. |

| Step 1 | From Emergency Responder, choose ERL Intrado ERL Intrado Schedule . The Intrado Schedule page appears. |
|---|---|
| Step 2 | Click the Edit link adjacent to the schedule that you want to
                                       			 update. |
| Step 3 | Choose the days
                                       			 of the week and the time of day. |
| Step 4 | Check the Enable Schedule check box to activate this schedule. |
| Step 5 | Click Update to change the schedule on the list of
                                       			 schedules. |