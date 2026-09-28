---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-exchange-integration-12-5-1-cup0-b-ms-outlook-calendar-inte-1dd4bec878
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/exchange_integration/12_5_1/cup0_b_ms-outlook-calendar-integration-1251/cup0_b_ms-outlook-calender-integration-1251_chapter_01000.html
retrieved_at: 2026-08-16T17:27:30.079753+00:00
---

Microsoft Outlook Calendar Integration for the IM and Presence Service, Release 12.5(1)

# Microsoft Outlook Calendar Integration for the IM and Presence Service, Release 12.5(1)

Updated: January 23, 2019

Chapter: Troubleshooting Exchange Calendaring Integrations

## Chapter: Troubleshooting Exchange Calendaring Integrations

# Troubleshooting Exchange Calendaring Integrations

## Troubleshooting Exchange Server Connection Status

Exchange
                              		  Server connection status displays under the Cisco Unified CM 
                                 		  IM and
                                 			 Presence Administration window after you configure the Exchange Presence
                              		  Gateway for  an Exchange Web Services (EWS) calendaring
                              		  integration (choose Presence > Gateways ). The Exchange Server Status area in the Presence Gateway
                                 Configuration window reports the status on the connection
                              		  between the IM and
                                 			 Presence Service and the Exchange Server.

You can add,
                                          			 update or delete 
                                          			 one or more
                                          			 EWS servers with no maximum limit. However, the Exchange Server Status area in the Presence Gateway
                                             Configuration window is designed to only verify and report status of the first 10 EWS
                                          			 servers that you configure.

.

Test

Status Description and Recommended Action

Exchange Reachability (pingable)

The IM
                                             						  and Presence Service successfully reached (pinged) the Exchange
                                          						Server.

Exchange Reachability (unreachable)

The IM
                                             						  and Presence Service failed to ping the Exchange Server. The server
                                          						may not be reachable due to an incorrect field value or an issue with
                                          						the customer's network, for example, cabling.

To resolve this, ensure that the Presence Gateway field contains
                                          						the correct value (FQDN or IP address) to reach the Exchange Server over the
                                          						network. Note that the UI does not require the Presence Gateway field value to
                                          						be the Subject CN value.

If you have connection problems with the Exchange Server, also
                                          						see the System Troubleshooter in Cisco Unified CM 
                                             						IM
                                             						  and Presence  Administration and implement the recommended solution.
                                          						Choose Diagnostics > System
                                                							 Troubleshooter .

## Troubleshooting SSL Connection Certificate Status

SSL
                              		  Connection/Certificate Verification status displays in Cisco Unified CM IM and
                                 			 Presence Administration window when you configure the Exchange Presence
                              		  Gateway for an Exchange Web Services (EWS) calendaring
                              		  integration (choose Presence > Gateways ). The Exchange Server Status area in the Presence Gateway
                                 Configuration window indicates if there is a certificate
                              		  Subject CN mismatch or a SAN mismatch.

You can add,
                                          			 update or delete one or
                                             				more EWS servers with no maximum limit. However, the Troubleshooter on the Presence Gateway window is designed to only verify
                                          			 and report status of the first 10 EWS servers that you configure.

Test

Status Description and Recommended Action

SSL Connection/Certificate Verification - Verified

The IM and Presence
                                             						  Service verified the SSL connection with the Exchange Server. Click View for the certificate details.

SSL Connection/Certificate Verification Failed - Certificate
                                          						Missing From Chain

These
                                                      						  instructions describe the view of the customized Certificate Import Tool. If
                                                      						  you are simply verifying connection status, the tool indicates the verified
                                                      						  status but you do not have the option to Save .

One or more certificates that the IM and Presence
                                             						  Service requires to establish a secure connection to the Exchange
                                          						Server are missing. The Certificate Viewer can provide details of the missing
                                          						certificates.

Complete these steps in the Certificate Viewer to display any
                                          						missing certificates:

Chose Configure to open the Certificate Viewer.

Check
                                                							 the Accept Certificate Chain check box 
                                                							 .

Click Save .

The
                                                							 certificate chain details display. Note any certificates with a status of
                                                							 Missing.

Close
                                                							 the Certificate Viewer.

To
                                          						complete the certificate chain, you must:

Download the missing certificates files from the Exchange
                                                							 Server.

