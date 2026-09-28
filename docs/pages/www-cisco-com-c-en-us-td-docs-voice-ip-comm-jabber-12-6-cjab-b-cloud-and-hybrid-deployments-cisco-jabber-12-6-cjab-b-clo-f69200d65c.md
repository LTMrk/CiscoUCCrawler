---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-6-cjab-b-cloud-and-hybrid-deployments-cisco-jabber-12-6-cjab-b-clo-f69200d65c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_6/cjab_b_cloud-and-hybrid-deployments-cisco-jabber-12-6/cjab_b_cloud-and-hybrid-deployments-cisco-jabber-12-6_chapter_01010.html
retrieved_at: 2026-08-21T19:09:31.847394+00:00
---

Cloud and Hybrid Deployments for Cisco Jabber 12.6

# Cloud and Hybrid Deployments for Cisco Jabber 12.6

Updated: April 2, 2024

Chapter: Configure Service Discovery for Remote Access

## Chapter: Configure Service Discovery for Remote Access

# Configure Service Discovery for Remote Access

## Service Discovery
                        	 Requirements

Service discovery enables clients to automatically detect and locate services on your enterprise network. Expressway for Mobile
                              and Remote Access allows you to access the services on your enterprise network. You should meet the following requirements
                              to enable the clients to connect through Expressway for Mobile and Remote Access and discover services:

DNS requirements

Certificate requirements

Test external SRV _collab-edge .

### DNS
                           	 Requirements

The DNS requirements for service discovery through remote access are:

Configure a _collab-edge DNS SRV record on an external DNS server.

Configure a _cisco-uds DNS SRV record on the internal name server.

Optionally, for a hybrid cloud-based deployment with different domains for the IM and Presence server and the voice server,
                                       configure the Voice Services Domain to locate the DNS server with the _collab-edge record.

Jabber attempts connections to a maximum of three SSO-enabled servers, which are chosen randomly from all SSO-enabled servers
                                             that the DNS SRV records ( _collab-edge and _cisco-uds ) identify. If Jabber fails to connect three times, it considers Edge SSO unsupported.

### Certificate
                           	 Requirements

Before you
                                 		  configure remote access, download the Cisco VCS Expressway and Cisco
                                 		  Expressway-E Server certificate. The Server certificate is used for both HTTP
                                 		  and XMPP.

For more
                                 		  information on configuring Cisco VCS Expressway certificate, see Configuring Certificates on
                                    			 Cisco VCS Expressway .

### Test _collab-edge SRV Record

Step 1

Open a command prompt.

Step 2

Enter nslookup .

Step 3

Enter set type=SRV .

Step 4

Enter the name for each of your SRV records.

For example _collab-edge. exampledomain

Displays server and address—SRV record is accessible.

Displays _collab-edge. exampledomain : Non-existent
                                                      						domain —There is an issue with your SRV record.

| Note | Jabber attempts connections to a maximum of three SSO-enabled servers, which are chosen randomly from all SSO-enabled servers
                                             that the DNS SRV records ( _collab-edge and _cisco-uds ) identify. If Jabber fails to connect three times, it considers Edge SSO unsupported. |
|---|---|

| Step 1 | Open a command prompt. |
|---|---|
| Step 2 | Enter nslookup . The default DNS server and address is displayed. Confirm
                                          			 that this is the expected DNS server. |
| Step 3 | Enter set type=SRV . |
| Step 4 | Enter the name for each of your SRV records. For example _collab-edge. exampledomain Displays server and address—SRV record is accessible. Displays _collab-edge. exampledomain : Non-existent
                                                      						domain —There is an issue with your SRV record. |