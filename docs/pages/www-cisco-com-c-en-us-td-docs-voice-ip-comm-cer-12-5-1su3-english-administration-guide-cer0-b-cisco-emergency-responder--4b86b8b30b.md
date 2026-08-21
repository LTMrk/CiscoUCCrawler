---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-12-5-1su3-english-administration-guide-cer0-b-cisco-emergency-responder--4b86b8b30b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/12_5_1su3/english/administration/guide/cer0_b_cisco-emergency-responder-administration-guide-1251su3/cer0_b_cisco-emergency-responder-administration-guide-1251su3_appendix_010100.html
retrieved_at: 2026-08-21T15:45:40.333103+00:00
---

Cisco Emergency Responder Administration Guide for Release 12.5(1)SU3

# Cisco Emergency Responder Administration Guide for Release 12.5(1)SU3

Updated: November 23, 2021

Chapter: Admin Utility Web Interface for Cisco Emergency Responder

## Chapter: Admin Utility Web Interface for Cisco Emergency Responder

- Admin Utility Web Interface for Cisco Emergency Responder

- Update Cisco Unified                              	 Communications Manager Version

- Update Cluster DB                              	 Host

# Admin Utility Web Interface for Cisco Emergency Responder

## Update Cisco Unified
                        	 Communications Manager Version

The Upgrade
                              		  CUCM Version page appears when you choose Update > CUCM
                                 			 Version .

### Authorization
                              		  Requirements

You must
                              		  have system administrator authority to access this page.

### Description

Use the
                              		  Upgrade CUCM Version page to select a different version of
                              		  CiscoUnifiedCommunicationsManager.

The
                              		  following table describes the Upgrade CUCM Version page.

Field

Description

Displays the current CiscoUnifiedCommunicationsManager
                                          					 version.

Choose the CiscoUnifiedCommunicationsManager version to
                                          					 upgrade

Use
                                          					 the pull down menu to select a version of CiscoUnifiedCommunicationsManager.

Go
                                          					 button

Click Go to
                                          					 begin the update process.

Change the
                                                      						CUCM version separately on the Publisher and Subscriber nodes.

Cancel button

Cancels the CiscoUnifiedCommunicationsManager update.

## Update Cluster DB
                        	 Host

The Update
                              		  Cluster DB Host page appears when you choose Update >
                                 			 Cluster DB Host .

### Authorization
                              		  Requirements

You must
                              		  have system administrator authority to access this page.

### Description

Use the
                              		  Update Cluster DB Host page to designate a new server as the Emergency
                              		  Responder cluster database host server.

The
                              		  following table describes the Update Cluster DB Host page.

Field

Description

Displays the name of the current cluster database host

ClusterDB Hostname/IP Address

Enter the hostname (if DNS is configured) or the IP address of
                                          					 the new cluster database host.

If the
                                                      						cluster is spread across domains, then enter a fully qualified hostname.

Password

Enter the password for the new cluster database host

Confirm Password

Reenter the password for the new cluster database host.

Go
                                          					 button

Click the Go button to designate the new server as the new cluster database host.

The
                                                      						Emergency Responder Cluster DB host details are updated. Emergency Responder
                                                      						services must be restarted for this change to take effect. You must restart
                                                      						Emergency Responder Services by rebooting the Emergency Responder publisher and
                                                      						subscriber servers. Only restarting Emergency Responder services does not work
                                                      						because the IP address is cached by other services and this updates the
                                                      						Emergency Responder Cluster DB host details for this server group only. Other
                                                      						servers in this Emergency Responder cluster are NOT updated automatically. For
                                                      						further details, see Update Emergency Responder Cluster Database Host Details .

Cancel button

Cancels the Update Cluster DB Host operation.

| Field | Description |
|---|---|
| Status | Displays the current CiscoUnifiedCommunicationsManager
                                          					 version. |
