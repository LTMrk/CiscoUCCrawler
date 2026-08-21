---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-security-12-5-1su4-cucm-b-security-guide-1251su4-cucm-m-contact-search--5fd455e7eb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/security/12_5_1SU4/cucm_b_security-guide-1251su4/cucm_m_contact-search-authentication.html
retrieved_at: 2026-08-21T18:06:44.551633+00:00
---

Security Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

# Security Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

Updated: March 22, 2024

Chapter: Contact Search Authentication

## Chapter: Contact Search Authentication

# Contact Search Authentication

## Contact Search Authentication Overview

Contact Search Authentication provides additional security for your system by ensuring that users whom access the company
                              directory must authenticate themselves. This feature secures the directory from being accessed by external parties.

## Contact Search Authentication Task Flow

Complete the following tasks to set up Contact Search Authentication in Unified Communications Manager. When this feature
                              is configured, users must authenticate themselves before searching the directory for other users.

Step 1

Confirm Phone Support for Contact Search Authentication

Confirm that your phones support this feature. Run the Unified CM Phone Feature List report in Cisco Unified Reporting to get a list of phone models that support the feature.

Step 2

Enable Contact Search Authentication

Configure Unified Communications Manager for Contact Search Authentication.

Step 3

Configure Secure Directory Server for Contact Search

Use this procedure to configure Unified Communications Manager with the URL to which phone users are directed when they search
                                          the directory for other users.

### Confirm Phone Support for Contact Search Authentication

Confirm that the phones in your deployment  support contact search authentication. Run a Phone Feature List report to obtain
                                 a full list of phone models that support the feature.

Step 1

From Cisco Unified Reporting, click System Reports .

Step 2

Select Unified CM Phone Feature .

Step 3

Click the Unified CM Phone Feature report.

Step 4

Leave the Product field at the default value.

Step 5

From the Feature drop-down, choose Authenticated Contact Search .

Step 6

Click Submit .

### Enable Contact Search Authentication

Use this procedure on Unified Communications Manager to configure contact search authentication for phone users.

Step 1

Log in to the Command Line Interface.

Step 2

Run the utils contactsearchauthentication status command to confirm the contact search authentication setting on this node.

Step 3

If you need to configure contact search authentication:

- To enable authentication, run the utils contactsearchauthentication enable command.

- To disable authentication, run the utils contactsearchauthentication disable command.

Step 4

Repeat this procedure on all Unified Communications Manager cluster nodes.

### Configure Secure Directory Server for Contact Search

Use this procedure to configure Unified Communications Manager with the directory server URL to which UDS sends user search requests. The default value is https://<cucm-fqdn-or-ip>:port/cucm-uds/users .

Step 1

From Cisco Unified Communications Manager Administration , choose System > Enterprise Parameters .

Step 2

In the Secure Contact Search URL text box, enter the URL for secure UDS directory requests.

Step 3

Click Save .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Confirm Phone Support for Contact Search Authentication | Confirm that your phones support this feature. Run the Unified CM Phone Feature List report in Cisco Unified Reporting to get a list of phone models that support the feature. |
| Step 2 | Enable Contact Search Authentication | Configure Unified Communications Manager for Contact Search Authentication. |
| Step 3 | Configure Secure Directory Server for Contact Search | Use this procedure to configure Unified Communications Manager with the URL to which phone users are directed when they search
                                          the directory for other users. |

| Step 1 | From Cisco Unified Reporting, click System Reports . |
|---|---|
| Step 2 | Select Unified CM Phone Feature . |
| Step 3 | Click the Unified CM Phone Feature report. |
| Step 4 | Leave the Product field at the default value. |
| Step 5 | From the Feature drop-down, choose Authenticated Contact Search . |
| Step 6 | Click Submit . |

| Step 1 | Log in to the Command Line Interface. |
|---|---|
| Step 2 | Run the utils contactsearchauthentication status command to confirm the contact search authentication setting on this node. |
| Step 3 | If you need to configure contact search authentication: To enable authentication, run the utils contactsearchauthentication enable command. To disable authentication, run the utils contactsearchauthentication disable command. |
| Step 4 | Repeat this procedure on all Unified Communications Manager cluster nodes. Note You must reset phones in order for the changes to take effect. | Note | You must reset phones in order for the changes to take effect. |
| Note | You must reset phones in order for the changes to take effect. |

| Note | You must reset phones in order for the changes to take effect. |
|---|---|

| Note | The default UDS port is 8443. When contact search authentication becomes enabled, the default UDS port switches to 9443. If
                                          you then disable contact search authentication, you must change the UDS port back to 8443 manually. |
|---|---|

| Step 1 | From Cisco Unified Communications Manager Administration , choose System > Enterprise Parameters . |
|---|---|
| Step 2 | In the Secure Contact Search URL text box, enter the URL for secure UDS directory requests. Note We recommend that for the URL, you choose a node that is not running the Cisco TFTP service. The CiscoTFTP and UDS services
                                                      may disrupt each other if either service gets restarted. | Note | We recommend that for the URL, you choose a node that is not running the Cisco TFTP service. The CiscoTFTP and UDS services
                                                      may disrupt each other if either service gets restarted. |
| Note | We recommend that for the URL, you choose a node that is not running the Cisco TFTP service. The CiscoTFTP and UDS services
                                                      may disrupt each other if either service gets restarted. |
| Step 3 | Click Save . |

| Note | We recommend that for the URL, you choose a node that is not running the Cisco TFTP service. The CiscoTFTP and UDS services
                                                      may disrupt each other if either service gets restarted. |
|---|---|