Copy
                                                							 or FTP the missing certificate files to the computer that you use to administer
                                                							 
                                                							 the IM and Presence Service .

Use Cisco Unified 
                                                   							 IM and Presence  OS Administration to upload any of the
                                                							 required missing certificates.

Troubleshooting Tips

Log in to the Cisco Unified 
                                                         								  IM and Presence OS Administration and user interface and upload
                                                      								  certificates to complete the certificate chain.

Return to the Presence Gateway Configuration window under the Cisco
                                                         								  Unified CM IM and
                                                         									 Presence Administration user interface, reopen the Certificate Viewer, and verify
                                                      								  that all certificates in the certificate chain now have a status of Verified.

- You must restart the Cisco
                                             						  Presence Engine after you upload Exchange trust certificates.

- Log in to Cisco Unified 
                                                								IM and Presence Serviceability user interface.

- Choose Tools > Service
                                                   								Activation . Note that this can affect Calendaring
                                             						  connectivity.

- Choose either Configure or View to launch the Certificate Chain Viewer. The Configure button displays if there are any issues with the
                                             						  certificate chain that the IM and Presence Service downloads from the Exchange Server. For
                                             						  example, the missing certificates scenario described above. Once you
                                             						  successfully import and verify the certificate chain, the SSL Connection /
                                             						  Certificate Verification status updates to Verified and the View button replaces Configure .

SSL Connection/Certificate Verification Failed- Subject CN
                                          						Mismatch

The Presence Gateway field value must match the Subject CN value
                                          						of the leaf certificate in the Certificate Chain. You can resolve this by
                                          						entering the correct value in the Presence Gateway field.

Verify that your entry in the Presence Gateway field is correct
                                          						as follows:

Re-enter the correct Subject CN value in the Presence Gateway
                                                							 field. The IM and Presence
                                                   								Service uses the Presence Gateway field value to ping the server. The
                                                							 host (FQDN or IP address) that you enter must exactly match the IIS certificate
                                                							 Subject Common Name.

Click Save .

Tip

Choose either Configure or View to launch the Certificate Chain Viewer. The Configure button displays if there are any issues with the
                                                      						  certificate chain downloaded from the Exchange Server. For example, the
                                                      						  missing certificates scenario described above. Once you successfully import and
                                                      						  verify the certificate chain, the SSL Connection / Certificate Verification
                                                      						  status updates to Verified and the View button replaces Configure .

SSL
                                          						Connection/Certificate Verification Failed - SAN Mismatch

The
                                          						Presence Gateway field value must match one of the Subject Alternative Name
                                          						(SAN) values of the leaf certificate in the Certificate Chain. You can resolve
                                          						this by entering the correct value in the Presence Gateway field.

Verify
                                          						that your entry in the Presence Gateway field is correct as follows:

Re-enter the correct SAN value in the Presence Gateway field.
                                                							 The IM and Presence
                                                   								Service uses the Presence Gateway field value to ping the server. The
                                                							 host (FQDN or IP address) that you enter must exactly match one of the entries
                                                							 in the certificate Subject Alternative Name.

Click Save .

Tip

Choose
                                                      						  either Configure or View to launch the Certificate Chain Viewer. The Configure button displays if there are any issues with the
                                                      						  certificate chain downloaded from the Exchange Server. For example, the
                                                      						  missing certificates scenario described above. Once you successfully import and
                                                      						  verify the certificate chain, the SSL Connection / Certificate Verification
                                                      						  status updates to Verified and the View button replaces Configure .

SSL Connection/Certificate Verification Failed - Bad
                                          						Certificates

Information in the certificate is incorrect, which renders it
                                          						invalid.

Typically, this occurs if the certificate matches the required
                                          						Subject CN but not the public key. This could happen if the Exchange Server
                                          						regenerates the certificate but the IM and Presence
                                             						  Service node still maintains the old certificate.

To resolve this, complete these actions:

- Choose the logs to
                                             						  determine the cause of the error.

- If the error is due to a
                                             						  bad signature, you need to remove the outdated certificate from the IM and Presence
                                                							 Service in CiscoUnified 
                                             						  IM and Presence OS Administration, and then upload a
                                             						  new certificate in CiscoUnified 
                                             						  IM and Presence OS Administration.

- If the error is due to an
                                             						  unsupported algorithm, you need to upload a new certificate that contains the
                                             						  supported algorithm in CiscoUnified 
                                             						  IM and Presence OS Administration.