| CUCM Version Details |  |
| Choose the CiscoUnifiedCommunicationsManager version to
                                          					 upgrade | Use
                                          					 the pull down menu to select a version of CiscoUnifiedCommunicationsManager. |
| Go
                                          					 button | Click Go to
                                          					 begin the update process. Note Change the
                                                      						CUCM version separately on the Publisher and Subscriber nodes. | Note | Change the
                                                      						CUCM version separately on the Publisher and Subscriber nodes. |
| Note | Change the
                                                      						CUCM version separately on the Publisher and Subscriber nodes. |
| Cancel button | Cancels the CiscoUnifiedCommunicationsManager update. |

| Note | Change the
                                                      						CUCM version separately on the Publisher and Subscriber nodes. |
|---|---|

| Field | Description |
|---|---|
| Status | Displays the name of the current cluster database host |
| Cluster DB Host Details |  |
| ClusterDB Hostname/IP Address | Enter the hostname (if DNS is configured) or the IP address of
                                          					 the new cluster database host. Note If the
                                                      						cluster is spread across domains, then enter a fully qualified hostname. | Note | If the
                                                      						cluster is spread across domains, then enter a fully qualified hostname. |
| Note | If the
                                                      						cluster is spread across domains, then enter a fully qualified hostname. |
| Password | Enter the password for the new cluster database host |
| Confirm Password | Reenter the password for the new cluster database host. |
| Go
                                          					 button | Click the Go button to designate the new server as the new cluster database host. Note The
                                                      						Emergency Responder Cluster DB host details are updated. Emergency Responder
                                                      						services must be restarted for this change to take effect. You must restart
                                                      						Emergency Responder Services by rebooting the Emergency Responder publisher and
                                                      						subscriber servers. Only restarting Emergency Responder services does not work
                                                      						because the IP address is cached by other services and this updates the
                                                      						Emergency Responder Cluster DB host details for this server group only. Other
                                                      						servers in this Emergency Responder cluster are NOT updated automatically. For
                                                      						further details, see Update Emergency Responder Cluster Database Host Details . | Note | The
                                                      						Emergency Responder Cluster DB host details are updated. Emergency Responder
                                                      						services must be restarted for this change to take effect. You must restart
                                                      						Emergency Responder Services by rebooting the Emergency Responder publisher and
                                                      						subscriber servers. Only restarting Emergency Responder services does not work
                                                      						because the IP address is cached by other services and this updates the
                                                      						Emergency Responder Cluster DB host details for this server group only. Other
                                                      						servers in this Emergency Responder cluster are NOT updated automatically. For
                                                      						further details, see Update Emergency Responder Cluster Database Host Details . |
| Note | The
                                                      						Emergency Responder Cluster DB host details are updated. Emergency Responder
                                                      						services must be restarted for this change to take effect. You must restart
                                                      						Emergency Responder Services by rebooting the Emergency Responder publisher and
                                                      						subscriber servers. Only restarting Emergency Responder services does not work
                                                      						because the IP address is cached by other services and this updates the
                                                      						Emergency Responder Cluster DB host details for this server group only. Other
                                                      						servers in this Emergency Responder cluster are NOT updated automatically. For
                                                      						further details, see Update Emergency Responder Cluster Database Host Details . |
| Cancel button | Cancels the Update Cluster DB Host operation. |

| Note | If the
                                                      						cluster is spread across domains, then enter a fully qualified hostname. |
|---|---|

| Note | The
                                                      						Emergency Responder Cluster DB host details are updated. Emergency Responder
                                                      						services must be restarted for this change to take effect. You must restart
                                                      						Emergency Responder Services by rebooting the Emergency Responder publisher and
                                                      						subscriber servers. Only restarting Emergency Responder services does not work
                                                      						because the IP address is cached by other services and this updates the
                                                      						Emergency Responder Cluster DB host details for this server group only. Other
                                                      						servers in this Emergency Responder cluster are NOT updated automatically. For
                                                      						further details, see Update Emergency Responder Cluster Database Host Details . |
|---|---|