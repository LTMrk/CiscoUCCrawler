---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-15-0-maintain-and-operate-guide-uccx-bee0f5fe7e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_15_0/maintain_and_operate/guide/uccx_b_1501_admin-and-operations-guide/uccx_m_1501_update-unified-cm-ip-address-change-in-unified-ccx.html
retrieved_at: 2026-08-16T21:27:26.246192+00:00
---

Cisco Unified Contact Center Express Administration and Operations Guide, Release 15.0

# Cisco Unified Contact Center Express Administration and Operations Guide, Release 15.0

Updated: April 30, 2025

Chapter: Update Unified CM IP Address Change in Unified CCX

## Chapter: Update Unified CM IP Address Change in Unified CCX

- Update Unified CM IP Address Change in Unified CCX

- Update Unified CM IP Address Change in Unified CCX

# Update Unified CM IP Address Change in Unified CCX

## Update Unified CM IP Address Change in Unified CCX

The following section details the procedure to update any change in Unified CM IP Address in Unified CCX.

Unified CCX supports changing one or more IP addresses of Unified CM servers but does not support changing the Unified CM
                                          cluster.

Run the following CLI commands on the Unified CCX publisher using the new IP address of Unified CM as input.

set uccx provider ip axl - Sets the Unified CCX AXL provider IP address.

set uccx provider ip jtapi - Sets the Unified CCX JTAPI provider IP address.

set uccx provider ip rmcm - Sets the Unified CCX Resource Manager-Contact Manager provider IP address.

After you run the above CLI commands, restart the Unified CCX Engine service on the publisher node. After Unified CCX Engine
                                                      service starts successfully, restart Cisco Tomcat.

| Note | Unified CCX supports changing one or more IP addresses of Unified CM servers but does not support changing the Unified CM
                                          cluster. |
|---|---|

| Run the following CLI commands on the Unified CCX publisher using the new IP address of Unified CM as input. set uccx provider ip axl - Sets the Unified CCX AXL provider IP address. set uccx provider ip jtapi - Sets the Unified CCX JTAPI provider IP address. set uccx provider ip rmcm - Sets the Unified CCX Resource Manager-Contact Manager provider IP address. Note After you run the above CLI commands, restart the Unified CCX Engine service on the publisher node. After Unified CCX Engine
                                                      service starts successfully, restart Cisco Tomcat. | Note | After you run the above CLI commands, restart the Unified CCX Engine service on the publisher node. After Unified CCX Engine
                                                      service starts successfully, restart Cisco Tomcat. |
|---|---|---|
| Note | After you run the above CLI commands, restart the Unified CCX Engine service on the publisher node. After Unified CCX Engine
                                                      service starts successfully, restart Cisco Tomcat. |

| Note | After you run the above CLI commands, restart the Unified CCX Engine service on the publisher node. After Unified CCX Engine
                                                      service starts successfully, restart Cisco Tomcat. |
|---|---|