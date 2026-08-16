---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-08600fb956
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_0110000.html
retrieved_at: 2026-08-16T17:32:52.590228+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure Application Servers

## Chapter: Configure Application Servers

# Configure Application Servers

## Application Servers Overview

Use the application server function to maintain associations between the Cisco Unified Communications Manager and off-cluster,
                           external applications, such as Cisco Unity Connection and Cisco Emergency Responder. Application servers also synchronize
                           information between Cisco Unified Communications Manager and applications such as Cisco WebDialer.

## Application Servers Prerequisites

For Cisco Unity and Cisco Unity Connection, make sure that the AXL web service is running on the Cisco Unified Communications
                              Manager node that is configured to communicate with the Cisco Unity and Cisco Unity Connection server.

## Application Servers Task Flow

Perform either of the following tasks, depending on the type of application server that you want to configure.

Step 1

Configure Application Servers

Configure application servers that you want to securely join, interoperate, and share information within your cluster.

Step 2

Configure Cisco WebDialer Servers

Configure Cisco WebDialer application servers as an alternative to the List of WebDialers service parameter, which limits the number of characters that you can enter. After you add a Cisco WebDialer application
                                          server in the Application Server Configuration window, the server appears in the List of WebDialers field in the Service Parameter Configuration window for the Cisco WebDialer Web Service. For complete details about configuring Cisco WebDialer, see the Feature Configuration Guide for Cisco Unified Communications Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html .

### Configure Application Servers

Configure application servers that you want to securely join, interoperate, and share information within your cluster.

Step 1

From Cisco Unified CM Administration, choose System > Application Server .

Step 2

Click Add New .

Step 3

From the Application Server Type drop-down list, choose one of the following server options:

- Cisco Unity Voice Mail 4.x or later

- Cisco Unity Connection

- CUMA Provisioning Server

- CER Location Management

- Remote System Log Server

Step 4

Click Next .

Step 5

Configure the fields on the Application Server Configuration window. See the online help for more information about the fields and their configuration options.

Step 6

Click Save .

### Configure Cisco WebDialer Servers

Configure Cisco WebDialer application servers as an alternative to the List of WebDialers service parameter, which limits the number of characters that you can enter. After you add a Cisco WebDialer application
                                 server in the Application Server Configuration window, the server appears in the List of WebDialers field in the Service Parameter Configuration window for the Cisco WebDialer Web Service. For complete details about configuring Cisco WebDialer, see the Feature Configuration Guide for Cisco Unified Communications Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html .

Step 1

From Cisco Unified CM Administration, choose System > Application Server .

Step 2

Click Add New .

Step 3

From the Application Server Type drop-down list, choose Cisco Web Dialer , and then click Next .

Step 4

In the Hostname or IP Address field, enter the hostname or IP address of the WebDialer server.

Step 5

From the Redirector Node drop-down list, choose < None > or a specific Unified Communications Manager node.

< None > indicates the WebDialer Server would apply to all nodes.

Step 6

Click Save .

Step 7

From Cisco Unified Serviceability, choose Tools > Control Center - Feature Services

Step 8

Click the Cisco WebDialer Web Service radio button.

Step 9

Click Restart .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Application Servers | Configure application servers that you want to securely join, interoperate, and share information within your cluster. |
| Step 2 | Configure Cisco WebDialer Servers | Configure Cisco WebDialer application servers as an alternative to the List of WebDialers service parameter, which limits the number of characters that you can enter. After you add a Cisco WebDialer application
                                          server in the Application Server Configuration window, the server appears in the List of WebDialers field in the Service Parameter Configuration window for the Cisco WebDialer Web Service. For complete details about configuring Cisco WebDialer, see the Feature Configuration Guide for Cisco Unified Communications Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html . |

| Step 1 | From Cisco Unified CM Administration, choose System > Application Server . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | From the Application Server Type drop-down list, choose one of the following server options: Cisco Unity Voice Mail 4.x or later Cisco Unity Connection CUMA Provisioning Server CER Location Management Remote System Log Server |
| Step 4 | Click Next . |
| Step 5 | Configure the fields on the Application Server Configuration window. See the online help for more information about the fields and their configuration options. |
| Step 6 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Application Server . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | From the Application Server Type drop-down list, choose Cisco Web Dialer , and then click Next . |
| Step 4 | In the Hostname or IP Address field, enter the hostname or IP address of the WebDialer server. |
| Step 5 | From the Redirector Node drop-down list, choose < None > or a specific Unified Communications Manager node. < None > indicates the WebDialer Server would apply to all nodes. |
| Step 6 | Click Save . |
| Step 7 | From Cisco Unified Serviceability, choose Tools > Control Center - Feature Services |
| Step 8 | Click the Cisco WebDialer Web Service radio button. |
| Step 9 | Click Restart . |