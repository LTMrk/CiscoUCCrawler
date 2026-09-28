---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-12-5-1-su8-english-administration-guide-cer0-b-cisco-emergency-responder-0cd9a912f9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/12_5_1_su8/english/administration/guide/cer0_b_cisco-emergency-responder-administration-guide-1251su8/cer0_b_cisco-emergency-responder-administration-guide-1251su3_chapter_01011.html
retrieved_at: 2026-08-21T15:30:10.039398+00:00
---

Cisco Emergency Responder Administration Guide, Release 12.5(1)SU8b-SU9

# Cisco Emergency Responder Administration Guide, Release 12.5(1)SU8b-SU9

Updated: July 23, 2024

Chapter: Cisco Emergency Responder Admin Utility

## Chapter: Cisco Emergency Responder Admin Utility

# Cisco Emergency Responder Admin Utility

## Cisco Emergency
                        	 Responder Admin Utility Overview

In CiscoEmergencyResponder (Emergency Responder), the Admin Utility is
                           		integrated into the Emergency Responder itself. The Admin Utility has its own
                           		web interface that you can access from the main Emergency Responder web page.
                           		As with the other Emergency Responder administration web interfaces, the Admin
                           		Utility web interface is password protected.

## Change Cisco Unified
                        	 Communications Manager Version

When the Unified Communications Manager cluster is upgraded, the AXL queueID will change on the  publisher node. To re-establish
                                          AXL connection after the Unified Communications Manager cluster upgrade, the Emergency Responder administrator must restart
                                          the CER Service. Failing to do so may result in the breaking of AXL change notifications between Unified Communications Manager
                                          and Emergency Responder.

Step 1

Log in to the
                                       			 Emergency Responder Admin Utility web interface.

Step 2

From the main
                                       			 Emergency ResponderAdmin Utility page, select Update > CCM Version .

Step 3

Select the new
                                       			 version of Unified CM from the Choose the CCM Version to Upgrade pull-down
                                       			 menu and click Go .

You must change the Unified Communications Manager version separately for the Publisher and Subscriber nodes.

The Status area
                                          				of the Upgrade CCM Version page displays the new version number after the system
                                          				makes the change.

## Update Emergency
                        	 Responder Cluster Database Host Details

By default,
                              		  each server in a cluster considers its own database to be the cluster database
                              		  host. Because each cluster should have only one database host, you must update
                              		  the cluster configuration accordingly.

For
                              		  example, if you have two server groups (ServergroupA and ServergroupB), each
                              		  containing a Publisher and a Subscriber, you would do the following to update
                              		  the cluster database host details:

Update the
                                    				cluster database host password for ServergroupA using ServergroupA's own host
                                    				name.

Update the
                                    				cluster database host password for ServergroupB by entering the IP address and
                                    				cluster database password for ServergroupA.

Repeat Step2
                                    				for other server groups in the cluster.

If you use
                                          			 hostnames, then the hostname must be resolvable using DNS. If DNS is not
                                          			 configured or DNS is unavailable for any reason, hostname resolution fails and
                                          			 cluster functionality is impaired. It is recommended that the DNS configuration
                                          			 include redundant entries to prevent unavailability. Alternatively, the IP
                                          			 address of the cluster database host can be configured on this screen. The
                                          			 hostname can begin with a numeric value.

This procedure
                                          			 only updates the Emergency Responder Cluster DB host details for this server
                                          			 group. Other servers in this Emergency Responder cluster do not updated
                                          			 automatically.

### Before you begin

You must reboot the
                              		  server to update Emergency Responder Cluster DB host details. Only restarting
                              		  Emergency Responder services does not work because the IP address is cached by
                              		  other services.

Step 1

Log in to the Emergency
                                          				Responder Admin Utility web interface.

Step 2

Select Update
                                          				> Cluster DBHost from the main Emergency
                                          				ResponderAdmin Utility page.

Step 3

Enter the new
                                       			 Cluster DBHost name (if DNS is configured) or IP address in the text box. If
                                       			 the cluster is spread across domains, enter a fully qualified host name.

Step 4

Enter the
                                       			 password for the new Cluster DBHost in the Password text box.

Step 5

Reenter the
                                       			 password for the new Cluster DBHost in the Confirm
                                          				Password text box.

Step 6

Click Go .

| Note | When the Unified Communications Manager cluster is upgraded, the AXL queueID will change on the  publisher node. To re-establish
                                          AXL connection after the Unified Communications Manager cluster upgrade, the Emergency Responder administrator must restart
                                          the CER Service. Failing to do so may result in the breaking of AXL change notifications between Unified Communications Manager
                                          and Emergency Responder. |
|---|---|

| Step 1 | Log in to the
                                       			 Emergency Responder Admin Utility web interface. |
|---|---|
| Step 2 | From the main
                                       			 Emergency ResponderAdmin Utility page, select Update > CCM Version . The Upgrade CCM Version page appears. |
| Step 3 | Select the new
                                       			 version of Unified CM from the Choose the CCM Version to Upgrade pull-down
                                       			 menu and click Go . Note You must change the Unified Communications Manager version separately for the Publisher and Subscriber nodes. The Status area
                                          				of the Upgrade CCM Version page displays the new version number after the system
                                          				makes the change. | Note | You must change the Unified Communications Manager version separately for the Publisher and Subscriber nodes. |
| Note | You must change the Unified Communications Manager version separately for the Publisher and Subscriber nodes. |

| Note | You must change the Unified Communications Manager version separately for the Publisher and Subscriber nodes. |
|---|---|

| Note | If you use
                                          			 hostnames, then the hostname must be resolvable using DNS. If DNS is not
                                          			 configured or DNS is unavailable for any reason, hostname resolution fails and
                                          			 cluster functionality is impaired. It is recommended that the DNS configuration
                                          			 include redundant entries to prevent unavailability. Alternatively, the IP
                                          			 address of the cluster database host can be configured on this screen. The
                                          			 hostname can begin with a numeric value. |
|---|---|

| Note | This procedure
                                          			 only updates the Emergency Responder Cluster DB host details for this server
                                          			 group. Other servers in this Emergency Responder cluster do not updated
                                          			 automatically. |
|---|---|

| Step 1 | Log in to the Emergency
                                          				Responder Admin Utility web interface. |
|---|---|
| Step 2 | Select Update
                                          				> Cluster DBHost from the main Emergency
                                          				ResponderAdmin Utility page. The Update
                                          				Cluster DB Host page appears. |
| Step 3 | Enter the new
                                       			 Cluster DBHost name (if DNS is configured) or IP address in the text box. If
                                       			 the cluster is spread across domains, enter a fully qualified host name. |
| Step 4 | Enter the
                                       			 password for the new Cluster DBHost in the Password text box. |
| Step 5 | Reenter the
                                       			 password for the new Cluster DBHost in the Confirm
                                          				Password text box. |
| Step 6 | Click Go . |