SSL Connection / Certificate Verification Failed - Network Error

Due to network issues, for example, a no-response timeout, the IM and Presence
                                             						  Service cannot verify the SSL connection.

We recommend that you verify the network connectivity to the
                                          						Exchange Server, and ensure that the Exchange Server is accepting connections
                                          						using the correct IP address and port number.

SSL Connection/Certificate Verification Failed

Verification failed for a non-specific reason or because the IM and Presence
                                             						  Service cannot perform the reachability test.

We recommend that you review the debug log files for more
                                          						information.

## Issues Known to Impact Microsoft Exchange Integrations

This section describes known issues that are common or specific to
                              		   Microsoft Exchange Server  2007,   2010, and 2013.

### Scale Limitations for Calendar Integrations

Cisco Unified Communications
                                    			 Manager IM and
                                    			 Presence Service and Exchange calendaring integrations have been
                                 		  validated with up to X% of the users subscribing to calendar presence and with
                                 		  up to Y% of the users doing simultaneous calendar transitions (for example,
                                 		  joining or leaving meetings simultaneously). See 
                                 		  the table below for percentage values pertaining to
                                 		  specific releases of Cisco
                                 			 Unified Presence.

Software Release

%
                                             					 of Users Subscribing to Calendar Presence

%
                                             					 of Users Performing Simultaneous Calendar Transitions

8.5(1)

50

30

8.5(2) and later

100

50

### Calendar State Does
                           	 Not Update if a User Moves Between Microsoft Exchange Servers

#### Problem

If an
                                 		  Exchange administrator moves a user from one Exchange Server to another in an
                                 		  Exchange integration, the calendaring state change does not update for that
                                 		  user.

#### Cause

The
                                 		  condition occurs because the Exchange Server does not signal when a user is
                                 		  moved from one server to another.

#### Solution

The IM and
                                    			 Presence Service administrator or user must disable and then reenable
                                 		  calendar integration for that user after the
                                 		  Exchange administrator has moved the user from one Exchange Server to another.

### LDAP User Removal
                           	 Takes at Least 24 Hours to Replicate on the IM and Presence Service

#### Problem

If a user
                                 		  is deleted from LDAP, the user state changes to Inactive on CiscoUnified
                                    		  Communications Manager and user authentication on client applications
                                 		  subsequently fails. However, it has been observed during testing that once CiscoUnified Communications Manager synchronizes the change from LDAP, the
                                 		  user is not removed for 24 hours after the
                                 		  synchronization occurred (either by the Administrator forcing the
                                 		  synchronization or scheduling it to occur at a specific time).

The Cisco
                                 		  Sync Agent on the IM and
                                    			 Presence Service does not synchronize any user state change until the
                                 		  user is removed. Until then, that user still exists on CiscoUnified
                                    		  Communications Manager and all IM and
                                    			 Presence Service capabilities (including Exchange calendaring
                                 		  subscriptions) remain licensed for that user for 24 hours. This delay means
                                 		  that users who were logged in to Cisco Jabber before
                                 		  the user was removed from LDAP are not logged out automatically. The user’s
                                 		  pre-existing calendar state (Available, Busy) persists for that user on the IM and
                                    			 Presence Service until the user logs out of the client.

#### Cause

The
                                 		  condition occurs when CiscoUnified Communications Manager is set up and LDAP
                                 		  authentication is used. When a user is deleted from LDAP, calendaring
                                 		  subscriptions continue to be established and updated for that user on the IM and
                                    			 Presence Service for a period of at least 24 hours.

#### Solution

If a user
                                 		  is removed from LDAP, you can manually remove the license for that user so that
                                 		  the IM and
                                    			 Presence Service ends the Exchange calendaring subscriptions with
                                 		  immediate effect and logs the user out of the client application. Otherwise, be
                                 		  aware that there may be a 24 hour delay.

### Verifying That the Microsoft Exchange Server URL Contains the Localized Word for Calendar

If you are
                                 		  localizing your Calendaring integration, verify that the Exchange Server URL
                                 		  contains the localized word for Calendar.

Step 1

Install the same
                                          			 language locales (load the locale installer) on both the IM and
                                             				Presence Service and Cisco 
                                             			 Unified Communications Manager . For more information about
                                          			 installing locales on the IM and
                                             				Presence Service , see 
                                          			 Configuration of Multilingual Support for Calendar Integration.

