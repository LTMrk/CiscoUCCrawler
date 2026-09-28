---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-troubleshooting-guide-b-15cuctsg-b-15cuctsg-chapter-01011-html-1249db7491
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/troubleshooting/guide/b_15cuctsg/b_15cuctsg_chapter_01011.html
retrieved_at: 2026-08-17T02:39:01.508023+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 15

# Troubleshooting Guide for Cisco Unity Connection Release 15

Updated: August 22, 2025

Chapter: Troubleshooting Cisco Unity Connection SRSV

## Chapter: Troubleshooting Cisco Unity Connection SRSV

# Troubleshooting Cisco Unity Connection SRSV

Troubleshooting Cisco Unity Connection SRSV

## Error Message Appears When Testing the Connectivity of Unity Connection with Branch

You may receive the following error messages on the Edit Branch page of Cisco Unity Connection Administration when you test
                           the connectivity of Unity Connection with the branch:

“Authentication failed. Incorrect Username and Password”: If you receive the “Authentication failed. Incorrect Username and
                                 Password.” error message on the Edit Branch page when you test the connectivity of the central Unity Connection server with
                                 the branch, make sure that the username and password of the branch entered on the Edit Branch page are correct.

“Branch is unreachable”: If you receive the “Branch is unreachable” error message on the Edit Branch page when you test the
                                 connectivity of the central Unity Connection server with the branch, make sure that the PAT port number specified on the Edit
                                 Branch page is correct.

“Server Address is Invalid”: If you receive the “Server Address is Invalid” error on the Edit Branch page, make sure that
                                 the FQDN/IP address of the branch entered on the Edit Branch page is correct. In case DNS is configured, make sure that the
                                 IP address of the branch is added to it.

## Certificate Mismatch Error Message for Appears on the Central Unity Connection Server

If you are getting the “Unable to start provisioning.” error on the Edit Branch page of Connection Administration page, make
                           sure that the hostname of the branch mentioned in the certificate installed on the central Unity Connection server is correct.

## Unable to login to
                        	 Cisco Unity Connection SRSV Administration

Connection SRSV Administration gets locked if you enter incorrect administrator username and password of the branch three
                           times on the Edit Branch page of Connection Administration. To unlock the Connection SRSV Administration interface, you need
                           to reset the administrator credentials for the branch using the utilsreset_application_ui_administrator_password CLI command.
                           For more information on this command, see “Utils Commands” chapter of the Command Line Interface Reference Guide for Cisco Unified Communications Solutions , available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

## Branch User is Unable to Login through Telephony User Interface (TUI)

If a branch user is unable to login through the TUI, check the following:

Make sure that the PIN entered on the central Unity Connection server is synchronized with the branch through provisioning.

If the branch user is logging in for the first time through the TUI, make sure that the user has set the PIN at the central
                                 Unity Connection server and provisioning is done successfully.

## Status of
                        	 Provisioning Remains In Progress for a Long Time

If the status of provisioning on Connection Administration
                           		remains “In Progress” for a long time, consider the following:

Check the network connectivity of the central Unity Connection
                                 			 server with the branch.

Check whether the central Unity Connection server details are
                                 			 entered correctly on the branch.

Check whether the Unity Connection Branch Sync Service is active on both central Unity Connection server and branch. For more
                                 information on the services required for Connection SRSV, see the “ Managing Cisco Unity Connection Services ” chapter of the Cisco Unified Serviceability Administration Guide, Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/serv_administration/guide/b_15cucservag.html .

Check whether the REST services are active on central Unity
                                 			 Connection server and branch.

## Provisioning from
                        	 the Central Unity Connection Server to Branch Not Working

If the provisioning of the users from the central Unity Connection server to the branch does not work, make sure that the
                           license status at central Unity Connection server is not “Expire”. If the license status at central Unity Connection server
                           is “Expire”, you need to install the required licenses for the central Unity Connection server to make the license status
                           as “Compliance” and start provisioning. For more information on licensing requirements, see the “ Managing Licenses ” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

