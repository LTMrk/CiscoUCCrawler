---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-14-0-cjab-b-deploy-jabber-webex-messenger-14-0-cjab-b-deploy-jabber-w-ece81a73b6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/14_0/cjab_b_deploy-jabber-webex-messenger-14_0/cjab_b_deploy-jabber-webex-messenger-129_chapter_01010.html
retrieved_at: 2026-08-21T19:14:42.676127+00:00
---

Webex Messenger Deployment for Cisco Jabber 14.0

# Webex Messenger Deployment for Cisco Jabber 14.0

Updated: April 1, 2024

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

| Step 1 | Open a command prompt. |
|---|---|
| Step 2 | Enter nslookup . The default DNS server and address is displayed. Confirm
                                          			 that this is the expected DNS server. |
| Step 3 | Enter set type=SRV . |
| Step 4 | Enter the name for each of your SRV records. For example _collab-edge. exampledomain Displays server and address—SRV record is accessible. Displays _collab-edge. exampledomain : Non-existent
                                                      						domain —There is an issue with your SRV record. |