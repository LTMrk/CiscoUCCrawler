---
doc_id: developer-cisco-com-docs-finesse-connect-to-xmpp-over-tcp-4cea49ba76
source_url: https://developer.cisco.com/docs/finesse/connect-to-xmpp-over-tcp/
retrieved_at: 2026-09-07T14:07:41.620397+00:00
---

# Connect to XMPP
	 over TCP

Any third party
		  XMPP client can connect to the Finesse Notification Service through TCP sockets
		  for sending and receiving notifications. You can connect to ports 5222
		  (non-secure connection) and 5223 (secure connection).

Cisco Finesse, Release 12.5(1) onward, the 5222 port (non-secure connection) is disabled by default. Set the utils finesse set_property webservices enableInsecureOpenfirePort to true to enable this port.

For more information, see Service Properties section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

Connect to Secure Port 5223 over SSL/TLS

Third party clients need to add the Finesse Notification certificate to their respective trust stores. Finesse Notification Service shares the same certificate with Cisco Finesse Tomcat. To download the certificate:

Sign in to the Cisco Unified Operating System Administration through the URL (https://FQDN:8443/cmplatform, where FQDN is the fully qualified domain name of the primary Finesse server and 8443 is the port number).

Click Security > Certificate Management .

Click Find to get the list of all the certificates.

In the Certificate List screen, choose Certificate from the Find Certificate List where drop-down menu, enter tomcat in the begins with option and click Find .

Click the FQDN link which appears in the Common Name column parallel to the listed tomcat certificate.

In the pop-up that appears, click the option Download .PEM File to save the file on your desktop.

| Note | Cisco Finesse, Release 12.5(1) onward, the 5222 port (non-secure connection) is disabled by default. Set the utils finesse set_property webservices enableInsecureOpenfirePort to true to enable this port. For more information, see Service Properties section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html . |
|---|---|