Step 2

Restart the IM and
                                             				Presence Service node, and log in to the Cisco Unified CM 
                                             			 IM and
                                             				Presence  Administration user interface.

Step 3

Find and delete
                                          			 the existing Exchange Presence Gateway that supports a different locale for
                                          			 calendaring (choose Presence > Gateways ).

Step 4

Add a new
                                          			 Exchange Presence (Outlook) Gateway. Click Add
                                             				New .

Step 5

Verify in the
                                          			 database (pebackendgateway table) that the 'localecalendarname' attribute is in
                                          			 whichever language locale you have installed.

Step 6

Ensure the user
                                          			 locale is set after the locale is installed on both the IM and
                                             				Presence Service and  toggling the user locale on the Cisco Unified Communications Manager , if necessary.

| Note | You can add,
                                          			 update or delete 
                                          			 one or more
                                          			 EWS servers with no maximum limit. However, the Exchange Server Status area in the Presence Gateway
                                             Configuration window is designed to only verify and report status of the first 10 EWS
                                          			 servers that you configure. |
|---|---|

| Test | Status Description and Recommended Action |
|---|---|
| Exchange Reachability (pingable) | The IM
                                             						  and Presence Service successfully reached (pinged) the Exchange
                                          						Server. |
| Exchange Reachability (unreachable) | The IM
                                             						  and Presence Service failed to ping the Exchange Server. The server
                                          						may not be reachable due to an incorrect field value or an issue with
                                          						the customer's network, for example, cabling. To resolve this, ensure that the Presence Gateway field contains
                                          						the correct value (FQDN or IP address) to reach the Exchange Server over the
                                          						network. Note that the UI does not require the Presence Gateway field value to
                                          						be the Subject CN value. If you have connection problems with the Exchange Server, also
                                          						see the System Troubleshooter in Cisco Unified CM 
                                             						IM
                                             						  and Presence  Administration and implement the recommended solution.
                                          						Choose Diagnostics > System
                                                							 Troubleshooter . |

| Note | You can add,
                                          			 update or delete one or
                                             				more EWS servers with no maximum limit. However, the Troubleshooter on the Presence Gateway window is designed to only verify
                                          			 and report status of the first 10 EWS servers that you configure. |
|---|---|

| Test | Status Description and Recommended Action |
|---|---|
| SSL Connection/Certificate Verification - Verified | The IM and Presence
                                             						  Service verified the SSL connection with the Exchange Server. Click View for the certificate details. |
| SSL Connection/Certificate Verification Failed - Certificate
                                          						Missing From Chain Note These
                                                      						  instructions describe the view of the customized Certificate Import Tool. If
                                                      						  you are simply verifying connection status, the tool indicates the verified
                                                      						  status but you do not have the option to Save . | Note | These
                                                      						  instructions describe the view of the customized Certificate Import Tool. If
                                                      						  you are simply verifying connection status, the tool indicates the verified
                                                      						  status but you do not have the option to Save . | One or more certificates that the IM and Presence
                                             						  Service requires to establish a secure connection to the Exchange
                                          						Server are missing. The Certificate Viewer can provide details of the missing
                                          						certificates. Complete these steps in the Certificate Viewer to display any
                                          						missing certificates: Chose Configure to open the Certificate Viewer. Check
                                                							 the Accept Certificate Chain check box 
                                                							 . Click Save . The
                                                							 certificate chain details display. Note any certificates with a status of
                                                							 Missing. Close
                                                							 the Certificate Viewer. To
                                          						complete the certificate chain, you must: Download the missing certificates files from the Exchange
                                                							 Server. Copy
                                                							 or FTP the missing certificate files to the computer that you use to administer
                                                							 
                                                							 the IM and Presence Service . Use Cisco Unified 
                                                   							 IM and Presence  OS Administration to upload any of the
                                                							 required missing certificates. Troubleshooting Tips If the certificates are not
                                             						  available in the Certificate Viewer, you may need to manually download and
                                             						  install the missing certificates from the Exchange Server, and upload these
                                             						  certificates in Cisco Unified 
                                                						  IM and Presence OS Administration as follows: Log in to the Cisco Unified 
                                                         								  IM and Presence OS Administration and user interface and upload
                                                      								  certificates to complete the certificate chain. Return to the Presence Gateway Configuration window under the Cisco
                                                         								  Unified CM IM and
                                                         									 Presence Administration user interface, reopen the Certificate Viewer, and verify
                                                      								  that all certificates in the certificate chain now have a status of Verified. You must restart the Cisco
                                             						  Presence Engine after you upload Exchange trust certificates. Log in to Cisco Unified 
                                                								IM and Presence Serviceability user interface. Choose Tools > Service
                                                   								Activation . Note that this can affect Calendaring
                                             						  connectivity. Choose either Configure or View to launch the Certificate Chain Viewer. The Configure button displays if there are any issues with the
                                             						  certificate chain that the IM and Presence Service downloads from the Exchange Server. For
                                             						  example, the missing certificates scenario described above. Once you
                                             						  successfully import and verify the certificate chain, the SSL Connection /
                                             						  Certificate Verification status updates to Verified and the View button replaces Configure . |