## Status of Provisioning is Partial Success

If the status of the provisioning on the Branch Sync Results page is “Partial Success”, consider the following:

Make sure that the name of an administrator on the branch is not same as the name of a subscriber on the central Unity Connection
                                 server associated with the branch.

Make sure that the extension of a call handler at the branch is not used as the extension of a branch user at the central
                                 Unity Connection server.

Make sure that the deleted user on the central Unity Connection server is not used on the branch. For example, if a branch
                                 user on Unity Connection is used as operator on Connection SRSV, make sure to change the operator at branch before deleting
                                 the user at central Unity Connection server.

Make sure that the deleted distribution list on the central Unity Connection server is not used on the branch. For example,
                                 if a distribution list is used in a call handler template on the branch, make sure to change the distribution list in the
                                 template before deleting the distribution list.

## Provisioning/Voicemail Upload Remains in Scheduled state for a Long Time

If the provisioning of the users or voicemail upload remains in the Scheduled state for a long time, make sure that the Unity
                           Connection Branch Sync Service is active on the central Unity Connection server.

## Unable to Reach a Branch User through Telephony User Interface (TUI)

If you are not able to reach a branch user through TUI, make sure that the associated partition is added in the Search Space
                           of the central Unity Connection server.

## Unable to Send a Voice Message to a Branch User During WAN Outage

If you are unable to send a voice message to a branch user during WAN outage, make sure that Visual VoiceMail (VVM) is not
                           installed on your phone. For more information, contact your phone service provider.

## Error Messages Appear on the Branch Sync Results Page

If the username and password of the branch is not entered correctly on the Edit Branch page, the provisioning of the users
                           and the voicemail upload does not work and you receive the following error messages or status in the Description field of
                           the Branch Sync Results page of Cisco Unity Connection Administration:

Unable to start Provisioning of the branch:: Message = Authentication failed.

Unable to fetch voice mail summary of the branch:: Message = Authentication failed.

If you receive the “Unable to start provisioning of the branch:: Message=Central Server is not Configured on CUCE” error message
                           on the Branch Sync Results page of Cisco Unity Connection Administration when you start provisioning of the branch, enter
                           the correct FQDN/ IP address of the central Unity Connection server on Cisco Unity Connection SRSV Administration to resolve
                           the problem.

## Logs are Not Created or SRSV feature Not Working Properly

If the logs for the branch are not generated or the SRSV feature is not working properly, you may restart the Unity Connection
                           Branch Sync Service and the REST APIs on both the branch and Unity Connection sites to resolve this issue.

## Unable to Perform Backup/Restore Operation on the Branch

If you are unable to perform the backup/restore operation on the branch, make sure that the backup server is configured correctly
                           on the branch.

## Central Unity
                        	 Connection Server Moves to Violation State

If the central Unity Connection server moves to the Violation state, make sure that the number of licenses for the Unity Connection
                           features, such as SpeechView and Connection SRSV, does not exceed its maximum limit. For more information on licensing, see
                           thesee the “ Managing Licenses ” chapter of the Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Release 15 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/install_upgrade/guide/b_15cuciumg.html .

## Non-Delivery
                        	 Receipts (NDR) on the Central Unity Connection Server

If you are getting NDR on the central Unity Connection server
                           		but the same email is delivered on the branch, check the NDR code and take
                           		action accordingly. For example, if user A sends email to user B from the
                           		branch, the email gets successfully delivered to user B on the branch. However,
                           		on the central Unity Connection server, user A receives “4.2.2” NDR code
                           		stating that the mailbox quota of user B has exceeded its maximum limit. In
                           		this case, user B needs to take appropriate action, such as delete existing
                           		emails or get the mailbax quota increased to receive further emails. For more
                           		information on NDR codes, refer to the Troubleshooting Non-Delivery Receipts chapter of this guide.