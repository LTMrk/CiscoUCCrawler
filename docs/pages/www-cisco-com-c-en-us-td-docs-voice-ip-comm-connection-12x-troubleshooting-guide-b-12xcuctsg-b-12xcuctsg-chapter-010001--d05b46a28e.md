---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-troubleshooting-guide-b-12xcuctsg-b-12xcuctsg-chapter-010001--d05b46a28e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/troubleshooting/guide/b_12xcuctsg/b_12xcuctsg_chapter_010001.html
retrieved_at: 2026-08-17T02:29:31.383350+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 12.x

# Troubleshooting Guide for Cisco Unity Connection Release 12.x

Updated: August 17, 2017

Chapter: Troubleshooting Comet Notifications over SSL

## Chapter: Troubleshooting Comet Notifications over SSL

- Troubleshooting Comet Notifications over SSL

- Unable to Send                              	 Comet Notification over SSL

# Troubleshooting Comet Notifications over SSL

Troubleshooting Comet Notifications over SSL

## Unable to Send
                        	 Comet Notification over SSL

Make sure of the following if Unity Connection is unable to send
                           		comet notifications over SSL:

User workstations are establishing connection on 7443 port.

Firewall is not blocking the traffic on 7443 port.

The show cuc jetty ssl status command is executed on both the
                                 			 primary and secondary nodes and the SSL mode is enabled.

Connection Jetty service is restarted on both the primary and
                                 			 secondary servers.

For more information, see:

The “ Service Ports ” section
                                 			 of the “IP Communications Required by Cisco Unity Connection” in the Security
                                 			 Guide for Cisco Unity Connection, Release 12.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/security/b_12xcucsecx.html

The Command Line Interface Guide for Cisco Unified
                                 			 Communications Solutions, Release 12.0(1), available at https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-maintenance-guides-list.html .