| Note | These
                                                      						  instructions describe the view of the customized Certificate Import Tool. If
                                                      						  you are simply verifying connection status, the tool indicates the verified
                                                      						  status but you do not have the option to Save . |
| SSL Connection/Certificate Verification Failed- Subject CN
                                          						Mismatch | The Presence Gateway field value must match the Subject CN value
                                          						of the leaf certificate in the Certificate Chain. You can resolve this by
                                          						entering the correct value in the Presence Gateway field. Verify that your entry in the Presence Gateway field is correct
                                          						as follows: Re-enter the correct Subject CN value in the Presence Gateway
                                                							 field. The IM and Presence
                                                   								Service uses the Presence Gateway field value to ping the server. The
                                                							 host (FQDN or IP address) that you enter must exactly match the IIS certificate
                                                							 Subject Common Name. Click Save . Tip Choose either Configure or View to launch the Certificate Chain Viewer. The Configure button displays if there are any issues with the
                                                      						  certificate chain downloaded from the Exchange Server. For example, the
                                                      						  missing certificates scenario described above. Once you successfully import and
                                                      						  verify the certificate chain, the SSL Connection / Certificate Verification
                                                      						  status updates to Verified and the View button replaces Configure . | Tip | Choose either Configure or View to launch the Certificate Chain Viewer. The Configure button displays if there are any issues with the
                                                      						  certificate chain downloaded from the Exchange Server. For example, the
                                                      						  missing certificates scenario described above. Once you successfully import and
                                                      						  verify the certificate chain, the SSL Connection / Certificate Verification
                                                      						  status updates to Verified and the View button replaces Configure . |
| Tip | Choose either Configure or View to launch the Certificate Chain Viewer. The Configure button displays if there are any issues with the
                                                      						  certificate chain downloaded from the Exchange Server. For example, the
                                                      						  missing certificates scenario described above. Once you successfully import and
                                                      						  verify the certificate chain, the SSL Connection / Certificate Verification
                                                      						  status updates to Verified and the View button replaces Configure . |
| SSL
                                          						Connection/Certificate Verification Failed - SAN Mismatch | The
                                          						Presence Gateway field value must match one of the Subject Alternative Name
                                          						(SAN) values of the leaf certificate in the Certificate Chain. You can resolve
                                          						this by entering the correct value in the Presence Gateway field. Verify
                                          						that your entry in the Presence Gateway field is correct as follows: Re-enter the correct SAN value in the Presence Gateway field.
                                                							 The IM and Presence
                                                   								Service uses the Presence Gateway field value to ping the server. The
                                                							 host (FQDN or IP address) that you enter must exactly match one of the entries
                                                							 in the certificate Subject Alternative Name. Click Save . Tip Choose
                                                      						  either Configure or View to launch the Certificate Chain Viewer. The Configure button displays if there are any issues with the
                                                      						  certificate chain downloaded from the Exchange Server. For example, the
                                                      						  missing certificates scenario described above. Once you successfully import and
                                                      						  verify the certificate chain, the SSL Connection / Certificate Verification
                                                      						  status updates to Verified and the View button replaces Configure . | Tip | Choose
                                                      						  either Configure or View to launch the Certificate Chain Viewer. The Configure button displays if there are any issues with the
                                                      						  certificate chain downloaded from the Exchange Server. For example, the
                                                      						  missing certificates scenario described above. Once you successfully import and
                                                      						  verify the certificate chain, the SSL Connection / Certificate Verification
                                                      						  status updates to Verified and the View button replaces Configure . |
| Tip | Choose
                                                      						  either Configure or View to launch the Certificate Chain Viewer. The Configure button displays if there are any issues with the
                                                      						  certificate chain downloaded from the Exchange Server. For example, the
                                                      						  missing certificates scenario described above. Once you successfully import and
                                                      						  verify the certificate chain, the SSL Connection / Certificate Verification
                                                      						  status updates to Verified and the View button replaces Configure . |
| SSL Connection/Certificate Verification Failed - Bad
                                          						Certificates | Information in the certificate is incorrect, which renders it
                                          						invalid. Typically, this occurs if the certificate matches the required
                                          						Subject CN but not the public key. This could happen if the Exchange Server
                                          						regenerates the certificate but the IM and Presence
                                             						  Service node still maintains the old certificate. To resolve this, complete these actions: Choose the logs to
                                             						  determine the cause of the error. If the error is due to a
                                             						  bad signature, you need to remove the outdated certificate from the IM and Presence
                                                							 Service in CiscoUnified 
                                             						  IM and Presence OS Administration, and then upload a
                                             						  new certificate in CiscoUnified 
                                             						  IM and Presence OS Administration. If the error is due to an
                                             						  unsupported algorithm, you need to upload a new certificate that contains the
                                             						  supported algorithm in CiscoUnified 
                                             						  IM and Presence OS Administration. |
| SSL Connection / Certificate Verification Failed - Network Error | Due to network issues, for example, a no-response timeout, the IM and Presence
                                             						  Service cannot verify the SSL connection. We recommend that you verify the network connectivity to the
                                          						Exchange Server, and ensure that the Exchange Server is accepting connections
                                          						using the correct IP address and port number. |
| SSL Connection/Certificate Verification Failed | Verification failed for a non-specific reason or because the IM and Presence
                                             						  Service cannot perform the reachability test. We recommend that you review the debug log files for more
                                          						information. |

| Note | These
                                                      						  instructions describe the view of the customized Certificate Import Tool. If
                                                      						  you are simply verifying connection status, the tool indicates the verified
                                                      						  status but you do not have the option to Save . |
|---|---|

| Tip | Choose either Configure or View to launch the Certificate Chain Viewer. The Configure button displays if there are any issues with the
                                                      						  certificate chain downloaded from the Exchange Server. For example, the
                                                      						  missing certificates scenario described above. Once you successfully import and
                                                      						  verify the certificate chain, the SSL Connection / Certificate Verification
                                                      						  status updates to Verified and the View button replaces Configure . |
|---|---|

| Tip | Choose
                                                      						  either Configure or View to launch the Certificate Chain Viewer. The Configure button displays if there are any issues with the
                                                      						  certificate chain downloaded from the Exchange Server. For example, the
                                                      						  missing certificates scenario described above. Once you successfully import and
                                                      						  verify the certificate chain, the SSL Connection / Certificate Verification
                                                      						  status updates to Verified and the View button replaces Configure . |
|---|---|

| Software Release | %
                                             					 of Users Subscribing to Calendar Presence | %
                                             					 of Users Performing Simultaneous Calendar Transitions |
|---|---|---|
| 8.5(1) | 50 | 30 |
| 8.5(2) and later | 100 | 50 |

| Step 1 | Install the same
                                          			 language locales (load the locale installer) on both the IM and
                                             				Presence Service and Cisco 
                                             			 Unified Communications Manager . For more information about
                                          			 installing locales on the IM and
                                             				Presence Service , see 
                                          			 Configuration of Multilingual Support for Calendar Integration. |
|---|---|
| Step 2 | Restart the IM and
                                             				Presence Service node, and log in to the Cisco Unified CM 
                                             			 IM and
                                             				Presence  Administration user interface. |
| Step 3 | Find and delete
                                          			 the existing Exchange Presence Gateway that supports a different locale for
                                          			 calendaring (choose Presence > Gateways ). |
| Step 4 | Add a new
                                          			 Exchange Presence (Outlook) Gateway. Click Add
                                             				New . |
| Step 5 | Verify in the
                                          			 database (pebackendgateway table) that the 'localecalendarname' attribute is in
                                          			 whichever language locale you have installed. |
| Step 6 | Ensure the user
                                          			 locale is set after the locale is installed on both the IM and
                                             				Presence Service and  toggling the user locale on the Cisco Unified Communications Manager , if necessary. |